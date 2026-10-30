// 단어 요새 — 서버 핵심 로직 (저장소 독립적)
// 서버(Netlify Blobs)와 브라우저(localStorage 오프라인 모드)가 같은 코드를 씁니다.
// store: { get(key) -> object|null, set(key, value) }
// hash:  async (pw, salt) -> hex string
// builtins: [{ id, title, desc, pairs:[{w,m}] }]

export async function handle({ store, hash, builtins, route, method, query, body, randomId, now }) {
  const ok = (data) => ({ status: 200, data });
  const fail = (status, error) => ({ status, data: { error } });
  const T = typeof now === "function" ? now() : Date.now();

  const clean = (s, max) => String(s ?? "").replace(/[\u0000-\u001f\u007f<>]/g, "").trim().replace(/\s+/g, " ").slice(0, max);
  const lower = (s) => String(s).toLowerCase();
  const hexOf = (s) => Array.from(new TextEncoder().encode(lower(s))).map((b) => b.toString(16).padStart(2, "0")).join("");
  const int = (v, lo, hi) => { const n = Math.round(Number(v)); return Number.isFinite(n) ? Math.min(hi, Math.max(lo, n)) : lo; };

  const BUILTIN = new Map(builtins.map((b) => [b.id, b]));
  const builtinMeta = (b, plays) => ({ id: b.id, no: b.no, title: b.title, desc: b.desc || "", owner: "단어 요새", count: b.pairs.length, public: true, builtin: true, plays: plays[b.id] || 0, updated: 0 });

  async function loadIndex() { return (await store.get("index/books")) || []; }
  async function loadPlays() { return (await store.get("stats/plays")) || {}; }

  // ---- auth ----
  async function auth(requireExisting) {
    const nick = clean(body?.nick, 12);
    const pw = body?.pw;
    if (!nick) return { err: fail(400, "닉네임을 입력해 주세요.") };
    if (typeof pw !== "string" || pw.length < 2 || pw.length > 64) return { err: fail(400, "비밀번호는 2~64자로 입력해 주세요.") };
    const key = "users/" + hexOf(nick);
    let user = await store.get(key);
    if (user) {
      const h = await hash(pw, user.salt);
      if (h !== user.hash) return { err: fail(401, "이미 등록된 닉네임이에요. 비밀번호가 맞지 않아요.") };
      return { user, key, nick: user.name };
    }
    if (requireExisting) return { err: fail(401, "로그인이 필요해요.") };
    const salt = randomId(16);
    user = { name: nick, salt, hash: await hash(pw, salt), created: T };
    await store.set(key, user);
    return { user, key, nick, created: true };
  }
  const isOwner = (meta, nick) => meta && lower(meta.owner) === lower(nick);

  // ---- routes ----
  if (route === "login" && method === "POST") {
    const a = await auth(false); if (a.err) return a.err;
    return ok({ ok: true, nick: a.nick, created: !!a.created });
  }

  if (route === "books" && method === "GET") {
    const q = lower(clean(query?.q, 40));
    const plays = await loadPlays();
    const idx = await loadIndex();
    let list = [...builtins.map((b) => builtinMeta(b, plays)), ...idx.filter((b) => b.public).map((b) => ({ ...b, plays: plays[b.id] || 0 }))];
    if (q) {
      const num = q.match(/^(?:#|no\.?\s*)?(\d+)$/);
      list = num ? list.filter((b) => b.no === Number(num[1]))
                 : list.filter((b) => lower(b.title + " " + b.owner + " " + (b.desc || "")).includes(q));
    }
    list.sort((a, b) => (b.builtin - a.builtin) || (b.plays - a.plays) || (b.updated - a.updated));
    return ok({ books: list.slice(0, 200) });
  }

  if (route === "mybooks" && method === "POST") {
    const a = await auth(true); if (a.err) return a.err;
    const plays = await loadPlays();
    const list = (await loadIndex()).filter((b) => isOwner(b, a.nick)).map((b) => ({ ...b, plays: plays[b.id] || 0 })).sort((x, y) => y.updated - x.updated);
    return ok({ books: list });
  }

  if (route === "book" && method === "POST") {
    const id = clean(body?.id, 40);
    const plays = await loadPlays();
    if (BUILTIN.has(id)) { const b = BUILTIN.get(id); return ok({ book: { ...builtinMeta(b, plays), pairs: b.pairs } }); }
    const book = await store.get("books/" + id);
    if (!book) return fail(404, "단어장을 찾을 수 없어요.");
    if (!book.public) {
      const a = await auth(true); if (a.err) return fail(404, "단어장을 찾을 수 없어요.");
      if (!isOwner(book, a.nick)) return fail(404, "단어장을 찾을 수 없어요.");
    }
    return ok({ book: { ...book, plays: plays[book.id] || 0 } });
  }

  if (route === "book/save" && method === "POST") {
    const a = await auth(true); if (a.err) return a.err;
    const title = clean(body?.title, 40);
    if (!title) return fail(400, "단어장 이름을 입력해 주세요.");
    const desc = clean(body?.desc, 120);
    const raw = Array.isArray(body?.pairs) ? body.pairs : [];
    const seen = new Set(); const pairs = [];
    for (const p of raw) {
      const w = clean(p?.w, 60), m = clean(p?.m, 100);
      if (!w || !m) continue;
      const k = lower(w) + "\u0000" + m; if (seen.has(k)) continue; seen.add(k);
      pairs.push({ w, m }); if (pairs.length >= 3000) break;
    }
    if (pairs.length < 3) return fail(400, "단어가 3쌍 이상 필요해요.");
    const pub = !!body?.public;
    let idx = await loadIndex();
    let id = clean(body?.id, 40);
    let book = id ? await store.get("books/" + id) : null;
    if (book && !isOwner(book, a.nick)) return fail(403, "내 단어장만 고칠 수 있어요.");
    if (!book) {
      if (idx.filter((b) => isOwner(b, a.nick)).length >= 50) return fail(400, "단어장은 한 사람당 50개까지 만들 수 있어요.");
      const seq = ((await store.get("stats/seq")) || { n: 1000 }).n + 1;
      await store.set("stats/seq", { n: seq });
      id = randomId(10); book = { id, no: seq, owner: a.nick, created: T };
    }
    Object.assign(book, { title, desc, pairs, public: pub, count: pairs.length, updated: T });
    await store.set("books/" + id, book);
    const meta = { id, no: book.no, title, desc, owner: book.owner, count: pairs.length, public: pub, builtin: false, updated: T, created: book.created };
    idx = idx.filter((b) => b.id !== id); idx.push(meta);
    await store.set("index/books", idx);
    return ok({ book: meta });
  }

  if (route === "book/delete" && method === "POST") {
    const a = await auth(true); if (a.err) return a.err;
    const id = clean(body?.id, 40);
    const book = await store.get("books/" + id);
    if (!book || !isOwner(book, a.nick)) return fail(404, "단어장을 찾을 수 없어요.");
    await store.set("books/" + id, null);
    await store.set("index/books", (await loadIndex()).filter((b) => b.id !== id));
    return ok({ ok: true });
  }

  const pubRows = (rows) => rows.slice(0, 100).map(({ name, score, stage, combo, acc, cpm, at }) => ({ name, score, stage, combo, acc, cpm, at }));

  if (route === "hof" && method === "GET") {
    const id = clean(query?.book, 40);
    if (!BUILTIN.has(id)) { const m = (await loadIndex()).find((b) => b.id === id); if (!m) return ok({ rows: [] }); }
    return ok({ rows: pubRows((await store.get("hof/" + id)) || []) });
  }

  if (route === "score" && method === "POST") {
    const a = await auth(false); if (a.err) return a.err;
    const id = clean(body?.book, 40);
    if (!BUILTIN.has(id)) {
      const m = (await loadIndex()).find((b) => b.id === id);
      if (!m) return fail(404, "단어장을 찾을 수 없어요.");
      if (!m.public && !isOwner(m, a.nick)) return fail(404, "단어장을 찾을 수 없어요.");
    }
    const rec = { name: a.nick, score: int(body.score, 0, 10_000_000), stage: int(body.stage, 1, 10), kills: int(body.kills, 0, 100000),
      combo: int(body.combo, 0, 100000), acc: int(body.acc, 0, 100), cpm: int(body.cpm, 0, 3000), time: int(body.time, 0, 86400), at: T };
    const plays = await loadPlays(); plays[id] = (plays[id] || 0) + 1; await store.set("stats/plays", plays);
    let rows = (await store.get("hof/" + id)) || [];
    const prev = rows.find((r) => lower(r.name) === lower(a.nick));
    const newBest = rec.score > 0 && (!prev || rec.score > prev.score);
    if (newBest) {
      rows = rows.filter((r) => lower(r.name) !== lower(a.nick)); rows.push(rec);
      rows.sort((x, y) => y.score - x.score || x.at - y.at); rows = rows.slice(0, 500);
      await store.set("hof/" + id, rows);
    }
    const i = rows.findIndex((r) => lower(r.name) === lower(a.nick));
    return ok({ ok: true, newBest, best: newBest ? rec.score : prev ? prev.score : 0, rank: i >= 0 ? i + 1 : null, rows: pubRows(rows) });
  }

  return fail(404, "알 수 없는 요청이에요.");
}

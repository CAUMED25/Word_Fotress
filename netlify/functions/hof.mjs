// 명예의 전당 API — Netlify Functions + Netlify Blobs
// GET  /api/hof                         → { rows: [...] }  (상위 100명)
// POST /api/hof {action:"check", nick, pw}
// POST /api/hof {action:"submit", nick, pw, score, level, kills, combo, acc, cpm, diff, time}
import { getStore } from "@netlify/blobs";
import crypto from "node:crypto";

const DIFFS = new Set(["easy", "normal", "hard", "hell"]);
const MAX_ROWS = 100;

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
  });

const norm = (s) => String(s ?? "").trim().replace(/\s+/g, " ");
const keyOf = (nick) => "users/" + Buffer.from(norm(nick).toLowerCase(), "utf8").toString("hex");
const int = (v, lo, hi) => {
  const n = Math.round(Number(v));
  return Number.isFinite(n) ? Math.min(hi, Math.max(lo, n)) : lo;
};

function hashPw(pw, salt) {
  return crypto.scryptSync(String(pw), salt, 32).toString("hex");
}
function pwMatches(user, pw) {
  const a = Buffer.from(hashPw(pw, user.salt), "hex");
  const b = Buffer.from(user.hash, "hex");
  return a.length === b.length && crypto.timingSafeEqual(a, b);
}
function validate(nick, pw) {
  if (!nick || nick.length > 12 || /[\u0000-\u001f<>]/.test(nick)) return "닉네임은 1~12자로, 특수 기호(< >) 없이 입력해 주세요.";
  if (typeof pw !== "string" || pw.length < 2 || pw.length > 64) return "비밀번호는 2~64자로 입력해 주세요.";
  return null;
}
const publicRows = (board) =>
  board.slice(0, MAX_ROWS).map(({ name, score, level, combo, diff, acc, cpm, at }) => ({ name, score, level, combo, diff, acc, cpm, at }));

export default async (req) => {
  const store = getStore({ name: "hall-of-fame", consistency: "strong" });
  const loadBoard = async () => (await store.get("board", { type: "json" })) || [];

  if (req.method === "GET") return json({ rows: publicRows(await loadBoard()) });
  if (req.method !== "POST") return json({ error: "허용되지 않는 요청이에요." }, 405);

  let body;
  try { body = await req.json(); } catch { return json({ error: "잘못된 요청이에요." }, 400); }

  const nick = norm(body.nick);
  const pw = body.pw;
  const bad = validate(nick, pw);
  if (bad) return json({ error: bad }, 400);

  const ukey = keyOf(nick);
  const user = await store.get(ukey, { type: "json" });
  if (user && !pwMatches(user, pw)) return json({ error: "이미 등록된 닉네임이에요. 비밀번호가 맞지 않아요." }, 401);

  if (body.action === "check") return json({ ok: true, registered: !!user });
  if (body.action !== "submit") return json({ error: "알 수 없는 요청이에요." }, 400);

  const rec = {
    name: nick,
    score: int(body.score, 0, 10_000_000),
    level: int(body.level, 1, 999),
    kills: int(body.kills, 0, 100_000),
    combo: int(body.combo, 0, 100_000),
    acc: int(body.acc, 0, 100),
    cpm: int(body.cpm, 0, 3000),
    diff: DIFFS.has(body.diff) ? body.diff : "normal",
    at: Date.now(),
  };

  const salt = user?.salt || crypto.randomBytes(16).toString("hex");
  const u = user || { name: nick, salt, hash: hashPw(pw, salt), best: 0, plays: 0, created: Date.now() };
  u.plays = (u.plays || 0) + 1;

  let board = await loadBoard();
  const newBest = rec.score > (u.best || 0);
  if (newBest) {
    u.best = rec.score;
    board = board.filter((r) => r.name.toLowerCase() !== nick.toLowerCase());
    board.push(rec);
    board.sort((a, b) => b.score - a.score);
    board = board.slice(0, 500);
    await store.setJSON("board", board);
  }
  await store.setJSON(ukey, u);

  const idx = board.findIndex((r) => r.name.toLowerCase() === nick.toLowerCase());
  return json({ ok: true, newBest, best: u.best, rank: idx >= 0 ? idx + 1 : null, rows: publicRows(board) });
};

export const config = { path: "/api/hof" };

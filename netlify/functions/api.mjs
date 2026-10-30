// 단어 요새 API — Netlify Functions + Netlify Blobs
// 라우트: /api/login, /api/books, /api/mybooks, /api/book, /api/book/save, /api/book/delete, /api/hof, /api/score
import { getStore } from "@netlify/blobs";
import crypto from "node:crypto";
import { handle } from "./lib/core.mjs";
import { BUILTINS } from "./lib/builtins.mjs";

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" } });

export default async (req) => {
  const blobs = getStore({ name: "word-fortress", consistency: "strong" });
  const store = {
    get: (k) => blobs.get(k, { type: "json" }),
    set: (k, v) => (v == null ? blobs.delete(k) : blobs.setJSON(k, v)),
  };
  const url = new URL(req.url);
  const route = url.pathname.replace(/^\/api\/?/, "").replace(/\/$/, "");
  let body = null;
  if (req.method === "POST") {
    try { body = await req.json(); } catch { return json({ error: "잘못된 요청이에요." }, 400); }
  }
  try {
    const r = await handle({
      store,
      hash: async (pw, salt) => crypto.scryptSync(String(pw), salt, 32).toString("hex"),
      builtins: BUILTINS,
      route,
      method: req.method,
      query: Object.fromEntries(url.searchParams),
      body,
      randomId: (n) => crypto.randomBytes(n).toString("base64url").replace(/[-_]/g, "").slice(0, n).padEnd(n, "x").toLowerCase(),
    });
    return json(r.data, r.status);
  } catch (e) {
    console.error(e);
    return json({ error: "서버 오류가 났어요. 잠시 후 다시 시도해 주세요." }, 500);
  }
};

export const config = { path: "/api/*" };

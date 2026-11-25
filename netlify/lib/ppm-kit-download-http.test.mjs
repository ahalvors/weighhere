import { test } from "node:test";
import assert from "node:assert/strict";
import handler from "../functions/ppm-kit-download.mjs";

async function call(url) {
  return handler(new Request(url));
}

test("HTTP: missing session_id returns 400 HTML and does not serve a PDF", async () => {
  for (const url of [
    "https://weighhere.com/ppm-kit/download/",
    "https://weighhere.com/ppm-kit/download/?session_id=",
    "https://weighhere.com/ppm-kit/download/?session_id=%20%20",
  ]) {
    const res = await call(url);
    assert.equal(res.status, 400, url);
    assert.equal(res.headers.get("Content-Type"), "text/html; charset=utf-8");
    assert.equal(res.headers.get("X-Robots-Tag"), "noindex, nofollow");
    assert.equal(res.headers.get("Cache-Control"), "private, no-store");
    const body = await res.text();
    assert.match(body, /download is not available/i);
    assert.match(body, /support@weighhere.com/);
    assert.doesNotMatch(body, /%PDF/);
  }
});

test("HTTP: a session_id without a configured Stripe key returns 503, not the PDF", async () => {
  const prev = process.env.STRIPE_CHECKOUT_READ_KEY;
  delete process.env.STRIPE_CHECKOUT_READ_KEY;
  try {
    const res = await call("https://weighhere.com/ppm-kit/download/?session_id=cs_test_bogus");
    assert.equal(res.status, 503);
    const body = await res.text();
    assert.match(body, /support@weighhere.com/);
    assert.doesNotMatch(body, /%PDF/);
  } finally {
    if (prev !== undefined) process.env.STRIPE_CHECKOUT_READ_KEY = prev;
  }
});

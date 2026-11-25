/**
 * Serves the PPM Weigh Ticket Kit PDF only after a paid Checkout Session
 * for the configured price / payment link is verified with Stripe.
 *
 * Env (set in the Netlify UI or CLI; never commit values):
 *   STRIPE_CHECKOUT_READ_KEY          Restricted key, Checkout Sessions: Read
 *   STRIPE_PPM_KIT_PRICE_ID           price_... for the $14 kit
 *   STRIPE_PPM_KIT_PAYMENT_LINK_ID    plink_... (optional but recommended)
 *
 * PDF storage: Netlify Blobs store "ppm-kit", key "kit.pdf" — not in git.
 */
import {
  rejectReason,
  httpStatusFor,
  publicMessage,
  REASONS,
} from "../lib/ppm-kit-verify.mjs";

export const config = {
  path: ["/ppm-kit/download/", "/ppm-kit/download"],
};

const BLOB_STORE = "ppm-kit";
const BLOB_KEY = "kit.pdf";
const FILENAME = "weighhere-ppm-weigh-ticket-kit.pdf";

function errorPage(status, message) {
  const body = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Kit download | WeighHere</title>
<link rel="stylesheet" href="/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="mast">
  <div class="wrap mast-inner">
    <a class="brand" href="/"><img class="brand-logo" src="/img/weighhere-logo.svg" alt="WeighHere" width="173" height="44"><span>Public scales for U-Hauls, RVs, horse trailers, and PPM loads</span></a>
  </div>
</header>
<main id="main">
  <section class="page-head">
    <div class="wrap">
      <p class="kicker">PPM Weigh Ticket Kit</p>
      <h1>This download is not available</h1>
      <p class="lede">${escapeHtml(message)}</p>
      <p>Need help? Email <a href="mailto:support@weighhere.com">support@weighhere.com</a>.</p>
    </div>
  </section>
</main>
</body>
</html>`;
  return new Response(body, {
    status,
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "private, no-store",
      "X-Robots-Tag": "noindex, nofollow",
    },
  });
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

async function retrieveSession(sessionId, secretKey) {
  const url = new URL(`https://api.stripe.com/v1/checkout/sessions/${encodeURIComponent(sessionId)}`);
  url.searchParams.append("expand[]", "line_items");
  const res = await fetch(url, {
    headers: { Authorization: `Bearer ${secretKey}` },
  });
  if (res.status === 404) return { session: null, stripeError: null };
  if (!res.ok) {
    const err = new Error(`stripe_http_${res.status}`);
    err.status = res.status;
    throw err;
  }
  return { session: await res.json(), stripeError: null };
}

export default async (request) => {
  const url = new URL(request.url);
  const sessionId = url.searchParams.get("session_id");

  const missing = rejectReason({
    sessionId,
    session: { id: "pending" },
    expectedPriceId: "pending",
    expectedPaymentLinkId: "",
  });
  if (missing === REASONS.missing_session) {
    return errorPage(httpStatusFor(REASONS.missing_session), publicMessage(REASONS.missing_session));
  }

  const secretKey = (process.env.STRIPE_CHECKOUT_READ_KEY || "").trim();
  const expectedPriceId = (process.env.STRIPE_PPM_KIT_PRICE_ID || "").trim();
  const expectedPaymentLinkId = (process.env.STRIPE_PPM_KIT_PAYMENT_LINK_ID || "").trim();

  if (!secretKey) {
    return errorPage(
      503,
      "Downloads are not configured yet. If you already paid, email support@weighhere.com.",
    );
  }

  let session;
  try {
    const result = await retrieveSession(sessionId.trim(), secretKey);
    session = result.session;
  } catch {
    return errorPage(
      503,
      "We could not verify this checkout right now. Please try again, or email support@weighhere.com.",
    );
  }

  const reason = rejectReason({
    sessionId,
    session,
    expectedPriceId,
    expectedPaymentLinkId,
  });
  if (reason) {
    return errorPage(httpStatusFor(reason), publicMessage(reason));
  }

  try {
    const { getStore } = await import("@netlify/blobs");
    const store = getStore(BLOB_STORE);
    const file = await store.get(BLOB_KEY, { type: "arrayBuffer" });
    if (!file) {
      return errorPage(
        503,
        "The kit file is not available yet. If you already paid, email support@weighhere.com.",
      );
    }
    return new Response(file, {
      status: 200,
      headers: {
        "Content-Type": "application/pdf",
        "Content-Disposition": `attachment; filename="${FILENAME}"`,
        "Cache-Control": "private, no-store",
        "X-Robots-Tag": "noindex, nofollow",
      },
    });
  } catch {
    return errorPage(
      503,
      "The kit file is not available yet. If you already paid, email support@weighhere.com.",
    );
  }
};

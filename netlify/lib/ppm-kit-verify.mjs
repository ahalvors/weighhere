/**
 * Pure checkout-session checks for the PPM Weigh Ticket Kit download.
 * No network, no secrets, no file I/O — safe to unit-test with fixtures.
 */

export const REASONS = {
  missing_session: "missing_session",
  not_found: "not_found",
  not_paid: "not_paid",
  wrong_product: "wrong_product",
};

/**
 * Collect price IDs from a Checkout Session, including expanded line_items.
 */
export function linePriceIds(session) {
  if (!session || typeof session !== "object") return [];
  const items =
    (session.line_items && Array.isArray(session.line_items.data) && session.line_items.data) ||
    (Array.isArray(session.line_items) && session.line_items) ||
    [];
  const ids = [];
  for (const item of items) {
    const price = item && item.price;
    if (!price) continue;
    if (typeof price === "string") ids.push(price);
    else if (price.id) ids.push(price.id);
  }
  return ids;
}

export function paymentLinkId(session) {
  if (!session || typeof session !== "object") return null;
  const pl = session.payment_link;
  if (!pl) return null;
  return typeof pl === "string" ? pl : pl.id || null;
}

function normalizeId(value) {
  if (value == null) return "";
  return String(value).trim();
}

/**
 * Return a rejection reason, or null if the session may be used to serve the kit.
 *
 * expectedPriceId and expectedPaymentLinkId come from env. If both are set, the
 * session must match the price and, when the session has a payment_link, that
 * link id. A paid session with no payment_link still passes if the price matches
 * (for test fixtures or a Checkout Session created without a Payment Link).
 */
export function rejectReason({ sessionId, session, expectedPriceId, expectedPaymentLinkId }) {
  const id = normalizeId(sessionId);
  if (!id) return REASONS.missing_session;
  if (!session || typeof session !== "object" || !session.id) return REASONS.not_found;

  if (session.payment_status !== "paid") return REASONS.not_paid;

  const wantPrice = normalizeId(expectedPriceId);
  const wantLink = normalizeId(expectedPaymentLinkId);
  if (!wantPrice && !wantLink) {
    // Misconfiguration: never serve the kit without knowing what was bought.
    return REASONS.wrong_product;
  }

  if (wantPrice) {
    const prices = linePriceIds(session);
    if (!prices.includes(wantPrice)) return REASONS.wrong_product;
  }

  if (wantLink) {
    const got = paymentLinkId(session);
    // Sessions created from the Payment Link should carry it. If a link id is
    // present, it must match. If it's absent, the price check above is enough
    // only when a price was also configured; require the link when we have one
    // on the session, and when the session originated as a payment link type.
    if (got && got !== wantLink) return REASONS.wrong_product;
    if (!got && !wantPrice) return REASONS.wrong_product;
  }

  return null;
}

export function httpStatusFor(reason) {
  switch (reason) {
    case REASONS.missing_session:
      return 400;
    case REASONS.not_found:
      return 404;
    case REASONS.not_paid:
    case REASONS.wrong_product:
      return 403;
    default:
      return 403;
  }
}

export function publicMessage(reason) {
  switch (reason) {
    case REASONS.missing_session:
      return "This download link is missing a checkout session. If you already paid, use the link from your receipt or email support@weighhere.com.";
    case REASONS.not_found:
      return "We could not find a checkout session for this link. If you already paid, email support@weighhere.com.";
    case REASONS.not_paid:
      return "This checkout is not paid, so the kit cannot be downloaded yet.";
    case REASONS.wrong_product:
      return "This checkout is not for the PPM Weigh Ticket Kit, so the file cannot be downloaded.";
    default:
      return "This download is not available. If you already paid, email support@weighhere.com.";
  }
}

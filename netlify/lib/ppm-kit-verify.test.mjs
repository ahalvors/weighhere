import { test } from "node:test";
import assert from "node:assert/strict";
import {
  rejectReason,
  linePriceIds,
  paymentLinkId,
  httpStatusFor,
  publicMessage,
  REASONS,
} from "./ppm-kit-verify.mjs";

const PRICE = "price_test_ppm_kit";
const LINK = "plink_test_ppm_kit";

function paidSession(overrides = {}) {
  return {
    id: "cs_test_123",
    object: "checkout.session",
    payment_status: "paid",
    status: "complete",
    payment_link: LINK,
    line_items: {
      object: "list",
      data: [{ price: { id: PRICE, object: "price" }, quantity: 1 }],
    },
    ...overrides,
  };
}

const env = { expectedPriceId: PRICE, expectedPaymentLinkId: LINK };

test("missing session_id is rejected", () => {
  for (const sessionId of [undefined, null, "", "   "]) {
    const reason = rejectReason({ sessionId, session: paidSession(), ...env });
    assert.equal(reason, REASONS.missing_session);
    assert.equal(httpStatusFor(reason), 400);
  }
});

test("missing or empty session object is not_found when an id is present", () => {
  assert.equal(rejectReason({ sessionId: "cs_test_123", session: null, ...env }), REASONS.not_found);
  assert.equal(rejectReason({ sessionId: "cs_test_123", session: {}, ...env }), REASONS.not_found);
  assert.equal(httpStatusFor(REASONS.not_found), 404);
});

test("unpaid and incomplete sessions are refused", () => {
  for (const payment_status of ["unpaid", "no_payment_required", null, ""]) {
    const reason = rejectReason({
      sessionId: "cs_test_123",
      session: paidSession({ payment_status }),
      ...env,
    });
    assert.equal(reason, REASONS.not_paid, `status ${payment_status}`);
    assert.equal(httpStatusFor(reason), 403);
  }
});

test("paid session for the expected price and payment link is allowed", () => {
  assert.equal(
    rejectReason({ sessionId: "cs_test_123", session: paidSession(), ...env }),
    null,
  );
});

test("wrong price is refused even when paid", () => {
  const session = paidSession({
    line_items: { data: [{ price: { id: "price_other" } }] },
  });
  assert.equal(rejectReason({ sessionId: "cs_test_123", session, ...env }), REASONS.wrong_product);
  assert.equal(httpStatusFor(REASONS.wrong_product), 403);
});

test("wrong payment link is refused even when the price matches", () => {
  const session = paidSession({ payment_link: "plink_other" });
  assert.equal(rejectReason({ sessionId: "cs_test_123", session, ...env }), REASONS.wrong_product);
});

test("payment_link may be an expanded object", () => {
  const session = paidSession({ payment_link: { id: LINK, object: "payment_link" } });
  assert.equal(rejectReason({ sessionId: "cs_test_123", session, ...env }), null);
});

test("line item price may be a string id", () => {
  const session = paidSession({ line_items: { data: [{ price: PRICE }] } });
  assert.equal(rejectReason({ sessionId: "cs_test_123", session, ...env }), null);
  assert.deepEqual(linePriceIds(session), [PRICE]);
});

test("paid session without a payment_link still passes if the price matches", () => {
  const session = paidSession({ payment_link: null });
  assert.equal(rejectReason({ sessionId: "cs_test_123", session, ...env }), null);
});

test("refuses when neither expected price nor payment link is configured", () => {
  const reason = rejectReason({
    sessionId: "cs_test_123",
    session: paidSession(),
    expectedPriceId: "",
    expectedPaymentLinkId: "",
  });
  assert.equal(reason, REASONS.wrong_product);
});

test("link-only config requires the payment_link to match", () => {
  const cfg = { expectedPriceId: "", expectedPaymentLinkId: LINK };
  assert.equal(rejectReason({ sessionId: "cs_test_123", session: paidSession(), ...cfg }), null);
  assert.equal(
    rejectReason({ sessionId: "cs_test_123", session: paidSession({ payment_link: null }), ...cfg }),
    REASONS.wrong_product,
  );
});

test("price-only config requires the price to match", () => {
  const cfg = { expectedPriceId: PRICE, expectedPaymentLinkId: "" };
  assert.equal(rejectReason({ sessionId: "cs_test_123", session: paidSession({ payment_link: null }), ...cfg }), null);
  assert.equal(
    rejectReason({
      sessionId: "cs_test_123",
      session: paidSession({ line_items: { data: [{ price: { id: "price_other" } }] } }),
      ...cfg,
    }),
    REASONS.wrong_product,
  );
});

test("helpers and public copy", () => {
  assert.equal(paymentLinkId(paidSession()), LINK);
  assert.ok(publicMessage(REASONS.missing_session).includes("support@weighhere.com"));
  assert.ok(publicMessage(REASONS.not_found).includes("support@weighhere.com"));
  assert.deepEqual(linePriceIds(null), []);
});

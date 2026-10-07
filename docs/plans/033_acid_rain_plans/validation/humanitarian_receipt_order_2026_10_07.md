# Acid Rain aftermath submission receipt order

Disposition: source repair verified, Humanitarian integration acceptance remains incomplete.

The aftermath helper previously set `acid_rain_humanitarian_tier_registered` before calling the famine owner.
An owner rejection or rounded-zero amount therefore recorded a successful tier submission that never occurred and prevented the same tier's later valid retry.
The new focused test reproduced that failure on the original source with `rejected tier request committed its registration watermark`.

`acid_rain_register_humanitarian_pressure` now returns the famine owner's receipt in temporary `acid_rain_humanitarian_result`.
The aftermath caller declares that output before invoking the helper and writes its persistent registration watermark only when the result equals the owner's success value.
Rejected, rounded-zero and invalid-state attempts leave the previous watermark unchanged.
An accepted tier still deduplicates later equal or lower-tier submissions.
No pressure amount, mortality, Chaos mapping, decision cost, AI weight, duration or source-retirement policy changes.
No shared famine effect or aggregate field was edited.

The test `.tools/validation/test_033_humanitarian_receipts.js` executes both actual Event 033 helper bodies through the existing Clausewitz parser, with helper-return storage modeled separately from persistent state variables.
It covers rejection, accepted retry, duplicate acceptance, rejected higher tier, accepted higher tier, old lower tier, rounded-zero amount and invalid frozen state.
The external famine owner, native predicates, scope values and arithmetic are explicit mocks, and unknown commands fail instead of receiving a permissive mock.
All eight cases pass after the repair.
The in-memory negative control removes the caller output declaration and confirms that the nested receipt is lost rather than silently promoted to persistent success.
The complete Event 033 synthetic/source validator was rerun and still passes.
Neither test proves native owner acceptance, source-specific retirement, migration or save/reload behavior.

Relevant references read by the parent are offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 435 to 442, describing temporary caller-owned output storage, and installed `documentation/effects_documentation.md`, lines 7820 to 7827, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, retrieved successfully with `hoi4.reference_read`.
The adapter's existing success receipt is assigned after `famine_request_disaster_pressure` in `common/scripted_effects/famine_adapter_effects.txt`, with output storage initialized before that nested request.

The corrected runtime file SHA-256 at test time is `2805a9af30ac54e332fb0ec09136c62c232f1b57083df9bee2cedebd6fcae09c`.
The source lookup successfully returned the corrected tier helper at `mod:common/scripted_effects/033_acid_rain_aftermath_effects.txt`, lines 653 to 679, revision `5001e6aea42d6217737f434a1f4221e9e6339bb5e60558405614e8c0d93aac90`, with its full body, one unshadowed definition and no omitted lines.
The original source SHA-256, focused test and current indexed helper receipt are retained in [the evidence record](humanitarian_receipt_order_2026_10_07.json).
The focused worker-event lint of `chaosx.nr33.20` timed out after 600 seconds with no graph or lint artifact.
It was retried on the smaller `chaosx.nr33.47` state-operation callback, still limited to one node, one edge, depth one and no helper expansion.
That retry is active at this checkpoint and does not yet provide event-lint acceptance.
Current completion and Humanitarian architecture auditors were notified of this exact repair so their source identities and proposals do not silently refer to the earlier file.
The broader proof-floor construction, generic aggregate pressure endpoint, source-specific recovery retirement and historical source attribution remain open requirements.

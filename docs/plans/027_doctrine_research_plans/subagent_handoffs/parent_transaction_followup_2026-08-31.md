# Event 027 Parent Transaction Follow-up

> **Superseded status notice (2026-09-01):** This dated transaction follow-up is preserved as historical source evidence and is superseded as a current MCP status authority by ../documentation_state.md. Its exact receipt-readback finding remains current source evidence, while its old transport statement is stale.

## Scope

This parent audit covers the native mastery transaction, receipt recovery, and the human continuation path after a banked native mastery assignment.

## Findings

The mastery grant is implemented through the documented native `add_mastery` effect in one-point increments, with a `has_mastery_level` readback after each increment and an exact one-level postcondition.

Grand Doctrine adoption uses the documented native `set_grand_doctrine` effect and verifies the selected Grand Doctrine with `has_doctrine` before consuming the choice.

Empty-track actions use the documented native `set_sub_doctrine` effect with explicit folder and track indexes, preserve the native banked mastery state, and grant the Event 027 mastery step only after the assigned track is occupied and the exact postcondition succeeds.

The receipt ledger records the batch, choice number, action, domain, Grand Doctrine, track, subdoctrine, pre-level, and post-level before mutation, and consumes the choice only after the native effect succeeds.

The audit found that a successful banked native adoption leaves the choice number unchanged by design, so a later choice could have been mistaken for the earlier terminal receipt. `doctrine_research_restore_current_receipt_selection` and `doctrine_research_confirm_selection` now recover receipts only while `doctrine_research_transaction_receipt_pending` is set, allowing later choices to use their new selection normally.

The generic confirmation path no longer marks every new selection as native completion, and the adoption adapter explicitly clears the native-completion marker before applying `set_grand_doctrine`. A failed adoption therefore cannot be reported as a no-choice banked-mastery result.

A pending marker without a matching receipt now records an ambiguous transaction and quarantines the active batch instead of applying a fresh selection or reopening the same confirmation indefinitely.

Receipt recovery for an `effect_applied` mastery receipt now re-reads the native mastery level on every retry and requires both the stored post-level and the current observed level to equal the receipt pre-level plus exactly one native mastery increment. Adoption recovery likewise requires the recorded Grand Doctrine to remain active. Any mismatch is marked ambiguous and quarantines the batch.

The global-host coordinator now persists the current host as `doctrine_research_global_host`; the tag-switch reconciliation path uses that target instead of an Event 027-specific recurring whole-world pass.

## Validation

The touched Event 027 scripted effects remain brace-balanced at 7,743 opening and closing braces after the recovery-proof guard was added.

The native exact adapter still contains 107 `add_mastery` calls and 107 `set_sub_doctrine` calls, with zero forbidden experience, technology, replacement-doctrine, or mastery-dump helpers.

The Event 027 localization file remains UTF-8 with BOM.

## Remaining evidence boundary

The implementation is source-playable for the ordinary native mastery path, but final acceptance still requires the mandated MCP event inspection/render/compare, doctrine and technology inspection/render/compare, named probability comparisons, and live save/reload and lifecycle evidence.

The current MCP route returns `Transport closed` before parsing Event 027, so no new engine artifact is claimed by this handoff.

Special Forces remains fail-closed when both reusable-token tracks are occupied because the documented native trigger surface exposes track occupancy but no exact subdoctrine identity-at-track query.

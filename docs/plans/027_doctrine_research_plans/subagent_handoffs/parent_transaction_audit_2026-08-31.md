# Event 027 transaction audit — 2026-08-31

> **Superseded status notice (2026-09-01):** This dated transaction audit is preserved as historical evidence and is superseded as a current MCP status authority by ../documentation_state.md. Its transport statement is stale after the fresh bounded Event 027 calls, while its runtime blockers remain open.

## Scope

This parent audit checks the native transaction paths after the receipt-recovery patch and records the current engine-evidence boundary.

## Source proof

- Grand Doctrine adoption dispatches all thirteen declared doctrine tokens through native `set_grand_doctrine` and verifies the corresponding `has_doctrine` postcondition.
- A verified adoption enters `doctrine_research_finalize_receipt`, which records `choice_consumed`, subtracts exactly one from the active batch, advances the choice number, records one successful adoption, and grants zero Event 027 mastery steps.
- Active-track mastery uses the native `add_mastery` effect through 107 explicit subdoctrine/track adapters, with one `constant:doctrine_research_event.mastery_point_increment` per loop and an exact post-level readback.
- Empty-track mastery uses native `set_sub_doctrine` followed by the same one-step mastery adapters when the selected branch remains incomplete.
- If native banked mastery completes an empty-track branch during assignment, the receipt is recorded as `native_adoption` without finalization or choice consumption, and the human/AI flow revalidates the remaining pool.
- Prepared and effect-applied receipts are recovered by batch and choice identity; the pending marker reopens the confirmation route after reload or an intervening invalidation, and an effect-applied mastery receipt is reread before finalization.
- No Event 027 transaction path calls generic military experience, technology helpers, doctrine replacement, or a multi-level mastery dump.

## Current evidence boundary

The source audit is balanced and the adoption/mastery dispatch is present, but the mandatory HOI4 MCP retry for `chaosx.nr27.1` still returns `Transport closed`. Native doctrine inspect/render/compare and the required live save/reload, queue, lifecycle, presentation, achievement, and probability evidence therefore remain unproven. The implementation is source-playable, but the Event 027 acceptance gate is not complete and no completion commit is authorized.

The final source audit also removed the unused first-valid Grand Doctrine helper from `common/scripted_effects/027_doctrine_research_effects.txt`; the active AI picker remains the scored adapter path, and no call site for the stale helper remains.

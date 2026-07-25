# Event 006 DM-58 preflight scope post-repair review — 2026-07-26

## Verdict

**PASS for commit `5dcb2c8de`'s requested scope repair.**

In `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, `is_independence_wave_reclamation_front_member_candidate` is invoked from `has_independence_wave_reclamation_front_preflight`'s `any_country` selector.

The relevant scope stack is activating decision country -> iterated candidate member -> candidate state -> external state owner.

At the owner level, `PREV` is the candidate state and `PREV.PREV` is the iterated candidate member.

The repaired self-tag, war-state, declaration-legality, and existing-wargoal checks therefore evaluate the candidate member against the current external owner, rather than evaluating the activating country or treating the state as a country.

`is_claimed_by = PREV` remains outside the `owner` block, where `PREV` correctly remains the candidate member.

## Remaining narrow caveat

`has_independence_wave_reclamation_front_preflight` still counts candidate members independently and cannot prove an injective member-to-owner assignment before selection.

The existing DM-58 execution ledger remains the authority for duplicate-owner rejection and rollback.

This is separate from the repaired scope error and does not require any further source change in this review.

## Boundary

Read-only review of commit `5dcb2c8de69c237b3b1a47b265599f246a9764cf` and its immediate DM-58 trigger context.

No gameplay, localisation, GUI, attestation, or registry source was changed.

# DM-58 Scope and Provenance Repair — 2026-07-25

## Status

Parent implementation repair applied after the post-`972037edd` audit. This handoff supersedes the unresolved implementation findings in `006_dm58_post_972037edd_reaudit_2026_07_25.md` for the source surfaces listed below.

## Source changes

- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
  - DM-58 state validation now resolves the requesting member through the saved `independence_wave_reclamation_front_member` target rather than relying on `ROOT` after a `for_each_scope_loop` scope change.
  - War legality is checked from the member against the current owner, and an existing `take_state_focus` wargoal against that owner makes the state ineligible.
  - The generic used marker plus the synchronized state array enforce one state per operation; the old member-keyed `@ROOT` generation marker was removed from this resolver.
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
  - Each member iteration overwrites the saved member target and appends aligned member, state, and owner entries.
  - Claims are added only when absent and are marked with `independence_wave_dm58_reclamation_front_claim_added` only when this transaction created them.
  - The resolver contains no `clear_event_target` call.
  - Pre-cost rollback walks the aligned arrays by index, uses the frozen owner entry rather than re-resolving a state's current owner, removes only transaction-created claims, removes the finite wargoal created for the aligned member/owner pair, clears staged markers, and clears the arrays.
- `common/decisions/006_independence_wave_decisions.txt`
  - Success cleanup clears the aligned member array and state provenance marker alongside the state array.
- `common/scripted_effects/006_independence_wave_effects.txt`
  - Shared operation cleanup clears the claim provenance marker and aligned member array while leaving successful finite wargoals to their explicit expiry.
- `docs/events/006_independence_wave/reclamation_front_lifecycle.md`
  - Documents the saved-target scope model, aligned arrays, claim provenance, and lossless pre-cost rollback.

## Validation evidence

- Touched Clausewitz files passed a brace/quote scan and contain no unsupported `<=` or `>=` operators.
- `python .tools/audit_event6_allocator.py` still passes with automatic counts `3 / 4 / 5 / 7 / 10` and World Collapse count `10`.
- No live game launch was performed; live decision, AI, and war-resolution evidence remains a separate blocker for final completion.

## Remaining audit boundary

The earlier focus-layout, package-depth, super-event, asset-frame, documentation-lock, scenario-runtime, and live/AI evidence blockers remain open. This handoff only closes the DM-58 scope/provenance findings.

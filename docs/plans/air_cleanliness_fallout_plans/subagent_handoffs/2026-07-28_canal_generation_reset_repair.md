# Canal Schedule generation-reset repair

Date: 2026-07-28

Scope: replace the reviewed candidate `628` reset shortcut with an exact stale-row cancellation route and wire it into the shared Fallout runtime reset.

Changed files:

- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_CANAL_SCHEDULE_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md`

Implementation evidence:

- `fallout_event_628_abort_on_generation_change` now runs before shared dispatch and runtime arrays are cleared.
- The effect authenticates the frozen state against owner, controller, current generation, Air Winter snapshot, native infrastructure, and rural or pastoral category.
- A stale uncommitted opening is cancelled through the issued ordinary receipt wrapper with one cancellation history row and state reservation release.
- Unpaid branches are refunded only before a result history receipt exists.
- Issued result and callback rows are terminalized through exact delayed-result wrappers, cleanup tombstones are removed, and the committed state flag is cleared only after no Canal Schedule token remains issued.
- Native infrastructure and water-policy modifier cleanup remains owned by `fallout_event_628_clear_state_reservation`.

Validation:

- Canal Schedule effects braces: `1031/1031`.
- Shared Fallout effect braces: `5324/5324`.
- Forbidden operators: zero in both touched script files.
- Runtime reset execution, delayed dispatch, save recovery, host authority, and multiplayer behavior remain unobserved because Hearts of Iron IV was not launched.

Remaining risk:

This is static source evidence. The live engine has not been observed rebuilding the generation while a Canal Schedule opening, result, callback, or cleanup receipt is issued.

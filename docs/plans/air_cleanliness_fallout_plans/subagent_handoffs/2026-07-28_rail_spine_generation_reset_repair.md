# Rail Spine Vote generation-reset repair

Date: 2026-07-28

Scope: replace the reviewed candidate `621` reset shortcut with an exact stale-row cancellation route and wire it into the shared Fallout runtime reset.

Changed files:

- `common/scripted_effects/fallout_world_end_rail_spine_vote_event_effects.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_RAIL_SPINE_VOTE_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md`

Implementation evidence:

- `fallout_event_621_abort_on_generation_change` now runs before the shared dispatch envelope and runtime arrays are cleared.
- The effect authenticates the frozen state against owner, controller, current generation, Air Winter snapshot, native railway, and infrastructure.
- A stale uncommitted opening is cancelled through the issued ordinary receipt wrapper with a typed cancellation history row and state reservation release.
- Unpaid branches are refunded only before a result history receipt exists.
- Issued result and callback rows are terminalized through exact delayed-result wrappers, cleanup tombstones are removed, and the committed state flag is cleared only after no Rail Spine token remains issued.
- The existing native-state modifier cleanup remains owned by `fallout_event_621_clear_state_reservation`.

Validation:

- Rail Spine effects braces: `898/898`.
- Shared Fallout effect braces: `5324/5324`.
- Forbidden operators: zero in both touched script files.
- Runtime reset execution, delayed dispatch, save recovery, host authority, and multiplayer behavior remain unobserved because Hearts of Iron IV was not launched.

Remaining risk:

This is static source evidence. The live engine has not been observed rebuilding the generation while a Rail Spine opening, result, callback, or cleanup receipt is issued.

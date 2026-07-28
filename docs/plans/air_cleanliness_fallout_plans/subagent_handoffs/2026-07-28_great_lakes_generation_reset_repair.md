# Great Lakes Lock Winter generation-reset repair

Date: 2026-07-28

Scope: repair the reviewed candidate `663` generation-reset path without activating the Fallout scheduler or expanding the content matrix.

Changed files:

- `common/scripted_effects/fallout_world_end_great_lakes_lock_winter_event_effects.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_GREAT_LAKES_LOCK_WINTER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md`
- `docs/plans/air_cleanliness_fallout_plans/source_of_truth_map.md`

Implementation evidence:

- `fallout_event_663_abort_on_generation_change` is called by `fallout_event_clear_country_runtime` before dispatch envelopes and runtime arrays are cleared.
- The effect authenticates the state owner, controller, Air Winter record, generation, native naval base, and infrastructure before treating the target as current.
- An uncommitted opening is cancelled through the issued ordinary receipt wrapper when its state is stale.
- An unpaid branch is refunded only when result effects are not committed.
- Issued result and callback rows are terminalized through the exact delayed-result wrappers, their cleanup tombstones are removed, one cancellation history row is recorded, and the state reservation is released.
- The effect clears Great Lakes runtime flags and frozen variables only after no Great Lakes token remains issued.
- The result-memory flag is cleared with the row cleanup so a stale transition cannot leave a replay marker behind.

Validation:

- Great Lakes effect braces: `1027/1027`.
- Shared Fallout effect braces: `5324/5324`.
- Forbidden operators: zero in both touched script files.
- Runtime reset execution, delayed engine delivery, save recovery, host authority, multiplayer behavior, and player-visible presentation remain unobserved because Hearts of Iron IV was not launched.

Remaining risk:

The source ordering proves the intended stale-row route only statically. It does not prove that the live engine evaluates the exact wrapper chain before rebuilding the global registry or that a save taken at each receipt boundary reconstructs the same state.

# Mine Generator opening-target repair

Date: 2026-07-28

Scope: keep the existing Mine Generator generation-reset route state-bound when it cancels a stale uncommitted opening.

Changed files:

- `common/scripted_effects/fallout_consolidated_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_MINE_GENERATOR_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md`

Implementation evidence:

- The stale opening branch now copies `fallout_event_dispatch_issued_target` into `fallout_event_642_target_state_id` before the exact ordinary cancellation wrapper runs.
- On accepted cancellation it records the typed cancellation history, reverses branch settlement, refunds the paid branch cost, releases the state reservation, clears the committed state flag, and clears the frozen row.
- The target snapshot prevents a lost opening from releasing only country receipt state while leaving the selected native resource state reservation behind.

Validation: static effect checks and documentation review remain required before commit. Runtime reset execution, delayed dispatch, save recovery, host authority, and multiplayer behavior remain unobserved because Hearts of Iron IV was not launched.

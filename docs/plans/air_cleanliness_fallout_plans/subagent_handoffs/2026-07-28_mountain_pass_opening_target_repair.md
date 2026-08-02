# Mountain Pass Census opening-target repair

Date: 2026-07-28

Scope: keep the existing Mountain Pass generation-reset route state-bound when it cancels a stale uncommitted opening.

Changed files:

- `common/scripted_effects/fallout_consolidated_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_MOUNTAIN_PASS_CENSUS_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md`

The stale opening branch now copies `fallout_event_dispatch_issued_target` into `fallout_event_635_target_state_id` before the exact ordinary cancellation wrapper runs. On accepted cancellation it records the typed cancellation history, releases the state reservation, clears the committed state flag, and clears the frozen row. This prevents a lost opening from releasing only country receipt state while leaving the selected native state reservation behind.

Validation: Mountain Pass effects remain brace-balanced after the patch, and the shared reset hook continues to call the existing `fallout_event_635_abort_on_generation_change` route. Runtime reset execution and save recovery remain unobserved because Hearts of Iron IV was not launched.

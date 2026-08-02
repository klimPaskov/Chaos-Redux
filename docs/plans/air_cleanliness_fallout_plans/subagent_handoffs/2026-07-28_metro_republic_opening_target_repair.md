# Metro Republic Below opening-target repair

Date: 2026-07-28

Scope: keep the existing Metro Republic Below generation-reset route state-bound when it cancels a stale uncommitted opening.

Changed files:

- `common/scripted_effects/fallout_consolidated_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_METRO_REPUBLIC_BELOW_PROOF.md`

Implementation evidence:

- The reset effect now recognizes the human and hidden-AI opening tokens before the generic generation branch runs.
- A stale opening snapshots `fallout_event_dispatch_issued_target` into `fallout_event_614_target_state_id` before the exact ordinary cancellation wrapper runs.
- On accepted cancellation it records typed cancellation history, refunds any unresolved paid branch, releases the state reservation, clears the committed state flag, and clears the frozen row.

Validation: Metro Republic effects remain brace-balanced with zero forbidden comparison operators. Runtime reset execution, delayed dispatch, save recovery, host authority, and multiplayer behavior remain unobserved because Hearts of Iron IV was not launched.

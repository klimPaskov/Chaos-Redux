# The New Year Without Fireworks generation-reset repair handoff

Status: static source repair complete for the dormant country-only candidate. Runtime delivery, save recovery, and scheduler activation are not claimed.

## Identity

The repair covers candidate `649`, events `649` through `655`, transaction `710064`, route `7164`, and Event Log history `9170`.

## Repair contract

`fallout_event_649_abort_on_generation_change` is called by `fallout_event_clear_country_runtime` before the shared dispatch envelope, ordinary receipt, and runtime arrays are cleared. It detects a registry-generation or issued-dispatch-generation mismatch, cancels an unconsumed human or hidden-AI opening, refunds only an uncommitted branch cost, terminalizes an issued result or callback receipt, prepares and releases the matching cleanup tombstone, and clears the country-only frozen flags and variables after the envelope is no longer live.

The row has no state reservation. Its stale path therefore does not release a state flag and instead clears only the candidate-owned country chain. It leaves newer unrelated dispatch tokens untouched.

The source ordering preserves the old registry header while the transition generation has changed. This lets the authenticated cancellation wrappers consume the old receipt before the rebuild clears the shared arrays. Static inspection proves the ordering in source, while runtime confirmation remains open.

## Files changed

- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_NEW_YEAR_WITHOUT_FIREWORKS_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md`
- `docs/plans/air_cleanliness_fallout_plans/source_of_truth_map.md` was already current and required no edit.

The older New Year and Second Dust Bowl reconciliation handoffs were updated so their remaining-risk language distinguishes static repair from runtime acceptance.

## Validation boundary

The New Year effect has balanced braces at `974` opening and `974` closing braces and no unsupported comparison operators, em dashes, or semicolons. The shared country cleanup effect has balanced braces at `5324` opening and `5324` closing braces and no forbidden tokens. No HOI4 process was launched.

Scheduler activation, host authority, save recovery, delayed delivery, multiplayer behavior, live Event Log rendering, player-visible presentation, wider stale-row coverage, and the exact all-valid-province thermonuclear sweep remain open.

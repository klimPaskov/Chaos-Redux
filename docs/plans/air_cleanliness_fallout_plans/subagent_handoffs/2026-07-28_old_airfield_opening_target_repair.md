# Old Airfield opening target repair

## Scope

This handoff covers the generation-reset guard for the dormant Old Airfield chain at `chaosx.fallout.586` through `chaosx.fallout.592`.

## Changed files

- `common/scripted_effects/fallout_consolidated_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_OLD_AIRFIELD_CHAIN_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/README_IMPLEMENTATION_STATUS.md`

## Repair

`fallout_event_586_abort_on_generation_change` now recognizes a human or hidden-AI opening receipt that is still issued and not committed. It evaluates the dispatch target through `fallout_event_586_state_is_current`, cancels a stale target with the shared ordinary receipt coordinator, records the chain cancellation stage, releases the state reservation and committed marker, and clears the frozen state snapshot. The existing paid-branch refund and generation cleanup paths remain unchanged.

## Static evidence

The touched effect file has `1067` opening braces and `1067` closing braces. A forbidden comparison scan found no `<=` or `>=` tokens. The new branch references only the existing Old Airfield human and hidden-AI event tokens, cancellation reason, history stage, reservation flags, and frozen snapshot helper.

## Remaining risk

This is source evidence only. The dormant scheduler has no activation setter. Runtime dispatch ordering, target-scope evaluation, save recovery, multiplayer behavior, Event Log rendering, and the exact engine timing of generation reset remain unobserved because HOI4 was not launched.

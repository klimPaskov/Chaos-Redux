# Fallout Living-World Scheduler Proof

## Status

The living-world scheduler has a dormant initialization substrate. It records the reveal timeline, freezes a stable post-allocation country registry, initializes country runtime rows, and exposes five-part orientation and anti-repetition contracts. It does not schedule or fire an event.

The activation flags `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` have no setter. Suffixes `100` through `122` are typed reservations only. Defined event blocks in that range: `0`. Countable blocks toward the 660-block release floor: `0`.

## Owned files

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`
- the narrow map-return and coordinator calls in `common/scripted_effects/fallout_world_end_effects.txt`

No Fallout event definition, localisation key, decision, focus, on-action file, sound, sprite, or asset path is added by this tranche.

## Reveal timeline transaction

A successful current-schema map return writes all three identity receipts:

- `global.fallout_event_timeline_generation`
- `global.fallout_event_timeline_start_date`
- `global.fallout_event_timeline_start_day`

It then sets `fallout_event_scheduler_initialization_pending`. The project coordinator calls `fallout_event_scheduler_reconcile` inside the existing at-most-once global-date transaction. No new daily or monthly on-action is added.

`fallout_event_map_return_receipts_are_current` requires completed Fallout, a successful map-return receipt, an inactive transition, the current transition generation, and start date and day values that are not in the future. Elapsed time is recomputed as current engine day minus the frozen reveal day. The exact phase bands are:

| Phase | Inclusive elapsed-day range |
| --- | ---: |
| Ash week | 0 through 7 |
| First season | 8 through 90 |
| First winter year | 91 through 365 |
| Consolidation | 366 through 730 |
| Rival orders | 731 through 1460 |
| New states | 1461 through 2190 |
| Soot retreat | 2191 through 2920 |
| Second world | 2921 through 3650 |
| Open continuation | 3651 onward |

The phase receipt records the transition generation and exact update day. Completed legacy Fallout saves do not receive a fabricated reveal day or scheduler request.

## Registry commit transaction

Registry construction begins only when `fallout_successor_allocation_is_current` passes. The builder copies the final deterministic order of `global.fallout_successor_assigned_countries`. It does not construct a second world-country pool.

Three aligned arrays retain country, transition generation, and stable zero-based index. Each country row stores the same generation and index. Validation proves:

- equal array lengths
- source count equal to the committed successor assignment count
- reciprocal membership between the source and registry arrays
- each stored numeric index equal to its real array position
- the country at that position stores that same index and generation
- current runtime schemas and bounded row values

The numeric index proof makes a duplicate country fail because one country cannot hold two different stable indexes. `fallout_event_scheduler_registry_ready` is written only after the complete uncommitted payload passes. It is the registry commit marker. Later annexation does not delete the identity row.

## Country runtime row

Each committed registry member receives versioned runtime receipts for the scheduler, orientation, arc slots, delayed queue, and bilateral ledger. The initialized row contains:

- active major-arc count of zero with a maximum of three
- twenty cooldown-family fatigue entries, including the unused index zero
- a last-family value used as a hard immediate-repeat veto
- an ordinary cooldown day
- a seven-day reveal quiet-period day
- five independent orientation receipts
- eight aligned bilateral arrays initialized empty

The five orientation components are national orientation, capital condition, immediate resource crisis, government archetype, and first character or institution. Ordinary-event eligibility requires all five current-generation receipts.

The ordinary cooldown helper is implemented but unreachable from gameplay because no event calls it and both activation flags remain unset. Fatigue slots are structural only. The accepted specs do not define mutation, decay, or score magnitudes, so no fatigue producer is implemented. Arc reservation, delayed-result scheduling, bilateral reservation, and survival-ledger effects are not implemented by this tranche.

## Required future survival ledger

The accepted resource identities are Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition. Cohesion and Reclamation are not resource entries.

The reviewed transaction contract requires state rows with immutable producer inputs and country rows with immutable initial values, raw aggregation numerators and denominators, and separate mutable values. Each row must bind to the transition generation. The global commit must cover the exact finalized successor assignment and every included state.

Survival initialization belongs inside the blackout after successor allocation and before player continuation. The live transition does not yet enforce this barrier. The constants file reserves the schema and nine resource identities only. No state or country row trigger, initialization effect, numerical formula, value, or ready flag exists in gameplay code.

## Bounded recurring cost

The recurring reconciliation path performs timeline arithmetic and checks the frozen registry arrays. It does not build a full global candidate pool. The expensive successor-allocation barrier is evaluated only before the initial registry commit. A successful commit prevents that initialization branch from running again.

## Engine references

The installed official documentation is the primary syntax reference:

- `documentation/triggers_documentation.md` documents `all_of` and `all_of_scopes` array validation.
- `documentation/effects_documentation.md` documents `for_each_scope_loop` and `for_loop_effect`.
- `documentation/script_concept_documentation.md` and `common/script_constants/documentation.md` document typed script constants.
- the offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` documents arrays, numeric array indexes, and scope arrays.

Repository precedents are `006_independence_wave_effects.txt` and `006_independence_wave_triggers.txt` for aligned scope registries and reciprocal row validation, plus `020_black_plague_effects.txt` for delayed scheduler state. The Fallout substrate retains separate schema and identifier ownership.

## Fail-closed boundaries

The initialization effects record one owned error for reveal, allocation, or registry failure. Country-row and orientation mismatches fail their eligibility triggers. Future arc, delayed, and bilateral systems must add their own error and cleanup producers before activation. The scheduler does not repair a missing reveal date, substitute a lost bilateral target, invent a survival value, or select an unreviewed successor.

The following work remains blocked or absent:

- Numeric initialization and aggregation rules for Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition are not accepted. Cohesion and Reclamation remain separate mechanics. The full state and country receipt transaction is not implemented.
- The frozen Fallout snapshot currently permits zero-seeded Air Winter fields when the producer is absent. Survival initialization must require an explicit producer-generation receipt or initialize the canonical state row before capture.
- Active arc slots, delayed-result tickets, bilateral reservations, target-loss handling, hidden AI resolution, cleanup recovery, and scheduler debug display are not implemented.
- The five orientation components have receipts but no Fallout orientation event content.
- Literal multiplayer lobby-host identity remains unavailable in the documented script surface. The live authority is the project coordinator.
- No runtime observation was performed. HOI4 was not launched.

These omissions keep both scheduler activation flags unset and keep every reserved living-world event outside the release-floor count.

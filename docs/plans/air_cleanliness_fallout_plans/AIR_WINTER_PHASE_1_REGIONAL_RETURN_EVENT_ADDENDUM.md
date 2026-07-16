# Air Winter Phase 1 Regional Return Event Addendum

## Status

Accepted for implementation after independent transaction and depth review on 16 July 2026.

## Review boundary

This addendum deepens the five existing Phase 1 regional openings in `events/fallout_world_end_events.txt`:

- `chaosx.fallout.1`, boreal and polar
- `chaosx.fallout.2`, maritime and oceanic
- `chaosx.fallout.3`, arid and Mediterranean
- `chaosx.fallout.4`, tropical and equatorial
- `chaosx.fallout.5`, mountain and highland

At review time, the openings each offered two immediate policies. They wrote ten distinct state memories but scheduled no result and provided no consumer for those memories. This tranche converts those policies into ten owner-bound delayed branches and adds one shared result event.

This is Air Winter content. It does not activate the Fallout living-world scheduler and does not count toward the 660-block Fallout release floor.

Hearts of Iron IV will not be launched. Runtime behavior remains unobserved.

## Sources and precedents

Required repository sources:

- `docs/specs/air_cleanliness_fallout_specs/matrices/fallout_winter_visual_state_matrix.md`
- `docs/specs/air_cleanliness_fallout_specs/specs/02_winter_climate_visual_overhaul.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_ARCHITECTURE.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_EVENT_PILOT_DEPTH_REVIEW.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_EVENT_SCHEDULER_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_ID_LEDGER.md`

Required engine references:

- installed `documentation/effects_documentation.md` for delayed `country_event`, timed dynamic modifiers, and event targets
- installed `documentation/triggers_documentation.md` for `count_triggers`
- offline `Data structures - Hearts of Iron 4 Wiki.md` for regular event targets across delayed child events
- offline `Event modding - Hearts of Iron 4 Wiki.md`
- offline `Scopes - Hearts of Iron 4 Wiki.md`
- vanilla delayed country-event calls such as `events/AAT_Denmark.txt`
- vanilla and repository timed state dynamic modifiers

The implementation must reuse the live regular event targets `air_winter_event_country` and `air_winter_event_state`. It must not add a global event target or a new world iterator.

## Event allocation

Allocate `chaosx.fallout.6` as the shared Phase 1 return event.

Suffix `6` was unused at allocation review and is assigned to this return event. Suffixes `100` through `126` remain reserved for the Fallout living-world foundation. Existing event ids are not renumbered.

The event must remain in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

## Opening contract

Each option in events 1 through 5 must:

1. revalidate the country and state targets at click time
2. revalidate any option-specific building or resource condition
3. clear older Phase 1 policy and result memory for the same state and country
4. clear every Phase 1 pending branch
5. apply the approved opening cost and ledger changes
6. write exactly one Phase 1 branch flag
7. preserve the existing regional policy memory on the state
8. write the same policy memory on the country
9. refresh the state so the shared pending-owner row binds
10. refresh the 46-day country cooldown
11. schedule event 6 after the existing 21-day short delay

At least one option must remain executable for every valid opening.

Add `air_winter_event_phase_1_opening_targets_are_valid`. It requires the existing country and state target proof and rejects any state that already has the generic pending flag or any pending Air Winter branch. Events 1 through 5 use it in their event triggers and option display gates. Every option repeats it at click time. A stale click routes through a dedicated `air_winter_event_reject_stale_opening_choice` effect and event 203. The opening-only rejection effect must never clear a generic pending row, branch flag, pending owner, or saved target because the state may already hold a newer transaction belonging to the same country. This prevents an old popup from attaching a Phase 1 branch beside a newer delayed family, adopting an orphaned generic row, or destroying the newer chain.

The boreal thermometer schedule replaces its pre-tranche minor Command Power deduction with a minor Stability loss. That consequence does not require an affordability gate and keeps the regional fallback executable when the state has no operational factory. The full-shift alternative remains conditional on operational industry.

The following choices receive exact extra eligibility:

- boreal full shifts require at least one operational civilian or military factory
- maritime shipyard priority requires an operational dockyard or naval base
- tropical drainage requires the existing moderate Manpower payment to be affordable
- highland route markers require operational infrastructure or railway and the existing minor Command Power payment to be affordable

The alternative choice in each affected opening remains available without that extra gate.

Each opening tooltip must disclose that a return arrives after 21 days and state the exact live success gate for its branch. Operational port and operational transport checks must be shared scripted triggers reused by opening eligibility, AI projection, and result evaluation.

## Branch ledger

The ten pending state branches are:

| Opening | Policy branch |
| --- | --- |
| boreal | thermometer shift network |
| boreal | full production shifts |
| maritime | warehouse shelter rooms |
| maritime | shipyard coal priority |
| arid | cistern rationing |
| arid | open fountains |
| tropical | field drainage |
| tropical | school shelters |
| highland | marked corridor |
| highland | recalled road crews |

One shared trigger must prove exact cardinality. It requires `count_triggers` with an amount of one and rejects `count_triggers` with an amount of two. The official trigger treats the amount as a minimum, so the second test catches every payload with two or more branches. A separate malformed-branch trigger uses the amount of two directly for reconciliation.

The result validator must independently require:

- valid regular country and state event targets
- the generic pending delayed-result flag
- the pending-owner variable
- equality between the pending owner and the saved event country
- current ownership by that pending owner
- exactly one Phase 1 branch

If a Phase 1 branch exists without the generic pending flag, if multiple Phase 1 branches exist, if ownership changes, or if the generic row loses its branch, the existing monthly reconciliation path must clear the transaction.

## Outcome tuning

Add one script-constant group for Phase 1 return thresholds and their exact pre-choice AI projections.

| Branch | Success test after the opening | Pre-choice AI projection |
| --- | --- | --- |
| thermometer shifts | Adaptation at least 18, Exposure no higher than 45 | Adaptation at least 14, Exposure no higher than 45 |
| full shifts | an operational civilian or military factory remains, Adaptation at least 15, Exposure no higher than 45, Disease no higher than 35, Building Damage Pressure no higher than 45 | operational industry, Adaptation at least 15, Exposure no higher than 43, Disease no higher than 34, pressure no higher than 37 |
| warehouse rooms | Shelter at least 20, Disease no higher than 35 | Shelter at least 16, Disease no higher than 35 |
| shipyard priority | an operational port remains, Reclamation at least 18, Exposure no higher than 45 | operational port, Reclamation at least 18, Exposure no higher than 43 |
| cistern rationing | Water at least 30, Disease no higher than 35 | Water at least 22, Disease no higher than 35 |
| open fountains | Water at least 20, Disease no higher than 35 | Water at least 25, Disease no higher than 33 |
| field drainage | Food at least 45, Building Damage Pressure no higher than 45 | Food at least 41, pressure no higher than 37 |
| school shelters | Shelter at least 25, Disease no higher than 35 | Shelter at least 19, Disease no higher than 34 |
| marked corridor | operational transport remains, Adaptation at least 18, Reclamation at least 18, Exposure no higher than 45 | operational transport, Adaptation at least 14, Reclamation at least 14, Exposure no higher than 46 |
| recalled crews | Shelter at least 20, Adaptation at least 8, Building Damage Pressure no higher than 45 | Shelter at least 16, Adaptation at least 10, pressure no higher than 30 |

Each failure predicate is the explicit complement of its success predicate. The ten branches therefore partition into exactly twenty possible visible results.

## Result design

Event 6 uses conditional regional titles, descriptions, option names, and tooltips. Every description names the local institution, physical failure or achievement, and government authority receiving the report.

### Boreal results

Thermometer shift success:

- raise Adaptation by 2
- lower Exposure by 1
- raise national Stability by 0.5 percent
- record Phase 1 success

Thermometer shift failure:

- lower Adaptation by 2
- raise Exposure by 2
- lower national Stability by 0.5 percent
- record Phase 1 failure

Full-shift success:

- raise Reclamation by 2
- lower Building Damage Pressure by 8
- raise national War Support by 0.5 percent
- record Phase 1 success

Full-shift failure:

- raise Exposure by 3
- raise Disease by 2
- raise Building Damage Pressure by 15
- apply the minor Phase 1 Deaths request
- apply a 21-day local factory-access disruption
- lower national Stability by 0.5 percent
- record failure and casualties

### Maritime results

Warehouse-room success:

- raise Shelter by 2
- lower Disease by 1
- lower Refugee Pressure by 2
- raise national Stability by 0.5 percent
- record Phase 1 success

Warehouse-room failure:

- lower Shelter by 2
- raise Disease by 2
- raise Refugee Pressure by 2
- lower national Stability by 0.5 percent
- record Phase 1 failure

Shipyard-priority success:

- raise Food by 2
- raise Reclamation by 2
- lower Building Damage Pressure by 8
- raise national War Support by 0.5 percent
- record Phase 1 success

Shipyard-priority failure:

- raise Exposure by 3
- raise Building Damage Pressure by 15
- apply the minor Phase 1 Deaths request
- apply a 21-day local supply disruption
- lower national War Support by 0.5 percent
- record failure and casualties

### Arid results

Cistern-rationing success:

- raise Water by 2
- lower Disease by 1
- raise Reclamation by 2
- raise national Stability by 0.5 percent
- record Phase 1 success

Cistern-rationing failure:

- lower Water by 2
- raise Disease by 2
- raise Refugee Pressure by 2
- lower national Stability by 0.5 percent
- record Phase 1 failure

Open-fountain success:

- raise Water by 2
- raise Reclamation by 2
- raise national Stability by 0.5 percent
- record Phase 1 success

Open-fountain failure:

- lower Water by 5
- raise Disease by 4
- raise Exposure by 2
- apply the minor Phase 1 Deaths request
- apply a 21-day local supply disruption
- lower national Stability by 1 percent
- record failure and casualties

### Tropical results

Drainage success:

- raise Food by 2
- raise Reclamation by 2
- lower Building Damage Pressure by 8
- raise national Stability by 0.5 percent
- record Phase 1 success

Drainage failure:

- lower Food by 4
- raise Disease by 2
- raise Building Damage Pressure by 15
- apply the minor Phase 1 Deaths request
- apply a 21-day local supply disruption
- lower national Stability by 0.5 percent
- record failure and casualties

School-shelter success:

- raise Shelter by 2
- raise Adaptation by 2
- lower Disease by 1
- raise national Stability by 0.5 percent
- record Phase 1 success

School-shelter failure:

- lower Shelter by 2
- raise Disease by 4
- raise Exposure by 2
- apply the minor Phase 1 Deaths request
- lower national Stability by 0.5 percent
- record failure and casualties

### Highland results

Marked-corridor success:

- raise Adaptation by 2
- raise Reclamation by 2
- lower Exposure by 1
- apply a 21-day local supply benefit
- raise national War Support by 0.5 percent
- record Phase 1 success

Marked-corridor failure:

- raise Exposure by 4
- raise Building Damage Pressure by 15
- raise Refugee Pressure by 2
- apply the severe Phase 1 Deaths request
- apply a 21-day local supply penalty
- lower national War Support by 0.5 percent
- record failure and casualties

Recalled-crew success:

- raise Shelter by 2
- lower Exposure by 1
- lower Building Damage Pressure by 8
- raise national Stability by 0.5 percent
- record Phase 1 success

Recalled-crew failure:

- lower Shelter by 2
- raise Exposure by 2
- raise Refugee Pressure by 2
- apply the minor Phase 1 Deaths request
- lower national Stability by 0.5 percent
- record failure and casualties

## Deaths and temporary disruption

Add two centrally tuned Deaths shares:

- minor Phase 1 failure at 0.005 percent of current state civilian population
- severe Phase 1 failure at 0.01 percent of current state civilian population

Every casualty result must call `air_winter_event_apply_deaths`. No event option may directly subtract state population.

Phase 1 must not issue direct building damage. `AIR_WINTER_ARCHITECTURE.md` reserves physical building damage for Phase 3 onward. Early failures may raise Building Damage Pressure and apply one short timed disruption instead.

Add three Phase 1 state modifiers:

- a 10 percent local factory-access penalty for full-shift failure
- a 10 percent local supply penalty for port, water-service, drainage, or corridor failure
- a 5 percent local supply benefit for a successful marked corridor

Each modifier lasts 21 days. Application first removes the other Phase 1 return modifiers so a malformed retry cannot stack them. Full state-memory cleanup removes all three. Generic pending-chain cancellation leaves a resolved result modifier intact because the modifier is applied only after the branch has reached its terminal event.

## AI contract

Every opening option keeps its current base weight and receives:

- a strong modifier when the exact pre-choice projection passes
- a weak modifier when that projection fails
- at least one government or crisis modifier where it expresses a real policy preference

Government weighting should favor coordinated public schedules and shelters for democratic or communist administrations where appropriate, military production and shipyard priority for fascist administrations, and local continuity choices for neutrality. War, Stability, and existing resource pressure may modify a choice only where the option directly addresses that condition.

The result event has one visible option for each success or failure. Its AI choice is deterministic because exactly one result option is available.

## Memory and cleanup

The state retains its existing policy flag and receives exactly one of:

- `air_winter_memory_phase_1_success`
- `air_winter_memory_phase_1_failure`

Casualty-bearing failures additionally receive `air_winter_memory_phase_1_casualties`. The country receives the matching policy, success or failure, and optional casualty flags. All three result flags are cleared before a new Phase 1 result is written. The generic state and country memory clearers must remove every new flag.

Every valid result must:

1. apply the outcome
2. record durable state and country memory
3. clear the exact Phase 1 pending branch
4. refresh the state
5. let shared reconciliation clear the generic pending-owner row

Stale result choices must use `air_winter_event_reject_stale_choice`.

Stale opening choices in events 1 through 5 must use `air_winter_event_reject_stale_opening_choice`. That effect only fires event 203 when Fallout is inactive. It does not call pending-chain cancellation or alter any state transaction data.

## Asset disposition

No new visual or audio asset is required. Event 6 belongs to the existing Phase 1 report family and uses `GFX_report_event_air_winter_phase_1`.

Update the Fallout asset manifest and Air Winter report-event handoff so the Phase 1 report row covers events 1 through 6. The asset remains Fallout-owned. No zombie id, file, asset, audio, sprite, or path may be referenced.

## Documentation and counts

Update:

- `docs/air_cleanliness_winter.md`
- `AIR_WINTER_ARCHITECTURE.md`
- `AIR_WINTER_EVENT_PILOT_DEPTH_REVIEW.md`
- `AIR_WINTER_EVENT_SCHEDULER_PROOF.md`
- `AIR_WINTER_PHASE_1_REGIONAL_RETURN_EVENT_PROOF.md`
- `AIR_WINTER_PHASE_2_DESERT_CITY_EVENT_PROOF.md`
- `AIR_WINTER_PHASE_5_DEAD_CITY_SALVAGE_EVENT_PROOF.md`
- `FALLOUT_EVENT_ID_LEDGER.md`
- `README_IMPLEMENTATION_STATUS.md`
- the report-event manifest and handoff

Every repository sentence that presents the old pilot totals as current must move to the totals below. A tranche proof may retain an older number only when it labels that number as a historical snapshot.

Expected static pilot totals after implementation:

- 52 Air Winter blocks
- 191 options
- 190 effect-bearing options
- 67 delayed-result schedules

The single effect-free option remains the stale-order acknowledgement already documented in event 203.

## Exclusions and blockers

This tranche does not implement or change:

- the numerical Fallout survival formula
- the NZL pilot
- blackout GUI correction
- treaty projects
- intelligence cleanup
- trade simplifications
- active combat pressure
- strategic bombing winter multipliers
- the manual SCN-014 scenario
- any monthly phase coefficient
- any Fallout grading coefficient
- any world iterator
- the Fallout living-world release-floor count

Static inspection cannot prove delayed callback timing, timed-modifier visibility, multiplayer presentation, or save recovery. Those remain runtime observation limits because Hearts of Iron IV will not be launched.

# Air Winter Event Scheduler Proof

## Implemented surface

The Air Winter pilot scheduler has three entry points in `common/scripted_effects/air_cleanliness_winter_event_effects.txt`:

- `air_winter_event_prepare_candidate_cycle` clears the bounded event and island-source arrays, clears old source receipts, and snapshots the documented current engine year before the existing monthly state pass
- `air_winter_schedule_phase_event` evaluates one state during that existing pass, captures durable seasonal observations, records one owner candidate, and records at most one island-refugee source receipt per source owner
- `air_winter_dispatch_phase_events` iterates only the bounded candidate and source-owner arrays after the pass

`air_contamination_monthly_update` calls dispatch before Air Winter finalization. No new state-wide or country-wide periodic scan was added. Seasonal capture occurs before the country cooldown gate, so a transition observed during cooldown remains available for a later cycle.

The scheduler retains the original one-time worsening-phase memories. A country phase remains eligible when its first qualifying month was blocked by cooldown. Generic recovery still requires an actual phase decrease and respects `constant:air_winter_event_runtime.recovery_arc_cap`. A 46-day country cooldown is one day longer than the longest 45-day delayed result. Dispatch applies it before opening the event. Every successful delayed-result choice reapplies it immediately before scheduling the child, so time spent on the opening popup cannot consume the result buffer.

## Calendar snapshot

The cycle opener assigns `global.year` once to `global.air_winter_event_cycle_year`. The installed `dynamic_variables_documentation.md` defines `global.year` as the current year. State capture, candidate validation, regional recurrence, and annual receipts read only the stored snapshot for that cycle.

The validator requires the snapshot to exist and be positive. Reset clears it. No seasonal marker mutation, owner candidate write, or receipt write occurs when the snapshot is absent or invalid.

## Durable seasonal observations

Five state marker families use the same complete base row shape:

- marker flag
- origin year
- origin Air Winter cycle id
- origin owner
- origin presentation class
- frozen candidate score
- typed event id

First frost also stores the typed route subtype because event 13 has an exact Desert City interface and a generic regional interface. The subtype validator accepts `desert_city` only with event 13 and requires `none` for every other first-frost route.

The families are first frost, dark harvest, ash thaw, second winter, and terminal season. Marker reconciliation runs during the existing state pass only after the calendar contract passes. A partial row, transferred row, unclassified row, invalid event id, invalid subtype, impossible year, invalid origin cycle, or already receipted row is cleared without adding another iterator.

Valid prior-year rows remain eligible when their origin year is no later than the current snapshot and the country receipt is earlier than that origin year. This preserves an observation across a cooldown and across a calendar boundary. Each state can hold one row per family.

The exact capture rules and event routes are recorded in `AIR_WINTER_SEASONAL_RECURRENCE_PROOF.md`.

## Deterministic candidate selection

Every selectable event number comes from the typed `air_winter_event_id` script-constant table. Presentation class, state role, shelter, phase, recovery direction, and seasonal family choose the id through ordered conditions. No random effect, random list, MTTH roll, or unordered first-match country search is used.

Within a selected Phase 3 state, route selection checks reactor, hydroelectric, oil or refinery, coal or heavy industry, transport, then clinic and heat. This is state-local routing. Country candidate selection still compares family priority, origin cycle, frozen score, and state id, so a higher-scoring transport state can defeat a reactor state elsewhere in the country. The shared Phase 3 seen flag permits one ordinary Phase 3 identity chain per country.

Within a selected Phase 2 state, an exact highland and capital classifier runs first. An engine island classifier using `is_island_state` or `is_one_state_island` runs next. The exact arid urban classifier then runs before the generic city route. This prevents a mountain capital with an urban state category from being consumed by `chaosx.fallout.11`, prevents an engine-classified island from being consumed by a generic coastal or city route, and prevents an exact Desert City from losing its water-convoy chain to the generic city row. Typed ids freeze the mountain and island identities. Event 13 also freezes `desert_city` or `none` through the ordinary and first-frost candidate paths. A later first-frost dispatch keeps the stored route while its original state and owner remain valid.

The island and exact Desert City routes each add 131 to their normal phase and pressure score. The current state-pressure range ends at 130. Either exact route therefore wins against another ordinary Phase 2 candidate owned by the same country without overtaking a Phase 3 candidate. Ordinary and first-frost capture apply the same route-specific bonus. A generic event 13 row receives no bonus.

Within a selected Phase 5 state, the dead-city salvage classifier runs before the generic city route, low-shelter abandonment route, and archive route. It requires an original `large_city`, `metropolis`, or `megalopolis` category, a persistent Air Winter building-loss receipt, current damaged-building evidence, and owner control. This is a ruined major-city classifier only. It does not read or create the later Fallout `dead_city` grade.

The dead-city route also adds 131 to its normal phase and pressure score. It wins against another ordinary Phase 5 candidate owned by the same country without overtaking a Phase 6 candidate. The shared Phase 5 seen flag still limits ordinary Phase 5 identity content to one chain per country.

Each eligible state calculates a candidate score from phase and pressure. Seasonal rows freeze that score at observation time. The owning country compares candidates in this order:

1. higher typed family priority
2. earlier origin cycle
3. higher frozen score
4. lower numeric state id

The family order is terminal season, ordinary unseen phase, second winter, dark harvest, first frost, ash thaw, and generic recovery. The ordinary and recovery candidates use the current cycle as their origin cycle. This makes the winner independent of state iterator order.

Unclassified presentation states cannot select a phase, recovery, or seasonal event. A missing regional route leaves the phase eligible for another classified state and does not write a seen flag or receipt.

The state pass adds each owner to `global.air_winter_event_candidate_countries` at most once. A partial current-cycle candidate is replaced before lexicographic comparison. It also adds each eligible source owner to `global.air_winter_island_refugee_source_countries` at most once. Each source owner keeps its highest phase and pressure score, with lower state id resolving a tie. Post-pass dispatch validates owner existence, cooldown, current cycle id, positive year snapshot, selected state, selected family, selected priority, typed event id, current ownership, presentation class, origin year, origin cycle, and the winning marker row when a seasonal family is selected.

## Receipt ordering

The five seasonal country receipts store the marker origin year. A receipt is written only inside the final dispatch branch after `air_winter_event_candidate_is_dispatchable` passes. The winning state marker is then cleared, the relevant phase memory is committed when required, the cooldown is applied, and the typed event is fired.

An ordinary worsening-phase event normally writes no seasonal receipt. First frost and dark harvest reuse exact ordinary routes. A validated ordinary dispatch coalesces dark harvest only when the same winning state stores the same typed event id. First-frost coalescing also requires the stored route subtype to match. It writes that marker's origin year and clears that one row. This prevents one physical incident from opening the same authored event twice while preserving unrelated seasonal rows and keeping exact and generic event 13 observations separate. A failed dispatch clears only the transient owner candidate. It does not clear a valid seasonal marker.

Event id 38 defers this commit. Dispatch first selects the highest live foreign source from the bounded source-owner array. No source means no offer, cooldown, seen flag, receipt, marker consumption, or event. A live source freezes a complete offer and opens event 38. Only a positive exact population transfer writes the Phase 2 seen flag and consumes or coalesces the first-frost marker. Stale or empty transfers clear the offer and cooldown while preserving route eligibility.

Second winter has nine additional regional severe-year memories. The first severe observation for a presentation class seeds its year without firing the recurring event. A severe state in a later year can create a marker. The regional severe-year memory advances to the marker origin year only after final second-winter dispatch validation.

## Event dispatch syntax

Dispatch saves the selected country and state as regular event targets. A `meta_effect` injects the typed numeric id into `chaosx.fallout.[AIR_WINTER_EVENT_ID]`.

The installed `effects_documentation.md` defines `meta_effect` for any scope and provides executable text replacement examples. Current vanilla uses variable localisation replacement inside `meta_effect` in `common/scripted_effects/CZE_scripted_effects.txt`. Air Winter follows that documented surface with a numeric event id.

## Event target lifetime and click-time validation

Before firing an event, dispatch saves:

- `air_winter_event_country`
- `air_winter_event_state`

Event 38 additionally saves:

- `air_winter_refugee_source_country`
- `air_winter_refugee_source_state`

The offline Data structures page states that a regular event target carries into events fired by the same effect chain, including delayed child events. The pilot uses regular targets so simultaneous countries cannot overwrite a shared global target.

Every initial event validates its typed targets before opening. Every effect-bearing option repeats target or response-target validation at click time. All 57 delayed-result schedules call the shared country-cooldown helper or the island commit helper immediately before the child timer begins. A stale click cancels only the matching pending branch or rolls back its uncommitted island offer and opens `chaosx.fallout.203` as a recovery notice. The notice is suppressed during the Fallout transition and active Fallout. It has one effect-free acknowledgement.

Delayed result blocks require their own pending branch flag and the stored original owner. Whenever the generic pending flag exists, `air_winter_event_targets_are_valid` requires a complete owner variable, equality with the saved country target, and current state ownership by that stored owner. Monthly reconciliation cancels a branch when ownership changes or the branch ledger is incomplete. Active Fallout and the Fallout transition also invalidate the target contract. The stored owner uses a regular scope-valued variable and `var:` entry, matching the documented variable-target pattern and the reviewed vanilla ownership precedent.

The dedicated second-winter opening has three weighted choices. Its military-heating choice also checks exact Command Power affordability both when the option is shown and when the click resolves. Its delayed result exposes one of six deterministic outcome options and repeats the exact outcome thresholds inside the click guard.

The dam, refinery, and reactor Phase 3 openings repeat manpower, Command Power, support-equipment, and fuel affordability at click time. Their AI weights combine government and war preferences with derived pre-choice state-ledger thresholds for each delayed success. Reactor emergency pumping also checks the documented country energy ratio and applies a temporary state energy-demand modifier. Its AI uses a separate 60 percent pre-choice energy floor above the 50 percent result threshold, accounting for the route's own local demand increase and later live grid movement.

The fourth Phase 3 infrastructure opening rechecks positive coal or an exact five-case ladder totaling at least four operational military and civilian factories. Full shifts resolve after 30 days against Adaptation 40 and Building Damage Pressure 55. Shutdown conditionally applies 31-day local-factory and coal-output modifiers, then day-30 delivery removes both. Failure damages at most one repairable operational military factory, civilian factory, or infrastructure level and issues no building damage when every target is exhausted. Both opening choices enter Deaths where required, create exactly one furnace branch, refresh state ownership, and refresh the cooldown directly before scheduling. The full-shift AI predicate is the exact pre-choice inverse of the result gate.

The mountain-capital opening repeats manpower and support-equipment affordability at click time. Its AI combines government and war preferences with exact pre-choice ledger boundaries derived from the civic and cellar opening effects. Civic conversion and shared shifts apply temporary state `local_factories` penalties. Five result options expose only the stored branch and deterministic outcome. Successful outcomes write a state memory that reduces the established monthly Air Winter civilian death percentage by 10 percent.

The Phase 2 seed-ledger opening repeats its 1,000-manpower affordability check at click time. Guarded seed plots apply a 10 percent local factory penalty for 46 days. Every valid choice opens one owner-bound branch, refreshes the 46-day country cooldown from the click, and schedules event 18 after 45 days. This preserves the one-day buffer when a human leaves the opening popup unresolved. Seed plots and breeding stock use exact result gates with pre-choice AI boundaries translated through the opening ledger changes. Herd slaughter returns through a fixed depletion result. Five result options expose only the matching branch and conditional outcome. Seed success, seed failure, branch replacement, and generic cancellation all remove the temporary factory modifier.

The Phase 2 island-refugee opening repeats its full offer, source, destination, topology, and affordability checks at click time. Rescue, quarantine, and exclusion request 2 percent, 1 percent, or 0.25 percent of current destination population with ceilings of 40,000, 20,000, or 5,000 people. The exact source-loss helper protects 1,000 people and returns the exact applied loss. Only that positive output is added to the destination. Migration therefore does not create population or enter Deaths. A successful opening writes one exclusive branch, commits the deferred scheduler receipt, refreshes the 46-day cooldown, and schedules event 39 after 30 days. Six result options expose only the matching branch and direct success or inverse failure. Failure casualties use the Deaths system.

The exact Desert City interface of event 13 requires an owner-bound `desert_city` receipt. The generic arid and Mediterranean interface requires that receipt to be completely absent and keeps the original immediate options. Municipal works remain executable without a resource gate. Railway tankers and motor columns repeat exact building and affordability checks when displayed and when clicked. Their three exclusive branches schedule event 49 after 30 days. The result independently proves the pending flag, stored original owner, saved event country, current state owner, exact branch, and one of nine exhaustive success, partial, or failure partitions. Casualties use Deaths. Failure damage checks an operational repairable building target. Timed state modifiers carry municipal factory diversion, supply relief, or supply disruption. Monthly reconciliation cancels a Desert City branch that lacks its pending receipt.

The Phase 5 dead-city opening repeats survey or military affordability and the exact ruined-major-city classifier at click time. Licensed district salvage remains executable without a resource gate. The three choices write exclusive state branches and distinct country and state policy memories. Each schedules event 48 after 30 days. Nine ordinary result predicates partition the three branches into success, partial, and disaster. A tenth altered result replaces only the active branch disaster when final-tier Chaos, a positive active nuclear fallout modifier, and chemical or biological contamination coexist. Result options recheck owner-bound targets, continued control by the original owner, the exclusive branch, and the exact outcome. Casualties use Deaths, equipment grants use fixed equipment types, and failure damage is repairable and conditional on a remaining operational target. Every completed result exhausts the site. The state-control-change on action immediately reconciles a live branch when control changes. Monthly reconciliation remains the ownership and malformed-ledger backstop.

## AI and cleanup

Every non-deterministic player-choice opening has explicit AI weights with state or country conditions. Delayed deterministic results expose only the option matching the stored pending branch and outcome. AI countries therefore use the same mechanical chain without a second visible-only scheduler.

`air_winter_event_clear_state_memory` clears state arc memory, delayed-result memory, island receiver and source memory, Desert City receipt, branch, policy, result, and timed modifiers, seed-ledger memory, infrastructure memory, furnace memory, tunnel-school memory, dead-city salvage memory, and all five complete seasonal marker rows. `air_winter_event_clear_country_memory` clears phase gates, cooldown, recovery count, five annual seasonal receipts, nine regional severe-year memories, island offers, source receipts, migration memory, Desert City policy and result memory, dead-city policy and result memory, candidate subtype data, and the remaining candidate row. Completed delayed results clear their pending flag and stored owner immediately. During Fallout snapshot capture, each state freezes its Air Winter values before the same pass cancels pending branches and removes temporary Desert City waterworks, seed-vault, refinery, reactor, furnace, or tunnel-school modifiers. `air_winter_reset_global` clears the calendar snapshot and bounded island-source array.

## Static validation

Static review establishes:

1. one bounded candidate record per owner per cycle
2. one documented year snapshot per opened cycle
3. cooldown-independent seasonal capture
4. complete marker rows for all five families
5. iterator-order-independent candidate selection
6. one dispatch attempt per candidate owner
7. receipt and marker mutation only after final dispatch validation
8. prior-year carryover only while the family receipt is earlier
9. later-year regional comparison for second winter
10. typed initial-event target validation
11. click-time choice validation
12. delayed-result branch validation
13. ownership-change cleanup
14. candidate cleanup after dispatch
15. complete country, state, and global reset coverage
16. pending-owner validation across all delayed Air Winter branches
17. Fallout snapshot capture before pending-branch cancellation
18. exact Phase 3 infrastructure identity and state-local route precedence, including the coal-or-four-factory ladder
19. exact mountain-capital identity, city-route precedence, and first-frost typed-id retention
20. seed-ledger branch exclusivity, threshold derivation, and delayed cleanup
21. click-time cooldown reanchoring for all 57 delayed-result schedules
22. furnace branch exclusivity, 40 and 55 threshold inverse, day-30 modifier removal, repairable damage exhaustion, and cancellation cleanup
23. exact engine island route precedence for ordinary and first-frost selection
24. one bounded deterministic source receipt per source owner without a new world scan
25. deferred seen and seasonal receipt commit with no-source retry
26. capped balanced source loss and destination gain with no minimum floor
27. three exclusive island policies and six complete delayed-result partitions
28. island offer, branch, receipt, migration-memory, state, country, and global cleanup
29. original major-city category, persistent loss receipt, and current damaged-building proof for the Phase 5 salvage route
30. Phase 5 dead-city route precedence and bounded same-phase score bonus
31. survey, military, and licensed branch exclusivity with nine exhaustive ordinary outcomes
32. narrow mixed-cause altered-result replacement without a Fallout trigger or ordinary radiation claim
33. owner-control cancellation, Deaths routing, concrete equipment grants, conditional repairable damage, and exhausted-site cleanup
34. exact state-control-change reconciliation without a periodic world scan
35. exact arid urban route precedence and bounded same-phase score bonus
36. route-subtype initialization, first-frost persistence, candidate validation, and exact dispatcher receipt
37. subtype-aware first-frost coalescing that separates the exact and generic event 13 routes
38. generic event 13 fallbacks with executable immediate choices and the shared Phase 2 picture
39. three exact Desert City policies and nine exhaustive delayed-result partitions
40. exact payment gates, pending-owner validation, malformed-branch cancellation, Deaths routing, repairable damage, timed supply results, and cleanup
41. literal inverse AI plausibility modifiers for all three Desert City policies

The 51 current Air Winter event blocks have unique `chaosx.fallout` ids and matching localisation. They contain 171 options. One hundred seventy effect-bearing options have click-time target guards, while the remaining stale-order acknowledgement has no effect. This pilot is separate from the Fallout living-world scheduler and does not satisfy the 660-block Fallout release floor. Island source and population proof is in `AIR_WINTER_PHASE_2_ISLAND_REFUGEE_SOURCE_AND_POPULATION_PROOF.md`. Desert City route, result, and dynamic-picture proof is in `AIR_WINTER_PHASE_2_DESERT_CITY_EVENT_PROOF.md`. Seed-ledger proof is in `AIR_WINTER_PHASE_2_SEED_LEDGER_EVENT_PROOF.md`. Dam, refinery, and reactor proof is in `AIR_WINTER_PHASE_3_INFRASTRUCTURE_EVENT_PROOF.md`. Heavy-industry proof is in `AIR_WINTER_PHASE_3_HEAVY_INDUSTRY_EVENT_PROOF.md`. Mountain-capital proof is in `AIR_WINTER_PHASE_2_TUNNEL_SCHOOL_EVENT_PROOF.md`. Dead-city salvage proof is in `AIR_WINTER_PHASE_5_DEAD_CITY_SALVAGE_EVENT_PROOF.md`.

## Unobserved engine boundary

The installed documentation supports the current-year dynamic variable, meta-effect text, scope-valued variables, array iteration, regular event targets, delayed event syntax, state dynamic modifiers, state population reads, positive state `add_manpower`, damaged and non-damaged building-level variables, concrete equipment grants, and repairable building damage. Vanilla also proves conditional event pictures through scripted localisation. A live session has not observed the year snapshot assignment, generated event dispatch, delayed regular-target retention, popup ordering, AI resolution, exact Desert City route and picture selection, subtype persistence, balanced migration readback, dead-city route selection, control-loss reconciliation, modifier arithmetic and expiry, equipment readback, damage repair, annual receipt persistence, or save-resume behavior. HOI4 was not launched. These surfaces are not claimed as runtime proven.

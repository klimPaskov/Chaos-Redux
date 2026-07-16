# Air Winter Event Scheduler Proof

## Implemented surface

The Air Winter pilot scheduler has three entry points in `common/scripted_effects/air_cleanliness_winter_event_effects.txt`:

- `air_winter_event_prepare_candidate_cycle` clears the bounded owner array and snapshots the documented current engine year before the existing monthly state pass
- `air_winter_schedule_phase_event` evaluates one state during that existing pass, captures durable seasonal observations, and records one owner candidate
- `air_winter_dispatch_phase_events` iterates only the bounded owner array after the pass

`air_contamination_monthly_update` calls dispatch before Air Winter finalization. No new state-wide or country-wide periodic scan was added. Seasonal capture occurs before the country cooldown gate, so a transition observed during cooldown remains available for a later cycle.

The scheduler retains the original one-time worsening-phase memories. A country phase remains eligible when its first qualifying month was blocked by cooldown. Generic recovery still requires an actual phase decrease and respects `constant:air_winter_event_runtime.recovery_arc_cap`. A 46-day country cooldown is one day longer than the longest 45-day delayed result.

## Calendar snapshot

The cycle opener assigns `global.year` once to `global.air_winter_event_cycle_year`. The installed `dynamic_variables_documentation.md` defines `global.year` as the current year. State capture, candidate validation, regional recurrence, and annual receipts read only the stored snapshot for that cycle.

The validator requires the snapshot to exist and be positive. Reset clears it. No seasonal marker mutation, owner candidate write, or receipt write occurs when the snapshot is absent or invalid.

## Durable seasonal observations

Five state marker families use the same complete row shape:

- marker flag
- origin year
- origin Air Winter cycle id
- origin owner
- origin presentation class
- frozen candidate score
- typed event id

The families are first frost, dark harvest, ash thaw, second winter, and terminal season. Marker reconciliation runs during the existing state pass only after the calendar contract passes. A partial row, transferred row, unclassified row, invalid event id, impossible year, invalid origin cycle, or already receipted row is cleared without adding another iterator.

Valid prior-year rows remain eligible when their origin year is no later than the current snapshot and the country receipt is earlier than that origin year. This preserves an observation across a cooldown and across a calendar boundary. Each state can hold one row per family.

The exact capture rules and event routes are recorded in `AIR_WINTER_SEASONAL_RECURRENCE_PROOF.md`.

## Deterministic candidate selection

Every selectable event number comes from the typed `air_winter_event_id` script-constant table. Presentation class, state role, shelter, phase, recovery direction, and seasonal family choose the id through ordered conditions. No random effect, random list, MTTH roll, or unordered first-match country search is used.

Within a selected Phase 3 state, route selection checks reactor, hydroelectric, oil or refinery, transport, then clinic and heat. This is state-local routing. Country candidate selection still compares family priority, origin cycle, frozen score, and state id, so a higher-scoring transport state can defeat a reactor state elsewhere in the country. The shared Phase 3 seen flag permits one ordinary Phase 3 identity chain per country.

Within a selected Phase 2 state, an exact highland and capital classifier runs before the generic city route. This prevents a mountain capital with an urban state category from being consumed by `chaosx.fallout.11`. The typed id `phase_2_mountain_capital` freezes that identity for ordinary and first-frost candidates. A later first-frost dispatch keeps the stored route even if the country moves its capital, while the original state, owner, and highland class must remain valid.

Each eligible state calculates a candidate score from phase and pressure. Seasonal rows freeze that score at observation time. The owning country compares candidates in this order:

1. higher typed family priority
2. earlier origin cycle
3. higher frozen score
4. lower numeric state id

The family order is terminal season, ordinary unseen phase, second winter, dark harvest, first frost, ash thaw, and generic recovery. The ordinary and recovery candidates use the current cycle as their origin cycle. This makes the winner independent of state iterator order.

Unclassified presentation states cannot select a phase, recovery, or seasonal event. A missing regional route leaves the phase eligible for another classified state and does not write a seen flag or receipt.

The state pass adds each owner to `global.air_winter_event_candidate_countries` at most once. A partial current-cycle candidate is replaced before lexicographic comparison. Post-pass dispatch validates owner existence, cooldown, current cycle id, positive year snapshot, selected state, selected family, selected priority, typed event id, current ownership, presentation class, origin year, origin cycle, and the winning marker row when a seasonal family is selected.

## Receipt ordering

The five seasonal country receipts store the marker origin year. A receipt is written only inside the final dispatch branch after `air_winter_event_candidate_is_dispatchable` passes. The winning state marker is then cleared, the relevant phase memory is committed when required, the cooldown is applied, and the typed event is fired.

An ordinary worsening-phase event normally writes no seasonal receipt. First frost and dark harvest reuse exact ordinary routes, so a validated ordinary dispatch coalesces a marker only when the same winning state stores the same typed event id. It writes that marker's origin year and clears that one row. This prevents one physical incident from opening the same authored event twice while preserving unrelated seasonal rows. A failed dispatch clears only the transient owner candidate. It does not clear a valid seasonal marker.

Second winter has nine additional regional severe-year memories. The first severe observation for a presentation class seeds its year without firing the recurring event. A severe state in a later year can create a marker. The regional severe-year memory advances to the marker origin year only after final second-winter dispatch validation.

## Event dispatch syntax

Dispatch saves the selected country and state as regular event targets. A `meta_effect` injects the typed numeric id into `chaosx.fallout.[AIR_WINTER_EVENT_ID]`.

The installed `effects_documentation.md` defines `meta_effect` for any scope and provides executable text replacement examples. Current vanilla uses variable localisation replacement inside `meta_effect` in `common/scripted_effects/CZE_scripted_effects.txt`. Air Winter follows that documented surface with a numeric event id.

## Event target lifetime and click-time validation

Before firing an event, dispatch saves:

- `air_winter_event_country`
- `air_winter_event_state`

The offline Data structures page states that a regular event target carries into events fired by the same effect chain, including delayed child events. The pilot uses regular targets so simultaneous countries cannot overwrite a shared global target.

Every initial event validates both typed targets before opening. Every effect-bearing option repeats target or response-target validation at click time. A stale click cancels only the matching pending branch and opens `chaosx.fallout.203` as a recovery notice. The notice is suppressed during the Fallout transition and active Fallout. It has one effect-free acknowledgement.

Delayed result blocks require their own pending branch flag and the stored original owner. Whenever the generic pending flag exists, `air_winter_event_targets_are_valid` requires a complete owner variable, equality with the saved country target, and current state ownership by that stored owner. Monthly reconciliation cancels a branch when ownership changes or the branch ledger is incomplete. Active Fallout and the Fallout transition also invalidate the target contract. The stored owner uses a regular scope-valued variable and `var:` entry, matching the documented variable-target pattern and the reviewed vanilla ownership precedent.

The dedicated second-winter opening has three weighted choices. Its military-heating choice also checks exact Command Power affordability both when the option is shown and when the click resolves. Its delayed result exposes one of six deterministic outcome options and repeats the exact outcome thresholds inside the click guard.

The three Phase 3 infrastructure openings repeat manpower, Command Power, support-equipment, and fuel affordability at click time. Their AI weights combine government and war preferences with derived pre-choice state-ledger thresholds for each delayed success. Reactor emergency pumping also checks the documented country energy ratio and applies a temporary state energy-demand modifier. Its AI uses a separate 60 percent pre-choice energy floor above the 50 percent result threshold, accounting for the route's own local demand increase and later live grid movement.

The mountain-capital opening repeats manpower and support-equipment affordability at click time. Its AI combines government and war preferences with exact pre-choice ledger boundaries derived from the civic and cellar opening effects. Civic conversion and shared shifts apply temporary state `local_factories` penalties. Five result options expose only the stored branch and deterministic outcome. Successful outcomes write a state memory that reduces the established monthly Air Winter civilian death percentage by 10 percent.

## AI and cleanup

Every non-deterministic player-choice opening has explicit AI weights with state or country conditions. Delayed deterministic results expose only the option matching the stored pending branch and outcome. AI countries therefore use the same mechanical chain without a second visible-only scheduler.

`air_winter_event_clear_state_memory` clears state arc memory, delayed-result memory, infrastructure memory, tunnel-school memory, and all five complete seasonal marker rows. `air_winter_event_clear_country_memory` clears phase gates, cooldown, recovery count, five annual seasonal receipts, nine regional severe-year memories, and candidate data. Completed delayed results clear their pending flag and stored owner immediately. During Fallout snapshot capture, each state freezes its Air Winter values before the same pass cancels pending branches and removes temporary refinery, reactor, or tunnel-school modifiers. `air_winter_reset_global` clears the calendar snapshot.

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
18. exact Phase 3 infrastructure identity and state-local route precedence
19. exact mountain-capital identity, city-route precedence, and first-frost typed-id retention

The 43 current Air Winter event blocks have unique `chaosx.fallout` ids and matching localisation. They contain 127 options. One hundred twenty-six effect-bearing options have click-time target guards, while the remaining stale-order acknowledgement has no effect. This pilot is separate from the Fallout living-world scheduler and does not satisfy the 660-block Fallout release floor. Infrastructure-specific proof is in `AIR_WINTER_PHASE_3_INFRASTRUCTURE_EVENT_PROOF.md`. Mountain-capital proof is in `AIR_WINTER_PHASE_2_TUNNEL_SCHOOL_EVENT_PROOF.md`.

## Unobserved engine boundary

The installed documentation supports the current-year dynamic variable, meta-effect text, scope-valued variables, array iteration, regular event targets, and delayed event syntax. A live session has not observed the year snapshot assignment, generated event dispatch, delayed regular-target retention, popup ordering, AI resolution, annual receipt persistence, or save-resume behavior. HOI4 was not launched. These surfaces are not claimed as runtime proven.

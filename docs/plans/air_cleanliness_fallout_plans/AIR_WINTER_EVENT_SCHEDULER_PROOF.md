# Air Winter Event Scheduler Proof

## Implemented surface

The Air Winter pilot scheduler has three entry points in `common/scripted_effects/air_cleanliness_winter_event_effects.txt`:

- `air_winter_event_prepare_candidate_cycle` clears the bounded owner array before the existing monthly state pass
- `air_winter_schedule_phase_event` evaluates one state during that existing pass and records an owner candidate
- `air_winter_dispatch_phase_events` iterates only the bounded owner array after the pass

`air_contamination_monthly_update` calls dispatch before Air Winter finalization. No new state-wide or country-wide periodic scan was added.

The scheduler tracks one country flag for each worsening phase. A country phase remains eligible when its first qualifying month was blocked by cooldown. Recovery requires an actual phase decrease and respects `constant:air_winter_event_runtime.recovery_arc_cap`. A 46-day country cooldown is one day longer than the longest 45-day delayed result.

## Deterministic candidate selection

Every selectable event number comes from the typed `air_winter_event_id` script-constant table. Presentation class, state role, shelter, phase, and recovery direction choose the id through ordered conditions. No random effect, random list, MTTH roll, or unordered first-match country search is used.

Each eligible state calculates a candidate score from phase and pressure. Recovery uses its own typed base. The owning country keeps the higher score. Equal scores select the lower numeric state id. This makes the selected state independent of `every_state` iterator order.

Unclassified presentation states cannot select a phase or recovery event. A missing regional route leaves the phase eligible for another classified state and does not write a seen flag.

The state pass adds each owner to `global.air_winter_event_candidate_countries` at most once. Post-pass dispatch validates owner existence, cooldown, current cycle id, selected state, selected event id, and current ownership. It writes the phase seen flag or recovery count only after those checks pass.

## Event dispatch syntax

Dispatch saves the selected country and state as regular event targets. A `meta_effect` injects the typed numeric id into `chaosx.fallout.[AIR_WINTER_EVENT_ID]`.

The installed `effects_documentation.md` defines `meta_effect` for any scope and provides executable text replacement examples. Current vanilla uses variable localisation replacement inside `meta_effect` in `common/scripted_effects/CZE_scripted_effects.txt`. Air Winter follows that documented surface with a numeric event id.

## Event target lifetime and click-time validation

Before firing an event, dispatch saves:

- `air_winter_event_country`
- `air_winter_event_state`

The offline Data structures page states that a regular event target carries into events fired by the same effect chain, including delayed child events. The pilot uses regular targets so simultaneous countries cannot overwrite a shared global target.

Every initial event validates both typed targets before opening. Every visible option repeats ownership and target validation at click time. A stale click calls `air_winter_event_reject_stale_choice`, which cancels only the matching pending branch and opens `chaosx.fallout.203` as a recovery notice.

Delayed result blocks require their own pending branch flag and the stored original owner. Monthly reconciliation cancels a branch when ownership changes or the branch ledger is incomplete. The stored owner uses a regular scope-valued variable and `var:` entry, matching the documented variable-target pattern and the reviewed vanilla ownership precedent.

## AI and cleanup

Every player-choice block has explicit AI weights with state or country conditions. AI countries resolve ordinary country events without a separate visible-only scheduler.

Result blocks expose only the option matching the stored pending branch or deterministic outcome. Eighty-five event options have click-time guards. Twenty-nine delayed-result branches validate their pending state before applying effects.

`air_winter_event_clear_state_memory` clears state arc and delayed-result memory on state reset. `air_winter_event_clear_country_memory` clears phase gates, cooldown, recovery count, and candidate data only in country scope. Completed delayed results clear their pending flag and stored owner immediately.

## Static validation

Static review establishes:

1. one candidate record per owner per cycle
2. score-first and lowest-state-id tie resolution
3. one dispatch attempt per candidate owner
4. no phase memory before successful dispatch validation
5. typed initial-event target validation
6. click-time choice validation
7. delayed-result branch validation
8. ownership-change cleanup
9. candidate cleanup after dispatch
10. country and state reset cleanup

The 33 current Air Winter event blocks have unique `chaosx.fallout` ids and matching localisation. This pilot is separate from the future Fallout living-world scheduler and does not satisfy the 660-block Fallout release floor.

## Unobserved engine boundary

The installed documentation supports the meta-effect text, scope-valued variables, array iteration, regular event targets, and delayed event syntax. A live session has not observed generated event dispatch, delayed regular-target retention, popup ordering, or save-resume behavior. HOI4 was not launched. These surfaces are not claimed as runtime proven.

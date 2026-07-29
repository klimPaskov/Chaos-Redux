# Air Winter Monthly Determinism Proof

## Status

The monthly Air Winter pipeline is statically deterministic for an unchanged save state. It uses one monotonic cycle id, one opening global snapshot, one existing world-state pass, explicit per-state cycle guards, deterministic post-pass selection, and one guarded finalization. HOI4 was not launched, so iterator execution and save-resume behavior are not runtime observations.

## Entry ownership

`air_contamination_monthly_update` in `common/scripted_effects/chaos_meter_effects.txt` is the only periodic owner. The existing host-authority trigger gates that entry before Air Winter begins. No Air Winter daily, weekly, or monthly on-action was added.

The live order is:

1. prepare the capped natural-source contamination ledger
2. prepare the regional visual schema, open the Air Winter cycle, and snapshot completed contamination inputs
3. run the existing `every_state` pass
4. update each state once, reconcile response designations, refresh its regional ordinary-map entities, and register bounded country candidates
5. rebuild evacuation quotes from the bounded priority-owner array
6. dispatch phase events from the bounded event-owner array
7. finalize global Air Winter aggregates

When `fallout_transition_active` is set, steps 2, 4, 5, 6, and 7 are skipped for Air Winter. This keeps the Fallout snapshot stable through its multi-event rewrite without adding a second state iterator. The permanent lock supplies a fixed 9,900-basis-point Fallout source and zeros all competing inputs. Air Winter resumes through its normal next monthly cycle after the transition flag clears.

## Opening snapshot

`air_winter_begin_monthly_cycle` compares `global.air_winter_last_prepare_date` with `global.date`. A new date increments `global.air_winter_cycle_id` exactly once and opens `air_winter_cycle_open`.

The helper copies these prior completed-pass inputs before the current world pass resets and rebuilds them:

- `global.air_contamination_bp`
- `global.air_contamination_last_delta_bp`
- `global.air_contamination_chem_states`
- `global.air_contamination_fallout_states`

Pressure and recovery calculations read the copied values. A state processed early in the current iterator cannot change the global input seen by a later state.

The begin helper also clears the two bounded post-pass arrays:

- `global.air_winter_event_candidate_countries`
- `global.air_winter_evacuation_cache_countries`

## One update per state

`air_winter_update_state` requires an open cycle and the current cycle id. A state runs its update only when `air_winter_last_update_cycle_id` does not equal `global.air_winter_cycle_id`. Both valid and suspended states write the current cycle id after their branch.

Calling the state helper twice in one open cycle therefore cannot apply a second phase change, death transaction, building loss, category loss, disease update, event candidate, or aggregate contribution.

## Neighbor snapshot rule

Severe-neighbor pressure uses `air_winter_was_severe_at_cycle_start`.

- A neighbor already processed in the current cycle exposes `air_winter_previous_phase`.
- A neighbor not yet processed exposes its current `air_winter_phase`.

Both values describe that neighbor at cycle opening. State iterator order therefore cannot change the adjacency result.

## Deterministic event candidate rule

Each eligible state derives a typed event id from phase, presentation class, state role, shelter, and recovery direction. It computes a numeric candidate score. The owning country keeps the higher score. Equal scores select the lower numeric state id.

The world pass adds each owner to the global candidate array at most once. Post-pass dispatch validates the current cycle, selected state, selected event id, ownership, and cooldown before firing. Dispatch order may follow array insertion order, but each country result is independent and its selected state and event do not depend on that order.

## Deterministic evacuation quote rule

Only states carrying the live response-priority designation register their owner in the evacuation cache array. The post-pass quote helper enters each owner's priority state and selects the lowest numeric id among valid reception states.

Population, resource, stability, and pressure values use script constants and state variables. No random effect or unordered first-match result determines the quote. The quote stores the current cycle id and is invalid outside that cycle.

## Finalization guard

`air_winter_finalize_monthly_cycle` requires:

- `air_winter_cycle_open`
- the current prepare date
- a cycle id different from `global.air_winter_last_finalize_cycle_id`

It calculates severe-state share, updates active, severe, terminal, and classification flags, records the finalized cycle, and closes the cycle. A repeated call cannot finalize the same cycle twice.

## Cleanup and save recovery

State reset clears `air_winter_last_update_cycle_id`. Global reset clears snapshots, prepare and finalize dates, transient candidate arrays, and the open-cycle flag. It deliberately preserves the monotonic cycle id so stale state stamps cannot collide with a restarted cycle. Countries previously registered from the existing state pass are reset through a bounded persistent array, including country scopes whose tags are absent from the map. State cleanup is requested for the next existing monthly state pass, then finalize clears the request after every state has received the reset branch. The legacy ordinary-map proof entity has a dedicated destroy helper. Regional slots are destroyed by the deferred state reset without adding another world iterator.

On a normal loaded save, persistent cycle variables retain the last completed ownership state. The next host monthly call opens a new cycle only for a new `global.date`. This is static script reasoning without a live observation claim.

## Engine references

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` for variables, temporary variables, scope values, and arrays
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` for ROOT, PREV, THIS, OWNER, and nested scope chains
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md` for periodic iteration behavior
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` for `for_each_scope_loop`, array operations, variable effects, and event firing
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md` for `global.date`, `state_population_k`, and state identifiers

## Static conclusion

The implemented pipeline removes the two known iterator-order dependencies: neighbor phase reads and same-country event candidate selection. It also prevents duplicate state work and duplicate finalization within one cycle. No additional periodic world scan was introduced.

Live repetition across save and reload is a later user validation handoff and is not a completion requirement for this static implementation tranche.

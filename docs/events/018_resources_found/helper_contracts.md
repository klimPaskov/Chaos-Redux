# Event 018 helper contracts

This reference records the reusable script boundaries used by the resource-field and Oth-Kesh systems. State records are authoritative for physical fields and anchors; country records are authoritative for UI selection, scheduling, cave capacity, and terminal verification.

## Field ledger and selection

### `resources_found_prepare_random_event_fire`

- Scope: country.
- Inputs: an eligible ordinary country and the current evolution settings.
- Outputs: regular event targets `resources_found_prefire_owner` and `resources_found_prefire_state`, plus temporary `resources_found_prefire_ready`.
- Side effects: none on the map. It chooses either a valid new state or an eligible existing field and never rerolls after the event opens.
- Callers: the generic random-event dispatcher and direct-fire entry protection.

### `resources_found_initialize_field_record`

- Scope: state.
- Inputs: an owned-and-controlled valid state with no active field.
- Outputs: stable field sequence, owner/controller/discoverer pointers, six zeroed Event 018 ledgers, field values, maxima, lifecycle stages, and owner registry membership.
- Side effects: acquires and releases the state transaction lock; it adds no resources by itself.

### `resources_found_add_random_standard_resource_roll_unlocked`

- Scope: state while the field transaction lock is held.
- Inputs: temporary `resources_found_roll_min` and exclusive `resources_found_roll_max`.
- Outputs: one uniform resource id from oil, aluminium, rubber, tungsten, steel, or chromium and one integer amount in the requested range.
- Side effects: adds the resource to the state and the matching Event 018 ledger, records the last roll, and increments the roll count. Duplicate resources deliberately stack.

### `resources_found_refresh_field_record`

- Scope: state.
- Inputs: the current physical ledger and lifecycle values.
- Outputs: total Event 018 addition, current state-resource total, distinct-resource count, compound/global significance flags, clamped field values, historical maxima, project scale factors, exploitation score, and AI evaluation weights.
- Side effects: none outside the field record and its dynamic modifier presentation.

### `resources_found_validate_country_field_selection`

- Scope: country.
- Inputs: the owned-field array and optional selected-field pointer.
- Outputs: one valid owned active selected field when available.
- Side effects: clears an invalid pointer and selects a replacement without changing any physical field.

### `resources_found_gui_toggle_closed_history` and `resources_found_gui_has_closed_field_history`

- Scope: country.
- Inputs: `resources_found_last_closed_field`, the exact-seal marker pair on that state, and the optional history-view flag.
- Outputs: a presentation-only switch between the current active selection and the most recent exact-seal record.
- Side effects: none on the active field registry or gameplay selection. The closed pointer cannot satisfy active-field or discovery triggers.

### `resources_found_refresh_closed_field_identity`

- Scope: permanently closed state.
- Inputs: current `OWNER` and `CONTROLLER` after a control or peace-conference ownership change.
- Outputs: refreshed recorded owner/controller identities for the history panel.
- Side effects: does not reactivate the state, restore a ledger, or register it with a new owner.

## Lifecycle, diplomacy, and transfer

### Canonical closure project launchers

- Scope: country (`resources_found_start_partial_closure_project`, `resources_found_start_full_seal_project`, and `resources_found_start_emergency_seal_project`).
- Inputs: the valid selected field, the matching cost-preview row, the shared project queue, and the profile's dynamic duration/cost context.
- Outputs: one exact payment, one locked active-project field, the physical partial/full closing state, and one containment mission with one timeout or cancellation callback.
- Side effects: emergency identity is set only after launch succeeds. Event `.59`, `.70`, and `.72` options occur inside another callback and therefore record nonblocking follow-up intent instead of starting or paying a second mission.

### `resources_found_fail_selected_field_project`

- Scope: country with an immutable active-project field pointer.
- Inputs: active kind and locked state, including contexts where owner or controller has been lost.
- Outputs: one failed-seal fact for seal kinds and cleared decision-project, partial/full/emergency, requirements, and closing flags on the locked state.
- Side effects: Event `.72` is shown only when an owner-facing selected-field context remains valid; cleanup does not depend on that event being displayable.

### `resources_found_score_foreign_interest_candidate`

- Scope: one valid foreign country inside the invite-bids scan.
- Inputs: regular event targets `resources_found_foreign_interest_owner_target` and `resources_found_foreign_interest_field_target`, optional existing-partner target, and a caller-initialized unscoped `resources_found_foreign_interest_score` temporary variable.
- Outputs: the same temporary score after resource-specific deficit, imports, industrial consumption, domestic extraction, route, opinion, claim, partner rivalry, war, major, factory, and overextension factors.
- Side effects: none. It creates no persistent variables, flags, or targets.

### `resources_found_select_foreign_interest_actor`

- Scope: the field owner when Invite Strategic Bids completes.
- Inputs: one valid selected field that is active, open, unconverted, and outside a field transaction. Tuning comes from `resources_found_foreign_interest_score` in `common/script_constants/018_resources_found_foreign_interest_constants.txt`.
- Outputs: regular owner, field, and best-candidate event targets during the effect chain. A qualifying winner receives `resources_found_foreign_field_actor` plus persistent owner and field pointers.
- Side effects: performs one `every_country` scan at bid completion. It computes the field and owner components once, rejects invalid, capitulated, and war-enemy candidates, keeps the highest score at or above the minimum, and refreshes only the winner's decision-cost previews. It creates no on-action or periodic loop.
- Tie behavior: equal qualifying scores keep the first country in deterministic iteration order.
- Callers: the Invite Strategic Bids project-completion branch in `resources_found_complete_selected_field_project`.

### `resources_found_suspend_field` / `resources_found_resume_field`

- Scope: state.
- Inputs: active-field validity, owner control, transaction state, and the minimum suspension release date.
- Outputs: reversible suspension flags, elapsed suspension history, yield clamp, and refreshed AI values. Suspension idempotently finalizes and clears a live maximum-extraction interval before recording its own start date. Resumption opens a fresh interval only when Maximum Shifts remains the durable posture.
- Side effects: pauses an active contract for explicit review; it never changes the six ledgers.

### `resources_found_complete_full_seal`

- Scope: state.
- Inputs: an active suspended field, completed seal requirements, owner control, and a reversible six-resource ledger.
- Outputs: the six sealed historical amounts, permanent closure, exact-reversal evidence, Evolution IV prevention, owner-registry removal, and closure date.
- Side effects: subtracts exactly each Event 018 ledger from the matching state resource, removes engine resource rights and DMZ state, clears field diplomacy/incidents, and zeroes only Event 018 ledgers. It fires no retaliation or cave callback.

### `resources_found_handle_field_ownership_transfer`

- Scope: state after ownership has changed.
- Inputs: the stored former owner and the engine's current owner/controller.
- Outputs: migrated owner registry, new owner/controller record, transfer date/count, and contract-review state.
- Side effects: removes the former engine resource-rights relationship before rebinding. It preserves physical resources, six ledgers, damage, pressure, and field history.

### `resources_found_remove_field_resource_rights`

- Scope: state.
- Inputs: stored contract, concession, or review partner pointers.
- Outputs: none.
- Side effects: removes engine resource rights for every valid stored partner. Closure, expiry, transfer, occupation cancellation, and cave conversion call it before clearing relationship variables.

### `resources_found_schedule_evolution_paths`

- Scope: country.
- Inputs: enabled evolution settings and the country's owned active fields.
- Outputs: independent state pointers and duration variables for all eight Evolution I-IV pre-fire/active clocks.
- Side effects: starts only eligible mission clocks. Per-path served flags distribute clocks across multiple fields; cancel or timeout queues a one-day reschedule after the old mission has left the decision system.

## Incidents and shared population loss

### `resources_found_apply_incident_civilian_loss`

- Scope: state.
- Inputs: temporary `resources_found_incident_base_loss` and `resources_found_incident_population_factor`, plus the field's safety, disturbance, breach, evacuation, and concealment evidence.
- Outputs: exact state civilian loss and field-death history.
- Side effects: calls the shared `apply_exact_state_civilian_population_loss` helper and records Deaths cause 16 when Deaths presentation is enabled. The same population reduction occurs when that presentation is disabled.

### `resources_found_record_evolution_*_from_field`

- Scope: state.
- Inputs: stable field sequence, actor, state, resource summary, and evolution stage.
- Outputs: one Event Details evolution payload tied to Event 018.
- Side effects: records only an evolution that actually begins; scheduling alone does not write history.

## Cave origin, capacity, and warfare

### `resources_found_calculate_cave_starting_strength`

- Scope: the emerging field state.
- Inputs: resource ledgers, discoveries, maxima, exploitation, deaths, sealing, safety, suspension, evacuation, and hunt evidence.
- Outputs: a starting score and 6-30 division allocation copied to DHO.
- Side effects: none on ownership or units. The emergence helper consumes the result after the former owner's continuation choice.

### `resources_found_refresh_captured_state_capacity`

- Scope: state.
- Inputs: current oil, aluminium, rubber, tungsten, steel, and chromium.
- Outputs: `floor(total / 10)` capacity capped at 10, plus the source total and refresh date.
- Side effects: a cave-origin state always outputs zero future capacity. Prepared denial does not make a state permanently ineligible. A successful activation consumes its named three-capacity penalty once and clamps the result at zero.

### `resources_found_cave_begin_anchor_activation`

- Scope: a DHO-controlled non-origin state.
- Inputs: positive capacity, uninterrupted control, and no active/activating anchor.
- Outputs: a 30-day activation date and DHO anchor-array membership.
- Side effects: applies the visible activating modifier. Recapture or denial interrupts the window.

### `resources_found_cave_daily_pulse`

- Scope: DHO through `on_daily_DHO` only.
- Inputs: DHO's bounded anchor array, capacity, cooldown, neighbor frontier, and terminal verification state.
- Outputs: activated/restored/expired anchors, one sequential replacement spawn when below capacity, Unfed status, newly adjacent wars, and completed or cancelled terminal verification. Successful verification unlocks the final focus and notice; the daily pulse never executes World End.
- Side effects: never iterates every country. Geographic full-state scans occur only at explicit milestones and state-change reconciliation.

### Cave objective target helpers

- Scope: DHO, with persistent state-scope variables.
- Inputs: land-reachable enemy resource states, fortified states, and non-DHO-controlled capitals on the stored origin continent. The Burrow target family is stricter: an active nondisrupted anchor must border a defended enemy capital, supply hub, or level-3 fortified state.
- Outputs: independent `resources_found_rich_target_state`, `resources_found_strongpoint_target_state`, and `resources_found_transport_target_state` pointers plus their matching map flags. The rich pointer is the deterministic maximum total standard-resource value among land-reachable enemy states, with the first stable iteration entry winning an exact tie. The continent scan marks current capital objectives separately.
- Side effects: selecting a new target clears only the prior target in the same family. Burrow preparation also snapshots `resources_found_burrow_objective_defended_at_start`, starts a 90-day mission, and clears the complete live contract on capture, timeout, cancellation, defeat, retarget, or World End. Capturing a marked continental capital records the focus milestone, and terminal defeat clears every remaining pointer and objective marker.

### `resources_found_refresh_active_raiding_brood_formations`

- Scope: DHO.
- Inputs: every currently deployed DHO division and the `cave_scree_tide_brood` battalion identity.
- Outputs: exact `resources_found_active_raiding_brood_formations` count.
- Side effects: none outside the count. The helper runs only at a paid surge start or an exact state/capitulation completion check; it is not a global country scan.

### Achievement evidence helpers

- `resources_found_record_thirty_from_below_candidate` snapshots the frozen opening army and starting capital for both legal owner and physical controller before the breach transfer.
- `resources_found_clear_burrow_objective_runtime` and `resources_found_cancel_burrow_objective_window` remove the live 90-day target contract without clearing historical success.
- `resources_found_try_complete_hills_begin_to_move` rechecks the same active surge, five different state captures, two different country defeats, three deployed Scree Packs, legal capacity, and pre-World-End state before setting its historical completion flag. Per-attempt marks on each state and defeated country keep recaptures and repeated capitulations idempotent.
- Mature regional-anchor evidence is set only after completed non-origin activation before World End and never on a World-End foothold. Cleanup credits each qualifying state once.

### `resources_found_cave_declare_neighbor_wars`

- Scope: DHO.
- Inputs: every land state adjacent to current DHO control.
- Outputs: wars against each distinct valid owner/controller not already at war, including newly adjacent actors after conquest.
- Side effects: sends a one-time frontier notice to affected ordinary countries.

### `resources_found_complete_anchor_cleanup`

- Scope: a liberated state owned and controlled by an ordinary country.
- Inputs: cave cleanup marker and completed cleanup project.
- Outputs: removed cave flags, capacity variables, DHO core, anchor/origin modifiers, a sealed-field scar, and cleanup contribution evidence.
- Side effects: restores ordinary state use without recreating Event 018 or implying a hidden cave return.

## Terminal verification and defeat

### `resources_found_cave_refresh_continent_progress`

- Scope: DHO.
- Inputs: stored origin continent and the explicit eligible-state trigger.
- Outputs: independent eligible, scanned, owned, controlled, owned-and-controlled, and remaining counts plus quarter/half/three-quarter milestones and current non-DHO-controlled capital objectives.
- Side effects: one-shot state scan on conquest or terminal milestones; it does not run as a global periodic country action.

### `resources_found_start_world_end_verification`

- Scope: DHO.
- Inputs: every eligible origin-continent state owned and controlled, chaos strictly above 1,000, Evolution IV and world-end settings enabled, no active world end, and a valid distant foothold registry.
- Outputs: a continuous 60-day verification date and active marker.
- Side effects: any failed input at expiry cancels the verification rather than relaxing a requirement.

### `resources_found_cave_begin_world_end`

- Scope: DHO exclusively from completion of `DHO_the_world_opens_below` after successful verification.
- Inputs: the complete verification marker and a repeated exact terminal trigger. The verification notice has no caller path to this effect.
- Outputs: shared `world_end`, Event 018 terminal id, World Below cosmetic identity, world-end spirit, faster spawn interval, and resource-weighted footholds on valid non-origin continents. Foothold candidates must be owner-controlled and cannot be the last state of their ordinary owner, so each rupture creates a local front instead of deleting a country.
- Side effects: suspends incompatible fields, clears their diplomacy/incidents, stops incompatible random-faction progression through the shared cleanup, declares new neighbor wars, and presents the dedicated super-event.

### `resources_found_cave_finish_defeat_if_valid`

- Scope: DHO.
- Inputs: the active cave identity, zero controlled states, and no previous defeat cleanup.
- Outputs: permanent containment, cleared threat source/targets/arrays/AI state, cleanup markers on every former origin/anchor/foothold, and regional or global aftermath routing.
- Side effects: global defeat presentation is enabled only by world-end or distant-foothold history, or by full origin-continent consumption sustained for the configured campaign period. A three-quarter milestone alone remains regional and never inherits the global presentation.

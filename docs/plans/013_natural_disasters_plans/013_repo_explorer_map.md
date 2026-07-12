# Event 013 Natural Disasters live repository map

> Superseded discovery snapshot, 2026-07-12: the fresh Event 013 controller, public API, decisions, GUI, assets, cluster, scenario, achievements, reports, news, and super-events described as absent below were implemented afterward. Event 099 is now the narrow dust-family bridge, Event 046 remains inert, and Event 051 remains separate. Use `013_event_completion_final_audit.md` and `docs/events/013_natural_disasters.md` for current implementation evidence.

Date: 2026-07-09
Mode: `chaosx_repo_explorer`, evidence-only mapping
Design source: `docs/specs/013_natural_disasters_specs/`

## Executive finding

Event 013 has no live gameplay implementation to preserve. The tracked entry file is an inert hidden placeholder, Event 013 is absent from the random-event registry and default-enabled allowlist, and all of the former gameplay/UI/localisation files were deleted in commit `dc7044f9` (`Remove natural disasters event`). The fresh implementation should therefore use the accepted specification package and current shared systems, not any historical Event 013 blob.

Two untracked foundation files appeared in the working tree during this mapping pass:

- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`

They are useful new-spec foundations, not tracked baseline. They must be reviewed and coordinated with their current owner before editing. They do not yet implement a controller, impacts, reports, decisions, GUI, log integration, scenario, cluster, achievements, or super-events.

The current related-event boundaries already match the accepted direction:

- Event 046 is an inactive earthquake placeholder.
- Event 099 is an inactive sandstorm placeholder, although Event 070 still calls it in three places.
- Event 051 remains an active separate fire-once Heat Wave event and applies its `heat_wave` idea to every country for two years.
- Whole-earth rupture has no live implementation and belongs only to Event 013 Evolution III.

## Required references consulted

The following offline wiki pages were consulted before repository inspection: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding, Graphical asset modding, Achievement modding, Sound modding, and Music modding.

Relevant vanilla documentation was also consulted, including:

- `documentation/script_concept_documentation.md`
- `documentation/effects_documentation.md`
- `documentation/triggers_documentation.md`
- `common/script_constants/documentation.md`
- `common/decisions/_documentation.md`
- `common/scripted_guis/_documentation.md`
- `common/on_actions/_documentation.md`
- `common/collections/_documentation.md`
- `documentation/script_collection_operator.md`
- `documentation/script_collection_input.md`
- `common/ai_strategy/_documentation.md`

Useful vanilla precedents:

- `events/TOA_Generic_Events.txt`, `south_american_events.13`: earthquake casualties, temporary relief pressure, and a delayed news event.
- `events/GOE_Raj.txt`, `GOE_RAJ_famine.2`: cyclone damage against a stored state followed by delayed chain events.
- `common/decisions/RAJ_GOE.txt`, `common/decisions/categories/RAJ_GOE_decision_categories.txt`, `common/scripted_guis/RAJ_famine_scripted_gui.txt`, and `interface/RAJ_famine.gui`: state-targeted crisis decisions and decision-category GUI.
- `common/scripted_guis/SOV_paranoia_system_scripted_gui.txt`, `common/decisions/categories/SOV_decision_categories.txt`, and `interface/sov_paranoia_system_scripted_gui.gui`: `context_type = decision_category` abnormal-system presentation.
- `interface/alerts.gfx`, `interface/countryconstructionsview.gfx`, and `interface/countrypoliticsview.gfx`: `frameAnimatedSpriteType` construction and repair/glow precedents.

The vanilla disaster events are structural references only. Their flat casualties and simple building damage are not sufficient for the accepted Event 013 design.

## Live state and target ownership

| Surface | Live evidence | Required disposition |
| --- | --- | --- |
| Entry event | `events/013_natural_disasters.txt` contains only hidden triggered-only `chaosx.nr13.1` with no effects. | Replace the placeholder body with the fresh entry controller while retaining the required root id `chaosx.nr13.1`. Add freshly allocated hidden/visible subevents in this file; do not inherit historical subevent numbering merely because the stale art handoff mentions it. |
| Constants | Untracked `common/script_constants/013_natural_disasters_constants.txt` defines event, family, target, severity, sequence, policy, death, damage, aftermath, scenario, abnormal, and old achievement constants. | Review as an in-progress foundation. Add missing target-scoring, vulnerability, family damage, chain chance, AI, log-mode, cleanup, and concurrency tuning. Remove or reconcile duplicate scenario intensity constants and obsolete achievement constants. |
| Triggers | Untracked `common/scripted_triggers/013_natural_disasters_triggers.txt` defines target, evolution, cost, and phase checks. | Review as an in-progress foundation. Replace hardcoded thresholds (`400`, building levels, `0.02`, stability values) with script constants; extend family eligibility, caller legitimacy, state-owner invalidation, active caps, chain gates, and AI value checks. |
| Controller effects | No live `common/scripted_effects/013_natural_disasters_effects.txt`. | Create fresh. This is the owner of season queues, target scoring, family resolution, deaths/damage, reports, aftermath ledgers, evolutions, abnormal paths, cleanup, and public call implementation. |
| Public dynamic API docs | `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` contain no Event 013 API. | Add only the stable public wrapper(s), or document the stable Event 013 effects there, with scope, inputs, defaults, outputs, side effects, and examples. Do not copy `damage_buildings_in_random_states`. |
| State modifiers | No live Event 013 state modifier file. | Create `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt` for family/severity disruption and recovery state. |
| Country ideas | No live Event 013 ideas file. | Create `common/ideas/013_natural_disasters_ideas.txt` only for player-visible country summary pressure; state damage remains in state dynamic modifiers. |
| Decisions | No live Event 013 decisions or category files. | Create `common/decisions/013_natural_disasters_decisions.txt` and `common/decisions/categories/013_natural_disasters_categories.txt`. |
| Abnormal GUI | No live Event 013 GUI, GFX, or scripted GUI. | Create `common/scripted_guis/013_natural_disasters_scripted_gui.txt`, `interface/013_natural_disasters.gui`, and `interface/013_natural_disasters.gfx`. |
| Event-specific scripted localisation | No live Event 013 scripted-localisation file. | Create `common/scripted_localisation/013_natural_disasters_scripted_localisation.txt` for family, state, card, risk, severity, timeline, report, and GUI routing. |
| Event localisation | No live `localisation/english/013_natural_disasters_l_english.yml`. | Create UTF-8 BOM localisation for events, decisions/missions, modifiers/ideas, GUI, evolutions, reports, and tooltips. |
| Event documentation | No live `docs/events/013_natural_disasters.md`. | Create only after implementation wording is stable; document actual behavior and limitations, not the implementation history. |
| On actions | No Event 013 on-action file. | Do not add `on_daily`, `on_weekly`, or `on_monthly`. Delayed events and decision mission timeouts are sufficient for the specified controller. Create `common/on_actions/013_natural_disasters_on_actions.txt` only if a narrow state-control/annex cleanup hook proves necessary. |
| AI strategy | No Event 013 AI strategy file. | Normal AI belongs in event `ai_chance`, decision `ai_will_do`, and scripted triggers/constants. A `common/ai_strategy/013_natural_disasters.txt` file is unnecessary unless implementation later introduces military front behavior. |

Historical path evidence from `dc7044f9` confirms that similarly named files once existed, but their deleted contents are explicitly out of bounds as an implementation base. Reusing clean path names is appropriate; reusing the deleted logic is not.

## Fresh controller and public call contract

### Stable public entry

Use one documented public effect id:

- `natural_disaster_start_sequence = yes`

The caller sets contract variables before the call. A specific family is requested by setting `natural_disaster_call_family`; a weighted random family uses `constant:natural_disaster_family.random`. The public effect should not require a second parallel API.

Recommended exact call variables, aligned with `013_disaster_call_contract.md`:

- `natural_disaster_call_caller_type`
- `natural_disaster_call_caller_event_id`
- `natural_disaster_call_family`
- `natural_disaster_call_target_mode`
- `natural_disaster_call_severity`
- `natural_disaster_call_sequence_mode`
- `natural_disaster_call_news_policy`
- `natural_disaster_call_report_policy`
- `natural_disaster_call_aftermath_policy`
- `natural_disaster_call_chain_policy`
- `natural_disaster_call_death_scale`
- `natural_disaster_call_building_scale`
- `natural_disaster_call_warning_scale`
- `natural_disaster_call_caller_cost_checked`
- `natural_disaster_call_log_mode`

Use regular event targets for caller-provided scopes within a single effect/delayed-event chain:

- `natural_disaster_call_target_country`
- `natural_disaster_call_target_state`
- `natural_disaster_call_anchor_country`

Do not store these as global event targets unless a reference genuinely must outlive the originating chain. Any global target must have an explicit cleanup call.

### Recommended internal helper ids

The implementation file should expose small, testable stages instead of one monolith:

- `natural_disaster_prepare_random_event_fire`
- `natural_disaster_prepare_call_defaults`
- `natural_disaster_validate_call`
- `natural_disaster_select_anchor`
- `natural_disaster_build_sequence`
- `natural_disaster_queue_impact`
- `natural_disaster_schedule_next_impact`
- `natural_disaster_resolve_current_impact`
- `natural_disaster_calculate_vulnerability`
- `natural_disaster_apply_family_damage`
- `natural_disaster_register_civilian_deaths`
- `natural_disaster_schedule_delayed_report`
- `natural_disaster_open_or_refresh_aftermath`
- `natural_disaster_roll_followup_chain`
- `natural_disaster_sync_evolution_unlocks`
- `natural_disaster_record_evolution_stage`
- `natural_disaster_cleanup_impact`
- `natural_disaster_cleanup_sequence`

These are new-spec names, not names recovered from deleted implementation.

### Concurrency requirement

A single global `natural_disaster_current_*` context is unsafe. Event 013 is repeatable, cluster members can overlap, the manual scenario can launch while ordinary aftermath remains open, and delayed reports can arrive after another impact. Persistent queue/ledger data must be keyed by a monotonically increasing sequence id and impact id, with parallel arrays or equivalent state/country-local storage. Temporary variables must remain unscoped.

The controller should prepare the queue before the first impact where practical, but recalculate target validity and vulnerability at impact time. State/country references carried only to a directly delayed child event may use regular event targets; multi-week aftermath state belongs on the affected state/country or in keyed persistent arrays.

## Random-event registration and one-row history

### Registration edits

Edit `common/scripted_effects/chaosx_logic_effects.txt`:

- Add `constant:natural_disaster_event.id` to `global.repeatable_events` in `initialize_event_categories`.
- Do not add Event 013 to `global.fire_once_events` or `global.major_events`.

Edit `common/scripted_triggers/chaosx_settings_triggers.txt`:

- Add Event 013 to `event_log_event_is_reworked_default_enabled` only when the implementation is actually ready.

Edit `common/scripted_effects/chaosx_settings_effects.txt`, helper `fire_event_by_temp_id_no_cluster`:

- Add an Event 013 preflight branch that calls `natural_disaster_prepare_random_event_fire`.
- Set `event_single_fire_allowed = 0` if no valid anchor/target can be prepared. This prevents a false history row for a failed dispatch.
- Preserve caller/scenario context when it has already been supplied.

### One-row invariant

The canonical tracked firing path is:

`fire_event_by_temp_id_no_cluster` -> `chaosx.nr13.1` -> `on_repeatable_event_fired` -> `record_events_log_history_entry`.

Only the entry event goes through that path. Warning events, impacts, reports, news, chain continuations, aftermath reassessments, and abnormal path pulses must be fired directly as Event 013 subevents and must never call `on_repeatable_event_fired`.

This yields one Event 013 history row for one season even when the season schedules many delayed subevents. A Natural Disasters cluster that creates several genuine Event 013 seasons should invoke the canonical dispatcher once per season and therefore create one row per season, exactly as the spec requires.

### History actor

Edit `common/scripted_effects/chaosx_events_log_effects.txt`, helper `events_log_set_default_actor_for_current_event`:

- For Event 013, prefer a valid regular event target such as `natural_disaster_log_actor`/`natural_disaster_call_anchor_country`.
- The affected anchor country is the actor for ordinary and scenario seasons.
- A truly global abnormal season may intentionally set `events_log_default_has_actor = 0` rather than inventing an institution.

Because the dispatcher records history after the entry event dispatch, the Event 013 preflight/entry chain can establish the actor before `record_events_log_history_entry` reads it.

## Delayed impacts and reports

`events/013_natural_disasters.txt` owns all delayed event shells. Keep `.1` as the only random-entry root and reserve fresh, documented subevent ranges before implementation. The old asset handoff's claim that family news uses `.305` through `.328` is historical/stale and must not dictate the new allocation.

Required flow:

1. Entry event validates and stores the planned sequence.
2. First impact is delayed by the configured 2-4 day band.
3. Impact revalidates the state and computes actual casualties/damage.
4. Affected-country report is scheduled 1-2 days later.
5. Report reads the completed impact ledger, not a planned estimate.
6. Next impact/chain is scheduled directly without another Event 013 history call.

The vanilla delayed `country_event = { days = ... random_days = ... }` structure is appropriate. A report cannot rely on one mutable “last impact” variable because another impact may resolve first. Key its data by sequence/impact id or preserve it through a dedicated delayed chain with a non-overwritable ledger.

## Deaths API integration

The correct state-scope API is `chaos_meter_register_state_civilian_deaths_percent` in `common/scripted_effects/chaos_meter_effects.txt`. It:

- calculates absolute deaths from `state_population_k`
- supports multipliers, caps, random ranges, and exact-percent mode
- attributes the target to `OWNER`
- calls `chaos_meter_register_deaths`
- reduces actual state population through `add_manpower`
- updates the global and country Deaths ledgers and UI
- converts configured death growth into Chaos Meter pressure

Event 013 should set, in state scope:

- `chaos_state_deaths_percent`
- optional `chaos_state_deaths_mult`
- optional cap/random override variables
- `chaos_deaths_reason = constant:chaos_meter_deaths_reason.natural_disaster`

Then call `chaos_meter_register_state_civilian_deaths_percent = yes`.

Do not use `modify_state_population_by_percent` or the population branch inside `damage_buildings_in_random_states` for disaster casualties. Those helpers directly change manpower but bypass the shared Deaths ledger.

### New Deaths reason ripple

Add `natural_disaster` to `chaos_meter_deaths_reason` in `common/script_constants/chaos_meter_constants.txt`. A visible, fully aggregated cause also requires coordinated edits to:

- `common/scripted_effects/chaos_meter_effects.txt`: initialize/reset country cause totals, cause switch, unsorted arrays, view array sizing/copying, legacy rebuild copy, and any reason-specific chaos weighting.
- `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt`: cause name and country-tooltip lines.
- `localisation/english/chaosx_chaos_meter_l_english.yml`: player-facing cause and tooltip labels.

Use the existing `death_consumption`/`zombie_outbreak_decay` branches as a complete ripple checklist. This is a high-conflict surface because `chaos_meter_effects.txt` is already modified in the working tree by unrelated work; merge deliberately and do not overwrite the current changes.

## Damage and modifiers

`damage_buildings_in_random_states` in `common/scripted_effects/chaosx_dynamic_effects.txt` is not a suitable Event 013 controller. It chooses random controlled states, uses generic random building rolls, and has a direct population branch. Event 013 needs a selected-state, family-specific effect.

The new `natural_disaster_apply_family_damage` should:

- run in the resolved state scope
- select only family-relevant building categories
- use dynamic damage points and caller building overrides
- use `meta_effect` where a static building type or otherwise static field must be constructed dynamically
- apply engine building damage plus Event 013 state dynamic modifiers
- write damaged-system fields to the aftermath ledger
- apply regional falloff only through explicitly queued neighbor impacts

Create `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt` for severity/family transport, supply, movement, attrition, repair, and resource pressure. Timed fields that reject `constant:` tokens should receive a normal/temp variable assigned from the script constant first.

The current untracked constants provide broad death/damage bands, but they do not yet provide the complete family-specific target weights, vulnerability multipliers, damage-category weights, or chain chances required by Parts 3 and 8 of the spec.

## Evolutions and Event Details

### Evolution recording

Use the Fury pattern in `common/scripted_effects/007_fury_effects.txt`:

- `natural_disaster_sync_evolution_unlocks` checks each Event 013 preview tuple through `is_current_evolution_enabled`.
- Global flags record whether Evolution I, II, and III are currently enabled.
- `natural_disaster_record_evolution_stage` calls `record_events_log_evolution_entry` once per accepted stage and sets a recorded flag only after the record succeeds.
- Ordinary impacts and chains never call the evolution logger.

Use the existing constants:

- event/evolution type: `constant:natural_disaster_event.id` / `constant:natural_disaster_event.evolution_type`
- stages: `evolution_i_stage`, `evolution_ii_stage`, `evolution_iii_stage`
- tiers: `evolution_i_tier`, `evolution_ii_tier`, `evolution_iii_tier`

Call the sync helper at season start and at controller/aftermath transitions that already occur. Do not introduce a global daily/weekly/monthly poll.

### Shared Event Log edits

Edit `common/scripted_effects/chaosx_events_log_effects.txt`:

- add the three Event 013 preview rows in `events_log_rebuild_open_event_details_view`, using `events_log_add_event_detail_evolution_preview`
- add Event 013 actor handling in `events_log_set_default_actor_for_current_event`

Edit `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`:

- `GetEventsLogEvolutionSourceEventNameView`
- `GetEventsLogEventDetailDescription`
- `GetEventsLogEventDetailEvolutionTitle`
- `GetEventsLogEvolutionNameView` and stage/tier variants
- selected-history and selected-evolution name/stage/title/body/summary functions
- `GetEventsLogHistoryEventName`
- `GetEventsLogClusterMemberEventName`

Edit `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`, `GetEventName`, and add `chaosx.event_name.13` to `localisation/english/chaosx_event_names_l_english.yml`.

Player-facing Event Details text belongs in `localisation/english/chaosx_gui_l_english.yml`; event/evolution-specific long-form routing may live in the new Event 013 scripted-localisation/localisation files. The text must describe current behavior, not implementation history or formula values.

## Recovery decisions, missions, and AI

### File ownership and structure

Use:

- `common/decisions/categories/013_natural_disasters_categories.txt`
- `common/decisions/013_natural_disasters_decisions.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `localisation/english/013_natural_disasters_l_english.yml`

The primary category should be `natural_disaster_response_recovery_overview`, matching the asset handoff and accepted GUI direction. Use `state_target = any_owned_state` with `target_root_trigger` for the country-level open-card check and `target_trigger` for the `FROM` state. Require owned-and-controlled state validity in the actual availability/effect helpers.

The current Death decision implementation is a good repo precedent:

- state targeting and `FROM` validation: `death_strengthen_quarantine_line`
- timed mission success/failure and cleanup: `death_hold_quarantine_line_mission`
- category plus attached scripted GUI: `death_country_containment_category`

### Fixed decision/mission ids from the accepted spec

Implement the exact ids from Part 10 rather than inventing parallel generic buttons:

- Rescue: `013_rescue_search_teams`, `013_rescue_open_shelters`, `013_rescue_clear_one_route`, `013_rescue_emergency_evacuation`, `013_rescue_medical_triage`, `013_rescue_port_lifeline`.
- Stabilization: `013_stabilize_clean_water`, `013_stabilize_restore_rail`, `013_stabilize_reopen_port`, `013_stabilize_secure_food`, `013_stabilize_factory_inspection`, `013_stabilize_chain_prevention`.
- Reconstruction: `013_reconstruct_resilient_rails`, `013_reconstruct_seismic_retrofit`, `013_reconstruct_coastal_barriers`, `013_reconstruct_firebreak_network`, `013_reconstruct_volcanic_exclusion_routes`, `013_reconstruct_water_security`, `013_reconstruct_crater_or_exclusion_cordon`.
- Chain missions: `013_chain_prevent_tsunami`, `013_chain_prevent_disease`, `013_chain_prevent_famine`, `013_chain_prevent_wildfire_spread`, `013_chain_prevent_supply_collapse`, `013_chain_prevent_lahar`, `013_chain_prevent_aftershock`.

Active caps and phase transitions should be centralized in constants/effects. Every complete, partial, failure, cancellation, annexation, state-owner change, and supersession path must release its slot and update/close the card.

### AI

Add a `natural_disaster_ai` constant group to `common/script_constants/013_natural_disasters_constants.txt`. Use it in decision `ai_will_do`, event `ai_chance`, target scoring, relief acceptance, and resource-reserve checks. Avoid one copied AI base for every family.

AI decisions should value capital/dense/supply/port/rail/industry states, war supply, family risk, remaining chain time, resources, and foreign relief. GUI can remain human-only, but AI must reach all gameplay effects through the normal decisions/missions. No required recovery action may exist only as a scripted-GUI click.

## Abnormal Evolution III GUI

Create:

- `common/scripted_guis/013_natural_disasters_scripted_gui.txt`
- `interface/013_natural_disasters.gui`
- `interface/013_natural_disasters.gfx`

Use `context_type = decision_category` and attach the scripted GUI to `natural_disaster_response_recovery_overview`. Follow the SOV paranoia and Death Black Atlas structures for ownership, but implement Event 013's accepted card/map/timeline design fresh.

The GUI reads controller state; it does not own gameplay truth. Card selection and map navigation may be scripted-GUI effects. Recovery buttons must route the player to the normal decision/mission surface or share the exact same gate/cost/effect helper without bypassing cost logic. The safest implementation is navigation/selection in GUI and purchases in decisions.

Stable sprite ids from Part 9 are:

- `GFX_013_abnormal_disaster_panel`
- `GFX_013_abnormal_disaster_panel_damaged`
- `GFX_013_disaster_card_frame`
- `GFX_013_disaster_card_frame_warning_animated` / `_static`
- `GFX_013_disaster_card_frame_impact_animated` / `_static`
- `GFX_013_map_marker_impact`
- `GFX_013_map_marker_next_hit_animated` / `_static`
- `GFX_013_map_marker_chain_risk`
- `GFX_013_rupture_wave_sheet` / `_static`
- `GFX_013_meteor_fall_sheet` / `_static`
- `GFX_013_eruption_plume_sheet` / `_static`
- `GFX_013_tsunami_train_sheet` / `_static`
- `GFX_013_storm_corridor_sheet` / `_static`
- `GFX_013_foreign_relief_badge`
- `GFX_013_recovery_progress_frame`
- `GFX_013_recovery_progress_fill`

The five surviving animation packages use different names and cover only warning, storm corridor, tsunami, eruption/ashfall, and skyfall. They can be source material after visual review, but they do not satisfy the stable id/coverage matrix by themselves.

## Natural Disasters cluster

The live cluster framework is owned by:

- `common/script_constants/event_cluster_constants.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`
- `events/chaosx_event_clusters.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/systems/event_clusters.md`

Cluster id `5` is currently unused between Peace (`4`) and Formables (`6`), and the removal diff confirms it formerly belonged to Natural Disasters. Re-register `event_cluster_id.natural_disasters = 5` as a fresh implementation choice, not by copying the old membership code.

Required shared edits:

- add `event_cluster_natural_disasters` unlock/cooldown constants and participation tuning
- add the registry row in `initialize_event_cluster_definitions`
- map Event 013 in `event_belongs_to_cluster`
- add only Event 013 logical slots in `load_event_cluster_members`
- add cooldown checks/setter in `can_event_cluster_fire` and `mark_event_cluster_fired_state`
- establish `event_cluster_actor` and Event 013 call context in `event_cluster_prepare_runtime_context`
- add cluster name/description mappings to Event Log and Settings scripted localisation
- add cluster localisation and documentation

Do not add Events 046, 051, 099, 043, or 120 as cluster members.

### Duplicate-member framework hazard

The cluster queue can technically store Event 013 several times, and `event_cluster_current_member_sequence` gives each queued occurrence a logical index. However, `prepare_event_cluster_firing` currently promotes every member whose event id equals `event_cluster_trigger_event_id` to required. If Event 013 appears three times, all three duplicate rows are promoted; “optional” participation chances will not work as expected.

Use one of two explicit implementations:

1. Deliberately make all tier-eligible duplicate slots required and tune only by minimum tier; or
2. Narrowly change `prepare_event_cluster_firing` so only the first matching duplicate claims required trigger-member status, leaving later duplicate Event 013 slots optional.

The second approach better matches “several entries are possible” but is a shared framework change and needs focused cluster validation. Do not restore the deleted duplicate-member code without resolving this behavior.

## Disaster Barrage scenario

The triggerable-scenario framework already has the correct generic four-stop intensity UI. Its files are:

- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
- `events/chaosx_triggerable_scenarios.txt`
- `interface/chaosx.gui`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/systems/triggerable_scenarios.md`

`triggerable_scenario_id.reserved_7` is the clean registry slot for Disaster Barrage. Replace the reserved id with `disaster_barrage = 7`, remove the initialization reset that treats 7 as invalid, add a name sort value, and register it in `triggerable_scenarios_initialize_registry`.

Add one scenario type variable, for example `triggerable_scenarios_disaster_barrage_type`, cycling the five accepted `natural_disaster_scenario_type` values. Reuse the framework's existing `triggerable_scenarios_intensity` and `triggerable_scenario_intensity.low/medium/high/maximum`; the separate `natural_disaster_scenario_intensity` group in the untracked Event 013 constants is redundant unless a concrete non-UI use is documented.

Add launch routing in `trigger_selected_chaosx_scenario`, eligibility in `triggerable_scenario_can_launch_selected`, name/type/detail/impact scripted localisation, and a launch report event if needed. The launch helper should set Event 013 call fields and invoke the same controller/entry dispatcher as ordinary Event 013. It must not contain a second disaster implementation and must never set `world_end` or a terminal world-end flag.

## Event 046, Event 051, and Event 099

### Event 046

Live files:

- `events/046_placeholder.txt`
- `localisation/english/046_great_earthquake_l_english.yml`
- event name mappings in `chaosx_event_names_l_english.yml`, Event Log scripted localisation, and debug scripted localisation

Both `.1` and `.2` are harmless report placeholders. Event 046 is not registered in the random pools. Leave it inactive and do not call Event 013 from it. Whole-earth rupture exists only behind Event 013 Evolution III.

### Event 051

Live files:

- `events/051_heat_wave.txt`
- `common/ideas/051_heat_wave_ideas.txt`
- `localisation/english/051_heat_wave_l_english.yml`

Event 051 is a fire-once event in `initialize_event_categories`. Its immediate effect gives every country the `heat_wave` idea for two years. Event 013 heat eligibility must therefore block while the target owner has `heat_wave`; the untracked `natural_disaster_is_valid_heat_impact_state` already sketches this check. Do not edit or absorb Event 051. Also prevent an already-open Event 013 heat card from adding a second heat modifier if Event 051 becomes active later.

### Event 099

Live files/callers:

- `events/099_desert_storm.txt`: inert `.1` and `.2` placeholders
- `common/dynamic_modifiers/099_desert_storm_dynamic_modifiers.txt`: orphan `desert_storm` definition with no live application
- `localisation/english/099_desert_storm_l_english.yml`
- `events/070_africa_gods.txt`: three calls to `chaosx.nr99.1`

The current placeholder satisfies the permitted placeholder disposition and is the lowest-risk choice. If a narrow bridge is explicitly selected later, `.1` should only prepare a deity/external caller Event 013 dust-and-sandstorm call and stop; the three Event 070 callsites must then be validated for target/cost/cooldown context. Do not revive `desert_storm` as a competing damage system.

## Assets and GFX

### Real surviving assets

The repository contains substantial produced art under:

- source/processed/package records: `docs/assets/013_natural_disasters/`
- report/news DDS: `gfx/event_pictures/013_natural_disasters/`
- decision/category DDS: `gfx/interface/decisions/013_natural_disasters/`
- idea DDS: `gfx/interface/ideas/013_natural_disasters/`
- animation DDS: `gfx/interface/animated/013_natural_disasters/`
- achievement DDS: `gfx/achievements/013_natural_disasters_*`
- super-event DDS: `gfx/super_events/013_natural_disasters/`

The asset package includes 14 report pictures, 29 news pictures, 22 category pictures, 22 category icons, 17 decision icons, 5 idea icons, 5 eight-frame animation packages with source frames/static fallbacks, 8 old achievement icon triplets, and 4 super-event images.

### Stale wiring claims

`docs/assets/013_natural_disasters/manifest.md` and `gfx_handoff.md` claim that sprites are wired through `interface/013_natural_disasters.gfx`, `interface/013_natural_disasters.gui`, `interface/chaosx_super_events.gfx`, and gameplay files. Those Event 013 files do not exist, and no Event 013 sprite references are present in the live interface files. Treat every Event 013 DDS as produced but unwired.

The category filenames use institutional working concepts such as `*_office`, `*_bureau`, `*_authority`, `*_commission`, and `*_command`. Filenames are not player-facing, but the art and final localisation still require review against the accepted “no generic global institution” direction.

### Animation gap

The existing animation packages have real separate source frames and static fallbacks, so they are eligible source packages under the frame-animation rules. They do not cover the full Part 9 stable sprite set, use different names, and are uniformly 8-frame 36x36 packages while the accepted rupture/meteor/eruption/tsunami/storm overlays call for different frame counts and map-scale uses. Reuse requires a documented mapping or regeneration; silent renaming is not enough.

## Achievements

Live achievement registry surfaces:

- `common/achievements/chaos_redux_achievements.txt` (`unique_id = chaos_redux_achievements`)
- `interface/chaosx_achievements.gfx`
- `localisation/english/chaosx_achievements_l_english.yml`

No Event 013 achievements are registered or localised.

The surviving eight asset ids are:

- `013_natural_disasters_aftershock_control`
- `013_natural_disasters_firebreak_master`
- `013_natural_disasters_global_relief`
- `013_natural_disasters_no_deaths_sequence`
- `013_natural_disasters_no_world_end`
- `013_natural_disasters_prepared_capital`
- `013_natural_disasters_skyfall_survivor`
- `013_natural_disasters_tame_the_barrage`

They do not match the ten accepted working ids in Part 6:

- `013_after_the_sirens`
- `013_no_second_wave`
- `013_every_bridge_counts`
- `013_ashes_without_famine`
- `013_no_global_announcer`
- `013_under_the_falling_sky`
- `013_shake_the_world_back`
- `013_disaster_barrage_maximum`
- `013_not_one_more_camp`
- `013_catalogue_of_ruin`

Do not wire the old eight by convenience. Resolve/recreate the ten accepted complete/grey/not-eligible triplets and implement the required route flags, disqualifiers, family-recovery ledger, refugee death threshold, tsunami/rupture prevention, and Maximum Barrage completion tracking. The `natural_disaster_achievement` constants in the untracked constants file currently describe the old eight and must be replaced or reconciled.

## Super-events

The accepted spec requires six roles: abnormal era reveal, earth rupture, skyfall, mantle opened, moving storm corridor, and delayed tsunami chain. The surviving asset package has only four images: great rupture, massive eruption, skyfall, and storm corridor.

Slots `67`-`70` are partially reserved in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` for title/quote/remark/description keys, but:

- `GetSuperEventImage` has no 67-70 image mappings
- `interface/chaosx_super_events.gfx` has no Event 013 sprites
- no `chaosx_super_event.67`-`.70` localisation exists
- no Event 013 OGG/WAV folders exist
- `music/chaosx_super_event_music.asset`, `music/chaosx_super_event_music.txt`, and `sound/chaosx_sound.asset` have no Event 013 registrations

The current untracked constants also define only four abnormal super-event slots. The six accepted roles need a final collision-free numeric allocation and complete research packages before wiring.

For each completed role, update:

- `interface/chaosx_super_events.gfx`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` (`GetSuperEventImage`, title, quote, remark, description)
- `localisation/english/013_natural_disasters_l_english.yml`
- `music/chaosx_super_event_music.asset`
- `music/chaosx_super_event_music.txt`
- `sound/chaosx_sound.asset`
- actual licensed/researched audio under new Event 013 music/sound folders
- Event 013 emit helpers using `super_event_visible`, `global.current_super_event_audio_id`, and `play_current_super_event_audio`
- super-event research/audio documentation and catalog

Do not invent final quotes, cultural remarks, titles, or audio choices. The research handoff matrix explicitly leaves them blocked until the super-event workflow verifies sources and licensing.

## Documentation, workbook, and prompts

Source-of-truth specs remain in `docs/specs/013_natural_disasters_specs/`. Accepted implementation addenda, audit notes, and handoffs belong in `docs/plans/013_natural_disasters_plans/`.

Required documentation surfaces after gameplay wording stabilizes:

- `docs/events/013_natural_disasters.md`
- `docs/systems/event_clusters.md`
- `docs/systems/triggerable_scenarios.md`
- `docs/systems/chaos_meter_deaths_mechanic.md` for the new death reason/source
- `common/scripted_effects/chaosx_dynamic_effects.md` for the public API
- `docs/assets/013_natural_disasters/manifest.md`
- `docs/assets/013_natural_disasters/gfx_handoff.md`
- super-event research/audio documentation

Workbook ownership:

- `docs/spreadsheets/chaos_redux_events_catalog.xlsx`

Update the Event 013 row, evolution fields, cluster id/member severity, scenario details, and status only after final in-game localisation exists. Spreadsheet details/evolutions must match final in-game wording. Do not mark Event 013 reworked until audits are complete.

Prompt/spec alignment surfaces that must remain consistent include the coding, decision/mission, asset, achievement, localisation, spreadsheet, super-event, and subagent prompts under `docs/specs/013_natural_disasters_specs/prompts/`, plus `docs_alignment/013_source_of_truth_and_disposition_map.md` and `docs_alignment/013_catalog_and_docs_alignment.md`.

## Recommended implementation order

1. **Claim and audit the two untracked foundations.** Resolve ownership; centralize hardcoded trigger thresholds; add missing call/log/concurrency/AI/family tuning; remove obsolete achievement/scenario duplication.
2. **Build the fresh controller and public API.** Create `013_natural_disasters_effects.txt`, document `natural_disaster_start_sequence`, implement sequence/impact ids, keyed queues, validation, target selection, and cleanup before content branches.
3. **Integrate the canonical Event 013 entry.** Replace the inert `.1`, add dispatcher preflight, register as repeatable, set log actor, and prove the one-row invariant with a minimal delayed baseline impact/report.
4. **Integrate Deaths and family damage.** Add the new Deaths reason across the complete shared cause pipeline, implement selected-state family damage and state modifiers, and verify actual population loss/attribution.
5. **Implement baseline and Evolution I families.** Complete target scoring, warnings, reports, news throttle, and family-specific damage/recovery identities before regional scaling.
6. **Implement aftermath decisions/missions and AI.** Add categories, staged rescue/stabilization/reconstruction/chain missions, active caps, partial outcomes, foreign relief, cleanup, and resource-aware AI.
7. **Implement Evolutions II and III.** Add regional falloff, vulnerability scaling, chain ledgers, abnormal families, whole-earth rupture inside Event 013 only, and non-terminal guards.
8. **Wire Event Log evolution/details localisation.** Register three evolution previews/records and every Event 013 name/detail/stage mapping.
9. **Add cluster and Disaster Barrage.** Resolve duplicate Event 013 logical-member behavior, register cluster id 5, claim scenario id 7, and route both through the same controller.
10. **Build abnormal GUI from real controller state.** Wire stable sprites and static fallbacks; keep gameplay costs in normal decisions.
11. **Reconcile related events.** Leave 046 inert, enforce 051 non-stacking for new/open heat cards, and keep 099 inert unless the narrow bridge is explicitly chosen.
12. **Reconcile assets, achievements, and six super-events.** Correct stale manifests/ids, generate missing stable GUI/achievement/super-event assets, complete research/audio, and wire only verified packages.
13. **Align localisation, docs, workbook, and prompts.** Use final in-game wording as the source for documentation and spreadsheet fields.
14. **Run specialised audits.** Decision/mission, localisation, scripted system/API, assets/frame animation, super-event, achievement, and final event-completion audits before the parent completion claim and commit.

## Task-specific validation map

Use `implementation_readiness/013_validation_scenario_matrix.md` as the full checklist. Highest-risk live-repo scenarios are:

| Scenario | Evidence required |
| --- | --- |
| Baseline dispatch | Valid target preflight, exactly one Event 013 history row, first impact after delay, actual Deaths entry, 1-2 day affected-country report, aftermath notification/card. |
| Direct family API | Each family can be requested through `natural_disaster_start_sequence`; invalid state/country/region calls fail without history or stale targets. |
| Concurrent seasons | Two overlapping seasons and two reports do not overwrite family, target, death, damage, or actor data. |
| Dense versus sparse | Same family/severity produces population-scaled absolute deaths while caps prevent impossible losses. |
| Damage identity | Earthquake/tsunami/heat/wildfire/ash/winter target different building/modifier/recovery profiles. |
| Evolution log | Exactly three mutation-stage entries; ordinary impacts and follow-ups do not appear as evolutions. Disabled evolution toggles are respected. |
| Evolution II | Neighbor falloff, vulnerability multipliers, chain risk, and news throttling operate without new history rows. |
| Evolution III | Whole-earth rupture exists only under Event 013, no Event 046 logic runs, and no abnormal family sets `world_end`. |
| Heat separation | With Event 051 `heat_wave` active, new Event 013 heat impact is blocked/deferred and an open Event 013 heat card does not stack another heat modifier. |
| Event 099 | Placeholder remains harmless; if bridged, all three Event 070 callsites create only a cost/cooldown-valid Event 013 dust sequence. |
| Cluster | Cluster id 5 contains only logical Event 013 slots; repeated seasons produce one row each; optional duplicate behavior matches the chosen framework fix. |
| Disaster Barrage | Scenario id 7 uses the same controller; type changes family pool; four intensity stops change size/access; Maximum remains non-terminal. |
| Recovery lifecycle | Success, partial, failure, cancellation, annexation, state owner/control change, and supersession all release caps and remove stale decisions/cards/targets. |
| AI | AI takes at least one warning and one recovery action through decisions without relying on human-only GUI and does not spend on invalid/expired cards. |
| GUI fallback | Animated and static modes both show current path/card/risk/progress state; GUI buttons do not bypass decision costs. |
| Deaths UI | Natural-disaster cause appears in latest reason, country totals, detailed cause totals, and tooltips, including rebuilt/legacy rows. |
| Achievements | Each accepted id requires its actual route and disqualifier; none unlock merely because Event 013 fired. |
| Super-events | Every emitted role has correct image, researched text/quote/remark, settings-aware music and sound registration, and no default/placeholder audio. |

## Risks, blockers, and unresolved choices

1. **Shared-file conflict:** `common/scripted_effects/chaos_meter_effects.txt` is already modified by unrelated work, but adding the natural-disaster Deaths reason requires several edits there.
2. **Untracked foundation ownership:** the new constants/triggers are not tracked and were not created by this explorer. They must not be overwritten blindly.
3. **Concurrent state design:** the specs require overlapping delayed impacts, reports, and aftermaths; a single mutable context will corrupt them. This needs architectural review before family expansion.
4. **Cluster duplicates:** the current trigger-member promotion logic makes all duplicate Event 013 ids required. Optional repeated seasons require the narrow framework fix described above.
5. **Event 099 disposition:** the current placeholder is valid and safest. A narrow bridge is optional but materially activates three Event 070 deity callsites and therefore needs caller-cost/target/cooldown context.
6. **Deaths reason ripple:** adding only the numeric reason and a localisation key is incomplete; country cause aggregation and view arrays must also change.
7. **Stale asset documentation:** produced DDS files are unwired despite manifest claims. Historical event ids and “all wired” statements cannot be trusted.
8. **Achievement mismatch:** eight old icon ids/thresholds conflict with ten accepted achievement ids and route definitions.
9. **Super-event blocker:** only four of six images exist and none of the six has complete final text/audio wiring. Super-event completion is blocked on research and asset/audio production.
10. **Abnormal GUI asset gap:** existing 36x36 eight-frame packages do not cover the stable panel/card/map-marker/overlay matrix.
11. **No periodic on-action authority:** the accepted implementation must progress through delayed events, decision missions, and narrow lifecycle hooks. A new world-scanning daily/weekly/monthly on action is not authorized.
12. **No fallback/simplification:** replacing family-specific damage/recovery, missing super-events, missing accepted achievements, or abnormal GUI with generic substitutes would be an unapproved simplification.

## Explorer handoff

This report is the only file created by the repository-explorer pass. No gameplay, localisation, asset, spreadsheet, or shared-system files were edited. No historical Event 013 logic was restored or copied.

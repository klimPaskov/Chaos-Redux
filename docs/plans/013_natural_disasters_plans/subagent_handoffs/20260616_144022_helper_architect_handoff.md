# Event 013 Natural Disasters Helper Architect Handoff

Timestamp: 2026-06-16 14:40:22 UTC

## Scope

Implemented only the reusable helper layer for Event 013 Natural Disasters. No event files, decisions, localisation, GFX, achievements, spreadsheets, clusters, Event 46, focus trees, or country packages were edited.

## Files Changed

- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `docs/plans/013_natural_disasters_plans/subagent_handoffs/20260616_144022_helper_architect_handoff.md`

## Constants Added

- `natural_disaster_event`: Event 13 ID, evolution type, baseline and Evolution I-IV stage IDs.
- `natural_disaster_family`: earthquake, flood, storm, drought, wildfire, landslide, volcano, tsunami, meteor IDs.
- `natural_disaster_severity`: local, serious, regional, cascading, abnormal, scenario maximum.
- `natural_disaster_phase`: none, warning, impact, recovery, chain, scenario.
- `natural_disaster_scenario_type`: mixed barrage, earthquake wave, coastal hyperstorm, volcanic eruption, meteor shower.
- `natural_disaster_target`: population gates, target score weights, cooldown durations.
- `natural_disaster_family_weight`: baseline random family weights mirrored by file-local `@` constants for `random_list`.
- `natural_disaster_warning`: family warning chances and mitigation multipliers.
- `natural_disaster_impact_damage`: severity damage values.
- `natural_disaster_population_loss_per_k`: severity population-loss values.
- `natural_disaster_aftermath`: aftermath and rebuilding durations, mirrored by file-local `@` constants for timed flags.
- `natural_disaster_recovery_cost`: concrete recovery cost variables for support equipment, trucks, trains, convoys, fuel, manpower, command power, army XP, stability risk, and war-support risk.
- `natural_disaster_mission_duration`: mission duration bands.
- `natural_disaster_burst`: burst incident counts and delay bands for later event call sites.
- `natural_disaster_scenario_barrage`: manual scenario intensity incident counts and severity values.
- `natural_disaster_ai`: AI response weight and cost multipliers for later decision AI.

## Scripted Triggers Added

- `natural_disaster_can_affect_country`: country must exist, not capitulated, not special chaos actor, and not under `world_end`.
- `natural_disaster_country_has_valid_target_state`: country has at least one valid controlled target state.
- `natural_disaster_is_recent_family_target`: checks family-specific recent-hit state flags.
- `natural_disaster_state_has_meaningful_exposure`: population/building/supply/port/rail/capital exposure gate.
- `natural_disaster_is_coastal_candidate_state`: physical fit for tsunami/storm/coastal families.
- `natural_disaster_is_mountain_candidate_state`: physical fit for landslide/earthquake-style mountain incidents.
- `natural_disaster_is_dry_candidate_state`: physical fit for drought and dry-belt pressure.
- `natural_disaster_is_wildfire_candidate_state`: physical fit for wildfire and industrial firestorm candidates.
- `natural_disaster_is_volcanic_candidate_state`: proxy volcanic fit using coastal mountains/hills or explicit `natural_disaster_volcanic_region` state flag.
- `natural_disaster_family_fits_current_state`: family-aware physical target gate.
- `natural_disaster_is_valid_target_state`: full target gate including controller validity, exposure, anti-repeat, and family fit.
- `natural_disaster_is_valid_base_target_state`: base exposure/cooldown gate used only to suppress impossible family weights.
- `natural_disaster_has_active_warning`, `natural_disaster_state_has_active_warning`: warning phase checks.
- `natural_disaster_state_has_active_aftermath`, `natural_disaster_country_has_active_aftermath`: recovery phase checks.
- `natural_disaster_country_should_show_response_office`: decision category visibility helper for later decision implementation.
- `natural_disaster_can_launch_manual_barrage`: broad manual scenario gate, blocking only terminal world-end state and impossible target pools.
- `natural_disaster_selected_scenario_is_event_13`: convenience trigger for later scenario UI routing.

## Scripted Effects Added

- `natural_disaster_prepare_launch_context`: sets evolution stage, severity floor, family, and impact phase.
- `natural_disaster_select_stage`: maps current `chaos_tier` flag to baseline/Evolution I-IV stage IDs.
- `natural_disaster_select_family_for_stage`: chooses family using family weights, stage locks, and physical target availability.
- `natural_disaster_select_target_state`: selects a valid owned-controlled target state, saves `natural_disaster_current_target_state` and `natural_disaster_current_controller`, and flags clean failure if none exists.
- `natural_disaster_score_current_state`: writes `natural_disaster_last_target_score` on the selected state.
- `natural_disaster_setup_warning`: stores country/state warning flags and family/severity variables on the current target.
- `natural_disaster_roll_warning_chance`: computes family warning chance and outputs `natural_disaster_should_warn`.
- `natural_disaster_apply_impact_to_current_state`: state-scope impact wrapper for damage profile, warning mitigation, building damage, population loss, and recovery setup.
- `natural_disaster_set_damage_profile`: maps severity to dynamic damage and population-loss temp variables.
- `natural_disaster_apply_population_loss`: applies state population delta through `add_manpower` and stores `natural_disaster_last_population_delta`.
- `natural_disaster_damage_selected_building_type`: meta-effect injection helper for dynamic building type and damage amount.
- `natural_disaster_apply_family_building_damage` plus family profile helpers: applies family-specific building damage profiles.
- `natural_disaster_setup_recovery_context`: sets recent target/family flags, aftermath flags, state recovery variables, country response visibility, recovery costs, and pressure refresh.
- `natural_disaster_set_family_aftermath_flags`: sets family-specific aftermath marker flags matching the spec labels.
- `natural_disaster_calculate_recovery_costs`: writes concrete country recovery cost variables for later decisions/missions.
- `natural_disaster_apply_recovery_progress`: increments state recovery progress and cleans state context when full recovery is reached.
- `natural_disaster_refresh_recovery_pressure`: counts controlled active aftermath states and writes active count/worst severity.
- `natural_disaster_record_evolution_if_needed`: sets shared Event Log evolution variables and records Evolution I-IV once when enabled.
- `natural_disaster_prepare_scenario_barrage`: stores manual barrage type, intensity, remaining incidents, severity, and scenario phase variables.
- `natural_disaster_select_scenario_family`: maps manual scenario type to family/stage.
- `natural_disaster_cleanup_current_state_context`: clears warning, aftermath, family marker flags, state variables, and refreshes controller pressure.
- `natural_disaster_cleanup_country_context`: clears country warning/response/cost variables.
- `natural_disaster_cleanup_scenario_barrage`: clears manual barrage global flag and global scenario variables.

## Event Targets And Cleanup Plan

The helper layer uses regular event targets only:

- `natural_disaster_current_target_state`
- `natural_disaster_current_controller`
- `events_log_evolution_actor` when recording an actor-bearing evolution

No global event target was added. Scenario persistence uses global variables and `natural_disaster_manual_barrage_running`; `natural_disaster_cleanup_scenario_barrage` clears them.

## Call Sites Changed

None. Event, decision, scenario GUI, Event 46, localisation, and log call sites were explicitly outside the owned write scope.

Expected later call sequence for a normal incident:

```txt
natural_disaster_prepare_launch_context = yes
natural_disaster_select_target_state = yes
natural_disaster_roll_warning_chance = yes
# If warning branch is used:
natural_disaster_setup_warning = yes
# In selected state scope when impact resolves:
event_target:natural_disaster_current_target_state = {
	natural_disaster_apply_impact_to_current_state = yes
}
natural_disaster_record_evolution_if_needed = yes
```

Expected later call sequence for manual barrage:

```txt
natural_disaster_prepare_scenario_barrage = yes
# Scenario event/GUI should consume global.natural_disaster_scenario_remaining_incidents.
natural_disaster_cleanup_scenario_barrage = yes
```

## Assumptions

- Dynamic state modifiers for `recent_earthquake_damage`, `flooded_transport_belt`, `crop_failure_pressure`, `storm_wreckage`, `burned_districts`, `unstable_mountain_passes`, `volcanic_ashfall`, `tsunami_scoured_coast`, and `meteor_scars` are not defined in this patch because `common/dynamic_modifiers/` is outside scope. This helper sets matching state flags and variables for the later modifier layer.
- Volcanic targeting uses a proxy trigger: coastal mountain/hill states or explicit `natural_disaster_volcanic_region` state flags. A later implementation should add curated volcanic-region setup or replace the proxy with a documented state group.
- Manual scenario constants in this file support Event 13, but the central triggerable scenario registry remains untouched by scope.
- Evolution logging helper assumes the shared events-log helpers and `is_current_evolution_enabled` are available from existing Chaos Redux systems.

## Risks And Follow-Up

- No call sites consume these helpers yet, so Event 13 is not implemented or complete.
- Event 46 absorption is not patched here; later work must disable/placeholder Event 46 and route the abnormal earthquake wave through Event 13.
- Family-specific state flags are gameplay markers only until dynamic modifiers, localisation, and decision text are wired.
- The target selector is family-valid but not a true weighted scorer. It scores the selected state for display/future logic; a later implementation can deepen this with arrays or staged priority pools if needed.
- `natural_disaster_selected_scenario_is_event_13` is a convenience trigger only. The final triggerable scenario ID may need to use the central scenario registry rather than the event ID.

## Validation

Ran task-specific static checks on the three helper files:

- Checked for unsupported `<=`/`>=`, broad world iteration helpers, global event targets, dynamic modifier references, and ambiguous direct dynamic `damage_building.damage` usage.
- Confirmed brace balance on the three added Clausewitz files.
- Ran `git diff --check` on the three added helper files.

Skipped in-game validation because no event/decision/scenario call sites were in scope and this subagent cannot claim Event 13 runtime completion.

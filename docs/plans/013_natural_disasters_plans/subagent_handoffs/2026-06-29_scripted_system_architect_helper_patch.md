# Event 13 Natural Disasters scripted helper patch handoff

## Files changed

- `common/script_constants/013_natural_disasters_constants.txt`
- `common/scripted_effects/013_natural_disasters_effects.txt`
- `common/scripted_triggers/013_natural_disasters_triggers.txt`
- `common/dynamic_modifiers/013_natural_disasters_dynamic_modifiers.txt`

## Helper map

| Helper | Scope | Inputs | Outputs and side effects |
| --- | --- | --- | --- |
| `natural_disasters_initialize_sequence_context` | Country | Optional `natural_disasters_sequence_evolution_stage`, cluster flags, scenario intensity flags | Creates `natural_disasters_sequence_id`, incident count, delay band, sequence flags, and global sequence counter. |
| `natural_disasters_set_sequence_incident_count_from_context` | Country | Evolution, cluster slot flags, scenario intensity flags | Writes `natural_disasters_sequence_incidents_planned`. |
| `natural_disasters_prepare_delay_band` | Country | `natural_disasters_sequence_incidents_planned`, scenario maximum flag | Writes `natural_disasters_delay_min_days` and `natural_disasters_delay_max_days`. |
| `natural_disasters_mark_delayed_subdisaster_queued` | Country | Current sequence variables | Advances completed incident count and refreshes delay band. Parent event code must still schedule the actual subevent. |
| `natural_disasters_open_warning_window` | State | Current state and owner | Adds warning flags, warning variables, and `natural_disaster_warning_disruption`. |
| `natural_disasters_set_profile_*` | State | None beyond selected family | Writes family id, base loss rate, building damage profile, and dynamic modifier values. |
| `natural_disasters_prepare_loss_rate` | State | `natural_disaster_severity_id`, `natural_disaster_evolution_stage`, optional preparedness and aftermath multipliers | Computes `natural_disaster_final_loss_rate` and clamps only that rate to severity ceiling constants. |
| `natural_disasters_register_state_population_loss` | State | `natural_disaster_final_loss_rate`, `natural_disasters_death_reason` | Computes `state_population_k * 1000 * natural_disaster_final_loss_rate` into `chaos_deaths_change`, then calls `chaos_meter_register_deaths` with civilian and state-population flags. |
| `natural_disasters_apply_building_damage_profile` | State | Family profile temp variables | Damages infrastructure, rail, supply hubs, factories, ports, airbases, defenses, radar, and anti-air using family-specific dynamic damage values. |
| `natural_disasters_apply_state_modifier_profile` | State | Family profile temp variables and severity | Applies `natural_disaster_state_disruption` with duration from severity. |
| `natural_disasters_mark_family_aftermath` | State | `natural_disaster_family_id`, `natural_disaster_severity_id` | Sets family aftermath flags, aftershock watch modifier when relevant, and owner country aftermath count. |
| `natural_disasters_apply_state_disaster_impact` | State | Family profile, severity, evolution, preparedness | Runs loss-rate, building damage, state modifier, death registration, and aftermath setup. |
| `natural_disasters_apply_<family>_impact` | State | Severity, evolution, optional preparedness and aftermath multipliers | Family-specific entry points for flood, cyclone or storm, severe storm, corridor storm, earthquake, rupture, tsunami, volcano, massive eruption, wildfire, drought or famine, heat, winter, dust or sandstorm, landslide or slope collapse, and skyfall or meteor. |
| `natural_disasters_advance_recovery_progress` | State | Optional `natural_disaster_recovery_progress_add` | Adds recovery progress and calls state cleanup at 100 progress. |
| `natural_disasters_cleanup_state_aftermath` | State | Active aftermath state | Clears aftermath and warning flags, removes dynamic modifiers, and clears state variables. |
| `natural_disasters_cleanup_sequence_context` | Country | Active sequence country | Clears sequence, cluster slot, scenario intensity, warning, and death reason variables and flags. |

## Trigger map

- `natural_disasters_has_active_sequence`
- `natural_disasters_state_has_active_aftermath`
- `natural_disasters_state_can_receive_impact`
- `natural_disasters_state_is_coastal_or_port`
- `natural_disasters_state_is_dense_or_built_up`
- `natural_disasters_state_is_mountain_or_slope`
- `natural_disasters_state_is_arid_or_desert`
- `natural_disasters_state_is_forest_or_fire_risk`
- `natural_disasters_state_is_cold_or_winter_risk`
- `natural_disasters_state_is_volcanic_candidate`
- `natural_disasters_state_can_receive_flood`
- `natural_disasters_state_can_receive_cyclone_or_tsunami`
- `natural_disasters_state_can_receive_seismic`
- `natural_disasters_state_can_receive_volcano`
- `natural_disasters_state_can_receive_wildfire`
- `natural_disasters_state_can_receive_drought_heat_or_dust`
- `natural_disasters_state_can_receive_winter`
- `natural_disasters_state_can_receive_landslide`
- `natural_disasters_state_can_receive_skyfall`

## Constants and tuning table plan

The patch adds script constants for family ids, severity ids, evolution ids, incident counts, delay bands, base family loss rates, severity multipliers, evolution multipliers, final loss-rate ceilings, preparedness multipliers, modifier durations, follow-up weights, family state modifier values, and family building damage profiles.

No absolute death cap constants remain. The earlier `natural_disasters_death_cap_factor` category was removed after the constraint update. Death safety is handled only by `natural_disaster_final_loss_rate` ceilings.

## Death path

The death helper does not call `chaos_meter_register_state_civilian_deaths_percent`, because that helper contains cap fields and default absolute caps. Event 13 instead computes the full per-state result directly:

```txt
chaos_deaths_change = state_population_k * 1000 * natural_disaster_final_loss_rate
```

It then calls `chaos_meter_register_deaths` with `chaos_deaths_is_civilian = 1`, `chaos_deaths_apply_state_pop = 1`, and owner country targeting. This keeps the shared deaths log, chaos-from-deaths sync, country death totals, state population reduction, and deaths map update.

Parent integration must set `natural_disasters_death_reason` to the future `constant:chaos_meter_deaths_reason.natural_disaster` value after the enum is added. Until then, the helper marks the state with `natural_disaster_death_reason_pending` and records no deaths.

## Event target and cleanup plan

This patch does not create persistent global event targets. Parent event code should use regular event targets for the current anchor state, current owner, forecast state, and delayed follow-up target because those targets only need to persist through a sequence or a fired follow-up event chain.

Cleanup exists in two layers:

- `natural_disasters_cleanup_state_aftermath` clears warning, aftershock, aftermath, family state flags, dynamic modifiers, and state variables.
- `natural_disasters_cleanup_sequence_context` clears country sequence state, cluster flags, scenario intensity flags, and the pending death reason variable.

## Migration plan for parent

1. Add `natural_disaster` to `chaos_meter_deaths_reason` and set `natural_disasters_death_reason` before impact helpers are called.
2. In `events/013_natural_disasters.txt`, use `natural_disasters_initialize_sequence_context` when a sequence starts.
3. Select the family and target state in parent code or later target-selection helpers, then call the matching `natural_disasters_apply_<family>_impact` entry point in state scope.
4. Use `natural_disasters_mark_delayed_subdisaster_queued` before scheduling hidden follow-up events, but keep history logging to one Event 13 row per sequence.
5. Wire decisions and missions to `natural_disasters_advance_recovery_progress` and cleanup helpers.
6. Replace any repeated family damage or aftermath code with the profile entry points instead of duplicating damage tables in events or decisions.

## Validation

- Checked new helper files for unsupported `<=` and `>=`.
- Checked new helper files for references to old Event 51, 99, 28, 43, 46, and 47 logic sources.
- Checked the required family entry point coverage in `013_natural_disasters_effects.txt`.
- Checked new Clausewitz files for leading-space indentation on script lines.
- Checked no Event 13 helper file still references `natural_disasters_death_cap_factor`, `death_cap_factor`, `cap_hard_max`, or `chaos_meter_register_state_civilian_deaths_percent`.

## Risks and follow-up

- The helpers are not wired to Event 13 event, decision, localisation, GUI, or log files because those files were outside this task scope.
- Family target groups use candidate flags such as `natural_disaster_volcanic_candidate`, `natural_disaster_river_candidate`, and `natural_disaster_cold_candidate`. Parent implementation still needs to seed those flags from curated state lists or fallback heuristics.
- Family state modifiers intentionally have no icons in this patch, because interface and asset files were outside scope.
- `natural_disasters_death_reason` must be populated by parent integration after the shared death enum receives `natural_disaster`.

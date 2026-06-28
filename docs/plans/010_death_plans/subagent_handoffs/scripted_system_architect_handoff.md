# Event 010 Death Scripted-System Architecture Handoff

Subagent: `chaosx_scripted_system_architect`
Date: 2026-06-15
Mode: architecture handoff only. No gameplay files were patched.
Active triggerable scenario ID: `SCN-006`. Earlier scenario-ID wording is superseded.

## Reference Pass Completed

Required project instructions and skills were read:

- `AGENTS.md`
- `CHAOS_REDUX_MECHANICS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `docs/specs/010_death_specs/specs/*.md`
- `docs/specs/010_death_specs/matrices/*.md`

Required offline Paradox wiki pages were consulted before implementation-file inspection:

- Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, AI modding
- Country creation, State modding, Map modding, Achievement modding, National focus modding
- Interface modding, Scripted GUI modding, Graphical asset modding, Unit modding, Division modding

Relevant vanilla documentation and examples were consulted under `/home/klim/projects/Hearts of Iron IV/`, especially script constants, effects, triggers, scripted localisation, dynamic variables, scripted GUI, state control-change on actions, `create_unit`, state transfer, building removal/damage, event targets, arrays, and meta effects/triggers.

## Design Boundary

This map keeps Death's spec intact. It does not redesign Death. It isolates repeated logic into event-specific helpers, adds only shared-system hooks where Death must integrate, and avoids broad daily all-world scans. Scheduled pulses must run from the Death country or from explicit state/control-change hooks, not from `on_daily`, `on_weekly`, or `on_monthly` all-country iteration.

Recommended file surfaces:

- `common/script_constants/010_death_constants.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/on_actions/010_death_on_actions.txt`
- `common/modifiers/010_death_modifiers.txt`
- `events/010_death.txt`
- Existing shared updates:
  - `common/script_constants/chaos_meter_constants.txt`
  - `common/scripted_effects/chaos_meter_effects.txt`
  - `common/scripted_effects/chaosx_dynamic_effects.txt`
  - `common/scripted_effects/chaosx_dynamic_effects.md`
  - `common/scripted_triggers/chaosx_world_threat_triggers.txt`
  - `common/scripted_triggers/chaosx_dynamic_triggers.txt`
  - `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
  - `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
  - `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
  - `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
  - `common/scripted_guis/chaosx_scripted_gui_settings.txt`
  - `events/chaosx_triggerable_scenarios.txt`
  - `localisation/english/chaosx_gui_l_english.yml`
  - `docs/systems/triggerable_scenarios.md`
  - `docs/systems/world_threat_mechanic.md`

## Helper Map

### Core Creation and Lifecycle

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `death_initialize_global_state` | Any stable root, usually global/event root | none | Initializes Death globals, arrays, and defaults | Clears stale Death launch/temp flags when Death is inactive; ensures counters exist | `chaosx.nr10.1`, `trigger_death_scenario`, save/load repair event if added |
| `death_create_country_if_needed` | Any scope | Optional `death_creation_context` temp | Regular `event_target:death_country_actor`; optional global target `death_country` | Creates or activates `DTH`, sets `death_country_created`, leader/cosmetic setup, neutral diplomacy posture, no start divisions | Entry event, SCN-006 launches, recovery hooks |
| `death_refresh_active_state_arrays` | `DTH` country scope | none | Rebuilds `global.death_active_wasteland_states`, optional `global.death_wither_targets` | Removes stale state-scope entries from arrays | After consumption, recapture, defeat check, world-end foothold creation |
| `death_defeat_cleanup` | Any scope | Optional `death_defeat_context` temp | Clears active Death flags and targets | Clears `world_threat_source_death`; refreshes world threat; converts active wastelands to recaptured; clears withers/cooldowns; stops pulses; removes or neutralizes `DTH` units/country | `death_refresh_defeat_state`, scripted defeat event, on control/capitulation hooks |

### Origin, Consumption, and Wasteland

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `death_select_origin_state` | Any scope | Scenario/type temps may bias target | `event_target:death_selected_state`; temp `death_origin_selection_tier` | One-time `random_state` search only; no daily scan | Entry event, Instant Outbreak SCN-006 |
| `death_consume_current_state` | State scope | `event_target:death_country_actor` or static `DTH`; temp `death_consumption_context`; optional `death_skip_public_effects` | Temp `death_last_consumed_population`; global counters updated | Records pre-consumption population, Death deaths, zeroes population, strips infrastructure/industry, transfers owner/controller/core to `DTH`, applies active wasteland modifier, sets `death_consumed_state` and `death_active_wasteland`, updates arrays, spread pressure, reveal/world-end checks | All origin, island spread, mainland reveal, wither completion, coastal jump, world-end foothold, SCN-006 launch paths |
| `death_register_consumed_population_deaths` | State scope before population removal | Temp `death_last_consumed_population`; reason constant | Death counters and chaos meter deaths ledger | Calls `chaos_meter_register_deaths` with `chaos_deaths_is_civilian = 1`, `chaos_deaths_apply_state_pop = 1`, `chaos_deaths_target_country = OWNER`; Death should add `chaos_meter_deaths_reason.death_consumption` and a 0.10 chaos weight | Inside `death_consume_current_state` |
| `death_strip_current_state_buildings` | State scope | Optional severity temp | none | Removes or damages `industrial_complex`, `arms_factory`, `dockyard`, `synthetic_refinery`, `fuel_silo`, `air_base`, `anti_air_building`, `radar_station`, forts, naval base, rail, supply node, infrastructure according to constants | Inside `death_consume_current_state`; optional harsher world-end branch |
| `death_apply_active_wasteland_state` | State scope | none | none | Adds active wasteland state modifier, clears recaptured modifier, sets state flags | Consumption and control-change refresh |
| `death_apply_recaptured_wasteland_state` | State scope | none | none | Clears active wasteland, adds recaptured wasteland modifier, preserves consumed/history flags | `on_state_control_changed`, `death_defeat_cleanup` |
| `death_refresh_wasteland_state_for_controller_change` | State scope from `on_state_control_changed` | ROOT new controller, FROM old controller, FROM.FROM state via hook wrapper | none | If a Death wasteland is recaptured, applies recaptured modifier and invalidates nearby withers; if Death retakes, reapplies active modifier | `on_state_control_changed` Death wrapper |

### Spread, Wither, and Coastal Jumps

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `death_refresh_spread_pressure` | Any scope | Death counters, reveal/world-end flags, chaos value, containment pressure | `global.death_spread_pressure` | Recomputes from constants instead of cumulative drift | After consumption, containment changes, reveal/world-end, SCN-006 setup |
| `death_schedule_next_spread_pulse` | `DTH` country scope | Current phase and spread pressure | Hidden event delay variables | Queues only `DTH` hidden country event; does not use daily on-action | Entry/reveal, end of each spread pulse, SCN-006 |
| `death_run_spread_pulse` | `DTH` country scope | Current phase flags | May set selected state targets | Attempts one bounded action: island consumption, wither advance, coastal jump, ghost refresh, or defeat refresh | Hidden Death pulse event |
| `death_select_or_advance_wither_target` | `DTH` or state scope, depending implementation | Active wasteland arrays or Death-controlled states | State `death_wither_target` flag and `death_wither_progress` variable | Selects adjacent valid states only; clears invalid stale targets | Hidden spread/wither pulse, on control-change invalidation |
| `death_advance_wither_targets` | `DTH` country scope | `global.death_wither_targets` or bounded `DTH` controlled-state loop | Completed targets consumed | Increases/decays `death_wither_progress`; pauses or decays if blocking divisions/protection appear | Hidden wither pulse only |
| `death_clear_wither_on_current_state` | State scope | none | none | Clears `death_wither_target` and progress variable | Recapture, invalidation, consumption, defeat cleanup |
| `death_start_coastal_jump_cooldown` | Any scope | Temp cooldown duration or phase | `global.death_coastal_jump_cooldown` | Sets numeric cooldown from constants | Successful coastal jump |
| `death_reduce_coastal_jump_cooldown_for_pulse` | Any scope | Pulse interval temp | `global.death_coastal_jump_cooldown` | Subtracts pulse interval on scheduled Death pulse; clamps at zero | Hidden Death pulse |
| `death_attempt_coastal_jump` | `DTH` country scope | Current phase, cooldown, target filters | Optional `event_target:death_coastal_jump_target` | Consumes one valid coastal target, starts cooldown, logs if revealed | Hidden spread pulse and after Death loses mainland foothold |

### Ghosts, Defeat, and World Threat

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `death_calculate_ghost_spawn_count` | `DTH` country scope | Temp `death_ghost_tier`; Death consumed population/states; scenario intensity | Temp `death_ghost_spawn_count` | Applies floors/caps/ratio ladder from constants | Ghost refresh pulse, world-end start, SCN-006 setup |
| `death_spawn_ghost_hosts_in_current_state` | State scope | Temp count, tier/template selector | Units spawned | Uses `create_unit` for `DTH`; static branches or meta effect for template names if needed | Ghost refresh, world-end footholds, SCN-006 Instant Outbreak |
| `death_spawn_ghost_hosts_for_tier` | `DTH` country scope | Tier and cap temps | none | Distributes hosts across active Death states or foothold states; respects total cap | Ghost refresh pulse, world-end start, SCN-006 |
| `death_refresh_defeat_state` | Any scope, preferably after relevant state event | none | Temp or global defeat marker | If `DTH` has no controlled states or every controlled state is occupied by enemies, calls cleanup once | `on_state_control_changed`, `on_capitulation`, after consumption/jump, after failed spread pulse |
| `death_refresh_world_threat_source` | Any scope | Reveal/world-end/Death active state | `world_threat_source_death` flag | Sets or clears Death threat source, then calls `refresh_world_threat_state` | Reveal, world-end, defeat cleanup, recovery |
| `death_try_start_world_end` | Any scope | Chaos value, continent-consumed facts | Starts world-end if eligible | Sets `world_end`/Death flags, creates footholds, upgrades ghosts, refreshes world threat | After each consumption once mainland spread is active |
| `death_create_world_end_footholds` | Any scope | Target continent constants and selection tiers | Foothold states consumed | Creates footholds on remaining continents; avoids duplicate continent footholds | World-end start |

### Trigger Helpers

| Trigger | Scope | Inputs/assumptions | Returns true when | Call sites |
| --- | --- | --- | --- | --- |
| `is_death_country` | Country | none | Scope is `DTH` or has `death_country_created` | Shared special-country filters, AI, events |
| `death_country_exists` | Any | none | `DTH` exists and is marked active | Scenario eligibility, entry guards |
| `death_is_valid_origin_state_preferred` | State | Population and geography constants | Remote low-pop ocean island, unprotected, not invalid for country creation | Origin selection |
| `death_is_valid_origin_state_fallback` | State | Broader population/geography constants | Acceptable fallback origin if preferred pool is empty | Origin selection only; report if used |
| `death_is_valid_island_spread_target` | State | Death not publicly revealed or early phase | Valid island target, not already consumed, low population/defense | Island spread pulses, SCN-006 Instant Outbreak |
| `death_is_valid_mainland_reveal_target` | State | Reveal threshold constant | Mainland state above reveal threshold, valid owner/controller, not consumed | Reveal target selection, SCN-006 Instant Outbreak |
| `death_is_valid_wither_target` | State | Death actor exists; adjacent-state trigger support validated | Neighbor of active Death mainland state, not consumed, not protected, not blocked by defenders, belongs to or is at war with a valid victim | Wither target selection |
| `death_wither_target_has_blocking_defenders` | State | Exact division trigger scope must be validated | Non-Death enemy divisions are present in the target state | Wither pause/decay |
| `death_is_valid_coastal_jump_target` | State | Cooldown already checked | Coastal, low defense/no divisions, not protected, valid continent preference | Coastal jumps |
| `death_can_attempt_coastal_jump` | Any | Cooldown variable and phase flags | Cooldown is zero and Death is revealed or in allowed high-chaos scenario phase | Spread pulse/coastal recovery |
| `death_is_defeated` | Any or `DTH` | `DTH` exists | Death controls no states, or all controlled states are enemy-occupied per final implementation | Defeat refresh |
| `death_should_be_world_threat_source` | Any | Reveal/world-end and active-state flags | Death is revealed or terminal and still controls at least one state | Threat refresh |
| `death_scenario_can_launch_selected` | Any/player country | Current triggerable scenario type/intensity variables | Selected SCN-006 type has at least one valid target and no impossible conflict | `triggerable_scenario_can_launch_selected` Death branch |

## SCN-006 Triggerable Scenario Helpers

The triggerable scenario architecture should register Death as ID `6`, display `#006`, and call it `SCN-006` in docs and localisation. This scenario must not be wired under any other scenario ID.

### Constants

Add to `common/script_constants/chaosx_triggerable_scenarios_constants.txt`:

- `triggerable_scenario_id.death = 6`
- `triggerable_scenario_sort.death_id = 6`
- `triggerable_scenario_sort.death_name = <chosen alphabetical slot>`
- `triggerable_scenario_death_type.instant_outbreak = 1`
- `triggerable_scenario_death_scale.*` for per-intensity island counts, mainland reveal counts, and starting ghost host counts

Avoid renumbering existing scenario IDs. If name sorting is meant to remain alphabetical, update only sort values and rebuild view logic, not visible IDs.

### Effects

| Helper | Scope | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `select_triggerable_scenario_death` | Player/settings country | none | `global.triggerable_scenario_selected_id = 6` | Rebuilds scenario detail view | Scenario row click in settings GUI |
| `trigger_death_scenario` | Player/settings country | Global intensity | Dispatches Instant Outbreak | Sets temporary launch flags, creates `DTH` if needed, preserves normal event timer, fires `chaosx.triggerable_scenarios.6`, clears bypass context | `trigger_selected_chaosx_scenario` Death branch |
| `death_launch_instant_outbreak` | Global/event root | Intensity temps | Origin, extra islands, and mainland reveal states consumed | Uses normal origin and consumption helpers, skips missing-island reports for the instant setup, schedules normal Death pulses afterward | SCN-006 Instant Outbreak |
| `death_triggerable_consume_extra_island` | Global/event root | Intensity-selected repeat count | One valid island consumed | Uses the shared consumption helper without shortcut chaos or evolution changes | SCN-006 Instant Outbreak |
| `death_triggerable_consume_mainland_state` | Global/event root | Intensity-selected repeat count | One valid mainland reveal state consumed | Uses the shared consumption helper and public reveal flow without natural evolution gates | SCN-006 Instant Outbreak |
| `death_triggerable_spawn_passive_hosts` | Player/settings country | Scenario intensity | One weak starting host created | Directly creates the scenario host and charges Death host counters afterward | Low and Medium SCN-006 |
| `death_triggerable_spawn_stronger_hosts` | Player/settings country | Scenario intensity | Two stronger starting hosts created | Directly creates scenario hosts and charges Death host counters afterward | High and Maximum SCN-006 |
| `death_cleanup_triggerable_scenario_context` | Any | none | none | Clears launch bypass flags, scenario temp variables, and any global event targets used only by launch | End of `trigger_death_scenario` and fail paths |

### Triggerable Scenario Call-Site Checklist

- Initialize default Death type in `initialize_triggerable_scenarios_settings`.
- Register Death in `triggerable_scenarios_initialize_registry`.
- Include Death in `triggerable_scenarios_rebuild_view` sort passes.
- Add `select_triggerable_scenario_death`.
- Add Death branches to `triggerable_scenario_type_previous` and `triggerable_scenario_type_next`, keeping the single Instant Outbreak type selected.
- Add Death branch to `trigger_selected_chaosx_scenario`.
- Add Death branch to `triggerable_scenario_can_launch_selected`.
- Add scripted localisation for Death ID, name, type, type effect, type impact, intensity impact, and blocked reasons.
- Add `chaosx.triggerable_scenarios.6` confirmation/result event.
- Add settings export/import scalar for `triggerable_scenarios_death_type` only if the scenario settings export is expected to preserve the single Instant Outbreak type explicitly.

## Constants and Tuning Plan

Use script constants for shared tuning, especially values used across effects, triggers, GUI, localisation, and scenario wrappers. Use file-scoped `@` constants only for fields that reject `constant:` tokens, and prefer assigning constants to variables before such fields when supported.

Recommended categories in `common/script_constants/010_death_constants.txt`:

| Category | Keys |
| --- | --- |
| `death_population` | `mainland_reveal_threshold = 100000`, origin preferred/fallback population caps, consumed-pop display bands |
| `death_spread_pressure` | base pressure, island/mainland/wither/coastal gains, consumed-pop divisor, consumed-state divisor, containment reduction, public reveal multiplier, world-end multiplier, min/max clamps |
| `death_pulse_timing` | quiet origin first delay, island pattern delay, revealed spread pulse min/max, wither pulse interval, ghost refresh interval, defeat retry delay |
| `death_wither` | progress gain per pulse, decay with defenders, quarantine reduction, completion threshold, max concurrent targets by phase |
| `death_coastal_jump` | base cooldown, reveal cooldown, world-end cooldown, pressure reduction, minimum cooldown, max attempts per pulse |
| `death_ghost_scaling` | tier thresholds at 600/800/world-end, population divisor per ghost, state divisor per ghost, min/max per tier, world-end foothold spawn counts |
| `death_wasteland` | building removal levels, infrastructure damage/remove severity, active/recaptured modifier duration if timed modifiers are used |
| `death_world_end` | chaos threshold 1000, continent foothold minimums, remaining-continent target preference constants |
| `death_scenario_scale` | SCN-006 intensity Low/Medium/High/Maximum island counts, pressure multipliers, ghost tiers, foothold counts, report delays |

Shared constants:

- Add `chaos_meter_deaths_reason.death_consumption = 13`.
- Add `chaos_meter_deaths.death_consumption_chaos_weight = 0.10`.
- Extend `chaos_meter_sync_chaos_from_deaths_delta` with a Death reason branch mirroring zombie decay weighting.
- Add triggerable scenario constants listed above.

Modifier values belong in `common/modifiers/010_death_modifiers.txt`, but their tuning names should map back to this constants file or to documented static values if modifier fields cannot consume constants.

## Event Targets, Arrays, and Cleanup Plan

Use regular event targets for short chains and global event targets only when the pointer must survive beyond the current chain.

Regular event targets:

- `death_selected_state`: one selected origin/spread/scenario target.
- `death_consumed_previous_owner`: previous owner for logging and deaths attribution.
- `death_consumed_previous_controller`: previous controller for logging and war/recapture logic.
- `death_reveal_state_target`: reveal state used by immediate report events.
- `death_coastal_jump_target`: coastal jump target inside the current pulse.
- `death_wither_candidate`: candidate while selecting or validating wither target.
- `death_trigger_actor`: player/settings country or event actor that launched SCN-006.

Global event targets only if needed:

- `death_country`: acceptable if GUI/localisation needs a persistent Death country pointer; clear on defeat.
- `death_origin_state`: acceptable if details window or reports need persistent origin state localisation; state flag remains the durable gameplay marker.
- `death_current_reveal_state`: acceptable only for detail/report UI; clear on defeat or when superseded.

Prefer arrays/state flags over global event targets for multiple states:

- `global.death_active_wasteland_states`
- `global.death_wither_targets`
- `global.death_world_end_footholds`
- `death_origin_state`, `death_consumed_state`, `death_active_wasteland`, `death_recaptured_wasteland`, `death_wither_target`, `death_quarantine_line`, `death_purification_project`

Cleanup helpers:

- `death_cleanup_event_targets`: clears Death global event targets that exist.
- `death_clear_runtime_arrays`: clears active wasteland/wither/foothold arrays when Death is defeated or reinitialized.
- `death_cleanup_triggerable_scenario_context`: clears SCN-006 launch-only flags and temps even if target selection fails.
- `death_defeat_cleanup`: calls all cleanup helpers, converts active wastelands to recaptured wastelands, clears threat source, and stops scheduled pulses.

## Avoiding Broad Daily All-World Scans

Death should not use daily all-country/all-state polling. The safe scheduling model is:

1. Entry or SCN-006 setup creates `DTH`, consumes the first target, then schedules a hidden `DTH` country event for the next Death pulse.
2. Each hidden Death pulse performs one bounded operation and reschedules itself only while Death is active.
3. Wither logic iterates `global.death_wither_targets` or a bounded `DTH = { every_controlled_state = { ... } }` loop, never `every_state` from a daily all-world on action.
4. Wasteland recapture and defeat refresh use `on_state_control_changed`, whose scopes identify the exact changed state.
5. Coastal jump checks run after relevant pulses or when Death loses a foothold, with a numeric cooldown decremented by pulse intervals.
6. Ghost refresh runs from the hidden Death pulse or from world-end/scenario launch, not from a global daily hook.
7. World-threat refresh is called only when Death reveal/world-end/defeat state changes, not every day.

If the parent later wants a whole-world daily scan, that should be an explicit approval because it conflicts with current constraints.

## Migration and Call-Site Plan

1. Add constants first, including Death scenario ID `6`, Death type constants, Death tuning categories, and chaos-meter Death reason/weight.
2. Add Death triggers before effects so selection and launch guards can be used in all call sites.
3. Add core Death effects: initialization, country creation, state consumption, wasteland application, spread pressure, world threat refresh.
4. Wire the entry event to helpers without duplicating consumption logic.
5. Add on-action wrappers only for `on_state_control_changed` and other specific hooks needed for Death recapture/defeat, not daily polling.
6. Add spread/wither/coastal/ghost hidden pulse events that call helpers.
7. Add SCN-006 launch helpers and triggerable scenario registry/GUI/localisation call sites.
8. Add shared system integrations: `is_special_chaos_country`, `is_actual_nonhuman_country`, world threat docs/triggers, Death details/log mappings.
9. Document new helpers in the relevant Death docs and shared dynamic helper docs if `refresh_world_threat_state` is changed.

## Unsupported or Risky Fields to Validate During Implementation

- Division presence in a state: validate exact trigger scope for "non-Death enemy divisions present". Vanilla has country-scope division-in-state patterns; the final helper may need `controller = { divisions_in_state = { state = PREV ... } }` or a state array workaround.
- Direct strength damage to divisions in withering states: if no safe effect exists, use state modifiers/attrition and report the limitation instead of faking direct damage.
- Dynamic building removal: building type names are static. Use explicit blocks per building type, or `meta_effect` only if a dynamic building type is genuinely required.
- State resources cannot always be dynamically removed the same way buildings can. Prefer wasteland modifiers and documented resource disablement behavior if direct resource zeroing is unsupported.
- Timed flag `days =` fields may reject `constant:`. Assign to a variable first or use file-scoped `@` constants where required.
- `create_unit` template names may need static branches or `meta_effect` injection if template selection must be dynamic.
- Global event targets must be cleared manually. Avoid them for every active state.

## Validation Notes for Parent

Evidence gathered during this architecture pass:

- Existing triggerable scenario IDs currently run through `5`; Death should be added as `6`.
- Current GUI localisation exposes `#001` through `#005`; Death needs `chaosx.scenarios.entry.id.death: "#006"`.
- `triggerable_scenarios_initialize_registry`, type cycling, selection, and launch dispatch are explicit branch lists; Death requires explicit branches in each.
- `refresh_world_threat_state` currently counts zombies, holy realm, Mengele, and Fury. Death needs one additional `world_threat_source_death` block plus docs.
- The chaos meter already uses `chaos_meter_register_deaths` for exact death counts and already has a 0.10 special chaos-weight path for zombie outbreak decay. Death consumption should reuse that path by adding a Death reason and weight branch.
- `on_state_control_changed` scopes are suitable for recaptured wasteland and defeat refresh because the changed state is provided directly.
- No broad daily all-world scan is required for any requested Death subsystem.

## Simplifications, Omissions, and Blockers

No gameplay simplification was made because no gameplay files were patched. This handoff intentionally leaves exact numeric tuning to the parent implementation pass, but it names the constants and helper surfaces that should hold those values.

Implementation blockers to resolve during patching:

- Validate exact state-scope division trigger shape before writing `death_wither_target_has_blocking_defenders`.
- Validate whether any desired resource removal is supported directly; otherwise document the modifier-based wasteland approach.
- Decide whether `death_country` and `death_origin_state` need global event targets for UI/localisation, or whether state flags and static `DTH` are enough.
- Decide final alphabetical name sort slot for Death in the triggerable scenario view while preserving visible ID `#006`.

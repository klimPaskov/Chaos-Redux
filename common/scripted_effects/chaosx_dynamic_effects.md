# chaosx_dynamic_effects

This file documents reusable cross-system scripted effects defined in `common/scripted_effects/chaosx_dynamic_effects.txt`. Subsystem-private APIs belong beside their owning system even when several files inside that system call them.

## Reuse guidance

Use this registry only for effects with demonstrated call-site breadth across unrelated systems or event families. Reusable logic confined to one subsystem belongs in that subsystem's scripted-effect files and dedicated reference documentation.

## Table of contents

- [chaosx_apply_startup_history_grants](#chaosx_apply_startup_history_grants)
- [chaosx_startup_mark_existing_scientists](#chaosx_startup_mark_existing_scientists)
- [chaosx_startup_clear_generated_scientist_helper_flags](#chaosx_startup_clear_generated_scientist_helper_flags)
- [call_natural_disaster](#call_natural_disaster)
- [air_contamination_register_natural_disaster_source](#air_contamination_register_natural_disaster_source)
- [air_contamination_prepare_natural_source_monthly](#air_contamination_prepare_natural_source_monthly)
- [natural_disaster_register_relief_recipient_country](#natural_disaster_register_relief_recipient_country)
- [natural_disaster_unregister_relief_recipient_country_if_inactive](#natural_disaster_unregister_relief_recipient_country_if_inactive)
- [natural_disaster_transfer_pending_jobs_for_state](#natural_disaster_transfer_pending_jobs_for_state)
- [natural_disaster_append_abnormal_history_record](#natural_disaster_append_abnormal_history_record)
- [natural_disaster_update_abnormal_history_record](#natural_disaster_update_abnormal_history_record)
- [natural_disaster_rebuild_abnormal_gui_view](#natural_disaster_rebuild_abnormal_gui_view)
- [modify_value_based_on_chaos_tier](#modify_value_based_on_chaos_tier)
- [calculate_economy_scaled_factory_grant](#calculate_economy_scaled_factory_grant)
- [damage_buildings_in_random_states](#damage_buildings_in_random_states)
- [get_random_sea_region](#get_random_sea_region)
- [clear_special_chaos_country_civilian_effects](#clear_special_chaos_country_civilian_effects)
- [refresh_world_threat_state](#refresh_world_threat_state)
- [Liberations release coordinator](#liberations-release-coordinator)
- [apply_crisis_rescue_event_weight_adjustments](#apply_crisis_rescue_event_weight_adjustments)
- [evaluate_random_event_active_pool_candidate](#evaluate_random_event_active_pool_candidate)
- [count_dynamic_major_weight_pool_events](#count_dynamic_major_weight_pool_events)
- [calculate_dynamic_major_weight_gain](#calculate_dynamic_major_weight_gain)
- [apply_dynamic_major_weight_gain_after_minor](#apply_dynamic_major_weight_gain_after_minor)
- [apply_state_population_loss_without_recruitable_manpower_gain](#apply_state_population_loss_without_recruitable_manpower_gain)
- [apply_exact_state_civilian_population_loss](#apply_exact_state_civilian_population_loss)

## chaosx_apply_startup_history_grants

This reusable startup helper lives in `common/scripted_effects/chaosx_startup_history_effects.txt`. It applies additive country and state setup that used to require copied vanilla history overrides.

Scope: Country scope, called once from `on_startup` through a random country. It uses static country and state scopes internally.

Inputs: none.

Outputs and side effects:

- Sets `chaosx_startup_history_grants_applied` globally to prevent duplicate grants.
- Calls one country-specific `chaosx_startup_grant_<tag>` effect per affected vanilla country.
- Grants starting technologies, equipment stockpiles, generated Chaos scientists, chemical commander traits, startup tuning variables, breakthrough progress, delayed biowarfare events, the British anthrax project, and startup chemical/biowarfare facilities.
- Uses `popup = no` on startup technology grants to avoid research popups.
- Syncs chemical tactic unlocks and preferred-weight suppression ideas after migrated technology grants, so behavior does not depend on on_action file order.
- Reads stockpile amounts, facility level, breakthrough values, and delayed-event timing from `common/script_constants/startup_history_constants.txt`.
- Adds facilities only when the expected starting owner still owns the state and the state lacks that facility type.

Do not use this effect for new custom country packages that require real history files before startup. Do not put `recruit_character` here; the engine only accepts it in history files. Do not move country-specific Chaos Redux scientists into `history/general`; that folder is for generic character pools, not specific country assignments. Named existing-country startup scientists should be created with `generate_scientist_character` in the relevant country grant with explicit portrait, gender, skills, and traits when any, then immediately selected with `random_scientist`, named with `set_character_name`, assigned the intended portrait if needed, and marked with a persistent identity flag for later scripted references.

Example:

```txt
on_startup = {
	effect = {
		random_country = {
			chaosx_apply_startup_history_grants = yes
		}
	}
}
```

## call_natural_disaster

This is the public country-scope entry point for Event 013. It validates a
disaster request, resolves exact states, allocates one sequence, persists every
delayed job in the affected state's current controller queue, and creates at most one Event 013
history row. Family impact, Deaths registration, damage, reports, news,
aftermath cards, and follow-ups remain internal to Event 013.

Inputs are temporary variables set immediately before the call:

- `natural_disaster_call_caller_type`: `natural_disaster_caller.*`
- `natural_disaster_call_caller_event_id`: positive numeric source event id
- `natural_disaster_call_family`: a specific `natural_disaster_family.*`, or `random`
- `natural_disaster_call_family_group`: a normal or abnormal `natural_disaster_family_group.*`; leave `random` when a specific family is supplied
- `natural_disaster_call_target_mode`: `natural_disaster_target_mode.*`
- `natural_disaster_call_target_region`: strategic-region id for `selected_region`
- `natural_disaster_call_origin_state_supplied`: set to `1` only after saving `natural_disaster_call_origin_state`; required for direct ashfall, lahar, and tsunami requests
- `natural_disaster_call_origin_family`: physical cause at the supplied origin; ashfall/lahar accept volcanic eruption or massive eruption, while tsunami accepts a compatible seismic, volcanic, rupture, or ocean-impact cause
- `natural_disaster_call_origin_medium`: `natural_disaster_origin_medium.*`; normally `none` or `land_impact`, and required as `ocean_impact` for a meteor-origin tsunami
- `natural_disaster_call_severity`: `natural_disaster_severity.*`
- `natural_disaster_call_sequence_mode`: `natural_disaster_sequence_mode.*`
- `natural_disaster_call_sequence_count`: optional exact primary-impact count
- `natural_disaster_call_news_policy`: `natural_disaster_news_policy.*`
- `natural_disaster_call_report_policy`: `natural_disaster_report_policy.*`; every value preserves the affected country's delayed report, while caller/global select additional recipients and `silent` suppresses only additional distribution
- `natural_disaster_call_aftermath_policy`: `natural_disaster_aftermath_policy.*`
- `natural_disaster_call_chain_policy`: `natural_disaster_chain_policy.*`
- `natural_disaster_call_death_scale`: optional Deaths multiplier, default `1.0`
- `natural_disaster_call_building_scale`: optional building-damage multiplier, default `1.0`
- `natural_disaster_call_damage_scale`: compatibility alias used only when `building_scale` was not supplied
- `natural_disaster_call_warning_scale`: optional warning-chance multiplier; reusable external calls retain this chance, while the first impact of a random Event 013 or cluster season always receives a delayed warning
- `natural_disaster_call_recovery_scale`: optional recovery-burden multiplier
- `natural_disaster_call_supply_scale`: optional state-disruption multiplier
- `natural_disaster_call_caller_cost_checked`: proof flag required for deity and hostile-actor callers
- `natural_disaster_call_caller_cooldown_checked`: proof flag required for deity and hostile-actor callers
- `natural_disaster_call_target_legitimacy_checked`: proof flag required for deity and hostile-actor callers
- `natural_disaster_call_log_mode`: `natural_disaster_log_mode.*`
- `natural_disaster_call_scenario_type`: Disaster Barrage family mix, validated against `natural_disaster_scenario_type.*`
- `natural_disaster_call_scenario_intensity`: Disaster Barrage intensity, validated against `natural_disaster_scenario_intensity.*`
- `natural_disaster_call_evolution_override_supplied` and `natural_disaster_call_evolution_override`: optionally request a specific stage from baseline through Evolution III; a stage above the current world evolution requires the scenario/debug-only manual evolution proof
- `natural_disaster_call_manual_evolution_bypass`: permits a manual scenario or debug call to use its intensity-selected evolution without unlocking or recording that evolution globally; rejected for every other caller type
- `natural_disaster_call_manual_abnormal_bypass`: permits an abnormal scenario to bypass only the abnormal-family cooldown; accepted only for scenario or debug callers
- `natural_disaster_call_target_state_supplied`: set to `1` in the same effect chain after saving `natural_disaster_call_target_state`
- `natural_disaster_call_target_country_supplied`: set to `1` in the same effect chain after saving `natural_disaster_call_target_country`

Target proof inputs and weaponized-caller proof inputs are binary. Values other than `0` or `1` are rejected instead of being treated as an implicit proof.

Optional regular event targets:

- `natural_disaster_call_target_state` plus `natural_disaster_call_target_state_supplied = 1` for `selected_state`
- `natural_disaster_call_target_country` plus `natural_disaster_call_target_country_supplied = 1` for `selected_country`
- `natural_disaster_call_origin_state` plus `natural_disaster_call_origin_state_supplied = 1` for origin-dependent ashfall, lahar, or tsunami calls
- either or both target/proof pairs for `caller_provided`

`natural_disaster_call_causal_context_*`, sequence-id and segment overrides, and `natural_disaster_call_internal_chain_override` are reserved for Event 013's own persisted physical-chain continuation. Their proof is validated against the live source card, sequence, evolution, family, and target; other callers cannot use them to bypass evolution or abnormal locks.

`natural_disaster_log_mode.none` is likewise reserved for that validated internal continuation. Standalone external, scenario, cluster, or debug calls must choose a history-bearing log mode so an accepted top-level sequence cannot become an unlogged disaster.

Outputs are temporary variables. A caller that needs to read them after the
scripted effect should initialize them in its outer effect block first:

- `natural_disaster_call_result`: accepted or rejected
- `natural_disaster_call_reject_reason`: the exact validation failure
- `natural_disaster_call_sequence_id`: allocated sequence id, or `0`
- `natural_disaster_call_primary_job_count`: queued primary impacts
- `natural_disaster_call_skipped_primary_count`: planned primary impacts omitted because their fixed target domain contained no valid pair
- `natural_disaster_call_resolved_primary_family`: the first successfully scheduled `natural_disaster_family.*`, or `0`
- `natural_disaster_call_has_resolved_primary_state`: proof that `natural_disaster_call_resolved_primary_state` was saved by this call
- `natural_disaster_call_has_resolved_primary_country`: proof that `natural_disaster_call_resolved_primary_country` was saved by this call
- `natural_disaster_call_resolved_target_region`: echoes the supplied strategic-region id only for a successful `selected_region` call

Successful calls also expose regular event targets `natural_disaster_call_resolved_primary_state` and `natural_disaster_call_resolved_primary_country`. Callers must test the matching numeric proof output because a regular event target from an earlier request can still exist in the same effect chain. These outputs always describe the first scheduled primary hit, never the last retry or last hit in a multi-impact sequence.

Side effects:

- reserves a unique delayed date for every subevent in the sequence
- opens with bounded weighted family draws, then visits the complete evolution-valid family pool once while preserving the caller's requested family group or Disaster Barrage type; selected state, country, and region scopes never widen during either pass
- requires immutable family geography and compatible origin tuples before scoring a state, so infrastructure, resources, coast, agriculture, and prior hazard history can improve priority but cannot make an impossible family or origin physically valid
- stores queued state scopes and metadata on each affected state's current controller
- stores active aftermath data on affected states
- merges a later caller-selected hit into an already open card for that exact state, with the latest sequence owning the card while accumulated recovery work and prior losses remain visible
- guarantees the affected state's current controller its delayed report whenever reports are enabled; `global` additionally delivers the same family report to every country
- may create one Event 013 history row according to `natural_disaster_call_log_mode`
- resets all public inputs after the call so a second request cannot inherit them

Validation is fail-closed. Unknown enums, conflicting specific family and family-group selectors, invalid scaling or sequence counts, missing or unproved target scopes, physically incompatible states, unproven hostile/deity calls, invalid scenario metadata, and unauthorized abnormal bypasses return `rejected` with a stable reject reason and queue no work. A specific family is never substituted. A call that finds no eligible target restores the global sequence counter and leaves the caller's last accepted sequence id, anchor flag, and hit counts unchanged.

Example:

```txt
GER = {
	set_temp_variable = { natural_disaster_current_family = constant:natural_disaster_family.earthquake }
	random_owned_controlled_state = {
		limit = { natural_disaster_is_valid_family_target = yes }
		save_event_target_as = natural_disaster_call_target_state
	}
}
set_temp_variable = { natural_disaster_call_caller_type = constant:natural_disaster_caller.external_event }
set_temp_variable = { natural_disaster_call_caller_event_id = 77 }
set_temp_variable = { natural_disaster_call_family = constant:natural_disaster_family.earthquake }
set_temp_variable = { natural_disaster_call_target_mode = constant:natural_disaster_target_mode.selected_state }
set_temp_variable = { natural_disaster_call_target_state_supplied = 1 }
set_temp_variable = { natural_disaster_call_severity = constant:natural_disaster_severity.severe }
set_temp_variable = { natural_disaster_call_sequence_mode = constant:natural_disaster_sequence_mode.single }
call_natural_disaster = yes
```

## air_contamination_register_natural_disaster_source

Purpose: Register a very small wildfire-smoke or volcanic-ash contribution after Event 013 resolves a physical impact. The effect lives in `common/scripted_effects/air_cleanliness_natural_source_effects.txt`.

Scope: State.

Inputs:

- `natural_disaster_current_family` temporary variable
- `natural_disaster_current_severity` temporary variable
- state variables `natural_disaster_sequence_id` and `natural_disaster_impact_index`

Defaults: Unsupported families, wildfires below regional severity, disabled Air Cleanliness, and the Final Silence lock add nothing.

Outputs and side effects:

- Adds the severity-scaled amount to `global.air_contamination_natural_source_reservoir_bp`.
- Clamps the reservoir from zero through `constant:air_contamination_natural_source.monthly_cap_bp`.
- Records the contributing sequence, impact index, and family on the state so the same physical impact cannot register twice.

Example:

```txt
natural_disaster_prepare_family_profile = yes
natural_disaster_prepare_severity_profile = yes
air_contamination_register_natural_disaster_source = yes
```

## air_contamination_prepare_natural_source_monthly

Purpose: Expose the current smoke-and-ash reservoir to the existing host-owned monthly Air Contamination calculation, then dissipate it once.

Scope: Country, called by the current host coordinator.

Inputs: Persistent global natural-source reservoir and the current `global.date`.

Defaults: Missing reservoir and contribution variables initialize to zero.

Outputs and side effects:

- Writes the current contribution to `global.air_contamination_natural_source_bp`.
- Outputs `air_monthly_natural_bp` as a temporary variable for the caller.
- Reduces the reservoir by `constant:air_contamination_natural_source.monthly_decay_bp`.
- Uses `global.air_contamination_natural_source_last_tick_date` to prevent a second decay on the same date.
- Exposes zero current contribution while Final Silence is locked, while the hidden reservoir still decays.

Example:

```txt
air_contamination_prepare_natural_source_monthly = yes
add_to_temp_variable = { air_contamination_delta_bp = air_monthly_natural_bp }
```

## natural_disaster_resolve_ordinary_family

Internal Event 013 caller-scope helper for an Evolution III random request whose first abnormal draw is blocked by the global abnormal-family cooldown. It draws only from the ordinary family pool before target resolution, so the dispatcher and canonical API never promise a blocked abnormal family and never substitute one specific family for another.

Input: `natural_disaster_force_ordinary_pool > 0` in the random resolver path. Output: `natural_disaster_current_family` set to one ordinary family. It does not allocate a sequence, select a target, create history, or change the cooldown. Example: `natural_disaster_resolve_ordinary_family = yes` after an unpresented random abnormal draw fails `natural_disaster_abnormal_family_is_allowed`.

## natural_disaster_register_relief_recipient_country

This Event 013 internal helper adds a country to the bounded foreign-relief recipient ledger when it controls at least one actionable recovery card. Chain-only warning cards and cards marked as unresolved territory do not qualify.

Scope: Country.

Inputs: none. The helper reads the current country's controlled states and their Event 013 card flags.

Defaults: it does nothing when the country has no actionable recovery card or is already registered.

Outputs and side effects:

- adds `THIS` to `global.natural_disaster_relief_recipient_countries` at most once;
- runs only from recovery-card activation or transferred-responsibility registration;
- performs no whole-world country iteration.

Example:

```txt
controller = {
	natural_disaster_register_relief_recipient_country = yes
}
```

## natural_disaster_unregister_relief_recipient_country_if_inactive

This Event 013 internal helper removes a country from the foreign-relief recipient ledger after its last actionable recovery card leaves its control. A second qualifying card keeps the country registered.

Scope: Country.

Inputs: none. The helper reads the current country's controlled states and its existing ledger membership.

Defaults: it does nothing when another actionable recovery card remains or the country is not registered.

Outputs and side effects:

- removes `THIS` from `global.natural_disaster_relief_recipient_countries` only after the last qualifying card closes or transfers away;
- is called by ordinary card closure and former-controller transfer cleanup;
- leaves final eligibility to the decision layer, which independently rechecks country existence, card state, war, and variant-specific requirements.

Example:

```txt
controller = {
	natural_disaster_unregister_relief_recipient_country_if_inactive = yes
}
```

## natural_disaster_transfer_pending_jobs_for_state

This Event 013 internal helper migrates all 26 aligned delayed-job snapshot arrays for one active disaster state when state control changes. It preserves the family, severity, sequence, dates, warning result, damage report, follow-up context, path context, and globally reserved due date, schedules replacement worker wakeups on the new responsible country, and leaves the former country's unrelated queue rows untouched.

Scope: Former responsible country. It is called only by `natural_disaster_handle_state_control_change` from the narrow `on_state_control_changed` hook.

Inputs:

- `event_target:natural_disaster_transfer_state`: the active state whose responsibility changed
- `event_target:natural_disaster_new_responsible_country`: a valid country that owns or controls the state

Outputs and side effects:

- removes matching indices from `natural_disaster_job_target_state_entries`, `natural_disaster_job_type_entries`, `natural_disaster_job_sequence_id_entries`, and `natural_disaster_job_due_date_entries`
- appends the same aligned rows to the new responsible country
- preserves the existing global sequence/day reservation instead of reserving a replacement date
- schedules a new `chaosx.nr13.2` worker for the exact remaining delay; a due-today row uses the engine-supported zero-day wakeup, while only an already-overdue row is clamped to zero
- clears the former country's queue-active flag only when no other delayed jobs remain

Do not call this effect directly from an event. The transfer handler owns mission-pointer cleanup, card registration, and responsibility validation around it.

## natural_disaster_append_abnormal_history_record

This Event 013 state-scope helper creates one immutable-identity abnormal-map
record for the current state and sequence. It writes an aligned global ledger
containing the state pointer, family, origin family, severity, sequence,
segment, dates, casualties, warning result, aftermath phase and scores, chain
risk, damage directions, linked state, display status, response result, and
relief state. Repeated registration of the same state/sequence updates the same
row; a later abnormal sequence in the same state appends a distinct row.

Inputs:

- current state disaster variables and flags
- a valid \`natural_disaster_sequence_id\`

Outputs and side effects:

- appends one row to the \`global.natural_disaster_abnormal_history_*_entries\` arrays
- stores the row index in \`natural_disaster_abnormal_history_record_index\`
- stores the row identity in \`natural_disaster_abnormal_history_registered_sequence_id\`

Defaults are prepared by \`natural_disaster_prepare_abnormal_history_record\`;
missing optional dates, scores, damage directions, and linked-state data become
zero rather than reading stale state data.

Example:

\`\`\`txt
event_target:natural_disaster_impact_state = {
	natural_disaster_append_abnormal_history_record = yes
}
\`\`\`

## natural_disaster_update_abnormal_history_record

This Event 013 state-scope helper refreshes the current abnormal row while its
state/sequence identity still matches. It fails closed when the state has since
received an ordinary disaster or another abnormal sequence, so an archived row
cannot be rewritten by the state's live disaster variables. Card closure calls
it after setting the closed phase and path status, freezing the final response
result before cleanup.

Inputs:

- \`natural_disaster_abnormal_history_record_index\`
- \`natural_disaster_abnormal_history_registered_sequence_id\`
- current state disaster variables and flags

Outputs and side effects:

- updates only the aligned global row whose recorded sequence matches the live sequence
- leaves every earlier row for the same state unchanged

Example:

\`\`\`txt
set_variable = { natural_disaster_card_state = constant:natural_disaster_card_state.closed }
set_variable = { natural_disaster_phase = constant:natural_disaster_phase.closed }
set_variable = { natural_disaster_path_status = constant:natural_disaster_path_status.closed }
natural_disaster_update_abnormal_history_record = yes
\`\`\`

## natural_disaster_rebuild_abnormal_gui_view

This country-scope presentation helper builds the five-card abnormal map from
record indices, not live state fields. Active view candidates are the
controller's active abnormal rows. History view candidates are every global
abnormal row, including multiple sequences in the same physical state. A
globally monotonic rebuild id makes the temporary exclusion marks safe when
several countries rebuild the global history view.

Inputs:

- \`natural_disaster_abnormal_history_view\` country flag
- active \`natural_disaster_abnormal_states\` when using the live view
- aligned \`global.natural_disaster_abnormal_history_*_entries\` ledger

Outputs and side effects:

- rebuilds aligned \`natural_disaster_gui_*_entries\` view arrays
- selects the highest-priority sequence by pending impact, warning state, open recovery, chain risk, severity, and date, then orders that sequence's focused records by physical path segment
- preserves a dormant zero-row history view without dereferencing a missing selected record

The companion \`natural_disaster_gui_selected_record_exists\` trigger guards every
selected-row scripted-GUI read. The selected layer triggers route the snapshot
origin/family to rupture, meteor, eruption, tsunami, or storm frame sheets.

Example:

\`\`\`txt
set_country_flag = natural_disaster_abnormal_history_view
natural_disaster_rebuild_abnormal_gui_view = yes
set_country_flag = natural_disaster_abnormal_map_open
\`\`\`

## chaosx_startup_mark_existing_scientists

This startup helper lives in `common/scripted_effects/chaosx_startup_history_effects.txt`. It marks all scientists already present in the current country before a country startup grant generates named Chaos Redux scientists.

Scope: Country scope.

Inputs: none.

Outputs and side effects:

- Sets `chaosx_startup_scientist_preexisting` on every current-country scientist.
- Allows later `random_scientist` blocks to target only newly generated startup scientists.

Example:

```txt
ENG = {
	chaosx_startup_mark_existing_scientists = yes
	generate_scientist_character = {
		portrait = GFX_portrait_ENG_paul_fildes
		gender = male
		traits = { scientist_trait_bright }
		skills = {
			specialization_biowarfare = 2
		}
	}
	random_scientist = {
		limit = {
			NOT = { has_character_flag = chaosx_startup_scientist_preexisting }
			NOT = { has_character_flag = chaosx_startup_scientist_named }
		}
		set_character_name = ENG_paul_fildes
		set_character_flag = chaosx_startup_scientist_named
		set_character_flag = chaosx_scientist_eng_paul_fildes
	}
	chaosx_startup_clear_generated_scientist_helper_flags = yes
}
```

## chaosx_startup_clear_generated_scientist_helper_flags

This startup helper lives in `common/scripted_effects/chaosx_startup_history_effects.txt`. It removes temporary startup-selection flags after a country grant finishes naming its generated scientists.

Scope: Country scope.

Inputs: none.

Outputs and side effects:

- Clears `chaosx_startup_scientist_preexisting` and `chaosx_startup_scientist_named` from every current-country scientist.
- Leaves persistent identity flags such as `chaosx_scientist_pol_franciszek_witaszek` intact.

Example:

```txt
POL = {
	chaosx_startup_mark_existing_scientists = yes
	generate_scientist_character = {
		portrait = GFX_portrait_POL_franciszek_witaszek
		gender = male
		traits = { scientist_trait_resourceful }
		skills = {
			specialization_biowarfare = 2
		}
	}
	random_scientist = {
		limit = {
			NOT = { has_character_flag = chaosx_startup_scientist_preexisting }
			NOT = { has_character_flag = chaosx_startup_scientist_named }
		}
		set_character_name = POL_franciszek_witaszek
		set_character_flag = chaosx_startup_scientist_named
		set_character_flag = chaosx_scientist_pol_franciszek_witaszek
	}
	chaosx_startup_clear_generated_scientist_helper_flags = yes
}
```
## evaluate_random_event_active_pool_candidate

This reusable event-system helper lives in `common/scripted_effects/chaosx_logic_effects.txt`. It checks whether a temp `event_id` is a current automatic random-pool entry before weight and UI filter checks are applied.

Inputs: `event_id` temp variable.
Output: `event_active_pool_candidate_is_valid` temp variable (`1` or `0`).

It excludes disabled events, fired non-repeatable events, and any other permanent-unavailable gates added to the helper. Repeatable events remain valid after firing as long as they stay in the pool.

Example:

```txt
set_temp_variable = { event_id = global.all_events^i }
evaluate_random_event_active_pool_candidate = yes
if = {
	limit = { check_variable = { event_active_pool_candidate_is_valid > 0 } }
	# Candidate is in the current automatic random pool.
}
```

## count_dynamic_major_weight_pool_events

This event-system helper lives in `common/scripted_effects/chaosx_logic_effects.txt`. It counts active random-pool entries for the dynamic major-gain formula, using `evaluate_random_event_active_pool_candidate` so counting and random selection share the same non-weight eligibility gate.

Inputs: `global.major_events`, `global.fire_once_events`, and `global.repeatable_events`.
Outputs: `global.current_dynamic_major_active_major_count` and `global.current_dynamic_major_active_non_major_count`.
Side effects: writes only the two global count variables and temp loop helpers.

The helper counts active major entries separately from active non-major entries. Fire-once entries leave the count after firing; repeatable entries remain in the count when they are still active, even if their current weight is low.

Example:

```txt
count_dynamic_major_weight_pool_events = yes
```

## calculate_dynamic_major_weight_gain

This event-system helper lives in `common/scripted_effects/chaosx_logic_effects.txt`. It calculates the current per-minor major-event gain from the configured baseline and active pool composition:

```text
gain = global.major_event_weight_per_minor * active_non_major / active_major * baseline_major / baseline_non_major
```

Inputs: configured baseline in `global.major_event_weight_per_minor`; baseline constants in `event_system_dynamic_major_gain`; current pool arrays.
Outputs: `global.current_dynamic_major_weight_gain`, `global.current_dynamic_major_active_major_count`, and `global.current_dynamic_major_active_non_major_count`.
Defaults: if active major count or active non-major count is zero, the gain is set to `0` and no division is attempted.
Side effects: refreshes active pool counts, rounds the result with `round_temp_variable`, and clamps it to `settings_advanced_bounds.major_weight_per_minor`.

Example:

```txt
calculate_dynamic_major_weight_gain = yes
log = "Current dynamic major gain: [?global.current_dynamic_major_weight_gain]"
```

## apply_dynamic_major_weight_gain_after_minor

This event-system helper lives in `common/scripted_effects/chaosx_logic_effects.txt`. It is the pacing hook used after one minor global pacing event. It calls `calculate_dynamic_major_weight_gain`, skips if the calculated gain is `0`, and adds the current calculated gain to each active, unfired major event.

Inputs: active pool arrays and current major event weights.
Outputs: updated `global.event_weights` entries for active major events and `global.current_major_event_weight` for status display.
Side effects: locked Event 91 is kept at weight `0`; reset major weights stored as `1` for engine safety are treated as `0` before gain is added.

Example:

```txt
update_major_event_weights = {
	apply_dynamic_major_weight_gain_after_minor = yes
}
```

## modify_value_based_on_chaos_tier

This effect converts a base value into a chaos-tier-scaled value. It reads the global flag `chaos_tier`, starts from `base_value`, then adds `add_value * tier_bucket` into the result. The produced output is the temp variable `modified_value`. Tier buckets are handled as `0`, `1`, `2`, `3`, and `4` for any tier above 3.

Use this when you want one place to control chaos scaling and keep call sites short. The usual call flow is to set `base_value`, set `add_value`, call the effect, and then consume `var:modified_value` in another effect like `add_popularity`.

Inputs: `base_value` (required), `add_value` (required).  
Output: `modified_value` (temp variable).  

Important: this effect reads `add_value` by name. If a caller sets a different variable name (for example `base_add`), that value is not used by this effect.

Example:

```txt
set_temp_variable = { base_value = 0.10 }
set_temp_variable = { add_value = 0.02 }
modify_value_based_on_chaos_tier = yes
# result in var:modified_value
```

## calculate_economy_scaled_factory_grant

This country-scope effect converts the current country's civilian and military factory count into a capped grant count for foreign investment, reconstruction, sponsor-aid, or similar systems. It does not create buildings by itself. It only writes the temp variable `economy_scaled_factory_grant_count`, so the caller can decide which building type to place and in which target scope.

Inputs:

- `economy_scaled_factory_grant_step`: factories per granted building.
- `economy_scaled_factory_grant_min`: minimum grant count.
- `economy_scaled_factory_grant_cap`: maximum grant count.

Output:

- `economy_scaled_factory_grant_count`

Side effects:

- uses `economy_scaled_factory_grant_pool` as a temp helper.
- reads `num_of_civilian_factories` and `num_of_military_factories` from the current country.

Example:

```txt
set_temp_variable = { economy_scaled_factory_grant_step = constant:my_system.factory_step }
set_temp_variable = { economy_scaled_factory_grant_min = constant:my_system.factory_min }
set_temp_variable = { economy_scaled_factory_grant_cap = constant:my_system.factory_cap }
calculate_economy_scaled_factory_grant = yes
FROM = {
	while_loop_effect = {
		limit = { check_variable = { economy_scaled_factory_grant_count > 0 } }
		random_owned_controlled_state = {
			add_extra_state_shared_building_slots = 1
			add_building_construction = { type = industrial_complex level = 1 instant_build = yes }
		}
		subtract_from_temp_variable = { economy_scaled_factory_grant_count = 1 }
	}
}
```

## damage_buildings_in_random_states

This is the heavy reusable block for random sabotage-style damage. It runs in country scope, calculates how many controlled states should be targeted, picks random owned/controlled states that have at least one eligible building type, applies optional population delta for each selected state, and then performs random building-damage rolls. Because building type must be static in `damage_building`, this effect uses `meta_effect` so damage amount can stay dynamic through `[DMG]`.

Use this whenever you need "damage random buildings across random states" behavior. It exists to avoid rewriting a long random-list/meta-effect pipeline in each event.

Inputs you can set before calling:

- `buildings_to_damage_per_state`: how many damage rolls per selected state.
- `percent_of_states_to_target`: fraction of controlled states to process.
- `damage_modifier`: damage amount per roll.
- `state_population_percent`: decimal population delta per selected state (for example `-0.001` is -0.1%).

Default/fallback behavior when values are not provided or are effectively zero:

- `percent_of_states_to_target = 0.1`
- `damage_modifier = 0.25`
- `buildings_to_damage_per_state = 3`
- `state_population_percent` falls back to `-0.001` effective behavior (internal per-thousand fallback is `-1`)

Main result is state building damage plus manpower delta from the state population calculation. The effect also uses temporary helper variables such as `num_controlled_states`, `num_states_to_target`, and `pop_loss`.

Eligible building types currently covered: `infrastructure`, `arms_factory`, `industrial_complex`, `air_base`, `supply_node`, `rail_way`, `naval_base`, `bunker`, `coastal_bunker`, `dockyard`, `anti_air_building`, `synthetic_refinery`, `fuel_silo`, `radar_station`, `rocket_site`, `nuclear_reactor`, `nuclear_reactor_heavy_water`, `commercial_nuclear_reactor`.

Example:

```txt
set_temp_variable = { state_population_percent = -0.001 }
set_temp_variable = { buildings_to_damage_per_state = 3 }
set_temp_variable = { damage_modifier = 0.25 }
set_temp_variable = { percent_of_states_to_target = 0.1 }
damage_buildings_in_random_states = yes
```

## get_random_sea_region

This effect picks one sea-region ID from a curated `random_list` and writes it to `global.rand_sea_region`. It is used as a helper before a second step that needs to inject a dynamic region token via `meta_effect`.

Use this when you want a reusable random sea region selector that can feed dynamic effects such as mine placement or region-based operations.

Input: none.  
Output: `global.rand_sea_region`.

Some IDs are intentionally repeated in the list, which gives those regions more weight than single-entry regions.

Example:

```txt
hidden_effect = { get_random_sea_region = yes }
meta_effect = {
 text = {
  add_mines = { region = [SEA_REGION] amount = 1000 }
 }
 SEA_REGION = "[?global.rand_sea_region|.0]"
}
```

## clear_special_chaos_country_civilian_effects

This country-scope helper removes the `mass_panic` flag and `galaxies_mix` idea from a special non-human country when a bounded caller explicitly invokes it.

Inputs: none.

Side effects: clears only those two civilian effects when present.

The existing `on_weekly` caller remains commented out because it would iterate every country and the cleanup contract is incomplete. The helper is retained as an explicit future hook rather than treated as live periodic infrastructure.

Example:

```txt
if = {
	limit = { is_special_chaos_country = yes }
	clear_special_chaos_country_civilian_effects = yes
}
```

## refresh_world_threat_state

This is the shared global aggregator for the mod-wide world-threat flag. It rebuilds `global.world_threat_source_count` from registered source flags and then sets or clears the global flag `world_in_threat`.

Use this whenever a threat-specific system changes whether its own source flag should be active. The threat-specific system is responsible for setting or clearing its own source flag first, then calling this effect. The current registered source set includes:

- `world_threat_source_zombies`
- `world_threat_source_holy_realm`
- `world_threat_source_mengele`
- `world_threat_source_fury`
- `world_threat_source_death`
- `world_threat_source_cannibalism`
- `world_threat_source_black_plague`
- `world_threat_source_resources_found_caves`
- `world_threat_source_brilliant_scientist`

Future threats should follow the same pattern:

1. add a source flag with a descriptive name such as `world_threat_source_aliens`
2. extend `refresh_world_threat_state` with one more source-flag count block
3. call the refresh effect whenever that source activates or deactivates

Output:

- `global.world_threat_source_count`
- `world_in_threat` global flag

Side effects:

- clears `world_in_threat` automatically when no registered source flags remain active

Example:

```txt
if = {
	limit = { my_threat_is_active = yes }
	set_global_flag = world_threat_source_my_threat
}
else = {
	clr_global_flag = world_threat_source_my_threat
}
refresh_world_threat_state = yes
```

## Liberations release coordinator

These reusable transaction effects live in `common/scripted_effects/chaosx_liberation_release_effects.txt`. They coordinate exact releases between Event 005 Soviet Collapse and Event 006 Independence Wave without allowing either event to inherit the other's origin, tree, mechanics, or AI.

Scope: the incident's coordinating country. Host reservation effects change to the supplied host scope, country reservation effects read regular event targets, and `liberation_release_add_state_reservation` is called in the exact state scope.

Required temporary inputs for `liberation_release_begin_plan`:

- `liberation_call_mode`: one `liberation_plan_mode.*` value.
- `liberation_call_expected_country_count`: the exact combined country-row count; zero and partial plans fail closed.
- `liberation_call_plan_owner`: Event 005, Event 006, or the joint owner enum.

Candidate publishers supply `liberation_candidate_package_id`, `liberation_candidate_plan_owner`, `liberation_candidate_reservation_group`, `liberation_candidate_territory_level`, `liberation_candidate_force_level`, and the regular event targets `liberation_candidate_country`, `liberation_candidate_anchor`, and `liberation_candidate_primary_host`. State rows additionally use `liberation_candidate_state_host` and `liberation_candidate_state_role`. Before appending a provisional candidate's anchor row, save `global.liberation_plan_states^num` as temporary `liberation_candidate_state_row_start` so `liberation_release_rollback_candidate_reservation` can remove only that tail.

Outputs: temporary `liberation_candidate_reject_reason` after host, country, or state reservation; global `liberation_plan_last_failure` after validation; aligned global country, state, host, and rejection ledgers; and phase/validity flags read by the execution barrier. There are no permissive defaults: a missing owner, event target, anchor, positive expected count, participant flag, or array alignment rejects or aborts the plan.

Side effects: reserves one surviving state for each host, marks absent target tags and exact states with the current plan ID, records original owners/controllers, increments per-host planned losses, and clears every transient scope mark on commit or abort. It does not select packages, release a country, transfer a state, create units, or apply Event 005/Event 006 content. Candidate rollback is valid only while that provisional anchor candidate owns the aligned array tail.

`liberation_release_select_and_reserve_host_state` is the reusable country-scope host-survival selector. It has no permissive input: the current country is the host. It reuses an existing plan row or chooses the owned/controlled capital, first owned/controlled core, first owned core, first owned/controlled state, or first owned state in that order. It outputs `liberation_candidate_reject_reason`, saves `liberation_candidate_protected_state`, and appends aligned host snapshot, protected-state, and original-capital rows when successful. `liberation_release_select_first_host_state_candidate` is its internal deterministic array helper and must not be called without a populated temporary `liberation_host_state_candidates` array.

Event 006's subsystem effects `independence_wave_expand_selected_packages_for_current_phase` and `independence_wave_expand_selected_optional_territory` live in `006_independence_wave_package_planner_effects.txt`. They require an open plan plus aligned Event 006 selected-package and country-row arrays. The dispatcher reuses each stable package publisher after rehydrating its frozen country, anchor, host, owner, and package ID. The public expansion effect runs every compact pass before any extended pass, records optional-state trims, restores the anchor phase when finished, and sets `independence_wave_plan_optional_expansion_failed` only for structural row corruption. It never selects or drops a country.

Event 006's DM-57 sponsorship transaction helpers live in `006_independence_wave_decision_effects.txt`:

- `independence_wave_reconcile_breakaway_sponsorship_queue` runs in the coordinating scope at the start of an Event 006 plan. Its only input is the bounded state-scope array `global.independence_wave_sponsored_breakaway_states`. It removes records only when their state flag or frozen sponsor/generation/strength/route metadata is structurally incomplete, the sponsor no longer has an active Event 006 origin, or the sponsor generation no longer matches. Current candidate ownership, package readiness, and selection are not inputs, so temporarily invalid and unselected candidates remain queued. The helper has no permissive default and never scans countries or states outside the queue.
- `independence_wave_clear_pending_breakaway_sponsorship_metadata` is country scope. It clears only the plan-bound pending flag and sponsorship variables on an absent selected tag. It does not touch the source state's queue record or a committed country's durable sponsorship provenance.
- `independence_wave_apply_pending_breakaway_sponsorship` is country scope and runs after generation reset but before package setup. It requires an exact current-plan ID plus matching pending state, sponsor, sponsor generation, opening strength, and route values. It publishes `independence_wave_sponsored_release`, the durable sponsor/state metadata, and `independence_wave_sponsorship_commit_pending`; it does not remove the source state from the queue.
- `independence_wave_consume_committed_breakaway_sponsorships` runs in the coordinating scope only after `global.liberation_plan_phase` equals `committed`. It consumes the aligned Event 006 sponsorship sub-ledger, requires each live country to have an origin-committed and commit-pending record matching the frozen state and sponsor row, clears the exact source-state queue record, and increments `global.independence_wave_successful_sponsored_releases` once. Clearing the country commit-pending marker and source record makes repeat calls idempotent. Abort, rollback, rejection, and terminal pre-commit paths never call this helper.

Example:

```txt
independence_wave_begin_plan_contribution = yes
# Candidate selection freezes matching sponsorship rows with the release plan.
independence_wave_execute_standalone_frozen_plan = yes
# The executor calls the consumer only after the shared commit is confirmed.
```

`independence_wave_scenario_clear_belligerence_target_marks` lives in `006_independence_wave_scenario_effects.txt`. It has no inputs beyond `global.independence_wave_scenario_belligerence_targets`, clears the temporary per-country selection flag from each bounded scope row, and empties the array. Universal Belligerence calls it before and after target selection so repeated launches and failed declarations cannot leave persistent exclusions.

The event-owned execution effects `independence_wave_transfer_frozen_states` and `soviet_collapse_joint_transfer_frozen_states` consume only locked aligned state rows. After applying the documented owner and controller effects, each state must satisfy both `is_owned_by` and `is_controlled_by` for its frozen target before the transferred count advances. A failed proof publishes the shared `unsafe_instantiation` reason, blocks all subsequent country initialization in that incident, and prevents the release plan from committing.

Example:

```txt
set_temp_variable = { liberation_call_mode = constant:liberation_plan_mode.cluster_joint }
set_temp_variable = { liberation_call_expected_country_count = combined_release_count }
set_temp_variable = { liberation_call_plan_owner = constant:liberation_plan_owner.joint }
liberation_release_begin_plan = yes
liberation_release_enter_allocation_phase = yes
# Event 005 and Event 006 publish tags and anchors, then both add optional rows.
# The package-specific planners must finish compact/extended passes here.
liberation_release_lock_plan = yes
liberation_release_begin_execution = yes
```

## apply_crisis_rescue_event_weight_adjustments

This reusable effect lives in `common/scripted_effects/crisis_rescue_effects.txt` because it owns a small registry and helper effects. It walks the registered crisis-rescue country/event-id arrays and raises the matching event weight to a temporary floor when a registered country is close to capitulation.

Use this for event chains that need a near-capitulation rescue chance without adding bespoke event-weight code to the core timer loop. Register a country with `register_crisis_rescue_target` by setting `crisis_rescue_event_id` in that country scope first. `initialize_crisis_rescue_registry` clears and rebuilds the default registry at event-system initialization.

Inputs:

- `global.crisis_rescue_countries`
- `global.crisis_rescue_event_ids`
- `global.default_event_weight`

Output:

- may update the target event's weight through `set_event_weight`
- sets `chaosx_near_capitulation_rescue_pressure` on countries currently receiving the rescue weight floor

Side effects:

- reads `chaosx_near_capitulation_crisis_rescue_candidate`
- uses `get_event_weight` and `set_event_weight` for the registered event id

Example:

```txt
TIB = {
	set_temp_variable = { crisis_rescue_event_id = constant:holy_realm_event_log.event_id }
	register_crisis_rescue_target = yes
}
apply_crisis_rescue_event_weight_adjustments = yes
```

## apply_state_population_loss_without_recruitable_manpower_gain

This internal state-scope transaction removes real state population without
leaving the recruitable-manpower credit that the engine attaches to a negative
state-scope `add_manpower` effect. It snapshots the legal owner's and, when
different, the controller's `manpower_k`, performs the single state mutation,
then removes only a positive manpower delta observed in those pools. The
correction is measured from the transaction itself and is clamped to the
requested loss; it does not assume whether an occupied state credits its owner
or controller.

Input:

- `state_population_transaction_loss`: positive population loss in people. The
  helper clamps and rounds it before use.
- `state_population_transaction_contract_supplied`: one-shot proof set to `1`
  immediately before the call. The helper clears it after use, so an omitted
  input cannot inherit a previous transaction in the same effect chain.

Output:

- `state_population_transaction_reconciled_gain`: total recruitable-manpower
  credit removed from the owner and distinct controller. A caller that reads
  this temporary output after return must initialize it in the enclosing effect
  before the call.

Side effects:

- applies one negative state-scope `add_manpower` mutation;
- may apply a compensating negative country-scope `add_manpower` to the owner,
  controller, or both when their measured manpower pool increased;
- uses temporary variables prefixed `state_population_transaction_`.

The official script surface exposes no population-only state mutation. The
engine documentation also does not identify which country receives an occupied
state's recruitable credit. Measuring both relevant pools is therefore the
strongest deterministic scripted transaction available; if the engine does not
surface a credit through `manpower_k` in the same effect chain, no unobserved
amount is guessed or removed.

Example:

```txt
set_temp_variable = { state_population_transaction_loss = 25000 }
set_temp_variable = { state_population_transaction_reconciled_gain = 0 }
set_temp_variable = { state_population_transaction_contract_supplied = 1 }
apply_state_population_loss_without_recruitable_manpower_gain = yes
```

## apply_exact_state_civilian_population_loss

This state-scope effect applies one exact, clamped civilian population loss. It
is the shared transaction for systems that must remove real state population
and report the same applied amount even when the optional Deaths display is
disabled. With Deaths enabled it delegates both population removal and logging
to `chaos_meter_register_deaths`; with Deaths disabled, or when logging is
explicitly suppressed, it invokes the same population-only transaction
directly. Both routes reconcile any observed recruitable-manpower credit.
Callers must derive rewards, costs, and cumulative totals only from the returned
applied value.

Every input is required on every invocation. The one-shot proof is cleared on
return so repeated calls cannot inherit a prior caller's optional values.

Inputs:

- `state_civilian_population_loss_requested`: requested people to remove.
- `state_civilian_population_loss_minimum_remaining`: protected population
  floor in people. Negative values are clamped to `0`.
- `state_civilian_population_loss_reason`: Deaths reason ID.
- `state_civilian_population_loss_log_deaths`: `1` to use the Deaths API when
  enabled, `0` to apply an unlogged transaction.
- `state_civilian_population_loss_target_country`: country scope used by the
  Deaths ledger.
- `state_civilian_population_loss_has_target_country`: set to `1` when the
  supplied target is valid.
- `state_civilian_population_loss_contract_supplied`: one-shot proof set to `1`
  immediately before the call.

Outputs:

- `state_civilian_population_loss_applied`: the rounded number of people
  actually removed after the real-population floor is enforced.
- `state_civilian_population_loss_result`: `1` when a positive loss was
  applied, otherwise `0`. Callers that read either temporary output must
  initialize both in the enclosing effect before the call.

Side effects:

- can update the shared Deaths totals, history, country cause totals, and state
  civilian-death total;
- always removes the returned applied amount from the current state's real
  population exactly once;
- reconciles owner/controller recruitable-manpower gains through
  `apply_state_population_loss_without_recruitable_manpower_gain`;
- uses temporary helper variables prefixed
  `state_civilian_population_loss_` and the public `chaos_deaths_*` Deaths API
  inputs.

Example:

```txt
set_temp_variable = { state_civilian_population_loss_requested = 25000 }
set_temp_variable = { state_civilian_population_loss_minimum_remaining = 10000 }
set_temp_variable = { state_civilian_population_loss_reason = constant:chaos_meter_deaths_reason.cannibalism_consumption }
set_temp_variable = { state_civilian_population_loss_target_country = OWNER }
set_temp_variable = { state_civilian_population_loss_has_target_country = 1 }
set_temp_variable = { state_civilian_population_loss_applied = 0 }
set_temp_variable = { state_civilian_population_loss_result = 0 }
set_temp_variable = { state_civilian_population_loss_contract_supplied = 1 }
apply_exact_state_civilian_population_loss = yes
ROOT = {
	add_to_variable = { my_actual_loss_total = state_civilian_population_loss_applied }
}
```

## union_compatible_researched_technologies_from_donor

This country-scope effect adds every compatible technology researched by a
saved donor to the current recipient without removing any technology the
recipient already owns. It iterates the donor's live `researched_techs` array,
so it covers vanilla and mod technologies without a static allowlist.

Scope: recipient country.

Inputs:

- required regular event target `technology_union_donor`: a valid donor
  country saved in the same effect chain before it is annexed or removed.

Outputs: none.

Defaults: none. A missing donor event target is an invalid caller contract and
is deliberately not converted into a silent fallback.

Side effects:

- grants each compatible donor technology missing from the recipient with
  `popup = no`;
- runs the granted technology's normal `on_research_complete` payload when it
  has one;
- preserves an existing recipient choice between `flexible_line` and
  `streamlined_line`;
- preserves an existing recipient choice between the concentrated and
  dispersed industry families;
- does not copy special-project completion, prototypes, facilities,
  scientists, or project progress stored outside `researched_techs`.

The recipient-side `has_tech` guard makes repeated calls idempotent for already
owned technologies. The industry guards follow the approved multi-donor
transfer pattern: mutually exclusive branches cannot coexist, so the
recipient's established branch takes priority while every other compatible
missing technology is added.

Example:

```txt
event_target:absorbed_country = {
	save_event_target_as = technology_union_donor
}
event_target:surviving_country = {
	union_compatible_researched_technologies_from_donor = yes
}
```

## black_plague_rat_refresh_swarm_meters

This Event 020 country-scope effect refreshes the reusable `RTA` carrier's
visible Brood Mass support registers during the existing capped growth pulse.
It derives Disease Dominion from controlled Rat-Controlled states, advances
Hunger and Coherence, applies hierarchy and hunger pressure, clamps every
meter to the shared 0 to 100 range, and opens the RTA hunger crisis report when
the crisis threshold is crossed.

Scope: active `RTA` country only. The effect explicitly excludes `RTX`, whose
Dominion, Sentience, Cohesion, and Hunger meters use the separate royal pulse.

Inputs: the country flags and variables maintained by
`020_black_plague_rat_effects.txt`, especially hierarchy, controlled-state
count, immune-blood hardening, and the existing Brood Mass pulse.

Outputs: `black_plague_rat_hunger`, `black_plague_rat_coherence`,
`black_plague_rat_disease_dominion`, and the persisted
`black_plague_rat_dominion_states` display register.

Side effects: can fire `chaosx.nr20.46` once per unresolved Hunger crisis. The
event choices then either spend mass to restore coordination or feed on one
controlled state, increasing infestation and devastation without curing the
underlying plague.

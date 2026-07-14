# chaosx_dynamic_effects

This file documents reusable dynamic scripted effects from `common/scripted_effects/chaosx_dynamic_effects.txt` and subsystem-specific reusable effects that are intended to be called by multiple systems. The point of these effects is to keep complex variable/meta logic centralized so events can call one reusable block instead of duplicating large script chunks.

## Reuse guidance

Before adding new dynamic logic, check this file and reuse an existing effect if it already matches the behavior. If no effect matches, create a new one in `chaosx_dynamic_effects.txt` and document it here in the same change with: purpose, scope, inputs, defaults, outputs, side effects, and example usage.

## Table of contents

- [chaosx_apply_startup_history_grants](#chaosx_apply_startup_history_grants)
- [chaosx_startup_mark_existing_scientists](#chaosx_startup_mark_existing_scientists)
- [chaosx_startup_clear_generated_scientist_helper_flags](#chaosx_startup_clear_generated_scientist_helper_flags)
- [call_natural_disaster](#call_natural_disaster)
- [natural_disaster_register_relief_recipient_country](#natural_disaster_register_relief_recipient_country)
- [natural_disaster_unregister_relief_recipient_country_if_inactive](#natural_disaster_unregister_relief_recipient_country_if_inactive)
- [natural_disaster_transfer_pending_jobs_for_state](#natural_disaster_transfer_pending_jobs_for_state)
- [natural_disaster_append_abnormal_history_record](#natural_disaster_append_abnormal_history_record)
- [natural_disaster_update_abnormal_history_record](#natural_disaster_update_abnormal_history_record)
- [natural_disaster_rebuild_abnormal_gui_view](#natural_disaster_rebuild_abnormal_gui_view)
- [modify_value_based_on_chaos_tier](#modify_value_based_on_chaos_tier)
- [calculate_economy_scaled_factory_grant](#calculate_economy_scaled_factory_grant)
- [damage_buildings_in_random_states](#damage_buildings_in_random_states)
- [modify_state_population_by_percent](#modify_state_population_by_percent)
- [get_random_sea_region](#get_random_sea_region)
- [refresh_world_threat_state](#refresh_world_threat_state)
- [grant_random_chaos_special_project_available_tech](#grant_random_chaos_special_project_available_tech)
- [apply_crisis_rescue_event_weight_adjustments](#apply_crisis_rescue_event_weight_adjustments)
- [evaluate_random_event_active_pool_candidate](#evaluate_random_event_active_pool_candidate)
- [count_dynamic_major_weight_pool_events](#count_dynamic_major_weight_pool_events)
- [calculate_dynamic_major_weight_gain](#calculate_dynamic_major_weight_gain)
- [apply_dynamic_major_weight_gain_after_minor](#apply_dynamic_major_weight_gain_after_minor)
- [cbrn_initialize_country_data](#cbrn_initialize_country_data)
- [cbrn_set_use_policy](#cbrn_set_use_policy)
- [cbrn_set_chemical_readiness_cap](#cbrn_set_chemical_readiness_cap)
- [cbrn_modify_chemical_readiness](#cbrn_modify_chemical_readiness)
- [cbrn_calculate_action_protection](#cbrn_calculate_action_protection)
- [cbrn_prepare_chemical_action_record](#cbrn_prepare_chemical_action_record)
- [cbrn_apply_state_contamination_delta_internal](#cbrn_apply_state_contamination_delta_internal)
- [cbrn_apply_state_evidence_delta_internal](#cbrn_apply_state_evidence_delta_internal)
- [cbrn_reset_action_context](#cbrn_reset_action_context)
- [CBRN payload logistics](#cbrn-payload-logistics)
- [cbrn_dispatch_chemical_action_record](#cbrn_dispatch_chemical_action_record)
- [CBRN equipment snapshots and protection resolution](#cbrn-equipment-snapshots-and-protection-resolution)
- [chem_set_equipment_backed_mask_reduction](#chem_set_equipment_backed_mask_reduction)
- [CBRN military issue and state distribution](#cbrn-military-issue-and-state-distribution)
- [CBRN filters, losses, reconditioning, and transfer](#cbrn-filters-losses-reconditioning-and-transfer)
- [CBRN protection decision effects](#cbrn-protection-decision-effects)
- [CBRN exact-state raid response adapter](#cbrn-exact-state-raid-response-adapter)
- [CBRN starting protection profiles](#cbrn-starting-protection-profiles)
- [Chaos Warfare doctrine effects](#chaos-warfare-doctrine-effects)
- [CBRN Army Headquarters operation effects](#cbrn-army-headquarters-operation-effects)

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

Optional regular event targets:

- `natural_disaster_call_target_state` plus `natural_disaster_call_target_state_supplied = 1` for `selected_state`
- `natural_disaster_call_target_country` plus `natural_disaster_call_target_country_supplied = 1` for `selected_country`
- `natural_disaster_call_origin_state` plus `natural_disaster_call_origin_state_supplied = 1` for origin-dependent ashfall, lahar, or tsunami calls
- either or both target/proof pairs for `caller_provided`

`natural_disaster_call_causal_context_*`, sequence-id and segment overrides, and `natural_disaster_call_internal_chain_override` are reserved for Event 013's own persisted physical-chain continuation. Their proof is validated against the live source card, sequence, evolution, family, and target; other callers cannot use them to bypass evolution or abnormal locks.

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
- sorts by pending impact, warning state, open recovery, chain risk, severity, date, and path segment
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

## modify_state_population_by_percent

TODO: needs integration with the deaths system

This is a focused state-scope utility for population-to-manpower delta. It converts `state_population_percent` into per-thousand scale, applies fallback behavior when value is too low, computes `pop_loss` from `state_population_k`, then applies it with `add_manpower`. It also logs the computed value for debugging.

Use this when you already have a state scope and only need the population math, without the building-damage pipeline from `damage_buildings_in_random_states`.

Input: `state_population_percent` (optional; decimal fraction like `-0.001`).  
Fallback behavior: defaults to `-0.001` effective result when unset/too low.  
Output/result: manpower change on the current state scope and a debug log line.

Example:

```txt
random_owned_controlled_state = {
 set_temp_variable = { state_population_percent = -0.001 }
 modify_state_population_by_percent = yes
}
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

## refresh_world_threat_state

This is the shared global aggregator for the mod-wide world-threat flag. It rebuilds `global.world_threat_source_count` from registered source flags and then sets or clears the global flag `world_in_threat`.

Use this whenever a threat-specific system changes whether its own source flag should be active. The threat-specific system is responsible for setting or clearing its own source flag first, then calling this effect. The current registered source set includes:

- `world_threat_source_zombies`
- `world_threat_source_holy_realm`
- `world_threat_source_mengele`
- `world_threat_source_fury`
- `world_threat_source_death`
- `world_threat_source_cannibalism`
- `world_threat_source_resources_found_caves`

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

## apply_exact_state_civilian_population_loss

This state-scope effect applies one exact, clamped civilian population loss. It
is the shared transaction for systems that must remove real state population
and report the same applied amount even when the optional Deaths display is
disabled. With Deaths enabled it delegates both population removal and logging
to `chaos_meter_register_deaths`; with Deaths disabled, or when logging is
explicitly suppressed, it applies the identical negative state-manpower delta
directly. Callers must derive rewards, costs, and cumulative totals only from
the returned applied value.

Inputs:

- `state_civilian_population_loss_requested`: requested people to remove.
- `state_civilian_population_loss_minimum_remaining`: protected population
  floor in people; defaults to `0`.
- `state_civilian_population_loss_reason`: Deaths reason ID; defaults to the
  shared unknown reason.
- `state_civilian_population_loss_log_deaths`: `1` to use the Deaths API when
  enabled, `0` to apply an unlogged transaction; defaults to `1`.
- `state_civilian_population_loss_target_country`: optional country scope used
  by the Deaths ledger; defaults to the state's owner.
- `state_civilian_population_loss_has_target_country`: set to `1` when the
  supplied target is valid; defaults to `1` with the owner target.

Outputs:

- `state_civilian_population_loss_applied`: the rounded number of people
  actually removed after the real-population floor is enforced.
- `state_civilian_population_loss_result`: `1` when a positive loss was
  applied, otherwise `0`.

Side effects:

- can update the shared Deaths totals, history, country cause totals, and state
  civilian-death total;
- always removes the returned applied amount from the current state's real
  population exactly once;
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
apply_exact_state_civilian_population_loss = yes
ROOT = {
	add_to_variable = { my_actual_loss_total = state_civilian_population_loss_applied }
}
```

## grant_random_chaos_special_project_available_tech

This country-scope effect grants one not-yet-owned chaos bio/chemical/zombie special-project unlock. It is a central registry for project families that should be available to experimental high-chaos countries and future bio/chemical event actors.

Inputs: none.
Output: may complete one special project and set the matching delivery technology.
Side effects: clears and may set `chaos_random_special_project_granted`.

Current registry entries:

- `anthrax_bomb` -> `anthrax_bomb_delivery_systems`
- `plague_bomb` -> `plague_bomb_delivery_systems`
- `tularemia_bomb` -> `tularemia_bomb_delivery_systems`
- `smallpox_bomb` -> `smallpox_bomb_delivery_systems`
- `weaponize_the_zombies` -> `zombie_disease_bomb_delivery_systems`
- `sp_cw_sarin_program` -> `sarin`
- `sp_cw_soman_program` -> `soman`

When new chaos biological or chemical special projects are added, add their project and delivery tech to this effect so old focus and decision rewards keep rolling from the expanded project pool.

Example:

```txt
completion_reward = {
grant_random_chaos_special_project_available_tech = yes
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

## cbrn_initialize_country_data

Initializes and clamps the persistent national CBRN data model without iterating other countries.

Scope: country.

Inputs: none.

Defaults: Chemical Readiness `0`, readiness cap `19`, defensive-preparation policy, no protection-program profile, full military filter condition, and zero decontamination, medical, biological-security, attribution-control, command-integration, issued-mask, distributed-mask, replacement-demand, reconditioning-cache, and protective-aid values.

Outputs: persistent country variables for Chemical Readiness and policy; the five national CBRN capacities; `cbrn_protection_program_profile`; model-specific military-issue ledgers; military filter condition; replacement demand and reconditioning cache; model-specific and aggregate civilian-distribution totals; and cumulative protective-aid export/receipt totals.

Side effects: existing values are preserved and clamped; readiness is additionally clamped to the current cap. It does not establish a program, grant equipment, distribute masks, award compliance credit, or schedule a pulse.

Example:

```txt
cbrn_initialize_country_data = yes
```

## cbrn_set_use_policy

Sets the national CBRN use-policy enum after validating the requested value.

Scope: country.

Input: temporary `cbrn_requested_use_policy`, from `constant:cbrn_use_policy.*`.

Defaults: invalid or absent requests change nothing.

Output: temporary proof `cbrn_policy_change_accepted` and persistent `cbrn_use_policy` on success.

Side effects: leaving retaliation policy clears `cbrn_retaliation_authorized`. Decision costs, cooldowns, institutions, and stockpile gates remain caller responsibilities.

Example:

```txt
set_temp_variable = { cbrn_requested_use_policy = constant:cbrn_use_policy.limited_battlefield_authority }
cbrn_set_use_policy = yes
```

## cbrn_set_chemical_readiness_cap

Sets an institutional Chemical Readiness cap and immediately brings current readiness inside it.

Scope: country.

Input: temporary `cbrn_requested_readiness_cap`.

Defaults: an absent input changes nothing; country data is initialized first.

Outputs: persistent `chemical_readiness_cap` and possibly reduced `chemical_readiness`.

Side effects: both values are bounded to 0 through 100. Milestone, institution, equipment, and HQ callers own the requested cap.

Example:

```txt
set_temp_variable = { cbrn_requested_readiness_cap = constant:cbrn_readiness.operational_cap }
cbrn_set_chemical_readiness_cap = yes
```

## cbrn_modify_chemical_readiness

Adds a signed readiness change without allowing the value to exceed its institutional cap or fall below zero.

Scope: country.

Input: temporary `cbrn_readiness_delta`.

Defaults: an absent input changes nothing; country data is initialized first.

Output: persistent `chemical_readiness`.

Side effects: none outside the current country.

Example:

```txt
set_temp_variable = { cbrn_readiness_delta = 5 }
cbrn_modify_chemical_readiness = yes
```

## cbrn_calculate_action_protection

Resolves six equipment- and institution-backed protection layers into chemical-agent-class multipliers. Equipment snapshots treat usable coverage as the active score and weighted model quality as its ceiling: partial basic issue follows its actual coverage band, while full basic issue caps at 55 effective protection. The weighted skin, antidote, decontamination, medical, and warning layers can raise the shared result.

Scope: the attacker country or the enclosing effect chain; the helper uses temporary variables only.

Required temporary inputs:

- `cbrn_action_agent_class`
- `cbrn_protection_respiratory`
- `cbrn_protection_skin`
- `cbrn_protection_antidote`
- `cbrn_protection_decontamination`
- `cbrn_protection_medical`
- `cbrn_protection_warning`

Defaults: missing inputs or a non-chemical class leave the proof missing and return unprotected multipliers.

Outputs:

- `cbrn_action_effective_protection`, 0 through 100
- `cbrn_action_casualty_mult`
- `cbrn_action_disruption_mult`
- `cbrn_action_contamination_mult`
- `cbrn_action_protection_resolved_proof`

Side effects: none. The helper does not infer stockpile or issued coverage and does not consume filters. Stage 2 prepares its six inputs from real equipment and state/force coverage.

Example:

```txt
set_temp_variable = { cbrn_action_agent_class = constant:cbrn_agent_class.nerve }
set_temp_variable = { cbrn_protection_respiratory = 80 }
set_temp_variable = { cbrn_protection_skin = 70 }
set_temp_variable = { cbrn_protection_antidote = 60 }
set_temp_variable = { cbrn_protection_decontamination = 75 }
set_temp_variable = { cbrn_protection_medical = 75 }
set_temp_variable = { cbrn_protection_warning = 65 }
cbrn_calculate_action_protection = yes
```

### Internal protection-calculator helpers

`cbrn_reset_protection_outputs`, `cbrn_set_protection_weights_from_agent_class`, and `cbrn_set_casualty_mult_from_protection` are private steps used by `cbrn_calculate_action_protection`.

Scope: the enclosing effect chain; all working values are temporary.

Inputs: `cbrn_action_agent_class` plus the six protection-layer inputs documented above. The weight helper maps choking, blister, nerve, or incapacitating classes to the centralized six-layer table. The casualty helper reads the resulting effective score and the decontamination/medical support bands.

Defaults: reset returns zero effective protection, neutral casualty/disruption/contamination multipliers, and missing proof. An unrecognized class keeps those fail-closed defaults.

Outputs: temporary layer weights, `cbrn_action_effective_protection`, the agent-specific casualty multiplier, and the public protection outputs/proof written by the wrapper.

Side effects: none. These helpers do not inspect technology, create equipment, consume filters, or mutate a country or state.

Usage example: call only the public wrapper after supplying all six layers; it invokes the three internal helpers in the required order.

```txt
cbrn_calculate_action_protection = yes
```

## cbrn_prepare_chemical_action_record

Validates and calculates the normalized temporary record for one deliberate chemical action. It is the shared route interface, not a payload or consequence effect by itself.

Scope: attacker country.

Required regular event target and proof:

- `cbrn_action_target_state`
- `cbrn_action_target_state_supplied = constant:cbrn_proof.supplied`

Required temporary metadata:

- `cbrn_action_weapon_class`
- `cbrn_action_agent_class`
- `cbrn_action_agent`
- `cbrn_action_delivery_route`
- `cbrn_action_severity`

Nerve use through cylinder, projector, artillery, armored delivery, or air delivery additionally requires `cbrn_action_late_agent_route_authorized = constant:cbrn_proof.supplied`, set only by the mapped late technology/doctrine gate. Nerve Suppression accepts nerve agents only.

Required payload inputs: positive `cbrn_action_payload_required`, positive `cbrn_action_payload_consumed`, and `cbrn_action_payload_consumed_proof`. The proof is valid only after a real CBRN payload-debit helper removes equipment.

Required protection inputs: outputs and proof from `cbrn_resolve_action_target_protection`.

Required condition inputs and proof: `cbrn_action_weather_mult`, `cbrn_action_terrain_mult`, `cbrn_action_target_density_mult`, `cbrn_action_command_mult`, `cbrn_action_evidence_control_mult`, `cbrn_action_context_condemnation_mult`, a positive `cbrn_action_doctrine_condemnation_mult` validation value, `cbrn_action_forecast_confidence`, `cbrn_action_command_integration`, `cbrn_action_base_friendly_risk`, and `cbrn_action_conditions_resolved_proof`. The context multiplier carries retaliation and target-relationship effects. Immediately after validation, the public wrapper overwrites the doctrine value from the attacker country's Integrated CBRN Command mastery and clamps it to `0.70` through `1.00`; route adapters cannot select a different doctrine discount.

Defaults: none. Validation is fail-closed. The continuous ordinary-air route returns `unsupported_continuous_air_route`; no neutral condition or idle-aircraft estimator is substituted.

Outputs include `cbrn_action_result`, `cbrn_action_reject_reason`, victim event target/proof when known, payload ratio, dose, disruption, military and civilian death fractions, exposed share, contamination points/duration, medical burden, evidence, attribution, Condemnation base, friendly risk, `cbrn_action_vehicle_sealing_applied`, and source label. The vehicle-sealing proof is set only when the attacker has `vehicle_overpressure_and_sealed_compartments` and the verified route is armored delivery; it reduces friendly crew exposure without changing target harm, evidence, attribution, or Condemnation.

Side effects: no persistent gameplay mutation. Rejected calls return zero consequence outputs. Accepted calls must immediately pass to `cbrn_dispatch_chemical_action_record` before the action context is reset.

Example:

```txt
random_owned_controlled_state = {
	save_event_target_as = cbrn_action_target_state
}
set_temp_variable = { cbrn_action_target_state_supplied = constant:cbrn_proof.supplied }
set_temp_variable = { cbrn_action_weapon_class = constant:cbrn_weapon_class.chemical }
set_temp_variable = { cbrn_action_agent_class = constant:cbrn_agent_class.choking }
set_temp_variable = { cbrn_action_agent = constant:cbrn_agent.chlorine }
set_temp_variable = { cbrn_action_delivery_route = constant:cbrn_delivery_route.cylinder_release }
set_temp_variable = { cbrn_action_severity = constant:cbrn_operation_severity.local }
# The real route adapter must set payload, protection, and condition inputs/proofs here.
cbrn_prepare_chemical_action_record = yes
```

### Internal chemical-action record helpers

The public action-record wrapper owns these private temporary calculators:

| Helper | Purpose and outputs |
| --- | --- |
| `cbrn_reset_action_outputs` | Resets every action result, proof, consequence output, attribution value, vehicle-sealing proof, and source label to its rejected, missing, unknown, or zero default. |
| `cbrn_set_route_profile_from_action` | Maps the validated delivery-route enum to disruption, civilian exposure, contamination, medical burden, evidence, Condemnation, and duration baselines. Unsupported routes retain zero values and are rejected before calculation. |
| `cbrn_set_agent_class_profile_from_action` | Maps the chemical class to disruption, persistence, medical, evidence, Condemnation, duration, and tactical/strategic lethality multipliers. |
| `cbrn_set_chemical_agent_profile_from_action` | Applies the distinct chlorine, phosgene, mustard, lewisite, tabun, sarin, soman, malodor, or behavioral-agent potency, persistence, evidence, and source-profile values. |
| `cbrn_set_action_source_label` | Chooses battlefield, persistent-contamination, strategic-raid, or nerve-suppression source classification from the validated route and severity. |
| `cbrn_set_action_attribution_from_evidence` | Converts the current episode evidence score into unknown, suspected, probable, or confirmed attribution without changing evidence. |
| `cbrn_calculate_chemical_action_outputs` | Combines payload ratio, conditions, protection, route, class, agent, response choices, doctrine-only Condemnation mitigation, and confirmed-use floors into the normalized action outputs. |

Scope: attacker country/enclosing effect chain. Inputs are the temporary metadata and proof contract documented for `cbrn_prepare_chemical_action_record`. Defaults are fail closed: the reset helper runs first, and missing or invalid inputs leave a rejected record. Outputs are temporary only. Side effects: none; even the doctrine multiplier changes only Condemnation, while evidence, attribution, deaths, contamination, and confirmed-use history are untouched.

Usage example: route adapters must call the public wrapper, which validates the contract and invokes these helpers in order.

```txt
cbrn_prepare_chemical_action_record = yes
```

## cbrn_apply_state_contamination_delta_internal

Internal state-scope mutation used by the single consequence dispatcher and exact-state decontamination responses.

Inputs: temporary `cbrn_state_contamination_delta` and optional positive `cbrn_state_contamination_duration_input`.

Defaults: no delta means no severity change. A new duration extends to the longer active duration rather than adding a second independent timer.

Outputs: previous/new contamination values and classes in `cbrn_state_previous_contamination_value`, `cbrn_state_previous_contamination_class`, `cbrn_state_new_contamination_value`, and `cbrn_state_new_contamination_class`.

Side effects: updates lazy state variables `cbrn_chemical_contamination`, `cbrn_chemical_contamination_class`, and `cbrn_chemical_contamination_duration_days`; clears them below Trace. Its private `cbrn_refresh_state_contamination_class` step clamps the contamination meter, derives the class thresholds, and clears duration/class data when contamination falls below Trace. It does not register deaths, Air Cleanliness, Condemnation, or a scheduler by itself.

Example:

```txt
event_target:cbrn_action_target_state = {
	set_temp_variable = { cbrn_state_contamination_delta = cbrn_action_contamination_points }
	set_temp_variable = { cbrn_state_contamination_duration_input = cbrn_action_contamination_duration_days }
	cbrn_apply_state_contamination_delta_internal = yes
}
```

## cbrn_apply_state_evidence_delta_internal

Internal state-scope evidence mutation for the single consequence dispatcher and later evidence-resolution actions.

Input: temporary `cbrn_state_evidence_delta`.

Defaults: no input changes nothing.

Outputs: temporary `cbrn_state_attribution_output`; persistent `cbrn_evidence_quality` and `cbrn_attribution_state` when applicable. The private `cbrn_refresh_state_attribution` step clamps accumulated evidence and derives unknown, suspected, probable, or confirmed attribution without changing the evidence score.

Side effects: evidence is clamped to 0 through 100. Values below Suspected remain latent while the public attribution state is cleared. It does not add Condemnation or expose latent responsibility by itself.

Example:

```txt
event_target:cbrn_action_target_state = {
	set_temp_variable = { cbrn_state_evidence_delta = cbrn_action_evidence_points }
	cbrn_apply_state_evidence_delta_internal = yes
}
```

## cbrn_reset_action_context

Invalidates all public chemical-action proof variables and zeroes metadata/outputs after every consumer has finished reading one action record.

Scope: the enclosing effect chain.

Inputs: none.

Defaults: none.

Outputs: action variables reset to their `none`, zero, rejected, or missing-proof constants, including the one-shot dispatch proof and optional evidence-floor override.

Side effects: regular event targets are not manually cleared because they expire with the chain; reset proofs prevent stale targets from being accepted within a reused chain.

Example:

```txt
if = {
	limit = { check_variable = { var = cbrn_action_result value = constant:cbrn_action_result.accepted compare = equals } }
	cbrn_dispatch_chemical_action_record = yes
}
cbrn_reset_action_context = yes
```

## CBRN payload logistics

These country-scope effects are defined in `cbrn_payload_effects.txt`. They keep the strategic-agent, shell-filling, and air-payload ledgers separate and supply `cbrn_action_payload_consumed_proof` only after exact equipment removal. Missing technology, mismatched profile, insufficient stock, an unsupported route, or an in-progress line change fails closed and creates no exposure.

### Public payload effects

| Effect | Inputs, defaults, outputs, and side effects |
| --- | --- |
| `cbrn_initialize_payload_logistics` | Country scope. No inputs. Initializes persistent shell and air profile variables to `cbrn_agent.none`; creates no equipment. |
| `cbrn_set_default_payload_requirement_for_action` | Country/enclosing action chain. Reads `cbrn_action_delivery_route`; writes the centralized positive route cost and resets consumed amount/proof. Unknown routes remain at zero. |
| `cbrn_try_debit_action_payload` | Country scope. Requires validated chemical metadata, unlocked agent, ready matching profile, and exact stock at least equal to `cbrn_action_payload_required`. Debits the exact strategic-agent model, shared shell lot, or class-specific air lot and then writes consumed amount/proof. A failed gate removes nothing. |
| `cbrn_change_shell_filling_profile` | Country scope. Requires temporary `cbrn_requested_payload_agent`, its unlock, a different current profile, and no active shell reconfiguration. Applies the centralized switch loss to prepared shell stock, stores the new agent, sets the timed line-change flag, and returns `cbrn_payload_profile_change_accepted`. |
| `cbrn_change_air_payload_profile` | Same contract for the air line. Wastage is removed only from the old class-specific air payload stock and the longer air reconfiguration delay is applied. |
| `cbrn_convert_selected_agent_to_shell_lots` | Country scope. Requires a selected ready shell profile and temporary positive `cbrn_payload_conversion_requested`. Clamps the input to exact selected-agent stock, debits that stock, applies the class-specific recovery ratio, adds shell lots, and returns completed proof plus actual input/output. |
| `cbrn_convert_selected_agent_to_air_payload_lots` | Same conversion contract for the selected air agent. Requires Chemical Air Interdiction and adds only the matching choking, blister, nerve, or incapacitating air lot. |
| `cbrn_migrate_legacy_payload_stockpiles` | Country scope, idempotent. Converts each legacy cylinder and experimental bomb model to its exact strategic-agent lot at the centralized save-preserving recovery ratio, selects deterministic initial profiles from recovered stock, and sets one migration flag. It must run only after every legacy consumer has moved to the shared pipeline. |

### Internal payload helpers

| Helper | Private responsibility |
| --- | --- |
| `cbrn_debit_strategic_agent_lots_internal` | Removes the exact chlorine, phosgene, mustard, lewisite, tabun, sarin, soman, malodor, or behavioral lot selected by action metadata. |
| `cbrn_debit_shell_lots_internal` / `cbrn_debit_air_payload_lots_internal` | Remove the route's shell lot or exact class-specific air lot after public stock validation. |
| `cbrn_remove_shell_profile_wastage_internal` / `cbrn_remove_air_profile_wastage_internal` | Apply bounded prepared-stock losses during profile changes without touching strategic agent stock. |
| `cbrn_read_selected_shell_agent_stock_internal` / `cbrn_read_selected_air_agent_stock_internal` | Read exact selected strategic-agent availability for conversion; unknown profiles return zero. |
| `cbrn_debit_selected_shell_agent_stock_internal` / `cbrn_debit_selected_air_agent_stock_internal` | Remove the exact conversion input selected by the persistent profile. |
| `cbrn_set_shell_conversion_recovery_internal` | Select the choking, blister, nerve, or incapacitating shell-filling recovery ratio. |
| `cbrn_add_selected_air_payload_output_internal` | Adds only the class-specific air payload output that matches the selected agent. |

Example:

```txt
cbrn_reset_action_context = yes
set_temp_variable = { cbrn_action_delivery_route = constant:cbrn_delivery_route.artillery_fire_plan }
# Set the remaining static action metadata.
cbrn_set_default_payload_requirement_for_action = yes
cbrn_try_debit_action_payload = yes
```

## cbrn_dispatch_chemical_action_record

Consumes one accepted chemical action record exactly once. The public country-scope effect lives in `cbrn_consequence_effects.txt`.

Required inputs: an accepted result from `cbrn_prepare_chemical_action_record`, positive consumed payload with supplied debit proof, supplied exact-target proof, and regular event target `cbrn_action_target_state`. Route adapters may optionally set `cbrn_action_evidence_floor_override` for an engine-proven outcome such as recovered aircraft wreckage. The override can raise evidence only.

Defaults: fail closed. A rejected record, missing target, missing payload proof, zero consumption, or an already supplied `cbrn_action_dispatch_proof` produces no mutation. Continuous ordinary-air missions never become accepted records.

Outputs: supplied one-shot dispatch proof, raw exact civilian deaths returned by the shared Deaths helper, actual evidence delta after absolute floors, cumulative attribution, and inspectable actor/state history variables.

Side effects:

- applies dynamic `damage_units` organisation and strength ratios only to armies in the exact selected state; hostile and bounded friendly/blowback limits are separate;
- lets the existing country-casualty tracker record exact engine military losses instead of inventing an estimated death count;
- removes civilian population and writes one immediate chemical Deaths record from the calculated exact fraction;
- accumulates CBRN contamination and updates the legacy `chem_state_contamination` modifier under a guard that prevents duplicate immediate deaths, so existing continuing-death and Air Cleanliness systems see the same state;
- adds medical saturation, consumes civilian and military mask/filter stocks, applies cumulative evidence and attribution floors, and schedules state-scoped expiry/recovery/decay events;
- applies Condemnation with cumulative visibility, raw civilian deaths, contamination, severity, victim, strategic/mass-casualty floors, sanctions, and confirmed treaty breach;
- records permanent confirmed-use history. Doctrine can reduce only the Condemnation base before the public floor; it never changes the other outputs;
- applies first-exposure multipliers to the affected state and a short defender adaptation idea. Prior world use and real protection reduce this shock without benefiting the attacker.

Internal helpers are `cbrn_dispatch_set_source_and_context`, `cbrn_dispatch_set_evidence_floor`, `cbrn_dispatch_apply_first_exposure_shock`, `cbrn_dispatch_apply_unit_damage`, `cbrn_dispatch_apply_mask_losses`, `cbrn_dispatch_apply_state_consequences`, `cbrn_dispatch_apply_condemnation`, and `cbrn_dispatch_record_actor_history`. They share the validated temporary record and must not be called directly by route adapters.

Example:

```txt
cbrn_prepare_chemical_action_record = yes
if = {
	limit = { check_variable = { var = cbrn_action_result value = constant:cbrn_action_result.accepted compare = equals } }
	cbrn_dispatch_chemical_action_record = yes
}
cbrn_reset_action_context = yes
```

## CBRN equipment snapshots and protection resolution

### cbrn_initialize_state_protection

Initializes one state's persistent civilian respirator ledger.

Scope: state. Inputs: none. Defaults: zero model crates, zero fitting points and replacement demand, and full unused-filter condition. Outputs: initialized and clamped `cbrn_civilian_mask_*` variables. Side effects: no equipment is created or consumed.

Example:

```txt
FROM = { cbrn_initialize_state_protection = yes }
```

### cbrn_refresh_country_mask_snapshot

Rebuilds the current country's inspectable respirator snapshot from real stockpile models, explicit military-issue ledgers, equipment actually in divisions, deployed manpower, filter condition, and aggregate civilian distribution.

Scope: country. Inputs: live equipment and persistent ledgers. Defaults: absent ledgers are initialized to zero. Outputs include reserve crates by model, `cbrn_military_mask_requirement`, coverage, respiratory/skin/warning protection, the respiratory-and-skin `cbrn_military_blister_mask_protection` composite, profile-specific `cbrn_ai_military_mask_coverage_target` and `cbrn_ai_mask_reserve_target_crates`, and `cbrn_mask_total_accounted`. Side effects: only derived persistent snapshot variables are rewritten; no stock moves.

Example:

```txt
cbrn_refresh_country_mask_snapshot = yes
```

### chem_set_equipment_backed_mask_reduction

Adapts the shared field-army protective-equipment snapshot to the legacy cylinder-ability combat modifiers. It replaces the former technology-only 25/50/75-percent lookup.

Scope: army leader. Inputs: the owner country's refreshed `cbrn_military_respiratory_protection` and `cbrn_military_skin_protection`; temporary `chem_mask_blister_bonus` selects the blister composite when positive. Defaults: missing snapshot values produce zero mask mitigation. Output: temporary `chem_mask_reduction_fraction`, using the equipment-backed score directly as a percentage and clamped from zero to the centralized 75-percent legacy ceiling. Side effects: none; it neither creates nor consumes equipment.

The leader-daily preview adapter refreshes the owning country's snapshot once before rebuilding all cylinder previews. Each ability activation refreshes again and rebuilds its selected preview so deployed manpower, issued models, divisional equipment, and filter condition are current at use time.

Example:

```txt
set_temp_variable = { chem_mask_blister_bonus = 1 }
chem_set_equipment_backed_mask_reduction = yes
```

### cbrn_refresh_state_civilian_mask_snapshot

Rebuilds one state's effective civilian protection from population, distributed model crates, fitting points, filter condition, registration, civil-defence institutions, exact-state alert choices, and the controller's medical/decontamination capacity. Fitting- and filter-adjusted coverage continues to measure the share of the population reached; each respiratory, skin, or warning protection component uses the lower of that coverage and the weighted model-quality score. Partial issue therefore remains valuable while full basic issue cannot exceed its accepted 55-point respiratory ceiling.

Scope: state. Inputs: persistent state ledger and current controller. Defaults: zero coverage when population or usable stock is zero. Outputs include raw and effective coverage, respiratory/skin/warning protection, decontamination and medical protection, and `cbrn_civilian_mask_effective_coverage`. Side effects: only derived state variables are rewritten.

Example:

```txt
event_target:cbrn_action_target_state = {
	cbrn_refresh_state_civilian_mask_snapshot = yes
}
```

### cbrn_resolve_action_target_protection

Resolves both military and civilian protection for the exact `cbrn_action_target_state`, then runs the shared agent-class calculator for each population.

Scope: attacker-country action chain. Required input: a valid regular event target `cbrn_action_target_state` plus `cbrn_action_agent_class`. Defaults: invalid or missing protection data leaves the final proof missing. Outputs: military and civilian effective protection, casualty/disruption/contamination multipliers, and `cbrn_action_protection_resolved_proof`. Side effects: refreshes only target/controller snapshot variables and consumes no equipment.

Example:

```txt
cbrn_resolve_action_target_protection = yes
```

## CBRN military issue and state distribution

### cbrn_issue_requested_masks_to_military

Debits a requested number of real respirator crates, preferring sealed, advanced, improved, basic, then reconditioned models, and transfers them to non-reclaimable military-issue ledgers.

Scope: country. Input: temporary `cbrn_mask_issue_requested_crates`. Defaults: absent, negative, or unavailable stock produces zero issue. Outputs: temporary completed/remaining amounts and refreshed military coverage. Side effects: removes real equipment, updates model-specific issue ledgers and weighted filter condition, and reduces existing replacement demand.

Example:

```txt
set_temp_variable = { cbrn_mask_issue_requested_crates = 500 }
cbrn_issue_requested_masks_to_military = yes
```

### cbrn_issue_masks_to_field_army

Convenience country effect that requests one centrally tuned increment of uncovered deployed-army need and calls `cbrn_issue_requested_masks_to_military`.

Scope: country. Inputs: current deployed manpower and stock. Defaults: zero issue when there is no uncovered requirement. Output/side effects: those of the underlying issue helper.

### cbrn_distribute_requested_masks_to_state

Population-scales an exact state's requested civilian distribution, measures its remaining effective-coverage gap, grosses that gap up for the fitting and filter quality of the new issue, applies urban, infrastructure, combat, occupation, reserve, registration, civil-defence, applied-registration-technology, and simplified-filter cost/effectiveness modifiers, then debits the controller's real models oldest-first.

Scope: state. Required temporary inputs: effective target `cbrn_distribution_target_fraction`, `cbrn_distribution_base_cost_mult`, fitting-quality `cbrn_distribution_effectiveness_mult`, and percent filter condition `cbrn_distribution_new_filter_condition`. Defaults: inputs are clamped; a zero fitting or filter factor produces no useful distribution. Outputs: consumed stock, usable crates, fitting points, weighted filter condition, effective coverage, and remaining state demand. Side effects: removes equipment from the controller, updates model-specific state and country aggregate ledgers, and never creates reclaimable national stock. Existing raw crates do not suppress a valid request when poor fitting or exhausted filters leave effective coverage below target.

Example:

```txt
set_temp_variable = { cbrn_distribution_target_fraction = 0.50 }
set_temp_variable = { cbrn_distribution_base_cost_mult = 1 }
set_temp_variable = { cbrn_distribution_effectiveness_mult = 1 }
set_temp_variable = { cbrn_distribution_new_filter_condition = 100 }
cbrn_distribute_requested_masks_to_state = yes
```

### cbrn_distribute_priority_masks_to_state, cbrn_distribute_full_masks_to_state, and cbrn_distribute_emergency_masks_to_state

These state-scope wrappers supply the accepted 50-percent priority, 95-percent full, or 35-percent effective emergency targets. The shared helper derives the larger raw emergency allocation needed after reduced fitting quality and degraded filter condition; emergency issue also applies the 0.60 improvised baseline and 1.30 wastage. Defaults and side effects are those of `cbrn_distribute_requested_masks_to_state`.

### cbrn_debit_mask_stockpile_oldest_first

Debits a requested amount from real country stock in reconditioned, basic, improved, advanced, then sealed order.

Scope: country. Input: temporary `cbrn_mask_stock_debit_requested`. Defaults: request is clamped to available stock and zero. Outputs: `cbrn_mask_stock_debit_completed` and remaining request. Side effects: model-specific stock removal and snapshot refresh.

## CBRN filters, losses, reconditioning, and transfer

### cbrn_replace_military_mask_filters and cbrn_replace_state_civilian_mask_filters

Restore worn military or exact-state civilian filters using real national respirator crates. The state helper additionally scales cost with current chemical contamination. `rapid_filter_replacement` reduces the real replacement-crate debit by the centralized 30-percent efficiency gain in either scope.

Scope: country for military; state for civilian. Inputs: current issued/distributed crates and filter condition. Defaults: no worn filters or no reserve causes no restoration. Outputs: proportional restored condition and refreshed coverage. Side effects: oldest-first stock debit and reduced replacement demand.

### cbrn_apply_military_mask_loss and cbrn_apply_state_civilian_mask_loss

Apply explicit exposure/storage loss to issued military or distributed civilian stock. `military_filter_standardization` reduces both crate loss and filter-condition loss by the accepted 15 percent for military and civilian ledgers. Controlled Retaliation Doctrine and Mask Discipline apply their separate military-only consumption multipliers; they do not reduce civilian loss or exposure consequences.

Scope: country or state respectively. Inputs: temporary `cbrn_mask_loss_fraction` and `cbrn_mask_condition_loss`. Defaults: values are clamped to safe ranges. Outputs: model ledgers, filter condition, and replacement demand. Side effects: civilian loss also updates the controller's aggregate distributed totals; no lost equipment returns to stock.

### cbrn_apply_standard_chemical_mask_losses, cbrn_apply_persistent_chemical_mask_losses, and cbrn_apply_strategic_raid_mask_losses

State-scope wrappers selecting the centralized ordinary exposure, persistent-agent, or strategic-raid loss profile before calling `cbrn_apply_state_civilian_mask_loss`.

### cbrn_recondition_damaged_masks

Converts the national damaged/rejected-mask cache and replacement ledger into low-reliability `gas_mask_equipment_reconditioned` at the configured recovery ratio and per-action cap.

Scope: country. Inputs: `cbrn_reconditionable_mask_cache` and `cbrn_mask_replacement_demand`. Defaults: no source material produces no output. Output: temporary `cbrn_recondition_recovered`. Side effects: consumes source ledgers and adds real non-buildable reconditioned equipment.

### cbrn_apply_annual_mask_storage_loss

Applies model-specific annual warehouse losses, reduced by an established national reserve.

Scope: country. Inputs: current stock by model. Defaults: empty stock produces no loss. Outputs: total storage loss and replacement demand. Side effects: removes real stock and refreshes the snapshot.

### cbrn_transfer_state_civilian_mask_ledger

Transfers distributed civilian protection after `on_state_control_changed` without refunding either controller.

Scope: transferred state. Required regular event targets: `cbrn_old_state_controller` and `cbrn_new_state_controller`. Defaults: the caller only invokes it for a non-empty state ledger. Outputs: surviving state stock and controller aggregate totals. Side effects: clears projects and exact-alert responses, removes their dynamic modifiers, applies turnover/occupation survival and filter loss, charges lost stock to replacement demand, and moves aggregate ownership.

### cbrn_start_protection_maintenance_job

Starts one self-scheduled annual country maintenance event if no job is active.

Scope: country. Inputs: none. Defaults: repeated calls are idempotent through `cbrn_protection_maintenance_active`. Side effects: schedules `cbrn_protection.1` after the centralized annual interval. It creates no all-country periodic pulse.

## CBRN protection decision effects

### cbrn_debit_requested_support_equipment and cbrn_debit_requested_train_equipment

Country-scope bounded debits. Inputs are `cbrn_support_equipment_debit_requested` or `cbrn_train_equipment_debit_requested`; missing/negative requests become zero. Outputs are the matching `*_debit_completed` temporary variables. Side effects: removes only stock actually available.

### National project begin/complete effects

The following effects are paired decision handlers:

| Effects | Purpose and side effects |
| --- | --- |
| `cbrn_begin_national_respirator_reserve` / `cbrn_complete_national_respirator_reserve` | Debits support equipment, establishes the program/reserve, raises readiness, and starts maintenance. |
| `cbrn_begin_population_registration` / `cbrn_complete_population_registration` | Debits support equipment and manpower, applies population-fitting loss, establishes fitting/civil-defence flags only when masks remain, raises readiness, and records rejected stock for reconditioning. |
| `cbrn_begin_field_army_mask_issue` / `cbrn_complete_field_army_mask_issue` | Debits support equipment, then runs real field-army issue. |
| `cbrn_begin_mask_reconditioning` / `cbrn_complete_mask_reconditioning` | Debits support equipment, recovers reconditioned crates, and may fire the weighted defective-batch event. |
| `cbrn_begin_civilian_mask_industry_conversion` / `cbrn_complete_civilian_mask_industry_conversion` | Debits support equipment and converts the timed factory burden into a tuned basic-mask batch. |
| `cbrn_begin_simplified_filter_program` / `cbrn_complete_simplified_filter_program` | Debits support equipment, adds a basic batch, and starts a timed low-cost/lower-effectiveness filter program. |

Scope: country. Inputs/defaults are the real decision gates and centralized constants; direct calls bypass political-power/factory costs and therefore should remain inside the matching decisions. Outputs are persistent flags, stock, readiness, and maintenance state.

Example:

```txt
hidden_effect = { cbrn_begin_national_respirator_reserve = yes }
```

### State project begin/complete effects

`cbrn_begin_state_protection_project` and `cbrn_end_state_protection_project` own the timed exact-state project lock. `cbrn_complete_priority_state_distribution`, `cbrn_complete_full_state_distribution`, `cbrn_complete_emergency_state_distribution`, `cbrn_complete_occupied_state_distribution`, and `cbrn_complete_state_filter_replacement` call the corresponding real allocation/filter helper and cleanup. Emergency completion additionally applies its timed congestion modifier; occupied completion changes resistance/compliance only after attempting real distribution.

Scope: state. Input for begin: `cbrn_project_duration_days`. Defaults: duration is clamped. Side effects: state flags/modifiers and real controller stock consumption.

### cbrn_resolve_defective_reconditioned_batch

Removes the configured fraction of the recorded reconditioned batch, adds replacement demand, lowers readiness, and clears the event ledger.

Scope: country. Input: persistent `cbrn_reconditioned_batch_size`. Defaults: no recorded batch does nothing. Output: refreshed stock snapshot. Side effects: real reconditioned stock loss.

### cbrn_export_masks_to_protection_partner, cbrn_import_masks_from_protection_partner, and cbrn_license_respirator_design_from_partner

Country-scope allied procurement handlers using regular event target `cbrn_protection_trade_partner`. Invalid or stale partners fail closed. Export sends a real 500-crate family shipment, records bilateral aid totals and recipient opinion, and gives a small capped decay credit only when the exporter already follows a verified Condemnation-compliance path; offense history is unchanged. Import sends real partner stock to the caller and marks the supplier with a timed allied-request production signal. Licensing grants one gas-mask research bonus. All successful paths refresh relevant readiness/maintenance state.

## CBRN exact-state raid response adapter

### cbrn_calculate_state_raid_response_costs

State-scope population calculator for hospital/utility masks and support equipment, plus shelter support equipment and trains. Costs are clamped to centralized minima/maxima and stored as persistent state variables for decision display.

### cbrn_register_exact_state_chemical_raid_alert

Fail-closed state-scope public adapter for a verified current-version raid/operation hook.

Required temporary proof: `cbrn_exact_state_alert_verified = constant:cbrn_proof.supplied`. Optional input: `cbrn_raid_alert_duration_days`, clamped to 1–30 days and defaulting to 7. Outputs: exact-state alert flag and response costs. Side effects: clears stale response choices before opening the new alert. It does not infer aircraft activity, create contamination, or estimate a continuous mission.

Example:

```txt
event_target:raid_target_state = {
	set_temp_variable = { cbrn_exact_state_alert_verified = constant:cbrn_proof.supplied }
	set_temp_variable = { cbrn_raid_alert_duration_days = 5 }
	cbrn_register_exact_state_chemical_raid_alert = yes
}
```

### cbrn_clear_exact_state_chemical_raid_alert

State-scope explicit alert cleanup. It clears only `cbrn_chemical_raid_alert_active`; timed response modifiers retain their own durations unless state control changes.

### Exact-state response effects

`cbrn_apply_hospital_utility_protection` and `cbrn_apply_civilian_shelter_movement` recalculate and debit their population-scaled real mask/support/train costs before setting timed protective flags/modifiers. `cbrn_apply_chemical_alarm` creates warning protection plus factory/movement disruption. `cbrn_apply_industrial_continuity_order` preserves local output while marking the shared exposure pipeline to increase civilian exposure. Missing equipment prevents the protected effects from being set.

## CBRN starting protection profiles

### cbrn_apply_starting_mask_profile

Applies one accepted 1936 country profile from temporary inputs: basic/improved stock, military issue target, civilian distribution target, registration proof, and program-profile enum.

Scope: country. Required temporary inputs: `cbrn_starting_mask_basic`, `cbrn_starting_mask_improved`, `cbrn_starting_military_issue_target`, `cbrn_starting_civilian_distribution_target`, `cbrn_starting_registration_proof`, and `cbrn_starting_program_profile`. Defaults: the static caller supplies every value. Outputs: technology, exact tuned starting crates, reserve/registration flags, readiness, actual manpower-scaled military issue, actual population-scaled distribution across controlled core states, and maintenance scheduling. Military targets above 100 percent represent replacement, training, and mobilization issue; protection remains capped while the extra issued ledger is retained. All issue and distribution are stock-limited, so unmet target demand creates no equipment. Side effects: a bounded one-time owned-state loop for that country; no periodic pulse.

### chaosx_apply_starting_cbrn_mask_profiles

Static startup dispatcher for the 30 explicitly mapped tags in `gas_mask_starting_stockpile_matrix.md`. It assigns all temporary inputs and calls `cbrn_apply_starting_mask_profile` per existing country. Exact totals are gameplay tuning inside accepted historical bands; relative preparedness and confidence, not literal inventory certainty, control the profiles. Britain has the largest reserve and strongest starting civilian share.

Example:

```txt
chaosx_apply_starting_cbrn_mask_profiles = yes
```

## Chaos Warfare doctrine effects

These country-scope effects are defined in `cbrn_doctrine_effects.txt`. They own institution, policy, mastery-record, technology-grant, and migration state. They never choose or consume a chemical payload and never dispatch exposure.

### Institutional value helpers

| Effect | Inputs, defaults, outputs, and side effects |
| --- | --- |
| `cbrn_doctrine_raise_readiness_to_minimum` | Country scope. Optional temporary input `cbrn_doctrine_requested_readiness_minimum`; absent input is a no-op. Initializes CBRN data, raises readiness only when below the request, and clamps to the current readiness cap. |
| `cbrn_doctrine_raise_decontamination_to_minimum` | Country scope. Optional temporary input `cbrn_doctrine_requested_decontamination_minimum`; absent input is a no-op. Initializes data, raises capacity only when below the request, and clamps to 0-100. |
| `cbrn_doctrine_apply_institutional_band` | Country scope. Optional temporary inputs `cbrn_doctrine_requested_readiness_cap` and `cbrn_doctrine_requested_readiness_minimum`. Applies whichever values exist through the shared readiness helpers; missing values do nothing. |
| `cbrn_doctrine_pay_command_power` | Country scope. Optional temporary input `cbrn_doctrine_command_power_cost`. Negates and debits that amount; callers must pass an affordability trigger first. Missing input is a no-op. |

Example:

```txt
set_temp_variable = { cbrn_doctrine_requested_readiness_cap = constant:cbrn_doctrine_readiness.protective_foundation_cap }
set_temp_variable = { cbrn_doctrine_requested_readiness_minimum = constant:cbrn_doctrine_readiness.protective_foundation_minimum }
cbrn_doctrine_apply_institutional_band = yes
```

### Adoption, establishment, and training

| Effect | Purpose and side effects |
| --- | --- |
| `cbrn_chaos_warfare_adopt` | Initializes the country model, records adoption/program/command flags and cumulative mask-production baseline, closes offensive authority, removes the legacy Concentration unlock, applies the 39/10 adoption band, unlocks Operations HQ plus Gas Mask/Decon support, and activates the bounded establishment mission. The public doctrine gate must pass first. |
| `cbrn_complete_chaos_warfare_establishment` | Records successful establishment, opens institutional authority, raises readiness to 20 and decontamination capacity to 20. The mission or remediation decision owns the exact stock/formation trigger. |
| `cbrn_fail_chaos_warfare_establishment` | Records failure, retains closed offensive authority, restores Defensive Preparation policy, and lowers readiness to at most 9 without removing the doctrine. |
| `cbrn_remediate_chaos_warfare_establishment` | Calls the successful-establishment effect after the delayed decision has re-proved every requirement and paid its costs. |
| `cbrn_begin_hazard_assault_training` | Requires the public training trigger. Debits 100 masks oldest-first and 10 Army Experience, records actual mask consumption, grants 0.25 daily Hazard Assault mastery for 30 days, and activates the matching mission. Because installed `add_daily_mastery` documentation demonstrates literal numeric fields only, the centralized amount and duration variables are rendered into that block through `meta_effect`; no parser support for direct variable tokens is assumed. It creates no exposure. |

Example:

```txt
available = { cbrn_can_begin_hazard_assault_training = yes }
complete_effect = { hidden_effect = { cbrn_begin_hazard_assault_training = yes } }
```

### Exact-state decontamination

`cbrn_apply_theater_decontamination_assignment` is state scoped. The caller must pass `cbrn_state_can_receive_theater_decontamination`. It refreshes the exact state's contamination class, selects 10/8/5/3 cleanup points for Trace-or-Local/Serious/Severe/Catastrophic, applies the Theater Contamination Doctrine 1.25 multiplier when present, calls `cbrn_apply_state_contamination_delta_internal`, records only the actual removed amount on the controller, and applies a 28-day state lock. Missing or clean state input produces no useful cleanup. It never alters evidence, attribution, deaths, Condemnation, or use history.

Example:

```txt
FROM = {
	cbrn_apply_theater_decontamination_assignment = yes
}
```

### Institutional claim effects

The four claim effects are country scoped and must be preceded by their corresponding `cbrn_can_claim_*` trigger. They set one persistent milestone, apply its readiness cap/minimum, and retry every doctrine-only technology whose independent gate is now true.

| Effect | Additional result |
| --- | --- |
| `cbrn_claim_protective_foundation` | Raises decontamination capacity to 30 and unlocks the Intelligence/Weather HQ Cell and Chemical Recon Detachment. |
| `cbrn_claim_delivery_integration` | Applies the 74/45 band and opens mapped offensive-HQ gates. |
| `cbrn_claim_theater_exploitation` | Applies the 89/65 band and opens exact-state theater gates. |
| `cbrn_claim_terminal_command` | Applies the 100/85 capstone band. |

### Doctrine technology grants and commissions

`cbrn_grant_available_doctrine_technologies` is a country-scope idempotent dispatcher. It evaluates every `cbrn_can_grant_*` trigger and silently grants only eligible Hazard Pioneer, Chaos Assault, Improved Chaos Assault, Chemical Artillery Shells, Armored Agent Delivery, Mobile Decontamination Columns, Chemical Air Interdiction, and Theater CBRN Headquarters technologies. A failed gate produces no grant. It does not grant Sealed Tank Crews, Persistent Agent Shell Filling, Nerve Suppression, or Biological Security Assault, which require explicit paid commissions.

The four country-scope commission completion effects are `cbrn_commission_sealed_tank_crews`, `cbrn_commission_persistent_agent_shell_filling`, `cbrn_commission_nerve_agent_suppression`, and `cbrn_commission_biological_security_assault`. Each rechecks its exact grant trigger and silently grants only its named technology. Missing prerequisites at completion fail closed; Political Power and Command Power are owned by the decision. In particular, the nerve-suppression commission requires the explicit occupation-policy authorization flag; no Chaos Warfare use-policy tier supplies it.

Example:

```txt
remove_effect = {
	hidden_effect = { cbrn_commission_sealed_tank_crews = yes }
}
```

### Track and mastery record effects

These country-scope effects translate current native doctrine state into stable flags used by institutions, policy, HQ, AI, and migration. They have no temporary inputs. Repeated calls are idempotent except that mapped technology dispatchers may grant a newly eligible technology.

- Adoption records: `cbrn_record_hazard_assault_adoption`, `cbrn_record_toxic_armored_adoption`, `cbrn_record_contaminant_fire_support_adoption`, and `cbrn_record_integrated_command_adoption`. Contaminant Fire additionally unlocks its ammunition train; Integrated Command unlocks Operations HQ.
- Hazard Assault rewards: `cbrn_record_infantry_mastery_one`, `cbrn_record_infantry_mastery_two`, `cbrn_record_infantry_mastery_three`, `cbrn_record_infantry_mastery_four`, and `cbrn_record_infantry_mastery_five`.
- Toxic Armor rewards: `cbrn_record_armor_mastery_one`, `cbrn_record_armor_mastery_two`, `cbrn_record_armor_mastery_three`, `cbrn_record_armor_mastery_four`, and `cbrn_record_armor_mastery_five`.
- Contaminant Fire rewards: `cbrn_record_combat_support_mastery_one`, `cbrn_record_combat_support_mastery_two`, `cbrn_record_combat_support_mastery_three`, `cbrn_record_combat_support_mastery_four`, and `cbrn_record_combat_support_mastery_five`. Levels 3-5 retain stable legacy operation flags while following the accepted payload pipeline.
- Integrated Command rewards: `cbrn_record_operations_mastery_one`, `cbrn_record_operations_mastery_two`, `cbrn_record_operations_mastery_three`, `cbrn_record_operations_mastery_four`, and `cbrn_record_operations_mastery_five`. These unlock mapped HQ companies, raise decontamination capacity at level 3, and retry doctrine technology grants.
- Native track completion records: `cbrn_record_native_infantry_track_complete`, `cbrn_record_native_combat_support_track_complete`, `cbrn_record_native_armor_track_complete`, and `cbrn_record_native_operations_track_complete`.

### Policy, Condemnation, and migration

`cbrn_change_chaos_warfare_use_policy` is country scoped. Required temporary inputs are those of `cbrn_set_use_policy` plus `cbrn_policy_command_power_cost`. When the shared setter accepts the request, it debits Command Power, applies a 90-day reassessment flag, updates peak policy, and records reached policy-history flags. Rejected policy input causes no debit or history change. It never sets `cbrn_nerve_suppression_policy_authorized`; the later CBRN Coercive Security occupation-policy surface owns that authorization.

`cbrn_set_doctrine_condemnation_mult_from_country` is country scoped and writes temporary `cbrn_action_doctrine_condemnation_mult` as 1.00, 0.90, 0.80, or 0.70 from Integrated Command mastery. The non-baseline values read the canonical `chem_integrated_operations.condemnation_mult` ladder also used by not-yet-migrated chemical and biological adapters, preventing parallel tuning tables during route migration. It clamps to the shared doctrine floor/ceiling and changes no persistent state. The helper is Condemnation-only and never touches evidence, attribution, deaths, contamination, medical saturation, domestic penalties, use counters, or history.

`cbrn_migrate_legacy_chaos_warfare` is an idempotent country-scope compatibility effect. For countries with Chaos Warfare, it initializes the model, removes the legacy Concentration unlock, reconstructs adoption and mastery flags from native doctrine state, restores the appropriate readiness cap, and retries legitimate doctrine technology grants. New games call it from `on_startup`; because that on-action does not run when a save is loaded, an old doctrine holder lacking `cbrn_chaos_warfare_adopted` receives the one-time zero-cost `cbrn_convene_institutional_review` decision instead. It does not auto-claim cross-track institutions, fabricate stock/formation proof, or grant a delivery consequence.

Example:

```txt
cbrn_set_doctrine_condemnation_mult_from_country = yes
# temporary cbrn_action_doctrine_condemnation_mult is now ready for the shared record
```

## CBRN Army Headquarters operation effects

These effects are defined in `cbrn_hq_effects.txt`. Character-scope effects expect a deployed army commander; `OWNER` is that commander's country. They never select a state, choose an agent, consume an unspecified payload, or call the shared exposure pipeline.

### Operation-state and preparation helpers

| Effect | Purpose, inputs, outputs, and side effects |
| --- | --- |
| `cbrn_hq_reset_operating_package` | Character-scope internal initializer with no required input. Sets every temporary operating-debit field—masks, filter wear, decontamination equipment, instruments, support equipment, trucks, fuel, medical capacity, and manpower—to zero before a package setter fills the applicable fields. It changes no persistent value or stock by itself. |
| `cbrn_hq_set_committed_force_band` | Character scope. Reads exact `num_battalions` through the force-band triggers and stores the light, standard, or mass enum in `cbrn_hq_committed_force_band`. Missing/invalid army size falls into the mass fail-safe only after the activation trigger has established a deployed command. |
| `cbrn_hq_stop_operation_benefits` | Character scope. Removes every CBRN preparation/active status trait but deliberately retains the operation code and commitments until planned cleanup. This prevents a stale delayed event from crossing into a newer operation. |
| `cbrn_hq_clear_operation_state` | Character scope. Calls the benefit cleanup and clears operation code, committed force band, and remaining upkeep ticks. It is reserved for the planned final event. |
| `cbrn_hq_calculate_preparation_days` | Character scope. Required temporary inputs: base, minimum, and maximum preparation days. Reads owner Chemical Readiness, applies the centralized readiness multiplier, rounds, and clamps into the accepted range. |
| `cbrn_hq_apply_operations_section_preparation_discount` | Character scope. Inputs: calculated preparation plus the same minimum and maximum temporary bounds. Applies the Operations Section's ten-percent preparation reduction, then reclamps and rounds. Call only for abilities that require that company. |
| `cbrn_hq_apply_high_protection_preparation_discount` | Character scope. Refreshes the owner's real military-mask snapshot and applies the accepted five-percent preparation reduction only at the high-protection threshold, then reclamps. It does not change exposure protection itself. |
| `cbrn_hq_apply_operations_commander_preparation_discount` | Character scope. Inputs: calculated preparation plus minimum/maximum bounds. Applies the doctrine-gated commander's ten-percent reduction only when the leader has `chemical_operations_commander`, then reclamps and rounds. It changes no cost, duration, cooldown, or exposure output. |
| `cbrn_hq_commit_preparation` | Character scope. Required temporary inputs: calculated preparation, active duration, full/native command-power costs, and an activation operating package. Stores the force band, debits the scripted CP remainder and real stores, applies the timed preparation trait, and schedules bounded preparation/final-cleanup events. Medical/manpower commitments recover on their planned date even if active benefits end early. |

### Model-aware operating-stock debit helpers

- `cbrn_hq_debit_decontamination_stock_oldest_first`: country scope; input `cbrn_hq_family_debit_requested`; outputs completed and remaining family debit; removes decontamination models 1 through 3 oldest-first.
- `cbrn_hq_debit_instrument_stock_oldest_first`: country scope; same contract for instrument models 1 through 3.
- `cbrn_hq_debit_command_power_remainder`: character scope; inputs full and native CP costs; subtracts only the non-native remainder from `OWNER` after clamping at zero.
- `cbrn_hq_debit_operating_package`: character scope; reads temporary mask, military-filter-condition, decon, instrument, support, truck, fuel, medical, and manpower amounts. It uses model-aware family helpers, routes every positive assigned filter debit through `cbrn_apply_military_mask_loss`, records the exact post-technology condition consumed in `cbrn_hq_filter_condition_consumption_total`, writes the other consumption ledgers, commits medical/manpower capacity, and schedules exact restoration events. The public and upkeep triggers fail closed unless the full issued-filter debit is affordable; zero inputs are no-ops.

### Activation and weekly package setters

Each setter resets all package fields before selecting the exact light, standard, or mass table. Activation setters also supply preparation, active duration, native CP, and full CP inputs. Weekly setters contain no medical or manpower recommitment.

| Operation | Activation setter | Weekly setter |
| --- | --- | --- |
| Chemical fire plan | `cbrn_hq_set_prepare_activation_package` | `cbrn_hq_set_prepare_upkeep_package` |
| Protective posture | `cbrn_hq_set_protective_activation_package` | `cbrn_hq_set_protective_upkeep_package` |
| Decontamination corridor | `cbrn_hq_set_decon_activation_package` | `cbrn_hq_set_decon_upkeep_package` |
| Sealed operational area | `cbrn_hq_set_seal_area_activation_package` | `cbrn_hq_set_seal_area_upkeep_package` |
| Antidote response | `cbrn_hq_set_antidote_activation_package` | `cbrn_hq_set_antidote_upkeep_package` |
| Infection corridor | `cbrn_hq_set_infection_activation_package` | `cbrn_hq_set_infection_upkeep_package` |
| Combined overmatch | `cbrn_hq_set_overmatch_activation_package` | `cbrn_hq_set_overmatch_upkeep_package` |

### Public ability-start effects

`cbrn_hq_start_prepare_chemical_offensive`, `cbrn_hq_start_theater_protective_posture`, `cbrn_hq_start_decontamination_corridor`, `cbrn_hq_start_seal_operational_area`, `cbrn_hq_start_mass_antidote_response`, `cbrn_hq_start_seal_infection_corridor`, and `cbrn_hq_start_combined_overmatch` are CHARACTER-scope one-time ability adapters. Their matching activation trigger must be checked first. Each stores a stable operation enum, selects the exact force-band package, calculates preparation, commits stock/CP, and schedules `cbrn_hq.1`. The two offensive preparations apply both the Operations Section and high-protection preparation adjustments. None dispatches exposure.

Example:

```txt
allowed = { cbrn_hq_can_activate_theater_protective_posture = yes }
one_time_effect = {
	hidden_effect = { cbrn_hq_start_theater_protective_posture = yes }
}
```

### Bounded upkeep effects

`cbrn_hq_debit_prepare_upkeep`, `cbrn_hq_debit_protective_upkeep`, `cbrn_hq_debit_decon_upkeep`, `cbrn_hq_debit_seal_area_upkeep`, `cbrn_hq_debit_antidote_upkeep`, `cbrn_hq_debit_infection_upkeep`, and `cbrn_hq_debit_overmatch_upkeep` select and debit one paid weekly installment from the force band stored at activation. The caller must first pass the corresponding upkeep trigger. Army reorganization after activation cannot reduce that package.

`cbrn_hq_schedule_next_upkeep_tick` schedules `cbrn_hq.2` only while the persistent finite tick budget is positive. `cbrn_hq_complete_upkeep_tick` decrements that budget and schedules the next tick when required. `cbrn_hq_fail_upkeep` removes active benefits and the tick budget while retaining the operation commitment until its already scheduled final cleanup. These targeted chains create no periodic country iteration.

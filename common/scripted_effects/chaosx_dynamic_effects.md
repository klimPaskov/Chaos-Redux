# chaosx_dynamic_effects

This registry documents the public, generally reusable effects defined in `common/scripted_effects/chaosx_dynamic_effects.txt`.

An effect belongs here when its contract is useful across events or systems, even if it currently has only one caller. Event-framework orchestration and subsystem-private helpers belong in their owning scripted-effect files and system documentation.

## Table of contents

- [modify_value_based_on_chaos_tier](#modify_value_based_on_chaos_tier)
- [calculate_economy_scaled_factory_grant](#calculate_economy_scaled_factory_grant)
- [damage_buildings_in_random_states](#damage_buildings_in_random_states)
- [get_random_sea_region](#get_random_sea_region)
- [clear_special_chaos_country_civilian_effects](#clear_special_chaos_country_civilian_effects)
- [refresh_world_threat_state](#refresh_world_threat_state)
- [union_compatible_researched_technologies_from_donor](#union_compatible_researched_technologies_from_donor)
- [call_natural_disaster](#call_natural_disaster)
- [apply_state_population_loss_without_recruitable_manpower_gain](#apply_state_population_loss_without_recruitable_manpower_gain)
- [apply_exact_state_civilian_population_loss](#apply_exact_state_civilian_population_loss)
- [Stockpile debit helpers](#stockpile-debit-helpers)

## modify_value_based_on_chaos_tier

Purpose: derive a temporary value by adding a chaos-tier-scaled increment to a supplied base.

Scope: any scope.

Inputs: `base_value` and `add_value` temporary variables.

Output: `modified_value` temporary variable.

Defaults: chaos tier `0` adds nothing, tiers `1` through `3` add one through three copies of `add_value`, and tiers above `3` add four copies.

Side effects: the effect multiplies the temporary `add_value` input in place.

Example:

```txt
set_temp_variable = { base_value = 10 }
set_temp_variable = { add_value = 2 }
modify_value_based_on_chaos_tier = yes
```

## calculate_economy_scaled_factory_grant

Purpose: convert the current country's civilian and military factory total into a bounded grant count.

Scope: country.

Inputs: positive `economy_scaled_factory_grant_step`, `economy_scaled_factory_grant_min`, and `economy_scaled_factory_grant_cap` temporary variables.

Output: `economy_scaled_factory_grant_count` temporary variable.

Defaults: the result begins at zero, counts complete step-sized blocks, stops at the cap, and then rises to the supplied minimum when necessary.

Side effects: none beyond temporary working variables. The effect does not grant buildings.

Example:

```txt
set_temp_variable = { economy_scaled_factory_grant_step = 10 }
set_temp_variable = { economy_scaled_factory_grant_min = 1 }
set_temp_variable = { economy_scaled_factory_grant_cap = 5 }
calculate_economy_scaled_factory_grant = yes
```

## damage_buildings_in_random_states

Purpose: damage a configurable number of eligible buildings in a configurable share of the current country's controlled states.

Scope: country.

Inputs: `buildings_to_damage_per_state`, `percent_of_states_to_target`, `damage_modifier`, and `state_population_percent` variables.

Outputs: direct state building damage and, when the population branch is selected, a proportional state population reduction.

Defaults: the effect derives the target-state count from controlled states and ensures that a positive percentage targets at least one state. Individual building choices with no available level receive zero random weight.

Side effects: mutates buildings or population in randomly selected controlled states and uses working variables during selection.

Example:

```txt
set_variable = { buildings_to_damage_per_state = 2 }
set_variable = { percent_of_states_to_target = 0.25 }
set_variable = { damage_modifier = 1 }
set_variable = { state_population_percent = 0.01 }
damage_buildings_in_random_states = yes
```

## get_random_sea_region

Purpose: select one strategic-region ID from the shared curated sea-region pool.

Scope: any scope.

Inputs: none.

Output: `global.rand_sea_region`.

Defaults: every branch writes a region ID. Repeated entries intentionally preserve the pool's existing weights.

Side effects: replaces `global.rand_sea_region`.

Example:

```txt
get_random_sea_region = yes
```

## clear_special_chaos_country_civilian_effects

Purpose: remove transient civilian penalties from a special Chaos country when a bounded caller decides cleanup is due.

Scope: country.

Inputs: none.

Outputs: clears `mass_panic` and removes `galaxies_mix` when present.

Defaults: absent flags or ideas produce no change.

Side effects: mutates the scoped country's flag and idea state. No periodic whole-world caller is enabled by this contract.

Example:

```txt
if = {
	limit = { is_special_chaos_country = yes }
	clear_special_chaos_country_civilian_effects = yes
}
```

## refresh_world_threat_state

Purpose: rebuild the mod-wide existential-threat aggregate after an event-owned source activates or deactivates.

Scope: any scope.

Inputs: none. Each threat system sets or clears its own registered global source flag before calling the effect.

Registered sources:

- `world_threat_source_zombies`
- `world_threat_source_holy_realm`
- `world_threat_source_mengele`
- `world_threat_source_fury`
- `world_threat_source_death`
- `world_threat_source_cannibalism`
- `world_threat_source_black_plague`
- `world_threat_source_resources_found_caves`
- `world_threat_source_brilliant_scientist`

Outputs:

- `global.world_threat_source_count`
- `world_in_threat`

Defaults: no active source produces a count of `0` and clears `world_in_threat`.

Side effects: none beyond rebuilding the aggregate count and flag.

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

## union_compatible_researched_technologies_from_donor

Purpose: add every compatible missing researched technology from a donor country to the current country without removing the recipient's existing research.

Scope: country recipient.

Input: `event_target:technology_union_donor`, saved as the donor country before the call.

Outputs: missing donor technologies granted to the recipient with popups disabled.

Defaults: technologies already held by the recipient are skipped. Flexible and streamlined production remain mutually exclusive, as do the concentrated and dispersed industry branches.

Side effects: newly granted technologies execute any engine behavior associated with `set_technology`. The effect does not change research slots, remove technologies, clear the donor target, or annex the donor.

Example:

```txt
FROM = { save_event_target_as = technology_union_donor }
union_compatible_researched_technologies_from_donor = yes
```

## call_natural_disaster

Purpose: provide the public country-scope entry point into Event 013 while Event 013 retains ownership of validation, targeting, delayed jobs, damage, Deaths registration, reports, aftermath, and follow-ups.

Scope: country.

Required temporary inputs:

- `natural_disaster_call_caller_type`: one `natural_disaster_caller.*` value.
- `natural_disaster_call_caller_event_id`: positive numeric source event ID.
- `natural_disaster_call_family`: a specific `natural_disaster_family.*` value or `random`.
- `natural_disaster_call_family_group`: one `natural_disaster_family_group.*` value. Leave it at `random` when supplying a specific family.
- `natural_disaster_call_target_mode`: one `natural_disaster_target_mode.*` value.
- `natural_disaster_call_severity`: one `natural_disaster_severity.*` value.
- `natural_disaster_call_sequence_mode`: one `natural_disaster_sequence_mode.*` value.
- `natural_disaster_call_news_policy`: one `natural_disaster_news_policy.*` value.
- `natural_disaster_call_report_policy`: one `natural_disaster_report_policy.*` value.
- `natural_disaster_call_aftermath_policy`: one `natural_disaster_aftermath_policy.*` value.
- `natural_disaster_call_chain_policy`: one `natural_disaster_chain_policy.*` value.
- `natural_disaster_call_log_mode`: one `natural_disaster_log_mode.*` value.

Target and origin inputs when required by the selected mode or family:

- `natural_disaster_call_target_region`: strategic-region ID for `selected_region`.
- `natural_disaster_call_target_state` plus `natural_disaster_call_target_state_supplied = 1` for `selected_state`.
- `natural_disaster_call_target_country` plus `natural_disaster_call_target_country_supplied = 1` for `selected_country`.
- `natural_disaster_call_origin_state` plus `natural_disaster_call_origin_state_supplied = 1` for origin-dependent ashfall, lahar, or tsunami calls.
- `natural_disaster_call_origin_family`: the physical cause at the supplied origin.
- `natural_disaster_call_origin_medium`: one `natural_disaster_origin_medium.*` value.
- Either or both target and proof pairs for `caller_provided`.

Optional scaling, sequence, and scenario inputs:

- `natural_disaster_call_sequence_count`: exact primary-impact count.
- `natural_disaster_call_death_scale`: Deaths multiplier, default `1.0`.
- `natural_disaster_call_building_scale`: building-damage multiplier, default `1.0`.
- `natural_disaster_call_damage_scale`: compatibility alias used only when `building_scale` was not supplied.
- `natural_disaster_call_warning_scale`: warning-chance multiplier.
- `natural_disaster_call_recovery_scale`: recovery-burden multiplier.
- `natural_disaster_call_supply_scale`: state-disruption multiplier.
- `natural_disaster_call_scenario_type`: validated Disaster Barrage family mix.
- `natural_disaster_call_scenario_intensity`: validated Disaster Barrage intensity.
- `natural_disaster_call_evolution_override_supplied` and `natural_disaster_call_evolution_override`: validated evolution override.
- `natural_disaster_call_manual_evolution_bypass`: scenario or debug proof for an intensity-selected evolution without a global unlock.
- `natural_disaster_call_manual_abnormal_bypass`: scenario or debug proof that bypasses only the abnormal-family cooldown.

Hostile-actor or deity callers must also provide `natural_disaster_call_caller_cost_checked`, `natural_disaster_call_caller_cooldown_checked`, and `natural_disaster_call_target_legitimacy_checked` as exact binary proofs.

Event 013 reserves `natural_disaster_call_causal_context_*`, sequence and segment overrides, `natural_disaster_call_internal_chain_override`, and `natural_disaster_log_mode.none` for validated internal continuation.

Outputs:

- `natural_disaster_call_result`: accepted or rejected.
- `natural_disaster_call_reject_reason`: stable validation failure.
- `natural_disaster_call_sequence_id`: allocated sequence ID or `0`.
- `natural_disaster_call_primary_job_count`: queued primary impacts.
- `natural_disaster_call_skipped_primary_count`: planned primary impacts omitted because no valid target pair existed.
- `natural_disaster_call_resolved_primary_family`: first successfully scheduled family or `0`.
- `natural_disaster_call_has_resolved_primary_state`: proof for `natural_disaster_call_resolved_primary_state`.
- `natural_disaster_call_has_resolved_primary_country`: proof for `natural_disaster_call_resolved_primary_country`.
- `natural_disaster_call_resolved_target_region`: successful `selected_region` echo.

Defaults: validation fails closed. Unknown enums, conflicting selectors, missing proofs, invalid scales, incompatible targets, or unauthorized bypasses reject the call and queue no work. No requested family is substituted.

Side effects: accepted calls allocate and persist delayed Event 013 jobs, may record one Event 013 history row, expose the first resolved state and country as regular event targets, and reset every public input before returning.

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

## apply_state_population_loss_without_recruitable_manpower_gain

Purpose: remove real state population without retaining the recruitable-manpower credit that HOI4 attaches to a negative state-scope `add_manpower` effect.

Scope: state.

Inputs:

- `state_population_transaction_loss`: positive population loss in people.
- `state_population_transaction_contract_supplied`: one-shot proof set to `1` immediately before the call.

Outputs:

- `state_population_transaction_reconciled_gain`: measured recruitable-manpower credit removed from the owner and distinct controller.

Defaults: a missing proof or loss produces a zero-value transaction. The requested loss is clamped to zero or above and rounded.

Side effects: the effect applies one negative state population mutation, measures the owner's and distinct controller's `manpower_k` before and after it, removes only an observed positive credit up to the requested loss, and clears the one-shot inputs.

Example:

```txt
set_temp_variable = { state_population_transaction_loss = 25000 }
set_temp_variable = { state_population_transaction_reconciled_gain = 0 }
set_temp_variable = { state_population_transaction_contract_supplied = 1 }
apply_state_population_loss_without_recruitable_manpower_gain = yes
```

## apply_exact_state_civilian_population_loss

Purpose: apply one exact civilian population loss clamped against a protected population floor while returning the amount actually removed.

Scope: state.

Inputs:

- `state_civilian_population_loss_requested`: requested people to remove.
- `state_civilian_population_loss_minimum_remaining`: protected population floor in people.
- `state_civilian_population_loss_reason`: Deaths reason ID.
- `state_civilian_population_loss_log_deaths`: `1` to use the Deaths API when enabled or `0` for an unlogged transaction.
- `state_civilian_population_loss_target_country`: country scope used by the Deaths ledger.
- `state_civilian_population_loss_has_target_country`: `1` when the supplied target is valid.
- `state_civilian_population_loss_contract_supplied`: one-shot proof set to `1` immediately before the call.

Outputs:

- `state_civilian_population_loss_applied`: rounded number of people actually removed.
- `state_civilian_population_loss_result`: `1` when a positive loss was applied or `0` otherwise.

Defaults: missing contract inputs produce a zero-value request with the unknown Deaths reason, no valid target, and a zero population floor.

Side effects: with Deaths logging active the effect passes the exact applied amount to `chaos_meter_register_deaths`. Otherwise it calls `apply_state_population_loss_without_recruitable_manpower_gain` directly. Both paths remove state population exactly once and reconcile observed recruitable-manpower credit. All public inputs are cleared before return.

Example:

```txt
set_temp_variable = { state_civilian_population_loss_requested = 25000 }
set_temp_variable = { state_civilian_population_loss_minimum_remaining = 10000 }
set_temp_variable = { state_civilian_population_loss_reason = constant:chaos_meter_deaths_reason.cannibalism_consumption }
set_temp_variable = { state_civilian_population_loss_log_deaths = 1 }
set_temp_variable = { state_civilian_population_loss_target_country = OWNER }
set_temp_variable = { state_civilian_population_loss_has_target_country = 1 }
set_temp_variable = { state_civilian_population_loss_applied = 0 }
set_temp_variable = { state_civilian_population_loss_result = 0 }
set_temp_variable = { state_civilian_population_loss_contract_supplied = 1 }
apply_exact_state_civilian_population_loss = yes
```

## Stockpile debit helpers

Purpose: remove a positive, dynamically calculated amount from a country's equipment or fuel stockpile through the current supported `add_equipment_to_stockpile` and `add_fuel` effects.

Scope: country.

Inputs: `equipment_stockpile_removal_amount` for equipment helpers or `fuel_stockpile_removal_amount` for `remove_fuel_from_stockpile`. The supplied amount must be positive.

Helpers: `remove_support_equipment_from_stockpile`, `remove_motorized_equipment_from_stockpile`, `remove_convoys_from_stockpile`, `remove_trains_from_stockpile`, `remove_plague_bombs_from_stockpile`, `remove_infantry_equipment_from_stockpile`, and `remove_fuel_from_stockpile`.

Outputs: the requested amount is removed from the matching stockpile.

Defaults: no default amount is inferred. A zero input performs a zero-value transaction.

Side effects: the helper negates its temporary amount input in place before applying the debit.

Example:

```txt
set_temp_variable = { equipment_stockpile_removal_amount = 250 }
remove_support_equipment_from_stockpile = yes

set_temp_variable = { fuel_stockpile_removal_amount = 500 }
remove_fuel_from_stockpile = yes
```

# chaosx_dynamic_effects

This registry documents the public scripted effects declared in `common/scripted_effects/chaosx_dynamic_effects.txt`. It is intentionally limited to neutral helpers with callers across multiple systems or event families.

Event-owned orchestration, validation, adapters, and lifecycle helpers belong in their owning source file and reference document. The owner index below keeps those APIs discoverable without copying their contracts into this registry.

## table_of_contents

- [calculate_economy_scaled_factory_grant](#calculate_economy_scaled_factory_grant)
- [damage_buildings_in_random_states](#damage_buildings_in_random_states)
- [get_random_sea_region](#get_random_sea_region)
- [clear_special_chaos_country_civilian_effects](#clear_special_chaos_country_civilian_effects)
- [refresh_world_threat_state](#refresh_world_threat_state)
- [union_compatible_researched_technologies_from_donor](#union_compatible_researched_technologies_from_donor)
- [call_natural_disaster](#call_natural_disaster)
- [apply_state_population_loss_without_recruitable_manpower_gain](#apply_state_population_loss_without_recruitable_manpower_gain)
- [apply_exact_state_civilian_population_loss](#apply_exact_state_civilian_population_loss)
- [stockpile_debit_helpers](#stockpile_debit_helpers)
- [owner_owned_apis](#owner_owned_apis)
- [maintenance_notes](#maintenance_notes)

## calculate_economy_scaled_factory_grant

Purpose: convert the current country's civilian and military factory total into a bounded grant count.

Scope: country.

Inputs: positive `economy_scaled_factory_grant_step`, `economy_scaled_factory_grant_min`, and `economy_scaled_factory_grant_cap` temporary variables.

Output: `economy_scaled_factory_grant_count` temporary variable.

Defaults: the result starts at zero, counts complete step-sized blocks, stops at the cap, and rises to the supplied minimum when necessary.

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

Inputs: `buildings_to_damage_per_state`, `percent_of_states_to_target`, `damage_modifier`, and optional `state_population_percent` temporary variables.

Outputs: direct state building damage and, when requested, a proportional state population reduction in selected states.

Defaults: a positive target percentage selects at least one state. Building types that are unavailable in a selected state receive no random weight.

Side effects: mutates buildings or population in randomly selected controlled states and uses temporary selection variables.

Example:

```txt
set_temp_variable = { buildings_to_damage_per_state = 2 }
set_temp_variable = { percent_of_states_to_target = 0.25 }
set_temp_variable = { damage_modifier = 1 }
set_temp_variable = { state_population_percent = 0.01 }
damage_buildings_in_random_states = yes
```

## get_random_sea_region

Purpose: select one strategic-region ID from the shared curated sea-region pool.

Scope: any scope.

Inputs: none.

Output: `global.rand_sea_region`.

Defaults: every branch writes a region ID. Repeated entries preserve the pool's existing weighting.

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

Defaults: absent flags or ideas produce no change. The registry does not enable a periodic whole-world caller.

Side effects: mutates the scoped country's flag and idea state.

Example:

```txt
if = {
	limit = { is_special_chaos_country = yes }
	clear_special_chaos_country_civilian_effects = yes
}
```

## refresh_world_threat_state

Purpose: rebuild the mod-wide existential-threat aggregate after an owning system activates or deactivates its source.

Scope: any scope.

Inputs: none. Each threat system sets or clears its own registered global source flag before calling the effect.

Registered sources: `world_threat_source_zombies`, `world_threat_source_holy_realm`, `world_threat_source_mengele`, `world_threat_source_fury`, `world_threat_source_death`, `world_threat_source_cannibalism`, `world_threat_source_black_plague`, `world_threat_source_resources_found_caves`, and `world_threat_source_brilliant_scientist`.

Outputs: `global.world_threat_source_count` and the `world_in_threat` global flag.

Defaults: no active source produces a count of `0` and clears `world_in_threat`.

Side effects: rebuilds the aggregate count and flag only.

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

Purpose: add every compatible missing researched technology from a donor country without removing the recipient's existing research.

Scope: country recipient.

Input: `event_target:technology_union_donor`, saved as the donor country before the call.

Output: missing donor technologies are granted to the recipient with popups disabled.

Defaults: technologies already held by the recipient are skipped. Flexible and streamlined production remain mutually exclusive, as do the concentrated and dispersed industry branches.

Side effects: newly granted technologies execute the normal `set_technology` behavior. The effect does not change research slots, remove technologies, clear the donor target, or annex the donor.

Example:

```txt
FROM = { save_event_target_as = technology_union_donor }
union_compatible_researched_technologies_from_donor = yes
```

## call_natural_disaster

Purpose: provide the stable country-scope gateway for callers that need to start a natural-disaster sequence.

Scope: country.

Contract: callers set the documented `natural_disaster_call_*` temporary inputs and any required regular event targets, then call `call_natural_disaster = yes`. The gateway delegates validation, target resolution, delayed work, impact, reports, aftermath, and cleanup to the Event 013 owner.

Outputs: `natural_disaster_call_result`, `natural_disaster_call_reject_reason`, `natural_disaster_call_sequence_id`, `natural_disaster_call_primary_job_count`, `natural_disaster_call_skipped_primary_count`, and the documented resolved-target proofs.

Defaults: invalid or incomplete input fails closed and queues no work. The gateway resets public call inputs after each call while leaving result and proof outputs available to the caller.

Full input, target, origin, authority, and scaling details are documented in [`natural_disasters_overview`](../../docs/events/013_natural_disasters/overview.md).

Example:

```txt
set_temp_variable = { natural_disaster_call_family = constant:natural_disaster_family.earthquake }
set_temp_variable = { natural_disaster_call_target_mode = constant:natural_disaster_target_mode.random_valid }
call_natural_disaster = yes
```

## apply_state_population_loss_without_recruitable_manpower_gain

Purpose: remove real state population without retaining the recruitable-manpower credit that HOI4 attaches to a negative state-scope `add_manpower` effect.

Scope: state.

Inputs: positive `state_population_transaction_loss` and one-shot `state_population_transaction_contract_supplied = 1` temporary variables.

Output: `state_population_transaction_reconciled_gain`, the observed recruitable-manpower credit removed from the owner and distinct controller.

Defaults: a missing proof or loss produces a zero-value transaction. The requested loss is clamped to zero or above and rounded.

Side effects: applies one negative state population mutation, reconciles only observed positive credit up to the requested loss, and clears the one-shot inputs.

Example:

```txt
set_temp_variable = { state_population_transaction_loss = 25000 }
set_temp_variable = { state_population_transaction_contract_supplied = 1 }
apply_state_population_loss_without_recruitable_manpower_gain = yes
```

## apply_exact_state_civilian_population_loss

Purpose: apply one exact civilian population loss against a protected population floor while returning the amount actually removed.

Scope: state.

Inputs: `state_civilian_population_loss_requested`, `state_civilian_population_loss_minimum_remaining`, `state_civilian_population_loss_reason`, `state_civilian_population_loss_log_deaths`, `state_civilian_population_loss_target_country`, `state_civilian_population_loss_has_target_country`, and one-shot `state_civilian_population_loss_contract_supplied` temporary variables.

Outputs: `state_civilian_population_loss_applied` and `state_civilian_population_loss_result`.

Defaults: missing contract inputs produce a zero-value request with the unknown Deaths reason, no valid target, and a zero population floor.

Side effects: applies the loss once, optionally registers the exact amount through `chaos_meter_register_deaths`, reconciles observed recruitable-manpower credit, and clears all public inputs before return.

Example:

```txt
set_temp_variable = { state_civilian_population_loss_requested = 25000 }
set_temp_variable = { state_civilian_population_loss_minimum_remaining = 10000 }
set_temp_variable = { state_civilian_population_loss_reason = constant:chaos_meter_deaths_reason.cannibalism_consumption }
set_temp_variable = { state_civilian_population_loss_log_deaths = 1 }
set_temp_variable = { state_civilian_population_loss_target_country = OWNER }
set_temp_variable = { state_civilian_population_loss_has_target_country = 1 }
set_temp_variable = { state_civilian_population_loss_contract_supplied = 1 }
apply_exact_state_civilian_population_loss = yes
```

## stockpile_debit_helpers

Purpose: remove dynamically calculated positive amounts from supported equipment and fuel stockpiles.

Scope: country.

Helpers: `remove_support_equipment_from_stockpile`, `remove_motorized_equipment_from_stockpile`, `remove_convoys_from_stockpile`, `remove_trains_from_stockpile`, `remove_plague_bombs_from_stockpile`, `remove_infantry_equipment_from_stockpile`, and `remove_fuel_from_stockpile`.

Inputs: `equipment_stockpile_removal_amount` for equipment helpers or `fuel_stockpile_removal_amount` for `remove_fuel_from_stockpile`.

Defaults: no amount is inferred. A zero input performs a zero-value transaction.

Side effects: each helper negates its temporary amount in place and applies the matching stockpile debit through the supported engine effect.

Example:

```txt
set_temp_variable = { equipment_stockpile_removal_amount = 250 }
remove_support_equipment_from_stockpile = yes

set_temp_variable = { fuel_stockpile_removal_amount = 500 }
remove_fuel_from_stockpile = yes
```

## owner_owned_apis

The following APIs are useful to other systems but are not declared in this registry. Use the named owner source and documentation for their contracts. This index is deliberately not a second copy of those event or subsystem implementations.

| capability | authoritative_source | reference |
| --- | --- | --- |
| `independence_wave_ledger` | [`006_independence_wave_iberian_package_effects.txt`](006_independence_wave_iberian_package_effects.txt) | [`independence_wave_effects`](006_independence_wave_effects.md) |
| `custom_technology_grants` | [`016_brilliant_scientist_custom_technology_api_effects.txt`](016_brilliant_scientist_custom_technology_api_effects.txt) | [`custom_technology_api`](../../docs/events/016_brilliant_scientist/systems/custom_technology_api.md) |
| `clone_system` | [`clone_system_effects.txt`](clone_system_effects.txt) | [`clone_equipment_and_infantry`](../../docs/systems/3d_model_pipeline/clone_equipment_and_infantry.md) |
| `alien_infantry` | [`016_alien_infantry_api_effects.txt`](016_alien_infantry_api_effects.txt) and [`016_alien_infantry_api_triggers.txt`](../scripted_triggers/016_alien_infantry_api_triggers.txt) | [`alien_infantry_api_effects`](016_alien_infantry_api_effects.md) |
| `project_bridge` | [`016_mengele_project_bridge_effects.txt`](016_mengele_project_bridge_effects.txt) and [`016_mengele_project_bridge_triggers.txt`](../scripted_triggers/016_mengele_project_bridge_triggers.txt) | [`project_system`](../../docs/events/016_brilliant_scientist/systems/projects.md) |
| `universal_cost_framework` | [`chaosx_universal_cost_effects.txt`](chaosx_universal_cost_effects.txt) and [`chaosx_universal_cost_triggers.txt`](../scripted_triggers/chaosx_universal_cost_triggers.txt) | [`universal_cost_modifier`](../../docs/systems/universal_cost_modifier.md) |
| `unit_family_registry` | [`019_infantry_spawn_unit_registry_effects.txt`](019_infantry_spawn_unit_registry_effects.txt) | [`chaos_unit_family_registry`](../../docs/systems/cbrn_warfare/chaos_unit_family_registry.md) |
| `famine_runtime` | [`famine_core_effects.txt`](famine_core_effects.txt) and [`famine_adapter_effects.txt`](famine_adapter_effects.txt) | [`famine_system`](../../docs/systems/famine_system.md) |
| `migration_runtime` | [`migration_core_effects.txt`](migration_core_effects.txt) and [`migration_adapter_effects.txt`](migration_adapter_effects.txt) | [`migration_system`](../../docs/systems/migration_system.md) |
| `humanitarian_validation` | [`humanitarian_validation_triggers.txt`](../scripted_triggers/humanitarian_validation_triggers.txt) | [`famine_system`](../../docs/systems/famine_system.md) and [`migration_system`](../../docs/systems/migration_system.md) |

## maintenance_notes

Add a helper here only when its contract is neutral and its callers cross subsystem or event-family boundaries. Give it a descriptive name based on its behavior, not the event that first needed it.

Keep one-event orchestration, event-specific selectors, lifecycle state, and private adapters in the owning source file. A cross-event public gateway may remain in this registry while delegating its owner-specific runtime to the owning source file.

When a shared helper changes, update its contract here and audit every call site. When an owner API changes, update the owner documentation and change only the corresponding index row here.

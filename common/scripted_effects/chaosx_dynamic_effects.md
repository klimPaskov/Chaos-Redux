# chaosx_dynamic_effects

This registry documents the public scripted effects declared in `common/scripted_effects/chaosx_dynamic_effects.txt`. It is intentionally limited to neutral helpers with callers across multiple systems or event families.

Event-owned orchestration, validation, adapters, and lifecycle helpers belong in their owning source file and reference document. The owner index below keeps those APIs discoverable without copying their contracts into this registry.

## table_of_contents

- [calculate_economy_scaled_factory_grant](#calculate_economy_scaled_factory_grant)
- [damage_state_building_dynamic](#damage_state_building_dynamic)
- [damage_buildings_in_random_states](#damage_buildings_in_random_states)
- [get_random_sea_region](#get_random_sea_region)
- [clear_special_chaos_country_civilian_effects](#clear_special_chaos_country_civilian_effects)
- [refresh_world_threat_state](#refresh_world_threat_state)
- [union_compatible_researched_technologies_from_donor](#union_compatible_researched_technologies_from_donor)
- [call_natural_disaster](#call_natural_disaster)
- [apply_state_population_loss_without_recruitable_manpower_gain](#apply_state_population_loss_without_recruitable_manpower_gain)
- [apply_exact_state_civilian_population_loss](#apply_exact_state_civilian_population_loss)
- [stockpile_debit_helpers](#stockpile_debit_helpers)
- [cbrn_debit_motorized_stockpile_oldest_first](#cbrn_debit_motorized_stockpile_oldest_first)
- [chaosx_convert_days_to_date_offset](#chaosx_convert_days_to_date_offset)
- [chaosx_convert_date_offset_to_days](#chaosx_convert_date_offset_to_days)
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

## damage_state_building_dynamic

Purpose: apply a caller-selected building type and numeric damage amount in the current state through `meta_effect`, which supplies literal damage text to `damage_building`.

Scope: state.

Inputs: required caller-set temporary variables `dynamic_building_damage_type`, containing a building token such as `token:infrastructure`, and `dynamic_building_damage_amount`, containing the numeric damage amount.
The helper reads both inputs without changing them.

Output: one native `damage_building` effect in the current state with the requested building type and amount.
There is no output variable.

Defaults: none.
The caller must initialize both inputs before use in the same effect chain.
The amount can be initialized once before a bounded group of calls when no intervening effect overwrites it.
An unset input is a caller error, and zero is an explicit amount rather than an absence sentinel.
The helper applies no explicit arithmetic rounding, clamp, scaling, repair modifier, or replacement amount.
Numeric interpolation uses the engine default formatter, matching the existing shared damage helper.
The current Acid Rain amount of one is preserved, while exact serialization of arbitrary fractional or large amounts requires separate runtime validation.

Side effects: building damage only.
The native effect retains its state-building lookup and, for province buildings, its search for the first matching province building in the current state.
The helper performs no random selection or scope change and writes no variables, flags, or event targets.
Temporary inputs last for the caller's effect chain, so no persistent cleanup is required.
Callers must overwrite inputs before an independent operation that requires different values.

Example, inside the state already selected by the caller:

```txt
set_temp_variable = { dynamic_building_damage_amount = acid_rain_damage_one }
set_temp_variable = { dynamic_building_damage_type = token:infrastructure }
damage_state_building_dynamic = yes
set_temp_variable = { dynamic_building_damage_type = token:arms_factory }
damage_state_building_dynamic = yes
```

Call sites: the building-damage loop in `common/scripted_effects/033_acid_rain_effects.txt` and the transport, depot, port, and arms-theft incident branches in `common/scripted_effects/031_random_terror_effects.txt`.
Building selection, damage tuning, and eligibility remain caller-owned.

References: vanilla `documentation/effects_documentation.md` sections `damage_building` and `meta_effect`, vanilla `common/scripted_effects/00_scripted_effects.txt` effect `SF_PARA_sabotage_effect`, and the building-token interpolation in `natural_disaster_damage_selected_building` in `common/scripted_effects/013_natural_disasters_effects.txt`.
The shared `damage_buildings_in_random_states` helper uses the same unformatted numeric interpolation.
The offline Data structures and Localisation pages document building tokens and `GetTokenKey`.

## damage_buildings_in_random_states

Purpose: damage a configurable number of eligible buildings in a configurable share of the current country's owned and controlled states.

Scope: country.

Inputs: `buildings_to_damage_per_state`, `percent_of_states_to_target`, `damage_modifier`, and optional `state_population_percent` temporary variables.

Outputs: direct state building damage and, when `state_population_percent` is above zero, a proportional population reduction in each selected state.
The reduction is the state population in thousands times that share, applied as a negative `add_manpower` amount.

Defaults: the helper counts the country's controlled states from zero and targets that count times `percent_of_states_to_target`, rounded and never below one while at least one controlled state exists.
A `percent_of_states_to_target` of zero becomes `0.1`, a `damage_modifier` of zero becomes `0.25`, and a `buildings_to_damage_per_state` below one becomes `3`.
Each target is chosen from the country's owned and controlled states that hold at least one targetable building, and building types that are unavailable in a selected state receive no random weight.
A missing or zero `state_population_percent` leaves population unchanged.

Side effects: mutates buildings or population in randomly selected controlled states and uses temporary selection variables.

This helper does not register deaths in the shared Deaths ledger, because the population branch changes manpower directly.
Callers that need ledger registration use `apply_exact_state_civilian_population_loss`.
The helper currently has no callers and is kept as a documented shared hook.

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

Registered sources: `world_threat_source_zombies`, `world_threat_source_holy_realm`, `world_threat_source_mengele`, `world_threat_source_fury`, `world_threat_source_death`, `world_threat_source_cannibalism`, `world_threat_source_black_plague`, `world_threat_source_resources_found_caves`, `world_threat_source_brilliant_scientist`, and `world_threat_source_sov_nuclear_bombs`.

The `world_threat_source_sov_nuclear_bombs` source counts only while none of `fallout_transition_active`, `fallout_active`, `world_end_final_silence`, and `world_end_final_silence_completed` is set, so the nuclear-bomb source stops contributing once fallout or the Final Silence takes over.

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

`state_civilian_population_loss_result` is `0` when no population was removed and `1` when a positive amount was applied, whichever branch below handled the removal.
`state_civilian_population_loss_applied` is the requested amount clamped between zero and the state population above the protected floor, rounded.

Defaults: missing contract inputs produce a zero-value request with the unknown Deaths reason, no valid target, and a zero population floor.

Side effects: applies the loss once, optionally registers the exact amount through `chaos_meter_register_deaths`, reconciles observed recruitable-manpower credit, and clears all public inputs before return.

The applied amount is registered through `chaos_meter_register_deaths` only when `state_civilian_population_loss_log_deaths` is above zero and either the Deaths ledger is enabled (`settings_chaos_deaths_disabled` is not set) or one of the fallout states `fallout_air_cleanliness_disabled`, `fallout_transition_active`, `fallout_active`, `fallout_manual_scenario_active`, `fallout_manual_sweep_active`, or `fallout_manual_countdown_active` is set.
In the deaths-disabled branch, which also handles any request with the log flag at zero, the loss is applied through `apply_state_population_loss_without_recruitable_manpower_gain` and nothing is written to the Deaths ledger, while the result value stays `1`.

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

## cbrn_debit_motorized_stockpile_oldest_first

Purpose: debit a requested number of CBRN trucks from the country's real motorized stockpile, taking `motorized_equipment_0` before `motorized_equipment_1`, and report how many trucks were actually removed.

Scope: country.

Input: caller-set temporary `cbrn_motorized_stock_debit_requested`, expressed as a nonnegative whole truck count. The helper reads this input without changing it.

Outputs: temporary `cbrn_motorized_stock_debit_completed` is the total removed from both models; temporary `cbrn_motorized_stock_debit_remaining` is the unmet part of the nonnegative request. Both are overwritten on every call.

Defaults: an unset request has no inferred value and is a caller error. A zero or negative request removes zero trucks. Each model's available stock is floored at zero, and each debit is limited to that model's actual stock and the remaining request. The caller must round any calculated price before showing and passing it so the display and debit use the same whole count.

Side effects: removes up to the requested number of `motorized_equipment_0` and then `motorized_equipment_1` from the scoped country's stockpile. It writes only temporary working variables and the two outputs; it creates no persistent flags, variables, or event targets and needs no cleanup. The helper does not grant the operation or enforce affordability: the caller must check full affordability before debiting, then use `completed` for consumption records and block the operation if any request remains.

Example, inside the paying country scope after the caller has calculated and displayed the same integer cost:

```txt
set_temp_variable = { cbrn_motorized_stock_debit_requested = cbrn_hq_motorized_debit }
cbrn_debit_motorized_stockpile_oldest_first = yes
add_to_variable = { cbrn_hq_motorized_losses_total = cbrn_motorized_stock_debit_completed }
```

The separate `remove_motorized_equipment_from_stockpile` helper is a legacy archetype debit and has no actual-payment output. CBRN callers that need exact payment should use this model-specific helper.

## chaosx_convert_days_to_date_offset

Purpose: convert a day count into the date-variable encoding so it can be added to `global.date` or to a stored copy of it.
Date variables count one game hour as 0.00001, so one day is 0.00024 date units, and adding a raw day count to a stored date moves it decades instead of days.

Scope: any scope. Temporary variables are unscoped, and the helper reads no scope data.

Input: caller-set temporary `chaosx_date_days`, a day count. The helper reads it without changing it.

Output: temporary `chaosx_date_offset`, the matching date-unit offset. It is overwritten on every call.
The caller must set `chaosx_date_offset` before the call, for example to `constant:chaosx_date_units.zero`, because a temporary variable first created inside a scripted effect may not survive the effect's return, while one defined before the call is carried in and modified in place.

Defaults: an unset input reads as zero and returns a zero offset.
Whole-day inputs, positive or negative, convert exactly.
Fractional days are converted at the engine's one-hour date resolution and round up to the next whole hour, so a due date built from the offset never lands before the requested duration has passed.
Negative inputs produce a negative offset for comparisons against past dates.

Side effects: none beyond temporary variables. The helper writes the private working value `chaosx_date_unrounded_hours`, which is not an output, and changes no date, flag, country, state, or persistent variable.

Constants: category `chaosx_date_units` in [`chaosx_date_units_constants.txt`](../script_constants/chaosx_date_units_constants.txt), using `hours_per_day`, `hour_step`, and `hours_per_date_unit`.
The day count is multiplied by `hours_per_day` and divided by `hours_per_date_unit`, so the int schema needs no five-decimal literal, and the five-decimal variable precision represents every whole-hour result exactly.

Example, storing a due date a tuned number of days ahead:

```txt
set_temp_variable = { chaosx_date_days = constant:my_system_tuning.due_days }
set_temp_variable = { chaosx_date_offset = constant:chaosx_date_units.zero }
chaosx_convert_days_to_date_offset = yes
set_variable = { my_system_due_date = global.date }
add_to_variable = { my_system_due_date = chaosx_date_offset }
```

Keep native `days =` fields, mission durations, timed flag durations, AI scores, and MTTH values in days.
Convert only the value that is written into or compared with a stored date, and copy an already encoded stored date without converting it again.

## chaosx_convert_date_offset_to_days

Purpose: convert a date difference, such as a stored due date minus `global.date`, into a whole-day count for native `days =` delays and day-based displays.

Scope: any scope. Temporary variables are unscoped, and the helper reads no scope data.

Input: caller-set temporary `chaosx_date_offset`, a difference between two date-variable values. The helper reads it without changing it.

Output: temporary `chaosx_date_days`, whole days rounded up and never below zero. It is overwritten on every call.
The caller must set `chaosx_date_days` before the call, for example to `constant:chaosx_date_units.zero`, because a temporary variable first created inside a scripted effect may not survive the effect's return.

Defaults: an unset input reads as zero and returns zero days.
Any partial day rounds up to the next whole day, so a delayed event or timed effect that waits the returned number of days resolves on or after the stored date, never before it.
A date that has already passed returns zero.

Side effects: none beyond temporary variables. The helper writes the private working value `chaosx_date_unrounded_days`, which is not an output, and changes no date, flag, country, state, or persistent variable.

Constants: category `chaosx_date_units`, using `hours_per_date_unit`, `hours_per_day`, `day_step`, and `zero`.
The offset is multiplied by `hours_per_date_unit` into whole hours and divided by `hours_per_day`; a remainder of even one hour leaves a fraction of at least one twenty-fourth, which the round-up step always detects.

Example, waking a worker on the stored due date:

```txt
set_temp_variable = { chaosx_date_offset = my_system_due_date }
subtract_from_temp_variable = { chaosx_date_offset = global.date }
set_temp_variable = { chaosx_date_days = constant:chaosx_date_units.zero }
chaosx_convert_date_offset_to_days = yes
set_temp_variable = { my_system_wake_days = chaosx_date_days }
```

Pass the returned day count to a field that accepts a variable, such as the `days` of a delayed `country_event` in the Event 013 job queue, or through `meta_effect` where a native field accepts only literal text.
Calling this helper overwrites `chaosx_date_days`, so copy a day input that another consumer still needs before the call.

References: the offline Data structures page, Game variables table, `date` row, documents one game hour as 0.00001 and the zero point of the encoding, and its Variables section documents the five-decimal variable precision and the scripted-effect temporary variable lifetime rule.
Installed `documentation/dynamic_variables_documentation.md` describes `date` as a comparable date value, and `documentation/script_concept_documentation.md` and `common/script_constants/documentation.md` define the schema-first constant groups and `constant:` access in variable operations.
Both helpers generalize the Event 013 `natural_disaster_convert_days_to_date_offset` and `natural_disaster_convert_date_offset_to_days` converters and the Event 021 `event021_days_to_date_offset` hour-rounding converter, which remain owner-private.

## owner_owned_apis

The following APIs are useful to other systems but are not declared in this registry. Use the named owner source and documentation for their contracts. This index is deliberately not a second copy of those event or subsystem implementations.

| capability | authoritative_source | reference |
| --- | --- | --- |
| `event021_calendar_conversion` | [`021_random_civil_war_date_effects.txt`](021_random_civil_war_date_effects.txt) | [`date_effects`](021_random_civil_war_date_effects.md), ANY-scope caller-owned day input/encoded-date output, hour rounding, defaults, side effects, and example |
| `cbrn_state_mask_escrow` | [`cbrn_state_escrow_native_effects.txt`](cbrn_state_escrow_native_effects.txt) and [`cbrn_protection_effects.txt`](cbrn_protection_effects.txt) | [measured concrete-model reservation/refund API](cbrn_scripted_effects.md#measured-native-state-escrow-primitives), including COUNTRY stock observations, STATE original-donor receipts, caller-owned outputs, partial refunds, exact mismatch quarantine, and cleanup |
| `test_country_facilities_and_projects` | [`chaosx_test_country_effects.txt`](chaosx_test_country_effects.txt), [`chaosx_test_country_special_project_effects.txt`](chaosx_test_country_special_project_effects.txt), and [`chaosx_test_country_triggers.txt`](../scripted_triggers/chaosx_test_country_triggers.txt) | [`chaosx_test_country`](../../docs/testing/chaosx_test_country.md), including the temporary building-token and `sp:` object inputs, construction legality, idempotence, and cleanup contracts |
| `independence_wave_ledger` | [`006_independence_wave_iberian_package_effects.txt`](006_independence_wave_iberian_package_effects.txt) | [`independence_wave_effects`](006_independence_wave_effects.md) |
| `custom_technology_grants` | [`016_brilliant_scientist_custom_technology_api_effects.txt`](016_brilliant_scientist_custom_technology_api_effects.txt) | [`custom_technology_api`](016_brilliant_scientist_custom_technology_api_effects.md), including the country-scope `chaosx_custom_technology_source_is_valid` provenance query and usage example |
| `conventional_technology_packages` | [`016_conventional_technology_api_effects.txt`](016_conventional_technology_api_effects.txt) and [`016_conventional_technology_api_triggers.txt`](../scripted_triggers/016_conventional_technology_api_triggers.txt) | [`conventional_technology_api_effects`](016_conventional_technology_api_effects.md), including six package families, Deployment/Weaponization tiers, and one shared computation-slot owner |
| `biological_operations` | [`016_brilliant_scientist_biological_operations_effects.txt`](016_brilliant_scientist_biological_operations_effects.txt) and [`016_brilliant_scientist_biological_operations_triggers.txt`](../scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt) | [`biological_operations`](../../docs/events/016_brilliant_scientist/systems/biological_operations.md) |
| `portal_beachhead_lifecycle` | [`016_brilliant_scientist_raid_effects.txt`](016_brilliant_scientist_raid_effects.txt) and [`016_brilliant_scientist_raid_triggers.txt`](../scripted_triggers/016_brilliant_scientist_raid_triggers.txt) | [`portal_raider_api`](../../docs/events/016_brilliant_scientist/systems/portal_raider_api.md) |
| `clone_system` | [`clone_system_effects.txt`](clone_system_effects.txt) | [`clone_equipment_and_infantry`](../../docs/systems/3d_model_pipeline/clone_equipment_and_infantry.md) |
| `alien_infantry` | [`016_alien_infantry_api_effects.txt`](016_alien_infantry_api_effects.txt) and [`016_alien_infantry_api_triggers.txt`](../scripted_triggers/016_alien_infantry_api_triggers.txt) | [`alien_infantry_api_effects`](016_alien_infantry_api_effects.md) |
| `project_bridge` | [`016_mengele_project_bridge_effects.txt`](016_mengele_project_bridge_effects.txt) and [`016_mengele_project_bridge_triggers.txt`](../scripted_triggers/016_mengele_project_bridge_triggers.txt) | [`project_system`](../../docs/events/016_brilliant_scientist/systems/projects.md) |
| `universal_cost_framework` | [`chaosx_universal_cost_effects.txt`](chaosx_universal_cost_effects.txt), [`chaosx_universal_cost_triggers.txt`](../scripted_triggers/chaosx_universal_cost_triggers.txt), and [`chaosx_universal_cost_exact_triggers.txt`](../scripted_triggers/chaosx_universal_cost_exact_triggers.txt) | [`universal_cost_modifier`](../../docs/systems/universal_cost_modifier.md) and [exact quotation contracts](../scripted_triggers/chaosx_universal_cost_exact_triggers.md) |
| `black_friday_sale_prices` | [`026_black_friday_price_table_effects.txt`](026_black_friday_price_table_effects.txt) | [`sale price table`](026_black_friday_price_table_effects.md): one global political power price per registered ordinary amount for native decision `cost =`, ANY-scope quote/apply/restore/versioned initialize, caller-owned output, ceiling with a minimum of 1, zero kept, registration steps, and example |
| `unit_family_registry` | [`019_infantry_spawn_unit_registry_effects.txt`](019_infantry_spawn_unit_registry_effects.txt) | [`chaos_unit_family_registry`](../../docs/systems/cbrn_warfare/chaos_unit_family_registry.md) |
| `famine_runtime` | [`famine_core_effects.txt`](famine_core_effects.txt) and [`famine_adapter_effects.txt`](famine_adapter_effects.txt) | [`famine_system`](../../docs/systems/famine_system.md) |
| `asteroid_mineral_control` | [`028_asteroid_incoming_mineral_effects.txt`](028_asteroid_incoming_mineral_effects.txt) and [`028_asteroid_incoming_mineral_triggers.txt`](../scripted_triggers/028_asteroid_incoming_mineral_triggers.txt) | [current-controller mineral API](028_asteroid_incoming_mineral_effects.md), unique processed fragment counts, uncapped armour, caller scopes, normal outputs, annex/release cleanup, legacy identities, icons and native acceptance limits |
| `migration_runtime` | [`migration_core_effects.txt`](migration_core_effects.txt), [`migration_adapter_effects.txt`](migration_adapter_effects.txt), and [`migration_reception_preparation_effects.txt`](migration_reception_preparation_effects.txt) | [`migration_system`](../../docs/systems/migration_system.md) and the [exact paid preparation contract](migration_reception_preparation_effects.md), including scope, saved state target, inputs/results, real service improvement, centralized payment/refund, rollback, and no movement before acceptance |
| `humanitarian_validation` | [`humanitarian_validation_triggers.txt`](../scripted_triggers/humanitarian_validation_triggers.txt) | [`famine_system`](../../docs/systems/famine_system.md) and [`migration_system`](../../docs/systems/migration_system.md) |
| `great_depression_start_or_deepen` | [`035_great_depression_effects.txt`](035_great_depression_effects.txt) and [`035_great_depression_triggers.txt`](../scripted_triggers/035_great_depression_triggers.txt) | [`gateway contract`](035_great_depression_effects.md) and [`great_depression`](../../docs/events/035_great_depression.md), exact receiver, frozen caller/source pointers, fail-closed receipts, evolution inheritance, synchronous outputs, examples, and cleanup |
| `great_depression_register_inherited_region` | [`035_great_depression_region_effects.txt`](035_great_depression_region_effects.txt) | [`regional companion`](035_great_depression_region_effects.md), exact state/episode proof, frozen source metadata, bounded aligned receipts, disposition/index outputs, caps, idempotence, and cleanup |

## maintenance_notes

Add a helper here only when its contract is neutral and its callers cross subsystem or event-family boundaries. Give it a descriptive name based on its behavior, not the event that first needed it.

Keep one-event orchestration, event-specific selectors, lifecycle state, and private adapters in the owning source file. A cross-event public gateway may remain in this registry while delegating its owner-specific runtime to the owning source file.

When a shared helper changes, update its contract here and audit every call site. When an owner API changes, update the owner documentation and change only the corresponding index row here.

The Event 012 owner API [`012_africa_gods_equipment_effects`](012_africa_gods_equipment_effects.md) documents its COUNTRY-scoped armoured and typed truck/artillery quotes, protected native capacity, integer amounts, native transfers, and payment-type binding in `012_africa_gods_mobile_contract_effects.txt`, including caller-set inputs, temporary outputs, cleanup, defaults, side effects, and boolean-helper usage.

The private Event 012 [`Gods report receipts`](012_africa_gods_report_effects.md) document response capture, frozen equipment subtype, cleanup, and whole-equipment classification, including explicit caller-set inputs, outputs, lifecycle owners, side effects, and boolean-helper usage.

The Event 012 [`Gods survivor settlement`](012_africa_gods_settlement_effects.md) contract documents exact history lineage, one-time grading and native reciprocal transfers, independent frozen-host receipt proof, cleanup, defaults, and boolean-helper usage.

The Event 012 [`Gods victor authority`](012_africa_gods_victor_effects.md) contract documents native capitulation-winner capture, permanent exemption, frozen episode/host renewal consent, withdrawal/decline, separate paid defiance, report receipts, cleanup, and boolean-helper usage.

The Event 012 [`Gods demand repetition`](012_africa_gods_repetition_effects.md) contract documents caller-set type/family inputs, recent actual-contract receipts, identity replay protection, percentage scaling, cleanup, and boolean-helper usage.

The private Event 012 [unique tribute contract ledger](012_africa_gods_contract_effects.md) documents caller-set closure input, immutable identity, replay consumption, issuance and outcome counts, neutral retirement, streaks, accepted reconciliation, lifecycle owners, and boolean-helper usage.

The Event014 owner API [Larder logistics](../../docs/events/014_cannibalism/larder_logistics.md) documents country effective-capacity calculation, post-transaction clamp/publication, caller-owned exact distance quotes from frozen regular capital targets, one-shot dispatch/receipt commit, opening inheritance, generation guards, cleanup and the fifty-flag administrative development mapping.

The private Event 012 [Gods original-owner recovery](012_africa_gods_recovery_effects.md) and [live epoch bindings](012_africa_gods_epoch_binding_effects.md) document exact host/consent proof, initial grant and revocation, current-due wake handling and bounded repair, native loss cleanup, historical report preservation, caller inputs, defaults, side effects, and boolean-helper usage.

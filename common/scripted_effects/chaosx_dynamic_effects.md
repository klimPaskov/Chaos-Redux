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
- [Shared clone equipment and infantry helpers](#shared-clone-equipment-and-infantry-helpers)
- [Mengele Directorate Event 016 prototype bridge](#mengele-directorate-event-016-prototype-bridge)
- [Event 19 integration obligation for new custom units](#event-19-integration-obligation-for-new-custom-units)
- [Event 006 AI reserve and ledger trigger contract](#event-006-ai-reserve-and-ledger-trigger-contract)

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

## Event 006 Iberian compact ledger helpers

Purpose: apply one bounded ledger transaction for the registered NAV or GLC carrier while refreshing its lifecycle idea.

Scope: country.

Inputs: NAV callers supply temporary `independence_wave_nav_fueros_delta` and `independence_wave_nav_industry_delta`; GLC callers supply `independence_wave_glc_council_delta` and `independence_wave_glc_port_delta`.

Helpers: `independence_wave_change_nav_compact_values` and `independence_wave_change_glc_compact_values`.

Outputs: the two carrier-specific values are added and clamped to the centralized Iberian pressure range, then the contested/compact idea lifecycle is refreshed.

Defaults: callers must supply both temporary deltas. The helpers do not perform a world scan or create a country.

Side effects: only the active matching registered carrier is changed. A failed project can use the same helpers with negative deltas, and generation cleanup clears both variables and all carrier-owned ideas.

Example:

```txt
set_temp_variable = { independence_wave_nav_fueros_delta = constant:independence_wave_iberian_pressure.minor_gain }
set_temp_variable = { independence_wave_nav_industry_delta = constant:independence_wave_iberian_pressure.standard_gain }
independence_wave_change_nav_compact_values = yes
```

## Event 016 reusable custom technology grants

Purpose: award only the eighteen Event 016 custom technologies to another event's country without creating Kruger ownership, Directorate state, project history, facilities, free formations, equipment stockpiles, vanilla technologies, or Event 016 log history.

Scope: country.

Inputs:

- `chaosx_grant_custom_operational_technology` reads temporary `chaosx_custom_technology_family` from `constant:chaosx_custom_technology_family.*`.
- `chaosx_grant_custom_technology_upgrade` reads temporary `chaosx_custom_technology_upgrade` from `constant:chaosx_custom_technology_upgrade.*`.
- `chaosx_grant_random_custom_operational_technology` takes no selector and considers only unresearched base operational families.

Outputs:

- `chaosx_custom_technology_grant_applied` is `1` for a valid operational selector.
- `chaosx_custom_technology_upgrade_applied` is `1` for a valid upgrade selector.
- `chaosx_custom_technology_random_grant_applied` is `1` when the random pool selected an unresearched family.

Defaults: invalid selectors and an exhausted random pool are safe no-ops. No vanilla technology or substitute family is inferred.

Side effects: a valid grant records an external knowledge ledger flag, restores the selected custom technology after Event 016 runtime rebuilds, recreates the existing locked and capped template, reopens matching custom-equipment production, and registers the existing Event 019 provider row. Clone grants select Mengele refinement for a Mengele Directorate country and Kruger refinement otherwise. Upgrade grants award their operational dependency first. Portal weaponization also unlocks the existing portal facility raid; Kruger changes its AI weight but is not an access requirement.

Example:

```txt
set_temp_variable = { chaosx_custom_technology_family = constant:chaosx_custom_technology_family.exotic }
chaosx_grant_custom_operational_technology = yes
```

## Shared clone equipment and infantry helpers

Purpose: grant provider-neutral clone manufacture and recruitment, select one provider refinement, create the reusable editable 20-width template, and derive reserve manpower from the physical clone-equipment stockpile.

Scope: country.

Inputs: none. `clone_refresh_reserve_manpower` reads `num_equipment@clone_equipment` directly.

Helpers: `clone_ensure_infantry_template`, `clone_grant_infantry_access`, `clone_select_kruger_refinement`, `clone_select_kruger_weaponization`, `clone_select_mengele_refinement`, and `clone_refresh_reserve_manpower`.

Outputs: access helpers grant the hidden shared technology and template; provider selectors grant their matching refinement while removing the incompatible refinement; the refresh helper stores the rounded stockpile and weekly output in `clone_equipment_stockpile` and `clone_reserve_weekly_manpower`.

Defaults: no provider refinement is inferred by `clone_grant_infantry_access`. A country with no physical clone equipment has no reserve modifier.

Side effects: `clone_refresh_reserve_manpower` adds, updates, or removes `clone_reserve_manpower`. Provider selectors deliberately enforce ordinary Kruger/Mengele refinement exclusivity.

Example:

```txt
clone_grant_infantry_access = yes
add_equipment_to_stockpile = { type = clone_equipment_1 amount = 10 }
clone_refresh_reserve_manpower = yes
```

## Mengele Directorate Event 016 prototype bridge

Purpose: expose the nine non-cloning Event 016 native prototype projects to the Mengele Directorate without making it an Event 016 host or creating Event 016 project-ledger state.

Scope: country.

Inputs: `brilliant_scientist_record_mengele_project_prototype` reads temporary `brilliant_scientist_project_family` using the existing `constant:brilliant_scientist_project_family.*` enum.

Outputs: a valid computation, materials, or biomedical completion sets a provider-owned `directorate_special_project_*_completed` flag and its provider dynamic modifier; teleportation, robotics, paleogenetics, xenobiological synthesis, alien arms, and temporal completion grants the mapped neutral custom operational technology through `chaosx_grant_custom_operational_technology` and sets the matching completion flag.

Defaults: an invalid provider, cloning family, Singularity family, or unknown family is a no-op. Cloning remains owned by `sp_mengele_cloning` and its Mengele refinement effect. Strategic Singularity remains Kruger State-only.

Side effects: completed-family availability flags are cleared, the temporary family selector is cleared, and dynamic modifiers are refreshed. The bridge never mutates `brilliant_scientist_project_stage_entries`, `brilliant_scientist_project_capacity`, Event 016 facility targets, event history, evolution state, containment state, or Singularity state. Public operational grants may rebuild the neutral custom-technology runtime consumers required for capped templates and provider rows, but do not create Event 016 project history.

Example:

```txt
set_temp_variable = { brilliant_scientist_project_family = constant:brilliant_scientist_project_family.robotics }
brilliant_scientist_record_new_project_prototype = yes
```

`brilliant_scientist_record_new_project_prototype` dispatches to the bridge only for a Mengele Directorate country; Kruger and other Event 016 host callers keep the existing ledger path.

## Event 19 integration obligation for new custom units

Any event, doctrine, technology, country package, or shared mechanic that adds a combat-capable custom land unit must update its Event 19 integration in the same change. The owning feature is not complete until the new unit can be discovered through the shared Chaos unit-family registry and can pass Event 19 generation, management, accounting, derivative, cleanup, AI, and player-facing documentation checks.

The integration is owner-side. Do not add a fixed family list to Event 19, do not create another Event 19 registry file, and do not append a provider directly inside `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`. A future family contributes one idempotent registration effect from its existing owner integration file and calls that registration from the owner's bounded startup or runtime rebuild path. Registration uses `chaos_unit_family_register_current_provider` from `common/scripted_effects/chaos_unit_family_registry_effects.txt`. It must not introduce a recurring whole-world scan.

When a new unit belongs to an already registered family, extend that family's owner adapter, template builder, token coverage, obligation manifest, and cleanup contract instead of allocating a second provider merely to enumerate another battalion. When the unit has a distinct availability, lot, sustainment, containment, derivative, AI, visual, cleanup, or parent-isolation identity, register one new family and provider ID.

Every new Event 19-capable family must provide one registration surface and all eleven provider callbacks:

- `chaos_unit_family_provider_N_event19_evaluate_eligibility`
- `chaos_unit_family_provider_N_event19_build_template`
- `chaos_unit_family_provider_N_event19_spawn_unit`
- `chaos_unit_family_provider_N_event19_reconcile_sustainment`
- `chaos_unit_family_provider_N_event19_get_management_cost_display`
- `chaos_unit_family_provider_N_event19_evaluate_management`
- `chaos_unit_family_provider_N_event19_pay_management_action`
- `chaos_unit_family_provider_N_event19_refund_management_action`
- `chaos_unit_family_provider_N_event19_setup_derivative`
- `chaos_unit_family_provider_N_event19_remove_public_additions`
- `chaos_unit_family_provider_N_event19_cleanup_derivative`

The callbacks must preserve the owner's real technology, source-event, train-versus-spawn, parent-isolation, and equipment rules. They must not substitute ordinary infantry, borrow another family's presentation, activate parent stages or evolutions, or propagate parent counts, wars, deaths, super-events, or world-end progression. A future provider uses the neutral army visual profile unless it owns a separately supported profile. Support-only definitions are not registered as standalone families because HOI4 cannot create a division without a combat regiment. They remain parent-owned obligations or join an inseparable provider formation that contains a valid combat component.

The owner must publish exact manpower and equipment requirements through the Event 19 obligation manifest. A provider with no separate standing stockpile debit must explicitly commit a zero-row manifest and select the ledger-backed zero-debit cost-display profile. `event19_get_management_cost_display` is presentation-only. Payment occurs only through `event19_pay_management_action`, and a failed build or spawn must restore the same resources through `event19_refund_management_action`.

The same change must add or update family names, descriptions, selection text, management costs, blocked tooltips, AI eligibility, and any derivative identity text exposed to the player. It must also update `docs/systems/chaos_unit_family_registry.md` and `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`. If the event catalog describes the affected family coverage, update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and regenerate its CSV exports through the repository exporter.

Before the owning feature is considered complete, verify that the registry arrays remain aligned, every registered provider has exactly one registration and eleven callbacks, every installed combat token is covered, manifest row counts and liabilities match the real formation, trainable and spawn-only policies are enforced, management payment and refund are symmetric, derivative setup and defeat cleanup prove their owner surfaces, and Event 19 does not inherit the parent feature's progression. Run the applicable HOI4 MCP event and weighted-logic inspections for the changed provider paths. An unresolved provider, missing callback, stale cost display, generic equipment substitute, undocumented support-only exclusion, or unvalidated registry row is a blocker rather than an allowed fallback.

The complete field, callback, accounting, isolation, and lifecycle contract is maintained in `docs/systems/chaos_unit_family_registry.md`. The current unit census and provider-to-token mapping are maintained in `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`.

## Event 006 AI reserve and ledger trigger contract

Purpose: provide reusable, package-scoped predicates for Event 006 decision AI. The contract keeps a released country from spending project resources before its foundation is settled, prefers the lower regional ledger, and suppresses a project when its post-spend reserve floor would not be preserved.

Scope: country.

Inputs: the carrier must already expose its package flags and initialized ledger variables. Reserve thresholds are read from `constant:independence_wave_karelia_crimea_ai_floor`.

Helpers: `independence_wave_kc_ai_foundation_ready`, `independence_wave_kar_ai_lower_ledger`, `independence_wave_cri_ai_lower_ledger`, `independence_wave_kar_ai_command_manpower_floor`, `independence_wave_kar_ai_land_material_floor`, `independence_wave_cri_ai_command_manpower_floor`, `independence_wave_cri_ai_land_material_floor`, `independence_wave_cri_ai_maritime_floor`, `independence_wave_kc_ai_diplomatic_floor`, `independence_wave_kar_ai_major_security_floor`, and `independence_wave_cri_ai_major_security_floor`.

Outputs: scripted triggers return a boolean result for `ai_will_do` modifiers. They do not alter ledgers, resources, flags, or decisions.

Defaults: missing package flags or ledger variables fail closed. Equal ledgers receive no lower-ledger preference. Player availability and costs remain controlled by the existing `can_pay_*` triggers.

Side effects: none.

Example:

```txt
ai_will_do = {
	base = constant:independence_wave_karelia_crimea_ai.standard
	modifier = { factor = 0 NOT = { independence_wave_kc_ai_foundation_ready = yes } }
	modifier = { factor = 2 independence_wave_kar_ai_lower_ledger = yes }
	modifier = { factor = 0 NOT = { independence_wave_kar_ai_land_material_floor = yes } }
}
```

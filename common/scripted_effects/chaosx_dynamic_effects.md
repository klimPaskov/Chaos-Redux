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
- [Shared alien-infantry contact and landing API](#shared-alien-infantry-contact-and-landing-api)
- [Mengele Directorate Event 016 prototype bridge](#mengele-directorate-event-016-prototype-bridge)
- [Event 19 integration obligation for new custom units](#event-19-integration-obligation-for-new-custom-units)
- [Event 19 derivative opening local-asset audit](#event-19-derivative-opening-local-asset-audit)
- [Event 006 AI reserve and ledger trigger contract](#event-006-ai-reserve-and-ledger-trigger-contract)
- [Famine and migration food-reserve ledger](#famine-and-migration-food-reserve-ledger)
- [Famine and migration runtime registry](#famine-and-migration-runtime-registry)
- [Famine and migration pressure adapters](#famine-and-migration-pressure-adapters)
- [Exact civilian transfer contract](#exact-civilian-transfer-contract)
- [Border, reception, return, and cohort contracts](#border-reception-return-and-cohort-contracts)
- [Famine and migration cleanup](#famine-and-migration-cleanup)

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
set_temp_variable = { chaosx_custom_technology_family = constant:chaosx_custom_technology_family.alien_infantry }
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

## Shared alien-infantry contact and landing API

Purpose: grant or revoke provider-neutral contact, maintain the single locked alien template, and create one paid D’Rhondan landing cohort through a state-targeted reservation or another explicitly authorized caller.

Definitions: public effects are implemented in `common/scripted_effects/016_alien_infantry_api_effects.txt`; public readers are implemented in `common/scripted_triggers/016_alien_infantry_api_triggers.txt`; tuning and stable receipt IDs are defined in `common/script_constants/016_alien_infantry_api_constants.txt`.

Scope: country for `alien_infantry_grant_contact`, `alien_infantry_revoke_contact`, `alien_infantry_can_call_landing`, `alien_infantry_spawn_landing_cohort`, and `alien_infantry_reconcile_country`. `alien_infantry_landing_state_is_valid` is a state-scope reader with the calling country as `ROOT`.

Inputs: grant and revoke read temporary `alien_infantry_contact_source_id` from `constant:alien_infantry_contact_source.*`. A landing caller stores its selected state ID in country variable `dhrondan_landing_state_id`. Direct spawn callers must have the exact laser stockpile and a valid selected state; the ordinary decision path debits the fixed reserve before its seven-day mission begins.

Outputs: contact reconciliation grants the hidden operational alien-infantry technology, creates and relocks the ten-battalion `D’Rhondan Landing Cohort`, and exposes laser production while at least one receipt remains. A successful spawn creates exactly one fully equipped cohort, marks the state, and records the persistent landing counters. `alien_infantry_landing_spawn_succeeded` is a temporary one-or-zero result for callers that need transaction evidence.

Defaults: unknown receipt IDs are safe no-ops. Revoking one receipt never removes another provider’s entitlement. A missing, invalid, uncontrolled, or impassable state prevents direct materialization. The ordinary pending path refunds exactly one 2,000-weapon reservation when contact or state control is lost.

Side effects: a normal successful landing adds one arrival, one Alien Presence, five Pact Strain, one history receipt, and the bounded landing cooldown. The sovereignty bootstrap mode is restricted to DHR’s positive sovereignty receipt and still consumes 2,000 weapons per cohort, but it does not impersonate pact-host arrivals or apply the ordinary cooldown. Event 019 provider 508 is a one-request provider: automatic generation and scenario actors materialize exactly one cohort even when the enclosing scenario targets several states. The provider supplies its allocated engine deletion ID and uses private `alien_infantry_commit_event19_landing` and `alien_infantry_rollback_event19_landing` hooks. The cohort and exact laser debit materialize first, while state flags, pact telemetry, cooldown, and callbacks remain deferred until the enclosing Event 019 ledger transaction commits. Same-tag scenario receipts are stored persistently on the actor country so asynchronous rollback retries retain the deletion ID and proven debit state; rollback deletes the exact cohort and refunds the one proven 2,000-weapon debit only after Event 019 proves that the package objects are absent and verifies its restored snapshot.

Example:

```txt
set_temp_variable = { alien_infantry_contact_source_id = constant:alien_infantry_contact_source.future }
alien_infantry_grant_contact = yes
set_variable = { dhrondan_landing_state_id = FROM.id }
alien_infantry_spawn_landing_cohort = yes
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

Every new Event 19-capable family must provide one registration surface and all thirteen provider callbacks:

- `chaos_unit_family_provider_N_event19_evaluate_eligibility`
- `chaos_unit_family_provider_N_event19_build_template`
- `chaos_unit_family_provider_N_event19_spawn_unit`
- `chaos_unit_family_provider_N_event19_reconcile_sustainment`
- `chaos_unit_family_provider_N_event19_get_equipment_token`
- `chaos_unit_family_provider_N_event19_publish_custom_equipment_tokens`
- `chaos_unit_family_provider_N_event19_get_presentation`
- `chaos_unit_family_provider_N_event19_evaluate_management`
- `chaos_unit_family_provider_N_event19_pay_management_action`
- `chaos_unit_family_provider_N_event19_refund_management_action`
- `chaos_unit_family_provider_N_event19_setup_derivative`
- `chaos_unit_family_provider_N_event19_remove_public_additions`
- `chaos_unit_family_provider_N_event19_cleanup_derivative`

The callbacks must preserve the owner's real technology, source-event, train-versus-spawn, parent-isolation, and equipment rules. They must not substitute ordinary infantry, borrow another family's presentation, activate parent stages or evolutions, or propagate parent counts, wars, deaths, super-events, or world-end progression. A future provider uses the neutral army visual profile unless it owns a separately supported profile. Support-only definitions are not registered as standalone families because HOI4 cannot create a division without a combat regiment. They remain parent-owned obligations or join an inseparable provider formation that contains a valid combat component.

The owner publishes exact manpower and equipment requirements through `event19_reconcile_sustainment`. Every non-generic equipment profile is a stable numeric constant in the owner's own constants file; the pair of family ID and profile is the save-compatible resolver identity. `event19_get_equipment_token` maps the current profile to the concrete local equipment token and sets `infantry_spawn_family_provider_equipment_is_specialist` when the row uses specialist salvage. Generic infantry, support, motorized, and coal-golem profiles may delegate to `infantry_spawn_provider_get_standard_equipment_token`. Unknown positive profiles fail closed.

`event19_publish_custom_equipment_tokens` calls `infantry_spawn_register_current_family_custom_equipment_token` once for every non-generic equipment type the provider can debit or refund. Event 19 dispatches every registered provider publisher when it snapshots pre-payment and post-payment stockpiles, so a future equipment type enters affordability, payment, rollback, derivative materialization, and exploit proof without an Event 19 equipment-list edit. Providers with no custom equipment explicitly return no token. Provider-owned debit and refund effects remain the only authority for direct request costs; Event 19 snapshots their published tokens and proves exact restoration instead of applying a second debit or refund.

`event19_get_presentation` returns positive localisation-key tokens in `infantry_spawn_family_provider_name_loc_token`, `infantry_spawn_family_provider_request_cost_loc_token`, and `infantry_spawn_family_provider_sustainment_cost_loc_token`. The Muster decisions, first-reception evidence, reports, and derivative records freeze or cache those tokens and render them with `GetTokenLocalizedKey`. A missing or malformed presentation token rejects the provider row; Event 19 does not substitute another family's name or cost text.

Payment occurs only through `event19_pay_management_action`, and a failed build or spawn restores the same resources through `event19_refund_management_action`. Event 19 owns only its shared request overhead. Pre-payment snapshots prove exact refund symmetry; transaction snapshots prove that structural rollback did not mutate provider stockpiles. Selected-lot exact obligations use country-persistent aligned token and amount arrays because decision availability is evaluated after the cache refresh effect returns.

The same change must add or update family names, descriptions, selection text, management costs, blocked tooltips, AI eligibility, and any derivative identity text exposed to the player. It must also update `docs/systems/cbrn_warfare/chaos_unit_family_registry.md` and `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`. If the event catalog describes the affected family coverage, update `docs/spreadsheets/chaos_redux_events_catalog.xlsx` and regenerate its CSV exports through the repository exporter.

Before the owning feature is considered complete, verify that the registry arrays remain aligned, every registered provider has exactly one registration and thirteen callbacks, every installed combat token has an explicit provider disposition, every non-generic equipment token resolves to a concrete local definition, manifest row counts and liabilities match the real formation, trainable and spawn-only policies are enforced, management payment and refund are symmetric, derivative setup and defeat cleanup prove their owner surfaces, and Event 19 does not inherit the parent feature's progression. Run the applicable HOI4 MCP event and weighted-logic inspections for the changed provider paths. An unresolved provider, missing callback, stale presentation token, generic equipment substitute, undocumented support-only exclusion, or unvalidated registry row is a blocker rather than an allowed fallback.

The complete field, callback, accounting, isolation, and lifecycle contract is maintained in `docs/systems/cbrn_warfare/chaos_unit_family_registry.md`. The current unit census and provider-to-token mapping are maintained in `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`.

## Event 19 derivative opening local-asset audit

Purpose: record the local economy and logistics a dynamic Event 19 derivative actually received, classify its opening capacity, and retire the temporary shortfall burden after the opening inventory focus proves that the seized district has been catalogued.

Owner source: `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`.

Scope: country after the derivative owns its opening states and has initialized or adopted its private Event 19 ledger.

Effect: `infantry_spawn_derivative_reconcile_starting_local_assets`.

Inputs: the current country scope; owned-state totals; `num_of_factories`, `num_of_civilian_factories`, `num_of_military_factories`, `num_of_naval_factories`, `amount_research_slots`, `fuel_ratio`, standard equipment stockpiles, `infantry_spawn_equipment_debt`, `infantry_spawn_manpower_liability`, and `infantry_spawn_active_division_count`; state-level population, infrastructure, railway, port, supply-node, and local-resource values; and owner-published custom-equipment token and amount arrays returned through the registered Event 19 provider publishers.

Outputs: persistent `infantry_spawn_derivative_opening_owned_state_count`, `infantry_spawn_derivative_opening_factory_count`, `infantry_spawn_derivative_opening_civilian_factory_count`, `infantry_spawn_derivative_opening_military_factory_count`, `infantry_spawn_derivative_opening_naval_factory_count`, `infantry_spawn_derivative_opening_population_k`, `infantry_spawn_derivative_opening_infrastructure_score`, `infantry_spawn_derivative_opening_railway_state_count`, `infantry_spawn_derivative_opening_port_level_count`, `infantry_spawn_derivative_opening_supply_node_count`, `infantry_spawn_derivative_opening_local_resource_total`, `infantry_spawn_derivative_opening_research_slot_count`, `infantry_spawn_derivative_opening_fuel_ratio`, `infantry_spawn_derivative_opening_infantry_equipment`, `infantry_spawn_derivative_opening_support_equipment`, `infantry_spawn_derivative_opening_motorized_equipment`, `infantry_spawn_derivative_opening_train_equipment`, `infantry_spawn_derivative_opening_convoy_equipment`, `infantry_spawn_derivative_opening_equipment_obligation`, `infantry_spawn_derivative_opening_manpower_obligation`, `infantry_spawn_derivative_opening_active_formation_count`, `infantry_spawn_derivative_opening_custom_equipment_total`, and `infantry_spawn_derivative_opening_local_capacity_score`.

Outputs also include exactly one of `infantry_spawn_derivative_local_assets_fragile`, `infantry_spawn_derivative_local_assets_strained`, or `infantry_spawn_derivative_local_assets_viable` country flags. A fragile result adds the temporary `infantry_spawn_derivative_local_asset_shortfall` idea.

Defaults: thresholds come from `constant:infantry_spawn_derivative_opening_asset` with minimum railway level `1`, factory and military-factory presence floors `1`, infrastructure-per-state floor `1`, population floor `100` thousand, local-resource floor `1`, infantry-equipment floor `100`, support-equipment floor `10`, motorized-equipment floor `10`, train-equipment floor `1`, convoy-equipment floor `5`, custom-equipment floor `1`, fragile score ceiling `4`, and strained score ceiling `8`. Missing optional local assets contribute zero evidence, and a mismatched custom-equipment token and amount array fails closed through the ledger-invariant path.

Side effects: the effect clears and rewrites the opening snapshot arrays, dispatches registered provider custom-equipment publishers, clears the three capacity flags and the prior shortfall-resolved flag, then adds the fragile idea or sets the strained/viable flag. It never creates factories, infrastructure, supply assets, or a generic economy grant.

Effect: `infantry_spawn_derivative_resolve_opening_local_asset_shortfall`.

Scope: country on the opening inventory focus `infantry_spawn_derivative_inventory_the_seized_districts` after the local asset audit.

Inputs: the current country scope and the existing temporary shortfall idea.

Outputs: removes `infantry_spawn_derivative_local_asset_shortfall` and sets `infantry_spawn_derivative_local_asset_shortfall_resolved`.

Defaults: the effect is idempotent when the idea is absent and does not require a fragile classification before setting the proof flag.

Side effects: opening measurements, capacity flags, private ledgers, factories, infrastructure, stockpiles, and provider-owned arrays remain unchanged. The effect only retires the temporary burden and records the resolved proof.

Example:

```txt
# Called during dynamic derivative setup after the opening states and private ledger exist.
infantry_spawn_derivative_reconcile_starting_local_assets = yes

# Called by the opening inventory focus after its district-catalogue work.
infantry_spawn_derivative_resolve_opening_local_asset_shortfall = yes
```

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

## Famine and migration runtime registry

The public registry effects live in `common/scripted_effects/chaosx_famine_migration_effects.txt` and are lazy-initialized by `famine_migration_initialize_runtime`.

`famine_migration_register_active_food_state` and `famine_migration_unregister_active_food_state` use the global `famine_migration_active_food_states` array and its count variable.

`famine_migration_register_active_displacement_state` and `famine_migration_unregister_active_displacement_state` use the global `famine_migration_active_displacement_states` array and its count variable.

`famine_migration_register_active_displacement_country` and `famine_migration_unregister_active_displacement_country` use the global `famine_migration_active_displacement_countries` array and its count variable.

`famine_migration_retire_inactive_displacement_country` is the non-destructive country-scope retirement path. It requires the category to be dormant, no selected cohort, no positive reception load, and no owned active food or displacement state. It removes live scheduler and selection state while preserving historical integration, resettlement, and return totals for mapmode, achievement, and documentation consumers.

`famine_migration_refresh_decision_phase_from_state` is the state-scope category projection. It reveals the emerging phase only when the state reaches the centralized sustained-exposure, repeated-incident, large-flight, trapped-population, or reception-load threshold, registers the owner country, and clears dormancy. It has no output variable and never scans unregistered states or countries.

Scope is state for state registries and country for the country registry.

Inputs are the current valid state or country scope; registry effects do not accept an implicit world scan.

Outputs are the bounded global arrays, count variables, and `famine_migration_registry_result` temporary value (`1` for an accepted entry and `0` for an invalid scope).

Defaults are empty arrays and zero counts on the first explicit call in a save.

Side effects are state flags `famine_migration_food_security_active` and `famine_migration_displacement_active`, country flag `famine_migration_displacement_active`, and removal of stale state or country data during unregister calls.

Example:

```txt
set_temp_variable = { famine_migration_pressure_request_proven = 1 }
set_temp_variable = { famine_migration_pressure_request_amount = 12000 }
famine_migration_request_famine_pressure = yes
```

The CXT fixture in `common/scripted_effects/famine_migration_cxt_test_effects.txt` registers the token `chaosx_cxt_extension_famine_migration` through the bounded general-system extension contract. When the fixture is initialized, it gives the test country reception capacity, submits capital-state surface inputs at the supply-strain threshold with relief at zero, and records proof without creating a transfer, route, severe famine, or mortality transaction. Startup and `on_daily_CXT` registration are additive and idempotent, so this fixture is test-only evidence rather than ordinary gameplay setup.

## Famine and migration pressure adapters

`famine_migration_apply_pressure_request` is the shared state-scope adapter for one positive pressure request.

Inputs are `famine_migration_pressure_request_proven`, `famine_migration_pressure_request_amount`, `famine_migration_pressure_request_source`, and `famine_migration_pressure_request_actor_proven` temporary variables.

`famine_migration_pressure_request_apply_food` and `famine_migration_pressure_request_apply_flight` optionally route the amount to food-security pressure, flight pressure, or both.

Missing apply flags default to food only, while missing proof, source, actor, or amount fails closed.

Outputs are state variables `famine_migration_food_pressure` and `famine_migration_flight_pressure`, source variable `famine_migration_last_pressure_source`, and temporary result `famine_migration_pressure_request_result`.

Side effects are idempotent registration in the active food-security and displacement registries and clearing of one-shot request inputs.

The named wrappers `famine_migration_request_occupation_pressure`, `famine_migration_request_camp_pressure`, `famine_migration_request_gulag_pressure`, `famine_migration_request_forced_labor_pressure`, `famine_migration_request_deportation_pressure`, `famine_migration_request_bombing_pressure`, `famine_migration_request_nuclear_pressure`, `famine_migration_request_fallout_pressure`, `famine_migration_request_outbreak_pressure`, `famine_migration_request_disaster_pressure`, `famine_migration_request_war_pressure`, `famine_migration_request_peace_pressure`, and `famine_migration_request_event_pressure` set the source enum and delegate to the shared adapter.

The additional owner seams `famine_migration_request_air_cleanliness_pressure`, `famine_migration_request_chemical_aftermath_pressure`, `famine_migration_request_biological_warfare_pressure`, `famine_migration_request_cluster_pressure`, and `famine_migration_request_scenario_pressure` do the same for Air Cleanliness contamination, chemical aftermath, biological warfare/outbreak callers, cluster-level causal records, and scenario-level causal records. They are input contracts only; Air Cleanliness and chemical/biological owners retain their direct effects, and catalog-only concepts 118, 120, and 131 have no fabricated event source.

`famine_migration_request_blockade_pressure` additionally requires `famine_migration_blockade_proof = yes` before delegating.

`famine_migration_request_famine_pressure` and its explicit alias `famine_migration_request_food_security_pressure` select the resource-shortage source and food route.

`famine_migration_request_flight_pressure` and its explicit alias `famine_migration_request_displacement_pressure` select the event source and flight route.

Owner systems remain responsible for setting the source-specific proof and amount at their existing call sites.

## Exact civilian transfer contract

`famine_migration_transfer_civilians_exact` is a state-scope state-to-state civilian movement contract.

Inputs are `famine_migration_transfer_request_proven`, positive `famine_migration_transfer_people`, `famine_migration_transfer_minimum_origin_remaining`, `famine_migration_transfer_route_deaths_requested`, `famine_migration_transfer_log_deaths`, and optional `famine_migration_transfer_route_death_reason`.

The caller must save the destination state as the regular event target `famine_migration_route_destination` and supply route border, transport, safety, actor, destination food, and destination reception proof variables before calling.

Outputs are `famine_migration_transfer_result`, `famine_migration_transfer_actual_origin_debit`, `famine_migration_transfer_route_deaths`, `famine_migration_transfer_survivor_credit`, and `famine_migration_transfer_conservation_ledger` temporary variables.

Optional `famine_migration_transfer_target_country` and `famine_migration_transfer_has_target_country` are passed to the Deaths registrar for actor attribution when route deaths are logged.

The result is `constant:famine_migration_route_result.valid` only when the actual origin debit equals route deaths plus destination credit.

The effect debits the origin once through `apply_state_population_loss_without_recruitable_manpower_gain`, measures exact people by multiplying `state_population_k` deltas by `constant:chaos_meter_deaths.people_per_k`, credits only survivors with positive state-scope `add_manpower`, and reconciles any owner or controller manpower change observed around that positive add.

Route deaths are a slice of the already debited population and never cause a second state debit.

When logging is enabled, route deaths call `chaos_meter_register_deaths` with `chaos_deaths_apply_state_pop = 0` and `chaos_deaths_record_state_ledger = 1`, so the Deaths ledger records the loss without removing population again.

Global conservation counters are `famine_migration_conservation_debit`, `famine_migration_conservation_credit`, `famine_migration_conservation_route_deaths`, and `famine_migration_conservation_residual`.

Invalid route requests clear one-shot inputs and leave population unchanged.

Example:

```txt
# The destination pointer is already resolved by the caller.
var:famine_migration_destination_state = {
	save_event_target_as = famine_migration_route_destination
	set_variable = { famine_migration_destination_food_safe_proven = 1 }
	set_variable = { famine_migration_destination_reception_proven = 1 }
}
# Return to the origin-state scope before submitting the movement request.
set_temp_variable = { famine_migration_transfer_request_proven = 1 }
set_temp_variable = { famine_migration_transfer_people = 20000 }
set_temp_variable = { famine_migration_route_border_proven = 1 }
set_temp_variable = { famine_migration_route_transport_proven = 1 }
set_temp_variable = { famine_migration_route_safety_proven = 1 }
set_temp_variable = { famine_migration_route_actor_proven = 1 }
famine_migration_transfer_civilians_exact = yes
```

`famine_migration_resolve_route` is a read-only state-scope adapter that evaluates the same route, destination, and proof inputs as the transfer contract and returns `famine_migration_route_resolution_result` (`valid` or `invalid`) without changing population.

`famine_migration_apply_destination_credit` is the destination-state helper called only by the exact transfer contract.

It requires destination food and reception proof plus a positive temporary destination request, and returns the actual positive state-population credit in `famine_migration_transfer_destination_actual_credit`.

`famine_migration_restore_origin_population_residual` is the origin-state rollback helper used only when the destination state API credits fewer survivors than the actual origin debit. Input is positive temporary `famine_migration_origin_restore_request`; output is actual restored state population in `famine_migration_origin_restore_actual`. It reconciles incidental owner/controller recruitable-manpower gains, clears the request, and lets the parent transfer recompute the conservation equation before accepting the transaction.

## Border, reception, return, and cohort contracts

The persistent cohort ledger is owned by `famine_migration_record_displaced_cohort`, `famine_migration_bind_cohort_destination`, `famine_migration_bind_cohort_destination_forced`, `famine_migration_resolve_cohort_origin`, `famine_migration_update_cohort_host_after_transfer`, `famine_migration_cleanup_cohort_record`, and `famine_migration_cleanup_cohort_records_for_state`.

`famine_migration_record_displaced_cohort` is a state-scope effect. The caller supplies a positive amount, owner proof, and a non-unknown source; the effect records `global.famine_migration_cohort_ids`, original state, current host, owner, amount, source, and status in aligned arrays. The origin is only an unbound placeholder in the destination slot, and no destination is valid until a destination-state consumer calls a bind effect inside that actual state scope. The effect persists `famine_migration_current_cohort_id` on the host state and, when unambiguous, `famine_migration_current_country_cohort_id` for the owner country.

`famine_migration_bind_cohort_destination` must run in the actual destination state and requires food-safe and reception-safe proof. `famine_migration_bind_cohort_destination_forced` must also run in the actual destination state, but requires explicit actor/policy proof and records `destination_bound_unsafe` without asserting safety; this is the deportation/forced-movement history contract. Both effects save the destination event target for the current chain and update the durable host/destination row.

`famine_migration_rebind_cohort_destination_safe` is the voluntary third-country resettlement update contract. The caller first resolves the persisted cohort, then enters the actual new destination state and supplies `famine_migration_cohort_resettlement_rebind_request_proven`, `..._food_safe_proven`, `..._reception_proven`, `..._route_proven`, and `..._actor_proven`. The trigger validates the current host and persisted owner targets, rejects a destination equal to the current host, and the effect accepts only `destination_bound` rows. It replaces aligned destination and host entries, preserves origin, owner, status, and survivor amount, returns `famine_migration_cohort_resettlement_rebind_result`, and never creates or removes population. It saves the actual destination as `famine_migration_route_destination` for the current chain.

`famine_migration_resolve_cohort_origin` derives a requested row from an explicit cohort ID or from an unambiguous host-state selection, returns the persisted original state and current host targets, and returns a bound destination target only for safe or unsafe bound rows. A decision transaction must call this resolver before testing event targets because ordinary event targets do not survive across transactions. Voluntary return requires the persisted original state plus food, route, housing, persecution, contamination, and host-safety proof; forced return resolves that same original state but intentionally uses its separate unsafe-host and policy proof and does not call the normal destination safety trigger. Missing, stale, or ambiguous IDs fail closed, and no random safe neighbor is ever selected.

The exact transfer's origin debit is the survivors plus route deaths, while destination credit is survivors only. After a successful transfer, `famine_migration_update_cohort_host_after_transfer` replaces the host and persisted amount with `famine_migration_transfer_survivor_credit`; a zero survivor credit removes the row so route deaths cannot be resurrected. `famine_migration_cleanup_cohort_record` removes all aligned entries by explicit ID, while the state invalidation helper removes rows touching an invalid state. State selection is authoritative for host decisions; the country selection is only a bounded owner-side convenience and is cleared on zero or ambiguous rows.

`famine_migration_set_border_policy` is a country-scope adapter that accepts one enum request from `famine_migration_border_policy` and returns `famine_migration_border_policy_result`.

The accepted policies are humanitarian open, controlled, transit-only, quarantine, closed, violent, and forced return.

Invalid policy tokens are rejected and the request is cleared.

`famine_migration_register_trapped_population` is a state-scope adapter that accepts a positive `famine_migration_trapped_request_amount`, sets the trapped flag, registers the state and owner country, and returns `famine_migration_trapped_result`.

`famine_migration_refresh_reception_capacity` is a country-scope adapter that accepts a positive absolute `famine_migration_reception_capacity_request`, stores it, registers the country, and returns `famine_migration_reception_result`.

`famine_migration_apply_reception_delta` is the centralized exact accounting seam for accepted survivor credits and debits. It runs in the actual destination state with a positive `famine_migration_reception_delta_amount`, one `famine_migration_reception_delta_request_proven` marker, and `famine_migration_reception_delta_mode = constant:famine_migration_reception_delta.credit` or `.debit`. A credit adds the same actual survivor amount to `famine_migration_state_reception_load` and its owner-country `famine_migration_reception_load`; a debit requires both ledgers to contain the full amount before subtracting from both. It returns `famine_migration_reception_delta_applied` and `famine_migration_reception_delta_result`, refreshes reception/overcrowded state flags and modifiers, and clears one-shot inputs. It does not infer or repeat a transfer, so callers use it once per exact survivor transaction.

`famine_migration_record_state_resettlement_projection` and `famine_migration_record_state_return_projection` record positive survivor projection amounts in the actual destination/origin state, set their explicit state flags, refresh modifiers, and never create population. `famine_migration_state_flight_population` and `famine_migration_state_trapped_population` mirror accepted flight/trapped request amounts while the existing displacement/trapped flags remain authoritative. State cleanup and displacement unregister clear all projection variables and flags; country cleanup clears reception, integration, resettlement, and return projections.

`famine_migration_evaluate_voluntary_return` requires all return proof inputs checked by `famine_migration_return_request_is_valid`, sets `famine_migration_voluntary_return_eligible`, and returns `famine_migration_return_result`.

`famine_migration_integrate_displaced_cohort` requires explicit cohort, capacity, and policy proof and records integrated population without creating population.

`famine_migration_resettle_displaced_cohort` requires an event-target destination plus destination proof and records resettled population without creating population.

`famine_migration_force_return_cohort` requires unsafe-host proof, forced-return policy proof, and a valid destination target, then sets `famine_migration_forced_return_pending` for the owner to execute through the exact transfer contract.

`famine_migration_mark_cohort_resolution_transaction` is a country-scope marker for a parent return or explicit cleanup consumer. After its exact transaction succeeds, the caller supplies `famine_migration_cohort_resolution_transaction_request_proven`; the effect sets `famine_migration_cohort_resolution_transaction_proven` and returns `famine_migration_cohort_resolution_transaction_result`. The bounded registered-country processor aggregates nonterminal aligned cohort amounts owned by that country into `famine_migration_achievement_cohort_people`, calls `famine_migration_achievement_record_major_cohort_duration`, and sets `famine_migration_achievement_all_major_cohorts_resolved` only when a previously tracked major total reaches zero with that marker. Integration and safe resettlement set the marker on successful completion; return and cleanup consumers must call the marker explicitly after valid completion.

All cohort adapters fail closed when proof or capacity is missing and clear one-shot request values after evaluation.

## Dynamic food-security evaluator and mortality

`famine_migration_submit_surface_context` is a state-scope owner adapter. The caller supplies explicit proof and normalized `famine_migration_input_production`, `famine_migration_input_transport`, `famine_migration_input_extraction`, `famine_migration_input_need`, `famine_migration_input_environment`, `famine_migration_input_vulnerability`, `famine_migration_input_governance`, and `famine_migration_input_relief` values on a 0-100 pressure scale.

The evaluator adds read-only public context from the existing Air Cleanliness, fallout, camp/genocide, occupation, war, outbreak, and disaster surfaces when their state or proof inputs exist. It never owns those systems' direct damage. Air contamination bands use the existing 25/50/75/100 global flags, while state Air exposure, strategic bombing pressure, nuclear fallout intensity, dynamic fallout/chemical modifiers, camp variables, and explicit local war/occupation/outbreak/disaster proof remain state-local inputs.

`famine_migration_resolve_occupation_profile` reads state-scope `occupation_law` and maps the audited vanilla tokens `foreign_civilian_oversight`, `local_police_force_garrison`, `secret_police_oversight`, `military_governor_occupation`, `martial_law_occupation`, `forced_labor_occupation`, `harsh_quotas_occupation`, and `brutally_oppressive_occupation`, plus Chaos Redux's `concentration`, `cbrn_coercive_security_occupation`, and `cbrn_protected_occupation_administration`, to bounded protective, standard, extraction, forced-labor, collective-punishment, population-transfer, or exterminatory context. It is read-only and does not invent an occupation-law change hook.

`famine_migration_resolve_historical_profile_context` is the sole profile eligibility resolver. It reads the requested profile ID but accepts it only when the audited state ID, owner/controller, date window, occupation/policy or route causal proof, and current food pressure conditions for that profile all pass; memory profiles additionally require explicit owner-supplied `famine_migration_profile_memory_proven` evidence and never activate from a date alone, policy analogues require the resolved occupation-law profile, and the nuclear-winter profile requires an active registered state plus Air Cleanliness/local vulnerability evidence. The resolver contains the fifteen profile-specific branches and fails closed for unmapped states or missing owner surfaces.

`famine_migration_apply_historical_profile_context` calls the resolver, writes dynamic starting component context and a mode (`memory`, `historical_window`, `policy_analogue`, or `dynamic_regional`), and never writes a historical death total. It clears stale context when a profile leaves its audited window or loses causal proof, so a prior profile cannot continue contributing pressure.

`famine_migration_register_historical_profile_anchor_state` and `famine_migration_unregister_historical_profile_anchor_state` maintain the bounded audited map-anchor registry. `famine_migration_bootstrap_historical_profile_anchors` seeds the registry once through exact `random_state` calls whose priority and limit each name one centralized state ID, including all 22 Spain anchors audited by `map-inspect.a672f4ba67035c47.json` (SHA-256 `01e2214cf4c25a9f39d32a7317c205984140281c120885e91905db7f2982c723`). `famine_migration_select_historical_profile_id` chooses among the fifteen profile IDs only after checking the mapped state, owner/controller, date, policy/war/food/route evidence, memory proof, or Air evidence. `famine_migration_process_registered_historical_profile_anchor` re-runs that selector from the host-only coordinator so a profile can enter its future date window without an owner setting an arbitrary profile boolean. `famine_migration_register_historical_profile_candidate_state` still adds a state only after the resolver's named result predicate is true, and `famine_migration_process_registered_historical_profile_candidate` refreshes those sparse validated candidates. `global.famine_migration_historical_profile_anchor_states` and `global.famine_migration_historical_profile_candidate_states` are explicit bounded registries, not map scans; their active flags and predicates expose lifecycle to callers and cleanup.

`famine_migration_evaluate_food_security` composes named components dynamically. Its score is `clamp(((1.15*production) + (1.10*transport) + (1.25*extraction) + (1.00*need) + (0.80*environment) + (0.90*vulnerability) + (0.95*governance) - (1.20*relief)) / 7.15, 0, 200)` after each component is clamped to 0-100. These values are centralized in `famine_migration_food_weight` and are not repeated in callers.

When a state has trapped population, the evaluator derives normalized trapped need pressure as `clamp((trapped_population / (state_population_k * constant:chaos_meter_deaths.people_per_k)) * 100, 0, 100)`. That pressure is added to both the normalized need and vulnerability components before the weighted score is composed, so a trapped population contributes according to its share of the state's measured civilian population rather than as an unbounded raw headcount.

The stage entry thresholds are stable below 25, supply strain at 25, acute shortage at 50, famine at 75, and catastrophic famine at 100. Each upward transition requires a candidate duration of 7, 7, 14, 21, or 30 days for stable, supply strain, acute shortage, famine, and catastrophic famine respectively. Recovery uses hysteresis thresholds of 20, 40, 60, and 80 and durations of 14, 21, 30, and 45 days for the active stage. `famine_migration_food_incident_count` increments on acute-or-worse entry and stage flags are reset atomically.

`famine_migration_apply_famine_mortality` runs only for acute shortage, famine, or catastrophic famine after its stage exposure minimum and due date. It derives population from `state_population_k * constant:chaos_meter_deaths.people_per_k`, reserves the larger of the dynamic 15 percent protected floor and the centralized minimum floor, and scales the pulse by stage rate, exposure, vulnerability, transport/need access, extraction, environment, governance, and relief factors. It calls `apply_exact_state_civilian_population_loss` exactly once with the protected floor, the actual famine reason, and death logging enabled, then stores the helper's `state_civilian_population_loss_applied` result. There is no fixed historical death outcome and no second debit.

## Famine and migration food-reserve ledger

Purpose: maintain a state-owned food reserve amount, capacity, target, replenishment/depletion history, and explicit decision-facing relief outputs without introducing a flat modifier or changing population.

Owner source: `common/scripted_effects/chaosx_famine_migration_effects.txt` with tuning in `common/script_constants/famine_migration_constants.txt`.

Scope: state. The evaluator invokes the refresh and date-idempotent update only for states already present in the bounded active-food registry, so reserve work remains sparse and never scans the world.

Units: one reserve unit is one thousand-person-day. A state with `state_population_k = 1000` therefore consumes approximately 1000 reserve units per day, and a 30-day target is approximately 30000 units before the logistics factor.

Capacity formula: `daily_need = round(max(1, state_population_k * constant:famine_migration_food_reserve.daily_need_per_k))`, `logistics_factor = clamp(constant:famine_migration_food_reserve.logistics_factor_base + infrastructure_level * constant:famine_migration_food_reserve.logistics_factor_per_infrastructure - component_transport * constant:famine_migration_food_reserve.transport_capacity_penalty - component_production * constant:famine_migration_food_reserve.production_capacity_penalty, logistics_factor_minimum, logistics_factor_maximum)`, `capacity = round(max(1, daily_need * capacity_days * logistics_factor))`, and `target = min(capacity, round(max(1, daily_need * target_days * logistics_factor)))`.

Initialization: the first valid refresh does not invent stock. An owner must provide a positive `famine_migration_food_reserve_initial_amount` with `famine_migration_food_reserve_initialization_proven > 0`, or an existing positive reserve amount must already be present in the save; only then does the helper set `famine_migration_food_reserve_initialized`. A zero amount remains zero until an explicit import or proven initial allocation, while a live amount is never silently raised to capacity.

Stable replenishment formula: once per game date, an initialized stable state adds `min(target - amount, round(daily_need * replenishment_per_k_per_day * max(replenishment_factor_minimum, 1 - component_production / 100) * max(replenishment_factor_minimum, 1 - component_transport / 100) * logistics_factor))`; an uninitialized zero ledger does not self-create stock.

Active depletion formula: once per game date, supply strain, acute shortage, famine, or catastrophic famine removes `min(amount, round(daily_need * stage_depletion_share * max(depletion_factor_minimum, component_need / 100)))`, where the stage shares are centralized as 0.05, 0.20, 0.50, and 1.00.

Score relief formula: `reserve_relief = clamp((amount / daily_need) * relief_per_day_covered + famine_migration_food_reserve_relief, 0, relief_maximum)`. The evaluator adds this bounded value to the existing normalized relief component before applying the centralized food-score weights.

Persistent state fields: `famine_migration_food_reserve_amount`, `..._initial_amount`, `..._initialization_proven`, `..._capacity`, `..._target`, `..._daily_need`, `..._logistics_factor`, `..._relief`, `..._last_update_date`, `..._last_replenished`, `..._last_depleted`, `..._last_imported`, `..._last_consumed`, `..._last_transfer_in`, `..._last_transfer_out`, and cumulative `..._total_replenished`, `..._total_depleted`, `..._total_imported`, `..._total_consumed`, `..._total_transfer_in`, and `..._total_transfer_out` are initialized by `famine_migration_initialize_food_state`.

`famine_migration_refresh_food_reserve_capacity` is a state-scope read/initialize helper. It takes live state population, infrastructure, and already-composed production/transport components, writes persistent capacity/target/need/logistics fields, and returns temporary `famine_migration_food_reserve_refresh_result`, `..._capacity_output`, `..._target_output`, `..._amount_output`, `..._daily_need_output`, and `..._logistics_factor_output`.

`famine_migration_update_food_reserve` is a state-scope date-idempotent mutation helper. It returns temporary `famine_migration_food_reserve_update_result`, `..._replenished_output`, `..._depleted_output`, `..._amount_output`, `..._daily_need_output`, and `..._relief_output`; repeated calls on the same game date do not replenish, deplete, or decay relief a second time.

`famine_migration_consume_food_reserve_for_relief` and its public aliases `famine_migration_release_food_reserves` and `famine_migration_consume_food_reserves_as_relief` accept positive `famine_migration_food_reserve_release_amount` only with `..._release_request_proven` and `..._release_actor_proven`. They return temporary `..._consume_result`, `..._consumed_output`, `..._relief_granted_output`, and `..._remaining_output`, consume only the actual available amount, add bounded transient relief, and clear the one-shot request/proof variables.

`famine_migration_add_food_reserves` and its public alias `famine_migration_import_food_reserves` accept positive `famine_migration_food_reserve_import_amount` only with `..._import_request_proven`, `..._import_source_proven`, and `..._import_actor_proven`. They return temporary `..._add_result`, `..._added_output`, `..._remaining_output`, and `..._capacity_output`, credit only free capacity, record the exact accepted amount in the import totals, and clear one-shot inputs.

`famine_migration_transfer_food_reserves` and its public alias `famine_migration_requisition_food_reserves` run in the source state and require positive `famine_migration_food_reserve_transfer_amount`, `..._transfer_request_proven`, `..._transfer_route_proven`, `..._transfer_actor_proven`, and the regular event target `famine_migration_food_reserve_destination`. The destination must be a distinct valid state. The helper returns temporary `..._transfer_result`, `..._transfer_source_debit_output`, `..._transfer_destination_credit_output`, and `..._transfer_remaining_output`.

Transfer conservation: `accepted = min(request, source_amount, destination_capacity - destination_amount)`, source debit and destination credit are measured from the actual before/after values, and a residual is rolled back before cumulative transfer ledgers advance. The valid result requires `source_debit - destination_credit = 0`, and the two actual amounts are then written once to `..._total_transfer_out` and `..._total_transfer_in`; no population or logistics ledger is touched.

Decision integration contract: an owner decision proves authority and route/source context, sets one documented request bundle, calls the matching public alias in the actual state scope, reads explicit accepted/result outputs in the same effect chain, and never edits `famine_migration_food_reserve_amount` directly. Decisions can display capacity, target, amount, and accepted output through their own localisation consumer without introducing a second reserve stockpile.

Cleanup: state registration cleanup removes active flags and transient food components but intentionally does not clear reserve amount, capacity, target, initialization, cumulative totals, or historical population ledgers. Retirement therefore stops scheduling without erasing reserve history; a later valid owner context can refresh capacity and resume the ledger.

Example:

```txt
# State-scope owner decision transaction.
set_variable = { famine_migration_food_reserve_release_amount = 250 }
set_variable = { famine_migration_food_reserve_release_request_proven = 1 }
set_variable = { famine_migration_food_reserve_release_actor_proven = 1 }
famine_migration_release_food_reserves = yes
# Read famine_migration_food_reserve_consume_result and accepted outputs here.
```

## Registry-only scheduling and lifecycle

`famine_migration_process_registered_runtime` is called by the existing `is_global_host` country guard in `common/on_actions/chaosx_on_actions_chaos_meter.txt`. It performs the one-time exact-anchor bootstrap, then uses `for_each_scope_loop` on `global.famine_migration_historical_profile_anchor_states`, `global.famine_migration_historical_profile_candidate_states`, `global.famine_migration_active_food_states`, `global.famine_migration_active_displacement_states`, and `global.famine_migration_active_displacement_countries`, so work is proportional to registered entries and never invokes `every_state` or `every_country`. The nuclear on-action also registers its actual nuked state as an anchor, allowing the Air Cleanliness profile to enter only after the state is active and local Air/food proof is present.

`famine_migration_process_registered_food_state`, `famine_migration_process_registered_displacement_state`, and `famine_migration_process_registered_displacement_country` validate each scope and retire invalid or recovered entries. `famine_migration_handle_state_control_change`, `famine_migration_mark_country_war_reassessment`, `famine_migration_mark_country_peace_reassessment`, and `famine_migration_handle_nuclear_state_change` are lifecycle adapters for the documented `on_state_control_changed`, `on_war_relation_added`, `on_peace`, `on_peaceconference_ended`, `on_annex`, and `on_nuke_drop` scopes.

`famine_migration_retire_recovered_state` clears active surface/profile flags, removes the historical-profile candidate, and removes a stable, pressure-free state from the registries without touching any other state.

## Movement request adapter names

`famine_migration_request_internal_displacement`, `famine_migration_request_cross_border_flight`, `famine_migration_request_organized_evacuation`, and `famine_migration_request_deportation_flow` are skeleton consumers for owner-local gameplay. Each requires positive amount and actor proof plus its route, border, transport, or policy proof; each fails closed and clears one-shot request values. They register flight/food pressure but do not debit population or fabricate a destination. Existing aliases `famine_migration_request_reception_capacity`, `famine_migration_request_integration`, `famine_migration_request_resettlement`, `famine_migration_request_voluntary_return`, and `famine_migration_request_forced_return` expose stable names for later decision owners.

## Famine and migration cleanup

`famine_migration_cleanup_route_request` clears one-shot route proof, amount, death, and result values; regular event targets are intentionally left to their engine lifecycle and are not global targets.

`famine_migration_cleanup_state_registration` is a state-scope cleanup helper for state invalidation, annexation, control loss, destination loss, or route cancellation.

It removes the state from both active state registries and clears food, flight, trapped, and source variables without scanning other states.

`famine_migration_cleanup_country_registration` is a country-scope cleanup helper for annexation, peace, country-classification, or explicit destination invalidation.

It runs when `famine_migration_cleanup_requested > 0` or the country no longer satisfies `famine_migration_country_is_valid`, removes the country from the displacement registry, clears lifecycle flags, and clears reception and integration variables.

The dormant-country retirement effect is narrower than full country-registration cleanup: it removes only an inactive scheduler entry and its transient state, so historical integration, resettlement, and return ledgers remain available to achievement and history consumers.

## Famine and migration dynamic state modifiers

The state-scoped definitions live in `common/dynamic_modifiers/famine_migration_state_modifiers.txt` and use the existing `GFX_fm_state_*` icons. `famine_migration_refresh_dynamic_modifiers` removes all nine famine/migration modifier families, then adds the stage and flow families whose state flags are active. `famine_migration_clear_dynamic_modifiers` removes the same set and forces one modifier refresh.

Stage families are `famine_migration_state_supply_strain`, `famine_migration_state_acute_shortage`, `famine_migration_state_famine`, and `famine_migration_state_catastrophic_famine`. They consume only centralized `famine_migration_modifier` constants for local supplies, production speed, local resources, supply impact, controller attrition, and controller movement speed. The modifiers supplement the normalized evaluator score; they do not write or replace any food-pressure variable.

Flow families are `famine_migration_state_exodus`, `famine_migration_state_reception`, `famine_migration_state_overcrowded`, `famine_migration_state_trapped_border`, and `famine_migration_state_return`. Exodus consumes the existing `famine_migration_displacement_active` state flag, and trapped-border consumes the existing `famine_migration_population_trapped` flag. Reception, overcrowded, and return are derived by `famine_migration_refresh_reception_context` from validated state and owner-country ledgers after accepted reception, resettlement, or return transactions. The shared layer never infers a policy outcome from a country-only capacity or return variable, and owner callers remain responsible for supplying the transaction proof.

Every stage transition and evaluator pass refreshes the modifiers. State cleanup clears them before unregistering the state and also clears the three owner flow-context flags. Control-change and nuclear lifecycle handlers refresh the current flag set. Repeated refresh and cleanup calls are safe because removal precedes addition and `remove_trigger` mirrors each enable flag.

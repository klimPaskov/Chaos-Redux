# chaosx_dynamic_triggers

This file documents reusable dynamic scripted triggers under `common/scripted_triggers/`. The point of these triggers is to keep complex trigger logic centralized so events, decisions, AI, and system adapters can call one reusable block instead of duplicating large script chunks.

## Reuse guidance

Before adding new dynamic trigger logic, check this file and reuse an existing trigger if it already matches the behavior. If no trigger matches, create a new one in `chaosx_dynamic_triggers.txt` and document it here in the same change with: purpose, scope, inputs, defaults, outputs, side effects, and example usage.

## Table of contents

- [is_desert_state](#is_desert_state)
- [is_special_chaos_country](#is_special_chaos_country)
- [is_actual_nonhuman_country](#is_actual_nonhuman_country)
- [cbrn_country_has_program](#cbrn_country_has_program)
- [CBRN readiness triggers](#cbrn-readiness-triggers)
- [CBRN policy triggers](#cbrn-policy-triggers)
- [CBRN state triggers](#cbrn-state-triggers)
- [CBRN action validation triggers](#cbrn-action-validation-triggers)
- [cbrn_chemical_action_metadata_is_valid](#cbrn_chemical_action_metadata_is_valid)
- [CBRN protection category and country gates](#cbrn-protection-category-and-country-gates)
- [CBRN state distribution gates](#cbrn-state-distribution-gates)
- [CBRN exact-state response gates](#cbrn-exact-state-response-gates)
- [CBRN allied procurement and AI profiles](#cbrn-allied-procurement-and-ai-profiles)
- [CBRN regimental support and AI gates](#cbrn-regimental-support-and-ai-gates)
- [CBRN payload-logistics triggers](#cbrn-payload-logistics-triggers)
- [CBRN designer trait triggers](#cbrn-designer-trait-triggers)
- [CBRN chemical-air raid reservation triggers](#cbrn-chemical-air-raid-reservation-triggers)
- [Chaos Warfare doctrine triggers](#chaos-warfare-doctrine-triggers)
- [CBRN Army Headquarters triggers](#cbrn-army-headquarters-triggers)

## is_desert_state

## is_special_chaos_country

Country-scope trigger. Returns true for system actors and special scenario countries that should not be treated like normal civilian societies.

Current coverage includes:

- `ZZZ` / original `ZZZ` outbreak countries
- dynamic zombie outbreak countries
- weaponized zombie outbreak countries
- `REV` and countries with original tag `REV`
- communist rebel-state flags
- `ZIN`
- countries using the `The Holy Realm` cosmetic tag
- countries using the `The Great Mandala` or `The Silent Mandala` Holy Realm identity cosmetic tags
- countries with the Holy Realm active marker
- Germany Mengele civil-war and post-coup state markers
- active Fury actor countries
- `DTH` / original `DTH` / countries with the Death country marker
- `DHO` / original `DHO` / countries with the Event 018 cave-country marker
- Event 014 cannibal warlord countries
- the unified Event 014 country
- the transformed Event 014 Wendigo country
- Event 019 derivative countries, including dynamically created claimant-led
  and family-host actors

## is_actual_nonhuman_country

Country-scope trigger. Returns true only for countries that should currently be treated as actually nonhuman rather than merely unusual or scenario-specific.

Current coverage includes:

- `ZZZ` / original `ZZZ` outbreak countries
- dynamic zombie outbreak countries
- weaponized zombie outbreak countries
- Wendigo outbreak flags or the Wendigo cosmetic tag
- `ZIN`
- `DTH` / original `DTH` / countries with the Death country marker
- `DHO` / original `DHO` / countries with the Event 018 cave-country marker
- the transformed Event 014 Wendigo country; ordinary cannibal warlords and the ordinary unified country remain human
- Event 019 derivatives carrying the nonhuman marker; claimant-only human
  breakaways remain special without being classified as nonhuman

## cbrn_country_has_program

Country-scope trigger. Returns true when the country has the explicit `cbrn_program_established` flag or currently uses the `chaos_warfare` grand doctrine. This preserves legacy doctrine adoption while program decisions are migrated.

Inputs: none. Defaults: false. Side effects: none.

Example:

```txt
visible = { cbrn_country_has_program = yes }
```

## CBRN readiness triggers

Country-scope, side-effect-free triggers:

- `cbrn_country_has_limited_readiness`: `chemical_readiness` is at least 20
- `cbrn_country_has_operational_readiness`: at least 40
- `cbrn_country_has_integrated_readiness`: at least 60
- `cbrn_country_has_full_readiness`: at least 80

Inputs: persistent `chemical_readiness`. An absent value returns false. Outputs: boolean trigger result only.

Example:

```txt
available = { cbrn_country_has_operational_readiness = yes }
```

## CBRN policy triggers

Country-scope, side-effect-free triggers:

- `cbrn_policy_is_defensive_preparation`
- `cbrn_policy_is_retaliation_authority`
- `cbrn_policy_allows_battlefield_use`
- `cbrn_policy_allows_strategic_use`
- `cbrn_policy_allows_extreme_use`

Inputs: persistent `cbrn_use_policy`; retaliation also requires temporary authorization flag `cbrn_retaliation_authorized`. Defaults: an absent or unset policy allows no offensive use. Outputs: boolean trigger result only.

Example:

```txt
available = {
	cbrn_policy_allows_battlefield_use = yes
}
```

## CBRN state triggers

State-scope, side-effect-free triggers:

- `cbrn_state_has_chemical_contamination`
- `cbrn_state_has_serious_chemical_contamination`
- `cbrn_state_has_severe_medical_saturation`
- `cbrn_state_attribution_is_suspected`
- `cbrn_state_attribution_is_probable`
- `cbrn_state_attribution_is_confirmed`

Inputs: the matching lazy state variables. Defaults: absent values return false. Outputs: boolean trigger result only.

Example:

```txt
event_target:cbrn_action_target_state = {
	cbrn_state_has_serious_chemical_contamination = yes
}
```

## CBRN action validation triggers

These side-effect-free triggers validate temporary action context:

- `cbrn_action_actor_is_valid`
- `cbrn_action_target_state_is_valid`
- `cbrn_action_weapon_class_is_chemical`
- `cbrn_action_agent_class_is_chemical`
- `cbrn_action_agent_is_valid_chemical`
- `cbrn_action_agent_matches_class`
- `cbrn_action_delivery_route_is_recognized`
- `cbrn_action_delivery_route_is_supported`
- `cbrn_action_agent_is_eligible_for_route`
- `cbrn_action_severity_is_valid`
- `cbrn_action_payload_debit_is_valid`
- `cbrn_action_protection_is_resolved`
- `cbrn_action_conditions_are_resolved`
- `cbrn_chemical_action_static_metadata_is_valid`

Scope: enclosing attacker-country action chain, except the target event target itself is state scoped.

Inputs: the temporary contract documented under `cbrn_prepare_chemical_action_record` in `common/scripted_effects/chaosx_dynamic_effects.md`.

Defaults: missing values return false. The continuous ordinary-air route is recognized so the caller can report an exact unsupported reason, but it is never supported.

Outputs: boolean trigger result only. Side effects: none.

`cbrn_chemical_action_static_metadata_is_valid` combines actor, exact target, weapon, agent/class, route eligibility, support status, and severity only. Route adapters use it before debiting payload so invalid metadata cannot consume stock.

## cbrn_chemical_action_metadata_is_valid

Composite country-chain trigger requiring the static preflight plus real payload-debit proof, resolved protection, and resolved conditions.

Inputs: complete temporary action contract. Defaults: fail closed. Outputs: boolean result. Side effects: none.

Use the public preparation effect for player-visible rejection reasons; this composite is intended for assertions and later internal dispatch guards.

Example:

```txt
if = {
	limit = { cbrn_chemical_action_metadata_is_valid = yes }
	# Continue to the shared action calculator.
}
```

## CBRN protection category and country gates

All triggers in this section are country scoped, side-effect free, and fail closed when required flags, equipment, factories, manpower, or variables are absent.

### Visibility and emergency context

- `cbrn_protection_program_category_visible`: true for an established program/reserve, Basic Service Respirators, real respirator stock, or confirmed enemy chemical use.
- `cbrn_civil_defence_category_visible`: combines program visibility with reserve/registration, a public emergency, or existing distributed state stock.
- `cbrn_country_has_public_chemical_emergency`: true only for confirmed enemy use, an exact scripted raid alert, or actual controlled-state contamination.

These triggers never inspect aircraft presence and cannot qualify idle chemical-capable aircraft.

### Stock-state triggers

- `cbrn_country_has_any_mask_stock`: actual gas-mask archetype stock is positive.
- `cbrn_country_has_exportable_mask_stock`: actual stock meets the centralized export reserve floor.
- `cbrn_country_needs_imported_masks`: actual stock is below that floor.
- `cbrn_country_has_military_mask_shortage`: a real refreshed military-coverage snapshot exists and is below 50 percent; an absent snapshot does not invent a shortage.
- `cbrn_country_has_military_choking_protection_low`, `cbrn_country_has_military_choking_protection_medium`, and `cbrn_country_has_military_choking_protection_high`: the refreshed model-, coverage-, and filter-weighted respiratory score reaches 25, 50, or 75.
- `cbrn_country_has_military_blister_protection_low`, `cbrn_country_has_military_blister_protection_medium`, and `cbrn_country_has_military_blister_protection_high`: the refreshed respiratory-and-skin blister composite reaches 25, 50, or 75.
- `cbrn_country_has_mask_replacement_backlog`: the persistent national replacement ledger exceeds the centralized research-priority threshold.
- `cbrn_country_controls_chemical_contamination`: at least one currently controlled state has actual chemical contamination.

Inputs are live equipment, snapshot, ledger, and controlled-state queries. Outputs are boolean only. The protection bands drive equipment-aware cylinder-ability AI and scripted localisation; the shortage, backlog, and contamination triggers support route- and condition-aware technology AI. They perform no scheduling or state changes.

### Production signals and stop conditions

- `cbrn_country_faces_enemy_chemical_capability`: a current enemy has researched a choking, blister, or nerve agent.
- `cbrn_world_has_confirmed_chemical_use`: the shared dispatcher has recorded confirmed chemical use, or an older save contains at least one country with positive public chemical Condemnation.
- `cbrn_country_has_priority_civilian_protection_gap` and `cbrn_country_has_full_civilian_protection_gap`: a controlled core state's effective coverage remains below its corresponding target.
- `cbrn_country_has_mask_production_signal`: reserve program, allied request, Chaos Warfare posture, enemy capability/use, public world use, or an exact controlled-state alert.
- `cbrn_country_below_mask_ai_target`: military coverage, reserve plus replacement stock, or eligible civilian distribution remains below the current profile target.
- `cbrn_country_should_produce_masks`: Basic Service Respirators plus both a valid signal/shortage and an unmet target.
- `cbrn_country_has_urgent_mask_production_need`: confirmed enemy use, field coverage below 50 percent, or an exact raid alert.

These triggers drive `common/ai_strategy/cbrn_protection_production.txt`. They are read-only trigger queries, not periodic country effects. The world-use query reads existing public Condemnation and does not expose latent evidence.

### National action gates

- `cbrn_can_establish_national_respirator_reserve`: Basic Service Respirators, no existing reserve, required factories, and real support equipment.
- `cbrn_can_register_and_fit_population`: reserve, unregistered population, mask stock, factories, support equipment, and 5,000 available manpower.
- `cbrn_can_issue_masks_to_field_army`: mask stock plus the issue project's factory/support burden.
- `cbrn_can_replace_military_mask_filters`: issued masks, worn filters, replacement stock, and factory capacity.
- `cbrn_can_recondition_damaged_masks`: damaged/rejected source ledger plus factory/support capacity.
- `cbrn_can_convert_civilian_mask_industry`: basic technology plus factory/support capacity.
- `cbrn_can_simplify_filters_for_mass_issue`: basic technology, no active simplified program, and factory/support capacity.

Example:

```txt
available = {
	cbrn_can_register_and_fit_population = yes
}
```

## CBRN state distribution gates

All triggers are state scoped and side-effect free. `ROOT` is the deciding country.

### State value and base validity

- `cbrn_state_has_priority_protection_value`: capital, victory point, industry, dockyard, air/naval base, or supply node.
- `cbrn_state_is_valid_distribution_target`: ROOT-controlled populated state, established ROOT national reserve, and no active protection project.

### Coverage gaps

- `cbrn_state_has_priority_distribution_gap`: effective coverage below 50 percent.
- `cbrn_state_has_full_distribution_gap`: effective coverage below 95 percent.
- `cbrn_state_has_emergency_distribution_gap`: effective coverage below 35 percent.
- `cbrn_state_has_occupied_distribution_gap`: effective coverage below 50 percent.

Absent `cbrn_civilian_mask_effective_coverage` counts as a gap. The value is written by `cbrn_refresh_state_civilian_mask_snapshot` and includes fitting and filter condition.

### Composite distribution targets

- `cbrn_state_can_receive_priority_masks`: valid ROOT core, priority value, and priority gap.
- `cbrn_state_can_receive_full_distribution`: valid ROOT core, registered/fitted ROOT population, and full gap.
- `cbrn_state_has_emergency_context`: an exact alert for this state or real contamination in this state. Country-wide confirmed enemy use does not qualify a clean, unalerted state.
- `cbrn_state_can_receive_emergency_masks`: ROOT-controlled populated state with emergency context and emergency gap; formal reserve/registration is deliberately not required.
- `cbrn_state_can_receive_occupied_masks`: valid non-core controlled state with occupied gap.
- `cbrn_state_can_replace_civilian_filters`: valid state with distributed masks and worn filters.

Example:

```txt
target_trigger = {
	FROM = { cbrn_state_can_receive_full_distribution = yes }
}
```

## CBRN exact-state response gates

All are state scoped, side-effect free, and require `cbrn_chemical_raid_alert_active`; a verified caller must create that flag through the exact-state adapter.

- `cbrn_state_has_exact_chemical_raid_alert`: exact alert flag only.
- `cbrn_state_has_hospital_response_resources`: the controller has the population-scaled mask/support amounts stored on the state.
- `cbrn_state_has_shelter_response_resources`: the controller has the population-scaled support/train amounts stored on the state.
- `cbrn_state_can_protect_hospitals_and_utilities`: exact alert, no prior hospital response, and full real resources.
- `cbrn_state_can_move_civilians_to_shelters`: exact alert, no shelter/industry-continuity conflict, and full real resources.
- `cbrn_state_can_sound_chemical_alarm`: exact alert and no alarm already active.
- `cbrn_state_can_keep_industry_operating`: exact alert and no shelter/continuity conflict.

The resource checks use meta triggers to inject the state-calculated dynamic equipment requirement into `has_equipment`, which otherwise accepts only static amounts.

Example:

```txt
available = {
	FROM = { cbrn_state_can_protect_hospitals_and_utilities = yes }
}
```

## CBRN allied procurement and AI profiles

### Allied partner triggers

- `cbrn_target_is_valid_allied_protection_partner`: existing, non-self, non-capitulated country in ROOT's faction.
- `cbrn_target_can_supply_imported_masks`: valid partner with at least the tuned shipment amount.
- `cbrn_target_can_receive_exported_masks`: valid partner at or below the low-reserve threshold.
- `cbrn_target_can_license_respirator_design`: valid partner with a higher gas-mask technology than ROOT.

Scope: candidate country with ROOT as the acting country. Defaults: stale or invalid candidates return false. Outputs: boolean only; side effects: none.

### Program-profile triggers

- `cbrn_profile_is_mass_civil_defence`
- `cbrn_profile_is_prepared_power`
- `cbrn_profile_is_military_first`
- `cbrn_profile_is_industrial_reserve`
- `cbrn_profile_is_civil_defence_network`
- `cbrn_profile_is_exposed_or_fragmented`
- `cbrn_profile_is_limited_program`
- `cbrn_profile_is_minimal_or_unassigned`
- `cbrn_profile_is_limited_or_minimal`

These country-scope triggers compare `cbrn_protection_program_profile` against the centralized enum and group related starting profiles for differentiated decision and production AI. Only `cbrn_profile_is_minimal_or_unassigned` deliberately accepts an absent profile. They do not choose targets, grant equipment, or alter policy.

Example:

```txt
modifier = {
	factor = constant:cbrn_protection_ai.mass_civil_defence_factor
	cbrn_profile_is_mass_civil_defence = yes
}
```

## CBRN regimental support and AI gates

These country-scope, side-effect-free triggers are defined in `cbrn_regimental_support_triggers.txt`. They use actual technology, policy, equipment stock, contamination, and outbreak state. Missing technology, equipment, or context fails closed. They do not infer per-division fulfillment, alter templates, authorize use, reserve payload, or dispatch exposure.

### Complete standing-template stock gates

- `cbrn_country_has_any_chemical_payload_stock`: true when at least one strategic chlorine, phosgene, mustard, lewisite, tabun, sarin, soman, malodor, or behavioral lot has positive real stock. Legacy cylinders remain accepted only during the bounded migration window. This is a production/readiness signal, not use authorization.
- `cbrn_country_has_protected_template_stock`: requires the full standing bill for one nine-infantry protected target, including infantry equipment, masks, decon, instruments, support equipment, and trucks.
- `cbrn_country_has_chemical_assault_template_stock`: requires the full standing bill for six infantry, three Chaos Assault Battalions, mask/decon, Hazard Pioneer, and Projector support, including the projector's standing strategic-agent payload load.
- `cbrn_country_has_armored_delivery_template_stock`: requires the full standing bill for three medium-armor and seven motorized battalions plus mask/decon, recon, and medium armored-delivery support, including the flame-role chassis and standing strategic-agent payload loads.
- `cbrn_country_has_containment_template_stock`: requires the full standing bill for nine infantry plus mask/decon, epidemiology, and medical support.

Inputs: current country equipment stock. Defaults: absent or insufficient stock returns false. Output: boolean only. Side effects: none.

### Template eligibility gates

- `cbrn_country_can_field_protected_template`: requires both defensive support unlocks, a complete stock set, and a CBRN program, Chaos Warfare doctrine, or real public emergency.
- `cbrn_country_can_field_chemical_assault_template`: requires all three unit unlocks, battlefield-use policy, positive chemical payload stock, and a complete standing set.
- `cbrn_country_can_field_armored_delivery_template`: requires armored-delivery and sealed-crew unlocks, a current medium-tank chassis path, battlefield-use policy, positive chemical payload stock, and a complete standing set.
- `cbrn_country_can_field_containment_template`: requires epidemiology and mobile-hospital unlocks, a complete standing set, and an actual domestic/neighbor outbreak, public chemical emergency, or controlled contaminated state.

Inputs: technology, policy, actual stock, outbreak, and contamination state. Defaults: false. Output: boolean only. Side effects: none. Offensive eligibility remains distinct from operation eligibility; the later adapter must still select and debit the exact payload before exposure.

### Production signals

- `cbrn_country_should_produce_regimental_decon`: field-decon technology plus a real program, emergency, contamination, or outbreak signal; actual nonhuman countries are excluded.
- `cbrn_country_should_produce_regimental_instruments`: detection technology plus the same bounded signals and exclusion.
- `cbrn_country_has_urgent_regimental_support_need`: true for a public chemical emergency, controlled contamination, or domestic/neighbor outbreak.

Inputs: technology and current system state. Defaults: false. Output: boolean only. Side effects: none. These feed AI strategies directly and create no periodic country iteration.

Example:

```txt
cbrn_ai_chemical_assault_ratio = {
	enable = { cbrn_country_can_field_chemical_assault_template = yes }
	abort_when_not_enabled = yes
	ai_strategy = {
		type = role_ratio
		id = cbrn_chemical_assault
		value = 2
	}
}
```

## CBRN payload-logistics triggers

These country-scope, side-effect-free triggers are defined in `cbrn_payload_triggers.txt`. They validate one temporary chemical-action record or one requested filling profile. Missing technology, a mismatched profile, a line-change lock, insufficient exact stock, or an unsupported route returns false and removes nothing.

- `cbrn_action_agent_is_unlocked` and `cbrn_requested_payload_agent_is_unlocked`: map each exact strategic agent to its technology or completed special project.
- `cbrn_action_uses_strategic_agent_lots`, `cbrn_action_uses_shell_lots`, and `cbrn_action_uses_air_payload_lots`: classify the action route into exactly one stock family.
- `cbrn_shell_profile_matches_action` and `cbrn_air_profile_matches_action`: require the persistent line profile to match the exact action agent and require the relevant reconfiguration lock to be absent.
- `cbrn_action_payload_profile_is_ready`: combines route family, matching profile, and the required shell- or air-delivery technology. Strategic lots need no filling-line profile.
- `cbrn_action_payload_stock_is_sufficient`: requires positive route demand and enough exact strategic-agent stock, shared shell lots, or class-specific air payload lots for the action.

Inputs are the temporary `cbrn_action_*` metadata and the persistent shell/air profile state. Outputs are boolean only. These triggers never set payload-consumption proof; only `cbrn_try_debit_action_payload` may do that after an exact equipment removal.

Example:

```txt
if = {
	limit = {
		cbrn_action_agent_is_unlocked = yes
		cbrn_action_payload_profile_is_ready = yes
		cbrn_action_payload_stock_is_sufficient = yes
	}
	cbrn_try_debit_action_payload = yes
}
```

## CBRN designer trait triggers

These country-scope, side-effect-free triggers are defined in `cbrn_designer_triggers.txt`. Each trigger searches the country's Military Industrial Organizations, includes an organization that later became invisible, verifies the exact CBRN organization token, and then requires the named trait to be completed. Merely having a trait in the tree, having it available, or owning another organization with a same-named trait never passes the check.

Chemical Munitions Combine queries:

- `cbrn_designer_has_stable_choking_fill` checks `cbrn_munitions_stable_choking_fill`;
- `cbrn_designer_has_persistent_agent_formulation` checks `cbrn_munitions_persistent_agent_formulation`;
- `cbrn_designer_has_rapid_front_distribution` checks `cbrn_munitions_rapid_front_distribution`;
- `cbrn_designer_has_standardized_fuzes` checks `cbrn_munitions_standardized_fuzes`;
- `cbrn_designer_has_high_output_filling_complex` checks `cbrn_munitions_high_output_filling_complex`.

Aerosol and Air Delivery Bureau queries:

- `cbrn_designer_has_lightweight_payload_assemblies` checks `cbrn_aerosol_lightweight_payload_assemblies`;
- `cbrn_designer_has_sealed_bomb_bay_interfaces` checks `cbrn_aerosol_sealed_bomb_bay_interfaces`;
- `cbrn_designer_has_controlled_dispersal` checks `cbrn_aerosol_controlled_dispersal`;
- `cbrn_designer_has_long_range_payload` checks `cbrn_aerosol_long_range_payload`;
- `cbrn_designer_has_precision_release` checks `cbrn_aerosol_precision_release`.

Scope: country only. Inputs: the country's loaded MIO instances and their completed-trait state. Defaults: false when the organization was not instantiated or the trait is absent or incomplete; calls outside country scope violate the helper contract. Output: boolean only. Side effects: none; these checks do not complete traits, assign an MIO to a task, alter equipment, change evidence, or modify Condemnation.

Example:

```txt
if = {
	limit = {
		cbrn_designer_has_persistent_agent_formulation = yes
		check_variable = { var = cbrn_action_agent_class value = constant:cbrn_agent_class.blister compare = equals }
	}
	multiply_temp_variable = { cbrn_action_contamination_points = constant:cbrn_munitions_designer_effect.persistent_contamination_mult }
}
```

## CBRN chemical-air raid reservation triggers

These temporary-record triggers live in `cbrn_chemical_raid_triggers.txt` and are valid only inside a native raid outcome effect chain:

- `cbrn_chemical_air_raid_result_has_no_release`: true only for the accepted aborted or failed result codes.
- `cbrn_chemical_air_raid_result_has_release`: true only for partial, successful, or catastrophic releases.
- `cbrn_chemical_air_raid_reservation_is_resolved`: requires the exact 120-lot reservation, positive net consumption no greater than that reservation, native reservation/debit proof, and a release-efficiency proof that agrees with the result class.

Scope: enclosing raid outcome chain after the actor-country effect has called `cbrn_resolve_chemical_air_raid_reservation`. Inputs are temporary `cbrn_raid_*` and `cbrn_action_*` values. Defaults: false; missing or contradictory proof fails closed. Outputs: boolean only. Side effects: none. These triggers do not infer weather, terrain, release, or aircraft activity.

Example:

```txt
if = {
	limit = { cbrn_chemical_air_raid_reservation_is_resolved = yes }
	# Continue to the no-release attempt record or the proven-release adapter.
}
```

## Chaos Warfare doctrine triggers

These country-scope, side-effect-free triggers are defined in `cbrn_doctrine_triggers.txt`, except for the one explicitly state-scoped cleanup target. Missing doctrine state, stock, variables, flags, technology, formations, or project proof fails closed unless an absent state is named as an accepted adoption route.

### Adoption and establishment

- `cbrn_chaos_warfare_has_agent_technology`: true for at least one supported choking, blister, or nerve-agent technology.
- `cbrn_chaos_warfare_has_completed_chemical_project`: true for one accepted completed chemical special-project flag.
- `cbrn_chaos_warfare_has_historical_program_profile`: true for a mapped preparedness, military, industrial, or civil-defence starting profile.
- `cbrn_chaos_warfare_adoption_capable`: accepts Basic Gas Masks plus an agent, a completed chemical project, established CBRN command, mapped historical profile, or explicit scenario override.
- `cbrn_chaos_warfare_ai_has_viable_program`: adoption capability plus a major, industrial, war, enemy-use, accepted profile, or explicit aggressive-route signal; actual nonhuman countries fail.
- `cbrn_chaos_warfare_has_establishment_stock`: at least 500 masks, 50 decontamination equipment, and 100 support equipment.
- `cbrn_chaos_warfare_has_fielded_operations_hq`: positive exact `num_battalions_with_type@cbrn_hq_operations_section`.
- `cbrn_chaos_warfare_has_fielded_protected_formation`: positive exact `num_battalions_with_type@cbrn_gas_mask_decon_detachment`.
- `cbrn_chaos_warfare_establishment_requirements_met`: adopted doctrine plus all stock and fielded-formation proofs above.
- `cbrn_can_begin_hazard_assault_training`: Hazard Assault active, protected formation fielded, no active training mission, 100 masks, and 10 Army Experience.

Scope is country; outputs are boolean only; no trigger starts a mission, removes stock, or grants mastery.

### Institutional proof and state cleanup

- `cbrn_chaos_warfare_has_post_adoption_mask_production`: cumulative gas-mask production is strictly above the persistent adoption baseline. Missing baseline fails.
- `cbrn_chaos_warfare_has_protective_foundation_reserve`: at least 500 live masks.
- `cbrn_chaos_warfare_has_operational_payload_reserve`: at least 100 units of one supported chlorine, phosgene, mustard, lewisite, tabun, sarin, soman, malodor, or behavioral strategic-agent lot; legacy cylinders remain accepted until migration.
- `cbrn_chaos_warfare_has_strategic_payload_reserve`: at least 250 of one supported payload.
- `cbrn_chaos_warfare_has_terminal_payload_reserve`: at least 500 of one supported payload.
- `cbrn_chaos_warfare_has_delivery_track_mastery_two`: Hazard Assault, Contaminant Fire, or Toxic Armor mastery 2.
- `cbrn_chaos_warfare_has_two_tracks_mastery_three`: any two of the four accepted tracks at mastery 3.
- `cbrn_chaos_warfare_has_all_tracks_active`: all four accepted subdoctrines currently active.
- `cbrn_chaos_warfare_has_any_track_mastery_five`: any accepted track at mastery 5.
- `cbrn_chaos_warfare_has_advanced_protection`: Advanced Gas Masks, Sealed Assault Protection, or explicit equivalent-project flag.
- `cbrn_can_claim_protective_foundation`, `cbrn_can_claim_delivery_integration`, `cbrn_can_claim_theater_exploitation`, and `cbrn_can_claim_terminal_command`: exact one-time institutional gates described in `docs/systems/chaos_warfare_doctrine.md`.
- `cbrn_country_has_active_decontamination_corridor`: country has at least one army leader with the active corridor trait.
- `cbrn_state_can_receive_theater_decontamination`: state-scoped target gate requiring ROOT control, actual chemical contamination, and no active assignment lock.

These triggers read exact current stock, persistent history, native mastery, formation counts, readiness-policy state, and selected-state contamination. They do not infer production lines, fabricate payload, choose a random state, or mutate a ledger.

Example:

```txt
target_trigger = {
	FROM = { cbrn_state_can_receive_theater_decontamination = yes }
}
```

### Doctrine-only technology gates

The following country-scope triggers return true only when the named non-researchable technology is still absent and all mapped mastery, institution, project, protection, policy, chassis, agent, or prerequisite technology is present:

- `cbrn_can_grant_chaos_assault_battalion`
- `cbrn_can_grant_hazard_pioneer_formation`
- `cbrn_can_grant_improved_chaos_assault_equipment`
- `cbrn_can_grant_chemical_artillery_shells`
- `cbrn_can_grant_armored_agent_delivery`
- `cbrn_can_grant_sealed_tank_crews`
- `cbrn_can_grant_persistent_agent_shell_filling`
- `cbrn_can_grant_nerve_agent_suppression`
- `cbrn_can_grant_biological_security_assault`
- `cbrn_can_grant_mobile_decontamination_columns`
- `cbrn_can_grant_chemical_air_interdiction`
- `cbrn_can_grant_theater_cbrn_headquarters`

### Policy and AI gates

- `cbrn_doctrine_policy_change_is_available`: Chaos Warfare adopted and no active 90-day reassessment lock.
- `cbrn_can_set_defensive_preparation_policy`: policy-change gate and not already defensive.
- `cbrn_can_set_retaliation_authority_policy`: policy-change gate, not already retaliation, 5 Command Power, and readiness 10.
- `cbrn_can_set_limited_battlefield_policy`: Delivery Integration, 15 Command Power, readiness 40, operational payload reserve, and not already limited.
- `cbrn_can_set_strategic_release_policy`: Theater Exploitation, 25 Command Power, readiness 65, strategic payload reserve, and not already strategic.
- `cbrn_can_set_unrestricted_policy`: Terminal Command, 40 Command Power, readiness 85, terminal payload reserve, and not already at extreme-use policy.
- `cbrn_ai_route_allows_first_use`: explicit first-use/unrestricted route, high-chaos Soviet successor, or mapped Japan-China chemical campaign context.
- `cbrn_ai_route_allows_unrestricted_use`: explicit unrestricted route or high-chaos Soviet successor.
- `cbrn_ai_has_defensive_cbrn_profile`: mass civil defence, prepared power, civil-defence network, or an ordinary democratic country without an accepted first-use route.
- `cbrn_ai_has_battlefield_cbrn_profile`: military-first profile or accepted first-use route.

These triggers provide differentiated weights only. They do not bypass institutions, readiness, Command Power, payload stock, operation cost, cooldown, or shared consequence accounting.

Example:

```txt
available = { cbrn_can_set_limited_battlefield_policy = yes }
```

## CBRN Army Headquarters triggers

These side-effect-free triggers are defined in `cbrn_hq_triggers.txt`. Character-scope triggers read the current army command and use `OWNER` for its country. They do not estimate the fill ratio of a deployed HQ company; exact HQ composition and national operating stock are separate checks.

### Force bands and exact HQ composition

- `cbrn_hq_force_is_light`: fewer than 100 affected battalions.
- `cbrn_hq_force_is_standard`: 100 through 199 affected battalions.
- `cbrn_hq_force_is_mass`: at least 200 affected battalions.
- `cbrn_hq_has_operations_section`, `cbrn_hq_has_intelligence_weather_cell`, `cbrn_hq_has_protective_logistics_section`, `cbrn_hq_has_mobile_decontamination_column`, `cbrn_hq_has_medical_countermeasure_directorate`, and `cbrn_hq_has_biological_security_section`: exact `num_battalions_with_type@...` checks for one named HQ-only company.
- `cbrn_hq_has_strict_overmatch_combination`: Operations plus Protective Logistics plus Mobile Decontamination.
- `cbrn_hq_has_no_preparation_or_active_posture`: no preparation/active trait and no persistent operation code. The operation code deliberately blocks a newer posture until planned cleanup even after early supply failure.

Scope: character. Defaults: missing command/company is false. Outputs: boolean only.

### Owner context and command-validity gates

The owner-context triggers are `cbrn_hq_owner_has_chemical_operation_context`, `cbrn_hq_owner_has_protective_context`, `cbrn_hq_owner_has_decontamination_context`, `cbrn_hq_owner_has_sealed_area_context`, `cbrn_hq_owner_has_antidote_context`, `cbrn_hq_owner_has_infection_context`, and `cbrn_hq_owner_has_overmatch_context`. They require the accepted policy, readiness, payload, emergency, contamination, outbreak, or capstone state for their operation.

`cbrn_hq_command_is_deployed` requires a non-army-group, non-border-war commander with assigned divisions. The seven composite command-validity triggers add exact company composition and owner context:

- `cbrn_hq_prepare_command_is_valid`
- `cbrn_hq_protective_command_is_valid`
- `cbrn_hq_decon_command_is_valid`
- `cbrn_hq_seal_area_command_is_valid`
- `cbrn_hq_antidote_command_is_valid`
- `cbrn_hq_infection_command_is_valid`
- `cbrn_hq_overmatch_command_is_valid`

These are reused at activation, preparation completion, and weekly upkeep so removing a required HQ company or losing the relevant context fails closed.

### Exact activation and upkeep resource gates

Each activation trigger branches on the current force band and includes the full command-power gate. Its paired upkeep trigger reads the force band stored when the order was accepted, preventing later army reorganization from lowering the commitment.

`cbrn_hq_country_has_issued_filter_ledger` is a country-scope, side-effect-free prerequisite requiring a positive military-issued mask ledger and an initialized military filter-condition ledger. Missing values fail closed.

The nine country-scope filter-affordability triggers require that ledger plus enough condition for one exact operation/force-band debit. Each selects the base threshold without `military_filter_standardization` or the exact technology-reduced threshold with it:

- `cbrn_hq_country_can_pay_prepare_light_filters`
- `cbrn_hq_country_can_pay_prepare_standard_filters`
- `cbrn_hq_country_can_pay_prepare_mass_filters`
- `cbrn_hq_country_can_pay_protective_light_filters`
- `cbrn_hq_country_can_pay_protective_standard_filters`
- `cbrn_hq_country_can_pay_protective_mass_filters`
- `cbrn_hq_country_can_pay_overmatch_light_filters`
- `cbrn_hq_country_can_pay_overmatch_standard_filters`
- `cbrn_hq_country_can_pay_overmatch_mass_filters`

Inputs are the persistent military-issued mask count, filter condition, and technology state. Defaults are fail-closed for absent masks, absent condition, or insufficient condition. Outputs are boolean only; there are no side effects.

| Operation | Activation trigger and exact owner resources | Upkeep trigger and exact owner resources |
| --- | --- | --- |
| Chemical fire plan | `cbrn_hq_can_pay_prepare_activation`: command power, masks, exact issued-filter condition, instruments, support equipment | `cbrn_hq_can_pay_prepare_upkeep`: masks, instruments, support equipment |
| Protective posture | `cbrn_hq_can_pay_protective_activation`: command power, masks, exact issued-filter condition, support equipment | `cbrn_hq_can_pay_protective_upkeep`: masks, exact issued-filter condition, support equipment |
| Decontamination corridor | `cbrn_hq_can_pay_decon_activation`: command power, decontamination equipment, trucks, masks, support equipment, fuel | `cbrn_hq_can_pay_decon_upkeep`: decontamination equipment, trucks, masks, support equipment, fuel |
| Sealed operational area | `cbrn_hq_can_pay_seal_area_activation`: command power, support equipment, manpower | `cbrn_hq_can_pay_seal_area_upkeep`: support equipment |
| Antidote response | `cbrn_hq_can_pay_antidote_activation`: command power, support equipment, masks, Medical Capacity | `cbrn_hq_can_pay_antidote_upkeep`: support equipment, masks |
| Infection corridor | `cbrn_hq_can_pay_infection_activation`: command power, support equipment, decontamination equipment, instruments, masks, manpower, Medical Capacity | `cbrn_hq_can_pay_infection_upkeep`: support equipment, decontamination equipment, instruments, masks |
| Combined overmatch | `cbrn_hq_can_pay_overmatch_activation`: command power, support equipment, decontamination equipment, instruments, masks, exact issued-filter condition, trucks, fuel, Medical Capacity | `cbrn_hq_can_pay_overmatch_upkeep`: support equipment, decontamination equipment, instruments, masks, exact issued-filter condition, trucks, fuel |

`cbrn_hq_committed_force_is_light`, `cbrn_hq_committed_force_is_standard`, and `cbrn_hq_committed_force_is_mass` read the stored force-band enum. Filter wear is a bounded condition loss, not a fictitious stockpile: every mapped activation or upkeep requires both issued masks and the full exact condition debit before the matching effect can run. Scope is character, `OWNER` supplies the country resource checks, missing or insufficient resources return false, output is boolean only, and these triggers have no side effects.

The seven public ability gates combine command validity, no existing commitment, and full activation resources:

- `cbrn_hq_can_activate_prepare_chemical_offensive`
- `cbrn_hq_can_activate_theater_protective_posture`
- `cbrn_hq_can_activate_decontamination_corridor`
- `cbrn_hq_can_activate_seal_operational_area`
- `cbrn_hq_can_activate_mass_antidote_response`
- `cbrn_hq_can_activate_seal_infection_corridor`
- `cbrn_hq_can_activate_combined_overmatch`

Protective Posture and Mass Antidote Response additionally require Protective Foundation; Prepare Chemical Offensive requires Delivery Integration; Decontamination Corridor and Seal Operational Area require Theater Exploitation; Seal Infection Corridor requires Theater Exploitation plus Integrated Command mastery 4; Combined Overmatch requires Terminal CBRN Command.

Scope: character. Defaults: insufficient institution or resources return false. Outputs: boolean only. These checks use national reserve stock because current 1.19 script exposes no exact fulfillment query for one named deployed HQ support company; no aggregate-army estimator is retained.

### Baseline AI HQ template gates

- `cbrn_country_can_field_protected_hq`: Protective Logistics and Medical unlocks plus one complete protected-HQ standing bill.
- `cbrn_country_can_field_chemical_fireplan_hq`: Operations/Weather unlocks, operational readiness, battlefield-use policy, positive payload stock, and one complete fire-plan-HQ standing bill.
- `cbrn_country_can_field_contaminated_theater_hq`: decontamination unlock, actual controlled contamination, and one complete contaminated-theater-HQ standing bill.
- `cbrn_country_can_field_biological_containment_hq`: Biosecurity/Medical unlocks, an active outbreak, and one complete biological-containment-HQ standing bill.
- `cbrn_country_can_field_overmatch_hq`: Theater technology, full readiness, battlefield-use policy, positive payload stock, and the complete four-slot capstone-HQ bill.

Scope: country. The common base bill is 420 infantry equipment: four vanilla infantry battalions at 100 each plus 20 for the mandatory vanilla HQ staff. Defaults: missing unlock, context, or stock returns false. Side effects: none. Stage 10 may differentiate country preferences, but these safety and supply gates remain authoritative.

Example:

```txt
allowed = {
	cbrn_hq_can_activate_mass_antidote_response = yes
}
```

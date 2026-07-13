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
- `cbrn_world_has_confirmed_chemical_use`: at least one existing country has positive public chemical Condemnation.
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

- `cbrn_country_has_any_chemical_payload_stock`: true when at least one supported chemical payload model has positive real stock. This is a production/readiness signal only; positive stock is not use authorization.
- `cbrn_country_has_protected_template_stock`: requires the full standing bill for one nine-infantry protected target, including infantry equipment, masks, decon, instruments, support equipment, and trucks.
- `cbrn_country_has_chemical_assault_template_stock`: requires the full standing bill for six infantry, three Chaos Assault Battalions, mask/decon, Hazard Pioneer, and Projector support.
- `cbrn_country_has_armored_delivery_template_stock`: requires the full standing bill for three medium-armor and seven motorized battalions plus mask/decon, recon, and medium armored-delivery support, including the flame-role chassis subset.
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

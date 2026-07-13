# chaosx_dynamic_triggers

This file documents reusable dynamic scripted triggers from `common/scripted_triggers/chaosx_dynamic_triggers.txt`. The point of these triggers is to keep complex trigger logic centralized so events can call one reusable block instead of duplicating large script chunks.

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

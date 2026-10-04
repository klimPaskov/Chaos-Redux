# Legacy humanitarian affordability predicates

Source: [humanitarian_legacy_cost_triggers.txt](humanitarian_legacy_cost_triggers.txt).
Tuning: [humanitarian_legacy_cost_constants.txt](../script_constants/humanitarian_legacy_cost_constants.txt).
This neutral API serves the existing independent famine and migration decision owners.

## Shared contract

All 33 predicates have COUNTRY scope and inspect the current country as payer.
Inputs are the country's current native reserves and fresh `humanitarian_legacy_cost` constants.
No caller variables, parameters, stored quotes, actor flags, or event targets are required.
The result is Boolean only, with no scalar or array outputs and no side effects.
No amount or scope defaults are inferred, and the caller must enter the correct existing country.
Each component returns true when its native resource is not below the positive fee.
Each profile returns true only when every component in its exact spent tuple passes.
Use Boolean calls with `= yes` or `= no`, never named arguments or `$PARAMETER$` substitution.

These helpers prove only affordability.
The decision owner separately proves actor eligibility, selected state/control, route, cohort, safety, factories, mission slots, non-spend requirements and paid continuation identity.
Use the profile in `available`, `custom_cost_trigger`, and immediately before debit.
Resource colour selectors use the matching component.
An already paid delayed continuation uses its owner's paid receipt rather than requiring the same resources again.

## Components

Every component name is `humanitarian_cost_<key>_is_affordable`.
The table lists all 15 `<key>` values, their current nominal fees and exact native resource token.
Positive and `<key>_debit` constants are paired centrally, and these predicates read only the positive key.

| Key | Nominal amount | Native reader |
|---|---:|---|
| `pp_light` | 10 | `has_political_power` |
| `pp_standard` | 20 | `has_political_power` |
| `pp_heavy` | 35 | `has_political_power` |
| `train_light` | 5 | `has_equipment.train_equipment` |
| `train_heavy` | 10 | `has_equipment.train_equipment` |
| `convoy_light` | 5 | `has_equipment.convoy` |
| `convoy_heavy` | 10 | `has_equipment.convoy` |
| `support_light` | 50 | `has_equipment.support_equipment` |
| `support_heavy` | 100 | `has_equipment.support_equipment` |
| `infantry_light` | 100 | `has_equipment.infantry_equipment` |
| `infantry_heavy` | 250 | `has_equipment.infantry_equipment` |
| `fuel_light` | 500 | `has_fuel` |
| `fuel_heavy` | 1000 | `has_fuel` |
| `transport_planes` | 5 | `has_equipment.transport_plane_equipment` |
| `air_xp` | 10 | `has_air_experience` |

The archetypes match current decision gates and debits.
This API makes no equivalence claim for model-specific `train_equipment_1` or `convoy_1` readers.
It does not replace the worker evacuation's strict non-spend support50 prerequisite or the airlift's strict AI-only50XP factor.

## Profiles and direct decision consumers

Every profile name is `humanitarian_cost_<profile>_is_affordable`.
The numeric labels identify the accepted nominal tuple, while the actual amounts always come from central constants.
All profiles share the scope, inputs, results, defaults and side-effect contract above.
Call-site wiring is owned by the decision worker and parent.

| Profile | Component keys | Decision IDs |
|---|---|---|
| `pp20_support50_fuel500` | `pp_standard`, `support_light`, `fuel_light` | `famine_release_reserves` |
| `pp20_convoy10_fuel500` | `pp_standard`, `convoy_heavy`, `fuel_light` | `famine_emergency_imports` |
| `pp10_train5_fuel1000` | `pp_light`, `train_light`, `fuel_heavy` | `famine_repair_relief_route` |
| `pp20_convoy10_support50_fuel1000` | `pp_standard`, `convoy_heavy`, `support_light`, `fuel_heavy` | `famine_escorted_relief_convoy` |
| `pp20_planes5_fuel1000_airxp10` | `pp_standard`, `transport_planes`, `fuel_heavy`, `air_xp` | `famine_emergency_airlift` |
| `pp20_convoy5_fuel500` | `pp_standard`, `convoy_light`, `fuel_light` | `famine_invite_relief` |
| `pp20_train10_fuel1000` | `pp_standard`, `train_heavy`, `fuel_heavy` | `famine_evacuation` |
| `pp20_train5_fuel500` | `pp_standard`, `train_light`, `fuel_light` | `famine_requisition_safer_state`, `migration_evacuate_vulnerable`, `migration_voluntary_return` |
| `pp10_infantry100_fuel500` | `pp_light`, `infantry_light`, `fuel_light` | `famine_conceal_crisis`, `migration_restrict_departure` |
| `pp10_train5_fuel500` | `pp_light`, `train_light`, `fuel_light` | `famine_maintain_extraction`, `migration_prepare_evacuation`, `migration_open_departure_routes`, `migration_distribute_arrivals` |
| `pp20_infantry250_fuel1000` | `pp_standard`, `infantry_heavy`, `fuel_heavy` | `migration_close_border`, `migration_enforce_closure` |
| `pp20_train10_fuel500` | `pp_standard`, `train_heavy`, `fuel_light` | `migration_evacuate_workers` |
| `pp35_infantry100_fuel500` | `pp_heavy`, `infantry_light`, `fuel_light` | `migration_negotiate_corridor` |
| `pp20_support100_infantry100` | `pp_standard`, `support_heavy`, `infantry_light` | `migration_controlled_medical_reception` |
| `pp10_convoy5_fuel500` | `pp_light`, `convoy_light`, `fuel_light` | `migration_transit_only` |
| `pp20_support100_fuel500` | `pp_standard`, `support_heavy`, `fuel_light` | `migration_local_integration` |
| `pp35_train5_convoy5_fuel500` | `pp_heavy`, `train_light`, `convoy_light`, `fuel_light` | `migration_third_country_resettlement` |
| `pp35_train10_fuel1000` | `pp_heavy`, `train_heavy`, `fuel_heavy` | `migration_forced_repatriation` |

## Usage

```text
# COUNTRY payer scope. Other action requirements remain in the owner.
available = {
	humanitarian_cost_pp20_convoy10_fuel500_is_affordable = yes
}
custom_cost_trigger = {
	humanitarian_cost_pp20_convoy10_fuel500_is_affordable = yes
}
if = {
	limit = { humanitarian_cost_pp20_convoy10_fuel500_is_affordable = yes }
	# Existing owner debit and receipt path follows inside this branch.
}
```

```text
# COUNTRY scope inside the existing convoy colour selector.
trigger = { humanitarian_cost_convoy_heavy_is_affordable = yes }
```

## Evidence and validation limits

The inclusive source precedent is `migration_reception_preparation_triggers.txt:4-10`.
Installed `documentation/triggers_documentation.md:3073-3081,3835-3842,3957-3966,4547-4554` documents the country-scoped native readers.
Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:2359-2400` documents Boolean scripted-trigger calls.
Installed `documentation/script_concept_documentation.md:216-245` and `common/script_constants/documentation.md` govern the central table schema and field support.
Exact source paths, revisions, case results and outstanding MCP/native gates are recorded in [the implementation handoff](../../docs/plans/famine_and_migration_system_plans/subagent_handoffs/legacy_cost_core_implementation_20261003.md).
Parsed-source reserve tests do not establish native equipment aggregation, field-specific constant parsing, click-time revalidation or AI willingness.
No AI weight is supplied by this API.

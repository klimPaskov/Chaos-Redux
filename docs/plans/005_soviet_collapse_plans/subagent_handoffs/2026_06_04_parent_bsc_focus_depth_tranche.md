# Parent Handoff: AEX Focus Depth Tranche

## Scope

This tranche deepened the Basmachi Confederation focus tree inside Event 005 Soviet Collapse. It did not touch flags, country history, sprite files, release logic, scenarios, or other event systems.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Focuses Updated

The following AEX focuses no longer use generic `soviet_collapse_custom_splinter_*_reward_tt` route filler. They now expose AEX-specific reward tooltips and call existing Soviet Collapse mechanics through hidden payloads:

- `AEX_first_guard`
- `AEX_stores`
- `AEX_legitimacy`
- `AEX_rival`
- `AEX_doctrine`
- `AEX_economy`
- `AEX_league`
- `AEX_foreign`
- `AEX_diplomatic_plan`
- `AEX_inner_faction`
- `AEX_special_arm`
- `AEX_supply`
- `AEX_enemy_front`
- `AEX_war_plan`
- `AEX_civil_rule`
- `AEX_propaganda`
- `AEX_settlement`
- `AEX_industry_plan`
- `AEX_hidden_doctrine`
- `AEX_extreme_gate`

## Behavior Before

AEX had 20 focuses that displayed broad route-level reward text such as political, logistics, diplomacy, industry, or high-chaos route rewards. Most of those focuses called generic custom-splinter identity helpers, so the route read as a template rather than a Basmachi road-war country package.

## Behavior After

AEX now ties the affected focuses to concrete existing mechanics:

- caravan guard and raiding-column focuses create assault strength, mobile columns, and Soviet-obedience pressure
- road-store and supply focuses increase depot control, equipment, factory recovery, and supply depth
- legitimacy and civil-rule focuses strengthen recognition, institution strength, resilience, and compact mechanics
- League and foreign-route focuses improve League support, liaison reach, foreign recognition, and deployable League decisions
- enemy-front and war-plan focuses create claims, neighbor-war pressure, assault columns, and high-chaos expansion behavior
- hidden-doctrine and extreme-gate focuses directly open the high-chaos road-war expansion package

## Localisation Keys Added

- `AEX_first_guard_tt`
- `AEX_stores_tt`
- `AEX_legitimacy_tt`
- `AEX_rival_tt`
- `AEX_doctrine_tt`
- `AEX_economy_tt`
- `AEX_league_tt`
- `AEX_foreign_tt`
- `AEX_diplomatic_plan_tt`
- `AEX_inner_faction_tt`
- `AEX_special_arm_tt`
- `AEX_supply_tt`
- `AEX_enemy_front_tt`
- `AEX_war_plan_tt`
- `AEX_civil_rule_tt`
- `AEX_propaganda_tt`
- `AEX_settlement_tt`
- `AEX_industry_plan_tt`
- `AEX_hidden_doctrine_tt`
- `AEX_extreme_gate_tt`

## Validation

- Parsed AEX focus tree: 47 focuses.
- AEX duplicate coordinates: none.
- AEX generic custom-splinter tooltip count: 0.
- AEX missing tooltip localisation: none.
- AEX-specific custom tooltip count: 20.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: passed.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: no matches.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` brace balance: 0, minimum balance 0.
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` BOM: `efbbbf`.

## Remaining Gaps

This is one local tranche. Other custom splinter trees still contain generic custom-splinter reward tooltips and need the same kind of country-specific depth pass. The broader objective also still requires release/scenario/evolution/decision-system validation before completion can be claimed.

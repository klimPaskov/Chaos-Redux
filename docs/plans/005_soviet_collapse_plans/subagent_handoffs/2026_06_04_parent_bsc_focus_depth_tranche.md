# Parent Handoff: BSC Focus Depth Tranche

## Scope

This tranche deepened the Basmachi Confederation focus tree inside Event 005 Soviet Collapse. It did not touch flags, country history, sprite files, release logic, scenarios, or other event systems.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Focuses Updated

The following BSC focuses no longer use generic `soviet_collapse_custom_splinter_*_reward_tt` route filler. They now expose BSC-specific reward tooltips and call existing Soviet Collapse mechanics through hidden payloads:

- `BSC_first_guard`
- `BSC_stores`
- `BSC_legitimacy`
- `BSC_rival`
- `BSC_doctrine`
- `BSC_economy`
- `BSC_league`
- `BSC_foreign`
- `BSC_diplomatic_plan`
- `BSC_inner_faction`
- `BSC_special_arm`
- `BSC_supply`
- `BSC_enemy_front`
- `BSC_war_plan`
- `BSC_civil_rule`
- `BSC_propaganda`
- `BSC_settlement`
- `BSC_industry_plan`
- `BSC_hidden_doctrine`
- `BSC_extreme_gate`

## Behavior Before

BSC had 20 focuses that displayed broad route-level reward text such as political, logistics, diplomacy, industry, or high-chaos route rewards. Most of those focuses called generic custom-splinter identity helpers, so the route read as a template rather than a Basmachi road-war country package.

## Behavior After

BSC now ties the affected focuses to concrete existing mechanics:

- caravan guard and raiding-column focuses create assault strength, mobile columns, and Soviet-obedience pressure
- road-store and supply focuses increase depot control, equipment, factory recovery, and supply depth
- legitimacy and civil-rule focuses strengthen recognition, institution strength, resilience, and compact mechanics
- League and foreign-route focuses improve League support, liaison reach, foreign recognition, and deployable League decisions
- enemy-front and war-plan focuses create claims, neighbor-war pressure, assault columns, and high-chaos expansion behavior
- hidden-doctrine and extreme-gate focuses directly open the high-chaos road-war expansion package

## Localisation Keys Added

- `BSC_first_guard_tt`
- `BSC_stores_tt`
- `BSC_legitimacy_tt`
- `BSC_rival_tt`
- `BSC_doctrine_tt`
- `BSC_economy_tt`
- `BSC_league_tt`
- `BSC_foreign_tt`
- `BSC_diplomatic_plan_tt`
- `BSC_inner_faction_tt`
- `BSC_special_arm_tt`
- `BSC_supply_tt`
- `BSC_enemy_front_tt`
- `BSC_war_plan_tt`
- `BSC_civil_rule_tt`
- `BSC_propaganda_tt`
- `BSC_settlement_tt`
- `BSC_industry_plan_tt`
- `BSC_hidden_doctrine_tt`
- `BSC_extreme_gate_tt`

## Validation

- Parsed BSC focus tree: 47 focuses.
- BSC duplicate coordinates: none.
- BSC generic custom-splinter tooltip count: 0.
- BSC missing tooltip localisation: none.
- BSC-specific custom tooltip count: 20.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: passed.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: no matches.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` brace balance: 0, minimum balance 0.
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` BOM: `efbbbf`.
- `git status --short -- gfx/flags interface/flags`: only pre-existing untracked `ZUL` flag files were present.

## Remaining Gaps

This is one local tranche. Other custom splinter trees still contain generic custom-splinter reward tooltips and need the same kind of country-specific depth pass. The broader objective also still requires release/scenario/evolution/decision-system validation before completion can be claimed.

# Parent SDZ Focus Depth Tranche

## Scope

Updated the Security Directorate Zone focus tree rewards in:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

No flag assets were edited.

## Focuses Changed

The following SDZ focuses no longer show generic `soviet_collapse_custom_splinter_*` reward tooltips:

- `SDZ_first_guard`
- `SDZ_stores`
- `SDZ_legitimacy`
- `SDZ_rival`
- `SDZ_doctrine`
- `SDZ_economy`
- `SDZ_league`
- `SDZ_foreign`
- `SDZ_diplomatic_plan`
- `SDZ_inner_faction`
- `SDZ_special_arm`
- `SDZ_supply`
- `SDZ_enemy_front`
- `SDZ_war_plan`
- `SDZ_archive_bunker_vaults`
- `SDZ_civil_rule`
- `SDZ_propaganda`
- `SDZ_settlement`
- `SDZ_industry_plan`
- `SDZ_hidden_doctrine`
- `SDZ_extreme_gate`

## Behavior

Before this tranche, these focuses mostly used shared route identity helpers and broad placeholder tooltips. The tree read like the same political, military, logistics, or diplomacy reward repeated under different names.

After this tranche, the early and mid SDZ branches tie into archive/security mechanics:

- archive control and decryption against `SOV`
- chaos assault and assault-column deployment
- lawful supply, chaos logistics, and depot control
- League security, League logistics, and deployable League unit hooks
- foreign security and foreign recognition hooks
- republican compact and civil-military authority hooks
- neighbor conflict, claims, and high-chaos expansion hooks

The hidden doctrine and extreme gate now push the SDZ hardline route toward assault columns, cores/claims, and neighbor expansion instead of only showing a generic high-chaos tooltip.

## Localisation

Added SDZ-specific reward tooltip keys:

- `SDZ_first_guard_tt`
- `SDZ_stores_tt`
- `SDZ_legitimacy_tt`
- `SDZ_rival_tt`
- `SDZ_doctrine_tt`
- `SDZ_economy_tt`
- `SDZ_league_tt`
- `SDZ_foreign_tt`
- `SDZ_diplomatic_plan_tt`
- `SDZ_inner_faction_tt`
- `SDZ_special_arm_tt`
- `SDZ_supply_tt`
- `SDZ_enemy_front_tt`
- `SDZ_war_plan_tt`
- `SDZ_archive_bunker_vaults_tt`
- `SDZ_civil_rule_tt`
- `SDZ_propaganda_tt`
- `SDZ_settlement_tt`
- `SDZ_industry_plan_tt`
- `SDZ_hidden_doctrine_tt`
- `SDZ_extreme_gate_tt`

## Validation

Ran:

- SDZ parser check: `47` focuses, no duplicate coordinates, no remaining SDZ generic route tooltip lines, no missing new localisation keys.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- Brace balance check on `common/national_focus/005_soviet_collapse_custom_splinters.txt`: balance `0`, minimum balance `0`.
- BOM check on `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: `efbbbf`.
- `git status --short -- gfx/flags interface/flags`: still shows only pre-existing untracked `gfx/flags/ZUL.tga`, `gfx/flags/medium/ZUL.tga`, and `gfx/flags/small/ZUL.tga`.

## Remaining Risks

This was a focused SDZ reward-depth pass. It did not complete the broader user goal:

- Other custom splinter trees still need the same generic-reward audit.
- Republic trees still need full route-depth and layout passes.
- Evolution detail/spreadsheet alignment and decision visibility issues remain separate active work.
- Existing untracked handoffs and broad dirty changes remain in the worktree.

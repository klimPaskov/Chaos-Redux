# Parent Handoff: UDC Focus Depth Tranche

## Scope

This tranche finished the Union Defense Committee cleanup flagged by the focus auditor. It only touched the Event005 custom-splinter focus file and matching English localisation.

No flag assets, interface flag definitions, country history, scenario release logic, or decision files were edited.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Focuses Updated

The following UDC focuses no longer use generic `soviet_collapse_custom_splinter_*_reward_tt` route filler:

- `UDC_doctrine`
- `UDC_economy`
- `UDC_league`
- `UDC_foreign`
- `UDC_diplomatic_plan`
- `UDC_inner_faction`
- `UDC_special_arm`
- `UDC_command_bunker_vaults`
- `UDC_settlement`
- `UDC_extreme_gate`

## Behavior Before

UDC still had ten generic custom-splinter route nodes. Several early branch gateways displayed generic doctrine, industry, League, diplomacy, and political route text. That contradicted the intended UDC identity as a loyalist district-command successor.

## Behavior After

The affected focuses now expose UDC-specific tooltips and connect to existing Soviet Collapse mechanics:

- command doctrine grows the UDC command-network helper, mobile columns, and assault planning
- economy and bunker focuses tie industry to district supply, depot control, command vaults, and command-network depth
- League and foreign focuses route through League-security, foreign-security, and liaison mechanics without implying ordinary patronage
- diplomatic and inner-faction focuses strengthen staff-room recognition, compact progress, and civil-military authority
- special-arm and extreme-gate focuses unlock their matching decisions and deploy high-chaos assault/expansion payloads
- settlement now reinforces recognition and compact strength instead of generic political identity filler

## Localisation Keys Added

- `UDC_doctrine_tt`
- `UDC_economy_tt`
- `UDC_league_tt`
- `UDC_foreign_tt`
- `UDC_inner_faction_tt`
- `UDC_special_arm_tt`
- `UDC_command_bunker_vaults_tt`
- `UDC_settlement_tt`
- `UDC_diplomatic_plan_tt`
- `UDC_extreme_gate_tt`

## Validation

- Parsed UDC focus tree: 47 focuses.
- UDC duplicate coordinates: none.
- UDC generic custom-splinter tooltip count: 0.
- UDC missing tooltip localisation: none.
- UDC-specific custom tooltip count: 22.
- Parsed BSC focus tree after this tranche: 47 focuses, duplicate coordinates none, generic custom-splinter tooltip count 0, missing tooltip localisation none.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_parent_bsc_focus_depth_tranche.md docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_160727_event005_custom_splinter_focus_audit_readonly.md`: passed.
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: no matches.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` brace balance: 0, minimum balance 0.
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` BOM: `efbbbf`.
- `git status --short -- gfx/flags interface/flags`: only pre-existing untracked `ZUL` flag files were present.

## Remaining Gaps

The focus auditor still reports many untouched or lightly touched custom-splinter trees with generic route scaffolds, especially NLC, FEV, ARD, BBH, KRS, GAC, DHC, KHC, SZA, UWD, MRC, IUL, and BAC. Republic-tree layout risks also remain in Ukraine, Central Asia, and Moldova. This tranche does not complete the overall Soviet Collapse focus-tree objective.

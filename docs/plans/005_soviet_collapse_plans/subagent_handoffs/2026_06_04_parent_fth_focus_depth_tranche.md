# Parent Handoff: FTH Focus Depth Tranche

Date: 2026-06-04

## Scope

Parent-side implementation pass for the Free Territory of Huliaipole focus tree in `common/national_focus/005_soviet_collapse_custom_splinters.txt`.

This tranche addresses the audit finding that high-chaos custom-splinter trees still contain generic route scaffolding and do not consistently connect to Soviet Collapse mechanics.

Flags were intentionally not touched.

## Changed Files

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Focuses Changed

- `FTH_first_guard`
- `FTH_stores`
- `FTH_legitimacy`
- `FTH_rival`
- `FTH_doctrine`
- `FTH_economy`
- `FTH_league`
- `FTH_foreign`
- `FTH_inner_faction`
- `FTH_special_arm`
- `FTH_supply`
- `FTH_enemy_front`
- `FTH_civil_rule`
- `FTH_propaganda`
- `FTH_settlement`
- `FTH_war_plan`
- `FTH_diplomatic_plan`
- `FTH_industry_plan`
- `FTH_hidden_doctrine`
- `FTH_extreme_gate`
- `FTH_communes_without_capitals`

## Behavior Before

The FTH tree had useful later branches, but the opening and central route structure still relied on generic `soviet_collapse_custom_splinter_*` reward tooltips and identity helpers. The player saw a broad route label, while the gameplay result was mostly abstract identity progress rather than concrete Free Territory behavior.

## Behavior After

- FTH now has no remaining generic `soviet_collapse_custom_splinter_*` tooltip calls inside its focus tree.
- Opening focuses now create tachanka-style assault columns, seized commune depot logistics, chaos legitimacy, and neighbor pressure.
- Political and civil branches now feed republican compact, civil-military authority, recognition, resilience, and old-movement pressure.
- League and foreign branches now connect to league unit deployment, foreign security, liaison reach, and pressure on Moscow.
- Expansion branches now core controlled territory, create claims and war plans against valid neighbors, and push aggressive AI conquest priorities.
- `FTH_hidden_doctrine`, `FTH_extreme_gate`, and `FTH_communes_without_capitals` now produce high-chaos escalation through assault columns and neighbor expansion instead of remaining mostly generic endpoint text.
- Added FTH-specific tooltip localisation for every replaced reward.

## Validation

- FTH parse audit: 47 focuses, no duplicate x/y coordinates.
- FTH tooltip audit: 21 `FTH_*_tt` custom effect tooltips, no missing localisation keys.
- FTH generic-tooltip audit: no remaining `soviet_collapse_custom_splinter_*` custom effect tooltips inside the FTH focus tree.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- Brace balance check on `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `balance=0`, `min=0`.
- Localisation BOM check on `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: `efbbbf`.
- `git status --short -- gfx/flags interface/flags` returned empty output.

## Remaining Gaps

This is not a completion claim for the full Soviet Collapse goal. Remaining work still includes:

- Full manual depth pass for the other custom-splinter trees that still use generic route scaffolding.
- Broader republic-tree layout review for Ukraine, Belarus, Central Asia, and other audit-flagged trees.
- Full release/evolution/scenario coverage proof for all possible Soviet breakaways and high-chaos successors.
- Decision visibility audit for expanded breakaway decision sections.
- Final focus-tree auditor pass after the remaining implementation tranches.

# Event005 parent focus tooltip and layout tranche

Date: 2026-06-04

Scope:
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

No-touch confirmation:
- No `gfx/flags`, `interface/flags`, flag sprite, or flag definition files were edited.

## Changes

Replaced all remaining focus references to the generic custom-splinter route tooltip in `005_soviet_collapse_custom_splinters.txt`.

Before:
- `custom_effect_tooltip = soviet_collapse_custom_splinter_route_identity_reward_tt`
- One broad tooltip covered legitimacy, depots, recognition, military preparation, construction, assault formations, and claims.

After:
- `soviet_collapse_custom_splinter_political_route_reward_tt`
- `soviet_collapse_custom_splinter_industrial_route_reward_tt`
- `soviet_collapse_custom_splinter_logistics_route_reward_tt`
- `soviet_collapse_custom_splinter_military_route_reward_tt`
- `soviet_collapse_custom_splinter_diplomacy_route_reward_tt`
- `soviet_collapse_custom_splinter_league_route_reward_tt`
- `soviet_collapse_custom_splinter_expansion_route_reward_tt`
- `soviet_collapse_custom_splinter_high_chaos_route_reward_tt`

Focus tooltip counts after replacement:
- Political route: 115
- Industrial route: 40
- Logistics route: 41
- Military route: 38
- Diplomatic route: 38
- League route: 19
- Expansion route: 39
- High-chaos route: 24
- Old generic route tooltip references in the custom-splinter focus file: 0

Added localisation for all eight new tooltip keys in `005_soviet_collapse_custom_countries_l_english.yml`.

Patched remaining audited focus layout problems in `005_soviet_collapse_republics.txt`:
- Generic breakaway route row: moved `soviet_collapse_foreign_liaison_government` and `soviet_collapse_capital_committee_records` so route-choice mutual-exclusion lines no longer run through intervening focuses on the same row.
- Baltic route row: moved `baltic_soviet_collapse_baltic_league_first`, `baltic_soviet_collapse_foreign_protection_council`, and `baltic_soviet_collapse_military_border_government` off the crowded same-row fork pattern.
- Moldova route row: moved `moldova_soviet_collapse_reject_the_union_question` and `moldova_soviet_collapse_conditional_union` off the crowded same-row fork pattern.
- Belarus route row: moved `blr_soviet_collapse_socialist_autonomy_without_moscow`, `blr_soviet_collapse_military_transit_directorate`, and `blr_soviet_collapse_foreign_corridor_administration`; also moved `blr_soviet_collapse_military_transit_directorate` away from a duplicate coordinate.

## Validation

Commands/checks run:
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_republics.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- Unsupported comparison operator scan on the touched focus and localisation files.
- Brace-balance check on the two focus files and localisation file.
- Per-focus-tree coordinate/pathline audit for:
  - duplicate same-tree coordinates
  - same-row mutual-exclusion spans through intervening focus nodes
- BOM checks:
  - `005_soviet_collapse_custom_splinters.txt`: matches existing BOM state.
  - `005_soviet_collapse_republics.txt`: matches existing non-BOM state.
  - `005_soviet_collapse_custom_countries_l_english.yml`: UTF-8 BOM present.

Validation results:
- `git diff --check`: clean.
- Unsupported operator scan: no matches.
- Brace balance: 0 for all checked files.
- Same-tree same-row mutual-exclusion spans through nodes: 0.
- Duplicate same-tree coordinates in checked focus files: 0.
- Each new tooltip key has exactly one localisation definition.

## Remaining gaps

This tranche reduces visible reward-tooltip spam and fixes the audited same-row focus pathline issues in the touched focus files. It does not complete the full Event005 goal.

Remaining broad work:
- Full deep rework of all Event005 focus trees into stronger political, industrial, military, diplomatic, and expansion route families.
- More overpowered and aggressive mechanics for chaos countries.
- Full audit of union-unmade and triggerable-scenario release coverage for all possible Soviet republics, niche republics, special splinters, and Soviet puppets.
- Evolution detail and spreadsheet wording alignment.
- Additional decision and focus hooks for inter-republic expansion and chaos-country neighbor wars.

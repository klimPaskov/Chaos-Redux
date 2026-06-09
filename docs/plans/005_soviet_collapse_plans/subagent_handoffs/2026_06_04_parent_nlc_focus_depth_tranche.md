# Parent Handoff: NLC Focus Depth Tranche

Date: 2026-06-04

## Scope

Cleaned the Northern Lights Committee focus rewards inside `common/national_focus/005_soviet_collapse_custom_splinters.txt` so the tree no longer exposes generic custom-splinter reward text for the audited NLC focus block.

No flag files were edited.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Focuses Updated

The following NLC focuses now use NLC-specific tooltip keys and mechanic-facing reward bundles instead of generic custom-splinter identity text:

- `NLC_first_guard`
- `NLC_stores`
- `NLC_legitimacy`
- `NLC_rival`
- `NLC_doctrine`
- `NLC_economy`
- `NLC_league`
- `NLC_foreign`
- `NLC_diplomatic_plan`
- `NLC_inner_faction`
- `NLC_special_arm`
- `NLC_supply`
- `NLC_enemy_front`
- `NLC_war_plan`
- `NLC_civil_rule`
- `NLC_propaganda`
- `NLC_settlement`
- `NLC_industry_plan`
- `NLC_hidden_doctrine`
- `NLC_extreme_gate`

## Validation

- NLC focus count: 47
- Duplicate NLC coordinates: 0
- Generic custom-splinter tooltips inside NLC focuses: 0
- Missing NLC tooltip localisation: 0
- NLC custom tooltip keys found in NLC focuses: 20
- NLC tooltip keys found outside NLC focuses: 0
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` brace balance: 0, minimum depth: 0
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` BOM: `efbbbf`
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: passed
- Unsupported operator scan for touched files (`<=` / `>=`): no matches
- Flag status check for `gfx/flags` and `interface/flags`: no output

## Notes

An initial broad replacement matched copied focus helper blocks outside NLC. This was corrected with an exact focus-id rewrite. Final validation confirms there are no `NLC_` custom tooltips in non-NLS focuses.

## Remaining Work

The wider Soviet Collapse goal remains incomplete. Remaining open areas include:

- More custom-splinter focus cleanup for generic/shallow reward trees beyond BSC, UDC, and NLC.
- Republic layout and route-depth cleanup, especially Ukraine and other previously reported overlapping pathline areas.
- Evolution detail alignment with spreadsheet wording.
- Dynamic release scaling and high-chaos release behavior across all eligible Soviet breakaways.
- Intervention decision visibility for every dynamic breakaway target.
- Scenario/unit scaling balance and final live-error follow-up.

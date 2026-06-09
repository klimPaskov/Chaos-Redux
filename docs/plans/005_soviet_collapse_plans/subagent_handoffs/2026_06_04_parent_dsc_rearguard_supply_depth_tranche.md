# Event005 Parent DSC Rearguard Supply Depth Tranche

Date: 2026-06-04

## Scope

Parent implementation tranche for the Soviet Collapse focus-depth cleanup.

Touched files:

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

No flag files, `.tga` files, `gfx/flags`, `interface/flags`, or flag sprite definitions were inspected or edited.

## Gameplay Changes

Changed focus:

- `DSC_rearguard_supply_bureau`

Before:

- Called `soviet_collapse_apply_focus_security_supply_plan`.
- Added `dsc_revenant_mobilization`.
- Called `soviet_collapse_apply_focus_chaos_supply_plan`.
- The reward felt like another generic supply packet.

After:

- Calls the new bespoke helper `dsc_soviet_collapse_apply_rearguard_supply_bureau`.
- Unlocks `dsc_mark_the_unfinished_front_roads` directly.
- Uses matched search filters for industry, army, and expansion behavior.
- Adds DSC-specific roll-call and revenant mobilization progress.
- Claims front-road states through the existing DSC front-road payload.
- Builds a rearguard workshop, infrastructure, railway, and supply node in controlled core territory.
- Grants manpower, infantry equipment, support equipment, artillery, army XP, and war support without adding a new idea.
- Spawns a normal mobile column by default; if the Revenant Staff route is active or chaos is tier 4/5, it musters custom-splinter assault columns and applies high-chaos neighbor expansion planning.

Changed decision visibility:

- `dsc_mark_the_unfinished_front_roads` now appears after `DSC_rearguard_supply_bureau`, not only after later map/road focuses.

Localisation added:

- `dsc_rearguard_supply_bureau_tt`

## Why This Is Aligned

This removes one direct example of repeated helper-reward sameness without adding more national-spirit churn. The focus now connects to an existing DSC decision, map claims, infrastructure, unit spawning, and high-chaos aggression, which is closer to the intended overpowered chaos-country identity.

## Validation

Ran scoped validation after the patch:

- `git diff --check` on all touched files: passed.
- Brace balance on all touched files: final depth 0, no early negative depth.
- Unsupported operator scan for `<=` and `>=` on touched files: no matches.
- Localisation file kept UTF-8 BOM.
- Focus block check for `DSC_rearguard_supply_bureau`: 0 calls to `soviet_collapse_apply_focus_security_supply_plan`, 0 calls to `soviet_collapse_apply_focus_chaos_supply_plan`, 1 call to `dsc_soviet_collapse_apply_rearguard_supply_bureau`.
- No flag diff under `gfx/flags` or `interface/flags`.

## Remaining Work

This is not a completion claim. The current focus audit still flags broad Event005 depth gaps, including compact chaos trees under 25 focuses, repeated helper call patterns, many trees with little direct decision integration, search-filter mismatch candidates, and uneven route AI depth.

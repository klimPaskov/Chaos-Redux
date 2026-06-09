# Event005 Parent Tranche: Ancient and High-Chaos Aggression

Date: 2026-06-01

## Scope

This parent tranche follows the focus-tree audit reports for Soviet Collapse focus depth and layout. It keeps flag assets out of scope.

Changed files:

- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`

## What Changed

Ancient restoration focuses now push actual aggressive mechanics instead of ending at generic claim helpers:

- `KZR_expansionist_steppe_levy`
- `KZR_returned_names_endgame`
- `KZR_road_beyond_the_caspian`
- `SOG_expansionist_merchant_claims`
- `SOG_returned_names_endgame`
- `SOG_cities_beyond_the_desert`
- `KHW_expansionist_water_claims`
- `KHW_returned_names_endgame`
- `KHW_delta_without_a_center`
- `ALN_expansionist_mountain_claims`
- `ALN_returned_names_endgame`
- `ALN_every_pass_a_border`

These focuses now call:

- `soviet_collapse_spawn_custom_splinter_assault_columns`
- `soviet_collapse_apply_custom_splinter_expansion_claims`
- `soviet_collapse_apply_high_chaos_neighbor_expansion_plan`

The expansionist route starts also grant a Soviet war goal when valid, so they are no longer only passive old-name/claim payoffs.

The shared high-chaos endgame helpers now also call `soviet_collapse_apply_high_chaos_neighbor_expansion_plan` where they previously stopped at stockpiles, ideas, or claim helpers. This makes high-chaos successors claim/core controlled claimed states and generate wars or war goals against neighboring breakaways through the existing dynamic neighbor expansion helper.

Affected helper families include:

- port council / Kronstadt successor
- black banner and Basmachi successors
- Turkestan and Alash routes
- union defense and security directorate routes
- green army, Don/Kuban host, Far Eastern, Siberian Zemstvo, Ural Workers, Mountain Republic, Idel-Ural
- OGB, Birobidzhan, PRA, TSC, ICD, RMC, DSC, ARD, NLC, NRF endgames

## Cleanup

- Removed ancient focus calls to `soviet_collapse_update_consolidated_republic_ideas` where they were only refreshing consolidated idea state after variable changes. This reduces helper-mediated idea churn in ancient focus rewards.
- Fixed malformed indentation around `KZR_khazar_charter` and `KHW_symbolic_oasis_authority`.
- Preserved the compact ancient symbolic-vs-expansion fork layout while separating the mutually exclusive route choices horizontally.

## Validation

Commands run:

- `git diff --check -- common/national_focus/005_soviet_collapse_ancient_restorations.txt common/scripted_effects/005_soviet_collapse_effects.txt`
- Brace balance checks on both changed files with `awk`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_ancient_restorations.txt common/scripted_effects/005_soviet_collapse_effects.txt`
- `git status --short -- gfx/flags interface/flags common/national_focus/005_soviet_collapse_ancient_restorations.txt common/scripted_effects/005_soviet_collapse_effects.txt`

Results:

- Diff whitespace check passed.
- Both changed files have brace balance `0`.
- No unsupported `<=` or `>=` operators were found in the touched files.
- `gfx/flags` and `interface/flags` remained clean.

## Remaining Gaps

This is not a full completion of the user goal. The focus audits still identify major remaining work:

- Ukraine and Belarus layout/pathline cleanup.
- Full route-depth expansion for 18-focus high-chaos trees.
- More direct mechanics for the 47-focus custom splinter trees.
- Reduced helper/equipment reward repetition across republic and custom splinter focus files.
- Screenshot or in-game layout validation for overlapping pathlines.
- Evolution details and scenario/release systems still need separate verification against the full objective.

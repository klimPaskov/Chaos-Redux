# Event005 Parent Compact Focus Layout Pathline Tranche

## Scope

Continued the Soviet Collapse focus-tree cleanup goal with a compact coordinate/pathline pass. No flag files, `.tga` files, `gfx/flags`, or flag-related sprite files were touched.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`

## Layout Changes

### Ukraine

- Moved `ukr_soviet_collapse_black_sea_port_ledgers` to `x = 31`, `y = 5`.
- Moved `ukr_soviet_collapse_direct_national_claims` to `x = 23`, `y = 7`.
- Moved `ukr_soviet_collapse_the_western_question_cannot_wait` to `x = 27`, `y = 7`.
- Moved `ukr_soviet_collapse_officer_patronage_lists` to `x = 6`, `y = 8`.
- Moved `ukr_soviet_collapse_black_banner_takes_the_villages` to `x = 22`, `y = 13`.

These changes break the exact vertical stack from `ukr_soviet_collapse_army_of_the_republic` through multiple expansion focuses and clear a later black-banner route line.

### Belarus

- `blr_soviet_collapse_a_forest_that_can_govern` now draws only from `blr_soviet_collapse_the_forest_general_staff`; `blr_soviet_collapse_council_bargains_with_forests` remains a required `available` gate.
- `blr_soviet_collapse_brest_is_not_a_gift` now draws only from `blr_soviet_collapse_foreign_aid_through_brest`; `blr_soviet_collapse_every_track_through_minsk` remains a required `available` gate.

This preserves route requirements while removing long cross-branch visual lines through unrelated rail/forest focuses.

### Kazakhstan

- Moved `kaz_soviet_collapse_the_steppe_arsenal` to `x = 23`, `y = 5`.
- Moved `kaz_soviet_collapse_the_steppe_keeps_many_memories` to `x = 32`, `y = 8`.

These keep the industry and political-memory payoffs compact while avoiding line corridors through neighboring route nodes.

### Baltic

- Moved `baltic_soviet_collapse_british_naval_observers` to `x = 20`, `y = 5`.
- Moved `baltic_soviet_collapse_foreign_advisers_under_baltic_law` to `x = 27`, `y = 5`.
- Moved `baltic_soviet_collapse_sponsor_fleet_rights` to `x = 26`, `y = 6`.

This clears same-row overlaps in the foreign-protection/naval-recognition branch.

### Chaos Splinters

- Moved `DHC_convoy_autonomy_guarantees` to `x = 9`, `y = 11`.
- Moved `KHC_grain_passage_guarantees` to `x = 9`, `y = 11`.
- Moved `UWD_industry_plan` to `x = 12`, `y = 10`.
- Moved `ARD_murmansk_dockyard_contracts` to `x = 7`, `y = 14`.
- Moved `NLC_ration_and_signal_escorts` to `x = 13`, `y = 7`.
- Moved `NLC_heated_workshop_contracts` to `x = 11`, `y = 10`.

These clear exact vertical host/corridor lines and obvious NLC/ARD route corridors while keeping the trees compact.

## Mechanical Layout Check

A parent script checked all four Event005 focus files for:

- exact duplicate focus coordinates inside the same focus tree
- simple same-column parent-child lines with another focus directly between them
- simple same-row parent-child lines with another focus directly between them

Result:

- `common/national_focus/005_soviet_collapse_republics.txt`: `0` duplicate coordinates, `0` axis blockers
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `0` duplicate coordinates, `0` axis blockers
- `common/national_focus/005_soviet_collapse_factory_successors.txt`: `0` duplicate coordinates, `0` axis blockers
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`: `0` duplicate coordinates, `0` axis blockers

This does not prove every diagonal focus path is visually perfect in-game, but it removes the mechanically obvious overlap classes that were repeatedly producing ugly lines.

## Validation

- Brace balance clean on all four Event005 focus files.
- `git diff --check` clean on all four Event005 focus files.
- Unsupported operator scan for `<=` and `>=` clean on all four Event005 focus files.
- No flag diffs:
  - `git diff --name-only | rg '(^|/)gfx/flags/|\.tga$|flag.*\.(gfx|dds|tga)$|(^|/)flags/' || true`
  - produced no output.

## Remaining Gaps

- This tranche is a compact layout pass, not the full final focus-tree depth rewrite.
- Diagonal pathline quality still needs visual/game review or a stronger geometric checker.
- Some branches still need deeper identity mechanics and less dense direct reward bundling.

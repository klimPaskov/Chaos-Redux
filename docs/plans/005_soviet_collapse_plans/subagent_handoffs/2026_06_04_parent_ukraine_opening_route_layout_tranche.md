# Parent Tranche Handoff: Ukraine Opening Route Layout Cleanup

## Scope

Bounded Event005 Soviet Collapse focus-tree layout cleanup for the Ukraine tree.

No flag, sprite, gfx, interface, localisation, decision, or scripted-effect files were touched in this tranche.

## Files Changed

- `common/national_focus/005_soviet_collapse_republics.txt`

## Identifiers Changed

- `ukr_soviet_collapse_village_granary_guards`
- `ukr_soviet_collapse_dnieper_workshops`
- `ukr_soviet_collapse_workers_congress_in_kharkiv`
- `ukr_soviet_collapse_coalition_of_three_ministries`
- `ukr_soviet_collapse_rural_deputy_bloc`

## Before

The Ukraine opening and route follow-up area still had several avoidable line risks:

- The grain-ledger industry follow-ups sat far left of their parent lane, making the early emergency trunk draw diagonally across the tree.
- The socialist worker follow-up drifted into the same visual lane as later democratic and military nodes.
- The democratic coalition/rural-deputy follow-ups sat close to the socialist and military branch lanes.

## After

- `ukr_soviet_collapse_village_granary_guards` moved to `x = 15, y = 3`, keeping it under the grain-ledger lane.
- `ukr_soviet_collapse_dnieper_workshops` moved to `x = 12, y = 2`, keeping its two prerequisites near the emergency trunk instead of drawing across it.
- `ukr_soviet_collapse_workers_congress_in_kharkiv` moved to `x = 16, y = 8`, separating it from the military route-lock pair.
- `ukr_soviet_collapse_coalition_of_three_ministries` moved to `x = 14, y = 7`, keeping it closer to the democratic route.
- `ukr_soviet_collapse_rural_deputy_bloc` moved to `x = 14, y = 8`, preserving the democratic follow-up lane without overlapping the military route.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt` passed.
- Brace balance ended at zero for `common/national_focus/005_soviet_collapse_republics.txt`.
- No unsupported `<=` or `>=` operators were found in `common/national_focus/005_soviet_collapse_republics.txt`.
- Parsed the Ukraine tree and confirmed all 83 focus coordinates are unique after this patch.
- `git status --short -- gfx/flags interface/flags` returned no scoped flag changes.

## Remaining Gaps

This is not a complete Ukraine focus-tree rewrite. The current audit still calls for deeper route-specific mechanics, more direct map/diplomacy/war consequences, and further in-game screenshot review because HOI4 can render bent focus paths and mutual-exclusion connectors differently than a straight coordinate parser.

# Event005 Parent Tranche: PRA Corridor Network Reward Cleanup

## Scope

Parent patch for the Soviet Collapse focus-depth goal. Flags were not touched.

## Files changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Identifiers changed

- `PRA_count_the_locomotives`
- `PRA_count_the_locomotives_tt`
- `pra_repair_the_branch_lines`
- `pra_repair_the_branch_lines_tt`

## Behavior before

`PRA_count_the_locomotives` exposed a raw list of rolling-stock variables, railway/infrastructure construction, a supply-node build, and a depot/supply helper. `pra_repair_the_branch_lines` directly displayed multiple railway and infrastructure construction effects without updating the Pale Railway Authority's central railway-state mechanics.

## Behavior after

`PRA_count_the_locomotives` now uses one player-facing tooltip and hides the implementation payload. The payload still inventories rolling stock and builds initial rail/supply infrastructure, but now also starts the existing `soviet_collapse_build_pra_corridor_network` mechanic.

`pra_repair_the_branch_lines` now presents one effect tooltip and hides the implementation payload. It repairs branch lines, extends the corridor network, raises railway authority, and refreshes the existing PRA authority idea through `soviet_collapse_update_pra_authority_idea`.

## Validation

- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt common/decisions/005_soviet_collapse_decisions.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_custom_splinters.txt common/decisions/005_soviet_collapse_decisions.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `python3` brace balance check returned level `0` for all three touched files.
- Localisation BOM check returned `efbbbf`.

## Remaining gaps

This improves the PRA rail identity and reward readability, but it is not the full focus-tree rework. Remaining work includes broader PRA route review, other chaos-country reward dumps, expansion/war payoff depth, layout/pathline blockers, release/scenario verification, and evolution-detail alignment.

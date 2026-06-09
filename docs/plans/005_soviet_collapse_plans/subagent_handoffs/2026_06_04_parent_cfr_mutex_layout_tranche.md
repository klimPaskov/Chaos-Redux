# Event005 parent tranche: CFR mutex layout cleanup

## Scope

Parent-side layout-only cleanup for `CFR_soviet_collapse_focus_tree`.

Files changed:

- `common/national_focus/005_soviet_collapse_factory_successors.txt`

No flag files were touched.

## Problem

The focus audit identified CFR as the worst remaining focus pathline risk. Two choice rows were visually staggered:

- Governance choices were split across y-levels, making mutually exclusive pathlines diagonal.
- Build-priority choices were split across y-levels with follow-up nodes sharing the same row span.

## Changes

Coordinate-only changes:

- `CFR_publish_the_planners_charter`: `(14,5)` -> `(14,6)`
- `CFR_the_concrete_committee`: `(25,5)` -> `(25,6)`
- `CFR_rails_first`: `(12,8)` -> `(12,9)`
- `CFR_contracts_first`: `(22,10)` -> `(22,9)`
- `CFR_client_city_charters`: `(20,10)` -> `(20,11)`
- `CFR_the_debt_map`: `(20,11)` -> `(20,12)`
- `CFR_contracts_with_the_league`: `(26,9)` -> `(26,10)`
- `CFR_the_concrete_republic`: `(28,9)` -> `(28,10)`

No prerequisites, mutual exclusions, rewards, AI weights, or localisation were changed.

## Validation

Commands/checks run:

- `git diff --check -- common/national_focus/005_soviet_collapse_factory_successors.txt`
- brace-depth scan for `common/national_focus/005_soviet_collapse_factory_successors.txt`
- CFR coordinate duplicate scan for the first 47 focuses in the tree
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_factory_successors.txt`
- `git status --short -- gfx/flags interface/flags`

Results:

- no diff whitespace errors
- final brace depth was 0
- no duplicate CFR focus coordinates
- no unsupported `<=` or `>=`
- no flag-folder changes

## Remaining Risk

This is not an in-game render proof. HOI4 pathline bending can still differ from coordinate-only checks, so the CFR tree should be included in the next visual/auditor pass.

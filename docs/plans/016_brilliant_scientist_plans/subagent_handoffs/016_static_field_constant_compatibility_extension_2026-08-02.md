# Event 016 static-field constant compatibility extension

Date: 2026-08-02

## Scope

This bounded continuation replaces shared `constant:` tokens only in Event 016 fields that reject script-constant expansion at load time. It covers sixteen decision files, two scripted-effect files, and three scripted-trigger files. The shared values remain authoritative in `common/script_constants/016_brilliant_scientist*.txt`.

## Implementation

Each touched file declares the file-scoped `@CR_SC_...` values required by its static fields, then uses those macros for the affected modifier, comparison, or timing fields. Existing dynamic fields continue to use `constant:...` tokens. The extension changes no gates, rewards, costs, project stages, routes, receipts, AI choices, event firing, localisation, assets, or model contracts.

The 21 source files contain 162 macro definitions and 451 corresponding static-field substitutions. A parser comparison against all 3,018 Event 016 shared constants returned `macros_checked=162`, `mismatches=0`, and `unmatched=0`. The equipment registry and its helper-gated bonus fields were intentionally not changed.

## Validation

`git diff --check` is clean for the source tranche. The changed source contains no unsupported `<=` or `>=` operators. Brace counts remain balanced for each touched Clausewitz source file. The repository probability inspector was not rerun for this loader-only change because its prior source scan stopped at the workspace byte limit; no campaign or game launch was performed.

## Ownership and remaining risk

The parent owns final staging and any live consumer validation. This tranche is a loader-compatibility repair, not a gameplay expansion and not a completion claim. If a runtime log identifies another field that rejects a shared constant, add a narrowly scoped macro with an equivalence check rather than replacing supported dynamic fields wholesale.

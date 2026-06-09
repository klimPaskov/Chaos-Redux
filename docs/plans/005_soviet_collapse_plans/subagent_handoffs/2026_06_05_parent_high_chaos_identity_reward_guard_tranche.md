# Event005 Parent Tranche: High-Chaos Identity Reward Guard

## Scope

Bounded cleanup for repeated generic focus rewards in Soviet Collapse focus helpers. This tranche does not edit flags or focus layouts.

## Changed Files

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Implementation

- `soviet_collapse_apply_focus_high_chaos_identity` now grants its base manpower, infantry equipment, command power, war support, recognition, and local-authority package only once per country through `soviet_collapse_high_chaos_focus_identity_base_granted`.
- Later focuses that call the same helper still refresh the high-chaos route payload, claims, assault-column/war-package gates, neighbor expansion plan, breakaway neighbor conflict plan, Soviet pressure, and anti-Soviet AI strategy.
- Updated `soviet_collapse_apply_focus_high_chaos_identity_tt` so the tooltip describes a one-time hardening package followed by repeated route-to-war conversion.

## Validation

- Brace-balance check passed for `common/scripted_effects/005_soviet_collapse_effects.txt`.
- Localisation file still has UTF-8 BOM.
- `git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt localisation/english/005_soviet_collapse_l_english.yml` passed.
- `git diff --name-only -- gfx/flags interface/flags` returned no files.

## Remaining Risks

- This removes one central repeated generic high-chaos payoff, but it does not prove the full focus reward cleanup is complete.
- Many focus rewards still call broad helpers and need current audit triage by country/tree.
- The focus auditor subagent spawned on this turn was still running when this parent tranche was recorded.

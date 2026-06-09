# Event005 Parent Tranche: Focus Reward Compacting and Force-All Chaos Scenario

## Scope

- Event: Soviet Collapse (`005_soviet_collapse`)
- Parent-side tranche while `chaosx_focus_tree_auditor` was running.
- Flag assets were not inspected or edited.

## Changed files

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`

## Focus reward cleanup

- `FEV_harbor_fortress_line`
  - Before: the focus exposed a long reward list with XP, convoys, claims, conflict-plan setup, dockyard, naval base, coastal bunkers, anti-air, land fort, and army XP.
  - After: the focus exposes one custom tooltip, `FEV_harbor_fortress_line_tt`, while preserving the actual effects inside `hidden_effect`.
  - Result: the Far Eastern harbor defense focus no longer reads like reward spam, but still grants the same port/rail defense and expansion-plan payload.

## Force-all chaos scenario cleanup

The triggerable Soviet Collapse chaos scenario sets `soviet_collapse_force_all_chaos_successors`, but several `can_soviet_collapse_spawn_*` triggers still enforced live-progression exclusivity or incident gates. This made direct candidate checks inconsistent with the scenario's stated force-all behavior.

Patched trigger families now allow `soviet_collapse_force_all_chaos_successors` to bypass mutually exclusive counterpart blockers and incident flags while preserving normal live progression gates:

- `can_soviet_collapse_spawn_fth`
- `can_soviet_collapse_spawn_bbh`
- `can_soviet_collapse_spawn_bsc`
- `can_soviet_collapse_spawn_khw`
- `can_soviet_collapse_spawn_tnc`
- `can_soviet_collapse_spawn_sog`
- `can_soviet_collapse_spawn_ala`
- `can_soviet_collapse_spawn_mrc`
- `can_soviet_collapse_spawn_aln`
- `can_soviet_collapse_spawn_iul`
- `can_soviet_collapse_spawn_ogb`
- `can_soviet_collapse_spawn_kzr`
- `can_soviet_collapse_spawn_bac`
- `can_soviet_collapse_spawn_ard`
- `can_soviet_collapse_spawn_nrf`

The actual spawn effects already include force-all fallbacks and split several overlapping successor pairs onto different states. This patch aligns the trigger layer with that behavior.

## Validation

- `git diff --check -- common/scripted_triggers/005_soviet_collapse_triggers.txt common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `rg -n "<=|>=" common/scripted_triggers/005_soviet_collapse_triggers.txt common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- Brace-balance check on:
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- UTF-8 BOM check for `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`: `efbbbf`
- `git status --short -- gfx/flags interface/flags` returned no changes.

## Remaining risks

- The focus reward-spam problem is systemic. The current audit still finds hundreds of top-level reward-heavy focuses that should be moved toward route helpers, custom tooltips, and mechanical unlocks.
- Ukraine and several republic/shared trees still need manual pathline review. Heuristic pathline output is noisy because multiple separate focus trees share coordinate grids in the same files, but Ukraine/republic branch overlaps remain credible.
- Full completion still requires an end-to-end audit of release coverage, focus depth, decision unlocks, AI behavior, and player-facing evolution descriptions.

# Event005 Soviet Collapse parent focus reward spam audit tranche

## Scope

- Inspected the four Soviet Collapse focus files:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
- Inspected related reward helpers in `common/scripted_effects/005_soviet_collapse_effects.txt`.
- Did not inspect, edit, or regenerate flags. `gfx/flags` and `interface/flags` remain out of scope.

## Findings

- Direct focus-block scan found no literal duplicate `add_ideas` entries and no focus block with multiple direct `add_ideas`.
- Direct focus-block scan found no repeated stockpile/manpower helper call inside a single focus block.
- The remaining reward spam risk is helper-driven:
  - many focuses call shared reward helpers that surface several same-type effects after helper expansion;
  - old staged idea cleanup still removes many legacy spirits, but current consolidated republic updates mostly use variables and staged cleanup rather than adding several direct spirits;
  - high-chaos/custom-splinter identity payloads still contain repeated same-type equipment, XP, PP, stability, and command-power rewards, often because a single helper handles many country archetypes.
- Concrete duplicate fixed in this tranche:
  - `soviet_collapse_complete_dead_soldiers_endgame` previously granted manpower twice with `chaos_assault_manpower_gain` and `front_manpower`.
  - It now grants one consolidated manpower reward through `constant:soviet_collapse_custom_splinter_payoff.dead_army_endgame_manpower_gain`, preserving the previous total while reducing visible duplicate reward lines.

## Changed files

- `common/script_constants/005_soviet_collapse_constants.txt`
  - Added `dead_army_endgame_manpower_gain = 102000`.
- `common/scripted_effects/005_soviet_collapse_effects.txt`
  - Replaced the two visible manpower grants in `soviet_collapse_complete_dead_soldiers_endgame` with one constant-backed manpower grant.

## Parent follow-up priorities

1. Rewrite helper families that repeatedly add the same type of equipment or XP into single constant-backed rewards where the branches are not true conditional costs.
2. Separate foreign-aid cost aggregation from conditional target scaling so decisions do not display repeated cost lines.
3. Keep the current consolidated republic variable model, but continue retiring old direct staged-idea rewards and cleanup paths.
4. Continue focus-tree layout work through route-by-route audit, because coordinate collision checks across files are noisy when multiple trees share the same coordinate grid.
5. Keep chaos-country focus rewards OP, but express them as fewer stronger mechanics: cores, war plans, dynamic units, claims, decisions, construction packages, and AI aggression instead of repeated stockpile lines.

# Event005 Parent Tranche: DSC Hardline Depth And Focus Reward Visibility

Timestamp: 2026-06-05 06:52 UTC

## Scope

Parent-owned focus-tree tranche for the active Soviet Collapse rework goal.

This pass did not attempt the full requested rewrite of every tree. It made concrete progress on two high-impact problems:

- the Dead Soldiers' Congress hardline branch should behave like a dangerous high-chaos death-state, not a normal republic route
- visible focus rewards should stop exposing stacked generic helper effects when a single route-specific payoff tooltip is clearer

No flag files or flag sprites were touched.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `localisation/english/005_soviet_collapse_l_english.yml`

## Dead Soldiers' Congress Change

`DSC_revenant_staff_line` now has a specific tooltip, `dsc_revenant_staff_line_tt`, and its hardline mechanics run immediately in a hidden effect:

- consolidates the existing dead-army spirit lifecycle through `soviet_collapse_update_dsc_dead_army_idea`
- claims the soldiers' road
- cores controlled soldiers' road states
- spawns assault columns
- adds infantry, support equipment, and artillery
- increases the Dead Soldiers' Congress revenant mobilization variable
- increases Soviet objective pressure against command obedience and republic confidence
- at chaos tier 4 or 5, applies broader splinter expansion claims and prepares dead-army neighbor war orders
- at chaos tier 5, the existing neighbor-war helper can immediately declare through its built-in logic

This uses the existing idea lifecycle instead of adding another national spirit.

## Visible Reward Cleanup

Seven remaining visible generic helper-stack focuses now show one route-specific custom tooltip while the old mechanics run hidden:

- `ukr_soviet_collapse_left_league_delegation`
- `ukr_soviet_collapse_grain_loan`
- `soviet_collapse_the_republic_endures`
- `internal_soviet_collapse_legal_autonomy_congress`
- `internal_soviet_collapse_border_and_rail_liaisons`
- `internal_soviet_collapse_volga_oil_and_workshops`
- `internal_soviet_collapse_volga_ural_compact`

The mechanical scan for visible generic helper stacks dropped from 16 to 9.

Remaining visible generic helper-stack focuses:

- `internal_soviet_collapse_black_sea_compact_observers`
- `internal_soviet_collapse_tuvan_steppe_compact`
- `internal_soviet_collapse_many_republics_common_front`
- `internal_soviet_collapse_no_return_to_oblast_rule`
- `central_asia_soviet_collapse_turkestan_city_congress`
- `central_asia_soviet_collapse_the_south_survives_together`
- `central_asia_soviet_collapse_foreign_border_schools`
- `central_asia_soviet_collapse_desert_republic_settlement`
- `moldova_soviet_collapse_prut_relief_depots`

## Audit Subagent

Spawned fresh focus audit subagent `Ptolemy` with `fork_context=false`.

Subagent scope:

- all Event005 focus files
- idea spam and indirect spirit lifecycle churn
- weak branch depth
- chaos-country aggression
- pathline and mutual-exclusion layout problems
- no flag files or flag sprites

At the time this handoff was written, the subagent was still running.

## Validation

Brace balance passed with zero early closes:

- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `common/national_focus/005_soviet_collapse_ancient_restorations.txt`

Unsupported operator scan:

- `rg -n "<=|>="` returned no hits in the audited Clausewitz files.

Whitespace check:

- `git diff --check` passed for the touched focus and localisation files.

## Remaining Work

- The full focus tree rework is not complete.
- Nine visible generic helper-stack focus rewards remain.
- Kazakhstan remains the known worst current layout hotspot from the prior audit.
- Several chaos country trees still need broader branch depth, especially sustained expansion, country-specific industry, special decisions, and AI aggression.
- Release/scenario/Union Unmade work remains part of the active goal but was not touched in this tranche.

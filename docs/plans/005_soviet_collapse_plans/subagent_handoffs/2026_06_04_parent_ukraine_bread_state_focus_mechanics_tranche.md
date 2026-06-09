# Parent Tranche: Ukraine Bread State Focus Mechanics

Date: 2026-06-04

## Scope

Parent-owned patch while `chaosx_focus_tree_auditor` was running in parallel.

Touched files:

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

Flag files were not inspected or edited.

## Focus IDs Changed

- `ukr_soviet_collapse_question_of_statehood`
- `ukr_soviet_collapse_war_without_a_declaration`
- `ukr_soviet_collapse_black_banner_compact`
- `ukr_soviet_collapse_black_soil_oath`
- `ukr_soviet_collapse_grain_census_of_everyone`
- `ukr_soviet_collapse_no_one_leaves_the_bread_line`
- `ukr_soviet_collapse_last_harvest_plan`

## Behavior

These focuses no longer rely only on visible generic legal, military, high-chaos, or chaos-supply helper rewards.

The new Ukrainian helpers:

- turn statehood into recognition, resilience, local authority, and Soviet breakaway pressure
- make the wartime emergency raise units, add equipment, create or open war with Moscow, and increase Soviet pressure
- make the Black Banner route use one route tooltip while preserving the cosmetic tag change
- make the Bread State route directly update grain authority, coercion, supply buildings, fortifications, manpower, war support, decision unlocks, and old-movement pressure

## New Helper Effects

- `ukr_soviet_collapse_apply_statehood_question_focus`
- `ukr_soviet_collapse_apply_war_without_declaration_focus`
- `ukr_soviet_collapse_apply_black_banner_compact_focus`
- `ukr_soviet_collapse_apply_black_soil_oath_focus`
- `ukr_soviet_collapse_apply_grain_census_focus`
- `ukr_soviet_collapse_apply_bread_line_focus`
- `ukr_soviet_collapse_apply_last_harvest_focus`

## Localisation Keys

- `ukr_soviet_collapse_statehood_question_focus_tt`
- `ukr_soviet_collapse_war_without_declaration_focus_tt`
- `ukr_soviet_collapse_black_banner_compact_focus_tt`
- `ukr_soviet_collapse_black_soil_oath_focus_tt`
- `ukr_soviet_collapse_grain_census_focus_tt`
- `ukr_soviet_collapse_bread_line_focus_tt`
- `ukr_soviet_collapse_last_harvest_focus_tt`

## Validation

- `git diff --check` passed for the touched files.
- Brace balance is clean for the touched files.
- No `<=` or `>=` operators were introduced.
- `localisation/english/005_soviet_collapse_l_english.yml` still begins with UTF-8 BOM `efbbbf`.
- Ukraine focus coordinate audit reports no duplicate coordinates.
- `git status --short -- gfx/flags interface/flags` returned no output.

## Remaining Risks

This is only a Ukraine high-chaos/Bread State tranche. The broader Event005 focus goal remains incomplete until the focus auditor's full cross-tree findings are implemented and rerun.

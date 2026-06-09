# Event005 Parent Tranche: TSC Focus Depth And High-Chaos Guard

## Scope

Parent implementation tranche for the active Soviet Collapse rework.

Flags were explicitly out of scope. No `gfx/flags` or `interface/flags` files were touched.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`

## Gameplay Changes

### Concrete pathline blockers

- `moldova_soviet_collapse_river_guard_brigades`
  - Moved from `x = 12` to `x = 14`.
  - Its prerequisite now comes from the actual route choices, `moldova_soviet_collapse_dniester_defense_directorate` or `moldova_soviet_collapse_independent_republic_council`, instead of drawing a long vertical line from `moldova_soviet_collapse_moldova_route_fork` through `moldova_soviet_collapse_ukrainian_border_compact`.

- `blr_soviet_collapse_join_the_league_when_war_comes`
  - Moved from `x = 19` to `x = 21`.
  - Its prerequisite now routes through `blr_soviet_collapse_quiet_recognition_letters`, avoiding the long vertical line from `blr_soviet_collapse_state_between_armies` through `blr_soviet_collapse_orders_printed_like_timetables`.

### Tunguska Star Committee focus cleanup

Several TSC focuses no longer expose raw flat reward lines as their main player-facing reward. They now use focused custom tooltips and hidden payloads that connect into existing TSC mechanics:

- `TSC_tura_observation_presidium`
  - Opens the observation-post decision surface through the route flag.
  - Advances the observatory network depth.
  - Raises TSC signal authority.
  - Adds Soviet crisis pressure when the Soviet collapse system is active.

- `TSC_kirensk_field_stations`
  - Builds the field-station industry package.
  - Advances field-station depth instead of being only a one-factory reward.

- `TSC_recover_the_burned_glass`
  - Advances both TSC depth tracks.
  - Strengthens high-chaos identity.
  - Keeps the local infrastructure payoff.

- `TSC_portable_laboratory_trains`
  - Keeps its logistics/equipment payoff, but hides it under one route tooltip.
  - Advances field-station depth.

- `TSC_the_committee_of_instruments`
  - Uses a route tooltip instead of showing every raw institutional/decryption reward.
  - Still clears starting tension, opens the observation-post decision, advances observatory depth, and improves recognition/institution variables.

- `TSC_the_committee_of_signs`
  - Uses a route tooltip.
  - Advances both TSC depth tracks.
  - Adds Soviet crisis pressure if the crisis is active.

- `TSC_night_survey_columns`
  - Uses a route tooltip and advances field-station depth.

- `TSC_claim_the_impact_zone`
  - Opens the Starfall Mandate decision path.
  - Advances field-station depth and high-chaos identity.
  - Applies special-splinter expansion claims and high-chaos neighbor expansion planning.

- `TSC_perimeter_regiments`
  - Filters now match its actual payload: army XP, air XP, industry, and manpower.

### High-chaos payload guard

`soviet_collapse_apply_high_chaos_focus_identity_payload` now excludes these special successors from the generic fallback package:

- `soviet_collapse_red_martyrs_successor`
- `soviet_collapse_iron_commissariat_successor`

They already have concept-specific war packages in the same helper, so this prevents stacking the generic high-chaos assault/claim package on top of their bespoke payload.

## Subagent Evidence

The focus audit subagent completed a read-only audit and wrote:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_152920_focus_auditor_event005_soviet_collapse_focus_audit.md`

Key current finding from that audit:

- Direct focus-level `add_ideas`, `add_timed_idea`, `swap_ideas`, `modify_idea`, and `remove_ideas` calls are no longer present in the four Event005 focus files.
- Remaining reward spam is helper-side and design-side: repeated generic route helper/tooltips, flat rewards, under-mechanised route branches, and layout conflicts.

## Validation

Commands run:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt localisation/english/005_soviet_collapse_custom_countries_l_english.yml common/scripted_effects/005_soviet_collapse_effects.txt`
- `rg -n "<=|>=" common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt`
- Brace balance check for:
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
- `xxd -p -l 3 localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `git status --short -- gfx/flags interface/flags`
- `rg -n` lookup for every new `TSC_*_tt` key in both focus and localisation files.

Results:

- `git diff --check` passed.
- No unsupported `<=` or `>=` operators were found in the checked files.
- Brace balance was `0` with no negative balance for all checked script files.
- Localisation file still begins with UTF-8 BOM: `efbbbf`.
- No flag files were listed as modified.
- All new TSC tooltip keys are present in localisation and referenced from the focus file.

## Remaining Gaps

This tranche does not complete the full focus-tree rework. The next priorities from the audit are:

- Replace repeated generic route tooltip/helper usage in the 47-focus custom splinter scaffolds.
- Add decision families and concept-specific payoffs to UDC, FTH, BBH, KRS, SDZ, GAC, DHC, KHC, FEV, SZA, UWD, MRC, IUL, and BAC.
- Patch the concrete Ukraine, Belarus, Moldova, Central Asia, internal republic, and UDC pathline/spacing blockers.
- Review helper-side staged idea updates so focus rewards do not feel like repeated idea churn even when direct focus-level `add_ideas` is gone.

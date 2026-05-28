# Event 005 Sidecar Decision Category Tooltip Verification

Date: 2026-05-28

## Scope

- Role: decision and mission subagent.
- Inspected files: `common/decisions/005_soviet_collapse_decisions.txt`, `common/decisions/categories/005_soviet_collapse_categories.txt`, and `localisation/english/005_soviet_collapse_l_english.yml`.
- Constraint honored: no balance scripted effects/constants, focus files, assets, flags, portraits, music, or unrelated dirty worktree changes were touched.
- Result: no narrow gameplay or localisation patch was needed; this pass adds verification evidence only.

## Issue List

- Critical: none found.
- High: none found. The scoped decision/category/localisation files do not contain the forbidden literal `current values` label.
- Medium: none found for the requested category fix. `soviet_collapse_breakaway_category_desc` already exposes live breakaway pressures, League formation costs, and formation thresholds.
- Low: `soviet_collapse_regional_faction_category_desc` is intentionally shorter than the Breakaway Emergency description, but it still exposes its own regional cohesion/tension values. No patch was made because the reported issue targets the breakaway emergency/category League-value surface.

## Decision Category Lifecycle Notes

- `soviet_collapse_breakaway_category` is visible for breakaway countries while `is_soviet_collapse_aftermath_active = yes` and `is_soviet_collapse_breakaway_country = yes`.
- `visible_when_empty = yes` keeps the category description visible even when no immediate breakaway action row is available.
- `soviet_collapse_regional_faction_category` reveals for regional faction leaders/members or countries that can found Baltic, Caucasus, or Central Asian leagues.
- `soviet_collapse_ukrainian_league_category` reveals through `has_ukr_soviet_collapse_league_decision_surface = yes`.

## Mission Quality Notes

- Owner: Event 005 Soviet Collapse breakaway and League sidecar surfaces.
- Category: primarily `soviet_collapse_breakaway_category`, with spot checks for `soviet_collapse_regional_faction_category` and `soviet_collapse_ukrainian_league_category`.
- Region: former Soviet breakaway republic and regional compact surfaces.
- Requirement: checked breakaway action requirements use `custom_trigger_tooltip` plus hidden triggers instead of exposing raw trigger blocks.
- Duration: inspected breakaway action rows are cooldown decisions, not timed missions. Existing cooldown constants remain unchanged.
- Success/failure: no effects changed; existing completion helpers and player-facing effect tooltips remain in place.
- Duplicate risk: no decision, category, mission, or localisation id was added or duplicated by this pass.

## Cost And Requirement Clarity Notes

- `soviet_collapse_breakaway_category_desc` displays live values for `soviet_collapse_league_support_strength`, `soviet_collapse_recognition_progress`, `soviet_collapse_depot_control`, `soviet_collapse_independence_resilience`, and `soviet_collapse_local_authority_pressure`.
- The same description displays Moscow-side live values for Union Crisis Threat, Armed Breakaway Momentum, League Cohesion, Foreign Penetration, failed Soviet objectives, and active breakaway count.
- The same description displays League formation costs through `soviet_collapse_league_found_pp_cost` and `soviet_collapse_league_found_cp_cost`.
- The same description displays formation thresholds through `soviet_collapse_league_member_gate`, `soviet_collapse_league_recognition_gate`, `soviet_collapse_league_threat_gate`, `soviet_collapse_league_foreign_gate`, and `soviet_collapse_league_failed_objective_gate`.

## AI Validity And Route-Lock Notes

- No AI weights, targets, route locks, or formable requirements were changed.
- The inspected categories have visible gates tied to breakaway status, regional faction status, or route-surface flags.
- No dead-target, closed-route, or disabled-evolution issue was found in the requested tooltip/category surface.

## Localisation And Tooltip Gaps

- No scoped UI source contains the literal `current values` label.
- `localisation/english/005_soviet_collapse_l_english.yml` remains UTF-8 with BOM; it was not edited.
- Breakaway Emergency text already exposes the requested dynamic League coordination, formation cost, member gate, and pressure threshold values.

## Cleanup And Exploit-Risk Notes

- No cleanup hook, cooldown, cost, unit, war goal, core, or equipment effect was changed.
- No new exploit surface was introduced because this was an evidence-only verification pass.
- Existing repeatable breakaway actions retain their existing cooldowns and cost text.

## Concrete Recommended Fixes

- No immediate patch is recommended for the requested tooltip/category issue.
- If a future UX pass wants shorter category descriptions, split the dense Breakaway Emergency explanation into scripted localisation or separate informational decisions; that is broader than this sidecar task.

## Changed Files

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_sidecar_decision_category_tooltip_verification.md`

No decision, category, gameplay localisation, scripted GUI, focus, asset, flag, portrait, music, balance, scripted effect, or script constant file was changed.

## Checked Identifiers

- Categories: `soviet_collapse_breakaway_category`, `soviet_collapse_regional_faction_category`, `soviet_collapse_ukrainian_league_category`, `soviet_collapse_idel_ural_league`.
- Localisation keys: `soviet_collapse_breakaway_category`, `soviet_collapse_breakaway_category_desc`, `soviet_collapse_regional_faction_category_desc`, `soviet_collapse_ukrainian_league_category_desc`.
- Display helper evidence only: `soviet_collapse_set_breakaway_category_display_values`.

## Before And After Behavior

- Before: scoped Event 005 decision/category UI text already avoided the literal `current values` label and exposed the requested Breakaway Emergency dynamic values.
- After: no gameplay or localisation behavior changed; this handoff records the verification.

## Validation Run

- `rg -n -i "current[ _-]?values|current values" common/decisions/005_soviet_collapse_decisions.txt common/decisions/categories/005_soviet_collapse_categories.txt localisation/english/005_soviet_collapse_l_english.yml` returned no matches.
- `rg -n "soviet_collapse_(league_support_strength|recognition_progress|depot_control|independence_resilience|local_authority_pressure|league_found_pp_cost|league_found_cp_cost|league_member_gate|league_recognition_gate|league_threat_gate|league_foreign_gate|league_failed_objective_gate)" common/decisions/005_soviet_collapse_decisions.txt common/decisions/categories/005_soviet_collapse_categories.txt localisation/english/005_soviet_collapse_l_english.yml common/scripted_effects/005_soviet_collapse_effects.txt common/scripted_triggers/005_soviet_collapse_triggers.txt common/script_constants/005_soviet_collapse_constants.txt` confirmed the localisation references and existing helper evidence.
- `file -bi localisation/english/005_soviet_collapse_l_english.yml` reported `text/plain; charset=utf-8`, and `xxd -g1 -l 8 localisation/english/005_soviet_collapse_l_english.yml` showed `ef bb bf`.

## Skipped Validation

- No in-game validation was run.
- Full Event 005 parser/load validation was not run because this was a bounded tooltip/category verification in a heavily dirty worktree and no script source was edited.
- Balance validation was skipped by explicit task constraint.

## Remaining Risk

- Existing display variables are populated by the existing breakaway setup helper. I did not alter helper call sites because scripted effects/constants were outside scope.

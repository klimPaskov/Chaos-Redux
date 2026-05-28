# Event 005 Release Risk And Breakaway Tooltip Handoff

## Scope

- Role: decision and mission subagent.
- Surface inspected: Event 005 decision categories, Breakaway Emergency category localisation, release-risk visibility decision, scripted display-value helper evidence, and clean merged specs under `tmp/soviet_collapse_final_clean_merged_spec_package/specs/`.
- Parent constraint honored: bounded decision/category cleanup only. No MTTH, balance source, scripted trigger, scripted effect, focus, event, asset, or AI source edits were made.
- Worktree note: the repo was already heavily dirty before this pass. Existing edits in Event 005 files and existing handoffs were not reverted or normalized.

## Issue List

- Critical: none found.
- High: none found. `soviet_collapse_breakaway_category_desc` already exposes the requested Breakaway Emergency dynamic values and does not show the old literal `current values` or `Republic ledger` label.
- Medium: `soviet_collapse_review_republic_release_risk_desc` still used the technical phrase `current MTTH release state` in a decision description. This was patched because it is player-facing decision tooltip text and the fix is localisation-only.
- Low: the release-risk ledger remains dense and still shows latest release weights, family candidate pools, and family weights. This was left in place because the decision is explicitly a non-clickable Soviet crisis ledger, and removing the ledger data would be broader design cleanup.

## Decision Category Lifecycle Notes

- `soviet_collapse_breakaway_category` is visible for breakaway countries while `is_soviet_collapse_aftermath_active = yes` and `is_soviet_collapse_breakaway_country = yes`.
- `visible_when_empty = yes` is present, so the Breakaway Emergency description remains available as the explanatory board even during cooldown or target gaps.
- `soviet_collapse_soviet_category` hosts `soviet_collapse_review_republic_release_risk`, a disabled informational ledger decision visible to `SOV` during the active collapse.

## Mission Quality Notes

- Owner: Event 005 Soviet Collapse.
- Category: `soviet_collapse_breakaway_category` for breakaway republic guidance; `soviet_collapse_soviet_category` for the release-risk ledger decision.
- Region: former Soviet republic and collapse-release surface.
- Requirement: no requirement or trigger logic was changed. The inspected release-risk decision is visible to the Soviet Union during the active collapse and unavailable by design through `available = { always = no }`.
- Duration: no mission duration was changed. The release-risk ledger is not a timed mission.
- Success: no success effect was changed.
- Failure: no failure effect was changed.
- Duplicate risk: no decision or mission id was added or duplicated.

## Cost And Requirement Clarity Notes

- `soviet_collapse_breakaway_category_desc` displays the category-introduced dynamic pressures: League Coordination, Recognition Progress, Depot Control, Independence Resilience, and Local Authority Pressure.
- The same category description displays dynamic League formation values: `soviet_collapse_league_found_pp_cost`, `soviet_collapse_league_found_cp_cost`, `soviet_collapse_league_member_gate`, `soviet_collapse_league_recognition_gate`, `soviet_collapse_league_threat_gate`, `soviet_collapse_league_foreign_gate`, and `soviet_collapse_league_failed_objective_gate`.
- The display variables are populated by existing helper lines in `common/scripted_effects/005_soviet_collapse_effects.txt` under `soviet_collapse_set_breakaway_category_display_values`. That helper was evidence only in this pass.
- The release-risk decision description no longer says `current MTTH release state`; it now says the ledger tracks republic release pressure before another republic appears.

## AI Validity And Route-Lock Notes

- No AI weights, route locks, or target checks were changed.
- `soviet_collapse_review_republic_release_risk` has `ai_will_do = { base = 0 }`, matching its disabled ledger role.
- No dead target, disabled evolution, closed route, impossible border, or unsafe formable issue was found in the inspected tooltip/category wording surface.

## Localisation And Tooltip Gaps

- Changed localisation key: `soviet_collapse_review_republic_release_risk_desc`.
- Verified localisation key: `soviet_collapse_breakaway_category_desc`.
- The Breakaway Emergency description currently preserves the dynamic values introduced by the category.
- The scoped scan found no remaining `current values`, `current value`, `current MTTH release state`, or `Republic ledger` text in the inspected Event 005 decision/category localisation and decision files.
- Localisation file BOM for `localisation/english/005_soviet_collapse_release_visibility_l_english.yml` remains `efbbbf`.

## Cleanup And Exploit-Risk Notes

- No cleanup hooks, cooldowns, costs, effects, or AI behavior were changed.
- No exploit surface was introduced because the patch only changes player-facing wording.
- Existing release-risk ledger values are still visible because the decision is informational; broader removal or reclassification would need parent design direction.

## Concrete Recommended Fixes

- Completed: removed technical `current MTTH release state` wording from `soviet_collapse_review_republic_release_risk_desc`.
- No further narrow fix is recommended for `soviet_collapse_breakaway_category_desc`; it already satisfies the requested dynamic category-value behavior.
- Remaining optional follow-up: if the parent wants fewer live ledger numbers in disabled informational decisions, audit `soviet_collapse_review_republic_release_risk_desc` separately as a broader release-visibility UX pass.

## Changed Files

- `localisation/english/005_soviet_collapse_release_visibility_l_english.yml`
- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_release_risk_breakaway_tooltip_current_values_handoff.md`

## Before And After Behavior

- Before: `soviet_collapse_review_republic_release_risk_desc` said the ledger showed the `current MTTH release state` and used `currently satisfy` in the candidate explanation.
- After: the same decision description says it tracks republic release pressure, and the candidate explanation says the republics satisfy the candidate rules. The displayed dynamic values and all gameplay behavior are unchanged.
- Before and after for `soviet_collapse_breakaway_category_desc`: no gameplay or text change in this pass. It already shows League coordination/member gates, formation costs, recognition/foreign/failed-objective thresholds, and the other category pressures.

## Validation

- `rg -n "current values|current value|current MTTH release state|Republic ledger" localisation/english/005_soviet_collapse_l_english.yml localisation/english/005_soviet_collapse_release_visibility_l_english.yml common/decisions/005_soviet_collapse*.txt common/decisions/categories/005_soviet_collapse_categories.txt common/scripted_localisation/005_soviet_collapse_scripted_localisation.txt` returned no matches.
- `rg -n "League Coordination|Recognition Progress|Depot Control|Independence Resilience|Local Authority Pressure|soviet_collapse_league_found_pp_cost|soviet_collapse_league_found_cp_cost|soviet_collapse_league_member_gate|soviet_collapse_league_recognition_gate|soviet_collapse_league_threat_gate|soviet_collapse_league_foreign_gate|soviet_collapse_league_failed_objective_gate" localisation/english/005_soviet_collapse_l_english.yml common/scripted_effects/005_soviet_collapse_effects.txt common/script_constants/005_soviet_collapse_constants.txt` confirmed the Breakaway Emergency category description and existing display helper evidence.
- `xxd -p -l 3 localisation/english/005_soviet_collapse_release_visibility_l_english.yml` returned `efbbbf`.
- `git diff --check -- localisation/english/005_soviet_collapse_release_visibility_l_english.yml localisation/english/005_soviet_collapse_l_english.yml common/decisions/categories/005_soviet_collapse_categories.txt common/decisions/005_soviet_collapse_release_visibility_decisions.txt` passed.

## Skipped Validation

- Full game load was not run because this was a bounded localisation/decision-category cleanup in a dirty worktree.
- Script parser validation and brace checks were not run because no script file was edited.
- MTTH and balance validation were skipped by parent constraint.

## Remaining Gaps

- The release-risk ledger remains intentionally data-heavy. It no longer uses the forbidden/technical wording found in this pass, but a future UX pass could decide whether a disabled decision should expose fewer latest-weight values.
- Broader Event 005 decision readiness tooltips are still dense in places. They were outside this narrow Breakaway Emergency/category and release-risk wording pass.

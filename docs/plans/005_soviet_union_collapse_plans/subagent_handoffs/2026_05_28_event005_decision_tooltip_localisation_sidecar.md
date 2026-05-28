# Event 005 Decision Tooltip Localisation Sidecar

Date: 2026-05-28

## Scope

Bounded audit for Soviet Collapse decision/category localisation and decision tooltip defects only.

Inspected primary files:

- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `localisation/english/005_soviet_collapse_l_english.yml`

Read only for source design/context:

- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_3_decisions_missions_influence.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_4_releases_leagues_union_unmade.md`

## Issues

1. High: none found in the scoped source files. The exact forbidden player-facing labels are absent from Event 005 decision/category script and the main Event 005 English localisation file.
2. Medium: none requiring a gameplay or localisation patch. `soviet_collapse_breakaway_category_desc` already exposes League Coordination, Recognition Progress, Depot Control, Independence Resilience, Local Authority Pressure, League formation political/command costs, same-region member quorum, regional membership examples, and pressure gates.
3. Low: the Breakaway Emergency category description is dense, but still directly relevant and player-facing. No wording-only rewrite was made because the current text already satisfies the bounded request and the worktree contains active edits from other agents.

## Lifecycle Notes

- Owner/category: breakaway republic player countries, `soviet_collapse_breakaway_category`.
- Reveal: category is visible for `is_soviet_collapse_aftermath_active = yes` and `is_soviet_collapse_breakaway_country = yes`.
- Lifecycle risk: no hidden-without-reveal issue found in the scoped category definition.
- Route-lock risk: no route-lock patch needed for this localisation-only request.

## Mission Quality Notes

- Owner: breakaway republics and Soviet crisis board, where relevant.
- Category: no mission definitions were changed.
- Region/requirement/duration/success/failure/duplicate risk: outside this sidecar's write scope except where tooltip wording would expose forbidden labels. The scoped phrase scan found no such mission tooltip text in `005_soviet_collapse_l_english.yml` or `005_soviet_collapse_decisions.txt`.

## Cost And Requirement Clarity

- Breakaway emergency category text states that emergency decisions spend local stability, political capital, command channels, army experience, fuel, manpower, and support stores on the relevant decision rows.
- League formation text exposes dynamic political and command power costs via `soviet_collapse_league_found_pp_cost` and `soviet_collapse_league_found_cp_cost`.
- Formation gates expose dynamic values for member quorum, recognition pressure, crisis or momentum pressure, foreign pressure, and failed Soviet objective pressure.

## AI Validity And Route Locks

- No AI weights or target checks were patched.
- No dead-target, disabled-evolution, closed-route, or formable issue was identified inside the bounded tooltip/localisation request.

## Localisation And Tooltip Gaps

- No exact forbidden label remains in the scoped decision/category/localisation files.
- `localisation/english/005_soviet_collapse_l_english.yml` already has a UTF-8 BOM.
- The category description uses player-facing crisis language and does not describe implementation history.

## Cleanup And Exploit Risk

- No cleanup hook, cooldown, equipment farming, war-goal spam, core spam, or free-unit loop was changed or newly identified in this bounded text audit.
- Existing decision cooldowns and costs were not modified.

## Concrete Recommended Fixes

- No source patch recommended for the bounded request.
- Keep `soviet_collapse_breakaway_category_desc` as the active category explanation unless a later UX pass chooses to split dense category text into additional scripted localisation.

## Changed Files

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_decision_tooltip_localisation_sidecar.md`

No decision, category, scripted GUI, event, focus, MTTH, asset, flag, portrait, or gameplay file was changed.

## Changed Identifiers

- None.

## Before And After

- Before: scoped files already avoided the forbidden decision tooltip labels and the Breakaway Emergency description already showed dynamic League and formation values.
- After: no gameplay/localisation behavior changed; the audit result is recorded for parent review.

## Validation Run

- Required wiki/context reading: AGENTS.md, `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, offline wiki pages for decisions, localisation, triggers, effects, modifiers, scopes, data structures, on actions, event modding, idea modding, and AI modding; vanilla trigger/effect documentation and vanilla Soviet decision/category precedent.
- Spec spot-check: clean merged Soviet Collapse parts 3 and 4 for decision cost-localisation and league-formation requirements.
- `git diff --check -- common/decisions/005_soviet_collapse_decisions.txt common/decisions/categories/005_soviet_collapse_categories.txt localisation/english/005_soviet_collapse_l_english.yml docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_decision_tooltip_localisation_sidecar.md` returned clean.
- `rg -n "<=|>=" common/decisions/005_soviet_collapse_decisions.txt common/decisions/categories/005_soviet_collapse_categories.txt localisation/english/005_soviet_collapse_l_english.yml` returned no matches.
- Exact scoped phrase scan across Event 005 decision/localisation source surfaces returned no matches.
- Localisation BOM check: `localisation/english/005_soviet_collapse_l_english.yml` starts with `EF BB BF`.

## Skipped Validation

- No in-game validation run; this sidecar made no gameplay or localisation source edits.
- No full event validation; outside bounded request.

## Remaining Issues

- None for the requested tooltip/localisation defect.
- Broader decision density, mission balance, and route coverage questions remain owned by the parent Event 005 implementation and existing broader audits.

# Event005 Documentation Curator Handoff: Full Documentation Cleanup

Date: 2026-06-05
Role: `chaosx_documentation_curator`
Scope: documentation-only cleanup for Event005 Soviet Collapse.

This is not an Event005 completion claim. Event005 remains incomplete and in urgent playability cleanup.

## Files Changed

This refresh touched exactly:

- `docs/events/005_soviet_collapse.md`
- `docs/plans/005_soviet_collapse_plans/documentation_state.md`
- `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_full_event005_cleanup.md`

Earlier documentation-curator cleanup in the same dirty worktree also included:

- `docs/events/005_soviet_collapse.md`
- `docs/plans/005_soviet_collapse_plans/documentation_state.md`
- `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_full_event005_cleanup.md`

No gameplay, localisation, scripted effect, scripted trigger, decision, focus, GUI/GFX, asset, spreadsheet, Event006, or flag files were edited.

## What Changed

- Reframed `docs/events/005_soviet_collapse.md` as a compact current overview and evidence router, not a blanket replacement for older handoffs.
- Added an explicit incomplete-status note and urgent playability priorities to the event overview.
- Added existing-country focus-tree eligibility as a current validation target. Current script evidence uses `soviet_collapse_event_created_republic` gating, but that is not treated as final proof.
- Removed implementation-history phrasing from the current overview's Dead Soldiers' Congress and Civilian Factory of Russia route summaries.
- Replaced stale legacy-doc wording that implied older Markdown bodies were removed with source-map routing: accepted, queued, superseded, or contradicted.
- Added an urgent playability resume packet to `documentation_state.md`: release pacing, Union Unmade sanity, focus layout, reward quality, intervention visibility, existing-country focus-tree eligibility, and no flag touching.
- Expanded `source_of_truth_map.md` with accepted current docs, queued docs/evidence, superseded findings, and known contradictions.
- Added spreadsheet follow-up notes to `source_of_truth_map.md` and `documentation_state.md`.
- Added active June 5 no-flag/no-asset scope notes to spec parts 6 and 7 while preserving their final-validation requirements.

## Spreadsheet Follow-Up

`docs/spreadsheets/chaos_redux_events_catalog.xlsx` was inspected as an `.xlsx` zip/XML package only. It was not edited because `openpyxl` is not installed in this environment and the workbook is already dirty in the parent worktree.

Exact workbook row found:

- Sheet: `Main Sheet`
- Row: `6`
- Columns: `A` ID, `B` Event Name, `C` Details, `D` Evo I, `E` Evo II, `F` Evo III, `G` Evo IV, `H` Evo V, `I` Evo VI, `J` World-End Scenario, `K` Type, `L` Status

Required safe updates for the spreadsheet doc worker:

- `L6`: replace `To Be Reworked` with `In progress`.
- `F6`: replace the current Chaos Tier text that says Union Unmade begins at Chaos Tier with: `Chaos Tier: High-chaos successor pressure can enter the progressive pool when severe crisis pressure exists. Ordinary progression stays pressure-gated; Union Unmade remains a terminal outcome, not a tier-only stage.`
- `G6`: replace the current Terminal Rupture text with: `Terminal Rupture: Union Unmade releases ordinary base republics, frees Soviet republican subjects, runs current-tier internal and niche passes, and performs all-possible former-Union core sweeps. Terminal and maximum-intensity scenario paths can escalate breakaway neighbor wars into a full rupture.`
- `H6`: keep the high-chaos successor mutation concept, but ensure it says only the first qualifying high-chaos successor records the actor-linked evolution entry.
- `I6`: if the workbook keeps a separate extreme-successor note, use: `Extreme Successor Mutation: at maximum collapse pressure, fringe and special successor authorities can also break away. The entry marks the first qualifying extreme successor without duplicating every later report.`

Do not mark spreadsheet parity complete until the in-game event-detail/evolution-detail localisation is compared to these cells and a spreadsheet doc worker handoff records the exact match.

## Source-Of-Truth Map Result

Accepted current docs:

- `docs/events/005_soviet_collapse.md`
- `docs/plans/005_soviet_collapse_plans/documentation_state.md`
- `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`
- seven source specs under `docs/specs/005_soviet_collapse_specs/`, read through the current no-flag urgent-playability constraint

Queued evidence:

- focus-depth backlog in `2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`
- current post-CFR audit baseline in `2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md`
- event-detail/evolution-detail/spreadsheet parity notes
- spec part 7 asset and flag requirements as final-validation scope only

Superseded findings:

- older low-threat release-floor wording
- older coordinate and route-lock findings replaced by later June 5 patches
- pre-CFR focus baselines replaced by the post-CFR focus audit for current focus-risk counts

Known contradictions preserved for parent handling:

- live releases are staged and pressure-gated, while terminal/max/scenario rupture paths can be exhaustive
- flags remain final-validation requirements but are no-touch under the active user correction
- Event005 has completed tranches, but the event and focus-tree goal are not complete
- existing-country focus-tree replacement needs validation before completion claims
- selected-breakaway intervention visibility remains a dynamic bug target

## Validation

- `git diff --check -- docs/events/005_soviet_collapse.md docs/plans/005_soviet_collapse_plans/documentation_state.md docs/plans/005_soviet_collapse_plans/source_of_truth_map.md docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
  - Result: passed with no output.
- `git diff --check --no-index /dev/null docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_full_event005_cleanup.md`
  - Result: no whitespace errors.
- `rg -n '[[:blank:]]$' docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_full_event005_cleanup.md`
  - Result: no matches.
- `git diff --name-only -- gfx/flags`
  - Result: no output.
- `python3` stdlib `.xlsx` XML inspection for `docs/spreadsheets/chaos_redux_events_catalog.xlsx`
  - Result: Event005 row found on `Main Sheet` row `6`; `L6` still reads `To Be Reworked`; no workbook edit was made.
- `python3` with `openpyxl`
  - Result: failed because `openpyxl` is not installed. The workbook was left untouched.
- Marker check:
  - `rg -n 'This overview is not a completion report|Event005 remains incomplete|Urgent Playability Resume Packet|Doc Disposition Summary|Accepted Current Docs|Queued Docs|Superseded Current-State Findings|Known Contradictions|soviet_collapse_event_created_republic|no active work|do not edit `gfx/flags`|final-validation requirements' ...`
  - Result: found the expected incomplete-status, disposition-map, queued/superseded/contradiction, event-created focus-tree gating, and no-flag/final-validation markers.
- Implementation-history wording check:
  - `rg -n '\bnow\b|\bnewly\b|\breworked\b|\badded\b|\bchanged\b|\bcurrent implementation problem\b|no longer' docs/events/005_soviet_collapse.md docs/plans/005_soviet_collapse_plans/documentation_state.md docs/plans/005_soviet_collapse_plans/source_of_truth_map.md docs/specs/005_soviet_collapse_specs/*.md docs/plans/005_soviet_collapse_plans/*.md`
  - Result: remaining matches are either player-facing sample text (`now test`) or implementation/status/legacy-plan contexts; the current event overview no longer uses `now` for DSC/CFR route summaries.

## Remaining Risks

- No gameplay audit was performed by this documentation curator pass.
- No spreadsheet or in-game parity validation was performed.
- Spreadsheet row 6 requires the cell-level follow-up listed above before parity can be claimed.
- The post-CFR focus audit still reports 520 pathline risks and 1,127 helper-only or nearly helper-only reward findings; those are implementation work, not documentation cleanup.
- Existing-country focus-tree eligibility is documented as a validation priority, not proven complete.
- Flag and asset work remains closed unless the user explicitly reopens it.
- This pass did not commit because the repository contains many unrelated dirty Event005/Event006/gameplay/asset changes, and committing would risk bundling unrelated work.

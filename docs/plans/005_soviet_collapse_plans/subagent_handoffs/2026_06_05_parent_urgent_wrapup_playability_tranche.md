# Event005 Parent Urgent Wrap-Up Playability Tranche

Date: 2026-06-05

## Scope

This tranche focused on urgent runtime and visibility issues needed to keep Soviet Collapse playable while avoiding a risky late full-tree rewrite.

## Gameplay Changes

- `common/scripted_effects/005_soviet_collapse_effects.txt`
  - Live `soviet_collapse_apply_terminal_collapse` no longer calls the exhaustive all-possible core-country release at calm and low chaos.
  - Union Unmade still releases ordinary republics and frees Soviet subjects.
  - Internal republic terminal release is now explicitly gated to chaos tier 3+.
  - Chaos tier 4+ still spawns terminal high-chaos successors.
  - Chaos tier 5 still enables force-all chaos successors and exhaustive possible-country release.
  - The standalone triggerable scenario path was left forceful and standalone.

- `common/national_focus/005_soviet_collapse_republics.txt`
  - Removed duplicate coordinates in the priority republic trees.
  - Ukraine coordinate audit after patch: 0 duplicate positions, 13 remaining crossing candidates.
  - Belarus coordinate audit after patch: 0 duplicate positions, 31 remaining crossing candidates.
  - Kazakhstan coordinate audit after patch: 0 duplicate positions, 50 remaining crossing candidates.
  - Targeted compact coordinate fixes were applied to Ukraine early trunk, Ukraine late bread-state/high-chaos lanes, Belarus rail/green lane separation, and Kazakhstan duplicated resource nodes.

## Confirmed Existing Safeguards

- Foreign patron intervention category and decisions already require `is_soviet_collapse_foreign_patron_candidate`.
- That trigger excludes SOV, countries at war with SOV, breakaway countries, event-created republics, high-chaos successors, Union Unmade, terminal collapse, and disabled triggerable-scenario systems.
- Terminal setup only loads Event005 custom focus trees when `soviet_collapse_event_created_republic` is set, so already-existing map countries do not receive custom trees from the terminal finalize pass.
- Breakaways already call `soviet_collapse_apply_breakaway_neighbor_conflict_plan` during terminal setup and high-chaos startup. High-chaos successors and tier 4+ worlds declare on neighboring breakaways when legal; lower-chaos worlds receive claims and wargoals more conditionally.

## Subagent Outputs Integrated

- Focus audit handoff:
  - `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_focus_tree_auditor_full_rework_gap_audit.md`
  - The audit confirms focus files no longer directly spam duplicate `add_ideas`; the remaining bloat is repeated helper-payload sameness and systemic route/layout design debt.

- Documentation cleanup handoff:
  - `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_full_event005_cleanup.md`
  - The documentation subagent updated Event005 docs and left exact workbook follow-up for `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Main Sheet` row `6`.

## Validation

- Brace balance passed for:
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
- `git diff --check` passed for the touched gameplay and documentation files.
- `git diff --name-only -- gfx/flags interface/flags` returned no output. No flags were touched.

## Remaining Risks

- The focus trees are more playable, but not fully clean. Kazakhstan and Belarus still have systemic crossing counts that require a real route-layout pass, not another small coordinate nudge.
- The reward-spam issue is not direct duplicate `add_ideas`; it remains a design-depth issue around repeated helper effects. The focus auditor recommends route-specific capstone rewrites rather than broad mechanical cleanup.
- No workbook edit was made because the documentation subagent could inspect the spreadsheet XML but did not have `openpyxl` available.

## Completion Status

This is an urgent playability tranche, not a full Event005 completion claim.

# Event005 Documentation Curator Handoff

Date: 2026-06-05
Role: `chaosx_documentation_curator`
Scope: documentation-only cleanup for Event005 Soviet Collapse.

## Files Changed

- `docs/plans/005_soviet_collapse_plans/documentation_state.md`
- `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_current_state_handoff.md`

No gameplay, localisation, scripts, focus files, decisions, events, history, AI, GUI, GFX, assets, spreadsheets, or flag files were edited.

## Files Inspected

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.codex/agents/chaosx_documentation_curator.toml`
- `docs/events/005_soviet_collapse.md`
- `docs/specs/005_soviet_collapse_specs/*.md`
- `docs/plans/005_soviet_collapse_plans/*.md`
- Selected recent handoffs under `docs/plans/005_soviet_collapse_plans/subagent_handoffs/`, especially the June 5 focus/release/CFR handoffs.

## Documentation Outputs

- Added a current-state ledger with resume facts, recent plan/handoff dispositions, contradictions, stale-doc notes, and next resume priorities.
- Added a source-of-truth map that ranks specs, overview docs, recent handoffs, and historical plans.
- Recorded that Event005 is not complete and that focus-tree completion, dynamic decision expansion, staged release behavior, and evolution detail parity still need parent-owned completion evidence.
- Recorded that flags and assets are out of scope for the active parent task.

## Key Dispositions Recorded

- `2026_06_05_parent_cfr_construction_focus_depth_tranche.md`: implemented CFR tranche with validation evidence, but not Event005 completion.
- `2026_06_05_parent_ukraine_belarus_route_lock_tranche.md`: implemented route-lock tranche, superseding the earlier Ukraine/Belarus route-lock audit finding.
- `2026_06_05_parent_focus_cleanup_layout_dsc_aggression_tranche.md`: implemented BLR/KAZ/GAC pathline and DSC aggression tranche, superseding matching audit findings.
- `2026_06_05_parent_dynamic_nonbase_release_gate_handoff.md`: implemented current active-crisis non-base release gate evidence.
- `20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md`: retained as latest full mechanical focus count baseline, with route-lock finding marked superseded.
- Older focus/release plans remain historical or partially queued; none are treated as completion proof.

## Contradictions Flagged

- Union Unmade terminal release wording conflicts across docs:
  - `docs/events/005_soviet_collapse.md` and spec part 4 describe exhaustive terminal release sweeps.
  - `2026_06_05_parent_dynamic_release_pacing_and_idea_cleanup_followup.md` says normal Union Unmade no longer calls the exhaustive all-possible helper directly.
- Older release-floor language is stale compared with current staged, live-pressure-gated active release wording.
- Spec part 7 requires flags/assets for final completion, but current parent scope forbids flag edits.
- Focus-tree completion must not be claimed because recent audits and handoffs still list helper-generic rewards, cloned custom splinter scaffolds, shallow compact/ancient trees, and missing final post-CFR audit evidence.
- Evolution detail parity must remain in progress until a later spreadsheet/event-detail handoff proves parity.

## Validation Grep Checks

Run only against documentation files inspected or touched:

- `rg --files docs/events docs/specs/005_soviet_collapse_specs docs/plans/005_soviet_collapse_plans | sort`
- `find docs/specs/005_soviet_collapse_specs docs/plans/005_soviet_collapse_plans -maxdepth 2 -type f -printf '%TY-%Tm-%Td %TH:%TM %p\n' | sort`
- `rg -n "^#|flag|flags|instantly|instant|immediately|complete|completion|evolution|spreadsheet|release|all republic|all.*release|focus trees?" docs/events/005_soviet_collapse.md docs/specs/005_soviet_collapse_specs docs/plans/005_soviet_collapse_plans -g '*.md'`
- `rg -n "Current Priority|Legacy Doc Routing|Event Log Evolutions|Union Unmade|Progressive general releases|Focus rewards|Current Gameplay Surface" docs/events/005_soviet_collapse.md docs/specs/005_soviet_collapse_specs/*.md docs/plans/005_soviet_collapse_plans/*.md docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05*.md docs/plans/005_soviet_collapse_plans/subagent_handoffs/20260605*.md`

Post-patch checks:

- `git diff --check -- docs/plans/005_soviet_collapse_plans/documentation_state.md docs/plans/005_soviet_collapse_plans/source_of_truth_map.md docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_current_state_handoff.md`
  - Result: passed with no output.
- `rg -n "Event005 remains incomplete|no flag edits|Union Unmade|CFR|route-lock|evolution detail parity" docs/plans/005_soviet_collapse_plans/documentation_state.md docs/plans/005_soviet_collapse_plans/source_of_truth_map.md docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_documentation_curator_current_state_handoff.md`
  - Result: found the required resumability, no-flag, contradiction, CFR, route-lock, and evolution-parity markers in the new docs.

## Skipped Checks

- No gameplay validators were run.
- No game launch or in-game validation was performed.
- No spreadsheet validation was performed.
- No asset, flag, GFX, GUI, localisation, script, focus, decision, event, history, or AI files were opened for editing.

## Remaining Parent Decisions

1. Decide whether accepted normal Union Unmade behavior is exhaustive terminal release or pressure-batched release, then update the overview and spec part 4 if needed.
2. Continue focus-tree depth tranches for custom splinters, compact high-chaos trees, ancient restorations, OGB, and helper-generic reward hotspots.
3. Run a fresh post-CFR, post-route-lock full focus audit before any focus-tree completion claim.
4. Produce explicit decision/evolution detail parity evidence before marking those surfaces complete.
5. Keep flags/assets closed until the parent explicitly reopens asset work.

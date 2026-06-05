# Event005 Documentation Curator Handoff: Release And Focus Resume Packet

Date: 2026-06-05 15:38 UTC
Role: `chaosx_documentation_curator`
Scope: documentation-only curation for Event005 Soviet Collapse during ongoing implementation.

This is not an Event005 completion claim. Event005 remains incomplete.

## Files Changed

- `docs/events/005_soviet_collapse.md`
- `docs/plans/005_soviet_collapse_plans/documentation_state.md`
- `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_153830_documentation_curator_release_focus_resume.md`

No gameplay files, localisation files, scripted effects or triggers, focuses, decisions, GUI/GFX, assets, flags, spreadsheets, binaries, history files, or country setup files were edited by this curator pass.

## What Was Clarified

- Recorded the accepted release boundary: active Soviet Collapse releases are gradual and pressure-gated; terminal, maximum-intensity, and standalone chaos scenario paths can run all-possible release passes.
- Recorded that extra non-base releases must depend on live dynamic state such as Union Collapse Threat, progressive release pressure, failed objectives, regional cascade pressure, war pressure, severe component pressure, urgency, or chaos-tier pressure.
- Recorded that calm worlds should release only base Soviet republics, while higher release pressure and chaos tiers unlock vanilla regional republics, then custom chaos/special splinters.
- Recorded that stronger republics should receive more initial divisions through dynamic scaling, not a short fixed major-tag list.
- Recorded that triggerable Soviet Collapse scenarios are standalone and should not inherit unrelated live-crisis settings.
- Recorded that the selected-breakaway decision visibility bug remains a dynamic-system priority, with Tajikistan-style empty intervention panels as the example to preserve. The fix must not use hardcoded tag lists.
- Replaced the earlier Union Unmade "parent decision needed" framing with the accepted distinction between live staged releases and terminal/max/scenario rupture paths.
- Updated the source map to trust `2026_06_05_focus_tree_auditor_post_cfr_current_audit_pathline_patch.md` as the latest focus-tree audit baseline.
- Marked evolution-detail/event-detail parity as pending and requiring exact spreadsheet wording after implementation facts are finalized.
- Marked flag and flag-asset work as no-touch/future scope under the latest user correction.

## Current Queued Implementation Items

- Prove release pacing across calm, high-pressure, chaos-tier, terminal, and maximum-intensity scenario starts.
- Keep extra non-base releases dynamic and pressure-gated.
- Validate dynamic starting-force scaling for strong republics and small edge candidates.
- Continue focus-tree cleanup around political, industry, and expansion branches; compact layouts; no overlapping lines; fewer pointless mutual exclusions; no idea spam; and meaningful mechanics, decisions, war goals, cores, units, templates, factions, and regional interaction rewards.
- Fix selected-breakaway intervention visibility dynamically.
- Finish event-detail/evolution-detail parity with the spreadsheet after implementation facts are stable.
- Keep flags and assets closed until the parent explicitly reopens that scope.

## Superseded Or Stale Notes

- Older low-threat release-floor wording is superseded by June 5 dynamic live-pressure gating.
- Older focus-audit route-lock and coordinate findings are superseded where later parent handoffs fixed them.
- `20260605T145855Z_event005_focus_tree_auditor_current_state_handoff.md` remains useful history, but the post-CFR audit is now the current baseline.
- Any docs treating flag work as active should be read as future/no-touch scope under the current correction.

## Validation Run

- `git diff --check -- docs/events/005_soviet_collapse.md docs/plans/005_soviet_collapse_plans/documentation_state.md docs/plans/005_soviet_collapse_plans/source_of_truth_map.md docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_153830_documentation_curator_release_focus_resume.md`
  - Result: passed with no output.
- `git status --short -- docs/events/005_soviet_collapse.md docs/plans/005_soviet_collapse_plans/documentation_state.md docs/plans/005_soviet_collapse_plans/source_of_truth_map.md docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_153830_documentation_curator_release_focus_resume.md`
  - Result: showed only the four documentation surfaces changed by this pass: three modified Markdown files and this new handoff.
- `rg -n "Event005 remains incomplete|gradual|pressure-gated|standalone|Tajikistan|hardcoded tag lists|no active flag work|no-touch|spreadsheet" docs/events/005_soviet_collapse.md docs/plans/005_soviet_collapse_plans/documentation_state.md docs/plans/005_soviet_collapse_plans/source_of_truth_map.md docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_05_153830_documentation_curator_release_focus_resume.md`
  - Result: found the expected markers for incomplete status, gradual/pressure-gated releases, standalone scenarios, Tajikistan/no-hardcoded-tag-list visibility work, no-active-flag/no-touch scope, and spreadsheet parity.

## Remaining Doc Risks

- Specs part 7 still contains final flag and asset requirements. This pass did not rewrite the source spec; it recorded the current no-flag boundary in the resume map instead.
- The event catalog spreadsheet was not edited. Evolution-detail parity remains pending until implementation facts are finalized and spreadsheet wording is mirrored exactly.
- No gameplay audit was performed by this curator pass.

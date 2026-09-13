# Event 027 Doctrine Research documentation curator handoff

Date: 2026-09-01.

Role: bounded documentation-only curator.

Scope: docs/events/027_doctrine_research/, docs/plans/027_doctrine_research_plans/, and the current Event 027 source files used as evidence.

No acceptance completion is claimed.

## Current status

Event 027 is source-playable with documented qualifications and remains acceptance-blocked.

The current source registers Event 027 in global.repeatable_events at common\scripted_effects\chaosx_logic_effects.txt:325 and includes constant:doctrine_research_event.id in the default reworked-event allowlist at common\scripted_triggers\chaosx_settings_triggers.txt:31.

The current effect-applied receipt recovery computes receipt pre-level plus the one-point increment at common\scripted_effects\027_doctrine_research_effects.txt:3174-3175, rereads the native level at line 3176, and compares the stored and observed levels at lines 3179-3181.

The old documentation claims that Event 027 is excluded from the default reworked-event allowlist and that effect-applied recovery lacks an exact readback are superseded.

The accepted criterion at docs/specs/027_doctrine_research_specs/027_doctrine_research_acceptance_criteria.md:13 still conditions default enablement on full rework readiness, so current source inclusion remains an open parent release decision.

## Current source-of-truth document

The current status ledger is docs/plans/027_doctrine_research_plans/documentation_state.md.

It contains the source-of-truth map, current source evidence, fresh MCP artifact references, plan and handoff dispositions, contradiction list, stale instruction list, hard-wrap audit, remaining blockers, and recommended parent decisions.

The event overview at docs/events/027_doctrine_research/overview.md was updated only for stale Event MCP, technology revision, and probability evidence paragraphs, while its current default allowlist inclusion, exact receipt-readback behavior, and remaining blockers were preserved.

## Files changed

The following files were changed by this documentation-only reconciliation.

| File | Change |
| --- | --- |
| docs/events/027_doctrine_research/overview.md | Refreshed stale Event MCP, technology revision, and probability evidence paragraphs against the fresh read-only MCP results. |
| docs/plans/027_doctrine_research_plans/documentation_state.md | Created as the current Event 027 source-of-truth status ledger. |
| docs/plans/027_doctrine_research_plans/mcp_evidence.md | Added a superseded notice while preserving the dated MCP evidence and obsolete artifact paths as history. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/completion_auditor_2026-08-30.md | Added a superseded notice for pre-reconciliation allowlist and receipt-status claims. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/completion_auditor_current_2026-08-31.md | Added a superseded notice for the old receipt defect and keep-out-of-default recommendation. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/completion_auditor_engine_retry_2026-08-31.md | Added a superseded notice for dated MCP references while retaining source receipt findings. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/completion_auditor_final_2026-08-30.md | Added a superseded notice for the dated broad completion audit. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/completion_auditor_final_current_2026-08-31.md | Added a superseded notice for the stale default-disable recommendation. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/completion_auditor_latest_2026-08-31.md | Added a superseded notice for the stale default-enable recommendation. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/completion_auditor_postfix_2026-08-30.md | Added a superseded notice for the dated broad audit and old MCP references. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/current_native_mastery_audit_2026-08-31.md | Added a superseded notice for the receipt-recovery defect that current source no longer shows. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/parent_ai_strategy_audit_2026-08-31.md | Added a superseded notice for the stale Transport closed MCP status. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/parent_current_status_2026-08-31.md | Added a superseded notice for the contradicted default-allowlist exclusion claim. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/parent_folder_track_guard_audit_2026-08-31.md | Added a superseded notice for the stale dated MCP transport statement. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/parent_implementation_2026-08-30.md | Added a superseded notice for the contradicted intentional default-allowlist exclusion claim. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/parent_native_mastery_edge_2026-08-31.md | Added a superseded notice for the stale MCP transport statement while retaining source findings. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/parent_transaction_audit_2026-08-31.md | Added a superseded notice for the stale MCP transport statement. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/parent_transaction_followup_2026-08-31.md | Added a superseded notice for the stale MCP transport statement while retaining exact receipt-readback evidence. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/probability_baseline_2026-08-29.md | Added a superseded notice for pre-rework fire-once and pool assumptions. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/probability_current_2026-08-31.md | Added a superseded notice for dated scenario artifacts and source snapshot references. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/probability_auditor_current_2026-09-01.md | Created to preserve the fresh scenario-specific read-only probability audit. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/probability_final_2026-08-30.md | Added a superseded notice for dated probability artifacts and source assumptions. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/repo_explorer_2026-08-29.md | Added a superseded notice for the pre-rework fire-once and absent-allowlist map. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/scripted_system_architect_2026-08-29.md | Added a superseded notice for pre-rework allowlist recommendations. |
| docs/plans/027_doctrine_research_plans/subagent_handoffs/documentation_curator_current_2026-09-01.md | Created this required curator handoff. |

No gameplay, localization, spreadsheet, asset, GUI, source, or generated file was changed.

## Document dispositions

The dated MCP ledger mcp_evidence.md and the handoffs named in the changed-files table are marked superseded through top-of-file notices where their current-status claims were stale.

The achievement, asset, localization, pagination, and spreadsheet specialist handoffs were retained unchanged because their bounded findings were not replaced by this reconciliation.

The fresh probability auditor handoff is current owner evidence for the weighted surface, but it remains partial and is not acceptance approval.

No document was deleted.

No standalone Event 027 plan or addendum was found under docs/plans/027_doctrine_research_plans/ outside mcp_evidence.md and the handoffs.

No plan or addendum was rejected or promoted to acceptance by this curator, and open validation items remain queued for parent review.

The new documentation_state.md promotes the current source facts and fresh MCP references into one status ledger without promoting acceptance.

## Contradictions resolved

The pre-rework explorer, architecture, probability baseline, parent implementation, and parent current-status records described Event 027 as fire-once or absent from the default allowlist.

Current source evidence shows repeatable registration at chaosx_logic_effects.txt:325 and default allowlist inclusion at chaosx_settings_triggers.txt:31.

Those historical registration claims are now marked superseded.

The current_native_mastery_audit_2026-08-31.md described effect-applied recovery as conditionally rereading a positive level without comparing receipt pre-level plus one.

Current source evidence at 027_doctrine_research_effects.txt:3174-3181 computes the expected level, rereads the native level, and compares both stored and observed values.

That historical receipt defect is now marked superseded.

The dated MCP records that presented old artifact paths or Transport closed as the current route state are marked superseded as current status authorities.

Fresh Event 027 inspect and render calls and a fresh technology folder query produced the current partial artifact references recorded in documentation_state.md.

## Contradictions still open

The accepted criteria still require full rework readiness before default enablement, while current source includes Event 027 in the default allowlist.

The parent must decide whether this source setting is intentional for controlled validation or whether the gameplay source should be changed to match the accepted criterion.

This curator did not edit gameplay to resolve that decision.

The package remains acceptance-blocked because source evidence does not prove live engine transaction behavior, save or reload recovery, full weighted-logic scenarios, or final consumer presentation.

## Fresh MCP evidence recorded

The fresh bounded hoi4.event_inspect lint returned EVENT_INSPECTED_PARTIAL with status ok, revision 2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570, graph hash e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d, and no direct Event 027 blocker.

The event lint artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c35961a2c95e3697e0a6b63ea3638be77bdb8753af69e71dce0765aaff42ebef/b15e170993e630b06139fa69c947dd1ae781f3e2a198552c3429f1b90eaf86b5/event-lint-2725045f62d1.json.

The fresh bounded hoi4.event_render overview returned EVENT_RENDERED_PARTIAL at the same revision with layout hash 1729fe993aee0578ed8fd2b03d51b4155b6fda6c3d8b83e712401a363f89cc5c.

The event overview manifest is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82a9f3c484279b79c8906905786c405700309397fa4ef64a692ecafb6befb6e4/a2c705976e871914085ad4710279a8ad685b70a87d4e82f4844e137d87fc99b8/event-overview-2725045f62d1-manifest.json.

The fresh shared GUI inspection for events_log_popup_window with scenario event_027_details-generated-1 returned GUI_INSPECTED with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/256b0d979744678bdb5dfcdf7d861548d6d9dd96f3781008f0047f5e70b4eb20/0ccedd3cce5d53cabd6dfba5622945ad1ff66c8a6235cb583d95e53cd157a1a1/gui-inspect.38e46b91effc0e21.json.

The GUI inspection reported shared revision 38e46b91effc0e21d4ce2877bb9e4e3ab0da5c1717a8139e75e6e6dc82b46a84 and 38 blocking GUI diagnostics, including symbol-collision diagnostics.

The fresh shared GUI render for the same window and scenario returned GUI_RENDERED with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/874e5416e079c875930d0789a94a08da679e432a55f6cc9dd31c2b6d1e8a5675/41afcf4a7ccebd9befa7308c790a0dfb27bd22923c62ba18cf21d98c29b0e1d9/events_log_popup_window-full.svg.

The GUI render response was truncated at the wire budget and returned validation false, so it is not accepted Event 027-specific Event Log or Event Details presentation evidence.

The fresh hoi4.tech_inspect folder query returned TECH_INSPECTED at revision 7080c50bf1467579a159640153bbb2d43902b0b7a42a6c35daa41609a5124ed9 with graph hash 3a8197353f9acbc3271a5bbd54995b9887f067674e8d69285cb83dff0b574c68.

The technology folder artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7963f7ee9fda2fb25ccb2e335a47183d76d740b21ac2f199c2909fe49f6f169d/bea79bbabdde3622cf45e20b70f0815f6a25c70f05d73cfd90c58f7f7482e633/technology-folders-7080c50bf146.json.

The Event 027 inspect and render results remain partial, and the technology result has 1,421 aggregate blocking diagnostics.

A fresh read-only chaosx_ai_probability_auditor run completed with fork_context=false and no gameplay write authority.

It inspected domain, Grand Doctrine, track, and subdoctrine random_list layers with 143 available candidates under scenario set DR_027_STATUS_2026_09_01 and scenario hash 358d038f31767e827cef245256e5ec9378c2d4c5f13b38fb05f08021099b9df4.

The primary probability artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c09b4c3db576d2ecdf4a7635909bd15cf8c7d16dd0587594450a31d15af77a44/89da83974e660c78c1e2ba2ceee7c4352c7d633a0673e7025c1d18dd477c7dc3/probability-inspect-db288f956997.json.

All four empty-fixture evaluations returned PROBABILITY_ANALYZED_PARTIAL with zero diagnostics and unresolved rows caused by missing typed country and doctrine fixtures.

Current-to-current probability compare controls returned comparisonChanges=0 and are not accepted baseline-to-final comparisons.

Required sweeps returned PROBABILITY_SWEEP_RANGE_REQUIRED because the DR-A01 num_divisions path supplied no scenario range, numeric alternatives, or numeric state value.

No threshold, sensitivity, rank-reversal, simulation, or sequence conclusion is available, and the explicit probability render refresh was interrupted before returning.

The preserved scenario-specific probability handoff is docs/plans/027_doctrine_research_plans/subagent_handoffs/probability_auditor_current_2026-09-01.md.

## Markdown hard-wrap audit

The scoped Markdown files were checked for accidental prose hard wraps while excluding headings, list items, tables, block quotes, code fences, metadata blocks, and identifier lists.

No accidental mid-sentence or mid-clause hard-wrap issue was identified.

The raw heuristic candidates were deliberate metadata and identifier rows in completion_auditor_achievement_postfix_2026-08-30.md and scripted_system_architect_2026-08-29.md, so no wrap edits were made.

## Validation checks run

Targeted source matching confirmed the current default allowlist entry, repeatable registration, and exact effect-applied receipt comparisons at the line references above.

Fresh read-only Event Viewer and technology MCP calls were made for the current source and their partial status and limitations were recorded.

Fresh read-only GUI inspection and rendering were made for events_log_popup_window with the named Event 027 generated scenario and their blocking diagnostics and truncation limits were recorded.

Source SHA-256 snapshots were captured for events\027_doctrine_research.txt, common\scripted_effects\027_doctrine_research_effects.txt, common\scripted_effects\chaosx_logic_effects.txt, and common\scripted_triggers\chaosx_settings_triggers.txt and recorded in documentation_state.md.

Targeted ripgrep checks identified stale allowlist, fire-once, receipt-defect, Transport closed, and old artifact-reference claims before the superseded notices were added.

The scoped hard-wrap heuristic was rerun and its deliberate metadata and identifier candidates were reviewed.

The documentation state and handoff paths were created under the requested Event 027 plan directory.

## Skipped meaningful validation

HOI4 was not launched because the user prohibited it and live validation belongs to the user.

The event catalog workbook and export were not opened or edited because spreadsheet work is outside the requested scope.

No gameplay source was patched, so no source reload or engine syntax validation was claimed.

Repository staging and commit were not performed because a zero-byte .git/index.lock last written on 2026-08-31 was present with no active Git process observed, and the lock was left untouched.

A complete probability acceptance result and same-scenario comparison were not claimed because the current evaluations use empty fixtures, the required sweeps are blocked by missing numeric ranges or alternatives, and the compare controls were current-to-current rather than baseline-to-final.

No accepted Event Log or Event Details consumer render was claimed because the fresh shared GUI artifacts have blocking validation diagnostics and the generated scenario does not establish Event 027-specific text fidelity.

## Remaining blockers for the parent

Live engine traces for low, middle, final, fractional, banked-active, banked-empty, and interrupted mastery transactions remain unavailable.

Save or reload recovery between prepared, effect-applied, and choice-consumed receipt states remains unproven.

Queue persistence, repeated confirmation, overlapping batches, tag switching, lifecycle transitions, and controller reconciliation remain open acceptance areas.

Special Forces branch-to-track identity remains a fail-closed source limitation without live proof for both occupied tracks.

Complete named-scenario probability evidence and a same-scenario baseline-to-current comparison remain unresolved.

The Event MCP result is partial, the technology result has 1,421 aggregate blocking diagnostics, and final shared Event Log and Event Details consumer presentation is not accepted.

The accepted criterion and current default allowlist setting require a parent release decision.

No acceptance completion is claimed.

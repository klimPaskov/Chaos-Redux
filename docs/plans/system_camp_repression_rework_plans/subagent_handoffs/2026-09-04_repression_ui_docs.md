# Repression UI Documentation Reconciliation Handoff

Date: 2026-09-04.

Scope: documentation-only reconciliation for the shared repression and camps UI redesign.

Status: the current UI source documents, named GUI implementation prompt, package entrypoints, and asset prompt now point to the final sparse redesign; GUI, localisation, scripts, active MCP previews, and final acceptance remain parent-owned work.

## Source-of-truth map

| Surface | Current source and role | Current disposition |
| --- | --- | --- |
| Scripted GUI design | `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md` defines the 960x600 `repression_ledger_window` compatibility surface, the `Repression and Camps` title, five navigation labels, three Situation panels, name-only bounded location lists, six context slots, four Policy directive panels, and three Accountability rows. | `promoted into an accepted spec`: user-authorized redesign and parent acceptance of the native layout within that scope; see the acceptance basis below. Implementation is `implemented` with the final report's evidence and limits. |
| UI and acceptance reconciliation | `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_4_ui_ai_assets_acceptance.md` points to Part 6 and records the presentation acceptance boundary while preserving its AI, country, asset, and gameplay obligations. | Reconciled and cross-linked. |
| GUI implementation prompt | `docs/specs/system_camp_repression_rework_specs/prompts/system_camp_repression_rework_gui_prompt.md` routes implementation to Part 6, names the sparse layout and values, and preserves the AI-equivalent and cleanup requirements. | Reconciled for parent implementation. |
| Package entrypoints | `docs/specs/system_camp_repression_rework_specs/README.md` and `docs/specs/system_camp_repression_rework_specs/package_index.md` point current UI work to Part 6 and the parent final report. | Updated with concise current-source pointers; broader gameplay prose remains dated or unchanged. |
| Asset operator prompt | `docs/specs/system_camp_repression_rework_specs/prompts/system_camp_repression_rework_asset_prompt.md` points GUI asset work to Part 6 and removes instructions to create Ledger background, card, copied-texture, status-sprite, or animation art. | Reconciled for the native-surface boundary. |
| Historical plan reports | The completion reports, audits, and repair notes under `docs/plans/system_camp_repression_rework_plans/` retain their dated layouts and MCP or source evidence. | Left unchanged as historical evidence; they are not current UI acceptance criteria. |

The player-facing design uses Situation, Territories, Sites, Policy, and Accountability, while `repression_ledger_window` and only the parent-verified window, panel, navigation-mark, and action identifiers remain compatibility names; removed `*_card` element ids are not retained.

The Situation page has three compact panels for civilian-loss pressure, administrative strain, and surviving evidence with a warning state, with current civilian-loss pressure, the resistance band, and inspection or closure guidance in the harm tooltip and current strain, labor contribution, and guards or quotas guidance in the strain tooltip; it has no bounded state summaries.

The Territories and Sites pages use the existing bounded `camp_gui_pool_states` and `camp_gui_active_site_states` arrays, expose up to 24 two-line location-name entries through six viewport rows with selected-row highlighting and explicit empty states, hide the right detail pane when empty, show a neutral selection instruction when nonempty and unselected, and show the selected name and site type plus six context button slots with paired cost rows when selected; the 24-entry bound is a retained data limitation, not a new world-state surface.

The Policy page shows the active institution, current course, four existing directive panels, and guard or quota actions, while Accountability shows three rows for exposure/evidence, recorded deaths, and closure/reform pressure.

The redesign changes the presentation contract only and does not add gameplay, effects, costs, AI paths, or new asset production requirements.

## Files changed

- `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_6_scripted_gui_wireframe_value_display.md` now defines the sparse native 960x600 replacement, exact navigation labels, three Situation panels, name-only dynamic Territories and Sites lists, selected-location review states, six context slots with cost rows, four Policy directive panels, three Accountability rows, and the limited compatibility identifiers.
- `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_4_ui_ai_assets_acceptance.md` now links UI acceptance to Part 6 and removes stale optional, paper-ledger, visible-card, and visible-table presentation language while leaving AI, country, asset, super-event, and achievement material outside the presentation scope intact.
- `docs/specs/system_camp_repression_rework_specs/prompts/system_camp_repression_rework_gui_prompt.md` now requests the `Repression and Camps` title, native tiled panels and buttons, five navigation labels, name-only bounded dynamic location lists, selected-location review states, six context slots, and no visible status, table, or ledger columns.
- `docs/specs/system_camp_repression_rework_specs/README.md` now points current UI work to Part 6 and marks the older implementation and asset paragraphs as dated evidence.
- `docs/specs/system_camp_repression_rework_specs/package_index.md` now points current UI work and final tracking to Part 6 and the parent report.
- `docs/specs/system_camp_repression_rework_specs/prompts/system_camp_repression_rework_asset_prompt.md` now routes GUI assets to native HOI4 surfaces and removes current instructions to create Ledger art.
- `docs/plans/system_camp_repression_rework_plans/subagent_handoffs/2026-09-04_repression_ui_docs.md` records this source-of-truth map, disposition audit, MCP baseline, unresolved contradictions, and parent follow-up.

## Resolved contradictions

- The GUI is a required player-opened surface when the existing visibility gates apply; the category header remains the compact title, institution, and phase entry surface while the window is closed.
- The old Summary, State Pools, Active Sites, Authority, and Records labels are replaced by Situation, Territories, Sites, Policy, and Accountability in the current design.
- The old 900x560 paper-ledger wireframe, card grid, table-like rows, and detached global action bar are superseded in Part 6 by the 960x600 dark framed two-pane composition with inline actions.
- Parchment, copied game textures, custom replacement panel art, old card elements, and custom status or animation art are removed from the current UI contract in favor of native HOI4 tiled panels, buttons, and parent-verified compatibility ids.
- The named GUI prompt no longer mandates chemical or biological killing-efficiency controls and now preserves the accepted evidence and consequence boundary.
- The title is `Repression and Camps`; `Repression and Camps System` is retained only where an older document records historical wording.
- The current display-array names are `camp_gui_pool_states` and `camp_gui_active_site_states`, matching the parent-provided bounded arrays; other shared subsystem arrays remain internal, and only window, panel, navigation-mark, and action identifiers remain compatibility identifiers.
- Empty Territories or Sites lists hide the right detail pane, nonempty unselected lists show a neutral selection instruction, and selected rows show only the selected name, site type, and six context slots with paired cost rows while the existing selected-state tooltip retains detailed context.
- Territories and Sites navigation resets selected state after each display-list rebuild, and a new row click establishes the current selection again; no gameplay action gate changes were made.

## Unresolved contradictions and out-of-scope stale documents

| File or surface | Remaining stale evidence | Disposition and parent decision |
| --- | --- | --- |
| `docs/specs/system_camp_repression_rework_specs/README.md` and `docs/specs/system_camp_repression_rework_specs/package_index.md` | Dated baseline paragraphs still mention the former Ledger, but current-source pointers now direct UI work to Part 6 and the parent final report. | Reconciled with concise pointers; dated gameplay and implementation prose remains historical. |
| `docs/specs/system_camp_repression_rework_specs/continuation/continuation_prompt.md` and Part 7 | Still contain old GUI labels, optional GUI language, or old asset references. | Left unchanged because the parent limited the patch to Part 4, Part 6, and the named GUI prompt; decide whether to queue a follow-up reconciliation. |
| `docs/specs/system_camp_repression_rework_specs/prompts/system_camp_repression_rework_coding_prompt.md` | Contains broader implementation guidance and stale non-UI chemical or biological optimization language. | Left unchanged to preserve AI and mechanic scope; parent should decide whether a separate prompt cleanup is needed. |
| `docs/specs/system_camp_repression_rework_specs/prompts/system_camp_repression_rework_asset_prompt.md` | Country and event asset families remain in the prompt, while the former Ledger GUI art instruction is replaced by native-surface guidance. | Reconciled only for the GUI asset boundary; non-UI asset guidance remains unchanged. |
| `docs/specs/system_camp_repression_rework_specs/prompts/system_camp_repression_rework_goal_prompt.md`, `system_camp_repression_rework_validation_prompt.md`, and `system_camp_repression_rework_decision_mission_prompt.md` | Contain broader mechanic, validation, or decision language that was not part of the named UI prompt scope. | Left unchanged; do not treat their stale presentation or mechanic notes as superseding Part 6 without a parent decision. |
| `docs/plans/system_camp_repression_rework_plans/completion_report.md`, `repression_and_camps_system_ui_completion_2026-08-28.md`, `repression_ledger_interface_audit_2026_07_29.md`, and `repression_ledger_ui_repair_2026-08-27.md` | Retain dated old tabs, 900x560 geometry, card or ledger composition, and prior asset or MCP evidence. | Left unchanged as historical or prior-plan evidence; they must not be cited as current acceptance for the redesign. |
| `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md` and older UI handoffs | Still contain old UI labels and completion wording. | Left unchanged by scope; parent should use Part 6 and this handoff for current UI decisions and decide whether to add a separate superseded notice. |

## MCP baseline evidence

The required read-only GUI route was checked against `repression_ledger_window` with the named scenario `repression_ledger_current_docs_baseline` before this documentation reconciliation.

The first call without a scenario returned `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.gui_inspect: windowName and scenario must be provided together`; the retried call with the named scenario succeeded with status `GUI_INSPECTED`.

The successful baseline result reported workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `6fb293b002ef3c20c22a39e80a1c5d5c54b359d3db4362c972b59ac1a65c1677`, `complete: true`, and `inspectedElementCount: 104`.

The baseline fidelity counts were modelled 986, approximated 14, ignored 102, missing 0, unsupported 14, and unresolved 0.

The source resolved to `mod:interface/camp_repression_ledger.gui`, and the baseline diagnostics reported overlapping click regions among the old `camp_gui_select_pool_*` and `camp_gui_select_site_*` rows, overlaps with country actions, a `GFX_tiled_window_transparent` declared-size mismatch warning, and visible title or background overlap; the result had `validation.passed: false` because of those visible-overlap diagnostics.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc85a8a38e8c54c964914ff2e3a663296b0fd1059d7e9f5dc3b99a6f4cbcfec9/0b6ae692e5dc9d2cba777538b66d0b954483550402acefc1eb19c9d07ca08fff/gui-inspect.6fb293b002ef3c20.json`.

This is baseline evidence for the superseded implementation, not post-change acceptance of the redesign.

No post-change GUI rewrite, render, or comparison was run by this subagent because the parent owns GUI implementation and active MCP previews; the parent must produce the current inspect, render, rewrite, and post-change comparison evidence.

## Markdown hard-wrap audit

No accidental mid-sentence or mid-clause hard wraps were introduced in the six edited documentation files or this handoff; new prose sentences are kept on one physical line, and tables, headings, lists, and code blocks retain deliberate Markdown structure.

No broad hard-wrap scan was run across out-of-scope historical and prompt files because they were not edited.

## Validation and skipped checks

- Targeted `git diff --check` and `rg` checks were run against the seven files in this handoff; the parent owns the final integration check because other agents may be editing adjacent files concurrently.
- The documentation review used targeted reads and searches of the named specs, prompt, plans, offline wiki pages, vanilla documentation, vanilla interface precedents, and the read-only GUI inspect route.
- No new MCP call was run during the 2026-09-05 resume because the parent owns current production previews; gameplay loading, localisation encoding, GUI source parsing after implementation, and in-game acceptance were not claimed or run by this documentation-only subagent.

## Parent follow-up and risks

- Implement the 960x600 window and five navigation surfaces in the GUI and localisation files, preserving `repression_ledger_window` and existing runtime identifiers for compatibility.
- Rebuild the Territories and Sites lists from the bounded arrays, verify six-row scrolling, selected-row highlighting, explicit empty states, right-pane details, and inline context actions at the parent-selected resolutions.
- Resolve the baseline click-region and visible-overlap diagnostics through the required MCP inspect, render, rewrite, and post-change comparison workflow.
- Reconcile the remaining out-of-scope Part 7, continuation prompt, broader prompts, trackers, and historical reports in a later documentation pass only if they must serve as current operator instructions; the README, package index, and asset prompt now carry current Part 6 pointers.
- The parent final MCP read passes and `docs/plans/system_camp_repression_rework_plans/repression_ui_redesign_2026-09-05.md` remain the acceptance source for the runtime surface; this handoff intentionally makes no runtime completion claim.
- A scoped commit was not created because the shared repository already held another Git process's `.git/index.lock`; no lock or unrelated staged changes were removed or altered.

## Simplifications, omissions, and blockers

This handoff contains no gameplay, AI, effects, cost, localisation, GUI, asset, or MCP implementation changes.

The requested documentation scope is complete, but the overall UI redesign remains incomplete until the parent implements and validates the runtime surface.

## Parent acceptance and final disposition, 2026-09-05

The user explicitly requested a complete repression UI redesign, removal of the ledger presentation, and active MCP previews.
The parent accepted the native 960x600 sidebar and adjacent location-order layout within that authorization, without claiming separate user approval of pixel geometry.
Part 6 is `promoted into an accepted spec` on that basis.
The six current source documents listed above are `implemented` documentation reconciliation, supported by the four runtime files and the final report at `../repression_ui_redesign_2026-09-05.md`.
Historical UI composition instructions are `superseded` by Part 6 for this presentation only; their gameplay and other system obligations are not reclassified by this task.
The final report records nine successful production MCP render cases, final source inspection, the writer transaction limitation, and the retained 24-entry array bound.
The parent completed these final acceptance and wording amendments after the documentation worker handoff.

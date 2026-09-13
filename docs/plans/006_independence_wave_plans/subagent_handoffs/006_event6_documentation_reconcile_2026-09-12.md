# Event 006 documentation reconciliation — 2026-09-12

## Disposition

Documentation reconciled only. Event 006 remains **HOLD / PARTIAL** at exactly 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows.

This pass does not approve design, admit a package, change gameplay, close an asset or GUI gate, or claim whole-event completion. Current source is evidence of what exists and is not an acceptance basis for intended design.

## Scope

The bounded cleanup covered the current source-of-truth map, resume packet, specification README, quality acceptance checklist, simplifications/blockers ledger, and package manifest. The current source checks were limited to `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/decisions/006_independence_wave_balkan_decisions.txt`, and `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, plus the existence check for `common/scripted_triggers/006_independence_wave_triggers.repair.tmp`.

The seven accepted specification parts remain unchanged. `docs/events/006_independence_wave/overview.md` was already modified by another concurrent worker and was left unchanged to avoid overwriting unrelated or newer work.

## Current source-of-truth map

| Surface | Current authority | Evidence and limitation |
| --- | --- | --- |
| Accepted design | `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md` through `006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` | Design authority remains unchanged; this reconciliation did not infer acceptance from source presence. |
| Implementation ledger | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Updated to the 2026-09-12 documentation snapshot while preserving **HOLD / PARTIAL** and 32/29/40/161. |
| Restart point | `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Updated with the same current boundary, resolved source conflicts, and unresolved gates. |
| Event 021 package setup | `common/scripted_triggers/006_independence_wave_triggers.txt:16-60` | Event 021 owns only the bounded origin-neutral setup and completed-adapter branches inside `is_independence_wave_package_content_active`; Event 006 player surfaces remain active-origin-only and explicitly reject adapter receipts. This resolves implementation authority wording but does not approve a package or expand Event 021 design authority. |
| Balkan decision registry | `common/decisions/006_independence_wave_balkan_decisions.txt` | The eight package sections remain consolidated under source markers, use `has_independence_wave_current_capital_controlled_by_root`, and contain no `# temporary_remove_immediately` marker; this resolves the earlier source-hygiene and raw-capital-scope conflicts without changing decision design. |
| IW-095 Dahomey AI registry | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3648,3661,3676` | The registry uses `independence_wave_dah_host_ledgers_settled`, `independence_wave_dah_compact_stabilized`, and `independence_wave_dah_emergency_government`; no stale `independence_wave_iw095_dah_*` receipt remains. Typed probability and quantitative balance remain unresolved. |
| Removed repair artifact | Canonical `common/scripted_triggers/006_independence_wave_triggers.txt` | `common/scripted_triggers/006_independence_wave_triggers.repair.tmp` is absent. This does not remove or supersede the separate persistent `independence_wave_event6_runtime_unlocked` gameplay marker. |
| Current MCP evidence | This handoff and `subagent_handoffs/006_event6_current_mcp_evidence_2026-09-12.md` | Event evidence remains partial, focus geometry remains structurally clean apart from the accepted authored long connector, GUI source inspection remains bounded by state/fallback/blendframe/click-region limitations, and the package planner exposes no typed custom-pool candidates. |
| Current visual disposition | `subagent_handoffs/006_event6_asset_audit_completion_update_2026-09-12.md` | Implemented repairs with **HOLD / PARTIAL**; ASSET-005, ASSET-006, ASSET-039, and ASSET-044 remain `needs_user_review`, while ASSET-045 and ASSET-046 remain `blocked`. |

## Unresolved plan and handoff dispositions

| Document | Disposition | Basis, evidence, and remaining limitation |
| --- | --- | --- |
| `006_event6_current_mcp_evidence_2026-09-12.md` | `implemented` as read-only evidence | Current event, focus, GUI, and probability routes were rechecked in this pass; none supplies live transaction or whole-event completion proof. |
| `006_event6_completion_gap_reaudit_2026-09-06.md` | `superseded` in part | Its Event 021 authority conflict, Balkan temporary-marker removal, and Dahomey receipt-name correction are resolved in current source; its remaining package, probability, GUI, asset, rights, formable, audio, and live-runtime gaps remain open. |
| `006_event6_asset_audit_completion_update_2026-09-12.md` | `implemented` repairs with **HOLD / PARTIAL** | Current asset inventory and explicit ASSET-005/006/039/044/045/046 gates remain authoritative. |
| `006_event6_afx_package_audit_2026-09-12.md` | `implemented` as bounded no-gameplay audit evidence | AFX is removed from the generated-flag blocker group, but no new identity, provenance, rights, admission, or balance approval follows. |
| `006_event6_flag_blocker_reconciliation_2026-09-12.md` | `implemented` documentation correction | Generated-flag blocker Group B changes from 39 to 37 by removing IW-006 AFX and IW-024 AXX; all other blocker rows remain. |
| `006_event6_bsk_lifecycle_repair_2026-09-12.md` | `implemented` bounded source repair | BSK remains admitted under its existing exact contract; this repair does not widen central admission or alter 32/29/40/161. |
| `006_event6_status_gui_warning_placement_repair_2026-09-12.md` | `implemented` bounded layout repair | The instability warning moved into the existing tab gap and preserves the accepted five-value readout; broader GUI acceptance remains open. |
| `006_event6_status_gui_mission_overlap_review_2026-09-12.md` | `unresolved` review evidence | The parent-approved five-value exception is the acceptance basis for retaining five values, superseding only the earlier request to choose a four-value ceiling. Mission/detail overlap and representative dynamic GUI fixtures remain unresolved. |
| `006_event6_status_gui_repair_2026-09-12.md` | `superseded` in part | Its request for a parent decision on reducing the five-value readout is superseded by the mission-overlap review and warning-placement repair; it remains historical baseline evidence for the observed layout concerns. |
| `006_catalog_audit_2026-09-12.md` | `implemented` no-change audit | Workbook-facing statuses remain Event `Needs Testing`, Cluster `Partially Available`, and Scenario `Needs Testing`; no spreadsheet was edited in this reconciliation. |

## Files changed

| File | Documentation disposition |
| --- | --- |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` | Current heading dated 2026-09-12; Event 021 ownership wording and removed Balkan temporary-marker disposition resolved; removed repair artifact distinguished from the persistent runtime marker; current visual, flag-blocker, BSK, and GUI handoff dispositions recorded. |
| `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md` | Restart authority aligned to the same current evidence and unresolved gates. |
| `docs/specs/006_independence_wave_specs/README.md` | Implementation overlay dated 2026-09-12; accepted spec authority preserved; current source conflicts and visual disposition recorded without editing design parts. |
| `docs/specs/006_independence_wave_specs/quality/spec_acceptance_checklist.md` | Current evidence overlay aligned to Event 021, Balkan, Dahomey, repair-artifact, asset, flag-blocker, and GUI evidence; acceptance criteria themselves remain unchanged. |
| `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md` | Current asset and GUI blocker authority updated while preserving every unresolved gate. |
| `docs/specs/006_independence_wave_specs/quality/package_manifest.md` | Current visual disposition and exact blocked/review statuses updated; no package admission or asset promotion recorded. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_documentation_reconcile_2026-09-12.md` | Created as the dated cleanup handoff and resume evidence for this pass. |

## Contradictions resolved

- Event 021 is no longer described as an ownerless or ambiguous origin-neutral receipt path: current source assigns it only the bounded internal package-content setup/completed-adapter branches and keeps every Event 006 player surface behind active Event 006 origin.
- The earlier Balkan raw-capital-scope concern is source-resolved: the consolidated registry uses the fail-closed current-capital helper across the relevant decision sections.
- The earlier Balkan source-hygiene blocker is source-resolved: `# temporary_remove_immediately` is absent from the consolidated registry.
- The earlier IW-095 Dahomey prefixed/unprefixed AI receipt mismatch is source-resolved: the canonical unprefixed receipts are current and the stale prefixed names are absent.
- The former trigger repair snapshot is no longer treated as a current path or outstanding cleanup item: the `.repair.tmp` file is absent and the canonical trigger registry remains authoritative.
- The older GUI repair handoff's implied need to reduce the readout to four values is superseded by the recorded parent-approved five-value exception; this does not resolve the separate mission/detail overlap or dynamic fixture questions.
- The generated-flag blocker list now uses Group B count 37 and excludes AFX and AXX without converting that correction into provenance, rights, or admission approval.

## Contradictions and gates still open

- Event 006 remains **HOLD / PARTIAL**; no current evidence changes 32/29/40/161 or the absolute no-pre-event boundary.
- The Statehood Ledger still lacks representative dynamic-state, click-region, blendframe-playback, static-fallback, and mission/detail overlap acceptance evidence.
- Package-planner probability discovery remains empty for the typed custom weighted-pool route; nested package odds, option/decision/mission/focus pools, strategy factors, and quantitative balance remain unresolved.
- ASSET-005, ASSET-006, ASSET-039, and ASSET-044 remain `needs_user_review`; ASSET-045 and ASSET-046 remain `blocked`.
- The AFX/AXX flag-blocker correction does not establish source identity, rights, ownership, or admission.
- IW-095 identity, portrait, flag, FORM-24, central-attestation, and engine gates remain open despite the corrected AI receipt spelling.
- Live release, transfer, report delivery, save/load, and transaction behavior remain unproved by the structural evidence.

## Duplicate and superseded documents

- `006_event6_status_gui_repair_2026-09-12.md` is retained as historical baseline evidence but is superseded only for its four-value-versus-five-value parent-decision wording by `006_event6_status_gui_mission_overlap_review_2026-09-12.md` and `006_event6_status_gui_warning_placement_repair_2026-09-12.md`.
- `006_event6_completion_gap_reaudit_2026-09-06.md` is retained as a broad historical gap audit, but its Event 021 conflict, Balkan temporary-marker, and Dahomey receipt-name findings are superseded by current source; its other listed gaps remain unresolved.
- `006_event6_visual_asset_audit_2026-09-03.md` remains the historical detailed audit baseline and is superseded for current disposition by `006_event6_asset_audit_completion_update_2026-09-12.md`.
- Removed per-package Balkan decision paths remain historical source-marker provenance only; `common/decisions/006_independence_wave_balkan_decisions.txt` is the current parser path.
- `common/scripted_triggers/006_independence_wave_triggers.repair.tmp` is removed and must not be cited as a current source path.

No duplicate documentation file was deleted.

## Stale prompt or instruction list

No named Event 006 prompt file was in the parent-provided cleanup scope, and no prompt was changed. The stale instructions found in scoped documentation were the outdated 2026-09-05 current-snapshot headings, the ambiguous Event 021 authority wording, the outstanding Balkan temporary-marker removal instruction, the 2026-09-03 visual audit labelled as current, and the superseded four-value GUI decision request; each is reconciled or explicitly superseded above.

## Markdown hard-wrap audit

No accidental mid-sentence or mid-clause hard wrap was introduced in the changed prose. Deliberate headings, paragraphs, list items, and table rows were preserved; unrelated historical prose outside the edited lines was not reformatted.

## Read-only MCP evidence

- `hoi4.event_inspect` for `{kind = event, eventId = chaosx.nr6.1}` returned `EVENT_INSPECTED_PARTIAL` at revision `4bccb6ec7fe1a73728780d86d162cce29175781f0177cb5975beec17f22caa3d`, graph hash `24f73f1a61d57d7a3c99c927d106bf7fd7fe21299898bf43d3d8eab152165819`, with helper/lifecycle analysis deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12ba6da213527c298b9d4372388861110aa2adbd10bcc29d63b651f4a95bdf37/1a1fc1c3cd1d0a879db8b612820bff12d4f7da162f3720c04b72e1909e595dd4/event-lint-4bccb6ec7fe1.json`.
- `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for 184 focuses and 196 connectors, zero crossings, zero node intersections, zero too-close same-row pairs, and one accepted authored ten-column long connector at layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce32c9ea1df9de2521ef9359819d15e244ff0caf439e1868c565ae0936724b06/c1b404761976c60f92a7c0176005fa26686d75b499ce4a763a9ad8bd46fc0ac8/focus-inspect.6427270db259cb43.json`.
- `hoi4.gui_inspect` returned `GUI_INSPECTED` for 48 Event 006 elements at shared revision `b7b6d0067e031dbe5ce3a2960dae3edd5ae91589cc7123f9ecc3ae75708ba16d`; four static-fallback warnings and offline blendframe limitations remain, so no GUI acceptance follows. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8fc6821d4a51fa3deb717fd9788dc755bdc0d0b25ce8de26a213bd3e3cc3dda/84e5d5cd5fa448cd7df43ebb77daecf22744df79d4ec7c6d7ea1339646930b12/gui-inspect.b7b6d0067e031dbe.json`.
- `hoi4.probability_inspect` with adapter `custom_weighted_pool` returned `PROBABILITY_SOURCE_INSPECTED`, source revision `fa97953a5f8a1d617e6a3036bc856fd08628fac7c4b7a75d673cef7c1a4b0442`, source hash `b8d529ef84040585e69b335733b61c7c66ba47fe2685f1f4b2a389077646bf21`, zero candidates, and `poolComplete = false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/964217d5fb77dad1e3925ae9aae8f3a67a59ea9802d8651b1b78908362b5940d/9f89bd705cc64075f2439454f359e0137f87ca73c4450131d8597427361cb244/probability-inspect-b8d529ef8404.json`.

Tool exposure and these successful read-only calls verify the four scoped service routes, not a standalone Technology Tree Viewer or any unscoped MCP surface.

## Validation

- SHA-256 source hashes were recorded as `B9B25CFE1A8AA9E70339E0B06D6CDF1AB01BC9EF017B2C6ADA2135767A08BDEA` for the trigger registry, `AC89181A395FD03ABE4F9A081CDDF648BEBF1DF9BF5E555E533BF710D52F00DF` for the Balkan decision registry, and `60FCBCCAD8DF110F1E050DC35D33D8EB2C397721567CF6AC4580DF345F444E0F` for the AI strategy registry.
- Targeted source search found the Event 021 preparing and completed-adapter receipts inside the package-content trigger and explicit adapter exclusions inside the Event 006 player-surface trigger.
- The consolidated Balkan decision registry contains eight source-marker sections, 69 current-capital-helper references, and zero `# temporary_remove_immediately` markers; no removed per-package decision file was treated as current authority.
- Targeted search found all three canonical Dahomey AI receipts and zero stale `independence_wave_iw095_dah_*` references in the current AI strategy registry.
- `Test-Path` returned false for `common/scripted_triggers/006_independence_wave_triggers.repair.tmp`.
- Targeted documentation search confirmed current 2026-09-12 headings, explicit 32/29/40/161 boundaries, the current asset completion handoff, exact ASSET review/blocked statuses, and Group B count 37.
- The accepted specification parts, gameplay, localisation, GUI, GFX, assets, spreadsheets, and generated agent files were not edited.

## Recommended parent decisions

- Retain the accepted five-value Statehood Ledger exception and decide only the still-open mission/detail layout and representative dynamic-fixture acceptance questions.
- Keep every current asset gate explicit until its named review, identity, rights, or reachability evidence is accepted; do not infer promotion from the corrected Group B count.
- Keep IW-095 fail-closed until identity, portrait, flag, FORM-24, central-attestation, and typed probability gates close independently.
- Continue to treat the 2026-09-12 MCP outputs as structural evidence with their recorded limitations, not as live or whole-event completion proof.

## Remaining risk

Historical sections in the large source-of-truth map and resume packet intentionally preserve dated counts, receipts, and parser paths for provenance. The new top-level authority text and explicit supersession notes govern current routing, but future cleanup should not flatten those historical snapshots or mistake them for current status.

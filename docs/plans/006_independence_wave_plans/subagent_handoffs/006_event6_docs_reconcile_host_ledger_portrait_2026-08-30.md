# Event 006 documentation reconciliation — host ledger and portrait audit

Date: 2026-08-30 (Europe/Kyiv).

Owner: `chaosx_documentation_curator`.

## Scope and disposition

This is a documentation-only reconciliation of the Event 006 source-of-truth map, resume packet, accepted specification index, package manifest, overview, and quality status pages against the latest standalone host-ledger repair, portrait wiring audit, consumer reconciliation, FSM retry, and read-only MCP evidence.

The whole Event 006 disposition remains **HOLD / PARTIAL** at 32 content-attested selectable packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows; no package, asset, localization, gameplay, workbook, or CSV completion claim is made.

No gameplay, localization, asset, GFX, GUI, spreadsheet, or CSV file was edited in this pass.

## Current source-of-truth map

| Surface | Current authority | Disposition and exact evidence |
|---|---|---|
| Accepted design | `docs/specs/006_independence_wave_specs/` seven specification parts | Retained as design intent; partial source implementation does not rewrite the accepted design. |
| Operational implementation | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `006_independence_wave_resume_packet.md` | Updated with the 2026-08-30 host-ledger repair, 51/38/13 portrait matrix, fresh Event MCP limitation, and fresh focus artifact. |
| Shared host ledger | `common/scripted_effects/chaosx_liberation_release_effects.txt` and `common/scripted_triggers/chaosx_liberation_release_triggers.txt` | Current runtime ownership is `global.liberation_plan_hosts`, with aligned host, owned-state, and protected-state arrays; the source-ledger contract is documented as evidence, not live proof. |
| Standalone host repair | `subagent_handoffs/006_event6_standalone_host_ledger_fix_2026-08-30.md`, commits `70231664a` and `d727d6a2b` | Promoted to implemented source repair plus focused regression guard; former-host validation and committed-wave achievement initialization now use the populated shared host ledger, while a user-supplied terminal receipt remains queued. |
| Portrait exact-input matrix | `subagent_handoffs/006_portrait_wiring_reconciliation_2026-08-30.md` and `006_portrait_wiring_supplied_runtime_2026_08_22.md` | Promoted as current source-to-runtime evidence: 51 selected inputs, 38 safe hash-matching mappings, and 13 unresolved inputs; all selected rows remain grounded `source_placeholder`. |
| Portrait consumer aliases | `subagent_handoffs/006_event6_portrait_consumer_reconciliation_2026-08-29.md` and durable manifest `docs/assets/portraits/006_independence_wave/processed/portrait_consumer_reconciliation_2026_08_29.md` | Retained as current consumer evidence for eleven ideology-specific consumers mapped to six existing grounded source-placeholder identities; no new art, binaries, characters, or GFX definitions were added. |
| Portrait provenance conflict | `subagent_handoffs/006_event6_portrait_consumer_closure_2026-08-26.md` | Retained as historical package/runtime evidence because it labels NAV Aguirre and GLC Castelao `styled_final`; it is not silently relabelled by the 2026-08-30 selected-input audit. |
| Non-portrait asset gate | `subagent_handoffs/006_event6_asset_source_repairs_2026-08-29.md`, commit `49d9a577c` | Promoted as current asset evidence: ASSET-004's `397x153` processed/runtime pair now has zero unequal RGB pixels, with repaired processed SHA-256 `c1bbca9b8083731faafaab384e341be27b8fb990a035405ff443ddd4d56b7e9c7` and DDS SHA-256 `4ad0366dc87d54599d77aa2735cc832adca657dd212c3585b7948a91d5e57cef`; the stable sprite basename is unchanged. |
| FSM portrait | `subagent_handoffs/006_iw179_fsm_portrait_source_gate_retry_2026_08_30.md` | Queued/blocked fail-closed: `independence_wave_fsm_sourced_identity_ready` remains unset, Elias Kihleng is not restored, and no fallback identity is accepted. |
| Event MCP | Revision `ac2516cf55a82d5ce3152e98d00c31e148f74b85a13a09c3ad7791c0453bef18`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/829d95ac7d1963c595c408d1674516ac6cab9f06e389505a56f6f27ca22c7e89/2c56668879c6c65bd691e063fe4b221bbc482009ed93395db498f9fef10f9248/event-scan-ac2516cf55a8.json` | Retained as partial evidence only: helper/lifecycle projections are deferred and four workspace-global `SOURCE_UNCLOSED_BLOCK` diagnostics occur at `common/on_actions/016_brilliant_scientist_achievement_on_actions.txt:8` and `common/on_actions/033_acid_rain_on_actions.txt:9`; no Event 006-scoped blocker was isolated. |
| Focus MCP | Revision `c0f89fe5c5bbdfd2d367aebd5424acf3d2b19da5e9fe6baf9a1214e4f33817b4`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/387cfab5049efe0c8e70b728951db42ee1aa49c5334b63f15c2e89b986f55760/025dd7cea43783222f1df794d0afb5009f25411b97c77ff84c1bd10120508ac3/focus-inspect.c0f89fe5c5bbdfd2.json` | Retained as current read-only structural evidence: `FOCUS_INSPECTED`, validation passed, 184 focuses, 195 connectors, zero Event 006 layout diagnostics, and one unrelated vanilla localization warning. |
| Catalog | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` plus generated exports | Left unchanged and out of scope; workbook authority remains with the spreadsheet worker. |

## Plan and handoff disposition

| Plan, handoff, or receipt | Disposition | Evidence or reason |
|---|---|---|
| `006_event6_standalone_host_ledger_fix_2026-08-30.md` / commits `70231664a` and `d727d6a2b` | Implemented source repair and regression guard; live receipt queued | The stale Event 006 host-array name was replaced in standalone validation and achievement initialization with the populated shared `global.liberation_plan_hosts` array, and the focused allocator audit now guards both consumers; no live invocation was performed. |
| `006_portrait_wiring_reconciliation_2026-08-30.md` / commit `525ce17bf` | Promoted current exact-input audit | 51 selected user-supplied DDS inputs, 38 safe byte-identical mappings, 13 unresolved rows, and no copy, rename, relabel, conversion, or runtime asset change. |
| `006_event6_portrait_consumer_reconciliation_2026-08-29.md` / commit `3dbf918b5` | Promoted current consumer alias evidence | Eleven new ideology-specific consumers resolve to six existing source-placeholder identities; no package or asset promotion follows. |
| `006_iw179_fsm_portrait_source_gate_retry_2026_08_30.md` / commit `ce19e6741` | Blocked and fail-closed | No safe period-fit, rights-cleared FSM identity was accepted; the source gate remains unset and no fallback was invented. |
| `006_event6_portrait_consumer_closure_2026-08-26.md` | Retained historical; parent decision required | Its NAV/GLC `styled_final` runtime labels conflict in vocabulary with the 2026-08-30 selected-input rows labelled `source_placeholder`; neither record is rewritten here. |
| `006_event6_asset_source_repairs_2026-08-29.md` / commit `49d9a577c` | Promoted implemented asset repair | The former ASSET-004 strict-grayscale defect is resolved with zero unequal RGB pixels and updated processed/runtime hashes; the older `006_event6_assets_audit_current_2026-08-29.md` remains a pre-repair baseline. |
| `006_event6_documentation_reconciliation_2026-08-30.md` | Superseded for current host/portrait/MCP overlay only | The earlier docs pass intentionally left the map and resume packet untouched and predates commit `70231664a`, the 51/38/13 audit, and the fresh Event MCP revision; it remains historical provenance. |
| `006_event6_documentation_contradictions_reconciled_2026-08-30.md` | Retained as bounded prior reconciliation | Its IW-173 and formable-count corrections remain valid; this handoff adds the separate host-ledger, portrait-provenance, and MCP evidence overlay. |
| `006_event6_parent_mcp_reaudit_2026-08-30.md` | Superseded for current Event MCP state | Its prior revision reported zero blocking diagnostics; the fresh Event 006 scan now reports four workspace-global unclosed-block diagnostics, so the older result remains dated evidence only. |
| `006_event6_completion_audit_current_2026-08-29.md` and 2026-08-28 portrait audit pages | Historical baseline for superseded input counts | Current exact routing is now the 2026-08-30 51/38/13 matrix; the older 110/70/64/47 counts remain traceability evidence, not current routing. |
| Accepted plans under `docs/plans/006_independence_wave_plans/` | Queued unless an explicit implemented, promoted, rejected, superseded, or blocked handoff exists | No plan is promoted merely because a source adapter, portrait file, or partial MCP artifact exists. |

## Contradictions

### Resolved in the patched current docs

- The source map and resume packet omitted the committed standalone host-ledger fix; they now identify `70231664a`, the shared host-ledger owner, changed consumers, and the still-required live terminal receipt.
- The current overview, accepted-spec README, package manifest, acceptance checklist, and blockers page repeated the older supplied-input snapshot; they now route exact portrait input questions to the 2026-08-30 51/38/13 matrix.
- The current Event MCP prose said zero blocking diagnostics or cited an artifact-blocked attempt; it now records the fresh `EVENT_INSPECTED_PARTIAL` revision and four workspace-global syntax diagnostics.
- The current focus prose lacked the fresh artifact reference; it now records the 2026-08-30 `FOCUS_INSPECTED` revision, artifact, validation, and unchanged 184/195 geometry evidence.

### Still open by design

- The 2026-08-30 portrait audit labels all selected grounded source/input rows `source_placeholder`, while the older 2026-08-26 closure labels NAV Aguirre and GLC Castelao `styled_final` runtime consumers. This is an unresolved provenance/lifecycle terminology boundary, not a reason to reclassify bytes or widen admission.
- The fresh Event MCP scan has four workspace-global `SOURCE_UNCLOSED_BLOCK` diagnostics and deferred helper/lifecycle projections. No Event 006-specific blocking diagnostic was isolated, but this is not clean engine evidence.
- A user-supplied standalone `event chaosx.nr6.1` terminal receipt is still missing, so source repair does not prove a non-empty release or achievement update.
- ASSET-004 is source/asset-complete for the requested strict-grayscale repair under `49d9a577c`; no further replacement, processing, or GFX basename change is authorized by this docs pass.
- Typed scenario-specific weighted-logic evidence remains blocked by the recorded `Transport closed` auditor route; no new balance claim is made.

## Duplicate and superseded document list

- `006_event6_documentation_reconciliation_2026-08-30.md` is retained as the immediately prior docs overlay and is superseded only where it predates the host-ledger, portrait-wiring, and fresh-MCP evidence recorded here.
- `006_event6_portrait_consumer_audit_2026-08-28.md` and `006_event6_portrait_consumer_closure_2026-08-26.md` remain dated portrait baselines; their old supplied-input counts are superseded for current routing, while the closure's NAV/GLC runtime labels remain an explicit parent decision.
- `006_portrait_wiring_supplied_runtime_2026_08_22.md` remains the durable 38-row hash ledger and is revalidated by the 2026-08-30 wiring audit rather than deleted.
- `006_event6_parent_mcp_reaudit_2026-08-30.md` remains prior MCP evidence and is superseded for current workspace diagnostics by the fresh Event scan.
- No file was deleted or archived because deletion was not authorized.

## Stale prompts and instructions

- The active routing prompt `docs/specs/006_independence_wave_specs/prompts/independence_wave_subagent_routing_and_briefs.md` points documentation work to the source map and resume packet; those files are now aligned with the current host-ledger and portrait authorities.
- Older dated handoffs that request a fresh portrait consumer pass are historical instructions and should not trigger duplicate art, conversion, or GFX work after the 2026-08-30 audit.
- The FSM retry remains explicitly fail-closed and does not authorize a fallback identity.
- No current prompt authorizes workbook/CSV edits in this reconciliation; those surfaces remain out of scope.

## Markdown hard-wrap audit

- No accidental mid-sentence or mid-clause hard wraps were introduced in the seven patched documentation files or this handoff; each new prose sentence is kept on one physical line, with headings, list items, tables, and code-style spans preserved.
- Pre-existing historical paragraphs were not globally reflowed because doing so would create unrelated churn and could obscure provenance; no hard-wrap correction outside the changed current-authority paragraphs was necessary.

## Recommended parent decisions

1. Decide whether the 2026-08-26 NAV/GLC `styled_final` runtime labels describe a distinct package/runtime lifecycle layer or should be retired in favor of the 2026-08-30 source-placeholder terminology.
2. Run the user-owned standalone `event chaosx.nr6.1` check and provide the terminal receipt fields before treating the host-ledger repair as live release or achievement evidence.
3. Keep the fresh Event MCP result marked partial until the four workspace-global unclosed-block diagnostics and deferred helper/lifecycle projections are resolved or explicitly accepted by the parent.
4. Keep the 13 unresolved portrait inputs and IW-179 FSM source gate fail-closed, with no replacement, fallback, or relabelling absent explicit evidence.

## Validation performed

- Fresh read-only `hoi4.event_inspect` scan for `events/006_independence_wave.txt`: `EVENT_INSPECTED_PARTIAL`, revision `ac2516cf55a82d5ce3152e98d00c31e148f74b85a13a09c3ad7791c0453bef18`, linked artifact recorded above, no Event 006-scoped blocker isolated, four workspace-global `SOURCE_UNCLOSED_BLOCK` diagnostics.
- Fresh read-only `hoi4.focus_inspect` scan for `common/national_focus/006_independence_wave_focus.txt`: `FOCUS_INSPECTED`, validation passed, revision `c0f89fe5c5bbdfd2d367aebd5424acf3d2b19da5e9fe6baf9a1214e4f33817b4`, 184 focuses, 195 connectors, zero Event 006 layout diagnostics, and one unrelated vanilla warning.
- Repository search confirms the runtime source has no `global.independence_wave_plan_hosts` reference; the old token remains only in the historical root-cause prose of the repair handoff and current documentation evidence.
- The current static validator receipts remain the evidence cited by the host-ledger handoff: allocator 149 publishers/32 attested packages with the 3/4/5/7/10 ladder, strict flags 102/102, SCN-008 32 cells with eight edge cases, and country API 242 broad rows with 191 resolved carriers and zero missing or duplicate mappings.
- `git diff --check` and targeted stale-term searches were run on the documentation scope; no localization, asset, workbook, CSV, or gameplay path appears in this patch.

## Remaining risks

- This reconciliation does not establish live Event 006 release, standalone country creation, achievement host-remnant tracking, package promotion, balanced weighted logic, clean MCP helper expansion, or GUI/runtime acceptance.
- The older portrait provenance vocabulary remains intentionally visible in historical docs until the parent resolves the lifecycle distinction.
- The workspace is concurrently edited by other agents; unrelated changes were preserved and no files outside the documentation scope were staged for this handoff.

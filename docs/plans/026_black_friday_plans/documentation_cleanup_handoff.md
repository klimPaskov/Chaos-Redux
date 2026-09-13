# Event 26 Black Friday documentation cleanup handoff

Cleanup date: 2026-09-02.
Scope: documentation-only reconciliation of the current Event 26 registry, exact inventories, Part 8 acceptance record, current completion handoffs, and related plan evidence under `docs/plans/026_black_friday_plans/`.
The gameplay, localisation, asset, source-code, spreadsheet, and CSV surfaces were not edited by this cleanup.
Event 26 remains disabled by default and incomplete.
No live game, save/reload, multiplayer, or full MCP probability/event evidence is claimed.

## Source-of-truth map

| Surface | Authority or evidence path | Current disposition |
| --- | --- | --- |
| Accepted design | `docs/specs/026_black_friday_specs/` and `PACKAGE_MANIFEST.md` | Accepted design only; it is not implementation or completion evidence. |
| Current custom-cost registry | `docs/plans/026_black_friday_plans/event26_cost_surface_registry.md` | Current status/disposition anchor; Appendix A now covers all 81 scanned Chaos Redux owner files, including the four Brilliant Scientist rows, the D'Rhondan bounded row, and nuclear-bomb count 63. |
| Current custom-cost exact inventory | `docs/plans/026_black_friday_plans/event26_cost_surface_custom_inventory.md` | Exact source anchor: 2,224 `custom_cost_trigger` occurrences and 2,225 `custom_cost_text` occurrences across 81 Chaos Redux decision files, with the intentional text-only disclosure at `common/decisions/020_black_plague_rat_decisions.txt:923`. |
| Current native-cost exact inventory | `docs/plans/026_black_friday_plans/event26_cost_surface_native_inventory.md` | Exact source anchor: 1,328 native `cost =` declarations across 62 top-level decision files, with 1,033 not written as the literal `cost = 0` and 295 literal zero/free sentinels. |
| Current design-modifier inventory | `docs/plans/026_black_friday_plans/event26_design_modifier_inventory.md` | Current source evidence for the accepted equipment, module, and unit-design field inventories; unchanged. |
| Part 8 acceptance | `docs/plans/026_black_friday_plans/event26_part8_acceptance.md` | Reconciled current acceptance ledger; arithmetic and source evidence remain bounded, while adapter, calendar, live, and MCP gaps remain open. |
| Current completion audit | `docs/plans/026_black_friday_plans/subagent_handoffs/completion_final_audit_current.md` | Reconciled to the current counts, adapter list, MIO blocker, and refreshed partial Event MCP artifacts; it remains incomplete. |
| Current decision/mission audit | `docs/plans/026_black_friday_plans/subagent_handoffs/decision_mission_cost_audit_current.md` | Reconciled to the current counts, ten bounded tranches, helper-callsite boundary, MIO blocker, and refreshed partial Event MCP artifacts. |
| Current owner-adapter handoff | `docs/plans/026_black_friday_plans/subagent_handoffs/owner_adapter_tranche_current.md` | Reconciled to 104 logical components across ten bounded tranches, including Random Faction and Africa source paths; live proof remains blocked. |
| Current parent status | `docs/plans/026_black_friday_plans/subagent_handoffs/event26_parent_implementation_status.md` | Reconciled to the current counts, 63/63 nuclear-bomb inventory, ten bounded tranches, and engine-inaccessible MIO status. |
| Current localisation patch evidence | `docs/plans/026_black_friday_plans/subagent_handoffs/localisation_patch_audit_2026-09-02.md` | Current source-level patch handoff; it supersedes the stale visual/MCP and terminal-Fury statements in the retained localisation audit. |
| Retained scoped localisation audit | `docs/plans/026_black_friday_plans/subagent_handoffs/localisation_final_audit_current.md` | Kept as a bounded historical record with a supersession note and corrected current key, visual, and terminal-Fury statements. |
| Current spreadsheet handoff | `docs/plans/026_black_friday_plans/subagent_handoffs/2026-09-02_event26_spreadsheet_handoff.md` | Current workbook evidence; unchanged because the workbook and CSV exports are outside this cleanup scope. |
| Event documentation | `docs/events/026_black_friday.md` and `docs/events/026_black_friday/overview.md` | Current event docs were checked and left unchanged; their bounded adapter and flat-MIO-blocker wording is consistent with the reconciled registry. |

## Exact count corrections

| Evidence statement | Before in current-status prose | After current source snapshot | Source anchor |
| --- | --- | --- | --- |
| Chaos Redux custom triggers | 2,205 across 77 files | 2,224 across 81 files | `event26_cost_surface_custom_inventory.md` current scan table and source scan |
| Chaos Redux custom text | 2,206 across 77 files | 2,225 across 81 files | `event26_cost_surface_custom_inventory.md` current scan table and source scan |
| Native decision costs | 1,321 across 60 files, with 1,038 non-zero and 283 zero/free | 1,328 across 62 files, with 1,033 not written as literal `cost = 0` and 295 literal zero/free | `event26_cost_surface_native_inventory.md` and current source scan |
| Bounded owner-adapter components | 76 across seven tranches | 104 logical components across ten tranches | `event26_cost_surface_registry.md` family summary and current owner handoff |
| Registry bounded component subtotal | 77 components, including 41 reachable Fury components | 104 logical components, including 42 reachable Fury components | Reconciled `event26_cost_surface_registry.md` family summary and current owner handoff |
| Nuclear-bomb owner paired declarations | Registry discovery prose said 67, Appendix A said 62, and the current parent status said 62/62 | 63 trigger and 63 text declarations | Exact custom inventory row and current source scan |
| Registry Appendix A owner counts | `025_alien_technology_in_antarctica_decisions.txt` was 36 and `032_missiles_decisions.txt` was 34 | 025 is 41 and 032 is 26 | Exact custom inventory rows and current registry Appendix A |
| Registry Appendix A owner coverage | 77 owner rows totaling 2,203 trigger declarations | 81 owner rows totaling 2,224 trigger declarations, including Brilliant Scientist biological operations (4), containment (8), portal containment (1), and technology actions (8) | Current source scan, exact custom inventory, and reconciled registry Appendix A |
| Fury custom-cost consumer list | Current localisation handoff said 18 consumers and included a non-consumer `generic core` entry | 17 consumers, matching the current Fury source file and bounded 42-component tranche | `common/decisions/007_fury_decisions.txt` and reconciled `localisation_final_audit_current.md` |
| D'Rhondan alien-reserve row | Omitted from current bounded lists and marked `blocked_pending_owner_adapter` in the exact inventory | One bounded source-adapter row with `source_adapter_bounded_pending_live` status | Registry BF-ALIEN-001, Appendix A, and current owner source handoff |
| MIO assignment and policy costs | Some current handoffs described four native country dynamic-modifier fields | Engine-inaccessible and blocked; Event 26 installs no MIO flat fields or generic confirmation adapter | Registry BF-ABS-002/004, Part 8 BF-F17, and current source inspection |

## Plan and handoff disposition

| File or group | Disposition | Cleanup result |
| --- | --- | --- |
| `event26_cost_surface_registry.md` | Current source-of-truth; patched | Corrected nuclear-bomb discovery, the bounded 104/42 subtotal, and Appendix A coverage/counts, and promoted the D'Rhondan, Random Faction, and Africa rows to bounded source-adapter-pending-live status. |
| `event26_cost_surface_custom_inventory.md` | Current exact inventory; patched | Corrected the D'Rhondan row status and bounded-tranche narrative; declaration totals and line inventories remain source evidence. |
| `event26_cost_surface_native_inventory.md` | Current exact inventory; unchanged | Its 1,328/62/1,033/295 snapshot was already current. |
| `event26_design_modifier_inventory.md` | Current source evidence; unchanged | No stale Event 26 count or status claim was in the cleanup target. |
| `event26_part8_acceptance.md` | Current acceptance ledger; patched | Corrected the evidence date, BF-F17 MIO disposition, bounded adapter list, and 2,224 blocking aggregate. |
| `completion_final_audit_current.md` | Current completion handoff; patched | Corrected counts, adapter list, native/MIO wording, Part 8 references, and read-only Event MCP artifact references. |
| `decision_mission_cost_audit_current.md` | Current decision/mission handoff; patched | Corrected counts, nuclear row, bounded tranche total, helper-callsite wording, MIO disposition, and read-only Event MCP artifact references. |
| `owner_adapter_tranche_current.md` | Current owner handoff; patched | Corrected the ten-tranche/104-component scope, added D'Rhondan, Random Faction, and Africa source paths, and corrected both exact inventories. |
| `event26_parent_implementation_status.md` | Current parent status; patched | Corrected counts, native breakdown, nuclear 63/63, D'Rhondan coverage, and MIO blocker wording. |
| `localisation_final_audit_current.md` | Retained bounded audit; patched and explicitly superseded where needed | Corrected the 44-key inventory, 17-consumer Fury list, Event Details consumer path, terminal-Fury blocker, and stale GUI-render interpretation, while preserving historical artifact references. |
| `localisation_patch_audit_2026-09-02.md` | Current specialist handoff; unchanged | Promoted as the current source-level localisation and bounded visual-evidence reference. |
| `event26_asset_audit.md` | Current asset audit; unchanged | Asset manifests and visual evidence were not edited; this cleanup records no new asset completion claim. |
| `2026-09-02_event26_spreadsheet_handoff.md` | Current specialist handoff; unchanged | Workbook evidence remains outside scope and no spreadsheet or CSV file was touched. |
| `cbrn_diplomacy_adapter.md`, `cbrn_doctrine_adapter.md`, `cbrn_occupation_adapter.md`, and `genocide_crisis_adapter.md` | Rejected or blocked owner tranches; unchanged | Their unsafe partial-adapter findings and exact blockers remain represented by the registry. |
| `germany_mengele_adapter.md` and `architect_universal_cost_framework.md` | Historical or owner-specific supporting handoffs; unchanged | Their source evidence remains subordinate to the current registry and owner-adapter handoff. |
| `completion_baseline.md`, `completion_final_audit.md`, `decision_mission_cost_audit_final.md`, `localisation_baseline.md`, `localisation_final_audit.md`, `probability_baseline.md`, and `probability_final_audit.md` | Historical records; unchanged | Their dated counts, artifacts, and incomplete findings are preserved and are not promoted as current completion evidence. |
| `scripted_system_architect_mio_followup.md` | Historical conflicting handoff; unchanged | Its dated 2,175-count and native-MIO-route statements are retained as historical evidence only and do not override the current registry. |
| `generated_report_art.md`, `icon_art.md`, `spreadsheet_worker.md`, and `spreadsheet_final_audit.md` | Supporting asset or spreadsheet handoffs; unchanged | No stale current count or completion claim required a documentation-only patch in this scope. |
| Event 26 prompts under `docs/specs/026_black_friday_specs/` | Accepted design instructions; unchanged | Targeted scans found no stale source counts; their completion requirements remain goals, not evidence that the goal is complete. |

## Contradictions resolved

- Current custom and native aggregate counts now agree with the 2026-09-02 exact source scans.
- The current registry and exact inventory now agree that the nuclear-bomb owner has 63 paired trigger and text declarations.
- The registry Appendix A owner counts now match the exact inventory for the previously stale `025_alien_technology_in_antarctica_decisions.txt` (41) and `032_missiles_decisions.txt` (26) rows.
- The registry Appendix A now includes all 81 current Chaos Redux custom-cost owner files and its trigger total reconciles from 2,203 to 2,224; the four Brilliant Scientist rows remain blocked pending owner evidence, including the eight technology-action pairs newly added to the current scan.
- The current localisation handoff now lists the 17 actual Fury custom-cost consumers and removes the stale `generic core` entry.
- The current registry, exact inventory, owner handoff, parent status, and Part 8 acceptance record now include the D'Rhondan alien-infantry landing reservation as one bounded source adapter pending live evidence.
- The current bounded total is consistently recorded as 104 logical components across ten owner tranches, including 42 reachable Fury components, 21 Random Faction components, and five Africa Elephant components.
- BF-F17 and the current MIO statements now match the registry and source inspection: MIO assignment and policy costs remain engine-inaccessible, with no Event 26 flat MIO fields or generic confirmation adapter installed.
- The current Event MCP references now identify the 2026-09-02 focused partial inspect and overview render, with deferred helper/lifecycle analysis and no full event evidence claim.
- The retained localisation audit now points current visual interpretation and terminal-Fury status to the 2026-09-02 specialist patch handoff.

## Contradictions still open

- The historical `scripted_system_architect_mio_followup.md` still contains the older 2,175 aggregate and native-MIO-route wording, but its date and historical disposition prevent it from serving as current evidence.
- The historical probability and completion handoffs still contain older aggregate counts and partial artifacts, but they are explicitly retained as historical records rather than current status.
- The current registry still has unresolved engine-inaccessible and owner-adapter rows for flat leader/tactic, native one-time decisions, equipment-upgrade, guarantee, operation, license-purchase, MIO, special-project, assignable-trait, factory/dockyard/commitment, custom-currency, and remaining owner-adapter surfaces.
- The current Event 26 MCP evidence is partial only, and no full probability comparison, decision-specific display/payment evidence, live game evidence, save/reload evidence, or multiplayer evidence is available.
- The D'Rhondan, Germany Mengele, Fury, Japan chemical, biological medical-capacity, CBRN shelter, Japan biological, and Communist-spread rows remain source-adapter-bounded and live-blocked; their presence is not universal owner completion.

## Duplicate or superseded document list

- `localisation_patch_audit_2026-09-02.md` supersedes the stale visual/MCP and terminal-Fury claims formerly presented as current in `localisation_final_audit_current.md`.
- The `_current` completion, decision/mission, owner, parent, and localisation handoffs are overlapping current ledgers with distinct audit ownership, not files to merge or delete.
- `completion_final_audit.md`, `completion_baseline.md`, `decision_mission_cost_audit_final.md`, `probability_baseline.md`, `probability_final_audit.md`, and `scripted_system_architect_mio_followup.md` remain dated historical records and were not deleted or rewritten.
- No file was deleted because the user did not authorize deletion or archival.

## Stale prompt or instruction list

- No active Event 26 prompt file with stale aggregate counts was found in `docs/plans/026_black_friday_plans/`.
- The accepted goal, coding, asset, and achievement prompts under `docs/specs/026_black_friday_specs/` remain design instructions and contain no current completion counts requiring a patch.
- `scripted_system_architect_mio_followup.md` is a stale dated handoff rather than an active prompt, and it is explicitly not promoted as current.

## Markdown hard-wrap issue list

The scoped Markdown hard-wrap audit found no accidental prose line breaks inside sentences or clauses after excluding headings, lists, tables, block quotes, and fenced code blocks.
No intentional Markdown structure was flattened.

## Recommended parent decisions

- Keep Event 26 disabled and incomplete until the registry, owner adapters, engine-inaccessible surfaces, probability evidence, and live acceptance gates are resolved or explicitly accepted by the parent.
- Decide whether future MIO coverage should use an exact engine-accessible route, a documented exclusion, or a separately approved static strategy; the current documentation records it as blocked.
- Decide whether to run a separate documentation pass over all Event 26 public event pages after any future registry change; the current pages were checked and are aligned with this snapshot.
- Run a fresh scenario-specific probability audit and comparison only when stable before/after owner-weight surfaces and candidate pools are available.
- Obtain the missing live event, decision tooltip, save/reload, refund, multiplayer, and calendar-calibration evidence before any completion claim.

## Proposed cleanup actions if patching is not allowed

No required current-scope patch was left unapplied.
If the parent rejects these patches, mark the listed current handoffs superseded at their headers, retain the exact source inventories as authoritative, and carry the count, MIO, D'Rhondan, and partial-MCP contradictions forward without claiming completion.

## Validation and remaining risk

The source snapshot was independently rescanned from `common/decisions/*.txt` and returned 2,224 custom triggers, 2,225 custom texts, 81 Chaos Redux custom-cost files, 1,328 native cost declarations, 62 native-cost files, 1,033 non-literal-zero declarations, and 295 literal zero/free sentinels.
The current registry Appendix A owner counts and statuses were cross-checked against the exact custom inventory for all 81 listed Chaos Redux owners, including the four Brilliant Scientist rows, corrected 025 and 032 rows, the 63-entry nuclear-bomb row, and the D'Rhondan status.
The focused read-only Event MCP evidence was refreshed for `chaosx.nr26.1`: `EVENT_INSPECTED_PARTIAL` at revision `27c77545e9241b4398d074f7bae0aaedf8ebba6790c26141f6e3508bf4238175` with graph hash `9231a40d3395079e08c9610848afcd4d0fc93e97e2dd33dcff81f5d140de7291`, and `EVENT_RENDERED_PARTIAL` with layout hash `3ea884981b1b4ab3fcaf97c911a7503b65b619f8757e3164f29a88b151b0d96a`.
The stable MCP artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c419c5ab66bbb6aed14324e01de84e2e8e3b0a88d0d31688f52f553279b3f40e/1135c00ddb02b646e0ff5a8e3233a6145bee2f878960d0aecd091da367b3bf66/event-lint-27c77545e924.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a946624da9c7623a7d5ef11c3a7fe3ce41656a18ec8c0b34c61957e5306a543/de553855fd2e77b036bc7415ed9c1c3f83c334c7b1732a50b094d694909fee88/event-overview-27c77545e924-manifest.json`.
A fresh read-only probability source inspection of `events/026_black_friday.txt` with the `event_option_ai_chance` adapter returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = true`, one discovered candidate, zero available candidates, zero required inputs, and zero unresolved inputs at source revision `a477c32d9183b75725e09db4c376b6207faf6cfb97047b2b577b89c455cf75d5`. Its source hash is `135da139b2368e30cf374cdcb389692bc649162f9bf7409dab57350a090b0995`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eab86ce19d442fff7e62eb716544540fad3d998f002fa2a3e2277514a31d133/155fd9cbd71664a2568e3ccef139b912d4a1ae58c6466b419a6c2a883932a2e4/probability-inspect-135da139b236.json`.
No full MCP probability or event evidence is claimed, and no probability comparison was run because no stable before/after owner-weight surface exists.
The implementation worktree remains dirty and unfrozen, and all live, owner-coverage, engine-inaccessible, calendar, and probability blockers remain the parent’s responsibility.

No gameplay completion claim is made by this handoff.

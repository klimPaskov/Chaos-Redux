# Biological Stockpile Safety Documentation Reconciliation

Date: 2026-09-26.

## Scope and disposition

The only edited system document is `docs/systems/cbrn_warfare/biological_warfare/biological_stockpile_safety.md`. This handoff is the only other file created. No gameplay, localisation, GFX, asset, spreadsheet, or other documentation file was edited, and no commit was made.

The parent supplied the accepted CBRN overhaul decision for this bounded task: remove human-facing arsenal designation and staging decisions, retain native Biological Raids for recovery, and allow exact-state internal safety pointers. The system document is **implemented as a source-reconciled description** under that instruction. This disposition applies to the document, not to gameplay completion or live-engine validation.

## Current source-of-truth map

| Claim | Acceptance basis or evidence | Status and limit |
|---|---|---|
| No player-facing arsenal designation or staging action | Parent-supplied accepted CBRN overhaul decision; no active `bio_designate_national_biological_arsenal` decision or localisation in the inspected source | Accepted design and source-aligned; other historical docs still disagree. |
| First qualifying project facility registers an exact pointer | `common/special_projects/projects/biowarfare_main_projects.txt` `facility_state_effects`; `common/scripted_triggers/biological_stockpile_safety_triggers.txt` pointer checks | Source behavior; a scripted completion with no supplied facility and no prior designation history remains unregistered. |
| Due-event repair can select a replacement | `events/biological_stockpile_safety_events.txt` `cbrn_bio_safety.1`; `common/scripted_effects/biological_stockpile_safety_effects.txt` `bio_stockpile_safety_reselect_arsenal_if_needed` | Source behavior; selects a random eligible owned and controlled operational facility only after prior designation history. |
| Risk bands use ordered explicit gates | `common/scripted_effects/biological_stockpile_safety_effects.txt` `bio_stockpile_safety_refresh_risk_band`; `common/scripted_triggers/biological_stockpile_safety_triggers.txt` band conditions; `common/script_constants/biological_stockpile_safety_constants.txt` | Source behavior; no verified player-facing score or risk idea. |
| Targeted stockpile monitor and accident dispatch | `events/biological_stockpile_safety_events.txt`; `common/scripted_effects/biological_stockpile_safety_effects.txt` selection, debit, and lifecycle helpers | Source behavior; probability and runtime timing need scenario evidence. |
| Exact captured-site recovery through native raids | `common/on_actions/biological_facility_capture_on_actions.txt`; `common/scripted_effects/biological_facility_capture_effects.txt`; `events/biological_facility_capture_events.txt`; `common/raids/biological_facility_recovery_raids.txt` | Source behavior; native target presentation on an enemy-owned state controlled by the actor is still unverified. |
| Raid asset consumers | `common/raids/biological_facility_recovery_raids.txt`; `interface/chaosx_raids.gfx`; the two target DDS paths exist | Source and file evidence; no active arsenal designation sprite consumer was found. |

## Plan and handoff dispositions

| Document | Disposition | Evidence or reason |
|---|---|---|
| `docs/systems/cbrn_warfare/biological_warfare/biological_stockpile_safety.md` | Implemented as source-reconciled documentation | Current source files above and the parent's accepted CBRN direction; engine and live-game limits remain open. |
| `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-19_biological_stockpile_safety_architect_handoff.md` | Unresolved as a current implementation guide | Historical helper handoff still asks for player-selected designation and says the helper never scans for a replacement; current due-event repair does select a bounded replacement. Retain it as provenance until the parent names a superseding guide. |
| `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-19_biological_stockpile_risk_idea_icons_handoff.md` | Superseded for runtime asset status by the system document and current GFX inventory | Its generated-asset provenance remains historical, but its statement that the designation icon remains active is contradicted by the absent consumer. |
| `docs/systems/cbrn_warfare/biological_warfare/captured_biological_facility_recovery.md` | Implemented as source-reconciled documentation by the parent concurrently | The parent replaced its explicit player relocation sequence with project registration and bounded internal repair while this handoff was being prepared. It remained outside this subagent's write scope. |
| `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-22_biological_captured_facility_runtime_handoff.md` and `2026-07-22_biological_captured_facility_scenario_audit.md` | Source evidence with unresolved engine scenario | Both describe native raids and exact capture accounting; their historical references to explicit manual relocation do not establish a current player action. The enemy-owned raid-target presentation limit remains. |
| `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-08-21_ai_probability_audit.md` | Blocked as a current probability conclusion | It recorded MCP transport failure and inventories the now-absent designation decision. Its named scenarios `prepared_route`, `unprepared_route`, `defensive_route`, `no_valid_target`, `low_stock`, `high_penalty`, `special_excluded_tag`, and `mastery_route` remain the prior handoff's scenarios, not verified current probabilities. |

No source spec was promoted or rewritten. There was no acceptance basis to promote historical manual-designation instructions, and a current source file does not by itself approve new design.

## Contradictions, stale instructions, and duplicates

- The old stockpile safety page claimed a manual `bio_designate_national_biological_arsenal` decision, no state reselection, paused monitoring on a disabled facility, ranked AI designation, and an active decision sprite. The revised page removes those claims because the inspected source contradicts them.
- The captured-facility document initially implied player designation and deliberate replacement. The parent corrected that contradiction concurrently; its current capture sequence describes verified project registration and bounded internal repair.
- The 2026-07-19 architect handoff's migration instruction to add a player-selected caller and its categorical no-replacement statement are stale. Its reusable helper and asset-provenance evidence remains useful, so the file was left intact.
- The 2026-07-19 icon handoff's runtime retirement notice and remaining-action list still call the designation icon active or ask for its wiring. Current `interface/biological_warfare.gfx` has no such sprite, and the decision file is absent.
- The 2026-08-21 AI audit names `common/decisions/biological_stockpile_safety_decisions.txt`, which is absent. Treat that line as historical inventory, not current coverage.
- No duplicate document was safely mergeable inside the assigned write scope. The related captured-facility document retains distinct raid detail and remains separate after the parent reconciled its relocation language.
- No prompt file was named by the parent or opened in this bounded pass. No claim is made about prompt freshness elsewhere in the repository.

## Markdown hard-wrap audit

The former `docs/systems/cbrn_warfare/biological_warfare/biological_stockpile_safety.md` split prose sentences and list items across physical lines. Its revised prose uses one physical line per sentence or paragraph while preserving headings, paragraphs, and table rows. `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-07-19_biological_stockpile_risk_idea_icons_handoff.md` still contains mid-sentence wraps in its historical retirement notice; it was outside the assigned patch scope and remains unchanged.

## Read-only MCP event evidence

Exposed event tool names were callable and both narrow inspections returned `status: ok` with `EVENT_INSPECTED_PARTIAL` at source revision `02a6322d0ab69e8bc7dcf76ef4e0bcefe6f1c7faefc5753b8d703069afb2347e`. The connected service returned artifacts, which verifies this route worked for these requests; it does not establish complete helper or lifecycle coverage or a standalone viewer.

- Targeted monitor trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7354aabc5ac005dc9c3bbf139b5909c28a80bfecf10f6aa1f8804e60f34480f/9f2ca3242ed4b30a77e195a8e6fce3a3a9ecfaf5f7bb4120098405d6e4365018/event-trace-02a6322d0ab6.json`.
- Targeted monitor neighborhood JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1ebba1ee9cb0081698d08c987470713ba66c026c93a0677880dd1d85ab22a00/7c7d11755ce7b16faff24af4b337f3b9947dbf7985d4b7ed50a1e2434a51a415/event-neighborhood-02a6322d0ab6.json`.
- Captured-facility event trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5fd563082592010a2c3a3e92c238ed7999504fdc6112831a9da7460fa4869dd/35710818b13c6b858944039d19b3ebcfe43217311c53438486c61a58e1efd0fb/event-trace-02a6322d0ab6.json`.
- Captured-facility hidden hazard neighborhood JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/800716224cce481fb4258c12424f7c28aa90ceac3b77a3c4fa8275aa360dd4af/107c8f899e3b0980dab054058aadfca9e959bee04de5689c0c24b8d84ef88e3a/event-neighborhood-02a6322d0ab6.json`.

Both renders returned `EVENT_RENDERED_PARTIAL` and `validation.passed = false` because large-workspace helper projections and lifecycle passes were deferred. They are structural source-linked evidence only.

## Scenario-specific probability handoff

The read-only `chaosx_ai_probability_auditor` returned no source edits and no exact, bounded, or sampled probability result. Its current evidence supersedes the absent-service inference in the August audit for this narrow surface: `hoi4.probability_inspect` worked, while the requested scenario evaluations remained unresolved. Tool exposure alone did not prove a usable evaluate route for each pool.

| Surface and named scenarios | MCP result | Classification |
|---|---|---|
| Monitor incident/no-incident `random_list`: `monitor_controlled_low_stock`, `monitor_critical_high_stock` | Inspect found two local candidates and `poolComplete=true`, but both evaluations returned `INTERNAL_ERROR: Unexpected internal error`. No scenario hash or numeric trace was produced. | Unresolved. |
| Agent selection: `agent_valid_low_stock`, `agent_valid_high_stock`, `agent_invalid_no_available_stock` | Evaluation isolated four candidates and returned `PROBABILITY_ANALYZED_PARTIAL`; `VALUE_UNRESOLVED` remained for the `var:bio_stockpile_safety_available_*_weight` expressions because flat scenario state did not bind those Clausewitz variables. | Unresolved. |
| Severity selection: `severity_controlled`, `severity_critical_high_stock`, `severity_invalid_no_inputs` | The effects inspection found two categorical pools with nine entries and `poolComplete=false`; the isolated severity evaluation returned `INTERNAL_ERROR: Unexpected internal error`. | Unresolved. |
| Native recovery raid AI: `raid_captured_high_hazard`, `raid_defensive_handler`, `raid_unrestricted_handler`, `raid_invalid_no_target` | The installed probability adapter returned `no_weighted_surfaces` and no raid `ai_will_do` candidate; the full raid choice pool and external factors were not exposed. | Source-score only for the scripted factors; normalized choice and target resolution unresolved. |

The auditor's event-pool inspection revision was `58337bd0b0926fbf21775811ab0f4e14cdbe4198cc66c6040aa30009181d533a` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b074d9df795d1d99f3dadcc959ad48412ff1a0cbb77ed8d5a64c3a13c894657/bc7203d220f69642e3991a0df154cb9e903818f1220391cf32342e32ef3af731/probability-inspect-a45605302994.json`. The agent-pool partial analysis ID was `probability-af943b56b1ad94fbfa454210`, scenario hash `fdb29494d7ea339838a279e98db039371e308b031d201421bc3bee2779f10882`, and JSON artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/710e78bbb448860f80b754f79be40111dcdc3292485da091a057799532b15e70/3b29f10d4ea5c1366f578a6fbf9d0d0bc00c4ec9ffc238e61bebbd38f53e53bc/probability-af943b56b1ad94fbfa454210.json`. The isolated effects inspection revision was `94c5ba8c9f07a1d439093685068e2336aafe85f9887951ee866054364febddb2` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f677a28a49e3b9ca1efad31fd2cca022cf713c90014786a17ec536e4537f8db5/55157205303711f0d6112618361723335f04a455fc8268bc126348823247e88d/probability-inspect-56d2a6d33658.json`. The raid inspection revision was `63c63a799d8f7b1169627e50133f1ac1190986172db38df9acb9a397caa29523` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ff8ed497dbc71bd94d2f5e606d0ef88cd941e820b95031f48f532935e8cb3e7/1a88c89adabbc04431ef39e404729630de718345c08eeebf030501f035742c0e/probability-inspect-bedba6da0a2d.json`.

`probability_sweep` was skipped because the variable weights could not be resolved, and `probability_compare` did not apply because no weighted source was patched. An attempted render returned `PROBABILITY_ANALYSIS_NOT_CACHED` for the partial agent analysis; the evaluate response itself supplied an unresolved SVG artifact. The source-defined monitor incident/no-incident and severity weights are not presented as verified overall odds because the monitor gates, agent cooldown exclusion, conditional draws, and missing engine trace affect the result.

## Validation and remaining parent decisions

The relevant offline Paradox wiki core pages, installed vanilla effects/triggers/script-concept documentation, installed raid documentation, and a vanilla land-raid precedent were consulted before editing. Targeted searches confirmed the removed decision and sprite have no active consumer, the recovery raid definitions and DDS targets exist, and the revised page no longer presents ranked designation AI or a paused monitor on a damaged facility. A focused diff review confirmed only the assigned system document changed before this handoff was added.

The parent has reconciled the captured-facility document's explicit relocation sequence. The remaining documentation decisions are whether to mark the icon and architect handoff runtime instructions historical and whether the orphaned `bio_stockpile_safety_ai` and `bio_stockpile_safety_designation` constants should be removed in a gameplay-owned patch. The parent should also review the repair path's two scheduled-event writes: `bio_stockpile_safety_reselect_arsenal_if_needed` can call `bio_stockpile_safety_start_monitor` before `cbrn_bio_safety.1` schedules its regular next event, leaving an earlier event that the due-day guard appears designed to make inert. This is a source-level observation, not a verified runtime defect.

Parent resolution: removed the repair helper's `bio_stockpile_safety_start_monitor` call in the same tranche. The due event now owns its next scheduled check, while initial project registration still starts the monitor. Focused pre- and post-edit MCP traces were partial, so exact runtime cadence remains unverified.

Meaningful live-game raid targeting, event cadence, incident odds, AI route choice, and end-to-end capture validation were skipped because agents do not run HOI4 and the partial MCP event and probability results do not prove them. No completion claim for the CBRN package is made.

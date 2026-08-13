# Event 018 decision and mission final current audit

Date: 2026-08-09. Scope: current Event 018 decision categories, decisions, missions, field commitments, cave and anti-cave responses, target lifecycle, cleanup, AI source coverage, and decision-owned GUI integration. This audit was recovered after the prior decision auditor failed to leave its final handoff. The current shared Event 018 sources were inspected in place. Concurrent provider additions in `common/scripted_effects/018_resources_found_cave_effects.txt` were preserved and were not reverted or redesigned.

## Verdict

**CONDITIONAL PASS.** The decision and mission implementation is materially complete and the previous exact-cost, target-lock, cleanup, localisation, and exploit repairs are present in the current source. The parent resolved the field-category action-density warning through the field-persistent workboard disposition recorded below. Engine-weight evidence remains conditional because the installed probability adapter cannot type every full campaign predicate or prove complete normalized campaign selection. The event and GUI MCP routes returned source-linked partial/complete artifacts with no Event 018-local blocking diagnostic, but the workspace/global graphs retain unrelated diagnostics. This handoff does not claim live gameplay or AI execution.

## Required references and evidence boundary

- Read and applied `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.
- Consulted the Event 018 source specification package under `docs/specs/018_resources_found_specs/`, including all eight sequential parts, `matrices/decision_mission_matrix.md`, `matrices/ai_strategy_matrix.md`, `matrices/tuning_and_balance_framework.md`, `matrices/acceptance_criteria.md`, and the cave focus architecture.
- Consulted the required offline Paradox wiki decision, trigger, effect, modifier, localisation, scope, on-action, event, idea, AI, interface, and scripted-GUI pages. Vanilla decision and mission precedent and the installed documentation were used through the earlier final decision handoff, including `documentation/decisions/_documentation.md`, `script_concept_documentation.md`, `triggers_documentation.md`, and `effects_documentation.md`.
- Reused the completed probability handoff at `docs/plans/018_resources_found_plans/subagent_handoffs/event018_probability_final_current_2026-08-09.md` as required. No second probability auditor was spawned and no weighted source was changed here.

## Current decision category lifecycle

| Category | Current lifecycle and cleanup result |
| --- | --- |
| `resources_found_field_management_category` | Visible for an owned active field or a valid closed-history record, with `resources_found_field_scripted_gui` attached. Active actions use the selected-field pointer. Closed history is read-only and cannot re-enter the active registry. Invalid or lost selected fields are reselected or cleared by the shared registry helpers. |
| `resources_found_trade_and_security_category` | Visible for a valid foreign actor or an owner with a live contract, foreign interest, or sufficient pressure. Targeted partner actions store the exact partner and cancel when that partner, route, field, or contract becomes invalid. It hides when no trade/security context remains. |
| `resources_found_containment_category` | Opens for revealed disturbance, breach, or an active full-seal state. It retains mission status during a crisis while ordinary projects are gated by field stage, suspension, control, supply, and equipment. Closure or terminal conversion removes obsolete actions and runtime pointers. |
| `resources_found_cave_brood_network_category` | Restricted to the living flagged `DHO`/Oth-Kesh cave country through `is_resources_found_cave_country` and `resources_found_cave_country`. Target, anchor, queue, doctrine, continent, and rupture projects use exact state or route locks and clear on loss, defeat, or terminal transition. |
| `resources_found_anti_cave_response_category` | Restricted to ordinary countries with a live cave threat, eligible aid/reconstruction context, or the defined post-defeat contribution state. Anchor, aid, denial, and restoration targets are revalidated and cleared when the threat, state, or recipient disappears. Reconstruction is one-shot after the required cleanup evidence. |
| `resources_found_hidden_clock_category` | `visible = { always = no }` and `visible_when_empty = no`. The nine evolution/reschedule missions are activated by effects and never leak into the rendered decision list. |

## Phase and category coverage

### Field management

The current field category covers navigation and estimate refresh, administration (`resources_found_establish_national_authority`, `resources_found_charter_domestic_operators`, reserve), appraisal (`resources_found_commission_geological_appraisal`, `resources_found_drill_deeper_test`, `resources_found_map_surrounding_basin`), development (`resources_found_open_primary_works`, `resources_found_extend_rail_road_corridor`, `resources_found_install_heavy_machinery`, `resources_found_build_local_processing`, `resources_found_expand_worker_settlement`), compound-field actions, labour and safety, extraction modes, suspension/reactivation, and exact closure. The project runner `resources_found_field_project_mission` stores field, kind, family, profile, exact days, and cost context rather than reading a mutable selected field at completion.

### Trade, pressure, and border/commission

The trade category covers foreign concessions, bids, export contracts, buyer balancing, domestic reservation, concession surge, nationalization, compensation, guards, counter-survey, smuggling, controlled demolition, transfer review, and contract review. Foreign-facing actions cover purchase requests, development assistance, exclusive rights, access guarantees, field pressure, smuggling, sabotage, and withdrawal. Border coverage includes claimant naming, arbitration, field administration, frontier corridor, commission creation, demilitarization, observation, compliance restoration, dissolution, limited border war, escalation/cancellation, and settlement. Claimant and partner targets are valid only when the state, country, route, and dispute context are live.

### Evolution II and III containment/closure

The containment category covers air/water testing, lower-work evacuation, armed underground sweep, scientific/military survey, restricted workings, transport corridors, perimeter reinforcement, surface hunts, urban clearing, settlement/state-center evacuation, foreign hard-attack aid, access-network sealing, partial closure, full sealing, last emergency seal, and ordinary exact closure. Hunts require real supplied forces and anti-armour/equipment inputs. Evacuation and corridor actions use transport, routes, receiving capacity, and timed objectives. Partial closure lowers danger but does not set the Evolution IV prevention flag. Full sealing requires suspension, control, civilian/worker safety, containment, engineering, and exact removal of Event 018 resources before setting permanent prevention.

### Cave country and anti-cave response

The cave category covers rich-state marking, anchor activation and acceleration, feeding-chamber guard, spawn-template choice, origin-brood replacement, unfed-brood consolidation, tunnel links, Stone/Burrow/Scree actions, industrial conversion, origin fortification, queue refresh, continent objectives, verification, and world-end rupture preparation. It does not expose ordinary training or equipment purchases. The anti-cave category covers emergency anti-armour contracts, denial before anchor loss, liberation and mature-anchor clearing, hard-attack intelligence, evacuation corridors, threat cooperation, aid to a live recipient, liberated-resource restoration, and reconstruction. This preserves AI-equivalent normal decision/effect paths for the human-only field GUI.

## Mission quality audit

Current source has **12 visible non-clock missions** and **9 hidden evolution/reschedule missions**. The older handoff's count of ten visible missions is stale.

| Mission family | Owner and category | Region/requirement | Duration | Success | Failure/cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| Field/trade/containment/cave/anti-cave project runners | Matching owner category | Exact locked field, state, recipient, or partner plus cached cost context | Family/profile duration from the centralized calculator | Route-specific completion helper | Invalid owner, field, state, route, threat, or partner clears runtime and cancels | Low, family-specific runners |
| `resources_found_contract_term_mission` | Trade owner | Locked field, owner, and partner must remain the launch contract | `resources_found_contract_term_days` | Contract-term completion | Partner/field/war/route failure helper | Low |
| `resources_found_frontier_corridor_mission` | Trade owner and claimant | Named owner/claimant border states, supplied divisions, route control | `resources_found_frontier_mission_days` | Corridor leverage helper | Pair invalidation or timeout settlement failure | Low, distinct map objective |
| `resources_found_commission_observation_mission` | Commission owner/claimant | Locked commission field and observation context | `resources_found_commission_observation_days` | Observation completion | Commission invalidation or timeout | Low |
| `resources_found_dispute_settlement_stability_mission` | Border settlement owner | Locked field and claimant settlement context | Stored settlement duration | Settlement qualification | Invalid claimant, field, or timeout failure | Low |
| `resources_found_border_war_limit_mission` | Owner and claimant | Stored owner state, claimant state, claimant country, and limited-war context | Exact stored 240-day conflict limit | Moves the dispute to settlement when the limited war ends | Timeout cancels the limited war and clears all border runtime | Low |
| `resources_found_burrow_objective_window_mission` | Cave country | Exact defended capital, supply hub, or fortification state | `resources_found_burrow_objective_window_days` | Captured-objective chain consumes the target | Target loss/timeout clears objective runtime | Low |
| `resources_found_liberate_activating_anchor_mission` | Ordinary defender | Exact activating anchor state, supplied forces, and live DHO control | `resources_found_anchor_recapture_days` | Interrupts activation and records liberation | State/war/timeout clears pointer and duration | Low |
| Evolution pre-fire/active clocks and rescheduler | Hidden clock category | Per-evolution field validity, owner, closure, enabled settings, and later-stage gates | Dynamic scripted MTTH values plus one-day reschedule mission | Calls the matching evolution/pre-fire helper | Closure, disable, invalid state, or timeout cancels the matching clock | Low, one clock per progression state |

No mission is a passive stockpile, manpower, stability, or wait-only checklist. The visible objectives require field/state control, supplied forces, route control, evacuation, partner persistence, anchor recapture, or explicit project completion.

## Issue list, sorted by severity

### Resolved parent disposition: field action density

The parent added five field-persistent workboard pages: Administration, Development, Infrastructure, Safety, and Operations. Each page has one navigation action plus five or fewer normal player actions. The Operations page permits at most five routine controls plus navigation; recorded casualties replace routine controls with compensation, concealment, and emergency suspension, while a suspended field replaces routine controls with reactivation. AI countries bypass every page and incident-presentation gate, so the valid weighted project pool is unchanged. Static current-source counts are 5 page-gated actions for Administration, Development, Infrastructure, and Safety, and 8 total Operations actions partitioned into four routine and four casualty/suspension actions; no player state can expose more than six actions including navigation.

### Medium MCP evidence limitation: complete decision probability is unresolved

The required probability handoff reports 113 decision candidates and 24 required inputs, but the adapter cannot type the complete owner/control/selected-field/contract/evolution/cost/cooldown target predicates for a normalized world pool. The retained decision inspect is source-clean, while bounded score evidence is not a click probability. This is an evidence limitation, not a proven AI-balance defect. Reuse `event018_probability_final_current_2026-08-09.md` and do not infer normalized choice probabilities.

### Low MCP event projection limitation

The refreshed Event 018 namespace/file event scans returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics, but the repository-size adapter deferred workspace-wide helper and delayed-delivery lifecycle projection. The source-linked reports therefore do not prove saved-scope recovery or live delayed-event delivery. Current artifact references are retained below.

### Low GUI/global diagnostic limitation

The final selected-field GUI artifacts report no Event 018-local overflow, clipping, click-region, missing asset, localisation, or resolution defect. The current whole-workspace `gui_inspect` still reports global index/overlap diagnostics from unrelated files and truncates the diagnostic ceiling. The recovery render completed with `GUI_RENDERED` and only a wire-budget warning. No GUI rewrite was needed or attempted in this audit.

### Low concurrent provider-scope note

The current working tree appends an Event 019 provider adapter to `common/scripted_effects/018_resources_found_cave_effects.txt`. It is concurrent provider work and was not reverted. This audit did not redesign that adapter or claim its separate Event 019 contract as decision validation. Parent should include it in the broader integration review.

## Cost and requirement clarity

- The current exact-preview ledger maps all **100 priced decisions** to a real family/profile/base duration. The prior mapping audit reports `PRICED=100`, `MISMATCH=0`, and all 100 custom affordability triggers match their profile/family.
- The calculator rounds and zero-clamps political power, command power, army XP, manpower, civilian/military capacity, infantry/support/anti-tank equipment, trucks, trains, convoys, fuel, and duration before display, affordability, cache, and payment. The frontier mission and limited border war expose their computed/stored duration rather than a generic timer.
- Forty referenced exact-cost localisation sets have base, `_blocked`, and `_tooltip` forms with no missing keys. Nonstandard requirements are summarized and detailed through custom tooltips. Free actions are navigation, policy, cancellation, or callbacks rather than repeatable resource/unit reward loops.
- State-target decisions use explicit `FROM` scoping and lock the exact state in `resources_found_active_response_state`; country targets remain direct targeted decisions. Completion revalidates the locked target rather than trusting the mutable selected-field pointer.

## AI validity and route-lock notes

- Every clickable non-mission decision has an `ai_will_do` block. Field-owner AI varies posture, investment, safety, closure, rush, and concession behavior by war, country scale, stability/safety, foreign pressure, field values, and valid target context.
- Foreign and claimant AI actions require live partner/claimant, route access, valid border, and non-terminal/nonhuman target conditions. Cave AI prioritizes resource-rich targets, anchors, origin protection, capacity recovery, doctrine actions, and continent objectives. Anti-cave AI uses the same decision/effect families as human actions and requires live DHO threat/state/recipient context.
- The field GUI is intentionally human-only (`ai_enabled = { always = no }`). AI does not depend on selected-field navigation and evaluates the normal decision/effect routes instead.
- The retained probability evidence is conditional. Exact bounded evidence exists for the two-candidate pre-fire pool (60/40 supports) and the complete cave-brood pool (default 50, Stone 15, Guard 5 when unlocked). Focus, event option, decision, mission, MTTH, direct-random, and strategy-factor campaign claims remain partial or unresolved due incomplete pools and typed-runtime adapter limits. No weighted source was changed here, so no new compare pass was applicable.

## Localisation and tooltip gaps

No Event 018 decision or mission localisation gap was found in the current audited surface. The previous scoped checks report 12 visible mission title/description pairs, dynamic exact-cost text, blocked-cost/tooltips, category strings, and GUI text coverage. Integer values use integer-oriented scripted localisation. Raw trigger blocks are not exposed as player-facing requirement text. The hidden clock category intentionally has no rendered mission text requirement because it never renders.

## Cleanup and exploit-risk notes

- Shared runtime cleanup clears selected field, active field/project variables, pending partner, target state, contract/commission/claimant references, active missions, disturbance/breach targets, closure state, cave origin/anchor/queue/capacity variables, and world-end candidates when their owner, state, target, route, war, or terminal context disappears.
- Cave denial persists through interrupted activation attempts. The accepted contract adds the tuned 30-day delay per attempt, applies the one-shot capacity penalty only on successful activation, clamps it at zero, then clears the prepared denial and penalty. Recapture interrupts activation without consuming geological reserve or the Event 018 ledger.
- Terminal defeat clears `resources_found_cave_spawn_state` with the other persistent cave targets. `resources_found_deep_survey_complete` is the single deeper-survey marker. Successful `seal_access_network` clears `resources_found_unsealed_nest`. Reconstruction `.99` is one-shot and requires global-defeat eligibility, contributor evidence, three cleanup contributions, no cleanup state, and no live threat.
- No free unit/equipment/factory/core/claim/war-goal/cooldown loop was found in the current decision-owned source. Repeatable actions pay the exact cached ledger or require a fresh valid project context.

## MCP evidence and blockers

### Event chain

- Reused current Event 018 event evidence: namespace scan `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62c9fec699b991370524339b03e190f6d6bfeb78643095cab53d39da42f779eb/f1dc3a093411c304e1679770c7f21a1499181a07d68e12b72ac8faf67743b16c/event-scan-8c2577b32af5.json`. Focused state-flow artifacts cover `.1`, `.40`, `.50`, `.60`, `.80`, `.85`, and `.98` as listed in `018_current_mcp_validation_2026-08-09.md`.
- Recovery `hoi4.event_inspect` also returned `EVENT_INSPECTED_PARTIAL` at revision `550da12aba6a66219fd9c18d562b6ffe63db4870cd36848223b6f0e39744cbd4` with no blocking diagnostics, but the large workspace projection is deferred. Artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7c88269fca286dabbde343ff2851d9b3e40d4fcebf97dd7f6a4fb13a82f8351/2393bc9f65045e7d182125140f22261a6879af09478158a44e35bcb59adb7388/event-scan-550da12aba6a.json`.

### Decision-owned GUI

- Reused final selected-field evidence from `event018_scripted_gui_visual_fix_handoff.md`: final `hoi4.gui_inspect` artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af65f01433f093d8e876c1a6acb462a7c5b98e7194d5243ea7d2b51619e39121/8865916154548f3bbebe8c7d748681c3f4a068e1ee9f2433a2ae3db9694e973b/gui-inspect.07ea06f0b395f66c.json` and final maximum-content render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c43cdb1bdae94790dd1a56ecf96fb772a3622ba65a87fe01787a907b6b6e81b/c21ccb6ec66cb82ac34db23852951e08a7fe7bd2b6f9d8298abbacf01ed6c38d/resources_found_field_window-full.svg`. Those probes cover 1280x720, 1366x768, 1920x1080, and 2560x1440 plus active/history/empty/full/minimum/maximum/long-text and interactive states, with no Event 018-local defect.
- Recovery `hoi4.gui_inspect` completed with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/265f4cf17d20ead8f3f19f448ed0e6076cba50a0d41edce787f1354776f3b324/142ab392219495d55787715e8d82947ad6044fa139939ef7151d9ca0dbd7d5f3/gui-inspect.355a693b7380f470.json`; its 34 Event 018 elements are present, while global unrelated diagnostics are truncated. Recovery `hoi4.gui_render` completed with `GUI_RENDERED`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65f260e93b8b02003e0d5a02f453a755dbc8582a27ec45fb9de593cac0f4310a/39a14f0e678f7fa51dc733d871cc288b6162a51fa5c9fe5ab1363c554617f4e6/resources_found_field_window-full.svg` (the response was wire-truncated, with the full linked SVG retained). No GUI source change was made.

### Probability

Reuse `docs/plans/018_resources_found_plans/subagent_handoffs/event018_probability_final_current_2026-08-09.md` and its linked inspect/evaluate artifacts. It is **CONDITIONAL**, not a normalized whole-campaign decision probability proof. No second probability pass was run in this recovery turn and no weighted source changed.

## Changed files and identifiers

The parent resolution changed `common/decisions/018_resources_found_decisions.txt`, `common/script_constants/018_resources_found_decision_constants.txt`, `common/scripted_effects/018_resources_found_decision_effects.txt`, `common/scripted_triggers/018_resources_found_decision_triggers.txt`, `common/scripted_localisation/018_resources_found_scripted_localisation.txt`, `localisation/english/018_resources_found_decisions_l_english.yml`, `localisation/english/018_resources_found_system_l_english.yml`, and `docs/events/018_resources_found/overview.md`. It added `resources_found_cycle_field_workboard`, `resources_found_workboard_page`, the five page triggers, the operations presentation trigger, the field-local cycle helper, and dynamic page labels. No project cost, duration, outcome, AI weight, mission, category attachment, or scripted-GUI geometry changed.

The decision/mission identifiers audited are the Event 018 categories and IDs in `common/decisions/018_resources_found_decisions.txt`, `common/decisions/categories/018_resources_found_categories.txt`, `common/scripted_effects/018_resources_found_decision_effects.txt`, `common/scripted_triggers/018_resources_found_decision_triggers.txt`, and `common/scripted_triggers/018_resources_found_triggers.txt`, with the exact mission families listed above.

## Simplifications, omissions, and blockers

- No new gameplay simplification, fallback, placeholder, omitted route, missing localisation, or missing AI path was accepted in this audit.
- The field action-density warning is resolved without hiding a mechanic, changing pacing, or changing AI incentives.
- Full engine campaign execution, delayed event delivery, state transfer, border timeout, cave front AI, live GUI playback, and audio/achievement runtime were not performed because agents must not launch Hearts of Iron IV.
- Full normalized decision probability, mission score, scripted MTTH, and direct-random results remain MCP-adapter limited as documented in the probability handoff. The Event MCP helper projection is partial. These are evidence blockers, not source-local defects.

## Final follow-up for parent

1. Treat this handoff as the current decision/mission audit record and supersede the stale visible-mission count in `decision_mission_audit_handoff.md`.
2. Treat the field action-density warning as resolved by the five-page workboard and retain the six-action maximum as a regression requirement.
3. Reuse the dated probability and GUI artifacts above in the aggregate Event 018 completion report. Do not claim complete normalized AI probabilities or live gameplay from these artifacts.
4. Include the concurrent Event 019 provider append in the broader integration review without reverting it.

## Parent post-resolution MCP evidence

- `hoi4.probability_inspect` on the complete 29-candidate selected-field decision pool returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, `candidates=29`, `requiredInputs=8`, `unresolved=0`, and no diagnostics at source revision `65977b1a30fdc9b258aa2606a58936e45e8cc3d43c5a81fdbea9d8804060af89`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a205eeded51bf7653fb51f73b4b98e22fda39ef19cc1777b3050a2011780302/8448b525fc55e2bd08176187552c7292883a5aef637b8b48080ad31a4576a37f/probability-inspect-dd2e5ef3aa15.json`.
- Fresh `hoi4.gui_inspect` retained all 34 Event 018 elements under scenario `event018_resources_found`, at revision `fa2d32d2408b7d9a5545257db3c2fbe39ae8dda2c6c4b7236a54097fe5f7a168`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cd3aca9fb9f2f5caa9f5cab064224a8c4887234702a0d8b5180ba3f12972d0a/38a46e5f974ec4fa90a4bb70c0bc2b40c4470b8452396828824236feb3c3d365/gui-inspect.fa2d32d2408b7d9a.json`. Its headline failure remains the known repository-global diagnostic ceiling, not an Event 018-local result.
- Fresh `hoi4.gui_render` completed across the supported four resolutions and normal, hover, selected, locked, disabled, warning, active, completed, empty/full list, minimum/maximum value, long-text, and missing-localisation states. The linked full render is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65f260e93b8b02003e0d5a02f453a755dbc8582a27ec45fb9de593cac0f4310a/1d84ec006e8779141c212e97a7586830837bad1abd27761b486b795a6b6d840c/resources_found_field_window-full.svg`; the only returned diagnostic was response-wire truncation.

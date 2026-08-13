# Event 006 decision and mission audit after v104

Date: 2026-08-03

Scope: Current Event 006 decision, mission, category, cost, cleanup, focus-gate, scenario-selector, and Statehood Ledger sources after the v104 completion evidence.

Disposition: Read-only audit.

No gameplay, GUI, localisation, or balance source was changed by this audit.

The Event 006 package remains `HOLD-PARTIAL` under the v104 evidence because package capacity, formable readiness, source rights, AI balance, 6001, audio, and live runtime proof remain open.

The decision and mission slice is conditionally source-closed except for the minor engine-semantics cleanup and runtime proof limits listed below.

## Sources and method

- Read the Event 006 v104 completion evidence and current decision/mission audit handoffs, including the current cost-gate and allocator repairs.
- Read the required offline Paradox wiki Decision modding, National focus modding, triggers, effects, scopes, localisation, and on-actions pages, plus the required vanilla documentation and vanilla decision/focus precedents.
- Applied `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-focus-trees`, and `chaos-redux-subagents` guidance.
- Inspected 31 Event 006 decision files, 31 category files, four Event 006 focus files, the Event 006 crisis and decision effects, related scripted triggers, on-action recovery, constants, English localisation, and the Statehood Ledger sources.

## Issues, sorted by severity

### P3 — three mission `visible` blocks are inert engine declarations

`independence_wave_rival_bloc_respond_to_invitation`, `independence_wave_rival_bloc_commit_shared_reserve`, and `independence_wave_rival_bloc_challenge_leadership` in [006_independence_wave_rival_bloc_decisions.txt](C:/Users/klimp/OneDrive/Documents/Paradox%20Interactive/Hearts%20of%20Iron%20IV/mod/chaos_redux/common/decisions/006_independence_wave_rival_bloc_decisions.txt) use `visible` despite HOI4 mission semantics ignoring that field.

Their working lifecycle does not depend on it: `activation`, `available`, `cancel_trigger`, and cleanup effects control the three missions, and each active mission has a valid invalidation path.

Recommended local cleanup: remove only those three inert `visible` blocks after the P2 localisation correction is reviewed, so later maintainers do not assume they control mission visibility.

### P3 — runtime and calibrated AI proof remain unavailable

The source proves valid AI declarations and static selector coverage, but it does not prove the exact available decision pools, AI action probabilities, recipient loss timing, or GUI persistence in an actual campaign.

This is a v104-level completion blocker rather than a source defect.

## Decision category lifecycle notes

| Category family | Reveal and ownership | Retirement and cleanup | Result |
| --- | --- | --- | --- |
| Pre-wave crisis | Current host, crisis requester, and queued-release state control the timed pressure work. | `independence_wave_recover_crisis_requester_loss` clears the global queue, requester flags, retry state, pressure state, and log payload when the requester is annexed. | Source-correct; runtime timing remains unproven. |
| Statehood, recognition, dependency, league, and formable work | Category and actions stage through release origin, capability, membership, target, regional, and map-control triggers. | Route guards and action-specific cancellation remove obsolete work when a country, target, member, or origin becomes invalid. | No passive political-power store found. |
| Rival bloc | Invitation and member categories are limited by valid contract, target, member, and leadership-candidate conditions. | Local and global invitation cleanup clears mission, flags, variables, and event targets; membership loss cancels reserve and leadership work. | Source-correct apart from the inert mission `visible` declarations. |
| Reclamation front / DM-58 | Membership and coordinator rules gate the operation and successor work. | `independence_wave_revalidate_reclamation_front_operation` now cancels when a stored witness leaves, and `independence_wave_cleanup_reclamation_front_operation` clears coordinator, state, participant, and operation state. | The historical participant-invalidation finding is resolved in source. |

There are 61 category definitions across the 31 Event 006 category files.

Every category title and description now resolves in the Event 006 English localisation.

The previously missing `independence_wave_evolution_incident_category` title was added as `"Evolution Incidents"` in `8ea15ea11` and was rechecked against the current worktree.

## Mission quality notes

Static inventory found 59 direct timed missions.

All 59 provide `available`, `days_mission_timeout`, and cancellation handling.

Nineteen are selectable missions, and all nineteen have an `ai_will_do` score.

The eight direct action blocks without AI are deadline/objective surfaces rather than AI-selectable decisions: the first integration, maritime-board, league-session, charter, convoy, procurement, and basing deadlines in the FORM01/02/04/05/48 decision files.

| Mission family | Owner, category, and region | Requirement and duration | Success and failure | Duplicate-risk result |
| --- | --- | --- | --- | --- |
| Pre-wave crisis | Requester and current host in the crisis category and affected release region. | Queued requester, active pressure, and release-barrier conditions; retry duration is centralised. | Release queue resolves through the crisis event; expiry, failed retries, or requester loss clear the queue and receipts. | Low: queue flag, requester flag, retry state, and on-annex recovery prevent stranded repetition. |
| Rival invitation | Recipient in the rival-bloc category; cross-country contract target. | Manually activated only after a valid pending acceptance; invitation-response timeout is centralised. | Acceptance enters the contract; decline, expiry, invalid target, or contract cleanup removes the mission and invitation state. | Low: `independence_wave_rival_bloc_clear_pending_invitation` removes the mission and both local/global state. |
| Shared reserve and leadership challenge | Rival-bloc members; member/host/cohesion conditions. | Valid member or leadership candidate plus CP, equipment, fuel, train, or Army XP costs; centralised commitment duration. | Timeout calls commitment or challenge resolution; membership/candidate loss invokes failure cleanup. | Low: a mission cannot start while its own active instance exists, and loss of eligibility cancels it. |
| Reclamation front / DM-58 | League coordinator and registered member countries in eligible border regions. | Active operation requires a valid coordinator, minimum member count, map preflight, and persisted witness list. | Completion executes the bounded operation; member loss or origin end runs operation cleanup. | Low in source: every stored witness is revalidated and cleanup resets operation, coordinator, and participant state. |
| FORM deadline objectives | Event-created formable country and its relevant regional category. | Explicit route/capability conditions and centralised deadline periods. | Named success resolution or deadline failure effect closes the objective. | Low: objective-only actions are not repeatable AI actions, and their route flags prevent repeated reward loops. |

The source contains three mission `visible` blocks named in the P3 finding.

They do not produce a missing active-mission lifecycle because the engine ignores them and the actual `activation`/cancellation paths remain present.

## Cost and requirement clarity notes

The audit found 133 unique custom-cost keys.

Every one resolves to a base, `_blocked`, and `_tooltip` localisation triplet.

The generic cost table is centralised in `common/script_constants/006_independence_wave_decision_constants.txt`: manpower 2,500/5,000/10,000; infantry equipment 250/500/1,000; support equipment 50/100/200; trains 5/10/20; convoys 5/10/20; fuel 250/500/1,000; Army XP 10/20/35; and Command Power 10/20/35.

Rival-bloc Command Power spends are centralised at 10, 15, 20, or 25, and FORM05's combined Command Power gate is 30.

All observed Command Power spends therefore stay at or below 35, beneath the 60-point affordability cap used by the decision audit guidance.

The repaired security gates use engine-backed `has_manpower`, `has_army_experience`, `has_equipment`, `has_stability`, and `has_war_support` triggers before subtracting those same resources.

The remaining `check_variable` references concern Event 006 custom values such as instability and rival-bloc cohesion, not engine resource fields.

Only three zero-cost regular controls exist, and each is a SCN-008 rejection-ledger navigation control with no reward and zero AI weight.

No negative `add_political_power` payment effect appears in Event 006 decision or shared decision-effect sources.

The only decision-owned unit spawn, DM-22 emergency formations, requires a major security payment, has `fire_only_once = yes`, sets a 180-day raised flag, and is removed by professionalisation and origin cleanup.

The other `create_unit` call is initial package force setup rather than a repeatable decision reward.

No political-power store, free-unit loop, equipment-farming loop, core-spam loop, or war-goal-spam loop was found in this audit slice.

## AI validity and focus/route-lock notes

All selectable missions carry AI weights, and their validity conditions include relevant member, candidate, host-front, target, map, route, origin, or faction checks.

A static reference check found 27 `has_completed_focus` decision gates and 319 Event 006 focus IDs across `006_independence_wave_focus.txt`, `006_independence_wave_pacific_focus.txt`, `006_independence_wave_iw043_iw058_focus.txt`, and `006_independence_wave_iw093_iw098_focus.txt`.

All 27 decision gates resolve to an Event 006 focus ID; no dangling focus gate was found.

The Pacific availability guards intentionally close early emergency actions after their matching HBX or HAW focus completes, while IW043 and IW058 follow-up decisions open only after their route-specific focuses complete.

The source cannot establish live AI selection probability or prove every dynamically loaded country receives the intended focus tree, so calibrated campaign behavior remains open.

## Scenario selector and scripted-GUI evidence

`python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 player-facing selector cells and eight source edge cases.

`python -B .tools/audit_event6_allocator.py` passed its publisher, automatic/high-chaos, scenario-ranked, package compatibility, intensity, and pre-wave crisis contract checks.

`python -B .tools/audit_event6_gui_matrix.py` passed the Statehood Ledger source matrix: five mutually exclusive tabs, five recognition frames, three dependency states, four league states, four formable states, required cleanup frame variables, and four static/animated pairs.

Read-only GUI inspection and render artifacts were recorded for `independence_wave_status_window` at 1080p and 720p with normal, selected, locked, active, and long-text variants.

Primary render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4cb77f76216bc0fbb09931da2f0e3b0001502f3f1778ba3c88dc6fc2ea68223/1b6bafcadcbd0e94567d02920a5cb0e7e85734a0b507377bc4069fdbda9f599f/independence_wave_status_window-full.png`.

Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df603cea8a7d346404cf344e8c9cbc4eed6de23c8263378660ccf43a994bdb80/9794f1af4635edee2c9baee6452a430e7023edbd9c2f6ffc99d434cf49c14d70/gui-inspect.3381c79c65902bd7.json`.

The MCP fidelity aggregate reported 426 modelled, 54 approximated, 65 ignored, one missing, four unsupported, and twelve unresolved GUI-source paths, but it also reported 1,983 workspace-wide blocking diagnostics with truncation.

Those aggregate diagnostics cannot be attributed to Event 006 and do not replace the passing targeted source matrix.

Live GUI rendering, player clicks, state persistence, and save/load behavior remain unresolved.

## Validation and skipped validation

Meaningful static validation passed for the scenario-selector matrix, allocator matrix, and Statehood Ledger semantic matrix.

The audit also checked direct mission contracts, selectable-mission AI coverage, custom-cost localisation triplets, category-title and description coverage, zero-cost decision uses, political-power payment effects, decision-owned unit creation, engine-backed resource gates, on-annex requester-loss scope, and decision-to-focus reference resolution.

Skipped meaningful validation: no HOI4 launch, live event triggering, AI campaign simulation with declared world-state inputs, real recipient annexation timing, save/load, or live GUI interaction was performed because those require the parent/user runtime environment and cannot be proven by source inspection.

## Concrete next fixes

1. The two narrow source findings from this audit are closed by commits
`8ea15ea11` (category title) and `5fb9800e0` (three inert mission `visible`
blocks). The remaining work is bounded runtime/AI/persistence evidence and the
package, formable, source-rights, audio, and capacity gates recorded by the
current completion audit.
2. Run live evidence for the 32 selector cells, requester loss during a queued crisis, rival invitation invalidation, membership exit during DM-58, and Statehood Ledger state/save-load persistence before lifting the v104 hold.

## Handoff status

Changed files: this audit handoff only; the historical source findings above
were closed by the parent commits listed in the current authority.

Changed decision, mission, scripted-GUI, or localisation IDs: none.

Before and after behavior: unchanged because this was a read-only audit.

Plan handoff path: not written; the two source fixes are narrow and listed above.

No simplification or fallback was introduced by this audit.

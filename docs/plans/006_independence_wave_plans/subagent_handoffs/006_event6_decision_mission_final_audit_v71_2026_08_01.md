# Event 006 final decision and mission audit v71

Date: 2026-08-01

## Scope and disposition

This was a read-only final source audit of Event 006's crisis category, SCN-008 rejection ledger, five evolution-incident decisions, shared and package decision files, mission contracts, DM-22 Armed Birth follow-through, and DM-58 reclamation safeguards.

No Event 006 gameplay, localisation, GUI, or focus source was changed.

No new source-level decision or mission defect was found in the audited surface.

## Issue list, sorted by severity

### P2 - Scenario and package runtime evidence remains incomplete

The SCN-008 source correctly freezes and exposes rejection rows, but this audit did not execute the required 32 mode-by-intensity matrix or collision-heavy allocator scenarios.

This is an evidence blocker, not a confirmed ledger, cost, or target-validity defect.

Recommended owner action: run the declared 32-cell source/MCP scenario matrix from `docs/events/006_independence_wave/systems/triggerable_scenario.md`, including zero-ready, living-tag, protected-host, reservation, Event 005 collision, and repeated-launch states.

### P3 - Package admission remains outside this decision audit

Package decisions remain source-gated by active-origin, package, route, target, and content-readiness state, but country-specific assets, admission, and package acceptance evidence are owned by their package audits.

Recommended owner action: retain the content-readiness gate and close package admission through the relevant country, asset, and allocator audits. Do not weaken a decision gate to make an unready package selectable.

### P3 - Live engine behavior was not exercised

Static review cannot substitute for live mission activation, timeout, cancellation, save/load, AI choice, or allocator execution.

No game process was launched, in accordance with repository ownership rules. This is a validation boundary rather than a claim that a source failure exists.

## Decision category lifecycle notes

- `independence_wave_crisis_category` appears only for current pressure, an active mission, or an eligible crisis request. Its 120-day mission consumes a concrete security package, queues the normal synchronized release only while pressure persists, and otherwise applies the documented blocked or cancellation consequence, clears runtime state, and starts the cooldown.
- `independence_wave_scenario_ledger_category` is a temporary, player-owned rejection viewer. It is visible only while its local display flag is set and frozen rejection rows exist. Previous, Next, and Close are zero-reward navigation controls, use `ai_will_do = { base = 0 }`, and cannot operate as a political-power or material store.
- `independence_wave_evolution_incident_category` has one active-stage decision per evolution. Visibility requires the active Event 006 country and exact global stage, while pending and mutually exclusive resolution flags prevent repeat resolution in the same origin generation. Generation reset and origin cleanup clear all five families' pending and outcome flags.
- Shared founding, government, security, recognition, network, league, borders, formable, high-chaos, and country-package categories continue to be route, phase, or package gated rather than permanent stores of flat political-power exchanges.

## Mission quality notes

| Mission or decision family | Owner/category/region | Requirement and duration | Success and failure or cancellation | Duplicate risk |
| --- | --- | --- | --- | --- |
| `independence_wave_open_host_crisis` | Current host, Crisis category, pressure-bearing homeland or foreign-controlled state | Concrete manpower, Army XP, Command Power, infantry-equipment, support-equipment, and stability commitment; 120 days | Timeout queues the ordinary Wave only if pressure persists. A blocked resolution or cancellation records the consequence, applies cooldown, and clears runtime state. | Low, guarded by active and queued flags. |
| SCN-008 ledger controls | Scenario ledger, frozen rejected-package rows | At least one frozen blocked row; no gameplay duration | Only changes the viewing index or closes the local display. | None, no reward or AI use. |
| Five evolution incidents | Active Event 006 origin, evolution-incident category, global stage 1 through 5 | Paid administration, diplomatic, major-security, or strategic action followed by a standard, extended, or strategic decision timer | Each `chaosx.nr6.360` through `.364` event offers two materially distinct ledger outcomes. Inactive-origin cancellation clears the pending flag; reset and origin cleanup clear all outcomes. | Low, one outcome per stage per origin generation. |
| `independence_wave_raise_emergency_units` (DM-22) | Active Event 006 country, Security category, severe former-host threat or Armed Birth frontier mandate | Major security payment, force-package receipt, and capital anchor; one-shot decision | Creates only the predefined understrength reserve, then blocks itself with one-shot and active flags. `independence_wave_professionalize_army` and origin cleanup demobilize the exact fixed-id reserve. | Low, no repeat or free-unit loop. |
| All Event 006 timed missions | Shared and package categories | Static direct-child inventory: 59 `days_mission_timeout` blocks, including 19 selectable missions | All 59 declare explicit `available`, `timeout_effect`, and `cancel_trigger`; all 19 selectable missions declare `ai_will_do`. | No missing-contract duplicate was found by the inventory. |

## Cost and requirement clarity

- Across 31 Event 006 decision files, 133 unique `custom_cost_text` identifiers resolve to base, `_tooltip`, and `_blocked` localisation keys in the Event 006 English localisation set. No missing triplet was found.
- The only literal `cost = 0` and `days_re_enable = 0` entries are the three SCN-008 navigation controls. All material actions use shared payment helpers and centralized constants.
- The crisis payment is concrete: `-5000` manpower, `-20` Army XP, `-20` Command Power, `-500` infantry equipment, `-100` support equipment, and the separately stated stability commitment through `common/script_constants/006_independence_wave_decision_constants.txt` and `006_independence_wave_crisis_constants.txt`.
- DM-22 requires the major-security cost, force-package receipt, and capital anchor before its defined unit creation helper can run. Its player text discloses the understrength reserve, immediate capital defense, threat or frontier-mandate gate, and professionalization demobilization.
- DM-58 exposes its nontrivial member, state, and owner requirement with `independence_wave_coordinate_reclamation_fronts_preflight_tt`, not an unlocalised raw trigger tree.

## AI validity and route-lock notes

- The crisis mission's AI score increases only for the actual stability or occupation pressure flags.
- The five incident decisions have centralized stage-appropriate AI weights, and every corresponding event has a two-option `ai_chance` pool. Their stage, active-origin, pending, and prior-outcome gates prevent invalid or repeated AI actions.
- DM-22 has urgent AI willingness but is invisible without either a severe host threat or the Armed Birth frontier-mobilization outcome. It also requires the same payment, force-package, and anchor proof as a player.
- SCN-008 ledger controls have zero AI willingness because they are display-only.
- The earlier DM-58 distinct-front HOLD is resolved in source: `has_independence_wave_reclamation_front_preflight` in `common/scripted_triggers/006_independence_wave_decision_triggers.txt` explicitly traverses three different league members and rejects repeat owners before its third state search. The decision remains route, focus, member-count, crisis, preflight, reserve, and cost gated; its failure branch rolls staging back before payment.
- No numeric decision willingness conclusion is claimed. A complete campaign candidate pool and state set were not supplied for probability evaluation.

## Localisation and tooltip gaps

No missing custom-cost triplet, unlocalised incident option, or raw DM-58 preflight exposure was found in the audited surface.

The five incidents use Event 006 localisation for titles, descriptions, both outcome labels, and player-facing tradeoffs. The crisis and DM-22 descriptions communicate the public requirement and outcome direction without exposing implementation state.

## Cleanup and exploit-risk notes

- No direct `create_unit` appears in the 31 decision files. DM-22 deliberately calls `independence_wave_decision_raise_emergency_formations`, which materializes only the persisted package template at a fixed unit id. `independence_wave_decision_demobilize_emergency_formations` deletes that exact id and clears the two reservation flags. Professionalization and origin-reset cleanup call the demobilization path.
- The only direct Event 006 decision-file claim and war-goal writers belong to the bounded DM-58 operation. The operation has a unique-owner preflight, staged rollback, a failure receipt, league-crisis consequence, one-operation guard, and finite war-goal policy.
- The five incident effects clear their own pending flag before writing outcome state. `common/scripted_effects/006_independence_wave_effects.txt` clears every pending and outcome flag on both generation reset and origin cleanup, preventing carrier-tag inheritance.
- No free unit loop, equipment farm, passive political-power store, core spam, or unrestricted war-goal loop was found in the audited decision source.

## Focus integration notes

`independence_wave_unlock_professional_army` is written by `common/national_focus/006_independence_wave_focus.txt` and opens DM-23, the path that demobilizes any active DM-22 reserve before professionalization proceeds.

DM-22 itself is a crisis or Armed Birth response, rather than a focus purchase. The Armed Birth decision `independence_wave_armed_border_incident` resolves through `chaosx.nr6.362`; only the frontier-mobilization option exposes the paid DM-22 reserve path. The civilian-command option does not.

## Decision-owned GUI and MCP evidence

No decision-owned GUI source changed in this audit, so no GUI rewrite was appropriate. The previously recorded Statehood Ledger GUI inspection and render evidence remains the relevant baseline in `006_decision_mission_post_dm58_deadline_reaudit_2026_07_28.md`.

This audit ran a fresh read-only Event MCP scan. It produced a workspace-wide partial graph with truncated source inventory and is not evidence of an Event 006 GUI or decision defect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/097cda140ac09903f963cc481f90ced13154f64cad0df66e6b8ee1a3714d08e2/6fdaf8b65eba3efb257107316b37cfe3923119975fac5b889ea3b032dc775f6d/event-scan-b43b1abfc68a.json`.

## Files changed and validation

Changed file:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_final_audit_v71_2026_08_01.md`

Changed gameplay, decision, mission, scripted-GUI, focus, and localisation identifiers: none.

Meaningful validation:

- Static mission-contract extraction across all Event 006 decision files.
- Cross-file custom-cost localisation triplet inventory.
- Direct readback of crisis payment, cancellation, timeout, cooldown, and cleanup helpers.
- Direct readback of all five incident decisions, events, option effects, centralized tuning, and reset cleanup.
- Direct DM-22 helper, exact-unit demobilization, professionalization, and origin-cleanup tracing.
- Direct DM-58 injective preflight tracing.

Skipped meaningful validation:

- No live HOI4, save/load, or AI execution was run.
- No 32-cell SCN-008 scenario/allocator matrix was executed.
- No complete campaign-state probability evaluation was attempted, because the required candidate pools and external state inputs were not declared.

## Simplifications, omissions, and blockers

No fallback or simplification was introduced by this audit.

The whole Event 006 completion claim remains blocked by the scenario-matrix and package-admission evidence described above. This audit is complete only as a bounded decision and mission source audit.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-focus-trees`, and `chaos-redux-subagents`.

# Event 006 decision, mission, and SCN-008 current re-audit

## Scope and disposition

This is a bounded source audit of the Event 006 decision categories, timed missions, custom costs, AI weights, cleanup paths, and SCN-008 decision-owned surfaces.

The audit found no confirmed local decision, mission, SCN-008, scripted-GUI action, localisation, or cleanup defect that supports a narrow patch.

No gameplay file was changed.

## Issue list, ordered by severity

| Severity | Finding | Disposition |
| --- | --- | --- |
| P0–P1 | No confirmed Event 006 decision or mission defect. | No patch required. |
| P3 | The full GUI-inspection validation bundle reports broad workspace diagnostics and truncates its source inventory, so it cannot establish a clean whole-workspace GUI result. | Not an Event 006 source failure; the decision-owned source and rendered window were inspected separately. |
| P3 | No live save-state or probability-normalisation run was performed for this audit. | The current source receipts cover structural inputs and the accepted static SCN-008 matrix; live consumer validation remains with the parent/user. |

## Decision category lifecycle notes

| Surface | Visibility and entry | Resolution and cleanup | Duplicate or route-lock protection |
| --- | --- | --- | --- |
| Core founding, government, recognition, security, crisis, and regional categories | The existing category and decision triggers require the released-origin and route state before player-facing actions appear. | Costed actions pair `custom_cost_trigger`, `custom_cost_text`, and payment/effect helpers; timed actions use mission completion, timeout, cancellation, or removal effects. | Existing active-project, route, target, and `fire_only_once` gates prevent repeated selection where an outcome is unique. |
| FORM01, FORM02, and FORM04 integration categories | The first-session objectives are activated by the relevant integration effects, not clicked as ordinary decisions. | Their success and failure helpers own progression advancement or deadline failure, and cancellation follows the active-progression gate. | `activation = { always = no }` prevents accidental manual creation; the active-progression checks prevent duplicate mission cycles. |
| FORM05 Mediterranean charter category | The charter deadline and first-board objective are effect-activated while the charter route is active. | The deadline uses the relevant duration constant and failure helper; the associated decisions reserve, pay, and cancel their commitment state through existing helpers. | Route, reservation, and charter-state conditions prevent closed or duplicate charter activity. |
| FORM48 Pacific carrier category | Recurring convoy, procurement, and basing cycles are activated by carrier workflow effects, while their fulfilment decisions remain costed player/AI actions. | Each deadline has success, timeout, and cancel handling; the cancel effects clear its cycle-active flag. | Carrier/post-formation gates, obligation-complete checks, and cycle-active flags prevent stale or freely repeated cycles. |
| SCN-008 scenario ledger category | The ledger controls are visible only while `independence_wave_scenario_ledger_visible` is set. | Previous, next, and close are zero-cost navigation only; close clears the visibility state, and scenario reset clears cursor, arrays, marks, and category state. | Navigation has no reward or gameplay effect. The selected-package ledger remains transaction-committed before it becomes selectable. |

## Mission quality notes

| Owner and category | Region | Requirement and duration | Success and failure | Duplicate risk |
| --- | --- | --- | --- | --- |
| FORM01 congress and FORM02 union first-session missions | Western/Central European integration routes | Effect-activated; the owning progression must remain active; duration is `constant:independence_wave_decision_duration.long_treaty`. | Route-specific completion helpers advance the session; deadline helpers fail it; cancellation follows the progression gate. | Low: no manual activation and route-active cancellation. |
| FORM04 first league-session mission | League/formable route | Effect-activated during its owning progression and guarded by the route state. | Existing session-complete and deadline-failure helpers resolve the mission. | Low: the route state controls the mission lifecycle. |
| FORM05 charter deadline and first maritime-board mission | Mediterranean | Effect-activated; hidden from manual selection; durations come from `independence_wave_mediterranean_duration.form05_deadline_days` and the FORM05 integration-duration table. | Charter and board helpers respectively resolve completion or failure. | Low: charter reservation and route-state gates own the lifecycle. |
| FORM48 convoy, procurement, and basing deadlines | Pacific carrier | Effect-activated; completion requires the matching obligation flag; durations use `independence_wave_form48_duration`. | Each mission calls its matching complete or fail cycle helper, and cancellation clears the matching active flag. | Low: carrier, post-formation, obligation, and active-cycle gates are all present. |
| Remaining Event 006 timed missions | Their owning regional/formable category | The direct audit found 59 timed missions, each with `available`, `timeout_effect`, and `cancel_trigger`. | Their pre-existing effect contracts define their outcomes. | No structural duplicate hole found in the audit. |

The eight missions initially appearing to lack `ai_will_do` are expected objective/deadline missions: FORM01/02/04 first sessions, FORM05 charter/first board, and FORM48 convoy/procurement/basing deadlines all have `activation = { always = no }` and are completed by state-changing effects or their deadlines.

## Cost and requirement clarity

- The Event 006 decision files declare 133 unique `custom_cost_text` keys; all 399 required base, `_blocked`, and `_tooltip` localisation keys were found in English localisation.
- Costed decisions consistently expose the matching `custom_cost_trigger` and use resource, factory, equipment, train, convoy, manpower, command-power, or route-state requirements through the existing helpers rather than a passive political-power store.
- Mission durations, scenario type/rule/intensity selection, and sampled regional costs resolve through script constants or existing dynamic helper inputs; this audit found no narrow static-number regression to centralise.
- The only zero-cost SCN-008 controls are ledger previous, next, and close. They only change cursor or visibility state and cannot grant resources, units, cores, war goals, or package commitments.

## AI validity and route-lock notes

- The current bounded probability receipt, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_probability_inspect_current_v116_2026_08_03.md`, reports zero unresolved inputs for 10 core-decision `decision_ai_will_do` candidates with 52 required inputs, 54 core-mission candidates with 30 inputs, and three SCN decision candidates with one input.
- The effect-activated missions listed above appropriately have no `ai_will_do`; their companion selectable decisions retain their existing AI blocks.
- `independence_wave_scenario_start_host_war` verifies an active origin and a valid former host, rejects self-targeting, avoids an existing war, and requires `can_declare_war_on` before declaring. Failed declarations remove their pending unique-target mark.
- SCN-008 Universal Belligerence with the Former Hosts rule sets `independence_wave_scenario_unique_belligerence_policy`, marks the selected host before declaration, and clears both per-target marks and the target array during completion and reset. This preserves the repaired one-former-host-per-released-country policy.
- Wars of Separation keeps that uniqueness policy disabled, as required by the accepted scenario contract.

## Localisation and tooltip notes

- All custom-cost triplets resolve, including the regional/formable overlays that are indented beneath `l_english:`.
- The sampled player-facing decisions use custom-cost text and effect tooltips instead of exposing raw trigger chains as their primary cost explanation.
- No new dynamic-localisation or tooltip key is required because no decision surface changed.

## Cleanup and exploit-risk notes

- SCN-008 reset clears scenario category state, ledger visibility/cursor, blocked-package arrays, danger arrays, and belligerence target marks through `independence_wave_scenario_clear_belligerence_target_marks` and the reset helpers.
- The universal-belligerence and host-war failure branches clear their target marks before returning, avoiding stale target blocks after a failed declaration.
- FORM48 cancellation clears the active flag for each recurring mission cycle.
- No resource-farming, free-unit, core, war-goal, or cooldown-bypass loop was found in the bounded source surface. Runtime sequence checks remain the meaningful way to prove all multi-country edge cases.

## Decision-owned GUI evidence

The audit used read-only GUI inspection and rendering for `independence_wave_status_window`; no `hoi4.gui_rewrite` was needed.

- Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1b975ec1281c84b7e2414d3d3a0a3a992d160f26a55bd1646048a878d59c960/a8a3a792bfa1afa6bb3d52fe5356f95677ce4813d17fda066b7b38818f072ea9/gui-inspect.4d2a2f7d123f320b.json`.
- Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4cb77f76216bc0fbb09931da2f0e3b0001502f3f1778ba3c88dc6fc2ea68223/f86710f6984ed85158e79934be9435e3c484acc579436e03d3f210fb68a0d898/independence_wave_status_window-full.png`.
- The render covers normal, selected, warning, and long-text states at 1920×1080. The scripted GUI only toggles presentation/tabs and refreshes country state; it does not offer an alternate gameplay reward, cost, or AI-only path.
- The inspector reports modelled, approximated, ignored, missing, unsupported, and unresolved elements across the broader GUI inventory. Its validation run is globally blocked by unrelated workspace diagnostics and a truncated source listing, so its fidelity figure is not a clean Event 006 completion claim.

## Changed files and identifiers

- Changed file: this handoff only.
- Changed decision, mission, scripted-GUI, scripted-effect, and localisation identifiers: none.
- Before and after behavior: unchanged; no source patch was justified by the audit evidence.

## Meaningful validation

- Ran `python -B .tools/audit_event6_scenario_matrix.py`; it passed all 32 SCN-008 cells across eight scenario modes and four intensity levels, including the documented edge-case references.
- Performed a direct Event 006 decision-file scan: 31 files, 481 direct child decision blocks, and 59 timed missions. Every timed mission had `available`, `timeout_effect`, and `cancel_trigger`.
- Performed a custom-cost localisation crosswalk: 133 unique `custom_cost_text` keys, 399 expected English keys, 399 found, and zero missing.
- Reviewed the current bounded probability inspection receipt cited above and read the SCN-008 scenario effects, triggers, constants, decision category, and decision-owned scripted GUI.

## Skipped meaningful validation and why

- No HOI4 runtime, save-state, or in-game validation was run; live consumer testing belongs to the user.
- No normalised AI probability comparison was run because this bounded audit had no supplied country-world scenarios. The existing inspection receipt establishes structural input resolution, not behavioural frequency.
- No full-workspace GUI repair was attempted because the reported diagnostics are outside this decision-owned scope and the tool output is globally truncated.

## Remaining issues and recommended follow-up

There is no current local decision or mission patch to apply.

The parent should retain the existing Event 006 completion blockers outside this audit surface, and should treat the GUI tool's global diagnostic set as a separate UI/workspace audit rather than an SCN-008 defect.

No simplification or fallback was introduced.

## Skills and references used

Applied `hoi4-decisions-missions`, `chaos-redux-events`, `hoi4-focus-trees`, and `chaos-redux-subagents`.

Consulted the required offline Paradox wiki decision, trigger, effect, scope, localisation, AI, interface, and scripted-GUI references, plus the relevant vanilla decision, scripted-GUI, script-concept, script-constant, effect, and trigger documentation and the vanilla border-conflict decision precedent.

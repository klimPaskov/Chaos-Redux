# Event 016 decision runtime audit handoff

## Scope and result

Audited the complete Event 016 decision surface as it exists in the shared worktree: host Directorate institutions, facilities, project board, containment and Evolution IV deadline, foreign operations, provenance achievements, postwar aftermath, every KRG category, KRG phase decisions, hazardous missions, and terminal actions.

No confirmed load blocker, missing Event 016 decision category, missing Event 016 decision or mission localisation, unresolved Event 016 constant, unresolved custom decision call, missing focus-unlock producer, or missing decision/category sprite reference was found.

No gameplay source patch was warranted. This handoff is the only file written by this audit.

## Issue list, sorted by severity

1. No critical or high runtime defects found in the audited surface.
2. Medium unresolved validation: the detailed Directorate GUI inspection is blocked by the MCP scanner's `SCAN_BYTE_LIMIT`, so no render-fidelity conclusion can be made for `kruger_directorate_container`. This is a tooling limit, not a source diagnostic.
3. Low unresolved validation: the focused Event 016 MCP lint produced a partial workspace-wide graph rather than a decision-only result. It reported no Event 016 blocking diagnostic in its inline result, but it is not sufficient to certify every helper projection in the full workspace.
4. Low design follow-up: the Directorate panel shows armed-singularity state but not the intermediate arming, fail-deadly, controlled-disarmament, or terminal-map-audit state. This was already recorded in the terminal review handoff and is not a load-safety defect.

## Category lifecycle notes

| Owner | Category | Reveal and closure contract | Audit finding |
| --- | --- | --- | --- |
| Current host or KRG | `brilliant_scientist_directorate_category` | Visible only to the current host or sovereign KRG, retains its dashboard with `visible_when_empty = yes`, and contains host, project, containment, and Evolution IV deadline actions. | Declared in the category file and consumed by six Event 016 decision files. Its scripted GUI is read-only and does not bypass decision costs or AI. |
| Evolution II observer | `brilliant_scientist_foreign_operations_category` | Requires a valid foreign actor, active contest, and initialized observer receipt. Covert actions each target the bounded host array and close through one-shot operation ledgers. | Declared, consumed, and guarded by current-host validity, actor validity, host incoming-operation capacity, transaction locks, and world-end cleanup. |
| Host or KRG provenance actor | `brilliant_scientist_origin_investigation_category` | Visible only after the achievement-origin actor trigger allows the investigation. | Declared and consumed. The evidence chain is one-shot and project-gated. |
| Aftermath custodian | `brilliant_scientist_aftermath_treaty_category`, `brilliant_scientist_aftermath_inspection_category`, `brilliant_scientist_aftermath_reconstruction_category`, `brilliant_scientist_aftermath_remnants_category` | Visible only to the active postwar custodian. | All four are declared and each has a decision consumer. The categories are not exposed to ordinary hosts or KRG. |
| KRG | `brilliant_scientist_krg_foundation_category`, `brilliant_scientist_krg_security_and_logistics_category`, `brilliant_scientist_krg_clone_and_machine_category`, `brilliant_scientist_krg_paleogenetics_category`, `brilliant_scientist_krg_xenobiology_category`, `brilliant_scientist_krg_portal_and_temporal_category`, `brilliant_scientist_krg_exotic_and_biological_category`, `brilliant_scientist_krg_foreign_policy_category`, `brilliant_scientist_krg_integration_category` | Each requires the live KRG focus layer plus its own focus-produced unlock receipts. | All 165 focus unlock flags read by Event 016 decisions and categories have a producer. |
| KRG | `brilliant_scientist_krg_terminal_program_category` | Survives the ordinary focus-layer closure through `brilliant_scientist_krg_terminal_decisions_are_active`, then closes on terminal/world-end cleanup. | The narrow terminal gate prevents the earlier commitment-lock bug from hiding disarmment and finalization actions. |

## Mission quality and lifecycle notes

| Owner | Category | Region | Requirement and duration | Success | Failure or duplicate risk |
| --- | --- | --- | --- | --- | --- |
| Host | Directorate | National | Sovereignty deadline is activated only by its active receipt and uses the country duration variable prepared by the evolution layer. | Marks expiry and invokes the deterministic containment resolver. | Cancels when host identity, deadline state, evolution enablement, resolution state, or world state invalidates. One active deadline only. |
| Host | Directorate | National | Loyalty review mission uses the institution/security route and the centralized review duration. | Resolves the recorded loyalty result and its follow-up state. | Its activation receipt and downstream result flags prevent a parallel duplicate review. |
| Host | Directorate project board | Project-family incident site | Fifteen incident missions are family-specific and activate only from their own incident receipts. | Their paired resolution decision records the family outcome. | Each has separate active/objective state, so identical display timers do not merge different project failures. |
| KRG | Clone and machine | Growth site or machine node | Clone-drift and rogue-node missions require an active site/node, paid response action, and live operational proof. | Full success needs both objective completion and rechecked facility/node evidence. | Cancellation and timeout distinguish lost operational proof from objective failure. No repeatable reward loop was found. |
| KRG | Foundation and security | Primary facility | Facility-defense and maintenance-audit missions require the primary site to remain KRG-owned and controlled. | Secure or service the site through their dedicated resolver. | The operation-evidence triggers reject stale site ownership or a destroyed facility. |
| KRG | Portal and temporal | Terminal network or danger state | Transit-breach, temporal rescue, and temporal-stabilization missions are separately activated by their own route and danger receipts. | Each resolves through a route-specific event/effect and clears its active state. | Distinct operational evidence avoids a generic temporal or portal success receipt. |
| KRG | Terminal program | Global | The disarmament hold requires the nonterminal proof and the central duration band. | Produces the durable disarmament proof used by settlement certification. | Cancellation rejects route loss, renewed armed/fail-deadly state, or lost dismantlement proof. It is distinct from the KRG controlled-disarmament decision. |

## Cost and requirement clarity

- Host containment uses paid political authority plus negative stockpile, fuel, manpower, experience, convoy, train, truck, support-equipment, or command-power constants. Gates are one unit below the exact spend, so the payment cannot produce a negative stockpile.
- Directorate facilities, staffing, foreign frameworks, projects, and KRG actions use named script constants rather than repeated bare numeric costs. The static scan resolved all 589 Event 016 `constant:brilliant_scientist_*` references.
- Complex containment, terminal, foreign, and hazardous-action requirements use custom trigger tooltips. All 199 Event 016 custom tooltip or custom-cost localisation references resolve.
- The audit found no flat political-power-only terminal or containment action. Foreign diplomatic offers remain immediate by design, while covert actions use timed work, target validation, cancellation, and one-shot ledgers.

## AI validity and route-lock notes

- Every clickable Event 016 decision block has an `ai_will_do` block. The only blocks without one are goal or timed missions, which are activated by their own decisions or event receipts rather than selected by AI.
- Foreign-operation willingness is centralized in `common/mtth/016_brilliant_scientist_mtth.txt`; the source inspection artifact found two weighted candidates, seven required inputs, and no unresolved source input. The candidate pool is incomplete, so no click probability or rank claim is made.
- Foreign actions revalidate current host, actor, target lifecycle, target cap, world-end state, character transaction lock, and route-specific access before they resolve.
- KRG decision categories are route-locked by focus receipts, and the terminal category has a terminal-only activity trigger for disarmment and finalization after commitment. All focus unlock flags consumed by this surface are set somewhere in `common/`.

## Localisation, tooltip, icon, and GUI notes

- All 312 Event 016 decision and mission ids, plus all 17 Event 016 category ids, resolve to English titles. Every decision or mission id also resolves to an English description.
- All 148 explicit Event 016 decision/category icon references resolve to a declared mod or vanilla GFX sprite.
- Every Event 016 localisation file tested has a UTF-8 BOM.
- All 36 Event 016 `GetBrilliantScientist*` scripted-localisation getter references resolve.
- The Directorate GUI's 38 text, button, and tooltip localisation keys resolve. The GUI inspect workspace is `mod_chaos_redux_ea3b2d67c2c0`; the detailed `kruger_directorate_container` inspection was not rendered because MCP returned `SCAN_BYTE_LIMIT`.

## Cleanup and exploit-risk notes

- Containment actions retain a board-level active-action lock, resolve from rechecked live causal state, and clear the in-progress state on cancellation. Invalid territory or exile contracts reopen the board without moving land or custody.
- Foreign covert operations use an actor lock, host incoming-operation cap, target revalidation at resolution, cancellation cleanup, and per-host one-shot ledgers.
- Hazardous KRG missions use separate facility, terminal, node, or site evidence so a lost map objective cannot grant stale mission success.
- Terminal routes retain explicit arming, fail-deadly, detonation, controlled-disarmament, and world-end cleanup. The audit found no direct free-unit, stockpile, core, war-goal, or mission-completion farming loop in the decision definitions reviewed.

## Files changed and exact identifiers

Changed by this audit:

- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_decision_runtime_audit_handoff.md`

No decision, mission, category, scripted GUI, localisation, effect, trigger, or constant identifier was modified.

## Meaningful validation

- Reconciled all 17 Event 016 category declarations against every Event 016 decision-file category consumer. There are no undeclared or unused Event 016 decision categories.
- Reconciled 312 decision/mission ids, title keys, description keys, 199 custom tooltip/cost keys, 36 scripted-localisation getters, and 148 icon references.
- Reconciled all Event 016 decision custom trigger/effect calls against 947 custom scripted definitions. There are no unresolved calls.
- Reconciled 589 Event 016 script-constant references and 165 consumed focus-unlock flags. There are no missing constants or missing unlock producers.
- Used `hoi4.probability_inspect` for `common/decisions/016_brilliant_scientist_foreign_decisions.txt`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebd1922cd00f9cf545aedc3ac3febdab9d731b33a1af80b2c13608563374baf0/f2dde471795cbbca598a83817eddb5786092d066acc36ddd0c3f4084ec044a63/probability-inspect-39cf5e7c5a56.json`.
- Used focused `hoi4.event_inspect` on `chaosx.nr16.1`. Its graph is partial because broad workspace helper/lifecycle projections were deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72024ad736007b548489c59f0a4d163a3ee5925266252ea4415d8f85a1b23734/4b7db8b2cc998125f25f10bd5d317bc36ecb2f6c161a45251405f8047ecdda8d/event-lint-947207ac4cdf.json`.

## Skipped meaningful validation and remaining risks

- No live HOI4 session was launched, per repository rules. Exact timer ordering, target persistence across every foreign event response, and full terminal-world scenarios remain user-owned runtime validation.
- `hoi4.gui_inspect` for `kruger_directorate_container` returned `SCAN_BYTE_LIMIT`, so no `hoi4.gui_render` fidelity artifact is available. The initial workspace inspection artifact is limited to the MCP workspace result.
- No source patch was made, so no probability comparison was applicable. Foreign-AI rankings remain unevaluated because the analyzer reported an incomplete candidate pool.
- This audit deliberately did not redesign the missing intermediate terminal status line in the Directorate GUI, expand decision depth, add assets, or alter balance philosophy.

## Skills used

- `chaos-redux-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-subagents`
- `chaos-redux-mtth`

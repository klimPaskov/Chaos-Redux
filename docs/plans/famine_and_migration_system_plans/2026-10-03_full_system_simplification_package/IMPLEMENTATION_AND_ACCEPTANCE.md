# Future implementation and acceptance contract

Disposition: `unresolved` future work.
This document becomes executable work only under a later explicit human launch and recorded acceptance of its selected design.
No work is scheduled by its existence.

## Dependency order

1. Freeze current source and reconcile old accepted obligations, current owners, and this proposal's acceptance ledger.
2. Audit/fix service proof, physical route repair, reachable famine severity, and payment preflight/result ordering before merging actions.
3. Preserve the neutral transfer primitive and public adapters; define one bounded owner-local operation receipt and one terminal-claim contract.
4. Implement famine commitments first, then migration protection/settlement commitments, retaining shared route and payer rules.
5. Replace redundant player actions only after their successor contracts and exact consumers exist.
6. Wire selected regional terms and current external adapters; leave missing owner receipts explicitly blocked or accepted/queued.
7. Complete AI baseline/owner-patch/comparison, native presentation, transaction/scenario audits, asset coverage, localisation, permanent docs and catalog alignment.
8. Run one final improvement closure review after prior accepted changes are resolved; do not expand the system again simply because another historical parallel exists.

Do not attempt a wholesale helper rewrite while repairing the public loop.
Small contract defects can be fixed in a coherent tranche with its own receipt tests; redesign follows only after that foundation is trustworthy.

## Exact touchpoints and ownership

`SOURCE_INVENTORY.csv` supplies the current hashed file inventory.
The table below defines responsibility/dependencies, not permission for the planning agent to edit them.

| Work surface | Exact paths / identifiers | Dependency and future owner |
| --- | --- | --- |
| Famine response and missions | `common/decisions/famine_decisions.txt`; `common/decisions/categories/famine_decision_category.txt`; all ten actions and two missions enumerated in the retirement table. | Parent and bounded decision owner. Shared quote, exact selected subject, operation term and physical objectives. |
| Migration actions and missions | `common/decisions/migration_decisions.txt`; `common/decisions/categories/migration_decision_category.txt`; eighteen weighted actions and four missions. | Parent and bounded decision owner. Exact cohort selection, policy terms, service contracts and terminal claims. |
| Famine evaluator/stock/stages | `common/scripted_effects/famine_core_effects.txt`; `common/scripted_triggers/famine_core_triggers.txt`; `common/script_constants/famine_core_constants.txt`. | Parent/architect. Stage reachability and reserve marginal benefit; preserve mortality ownership and population floor. |
| Famine decision/phase owner | `famine_decision_owner_effects.txt`, `famine_decision_phase_effects.txt` and paired documentation/triggers in `common/scripted_effects` / `common/scripted_triggers`; `famine_decision_constants.txt`, `famine_mission_constants.txt` in `common/script_constants`. | Parent/architect and decision owner. Case-scoped suppression, operation lifecycle, payment, missions, timing. |
| Famine relief/opposition | `common/scripted_effects/famine_relief_effects.txt`, `famine_opposition_effects.txt`, paired `.md` and trigger files; `famine_relief_constants.txt`, `famine_opposition_constants.txt`. | Proven donor stock and route modes precede routine delivery; opposition follows sustained exact responsibility. Every weighted edit goes through probability auditor. |
| Migration cohorts | `common/scripted_effects/migration_core_effects.txt`, `migration_cohort_history_effects.txt`; `common/scripted_triggers/migration_core_triggers.txt`, `migration_cohort_history_triggers.txt`; `migration_core_constants.txt`, `migration_custody_constants.txt`. | Architect preserves eight-array alignment, identity, history, reservations, terminal accounting and independent retirement. |
| Reception/proof | `common/scripted_effects/migration_capacity_effects.txt` and `.md`; `migration_decision_owner_effects.txt` and `.md`; `migration_decision_phase_effects.txt` and `.md`; paired owner triggers; `migration_decision_constants.txt`, `migration_mission_constants.txt`. | Correct proof-of-one rejection before service automation; prove exact subject/host and source-safe capacity. |
| Movement selectors | `common/scripted_effects/migration_destination_selection_effects.txt`, `migration_spontaneous_movement_effects.txt`, `migration_forced_movement_effects.txt` and paired `.md`/triggers; their constants. | Route/capacity/food/persecution inputs stay owner-proven; batching does not combine physical rows. Complete dynamic pools before probability claims. |
| Persecution/custody | `common/scripted_effects/migration_persecution_effects.txt`, `migration_adapter_effects.txt` and paired `.md`/triggers; `migration_persecution_constants.txt`, `migration_adapter_constants.txt`. | Exact existing owner actions produce/clear facts; no ideology/site-presence proxy. Preserve current Gods of Africa service identity and cleanup. |
| Neutral physical transaction | `common/scripted_effects/civilian_transfer_effects.txt`; `common/scripted_triggers/civilian_transfer_triggers.txt`; `common/script_constants/civilian_transfer_constants.txt`; existing exact population-loss helper and its docs in `common/scripted_effects/chaosx_dynamic_effects.*`. | Parent/architect. Reuse one atomic transfer and inverse/quarantine; no new population path. Railway projection observes physical damage only. |
| Corridors | `common/scripted_effects/humanitarian_corridor_effects.txt` and `.md`; paired triggers/constants. | One offer/route/cohort generation; local pending presentation. Permission does not substitute for delivery. |
| Sparse runtime | `common/scripted_effects/humanitarian_runtime_effects.txt`; `common/on_actions/humanitarian_runtime_on_actions.txt`; registered state/country processors in both core files; `humanitarian_runtime_constants.txt`; existing `chaosx_on_actions_chaos_meter.txt` host coordinator. | Insert finite operation jobs into existing registries only. No worldwide daily/weekly/monthly scan, no automatic CXT grants. |
| CXT | `common/scripted_effects/famine_cxt_test_effects.txt`, `migration_cxt_test_effects.txt`; `common/ideas/famine_cxt_extension_ideas.txt`, `migration_cxt_extension_ideas.txt`; `docs/testing/chaosx_test_country.md`. | Keep package-owned idempotent setup and modifier-free carrier. Add player-triggered fixture decisions only where necessary; reception capacity setup must not create people. |
| Report/category presentation | `interface/famine_report_header.gui`, `migration_report_header.gui`; `common/scripted_guis/famine_report_header_scripted_gui.txt`, `migration_report_header_scripted_gui.txt`; category attachments; report effects/triggers and famine/migration scripted-localisation files. | These are shared system-owned category headers, not a named event-owned GUI. Parent owns GUI changes; `chaosx_event_ui_worker` is not eligible solely because events feed these systems. Mandatory native reference/baseline/post-change evidence. |
| Map projections | `common/map_modes/chaosx_state_map_modes.txt`, its owner constants, `migration_presentation_effects.*`, `famine_*` presentation and scripted localisation, `interface/mapmodes_interface.gfx`. | Keep exactly two mapmodes and transaction-time state projections. Map render validates geography/rail/port substrate; it cannot by itself prove scripted mapmode colors/privacy/branches. |
| Costs/text | `common/scripted_localisation/humanitarian_cost_scripted_localisation.txt`; `localisation/english/humanitarian_cost_l_english.yml`; separate famine/migration and mission localisation files; `interface/chaosx_texticons.gfx`. | One quote and inclusive gate; every spent/committed type has correct texticon. Localisation worker audits meaning, fraction precision, blocked and native row fit. |
| Assets | `interface/famine_system.gfx`, `migration_system.gfx`, `famine_report_pictures.gfx`, `migration_report_pictures.gfx`; existing `gfx/interface/decisions/famine/`, `migration/`, state modifiers, report scenes, achievement triplets and mapmode buttons. | Reconcile requirement→sprite→consumer coverage, actual binary pixels, dimensions, alpha and provenance; historical total 61 is not coverage proof. Retire consumers, not unrelated assets. |
| Achievements | `common/scripted_effects/humanitarian_achievement_effects.txt`; paired triggers/constants; `common/achievements/chaos_redux_achievements.txt`; `humanitarian_achievement_l_english.yml`. | Preserve all eight accepted identities and exact reachability after merges; success is once per valid cohort/operation generation. |
| External owners | `013_natural_disasters_effects.txt`, `020_black_plague_effects.txt`, `fallout_consolidated_effects.txt`, `cbrn_occupation_effects.txt`, `camp_repression_rework_effects.txt`, `035_great_depression_external_adapters.txt`; current event/cluster/scenario and Gods of Africa owners discovered by caller census. | Parent coordinates owner-specific boundaries. Preserve direct mortality and site ownership; verify current receipts instead of relying on old integration matrix. |
| Design/docs/catalog | Three `docs/systems/*_system.md` documents; eight old specs and supporting matrices; `source_of_truth_map.md`, `completion_report.md`, `handoff_dispositions.md`, `ai_probability_current.md`; affected event docs and authoritative workbook. | Documentation curator after implementation facts; workbook worker after wording is final. Export CSVs only through `.tools/export_event_catalog_csv.py`. |

Shared dynamic public effects/triggers require explicit purpose, scope, inputs/outputs, defaults, side effects, and usage in their owning paired documentation.
Do not rename external public contracts merely to match the new action labels.

### Proposed new owner contracts

These names are proposed implementation surfaces, not current definitions or accepted APIs.
Keep their bodies bounded to already registered subjects and existing neutral primitives.

| Proposed file family | Public responsibility and receipt |
| --- | --- |
| `common/scripted_effects/famine_operation_effects.txt` and `.md`; paired `famine_operation_triggers.txt`; `common/script_constants/famine_operation_constants.txt` | `famine_begin_response_term`, `famine_process_response_slice`, `famine_finish_response_term`: famine actor/subject/route/generation, finite food budget and term; return actual food debit/credit, useful relief and unused expenditure. No cohort or population ownership. |
| `common/scripted_effects/migration_operation_effects.txt` and `.md`; paired triggers/constants | `migration_begin_protection_term`, `migration_begin_durable_plan`, `migration_process_operation_slice`, `migration_finish_operation`: exact cohort/host/generation, progress, service and terminal claim; movement only through `civilian_transfer_execute_transaction`, integration only through the current migration owner. |
| Narrow neutral `common/scripted_effects/humanitarian_logistics_effects.txt` and `.md`; paired triggers/constants only where needed | `humanitarian_reserve_logistics`, `humanitarian_release_logistics`: exact payer and paid equipment/factory quote, operation identity, remaining/released amount. Physical resource allocation only, with no player category, simulation, population or policy ownership. |

Every begin call resets output state, performs one fresh all-input preflight, claims an operation identity and resource receipt, and publishes success only when the owner's terms can be established atomically.
Every slice resolves its exact identity and payer, revalidates dirty owner facts and spends only its remaining finite budget.
Every terminal/cancel call releases the recorded remainder once and preserves prior useful-work receipts.
The shared allocator must reconcile actual stock/committed factory availability across parallel famine/migration cases, preventing both owners from claiming the same equipment or service while allowing independent affordable cases.
Reuse the existing famine and migration CXT setup effects/carriers for bounded player-triggered operation fixtures; the neutral allocator does not become a third content-grant system.

## Decision-density and payment proof

Inventory every action instance per target, not only every unique action ID.
For each named fixture, report primary actions, offer responses, missions, target controls, repeated state instances, and the intervention sequence over time.
Expected normal presentation is three to five primary actions, never more than six actionable choices for the selected current case, one to three urgent subjects/objectives, and no hidden permanent counters.
These are design and readability targets, not HOI4 engine row limits; native capacity/clipping requires actual consumer evidence.
A ten-state crisis must not repeat ten complete action grammars in the native list.
If selected-case native targeting is unavailable, that presentation conclusion remains blocked pending an explicit accepted design choice.

For each action compare displayed quote, available gate, custom-cost gate, activation debit/reservation, actual slice consumption, expiry/cancellation release, partial refund, and AI affordability.
Test exact balance, one resource below, one above, fractional amount, changed target, changed actor, stale donor/capacity receipt, and partial useful work.
Expected rejected/no-service transaction: zero final spending, zero population/Deaths/reward/success receipt.
Expected partial service: spending/loss only for measured work plus explicitly accepted setup expenditure, one release of remaining reserved stock, no fabricated full-success outcome.
No action consumes more than four distinct types; no inline row displays more than three values.

## Measurable scenario expectations

Numbers below are proposed calibration targets or invariants, never historical casualty quotas or existing test results.
Use identical initial facts for comparisons, including live population, component inputs, prior exposure, reserves, routes, capacity, policy, actor, generation, damage, equipment and date.
Keep a no-intervention control beside each managed case.

| Scenario | Fixture and expected behavior | Evidence / measurable gate |
| --- | --- | --- |
| S01 healthy peace | Safe populated state, functioning routes, no source. | No famine mortality, no new cohort, hidden categories; two mapmodes available. |
| S02 short interruption | 7-day transport loss, 30 days initial stock, no other harm. | No full-famine mortality; one ordinary response at most; no expensive forced emergency. |
| S03 reachable severe famine | Population 1,000,000, harm vector 95/100/90/95/90/95/90, no effective relief, depleted stock. | Proposed score/threshold can enter catastrophe without all seven components at 100. Prove candidate duration and early-relief prevention. |
| S04 managed versus ignored | Same severe initial state, funded land relief versus no response for 90 days. | Managed cumulative famine deaths at most half control; one funded term has visible material service, not only ±1–3% country modifiers. Proposed ignored full-famine band 1–5% loss over 90 days for the stated ordinary fixture, catastrophe 10–30% over 60 days for the declared high-harm fixture; tune only from full factor evidence. |
| S05 physical rail repair | Positive `damaged_building_level@rail_way`, operation funded, route later repaired by native work. | No success while real damage/control requirements fail; actual repair enables receipt and hold objective; no projection clearing as substitute. |
| S06 land/sea/air quotes | Same served population with three valid route modes. | Land consumes/commits no convoy; sea no train; air quarter surface throughput and higher fuel. Full four-type budget and matching payer. |
| S07 island at war | True isolated island, port/convoys/escorts healthy versus proven blockade. | War/island alone causes no blockade. Blockaded case offers at least two materially different viable strategies when both are proven. Geography proof required. |
| S08 extraction correction | Crop/transport harm with positive responsible extraction. | Suspension changes actual causal input immediately and prevents severe escalation versus control; continuation has a real beneficiary and attributed consequence. No small repeat reward as its sole benefit. |
| S09 service proof | Identical positive shelter/medical amounts with proof zero, one, stale generation, and accepted contract. | One canonical proof contract; ordinary reception succeeds with its legitimate token, missing/stale proof rejects, no `2` workaround spread. |
| S10 ten affected states | Ten active states; three urgent, others stable or lower risk. | Selected case has at most six choices, category summarizes unselected obligations, funded bounded upkeep serves at most three exact states. Proposed 60-day mixed crisis needs four to seven strategic interventions, no per-state weekly clicks. |
| S11 concurrent offer and famine | Pending corridor offer in one exact migration case plus unrelated food emergency. | Offer responds once; famine relief remains usable; suppress only conflicting route work. |
| S12 overload and settlement | Host load 120% of capacity, ready safe hosted cohort, different active origin crisis. | Distribution/settlement can relieve exact burden without awaiting national resolution; no deletion or population creation. Closure preserves hosted/trapped people. |
| S13 exposure specificity | One exposed arrival and one clean cohort under identical host policy. | Medical terms require exposed receipt; clean refugees create no outbreak by identity. Three supported outcomes remain possible for eligible cases. |
| S14 safe/persecuting destination | Complete pool including safe internal state, same-ideology persecutor, full-capacity neighbor, accepting safe partner. | Ineligible candidates exactly zero/excluded; ideology cannot rescue unsafe/persecuting choice. If all excluded, no population mutation and living trapped obligation preserved. |
| S15 evacuation priority | Authentic vulnerable and worker identity, same danger/route. | Different service burden and durable consumer; absence of identity/consumer leaves choice unresolved rather than simulated demographic facts. |
| S16 integration progress | Exact hosted cohort, funded 60-day term, actor/food/service stable. | No terminal integration/load release on day zero; progress persists, final measured terminal result once. No immediate manpower farming. |
| S17 interrupted durable plan | Change origin safety, host control, funding or service at midterm. | Pause/cancel appropriate work; preserve exact people/host/history; only unused resources released once; no forced-return substitution. |
| S18 transfer conservation | Zero-death, hazardous route, floor clamp, partial destination credit, failed reception/bind, failed inverse. | Valid identity `origin debit = route deaths + survivor credit`; invalid transactions roll back or quarantine; Deaths never applies another physical debit. Test failures between every commit stage. |
| S19 multiple cohorts and cycling | Two cohorts in one state, ambiguous selector, A→B→A, repeated terminal/reload. | Exact row selection, no arbitrary aggregate debit, no repeated reception/outcome reward, visit/terminal history survives. |
| S20 retirement and external owners | Famine recovers while migration obligation persists; owner-specific death precedes later hazard request. | Independent retirement; source pressure/flight adds no second direct death; full external receipt required. Undefined APIs stay explicitly blocked. |
| S21 historical variants | Greece neutral maritime access, Bengal distribution, Leningrad constrained lift, Ireland memory, later-policy analogues. | Same small action grammar produces different route/concession/priority/durable consequence; profile/date alone produces no fixed casualty script. |
| S22 finite automation | Term ends, payer resources fall, target becomes invalid, dirty callback repeats. | Maximum four funded weekly slices per term; no paid renewal by default, no unauthorized policy change, no repeated no-result reward, no new world scan. |

“At least two strategies” means outcomes differ in conserved population, food stock, transport commitment, physical restoration, diplomatic access, or durable burden.
It does not mean two buttons producing the same packet with different names.
If current engine facts cannot support a numeric outcome band, label that target unresolved, explain the missing factor, and do not simulate invented route state.

## Weighted AI and timing evidence

`chaosx_ai_probability_auditor` is read-only and starts with `hoi4.probability_inspect` for every in-scope weighted surface.
Freeze exact before source files and pool manifests outside runtime-loaded folders; source hash alone cannot replace a `before.path` when the live compare schema requires a path.
The owner selects accepted balance targets and applies changes; the specialist performs `hoi4.probability_compare` on the same named scenario set after every weight/probability/timing patch.

Use names `fm03_severity_reachability`, `fm06_route_modes`, `fm07_blockade_response`, `fm08_extraction_correction`, `fm09_service_affordability`, `fm11_parallel_offer`, `fm12_host_overload`, `fm13_exposed_reception`, `fm14_destination_safety`, `fm16_durable_choice`, `fm22_term_renewal`, and the old named scenarios where still applicable.
Inspect famine/migration decision and mission scores, destination custom pool, relief donor custom pool, catastrophic-opposition custom pool, and corridor response scores separately.
Preserve source revision, scenario hash, exact source paths, candidate pool, all required inputs, unresolved terms and artifacts.

Expected ordinal choices: valid cheap surface supply outranks airlift when it can arrive in time; air bridge gains preference when it prevents the next mortality interval; spare-capacity protective reception outranks closure; exposed cohort with medical service prefers controlled reception; full host prefers redistribution/durable plan; known persecution excludes safe voluntary return; source harm/visibility/strategic motive bound extraction and concealment.
Sweeps vary population, stage/exposure, stock, headroom, equipment/fuel, war and policy within each declared domain, looking for reversals, starvation, harmful dominance and unaffordable positive scores.
Complete custom pools enumerate every actual candidate from a fixed fixture with route, stock, policy, safety and capacity receipts.
Sample simulation only when the selection semantics and complete pool are known; report seeds/run counts/confidence.
Decision `ai_will_do` can remain score-only and is not automatically a normalized probability or waiting-time distribution.
Sparse cleanup and transfer invariants are deterministic; do not turn them into random-pool sequences to appease a tool.
Automation duration is deterministic owner scheduling unless an actual weighted timing surface exists.

## MCP and native presentation gates

Before work, discover live schemas and separately confirm service response/version/client support; exposed tool metadata or installed package version does not prove connected process health.
Use reference context/search/read for offline wiki and installed docs, source lookup for exact precedents, and retain citation path/line/revision.
If any route fails to return, retain exact request/error/elapsed boundary, stop repeated long retries, read the relevant local sources, and leave affected engine conclusions open.

Use `hoi4.decision_inspect` inventory/inspect before changes and compare over matching actor/target fixtures afterward where the installed schema supports proposed/current source comparisons.
It establishes source/fixture gating, payment and lifecycle, not native row geometry.
Use `hoi4.gui_inspect` and `hoi4.gui_render` for both `famine_report_header_window` and `migration_report_header_window`, category parent/attachment, and the actual native decision consumer if supported.
Required native matrix: 1920×1080 and 2560×1440, both UI scale 1.0.
1280×720 and 1366×768 may be optional stress cases; they do not replace either required resolution.
Review full window, category art/report space, costs, longest state/country labels, empty/full lists, hover, disabled, exhausted, warning, active and terminal states, and all click regions.
Create an accepted scoped reference before layout redesign.
Preserve exact before `.gui` source and baseline artifacts; use supported `sourceBaseline` for source comparison and `comparisonScenario` only for scenario comparison, not as a made-up snapshot facility.
Every visible clipping, spacing, asset, background, text, alignment, state or click-region defect blocks visual completion.

Use `hoi4.map_inspect` and `hoi4.map_render` for proposed actual states, provinces, ports, railways, supply nodes, adjacency and control substrate.
Map render supports a geographic layer/overlays, not general scripted mapmode execution or route arrows.
Two-mapmode fill/border priority, tooltip privacy, receipt invalidation and context need their supported source/mechanic evidence and user-owned live consumer facts; retain the unsupported execution gap explicitly.

For any changed external event boundary use narrow `hoi4.event_inspect`, render and compare on its exact root/owner only.
Do not create synthetic famine/migration event roots to generate a graph.
No focus or technology redesign is proposed; if a later accepted integration actually changes those surfaces, read their skills and require their inspect/render/compare gates.
If an actual technology/doctrine touchpoint enters accepted scope, verify standalone Technology Tree Viewer separately and record its package gap if absent; current redesign has no such gate.
Do not use rewrite tools during the audit or planning pass.

Use `hoi4.mechanic_test` / `hoi4.scenario_test` only with confirmed live schemas and source-backed typed fixtures; unsupported effects remain unresolved.
They do not execute the game or replace save/runtime evidence.
Agents never launch HOI4 or take over live validation; the human owns live consumer observations.
If a supplied save resolves a disputed state, use `chaos-redux-save-inspection` before forming the hypothesis.

## Docs, catalog, and independent review

After accepted implementation facts settle, update famine, migration and neutral transfer permanent docs separately.
Reconcile each affected old spec/matrix/handoff using the AGENTS dispositions with acceptance and implementation evidence distinguished.
Promote accepted proposal sections to the eight-part source pack; retain historical handoffs as provenance, not live instructions.
Refresh current probability and completion reports to the final revision.
Update event docs and workbook rows only where their actual owner integration or player wording changes.
Event 149 remains retired/absorbed/unavailable; create no system event row, incident event, log entry or pacing weight.
Use `chaosx_spreadsheet_doc_worker` after localisation facts, then run `python .tools/export_event_catalog_csv.py`; never edit catalog CSVs directly.

Required final specialists: decision/mission auditor, AI/probability auditor, localisation auditor, system-adapted completion auditor, and documentation curator as needed.
Use a bounded architect for reusable transaction/operation contracts.
Asset workers are required only for a real accepted missing asset; parent retains all final wiring and review.
Shared report headers remain parent-owned and do not qualify for the event-owned GUI worker.
All specialist prompts must be self-contained, `fork_turns="none"`, exact file responsibilities, current acceptance decisions, allowed report paths, and the instruction that other agents' edits must be preserved.

## Decisions still unresolved

| Question | Recommended choice | Why it needs a recorded decision |
| --- | --- | --- |
| Q01 current-case targeting | One selected exact case with native targeting, maximum three urgent subjects. | The live native consumer must support selection/list curation without a new full GUI; unsupported presentation cannot be waived. |
| Q02 catastrophe rule | Start with threshold 90 plus depleted stock/effective-access failure and 21-day persistence. | It changes accepted balance. Alternative exposure-based entry must not be implemented simultaneously without explicit design. |
| Q03 payment commitment | Reusable transport reservation and slice-based consumption/refund. | Engine stock/equipment identity, losses and actor transitions need proof; destructive payment is not an implicit fallback. |
| Q04 worker priority | Preserve only with exact worker identity and a durable production consumer. | Current similarity does not prove demographic identity; otherwise one evacuation mode is a deliberate accepted simplification. |
| Q05 concealment/extraction | Contextual policy terms; benefit must exist beyond small country modifiers. | A real military/economic beneficiary and disclosure owner may be absent. Retire or keep queued only with reason. |
| Q06 routine automation | Funded 28-day term, four weekly slices, no paid auto-renewal. | Future human launch must accept the finite spending authority and renewal behavior. |
| Q07 persistent settlement | 60-day progress with exact terminal release. | Contract changes timing and eligibility; decide whether staged partial terminal slices are worth their additional identity work. Default one terminal commit. |
| Q08 existing integration blockers | Close exact owners available now; formally queue others by owner/dependency. | Missing accepted requirements cannot be silently removed to declare completion. |
| Q09 broad profile institutions | Verified regional terms only; preserve fifteen IDs. | Ceará/Congo/Ethiopia institution detail and exact longer routes need further primary-source/map evidence. |
| Q10 mortality bands | Scenario-relative targets first; numeric bands calibrated from complete factor model. | Numeric ranges are proposed play calibration, not historical claims or current observed performance. |

The future launch may authorize the recommended direction within its scope, but does not erase these factual uncertainties.
Resolve dependent choices before changing their surfaces, continue independent authorized work, and record any exact blocker instead of inventing missing capabilities or facts.

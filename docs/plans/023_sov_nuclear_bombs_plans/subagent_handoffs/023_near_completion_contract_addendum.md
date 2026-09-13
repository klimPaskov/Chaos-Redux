# Event 023 near-completion accepted-contract addendum and parent handoff

Review date: 2026-09-05.
Disposition: **queued** for accepted-contract repairs; **blocked** for implementation clarifications awaiting parent decisions and incomplete validation; overall event closure **blocked**.
This is a plan-only output, not an implementation or closure certificate.
The planner wrote only this file and changed no gameplay, localisation, assets, GFX, spreadsheets, generated files, or runtime configuration.

## Decision

Do not add another broad mechanic, country package, focus route, GUI, visual layer, or super-event.
The accepted package already has a distinctive playable premise: managing an additive arsenal through custody, preparation, deterrence, bargaining, fracture, and restraint.
Its remaining depth problem is that several named actions do not yet produce or verify their promised physical or diplomatic outcome.
More content would conceal those gaps rather than improve the event.

A clean closure handoff is not justified at this snapshot.
The source contains test-result selection after native detonation, ledger/native-stockpile divergence, unilateral reciprocal-restraint receipts, an ultimatum mission scope mismatch, and exchange presentation triggered without an observed answering detonation.
These are accepted-contract connection gaps, not requests for a larger feature.
Source findings below remain distinct from unresolved engine execution and MCP evidence.

The acceptance basis is the parent/user's current instruction explicitly identifying this Event 23 package as accepted, together with its named prompts and Parts 1–10.
Older reports and placement in `docs/specs` are not independent evidence of approval.
In this document, **queued** means an already accepted behavior remains unfulfilled and is assigned to the parent for repair; it does not mean the parent has accepted every proposed helper or implementation detail below.
Any change to an accepted behavior requires a recorded parent acceptance within user-authorized scope or an explicit user decision.

## Authoritative proposal dispositions

Every recommendation below inherits its section's disposition unless this register explicitly gives it a narrower disposition.
"Unresolved" elsewhere describes missing evidence or a pending decision, not a sixth proposal disposition.
An accepted behavior stays queued even when the proposed implementation mechanism is blocked; neither status waives that behavior.

| Proposal or follow-up | Disposition | Exact scope and acceptance basis | Required before closure? |
| --- | --- | --- | --- |
| Retain the completed repairs rather than repeat them | implemented | Exact identifiers and acceptance bases in the implemented-findings table | Retain and regression-check |
| C1: outcome-first test/demo/strike/accident/demolition and shared consequence ownership | queued | C1 files/helpers; coding prompt and Parts 2–4, 7 | Yes |
| C1: native completion observation and target-specific delivery proof | blocked | C1 `launch_nuke`/`on_nuke_drop` integration and route predicates; missing engine/route evidence | Yes |
| C2: actual demand terms, correct mission scope, bilateral restraint, answered exchange | queued | C2 EV `.120/.150/.161/.162` and listed helpers; Parts 4–7, 10 | Yes |
| C2: optional additional ordinary response event | blocked | EV only; parent must first determine whether `.120` can safely serve both contexts | No particular extra event is required; real bilateral response is required |
| C2: unsupported native settlement operation, if discovered | blocked | The affected named demand family and C2 settlement helpers; no accepted family may be silently omitted | Yes, if that limitation prevents the accepted family |
| C3: exact custody/native deltas, one-device transactions, actor-owned stages and cleanup | queued | C3 RFX/RTR/EFX/ETR/DEC/OA/ATR/AFX; Parts 2, 6, 7, 10 | Yes |
| C3: mixed native-stockpile attribution policy | blocked | Shared consumption and C3 transaction boundary; explicit parent choice and engine evidence missing | Yes |
| C4: phase reachability, knowledge monotonicity, later doctrine reform, meaningful support outcomes | queued | C4 exact files and identifiers; Parts 2–4, 6, 8 and decision map | Yes |
| C4: numerical reform costs/duration and associated AI targets | blocked | DEC, CONST, MTTH and doctrine helpers; parent must record exact accepted tuning before implementation | Yes for the accepted reform route; no invented values are approved here |
| C4: safe-site, transport-corridor and delivery-map acceptance | blocked | C4 site/route predicates; map render and dynamic route evidence unavailable | Yes |
| C5: repair existing reactor observation, scope, capacity and lifecycle connections | queued | EV `.180/.181`, EFX/ETR and existing reactor handoff; Part 5 | Yes |
| C5: resolve prior reactor architecture, free entitlement semantics and timing targets | blocked | `023_reactor_architect.md`, Part 5, CONST/MTTH and named probability scenarios; parent decision/native queue evidence missing | Yes; do not add a second reactor architecture |
| C6: documentation, semantic localisation, achievement truth, authoritative catalog reconciliation, CXT documentation and current audits | queued | Exact C6 table files/identifiers; Parts 8–10 and named prompts | Yes |
| C6: outstanding visual acceptance and same-scenario MCP comparison | blocked | GFX/manifests and MCP evidence section; current evidence is insufficient | Yes where required by package acceptance |
| Standalone Technology Tree Viewer availability | blocked | Installed 3.0.7 package inspection; no standalone entrypoint identified | Package/tooling gap, not a new gameplay mechanic; retain explicit limitation |
| Shared Event 32 compatibility review | blocked | `common/scripted_effects/032_missiles_operations_effects.txt`; parent review of C1/C3 shared ownership changes not performed here | Yes before shared integration is closed |
| Extra trees, tags, GUI, visuals, meters, exchange presentations or cluster creation | rejected | Exact exclusions below and current user lock | No; do not implement |
| Earlier catalog membership claim | superseded | `023_spreadsheet_worker.md` replaced by `023_spreadsheet_cluster_cleanup.md` for membership only | No duplicate cleanup; final wording/status still queued |
| Promote new clarifications into existing accepted specs | blocked | Existing Parts 2–7, 9–10 and decision map; await recorded parent acceptance | Required if those clarifications are accepted; never promote approval by location |

This is implementation-ready for the source-local repairs explicitly described below, but it is not authority to invent missing balance values, native capabilities, or settlement operations.
Those particular choices are blocked and remain visible to the parent.

## Locked scope

- Keep Event 23 Minor Fire-Once, SOV-owned, Chaos level 2, entry `chaosx.nr23.1`.
- Preserve exactly +100 additive baseline atomic bombs, with no baseline free reactor or delivery aircraft.
- Preserve cumulative evolution packages 175/275/400/600, increments 75/100/125/200, and reactor totals 2/4/6/8.
- Disabled evolutions grant, unlock, and record nothing.
- Preserve separate physical custody, technical access, command formation, and delivery integration.
- Retain the conserved device ledger and ordinary decisions/missions, normally three to five primary actions, maximum six, and one to three active missions.
- Keep one nonterminal multi-major exchange super-event separate from Fallout and Final Silence.
- Preserve shared ownership of test, demonstration, strike, accident, demolition, deaths, contamination, condemnation, and direct Chaos consequences.
- Add no tag, focus tree, portrait, flag, custom unit, model, animation, dedicated scripted GUI, triggerable scenario, or speculative Arms-race membership.
- No whole-world periodic scan, new fallback, or alternate reward is authorized by this review.

## Source map

The aliases below identify exact implementation files for every recommendation.

| Alias | Exact repository path |
| --- | --- |
| EV | `events/023_soviet_nukes.txt` |
| DEC | `common/decisions/023_sov_nuclear_bombs_decisions.txt` |
| CAT | `common/decisions/categories/023_sov_nuclear_bombs_categories.txt` |
| EFX | `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` |
| RFX | `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` |
| RTR | `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt` |
| ETR | `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt` |
| OA | `common/on_actions/023_sov_nuclear_bombs_on_actions.txt` |
| CONST | `common/script_constants/023_sov_nuclear_bombs_constants.txt` |
| MTTH | `common/mtth/023_sov_nuclear_bombs_mtth.txt` |
| ATR | `common/scripted_triggers/023_sov_nuclear_bombs_achievement_triggers.txt` |
| AFX | `common/scripted_effects/023_sov_nuclear_bombs_achievement_effects.txt` |
| ACH | `common/achievements/chaos_redux_achievements.txt` |
| LOC | `localisation/english/023_soviet_nukes_l_english.yml` |
| GFX | `interface/023_sov_nuclear_bombs.gfx` |

The complete current specification package, including the six prompts, Parts 1–10, decision map, probability scenarios, research, technology/DLC notes, catalog notes, README, and historical source/audit report was inspected.
The named Event 23 implementation families and latest country, decision, localisation, asset, spreadsheet, reactor, probability, and completion handoffs were reviewed.
The historical source/audit report describes the planning environment, not the availability of today's repository or tools.

## Implemented findings: retain, do not request again

These dispositions concern the named source repair, not whole-feature runtime completion.

| Finding | Exact evidence | Disposition and acceptance basis | Required before closure? |
| --- | --- | --- | --- |
| Four opening doctrines | EV `.2.party`, `.2.military`, `.2.scientific_safety`, `.2.dispersed_commands`; EFX `sov_nuclear_bombs_opening_doctrine_option` | Implemented in source; opening prompt, Part 2, decision map | Retain and regression-check; do not recreate the opening |
| Numeric package and disabled-stage checks | CONST `sov_nuclear_bombs_evolution`; EFX opening/progression helpers; ETR `event_can_enable_evolution_i` through `_iv` | Implemented in source; current user lock and Part 5 | Retain; ledger, timing, and reactor lifecycle still require the separate checks below |
| Terminal predicates | RTR `sov_nuclear_bombs_terminal_world_state_is_active`, actor/action predicates; EV `.160/.161/.162` | Implemented in source for Fallout and Final Silence gates; Parts 7 and 10 | Retain; do not report these predicates absent |
| Canonical world-threat source | EFX `sov_nuclear_bombs_refresh_world_threat_source`; `common/scripted_effects/chaosx_dynamic_effects.txt` `refresh_world_threat_state` consumes `world_threat_source_sov_nuclear_bombs` | Implemented source registration; Part 7 | Retain; real threat/settlement semantics remain separate |
| Inclusive resource affordability | `common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt`, five `sov_nuclear_bombs_can_pay_*_cost` predicates | Implemented inclusive checks; decision prompt and decision audit | Do not repeat the old strict-comparison repair |
| Event 5 pre-release integration | `common/scripted_effects/005_soviet_collapse_effects.txt`, `soviet_collapse_release_scope_from_soviet_collapse_owner`, snapshot calls at current lines 4290, 4314, 4349, 4384 | Implemented source call placement; Part 6 and current country audit | Retain; this does not prove subsequent ledger transactions |
| Separate breakaway mission stages and category visibility | DEC technical-access, command-formation, delivery-integration missions; CAT includes `event_has_breakaway_custody_crisis` | Implemented definitions and source visibility; Part 6 | Retain; staged reachability and operational outcome remain queued |
| Dedicated reactor completion event | EV `chaosx.nr23.181`; EFX `sov_nuclear_bombs_verify_pending_reactor_construction` | Implemented source surface; reactor architect requirement | Do not ask for another verifier; repair its lifecycle |
| Disablement icon and breakaway report | DEC `sov_nuclear_bombs_disable_devices`; GFX `GFX_decision_sov_nuclear_decision_device_disablement`, `GFX_report_event_sov_nuclear_breakaway_custody`; EV `.110` | Implemented wiring in current source; asset prompt and later asset handoffs | Parent visual acceptance remains; no regeneration requested |
| Ultimatum refusal key | EV and LOC `chaosx.nr23.120.refuse` | Implemented collision repair; localisation audit | Retain; unrelated `.161/.162` wording still needs semantic review |
| Audio allocation documentation | `docs/super_events/023_sov_nuclear_bombs_super_event_research.md`, `music/chaosx_music_track_list.html`: playback/visible ID 108 and `sound/023_sov_nuclear_bombs/super_event_108_first_major_exchange.wav` | Implemented alignment; super-event prompt | Do not repeat the old 104-to-108 repair |
| Default enablement removed | `common/scripted_triggers/chaosx_settings_triggers.txt`, `event_log_event_is_reworked_default_enabled`, no Event 23 member in current list | Implemented removal; Part 10 and catalog transition contract | Keep disabled until actual closure; do not remove it again |
| Unclustered catalog | `subagent_handoffs/023_spreadsheet_cluster_cleanup.md`, Events row 24, Clusters row 19, Membership row 72 | Implemented according to bounded worker/export evidence; Part 7 and catalog notes | Do not recreate Arms-race or repeat de-clustering; workbook wording/status needs final reconciliation |

## C1 — Outcome-first shared actions and actual delivery proof

Disposition: **queued**, with native execution/route verification **blocked** by incomplete evidence.
Required before closure: **yes**.
Acceptance: coding prompt, Parts 2–4 and 7, current explicit shared-action ownership and physical-delivery requirements.
Affected files: EV, EFX, RFX, RTR, ETR, CONST, LOC, `common/on_actions/chaosx_on_actions_chaos_meter.txt`, `common/scripted_effects/chaos_meter_effects.txt`, `common/on_actions/humanitarian_runtime_on_actions.txt`, and `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md`.
Shared files remain parent-owned; this plan does not authorize an independent shared-system rewrite.

### Current gap

EFX `sov_nuclear_bombs_resolve_test` calls `sov_nuclear_bombs_execute_shared_action` before `sov_nuclear_bombs_record_action_receipt`.
RFX `sov_nuclear_bombs_execute_shared_action` marks acceptance, invokes `launch_nuke` for every action except demolition, and commits the reservation.
The test success/failure/accident random list runs afterward in `sov_nuclear_bombs_record_action_receipt`.
The probability auditor independently established its exact 70/20/10 pool with no scenario inputs.
Public demonstrations take a different receipt branch that does not run that test-result pool.
The instrumented/concealed labels and evacuation support therefore do not currently establish the accepted distinct physical outcomes.

The shared Chaos callback treats the native callback as nuclear use, applies its normal nuclear-death/fallout/condemnation route, and selects thermonuclear consequence tuning from the launcher's technology.
Event 23 requests `nuke_type = nuclear_bomb`, so an actor's unrelated thermonuclear technology must not upgrade this atomic action's shared consequence profile.
The humanitarian callback also applies its nuclear-pressure path without an Event 23 test/evacuation profile in the inspected code.
These shared-source observations require parent review of all consumers, not a private Event 23 duplicate consequence call.

ETR `sov_nuclear_bombs_event_has_targeted_delivery_route` adds an extant state and owner/controller to generic strategic-bomber technology, deployed bomber count, and any controlled airbase.
RTR `sov_nuclear_bombs_action_delivery_route_is_valid` is likewise not proof of source-base-to-target reach, access, fuel, or current native mission conditions.
EFX `sov_nuclear_bombs_stage_action_context` writes route/authorization proof values itself; a proof flag is not a substitute for the route it names.

### Bounded repair contract

1. Keep one existing action transaction with actor, source depot, exact target state, target actor, weapon type, action/profile, reservation amount, and nonce.
2. Before physical dispatch, determine the test outcome from the prepared profile and current readiness, integrity, site, war, and completed support inputs.
3. Classify the outcome explicitly as no-yield failure, successful test/demonstration, yield accident, or combat strike.
4. A no-yield failure must never call the native nuclear detonation route or its shared blast consequences.
5. Return an intact failed-test reservation to its original custody, or record the documented damaged/dismantled disposition exactly once if that is the selected accepted outcome.
6. Successful tests and demonstrations invoke the shared test profile once, retain actual humanitarian/environmental consequences, and do not fabricate a combat-use or multi-major-exchange receipt.
7. Yield accidents invoke the shared accident profile once; non-yield demolition remains non-nuclear.
8. Feed completed evacuation/instrumentation and the requested atomic weapon type into the shared consequence owner, without a second event-owned deaths, contamination, condemnation, or Chaos adjustment.
9. Distinguish request acceptance, dispatch, and observed completion.
10. The installed `launch_nuke` effect documents no success return; resolve the observation/commit contract against documented `on_nuke_drop` behavior and current native consumers before claiming physical success.
11. If matching callbacks cannot safely establish a receipt, record that exact engine blocker; do not silently treat invocation as observed success or invent a fallback delivery route.
12. Revalidate the same target-specific native capability at selection, preparation, certification, and release.
13. No platform grant, missile shortcut, target substitution, or arbitrary airbase proxy may satisfy the accepted delivery requirement.

Use existing IDs `sov_nuclear_bombs_stage_action_context`, `sov_nuclear_bombs_execute_shared_action`, `sov_nuclear_bombs_commit_reserved_device`, `sov_nuclear_bombs_release_reserved_device`, and `sov_nuclear_bombs_record_action_receipt` as the parent integration boundary.
Any additional receipt fields should extend that transaction, not create another independent launch system.
Cost ownership stays with the existing matching command/security/logistics/diplomatic/strategic payment helpers; rejected dispatch never charges a second time.

Acceptance cases: prepared secure proof; weak-command concealed test; public demonstration; completed versus incomplete evacuation; non-yield failure; yield accident; non-yield demolition; atomic action by a thermonuclear-capable actor; duplicate nonce; invalidated target; one aircraft at an unreachable base; fuel/access loss during preparation.
For each, reconcile native stockpile, actor/site/global buckets, callback count, combat/test counters, shared consequences, and final receipt.
The exact named probability cases remain `P23_TEST_PROOF_SECURE`, `P23_TEST_CONCEALED_WEAK_COMMAND`, `P23_TEST_PUBLIC_PREPARED`, and `P23_TEST_INVALID_SITE`.

## C2 — Real bargaining, reciprocal restraint, and observed exchange

Disposition: **queued**.
Required before closure: **yes**.
Acceptance: decision/mission and super-event prompts, Parts 4–7 and 10, current explicit nonterminal multi-major exchange requirement.
Affected files: EV `.120`, `.150`, `.161`, `.162`; EFX coercion/hotline/exchange helpers; ETR response, target, first-use, and exchange predicates; DEC response/stand-down decisions and missions; OA; CONST; ATR; AFX; LOC.

### Current gap

`DEC:sov_nuclear_bombs_ultimatum_response_mission` runs on SOV but calls `ETR:sov_nuclear_bombs_event_target_response_is_valid` without entering the target scope.
That predicate requires `NOT = { tag = SOV }`, so its negation is a source-level cancellation path in the SOV mission.
The target's `.120` event is separately scheduled and does not repair that mission contract.

`EFX:sov_nuclear_bombs_resolve_coercion_response` and `sov_nuclear_bombs_accept_partial_settlement` mainly write compliance/settlement flags and credibility/integrity values.
`sov_nuclear_bombs_target_demand` is a magnitude between 1 and 5, not one of the six specified concrete demand families with enforceable terms.
The `.162` verifier checks a surviving independent target and pending/failure flags, not fulfillment of the named political, territorial, or custody transaction.
Delay does not establish the accepted bounded negotiated extension.

`sov_nuclear_bombs_reciprocal_restraint` writes an accepted response and verification request without recording or consulting an opposing actor.
`sov_nuclear_bombs_resolve_hotline` supplies Soviet stand-down state, while `.161` can verify Soviet flags without a bilateral acknowledgement.
The posture/idea is not the `sov_nuclear_bombs_atomic_moratorium` country flag used by the first-use gate.
A verified stand-down therefore needs an explicit release exclusion, not an inference from presentation state.

`sov_nuclear_bombs_open_major_exchange` accepts the current major-exchange world gate and assigns `global.sov_nuclear_bombs_exchange_major_count` the constant 2.
That gate can be reached by a single confirmed major strike plus another nuclear major's existence.
Neither an observed answering detonation nor two distinct launch receipts is required by that helper.
The super-event's text says an attack has been answered, so this is an actual accepted trigger/meaning gap, not missing art or audio.

### Bounded repair contract

Keep one active target dossier per initiating actor, with immutable demand kind, exact affected states/device group, counterparty, response deadline, proposed partial terms, and transaction nonce.
Store the response on the actual counterparty and evaluate SOV mission validity in that stored scope.
Revalidate independence, faction exclusions, current issue, and delivery backing before sending and applying terms.
Preserve the existing four-cost ceiling; changing or narrowing terms does not repay the initial ultimatum cost or restart its deadline indefinitely.

| Existing accepted demand family | Concrete transaction and verification target | Partial settlement |
| --- | --- | --- |
| Cease hostilities | The named ongoing SOV-target war ends through the supported current peace/armistice route; verify the named belligerents, not a generic flag | A bounded verified pause instead of full war settlement |
| Withdraw from Soviet territory | Named currently occupied Soviet core/site states change the specified control condition; do not add claims or annex unrelated states | A named subset changes control while the remaining dispute is retained |
| Return devices/personnel | The exact held cohort is transferred through C3, with staff/access terms recorded separately; no country annexation is needed | Joint custody or return of the agreed subset |
| Accept protection | A supported named guarantee/nonaggression/access settlement is created; any stronger subject/reintegration variant needs the stronger accepted leverage gate and explicit terms | Guarantee or access without subject status |
| Demilitarize a strategic zone | The exact named zone loses the specified threatening military condition through a supported state/peace effect; verification examines that condition | A smaller named zone or narrower military restriction |
| Surrender in a collapsing war | Only an already collapsing target under conventional defeat uses the existing peace-objective route | Ceasefire or limited withdrawal; never healthy-country free annexation |

This table restores the six accepted families, not six new parallel mechanics.
If a specified native settlement operation cannot be supported, leave that family blocked and obtain an explicit disposition; do not turn it into an opinion modifier or omit it silently.
A partial acceptance must apply actual partial terms before issuing its receipt.
Refusal and exposure preserve the live issue without awarding settlement success.
Requested extra time changes one recorded deadline within the accepted 14–45-day response envelope; repeated delay cannot create a free reset loop.

For hotline/stand-down, reuse the dossier model with an opposing operational nuclear major and actual target-side accept/refuse response.
The parent may add one ordinary response event within EV if `.120` cannot cleanly distinguish negotiation contexts; no custom GUI is needed.
Both actors must reference the same agreement nonce and pause window.
Acceptance freezes new Event 23 authorizations on both sides while preserving already released actions and all existing damage.
Refusal, disappearance, terminal transition, renewed relevant combat use, or breach invalidates verification and retains a reason.
`.161` verifies continued bilateral adherence; it must not manufacture acceptance.
`ETR:sov_nuclear_bombs_event_severe_first_use_gate` and all release routes must explicitly reject a valid stand-down.

Record distinct observed combat detonation receipts with actor, victim, exact state, weapon/action classification, and order.
A first hostile major detonation can open a retaliation crisis, but only an observed answering cross-major combat detonation can trigger the one-shot exchange presentation.
Tests, demonstrations, accidental yield, repeated delivery callbacks, and one unanswered major strike do not satisfy it.
Derive the participant count from distinct receipts instead of assigning 2.
Retain slot/audio 108 and existing art; do not add another super-event or terminal branch.

Acceptance cases: SOV mission plus human target; target annexed before reply; partial device return with independent state preserved; invalid/satisfied dispute; one bounded delay; guaranteed stable minor versus isolated losing minor; rejected hotline; actual bilateral acceptance; breach before verification; one unanswered major strike; two distinct opposing combat strikes; duplicate callback; Fallout transition.
`Ultimatum Without Ash`, `Firebreak`, and `The Last Telephone` consume these real records and must remain impossible from empty receipts alone.

## C3 — Physical custody must reconcile with native usability

Disposition: **queued**.
Required before closure: **yes**.
Acceptance: current conserved-ledger and four-stage lock; Parts 2, 6, 7, and 10; achievement prompt.
Affected files: RFX transfer/restore/disposition/reservation helpers; RTR; EFX breakaway and recovery completion; ETR one-device and local-capability predicates; DEC local stages/return/dismantlement; OA; ATR/AFX; LOC; `common/scripted_effects/005_soviet_collapse_effects.txt` only if the reviewed boundary needs an owner-applied correction.

### Current gap

`sov_nuclear_bombs_mark_site_transferred` moves ledger buckets but does not remove those event-owned devices from Soviet native usability.
`sov_nuclear_bombs_operationalize_breakaway_site` changes actor/site/global operational counters but does not make that exact transferred quantity available through the breakaway's native stockpile.
Several transactions use scoped temporary names such as `PREV.sov_nuclear_bombs_operationalized_amount`, although temporary variables are unscoped.
The global arithmetic reconciliation alone therefore does not prove actor/site or native conservation.

The demolition receipt commits one reservation and then calls `sov_nuclear_bombs_mark_site_dismantled`, which moves every remaining intact site bucket to dismantled.
A one-device dismantlement action must not remove an entire site's ledger while leaving the other native devices available.
Several source/transfer/return/dismantlement predicates require strictly more than one device and strand an exact-one cohort.

Breakaway technical completion clears the shared selected-state pointer, but command formation requires a selected site and the initial secure-custody selector is one-shot.
SOV and different breakaways also share global selected-state/cleanup targets.
`sov_nuclear_bombs_cleanup_annexed_actor` can clear shared pointers belonging to another actor's project.
The category correctly exposes local custody, but source existence is not proof of a reachable, independent four-stage campaign.

OA observes ordinary state-control change for Event 5 pending snapshots and reactor construction, not every already registered custody site.
Soviet native launches outside the Event 23 action helper do not update its combat-use counter in this hook.
Consequently custody capture, external native consumption, and achievement accounting need one reconciled integration contract.

### Bounded repair contract

- Keep the existing ledger; do not introduce another stockpile meter or register the same device twice.
- Reconcile global totals, every holder's totals, every registered site/cohort, reservations, and the event-owned portion of native usable stockpile.
- Preserve pre-existing and unrelated native bombs; use exact additive/subtractive deltas rather than overwriting `num_of_nukes`.
- When custody leaves operational Soviet control, move that event-owned usable quantity into non-operational escrow and record where it went.
- Technical access and command formation do not restore native usability.
- Delivery integration may convert only the already held, fully authorized cohort to the new actor's usable allocation; it is not a new grant and inherits no Soviet evolutions.
- A return changes devices/access, not sovereignty, unless a separately accepted settlement explicitly changes sovereignty.
- A one-device dismantlement removes exactly one native/event-owned device and updates only that cohort's quantity.
- Whole-site demolition is a distinct selected quantity transaction, with its own exact reservation/disposition and no automatic nuclear yield.
- Handle quantities 0, 1, and N explicitly; duplicate callbacks and repeated clicks are idempotent.
- Replace scoped temporary references with valid temporary values or explicitly scoped durable transaction fields as appropriate.
- Store selected site, counterparty, stage, and transaction nonce on the owning actor; retain/reconstruct the same site between local stages and never substitute another actor's selection.
- Cleanup clears only the owning transaction; annexing one actor cannot cancel an unrelated Soviet reactor or another breakaway's project.
- Use bounded exact state/actor hooks for ordinary capture, release, recovery, annexation, and native consumption; no world scan is needed.
- A native launch without an Event 23 pending nonce still contributes to the correct actor's combat-use/achievement history and reduces the correct allocation under an explicit shared attribution policy.

The attribution policy for an actor holding both Event 23 and unrelated native bombs needs a parent-recorded choice before implementation; neither silently charging unrelated bombs nor allowing Event 23 bombs to escape accounting is acceptable.
The recommended policy is to preserve the unrelated opening balance separately and require shared launch accounting to identify/allocate the consumed event-owned share deterministically.
If the native route cannot expose sufficient information, record that limitation as blocked rather than claiming conservation from a matching global sum.

Acceptance cases: existing native stockpile plus baseline; baseline site split; later evolution and assembly batches assigned to actual custody; capture with quantity 1; simultaneous SOV/two-breakaway projects; local 180/240/180-day stages; SOV disappearance; technical denial; exact device return without annexation; one-device dismantlement at a multi-device depot; whole-site demolition; duplicate release callback; native non-Event-23 launch; complete remaining-arsenal reconciliation.
`Scattered Arsenal` must also require the accepted negotiated/monitored resolution evidence, not merely the generic `sov_nuclear_bombs_custody_resolution_recorded` flag set by finalization.

## C4 — Reachable phases and meaningful existing support actions

Disposition: **queued**; map-dependent safety/route conclusions remain **blocked** pending evidence.
Required before closure: **yes**.
Acceptance: Parts 2–4, 6, and 8; decision map and decision/mission prompt.
Affected files: EV `.100`; EFX doctrine, preparation, support, production, and recovery helpers; ETR phase/site predicates; DEC; CAT; CONST; LOC.

The current `.100` board only acknowledges a report.
The test survey and preparation choices require phase `test`, while ordinary test preparation itself writes that phase; the inspected global producer search found no independent normal phase-navigation entry into testing.
Evolution I opens production and Evolution II opens coercion, but phase presentation must not make already accepted baseline testing or earlier operational tasks inaccessible.
Likewise, test completion resets to custody while investigation visibility requires testing.

Use the existing operational-command entry to select an eligible working phase without granting an unlock, consuming a bomb, or bypassing an active mission.
Separate navigation state from progression authorization.
Custody and eligible test preparation remain reachable at baseline; production requires actual capacity, not merely a later phase label; coercion retains Evolution II gates; major planning and first use retain their separate world gates.
Mission completion returns to a usable phase, and failure exposes investigation without requiring another test.
AI must enter the same eligible action family through its own selection route, not a human-only board click.
Keep the decision budget by showing the selected task family, not all 67 definitions at once.

Opening doctrine selection currently overwrites posture with demonstrative deterrence even without a public demonstration.
`sov_nuclear_bombs_send_private_signal` can also lower public knowledge to private after stronger evidence exists.
Keep doctrine, posture, and public knowledge separate; public knowledge advances monotonically, and an opening custody choice does not certify a demonstration or overwrite the stronger eligible opening posture.
The four doctrine options are implemented, but the accepted later costly timed reform route is not established by those one-shot initial-choice definitions.
Complete one reform route tied to a recorded command incident, evolution, or major war-state change; reuse the four doctrine identities, impose a long existing-scale preparation/disruption cost, and prohibit repeated free switching or replaying the opening grant.
The unused initial dispersed decision references `constant:sov_nuclear_bombs_doctrine.dispersed`, while the defined identity is `dispersed_commands`; reconcile that legacy path when deciding whether it remains needed.

Support actions need their promised consumers: `sov_nuclear_bombs_site_hardened` currently blocks repeat hardening but does not establish reduced capture/sabotage risk; `sov_nuclear_bombs_complete_rail_security` can mark the corridor secured from a valid depot without checking a named corridor; a recovery-raid success flag can be issued without recovering an enemy-held cohort.
Connect these existing actions to exact site security, named controlled transport route, and recovered/disposed cohort outcomes.
A rail-security mission should complete from its held/supplied route objective, not solely because its timeout expired.
If the route or objective is lost, pause/cancel or resolve the accepted loss branch and preserve device accounting.
Do not add a rail network management minigame.

Population/transfer/denial checks have been added to test/reactor sites, but border-conflict checks are not proof that ordinary land combat, hostile exposure, contamination, and transport constraints are covered.
Initial randomly registered sites and later chosen sites must meet the same accepted safety/role contract; capital command identity does not make the capital a valid test or reactor site.
No fixed historical state grant or map rewrite is proposed.

Acceptance cases: each doctrine at baseline with evolutions disabled; enter and leave test preparation; failed-test investigation; production before/after loss of actual capacity; stronger pre-fire opening plus doctrine choice; private signal after demonstration/use; two distinct safe storage sites; route cut during transfer; failed raid that recovers nothing; invalid site after selection; at most six primary actions and three missions per actual phase.

## C5 — Resolve the existing reactor and timing contracts, not another reactor plan

Disposition: **queued**, with native queue identity/cancellation and timing evidence **blocked**.
Required before closure: **yes**.
Acceptance: Part 5, decision map, probability scenarios, and current exact reactor package lock.
Affected files: EV `.180/.181`; EFX opening, progression, reactor queue/verification/control-change helpers; ETR reactor/world gates; CONST; MTTH; `subagent_handoffs/023_reactor_architect.md`.

The reactor architect handoff is a prior design proposal and has not acquired approval merely because current source resembles it.
Do not duplicate that architecture here.
Parent must record which claims are implemented, accepted and queued, rejected, or superseded, with acceptance and current evidence.

Current `.181` and completion counting are present, but `sov_nuclear_bombs_try_evolution_progression` queues reactors without scheduling the reactor completion check that opening and ordinary expansion schedule.
A baseline opening with zero reactors can therefore reach an evolution queue without that queue's dedicated observation chain being established by the inspected caller.
`verify_pending_reactor_construction` also invokes the state-oriented pending-site predicate from its country-level branch.
Review exact scope, one verifier per pending queue, control-loss cleanup, requeue reachability, and no double-credit for the same native building.
Construction queue removal cannot be assumed from clearing Event 23 flags.
Current `reactor_count` is historical completion credit and must not substitute for present controlled production capacity after reactor loss.

Reconcile free pre-fire/active evolution entitlements with Part 5's immediate stronger opening and add-or-queue language.
Do not silently convert every free valid-site reactor grant into an unrelated paid construction reward, nor call an uncompleted queue a completed free reactor.
If native job identity/cancellation prevents the accepted behavior, leave the affected entitlement unresolved with an exact blocker and keep its balance conserved.

The MTTH file computes intervals 180/240/300/360 and schedules `.180`; this is not automatically an engine event-MTTH distribution.
Accepted `P23_EVO1_HIDDEN_NORMAL` expects a roughly 120-day center, and Part 5 also recommends different stage pacing.
The parent chooses final balance targets and records the acceptance basis; the auditor does not choose them.
Compare the actual scheduled sequence, including other callers of `try_evolution_progression`, rather than assuming the interval file alone owns all advancement timing.

Reconcile `P23_EVO3_MAJOR_RIVAL_NORMAL` and the prepared-enemy world-gate alternative with current gates that require an opened flag, exchange, or confirmed enemy use.
Do not remove accepted stable-rival/prepared-threat alternatives without a recorded decision.
For `P23_EVO1_MORATORIUM_DELAYED`, the accepted expectation permits strong delay or safe skipping; lack of a hard moratorium exclusion alone is not proof that this expectation is violated.
The actual refusal/delay behavior, queued grants, phase transitions, and existing scheduled pulses still need to be demonstrated.

Acceptance cases: baseline then Evolution I; strongest pre-fire package; no valid reactor site; site becomes valid; construction still pending; target control changes; recapture; lost completed reactor; disabled stage toggles; duplicate pulse; stable nuclear rival; verified enemy preparation; moratorium before and during a scheduled interval.

## C6 — Final documentation, asset acceptance, catalog, and audit closure

Disposition: **queued**, with visual/current-scenario acceptance **blocked** where noted below.
Required before closure: **yes**, except explicitly rejected scope and package-only gaps.
Acceptance: asset, achievement, super-event, and coding prompts; Parts 8–10; repository completion rules.

| Task | Exact files/identifiers | Current status and required action |
| --- | --- | --- |
| Event documentation | `docs/events/023_sov_nuclear_bombs.md` | Missing at final checked snapshot; parent writes current implementation truth, integration boundaries, assets, and remaining accepted work after repairs |
| Runtime contract documentation | `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.md` | Present but describes future stages/profiles that now have source implementations and treats invocation as the commit point; reconcile against C1–C3 without promoting unsupported success claims |
| Semantic localisation | LOC `.101/.102/.120/.161/.162`, category and breakaway mission descriptions; Event Details/evolution keys | Re-audit after behavioral repair; `.161` is a stand-down verifier but has moratorium text, `.162` is a settlement verifier but has incomplete-stand-down text; the breakaway mission description denies a direct launch route while final delivery must produce actual independent operational capability |
| Achievement truth | ACH seven `023_sov_nuclear_bombs_*` IDs; ATR criteria; AFX receipts | Registration is present; derive completion from physical/settlement/exchange evidence and test negative cases, including native launches outside the event wrapper and no negotiated custody outcome |
| Existing visual acceptance | GFX; `docs/assets/023_sov_nuclear_bombs/manifest.md`, `gfx_handoff.md`; latest asset handoffs | Source wiring and worker technical reviews exist; retain pending review where no parent acceptance is recorded; resolve stale wiring notes without interpreting `needs_user_review` as a discovered image defect; no new asset family requested |
| Catalog wording/status | `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, `Events!24`; worker/cluster handoffs | De-clustering is reported implemented; the worker's recorded detail/evolution prose is not verbatim current LOC, and `Playable` was outside its preserved validation list; spreadsheet owner must read the authoritative row, align exact final text and valid status, then run the exporter; do not edit CSVs directly |
| Default availability | `common/scripted_triggers/chaosx_settings_triggers.txt`, `event_log_event_is_reworked_default_enabled` | Currently excludes Event 23; restore only in a genuine closing change supported by completed acceptance evidence |
| Bounded CXT contract | `common/scripted_effects/023_sov_nuclear_bombs_cxt_test_effects.txt`, `common/on_actions/023_sov_nuclear_bombs_cxt_on_actions.txt`, `sov_nuclear_bombs_cxt_extension_event023_apply` | Source registration exists and does not grant the opening; parent documents bounded ledger/action fixtures and retains debug/achievement disqualification |
| Current audits | Latest country, decision, localisation, asset, probability, and completion handoffs under `subagent_handoffs/` | Re-audit changed transaction/mission/achievement surfaces after parent repair; obsolete snapshots cannot certify new code |

The shared Event Details/settings/super-event framework remains parent-owned.
There is no Event 23 dedicated scripted GUI to delegate to an event UI worker.
A failed ordinary-decision render is an evidence blocker, not permission to replace the accepted presentation with a custom window.

## Prior-handoff disposition reconciliation

All paths in this section are relative to `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/`.

| Handoff | Disposition of relevant claims in this review |
| --- | --- |
| `023_event_completion_auditor_current.md` | Several listed repairs are implemented, as credited above; its overall incomplete result remains warranted for current C1–C6 reasons, not by blindly repeating its stale list |
| `023_country_package_auditor_current.md` | Pre-release calls and staged checks implemented in source; broad ledger/native/independent operational completion remains unresolved; do not require a full delivery platform at the technical-access stage because the current user explicitly separates those stages |
| `023_decision_mission_auditor_final_current.md` | Bounded mission/cancellation repairs implemented; complete reachability, scope, route objectives, and settlement outcomes remain queued; its failed render is not visual acceptance |
| `023_localisation_auditor_final_current.md` | Named collision/routing repairs implemented; later behavioral wording and achievement semantics remain queued |
| `023_event_art_asset_audit_repair.md`, `023_icon_asset_audit_repair.md`, `023_breakaway_report_asset.md`, `023_device_disablement_icon.md` | Worker production/technical-review tranches implemented; current GFX wiring credited; parent visual acceptance and truthful manifest dispositions still required |
| `023_spreadsheet_worker.md`, `023_spreadsheet_cluster_cleanup.md` | First is superseded by the cluster cleanup for final membership; de-clustering implemented according to worker evidence; text/status closure remains queued |
| `023_reactor_architect.md` | Blocked pending parent acceptance/queue-semantics resolution; reconcile the prior proposal rather than adding a second architecture |
| `023_ai_probability_baseline.md`, `023_ai_probability_postpatch.md` | Historical partial evidence; postpatch revisions do not match current source; not a final balance/compare pass |

No previous top-level improvement-loop addendum was present when this pass began.
This document is the single consolidation of the newly identified accepted-contract connection gaps.
Do not run another Event 23 improvement pass until this addendum and the existing reactor proposal receive explicit dispositions.
No already accepted requirement is rejected or downgraded by this planner.

## MCP evidence and exact limitations

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
All MCP use was read-only; no rewrite route was used.
The following evidence is static inspection/render/probability evidence, never live-game execution.

### Event chain

The initial narrow root `.1` trace and neighborhood render returned `EVENT_*_PARTIAL`, revision `4aa5df917da5f3cd3d8f18be8af5c314412c5c9d3c91955a5a9f603ef898aaf8`.
The render selected six nodes; helper expansion was deferred, so it does not validate the ledger or outcome ordering.
Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59900b606d5cf126c3231ab64f94c2ba77a04affbf8f6c2bb8dfdabb6ea2b3d3/21f1670e61a3541f9bca0ccc4582945c140c17c553066e61d2d7681bf95d3a6f/event-trace-4aa5df917da5.json`.
Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a26bcf3eb41d247904bed46ebdcc362b8cd424c05c4b438de0ebd4375e55291/d97bbacd558e1cb9af88027f090ff0c479abd55f688e075be2cd0f91c2dfa180/event-neighborhood-4aa5df917da5-manifest.json`.
The returned PNG was not visually inspected; no graphical pass is claimed.

A full state-flow request built workspace revision `6c86dde0012bbfdcadea518ba027a52201ec97d544945279cee2cd67c097398e`, but its requested variable name was not a current Event 23 variable.
Its empty selected flow is not evidence about the actual ledger, and its workspace-wide diagnostics are not Event 23 defect counts.
The subsequent impact query for helper `sov_nuclear_bombs_execute_shared_action` and `event_compare` from that full revision each failed with `timed out awaiting tools/call after 180s`.
Final file-scoped trace and options render, selector `{kind: file, sourcePath: events/023_soviet_nukes.txt}`, also each failed with that exact timeout.
Thus affected C1–C5 event-chain execution/compare conclusions remain unresolved; source review is not substituted for them.

### Map, technology, standalone viewer, and GUI

`map_inspect` query `Moscow` with overview returned `MAP_INSPECTED`, revision `a5c63a8a007d736c8ff2fb269b44e1e16c311021a234b5a6fc7c753df3781b46`.
It indexed 1,081 states and connected map/network data; it did not prove a runtime-selected Event 23 site's safety or aircraft reach.
The map report is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3fcc5d43360f8d96ccb43d22eb692ed9cc8c1d0c2216b227f2793e97400f66ec/6bb2d063ff61088e6243294150aef55cc8dcca9bffd8fdf240835f608ff34177/map-inspect.a5c63a8a007d736c.json`.
`map_render`, state layer, railway/supply-node/state-building overlays, scale 0.25, timed out after 180 seconds.
Dynamic safe-site, corridor, and delivery-map acceptance remains blocked.

`tech_inspect` explain `nukes`, maximum 20 nodes, and `tech_render` technology `nukes`, maximum 20 nodes, both timed out after 180 seconds.
The installed vanilla `electronic_mechanical_engineering.txt` directly defines `atomic_research`, `nuclear_reactor`, and `nukes`; their source presence does not prove every installed DLC/native delivery combination.
No missing custom technology tree is inferred.

Standalone Technology Tree Viewer availability was checked separately from tool exposure and service results.
The installed shim resolves to `C:\Users\klimp\AppData\Local\hoi4-agent-tools\3.0.7\node_modules\hoi4-agent-tools`.
Its package/bin inventory exposes stdio, HTTP, and setup entrypoints; inspected client examples are MCP configuration examples, and the dist search did not identify standalone viewer/client HTML assets or a viewer launch entrypoint.
`docs/technology.md` names the technology analyzer/render tools a viewer but provides tool workflows, not a separate application entrypoint.
Disposition: **blocked package gap — no standalone viewer entrypoint identified in the installed 3.0.7 package**.
This is not evidence that the exposed technology routes do not exist, and not a new Event 23 gameplay requirement.

GUI inspection and rendering targeted the existing vanilla `countrydecisionview`, with explicit `evt23-planner-custody-source-view`, generated scenarios disabled, readiness 43, integrity 87, 100 devices, custody labels, and no selected site/target/deadline.
Rendering requested normal state at 1920×1080 and 1280×720, UI scale 1.
Both `gui_inspect` and `gui_render` timed out after 180 seconds.
This fixture describes intended values, not proof of an engine-populated decision list or actual opening posture.
The ordinary-decision visual conclusion remains blocked; no visible defect is dismissed as renderer discrepancy and no visual completion is claimed.
Resource listing also failed with `timed out awaiting resources/list after 180s`, preventing further artifact retrieval through that route.

### Probability specialist handoff

Read-only specialist: `chaosx_ai_probability_auditor`, agent `01a06ee4-fee6-7bd2-a821-867a372184de`.
It wrote no files and began with `hoi4.probability_inspect`.
The planner's initial probability revision `21d94843...` is stale and is not closure evidence.

| Surface | Current evidence and limitation |
| --- | --- |
| Opening `.2` | Four candidates discovered; revision `857888d38b9b0c8b55be36bc64fc7f1214d7b8ea2d790fa61baa7ae6cd86240d`; eight evaluation rows, two unresolved `has_government` bindings; no normalized pool probability accepted |
| Response `.120` | Complete bounded six-option pool; fixed source bases 35/25/20/20/10/10; revision `25f56e7fa304786055d8e8ae0130550d396b8499aa655404ad88838441747e01`; scenario scope/target bindings unresolved, so all-ineligible output and apparent fallback/dominance are not gameplay probabilities |
| Test random list | Revision `457cd850acbc9b0adb2706b7f2173ff19f225aa106b020565af55a1b4c2cdd42`; `P23_TEST_PROOF_SECURE` exact 70%/20%/10%, no required inputs; proves the flat pool, not overall action success |
| First-use evaluation | Revision `623572e2c3ec8240283ff7c94a81eecfe37059d564995b310cf1a55c4155e0a0`; three tier/stability/severity cases, 49 unresolved bindings; source hard gates exist, rarity and normalized authorization probability remain unproven |
| Timing | MTTH adapter discovered no surfaces in the Event 23 MTTH file; schedule/world-gate behavior requires source-linked sequence evidence, not guessed timing probabilities |
| Rendering/comparison | `probability_render` returned `PROBABILITY_ANALYSIS_NOT_CACHED`; no current same-snapshot `probability_compare` was completed; historical comparison cannot certify the dirty concurrent source |

Exact test-pool inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a8b6c0735b45f0692d8445d9c2a85ff27c7977bea969be2355e4aced2c60e59/f8b21c1472b66d3e5925dd944429fcffc1ed42f1625e56007c7a3314f022d868/probability-inspect-f61e7be135de.json`.
Exact test evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/695e8196273be2a770afa3a78216bdb100e5506fd961596758ec46d01bbdf99a/ed510bf61ac5086b9e2d77b42183de1a76810ede4fc23f30daba28c2e9d516f8/probability-60d2dd1c69aae24bb219f519.json`.
Unresolved response evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d14079d35bf991ed70978e2cea01c55aa30e3f676a52d5e8f59369f8dfcb1c11/0f320915150e9bdacbb5e78dd194bb142fb95447e9c05912b1c078b5f42bb782/probability-106bac5b574c9e28461e9abb.json`.
Unresolved first-use evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1e9e2d424587a39714460455570584743fbc41ab1ce737dbadfcc6695d0065c2/af35135e814e1ec542f7b3385bbfc3ca32b1971be6fba9a33e5063a9c28d2c3a/probability-7a7f1dfcb0027710ab146c11.json`.

Required owner sequence: preserve a current baseline, approve the intended behavior/targets, apply the bounded patch, then have the specialist compare the same named scenarios and complete candidate pools.
At minimum retain the test cases above; all four `P23_COERCE_*` cases; `P23_FIRST_USE_TIER_800_BLOCKED`, `P23_FIRST_USE_TIER_1000_STABLE_BLOCKED`, `P23_FIRST_USE_TIER_1000_SEVERE_RARE`, `P23_FIRST_USE_STANDDOWN_BLOCKED`; the named target/profile/retaliation cases; and the evolution/collapse cases named in C3/C5.
Do not change weights merely to eliminate unresolved fixture diagnostics.

## Research basis and scope exclusions

The existing accepted research package already provides sufficient historical depth; no new historical branch is needed.
The [CTBTO account of the International Day against Nuclear Tests](https://www.ctbto.org/news-and-events/international-day-against-nuclear-tests) supports the Semipalatinsk connection and the importance of distinguishing test preparation from humanitarian consequences.
The [U.S. Office of the Historian's Clinton–Yeltsin overview](https://history.state.gov/milestones/1993-2000/clinton-yeltsin) supports custody/security/dismantlement cooperation as historical inspiration for actual negotiated device outcomes.
These are design connections, not instructions to transplant later treaties or institutions literally into a 1936–1945 alternate-history campaign.
They do not justify changing the explicitly fictional +100-bomb premise.

Disposition **rejected** for this pass: another focus tree, formable, successor tag, portrait/flag set, nuclear unit/model, animated command room, additional permanent meter, extra exchange super-event, Event 23-owned Fallout, or automatic Arms-race cluster creation.
Acceptance basis: the current user exclusions and Parts 1, 7, 8, and 10.
Required before closure: no implementation of these additions; maintain the exclusions.

Event 32 is not assumed absent: `events/032_missile_crisis.txt` and `docs/events/032_missiles.md` exist, and the latter describes shared nuclear consequences and Event 23 stockpile ownership.
This pass did not audit the complete Event 32 payload implementation or propose changing it.
Any shared action change in C1/C3 needs a parent-owned compatibility review with `common/scripted_effects/032_missiles_operations_effects.txt`; its compatibility conclusion remains unresolved, not an invented new delivery entitlement for Event 23.
Event 76/47 expansions and shared scenario-catalog discrepancies remain outside this bounded addendum.

## Snapshot and uncertainty

Source hash capture: `2026-09-05T03:39:05+03:00`.
Concurrent parent work was present; recheck changed files before applying a recommendation.

| File alias | SHA-256 |
| --- | --- |
| EV | `EDE5FDF481B3C374DBE3200D03ED5278755902DB3B18CBEFD146E6F3E3675C32` |
| DEC | `DC55183F9E49B849C6A2431BF7646D745B5B12C68B643535F3C55563929CB42A` |
| EFX | `A4010965650E4EE1DB45103707670FFB2FD5478177BEB3DE2CE69319FBDB7387` |
| RFX | `3042EAA6C695520AF4AE9B7421D6ABC74800340DE8FB18665F8D26EB32884489` |
| ETR | `D893E91D1C1B43E1E08D47CE73BC58651FF552334924D52FB78D57B922BEF19C` |
| RTR | `4E301FE59FC752E8759EE4AC93C23D38EAC3B08B445BBBAFF3038867B40A235E` |
| OA | `95ABED4ECBBD88B5D7A55C45F986070EFFC24B87D496805F70A3A24940F58747` |
| ATR | `F033F138536A604CDDA38DC810E6E912F3B685AF007BE85BF1273AC40A1286AF` |
| LOC | `B9DBF79D673F482385AA20D99DF16C77A95536214B871122D8B9B20FB4E0F493` |
| GFX | `C5CD40E1DC6B633E1CA06CB65FEFA9210F198F87BE870CCB9774D4C793969D28` |

References consulted include the required offline wiki core pages and relevant event, decision, variable/event-target, interface, and scripted-GUI sections; installed vanilla script-concept/constants documentation, nuclear effect/callback documentation, nuclear technology definitions, and native decision/scripted-GUI precedents.
No Paradox web wiki was used.
The installed `launch_nuke` effect and documented callback are syntax/scope evidence, not proof of aircraft reach or successful gameplay execution.
No live game was launched, and this planner does not request logs or instruct the user to perform testing.

Skills used: `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-super-events`, `chaos-redux-subagents`, `chaos-redux-scripted-gui`, and `chaos-redux-mtth`.
The improvement-loop/event-planning guidance limited this output to completing existing meaningful choices instead of adding more content.
The MCP/GUI/MTTH guidance required explicit blocked evidence rather than source-only or score-only completion claims.
No skill was created or updated.

## Parent handoff and promotion

File written: `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_near_completion_contract_addendum.md`.
The planner's same-turn draft at `docs/plans/023_sov_nuclear_bombs_plans/023_near_completion_contract_addendum.md` was relocated here at the user's request; no duplicate plan layer remains.
Completed work: accepted-package/source/handoff review, read-only MCP attempts, current probability specialist review, stale-finding reconciliation, and this bounded repair design.
Not completed: gameplay repairs, final visual acceptance, workbook reconciliation, full route/sequence/compare evidence, or event completion.
No implementation simplification or fallback was introduced by this planner.
The incomplete behaviors and evidence limits in C1–C6 must not be described as completed or silently waived.

Implementation order: C1/C3 shared transaction boundary; C2 settlement/exchange receipts; C4 reachable task families and support consumers; existing C5 reactor/timing reconciliation; then C6 localisation/docs/catalog/assets and matched audits.
Parent must review the shared integration boundary before distributing bounded implementation work.
Outstanding decisions are the native mixed-stockpile attribution/observation contract, reactor proposal acceptance versus free entitlement semantics, and recorded timing/balance targets where current values differ from accepted scenario expectations.
These are not requests for a broader event.

Keep this file in `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/` until the parent records dispositions.
If accepted, promote only the new clarifications to the corresponding existing Parts 2–7, 9–10 and decision map under `docs/specs/023_sov_nuclear_bombs_specs/`, with parent acceptance basis and links back to this handoff.
Do not copy the whole audit into specs or treat a promoted location as approval.
Mark individual claims implemented only with current source/behavior evidence and their validation limits.
The parent can finish the final validations and mark the goal complete only after no required blockers or unresolved accepted plans remain.
No Git commit was created because the current parent instruction authorizes writes only to this plan/handoff path; the parent owns integration and any plan-specific commit.

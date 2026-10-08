# Event 012 Gods of Africa: bounded decision-phase repair

Date: 2026-10-07.
Owner: `chaosx_improvement_loop_planner`, plan only.
Disposition: `implemented` at source level for the host/participant integration, with the Council portion committed in `b0d53742ec12ba87b690898420c4bb1e58988c28`.
The parent adopts the bounded recommendation under the user's full-Gods action-budget requirement and recommended-choice authorization.
This plan-only author wrote only the addendum; current implementation and acceptance limits are owned by `012_gods_response_phases_implementation_2026-10-07.md`.

Parent integration refinements: reply rows prewarm their existing bounded arrays by existence and evaluate the exact old volatile target predicates in live visibility; discretionary actions recheck view in availability and execution; final commitment stays on overview, doctrine or pending-answer surfaces to preserve six primary priorities.
The new response-view enum is isolated in its own schema-first constants file.
No clock, paid offer, material amount or numeric willingness factor changes.
The 21-group source model and independent review cover action counts, 768 reply-predicate comparisons, stale clicks, AI bypass, old payment/weight/mission AST preservation and manual clock-handler orders.
Native scheduling, target-cache timing, row appearance and complete probability evaluation remain unproved; this disposition is not whole-feature completion.

## Acceptance and problem

The authority is the parent's October 7 bounded repair assignment, the full-Gods/no-simplification goal in `docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md`, and the scoped accepted decisions in `agent_decisions_2026-10-04.md` and `agent_decisions_2026-10-05.md`.
The full spec's Participant response model and Presentation require at most five ordinary participant responses.
The decisions skill applies the scripted-GUI skill's six-primary-action ceiling to ordinary decision surfaces; these are readability limits, not engine row limits or clipping findings.
L23 preserves reconciliation during wars elsewhere, L26 owns staged ultimata and their punishment rules, L27 owns both Council choices and expedition, and L13 owns frozen grading and continuing settlement delivery.
The October 6 decisions preserve cumulative support reporting, measured restitution and prepayment accounting.

The prior `012_africa_gods_full_grading_rewards_design_2026-10-03.md` is explicitly `implemented` and `promoted into an accepted spec`, corroborated by L13 and the October 7 documentation reconciliation.
It is not reopened.
The new gap is the concurrent action surface established in `012_gods_decision_surface_review_2026-10-07.md`: host doctrine plus priorities plus targets; Council plus ordinary demand; four preparations plus reconciliation plus ultimatum.
This repair should finish that gap rather than expand mechanics, focus routes, countries, actors, prices, meters, categories or GUI.

## Recommended host flow

Use the existing `gods_of_africa_host_category` and one private host variable, `gods_of_africa_response_view`.
Centralize its enum in `common\script_constants\012_africa_gods_constants.txt` as `gods_of_africa_response_view`: `overview = 0`, `priorities = 1`, `partners = 2`, `judgment = 3`.
Absent or invalid state means overview.
The variable is presentation state only: it never changes doctrine, selected priority, need, dispatch, punishment, history, costs or timers.

Resolve the human host's visible phase in this order:

| Phase | Exact visible action families | Maximum primary actions |
| --- | --- | --- |
| Pending answers | `gods_of_africa_accept_substitute`, `gods_of_africa_reject_substitute`, `gods_of_africa_accept_reconciliation`, each only for its existing valid targets; also the existing untargeted `gods_of_africa_commit_settlement` if already eligible | 4 |
| Doctrine unset, no pending answer | `gods_of_africa_choose_reciprocal_covenant`, `gods_of_africa_choose_sovereign_exaction`, `gods_of_africa_choose_strategic_ambiguity`; eligible settlement commit may remain | 4 |
| Overview after doctrine selection | Three free parent choices described below, plus eligible settlement commit | 4 including navigation |
| Continental priorities | Five existing core choices and one existing advanced lane, preserving every shortage/focus gate | 6 |
| Partner relations | `gods_of_africa_grant_leniency`, `gods_of_africa_public_pardon`, `gods_of_africa_protect_partner`, `gods_of_africa_send_expedition` | 4 |
| Proven offenses | `gods_of_africa_mark_offender`, `gods_of_africa_escalate_offense`, `gods_of_africa_arm_offender_enemies`, `gods_of_africa_coerce_occupier` | 4 |
| Committed settlement / owner recovery | Existing delivery/recovery/victor lifecycle, outside the ordinary view gates | Existing scoped actions |

The priorities phase retains `gods_of_africa_prioritize_land`, `_fuel`, `_manpower`, `_industry` and `_transport`.
Its sixth choice follows the existing replacement chain: `gods_of_africa_prioritize_emergency` before either capability, `gods_of_africa_prioritize_support` after arsenal support but before logistics support, or `gods_of_africa_prioritize_air_defense` after logistics support.
Do not collapse independent shortages, choose a priority automatically, or show all three advanced choices together.

Add only four free ordinary navigation decisions, each paired with a same-named guarded effect: `gods_of_africa_open_priorities` (“Choose the next tribute priority”), `gods_of_africa_open_partner_relations` (“Review cooperation with a partner”), `gods_of_africa_open_judgments` (“Address a proven offense”), and `gods_of_africa_return_to_overview` (“Return to continental affairs”).
Use `GFX_decision_012_africa_gods_set_priority`, `GFX_decision_012_africa_gods_protect_partner` and `GFX_decision_012_africa_gods_mark_offender`; reuse the priority icon for return.
Each new decision's title key is its ID and its description key is `<ID>_desc`, describing navigation without promising a gameplay effect.
Each parent appears only when at least one of its existing children has a valid visible context; an unaffordable but otherwise valid child remains readable with its existing blocked reason.
Each opens one semantic family in place, in the same native category.
The family selector asks a distinct operational question, and its children retain consequential alternatives; this is not a popup, tab, extra category or miscellaneous “more actions” warehouse.
One return row is ordinary navigation and does not consume a gameplay-action slot.
No navigation action pays, applies rewards, consumes cooldowns, sends a report or restarts work.
Selecting a priority returns to overview after the existing `gods_of_africa_set_priority` call; targeted actions may leave their family open for another valid target.

Proposed trigger `gods_of_africa_host_has_pending_answers` derives urgency from the existing target predicates over the bounded arrays.
Include a current substitute offer in `gods_of_africa_participants`, a current paid reconciliation offer satisfying the existing acceptance target predicate, and the existing `gods_of_africa_victor_renewal_is_current` branch in `gods_of_africa_candidate_registry`.
Do not require substitute affordability to enter this phase: an unaffordable offer still needs its visible accept-with-reason/reject choice.
An unpaid reconciliation review creates no host answer yet; participant payment remains available independently.
Do not replace the candidate registry with live membership, because the reject/accept-reconciliation decisions also serve the explicit victor exception.

Pending answers automatically replace every discretionary family, including doctrine, without changing the stored view.
All valid answer targets remain visible; do not select the first country, cap paid offers, rotate countries or defer an answer behind navigation.
When the last offer resolves, expires or loses legitimate authority, the previous discretionary family returns, or doctrine selection if still unset.
A reconciliation offer's deadline continues throughout this substitution.
Urgency must not disappear because a child is greyed or the previous view lacks a target; derive it from target identity, not payment success.
A submitted substitute uses the participant's existing demand deadline.
This finite pending-work phase must not hold optional affairs open after its target predicates cease to match.

Gate discretionary children in `visible` and recheck the view at selection before invoking their existing effect.
For targeted children, evaluate presentation state on host ROOT/THIS, keep participant checks on FROM, and retain the existing arrays, target-root gates and helper call scope.
Use live visibility to replace the phase promptly; do not depend solely on the documented daily `target_root_trigger` refresh.
Keep the existing campaign-valid target checks in both their normal target and click-time paths.

Human navigation is bypassed for an AI host: existing AI decisions retain their campaign eligibility and scores, and the new navigation rows are human-only with zero AI willingness.
The phase selector must not become an AI prerequisite.
Add `gods_of_africa_clear_response_view` to the existing host initialization/loss/final-settlement lifecycle; do not transfer the scalar as gameplay authority.
No participant flag or global selected-target pointer is needed.
The existing `gods_of_africa_deliver_settlement_support` is never view-gated: its committed-settlement predicate excludes ordinary active-host policy, so its frozen debt remains payable through the original row.
Keep original-host recovery decisions and their receipts outside these ordinary view gates.

## Participant flow and both clocks

Add proposed participant trigger `gods_of_africa_council_response_phase_is_open`.
It requires the original `gods_of_africa_council_is_open` plus no active demand, no negotiation flag, no reconciliation pending flag and no final ultimatum pending flag.
Use it for the visibility and selection preflight of `gods_of_africa_council_pledge` and `gods_of_africa_council_speech`.
Keep the underlying Council eligibility and voice receipt unchanged.
No deferred-Council flag or timer is created: the two choices reappear directly when the obligations end, until the existing settlement/outcome closes them.
The existing host-owner settlement commit remains authoritative; this repair grants no extra Council grace period and delays no final security.
Use proposed status key `gods_of_africa_council_deferred_status` in the existing category description: “The Council will hear us after our outstanding obligations are settled.”
This is status prose, not another public value.

Retain the ordinary five-response family exactly: comply, partial shipment OR continuing-support sign where applicable, negotiate/request time, refuse, and permanent defiance through the parent's confirmation path.
Signing continuing support removes its sign action and retains its owner-managed instalments and whole-balance payment.
Do not change frozen amounts, agreed terms, partial receipts, the running demand mission or extension synchronization.
In negotiation, expose the three valid named `gods_of_africa_substitute_demand_slot_1/2/3` choices and `gods_of_africa_return_to_demand`, at most four actions.
Hide the generic `gods_of_africa_substitute_demand` row: its current effect only calls the first valid named slot and adds no outcome.
Retain that helper and its zero AI score for compatibility; an empty offer pool leaves the return action, not a fabricated substitute.

When `gods_of_africa_final_ultimatum_pending` is set, hide the four optional preparation rows: `gods_of_africa_prepare_defensive_defiance`, `gods_of_africa_harden_stockpiles`, `gods_of_africa_secure_transport`, `gods_of_africa_prepare_countermeasures`.
Use the pending receipt, not only the pre-deadline `gods_of_africa_final_ultimatum_is_open`, so an expired-but-unresolved obligation cannot reveal preparations between expiry and resolution.
Apply the same exclusion to their affordability/action preflight triggers `gods_of_africa_can_prepare_defensive_defiance`, `gods_of_africa_can_harden_stockpiles`, `gods_of_africa_can_secure_transport` and `gods_of_africa_can_prepare_countermeasures`; original prices, once-only receipts and AI factors remain.
Previously bought preparations keep their full effects.
Unbought preparations return after legitimate ultimatum resolution if the participant remains defiant; successful reconciliation legitimately closes the defiant route.

Keep `gods_of_africa_seek_reconciliation` visible under its original pending-review/victor conditions throughout an ultimatum.
Before payment it keeps its original peace, territory, deadline and price gates.
After payment its existing paid-offer guard prevents another debit; show its existing blocked/status reason and retain host acceptance.
Keep all `gods_of_africa_ultimatum_return_land`, `_pay_settlement` and `_refuse` answers visible under their existing conditions.
A defiant participant therefore sees two or three ultimatum answers plus reconciliation, at most four primary actions.
Outside an ultimatum it has its four preparations plus reconciliation, at most five.
During a pending ultimatum also defer the untimed `gods_of_africa_permanent_defiance` entry using its `visible` gate and `gods_of_africa_participant_can_defy` preflight; restore it after resolution under its original eligibility.
This prevents the parent's irreversible confirmation from competing with the urgent answers; do not alter confirmation internals.
For a non-defiant ultimatum target, voluntary aid is already excluded by pending reconciliation, so at most three ultimatum answers plus either aid or reconciliation remain.

**Do not defer or pause either 60-day mission.**
The participant owns `gods_of_africa_reconciliation_mission`, started by `gods_of_africa_start_reconciliation` with `gods_of_africa_reconciliation_start_day`, `_due_day`, epoch binding and `gods_of_africa_timing.defiance_review_days`.
The participant independently owns `gods_of_africa_final_ultimatum_mission`, started by `gods_of_africa_issue_final_ultimatum` with `gods_of_africa_final_ultimatum_due_day` and `gods_of_africa_ultimatum.deadline_days`.
Both clocks keep their original remaining days, cancellation conditions and original timeout callbacks.
Never add a view gate to mission activation/cancellation or remove/reactivate a running mission to refresh presentation.

Proposed precedence: `gods_of_africa_complete_reconciliation` resolves only reconciliation; it must not clear, restart or answer a live ultimatum.
The probability auditor identified the current cross-clock semantics as implicit, so this independent-obligation rule requires explicit parent adoption.
L23/L26/L27 do not explicitly say a ten-PP reconciliation also fulfils the separate 150-PP/3000-rifle ultimatum; automatically clearing that threat would weaken its accepted answer price and failure route.
Reconciliation removes its original hostility/defiance causes, while ultimatum expiry re-evaluates the resulting current Wrath, conduct, Strength and extreme gates rather than guaranteeing a catastrophe from stale state.
`gods_of_africa_resolve_final_ultimatum` resolves only the ultimatum; it must not clear `gods_of_africa_reparations_paid`, `gods_of_africa_reconciliation_offer_pending`, offer sequence, review epoch or the reconciliation deadline.
Refusal/expiry still calls `gods_of_africa_expire_final_ultimatum` and current punishment evaluation; reconciliation failure still calls `gods_of_africa_fail_reconciliation`, records its failure and preserves its retry rule.
View changes never invoke `gods_of_africa_clear_reconciliation_review` or discard a paid offer.
At a legitimate reconciliation timeout, its live paid/offer flags close through the existing failure path, but the actual PP transfer, offer sequence and paid-offer history remain recorded as a paid review that failed, rather than being relabeled unpaid.
The host must be able to accept until that original deadline; opening an ultimatum cannot forfeit the paid offer early.
Settlement and authority-loss cleanup likewise retain durable paid-offer/history records; no refund, pardon, duplicate debit or invented reconciliation acceptance results from changing phase.

Keep both countdowns and their required responses readable.
The ultimatum notice remains `chaosx.nr12.618`; existing reconciliation failure and punishment reports remain on their original owners.
Do not send reports on entering/exiting a view, opening navigation, or temporarily hiding Council/preparations.
Use proposed status key `gods_of_africa_parallel_reviews_status` once in the existing mission/category text when both reviews run: “The reconciliation review and the final ultimatum have separate deadlines.”
No new deadline, report event, notification loop or punishment suppression is introduced.

## Source scenarios and acceptance contract

Count greyed visible actions and count each targeted family once, as in the audit.
Target multiplicity and native row geometry remain separate acceptance questions.

| Named case | Required result |
| --- | --- |
| `012_GODS_HOST_DOCTRINE_ALL_NEEDS` | Doctrine zero, five core shortages and each advanced-focus variant: three doctrine choices; no discretionary priority/target children until doctrine selection; pending replies still preempt. |
| `012_GODS_HOST_PRIORITY_AND_OFFENDER` | Selected doctrine, five core needs, one advanced lane, valid leniency/protection/offender/expedition/coercion targets: priorities alone number six; partners and judgment retain all four respective outcomes through meaningful parent choices. |
| `012_GODS_HOST_REPLIES_PREEMPT` | A submitted substitute and a paid reconciliation offer interrupt any view: accept/reject substitute and accept reconciliation stay accessible before the original deadlines; invalid affordability keeps its blocked reason, and victor exceptions survive. |
| `012_GODS_OPEN_DEMAND_NARROW` | Reuse the audit's declared ordinary-demand case, add Council eligibility: ordinary response family remains five and Council is deferred. |
| `012_GODS_SUPPORT_AND_COUNCIL` | Before sign, after sign and after a short/manual payment: Council remains deferred; frozen instalments, measured balances, grace and cumulative terminal reporting are unchanged. |
| `012_GODS_NEGOTIATION_AND_COUNCIL` | Three, fewer and zero valid slots; submitted offer; return/rejection; same deadline and paid receipts: at most three named substitutes plus return; no duplicate generic row or Council overlap. |
| `012_GODS_DEFIANCE_TWO_CLOCKS` | Reconciliation start day 100, due 160; ultimatum start day 120, due 180; at day 130 show both remaining clocks, reconciliation and two/three ultimatum answers, no preparations; neither due day changes. |
| `012_GODS_NONDEFIANT_ULTIMATUM` | A non-defiant target with Council eligibility and voluntary-aid need: retain all ultimatum answers and allowed aid/reconciliation, suppress Council and untimed defiance entry, preserve the parent's confirmation safeguards; at most four actions. |
| `012_GODS_PAID_OFFER_AND_ULTIMATUM` | Pay reconciliation at day 125; answer ultimatum at 140: the paid offer/sequence and due 160 survive, host acceptance stays usable and no second reparations payment occurs. Reverse resolution order: reconciliation acceptance leaves the ultimatum's due 180 and responses intact. |
| `012_GODS_TWO_CLOCK_EXPIRY` | Miss reconciliation at 160 while ultimatum runs to 180, then reverse deadline order and test same-day expiry: each applicable existing failure resolves once, with its own reports and unchanged current Strength/Chaos/host-validity punishment checks. |
| `012_GODS_PHASE_EXIT_AND_AUTHORITY` | Switch views, return, save/load, change human/AI control, end war elsewhere, begin war with Africa, invalidate host generation, commit settlement and enter recovery: no phase resets a clock, loses paid history, revives an old offer or suppresses frozen delivery. |

Never hide a still-running demand's required responses to make an overlapping state pass the table.
L26 requires no ordinary demand alongside a final ultimatum; verify the existing issuer/escalation and retirement paths before treating that invariant as proven, because the audit's partial scenario projection did not prove it.
If a valid demand/ultimatum overlap survives, leave that scenario unresolved for the parent owner's lifecycle repair rather than silently closing a paid contract or claiming the phase budget passes.

Prices are invariants, not repair targets.
Event 012 protection remains infantry equipment, fuel and PP plus at most one convoy OR train type, with the common-defence reserve covering and decreasing by the same accounted rifle shipment.
The separate Event 013 relief choice retains its existing price and ownership.
Keep expedition, preparations, reconciliation, Council, ultimatum and substitute costs, retained reserves, measured receipts and cooldowns unchanged.
The parent separately owns permanent-defiance confirmation, the measured Council pledge receipt and ultimatum-payment transaction verification; this addendum specifies only their phase interfaces.
Public mechanic values remain Strength and participant Wrath.
Reuse report art for .611–.613 and dedicated .614 art; all core phase behavior is available without DLC.

## Evidence limits and parent handoff

Research basis is the current source audit, accepted source design and installed/offline native decision rules.
The existing fictional continental doctrine already distinguishes common priorities, bilateral cooperation and judgment for proven offenses; that distinction supplies the semantic families.
No historical claim, new regional actor or cultural expansion is needed for this readability repair.

Source inspected: `common\decisions\012_africa_gods_decisions.txt`, targeted portions of `012_africa_gods_recovery_decisions.txt`, and the linked Gods effects, triggers, focus-payoff, punishment, lifecycle, epoch-binding and settlement owners.
The ordinary decision source SHA-256 at this read is `5515165dea18746734df2d50c7005d1a9c163b3afe015b2dce00967b3e4a7d45`; it can change while the parent implements parallel repairs.
The audit's `DECISION_ANALYZED_PARTIAL` revision `42dda9cb037cb3721cca63618cc62bd797e248553b1556eaa15ac2be9d711607` had 100 unresolved definitions.
Its narrow `012_GODS_OPEN_DEMAND_NARROW` artifact SHA-256 `8ed11780435e1f1d400507e02f48c5ceffd1efcbaa285c343488bbd2b9c1aa51` had 145 unresolved scenario inputs, including live country, host/member/epoch, war and helper operands.
Its false visible/available projections are not proven states.

The audit's GUI inspection found zero elements for the ordinary participant category, and its 706-byte offline render reported a missing GUI window.
It contains no native decision rows or click regions.
Native wrapping, row density, action accessibility and clipping therefore remain unresolved; do not substitute source counts or that placeholder render for native acceptance.
Existing event evidence in the final probability handoff also records `JOB_WORKER_EXIT` and no successful event overview artifact.
No new GUI, focus, map, technology/doctrine or event branch is designed here; technology-tool exposure and standalone-viewer availability are not evidence for this decision repair, and no absent-viewer package claim is invented.

One narrow connected `hoi4.reference_search` for `target_root_trigger` returned `OK`.
Detailed rules were read directly from `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md`:465–530 (missions and ROOT/FROM targets), revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, and installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md`:1–46 (frame/daily trigger cadence), revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
The existing audit's vanilla precedent `GER_mefo_bills_mission`, `common\decisions\GER.txt`:92–161, was also read directly.
These support presentation gates and independent mission ownership, not an engine six-row maximum.

`chaosx_ai_probability_auditor` performed one narrow `hoi4.probability_inspect` with `mission_ai_will_do` over only the reconciliation and ultimatum mission definitions.
It returned `PROBABILITY_SOURCE_INSPECTED`, revision `fca91fa6cb4510ad0919cd1b68aec8ee7633fbb6b3717bf321b80706f46969bb`, source hash `5e5c14392d42ceb3c7f6419dbf7637284c0502725362fa4fca0b46387ebbf6e6`, and the matching decision-file provenance hash above.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/038b75affe42b0cf09344d330f9ca5cce9bba016577512a54df19af3af489c29/1b254a6e411a40cd5f2557b9d0c59544f61b0bfcbc95eca4d841d94e24f47c37/probability-inspect-5e5c14392d42.json`.
Both supplied definitions were covered, with zero mission AI bases; `timeDistribution`, `normalizedProbability` and `sequence` were false, and no scenario/hash or timer-transition evidence was returned.
This is definition evidence only; deterministic deadline ordering and native cross-clock outcomes remain unresolved.
The auditor also confirmed the paid-review expiry and reconciliation-before-ultimatum edges; the explicit precedence and paid-history rules above resolve the proposed design without changing prices or inventing a pause.
The existing final probability handoff's incomplete eight-candidate model and 600-second evaluate/compare timeouts remain open; no broad retry, normalized probability or before/after delta is claimed.

Parent implementation surfaces are the existing decision file, Gods trigger/effect/lifecycle owners, the existing constants group and existing English/scripted-localisation status text.
No category registration, GUI, asset, focus, workbook or shared system change is required.
Acceptance requires matched source scenarios with concrete host ROOT/participant FROM, both arrays, current epoch, war state, receipts, deadlines and original cost/cooldown gates; unresolved bindings remain blockers.
AI eligibility changes, including preparation gates, untimed defiance entry and Council phasing, require the read-only `chaosx_ai_probability_auditor` to begin with `hoi4.probability_inspect`, retain a real pre-edit source, and compare the same named scenarios after the owner patch.
Retain all numeric bases/factors; compare decision willingness and eligibility without claiming normalized click probabilities.
Use separate mission, participant-response, Council and host-target comparisons, covering the two mission IDs, four preparations, permanent defiance, reconciliation, three ultimatum answers, both Council choices and the three host answer IDs in their own declared contexts.
The specialist's overlap cases map to `012_GODS_PAID_OFFER_AND_ULTIMATUM` and `012_GODS_TWO_CLOCK_EXPIRY`; these are proposed source scenarios, not already evaluated MCP fixtures.
Do not replay broad timed-out evaluations or substitute a current-to-current comparison for a missing baseline.

Remain in `docs\plans` while this proposal is unresolved.
On adoption, record the parent acceptance basis, promote these phase rules into the full spec's Participant response model, Africa-side gameplay, Defiance and reconciliation and Presentation sections, and align `docs\events\012_africa\gods_of_africa.md` with the resulting source.
Mark implemented only with the owner patch and its bounded validation evidence; keep native/probability gaps explicit.
No further expansion is recommended.
This is a concrete repair handoff, not whole-feature closure: phase implementation, parent-owned confirmation/receipts and the stated evidence limits remain.
No gameplay simplification or fallback is authorized or applied by this plan-only pass.
Skills applied: improvement-loop, event-planning, decisions-missions, events, subagents and the scripted-GUI content/interaction budget; no skills changed.

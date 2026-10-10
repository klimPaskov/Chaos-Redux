# Private Event016 staffing decision integration review

Date: 2026-10-09.
Reviewer: bounded read-only chaosx_decision_mission_auditor.
Disposition: source review delivered after owner fixes; no additional confirmed gameplay defect remains in the reviewed staffing paths.
Parent owns final documentation reconciliation, integration and commit.

## Scope and authority

The accepted contract is [016_private_paleogenetics_staff_integration_2026-10-09.md](../016_private_paleogenetics_staff_integration_2026-10-09.md).
The staff API document and [worker handoff](016_private_paleogenetics_staff_core_2026-10-09.md) were read.
The paired construction commits a048109ce and 9be5ce075 remain the supplied dependency.
Their paid transaction logic and old visual evidence were not re-audited.
The only inspection of the eight existing Biological Programs decision files was preservation of the added presentation predicate.

This review owns only this report and permitted temporary audit output.
The report destination was absent when ownership was checked.
No gameplay, model, asset, unit package, game, index or Git write occurred.
Tests ran without result-file writing; no duplicate JSON snapshot or separate status report was created.
Latest AGENTS.md, SHA-256 70c6820d5efe34dc2bb47d6eeca7c02ec6726fdad85c60667b81a0b395fe1b10, governs the bounded source/local-check route.
Unavailable or inconclusive tooling is a verification limit, not an automatic implementation or user-game acceptance gate.

## Findings and owner resolutions

### Resolved: completed training must not expose settlement recovery

The parent added NOT mengele_event016_paleogenetics_staff_trained to staff_can_recover_training before this audit.
The ordinary recovery row also excludes trained state.
The literal native-consumer case “completed training exposes no settlement recovery row” verifies that a qualified completed team has neither a repeated completion row nor an eligible recovery helper.
This preserves completed history and prevents another settlement attempt from being presented as work still owed.

### Resolved: terminal zero debt could expose a no-progress release action

The separate AI auditor identified the conditional zero-debt/in-flight edge.
This auditor reproduced it using the actual staff source and native fixture: a conserved original receipt with crew_held=0, support_due=0 and crew_credit_inflight remained current and passed can_recover_release.
Recovery returned result_partial=2, made no currency write and left the receipt open because finalize_release correctly required both in-flight flags to be absent.
This was a source availability/finalization mismatch; no live-engine interruption or currency exploit was claimed.

At the earlier trigger hash dcc9bc23c8d6a8729743d16ffda00e78d5ba677d9b6c41b635afa7b46c58456f, the zero-debt OR arm checked only the two zero obligations.
The parent added NOT crew_credit_inflight and NOT support_credit_inflight to that arm, matching the finalizer.
The current trigger hash is 709dbc1d6338d5e9fae3aecab4e94ed959215402dbf2d4c89fe3f10b8e6659a1.
Independent post-fix checks for each in-flight role returned receipt_current=true, can_recover_release=false, result_no_op=0 and zero new currency writes.
The added maintained native regression also passes.

The fix is confined to terminal zero-debt acknowledgment.
An independent positive non-inflight obligation can still be recovered while another role is in flight.
No weight change, blanket credit bypass or blind retry was introduced.

### Resolved: suspended status gave an incorrect repair-only instruction

The earlier mengele_paleo_staff_status_suspended told the player to restore control and repair the sites.
An actual-source branch check with a trained team and missing operational technology selected that text while qualification was false, despite intact sites.
A conserved-proof corruption case likewise selected suspended state while demobilization availability was false.
Repair alone could not resolve those conditions.

The parent replaced the text with “Service is suspended. The trained team remains allocated to the sites.”
It retains the real allocation without claiming a specific cause or inventing casualties.
Admission/recovery requirements separately name programme access, operational entitlement, ownership/control, repaired capacity and original receipt proof.
The broad status is not an attestation that financial proof is valid; action availability continues to require the full current receipt.
The final handler/veterinary description also reads 100 and150 through constant-backed getters.

### Reviewed policy boundary: sale expiry does not create delayed Personnel credit

The real native achievement chain is attached: funded support record registers a refundable Personnel claim; qualified settled completion calls confirmation; unused-fee cancellation retracts; completed-fee demobilization retains an already earned claim.
Actual Personnel role/proof/record/confirm/retract helpers execute in the native driver.
Only the consumed concrete support fee enters purchase proof.
Workforce escrow and native CIC do not become purchase members.

There is a temporal limit in the existing ordinary achievement policy.
Training lasts60 days; Event026 active_duration_days is1; black_friday_confirm_achievement_transaction at common/scripted_effects/026_black_friday_effects.txt:810-848 requires an active valid sale.
An ordinary receipt completed after expiry therefore remains unconfirmed rather than earning post-expiry Personnel credit.
The original positive claim test keeps sale eligibility true and calls the native removal body directly; it proves the owner chain and earned-credit retention, not natural clock overlap.

The parent added “sale expiry keeps the paid fee and obeys ordinary delayed-credit policy.”
An independent expiry fixture likewise qualified the funded staff while leaving claim state pending0 rather than committed1.
Parent/user acceptance confirms that the current staffing contract authorizes no post-expiry Personnel-credit exception and no new achievement.
The owner therefore preserves the existing active-sale confirmation policy.
The ordinary staffing discount still applies to the exact support fee, but the one-day sale normally expires before the60-day training completes, so the registered receipt normally remains pending and earns no family credit after expiry.
There is no promise that staffing automatically earns the Personnel family.
The positive sale-valid fixture tests only that eligible branch; the separate expired fixture proves pending/no award.
This accepted consequence does not block the bounded staffing implementation and does not claim global Black Friday completion.
It does not alter payment, escrow, native reservation or timing, and consumed material is not refunded because the sale expired.
If another owner later changes the shared confirmation policy, that is a new input for a narrow recheck of this owner call chain; unchanged staffing, paired logic and old tool failures need not be re-audited.

## Costs, ownership and lifecycle

The action consumes a nominal100 concrete support_equipment_1 through the exact UNIVERSAL quote/payment/record APIs.
A valid four-input owner descriptor selects Personnel family2097152, support primary component6, primary-component basis1 and member1.
Price eligibility remains support mask32 and physical resource kind11.
The descriptor is supplied by the literal owner binder, validated, frozen and consumed by BEGIN.
It does not infer a family from currency or borrow Portal identity.

The fixed250-person allocation is real returnable escrow:100 handlers and150 veterinary staff.
Shared native manpower kind3 is used without a purchase quote, discount subtotal or achievement member.
Only a bounded manpower_k before/after difference is multiplied by1000; no deprecated total-manpower expansion is used.
The native decision assigns two CIC for60 days.
This is three distinct consumed/held/committed types, below the four-type limit.

The inline support and workforce costs use support_equipment_text_icon and manpower_texticon.
The native cost tooltip uses civ_factory, explicitly distinguishes consumed material from held people and states the duration.
Base, blocked and tooltip keys exist.
Colour predicates share the exact fee and inclusive personnel checks used by admission.
The shared quote uses quantum1: a33.33-percent source ratio produced fee34, and support33 was correctly blocked; integer formatting therefore agrees with this quote contract.

Full admission requires the descriptor, valid complete paid pair, provider/neutral entitlement, original undamaged post-level capacity, empty obligations, actual resources and two free CIC.
The literal complete_effect sets the native-entry marker; BEGIN consumes it and rechecks direct conditions after native admission without requiring two factories again.
No bare invocation, wrong descriptor or incomplete payment can fund staff.
Actor, serial, transaction, pair, source/fee and owner role freeze before debits.
Current qualification uses the frozen pair/generation and non-damaged infrastructure/factory thresholds.

Only full actual250 allocation and exact recorded support payment fund training.
Positive partial payment retains actual obligations; uncertain zero/negative debit cannot be repeated by ordinary decisions.
Training commits material consumption before settlement, then publishes trained roles/history only after settled proof.
Settlement recovery has no new payment, timer or CIC.
Completed training's NOT trained guard and duplicate receipt restrictions prevent a free second service.

Cancellation and demobilization retire qualification/timer before credits.
They return only actual held personnel and, for unfinished training, the actual unused fee.
Consumed material is not refunded.
Debt and observed acknowledgment remain actor/serial/nonce bound; partial credits reduce only their own remainder.
A zero, negative or oversized native readback retains an in-flight obligation.
No gameplay button calls the attestation APIs or manufactures a delayed debit from unrelated later stock changes.

The native demobilization and provider-cleanup adapters call receipt release before remove_decision.
The single provider-cleanup hook calls staff_cleanup_native before the existing programme receipt loop.
Removal is not treated as an implicit remove_effect or refund.
After programme loss, identity-only category/navigation visibility keeps the original obligation discoverable; payment and recovery still require full current proof.
After acknowledged closure, retraining uses a fresh serial/transaction and pays a new fee.
Ordinary Prototype production and learned neutral access remain independent of private staffing.

## Presentation, action count and mission quality

No category, GUI, asset, public meter or unit was added.
The operations flag is human navigation inside the existing Biological Programs category.
The added family filter is is_ai=yes OR NOT operations_view; the staff filter is is_ai=yes OR operations_view.
All eight saved-before files compare identically after removal of the26 added filter calls from their parsed source.
The separate AI audit additionally records44 unchanged existing weight blocks.
No old paired behavior was re-reviewed to obtain this preservation result.

Humans keep the family-stage view plus operations navigation, or the bounded staff phase plus return navigation.
Training, pending settlement, qualified-team release and owed-release phases replace one another rather than warehouse simultaneous primary actions.
The normal added operations phase has no more than three action rows including return navigation.
An engine-owned active timed row may additionally be shown; its presentation switch is not a cancellation condition.
The accepted six-primary-action budget is maintained by the new filter design without hiding original family access from AI.

The named paid pair, one service status, actual held/refund amounts when release is owed, and100/150 role breakdown explain what belongs to the player and what remains to do.
Descriptions separate the training fee, returnable allocation and native factory assignment.
No raw receipt arrays, source IDs or descriptor fields are shown.
There is no UI attestation/confirmation button that bypasses financial evidence.

No mission definition is in this tranche.
The COUNTRY owner starts a60-day timed training decision for its frozen reserve/hatchery region.
Success is a trained, settled team; loss of qualification suspends service without invented casualties.
Cancellation/failure retains or releases original actual obligations.
The explicit receipt, trained guard, closing conditions and in-flight guards address duplicate settlement, return farming and premature retraining.

## AI, registry and CXT review

The independent [staff probability/source review](016_private_paleogenetics_staff_probability_2026-10-09.md) was read.
It uses the updated authorized source-derived route, not normalized click probabilities or native campaign observations.
Training willingness is5 in peace and10 at war.
Demobilization is0 while pair_is_available and5 when it is false; completion and release recovery are5; both human navigation actions are0.
Other visible/available gates still decide eligibility.
The four human/AI view states preserve both contexts for AI.
No weight retune is recommended.

That AI report's dcc9bc23 trigger reading point predates the terminal zero-debt fix.
The new709dbc1d predicate and post-fix checks above resolve its no-progress retry edge without changing scores.
Its stale global-pair versus frozen-staff-pair note remains conditional on an unproved generation transition; no actual reachable release exploit was demonstrated or broadened into a paired-system audit.

Only the three BF-EVT016-PALEO-STAFF-TRAINING component rows in the master Event026 registry were reviewed.
They record consumed support/Personnel-primary proof, excluded250-person escrow and excluded fixed2-CIC/60-day occupancy.
The surrounding registry and shared ledger continuation/role comparisons were not edited or globally re-audited.

The new hidden carrier is modifier-free.
Its literal _apply helper sets only an idempotent CXT fixture-ready flag.
Startup registration is bounded to existing GER; daily_CXT only registers the bus token and marks pending synchronization, with no production grants.
The existing ownership probe calls the staff observer.
The observer reads current qualification/debt and writes CXT-owned diagnostic flags/scalars without payment, refund, personnel allocation or history.
The maintained native cases verify that observation leaves production/currency unchanged and carrier application is inert/idempotent.

## Checks and limits

This auditor independently executed57 core cases and17 actual native-consumer cases, for74 source cases, using the maintained CommonJS drivers.
The native module was required with its main output writer inactive; the core ran without --results.
No result file outside the assigned report was written.

The core reuses the checked-in fixed-point/lifetime interpreter and executes real UNIVERSAL quote/pay/credit/record/refund/settle/ack and allocator code.
Its explicit out-of-scope fixtures are the strict provider and the two paired API boundaries.
The native driver additionally executes real Black Friday metadata/proof/record/confirm/retract bodies while modeling campaign/sale predicates and native primitives.
Cases include exact discounted fee boundaries, admitted reservation, completed recovery suppression, cancellation withdrawal, consumed-fee earned-credit retention, expiry policy, provider-loss partial release, navigation, observer preservation and the terminal credit-in-flight edge.
These are useful source-model results, not live native callbacks or displayed glyph measurements.

The worker's retained command/scope validation is partial: valid=null, parametersChecked=false and unchecked native argument/root-scope coverage remain explicit.
Its cited installed documentation covers manpower_k thousands, native manpower credit/debit, non-damaged building readers and decision lifecycle; the offline references support the same bounded syntax.
This audit did not turn those receipts into parameter/runtime proof.

No new populated native-view, compound-decision-helper, graph or render request was made.
The initial-plus-corrected/narrower attempts for those underlying capabilities were already exhausted across agents/resumed turns.
No new input or capability change justified repeating them.
This task adds no dedicated GUI and does not reopen the old paired visual review.
Current review uses source, available local checks and the separate source-derived AI audit.
A future targeted retry would require a tool/input change that actually answers a specific remaining question.

Unverified native details include reserve/stockpile clipping and delayed recount, concrete model/design/producer restitution, interruption between effect and acknowledgment, destroyed-country persistence, save/reload, fixed native occupancy/order and immutable same-action callback generation.
No live test, restart or log request is an audit completion condition.
The user owns game observation; unavailable tool output was never reported as passed.

## Source identities at report creation

The identity table is a reading point, not a claim that entire mixed shared files were audited.
| Source | SHA-256 |
|---|---|
| common/decisions/016_mengele_paleogenetics_staff_decisions.txt | 0a64bf4d456a4f223c133d249366ec8aa269572f9d5ed6b3c8a976d8553e9308 |
| common/scripted_triggers/016_mengele_paleogenetics_staff_triggers.txt | 709dbc1d6338d5e9fae3aecab4e94ed959215402dbf2d4c89fe3f10b8e6659a1 |
| common/scripted_effects/016_mengele_paleogenetics_staff_effects.txt | b8bd7ff7176d3184cc6accac604ebd8fff0580574d4380ea61b0d3c0f06ec9a4 |
| common/script_constants/016_mengele_paleogenetics_staff_constants.txt | ecf3fd2b51392a39981a4038b9cbc3da304fdc827859ccc136a65a97b645e1d6 |
| common/scripted_localisation/016_mengele_paleogenetics_staff_localisation.txt | 8aa39133a7678178bfa5e49bc6b7af96ad4f97a8e3803ba8408a538526a6ecb3 |
| localisation/english/016_mengele_paleogenetics_staff_l_english.yml | ea7a55cda497454fa7b7fd7fc0eab7365eb8353bd808a10943fc400db0f45258 |
| common/decisions/categories/germany_mengele_categories.txt | 838451f2cfb0ea3bdee38993de7cb067ee8ed96c25936b46b1a3a7d46ece6a3f |
| common/on_actions/016_mengele_paleogenetics_staff_cxt_on_actions.txt | 8bbac0a78a552a888f716e78aefb9c6b0af7967cc13f89281750e63976a39656 |
| common/ideas/016_mengele_paleogenetics_staff_cxt_ideas.txt | c097c5621fd4001bc518134a2db08e551cba402ff0369bcdbf1c0c4d3ee52aa0 |
| .tools/tests/event016_paleogenetics_staff.test.js | 2bdbe4b0dddc6311ba3d8872e1261e1d4bc6381006c91e8820bf8ca9152fb939 |
| .tools/tests/event016_paleogenetics_staff_native.test.js | 63c82b5a3c06d707137d8067bb68bb39938f8ec2dda86b89e13f64667f25fda9 |
| docs/plans/016_brilliant_scientist_plans/016_private_paleogenetics_staff_integration_2026-10-09.md | 620be864924e6944c2d54ffc55dc73ac5b76aace0caedddf8f6b87af056dfe88 |
| common/scripted_effects/016_mengele_paleogenetics_staff_effects.md | 4fb67910d4c52e2fa3a43003b14d30d5531cda00183dd393d1f761335e16c0d4 |
| docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_private_paleogenetics_staff_core_2026-10-09.md | 60985ab720cfa9f62b2c9261a6f161329a2fd3713ac06f644e50fee15cda27b1 |
| docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_private_paleogenetics_staff_probability_2026-10-09.md | 17ac55f7194619c257790344677e6a2becc3b2bef28dd6ae48b10b66b41e5229 |

## Completion and remaining scope

Known local findings were corrected by the owner and the affected source behavior was rechecked.
No further confirmed staffing gameplay defect remains in the named reviewed surfaces.
No simplification was introduced by this audit.
The parent is reconciling its integration documentation/registry and owns the isolated commit.
Transport, kit escrow and breeding remain accepted future tranches; full private Paleogenetics and Event016 completion are not claimed.

Skills used: chaos-redux-decisions-missions, chaos-redux-events and chaos-redux-subagents.
No skill was created or changed.
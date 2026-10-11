# Event 026 CBRN coverup cost adapter handoff

Date: 2026-10-07.
Acceptance basis: the parent's bounded implementation request for the existing `cbrn_seal_state` and `cbrn_destroy_contaminated_records` purchases, including its subsequent four-output quote, persistent recovery, queue-limit and localisation-audit corrections.
Disposition: production adapters and source tests implemented within the delegated files.
Exceptional owner-trigger exposure and native scenario validation remain unresolved, so this handoff does not claim complete runtime recovery integration or Event 026 completion.
No staging, commit, revert, localisation edit, registry generation, default-enable change or gameplay redesign was performed by this worker.
The parent owns integration and commits.

## Files changed by this worker

- `common/scripted_triggers/cbrn_occupation_triggers.txt`, only the two price and two can-pay bodies plus their directly attached price comment.
- `common/scripted_effects/cbrn_occupation_effects.txt`, only `cbrn_occupation_execute_paid_coverup` and `cbrn_occupation_settle_paid_coverup`.
- `common/script_constants/cbrn_occupation_coverup_cost_constants.txt`, owner receipt-phase enum with integer schema.
- `common/scripted_effects/cbrn_occupation_coverup_cost_effects.txt`, three receipt recovery and cleanup helpers.
- `common/scripted_effects/cbrn_occupation_coverup_cost_effects.md`, public and internal cost/recovery API contract.
- `common/scripted_triggers/cbrn_occupation_coverup_cost_triggers.txt`, pure authoritative refund preflight.
- `common/scripted_triggers/cbrn_occupation_coverup_cost_triggers.md`, preflight caller-output contract.
- `docs/plans/026_black_friday_plans/subagent_handoffs/2026-10-07_cbrn_coverup_cost_source_tests.js`, actual-source suite.
- This handoff.

Parent-owned `common/scripted_localisation/cbrn_occupation_value_localisation.txt` and `localisation/english/cbrn_occupation_l_english.yml` are loaded and exercised by the test suite but were not edited by this worker.
No new visual asset, icon, sprite or equipment definition was required.

## Helper map and migration

| Helper | Scope and inputs | Outputs | Side effects and call sites |
| --- | --- | --- | --- |
| `cbrn_occupation_prepare_seal_state_pp_quote` | COUNTRY, current Condemnation and source registry | Four caller-owned price outputs | Temporary arithmetic only, called from seal availability and parent price/detail getters |
| `cbrn_occupation_prepare_destroy_records_pp_quote` | COUNTRY, current Condemnation and source registry | Same four outputs | Temporary arithmetic only, called from destruction availability and parent price/detail getters |
| `cbrn_occupation_can_pay_seal_state_pp` / `cbrn_occupation_can_pay_destroy_records_pp` | COUNTRY with FROM STATE | Trigger result and caller-owned forwarded price outputs if consumed | Pure normal-state reads, shared recovery preflight or shared inclusive affordability, used by existing decision gates and execute |
| `cbrn_occupation_coverup_can_retry_refund` | COUNTRY with FROM STATE | Trigger result, caller-owned target and receipt ID if consumed | Pure validated private receipt read, called by both can-pay helpers and four parent getters |
| `cbrn_occupation_execute_paid_coverup` | COUNTRY with FROM STATE, existing temporary action enum | No consumed temporary result | Recovers payer queue before preserving original fresh-action gates, called by the existing two decision complete effects |
| `cbrn_occupation_settle_paid_coverup` | Internal COUNTRY entry after fresh execute gate, same quote and action | No consumed temporary result | Real shared debit, typed record, unchanged state mapper, settlement or actual-paid refund |
| `cbrn_occupation_recover_paid_coverup_receipt` | Payer COUNTRY, temporary receipt ID | No temporary result | Acknowledged direct credit, shared refund or shared settlement, retains rejection proof, called by settle and queue recovery |
| `cbrn_occupation_clear_paid_coverup_receipt` | Payer COUNTRY, temporary receipt ID | No temporary result | Clears exact private receipt and matching state pointer only after acknowledgment |
| `cbrn_occupation_recover_paid_coverups` | Payer COUNTRY, no FROM required | No temporary result | Rotates only payer pending IDs, called before every existing paid-coverup execution and available for bounded owner integration |

The original repeated direct debit/refund logic was replaced in its two owned transaction bodies.
The existing decision call sites, requested-action mapper, seal/destruction outcome bodies, UID selector, admission/inspection paths, target/route checks, AI weights, casualties, upkeep and non-cost penalties remain intact.
The wrapper preinitializes the coverup proof, nested exact suppression proof, exact-row output and doctrine multiplier before state/helper traversal.
It preserves the state's requested-action input and its cleanup.
No central router or wrapper skill was introduced.

## Exact public quotation contract

The original producer names are retained.
Their four public temporary outputs are exactly:

1. `cbrn_occupation_coverup_pp_quote`, final payable price.
2. `cbrn_occupation_coverup_pp_ordinary`, represented ordinary fractional price.
3. `cbrn_occupation_coverup_pp_quote_valid`, one for a valid quote.
4. `cbrn_occupation_coverup_pp_source_id`, actual primary source from the neutral producer.

Every caller reading them after return initializes all four to zero before the helper call.
An invalid quote is not payable even if a diagnostic final value exists.
The parent price and detail getters implement that contract and use price unavailable on invalid data.

Ordinary scaling still calls `condemnation_prepare_scaled_fraction_cost` with the existing 40/60 PP bases and score clamp 0 through 1000.
The multiplier remains `1 + score / 500`.
No ordinary pre-sale rounding was added.
The resulting represented amount enters `universal_cost_quote_exact` with family Political Power and quantum one.
No eligible source preserves the ordinary fraction, while eligible sources multiply exactly and quantize once.
Quotes are recomputed for fresh display, affordability and payment through the same original helper names.
Both fresh can-pay paths and the parent hover invoke `universal_cost_component_is_affordable` with identical resource kind and amount.

At score 500.12345, ordinary seal/destruction prices are 80.00987 and 120.01481 under the modeled five-place truncation.
Baseline sale prices are 41 and 61.
At score 1.6665, the ordinary seal is 40.13332 and remains fractional without a source.
An eligible ratio 0.00001 still produces one positive integer PP quantum.
The producer supports future composable sources and does not depend on merely observing the Black Friday active flag.

## Receipt roles, constants and persistent recovery

Every payment uses the real `black_friday_allocate_owner_transaction`, `universal_cost_pay_component`, `universal_cost_record_transaction`, `universal_cost_settle_transaction`, `universal_cost_refund_transaction`, and direct credit API for an unrecorded debit.
The typed receipt family is `constant:universal_cost_family.political_power`.
Its primary ID is `constant:black_friday_event.owner_component_political_power`.
Its basis is `constant:universal_cost_achievement_basis.primary_component`.
Primary membership is one.
Ordinary, quoted, actual-paid and actual-source fields are snapshotted from the fresh producer.
There is one transaction per actual purchase, not a country-wide slot that another state overwrites.

New constants are lifecycle enum values only: `cbrn_occupation_coverup_receipt_phase.unrecorded_refund = 1`, `recorded_refund = 2`, and `applied_settlement = 3`.
Existing price, multiplier, source, quantum, component, cooldown, penalty and AI tuning is reused.
No balance value or source-count cap was added.

The payer owns `cbrn_occupation_coverup_pending_receipts` and the exact-state open pointer `cbrn_occupation_coverup_open_receipt_@var:cbrn_occupation_coverup_target`.
Each transaction also owns normal `cbrn_occupation_coverup_receipt_{target,action,ordinary,paid,source,sale,phase}_@var:cbrn_occupation_coverup_receipt_id` fields.
The braces here abbreviate seven separate variable names, not script syntax.
The matching API doc lists them individually.
No regular or global event target was added because normal payer target snapshots are needed beyond one chain.

A failed record retains unrecorded payment proof until actual-paid credit succeeds.
A failed exact-record dispatch refunds the shared recorded amount and cannot grant family credit.
A rejected shared refund retains the private fields, queue ID and state lock.
A successful outcome immediately releases its state payment lock, even when later settlement rejects, while unique private settlement proof remains.
Recovery never replays an applied outcome or refunds a success.
Only acknowledged settlement can call `black_friday_record_achievement_transaction`, using actual typed receipt proof and the retained matching sale generation.
The ordinary active/natural/human/disqualifier gates remain authoritative, and there is no post-expiry ordinary credit.
The payer also retains positive payment-time eligibility as exact receipt-ID membership in `cbrn_occupation_coverup_achievement_eligible_receipts`.
The snapshot uses the current public `black_friday_achievement_is_valid_sale` predicate, actual source 26 and positive ordinary/quoted costs immediately before the debit, and persists membership only after payment succeeds.
It is a normal array of eligible IDs, not a regular 0/1 boolean variable.
Recovery requires that membership in addition to current public receipt and campaign gates.
An AI-paid or debug-paid receipt cannot become creditable by changing control mode before settlement recovery.
Missing payment-time proof cannot be reconstructed from current eligibility.
Acknowledged refund or settlement cleanup removes only that exact eligibility ID and preserves other receipts' proof.

The queue removes its front ID before processing and re-appends only unresolved IDs.
It snapshots the initial count and respects the native 1,000-iteration stop without deleting any unvisited suffix.
The 1,001-entry cases prove both successful suffix retention and unresolved rotation in the source model.
This is bounded payer work on an existing click, with no world daily scan or new tick consumer.

## Pending preflight and player-facing integration

The authoritative pure trigger is `cbrn_occupation_coverup_can_retry_refund`.
It requires a positive exact-state open ID, existing saved target/paid/phase fields, target equal to FROM, paid amount greater than zero, and a refund phase.
Applied settlements, zero pointers, unknown pointers, wrong targets, missing/zero paid values and unknown phases are not refund affordances.
Fresh payment also rejects the presence of any open pointer, so malformed recovery proof cannot silently fall through to another debit.

The preflight exports only `cbrn_occupation_coverup_target` and `cbrn_occupation_coverup_receipt_id`.
Callers consuming them after return must initialize both to zero in their own frame.
The parent getters do this and use the successful returned receipt ID to read the paid snapshot.
The two can-pay helpers initialize those nested output fields internally.
An outer caller consuming their forwarded target or receipt ID also needs caller-owned storage.
The original four price outputs are unchanged.

Valid refund-only clicks pass affordability at zero PP while the native legacy target remains eligible.
Execute remembers that the click began as recovery and makes no new purchase after that recovery succeeds.
The parent owns four pending display branches, malformed-pointer unavailable branches, precision selectors and revised prose.
Those actual parent sources are tested, not represented by mocked display counters.

## Meaningful validation

Command: `node docs/plans/026_black_friday_plans/subagent_handoffs/2026-10-07_cbrn_coverup_cost_source_tests.js`.
Current result: 86 scenarios passed, 21,550 real scripted helper returns, and 82,017 helper-local temporary items discarded under the conservative frame model.
The test imports the existing exact-quote VM and actual current production definitions.
It runs the real selectors, native-affordability dispatcher, debit/credit, allocator, typed receipt record, shared settlement/refund, exact UID selector, evidence suppression, requested-action mapper, seal/destruction outcomes and achievement record/proof/family chain.
No action or receipt proof helper is mocked.
Native scopes, PP balances, flags, duration requests, modifiers and final sanctions publication are explicitly modeled.
The out-of-scope `condemnation_add_source` publication captures the actual owner/context/doctrine inputs without asserting the entire sanctions subsystem.

Coverage includes score 0/500/1000 and fractional 500.12345/1.6665, no source/baseline/evolution/composed/tiny/identity/excluded sources, invalid registry, PP below/exact/above payment, expiry and score changes before click, route/controller/actor/action rejection, missing exact UID, rejected record, rejected refund and retry, rejected settlement and owner recovery, payer/state isolation, no early/failure/refund/AI/manual/forced/debug/expired family credit, all four parent normal/invalid/pending display chains, malformed pointer fields, broken shared-row retention, actual seal duration and flag write counts, and repeated invocation.
The parent-reported AI-to-human failure was reproduced before the fix through the real applied-outcome/rejected-settlement/recovery chain, producing one invalid family claim.
Both AI-to-human and debug-to-normal transitions pass after the payment-time snapshot patch.
Additional cases cover human-to-AI/debug recovery under current public gates, two eligible pending transactions recovering independently, exact eligibility-ID cleanup, record/refund cleanup, and missing eligibility proof without retrospective inference.
The native array model explicitly handles value removal for eligibility IDs separately from index/front removal for the recovery queue.
An exact UID beyond the existing 1,000-row selector limit refunds instead of falling back to another record.
That pre-existing selector limit is preserved and explicitly reported, not replaced with a cap on shared sources or receipt history.

The latest tested worker source hashes are:

| Source | SHA-256 |
| --- | --- |
| `common/scripted_triggers/cbrn_occupation_triggers.txt` | `55d9f4ce79911d202f42072f4cc01b59feaa1315299be6d0c5a42adafbcc5d3f` |
| `common/scripted_triggers/cbrn_occupation_coverup_cost_triggers.txt` | `a6c1beb547ef0cdd721141f95faa75422f6083cd523ec411e29334bf3bdeb615` |
| `common/scripted_effects/cbrn_occupation_effects.txt` | `43f6d7c043d227f698fee88707c38caade23113ea9d4662000590ce89764a0de` |
| `common/scripted_effects/cbrn_occupation_coverup_cost_effects.txt` | `bb4d0d6b4d0fbb84d0664ccfc0e5a514b63d5a938f95280666860b2b6716e17f` |
| `common/script_constants/cbrn_occupation_coverup_cost_constants.txt` | `643e35988e556b3991239b452ec0458a05529755cffddab8dfb0f0149aaac12c` |

The suite prints hashes of all loaded shared and parent presentation files for independent current-state review.
Parent source hashes at final read were `2a5495aea10e11216341142a372bdd5abc951103732809433fba8cc5c6b0bb96` for the scripted localisation and `23a74c0e952e417b73daa04f748543be4f268ccd61cc7ea30d8a29221aa217a2` for its YML.

## Native references and MCP evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
Live `hoi4.reference_context`, search, read and source lookup returned real results.
No omitted required source kind was reported by the decision context bundle.
The source-kind `script_doc` snapshot is unavailable, while installed `game_doc` and offline `wiki` sources exist.

- Native decision scopes: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, read through MCP.
- Custom-cost payment/display and static AI hint: repository `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md:284-336`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, read through MCP.
- Temporary output lifetime: repository `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, read through MCP.
- Numeric variables and state/integer targeting: same Data structures revision, local sections 425-443 and 547-555.
- Array mutation and iteration limits: same Data structures revision, local sections 1212-1256, plus installed `documentation\effects_documentation.md:4279-4312,6016-6030,7888-7908`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Payment eligibility array membership: installed `documentation\triggers_documentation.md:5672-5685` (`is_in_array`) and `documentation\effects_documentation.md:2278-2291,6016-6030` (`add_to_array` and value-based `remove_from_array`), read directly for the snapshot correction.
- Native PP effect: that effects revision, section 1854-1862.
- Native PP trigger and temporary primitives: installed `documentation\triggers_documentation.md:4547-4555,6442-6454,7482-7502`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, read locally.
- Native constants: `documentation\script_concept_documentation.md:184-234`, hash `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, plus all of `common\script_constants\documentation.md`, hash `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.
- Localisation temporary calculations: repository `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md:729-776`, revision `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`, read locally.
- Scope types and validation: repository `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md:42-86`, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`, read locally.
- Native targeted custom-cost precedent: `game:common/decisions/AFG.txt`, `AFG_cross_border_target_state:458-522`, read through `hoi4.source_lookup`, source revision `e7d8019d546aa571f52f6634375f033bf88b17661ee8785f21f278a3851e785b`, with complete one-definition result and no references requested.
  Its custom-cost gate/manual debit/STATE FROM structure was read locally at 474-515 too.
  Local AFG source hash is `dabc91c3f7fb1810d64d91d07147e827068d42540326ce10554a0752ee48d7a7`.
- Existing mod precedent: `common/scripted_effects/012_africa_rsa_purchase_effects.txt`, shared pay/record/settle/refund and typed-role pattern, with caller lifetime and actual-source issues handled explicitly rather than copied blindly.
- Existing neutral helper registry and markdown were read before creating owner recovery helpers.

Initial `hoi4.decision_inspect` calls without scenarios were rejected with `Decision inspection requires declared scenarios at scenarios`.
Corrected declared-scenario queries for `cbrn_seal_state` and `cbrn_destroy_contaminated_records` each failed with `timed out awaiting tools/call after 600s`.
Their named requests were `CBRN-SEAL-ordinary-zero` and `CBRN-DESTROY-ordinary-zero`.
No successful decision scenario artifact or engine coverage is claimed.
The first guessed vanilla symbol had zero definitions and was replaced by the exact AFG precedent above.
An initial `hoi4.script_validate` request with limit 40 was rejected because the live route accepts at most 32.
The recovery-body validation request was subsequently rejected with `Provide either source with kind and scope, or a mod file path at source`, so it supplies no validation evidence.
The COUNTRY/FROM STATE preflight validation returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, 12 checked commands, eight unchecked argument blocks and zero omitted findings.
Its checks cover syntax, command kind and declared scope only, with `parametersChecked = false`.
Documentation aggregate revision is `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The cited native temporary and variable syntax was read directly, including `check_variable:2110-2135`, but the partial checker result cannot be described as complete argument or engine validation.

The mandated read-only `chaosx_ai_probability_auditor` was spawned as `01a11623-fbaf-7722-9a66-98640e57fba2` for the existing two decision weights and named score/sale/affordability states.
Its final findings returned before this handoff closed.
Two `hoi4.probability_inspect` requests for adapter `decision_ai_will_do`, source `{ path: "common/decisions/cbrn_occupation_decisions.txt" }` and the two named decision IDs each timed out after 600 seconds.
Its structural decision inspection and Event 026 event trace also timed out after 600 seconds, and its event render remained unobserved.
No artifact URI, accepted input contract, source revision, scenario hash, analysis ID or complete candidate pool was returned.
Consequently no probability evaluation, sweep, compare or render conclusion is available.
No AI weights were edited and no numerical probability comparison, normalized choice or AI pacing result is asserted.
The auditor's intermediate source findings used older trigger/recovery hashes `08709481...` and `28b585ec...` before the final authoritative preflight and shared-affordability correction.
Its comments about direct native PP comparison and a missing helper markdown therefore do not describe the final patch.
Both public API markdown contracts exist, and the final source hashes above identify the corrected files.
Its remaining source observations are the preserved base willingness scores 20 for sealing and 10 for destruction, existing ideological/route zero-weight gates, and fixed nominal PP hints.
Those are source inputs, not evaluated choice probabilities, and preference or starvation across the complete native decision pool remains unresolved.
The parent has independent decision/localisation audits and owns final integration review.

## Unhandled settlement access, limits and parent follow-up

The underlying rejection paths retain actual payer proof and are source-tested through real recovery helpers.
Full availability of a recovery invocation is not implemented for every world state in this delegated patch.
If a failed-refund target loses its legacy control/route/record/visibility requirements, the native decision still hides or rejects it.
If an outcome succeeds and receipt settlement rejects, that state's existing response flag normally hides the purchase decision, although its payment lock is already released.
Another eligible paid-coverup click services the queue, but a payer with no such click has no guaranteed player recovery invocation supplied here.
This is the exceptional integration gap and must not be labeled complete.

The parent can wire `cbrn_occupation_recover_paid_coverups = yes` into an existing bounded original-payer owner action or callback.
The helper requires no FROM and never replays outcomes, refunds a success, changes route gates or scans the world.
For a state-control callback, `ROOT` is the new controller and is not necessarily the payer.
The existing `common/on_actions/cbrn_occupation_on_actions.txt` documents FROM as the former controller and FROM.FROM as the state.
Any parent recovery dispatch must select the existing original responsible payer rather than assuming the new controller or arbitrary ROOT is responsible.
Existing delayed `cbrn_occupation.1/.2` callbacks are state-owned and conditional, so their presence alone does not prove guaranteed receipt recovery.
No additional call site was patched outside the assigned bodies.

Persistent normal fields and queues are modeled separately from temporary helper storage, but native save/reload serialization was not observed.
Native integer/fractional resource debits, modifier expiry, cooldown consumption on a rejected native click, actual row rendering, AI eligibility timing and multiplayer scheduling remain live-consumer limits.
The fixed nominal 40/60 PP AI hints are preserved.
The installed decision documentation requires a constant hint, so this work does not claim those hints accurately pace dynamically scaled or discounted purchases.
The unchanged exact UID selector stops after 1,000 iterations, and a later UID is refunded rather than approximated.
Malformed or missing shared receipt rows remain retained for repair and are never converted into guessed refunds or successful settlement.
There is no unapproved fallback or gameplay simplification in the owned source patch.
These explicit integration and validation gaps prevent a broader completion claim.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or modified.

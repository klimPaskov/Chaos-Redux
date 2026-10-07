# Final Council measured-receipt source review

Status: completed bounded source review and actual-source model verification, with both R1 and R2 corrected by parent and rechecked.
No outstanding scripted-receipt defect remains in this bounded review.
Parent documentation and MCP/probability evidence remain separate completion work.
Acceptance basis: the parent assignment in this session specifies accepted L27 prices and accepted L3 sender-loss accounting.
The original assignment permitted only this handoff.
The follow-up explicitly permits one bounded verification file at `.tools\validation\test_012_gods_council_receipts.js`.
No gameplay, other documentation, Git, or game launch work was performed.

## Findings and parent fixes

R1, original finding: `common/scripted_triggers/012_africa_gods_council_triggers.txt:69-77` checked `gods_of_africa_council_material_is_accounted` only inside the current-pledge branch of `gods_of_africa_council_speech_can_replace_pledge`.
The absent or stale context branch therefore authorized speech even with a retained `gods_of_africa_material_transaction_unresolved`, prepared transfer, or pending native receipt.
This can occur after live pledge terms are cleared while unresolved receipt evidence is deliberately retained.
Require accounting-clear outside the OR, or in the shared speech execution and availability gate, to preserve the instructed speech-switch policy.
This is a source control-flow finding, not a native engine observation.
Disposition: implemented by parent during the verification follow-up, with the accounting-clear predicate moved before the OR.
The actual-source regression case fails on the old source and passes on the corrected source, whose SHA-256 is `1c9266025c6f7b92e728ed35d9663256a020ac99ebae0a076c210e2aa82e0218`.

R2, original finding: normal final settlement did not clear live Council terms in the first ready source.
`common/scripted_effects/012_africa_gods_settlement_effects.txt:196-203` calls `gods_of_africa_finalize_participant` on the successful `settlement_pass_pending` path.
That participant finalizer at `common/scripted_effects/012_africa_gods_effects.txt:4334-4431` originally did not call `gods_of_africa_clear_council_pledge` or clear the private Council inventory directly.
The `clean_participant` call at settlement effects line 58 belongs only to the rejected-grading branch.
Add the narrow Council clear inside the guarded normal participant finalizer, preserving measured quantities and unresolved shared receipts and leaving events untouched.
The four other requested lifecycle sites already contain the clear.
Disposition: implemented by parent and rechecked in the actual guarded normal finalizer at `common\scripted_effects\012_africa_gods_effects.txt:4344`, immediately after retire/release.
The four other cleanup additions are unchanged.
The production-source call-site assertion passes and the file SHA-256 is `ae6bc014b3485b6cb9225c8d3ad95e3b6e3c25cc39b842a8e9a17660e7fbd0a8`.

## Core findings established so far

The contribution identity guard does not recheck pre-debit affordability after native transfer.
A full payment from exactly remaining plus the frozen 500-rifle reserve therefore does not fail merely because only the reserve remains.
The purpose flag excludes the ordinary voluntary-aid owner and selects the Council reserve requirement at begin.
The receipt uses typed country references and identity comparisons without ordinal arithmetic on `THIS.id`.
Measured donor loss reduces the pledge balance, while the separate host reserve increment is bounded by actual receiver credit and consumed donor quantity.
The completion-consumed signal is cleared on entry and the reserved ID is consumed before cumulative credit.
Partial and zero results do not publish Council voice or coarse aid in the Council owner.
Unknown native quantity retains receipt evidence and grants no consumed result.

## Final pass scope

The parent core/code-ready signal was received after the preliminary matrix was written.
Final decision and localisation review is complete against the ready source and the parent's explicit R1/R2-applied follow-up signal.
Parent documentation is explicitly still pending.
The final pass, source matrix, ready-snapshot hashes, reference evidence, and remaining limits are recorded below.
The parent owns mandatory MCP inspection and validation, and the probability auditor owns the two Council decision scenarios.
This source review makes no whole-goal or native completion claim.

## Source case matrix

These are control-flow and arithmetic traces through actual production bodies, not execution of a replacement arithmetic harness.
`D` is positive donor BEFORE minus AFTER, `G` is positive receiver AFTER minus BEFORE, and `R` is the frozen unpaid pledge balance.
Supported consumed quantity is `min(R,D)` under the accepted L3 policy.
Host reserve credit is `min(R,D,G)` through the Council clamp, matching the existing `_complete_payment_receipt` policy.

| Case | Production source trace and result | Limit |
| --- | --- | --- |
| First affordable attempt | `pay_council_pledge` checks shared affordability, `initialize_council_pledge` freezes the exact participant/host/origin/generation/epoch tuple, 1,000 total and 500 reserve, then shared begin independently checks source stock against `R + reserve`. | Native transfer semantics remain parent-owned evidence. |
| Stock below 1,500 | Fresh affordability rejects before freezing or sending. | Inclusive stock comparison follows the actual `NOT has_equipment < needed` source. |
| Partial loss 400, gain 400 | Shared recorder adds 0.400 to total and voluntary infantry ledgers and campaign subset when proven, consumes the unique receipt ID, then Council leaves remaining 600 and adds 400 host reserve with no voice or coarse aid. | Reads and prospective ledger writes must satisfy the existing exact accounting domain. |
| Resume partial | Current tuple selects frozen remaining 600 plus frozen reserve 500, not a fresh 1,000 price. Shared begin requests 600 and reserves another monotonic ID. | Fresh source stock and funding are recalculated for each click. |
| Zero loss and gain | Shared recorder consumes zero once, leaves quantities unchanged, Council leaves the full balance, sets retry day to `global.num_days + undelivered_retry_days`, and publishes no voice or aid. | Seven-day expiry is a source comparison, not observed timed engine behavior. |
| Mismatch loss 400, gain 250 | Recorder credits donor loss 0.400 once and retains mismatch evidence. Council balance falls by 400, host reserve rises by 250, and no final voice occurs. | Deliberately follows accepted sender-loss policy. |
| Mismatch loss 250, gain 400 | Donor credit and pledge reduction are 250, host reserve increment is clamped to 250, and excess receiver gain is not counted as maintained reserve. | Matches `_complete_payment_receipt` donor bound. |
| Full loss 1,000, gain 1,000 from source 1,500 | Post-send identity guard does not require the old 1,500 affordability again. Recorder consumes one receipt and adds 1.000 measured infantry, Council adds 1,000 reserve, clears live terms first, then publishes pledge voice and one aid history entry and world-history sync. | Native quantities are not established by this source trace. |
| Full donor loss with lower receiver gain | Full donor payment may finish voice and aid, while host reserve follows the lower bounded gain and the mismatch flag survives. | Accepted L3 policy permits this and the review does not redesign it. |
| Unknown native quantity | Completion retains pending receipt, snapshots and unresolved state without a fresh consumed signal. Council leaves balance and reserve unchanged and publishes no voice or aid. | No fabricated zero, refund, replayed transfer, or deferred recovery is introduced. |
| Prospective ledger accumulation rejected | Recorder retains measured pending evidence and unresolved state without consuming ID. Council does not use the durable actual output unless the fresh consumed flag is set. | An output quantity alone does not establish accounted payment. |
| Tuple drift during receipt | Exact source/receiver, typed identity, generation, origin, epoch, request binding, sequence and same-day guard fail closed. Existing prepared receipt is quarantined as unresolved rather than converted to zero. | Participant terms require lifecycle cleanup by parent. |
| Begin rejects after live terms freeze | Begin freshly clears readiness and consumed signals before checking ownership, sequence, reserve and receipt state. With a missing or exhausted sequence it grants no native send. Council leaves the uncharged terms and frozen quote, clears its synchronous purpose flag, and adds no quantity, reserve, retry, voice or aid. | A false begin is not an empty consumed transfer and therefore does not acquire a seven-day retry. |
| Recorder replay | Pending is consumed and last-consumed ID advances before cumulative writes. Repeat completion clears the result flag and has no prepared identity after work cleanup, so Council cannot apply the old actual output again. | Read-only source proof, no native callback execution. |
| Council click replay after full | `council_is_open` rejects the existing voice flag. No new begin, debit, reserve increment, or aid entry occurs. | Requires the final decision to use the same shared gate. |
| Accounted uncharged quote to speech | Current pending terms with remaining equal total and accounting clear permit the alternative 25 PP debit once, then clear live pledge terms and publish speech voice. Retry day does not bar this alternative. | Shared decision and execution gates reviewed, source-model case passes. |
| Partly paid current pledge to speech | Remaining differs from frozen total, so speech replacement rejects without PP debit or term clearing. | Parent R1 fix also rejects unresolved native work when live terms are absent or stale. |
| Ordinary demand, negotiation, reconciliation, ultimatum | Shared response-phase predicate rejects either Council response for any of the four live flags. Council helpers do not remove missions, alter demand balances, or edit deadlines. | Final availability wiring and five lifecycle cleanup sites source-reviewed. |
| Ordinary voluntary aid | Exact ordinary aid owner, shared native reader, completion, recorder, payment adapter, identity guard and accumulation predicate were compared with the immutable baseline and are unchanged. The ordinary lane excludes only the synchronous Council purpose flag and retains its 500 shipment and 1,000 stock requirement. | Purpose and frozen receipt-council flags are additional work flags, not new public quantities. |

## Helper and ledger map

| Helper | Scope and inputs | Outputs and side effects | Direct consumer |
| --- | --- | --- | --- |
| `gods_of_africa_initialize_council_pledge` | Current participant country and proven `africa_host`, existing constants and material readiness | Private exact tuple, pending flag, frozen total/remaining/reserve. Replaces stale live terms only after payment eligibility. | `pay_council_pledge` |
| `gods_of_africa_pay_council_pledge` | Participant country, shared read-only gate, frozen or new pledge | Purpose flag, exact regular receiver target, one begin/send/complete sequence, actual balance decrement and bounded reserve increment after consumed receipt, zero retry and guarded finish. | Existing Council pledge effect |
| `gods_of_africa_complete_council_pledge` | Participant country, current response phase, exact tuple, zero remaining | Clears terms before one-time voice, coarse aid and world history. | Consumed receipt branch |
| `gods_of_africa_clear_council_pledge` | Participant country, no inputs | Clears only live pledge flags and ten private fields. Does not erase measured totals, shared unresolved receipts, sequence or retained output evidence. | Initialization, full finish, speech, archive, defiance, clean-participant, cancel-participant and guarded normal finalizer |
| Existing `begin_material_transfer` / `complete_material_transfer` / `record_paid_contribution` | Participant country with bare kind/request/voluntary/emit-kind temps | Existing monotonic native receipt and measured contribution owner. Council purpose selects a distinct voluntary lane and frozen source reserve. | Council, ordinary tribute and ordinary voluntary aid |

No new constants are required.
Retain `gods_of_africa_council.pledge_equipment = 1000`, `pledge_equipment_reserve = 500`, `speech_pp = 25`, and `gods_of_africa_timing.undelivered_retry_days = 7` in their existing categories.
The `-1` speech multiplier is unchanged baseline arithmetic, not a new price.
The draft adds no loops, DLC conditions, model callbacks, new public grading values, or arithmetic on typed country identity tokens.
The participant history and full grading ledger must be valid before begin.
Total and qualified subsets are preflighted together and written by the existing recorder, so Council does not create a second measured ledger writer or manipulate ordinary demand denominators.

`gods_of_africa_council_receiver` is a regular target rebuilt synchronously from the frozen host pointer and used for native transfer and reserve credit.
The shared receipt owns separate persistent source and receiver pointers and exact identity mirrors.
No new global target requires clearing.
Cancellation, archive, defiance and final settlement must invoke only the live Council clear alongside their existing cleanup and preserve both measured lifetime quantities and shared unresolved receipt evidence.

Migration is narrow: replace the old unconditional Council shipment and nominal reserve credit with the existing pledge wrapper delegating to `pay_council_pledge`, route both decisions and their visible quote through shared predicates, and add live-term cleanup to existing owner lifecycle sites.
The core receipt measurement and ordinary aid bodies remain unchanged.

## Baseline and meaningful validation

All eight archived files were read through `before/manifest.json` and their SHA-256 digests match the immutable manifest.
The source comparison used Python `difflib` and direct production block comparison without Git operations or output files.
Exact unchanged bodies confirmed: `read_contribution_native_stock`, `complete_material_transfer`, `record_paid_contribution`, `complete_payment_receipt`, `material_transfer_identity_is_current`, `contribution_accumulation_is_representable`, and `offer_voluntary_aid`.
Draft differences in shared begin are the frozen Council purpose and reserve branch, with corresponding work clear.
The owner-input guard adds the exclusive Council alternative without altering ordinary request binding.

No existing Event 012 host interpreter was found in the initial review.
The follow-up supplied the reusable Event 033 parser and execution pattern and authorized a bounded Council model, recorded below.
Existing Event 021 front-receipt and Event 033 humanitarian-receipt tests cover different owners and are not evidence for this path.
The matrix above is the permitted meaningful source-case review and retains its execution limits.
No arithmetic-only replacement harness was created.
The follow-up model loads actual production effect and trigger bodies and fails on unsupported commands.
AI willingness, GUI, focus layout and maps were not audited or broadened.

## Reference evidence

MCP reference routes were present and the live searches, context and revision-bound reads returned `status = ok` for workspace `mod_chaos_redux_ea3b2d67c2c0`.
`reference_context` identified sources and reported omitted Decision modding, Triggers and Localisation sections at its four-item limit.
That broad context is not claimed as complete domain coverage.
The parent retains mandatory surface inspection and final source validation ownership.

| Source path | Read lines | SHA-256 revision | Relevant rule |
| --- | --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 6550-6558 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | `send_equipment` country scope and supported targets. |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 2254 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | Variable amount and target, partial transfer rather than negative stock. The old `type` spelling is superseded for this consumer by installed vanilla precedent. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 216-222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | Shared constants and scoped-variable `constant:` support. |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | 1-34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | Schema and supported-field limitation. |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 260-263 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` | ROOT persists, THIS is the current participant and PREV follows actual nesting. |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263-269 via MCP, 303-325 and 429-451 directly | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | Event-target pointers, regular-chain lifetime, typed object variables and unscoped temporary variables. |

Direct vanilla precedent read: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\scripted_effects\USA_scripted_effects.txt:403-418` uses `send_equipment = { equipment = small_plane_airframe amount = 25 target = ROOT }`.
The Council's fixed `equipment = infantry_equipment` mirrors that native keyword without synthesizing models.
The installed send-equipment section does not establish exact runtime stock-reader range, synchronous donor/receiver observations, typed-ID engine implementation, or native cooldown behavior.
Those limits remain explicit and the review does not invent a country ordinal from `THIS.id`.

## Documentation review still pending

The adjacent Council helper documentation does not exist in the inspected draft yet and remains parent-owned work.
Existing contribution documentation has historical text that says unequal or zero measured deltas set durable unresolved state, while the unchanged current production completion sets mismatch and credits supported donor loss.
The parent should make the touched helper documentation describe the actual accepted L3 policy when completing the Council documentation.
This discrepancy does not justify changing the shared receipt mechanic during this review.

Skills applied: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill files were edited.
No gameplay implementation simplifications or fallbacks were made by this reviewer.

## Ready-source decision, quote and lifecycle pass

Parent-ready signal: core/code wiring was declared ready for a final bounded source review in this session.
It identified new Council files, shared purpose/native floor, wrappers, two decision preflights and AI zero gates, dynamic amount/reserve getters and English keys, and four Council cleanup hooks.
It explicitly left parent documentation for the next step.

The new `common/scripted_localisation/012_africa_gods_council_scripted_localisation.txt` contains both getter definitions.
The getters and affordability use the same exact pledge-context predicate, selecting frozen remaining/reserve for a current tuple and existing 1,000/500 constants otherwise.
The two affordability branches have separate scratch names, so evaluating a nonselected branch cannot overwrite the selected branch's needed-stock value.
Quoted costs therefore stay separate from fresh affordability and from the shared native begin reserve check.
English cost rows, blocked cost rows, reserve requirement and effect text all consume those getters.
Speech retains the existing 25 PP cost and effect-owned single debit.
The existing two decision consumers call the wrappers in their participant scope.
Neither callback changes ROOT to the host, and the helper accesses the participant through THIS and the proven frozen host pointer.
The pledge decision repeats while unfinished, gates availability through `pledge_can_be_paid`, and hides with speech during any of the four response phases.
The speech availability composition matches its execution gate, and the parent corrected its shared R1 predicate defect during the follow-up.
The AI zero-factor gates reference the same predicates, which is source coupling only and is not a probability audit.

Confirmed live-term cleanup calls in ready source: archive-invalid participant, guarded declare-defiance, clean-participant and cancel-participant.
These additions invoke only the narrow Council clear and leave the existing cleanup bodies otherwise unchanged against the immutable baseline.
Parent R2 fix covers normal final-settlement success through its distinct guarded normal finalizer.
An unresolved grading attempt reaches clean-participant, and a valid classified survivor reaches the normal finalizer.
Both paths clear live Council terms while retaining measured contribution and shared unresolved receipts.
No event edits are required or performed.

The following actual SHA-256 hashes identify the final reviewed source including both parent fixes and the corrected English obligation text.
Any further source change requires re-review of the affected path and replacement of its recorded hash.

## Final reviewed source hashes

| Source | SHA-256 |
| --- | --- |
| `common\decisions\012_africa_gods_decisions.txt` | `b39073b4370a8f7508ddc7902a6d9f4e5907942375313257fd063268a60fc6e8` |
| `common\scripted_effects\012_africa_gods_focus_payoff_effects.txt` | `26fa6867fb7a75a14e58f10660653fe5fd73cc8c7650ae8ffb0b64a935213e2f` |
| `common\scripted_triggers\012_africa_gods_focus_payoff_triggers.txt` | `23d5bfdf4e762b9dd390e5029d5168c7c7714f4922882aea0310d0c4aee31f23` |
| `common\scripted_effects\012_africa_gods_contribution_effects.txt` | `bc06a98c1a2582e7fc2d54c6db73958273141e816de17ae13f1872a95fc749e6` |
| `common\scripted_triggers\012_africa_gods_contribution_triggers.txt` | `539ed074652034d2dacdfff540102f74caca85b8be267e424e03ad420f8c01dd` |
| `common\scripted_effects\012_africa_gods_effects.txt` | `ae6bc014b3485b6cb9225c8d3ad95e3b6e3c25cc39b842a8e9a17660e7fbd0a8` |
| `localisation\english\012_africa_gods_l_english.yml` | `92cc1d8a367ebc4f158f427d5fb78f45de2c77b68a90763bddade597820dce08` |
| `common\scripted_localisation\012_africa_gods_scripted_localisation.txt` | `67fd4744b911e1b7c38a0c25e4063a1a521f7b6da534dd1519b34a2dd48e4b7b` |
| `common\scripted_effects\012_africa_gods_council_effects.txt` | `0b7db3b048c92bdf5fef8b482a6963558d0ca925db7f80bf4eba49e0558b1e05` |
| `common\scripted_triggers\012_africa_gods_council_triggers.txt` | `1c9266025c6f7b92e728ed35d9663256a020ac99ebae0a076c210e2aa82e0218` |
| `common\scripted_localisation\012_africa_gods_council_scripted_localisation.txt` | `aaabf0f0d54a7408cd251c50a43dac83585876f57742553e3152add3c6cf79ce` |
| `common\script_constants\012_africa_gods_constants.txt` | `be9f4d3cd489b86d6dca14b213d8d02fd48b42020228dd209f0f8098a14d563e` |
| `common\script_constants\012_africa_gods_contribution_constants.txt` | `0b4f0fc738321f0965f3279e0ef06252b77d38fde79ab02a526fa9a0e161ae6e` |
| `common\scripted_effects\012_africa_gods_settlement_effects.txt` | `888652459bd40d41491cb8995e48d46399a50a2c52d0d52db2348044db38170e` |

## Reviewer delivery and remaining work

Files changed by this reviewer: this handoff and the explicitly authorized `.tools\validation\test_012_gods_council_receipts.js`.
No gameplay helper, direct call site, constant, cleanup path, localisation file, event, other documentation, or Git state was changed by this reviewer.
The parent-added helpers, direct decision/wrapper consumers, constants retained, cleanup hooks, quoted-value wiring and exact unchanged receipt bodies are mapped above.
Meaningful validation consists of immutable baseline digest verification, bounded production-body comparison, and the actual-source receipt, quote and lifecycle case matrix.
The bounded model follow-up below adds actual production-helper execution under explicit injected native and external boundaries.
Native execution, cooldown expiry and engine stock-reader semantics were not tested or inferred.
Parent-owned MCP results and the probability auditor's named two-decision comparison remain required external evidence and are not replaced by this report.

R1's unconditional accounting-clear speech guard is corrected by parent and regression-covered.
R2's normal finalizer Council clear is also corrected by parent and source-assertion-covered.
Adjacent Council helper documentation is absent at the ready snapshot, as expected from the parent's explicit docs-next instruction.
The touched documentation should explain the accepted donor-loss policy and remove the conflicting old contribution-document sentence about supported zero or mismatch receipts becoming durable unresolved transactions.
No review fallback or simplification was used.
This handoff establishes source findings and source limits, not whole-event completion or native behavior.

## Authorized actual-source model follow-up

Command: `node .tools/validation/test_012_gods_council_receipts.js` from the mod root.
The file reuses `parse`, `namedBlock`, `assignment`, `constants`, and `hash` from `docs\plans\033_acid_rain_plans\validation\caller_repairs_source_tests_2026_10_03.js` without running that file's independent tests.
`.tools\validation\test_033_humanitarian_receipts.js` provided the source-execution and temporary-frame pattern.
No reusable generic runtime or secondary output artifact was created.

The model executes the actual Council initializer, payment owner, completion helper, clear helper, wrappers, speech debit path, response/quote/preflight triggers, shared native reader, begin, complete, recorder, work clear, identity guards and prospective accumulation guards.
Thirty-eight distinct production helpers and triggers execute in the infantry Council scenarios, including guarded armor capture helpers whose unrelated branch is inactive.
Actor and host scope objects and identity tokens are opaque objects, with arithmetic rejecting object references or nonfinite values.
Scoped normal variables and helper-local temporary frames use separate maps, following the supplied Event 033 pattern.
Source arithmetic is modeled to three decimal places for the current conservative accounting domain and does not establish HOI4 arithmetic precision or native type ranges.

Explicit injected native primitives: actor and receiver stock reads, specified send debit/gain observations, political-power reserve/debit, country flags, scoped variables and their arithmetic, native existence, war predicates, equipment affordability, and the fixture day.
History/world/opinion integration is external to this receipt test, so the model records the production history request and world-sync call without evaluating external reward or world-order systems.
External predicate boundaries are `participant_epoch_is_current`, `participant_generation_is_current`, `participant_host_is_active`, `contribution_history_is_proven`, and `contribution_contract_is_current`.
The ordinary-contract boundary is false in Council fixtures.
The actual receipt ownership, native floor, full/partial quantity measurement, outstanding balance, finalization, retry date, and prospective ledger math are never mocked.
The normal settlement finalizer is not replaced with a stub, and its R2 check is explicitly a production-source call-site assertion rather than an executed ordinary-settlement scenario.

Initial run: 10 executed cases passed and the no-current-terms unresolved-speech case failed, reproducing R1.
After the parent R1 correction: 12 executed cases pass and the normal-finalizer call-site assertion fails on R2, with process exit code 1.
Final run after the parent's explicit R1/R2-applied signal: all 13 checks pass, comprising 12 executed production-helper scenarios and the normal-finalizer production-source call-site assertion, with process exit code 0.
The source fixes were not made by this reviewer and no expectation or boundary was relaxed to obtain a passing result.
The twelve executed cases are full payment from 1,500 with exact host and one voice/history write, 700 then 300 with inclusive 800 second-step stock gate, zero credit with existing seven-day retry and speech switch, retry threshold at days 106/107, speech blocked after positive partial, both directions of unequal donor/receiver gain, opaque participant/host/origin/generation/epoch drift and wrong purpose/request rejection, false begin with missing sequence, unknown native quantity retaining pending/unresolved work without voice, cleanup retaining measured quantities and consumed sequence, prospective voluntary-subset accumulation failure retaining an unconsumed pending receipt, and unresolved native work blocking speech after live terms are absent.
Duplicate Council finalization, shared completion and recorder invocation execute the real production bodies and cannot repeat the debit, contribution, reserve or voice/history write.
The harness prints source hashes, each passing case, every failure, executed production identifiers and explicit limits to stdout and writes no files.
Verification-file SHA-256: `e945e30de770e88f6adfa85684e32db51f59dd2b06c40a2977e63fce57ac644a`.

No native engine, timed expiry, save/reload, ordinary tribute, armor or fuel gameplay proof is claimed.
Parent MCP and documentation work remain separate owners.

## Communication limit

The app thread-message route rejected a preliminary finding notification because the parent is this session's native ancestor.
No native collaboration messaging tool is exposed to this reviewer.
R1 is reported promptly in commentary and here for the parent to inspect.

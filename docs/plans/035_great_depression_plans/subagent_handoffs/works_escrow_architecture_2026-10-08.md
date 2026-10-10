# Event 035 works escrow architecture and implementation, 2026-10-08

Disposition: delivered isolated helper implementation, accepted U1 quantity policy, pending parent integration and native evidence.
Acceptance basis: the parent authorized only the three new escrow helper/documentation files and this handoff.
The parent subsequently explicitly accepted exact unused budget by monotone accepted controlled work, with conservative whole native units, no arbitrary salvage fraction, no mobilization anchor, and no retargeting of a missing payer.
That acceptance applies only to the exact matched paid Public Works escrow.
The parent owns SourceMain, mapper, selectors, refund/closure callbacks, CIV integration, UI/localisation, and final completion.

## Files changed and helper IDs

Only these four new files were authored:

- `common/scripted_effects/035_great_depression_works_escrow_effects.txt`
- `common/scripted_effects/035_great_depression_works_escrow_effects.md`
- `common/scripted_triggers/035_great_depression_works_escrow_triggers.txt`
- `docs/plans/035_great_depression_plans/subagent_handoffs/works_escrow_architecture_2026-10-08.md`

STATE effect IDs:

- `great_depression_works_escrow_prepare`
- `great_depression_works_escrow_bind`
- `great_depression_works_escrow_adopt_live_context`
- `great_depression_works_escrow_authorize_full_unused_return`
- `great_depression_works_escrow_measure_unused`
- `great_depression_works_escrow_settle`
- `great_depression_works_escrow_discard_preparation`

The ten STATE predicates are `integer_input_is_whole`, `quote_is_nonnegative_whole`, `can_prepare`, `can_bind`, `funding_is_coherent`, `request_matches_funding`, `project_matches_funding`, `payer_can_receive`, `can_settle`, and `no_material_return_due`, all under the `great_depression_works_escrow_` prefix.
The matching markdown documents scopes, inputs, outputs, defaults, side effects, units, examples, call-site ordering, references, and remaining work.
No parent source, mapper, selector, test file, script constant, Git index, workbook, asset, or old handoff was edited.

## Helper map and exact funding contract

Prepare runs on the exact STATE under the actual paying COUNTRY ROOT after the existing PW need preparation, before the real debit.
It requires current eligible actor, exact current center registration and site, ownership/control, an open project slot, and all four nonnegative whole quote variables.
It snapshots gross manpower/fuel/train/CIV quotes, original payer and site as actual scope pointers, original episode, preparation day, prior authorization, and next expected action count.
An absent first-action counter is the sole permitted zero default, under trusted actor preflight.
It is not written to the country by this sidecar.
No material quote or funded identity defaults to zero.

Bind runs after the actual existing debit, authorization, and paid PW binding.
It requires the original preparation, exact payer/site/episode, fresh positive actual action count/day, newer whole authorization, unchanged quotes, coherent immutable required work, and existing unspent PW payment proof.
It creates an open state funding row and clears stale policy and retirement permission from prior funding.
The original capture fields remain as a second immutable witness for the funding identity and gross amounts.
A duplicate prepare/bind cannot overwrite outstanding funding.

The parent then sets the exact state request tuple and calls the U1 authorization helper once after successful funding capture.
Funding also freezes an initially identical live owner/episode mirror.
The guarded `adopt_live_context` helper changes only that live mirror after the parent's actual matching adoption receipt, prior live episode, and payer/site/auth/action/duration proof.
It does not migrate CIV, refund materials, choose a successor, or change original funding provenance.
Measure/settle compare the shared project and paid-plan live episode/owner with that mirror, preventing later unrelated same-serial projects from borrowing the old budget.
It verifies the funded tuple and current paid PW payer/action witness before setting the private full-unused permission.
The sidecar never executes a second payment.

Measure compares the request with the immutable funded site, original payer, original episode, authorization, and positive paid-action count.
ROOT must be that original payer or the actual existing live PW owner that owns the state.
It also requires the still-present paid-plan payer/site/auth/action fields, PW project type, matching required work, and an actual nonnegative whole controlled-work counter.
That gate rejects type, slot, scope, receipt, count, duration, and actor near misses.
A successor supplies the original funded episode, not its new live national episode.

Used work is a bounded monotone high-water measurement of the existing authenticated controlled-work counter.
Unused quantities are exact conservative whole units.
No world or state registry scan, RNG, paid-action shop, field-of-view callback, or balance redesign is introduced.

## Arithmetic and tuning

For gross G, required work R and monotone bounded used work W:

`unused = floor(G * (R-W) / R)`

`used = G-unused`

The code avoids G times days by quotient/remainder decomposition.
Its large component and final output stay bounded by G, and the small remainder product is below R squared.
The existing accepted maximum R is 245, so the tail product is below 60,025.
All actual division results are integral after modulo subtraction.
This avoids over-refunding fractional trains and avoids claiming later clamps repair an overflowing earlier multiplication.

No new tuning constant was added or requested for this accepted policy.
The helpers reuse `great_depression_api.zero`, `great_depression_api.one`, `great_depression_center_project.public_works`, and `great_depression_project_duration.maximum_work_days`.
There is no artificial material or receipt maximum gate in source.
The test adapter uses a conservative signed-32-bit integer-part bound and five-decimal downward quantization as an explicit model, not a claimed universal engine maximum.
Installed math-expression fixed point and offline normal-variable precision remain distinct evidence.

Material-progress consumption is an accepted budget abstraction.
The engine already debits the materials upfront and does not expose a physical reservation/burn registry for these projects.
The helper cannot prove which actual workers, fuel batches, or concrete train versions were physically unspent.
At work zero, a valid authorized retirement can return the full proved unused material budget.
At completed work, unused is zero.
The used portion is never refunded.
No additional mobilization or salvage fraction is invented.

## One-shot settlement, authority, and cleanup

Funding authorization alone does not permit a return during an ordinary active project.
An exact parent-authorized retirement callback must also set `great_depression_works_escrow_retirement_requested`.
The flag is cleared by every new funding and never set by this sidecar.
An old completed/failed raw authorization serial alone cannot substitute for that permission, because serials can restart in later episodes.

The parent must stop/retire that exact shared authorization as part of the terminal transaction while keeping its identity/work fields available for settlement.
Otherwise a refunded parent project could continue awarding output, which this isolated sidecar cannot prevent without the parent-owned integration.
Do not wire settlement as a general active-project decision.

Settle snapshots the original payer, state, episode, authorization, action count, measured work, quantities, and day before entering any country scope.
It consumes only the matched open funding row before emitting native credit commands.
The COUNTRY target is the stored original payer, never arbitrary ROOT or an adopter.
Within that country, PREV is the funding STATE and ROOT remains the caller.
Positive manpower, fuel, and train quantities use the same resource families as the existing debit.
There is no political power, cash, unrelated equipment, building, or slot compensation.

A nonzero return requires the matched U1 permission and an existing eligible original payer.
Vanished, noncivilian, special, or actual-nonhuman payers leave nonzero liability open and pending.
Missing/undefined funding fields reject without fabricating zero settlement.
No successor retarget or forfeiture is introduced.
Fully consumed zero-unused funding may close without entering a dead payer scope.

Every attempt clears only the fresh output flag and fresh quote-readiness output.
Only a newly consumed matching row sets `fresh_settlement`.
Durable settlement fields and the settled receipt survive repeats and mismatches.
A repeated attempt cannot refund twice, undo an already consumed receipt, or change another row's durable settlement.
The parent must read fresh versus already-used acknowledgment before clearing project data.

Prepare/bind inputs and all public outputs use normal STATE variables.
Integer-predicate temporary storage is internal and consumed before return.
No scoped temporary or surviving temp-output assumption is used.
No new global event target is needed.
Persistent payer/site pointers remain separate from all integer counters.

## Golden actual-source proof row

The fixture executed the real current payment and authorization helpers, then the sidecar helpers.
The shared processor accrued 48 actual controlled work days.
The authorized retirement was a declared parent callback input.

| Frozen field | Observed fixture value |
| --- | --- |
| Original funded episode | 35 |
| Authorization and paid action count | 1, 1 |
| Funding day | 300 |
| Payer / site representation | COUNTRY Scope / STATE Scope, not numeric ID aliases |
| Required / controlled work | 145 / 48 |
| Gross manpower / fuel / trains | 13 / 11 / 7 |
| Issued unused manpower / fuel / trains | 8 / 7 / 4 |
| Used budget | 5 / 4 / 3 |
| Frozen CIV quote | 2 |
| Later overwritten country CIV quote | 44 |
| Native fixture recipient | Original AAA country only |

The fixture logged exactly original-payer native credits of manpower 8, fuel 7, and train_equipment 4.
This is actual-source execution with declared native fixtures, not a observed in-game refund.

## CIV proposal, not implemented

The state row freezes the funded CIV quote independently of the shared last-action field.
That snapshot alone is not an implemented reservation, refund, or CIV closure.

The parent needs a dedicated bounded list of funded state pointers under each live CIV obligor.
Each row must have exact state/funding identity, original material payer, live CIV obligor, active/suspended/retired disposition, and a one-shot obligation-transfer acknowledgment.
Aggregate only valid live obligation rows using existing bounded center/funded-state arrays.
Keep material liabilities pending when the payer disappears rather than scanning the world or discarding rows during actor cleanup.

The successor acceptance gate must check usable free CIV after unrelated existing obligations, exclude the exact row being migrated from double-counting, and use one inclusive quote for display and affordability.
Old and new obligor equality is a no-op transfer rather than two debits.
Remove the old obligation and add the new one once under the same acknowledged row.
Materials, gross budget, original payer, original funded episode, authorization, required work and consumed work do not reset.

The parent owns CIV-term modifiers, active caps, pause/release policy, exact availability, recovery closure and once-only legacy integration.
No shared CIV variable or modifier was changed.
No capacity rebalance or new slot policy was chosen.

## Parent migration and call-site plan

1. After existing need preparation, prepare escrow and check its positive prepared output before payment.
2. Execute the existing actual affordability/debit/authorization/PW paid binding, then escrow bind.
3. Set the immutable request tuple and call U1 authorization only after successful capture.
4. Measure accepted controlled work in the parent's real processor, with exact receipt identity and before any terminal field clearing.
After actual transfer adoption, call the escrow live-context helper before successor work/settlement, preserving the original funded request tuple.
5. On exact authorized failure/cancellation/recovery/success retirement, stop future work, set retirement intent, settle, and consume the fresh or matching historical acknowledgment.
6. Clear project/selection/temporary data only after settlement acknowledgment while retaining funding history and any pending state rows.
7. Add the new files and the documented primitive arithmetic adapter to the parent's production-source test loader.
8. Integrate the separate CIV row/transfer gate and the independently owned lasting-capacity prerequisite/closing transaction.

Binding failure after a possible real debit must retain the preparation for exact pending recovery.
It must not call unpaid discard or invent a generic refund.
The sidecar intentionally has no shared call-site edits because the parent explicitly requested isolated review before local wiring.
This is requested scaffolding, not an unused-helper cleanup refactor.

## Meaningful validation run

The existing `.tools/test_event035_public_works.py`, BankRuntime, report runtime and center-project runtime were read.
Tests loaded the newly authored source definitions into that existing source interpreter.
No production helper was stubbed or replaced.
Only the newly required native modulo/divide primitives received explicit bounded fixed-point fixtures.
The sole undefined-counter reader accommodation was the existing first-action zero convention.
All scope pointers used real Scope objects, and an integer site alias was rejected.

Passed source scenarios included:

- First action with absent counter, prepare without debit, reject prepayment bind, actual paid bind, duplicate capture/settlement, preserved historical acknowledgment.
- Work zero full-unused return, partial monotone use, decreasing counter without increased refund, completed work zero return, no return without retirement permission.
- Wrong caller, site, payer, episode, authorization, action count, project type, fractional work, missing payer field, numeric site alias.
- Pending nonzero liability for policy omission or vanished payer, no successor return.
- Transfer to a different live episode with original payer and funding episode preserved.
- Fractional/negative/missing quotes, fractional counters/authorization, occupied project slot, stale paid action/day, changed quote, bad type.
- Every work-day boundary for two gross tuples, including large quantities near the explicit conservative test bound, with whole-unit conservation.
- Corrupted gross capture, changed/zero required work and missing work reject without credit.
- Golden 145/48 controlled-work row and retained CIV quote after another action overwrites the country quote.
- An old terminal serial without the private current-row retirement permission cannot refund.
- An unrelated later same-serial live episode cannot borrow old funding, and an absent actual adoption receipt cannot rebind its live context.
- An undefined paid-day field at day zero cannot be mistaken for a real zero-valued payment witness.

The initial grouped source tests passed 17 transaction scenarios and 306 preparation/binding/arithmetic scenarios.
Additional capture-integrity and retirement/golden probes passed.
These are scenario counts, not a claim of 323 independently named unittest methods.
The parent still needs committed production tests for the integrated callbacks, actual CIV bookkeeping, interrupted bind recovery, and no continuation after refunded retirement.

Final native MCP checks returned `SCRIPT_CHECK_PARTIAL` for both new script files.
Effects: 185 checked commands, zero unresolved commands, 108 unchecked argument blocks.
Triggers: 210 checked commands, zero unresolved commands, 86 unchecked argument blocks.
Both return `valid = null`, `parametersChecked = false`, with checks limited to syntax, command kind, declared scope and event popup checks.
No native parameter or execution pass is claimed.

## Reference evidence, source IDs, and coverage

Confirmed routes used: `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, and `hoi4.script_validate`.
The calls returned no artifact URIs, so exact section IDs, paths, spans, revisions and source hashes are the retained references.
No native task/job/helper-expansion route was used, and no server/task capability beyond successful called routes is inferred.

| Source | Span / section ID | Revision |
| --- | --- | --- |
| Installed effects add_manpower | 1468-1476 / `138ba70b49b5d445953f7b2260dfddb40cc17cb93664857074e981c4e5437970` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed effects add_fuel | 1388-1396 / `9a38fef4fd297bda88b1913a061ca9adcdc93c44c5c4482f35ad25d33398c16e` | Same effects revision |
| Installed effects stockpile | 1252-1266 / `e91bc28e05be536f65f989ff9b2598c1fc4a48eee032786777d9cdf538931844` | Same effects revision |
| Installed effects modulo | 4999-5011 / `9bd86d91cefb1a3f326f23d884b2834244f61cda9ba7641168102cc26a33eddc` | Same effects revision |
| Installed effects divide | 3609-3615 / `ee14828a2febe0b7c94ab901a92dff3c200ae0f07fc3855f048f019a83870395` | Same effects revision |
| Installed effects rounding | 6486-6495 / `f4e6722423e143fa9456f7c8b0de186604e781e47b268495209623da7e1b089b` | Same effects revision |
| Offline Data structures operations/types | 571, 572, 573, 435-443 / `44c26803d1a55cd69ea7e2d99211abe7f8093760f374e0c0706e5ff41e8a0dbc`, `857e74de57348f47bc5a5855525e08236396e069fac4898da588fbddb1177e6b`, `3165fd513548c2ad7b040f81615f9ab74ac72eed953284461ab5a4a9cb75d761`, `93a8a69289bba58764f83d5e14f30b8ecd53bf302360aa6db24d21dcb7c17578` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Installed Script Constants concept/schema | 216-222 and 1-34 / `c859ab9d6a857bfc830f89b36b004514b78ee454e001a80238a9d1f7b355ccd0`, `48deec564822a81f6806514736148c344258acac56db7e9989998ed30dd26b68` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

The installed files are under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation`, plus `common\script_constants\documentation.md`.
Offline pages are under this mod's `paradox_wiki`.
Additional relevant sections read directly are offline Scopes 811-833, normal-variable precision 425-434, installed math-expression concept 184-215, installed decision scope documentation 1-34, and installed modulo-temp effect/trigger documentation 4986-4998 and 6442-6454.
Native `common\scripted_effects\GRE_scripted_effects.txt:193-198` supplies an explicit divide-variable example.

Exact source lookup of `great_depression_pay_action_cost` returned helper revision `20b47f810126de7f8e98485f9827744778755b10b50c7f6039d79c095a8ad9ef`.
It agrees with the local authoritative Public Works debit at `035_great_depression_effects.txt:491-538,607-619`.
Lookup of the escrow settle helper returned revision `cd47f53947fc6788315315f56048fd5794a117b008fbb76b2ed05ea9e2da75bb` for its earlier pre-retirement-gate shape.
Final lookup returned revision `e690c8446953056787c89d3ab475b77eed32b283dbfce3f18c7cc4f7a5459f43`, with one complete indexed definition at lines 173-216 and a bounded source read at lines 173-182.
Final bytes are identified below and final checker coverage is reported separately.
Reference read outside the one-line modulo section was rejected and corrected with the exact line.
The initial context omitted Localisation and indexed `script_doc` sources are absent.
These non-visible helper changes introduce no localisation/GUI consumer, and presentation remains parent-owned.

## Remaining integration, unsupported analysis, and limits

Delivered: reusable state funding, exact quote/payment witness capture, matched U1 authorization, conservative work accounting, one-shot original-payer native return emission, pending missing-payer liability, fresh/historical receipts, docs and reviewable CIV proposal.

Pending parent integration: shared call sites, terminal authorization retirement before credit, exact payment/binding failure recovery, dedicated bounded CIV rows and affordability/transfer gate, cleanup retention, integrated tests, and lasting-capacity closing semantics.
The Reopened-only legacy prerequisite is separately parent-owned and was not patched or treated as escrow success.

Native limits: source policy models material consumption by accepted work rather than physical reservation, fixed-point behavior remains a declared test assumption, native refund receipt may be affected by fuel capacity, manpower mobilization semantics and train archetype/producer/version selection.
The helper snapshot records credit instructions offered, not an observed engine delta.
No invented compensation or numerical maximum resolves those limits.

Skipped: HOI4 launch/live tests, save/reload, broad map scan, event rerender, AI/probability audit, Git and shared source edits, workbook/asset work, because they are outside this bounded assignment or explicitly prohibited.
No gameplay simplification or unapproved fallback was used.
The isolated scaffold was expressly requested, so pending integration is explicit scope rather than claimed complete behavior.
No whole Event 35 claim is made.
Skills used: chaos-redux-events, chaos-redux-decisions-missions, chaos-redux-subagents.
Skills created/updated: none.

## Final source identities

- Escrow effects SHA-256: `5f43f6c8644cabdf74580ef5b1980c40d278235b9b9ebc458523c9b60212fd2c`.
- Escrow triggers SHA-256: `b8da096791d5557c61b9ed8b79ce9f585f748bde432f66882065d8d9856703d2`.
- Escrow markdown SHA-256: `ffc65794dc5d48d55e630ef870b069b53a4a5c01483b91e863067e6db6feea2b`.
- Reviewed unchanged main effects SHA-256: `235c9a3775913c41dea22940a0ab4fcec7bb23d887d524256231e8bbf9c563a3`.
- Reviewed parent-owned mapper SHA-256: `2919e0882eea6edf59183b4cdd79d757378d165fa7c4e1b1a3c774b2131f178d`.

## Independent parent-integration review, 2026-10-09

Disposition: review delivered, three concrete integration defects remain for the parent to fix.
Acceptance basis: the parent requested a read-only review of the current MATERIAL escrow integration, with evidence appended only to this existing handoff.
The accepted U1 policy still returns the complete unused budget and never the used portion.
This review changes no gameplay, tests, constants, GUI, assets, workbook, or Git state.
The earlier isolated-helper results and hashes above remain historical evidence.

### Findings requiring source changes

1. **Failure can clear another country's paid plan even though escrow rejects the caller.**
At `common/scripted_effects/035_great_depression_effects.txt:827-846`, failure accepts the shared registration and authorization predicate, publishes a failed receipt, calls escrow, and then clears the paid plan without checking retirement acknowledgment or the exact live owner.
The shared predicate at `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt:821-839` proves registration, episode, and an unspent serial, but does not bind the caller to the paid-plan owner.
An actual-source probe created an unrelated existing country with the same episode and registry inputs, then invoked the real failure callback on the funded state.
Escrow correctly issued no credit, but the callback removed the actual paid plan, recorded a failure against the unrelated country, and left the original funding open without a retirement record.
The parent should validate the exact current project owner and funding context before any failure mutation, while preserving the intended old-owner interruption behavior for an open transfer.
Calling escrow first is insufficient if the caller subsequently clears the record after escrow rejects it.

2. **Failure and registered cleanup erase recovery evidence when retirement rejects a mismatch.**
At `035_great_depression_effects.txt:844-846` and `:3251-3286`, destructive clearing proceeds regardless of whether `great_depression_works_escrow_capture_retirement` froze the funded tuple.
An actual-source probe changed only the paid-action count after genuine payment, then separately exercised real failure and real registered cleanup.
Both paths emitted no refund, left `great_depression_works_escrow_open`, set neither `retired` nor `pending_return`, and deleted the paid-action witness.
The country recovery queue retained the state but could never freeze retirement after those fields were cleared, so this is stranded liability rather than the supported missing-payer pending case.
The parent should preserve the rejected transaction's exact identity and work evidence until a matched retirement is acknowledged, with a distinct retained recovery state for a rejected retirement.
Do not reconstruct a funding tuple or manufacture a refund from the mismatched live fields.
Valid retirement with an unavailable payer is different and works: its already frozen tuple survives project clearing and can settle later.

3. **A stale prepared flag permits a real debit without a successful escrow bind.**
At `common/scripted_effects/035_great_depression_decision_effects.txt:790-806`, payment tests preparation flag presence rather than proving that this invocation prepared the current site, payer, episode, day, expected payment count, previous authorization, and quotes.
The actual-source reproduction runs the real need preparation and real escrow preparation without payment, advances one day, and invokes the real launch helper.
The new need plan is prepared, escrow preparation refuses to overwrite the retained older preparation, and the old preparation flag still satisfies the launch gate.
The launch emits three real fixture resource debits and activates a paid PW plan, but escrow bind rejects the old preparation day.
The observed result is `prepared = true`, no open funding, no payer queue row, and an active paid receipt.
The parent should require an exact current preparation before debit and explicitly retain/recover any payment for which binding fails.
The current preservation of preparation fields alone does not provide post-debit recovery or stop an unbound paid project from progressing.

### Documentation and validation gaps

The helper markdown remains the original isolated-scaffold document despite parent integration.
Its public map omits `capture_retirement`, `prepare_request`, `retire_and_settle`, `process_retired_sites`, and `retired_matches_funding`.
At `common/scripted_effects/035_great_depression_works_escrow_effects.md:136` it says this sidecar never sets retirement intent, but the current capture helper sets it at effect line 289.
At markdown line 188 it says there are no shared call-site edits, despite the reviewed launch, binding, processing, adoption, failure, completion, cleanup, reset, and event receiver calls.
The parent should update that existing document with the frozen retirement fields, queue lifetime, current call-site ownership, and rejection/recovery ordering.
No additional report or helper documentation file is needed.

The actual loader is `Event35Runtime`, extended by `ReportRuntime` and `BankRuntime`.
It loads both new escrow files and executes the real production payment, mapper, authorization, retirement, refund, and cleanup helpers.
No escrow production helper was replaced or stubbed for this review.
Its `for_each_scope_loop` implementation at `.tools/test_event035_center_projects.py:752-762` discards the `break` argument and traverses every fixture element.
Therefore the added test that seeds break variables proves queue retention and recovery under the current fixture, but does not prove resistance to an inherited native break value.
The source correctly supplies two distinct reset private break variables, which is direct source evidence under installed effects lines 4279-4311.
Its arithmetic at runtime lines 655-672 uses ordinary Python arithmetic and division, with no fixed-point quantization or bounded intermediate check.
The eight maintained tests therefore do not establish the helper markdown's separately declared conservative numeric model.
The quotient/remainder source still avoids gross quantity times work and keeps the small product below the squared duration bound, but native arithmetic and material-delivery semantics remain unproven.

### Meaningful checks and outcomes

The final maintained suite ran with `python -B -m unittest discover -s .tools -p test_event035_works_escrow.py -v` and passed all eight methods after the parent supplied the successor's real initialization values.
The earlier transfer run failed in generic severity comparison after material retirement and credit, because the successor fixture lacked peak-severity data.
The parent corrected the native fixture, and the corrected transfer test passed without a production helper stub.

Eight bounded actual-source probe groups were run through the existing runtime with native data fixtures only:

- Five request near misses covering site, payer, funded episode, authorization, and paid-action count, plus an early direct settlement, all emitted zero credit and preserved open funding.
- An unrelated caller with matching episode and copied registration data reproduced finding 1.
- Paid-action mismatch in failure and registered cleanup reproduced finding 2, including the retained but unpayable queue row.
- Invalid project type during actual adoption left the escrow live owner unchanged even though the parent published its adoption receipt, demonstrating that the escrow adoption shape guard rejects the altered project.
- Next-day unpaid preparation followed by real launch reproduced finding 3.
- Missing payer at registered cleanup froze a pending retirement, preserved it after active fields were cleared, and credited the restored original country exactly once through the real country queue.
- A mixed queue retained one pending and one active own row and ignored an open row assigned to another payer without changing that other row.
The initial mixed-row fixture copied the country object, which was not a valid identity fixture for this runtime's equality operation.
The corrected native fixture preserved the original country object and passed, with loop-break behavior explicitly unmodelled.
- Failure followed by a genuinely new paid authorization cleared old retirement permission, and a direct retirement/settlement attempt on the new active authorization issued zero credit.

Existing maintained tests also prove zero material credit for completed work, exact partial unused return, no output continuation after valid failed retirement, repeated-callback one-shot behavior, original-payer credit after transfer, and restoration of pending liability after payer disappearance.
Events `chaosx.nr35.7` and `.8` call the country recovery helper before other receiver work, and episode reset calls it before clearing episode controls.
Those call sites were reviewed directly, not executed as a native event scheduler.
The retirement record permits recovery after paid-plan clearing and does not by itself depend on a later country's active episode.

### References, tool limits, and source identities

The connected list exposes the four reference routes and script validation.
No fresh MCP source-check request was issued because the parent identified the underlying source capability as already exhausted and supplied the previous partial checker evidence.
The historical checker results remain partial with `valid = null` and unchecked argument blocks, not a native pass.
Only a capability or input change that addresses the exhausted analysis would justify another request.
Relevant local reference sections were read directly for this review, with no Paradox wiki web access.

| Local source | Read span | SHA-256 revision |
| --- | --- | --- |
| Installed `documentation/effects_documentation.md` | 3609-3615, 4279-4311, 4986-5011 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Installed `documentation/triggers_documentation.md` | 2110-2134, 6442-6454, 7561-7568 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Installed `documentation/script_concept_documentation.md` | 184-222 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Installed `common/script_constants/documentation.md` | 1-34 | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 425-443, 1216-1256 | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 811-834 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Vanilla `common/scripted_effects/GRE_scripted_effects.txt` | 193-199 | `f32ed7b16b485e67ddda2abf8e0ec28c469391e8111a7a3e3036cc02e99675c3` |

Installed paths are below `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Reviewed mod paths are below `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Hashes identify the reviewed bytes, rather than claiming the shared checkout will remain unchanged after this review.

| Reviewed source | SHA-256 |
| --- | --- |
| Escrow effects | `d1afd6859aff8ff80b86076cd19b6ed183c121c085b99ddce40989ed6c93f4ef` |
| Escrow triggers | `fe0b0a2c530cc282bcadfcfc85a5cf059e84af516d28c5f74109e0d1edb93041` |
| Escrow markdown | `ffc65794dc5d48d55e630ef870b069b53a4a5c01483b91e863067e6db6feea2b` |
| Main effects | `a3c46390c896086827afb6c408113118ac1bf0e1f58cf7a08fc6d753d4d62da7` |
| Decision effects | `1bf70a71ddd37a68cab2197888d1e6812d28e7e331b4b6f1b2fa692064c11b27` |
| Public Works effects | `4c09d94e0ba66ab1f4dc07cd728fe418763fc86f6b890fef1436c629c4ed3a8c` |
| Decision surface triggers | `b8e69b3f9196ea8bdbee08c6885792a07222ae1ed14cc9c9dd6e81b3100b6369` |
| Event receivers | `fa50db6901890eed07f9ae74fee58d7c1d56c96117cc67ce904e7d7503fc3897` |
| Final eight-method escrow test file | `cfa338ac14f076d92b2fea8db143ddc84b3d7d75a8cdd85d3785304c97c4b551` |
| Base production-source runtime | `b1bc57bd30e6ec2110d486b1eeadf93076d680cabaa53cd55a80fc99d2794c9a` |

### Completion and remaining work

Completed: bounded independent source review, eight actual-source probe groups, corrected eight-method suite, and this appended evidence.
Only this handoff was changed by the reviewer.
Source fixes, matching regression coverage, and helper-documentation updates remain parent-owned and are required before the MATERIAL integration is claimed closed.
CIV reservation aggregation and migration, along with lasting physical closure, remain unimplemented and are not approved or closed by these material results.
No CIV policy, helper phase, new gameplay design, weighted behavior, asset work, or Git operation was selected.
No gameplay simplification was introduced.
No live-engine, timed-event, save, physical resource provenance, or native capacity outcome is claimed.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
Skills created or updated: none.


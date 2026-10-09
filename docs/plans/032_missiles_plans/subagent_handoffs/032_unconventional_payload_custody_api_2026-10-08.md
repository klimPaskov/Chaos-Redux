# Event 032 unconventional payload custody API handoff

Date: 2026-10-08.
Disposition: `unresolved` API proposal with source-confirmed defects and explicit native-evidence blockers.
Acceptance basis for the required behavior: the parent assignment authorizes implementing the accepted Event 032 specification package with no simplifications, physical custody throughout lifecycle changes, and separate Event 023 and Event 076 ownership.
This handoff does not independently accept new mechanic design or certify implementation.
Only this previously absent document was created.
No gameplay, localisation, assets, helper definitions, Git index/history, or other documents were changed.

## Implementation decision

Keep the committed chemical API unchanged as the chemical owner and add narrow nuclear and biological owner receipt endpoints behind the existing Event 032 payload adapter.
Do not generalize `cbrn_reserve_action_payload` by accepting another payload ID.
Its authorization, model resolver, stock reader, profile locks and receipt metadata are chemical-specific, and its native wrappers explicitly accept only four chemical models.
Its underlying measured stock primitive observes concrete-model totals without producer or variant identity.
An exact nuclear or biological implementation therefore cannot be obtained merely by removing that whitelist.
The chemical receipt lifecycle is a useful structural precedent, with its remaining native identity limits retained as limits.

The smallest justified extension is two owner APIs for this existing feature, an Event 023 allocation adapter for represented Soviet-origin cohorts, and direct lifecycle calls at the existing Event 032 boundaries.
No central router, provider registry, new GUI, balance model, production system, new equipment family, or replacement Event 023/076 gameplay is proposed.
The parent retains survey/refund/recovery implementation ownership.
The transaction requirements below tell that work which receipt must survive and when it may close.
Preserve commits `5793df434` and `21e812c8e`, including all existing payload-change and evolution notifications.

## Source-confirmed findings

All line references are to the inspected checkout, not immutable engine execution evidence.
`common/scripted_effects/032_missiles_operations_effects.txt` is abbreviated as `operations` below.

1. `operations:4194-4236` accepts an already-active escrow without matching operation nonce, exact site, actor or current payload binding.
Nuclear and thermonuclear preparation use the same `num_of_nukes` pool and stamp the requested amount after an unmeasured debit.
Biological preparation freezes only the agent and nominal quantity after a debit whose success proof is assigned immediately after the stock command.
2. `operations:4239-4265` unconditionally restores nominal native stock for an active nuclear/biological escrow and clears it.
It does not inspect capture, destroyed-site disposition, current custodian, actual refundable balance, producer/variant identity or measured credit.
The chemical call in the same function already has a distinct physical settlement contract.
3. `operations:4314-4358` validates active escrow only by payload type, then clears it.
When escrow is absent it can buy fresh biological or nuclear stock at resolution.
Remove these replacement-debit branches for prepared operations.
A lost or mismatched receipt must not turn another country's or another site's free stock into the original payload.
4. `common/scripted_triggers/032_missiles_operations_triggers.txt:259-299` requires a paid receipt only for chemical preparations.
The nuclear/biological custody gates at `438-501` establish integration flags and a typed site marker, not a counted, nonce-bound physical holding.
Extend preparation and commitment validation to the exact owner receipt without requiring a second free unit.
5. `operations:4466-4494` dispatches biological consequences using mutable `missiles_selected_biological_agent`.
Use the consumed receipt's frozen agent, model and measured quantity instead.
The amount held for one agent cannot authorize a different selected agent.
6. `operations:4502-4557` issues `launch_nuke` with `use_nuke = no`, then immediately claims completed delivery and special-use history.
That command is appropriate only after a proven native preparation debit, but invocation alone is not callback-confirmed release.
`operations:6085-6120` consumes before guidance and interception, so consumption and actual release must remain separate outputs.
An intercepted payload can be expended without confirmed use.
7. `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:91-162,164-243` books native shortfalls as expenditure before reconciliation.
With one operational Event 023 device and one native bomb, Event 032 preparation removes the native bomb, and the next owner refresh can move the operational device to expended.
Cancellation then restores the native bomb while the Event 023 expenditure remains.
Its existing reserve/release functions at `509-676` move ledger buckets without removing native stock and require Event 023's action context.
Its commit at `682-786` and native confirmation at `1099-1130` have their own action and callback contract.
They are not directly callable Event 032 missile APIs.
8. Capture at `operations:6470-6629`, integration at `6708-6747`, and removal at `7047-7078` explicitly settle chemical holdings, while nuclear/biological holdings pass through generic operation cleanup and nominal return.
The planned inheritance path at `6324-6421` skips the ordinary control-change handler and aborts before transferring site ownership.
The split preflight at `6823-6868` similarly aborts before assigning child states.
Neither path supplies a nuclear/biological receipt migration contract.
The bounded literal source scan of `common` and `events` found definitions but no direct caller of `missiles_prepare_planned_inheritance` or `missiles_transfer_inherited_site`.
This does not rule out constructed meta calls, so Event 005/006 explicit inheritance integration remains unproven and needs a direct call-chain check by the parent.
9. `common/scripted_effects/biological_facility_capture_effects.txt:106-195` snapshots and removes free national biological equipment into its facility ledger.
It cannot see equipment already held for Event 032 at a different missile site.
Its recovery at `211-265` and transfer at `337-388` restore aggregate agent-model quantities with `producer = THIS`, without preserving the removed producer/variant or measuring the credit.
Calling these helpers for a missile-site hold would assign the wrong physical location and could debit unrelated free stock.
Do not place missile holds into that facility ledger or mark a missile state as a biological facility to obtain recovery UI.
10. Shared nuclear consequence selection in `common/scripted_effects/chaos_meter_effects.txt:3381-3405,5955-5965` uses researched thermonuclear technology unless the atomic-delivery context is present.
An explicit atomic Event 032 launch by a thermonuclear-capable country currently lacks the Event 023 atomic context used to preserve atomic consequences.
The owner must consume an exact receipt-bound yield profile at the native callback, without overwriting an unrelated Event 023 pending action.

## Proposed helper map and calling convention

These are concrete proposed names, not existing definitions.
Implement them as narrow owner additions, with common responsibilities documented once, rather than building a new generic dispatch system.
All effects are zero-argument `= yes` calls using documented scoped input variables and flags.
Named scripted-effect argument blocks and `$PARAMETER$` substitution are not a supported API.

| Responsibility | Nuclear owner endpoint | Biological owner endpoint | Scope and result |
| --- | --- | --- | --- |
| Prepare and measure debit | `nuclear_payload_reserve_for_operation` | `bio_payload_reserve_for_operation` | Actual payer COUNTRY, actor-rooted authorization, durable handle and observed holding |
| Validate exact paid holding | `nuclear_payload_validate_operation_hold` | `bio_payload_validate_operation_hold` | Actual holder COUNTRY, independent validation result, no stock mutation |
| Release from local custody into launched expenditure | `nuclear_payload_consume_operation_hold` | `bio_payload_consume_operation_hold` | Actual authorized actor COUNTRY, fresh once-only consumption acknowledgement and frozen identity |
| Recover to usable stock | `nuclear_payload_recover_operation_hold` | `bio_payload_recover_operation_hold` | Actual current holder COUNTRY, exact state and recovery proof, measured credit and persistent remainder |
| Transfer sealed custody | `nuclear_payload_transfer_operation_hold` | `bio_payload_transfer_operation_hold` | Actual former holder COUNTRY, explicit receiving COUNTRY, linked sealed handle, no stock grant |
| Integrate a captured hold | `nuclear_payload_integrate_captured_hold` | `bio_payload_integrate_captured_hold` | Current holder COUNTRY, exact control, owner capability and recovery proof, measured usable-stock credit |
| Destroy or retain inaccessible custody | `nuclear_payload_settle_site_holds` | `bio_payload_settle_site_holds` | Explicit holder COUNTRY and exact STATE input, disposition-specific acknowledgement, persistent unresolved records |

Reuse `missiles_reserve_operation_payload`, `missiles_release_operation_payload` and `missiles_consume_special_payload` as the bounded Event 032 call sites.
Add `missiles_check_unconventional_receipt_for_commit` and `missiles_settle_unconventional_payloads_at_site` to `032_missiles_payload_receipt_effects.txt` only for these already-existing families.
The latter must preserve the chemical exact-site call and supply each owner the same physical disposition.
Retain existing chemical names for callers rather than renaming committed plumbing.

For each owner, normal COUNTRY request fields are `<owner>_request_consumer`, `_nonce`, `_actor`, `_site`, `_site_id`, `_target`, `_target_id`, `_weapon` or `_agent`, `_quantity`, and `_handle` on follow-up calls.
Transfer also supplies `_recipient` and the exact site transfer/capture generation.
Nuclear tracked-origin requests carry `_allocation_owner`, `_allocation_source_state`, `_allocation_source_bucket` and `_allocation_receipt` issued by Event 023.
Biological requests need the concrete equipment model and the proven producer/variant identity of the actually removed stock.
An opaque native aggregate must be labelled as such rather than manufactured into a producer-specific receipt.

Freeze original payer/actor, origin receipt, original allocation source, current holder, actual custody state, target, consumer, nonce, model/profile, required amount and measured observations before payment or nested dispatch.
Store the originating country's generation/ledger-owner identity so copied civil-war variables do not become valid receipts on the child.
Keep a state mirror binding the current holder and handle to the physical source site.
Store holder-local open handles for bounded exact-site settlement, with back-links across transfers.
The original actor/nonce stays historical after capture, while only the current holder may settle the linked receipt.

Normal COUNTRY outputs are `<owner>_result`, `_result_amount`, `_handle`, `_validation_result`, `_consumed_quantity`, `_consumed_model`, `_consumed_agent` or `_consumed_weapon`, `_transferred_handle`, and `_closure_ack`.
Default results reject and amounts are zero.
Validation success and `already_settled` are never fresh consumption acknowledgements.
The native measurement primitives expose before, after, requested, observed and validity in caller-preinitialized temporary storage.
Persist observation evidence on the receipt before returning, including partial and invalid deltas.
Public result variables must not be shadowed with same-named temporary variables.

## Exact transaction boundaries and closure invariants

| Boundary | Required transaction |
| --- | --- |
| Before accepted preparation | Freeze operation identity, owner allocation and exact payload source site, then perform at most one measured native debit. Accept preparation only with the complete holding and matching site/actor mirrors. A partial debit retains a return-pending hold, an invalid observation retains quarantine, and missile payment rolls back through the existing parent boundary. |
| Duplicate prepare | Reuse only the identical actor generation, consumer, nonce, site, target and frozen payload identity. A mismatched request cannot overwrite or close the original hold. A closed nonce cannot buy another payload. |
| Commitment | Revalidate technology, current policy, exact holding and actual source custody. Do not require replacement free stock. Do not set committed or increment accepted-launch counters until validation succeeds. |
| Physical launch/expenditure | Move the paid hold into launched expenditure once, publish its frozen payload identity and retain a release-pending acknowledgement independently of cleared preparation UI. Preserve the existing deliberate expenditure on interception. A guidance refusal before physical launch requires an explicit owner disposition, never a guessed refund. |
| Confirmed release | Biological delivery uses the existing shared dispatcher acknowledgement for the frozen agent and actual impact state. Nuclear delivery waits for its exact native callback receipt. Only that accepted release may publish confirmed-use history and release-dependent incident, evolution or achievement facts. The shared consequence owners continue to apply deaths, condemnation, contamination and Fallout once. |
| Ordinary abort while source remains recoverable | Refund only the exact observed remaining hold at the frozen controlled site. Technology or target loss need not prevent physical recovery. Measured credit reduces the hold only by the observed gain. Partial/zero gains and invalid observations retain their records. |
| Loss of another barrage participant | Cancel that operation under the existing missile allocation rule. Settle the payload by its own source site's actual condition, rather than pretending it was carried by every participating site. |
| Capture or recapture of payload site | Invalidate former launch authority, move known held quantity into a linked sealed receipt on the actual new controller, retain source identity and uncertainty, and credit no usable stock. Guard/study remain sealed. Integration requires owner capability and measured credit. Same-controller callbacks and owner-equals-holder cases do nothing twice. |
| Damage, disablement or isolation | Hold or mark recovery-pending according to the existing physical disposition. Site disability is not proof of payload destruction or release. Destruction/scuttle requires explicit loss proof and closes only the acknowledged held amount without use effects. |
| Planned Event 005/006 inheritance or civil-war split | Before abort/cleanup, mark the payload's disposition as held for that exact transfer generation. After actual control changes, transfer it with its physical state, irrespective of missile reserve capacity ratios. A recovered payload may enter native split accounting only when recovery was explicitly completed before the transfer. Never auto-refund a known site-held device simply to erase the order. |
| Removed actor | Settle surviving state-attached holdings to their real controllers before clearing the actor or its site registry. Retain inaccessible/uncertain custody until acknowledged. A nonexistent actor does not establish physical destruction. Archive spent/closed nonces and historical receipts, and preserve other living actors' selections. |

For reconciled quantity, require `reserved + received = held + returned + consumed + destroyed + transferred` per receipt.
Transfer is internal movement and the receiver's `received` equals the sender's acknowledged `transferred` exactly once.
Quarantined observations are unresolved evidence and cannot satisfy a reconciled equation by clamping an impossible delta.
Require exact actor/site nonce mirrors, actual STATE identity, real COUNTRY existence for active actors, and current control at every authority-bearing closure.
Never validate a variable scope with `scope_exists` or a STATE with COUNTRY-only `exists`.
Retain the receipt and its site index whenever `_closure_ack` is absent, including after the missile order UI is cleaned.
Do not infer closure from a cleared order flag or a positive stockpile.

## Event 023 owner extension

Add `sov_nuclear_bombs_reserve_for_missile_payload` and `sov_nuclear_bombs_settle_missile_payload` as narrow allocation-only endpoints in the Event 023 runtime owner.
They take the actor/generation, Event 032 nonce and receipt, exact allocation source, actual missile custody site, measured native amount, and closure disposition.
They return an owner allocation receipt and fresh acknowledged quantity.
They must not stage Event 023 test/combat actions, require bomber delivery, change Event 023 evolution gates, activate its terminal routes or call detonation consequences.

At preparation, the owner moves the exact represented source allocation into its existing reserved bucket and records an external-native-hold memorandum subset.
That subset is already contained in reserved, so it is never an additional conservation term.
The native-required comparison and stock-shortfall booking subtract the acknowledged externally held subset from native-represented custody.
The native available count already excludes this debit, so the usable-device calculation must not subtract the same externally held reservation again.
Do not suppress all native raid bookkeeping while one missile receipt exists.

Refund reverses the exact owner allocation only for acknowledged native credit.
Capture moves reserved custody to the appropriate transferred owner/holder mirrors without issuing native stock, and integration changes those mirrors only after measured usable-stock credit.
Launch expenditure moves the allocation into expended once, while confirmed detonation remains separate.
Scuttle uses the owner's existing dismantled/missing meaning according to the proven disposition, without changing total registered or inventing production.
Keep the original source depot distinct from the actual missile custody site so source bookkeeping does not falsely represent the device at two physical locations.
Coordinate existing whole-depot transfer/removal callbacks with that exact allocation receipt to prevent both handlers moving the same reserved unit.

This also applies to Event 023-origin cohorts operationalized on breakaway holders at `023_sov_nuclear_bombs_runtime_effects.txt:1213-1309`.
An active global Event 023 ledger does not make every country's vanilla bomb a Soviet device.
The owner must positively select and prove tracked provenance, or prove a genuinely untracked native allocation before using the untracked path.
Native stock surplus alone does not prove a specific production origin.

## Native callback and stock identity limits

`launch_nuke` documents `use_nuke` and `nuke_type`, but `num_of_nukes` and `add_nuclear_bombs` expose a common count without a documented per-type producer/variant getter.
Vanilla `nuclear_missile_strike` has `essential_equipment = { nukes = 1 }`, which proves its source payment shape, not distinct thermonuclear inventory or observed native callback behavior.
Keep the selected nuclear yield profile immutable, but do not claim this proves separately produced thermonuclear stock.
The exact supported thermonuclear inventory claim remains blocked pending owner/native proof.

The nuclear owner needs one pending delivery receipt per actor with the exact actual impact state, consumer, operation nonce, yield profile and actor generation.
Mirror that identity on the impacted state and retain it independently of `missiles_cleanup_operation`.
Add `nuclear_payload_confirm_native_release` to the bounded `on_nuke_drop` observer and guard stale/repeated callbacks.
Native `on_nuke_drop` exposes launcher ROOT and struck STATE FROM, but no echoed Event 032 nonce.
Consequently same-actor/same-state competing native releases cannot be declared unambiguously correlated from those fields alone.
Serialize owned pending deliveries or retain ambiguity without confirmed-use credit, and test interleaving with Event 023 and vanilla raids explicitly.
The callback's consequence path must consume a receipt-bound atomic/thermonuclear profile rather than infer the weapon exclusively from research.
Do not reuse the Event 023 action scalar to hold a concurrent Event 032 delivery.
An unreturned callback preserves expenditure and disputed release status, never refunds or retries a detonation.

For biological equipment, concrete model mapping is proven by `common/units/equipment/bioweapons.txt:101-178` and the current debit branches.
Producer and variant preservation is not proven.
Installed docs say omitted producer affects all creators, while the wiki describes producer and variant fields and producer-scoped negative removal.
The inspected `num_equipment@MODEL` getter supplies an aggregate count, not a removed producer/variant manifest.
The chemical primitive and facility ledger cannot reconstruct that identity after removal.
Do not implement nominal domestic refunds or treat mixed-producer stock as identity-preserving until an exact native selection/observation contract is established.
Event 076 keeps its existing technology, project, production and advancement ownership.
This receipt extension grants none of those capabilities and does not replace the shared biological consequence/lifecycle dispatcher.

## Constants, targets, cleanup and migration

Preserve existing `missiles_resolution.nuclear_payload_units` and `.biological_payload_units` tuning and family IDs.
Add only owner receipt phase/result/source/disposition constants needed by these endpoints, using unique schema-first groups in `common/script_constants`.
Keep quantity tuning with its existing delivery owner and introduce no new chance, duration or weight targets in this handoff.
No probability balance changes are recommended, so a probability audit and additional subagent are outside this bounded assignment.

Use normal scoped receipt fields for asynchronous state and regular event targets only for an immediate callback relay.
Create no shared global selection target.
Freeze private transaction inputs before nested owner calls because regular aliases and temporary cursors can be overwritten within one chain.
Snapshot matching handles before a settlement loop changes arrays, reset distinct private break variables for every nested iteration, and remove only acknowledged handles.
The owner generation must prevent inherited child ledgers from replaying parent nonces, without clearing physically surviving state receipts.

Migration order is owner native identity/payment proof, owner receipt implementation and Event 023 accounting, Event 032 preparation/commit/consume adapters, exact-site lifecycle calls, then callback-confirmed release plumbing and source-driven tests.
Existing nominal escrows lack the required physical receipt evidence.
Do not manufacture a new proven receipt by copying their nominal amount and a currently selected site.
Any encountered unproven escrow must retain uncertainty rather than obtain an automatic credit or replacement purchase.
No legacy-save support promise is made by this handoff.

Smallest necessary source touchpoints are:

- `common/scripted_effects/032_missiles_operations_effects.txt`: existing prepare/release/consume/dispatch, commit, cleanup, capture, integration, destruction, inheritance, split and removal boundaries.
- `common/scripted_effects/032_missiles_payload_receipt_effects.txt` and `common/scripted_triggers/032_missiles_payload_receipt_triggers.txt`: narrow owner adapters and paid-hold gates.
- `common/scripted_triggers/032_missiles_operations_triggers.txt`: all-family receipt validation, preserving current policy/integration gates.
- Proposed `common/scripted_effects/nuclear_payload_reservation_effects.txt` and `common/scripted_effects/biological_payload_reservation_effects.txt`, with matching trigger files and receipt constants if needed: owner payment, exact receipt lifecycle and bounded site settlement.
- `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` and its matching triggers: exact represented-allocation adapter and native reconciliation, without reusing its ordinary action context.
- `common/on_actions/032_missiles_on_actions.txt` only for receipt-bound native acknowledgement, preserving existing narrow lifecycle callbacks.
- `common/scripted_effects/chaos_meter_effects.txt` only for explicit nuclear profile input at the existing shared native consequence boundary.
- `common/scripted_effects/biological_facility_capture_effects.txt` only if its free-stock capture and missile-held custody need coordination for the same proven site transaction, never as the missile receipt store.

Prefer the existing planned inheritance and split endpoints over editing every Event 005/006 call site.
Verify those callers actually invoke the endpoints before claiming bridge coverage.
Owner helper docs, `023_sov_nuclear_bombs_runtime_effects.md`, the Event 032 event doc and relevant test/acceptance rows must describe the implemented API in the parent change.
Keep chemical documentation's nuclear/biological limitation accurate.
Register any reusable shared owner API in the existing dynamic-effect documentation crosswalk, without placing Event 032 context inside skills.

## Required tests for the parent implementation

1. One native unit, zero free stock after preparation, full holding: duplicate prepare does not debit, commitment succeeds from the paid receipt, abort returns once, launch spends once, and repeated cleanup does nothing.
2. Correct handle with wrong nonce, actor generation, target, state pointer, state ID or payload identity: every validator and closer rejects without consuming, crediting or overwriting another receipt.
3. Capture the actual payload site during preparation: former holder receives zero credit, new holder has a sealed exact receipt, guard/study remain sealed, integration needs owner capability, and recapture transfers the remaining quantity once.
4. Capture another participating site: the operation closes, but payload settlement uses its own site's recovery condition, with missile allocation loss handled separately.
5. Partial debit, partial/zero refund, invalid before/after and repeated recovery: only measured amounts move, quarantine remains reachable after order cleanup, and no new operation silently replaces an open receipt.
6. Damage, disability, isolation, destruction and scuttle: only explicit recover/hold/destroy dispositions settle the payload, and no inventory loss produces confirmed use or a biological release.
7. Two actors with two receipts each and inherited `break = 1`, nested callback dispatch, removed actor and identical owner/holder: every eligible row settles once and unresolved rows remain discoverable.
8. Planned inheritance and civil-war child assignment: receipt follows exact physical control, no capacity-based payload duplication, no parent-refund shortcut, no inherited child authority, and repeat callbacks settle nothing twice.
9. Event 023 operational, assigned and breakaway-origin cohorts with and without native surplus: prepare, owner refresh, native raid interleaving, abort, capture, integration, loss and launch preserve registered totals and do not misbook preparation as expenditure.
10. Change biological selection after payment: dispatch uses the frozen consumed agent/model/quantity, with no replacement stock debit or generic agent substitute.
11. Atomic delivery from an actor with thermonuclear research: atomic consequence profile remains atomic, thermonuclear delivery uses its own profile, and Event 023 pending context stays intact.
12. Interception, dud, wrong-state impact, callback repetition, missing callback, late callback after cleanup, and same-actor/same-state concurrent native raid: consumption and release are separately acknowledged, no false completed release, and no second shared consequence call.
13. Native production and mixed producer/variant equipment, measured debit visibility, refund identity, `use_nuke = no` callback behavior and callback ordering need separate native evidence.
Source fixtures or documented syntax cannot certify these observations.

These refine `PAYLOAD-02/03/04/05/06`, `PAY-02/03`, `ROGUE-LIVE-07`, part 2 capture/succession/removal, and the physical custody regression contract.
They do not change accepted gameplay targets.

## Evidence and validation limits

Skills used: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-native-raids`, and the events skill's loop-break reference.
No skill was modified or new subagent spawned.
Read acceptance-relevant part 2 site/capture/inheritance/removal, part 3 preparation/commit/special payload/cleanup, part 4 Special Warheads, part 8 owner/persistence/shared adapter contract, acceptance entries and the payload/custody test rows.
The current parent assignment supplies the acceptance basis, while the proposed API remains for parent review.

Live `hoi4.reference_context`, `reference_search`, `reference_read` and `source_lookup` were exposed and returned results.
The context bundle omitted Triggers and On actions by its limit, so relevant exact command searches/reads were performed separately.
`script_doc` is unavailable in reference coverage, but installed `game_doc` and offline `wiki` are present.
GetTokenKey has an existing repository meta-effect precedent, but no installed documentation match was found through the live reference search or documentation-folder search.
The installed scripted-localisation directory contains native `defined_text` precedents, but no `documentation.md` at that directory.
No new dependency on an undocumented getter is established here.

| Read source | Revision | Relevant read spans |
| --- | --- | --- |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | 1252-1266 equipment add/remove, 1804-1812 nuclear stock, 4745-4761 launch_nuke, 4833-4852 meta_effect, 6496-6504 regular target |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md` | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` | 558-559 num_equipment, 643-646 num_of_nukes |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | 6813-6821 num_of_nukes scope |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` | 216-222 constants |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` | 2-34 schema and access |
| `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\raids\_documentation.md` | `eac06474fcbde3920523b9b49364f7797851c0cc45f4f0ef41321999a93be43e` | 239-302 RaidInstance outcome scope |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | 1516 nuclear stock, 2253 producer/variant and equipment removal |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` | 263-269 targets, 303-328 regular-target lifetime, 435-443 temporary lifetime |
| `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md` | `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a` | 509 on_nuke_drop ROOT/FROM |

Relative wiki paths resolve under `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Vanilla source precedents read directly are `common\raids\nuclear_raids.txt:300-325`, `common\on_actions\00_on_actions.txt:384-402`, `common\scripted_effects\CZE_scripted_effects.txt:436-458` and the first `defined_text` in `common\scripted_localisation\FR_SCRIPTING_FULL_AUTOMATED.txt`.
The vanilla raid SHA-256 is `966408c81eba9f5928ed352d5f95f6648977b23a8e12ce9aa2cd2cdbca76256f` and vanilla on-action SHA-256 is `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9`.
Live source lookup identified the vanilla nuclear missile `essential_equipment` nested key path but marked that vanilla source shadowed, so it is a precedent rather than the effective mod definition.

Live source lookup located the Event 032 reservation at 4194-4236 under workspace revision `c6aa60876712088f5954ee40cad2bb1fee05ad575fba86650a99b40e1a2ba5af`.
Later owner lookups under revision `0a6f9e820a8abdcba68e79ef02b268a7e15783694d096f41742bcf2d3425594b` located `sov_nuclear_bombs_book_native_stockpile_use:91-162`, `bio_facility_capture_initialize_exact_state_ledger:106-195`, `cbrn_payload_measure_model_debit:66-93`, and the current `chaosx.nr32.1` definition.
Underlying relevant source bodies were read locally, beyond the bounded lookup excerpts.

The connected event trace returned `EVENT_INSPECTED_PARTIAL`, focused analysis and zero indexed helpers, with revision `283a550085362183c930b3e9508acd4051d381fab0d6edd4f1b8afac59de6889`.
Its source inventory was limited inline to 64 of 404 paths and whole-workspace helper/lifecycle passes were deferred.
The `chaosx.nr32.1` scope render returned `EVENT_RENDERED_PARTIAL` with `selectedNodes = 0`.
A refresh trace retained the same graph revision.
This is an exact current coverage blocker, despite source_lookup locating that event, and cannot establish payload lifecycle coverage.
The first resource read was transport-truncated inside its JSON despite complete metadata, so no full-artifact verification is claimed.
A bounded byte-range read supported the manifest's empty selected-node set, but did not establish the whole artifact hash.

Artifact references:

- Refreshed Event 032 trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f92d300e224113f3aaba60e62ba9b73429fe78b4b3e17761628bdcf5879b9ef5/67c101f2b438aa8899cdb81bfc07f5c321a376db367e7afc2626ca79797859a4/event-trace-283a55008536.json`.
- Event 023 trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/679f725a8e5e369d2c626b554afffef037b49e6371b5bc46ce556bf1ca5fc655/1184b810ec0b946ec81904c3aac6ccd38fe69318813dcae97bc34d59ff6fa28e/event-trace-283a55008536.json`.
- Event 032 render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05d1610492434b8bad8bca9d59c260a5745e10c74cca2e1bc9d3a32832463dfa/9989c7b68773b16dfe466b99c1c8a8eb44f6479c2a8373eba6fdbf57e15304b9/event-scope-283a55008536-manifest.json`.

Inspected source SHA-256 evidence:

| File | SHA-256 |
| --- | --- |
| `common/scripted_effects/032_missiles_operations_effects.txt` | `50a48865aa2c33575493ed0904f3cfdeea350df72f9bd41db374f98789d2ab91` |
| `common/scripted_triggers/032_missiles_operations_triggers.txt` | `fe6bba308fe0b92380d4573f5eec8637a804395f245a907ceb86b2848229b430` |
| `common/scripted_effects/032_missiles_payload_receipt_effects.txt` | `45aa0ed3dbf21156072520da49389fd5e042205c7e9e3d7df7b3107fb84d27c7` |
| `common/scripted_effects/cbrn_payload_reservation_effects.txt` | `fd8535a93429919eff2a0b22e0d9b5906872ee78c34d6fa96f4dbd9fe07c02f2` |
| `common/scripted_effects/cbrn_payload_reservation_native_effects.txt` | `a583e9e786593678a1a59ed32b97a90a0d9c3e6241a7ca04084d9a0c459a4add` |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | `9cf6c619f477c6989a724029463e078603155f4ab2f83585021393696f027db7` |
| `common/scripted_effects/biological_facility_capture_effects.txt` | `50861b7a8314c698d11a7a40ade3e35cc2de614cf8c03db15c80c65ac7c8a47f` |
| `common/scripted_effects/chaos_meter_effects.txt` | `f2e4a3a6dbdd30bee11b5ceea021213cff23d772bc9ad05317988e15962ac257` |

No replacement implementation was executed, so the proposed regression cases were not run and no numeric balance or live custody pass is claimed.
No engine-facing source was edited, making script_validate and before/after event comparison implementation follow-ups rather than completion evidence for this document.
No game was launched, no runtime logs were accessed or requested, and no Git write was performed.
No fallback or simplification was adopted.
Completed work is this bounded architecture handoff and source/reference audit.
Blocked work is native identity and callback proof plus current event-render coverage.
Implementation remains with the parent and cannot be marked complete from this handoff.

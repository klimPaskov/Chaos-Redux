# Event 032 chemical receipt source review, 2026-10-07

Disposition: `implemented` for this read-only audit, updated to the latest source hashes below, with capture identity and collector break isolation findings `unresolved` pending parent review and repair.
Acceptance basis: the parent requested a source audit of the current receipt transactions, normal COUNTRY request fields, caller-owned TEMP proofs, selected-receipt counter deltas and the delivered native layer.
Only this handoff was written, after checking its absence at discovery and immediately before creation.
No source or tests were edited, no Git/index operations or further agents were used, and no MCP graphs, game process or logs were accessed.
This is source reasoning rather than compiled or executed engine proof.

## Findings

### R1. Public storage finding corrected to a conditional API naming risk

Disposition: `rejected` as a demonstrated receipt implementation defect.
The earlier review inferred that every normal result fact had to be a TEMP proof output.
That inference was too strong: the parent specified caller-owned TEMP proofs, while the draft explicitly uses normal COUNTRY result facts.
Normal result facts can coexist with separately named TEMP proofs in the parent consumer.
No such consumer is owned or audited by this sidecar, so its absence is not a defect assigned here.

The remaining interface risk is conditional: callers must not create same-named temporary `cbrn_payload_result`, `_result_amount`, `_validation_result`, `_consumed_agent/model/class` or `_transferred_handle` and expect the normal writers to modify those cells.
The consulted references distinguish the storage kinds but do not establish same-name native read precedence.
No conservation failure due to that collision was observed or demonstrated on the draft's documented normal-result API.
This warning must not be reported as a closed-replay acceptance bug or as a requirement to convert every normal result fact to TEMP.
The latest consume/reset/validation ordering is reviewed separately below and rejects closed replay under that API.

### R2. Capture checks the pointer's controller without verifying its frozen state identity

Latest location: `common\scripted_effects\cbrn_payload_reservation_effects.txt`:413-431 and 444-445.
Transfer checks the holder/consumer/nonce, transfer proof, existing recipient, positive held amount and allowed phase, then verifies the current controller of the stored site pointer against the recipient.
It never compares that state's `id` with `cbrn_payload_receipt_site_id_<handle>`.
The return/integration predicate already performs that comparison in `common\scripted_triggers\cbrn_payload_reservation_triggers.txt`, `cbrn_payload_receipt_source_is_controlled`.

Concrete rejection counterexample: source receipt has frozen site ID A but its site pointer refers to state B, with B controlled by recipient R and a supplied transfer proof associated with the receipt's frozen site A.
All implemented transfer conditions can pass, the source quantity closes as transferred, and R receives a sealed record containing the mismatched B pointer and A ID.
The helper has assigned custody using B's controller rather than proving custody at A.
Later integration rejects the mismatched row through its stronger predicate, so this example proves wrong sealed custody and a stranded receipt, rather than an immediate free-stock grant.
This is a source-level invalid-binding counterexample, and no ordinary internal creation path was found that itself generates that pointer/ID mismatch.

Parent repair direction: require the selected source state to match the frozen site ID inside transfer's existing state block, in addition to its current-controller comparison.
The controlled-source predicate cannot be used unchanged for capture because its owner must be the new recipient rather than the old holder.
Keep the current recipient existence/different-holder/controller checks and quarantine or reject the mismatched binding before creating the destination row.
This finding concerns the implemented transfer gate, not an unfinished Event32 capture hook or generation mirror.

## Transaction and conservation review

The following are manual traces of the actual source branches, with normal public results used consistently and valid whole quantities supplied.
They are not executable fixtures or native stock simulations.
For an individually settled valid row, the traced identity is `reserved + received = held + returned + consumed + destroyed + transferred`.
Across transfer-linked rows, transferred and received quantities are internal flow, so global physical conservation counts only original measured reservation, current held leaves, actual native return and terminal consumption/destruction.
Quarantined invalid native observations remain unresolved physical evidence and are not converted into nominal conservation acknowledgements.

| Surface | Source trace and outcome |
| --- | --- |
| Full reserve | Authorization reconstructs exact agent/class/model/route, current policy and profile. Required 240 with observed native debit 240 records reserved/held 240 and phase held. Native outputs are precreated before the nested wrapper. |
| Matching duplicate | Existing full hold plus same consumer/nonce/agent/route/site/target reauthorizes without a stock test and returns its existing quantity. It does not call native debit again. |
| Different binding or nonce with open receipt | The existing consumer slot blocks new allocation. Mismatched binding/full-hold failure leaves the receipt and stock intact. Closing retains last nonce to reject late reuse. |
| Valid partial debit | Required 240 with observed 100 records reserved/held 100 and return_pending. It cannot pass full-hold consumption, and the parent owns settlement initiation. No nominal 240 payment is recorded. |
| Return and repeated return | For held 100, observed credit 40 leaves held 60 and returned 40. A later observed credit 60 closes returned with total returned 100. A settled replay emits already_settled and performs no credit. |
| Invalid native debit or credit | Before/after/observed are retained. Debit remains quarantined without fabricated held payment. Credit preserves the pre-attempt held remainder, moves to quarantined and prevents further ordinary return/transfer/discard. |
| Consume | Full held 240 plus exact binding, source control and current reconstructed authorization moves 240 into consumed, clears held, retires the live slot and performs no second debit. Closed replay rejects as described in R1. |
| Discard | Proven loss of a matching allowed held/captured row moves its exact held amount to destroyed, with no native credit or use record. Quarantined rows reject and settled rows are already_settled. |
| Sealed transfer | Sender held 100 becomes transferred 100/held 0. Recipient receives a distinct local handle with received/held 100, copied exact agent/model/site provenance and captured phase. No native credit or technology/profile change occurs. R2 limits exact source binding. |
| Recapture | A non-quarantined captured row can transfer onward under the same current-controller gate. It preserves original origin and previous holder/handle and closes the old held balance. |
| Captured integration | Actual holder/source identity, recovery proof, current agent unlock and matching profile are checked. Phase changes to return_pending, then the ordinary measured return credits only observed gain. A valid partial unseal of 40 from 100 leaves held 60, returned 40 and return_pending, rather than inventing a full credit. |

## Scope, temporary lifetime and counters

Reserve/consume authorization requires the current COUNTRY to equal ROOT through `ROOT = { tag = PREV }`, then runs the shared ROOT-dependent exact-target policy.
It does not silently authorize a foreign-ROOT capture callback as a launch actor.
Return, discard and transfer account in the selected actual holder COUNTRY and do not redirect stock or receipt reads to a foreign ROOT.
Integration technology/profile checks are current-holder checks and do not borrow launch policy.
The nine exact agents retain existing technology/project alternatives through `cbrn_action_agent_is_unlocked`, including the shared Sarin/Soman project paths.
The resolver derives class from exact agent and maps only the four prepared-air models on the two supported air routes.

Native model/matched/class/default-cost outputs are created inside the authorization helper before their nested calls and copied into normal validated facts before return.
Both reserve and return create every public native observation output before their nested accounting calls.
The delivered wrappers initialize all seven lower-level mask scratch fields, including the meta debit output.
Transfer's temporary source handle is created in the transfer caller before entering the receiver and invoking nested initialization/count helpers.
No nested call in that path writes it, so conservative cleanup of nested-created temporaries does not erase the outer source handle.
Receiver and sender handles are normal variables scoped to their own COUNTRY, while lookup and count scratch are unscoped temporaries.
R1 is the public acknowledgement storage discrepancy, rather than a missing initialization in the delivered native wrappers.

`cbrn_payload_refresh_reservation_counts`:38-62 updates only the selected receipt and first verifies holder ID equals the current country ID.
It subtracts the row's previous counted quantity and previous phase contributions, then adds its current phase/held contribution and stores the new counted snapshot.
Repeated refresh of an unchanged valid row has zero net effect, including refresh after a rejected callback.
No global or per-country receipt recount or scope iterator appears in this helper.

| Transition | Selected-row total/profile delta |
| --- | --- |
| New quarantined zero row to held 240 | Held total becomes 240, profile count stays one, quarantine count drops from one to zero. |
| Return_pending 100 to return_pending 60 | Held total drops 40, profile count remains one. |
| Held or pending to closed zero | Previous held quantity and profile contribution are removed once. |
| Sender held 100 to transferred zero | Sender held total drops 100 and bound count drops one. |
| Receiver new captured 100 | Receiver held/captured totals add 100 and profile count stays zero. |
| Captured 100 to integration return_pending 100 | Held total stays 100, captured total drops 100 and profile count adds one. |
| Partial unseal 100 to 60 | Held total drops 40, captured total stays zero, and the remaining integrated return_pending row retains the profile lock. |
| Invalid credit after integration | Quarantine count adds one and the existing bound contribution remains. No recounted global correction occurs. |

Sealed captured and captured_quarantined phases are excluded from the profile-bound predicate.
The transition into integration begins profile binding before native credit, retaining the lock on a partial or invalid integrated return.
No incremental-counter arithmetic defect was found for the traced valid transitions.

## Latest-source follow-up

The latest effects file has 578 physical lines.
The native primitive and trigger files are unchanged from the preceding review, while effects and constants have the following current identities.

| Current source | SHA-256 |
| --- | --- |
| `common\scripted_effects\cbrn_payload_reservation_effects.txt` | `B70D6868E9438CD86BF68E646F1C773677BC23275539ACA90A9B30E78759D8D3` |
| `common\scripted_triggers\cbrn_payload_reservation_triggers.txt` | `AF9316CDF8ED8CF9A21E7986DF78BCF6524E69DCE763499A7C0EA6B9A45F45E0` |
| `common\script_constants\cbrn_payload_reservation_constants.txt` | `498D969175382ACA6E8157806746E1438EAC09E283E5B8DF5557347C9F0CC293` |
| `common\scripted_effects\cbrn_payload_reservation_native_effects.txt` | `A583E9E786593678A1A59ED32B97A90A0D9C3E6241A7CA04084D9A0C459A4ADD` |

### Validation and fresh consumption

`cbrn_validate_payload_reservation`:310-333 resets and writes only `cbrn_payload_validation_result`, while preserving separation from fresh `cbrn_payload_result` acknowledgement.
It checks full hold, binding, controlled source, reconstructed current authorization and exact resolved model without requiring replacement free stock.
`cbrn_consume_payload_reservation`:338-362 first resets the fresh result, calls validation, recreates lookup storage after the nested return, and rechecks full hold, binding and controlled source.
It sets accepted only after moving the held amount to consumed and closing held/phase, then retires the live receipt.
An old accepted validation value is overwritten on this invocation, and a consumed row fails the subsequent hold predicate.
Source traces therefore reject validate-then-consume-then-consume replay, already-closed validation, changed nonce/binding and lost current source control without minting a fresh accepted result.
There is no second native debit on these paths.

### Counter and copied-ledger confirmation

Refresh remains an O(1) selected-row delta, not a global or per-country recount.
The normal constructor and captured transfer initialize both counted fields to zero before first publication.
The holder marker in refresh excludes foreign-owned copied rows, and initialization resets inherited aggregate/sequence/live-slot state when its ledger owner does not match the current country's ID.
The reviewed foreign-ledger protection does not itself transfer, destroy or grant copied physical stock.
No defect was found in those current counter mechanics or the sealed exclusion from profile binding before integration.

### R3. Snapshot collector does not isolate its documented default loop-break variable

Location: `cbrn_settle_site_payload_reservations`:512-575.
The first loop collects matching holder/site IDs into a temporary snapshot, and the second iterates that snapshot while transactions can safely retire entries from the original live array.
This avoids the documented prohibition on removing elements from the array currently being iterated.
Lookup, model and native measurement outputs remain created at the consuming nested boundaries, and transaction helpers do not overwrite the collector's explicit `cbrn_payload_site_handle` value variable.

Both `for_each_loop` blocks omit `break`, however.
Installed `documentation\effects_documentation.md`:4279-4294 identifies the default temporary break variable as `break` and specifies nonzero as the break condition.
The collector neither initializes that default variable nor selects a private break field.
Source-level counterexample under that documented contract: caller enters with temporary `break = 1` and two valid same-site receipts H1 and H2.
Collection or settlement can stop before exhausting the matching rows, yet line 524 initializes site_result to accepted and the aggregate only downgrades for a visited failed transaction.
A visited successful settlement can therefore leave H2 open while the site method reports accepted.
The exact initial-versus-post-iteration break timing is not established here, but either early boundary exposes incomplete coverage without a completion check.
This is a source contract counterexample rather than an executed engine observation.

Parent repair direction: give each loop an explicit collector-owned break temporary, initialize it to zero immediately before that loop, and avoid altering a caller's unrelated `break` field.
Keep the frozen handle snapshot and per-receipt delta refresh design.
Consider an explicit collected/visited coverage check before publishing complete site settlement, with unresolved handles retained when completion is not proven.

The separate large-array ceiling remains `unresolved` rather than a confirmed truncation bug.
The events skill requires conservative tests at more than 1,000 rows, but offline Data structures:1216-1220 explicitly attaches the 1,000 limit to `while_loop_effect` and `for_loop_effect`, without specifying it for `for_each_loop`.
Installed `for_each_loop` prose does not supply a numeric ceiling either.
Thus a 1,001-row truncation claim for these particular loops would exceed the available evidence.
Pending source/runtime-contract validation should cover a relevant receipt after a long unrelated prefix, more than 1,000 same-site receipts, inherited nonzero default break, partial refund, quarantine and same-site mixed-agent integration.
No fixture was executed and no new count cap or source patch was added.

### Site settlement scope and parent boundary

The collector rebuilds each handle's consumer and nonce from the selected holder's own row, resets its local proof inputs, dispatches the requested recover/destroy/capture/integrate/hold action, and aggregates measured settlement amounts.
It matches holder ID and the frozen site ID to the requested state ID, while the public transaction still checks its own phase and identity conditions.
The collector does not cure R2: a row with frozen site ID A and pointer B can still be selected for A, then transferred using B's controller.
Sealed receipts remain excluded from profile locking until the integration phase transition, and partial unseal retains the bound remainder.
No missing Event32, profile, custody or removal owner hook is reported as implemented, repaired or failed by this review.
Their wiring and tests remain parent-owned.

## Earlier-review evidence identities and limits

| Source inspected | SHA-256 |
| --- | --- |
| `common\scripted_effects\cbrn_payload_reservation_effects.txt`, all 480 physical lines | `4DA53E9C310DB45ADBC585E32050BE723925FDBDB380868E75BDD9A86678AC1C` |
| `common\scripted_triggers\cbrn_payload_reservation_triggers.txt`, complete file | `AF9316CDF8ED8CF9A21E7986DF78BCF6524E69DCE763499A7C0EA6B9A45F45E0` |
| `common\script_constants\cbrn_payload_reservation_constants.txt`, complete file | `963F2CCE392A087B39FCEF1A9CC3E4B38743C550C345FBEAAE8B6DFC16EBCB45` |
| Delivered `common\scripted_effects\cbrn_payload_reservation_native_effects.txt` | `A583E9E786593678A1A59ED32B97A90A0D9C3E6241A7CA04084D9A0C459A4ADD` |

The three parent draft hashes were unchanged on the closing pre-handoff check.
Source dependencies read include `cbrn_payload_triggers.txt`:29-91 and 147-190, `cbrn_triggers.txt`:268-314 and 410-433, `cbrn_diplomacy_triggers.txt`:103 onward, and `cbrn_exposure_effects.txt`:1135 onward.
Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`:435-454 and 551-559 was reread for temporary versus normal storage, scoped normal values and targeted fields.
Its previously recorded SHA-256 is `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4`.
The native layer's reference evidence remains in [032_chemical_native_primitives_2026-10-07.md](032_chemical_native_primitives_2026-10-07.md), including installed effects documentation and the prior bounded validation limits.
No new engine or MCP graph evidence was sought, as explicitly required by this source-only assignment.
No findings are based on missing parent-owned hooks, integration tests, Event32 call sites or planned custody/profile integration.
Repairs and executable scenario validation remain parent-owned.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, already fully read in this conversation.
No skill was changed and no implementation fallback or simplification was made.

## Repair source check and revised dispositions

This appended check supersedes the earlier open-finding statuses for R1-R3.
Acceptance basis: the parent reported the R2/R3 repairs, explicitly retained normal public result fields, stated that the Event32 adapter does not precreate those names as TEMP, and requested only this bounded source check and disposition append.
Only this review handoff was updated.

| Source checked | Current SHA-256 |
| --- | --- |
| `common\scripted_effects\cbrn_payload_reservation_effects.txt`, repaired file with 583 physical lines | `052EB60CA529401E521B29A7236E9D3B73EC42850CD6A4888BDB51C1C6A85A84` |
| `common\scripted_triggers\cbrn_payload_reservation_triggers.txt` | `AF9316CDF8ED8CF9A21E7986DF78BCF6524E69DCE763499A7C0EA6B9A45F45E0` |
| `common\script_constants\cbrn_payload_reservation_constants.txt` | `498D969175382ACA6E8157806746E1438EAC09E283E5B8DF5557347C9F0CC293` |
| `common\scripted_effects\cbrn_payload_reservation_native_effects.txt` | `A583E9E786593678A1A59ED32B97A90A0D9C3E6241A7CA04084D9A0C459A4ADD` |

R1 disposition: `rejected` as an implementation defect, with the normal-result API clarified by explicit parent direction.
The public result names remain normal COUNTRY facts and are not caller-created TEMP outputs in the new Event32 adapter according to the parent's report.
Caller-owned TEMP proofs use their separate contract.
The adapter itself was not read or audited in this bounded check, so the naming assurance is attributed to the parent rather than presented as independent integration evidence.
The prior hypothetical same-name storage collision is not an active finding against this accepted API.

R2 disposition: `implemented`, verified in repaired capture source with executable/native validation pending.
At effects:409 the transfer helper creates the unscoped temporary `cbrn_payload_lookup_handle` before the state entry.
At effects:429-432 the stored source-state block now compares its `id` to `PREV.cbrn_payload_receipt_site_id_@var:cbrn_payload_lookup_handle` and separately checks the current controller against the proven transfer receiver.
In that STATE block, PREV is the sender COUNTRY, so the frozen field is read from the correct holder and the temporary lookup remains available without a scope prefix.
The intervening identity/phase checks and target saves do not overwrite that lookup.
The earlier pointer-B/frozen-ID-A example now fails the identity equality before destination-row creation or source quantity closure.
No replacement state, alternate holder or stock grant was introduced by the repair.

R3 disposition: `implemented`, verified in repaired collector source with executable/native validation pending.
The collect loop initializes `cbrn_payload_site_collect_break` to `constant:cbrn_math.zero` at effects:514 and passes it explicitly at 518.
The settlement loop independently initializes `cbrn_payload_site_settle_break` to zero at 528 and passes it explicitly at 532.
Neither loop uses or writes the caller's unrelated default `break` temporary, and no other reference to either private break field appears in this source file.
The inherited-default-break counterexample is therefore removed under the documented loop contract.
The snapshot remains the iteration input for settlement, while retirement modifies only the original live receipt array.
The selected-row counter delta mechanism is retained.

The parent reports that the test worker is adding both counterexamples.
No test result was supplied or executed in this check, so no fixture pass or engine proof is claimed.
The separate `for_each_loop` large-array ceiling remains unverified, with the earlier reference limits unchanged.
Native primitive source is unchanged.
Event32/profile/custody/removal integration hooks are being wired by the parent and are excluded from completion claims.
No gameplay writes, scope expansion, Git/index operations, MCP graphs, further agents, game process or log access occurred.

## Bounded final owner-hook source review

Disposition: `implemented` for this read-only review, with R4 `unresolved` pending parent repair or contrary loop-contract evidence.
Acceptance basis: the parent reported review of R1-R3 and 39 passing tests, then assigned the new Event32 chemical adapter, its trigger peer and chemical settlement call sites only.
Only this bounded appendix was written.
The parent's existing test results are reported evidence, not tests rerun by this sidecar.
No broader consequence tests, new tests, MCP calls, gameplay edits, Git/index operations, agents, game process or logs were used.

| Current inspected source | SHA-256 |
| --- | --- |
| `common\scripted_effects\032_missiles_payload_receipt_effects.txt` | `C0C1F9A5882C5A5A5CC8D652D96ED8DA1810686C5B7A22E2172D25B918306834` |
| `common\scripted_triggers\032_missiles_payload_receipt_triggers.txt` | `9DA2E18A7114153600196FFFABC94FE21C4FBD6C393D664F3B20DB84ACDE4998` |
| `common\scripted_effects\032_missiles_operations_effects.txt`, bounded call-site contexts | `F1344D6ACD266DA99ABCE45A6880FC582AD299B6A32B139EFF0B7E2689F2037A` |
| Shared `common\scripted_effects\cbrn_payload_reservation_effects.txt`, current site collector dependency | `FD8535A93429919EFF2A0B22E0D9B5906872EE78C34D6FA96F4DBD9FE07C02F2` |
| Shared `common\scripted_triggers\cbrn_payload_reservation_triggers.txt` | `AF9316CDF8ED8CF9A21E7986DF78BCF6524E69DCE763499A7C0EA6B9A45F45E0` |

The adapter, peer, operations and shared effects hashes were stable on the closing source check.
The shared owner API contract was read from `docs\systems\cbrn_warfare\chemical_payload_reservations.md` and the implementation report from `docs\plans\032_missiles_plans\032_chemical_receipt_implementation_2026-10-07.md`.
That report attributes 39 receipt tests and additional Event32 source-contract checks to the parent and identifies native/callback coverage limits.
No new engine coverage is inferred from those reports.

### R4. Country-removal wrapper leaves its outer scope iterator on the default break field

Location: `032_missiles_payload_receipt_effects.txt`:160-175.
`missiles_settle_chemical_payloads_on_removal` uses `for_each_scope_loop` over `missiles_launch_site_states`, without declaring `break` or initializing an isolated break temporary.
The repaired inner CBRN collector has its own break fields, but those do not protect this outer iterator.
The previously consulted installed effects documentation for `for_each_scope_loop` identifies its default break variable as `break`, with nonzero breaking the loop.

Concrete source-contract reproduction:

1. Removed holder O has two registered physical custody sites S1 and S2, each with a valid positive held or sealed chemical receipt owned by O.
2. Both states survive under living controller N, and the callback ROOT is a foreign country.
3. The caller has an inherited temporary `break = 1` before `missiles_cleanup_removed_country` enters the removal wrapper.
4. Under the documented default-break semantics, the outer site iterator can stop before visiting both sites, regardless of the repaired private break fields inside CBRN.
5. Cleanup already sets `missiles_program_cleanup_complete` before this call at operations:7062-7063 and subsequently clears `missiles_launch_site_states` at 7203.
6. An unvisited site's held balance remains on removed O instead of receiving the supported sealed transfer to N, while the one-time owner cleanup cannot repeat its site enumeration.

The timing of the iterator's first break check and actual native execution remain unobserved, as in R3's source-contract review.
The concrete dangerous outcome is incomplete removed-owner custody settlement and a stranded positive receipt, not a demonstrated stock duplication or automatic use record.
No source in this bounded wrapper establishes that all removal callers enter with the default break temporary cleared.
Parent repair direction: initialize a removal-owned private break variable to zero immediately before `for_each_scope_loop`, pass it explicitly, and let the test worker exercise the two-site foreign-ROOT case with inherited nonzero default break.
No source change or test duplication was performed here.

### Ownership and lifecycle findings within the assigned surface

The preparation adapter freezes agent, consumer, operation nonce, source and intended target, initializes custody proof before its nested request builder, and records partial/quarantined receipt handles rather than claiming nominal full payment.
Commit and consumption use the same operation binding, full held receipt, exact source/target IDs, current technology/profile and shared current authorization.
Consumption clears its operation amount and verified flag before attempting the fresh CBRN transaction, then sets verified only for fresh accepted positive consumption.
No adapter path treats validation or already_settled as fresh consumption.

Release binds the actual holder's handle and operation nonce.
During site settlement it compares the lost participant ID with the operation's frozen launch-site ID.
Primary destruction supplies loss proof, primary capture obtains the actual current controller, and primary isolation supplies no recovery proof.
For a secondary participant loss, the adapter separately checks the primary source's control, registration, capture/rogue/scuttle/isolation and irreparable-damage flags before supplying recovery proof.
The CBRN owner still checks its own frozen source pointer/ID and profile before native return.
Blocked or quarantined quantities remain in CBRN's receipt registry after the missile adapter clears its local active flag/handle.

The site wrapper freezes the exact STATE target and its current controller before entering the expressly supplied holder COUNTRY.
Capture call sites select `missiles_capture_former_controller` as that holder under a foreign new-controller ROOT at operations:6534-6536.
The capture tail removes the state from the former holder's site array and registers it on the current controller at operations:6542 and 6609-6612, so a sealed captured site is not assumed absent from the new holder's registered sites.
Recapture can therefore reach the previous actual holder's sealed receipt, without native credit or technology grant.
Scuttle uses its stored actual controller at operations:2200-2203, and ordinary isolation/scuttle/disaster contexts supply their explicit hold/destroy disposition before mutating physical state flags.
Repair clears isolation and irreparable damage before its recover call at operations:1603-1617.
Rogue recovery separately checks the recovery predicate before the site call at 1753-1756.
Captured integration supplies the selected current holder and exact state at 6746-6748, leaving profile/technology and measured unseal accounting to CBRN.

No other critical ownership or replay defect was established in this bounded source trace.
The removal wrapper's registry coverage for every possible pre-existing orphan/quarantined row and the native large-array iterator behavior were not proven by these call-site reads.
Those are explicit coverage limits rather than declarations that an implemented owner API is missing.
Profile-lock and sanctions contracts are documented and parent-tested, but their separate source surfaces and broader consequence dispatch were not re-audited here.
R1-R3 dispositions from the previous source check remain unchanged.
Full Event32, physical callback, save-persistence and native execution completion are outside this review.
Skills used remain the previously read events and subagents guidance, with no skill edits or implementation simplifications.

### Parent disposition of R4

Disposition: `implemented` in `missiles_settle_chemical_payloads_on_removal` after the bounded review.
The wrapper initializes `missiles_chemical_removal_break` to zero immediately before the scope iterator and passes that private field explicitly.
The added `test_country_removal_does_not_inherit_an_outer_loop_break` source-contract regression passes in the ten-test special-payload module.
This removes the inherited-default-break dependency under the cited documented contract; full two-site native callback execution remains unobserved and is not claimed by that structural test.

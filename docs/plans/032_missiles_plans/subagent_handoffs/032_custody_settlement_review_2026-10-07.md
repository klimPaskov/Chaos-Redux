# Event 032 custody settlement review, 2026-10-07

Disposition: `unresolved` for the findings requiring parent review and implementation.
The requested bounded source audit is finished, but this document does not approve the patch or claim completion of the accepted Missiles specifications.
Authority: the parent requested a read-only audit of the current reserve custody patch, with this handoff as the sole permitted write, no spawning, no Git writes, no game launches, and source-reference/MCP work and concurrent tests retained by the parent.
The requested handoff did not exist at the initial check or the final check immediately before creation.

## Source identity and scope

Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Line references below are one-based and refer to the inspected working files, not HEAD.
Abbreviations: `operations` means `common\scripted_effects\032_missiles_operations_effects.txt`, `effects` means `common\scripted_effects\032_missiles_effects.txt`, and `operation triggers` means `common\scripted_triggers\032_missiles_operations_triggers.txt`.

| File | SHA-256 of inspected bytes |
| --- | --- |
| operations | `A2E9309033DBECEB3481D0CF24456059CDFF22196C35D3834B5B8A00F1F8E5A6` |
| operation triggers | `424E1749A463C7621C89F8A881ECCFD05109F78B8911F6598601C7D324948504` |
| effects | `A6270203F41D78E6658B249D5105F2B945B303B49FEFEB9F62AF9CC0988333EB` |

The two patch-file hashes were checked again immediately before writing this handoff.
Read-only Git diff inspection was restricted to the two requested patch files.
The final diff also includes removed-country cleanup of `missiles_unallocated_reserve` and `missiles_site_settlement_in_progress` at operations:7162-7163.
Other source reads were limited to definitions, callers, and refresh consumers relevant to custody and site-loss settlement.

Required instructions read: `AGENTS.md`, `.agents\skills\chaos-redux-events\SKILL.md`, `.agents\skills\chaos-redux-subagents\SKILL.md`, and `.agents\skills\chaos-redux-decisions-missions\SKILL.md` for the direct state-targeted decision callers.
Specification evidence: `docs\specs\032_missiles_specs\032_missiles_spec_part_2_program_and_launch_sites.md`:142-159, 161-180, 339-398, 400-443, and `docs\specs\032_missiles_specs\032_missiles_spec_part_3_operations_and_consequences.md`:260-277, 721-743.
These sections require authoritative reserve accounting, exact-once captured custody transfer, explicit reserved-resource settlement, and refreshed program display after cleanup.
Acceptance basis is the parent's explicit instruction to preserve the full accepted Missiles specs without simplification.

## Findings

### F1, high: recapturing a sealed arsenal strands the former controller's held ledger

Relevant lines: operations:1343-1347, 6485-6497, 6503-6518, 6578-6579, 6634-6675.
The capture amount reads only `missiles_site_reserve`, while the handler overwrites `missiles_site_captured_reserve` at line 6518 and debits only `missiles_operational_reserve` at line 6506.
It never settles the former controller's existing `missiles_captured_reserve_held` receipt.
Registered captured and isolated sites remain eligible for this callback through `common\scripted_triggers\032_missiles_triggers.txt`:471-485.

Concrete counterexample:

1. B controls a site previously captured from A, with state `missiles_site_reserve = 0`, state `missiles_site_captured_reserve = 8`, and B's `missiles_captured_reserve_held = 8`.
2. B guards or studies the site, preserving those sealed weapons, or simply leaves its capture unresolved.
3. C takes control, and the native control-change caller binds B as `missiles_capture_former_controller`.
4. The transfer helper returns zero because ordinary site reserve is zero.
5. Line 6518 overwrites the physical held receipt with zero, while B retains held reserve 8 and C receives held reserve zero.

The eight missiles have no surviving physical receipt, but B still reports them in its held ledger.
Repeating C's callback is blocked by the controller-id guard, so repetition does not repair the orphaned ledger.
This is an existing relevant accounting gap left by the patch, not a newly introduced defect in PREV binding.
Parent follow-up: settle the old sealed receipt once against its proven holder before replacing it, with an explicit transfer or destruction outcome under the accepted capture contract.

### F2, high: a nonlethal foreign strike still invokes ROOT-bound network accounting for the defender

Relevant lines: operations:4673-4678 and 4559-4569, effects:829-876.
`missiles_apply_operation_site_damage` saves the attacker as ROOT and enters the site's controller directly to call `missiles_record_site_network_achievement_snapshot` at line 4678.
That snapshot calls `missiles_recalculate_network` at line 4562 without a recipient event boundary.
Network recalculation resets the current country's counters and array at effects:830-832, but credits the original ROOT at effects:846, 860, and 868-871.

Concrete counterexample:

1. A strikes B's site, with B having two working sites totaling capacity 12 and A having its own unrelated network.
2. In B's country scope, the snapshot zeros B's network counters and region array.
3. Iteration over B's controlled states adds B's working-site counts and capacity to A's counters and records regions on A.
4. A nonlethal hit never calls the controller scuttle adapter, so no `chaosx.nr32.7` refresh is sent from that path.

B's snapshot is recorded with zero country counters, and B's network remains stale until another owner-bound refresh.
The later incoming-damage recorder also has a separate source gate problem: operations:4579 tests the normal variable `missiles_incoming_damage_state`, but the producer at line 4672 creates only an event target with that name.
A targeted source search found no normal-variable writer for it, so that recorder does not supply the expected ordinary post-hit refresh under normal inputs.
If that gate is repaired, its direct recalculation calls at operations:4614, 4640, and 4661 also require correct ROOT binding.

This is a relevant surrounding caller gap, not a failure of the new custody projector's PREV accounting.
The lethal scuttle path does send the controller-bound receiver after retiring the physical site, but the pre-hit snapshot still has the scope defect.
Parent follow-up: preserve the defender's pre-hit snapshot and final refresh under an explicit defender ROOT, and distinguish the event-target gate from normal-variable storage.

### F3, medium, helper-contract gap: ordinary isolation does not restore deferred phase refresh

Relevant lines: operations:2048-2061, 6250-6259, 1821-1823.
Cleanup clears `missiles_program_phase_prepared` at line 6250, then skips phase recalculation while settlement is in progress.
Isolation's unconditional post-mutation block restores network and custody at lines 2055-2056 but calls no phase or status helper.
Only the conditional rogue-closure branch restores phases through `missiles_close_rogue_incident` at line 1823.

Concrete helper-level counterexample: invoke `missiles_isolate_site` on a participating site under its documented program-country ROOT while a prepared operation is active and no warning, incident, or rogue crisis is active.
Settlement refunds and closes the operation and clears its prepared phase, but no replacement program phase is selected after isolation.
If it was the last usable site, the expected establishment phase is also absent.

The inspected player callers are rogue isolation at `common\decisions\032_missiles_decisions.txt`:1410 and retaliation isolation at line 1641.
Rogue isolation has a closing helper, while retaliation isolation requires an active warning and can retain a correct retaliation phase.
Therefore this proves the general helper contract and the claim that every caller restores all three refreshes are incomplete, but does not prove a visible phase failure through those currently gated player decisions.
Parent follow-up: an unconditional phase refresh after isolation completes its physical changes would restore the helper contract without changing reserve settlement.

## Patch-local assessment and caller coverage

| Surface | Scope and accounting inspection | Deferred refresh after physical change |
| --- | --- | --- |
| Custody, operations:1289-1327 | COUNTRY input, STATE iteration, actual COUNTRY PREV owns remaining reserve, foreign controlled-state mismatches skipped without modifying their custody, free room excludes matching live escrow allocation | Normal country output `missiles_unallocated_reserve` records the remainder |
| Preparation, operations:3384-3388 | Site receipts written before custody projection, escrow is deducted from ordinary reserve by effects:569-572 | Custody refresh follows the markers, avoiding occupied/free slot overlap |
| Isolation, operations:2031-2062 | STATE with owning program ROOT, allocation-loss mode zero, escrow refunded, physical isolated marker set after settlement | Network/custody unconditional, phases conditional on rogue closure, see F3 |
| Normal scuttle, operations:2072-2130 | STATE with owning program ROOT, loss mode one, matching assigned stock settled before ordinary free stock, captured-held stock debited separately | Network/custody at 2118-2119, status helper at 2124 also recalculates phases |
| Controller scuttle, operations:2136-2204 | STATE with potentially foreign ROOT, controller target owns refund/loss and ordinary/held debits, state retired before receiver | `chaosx.nr32.7` dispatched at 2202, receiver restores network/custody/status/phases at 6772-6788 |
| Disaster, operations:4852-5063 | Controller ROOT supplied by `chaosx.nr32.9`, percentage free-stock debit precedes matching assigned-stock settlement, physical damage/capacity change follows | Network/custody/status/phases at 5042-5045, wreck also uses controller scuttle |
| Capture, operations:6456-6600 | STATE with new-controller ROOT, actual former-controller COUNTRY owns settlement, captured amount initialized in the consuming caller | Former-country receiver at 6516 after registry removal, new-country network/status at 6593-6595 after captured marker, F1 remains |

All five direct calls to `missiles_settle_lost_site_allocation` were inspected: operations:2048, 2097, 2144, 4959, and 6502.
Normal scuttle callers were traced from rogue AI at 2015, generic site damage at 4767, and captured-site scuttle at 6723, including direct player rogue scuttle at decision line 1510.
Controller scuttle callers were traced from operation damage at 4721 and wrecking disaster at 4986.
Isolation callers were traced from regional-seizure timeout at 1967, rogue AI at 2000, and the two direct decisions above.
Capture callers were traced from `common\on_actions\032_missiles_on_actions.txt`:168-181 and released-country reconciliation at operations:6602-6621.
`missiles_cleanup_site` at 2206 has no production caller found by the targeted search and was not treated as a proven site-loss path.
The generic damage alias at 7245 calls the ROOT-dependent non-operation adapter, but no external production invocation of that alias or adapter was found by the targeted search.

The inspected `missiles_abort_operation` to `missiles_refund_operation_reserve` closure changes reserve and clamps values, without recalculating network, custody, or phases.
The cleanup closure's payload release, mission removal, receipt clearing, and `missiles_back_to_target_profiles` likewise have no additional source-level calls to those three refresh helpers.
The guard at operations:6255-6260 therefore covers the inspected cleanup refresh closure.
Native mission-removal behavior remains part of the parent's reference/engine evidence, not proven by this audit.

## Temporary lifetime, exact-once behavior, and arithmetic walkthroughs

The capture caller initializes `missiles_captured_reserve_amount` at operations:6490 before `missiles_transfer_captured_reserve` returns at line 6491.
All later reads at 6494-6495, 6505-6506, 6518, and 6579 are inside that owning caller.
No other production caller of the capture-amount helper was found.
The helper's damage-survival and capture-loss scratch variables are consumed before it returns.
Custody's room/take scratch values and settlement's lost-allocation scratch value are also consumed inside their defining helpers.
The settlement callers initialize the input `missiles_allocation_loss_mode` before every inspected call.
No newly introduced outward temporary-output lifetime gap was found in these changes.

Settlement's matched positive state operation ID, active country operation, and uncommitted guard reject an ordinary second invocation after cleanup clears the active flag and state receipt.
Normal and controller scuttle zero the state ordinary/held receipts, preventing a second debit on repeat execution.
Capture's controller-id guard prevents a duplicate same-controller transfer, but does not solve the distinct-controller recapture case in F1.
Disaster clears pending severity at operations:5060, and its queue processor clears the pending-state array at 4843, preventing repeat settlement of the same queued impact.

These are source arithmetic walkthroughs, not executed production-script tests:

- Single-site scuttle with free stock 6 and assigned stock 4: abort refunds 4, assigned loss debits 4, unchanged physical free snapshot debits 6, leaving zero.
- Wrecking disaster with site free stock 6, total escrow 4, site assignment 2, and catastrophic loss 60 percent: percentage debit 4 after whole-count rounding, refund 4, assigned loss 2, remaining physical free debit 2, leaving the other site's returned assignment of 2.
- Capacity 10, matching assignment 4, free country stock 8: the custody helper projects 6 to this site and leaves 2 unallocated when no other eligible site exists.
- Foreign-origin call with COUNTRY B current and COUNTRY A ROOT: owned-state PREV updates B's remaining reserve, and a state controlled by A is skipped without clearing its reserve.

Suggested parent test additions are the recapture fixture in F1, defender-root nonlethal strike snapshot in F2, and generic no-warning/no-rogue isolation in F3.
Adversarial escrow tests should also distinguish a missing or insufficient refund receipt from a successful refund: settlement's outer guard does not require `missiles_operation_reserve_receipt_active` or a sufficient escrow amount, while the abort refund does at operations:6165 and effects:582-584.
No normal producer of an inconsistent escrow state was established here, so this is a robustness scenario rather than a confirmed normal-path accounting defect.

## Documentation, validation limits, and handoff

Only this handoff was written.
No gameplay helpers, call sites, constants, tuning values, cleanup code, localisation, tests, or Git state were edited by this audit.
The new predicate, allocation-room rule, normal-variable remainder output, and settlement deferral require matching helper documentation in the parent patch.
`common\scripted_effects\032_missiles_operations_effects.md`:5-12 still describes scratch lifetime in enclosing-evaluation terms and line 9 attributes capture output initialization only to the returning helper.
Its capture API documentation should state the required caller-owned zero initializer and retain the actual lifetime limit from the events skill.

Meaningful validation performed: source call-chain tracing of the five settlement entry points, transitive cleanup-refresh inspection, capture-output producer/consumer tracing, targeted controller and held-ledger searches, the numerical walkthroughs above, and final source-identity verification.
No source interpreter, concurrent parent tests, live game, save observation, probability audit, or MCP scenario/render/compare was run by this subagent.
The parent explicitly retained source-reference and MCP work, so no MCP artifact URI or engine proof is claimed.
An exposed `hoi4.event_inspect` route was visible in tool metadata, but service health and analysis coverage were not tested, and no unavailable route was inferred.
No new helper was designed, and probability, GUI, focus, map, and unrelated feature audits were excluded as requested.
No gameplay simplification or fallback was made.
The remaining implementation and runtime uncertainty belongs to F1-F3, the adversarial escrow case, native callback/mission semantics, and the parent's concurrent validation results.

## Parent repair review and dispositions, 2026-10-07

This appended review supersedes the unresolved source findings F1-F3 above for the source revisions identified here.
The original findings remain historical evidence of the counterexamples that prompted the parent repairs.
Authority and acceptance basis: the parent reported reviewing the whole handoff, applying the bounded F1-F3 repairs, and requested this read-only follow-up and appended dispositions.
No new gameplay or audit surface was added.

| File | SHA-256 reviewed after parent repairs |
| --- | --- |
| operations | `E4437F0F57D48D2D6FCD1990E808D6D36FE167744A9FB63A0570A17A1E28A2AE` |
| effects | `B28EF2A3CE3E88C177E29FCF7DEEFC0AE253531D17FF41AFB1EABEE90A7F4E64` |
| operation triggers | `424E1749A463C7621C89F8A881ECCFD05109F78B8911F6598601C7D324948504` |

The hashes above were checked again immediately before appending this review.
Current line references in this appendix use these revisions and supersede the original line numbers where parent edits shifted them.

### F1 disposition: implemented, source counterexample resolved

Operations:6494-6495 initializes both ordinary capture output and recaptured sealed amount in their consuming caller.
The former-holder COUNTRY block at 6497-6514 reads the physical STATE through PREV, bounds its sealed amount by the holder's nonnegative held ledger at 6510-6511, and debits that held ledger at 6512.
The ordinary available-reserve bound at 6499-6500 and debit at 6523 consume only the ordinary capture amount.
The sealed amount is added at 6535, after that ordinary debit, and copied to the new physical receipt at 6536.
The new holder's existing credit consumes the combined amount at operations:6597, where `add_to_variable = { missiles_captured_reserve_held = missiles_captured_reserve_amount }` remains inside the new-controller block.

The original B-to-C recapture example now moves sealed stock 8 from B's held ledger to C's held ledger and replaces the state receipt with 8.
In a mixed fixture with ordinary capture amount 3, sealed receipt 8, and B's held ledger 10, B loses ordinary reserve 3 and held reserve 8, and C receives held reserve 11.
The sealed amount is not charged against B's ordinary reserve.
If the physical sealed receipt is 8 but the former held ledger is only 5, the code transfers and debits 5, without inventing the unmatched 3.
The latter is an adversarial inconsistent-ledger case, not proof of a normal producer of missing stock.
Missing sealed receipt or held ledger retains the caller's zero output.
The unchanged same-controller receipt guard at operations:6479-6481 prevents a repeated callback from debiting or crediting again.

### F2 disposition: implemented, source counterexample and incoming receipt gate resolved

Effects:848, 862, and 870-873 now accumulate site count, capacity, and region membership on the actual COUNTRY PREV of the controlled-state iterator.
The PREV inside the country accumulator block refers back to the physical STATE for its capacity and region reads.
The snapshot at operations:4560-4572 and its hardened predicate at operation triggers:595-601 operate on the current country and its controlled states.
The nested long-reach snapshot at `common\scripted_effects\032_missiles_achievement_effects.txt`:756-775 also uses the corrected network helper and current-country durable fields.
The inspected site-network, site-damage, and long-reach recorders and their receipt finalizers publish their durable achievement fields on that current country.

Incoming damage now requires the event target and verifies its current controller against COUNTRY PREV at operations:4581-4583.
The producer saves that STATE target at 4676 and writes its incoming facts on the state at 4685-4712.
The consumer reads the supplied facts explicitly through the STATE target at 4591-4610 and copies the durable incident record onto the defender.
The producer calls the consumer at 4732, then clears the state scratch at 4735-4750.
Those are normal state variables, so they survive the synchronous consumer call and do not depend on temporary-output lifetime.
The consumer sends the existing defender receiver at 4667, and operations:6790-6806 performs the final owner-bound network, custody, status, and phase refresh.
The receiver uses the durable copied incident facts rather than the cleared producer scratch.

Region-probe closure inspected at effects:668-709: `missiles_region_probe_states`, `missiles_region_probe_found`, and `missiles_region_probe_found_id` are created on original ROOT and cleared at 705-707.
The only retained region result is written through the exact saved STATE target at 702-703.
Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`:4324-4325 explicitly describes the loop `value` and `break` variables as temporary, so `missiles_region_probe_id` is not an uncleared normal country variable.
That documentation file's SHA-256 was `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`.
No persistent foreign-country mutation was found in the inspected network, snapshot, region-probe, and incoming-damage closure.
Closing a previous defender incident can call the phase helper before the final receiver, but its source writes are current-country local and the final receiver restores the defender ROOT context.
This conclusion concerns source scope and writes, not observed engine execution or native event delivery.

### F3 disposition: implemented, helper phase-refresh contract resolved

Operations:2061 calls `missiles_set_program_phases` unconditionally after isolation changes the physical markers, recalculates network/custody, and optionally closes the rogue incident.
The no-warning/no-rogue counterexample from F3 therefore receives a replacement phase after its prepared receipt closes.
Isolating the last usable site can select establishment through the existing phase helper.
The addition does not change the refund/loss mode or charge any extra reserve.

### Insufficient escrow disposition: unresolved robustness case, no normal producer established

The settlement guard at operations:3307-3316 still accepts a matching active uncommitted operation without proving sufficient escrow.
Refund at effects:582-588 requires both the receipt flag and escrow at least equal to the operation's missile cost.
For a deliberately inconsistent fixture with free reserve 6, escrow 1, operation cost 4, matching site allocation 2, and loss mode one, abort does not refund, settlement subtracts 2 from free reserve at operations:3340, and cleanup zeros the remaining escrow at 6257.
In isolation's refund mode, the same malformed fixture loses its remaining escrow 1 when cleanup runs, without returning it.
Thus the helper is not a repairing reconciliation path for insufficient escrow, and tests should identify the fixture as inconsistent rather than report a successful full refund.

The bounded producer review found no normal path that creates this state from valid input.
Reservation at effects:565-572 adds the exact positive missile cost to escrow and marks its receipt in one synchronous helper.
The only normal escrow decrement found is the guarded exact refund at effects:586, with cleanup/removal zeroing it as the operation closes.
Targeted searches found no additional external escrow or receipt-flag writer and no production caller of the unguarded reserve/refund aliases.
The frozen operation missile cost is calculated at operations:3402 before receipt creation/reservation at 3424-3425, and its sole production calculator call is in that preflight.
Normal preparation entry at 3448 and preparation eligibility at operation triggers:184-193 reject an existing active operation.
Cost previews at operations:2351-2362 write separate preview fields, not the reserved operation cost.
Special-payload reservation rejection refunds before the failed preparation is cleaned up at operations:3376-3382 and 3438-3441.
This supports retaining the insufficient-escrow scenario as adversarial robustness uncertainty rather than a demonstrated normal-path regression.

### Follow-up limits

The F1-F3 repairs are implemented and resolve the inspected source counterexamples, with no additional gameplay blocker found in these bounded additions.
Only this handoff was appended by the subagent, with no gameplay writes, Git writes, launches, subagent spawning, simplification, or fallback.
The events and subagents skills remain the applicable audit guidance already read for this task.
Parent actual-source ledger tests are concurrent work and were neither run nor claimed here.
The earlier helper-documentation follow-up remains with the parent, and this review does not establish native timing, callback execution, runtime balance, or full accepted-spec completion.

## Biological caller-output follow-up, 2026-10-07

Disposition: `implemented`, source lifetime gap resolved under the parent's explicitly requested two-initializer repair.
Verified `missiles_reserve_operation_payload` initializes `missiles_biological_payload_debit_proof = constant:bio_lifecycle_proof.missing` at operations:4212 immediately before the helper at 4213 and consumes its supplied proof at 4215, while `missiles_consume_special_payload` does the same at 4392, 4393, and 4395.
Both callers own the output storage before helper entry, preserve its returned success modification, and reset stale proof on each invocation.
Reviewed operations SHA-256: `5EC05957945AD6F2F2E71ADF4091EDECA7B08E57A233F8267585B7428CBCD6E7`.
The core effects and operation-trigger hashes still match the preceding F1-F3 review.

The earlier capture-output documentation follow-up is also resolved by the current `common\scripted_effects\032_missiles_operations_effects.md`:5 and 9-11, which explicitly documents caller-owned capture, recapture, and biological outputs.
The parent reports the source lifetime regression and all eight payload tests passing, which is attributed parent evidence and was not rerun by this subagent.
Only this handoff was appended, with no gameplay or Git writes, simplification, fallback, engine-proof claim, or change to the remaining adversarial insufficient-escrow disposition.

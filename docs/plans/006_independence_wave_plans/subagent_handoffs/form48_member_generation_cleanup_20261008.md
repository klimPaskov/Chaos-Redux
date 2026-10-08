# FORM-48 member-generation cleanup review

Date: 2026-10-08.
Role: chaosx_scripted_system_architect; read-only lifecycle follow-up.
Disposition: confirmed source defect; accepted correction queued for the parent's separate R4 transaction after the frozen comparison.
Only this new handoff was written for R4; core FORM-48 effects/triggers, R3, the fourteen-file baseline, Git/index, admission, assets, workbook, and game state were not changed.
The full Event 006 goal remains active.

## Confirmed defect

The exact helper is `has_independence_wave_form48_current_autonomous_binding`, not `has_current_independence_wave_form48_current_autonomous_binding`.
Its source is `common/scripted_triggers/006_independence_wave_form48_triggers.txt:287-302`.
At 294 it compares the member's current `independence_wave_generation_id` to `independence_wave_form48_autonomous_carrier_generation`.
The installer at `common/scripted_effects/006_independence_wave_form48_effects.txt:57-64` stores `ROOT.independence_wave_generation_id` in that latter field, where ROOT is the carrier.
It records no separate member birth-generation receipt.

`independence_wave_prepare_origin_state` at `common/scripted_effects/006_independence_wave_effects.txt:715-740` resets the country, advances the global generation counter for the ordinary Event 006 branch, and assigns that generation to the individual country at 738.
Individual countries therefore need not share a birth generation.
With carrier generation 100 and member generation 101, the installed carrier snapshot is 100: the outer member check `101 == 100` fails even though the inner carrier check `100 == 100` is correct.
This is a mismatch between two owners' generation identities, not a broken carrier snapshot assignment.

The helper's only direct consumer found by the repository search is the guarded block in `independence_wave_form48_remove_event6_autonomous_relations` at effects 610-654, with the guard at 614.
When it rejects a valid distinct-generation member, all four ownership-directed native relation removals and the carrier's departure/binding-state update are skipped.
The function then unconditionally clears the four relation ownership flags and the carrier pointer/generation at 648-653.
Thus the source cleanup path can leave its owned relations without the receipts needed for a later precise removal, and fail to publish member departure to the carrier.
No observed native relation leak is claimed; actual engine relation lifetime remains separate evidence.

Equal numbers are not proof of a valid member incarnation.
If stale member binding fields survive in a source state whose new member generation happens to equal the saved carrier generation, the current guard has no recorded member installation generation with which to reject that state.
This is a source authorization weakness, not a claim that the ordinary monotonic counter naturally produces such a coincidence or that the normal cleanup always preserves stale fields.

## Complete cleanup chains and ordering

| Entry | Source chain and order |
| --- | --- |
| Member or carrier origin reset | Main effects `independence_wave_reset_current_generation:468` -> package dispatch at 470 -> `independence_wave_dispatch_pacific_package_cleanup` -> FORM-48 origin/runtime cleanup; current generation is not erased until main effects 612 |
| Origin end | `independence_wave_end_active_origin:3112` -> package cleanup at 3133, then decision-layer cleanup; FORM-48 runs while origin/package provenance remains addressable |
| Pacific dispatch | Pacific package effects 1062-1072 recognizes HBX/IW-184, HAW/IW-173 or FSM/IW-179 and calls `independence_wave_form48_origin_cleanup` before package-specific teardown |
| Shared formable teardown | `independence_wave_cleanup_decision_layer:1147-1148` -> `independence_wave_formable_cleanup_runtime:3169`; FORM-48 origin cleanup at 3195 precedes clearing member arrays at 3197 and loaded profile at 3198 |
| Failed formation / partial integration | `independence_wave_formable_fail_transaction:2865` closes founding invitations, then the FORM-48 branch at 2886-2889 calls rollback; `independence_wave_form48_rollback_identity:694-715` cleans frozen autonomous members before dropping uncommitted identity flags |
| Dissolution decision | `independence_wave_form48_dissolve_pacific_federation:376-401` -> remove_effect calls `independence_wave_form48_dissolve_federation:590-607` -> shared formable cleanup -> FORM-48 runtime cleanup |

`independence_wave_form48_origin_cleanup:767-769` delegates to runtime cleanup at 718-765.
That function first retires native missions/decisions, clears cycle responses/compact ideas, visits frozen member rows at 730, and clears current-country member state at 731; only then does it drop carrier identity/public state and numeric ledger values.
`independence_wave_form48_clear_autonomous_member_state:656-665` clears cycle responses/ideas, calls the defective relation-removal path at 659, then clears the member flag, invitation receipts, and family.
Repeated cleanup cannot repair a skipped relation undo once the first call has already removed its ownership flags and pointer.
Do not compensate by removing unowned relations indiscriminately.

The frozen-member walker at 667-692 currently checks pointer, carrier-generation snapshot, family, and array alignment, but does not compare the visited member's current generation to the frozen generation row at the same index.
It calls the destructive member-state cleanup after that weaker filter.
This is relevant to R4: a correction only inside the later relation guard does not protect an unrelated/stale member incarnation from the earlier response/idea clearing.

## Smallest accepted-contract owner correction

1. At install, before any owned relation is granted, add a separate normal receipt such as `independence_wave_form48_autonomous_member_generation = independence_wave_generation_id` in the member scope.
2. Retain the existing carrier pointer and carrier-generation snapshot from ROOT.
3. In `has_independence_wave_form48_current_autonomous_binding`, require the new member receipt and compare current member generation to it; preserve carrier existence/family proof and compare actual carrier generation to the existing carrier snapshot.
4. Clear the new member-generation receipt with the existing binding pointer/generation after owned relation undo in `independence_wave_form48_remove_event6_autonomous_relations`.
5. Before `cleanup_frozen_autonomous_members` invokes destructive member cleanup, validate the exact frozen member-generation row and the corrected binding proof in addition to its existing pointer/family/carrier-generation checks.
The paired row can be read as the carrier's `independence_wave_formable_member_generation_entries^independence_wave_form48_cleanup_member_index` in the member loop's caller scope; keep the index temporary unscoped.

No generation guard should be deleted, weakened, or replaced by equality between member and carrier generations.
An absent new receipt is not authority to infer a member generation from the carrier snapshot.
Do not mix R4 into the R3 display helper or silently extend neighbouring availability/AI gates while fixing cleanup.
The existing display already verifies the member's own frozen row independently and remains unchanged.
The parent owns the exact patch and transaction after baseline completion; no proposed correction above was applied by this reviewer.

## Member-array persistence and R3 proof

The successful commit tail at `006_independence_wave_formable_registry_effects.txt:3043-3115` publishes committed state and initializes FORM-48, then closes the founding proposal.
`independence_wave_formable_close_founding_proposal:827-863` clears invitation arrays/flags and proposal fields, not the frozen member country/generation/anchor/consent arrays.
The actual member-array clearer at 664-680 is used by pre-commit ledger rebuilding and shared runtime teardown; the FORM-48 teardown consumes the frozen rows before the latter clear.
The direct caller scan also found signature-family and ready-formable rebuilding/cleanup consumers, not an unconditional clear in the successful FORM-48 commit tail.
Accordingly, R3's committed-state proof has actual retained member rows to read; this is a source lifetime trace, not a duplicated assumption or a claim that every arbitrary external consumer preserves the arrays forever.
R3's owned source hashes remain those published in its handoff, including display trigger `0a88413354580e3daad68d9a74417f202a5fa83c9d6032595ddbaac31607f175`.

## Weighted callsite classification

The defective binding helper is not called directly by `ai_will_do` in the searched source; it authorizes cleanup effects.
However, its guarded block clears `independence_wave_form48_all_autonomous_members_bound` and sets `independence_wave_form48_member_departed` on an active carrier at effects 638-646.
Those flags feed `has_independence_wave_form48_dissolution_pressure` at triggers 443-455 and the dissolution action's visible/available gates at decisions 381-382.
The same flags feed separate authored major-factor AI modifiers at decision lines 390-391.
Correct cleanup therefore changes relevant score inputs and eligibility even if every numerical coefficient stays untouched.
R4 should participate in the parent's probability-auditor baseline/compare cycle for these lifecycle-induced states; an indirect flag writer is not an unchanged-score proof.

Named source scenarios should include valid distinct-generation removal with each owned direction, no owned receipts/pre-existing relations, missing/stale own receipt, stale carrier snapshot, stale frozen member row, numerical generation coincidence, member origin end, carrier teardown, partial rollback and repeated cleanup.
Keep current IW-179 admission and native unattainability limits separate from committed-state source fixtures.
No balance target, coefficient change, scenario evaluation, or probability comparison was performed here.

## Read-only evidence

The connected source_lookup schema was used with bounded symbol reads, includeReferences for consumers, and a narrow source continuation.
It returned one non-shadowed definition for the exact binding helper at 287-302 and relation-removal helper at 610-654 under indexed revision `fab530ff4c1e7c35bcbf78210ce6dc6dfd95e0088c3134afe339bd5defb466e2`.
The relation-removal continuation from 640 to 654 completed under revision `f3e1e769183dcb6442bd21211ecd25b7d97d8cce1e70d0f933609f80786054fd` after shared indexing changed.
Reference discovery was incomplete (`referencesComplete = false`, 20,220 unresolved workspace references), so the complete caller/order findings above come from the direct source reads/search, not a claimed complete indexed graph.
No artifact URI was emitted by those source lookups.

Probability discovery used `mission_ai_will_do` for the timed dissolution decision source object, identifier `independence_wave_form48_dissolve_pacific_federation`.
It returned one candidate, `poolComplete = false`, and no complete required-input discovery under source revision `db23bad509bf382433715e76deee3c7457ec5b958d2ad07fceb7702f84f3a546`, analyzer source hash `d71e337e36fd0b0047128160c3e63a7c352912244603268781ef3cff6ecd30ed`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/24c8fc2ab65a6699f56f8cdcdadce21a4c04158c5be323db7469573d1f1c28d6/3cd462806128c4f483cbcde715198e14e2d681704fb3ec88f8aa73bfa83235e1/probability-inspect-d71e337e36fd.json`, declared 6,957 bytes.
This is adapter/candidate discovery only, not a numerical baseline or a complete runtime candidate pool.

The actual source guard equation was checked with other required fields assumed valid: member/carrier/saved-carrier generations 101/100/100 return false; 100/100/100 return true; 100/101/100 return false.
The equality checks were matched against the actual helper body before this calculation.
These three input/result receipts illustrate the wrong-owner comparison only; they do not execute the native helper or assert that coincident stale values naturally occur.

Read-only source hashes at the R4 audit were: FORM-48 trigger `4a96541f67c525067f455981fc7d3c82c4d7e5512d506a7e0878e082f10a7173`, FORM-48 effects `e403280c4108300df7bd7949f82b495ffd741bea24576e18271b488a55bdd2d4`, and formable registry effects `781c75b80725e184af4420aefebbd4bc510374f78c9b38f45cb752fa3d628454`.
These reflect parent-owned source updates since the R3 review, not reviewer edits.
Existing installed/offline variable scope, array-index, and temporary-lifetime references retained in the R3 handoff support the owner/value distinctions; no new engine syntax is claimed implemented or validated by this read-only proposal.

## Actual R3 case input/result receipt

No private script path exists.
The R3 evaluator was executed via Python stdin and retained only in session memory; no script file or broad tool was created.
Its published 35 cases used the actual R3 bodies and existing unweighted predicates with supplied native primitives and conservative temporary call frames.
The exact common fixture was:

- Carrier ID 901: original HBX, package 184, anchor/capital/owned/controlled state 378, generation 40, cosmetic PFX, active origin and committed/initialized FORM-48 carrier flags; family 48 and committed transaction enum read from actual constants.
- HAW ID 902: package 173, anchor 629, own generation 41; FSM ID 903: package 179, anchor 684, own generation 42; both have active origin, autonomous-member flag, carrier pointer 901, carrier snapshot 40 and family 48.
- Carrier member arrays: IDs `[901,902,903]`, generations `[40,41,42]`, anchors `[378,629,684]`, consent values `[consenting_member,consenting_member,consenting_member]` from the actual constant.
- Other HBX ID 904: copied carrier fixture, own generation 99 and shipping 88, deliberately not the requested carrier; copied member arrays still identify 901.
- Global active arrays: IDs `[904,901,902,903]`, generations `[99,40,41,42]`; global PFX identity flag true; native access/guarantee sets and owned direction receipts initially empty.
- Carrier metric vector: shipping 11, industry 22, defense 33, autonomy 44, strain 55, cycles 6.

Every live result was key `independence_wave_form48_federal_compact_live_desc` and output vector `[901,11,22,33,44,55,6]`.
Every rejection was key `independence_wave_form48_display_unavailable` and seven reset zeros; no fake name or default ledger was formatted.

| Actual case inputs (delta from fixture) | Viewer | Result |
| --- | --- | --- |
| Unchanged carrier self | 901 | Live |
| Unchanged bound HAW | 902 | Live |
| Unchanged bound FSM | 903 | Live |
| Other HBX appears first, unchanged | 902 | Live 901 |
| Other 904 own/registered generation both set to 40 | 902 | Live 901 |
| Carrier global paired generation at index 1 set to 39 | 902 | N/A |
| Viewer global paired generation at index 2 set to 39 | 902 | N/A |
| Frozen member generation at index 1 set to 39 | 902 | N/A |
| Member saved carrier generation set to 39 | 902 | N/A |
| Member carrier pointer removed | 902 | N/A |
| Carrier object 901 removed, registry retained | 902 | N/A |
| Carrier origin_ended flag set | 902 | N/A |
| Viewer origin_ended flag set | 902 | N/A |
| Carrier ID/gen row removed together from global arrays | 902 | N/A |
| Last global generation removed only | 901 | N/A |
| Last member generation removed only | 902 | N/A |
| Carrier package changed to 177 | 901 | N/A |
| Carrier controlled-state set emptied | 901 | N/A |
| Carrier family changed to zero | 901 | N/A |
| Carrier strain variable removed | 901 | N/A |
| Member ledger ID at index 1 changed to 905 | 902 | N/A |
| Carrier self ledger generation at index 0 changed to 39 | 902 | N/A |
| Carrier self ledger ID at index 0 changed to 905 | 902 | N/A |
| Member pointer/saved carrier gen changed to 904/99 | 902 | N/A; copied other ledger rejected |
| Access and guarantee sets contain both 902->901 and 901->902, no owned receipts | 902 | Live |
| Member->carrier access receipt set but only 901->902 access exists | 902 | N/A |
| Each of four receipt/direction pairs individually set with its exact relation: member access, member guarantee, carrier access, carrier guarantee | 902 | Four Live cases |
| Each of those four receipt flags individually set without its exact relation | 902 | Four N/A cases |
| Same temporary context: valid, remove member pointer, then restore 901 | 902 | Live -> N/A/reset -> fresh Live |

This table represents all 35 cases; grouped rows explicitly account for the four receipt successes and four failures.
The evaluator also asserted no persistent fixture-world mutation, no private helper temporary escaping return, and caller initialization at both nested proof boundaries.
These are actual source-model receipts, not native VM, live/save, formatted text, admission or balance evidence.
The R3 source/text/color/ownership checks and all implementation files remain untouched by this R4 report.

No implementation simplification or fallback was applied; R4 has deliberately not been implemented while the parent completes its baseline/compare transaction.
No game, log, save, workbook, asset, Git, index or other document was requested or modified.

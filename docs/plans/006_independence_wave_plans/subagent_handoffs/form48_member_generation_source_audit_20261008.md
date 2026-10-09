# FORM-48 member-generation owner-patch source audit

Date: 2026-10-08.
Role: chaosx_scripted_system_architect, read-only gameplay review.
Disposition: parent-applied R4 correction supported by the bounded actual-source cleanup cases; no definite residual defect found in the new lifecycle hunks.
This audit verifies the parent's accepted correction from `form48_member_generation_cleanup_20261008.md`; it does not expand the design or close full Event 006 acceptance.
The parent owns current API/MCP documentation and the probability auditor owns the separate thirteen-scenario baseline/compare transaction.

## Source verdict and exact hunks

The parent fixed the wrong-owner generation comparison without requiring member and carrier birth generations to equal each other.
The installer at `common/scripted_effects/006_independence_wave_form48_effects.txt:57-87` saves member-local `independence_wave_form48_autonomous_member_generation = independence_wave_generation_id` at 63, after the ROOT carrier generation at 62 and before the first owned relation grant at 66.
The corrected `has_independence_wave_form48_current_autonomous_binding` at `common/scripted_triggers/006_independence_wave_form48_triggers.txt:288-304` requires that own receipt at 293 and compares member current generation to it at 296.
The existing carrier pointer, both families, carrier existence and carrier current generation versus the member's carrier-generation snapshot remain required; the latter comparison remains at 302.

Relation removal at effects 611-656 keeps the four original directional operations and ownership flags.
It clears the new member receipt at 655 beside the existing carrier pointer/generation clear at 653-654.
The frozen walker at 669-696 adds member current generation versus `PREV.independence_wave_formable_member_generation_entries^independence_wave_form48_cleanup_member_index` at 687 and the corrected binding predicate at 688.
Both checks occur in the limit before the first destructive member-state call at 690.
The nested clear helper at 658-666 still begins with response and compact-idea removal; the new outer gate is therefore necessary and correctly placed.

Inside the walker member scope, PREV is the carrier being cleaned, regardless of ROOT.
The nested carrier-pointer scope's `tag = PREV.PREV` matches that same caller carrier, while the new row read uses its normal array and the unscoped temporary index.
The actual index is initialized at 672 before scope entry and incremented at 693 after the member returns.
The binding helper creates no temporary outputs that could overwrite it.
The third-country ROOT fixture exercises this distinction directly.

Comparison against the parent's frozen R4 files shows exactly three effects hunks and one trigger hunk including its explanatory comment.
No other FORM-48 effect/trigger logic, AI coefficient, availability gate, ROOT/PREV relation direction or ownership receipt was changed in that comparison.
The full narrow source differences are retained in `case_receipt.json`, together with before/current hashes.
No source patch was made by this reviewer.

## Actual-source cases and results

Runnable evidence: `docs/plans/006_independence_wave_plans/evidence_20261008/form48_member_generation_source/actual_source_cases.py`.
Run from the mod root: `python docs/plans/006_independence_wave_plans/evidence_20261008/form48_member_generation_source/actual_source_cases.py`.
The successful run records 25 passing assertion cases in the adjacent `case_receipt.json`, including two explicit preparation records for repeated-cleanup cases.
Each record retains actual input/output worlds, helper, scope inputs where recorded, and the ordered mutation trace.
This is the existing R1 parser/evaluator reused through its parser functions and VM class; its prior tests and output writes are not executed.
Only narrow R4 native primitives and scoped array/variable resolution were added in the new evidence runner.

| Case inputs | Source result |
| --- | --- |
| Member 101, carrier 100, valid own/carrier receipts and four owned directions | all four relations removed; unrelated guarantee retained; carrier all-bound flag cleared and member-departed flag set; all three binding pointer/generation fields cleared |
| Member current generation 102, installed own receipt 101 | no diplomatic removal and no carrier mutation; direct helper retires stale member binding receipts |
| Carrier current generation 99, saved carrier receipt 100 | no diplomatic removal and no carrier mutation |
| Missing own member receipt | no diplomatic removal and no carrier mutation |
| Member current generation equals carrier number 100, but own receipt remains 101 | rejected; numerical coincidence grants no authority |
| Carrier object exists flag false | no diplomatic removal |
| Walker row remains 101, new member current and own receipt both 102 | entire new member world preserved, including responses, ideas, decisions, flags, binding and relations |
| Walker row updated to 102 but own binding receipt remains 101 | entire world preserved |
| Walker missing own receipt or stale carrier generation | two whole-world preservation cases; no destructive primitive called |
| Another carrier has copied ledger/family/generation, but member pointer still identifies the original carrier | copied carrier walker leaves whole world intact |
| Unaligned member arrays | whole world intact |
| Valid walker with ROOT a third country, current scope the actual carrier | member responses/ideas and FORM-48 decisions removed; unrelated idea/decision retained; four owned relations removed and departure inputs published |
| Repeated walker after valid cleanup | no further primitive call or world change |
| Repeated direct relation cleanup after valid removal | no second diplomatic removal and no world change; harmless existing receipt-clear operations may repeat |
| Actual installer with no four relations present | own generation 101 captured before all four grants; carrier receipt remains 100 |
| Four pre-existing relations, no ownership receipts | all four preserved by cleanup |
| Each of the four ownership receipts selected alone, other three directions pre-existing/unowned | four cases; only the selected exact direction removed |
| Actual installer and cleanup when all four relations already exist | installer sets no ownership receipt or grant; cleanup preserves all four |
| Actual rollback before postformation initialization and without integration-committed flag | valid frozen member still cleaned; owned relations, response work and compact ideas removed before cosmetic identity is dropped |

The repeated walker and direct cleanup each have a preceding valid setup record, bringing the table's grouped executions to 25.
No campaign admission claim is implied by these constructed member/carrier states; in particular IW-179's existing fail-closed admission is not changed or bypassed.

Direct invalid-binding cleanup does not mean a wholly unchanged member world.
Its pre-existing unconditional tail still retires four ownership flags and the pointer/carrier receipt, now also the member receipt.
The invalid direct cases assert no native relation removal and no carrier change, and explicitly assert this receipt retirement.
The walker cases instead assert complete world preservation because the new authority gate prevents calling any response, idea, relation or member-state clearer on a rejected incarnation.
This distinction is deliberate accepted cleanup behavior, not an invented fallback or a newly weakened guard.

Rollback remains usable before postformation initialization because corrected binding requires installed pointer/family/generation receipts rather than the stricter postformation surface.
The rollback trace sets the carrier's member-departed flag during valid member removal and subsequently clears it during identity rollback, preserving the existing ordering.
The ordinary valid walker leaves departure inputs set for the active carrier.
The full dissolution-pressure predicate and native decision scoring were not executed by this source subset; the flag changes are the exact inputs consumed downstream.

## Fixtures and native primitive assumptions

IDs are source-model surrogates: carrier 901, member 902 and unrelated ROOT 903.
Carrier own generation is 100 and FORM-48 family is read from the current constants; member own generation is 101, member saved carrier generation is 100, own installation receipt is 101 and carrier pointer is 901.
Carrier frozen country/generation/anchor/consent arrays are `[901,902]`, `[100,101]`, `[378,629]`, `[1,1]` and aligned; consent/anchor values are fixture metadata, not eligibility or owned-state proof in this cleanup subset.
The unrelated country generation 999 differs from both binding owners.
Original-tag identity is unused by these exact cleanup bodies and represented as fixture metadata; no template/static/dynamic country creation is simulated.
The source evaluator does not infer hidden membership validity from that metadata.

Member fixture includes the six exact response flags and six response decisions parsed from the production clearer, both compact ideas parsed from the production remover, invitation authorization, and an unrelated idea/decision.
The four relation entries are member-to-carrier access/guarantee and carrier-to-member access/guarantee, with an unrelated member-to-third-country guarantee always present.
Installer tests start without membership binding; pre-existing relation tests supply those relations before installation so its actual ownership conditions execute.

Country scope/ROOT/PREV nesting, variable scope, event-target pointer storage, array element resolution, temporary lifetime, flags, idea/decision removal and diplomatic effects are supplied primitive semantics.
`diplomatic_relation active = no` is modelled as idempotent cancellation of the exact current-country-to-target relation/type; guarantee/access direction and actual native cancellation behavior remain engine evidence, not a new native proof from this runner.
An unknown production command raises rather than being silently skipped.
The actual installer, corrected binding, array-alignment helper, frozen walker, response/idea clearer, member-state clearer, relation remover and rollback bodies are parsed and executed, with a 1,000-iteration loop ceiling.
New helper temporaries are conservatively discarded on return; caller-owned temporaries retain modifications across nested calls.
The walker cases assert no leaked private temporary, but this does not prove native temporary-frame implementation.
Source bytes are checked unchanged during the case run and receipt creation.

## MCP and reference evidence limits

Live tool declarations for source_lookup, reference_context/search/read and script_validate were inspected before use.
Retained results: `evidence_20261008/form48_member_generation_source/mcp_receipts.json`.
No event-render/full-project graph or probability call was added to this exact lifecycle-hunk source review; the parent/auditor own their current domain evidence and comparison.
No required source/reference route failed or timed out here.

The binding 288-304, installer 57-87 and walker 669-696 source lookups returned complete single, non-shadowed definitions under indexed revision `108db46475e9b98b607cf5622b428578c33de59a8defb3319d33d0708f758c49`.
Relation removal 611-656 returned under revision `eda74ea79a795477a56f05ec434909fc40fab8948939850f2745a8c58b4b0364`, with its first text excerpt cut at line 651/column 27.
A narrow continuation 649-656 at that same revision completed the clear tail with nextLine/nextColumn null.
Both revisions are retained rather than implying one immutable whole-workspace index; gameplay hashes stayed unchanged during this review.
References were deliberately disabled, so this is not a complete global consumer graph.
No artifact URI was emitted by these source/reference/validation reads.

The binding trigger was validated as COUNTRY with an explicit COUNTRY binding for `var:independence_wave_form48_autonomous_carrier`.
It returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, thirteen checked commands, four unchecked `check_variable` argument blocks and no omitted findings.
The walker effect was validated as COUNTRY with explicit COUNTRY bindings for its member-array variable scope and carrier-pointer scope.
It returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, three checked commands, one unresolved `independence_wave_formable_member_arrays_are_aligned` call and unchecked `set_temp_variable` / `while_loop_effect` argument blocks.
In particular the validator did not descend into that unchecked loop to prove its nested helpers or PREV row expression.
The actual-source cases exercise those bodies, while native parameter/scope behavior remains separate evidence.
Both validation results cover syntax/command-kind/declared-scope checks only and report parametersChecked false, documentation revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

Read directly through revision-bound references: offline Scopes line 262, PREV chaining, revision `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`; installed `documentation/effects_documentation.md:3564-3577`, diplomatic relation active/cancel form, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`; installed `documentation/triggers_documentation.md:2110-2135`, variable-to-variable equality syntax, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
The event context bundle omitted Data structures/Effects/Triggers/Scopes/On actions/Localisation; its summary is not claimed as detailed coverage.
Pertinent additional direct local reading was `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:429-442` and `1069-1076`, covering stored scope IDs, scoped normal versus unscoped temporary variables and arrays/elements; raw SHA256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
The array search returned unrelated near matches, so those local sections supplied the needed array rule rather than treating search snippets as proof.
Installed vanilla precedent `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/MTG_Britain.txt:1923-1929` uses the same COUNTRY `diplomatic_relation` block shape, though for adding a non-aggression pact; raw SHA256 `f4f1e87ed13591d861afc778e57da0b986ff4d846606dc3db14c16a7631baa32`.
That precedent supports block structure only, not four-direction cancellation semantics.

## Source and evidence identities

Frozen parent baseline manifest `evidence_20261008/form48_generation_cleanup_probability/source_manifest.json` identifies the two pre-R4 raw source snapshots and reports copiedBytesMatch true.
Those exact snapshots are read for the narrow diff; no frozen source is modified.

| File | SHA256 |
| --- | --- |
| Current FORM-48 effects | `b0f35d16bf6618cde8378a2c871763aa23bf15d034e1784dcaf5e198eade2fdf` |
| Current FORM-48 triggers | `70eb4cc9002cf551bb87ba1a21ca87a87461ecff6819020093034e90a530ddd8` |
| Frozen FORM-48 effects | `e403280c4108300df7bd7949f82b495ffd741bea24576e18271b488a55bdd2d4` |
| Frozen FORM-48 triggers | `4a96541f67c525067f455981fc7d3c82c4d7e5512d506a7e0878e082f10a7173` |
| Current member-array alignment source | `f3d279218cf006ed3ec27f21c545460ea18fb536a4464edd2a56c8996b0c8691` |
| Current constants | `efb839a1ca3242f1e88760f307fc6033bea8920d14b168001f0aca3bd6f628c8` |
| Narrow runner | `477f490e8625b6398c38f034686f2fe4be63740eed47d05ece8c06a7ef279c79` |
| Twenty-five-case receipt | `e8a36f1500cd46303a234afe0100eb714c591f4e808f2405a08fbfceb3fe715d` |
| MCP receipts | `bb7615a37a9269fbc90e2019808c95c2fed5a00435b402e5f0e6b8617c111676` |

## Ownership and remaining evidence

Only this new handoff and its new evidence directory were written.
No gameplay/API/other-document, Git/index, workbook, asset, game, log or save operation was performed.
Skills applied: chaos-redux-events and chaos-redux-subagents; the earlier decisions guidance remains applicable to the downstream weighted classification, and no skill was changed.
No simplification or fallback was applied.

R4's valid cleanup writes the member-departed/all-bound flags consumed by dissolution pressure and authored decision modifiers; unchanged coefficients do not imply unchanged downstream state or score.
The parent's retained thirteen-case `r4_scenario_assessment.json` labels its prepatch baseline partial and separates synthetic states from native observations.
Current probability comparison and parent native validation remain their own completion gates; this report neither reruns that audit nor upgrades partial results.
The new lifecycle source hunks have a clean bounded source verdict, with native VM behavior, native admission/reachability and full weighted evidence explicitly unresolved here.

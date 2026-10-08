# D34 owner dynamic-target source audit

Current verdict: the parent's epoch-pinned correction resolves the recorded missing-row counterexample in all 26 bounded actual-source cases.
The initial risk review below is retained as historical evidence; the final section, "Third-receipt correction: bounded source closure", supersedes its outstanding R1 risk disposition.

Date: 2026-10-08.
Role: chaosx_scripted_system_architect, read-only owner-patch review.
Historical initial disposition: caller/target correction was supported by the bounded source cases, with a definite registration immutability counterexample requiring parent correction.
Current disposition: the final third-receipt section and 26-case replay close that bounded source finding; native/probability gates remain partial.
No gameplay patch, API documentation edit, frozen-baseline mutation, Git/index operation, workbook, asset, game launch or log request was made.
The parent owns application and the ongoing probability comparison; no balance change is recommended here.

## Immediate verdict

The target helper correctly checks the decision's FROM country, not ROOT; its paired-array iterator matches the exact country and generation row.
The ordinary static foreign branch is preserved, while invalid custom templates, Event 021/civil-war dynamic origins, absent/stale registration, bad provenance and lost anchor control are rejected in the source fixtures.
The three decision bodies retain their original target lists, coefficients, payments, effects and timers after removing only the intended dynamic-targeting declaration and hidden FROM guard for comparison.
However, registration's claim that a same-generation call cannot restamp changed identity is true only while the valid row remains present.
When that cache row is missing, the actual registration helper overwrites existing birth snapshots from current mutable fields even without a new generation, and the actual target guard then accepts the wrong package identity.
This is a definite source contract counterexample, not an observed native exploit or proof that the normal engine naturally loses a row.
Audit expansion stopped at that risk as requested.

## Exact counterexample and recommendation

Owner source: `common/scripted_effects/006_independence_wave_effects.txt:1974-1990`, `independence_wave_register_active_country`.
It reconciles the registry, then appends/stamps only under active-country, aligned-array and absent-country-row conditions.
The stamp writes at 1986-1987 do not distinguish first publication of a new generation from repair/republication of a missing row within the same generation.

Executed actual-source sequence:

1. D01 is a dynamic AFX-origin country, current generation 101, package 6, held anchor 34, completed setup and current force-generation receipt 101.
2. Register into an empty aligned registry: country row 1001/gen 101 and birth snapshots package 6/original-tag surrogate 501 are published.
3. Change only current package to 7 and register again while the row is present: the birth package remains 6 and no snapshot write occurs; this correctly rejects changed identity.
4. Remove that country/gen row together, retaining current generation 101 and the existing package-6/original-501 birth snapshots.
5. Call the same production register helper again: it re-adds gen 101 and overwrites the birth package with 7.
6. Call the production target predicate: it returns true, because current package 7 now matches the restamped receipt, original-tag receipt still matches AFX, force/current generations match, the anchor is held, and the repaired row is exact.

The receipt preserves each input/world, normal-variable write, final world and target result.
Nothing in this sequence changes the actual country generation; the predicate need not lose its normal force-generation receipt for the counterexample.
AFX with a Frisia package-7 receipt is sufficient to expose the wrong-generation-restamp boundary because the target helper relies on the birth snapshot rather than independently re-deriving the exact package/original-tag identity contract.

Smallest recommendation: pin the birth tuple to its own published generation receipt rather than to presence of a mutable registry-cache row.
A same-generation missing/stale-row repair may restore the paired row but must preserve the original package/original-tag snapshots and continue to reject changed current identity.
A genuinely renewed generation may capture a newly validated tuple.
Missing or mismatched old tuple receipts should fail closed rather than be silently inferred from mutable current fields.
Do not remove the comparison, widen targets, change coefficients, or synthesize a fallback identity.
The parent must explicitly authorize/apply any extra registration patch; this reviewer made none while the frozen comparison was active.

## Scope, paired-row and native getter review

`is_independence_wave_current_diplomatic_target`, `common/scripted_triggers/006_independence_wave_diplomatic_target_triggers.txt:11-53`, is called inside FROM by the three owned decisions at 780, 1462 and 1831.
Its root remains the actor, but its current scope is the target.
`any_of` leaves that scope unchanged and supplies private value/index temporaries.
Entering `var:independence_wave_diplomatic_registry_country` makes PREV the original target; `tag = PREV` therefore matches the exact row country, not merely the same original tag or the actor.
The row's current generation is compared to the aligned global generation entry at the provided index.
The D02 pointer-mismatch case gave D02 the same original tag and generation as D01 and made D02 own/control its anchor, so rejection specifically exercises the wrong-country row rather than an earlier anchor/gen failure.

The anchor variable scope is entered from the target, and `is_owned_by = PREV` / `is_controlled_by = PREV` refer to that target.
`has_independence_wave_force_package_for_current_generation` compares its local saved generation to the current target generation; the actor's distinct generation is not used.
The ordinary branch requires a non-dynamic target outside the Event 006 custom-template ownership set, preserving ordinary static foreign countries.
Dynamic origins instead require Event 006 origin/setup, current generation, stored package/original provenance, held anchor and exact paired registration.

Native dynamic-variable documentation was read through reference_read at `documentation/dynamic_variables_documentation.md:710-712`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`, documenting `original_tag` as returning the original tag of the country.
The getter used by both registration and comparison is appropriate to dynamic original identity; the evaluator supplies numeric original-tag surrogates and does not claim native enum IDs or coercion execution.
The installed `any_of` value/index rule at triggers 1515-1530, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, and the actor/FROM decision-scope rules retained in the earlier audit support this source interpretation.
No index field was guessed for `any_of_scopes`.

## Actual-source case receipt and narrow runnable evidence

The existing session R3 parser/scope/temporary-frame evaluator approach was adapted only for this helper and the actual registration/reconciliation bodies.
Runnable file: `docs/plans/006_independence_wave_plans/evidence_20261008/d34_dynamic_target_source/actual_source_cases.py`.
Run from the mod root: `python docs/plans/006_independence_wave_plans/evidence_20261008/d34_dynamic_target_source/actual_source_cases.py`.
It writes only its adjacent `case_receipt.json`; no source, API, frozen baseline, or score file is modified.
This is a narrow evidence test, not a general tooling package or native VM.
Production helper bodies are parsed from the current exact owner files and constant categories; the test does not replace the target or register/reconcile helpers with no-ops.
Native country/state, scope, flags, variables, arrays, `original_tag` scalar getter, event-target storage and effect primitives are supplied semantics, with a 1,000-iteration effect ceiling and conservative temporary call-frame disposal.
Trigger cases assert no persistent world mutation and no callee-created private temporaries escaping.

Fixture IDs are numeric surrogates: D01 1001, D02 1002, actor 1003, ordinary SOV 1004; AFX original-tag scalar 501, AGX 502, SOV 503, CHU 504.
The actor has generation 999 and package 43, deliberately different from D01's 101/6.
D01's state 34 is owned/controlled by D01, force-generation receipt is 101, setup/origin flags are present, and the global registry initially contains D01/gen 101.
These are source contract values, not campaign observations or admission changes.
All exact worlds and modifications are archived in `case_receipt.json`.

| Executed case | Result |
| --- | --- |
| Legal D01 AFX, actor generation differs | true |
| Missing registration | false |
| Wrong paired generation row | false |
| D02 same original and generation, D02-held anchor, but only D01 row | false |
| Missing package/original receipt | two false cases |
| Wrong package/original receipt | two false cases |
| Stale force generation | false |
| Lost anchor control | false |
| Event 021-style different origin value | false |
| Same-original civil-war target without Event 006 origin receipt | false |
| Ordinary static SOV outside registry | true; static branch does not require the Event 006 tuple |
| Invalid static custom AFX | false |
| Repeat register with present row after current package changes | old birth tuple retained; no snapshot restamp |
| Same-generation missing-row re-register after current package changes | definite risk: tuple restamped and target returned true |

There are 16 recorded cases, including grouped missing/wrong receipt cases.
The ordinary SOV fixture uses the generic fixture object's extra variables/flags, but the actual static branch exits before consuming them; absence of registry and the static/non-owned branch are what this case proves.
No new generation-renewal execution case was added after the definite risk was found; that requested scenario remains a follow-up for the parent's epoch-pinned correction.
No source-only result is presented as native reachability, formatted UI, score equality, probability completeness or gameplay acceptance.

## Decision preservation and ownership

Compared each complete patched decision against the parent's frozen pre-owner source at `evidence_20261008/d34_dynamic_pool_probability/source_snapshots/common/decisions/006_independence_wave_iw043_iw058_decisions.txt`.
After removing only the intended `targets_dynamic = yes` declaration and hidden FROM helper line, all remaining tokens—including quoted text and target order—match.
This establishes unchanged target lists, authored coefficients, payment paths, effects, native durations and timer values within these three bodies; it is not a native economic or AI-equivalence test.
The comparison receipt is `evidence_20261008/d34_dynamic_target_source/decision_preservation_receipt.json`.

| Decision | Preservation result |
| --- | --- |
| `independence_wave_iw043_dispatch_volga_trade_delegation` | all other tokens unchanged |
| `independence_wave_iw058_open_diaspora_expert_mission` | all other tokens unchanged |
| `independence_wave_iw058_request_named_external_guarantee` | all other tokens unchanged |

The target helper's iterator variables are private and initialized in its own frame; they are not output fields expected to survive return.
The registration/reconcile tests retain native normal-variable/array mutation while discarding newly created temporary keys on helper return.
No broad audit, additional MCP call, full-project generator, balancing work or implementation patch was added after the definite risk.

## MCP/source provenance and limits

The connected source_lookup read returned one non-shadowed definition for the new target helper and registration helper under revision `e9ada77167c0b1d2cb702e05927df73b38c53c238523cb361f26159e49784238`.
Registration was complete at `mod:common/scripted_effects/006_independence_wave_effects.txt:1974-1990`.
The target helper excerpt covered 11-36; its narrow continuation from 37-53 completed under shared indexed revision `ed915a0880f765a2f48dcd59dcbf9a90b648f2baddebbb8d1c336743e0304c35`.
Lookup retained exactly the three decision references at 780/1462/1831 but still reported referencesComplete false and 20,220 unresolved workspace references, so no complete global consumer graph is claimed.
The primary native original_tag reference above was a successful revision-bound read, with nextLine null.
No new native validation or score comparison was initiated by this source reviewer beyond those exact owner reads; the parent/auditor retain their requested validations and comparisons.

The parent reports its corrected 54-case comparison stage returned R1 same-score partial results and R2 unsupported dependency contexts/internal error metadata.
Those results do not negate this registration authority counterexample or establish native target eligibility.
This audit does not choose a balance target or alter/replace the ongoing frozen comparison fixtures.
R4 remains separately queued in `form48_member_generation_cleanup_20261008.md`; the lifecycle core was not patched, and R3's published display fix was not changed.

No simplification or fallback identity was applied.
The bounded source audit is complete with a risk verdict rather than an unqualified clean verdict; parent disposition and any separate authorized fix remain outstanding.

## Third-receipt correction: bounded source closure

Disposition: parent-applied R1 registration correction verified within the exact source subset; no definite residual defect found in the tested helper/registration contract.
The historical missing-row risk is resolved for the retained input sequence, while R4 remains accepted and queued separately.
This closes this read-only source follow-up and does not close full Event 006 acceptance, native engine behavior or probability evidence.

Current registration is `independence_wave_register_active_country`, `common/scripted_effects/006_independence_wave_effects.txt:1974-2006`.
Reconciliation precedes the active-country/aligned-array/absent-row append at 1975-1983.
The nested publication guard at 1986-1999 permits tuple writes only when all three receipts are absent, or when current generation is strictly greater than an existing registered generation.
The package, native `original_tag` getter and generation are written together at 2000-2002.
A missing/stale cache row is therefore repairable without granting authority to overwrite same-generation or older-generation identity.
The target helper at `common/scripted_triggers/006_independence_wave_diplomatic_target_triggers.txt:11-55` requires registered generation presence at 26 and current/registered generation equality at 30, alongside the existing package/original receipts, force-generation proof, held anchor and exact paired country/generation row.
Same-generation identity is not reconstructed from current mutable package/original fields.

The existing narrow runner was reused and rerun successfully: `python docs/plans/006_independence_wave_plans/evidence_20261008/d34_dynamic_target_source/actual_source_cases.py`.
All 26 assertions passed; `definite_registration_risk = false`, `target_accepted_after_restamp = false`, and `third_receipt_epoch_guard_passed = true` are retained in `case_receipt.json`.
The first-publication and repeat-call receipts now include the actual input immediately before each call.
Positive fixtures carry all three registration receipts.
The D02 exact-row negative fixture sets current, force and registered generations to 101 and gives D02 its held anchor, ensuring that its false result exercises country-row identity rather than a premature receipt mismatch.
The ordinary SOV fixture has no Event 006 flags or variables and still returns true through the preserved static branch.

| Correction case | Actual source result |
| --- | --- |
| First publication, all three receipts absent | paired row appended; package/original/generation tuple `[6,501,101]` published |
| Repeated registration, row present, current package changed to 7 | no tuple writes; old tuple preserved |
| Missing row, current package changed to 7, same generation 101 | row repaired; no tuple writes; old tuple preserved; target false |
| Valid same-generation missing row | row repaired; tuple `[6,501,101]` unchanged; target true |
| Valid same-generation stale cache row at generation 100 | reconciliation removes stale row and appends current row; tuple unchanged; target true |
| Genuine renewal to current/force generation 102 with valid AGX/package-7/held-state-36 fixture | stale row reconciled; tuple `[7,502,102]` published; target true |
| Older current/force generation 100 with stored generation 101 | no tuple writes; tuple `[6,501,101]` unchanged; target false |
| Only package receipt missing, same generation | missing field remains missing; no tuple writes; target false |
| Only original-tag receipt missing, same generation | missing field remains missing; no tuple writes; target false |
| Only generation receipt missing, remaining old fields present | missing field remains missing; no tuple writes; target false |

The other 16 cases retain exact caller/FROM scope, legal AFX eligibility, missing registry, wrong paired row, different same-original country, missing/wrong receipts, force-generation expiry, lost anchor control, Event 021 origin, civil-war origin, ordinary SOV and invalid static custom-template rejection coverage.
The renewal scenario supplies a new-generation identity fixture and is not a claim that a native country's original tag mutates.
The source evaluator parses the actual target, registration and reconciliation bodies and raises on unmodelled production commands; native primitive behavior remains supplied semantics.
Its temporary-frame model does not prove native temporary lifetime, and scalar surrogate values do not prove native enum coercion.

### Retained pre-fix and current identities

The pre-fix `case_receipt.json` was archived byte-for-byte as `evidence_20261008/d34_dynamic_target_source/case_receipt_before_epoch_fix.json` before replacement.
Its SHA256 is `c6edb00b244c6b9d0144807347f5faf3d28c53aae348f6736cfd45269a20a39a`; it retains the original true risk/accepted-after-restamp results and source hashes.
The historical main-effects hash is `0c41283023dc9b48ec56c64b033cb193210f669d432dc1a69293498e7fe1e4aa`; the historical diplomatic-helper hash is `67c01c57275b9cdf6649b2c042d46f541b38ecd56980db45212f341c30051db6`.

| Current file | SHA256 |
| --- | --- |
| Main effects | `12c33557710adf25160cf1d7e0066ea0258a40d1a832683fc8c831d20fe61c41` |
| Diplomatic target helper | `d6cf58214d3cb9c3c2356916847824fede5f1ad77de140f9b7d09eaf36f6c655` |
| Three timed decisions | `ef6020ddbd75e589b0cafdb2ce39a159a949821e8ea57acc70ac7158a30858d8` |
| Core FORM-48 triggers, including R2 | `4a96541f67c525067f455981fc7d3c82c4d7e5512d506a7e0878e082f10a7173` |
| Current 26-case receipt | `bc983f51ee46ec738f97de216d22a29bc54dc024e2bbff937879abc971fa8ef9` |
| Narrow runnable case script | `5c4fb49e848e62497badc0e26190466b54dff08ca000f637dc2492497ac667ac` |

The unchanged timed-decision file hash preserves applicability of the earlier three-body preservation receipt: target lists/order, authored coefficients, payment effects and timers have not changed in this epoch correction.
The paired-row and actor/FROM interpretation above remains applicable; the new generation check consumes no new output temporary, scope switch or fallback identity.
Earlier MCP revisions describe the pre-correction indexed source and are retained as historical provenance, not presented as current-patch validation.
No extra MCP/full-project audit was initiated for this requested bounded rerun; the parent owns current native validation/API publication and the probability auditor owns the same-scenario evidence pass.
The parent's R1 same-score partial and R2 unsupported/internal-error results remain partial; these source cases do not turn them into complete native or probability proof.

Owned changes for this follow-up are this report, the existing narrow evidence runner, the current receipt and the separately retained pre-fix receipt.
No gameplay/API/Git/index/workbook patch was made, no balance recommendation was introduced, and no simplification or fallback identity was applied.
`form48_member_generation_cleanup_20261008.md` remains the completed read-only R4 handoff; core R4 application and its separate baseline/compare transaction remain with the parent.
Skills used remain `chaos-redux-events`, `chaos-redux-subagents` and `chaos-redux-decisions-missions`; no skill was changed.

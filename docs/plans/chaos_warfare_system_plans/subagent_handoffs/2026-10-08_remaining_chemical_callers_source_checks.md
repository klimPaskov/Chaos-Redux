# Remaining chemical callers: independent source checks

Date: 2026-10-08.
Disposition: implemented bounded test review and reporting correction, with 46 passing cases.
Acceptance basis: the parent assigned independent recovery and review of the existing Camp and missile caller-storage tests, restricted edits to the two test artifacts when a concrete defect was found, and requested this new handoff.
The parent subsequently requested a scoped current-source check after concurrent evolution edits changed the missile full-file identity during commit preparation.
The parent then requested canonical dependency pins after an isolated candidate-tree check exposed line-ending portability failure.
The parent subsequently authorized replacing only the whole Chaos Meter file guard with a precisely scoped guard derived from the actual exercised definitions and fixture inputs.
This is source-model evidence for the 66 Camp declarations and one missile declaration already applied by their owners.
It does not establish native execution, whole chemical-system completion, or design approval beyond that assigned scope.

## Files owned and changed

- `docs/testing/2026-10-07_remaining_chemical_callers_source_tests.js`: corrected one generated limit sentence about the constant loader's lexical restriction, separated archive reconstruction from current owned-source checks for the mixed missile file, made dependency pins canonical under CRLF-to-LF conversion only, and replaced the full Chaos Meter file pin with the two exercised token definitions and exact runtime read coverage.
- `docs/testing/2026-10-07_remaining_chemical_callers_source_results.json`: regenerated from the reviewed test file against the current source.
- This handoff: added independent scope, findings, source identities, references, and limitations.

No gameplay, shared Event 026 parser/VM, constants, call sites, cleanup logic, helper documentation, Git index, or commit was changed by this review.
MCP graph and documentation integration remain parent-owned.
Skills used: `chaos-redux-events` and `chaos-redux-subagents`, including the temporary-output lifetime and conservative actual-source test requirements.

## Source integrity

The first test verifies each raw archive against its insertion manifest, verifies the exact inserted bytes at their recorded offsets, removes only that insertion, and reconstructs the raw before archive byte for byte.
It also parses the reconstructed source to verify original statement structure and order and requires 66 Camp and one missile `set_temp_variable` declarations.
Current Camp source retains whole-file CRLF-to-LF normalized equality and raw hash equality with its frozen after archive.
The current mixed missile file compares every definition of `missiles_dispatch_chemical_payload` against the frozen after AST, so a changed or duplicate owned definition fails.
Its current full-file identity differs because the peer changed `missiles_measure_evolution_pressure` and `missiles_arm_evolution_track`.
Those unrelated definitions are recorded as excluded AST differences and are not executed by these tests.
The owned chemical caller AST hash is `a18e482af3ec5b290ae57253686442a6375fe44277c88818eccbb1bf26c2985c`.
This preserves the missile baseline's other working-tree changes rather than treating the old peer commit as the current baseline.
The frozen missile baseline already contains the peer's prior civil-war site integration changes, which remain outside this declaration review and are not reverted or certified here.
No constants, random draws, policy or eligibility gates, helper calls, debit/refund paths, severity, target, timer, consequence ordering, or existing cleanup were rebalanced by these insertions.

| Source | Raw before SHA-256 | Raw frozen after SHA-256 |
| --- | --- | --- |
| `common/scripted_effects/camp_repression_rework_effects.txt` | `7c68d93e8097fc6a33af11ff7cd3bae3216dc9335f36b65ac0cdcf94aff5644c` | `cf83c6498e7cd94ebd8125f26e572113d0a83cb121829c87636cf86487a20ada` |
| `common/scripted_effects/032_missiles_operations_effects.txt` | `3ae3a6ec33c61c7bb7846c47628d9a2b978bc886b4841be09004d4722358f23f` | `5f803dd63867d0303d19e7e7e388f00ba6440130b53237ffbe961b715d0ae67b` |

Current full missile file SHA-256 at the final working run: `0ce202634f2e78686253483096df2ff76e31a003bcc4e564fae950c255172e2c`.
The preceding working run used `684eef78ad0e21eed6428516cde4d0d0ca3fbe614d51c832f0c1b81ab99a33db`, and the peer's later evolution edit changed the full-file identity during handoff preparation.
The final suite was rerun against the updated file, retained the same chemical caller AST and the same two excluded evolution definitions, and passed all 46 cases with byte-stable inputs during that run.
Current `common/script_constants/032_missiles_constants.txt` SHA-256: `28c66b9d5543126c40bdef4cc717d4229307d7f4c0c79e1ccd17d132b85b837f`, compared with the prior run's `1dabadf3281586ef3106819e5b130f0685c726c85d495a5ef59798fa3c368a94`.
The constants diff affects only `missiles_evolution_pacing`, with spread/watch fields replaced by collapse/coalescing fields.
The caller's relevant `missiles_result`, `missiles_resolution`, and `missiles_guidance_outcome` category ASTs match their preceding versions and are pinned by explicit digest in the test.
All other previously recorded inputs retain their raw hashes.
The test pins 18 shared source, trigger, tuning-file and Event 026 VM canonical hashes directly rather than reading expected hashes from a mutable result file.
The Chaos Meter file uses the two token AST guards described below, with its actual full-file raw identity still recorded and required to remain stable during each run.
All 19 preceding raw dependency pins were verified against current working bytes before computing the replacement canonical hashes, so this conversion did not accept substantive working changes.
This check covers the exercised shared definitions and refuses relevant dependency drift, while the final stability case still requires every loaded file, including both mixed missile files, to remain byte-stable during the run.

Archive and manifest roots are `docs/testing/2026-10-07_camp_chemical_lifetime/` and `docs/testing/2026-10-07_missile_chemical_retaliation/`.
The accepted Camp contract remains `proposed_insertion.json` under its archive root.
The preceding Camp patch and missile follow-up Markdown/JSON under this handoff directory were read, with their older read-only findings treated as historical evidence rather than current patch status.

## Test execution and meaningful findings

Command: `node docs/testing/2026-10-07_remaining_chemical_callers_source_tests.js`.
The recovered version passed all 46 cases, then the reporting correction passed the same 46 cases.
After the concurrent missile drift was inspected and the scoped source guard was applied, all 46 cases passed again with no failures and stable current inputs.
The canonical dependency-pin version also passes all 46 working-tree cases.
The final scoped Chaos Meter revision passes all 46 working-tree cases and all 46 cases in a nonwriting projection against the supplied extracted tree.
Two separate in-memory negative probes confirmed that the first integrity case fails for a duplicate current chemical caller and for changed shared exposure dependency bytes.
Those probes disabled the test's result-file writer, left all source files untouched, and did not replace the accepted 46-case result artifact.
The final result status is `passed_bounded_remaining_chemical_source_model`.
The shared Event 026 parser and `BaseVM` are imported unchanged from `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js`.
Every scripted call uses that VM's conservative lexical cleanup of newly created temporary fields, while inherited temporary fields retain changes.
The extension keeps actor 7, victim 9, and exact state 100 regular stores separate from the unscoped temporary store.

| Coverage | Cases | Result and scope |
| --- | --- | --- |
| Archive preservation and exact declaration contract | 2 | Original raw bodies recover exactly, the Camp declaration fields/defaults match the 66-entry contract, current owned chemical source remains unchanged, and relevant dependency identities remain pinned. |
| Camp reset forwarding | 1 | Before source retains zero of the 60 reset packet fields after return, while the declared after source retains all 60 defaults. |
| Actual Camp method getter, seven tiers with and without mastery | 14 | Five method outputs disappear before the insertion and remain after it. Exact cost is asserted for each tier, including the nerve-mastery cost factor. The other four fields are captured and checked for retained presence, rather than independently rederived tuning correctness. |
| Actual Camp exact-model stock path at cost minus one, exact cost, and cost plus one | 21 | All seven tiers reject insufficient fixture stock without debit/death, or debit the selected cylinder model once for the exact method cost and leave the expected fixture remainder. These stock boundary cases use the standard cost without mastery. |
| Camp outer eligibility and prepare rejection fixtures | 2 | Outer rejection performs no debit or death. Prepare rejection occurs after the existing debit and produces no death or site receipt, preserving current ordering without claiming refund behavior. |
| Actual missile prepare/classifier/actor history with rights absent or present | 2 | Before source drops the returned retaliation temporary. With rights present, generic persisted status is 1 while chemical history is 0. After the declaration, both are 1 and the captured unified-record field is 1. With rights absent, after history remains none 0. Missile death receipt receives the fixed sink value 25 and performs no script-side equipment debit. |
| Separate generic proportionate classifier probe | 1 | Using the missile-owned slot, a supplied tactical proof and cylinder route return proportionate 2 through the actual generic classifier. The actual strategic missile route has none/authorized coverage only. |
| Repeat shared dispatch within one supplied paid record | 1 | Two calls produce one fixed death sink and one actor history count because the actual shared dispatch guard retains its proof. This case does not execute payment. |
| Isolated Camp returned death-count probe | 1 | Actor private history receives 25 with either ownership choice. The actual Camp bridge records 0 without the ancestor-owned count slot and 25 with it. Actual local Camp state writes execute, while genocide-credit and famine calls are captured boundaries. |
| Input stability | 1 | Every input loaded by this test retained its captured byte hash during the run. |

The method getter, reset, tier-to-agent adapter, restricted-site release, actual Camp stock predicate and model debit bodies, supported prepare/classifier branches, dispatch guard, actor history, and actual Camp death bridge execute from parsed source.
The supported consequence body is deliberately restricted to its actual prefix and first civilian-death branch.
Successful Camp stock cases also traverse the actual consumer after dispatcher return and assert both `camp_site_last_month_deaths` and `genocide_last_state_deaths` equal 25, along with the captured downstream death receipt.

## Reporting defect corrected

The loader rejects a numeric literal when its fractional text contains more than five characters.
Its `unsupportedConstants` array contains 19 six-character literals, including `0.003000`.
All 19 current values are mathematically representable at five decimal places after trimming trailing zeros.
The old limit wording incorrectly implied that every rejected literal exceeded fixed-point precision.
The corrected sentence identifies a lexical loader limit and retains the fail-on-request behavior for skipped constants.
The loader, shared `ticks` function, arithmetic, fixtures, source definitions, and case count remain unchanged.
The later source-integrity revision changes only which current missile definitions and constant categories must match the audited baseline, while keeping immutable archive reconstruction and complete run-time input stability checks.

## Isolated-tree portability check

The parent supplied an extracted candidate tree at `C:/Users/klimp/AppData/Local/Temp/cbrn-remaining-callers-commit-u9t2r9t0/review-tree`.
The earlier raw dependency guard rejected its `cbrn_chemical_delivery_constants.txt`, whose raw hash is `c296cf70f13594279ef68f520c4923d93dfc7df1f4d46f6682f4c0fe08fd7c59`.
The reviewed working file's raw hash remains `de562a850a09de19d9aa37c121df3b038104ba60d67d2ed50fde862d3fc4fad3`.
Direct inspection found 238 CRLF and four bare LF endings in the working file, versus 242 CRLF and zero bare LF endings in the extracted file.
Their text is identical after CRLF-to-LF conversion, with common canonical SHA-256 `3a0e1cdfe4e57167d7c9fc15e85f7b6bfd8d46d505a3957bf5df85d2812b4b7a`.
No spaces, tabs, comments, tokens, trailing whitespace, or other content are normalized.
Raw archive before/after hashes, byte-exact insertion recovery, missile caller/category AST guards, and raw `sourceHashes` provenance remain unchanged in scope.

All 19 current raw dependency identities matched the preceding reviewed pins before replacement, and 18 of the 19 canonical dependency bodies equal the supplied tree.
One substantive mismatch remains in `common/script_constants/chaos_meter_constants.txt`.
The working file contains only three additional lines relative to the extracted version: `equipment_from_heavens_skyfall = 222`, `equipment_from_heavens_proliferation = 223`, and `equipment_from_heavens_arsenal_escape = 224`, under `chaos_meter_history_reason.special`.
Removing those three lines in memory makes the canonical file bodies equal.
Working canonical SHA-256 is `6290453b07e71f99624fa5282e89c2aa06013ae207856953956f9020ac2b4ec1`, while the extracted canonical SHA-256 is `9cf85072803d5103be9d9753b5afd7a920b23f9a8c2f78f30491fbf4b9e83cb8`.
The preceding strict whole-dependency revision rejected this substantive difference.

An in-memory projection compiled the revised test module using the extracted tree's module path and unchanged tree VM, with the result writer disabled.
The preceding canonical-only revision ran all 46 cases, with 45 passing and only the integrity case failing on the Chaos Meter dependency mismatch.
The projection did not alter the extracted tree or the accepted working-tree result artifact.
The parent then authorized the scoped Chaos Meter token guard below.
The final nonwriting projection passes all 46 cases and reads extracted Chaos Meter raw SHA-256 `3406d3d8d081f64d226bc48b3adf42c839e7122a8d88d31bfa118ae924f732c3`.
Its extracted missile full-file SHA-256 is `28bfda9fc8918ee7ed6e9a9b28c67d240e212cf613810e99f2e6adfaf514bddb`, with the same owned chemical caller AST hash `a18e482af3ec5b290ae57253686442a6375fe44277c88818eccbb1bf26c2985c`.
Its recorded unrelated definition differences against the frozen missile archive are `missiles_preflight_country_split`, `missiles_finalize_civil_war_split_child`, and `missiles_finalize_civil_war_split_parent`.
Those split changes remain outside the chemical caller test contract and are neither imported nor certified by this review.
The parent retains independent final candidate extraction and staged-tree validation.

## Scoped Chaos Meter dependency contract

A nonwriting runtime-read probe over the same 46 cases found exactly two Chaos Meter constant tokens.
Source review identifies their literal assignments in the retained first civilian-death branch of `common/scripted_effects/cbrn_consequence_effects.txt:252-254`.
The shared consequence source itself remains protected by its canonical dependency hash.
The exercised Camp bridge at `common/scripted_effects/cbrn_camp_effects.txt:77-79` and `camp_rework_record_latest_state_deaths` at `camp_repression_rework_effects.txt:2025-2050` consume the already returned scalar and do not read another Chaos Meter constant.
The fixed native-death fixture supplies 25 directly, and the captured/no-op sink fixtures contain no Chaos Meter category lookup.
There is no dynamic Chaos Meter constant-name construction in the exercised definitions or fixtures.
The 19 skipped lexical constant literals remain recorded loader exclusions, rather than executed input values.

| Exercised token | Exact definition | Field AST SHA-256 |
| --- | --- | --- |
| `constant:chaos_meter_state_death_dynamic.chemical_cap_factor` | `chemical_cap_factor = 1.45` | `dfe33d37b4c2b58d724fd996865bc54c166368e2f2b9cee1f8f8b388e8e5b81e` |
| `constant:chaos_meter_deaths_reason.chemical_attack` | `chemical_attack = 3` | `6bb8fa5abc08399ea5465e2a7bdf195d18ec0240a95b0a1fea048c5512dd0707` |

The test requires one unique category and one unique field for each token, then compares the field AST including its key, assignment operator, and literal value.
Runtime tracking requires the actual Chaos Meter read set to equal these two names exactly, so an added or removed accessed token fails the final existing stability case.
The shared parser, arithmetic, source definitions, fixtures, case count, 18 other canonical dependency pins, missile caller AST guard, missile constant-category guards, exact raw archive recovery, and raw run-provenance checks remain intact.
The guard has no exception for the unrelated reason-ID names.
Those three added IDs belong to `chaos_meter_history_reason.special`, which is neither referenced by the retained chemical consequence prefix nor read by any executed fixture or real consumer in this suite.
They therefore cannot change this bounded test contract, while the raw file hash still documents which complete file was read.

A separate nonwriting negative probe changes the used `chemical_cap_factor` literal from `1.45` to `1.46` in the test's in-memory read only.
The integrity case fails with `audited Chaos Meter token drift: constant:chaos_meter_state_death_dynamic.chemical_cap_factor`.
The probe disables the result writer and alters no source, shared VM, extracted tree, or accepted result bytes.
This proves that narrowing the dependency scope preserves rejection of changed exercised inputs, without claiming the fixed sink simulates real death arithmetic.
No native truncation or rounding rule was simulated or inferred from those excluded spellings.

## Explicit fixture and sink boundaries

Country initialization and method-tier resolution are no-op fixtures, with the intended tier supplied directly.
Actor, target, site, policy, researched-tech, agent-unlock, payload-profile, war, division, and active-retaliation-right conditions are explicit fixtures rather than complete native eligibility or policy evaluation.
The generic default payload getter supplies a placeholder that the actual caller overwrites with the Camp method cost or missile frozen quantity.
Doctrine multiplier, target protection resolution, and exposure calculation are supplied outputs.
The exposure fixture supplies civilian death fraction 1 and forwards the actual duration override.
The native population/death sink supplies the fixed return 25.
Unit damage, first-exposure shock, contamination, full state consequences, protection arithmetic, weather, masks, real atrocities, and balance are outside the model.
Condemnation, unified append, humanitarian callback, site/evidence registration, genocide credit, famine adaptation, country recalculation, and achievement sinks are captured or no-op boundaries.
Actor history assignments and local Camp state receipt writes execute, but the full external ledgers do not.
Exact model removal updates fixture stock maps only, rather than native stockpile accounting.
Missile verified-debit flag and frozen consumed quantity 40 are supplied receipts, with no payment, custody, refund, or outcome-selection proof.
The repeated-dispatch case covers one existing prepared record only.
A fresh full Camp invocation prepares a separate record and may pay again, and no whole-Camp replay or invented outer receipt is claimed.

## References and parent-owned validation

The pertinent offline and installed sections were read directly for this bounded source review.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:435-443` explains variable types, unscoped temporaries, scripted-helper return uncertainty, and preinitialized caller storage, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:7820-7827` documents `set_temp_variable` support and values, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The latter section does not itself establish native scripted-call frame cleanup, so the test remains explicitly conservative source-model evidence.
Reference routes, MCP event inspection/comparison, probability evidence, native policy/payment behavior, full ledger sinks, wider documentation reconciliation, and final commits were not run here because the parent retained those responsibilities and explicitly excluded MCP graphs, game, logs, index, and commit access from this assignment.
No unavailable-route claim is made by this review because route health was not tested here.
No balance target or probability-bearing patch was designed or applied.

## Frozen artifact identities

- Reviewed test SHA-256: `410f99652c78f96e097b5e61a19f473043928d90ab2eea82b8789077231fdc60`.
- Final working-tree result SHA-256: `29f367c46b37f7b3ef4f93bdcefea7d31638024f8f2a1b6096bc51c12c22dc71`.
- Unchanged shared Event 026 VM/parser SHA-256: `b048592fb35b86ae2dd915aec0cda54896f7d2f1c1d3a2e358bd2fe3b2e8ccf7`.

The result JSON retains all case captures, actual current full-file input hashes, scoped source-integrity metadata, excluded definition differences, skipped constant spellings, exact reference paths/spans/revisions, and fixture limitations.
No gameplay simplification or fallback was introduced in this review.
The working-tree independent source checks and the nonwriting projection against the supplied extracted tree both pass.
The recorded earlier isolated-tree dependency blocker is resolved by the parent-authorized guard derived from the actual exercised inputs.
Native execution, full sink transactions, and broader balance confidence remain unresolved outside this bounded model.

# CBRN helper output lifetime audit - 2026-10-06

Disposition: source storage repair accepted by this read-only audit; native execution remains unproved.
No gameplay file, asset, workbook, CSV or Git index was edited by this auditor.
This follow-up covers only the three named API output families and the four parent-owned effect files.

## Findings

No remaining missing caller-owned storage was found at a return boundary that consumes these outputs.
The repository search found four contamination-class refresh calls, two Air contribution calculator calls and three state-delta calls.
All six calculator callers consume their outputs and now preallocate the corresponding scalars before invocation.
Only two state-delta callers read previous/new values after return; both now preallocate those two scalars.
The consequence dispatcher does not consume these returned scalars and needs no unused-output allocation.

| Return boundary | Current source evidence | Consumption and result |
| --- | --- | --- |
| Class refresh inside state delta, before mutation | `cbrn_exposure_effects.txt:1026-1028` | Storage exists before the helper returns; its returned class is copied into the previous class. |
| Class refresh inside state delta, after mutation | `cbrn_exposure_effects.txt:1062-1064` | Storage is reset before the second call; the new class is captured separately. The previous class is a value copy and is not overwritten. |
| Class refresh for paid theater cleanup | `cbrn_doctrine_effects.txt:118-149` | The paid STATE helper owns the output before selecting the existing severity-dependent cleanup coefficient. Its outer wrapper does not consume this output after the paid helper returns. |
| Class refresh for international cleanup | `cbrn_diplomacy_effects.txt:1215-1246` | The STATE completion helper owns the output before selecting its existing severity-dependent coefficient. |
| Air calculation inside state delta | `cbrn_exposure_effects.txt:1073-1076`; `cbrn_chemical_state_effects.txt:34-109` | The delta frame owns the output before the calculator call; the following updater reads it through its nested STATE/country work. No updater writes or discards that input scalar. |
| Air calculation in explicit rebuild | `cbrn_chemical_state_effects.txt:159-169` | Each eligible STATE iteration resets output storage before the calculator call, then reads it into state/global contribution and state count. |
| Previous/new values returned to paid theater cleanup | `cbrn_doctrine_effects.txt:173-180` | Both outputs exist in the paid helper before delta invocation; actual previous minus resulting contamination is copied into the cleanup total before further calls. |
| Previous/new values returned to international cleanup | `cbrn_diplomacy_effects.txt:1259-1263,1282-1287` | Both outputs exist before invocation; actual cleanup is captured before later observation/helper work and credited to the exact provider and recipient. |
| State delta called by consequence dispatch | `cbrn_consequence_effects.txt:265-280` | No post-return read of either previous/new scalar; duration reads are separate. No additional storage is required for these unused outputs. |

The class calculator itself still writes its normal STATE class and clears that class for a clean state (`cbrn_exposure_effects.txt:987-1023`).
The Air calculator's existing class-to-contribution coefficients remain untouched (`cbrn_chemical_state_effects.txt:14-32`).
The new API note at `common/scripted_effects/cbrn_scripted_effects.md:1319` accurately describes STATE scope, input/output storage, existing side effects and the no-retuning boundary.

## Before/source comparison

Immutable before files were read from `.git/cbrn_takeover_20261006/helper_lifetime_before/<same path>`.
Their comparison with current source contains exactly ten added `set_temp_variable` storage assignments and zero removed lines: exposure three, doctrine three, diplomacy three and chemical-state one.
No condition, price, timing, class threshold, Air coefficient, cleanup coefficient or callback was changed by this repair.

| Source | Before SHA-256 | Audited current SHA-256 |
| --- | --- | --- |
| `common/scripted_effects/cbrn_exposure_effects.txt` | `ef0007800a958cf2390cdfe66a881993959490435bd973f8393577ddcf1c6be4` | `3112e6b2d976f592d714eced13440871ea1a8214d945d646672b6853335c3580` |
| `common/scripted_effects/cbrn_doctrine_effects.txt` | `0fb4fd94bf3ef135c6773a4cb1444d0b60fd8fcedbcb15d806e271532a9d497c` | `32f684dc0022b2bc0149a06028ed9a8a158222df8b21630f20102999f4523d18` |
| `common/scripted_effects/cbrn_diplomacy_effects.txt` | `0946a66ae916455d5988b0de2f894c50444e6a37b9f19dad1c7552f26272018d` | `c005b6687b816c9fd8d09e1749f289a19239e63335afbd6c19641c7a33ef14d2` |
| `common/scripted_effects/cbrn_chemical_state_effects.txt` | `cf70ead29b152d9ba84d79e5e4f7e0b4f72fcfa32b0c4cda8ce75b6e74b8d87d` | `1873d29b193023e5121273376ac28af0119f91a0c11e4a7eb0e4b2a5ac063f40` |

The earlier `2026-10-06_completion_audit_evidence.json.finalSourceHashes` map is evidence of the prior tranche, not a current final identity after this repair.
For these four files, the current hashes above supersede any prior-source identity for this audit.

## Meaningful validation

| MCP check | Checked commands | Result and limit |
| --- | ---: | --- |
| Exposure file | 860 | `SCRIPT_CHECK_PARTIAL`, `valid = null`, zero findings; 14 unknown-scope roots and 572 unchecked argument blocks. |
| Chemical-state file | 225 | Same partial result, zero findings; seven unknown-scope roots and 118 unchecked argument blocks. |
| Doctrine file | 451 | Same partial result, zero findings; 64 unknown-scope roots and 154 unchecked argument blocks. |
| Diplomacy file | 486 | Same partial result, zero findings; 30 unknown-scope roots and 274 unchecked argument blocks. |
| Class calculator body, explicit STATE scope | 27 | `valid = null`; 13 unresolved native argument blocks; 35 total findings with 15 omitted. No concrete invalid command/scope finding returned. |
| Air calculator body, explicit STATE scope | 13 | `valid = null`; nine unresolved native argument blocks; 19 total findings with none omitted. No concrete invalid command/scope finding returned. |

Whole-file checks cover syntax/command-kind/declared-scope/event-popup surfaces only to their reported coverage.
Explicit STATE checks narrow the root scope but do not validate native argument blocks from prose or establish engine temporary-variable lifetime.
The result is source-contract confidence, not complete MCP or live-game proof.
The parent owns the actual-source conservative call-frame regression; this auditor did not run or author that regression and does not claim engine emulation.

## References and boundaries

Read through live `hoi4.reference_read`: offline `Data structures - Hearts of Iron 4 Wiki.md:435-443`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
It states that temporary variables first created inside a returning scripted helper may not persist, while variables defined before the helper call are carried into and modified by it; temporary values are unscoped.
Read installed `documentation/effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, for `set_temp_variable` support in any scope and variable/value inputs.
Read installed `documentation/triggers_documentation.md:2110-2135`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, for the comparison forms used by class and contribution logic.
The validator used installed-documentation aggregate revision `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

No GUI retry, technology/event/state-flow/helper-expansion request, refresh, game launch, log search, balance retuning or unrelated helper audit was performed.
The broader completion audit's unresolved native, asset and achievement gates remain unchanged.
Skills applied: the previously read Chaos Redux events helper-output contract and subagent/read-only handoff rules; none were changed.


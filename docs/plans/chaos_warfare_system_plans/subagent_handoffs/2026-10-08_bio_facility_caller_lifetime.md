# Biological facility caller lifetime

Disposition: implemented within the parent-accepted temporary-output contract, with bounded source tests complete and parent review, probability comparison and native acceptance still open.
Acceptance basis: the parent task continues the [accepted CBRN overhaul](../../../specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md) and explicitly accepted the seven-site insertion map before authorizing gameplay edits, exact archives and tests in a follow-up task message.
The initial assignment was audit-only, and the later authorization was limited to the three named gameplay files.
No Git commit or index change was made by this worker.

## Completed implementation

The patch adds 29 literal temporary declarations at seven sites across these three files.
No original statement, statement order, policy, target filter, callback, resource payment, price, tuning value or weighted block was changed.

| File | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `common/scripted_effects/biological_facility_capture_effects.txt` | `af68fb98172452b324db17b2a273110e1d9c08e6a3d7f30aecabcce4e9d1f00c` | `00d870fe2fc877ca389368b5809b5b9ec741fcf9bab018fdf524fc158fad34f0` |
| `common/scripted_effects/biological_field_test_effects.txt` | `c8b06c41de34753fcafa4eed489e4473ec928ecfecb5627dea0208fecc0c669b` | `cd51646a7de57f444e95a2e5147c6581a436d84d9c1f1b86d7ad7969a8170fbe` |
| `common/scripted_effects/biological_stockpile_safety_effects.txt` | `922a3aa5a32b91a6c744d4512fd8afd0e1f1b5791c9e3ba00b76f6a5a7dc05d3` | `610af2118ef4fa2a5b195c4e799f12dbfe97475ce66c8374ab4286bf54285c75` |

Exact bytes reside under [the testing evidence folder](../../../testing/2026-10-08_bio_facility_lifetime/), with `before/` and `after/` mirroring each gameplay path.
The folder's local `.gitattributes` applies `-text` to both archives without editing the shared root attributes file.
The [insertion manifest](../../../testing/2026-10-08_bio_facility_lifetime/insertion_manifest.json) records original offsets, original line anchors, exact inserted text, owners, call targets and defaults.
The source suite reconstructs the entire original byte string by removing only those inserted spans and compares all original parsed statements and every weighted AST.
Current-source verification tolerates CRLF/LF conversion only, while execution uses current gameplay bytes.

## Exact storage map

Line anchors in this section refer to the frozen before files.
All storage declarations use unscoped temporary variables.

| Actual consuming owner | Returning helper and insertion point | Missing output storage | Consumer after return |
| --- | --- | --- | --- |
| STATE `bio_facility_capture_debit_selected_release` | Immediately before `bio_facility_capture_select_release_agent` at line 483 | `bio_facility_capture_selected_agent = constant:bio_lifecycle_agent.none` | Four selected-stock branches at lines 486-499, then exact selected-agent debit branches at lines 510-533 |
| STATE `bio_facility_capture_debit_selected_release` | Immediately before `bio_facility_capture_prepare_fraction_amount` at line 504 | `bio_facility_capture_fraction_amount` and `bio_facility_capture_fraction_amount_negative`, both `constant:bio_facility_capture_math.zero` | `bio_facility_capture_enforce_release_minimum` at line 505 and positive/negative exact-ledger debit at lines 507-534 |
| STATE `bio_facility_capture_dispatch_accidental_release` | Immediately before `bio_facility_capture_debit_selected_release` at line 555 | `bio_facility_capture_selected_agent = constant:bio_lifecycle_agent.none`, `bio_facility_capture_fraction_amount = constant:bio_facility_capture_math.zero` | Positive-release branch at line 557, release identity/amount history at lines 558-559, seed agent and payload receipt at lines 585 and 590-591 |
| STATE `bio_facility_capture_dispatch_accidental_release` | Immediately before `bio_lifecycle_reset_seed_record` at line 564 | Eight residual inputs listed below | Seed dispatch at line 593 and its downstream normalized input consumers |
| STATE `bio_field_test_resolve_exact_facility_test` | Immediately before `bio_lifecycle_reset_seed_record` at line 42 | Eleven residual inputs listed below | Seed dispatch at line 52 and its downstream normalized input consumers |
| STATE `bio_field_test_resolve_exact_facility_test` | Immediately before `bio_lifecycle_dispatch_seed` at line 52 | `bio_seed_dispatch_status = constant:bio_lifecycle_proof.missing` | Accepted receipt check at line 55 and actor history/notification at lines 56-65 |
| COUNTRY `bio_stockpile_safety_dispatch_selected_accident`, inside its exact arsenal STATE and noncontained branch | Immediately before `bio_lifecycle_reset_seed_record` at line 654 | Four residual inputs listed below | Seed dispatch at line 673 and its downstream normalized input consumers |

The capture dispatcher does not consume the negative fraction output after the debit helper returns, so it does not own an unnecessary outer negative output declaration.
The debit helper owns that field locally for the fraction/minimum/debit sequence.
The three capture wrappers at original lines 619, 659 and 719 already directly assign `bio_facility_capture_release_fraction` before dispatch and consume regular state records afterward.
They require no additional outer temporary outputs for this task.

Capture's eight reset-only residual inputs are:

- `bio_seed_use_history_proof` and `bio_seed_batch_condemnation_proof`, each `constant:bio_lifecycle_proof.missing`.
- `bio_seed_concealment`, `bio_seed_intensity_override`, `bio_seed_exposed_share_override`, `bio_seed_evidence_override` and `bio_seed_condemnation_override`, each `constant:bio_lifecycle_math.zero`.
- `bio_seed_weaponization_mult = constant:bio_lifecycle_math.one`.

Field test's eleven reset-only residual inputs are:

- `bio_seed_payload_debit_proof`, `bio_seed_use_history_proof` and `bio_seed_batch_condemnation_proof`, each `constant:bio_lifecycle_proof.missing`.
- `bio_seed_payload_required`, `bio_seed_payload_consumed`, `bio_seed_concealment`, `bio_seed_intensity_override`, `bio_seed_exposed_share_override`, `bio_seed_evidence_override` and `bio_seed_condemnation_override`, each `constant:bio_lifecycle_math.zero`.
- `bio_seed_weaponization_mult = constant:bio_lifecycle_math.one`.

Field-test validity does not require a payload-debit proof, and the declaration preserves the canonical missing-proof reset contract rather than granting debit authority.
Its zero required/consumed quantities are still consumed by the normalized state record writer.

Stockpile dispatch's four reset-only residual inputs are:

- `bio_seed_use_history_proof` and `bio_seed_batch_condemnation_proof`, each `constant:bio_lifecycle_proof.missing`.
- `bio_seed_concealment = constant:bio_lifecycle_math.zero`.
- `bio_seed_weaponization_mult = constant:bio_lifecycle_math.one`.

These declarations make reset modifications survive in actual consuming owners.
Initialization only inside the returning reset helper cannot establish storage in its caller.
Directly assigned agent, route, source, result, actor/victim proofs, explicit payload quantities and force-detection values are already caller-owned.
The stockpile dispatcher directly assigns all four seed overrides from its own six snapshots and does not need default declarations for them.
Dispatcher-owned route/profile/final-value outputs are deliberately excluded from this owner audit and remain the parent's shared-lifecycle responsibility.

## Scope and target contract

Capture executes in the exact captured STATE.
Its optional actor is `var:bio_stockpile_safety_arsenal_actor`, only when that country exists, and its victim is the current `CONTROLLER`.
Missing original custodian retains a missing actor proof and substitutes no country.
The captured-facility validity branch requires exact victim/control and positive payload-debit quantities without requiring an original actor.
Regular state ledger changes remain persistent across nested helper returns.

Field testing executes in the native facility STATE, with `FROM` representing the active special project and `FROM.owner` supplying the actor country.
Its real owner guard requires existing actor and victim targets and controller equality to the actor.
Both seed targets are copied from that verified pair.
The agent, project-progress ratio and event identifiers are directly assigned by each of the four `conduct_*_field_test` wrappers before the shared resolver.
The contained-test random flag is assigned directly in the consuming resolver before its inline random block and requires no helper lifetime repair.

Stockpile dispatch executes in COUNTRY scope and directly snapshots six regular country values before entering `var:bio_stockpile_safety_arsenal_state`.
Those snapshots are agent, intensity, exposed share, evidence, condemnation and already removed payload quantity.
They already exist in the owner before its state block and survive scope changes.
Actor and victim targets are both `ROOT`, matching the current country-root owner callback, and the state receipt remains on the exact registered arsenal.
Selected severity is read through `ROOT` while the six snapshots are read from the executing country.
The tests bind those to the same country and do not prove a caller with a different ROOT.

The regular targets `bio_seed_actor`, `bio_seed_victim`, `field_test_state`, `bio_field_test_actor`, `bio_field_test_victim`, `lab_accident_state` and `bio_facility_notice_state` keep their existing chain lifetime.
No global target, flag lifecycle, cleanup hook, new helper, tuning constant or new event is added.
An extra reset helper would not replace caller-owned declarations, so this patch retains local literals instead of introducing another generic abstraction.
`bio_active_agent` remains the accepted-dispatch cursor owned by the existing shared dispatcher and any preexisting outer spread cursor.
None of these caller declarations resets that cursor.
`bio_seed_dispatch_status` remains an acceptance receipt, not a replay guard.
Only field tests read that returned receipt in this task, so capture and stockpile callers receive no unused status declaration.

## Meaningful source tests

Run `node docs/testing/2026-10-08_bio_facility_lifetime_source_tests.js` from the repository root.
The [suite](../../../testing/2026-10-08_bio_facility_lifetime_source_tests.js) completed 56 cases with zero failures, and [the results](../../../testing/2026-10-08_bio_facility_lifetime_source_results.json) preserve per-case traces, input values, scope bindings, source/constant hashes, executed helpers and observed command keys.
The unchanged `docs/plans/026_black_friday_plans/subagent_handoffs/exact_quote_source_tests.js` BaseVM supplies parsing, fixed-point operations, branches and conservative scripted-call cleanup.
Temporary names first created inside a returning helper disappear, while modifications to inherited storage persist.
Country, state and project records use separate maps.

Coverage includes:

- Twelve capture cases over four fixed selected agents and state stocks 1, 10 and 100, proving the minimum-one path, rounded larger releases, exact selected stock reduction, release history, forwarded identity, positive required/consumed payload and original actor/current victim separation.
- Four direct debit cases proving local selected-agent storage and positive 10/negative 10 return values across the fraction-helper boundary independently of the outer dispatcher declarations.
- Capture context rejection, empty payload/no selected release, missing original actor, and rejected canonical seed.
- Eight field-test cases over four agents and accepted/rejected canonical seed gates, proving accepted-only notification, returned receipt ownership and preservation of an existing outer cursor on rejection.
- Field contained test, wrong controller and missing actor rejection through the actual resolver guard.
- Twenty stockpile cases over four agents and all five already-selected severities, proving contained incidents make no seed and the other branches forward exact state, actor/victim, payload and four override values.
- Three reset-only storage checks covering all 23 residual declarations with fresh storage, baseline absence after reset return, and stale-value reset to canonical defaults.
- Entire-file byte reconstruction, preservation of every original weighted AST, and unchanged BaseVM hash.

The archived baseline reproduces 12 capture dispatch losses, four direct-debit losses, four accepted field-test receipt losses and three residual-storage failures under the conservative lifetime model.
This is 23 baseline failure cases rather than 23 observed engine failures.

The actual three seed owners, four `conduct_*` wrappers, capture selector/debit/fraction/minimum/recompute helpers, seed reset and the shared dispatcher's acceptance/receipt body execute from parsed source.
The selected weighted branch and field accident outcome are explicit fixtures.
The capture release context and shared canonical seed-validity result are explicit booleans.
Shared route and agent profiles, final-value arithmetic, retaliation classification, later state storage, integrated recovery, incubation scheduling and detection are declared sinks or fixtures in the suite.
The suite does not duplicate the parent's shared-lifecycle audit or infer a complete outbreak from its recorded input sink.
Stockpile country stock is an unchanged fixture of 95 at seed entry and after seed, representing a separately completed five-unit debit from an initial 100.
That check proves this seed owner adds no further country stock command, and it does not simulate the earlier native equipment debit.
No native stock payment, refund, callback settlement, RNG distribution, queue execution, later disease tick, policy gate or balance conclusion is inferred.

## References and MCP evidence

The connected reference context, search, read, source lookup, event trace, probability inspection and script validation routes were exposed and responded.
No helper-expansion route, persistent job or native task was used, because service/task negotiation was not verified for this worker.
The parent's last reported service version was 3.10.0 and is not independently reasserted here.

The live offline wiki read was `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types, lines 435-443, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Line 440 explicitly distinguishes temporary values first defined inside scripted helpers from values defined before a helper call.
The same wiki revision's Regular event targets section was read at lines 303-312.
Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` was read at `set_temp_variable`, lines 7820-7827 and Examples 7828-7841, and `save_event_target_as`, lines 6496-6504, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
The initial context bundle omitted unrelated Event modding, Effects, Triggers and On actions sections from its limit, so it is not used as a claim of full topic coverage.
Targeted reads above cover the syntax and lifetime rule used here.

Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_effects/00_scripted_effects.txt`, lines 839-855, was read for the unscoped literal `set_temp_variable` pattern in `remove_from_allowed_party`.
Its SHA-256 is `93ddd0d2e9f7a1a5640cfdafbae6b9ff0e1b4ee57e829c81d13b0cac23ad90bf`.
That is a syntax precedent and does not prove caller lifetime.
The existing Chaos Redux owner-storage implementation in commit `0afbdf4d356e4fe0888e35a03d99e65efce0e272` is the matching project pattern.

The focused source lookup for capture returned the exact helper at original lines 542-610 with index revision `dd064215120af77b958739d795ad109c7e36a2d6ff5871cc662400c986456ba3`.
Source lookup reported a truncated inline helper excerpt, so the underlying file was read in full relevant ranges.
The initial invalid selector/maxLines requests were corrected against the live validation messages rather than treated as service failures.

Three corrected source traces used `selector.kind = source`, `sourcePath` naming each gameplay file, original lines 542, 20 and 629, `maxDepth = 1`, `maxNodes = 8`, `maxEdges = 10` and `expandHelpers = false`.
They returned `EVENT_INSPECTED_PARTIAL` at graph revision `5b61a45d5836c19fd276ef8a5e51b000c91b28ce24b8158b45c373319843902d`, explicitly deferring helper projections and whole-workspace lifecycle passes.
The [JSON companion](2026-10-08_bio_facility_caller_lifetime.json) retains their original artifact URIs and compact route results.
The reports remain partial, and their global inventory counts or unreviewed large artifact bodies are not attributed as findings about these three owners.
No event render or matched event comparison is claimed.
The parent owns any remaining graph comparison and the known baseline/cache constraints.

Capture `random_list` inspection discovered four candidates, all four exact state-ledger input paths, complete pool discovery and zero unresolved discovery items.
Its source revision was `e2abc8fa287f03d3c98697840ce0460cf4566d6ccb9c5b986a5c0265ecba0a03` and its artifact URI is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0effef28cd4bf42ba251ffbe8d32e52ded7306f3a823b04475063cc5b2acdbe2/a84b8133e3e83aa6d48116935dbbd9970eb6d2ed575f52ba01f33f3b07f1f754/probability-inspect-31d9c213d75e.json`.
Field `direct_random` inspection discovered one candidate, complete pool discovery and zero unresolved discovery items at source revision `2fc0d50e61eba0d4451e91981f1ce8447c6f6ec3a2f203370e919658f3217c09`.
Its artifact URI is retained in the JSON companion.
These are discovery results, and no numeric or before/after probability conclusion is claimed.
The parent explicitly retained routing to `chaosx_ai_probability_auditor` over the frozen before/after files with matching scenarios.

A state-scoped representative snippet containing four declarations returned `SCRIPT_CHECK_PARTIAL`, with supported command kinds/scopes, `valid = null`, four `SCRIPT_ARGUMENT_BLOCK_UNCHECKED` findings, and unchecked parameter semantics.
The checked documentation index revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The direct installed syntax reads and bounded source suite supplement that partial result, and they do not convert it to engine proof.

## Hazards and remaining work

Capture ledger debit, release history and notification already precede or ignore the shared acceptance receipt.
The rejected-seed case preserves that ordering and demonstrates a debit from 100 to 90 with no fixture seed store.
Changing that transaction policy, rollback behavior or notification condition is outside this lifetime patch.

Stockpile severity and actor/victim use ROOT, so a future caller with a different root-country identity requires a separate scope contract review.
The current six snapshots use executing-country values, and the existing root assumption is preserved.
Native facility/project scope availability, queue execution and all normal callback/payment semantics remain unobserved here.
The complete facility transfer/destruction routes and other shared fraction-helper consumers were not broadened into this three-caller task.
Their source statements are preserved, and their full lifetime contracts remain separate work.

No gameplay simplification or substitute mechanic was introduced.
There is no asset, localisation, event-log, spreadsheet, public wording, tuning-table, constant or cleanup change in this storage-only patch.
The parent must review this handoff, probability evidence and the exact diff before committing.
Full accepted CBRN completion remains incomplete.

Skills used: `chaos-redux-events` and `chaos-redux-subagents`.
No skill was created or changed because the existing events skill already documents this lifetime workflow.

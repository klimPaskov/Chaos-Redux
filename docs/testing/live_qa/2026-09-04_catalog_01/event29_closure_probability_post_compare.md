# Event 29 temporary-closure AI willingness post-patch comparison

Audit date: 2026-09-05.

This is the read-only post-patch follow-up for `decision_riches_found_temporary_closure` in `common/decisions/029_riches_found_decisions.txt`.

The owner moved the missing close from the severe-pressure modifier boundary and removed the compensating close after the democratic modifier.

The factors, constants, predicates, and threshold values were not changed.

The local current source SHA-256 is `1a485534b48a59d780a53c09642e4618659c69f8fcedda9f735cca412f886a14`.

The retained before snapshot is `docs/testing/live_qa/2026-09-04_catalog_01/pre_compare_event29_decisions/common/decisions/029_riches_found_decisions.txt` with SHA-256 `2fd18aba5b34587c2594c148f8c55a7a0468ae9b37f5965af2a9b3693c922491`.

No gameplay file was edited by this audit and no commit was created.

## Audited surface and source evidence

The audited surface is the `ai_will_do` block for `decision_riches_found_temporary_closure` under the `riches_found_mine_management` decision category.

The repaired source order is:

```text
ai_will_do = {
	base = constant:riches_found_decision_ai.medium
	modifier = { factor = constant:riches_found_decision_ai.high_factor is_major = yes }
	modifier = { factor = constant:riches_found_decision_ai.urgent_factor has_war = yes }
	modifier = { factor = constant:riches_found_decision_ai.high_factor FROM = { has_state_flag = riches_found_multiple_mine_priority } }
	modifier = { factor = constant:riches_found_decision_ai.low_factor FROM = { check_variable = { var = riches_found_local_order value = constant:riches_found_decision_threshold.order_low compare = less_than } } }
	modifier = { factor = constant:riches_found_decision_ai.urgent_factor FROM = { check_variable = { var = riches_found_extraction_pressure value = constant:riches_found_decision_threshold.pressure_severe compare = greater_than } } }
	modifier = { factor = constant:riches_found_decision_ai.high_factor has_government = democratic }
}
```

The relevant MCP provenance places the base at line 3742, the five pre-existing modifiers at lines 3743–3747, the democratic sibling at line 3748, and the block close at line 3749 in the current source revision.

The source constants are `riches_found_decision_ai.medium = 3`, `riches_found_decision_ai.low_factor = 0.50`, `riches_found_decision_ai.high_factor = 2`, `riches_found_decision_ai.urgent_factor = 4`, `riches_found_decision_threshold.order_low = 35`, and `riches_found_decision_threshold.pressure_severe = 85`.

The source uses strict `compare = greater_than` for severe extraction pressure, so source semantics exclude exactly 85 and activate above 85 when the `FROM` scope is correctly bound.

## MCP inspection

The required first inspection used the requested `decision_ai_will_do` adapter and the exact decision identifier.

It returned `PROBABILITY_SOURCE_DISCOVERED` with `identifier_not_found` and suggested the matching `mission_ai_will_do` adapter.

The decision-route inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99ab1b4154066ad0ec02b9c6ac277df53b58a322b7a94011368a8b2cf6747b10/2962e565001e7463d045d6a06e2c50dafdf20f67e30181fcbc139f2366220b32/probability-inspect-0f70e76d1dd0.json`.

The matching `mission_ai_will_do` inspection returned `PROBABILITY_SOURCE_INSPECTED` with the one-candidate pool complete, one candidate, zero statically available candidates, four required inputs, and zero inspect-unresolved entries.

The matching inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5eff06fff28168314bf9c92391e3e15b86776364f9b8fd272453a52dba746cd4/6a96de35e9a0ba9922e8c605465b6a29276cc361d2ba6109d775e52124e490de/probability-inspect-0f70e76d1dd0.json`.

The post-patch MCP canonical source hash reported by the matching inspection is `0f70e76d1dd0c1b13cab670173a89b9eaa1d9500f2380a810c1a48b015953fd7` with source revision `811523609d768d1bd3d34a55e39b14d0d79a80e080cc857682cbab78e5ebc5f2`.

The canonical MCP hash is retained separately from the local raw file hash above.

## Scenario contract

The same six named scenario IDs and labels from the baseline were used.

| Scenario ID | Government | Extraction pressure | Fixed country and target declarations |
| --- | --- | ---: | --- |
| `RF29_CLOSURE_PRESSURE_BELOW_NON_DEMOCRATIC` | `fascism` | 84 | `CXT`, AI, peace, non-major, priority false, local order 60 |
| `RF29_CLOSURE_PRESSURE_AT_NON_DEMOCRATIC` | `fascism` | 85 | `CXT`, AI, peace, non-major, priority false, local order 60 |
| `RF29_CLOSURE_PRESSURE_ABOVE_NON_DEMOCRATIC` | `fascism` | 86 | `CXT`, AI, peace, non-major, priority false, local order 60 |
| `RF29_CLOSURE_PRESSURE_BELOW_DEMOCRATIC` | `democratic` | 84 | `CXT`, AI, peace, non-major, priority false, local order 60 |
| `RF29_CLOSURE_PRESSURE_AT_DEMOCRATIC` | `democratic` | 85 | `CXT`, AI, peace, non-major, priority false, local order 60 |
| `RF29_CLOSURE_PRESSURE_ABOVE_DEMOCRATIC` | `democratic` | 86 | `CXT`, AI, peace, non-major, priority false, local order 60 |

Every row used actor `CXT` and date `1936.1.1`.

The fixture declared `FROM` as present and declared controlled-by-`ROOT`, mine-state, active-selected-or-only-mine, emergency-phase, crisis-phase, and unset closed-state booleans.

It also declared `riches_found_local_order = 60`, `riches_found_extraction_pressure = 84/85/86`, and `riches_found_multiple_mine_priority = false` in the scoped fixture fields.

The candidate pool contains exactly `decision_riches_found_temporary_closure` and is complete at the discovered source boundary.

The pool is complete for this bounded score audit, but the adapter cannot bind the decision's engine-equivalent `FROM` state from the flat scenario declarations.

No seed, cadence, timer transition, or terminal state was declared because this is an `ai_will_do` willingness score rather than a sampled pool or timing distribution.

The current evaluate and compare requests report scenario hash `190a0f8df318e23e9a08f28c08ff940a94ce670b52806bdea35f8cd6c77eb061`.

The baseline evaluation recorded scenario hash `b83074bcc4e048ea4bf1773d6d45aceaa6787979cfd417f86ec852c34b974954`, and the baseline sweep recorded `7694774360a69c3662b80c7319b97d82087cfbd36fae4bf54ec3e2aac2e9ae81`.

The current request used the six same IDs and documented values, but the retained baseline report and artifact do not preserve the original scenario request body or scenario-set identifier, so the cause of the hash difference is unknown and no explanation is inferred.

## Post-patch evaluation

`hoi4.probability_evaluate` used `mission_ai_will_do`, the complete one-candidate pool, the six scenarios above, metric `raw_value`, and JSON, ranking, matrix, waterfall, and unresolved outputs.

The call returned `PROBABILITY_ANALYZED` with analysis ID `probability-8e3d3b6980089ec2081d4ed7` and complete adapter status.

Its source revision is `8076d5991482396c2f61076ed842cdc9a791669d80e5481540b313476bb082c8`, its MCP canonical source hash is `0f70e76d1dd0c1b13cab670173a89b9eaa1d9500f2380a810c1a48b015953fd7`, and its scenario hash is `190a0f8df318e23e9a08f28c08ff940a94ce670b52806bdea35f8cd6c77eb061`.

The adapter reported one eligible candidate at rank 1 in every row, with no conditional probability because the adapter is `score_only`.

The trace resolves the base to exactly 3 in all six rows.

The `is_major = yes` and `has_war = yes` factors resolve false in all six rows.

Under the flat fixture, the adapter reports the `FROM` multiple-priority factor as applied at 2, the local-order factor as applied at 0.5, and the severe-pressure factor as applied at 4 in every row.

The adapter therefore reports raw value 12 for the non-democratic rows and 24 for the democratic rows after the independent democratic factor applies at 2.

Those `FROM` applications do not prove the intended target-state predicates or the 84/85/86 threshold boundary because the pressure factor did not change across the three declared values.

The MCP response is complete for its flat fixture evaluation, while engine-equivalent `FROM` resolution remains unresolved for this audit.

The authoritative evaluation JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9abbd4c21486d223c7a89c7da0c46c0e641e8525cf86e53f2fafb47cf38b2a3c/d4b587bf45423552a2e530300304931644bbd88d5619e674051a43d3e4b496ae/probability-8e3d3b6980089ec2081d4ed7.json`.

The emitted ranking, matrix, waterfall, and unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52489a4f751ac82171a4a5bb0afadc951bc4b7a9e53e69a4d92762280ef13bdf/77b42f2c73b58bc50eb6e727a2daf0ae87d287eb343e420fc72a3a515b3cc1a0/probability-probability-8e3d3b6980089ec2081d4ed7-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21e5bed5acacc6319a2e69f31a2c4394f7fb27237b467b44d452cb107e2df29b/ab2c313ff71269c1ed7f184798edfd084c5758b69ebe0bf9e9a33c8e6f70a0e8/probability-probability-8e3d3b6980089ec2081d4ed7-matrix.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fe0d8f1567727402e56f306c4f8d62cebd31685d77f833f1f8f2c0ba51874ac/997a06691d6817f237c5910cb4be0087842b20cff87de68bdba3c03a753c73e3/probability-probability-8e3d3b6980089ec2081d4ed7-waterfall.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/e1555a58aa2ff87cc2cf74c1e6af89d6904fbdb90ad3e59926d5beff227fd3/probability-probability-8e3d3b6980089ec2081d4ed7-unresolved.svg`.

The result is classified as `score_only` with a bounded flat-fixture trace and unresolved engine-equivalent `FROM` target validity.

## Post-patch threshold sweep

`hoi4.probability_sweep` reused the six IDs and varied `scope.var:riches_found_extraction_pressure` at 84, 85, and 86 with three steps, pairwise sensitivity, and rank-reversal detection enabled.

The sweep returned `PROBABILITY_ANALYZED` with analysis ID `probability-50198783aaca6a09ae824531`, source revision `c939f8dad6caadd40f6a62c32af5a2435101817809b5b1749baac0f033cd4461`, and the same current scenario hash `190a0f8df318e23e9a08f28c08ff940a94ce670b52806bdea35f8cd6c77eb061`.

It produced six sweep points and reported no breakpoint, local elasticity, pairwise interaction, or rank reversal.

The empty reversal result is an adapter observation under the unresolved flat `FROM` binding and is not evidence that the source threshold cannot change a live score.

The authoritative sweep JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2d8ae8d34ae6547f5a1e535faddbb67be56fc576bc304a00231ba7a2efe677ab/c566af7fc9b530c552588b622d8f63513faafd370aeece1e7e8ba5a4b71942af/probability-50198783aaca6a09ae824531.json`.

The sweep sensitivity, threshold, and unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f326ed62192bd4971691f9a470f0fd496147633ee629568741bed7334047145/36e0868dbdcb606e339252b4377034b3e6c080377c5a68315cbeb304362e251c/probability-probability-50198783aaca6a09ae824531-sensitivity.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/254291f5648f8326f94a04ab16dfe405b1201d405130c3f28ecc8169a4607aa2/probability-probability-50198783aaca6a09ae824531-threshold.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/78c695e521406856e1124c92ba4b8a814eac1e92c8f7d130ed8f12b8816eab67/probability-probability-50198783aaca6a09ae824531-unresolved.svg`.

## Mandatory same-scenario comparison

The real post-patch `hoi4.probability_compare` used `mission_ai_will_do`, the same six scenario IDs, the one-candidate pool, and the current scenario hash above.

The before input was the exact archived decision block extracted from `pre_compare_event29_decisions/common/decisions/029_riches_found_decisions.txt` through `inlineClausewitz`.

The after input was the exact current decision block extracted from `common/decisions/029_riches_found_decisions.txt` through `inlineClausewitz`.

Both exact blocks were placed under a temporary `riches_found_mine_management = {}` wrapper in the MCP request so the nested decision surface could be identified.

The wrapper existed only in the read-only MCP request and was not written to the repository.

Initial full-file inline submissions returned `PROBABILITY_SURFACE_EMPTY` after the command-output transport truncated the source text, so those attempts are not used as evidence.

The successful bounded decision-block comparison returned tool status `ok`, code `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-fcb67a56bd40156e95968f59`, `beforeAnalysisId = probability-5cf2cde7857fc593d711384`, `afterAnalysisId = probability-97ddc0903c3cfd94650cffa5`, `comparisonChanges = 6`, zero diagnostics, and an empty regressions list.

The comparison source revision is `5c0ef6f9c1e515a6b7402b2c92f88693f8444ca82a71cfa34cbc9fd79cc0b738`.

The MCP comparison source hash is `b93004c14c5bcbb69b0465f508e317e2d3bf2be54d013add3b7232758f95e544` for the wrapped inline comparison source and must not be confused with either local raw file hash.

The comparison JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8794138b1bf30e238654d8ed6764812f0bb87d262b74c7ee4d751c3b2f36c50/9bfd5e4b3fd75daf4c321def42e430aab83a3242ee630191276dbd0cfed33ae3/probability-fcb67a56bd40156e95968f59.json`.

The direct comparison emitted `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a7cbf1e08330875f00c1fea952d9721263ad12539b65145f80206c6feaf86cd/ec1ebf26d79afe25b2128583281d09cd81937a4a1aab4958ee61021e32873975/probability-probability-fcb67a56bd40156e95968f59-comparison.svg`.

An explicit `hoi4.probability_render` for the compare analysis returned `PROBABILITY_ANALYZED_PARTIAL` with the expected scenario hash and regenerated comparison, ranking, matrix, and unresolved views.

The regenerated comparison and unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a7cbf1e08330875f00c1fea952d9721263ad12539b65145f80206c6feaf86cd/f76454251db6c70729baf72459f0b50d38abb7212716cda407f2eabaab208e59/probability-probability-fcb67a56bd40156e95968f59-comparison.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae82a64c123a549500e5478ff96e15583ae0a50127b0c0a8641b93a33e6689d6/651d49e051e8a6f97695767a535bf8c39533f05ec8e25736064303f6a3dc041d/probability-probability-fcb67a56bd40156e95968f59-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/21e5bed5acacc6319a2e69f31a2c4394f7fb27237b467b44d452cb107e2df29b/b658c2c03eeaa25559eeb6751ac3591d9754913b3945af13f3580787a3623bfd/probability-probability-fcb67a56bd40156e95968f59-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/733315539999b96da9d42f186ad9d40f750465c958e2f11d256c6f7e2f0a63da/b3e92e4cce574a9bf6f3f36eddb8f92dbd986f336bf7186b348dff9720f767cc/probability-probability-fcb67a56bd40156e95968f59-unresolved.svg`.

The six scenario changes all reflect the repaired parse boundary.

For each non-democratic row, the comparison attributes an added `constant:riches_found_decision_ai.urgent_factor` result of 12 and removal of the before unresolved pressure factor.

For each democratic row, it attributes the same pressure-factor change and an added democratic `constant:riches_found_decision_ai.high_factor` result of 24.

The comparison reports one unresolved aggregate with code `TRIGGER_UNRESOLVED`, message `Scoped or compound trigger modifier is not declared by the scenario`, and path `modifier` on the synthetic inline before side.

The six changes are therefore bounded structural and adapter-attribution evidence for the brace repair, not a final live balance or target-validity certification.

## Validity and risk findings

The `visible`, `available`, `target_trigger`, and `target_root_trigger` logic requires a valid `FROM` state with controlled ownership, mine-state and active-selection gates, emergency and crisis phase flags, and an unset closed flag.

The adapter's flat scenario contract does not bind that decision-to-state `FROM` scope with engine-equivalent semantics.

The post-patch adapter's `eligibility = true` and rank 1 result are therefore not promoted to proof that the positive willingness score is attached only to a valid live target.

The current six-row pool contains one candidate, so it cannot establish competitive dominance, starvation, or meaningful rank reversal.

The `mission_ai_will_do` adapter exposes a willingness score and does not provide normalized selection probability, click probability, cadence, timing distribution, repetition rate, or campaign recurrence.

The source-level strict pressure boundary remains the expected 84/85/86 distinction, but MCP evidence cannot certify that distinction until the `FROM` target state is bound or the adapter limitation is explicitly accepted.

No exploit, starvation, dominance, repetition, or snowball conclusion is claimed from this bounded pass.

## Skipped analyses and remaining blockers

`hoi4.probability_simulate` was skipped because no uncertain input distribution or seed was declared for this score-only surface.

`hoi4.probability_sequence` was skipped because this decision is not a declared custom weighted pool with cadence, cooldown, recovery, removal, reset, and terminal-state semantics.

Event structural inspection and rendering were skipped because this follow-up audits only the decision AI willingness surface.

No game launch or live validation was performed.

The requested `decision_ai_will_do` route remains an adapter mismatch and the engine-equivalent `FROM` target scope remains unresolved.

No source-only result is promoted to a fake AI pass, and no unapproved fallback was used.

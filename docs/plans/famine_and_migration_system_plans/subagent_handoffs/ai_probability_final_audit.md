# AI Probability Final Audit Handoff

> **Superseded historical snapshot (2026-08-25):** This standalone audit records a pre-split probability snapshot and is retained as historical evidence only. Its combined source paths, 20-row unresolved status, and pre-refresh artifact claims are not current instructions. Use [source_of_truth_map.md](../source_of_truth_map.md), [completion_report.md](../completion_report.md), and [../ai_probability_current.md](../ai_probability_current.md) for the current partial audit status and remaining typed-fixture and dynamic-pool blockers.

Audit date: 2026-08-24.

Owner handoff: read-only final audit for the famine and migration AI and custom weighted-pool surfaces. Full evidence is in docs/plans/famine_and_migration_system_plans/ai_probability_post.md.

## Status to parent

- No MCP request is currently running.
- The mandatory decision-source probability_inspect completed for the inspected snapshot.
- A narrowed refresh probability_inspect timed out after 180 seconds.
- No fresh current-source probability_evaluate, probability_sweep, probability_sequence, probability_simulate, or probability_compare was started after that timeout.
- The current-source 20-scenario evaluation is incomplete; all 20 rows are unresolved.
- The only completed comparison is historical current/current with comparisonChanges=0 and is not a baseline/current proof.
- The current working tree has emergency_airlift_factor_2 = 2 on the high-air-experience branch. The current source is not inverted; MCP probability confirmation is unresolved because the inspect artifact predates the current physical hashes.

## Audited files and current physical hashes

The weighted source contains 28 decisions and six missions in common/decisions/famine_migration_decisions.txt. The current physical SHA-256 values read during this audit are:

- common/decisions/famine_migration_decisions.txt: 810AFFA3268096F7F82777485CBD02AB6238FD4A0E2A93AC7C355E28F6C19074
- common/script_constants/famine_migration_constants.txt: 8345111A1BE7A1924668A1DF25C374F18A66BAC50DC77E6D16AF6ACD4E4E62FD
- common/script_constants/famine_migration_destination_selection_constants.txt: 09CD3C8E50D882A21532ABF14D1593C3CF49CA6504EAB8EE88983AD96E0DFFAC
- common/script_constants/famine_migration_relief_constants.txt: 9420DE72A7DAE5DB871891E898E2759749F1B991C30DEEACCB958617F89CE609
- common/script_constants/famine_migration_corridor_constants.txt: 00D9FEC8026692FDC1E7782F5935738219318469D136D6328C820FB861BF0909
- common/scripted_effects/famine_migration_destination_selection_effects.txt: A470B9C0AE28E3A48CEA40733976363C313E65238F4C267AD045A5CDD6A32775
- common/scripted_effects/famine_migration_relief_effects.txt: 7664234A3F13A2494373E9E0DB463091F6E3F17A217DCBD61621BED7B358EC35
- common/scripted_effects/famine_migration_corridor_effects.txt: FFBFEF2B841486BE2D54F7243C27CA39EB1BB264FD07403EB996A0ADC0F841C7
- common/scripted_effects/chaosx_famine_migration_effects.txt: 4108EC7F7B581D4471253B4457C95130EC9021891B47BBB0DEA60D8650CB837B
- common/scripted_triggers/famine_migration_destination_selection_triggers.txt: 6987D9D2B7C8B0AACCB740F3ED667B845CD8CF04B9FAA0728CEE5E3821224CAF
- common/scripted_triggers/famine_migration_relief_triggers.txt: FB181D81FC6ACB390FEE586874814A0CA743D307CBD650BC0C76E9CCD5628053
- common/scripted_triggers/famine_migration_corridor_triggers.txt: 8CD896D3E14C5D992131425453AB19B953D373BC0231DCAD5011899CBD1D9D8D
- common/scripted_triggers/chaosx_famine_migration_triggers.txt: 2EA45BC12480E8D3850599192A439469994D0A2B20A1127C9E06D8C74AE8FC33
- common/on_actions/chaosx_famine_migration_on_actions.txt: 17E5FC070479F36E7B1398648AC788315BD17C4589A672C03F30C317E201FDAD

## MCP artifacts

The completed decision inspect returned PROBABILITY_SOURCE_INSPECTED with poolComplete=true, 28 candidates, 11 required inputs, and zero inspect-unresolved inputs.

- Discovery: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee5dd83f47cf589cf1de1d96b68931a20a1c349e41a3a3b97c8d143cb53ef507/096805e177cb7920a229d0a445b884edd44ab4c8f02a60e43ad27ec68ec3264f/probability-inspect-187e663a01be.json
- Explicit: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4300a2d0f084e56ce212c7a1c6592d1b40a38ec30f3558c9ab2c327b81fe2231/9150ff8e690facbd8aaf5fc765330f38a54c1fe737e315f672deafe36bffeabb/probability-inspect-187e663a01be.json
- Inspected source revision: 549977bae28a88c6d1082ccb5aa602c592e56b96c1ba3002b7785b002d176dfa
- Inspected aggregate source hash: 187e663a01be197531391843f18b204521689d39ea0db30d8fd1f849632a3c0c
- Adapter: Operation Postern 1.19.2.0 (d245), rawScore=true, normalizedProbability=false, selectionRule=score_only, sequence=false, timeDistribution=false.

Explicit custom-pool inspections were incomplete with zero candidates:

- Destination: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35a7c0739df0654d46bea8c3f2aa9054558010106c0984bd40a0aa3ab5c6a41f/f61e0c0e5da85b3d88de8f945c83f5a727ddb854fd669bccee2be1a2f7ab2fc7/probability-inspect-95d51b3eb64a.json
- Relief donor: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c95af4bfbe8b094ae6aed14dad557024c3d2a7c40fb187d35338ce9285d3dbcd/94d062edba52ea66f3ce9f2feda32e2b0afea43000ed614350288be616f7f4b2/probability-inspect-40b35335ef2b.json
- Corridor helper: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/774634e79bc1db0a40018279615b0f4f391b2da5f15f06478cd226ec074cba08/58aa07926aff72a39bfb641df0b141273df2ce53e5273107181fb1a1fa3d0c6e/probability-inspect-3e2e9b28b297.json
- Shared effects: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b84ae289134e1be68ad17fc77f20cb8bca7473fb490cc504909e919008242701/0fd8ac04bcb6bee84c7968c6647c6f780df48aab6f4e40ba494340090b7f5eaa/probability-inspect-1036274a63eb.json

The old partial evaluation was probability-27f3952bc314506bb9f685f5 with source hash c874297e02df691eda7e9bea00a87d1352e3f9a60b5c747573d493d79ce8bb3d, scenario hash c72e02ef3aeaf7a48001c6d656e2898e18bab63387269eddbcb9f975275a6f67, candidate-pool hash 90d337c26916e9db69c4e41327367942fd5139b29f25c52824e71858e04bfda9, 520 rows, 59 unresolved, and 20 diagnostics.

- Evaluation JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad819f65fad7b1d96cf62ad5ec0bb8491aed28a1343178f0298c81067f308978/ff7122146a44b03e4defe5c2c5181ad4793eacb387192a62e2cb7738d153465a/probability-27f3952bc314506bb9f685f5.json
- Historical flat sweep: probability-e5e77d07e1a716315c92d64f, 20 points, 59 unresolved, no reported reversals; the first range sweep failed PROBABILITY_SWEEP_RANGE_REQUIRED.
- Historical current/current compare: probability-e7b9a0a14bc5741afdc6f63e, 520 rows, 59 unresolved, comparisonChanges=0; not a genuine baseline/current compare.
- Compare JSON: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6fa6b0695f2e8e83553b8266831a2c46babfd452c1534dcd728029a55c7f0f8c/a7fe0003e1dff35960086c0d13c6d5c683ae8592794ca98ee4ca007090328b51/probability-e7b9a0a14bc5741afdc6f63e.json

## Scenario handoff

The following exact CSV scenario IDs remain unresolved for current-source MCP evidence:

prob_famine_relief_dense; prob_famine_relief_blocked_island; prob_soviet_extraction; prob_humanitarian_border; prob_capacity_exhausted_border; prob_outbreak_reception; prob_nuclear_evacuation; prob_genocide_escape; prob_authoritarian_pushback; prob_destination_selection_internal; prob_destination_selection_persecution; prob_corridor_acceptance; prob_forced_return; prob_integration; prob_opposition_channel; prob_disaster_flight; prob_bombing_exodus; prob_requisition_donor; prob_relief_donor; prob_cleanup.

No row is exact, bounded, sampled, or probability-proven for the current source. The adapter schema did not accept the nested FROM and target objects needed to resolve route, destination, donor, cost, capacity, ideology, exposure, stock, cooldown, and terminal inputs.

## Static findings that are not probability claims

- Destination candidate weights start at zero, add only valid positive contributions, clamp to 0-to-1000, and leave the target unbound on a zero total.
- Relief donor rows are sparse; invalid rows are skipped, valid rows receive bounded route, relation, ideology, persecution, stock, and headroom contributions, and a zero total returns no_candidate.
- Corridor acceptance and rejection are score races gated by a valid pending offer; bases are 20 and 10 with the documented humanitarian, democratic, and hostile factors.
- Six missions have explicit activation, timeout, completion, cancellation, and cleanup paths; decisions use repeatable fire_only_once=no plus removal and re-enable timing.
- No package-owned opposition pool or registry was found.
- No MCP evidence supports claims of starvation, dominance, repetition, timing drift, rank reversal, or terminal cleanup safety.

## Parent actions

1. Let concurrent source changes settle and run a fresh probability_inspect.
2. Re-evaluate all 20 IDs with typed scopes and complete external factors.
3. Add complete MCP manifests for destination, safe donor, relief donor, and opposition pools.
4. Run explicit numeric-range sweeps and fresh renders.
5. Run a genuine same-scenario baseline/current probability_compare after the decision-visibility owner patch.
6. Verify the current emergency-airlift split of legal air experience >10 versus AI factor branch >50. The factor is currently positive and not inverted, but impact is unresolved.

No weights or balance targets were chosen by this auditor, and no source patch was applied.

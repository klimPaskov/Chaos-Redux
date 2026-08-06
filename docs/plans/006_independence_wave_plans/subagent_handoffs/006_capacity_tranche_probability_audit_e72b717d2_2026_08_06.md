# Event 006 capacity-tranche probability audit

Evidence date: 2026-08-06.

Audit owner: `chaosx_ai_probability_auditor`.

Audited commit: `e72b717d2b6ebe699a3f0a43d4b43431394b073c` (`fix(event006): admit attested carriers to capacity transaction`).

Accepted pre-patch snapshot: parent commit `3dfdfc9b051cbb3c9f79c79f0ae69c5529be4e1b`.

Verdict: **bounded source evidence; runtime probability and before/after delta unresolved**.

The commit adds exact automatic-readiness wrappers and deterministic capacity-reservation witnesses for IW-023 (TRA, state 84), IW-033 (KAR, state 146), and IW-041 (CRI, state 137), then calls all three from the Liberations capacity transaction. The installed probability adapter does not recognize scripted-trigger capacity witnesses as a weighted pool, so it reports zero custom-pool candidates and cannot prove a package selection probability, deterministic capacity success, rank ordering, starvation, or a 21/20 release result.

## Scope and source surfaces

The primary source is `common/scripted_triggers/006_independence_wave_triggers.txt:533-565,958-1041,1098-1125`.

The new readiness wrappers set `independence_wave_execution_package_id`, enter the exact carrier scope, require the package identity and runtime preflight, and recheck the package anchor through `is_independence_wave_candidate_anchor_available`.

The new `independence_wave_liberations_capacity_try_iw_033`, `independence_wave_liberations_capacity_try_iw_041`, and `independence_wave_liberations_capacity_try_iw_023` blocks gate on selected-count capacity, earliest chaos band, readiness, Event-005 country/anchor/host exclusion, duplicate country/anchor prevention, and reservation-group uniqueness before appending package, country, anchor, and group arrays and incrementing the selected count.

The central transaction clears its temporary arrays, captures chaos band and target count, executes the complete deterministic try list, then requires exact target count, equal package/country/anchor/group array lengths, and selected-anchor owner coverage.

Supporting identity and scope helpers are in `common/scripted_triggers/006_independence_wave_package_triggers.txt`, `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt`, `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt`, and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.

The same commit also changes `common/scripted_effects/006_independence_wave_scenario_effects.txt` to use file-scoped distance literals in unsupported fields; that change is outside this capacity-weight audit and has no recognized probability surface.

## MCP provenance

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

The current probability source revision for the trigger snapshot is `ec3fd2a80e7a70b9556167d7964ea4a6ca11c336c250f9d541ce887e4e054099`.

### Mandatory source inspections

| Surface and adapter | Source hash and result | Artifact or blocker |
| --- | --- | --- |
| Central capacity trigger, `custom_weighted_pool` | `bb73400fe73836b7c969061da700e7b3771f0c9ab943c03dd0857b1e9ea2b1f7`; `poolComplete=false`; 0 candidates; 0 required inputs; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3210b0a6cc29ebc6997a1bd11bf9479bc37b392beb2597377a0aa2fddfe3fb22/8b72f6ad96a39953c7250b2aea2428e3f8890a4933a3fcba80ba418531edd696/probability-inspect-bb73400fe738.json` |
| Central capacity trigger, `random_list` | No weighted blocks matched this request | Exact blocker: `PROBABILITY_SURFACE_EMPTY` |
| Central capacity trigger, `direct_random` | No weighted blocks matched this request | Exact blocker: `PROBABILITY_SURFACE_EMPTY` |
| Region 03 allocator (`IW-023`), `random_list` | `ff114c943badadd55246dac02b8e5ec434090d0339957dd696559afa17b360bf`; complete 8-candidate/8-input pool; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b983da7c81c4095360b663b6858b615a00997d6e08fe2dc53cd849459ac3d2d/0f93c966a3a3581e89f0c288e660be4bef00a24ef1368ec49bdefaccaa87b632/probability-inspect-ff114c943bad.json` |
| Region 04 allocator (`IW-033`/`IW-041`), `random_list` | `e8f1792fa6b12a426551789a259fb67b570cb5194059ccc17e433ade122af2eb`; complete 8-candidate/8-input pool; 0 unresolved | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17ee9caa4bc1afa1f1874d421b3423ffc12a3124408274f78d814057c3e4d7b2/e3683629424c551fad79297bc64550108e6f601da157f07a1030c5e106f97642/probability-inspect-e8f1792fa6b1.json` |

The Region-03 and Region-04 random-list inspections prove source-level candidate discovery only. They do not prove that `can_plan_independence_wave_package_*`, anchor ownership, host survival, Event-005 collision, attestation, or reservation-group gates resolve in a live state.

The previously inspected outer allocator remains a complete 14-entry `random_list` with source hash `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83`; current evaluation evidence for that pool is recorded below.

### Capacity scenario evaluation

Scenario set: `E6_CAPACITY_TRANCHE_SCENARIOS_E72B717D2_2026_08_06` with `IW023_READY`, `IW033_READY`, `IW041_READY`, and `TARGET_REACHED`.

The declared scenario records named selected count, target count, chaos-band threshold, carrier tag, anchor state, host-clear state, Event-005-clear state, and reservation-group-clear state. The custom-pool adapter still found zero candidates because those are scripted country/state scopes and temporary-array effects rather than a declared weighted-pool surface.

Evaluation analysis: `probability-4d55b19fa4afb1881aacdaf6`.

Scenario hash: `9276120b474d698795521ad1c10c9066f7b9ccd091c7289811f7596dc11ebaba`.

Result: `PROBABILITY_ANALYZED`, 4 scenarios, 0 candidates, 0 unresolved rows, and diagnostic `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` stating that normalized probabilities are withheld.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1299176cbb757f3737dc9c736c84aa7a9aeb7e694dd8ec14ed483cd1ba9736c/6431b1b05fcba036ee01b6857657e9a146909343e0228eea6302da6e60b866b5/probability-4d55b19fa4afb1881aacdaf6.json`.

The ranking and unresolved renders for this zero-candidate surface are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0a50ed502c0af04f2bd2c2473e27451363f28e9f92c706e11270cf5ef9aa498/9f7b881f0a7d14a168af7e435b355a45d0fbd2307cf88fd1e80b50c674b2119e/probability-probability-4d55b19fa4afb1881aacdaf6-ranking.svg` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/57772fc2ff5bbda4948712cf02419be7c86ca70769ce59fd96c45ca99a6efdea/probability-probability-4d55b19fa4afb1881aacdaf6-unresolved.svg`.

Classification: **unresolved adapter coverage**, not an exact or bounded package probability.

### Outer allocator evaluation and sweep

Scenario set: `E6_CAPACITY_OUTER_SCENARIOS_E72B717D2_2026_08_06` with `R03_MAC_OPEN`, `R04_ALL_OPEN`, `R04_KAR_BLOCKED`, `R04_CRI_BLOCKED`, and `CAPACITY_20_WITNESS`.

Evaluation analysis: `probability-77e59bf4c6b25832f36a154f`, scenario hash `fd3f751984611c6072621ed178ef3e5aee170c13afe4e900d39ea955173646e8`, 5 scenarios, 70 candidate rows, 14 unresolved items, and 0 diagnostics.

JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5ea3f7ded54ebe963e42dfd223ea1ec29abdb524db4ad76d0a5c1df52425781/7957d51115719c9ab12837ad7d3a602d1a5e6ec2bce5100ddf2cdfae825b1597/probability-77e59bf4c6b25832f36a154f.json`.

The ranking, matrix, and unresolved renders are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8bc7a191db4cd78a864e30faa8a17c9148d314281ccd52ff85e053209bdbed91/dadea469b54eb8a4daf1f53f8e34556a587ae5d793ef717a0e637ade64f1435c/probability-probability-77e59bf4c6b25832f36a154f-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bde4b47cf89dbd532ad61392e7934e13e4cc9d9c53814a4a408234542e9d8d4b/6516c12fa1772658a1ae49d78f8ec5ea85ed7e12d8749ec836587ed11e36faed/probability-probability-77e59bf4c6b25832f36a154f-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/c954684b990b6723c5087aa715d0d9f618ff7489af9ba8af904fd9e0c58e0968/probability-probability-77e59bf4c6b25832f36a154f-unresolved.svg`.

The sensitivity pass reused the current outer pool under `E6_CAPACITY_OUTER_SWEEP_E72B717D2_2026_08_06`, varying `wave_chaos_band`, `capacity`, and `target_count` across three declared numeric states with pairwise and rank-reversal search.

Sweep analysis: `probability-53372ca822df577de9fb7329`, scenario hash `f668719f820faa7ca52cd612204b025e2726d203ee63388e8568d04fd189452e`, 3 scenarios, 42 candidate rows, 9 sweep points, 14 unresolved items, and 0 diagnostics.

The authoritative sweep JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba3b84bda51dfd0b0766e4eff6a058c407a585c7c853fac2a200fbed5ccec256/2a22bf54c44bdc954b18559f8a633efeec2cc6fafb27ce126f5e82968ecf29a0/probability-53372ca822df577de9fb7329.json`.

The explicit `hoi4.probability_render` receipt returned sensitivity `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf081b9686fef69622deefd3d06d30e1645bc4326b08b48052f62051a916d795/986a6c73772f41170fcc663904d8d70703ad63b579f604e3bf819461f0677e80/probability-probability-53372ca822df577de9fb7329-sensitivity.svg`, threshold `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/2140988d8218a9919f25615039b02462afb1a3ec4280e400d659b6edc5bac714/probability-probability-53372ca822df577de9fb7329-threshold.svg`, and unresolved `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/d8c57adaca3c92b31126858b759b68f366cdca28d2bd342afedc0c849ae4bdb6/probability-probability-53372ca822df577de9fb7329-unresolved.svg`.

Classification: **bounded incomplete sweep**. The adapter retained unresolved dynamic package and scope gates, so no rank reversal, dominance, starvation, or normalized IW-023/IW-033/IW-041 probability is proven.

### Before/after comparison status

The accepted pre-patch Git snapshot exists at parent commit `3dfdfc9b051cbb3c9f79c79f0ae69c5529be4e1b`, but the installed compare route cannot address Git revisions.

Attempting `before = { path = "common/scripted_triggers/006_independence_wave_triggers.txt", revision = "3dfdfc9b051cbb3c9f79c79f0ae69c5529be4e1b" }` failed validation with exact MCP blocker `unrecognized_keys: revision`.

Attempting the route's path-suffix form `common/scripted_triggers/006_independence_wave_triggers.txt@3dfdfc9b051cbb3c9f79c79f0ae69c5529be4e1b` failed with exact blocker `PROBABILITY_SOURCE_NOT_FOUND`.

A same-source capability receipt used the four capacity scenarios with the current path for both `before` and `after`.

Same-source compare analysis: `probability-b7d914c1a5770727c14b0fcc`, source hash `bb73400fe73836b7c969061da700e7b3771f0c9ab943c03dd0857b1e9ea2b1f7`, scenario hash `83cd088d4587a39686c8cdbeca6ab52ae1f1487483265551f715be28672a72d2`, 4 scenarios, 0 candidates, 0 unresolved, and `comparisonChanges=0`.

Same-source comparison JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94612d51b048955e9628efc221963e359fcf92ea7c6e0c07d2bbcf6bbfe60404/daf9ed8ef4e40a5cf022e6414cbcbd82d25ddd6743e1e703be34e83c682f6fd3/probability-b7d914c1a5770727c14b0fcc.json`.

Same-source comparison render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/596d1d688d60d79758028fcf16e7d3fd7597cfa836f6982ed381b3cc27847cd4/probability-probability-b7d914c1a5770727c14b0fcc-comparison.svg`.

This is a capability receipt only, not evidence of the e72b717d2 before/after delta.

## Structural event evidence

The required read-only event scan used selector `{ kind = file, sourcePath = events/006_independence_wave.txt }` and returned `EVENT_INSPECTED_PARTIAL`, revision `be8a459e712970f13eb790070ee12b3a049d0cca9adde963a523ddcd7e71f529`, graph hash `fb0ec7e0b63fe739af673fafab0b9f9a97b89f6f1814f1a5de3cd1b4bd769702`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/282a970fa19904ae85e621a6d5c5483f65870133144c211f3355189e3539f6fd/7f59a62d7c82feee9eae600d8442db3e484948d231426d31c335a8b6144d603b/event-scan-be8a459e7129.json`.

The matching unresolved event render returned `EVENT_RENDERED_PARTIAL` with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b53d3b5c4db34b2a40783515ac8d6414cce546ef24964ffeb15c88dea500e7f/1a0db99092758580c97032bb92f73019d21c9084b963e649df95cdb2ec6aa37a/event-unresolved-be8a459e7129-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/560e05604764da9b3b28608470041114cd8bec1eb93a94355e211212459de193/b347054e0746a3e91b628c266d9201b84330d93c920a188f7c19e190b95c887c/event-unresolved-be8a459e7129.json`, and SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b4e8aa48d59a52366eb082e69f4b35d122f721197db3acced210b5fa96d9c81/30355357289b9212e6e5902ad07913b7236d7dfb2539bcc243f4c251efee00bc/event-unresolved-be8a459e7129.svg`.

The structural scan is workspace-wide and MCP reports deferred helper projections with 8,145 unresolved nodes and 2,119 diagnostics; it does not replace the probability evidence and does not prove runtime capacity success.

## Findings

- **Pool completeness:** the central scripted-trigger adapter exposes no weighted/custom-pool candidates; Region 03 and Region 04 source random lists are complete at 8/8 each, and the outer allocator source pool is complete at 14/14.
- **Readiness validity:** each new wrapper requires exact package identity, package preflight/attestation, origin safety, and anchor availability; each try block repeats Event-005 country, anchor, and host exclusions and reservation-group uniqueness before appending aligned arrays.
- **Selection semantics:** the central capacity witness is a deterministic existence test, not an AI score race or probability-proportional draw. The actual package draw remains in the separate dynamic random-list allocator.
- **Ordering risk:** the transaction calls IW-023, then IW-184, then the new IW-033 and IW-041 rows. The constants set earliest bands `p23 = 0`, `p33 = 0`, `p41 = 1`, and `p184 = 1`, so the call order is not monotonic by earliest band. This can omit IW-033/IW-041 from a low-target deterministic witness when earlier rows already satisfy the count; the current source comments describe a capacity witness rather than a package-priority policy, so this is a bounded selection-bias risk, not proof of runtime starvation.
- **Dominance and starvation:** no exact candidate dominance, starvation, or rank reversal is proven. The outer sweep retained 14 unresolved dynamic inputs, and the central adapter had no candidate pool to rank.
- **Repetition and exploit risk:** country, anchor, and reservation-group duplicate guards plus exact-count/aligned-array checks are source-visible fail-closed controls. The MCP route cannot prove rollback, reservation release, host survival, or a complete 20-release sequence.
- **External-factor completeness:** the named scenarios declared numeric count/band fields and symbolic carrier/anchor/host/Event-005/group conditions, but typed MCP state cannot represent the event-target scopes, country ownership, controller, package attestation helper, prior-wave arrays, or temporary-array transitions used by the trigger.

## Recommended follow-up (do not apply in this audit)

1. Add a supported typed MCP fixture or adapter manifest for deterministic capacity witnesses, including country original tags, anchor owner/controller, host Event-005 exclusion, attestation, chaos/count variables, selected arrays, and reservation-group state, then rerun the four capacity scenario IDs.
2. Preserve parent commit `3dfdfc9b0` as an explicit source snapshot or add revision-aware compare support, then rerun `hoi4.probability_compare` with the exact same scenario hash; the same-source receipt above must not be treated as a patch comparison.
3. Run a complete target-count matrix at 6, 8, 10, 14, and 20 with all earlier carriers blocked/open permutations to determine whether IW-023/IW-033/IW-041 are intentionally witness-only or should be ordered by earliest band.
4. Keep the Region-03 and Region-04 8-entry pools and the outer 14-entry pool under the same inspect/evaluate/sweep/compare evidence whenever another carrier is admitted or removed.

## Skipped analyses, blockers, and uncertainty

- `hoi4.probability_sequence` was not run because no complete custom-pool manifest, cadence, cooldown/recovery, reservation release, reset, timer, or terminal-state contract is exposed to the adapter.
- `hoi4.probability_simulate` was not run because no uncertain input distribution or seed was declared and simulation cannot substitute for missing country/state scopes.
- A true before/after `hoi4.probability_compare` is blocked by the exact MCP revision/path limitations recorded above despite the accepted Git pre-patch snapshot.
- No exact selection probability, click probability, timing distribution, 20-release success claim, or live-game result is made.
- `python -B .tools/audit_event6_allocator.py` passed for the current repository snapshot and reported 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 23 attested packages, 22 compatible reservation groups, and 20 admitted packages in its static witness. These counts are static repository evidence and not runtime probability evidence.
- No gameplay, AI, event, trigger, effect, localisation, asset, or runtime file was changed by this audit; only this handoff is new.

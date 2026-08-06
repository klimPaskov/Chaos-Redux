# Event 006 central capacity expansion probability audit

Date: 2026-08-06

Scope: read-only audit of the uncommitted central capacity expansion in `common/scripted_triggers/006_independence_wave_triggers.txt` and its MAC/BOS exact-anchor changes in `common/scripted_triggers/006_independence_wave_macedonia_package_triggers.txt` and `common/scripted_triggers/006_independence_wave_bosnia_package_triggers.txt`.

Worktree anchor: `efba9b1e2ba23869078341723de4eb6d744c2202` (`docs(event006): reconcile current capacity authority`). The three audited worktree files were modified and were not changed by this audit. Their local SHA-256 values at audit time were `5219716EE9DBFF2E6AB87EAE30134E4E24F3330F1C3E77A4DF3352E1943396D` (central triggers), `3FCF9F16C57DDEF2405AC1E41A383AD701AB628439C97C7606D7217FB0991B01` (Macedonia triggers), and `F8D9936935110D803BF88AC94B31BD2D82254F3792742D1A406FFBECBB90E61F` (Bosnia triggers).

## Audited surfaces

- Central deterministic capacity witness: `is_independence_wave_liberations_cluster_member_capacity_available` and `independence_wave_liberations_capacity_try_iw_012`, `_iw_026`, `_iw_029`, `_iw_070`, `_iw_071`, `_iw_072`, and `_iw_173` in `common/scripted_triggers/006_independence_wave_triggers.txt`.
- Host and anchor collision gates: `is_independence_wave_liberations_capacity_host_clear_of_event5`, `is_independence_wave_liberations_capacity_anchor_clear_of_event5`, and the Event 005 opening-core helper in the same file.
- Exact MAC and BOS package admission: `is_independence_wave_exact_package_iw_026_tag_available` and `is_independence_wave_exact_package_iw_029_tag_available` in the package trigger files above.
- Runtime package dispatch and region pools: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt`, `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt`, `common/scripted_effects/006_independence_wave_packages_region_06_effects.txt`, `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt`, and `common/scripted_effects/006_independence_wave_package_allocator_effects.txt`.

The current transaction order is IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-017, IW-018, IW-019, IW-012, IW-026, IW-029, IW-070, IW-071, IW-072, IW-173, IW-014, IW-023, IW-184, IW-033, and IW-041. This is a deterministic score/witness race, not a probability-proportional selection claim.

## Mandatory MCP provenance

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Current MCP source revision for all fresh calls: `8334b79e6e1a4a7d0614281c4452be26afc8d6b01a3093a84686586c2921513e`.

Fresh central `hoi4.probability_inspect`, adapter `custom_weighted_pool`, source hash `554a916178de8e30579ff90dadca61e001e9099bcc64a4e0b45c4421f9cd6c9f`, returned `PROBABILITY_SOURCE_INSPECTED` with `poolComplete=false`, zero candidates, zero required inputs, and zero unresolved items. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/928a47721a042ef0e8f3d945afdd49ff710021b00c7149bda2af5f0b50cf2f05/5d62fb3a015d6377015f612ff75e6f02457974aaba7a619364ac7e192d671d65/probability-inspect-554a916178de.json`.

The same central source under `random_list` and `direct_random` returned `PROBABILITY_SURFACE_EMPTY` with the exact blocker `No weighted blocks matched this request`.

Region source inspections found complete source-level pools, but these do not prove runtime trigger eligibility or central witness selection:

- Region 01 random-list source for IW-012: 9 candidates, 9 required inputs, 0 unresolved, source hash `183d00a517723c51d3c8272fd2e1e28040d01d655b314fdb02c33e880c50f2b7`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/852ff1034584729470aa7c0d226a1523e601cd78e6c7e19eda6b972fc51888fd/9a76e5d0647dca68ec7555c7025c1d611ee8a321c9114e1751a023789b5535eb/probability-inspect-183d00a51772.json`.
- Region 03 random-list source for IW-026/IW-029: 8 candidates, 8 required inputs, 0 unresolved, source hash `ff114c943badadd55246dac02b8e5ec434090d0339957dd696559afa17b360bf`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab881e792e9545705b567cd6b9a115e896d1ce845e6bd05cad37a91ffa876cc2/ecf689579198b778524300293405c5f5e6dec1877d07058ea21ab7f79d7b5e1f/probability-inspect-ff114c943bad.json`.
- Region 06 random-list source for IW-070/IW-071/IW-072: 12 candidates, 12 required inputs, 0 unresolved, source hash `63b4f675efe3c0fa0604574ea9af34746c0289fc2927ab8c72651ad606a72696`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0fdd8724a11aebdedebc30f7ba5beb52adbb3a8c808dc3ce39df7eae34/edfb337daeb5e54d88766ae562b5920abe8b6155c54fe669b95ccf4b356acab0/probability-inspect-63b4f675efe3.json`.
- Region 13 random-list source for IW-173: 19 candidates, 19 required inputs, 0 unresolved, source hash `b4602eedcf453e4eeda1b2bd54f4df3be4bad9fa3aab372a6a545c036d0161cc`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e58ce4c548d4567f1141515e8a2226f88d4994a91a192771c566e7fe8acf6956/14348f50a358c8857360d64e6a7d5d30977b9671c78557f82192a52cc71fbb35/probability-inspect-b4602eedcf45.json`.
- Outer package allocator random-list source: 14 candidates, 14 required inputs, 0 unresolved, source hash `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4e4ce40fe0406a7bdde19c10b1df22612bb149e08d12ece0e80d70ab80d9224/b7b307554cd945166d5afb5ddc082bf26495c34e3f013aa8dc452d4a8bd0bd1c/probability-inspect-bc6f7ff8598d.json`.

## Central capacity scenarios and result classification

Scenario set ID: `E6_CAPACITY_EXPANSION_SCENARIOS_CURRENT_2026_08_06`.

The declared scenarios were `IW012_ICE_READY` (IW-012, ICE, anchor 100, FIN owner, clear host/Event 005/group, chaos band 1, selected 0, target 8), `IW026_MAC_YUG_READY` (IW-026, MAC, anchor 106, YUG owner, clear, band 2, target 10), `IW029_BOS_YUG_READY` (IW-029, BOS, anchor 104, YUG owner, clear, band 2, target 10), `IW070_ARM_EVENT5_SHARED` (IW-070, ARM, anchor 230, clear, band 3, target 14), `IW071_GEO_EVENT5_SHARED` (IW-071, GEO, anchor 231, clear, band 3, target 14), `IW072_AZR_EVENT5_SHARED` (IW-072, AZR, anchor 229, clear, band 3, target 14), `IW173_HAW_READY` (IW-173, HAW, anchor 629, USA owner, clear, band 4, target 20), and `TARGET_REACHED_AND_HOST_RISK` (selected 20, target 20, host/Event 005/group not clear).

`hoi4.probability_evaluate` with adapter `custom_weighted_pool` returned `PROBABILITY_ANALYZED`, analysis ID `probability-e852ac5e349266a53fd8959c`, source hash `554a916178de8e30579ff90dadca61e001e9099bcc64a4e0b45c4421f9cd6c9f`, scenario hash `fd27368bf98c0e79c59e2aef185aaa68fc50a117500ec72b98d6df1080e7c635`, eight scenarios, zero candidates, and one `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` diagnostic. Normalized probabilities were withheld. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/debfc877fbfd9db0e899b011ce3a86a2c9a12f18ddec3f3d5b314535da6bde3f/65cabaf90e4bf0438b38d4f183936137e01a812eec596660fb4e38a0e90c1d7e/probability-e852ac5e349266a53fd8959c.json`; ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a4797964df171c00e330c459ec0ff08e1f2edf1ac754aa6190c447dcd397413b/2a50d54b14db0f93192ecbcee1bcf6f9f7078b8c8ee6bf768a8688d555684d46/probability-probability-e852ac5e349266a53fd8959c-ranking.svg`; unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/4d78f9521becb7f0c351e19d6271849b1980dfde4215321da1b485692bfb561d/probability-probability-e852ac5e349266a53fd8959c-unresolved.svg`.

Classification: unresolved adapter coverage. The MCP adapter can discover the custom surface but cannot model its scripted-trigger scope, temp-array mutation, or runtime package gates. No exact package probability, normalized ranking, dominance, starvation, or repetition rate is proven by this call.

## Outer allocator evaluation and sweep

Scenario set ID: `E6_CAPACITY_EXPANSION_OUTER_SCENARIOS_CURRENT_2026_08_06`.

The declared scenarios were `EXPANSION_ALL_OPEN`, `EXPANSION_YUG_CARRIERS_ONLY`, `EXPANSION_EVENT5_SHARED_HOSTS`, `EXPANSION_WORLD_COLLAPSE`, and `EXPANSION_TARGET_REACHED`, covering all-open, MAC/BOS-only, shared ARM/GEO/AZR hosts, maximum chaos, and target-reached states. Each supplied chaos band, target count, capacity, package-open booleans, and Event 005 shared-host state.

`hoi4.probability_evaluate` with adapter `random_list` returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-deb60a5c5afdf33dff80e189`, source hash `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83`, scenario hash `21347e65b47fee8c1506c4d5c70f180107570c1573350b6aecbb8a00c9943708`, 70 candidate rows, and 14 unresolved rows. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b1fbeda6452668868b16653b2bfb3e3b1413e3c8b00505c7596ce36ac4d7121/c131f4004a16de2021128cc9a828c47b393f8f3d5d14f6d20671c202c4e41e58/probability-deb60a5c5afdf33dff80e189.json`; ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c38c2f5e229791077a16c40bac0976c271ecbc884cfa0acc0fff7c40f57b7762/44c164f3096dfbc8de82de9e85f238ba1146f357aacdd8cbea7a3b9c2fa32e28/probability-probability-deb60a5c5afdf33dff80e189-ranking.svg`; matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/412a77bd42d5271dbe25201df8b01f30fb9d312347c1736460233e98ecef7514/59ef3751aa8311750e59f1f330f806a8e4d918f49038fa03fbcc5633d6d1aa45/probability-probability-deb60a5c5afdf33dff80e189-matrix.svg`; unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/aaaa4a7d347ca5d1d8689d5e960733f9f44b64cb192e42442bf92d3cc1c3ef27/probability-probability-deb60a5c5afdf33dff80e189-unresolved.svg`.

`hoi4.probability_sweep` used the same outer source and paths `chaos_band`, `target_count`, and `capacity`, with three steps, pairwise sensitivity, and rank-reversal search. It returned analysis ID `probability-df2db183c71e54c4cd42114e`, source hash `bc6f7ff8598df33b610442e6ada24c28d7d82167fe135474deb18094b3b6cf83`, scenario hash `c0de5b3972be69d407215e3ac19de40d31ccc3d928fec9058b3479d6b5c9ed0c`, 15 sweep points, 70 candidate rows, and 14 unresolved rows. The rendered sweep returned `PROBABILITY_ANALYZED_PARTIAL` and made uncertainty visible. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ac226dd67f9ffbfa2eaa387a243626eac8c69bf17c9abe2a0bd7c0b2b6b4f184/84765cc2a670f5f313c66b58941731217b9c3c80a36621cb9128d6f43a0417ba/probability-df2db183c71e54c4cd42114e.json`; sensitivity SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00b5a0160c5a333a5ef53693dde50803844efd49066ad5119cc26aad63880699/d963b33a54705c405a7f81246e9bc92117c9f186189919b01cd7f25abffa5292/probability-probability-df2db183c71e54c4cd42114e-sensitivity.svg`; threshold SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/029dd17bf2e2344fff49d7812ade843573801fbe3cdbd0ddf71febec3cce2b33/probability-probability-df2db183c71e54c4cd42114e-threshold.svg`; ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05ef133baaf8ec0226c87e8154dd4426d0d1d4a915a7d7e5752954f59c49b279/9af6dafd8569d909b46d9c1cc6b56a825af30f8eb23cc356b64a6f01fc1067be/probability-probability-df2db183c71e54c4cd42114e-ranking.svg`; unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b376452dd35a669b20b3ba5787e6af6347617460240eb4e6e0da2f2ae9a45962/4eca848cbdb317048dc9fd62a11145d3a725cecfe7ece9ec6d7f5e4c1dbdcad6/probability-probability-df2db183c71e54c4cd42114e-unresolved.svg`.

Classification: bounded incomplete score/sensitivity evidence only. The outer adapter exposes source-level candidates but not all scripted trigger scopes and temp-array state, so no package-specific rank reversal, exact probability, dominance, starvation, or repetition conclusion is valid.

## Comparison capability and blockers

The required true before/after comparison was attempted with the current central trigger path and the prepatch worktree anchor. Passing a `revision` field in `before` was rejected by input validation with the exact error `unrecognized_keys: revision`. Passing the current prepatch commit suffix in the path (`common/scripted_triggers/006_independence_wave_triggers.txt@efba9b1e2`) returned `PROBABILITY_SOURCE_NOT_FOUND` with the exact blocker `Probability source path was not found`. Therefore no true prepatch/postpatch comparison artifact exists.

A same-path current/current `hoi4.probability_compare` capability check did complete as `PROBABILITY_ANALYZED`, analysis ID `probability-97963fe8e116df871d9a7357`, source hash `554a916178de8e30579ff90dadca61e001e9099bcc64a4e0b45c4421f9cd6c9f`, scenario hash `288766a33be6164575d399732c182a4970553e840926d3e30688fba0a893b4df`, `comparisonChanges=0`, and the expected `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` diagnostic. Artifacts: JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a340ff825fe4ce64e201138d7c205becf5355c65d965afffa613809ff6b343e5/5c127e7837b151a9c21e81a7eee9f523694e144acf3e5ff3667702c7640a4028/probability-97963fe8e116df871d9a7357.json`, comparison SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/54484a335404a46eeed5d77a063938ee973e093c3587a0cc75a924fff4b5f769/probability-probability-97963fe8e116df871d9a7357-comparison.svg`, unresolved SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/92569cb36baad49ef84bece57f031d28dada118d8af24ec65658aee0042b0fb7/probability-probability-97963fe8e116df871d9a7357-unresolved.svg`.

This same-path result is a route-capability record, not evidence that the uncommitted patch has zero behavioral change.

## Structural event evidence

`hoi4.event_inspect` scan of `events/006_independence_wave.txt` returned `EVENT_INSPECTED_PARTIAL`, revision `be8a459e712970f13eb790070ee12b3a049d0cca9adde963a523ddcd7e71f529`, graph hash `fb0ec7e0b63fe739af673fafab0b9f9a97b89f6f1814f1a5de3cd1b4bd769702`, 9,464 events, 14,614 options, 36,847 edges, 2,119 diagnostics, and zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e33692a11b08e809bdd9175e50d7a30301955064e06873d4f4e4bf68b0191fc/6dc236904e9f180015e789dca1c22fede48fa2c48584b1dbd30fb06b6d2984d3/event-scan-be8a459e7129.json`.

`hoi4.event_render` unresolved view returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash. It produced a manifest, JSON, SVG, and PNG; the source-linked SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b4e8aa48d59a52366eb082e69f4b35d122f721197db3acced210b5fa96d9c81/eb8e72e7be1f1d28062f7fd9755fe6ea548e5143102ab6105220575fe698f8b3/event-unresolved-be8a459e7129.svg`. The tool reports deferred workspace-wide helper projections but no blocking diagnostics.

## Static and source findings

The repository audit `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 23 attested packages, 22 compatible reservation groups, and 20 static standalone witness admissions. The audit also reports automatic counts 6/8/10/14/20 and the expected joint order `Event 005 anchors -> Event 006 anchors -> optional territory -> lock`.

The constants are `p12=1`, `p26=0`, `p29=0`, `p70=0`, `p71=0`, `p72=0`, and `p173=1`. Thus IW-026, IW-029, and IW-070/071/072 are eligible at every nonnegative captured chaos band if all gates pass, while IW-012 and IW-173 begin at bands 1 and 1 respectively. The new calls occur after the earlier IW-019 call and before IW-014/IW-023/IW-184/IW-033/IW-041, so the source order is not monotonic by the package earliest-band constants.

The MAC and BOS exact admission helpers now require state 106/state 104 to be owned by YUG. This closes the former broad `owner != self` admission, but it can intentionally starve the package whenever the anchor is owned by another tag. The central wrappers repeat the exact YUG owner check.

The unconditional `NOT = { tag = SOV }` host exclusion was removed from `is_independence_wave_liberations_capacity_host_clear_of_event5`. The replacement only rejects countries currently owning or controlling an Event 005 opening-core state. This increases admitted-host coverage, but the MCP adapter cannot prove whether a host that has no currently owned/controlled opening-core state is nevertheless reserved by an Event 005 carrier or will be claimed before the Event 006 transaction. This is a bounded collision/false-positive risk, not a proven runtime collision.

IW-070/IW-071/IW-072 deliberately omit the Event 005 country-clear helper because ARM/GEO/AZR reuse Event 005 carrier tags. Their source comments defer the joint country/state reservation to the shared transaction after the Soviet contribution freezes. That dependency is not modeled by the probability adapter, so a collision or ordering failure remains unresolved if the shared arrays are not materialized before this witness.

The deterministic witness appends package, country, anchor, and reservation-group IDs and increments selected count for each admitted candidate. The checks cover target cap, earliest band, package readiness, country duplication, anchor Event 005 core clearance, anchor duplication, host clearance, and group duplication. They do not expose a weighted candidate pool to MCP.

## Recommendations to the owner

- Keep the central witness as score-only until an adapter can evaluate scripted scope, temp-array mutation, Event 005 reservation state, and transaction order. Do not describe it as a click probability or normalized random selection.
- Add a typed fixture or MCP-supported custom-pool manifest that exposes all 23 transaction candidates, their gate traces, and post-append state so the same eight central scenarios can be re-run with exact candidate completeness.
- Add an explicit joint Event 005/Event 006 scenario for SOV and for ARM/GEO/AZR shared carriers where Event 005 has reserved a country but does not yet own the anchor. Resolve whether the intended result is rejection, reroll, or deterministic precedence.
- Add target-count/order scenarios with IW-026/IW-029 and IW-070/IW-071/IW-072 individually blocked and open. The current non-monotonic call order and zero earliest bands make package-specific starvation a plausible design risk, but it is not proven without a complete stateful adapter.
- Preserve the exact YUG owner requirement in MAC/BOS unless the design intentionally permits alternate former hosts; if alternate ownership is intended, add a bounded candidate set and a separate source admission rule rather than broadening `owner != self`.

## Skipped analyses and uncertainty

- No exact normalized central probability was possible because `custom_weighted_pool` returned zero candidates and `random_list`/`direct_random` returned `PROBABILITY_SURFACE_EMPTY`.
- No seeded simulation was run because the complete candidate pool, state transition cadence, and uncertain external inputs were not declared.
- No sequence analysis was run because cooldown, reset, removal, recovery, and terminal-state manifests for the custom transaction were not available to the adapter.
- No true before/after probability comparison was possible because MCP rejected `before.revision` and did not resolve the current prepatch hash-qualified source path (`@efba9b1e2`). The same-path comparison is only a capability check.
- No package-specific dominance, starvation, rank reversal, repetition, or exploit probability is proven. The findings above are source-bounded risks with explicit unresolved adapter coverage.

This handoff is read-only audit evidence. No gameplay, AI, event, focus, decision, localisation, or runtime source was edited.

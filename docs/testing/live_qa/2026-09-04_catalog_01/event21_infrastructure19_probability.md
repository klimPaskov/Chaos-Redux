# Event 021 infrastructure19 probability baseline

Date: 2026-09-05

This is a read-only baseline for five parser wrappers that the parent is authorized to apply. The affected checks are `event021_parent_event6_package_setup_proven` at `common/scripted_triggers/021_random_civil_war_parent_triggers.txt:82`, `event021_parent_viable_anchor_state` at line 144, `event021_parent_secondary_state_candidate` at line 349, `event021_begin_achievement_history` at `common/scripted_effects/021_random_civil_war_achievement_effects.txt:116`, and `event021_parent_find_event6_package` at `common/scripted_effects/021_random_civil_war_parent_effects.txt:161`.

The authorized repair preserves the strict `>` operator and each existing right-hand side. The trigger source baseline hash is `C333001E5E7A122C73672F1EDDA780EC47ADC90EC7507A2A8A83D53B8AB6BBBB`, the parent-effects baseline hash is `2B3010670576F3C741684AAC2C8A2E590360670871F1AB62FD0BE99C76445D3E`, and the achievement-effects baseline hash is `365130615F3EE29BE9647255820405B4DC525E33976310C69B0DDEEABBC7BEBA`. The postpatch hashes are `7F47BA3F4DCA0D1BFE1B7BF6C586CCECF41E16E112985A97222901911D7BAFD6` for the triggers, `095079037B360867FE7E60B750807725F68D51D1CD4B3CD53924FCFD13F8EE31` for the achievement effects, and `E84C38F6A64EE5C83E81E65AC4D5ED7768BBACBF43C28B4C6EBA0C0CBE6068F6` for the parent effects. No gameplay source was edited by this auditor.

## Mandatory probability inspection

Fresh `hoi4.probability_inspect` on `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` returned status `error`, code `INTERNAL_ERROR`, no files scanned, no artifact, and blocker `Unexpected internal error`.

Fresh `hoi4.probability_inspect` on `common/scripted_effects/021_random_civil_war_achievement_effects.txt` returned status `error`, code `INTERNAL_ERROR`, no files scanned, no artifact, and blocker `Unexpected internal error`.

Fresh source inventory inspection on `common/scripted_effects/021_random_civil_war_parent_effects.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with source revision `d01b0cd3369af2a9668e16e52291e40febfac25cf342b749e141ca38f3261df8`, source hash `b3edc2585d8faa4fc75ba6b5937cc8ccd234868298f0f61ac9c725d8030abf1e`, and eight available `random_list` candidates. The six entries at line 1070 are the Event 021 archetype pool and the two entries at line 5194 are unrelated strange-incident choices. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40be10dc07f0213f63fa975f277c72db42806caf9357ef2e38b8f32d475e0fc4/30884a469273e5298f6189036c5350b42f6714bef42747ef407fd8b9ec552b81/probability-inspect-b3edc2585d8f.json`.

An explicit `custom_weighted_pool` probe for `event021_parent_secondary_state_candidate` returned zero candidates, `discoveryReason: identifier_not_found`, and only the unrelated `random_list` adapter candidates. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ecfb7a1fe549d03d970c753360a543ab846883af26d8b5ed656613da806f4672/345cb8d2528605d328c3c1a83960464039148ea1c117442c754df601426ce644/probability-inspect-b3edc2585d8f.json`.

## Caller and pool boundary

`event021_parent_viable_anchor_state` feeds the deterministic `find_highest_in_array` race at parent effects line 1182. The connected closure at line 1237 is a separate bounded traversal, not a scoring race. This is score evidence only when the candidate states and score factors are declared; no probability-proportional pool is exposed for this gate.

`event021_parent_secondary_state_candidate` feeds `random_owned_state` at parent effects line 2484. This is a dynamic owned-state pool whose members depend on runtime scope and validity. The installed probability adapters expose no `random_owned_state` projection, so no static candidate list or normalized probability is claimed.

`event021_parent_find_event6_package` feeds route evidence at parent effects line 960 and the secondary Event006 front at line 3078. `event021_parent_event6_package_setup_proven` is reached through package completion at line 125 and actor setup at line 2906. `event021_begin_achievement_history` gates committed achievement history. These are eligibility and state-flow gates, not independently weighted blocks in the inspected sources.

The prior six-entry Event 021 random-list fixture is not reused as evidence that any of these five nested checks propagate to a route weight. It remains a separate declared-weight fixture with an incomplete campaign actor pool.

## Baseline classification

`event021_parent_event6_package_setup_proven` is `unresolved` for probability impact because its trigger inspection failed at the MCP service boundary and the gate has no direct weighted block.

`event021_parent_viable_anchor_state` is `score-only` for the downstream deterministic race and `unresolved` for campaign ranking because the complete state candidate set, score factors, and nested gate evaluation are unavailable.

`event021_parent_secondary_state_candidate` is `unresolved` because the dynamic `random_owned_state` pool has no supported MCP probability projection and no declared pool manifest.

`event021_begin_achievement_history` is `unresolved` for probability impact because it is a committed-history eligibility gate and its source inspection returned `INTERNAL_ERROR`.

`event021_parent_find_event6_package` is `unresolved` for probability impact because it is an anchor/package eligibility gate; the parent-effects inventory exposes only the separate `random_list` pool and not helper eligibility.

No dominance, starvation, repetition, rank-reversal, exploit-risk, balance, or exact campaign probability conclusion is supported by this baseline. The manually supplied six-entry weight fixture establishes no infrastructure19 upper or lower campaign bound.

## Skipped or blocked analyses

`hoi4.probability_evaluate` is not used for the five nested checks because the trigger and helper surfaces did not yield a supported candidate pool or a resolvable runtime state declaration. `hoi4.probability_sweep` is not applicable without a supported weighted surface and declared sensitivity ranges. `hoi4.probability_simulate` is skipped because no uncertain input distributions were declared. `hoi4.probability_sequence` is skipped because no complete dynamic-pool cadence, cooldown, recovery, cap, removal, reset, or terminal-state manifest exists.

## Same-scenario comparison

The required comparison used scenario set `E21_INFRA19_GATE_ROUTE_FIXTURE_2026_09_05` with `E21_INFRA19_ZERO_GATE_ROUTE_FIXTURE` and `E21_INFRA19_POSITIVE_GATE_ROUTE_FIXTURE`. The fixture supplies five route weights of 80 and Event006 weight 0 in the first scenario, then all six route weights of 80 in the second. These are declared downstream weights only and do not model any of the five nested gates.

The parent-effects comparison used the exact archived source at `docs/testing/live_qa/2026-09-04_catalog_01/pre_patch_event21_infrastructure19/021_random_civil_war_parent_effects.txt`, the current source at `common/scripted_effects/021_random_civil_war_parent_effects.txt`, and both source-specific forms of the six known line-1070 candidate IDs. It returned `PROBABILITY_ANALYZED_PARTIAL` with analysis `probability-7751187093fb2fc529a9e931`, source revision `fcf567abe45dc7e7178838299c8fbab66a1e8f4735e7007a01246429f2d37f08`, source hash `d3c0977c47cd7384d0710b75fde4cef32ee58c88a332bb94c6cc4ebf74c776e1`, scenario hash `4a4c0a35db9a7347329435bb499259114984317b67961bca9fb1f7d629118a01`, 12 candidate rows, 12 unresolved rows, one `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` warning, and `comparisonChanges: 24`. The adapter resolved only the six current-source candidates; the archived candidate identifiers remained unresolved because their source path differs. Normalized probabilities are withheld, and the comparison does not attribute any change to the five parser wrappers. The JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9894583d777db639a1e23e84413c81d1966c696d8920c05c3ef56d63dcd5c584/296687d1538e80d265771839aad0d474bbf046fef7f9fa0b81d37186b6f4bb22/probability-7751187093fb2fc529a9e931.json`.

The parent-effects comparison render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b335f4f626fb07a62cf5e7c4958dac23fe863e69e2c38446b69163ee1945837a/6356003e8cce06a98d21eaea0836d7e4371028b9b570777e8bc1d3c8d50498d4/probability-probability-7751187093fb2fc529a9e931-comparison.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7ef9010ea0397a64c4c7210995562bc7464a5a5289ae8bf9c7c86397fdf018c/36efae2be951bdad13025980f1e0927f5297d2030189aa3577b867f86698edf5/probability-probability-7751187093fb2fc529a9e931-comparison.png`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/365553cc4fe20b5404e6a2c2f702ebd3a47eb9b6210880a3397cd5507d919089/28daa2b92959622948f20cdaf06443021e840579eef51ceadb2324a6c3bcbaec/probability-probability-7751187093fb2fc529a9e931-unresolved.svg`.

Exact inline before/after comparisons of `021_random_civil_war_parent_triggers.txt` and `021_random_civil_war_achievement_effects.txt` used the same scenario set and candidate declarations and both returned status `error`, code `PROBABILITY_SURFACE_EMPTY`, no analysis ID, and blocker `No weighted blocks matched this request`. The trigger comparison therefore cannot evaluate `event021_parent_event6_package_setup_proven`, `event021_parent_viable_anchor_state`, or `event021_parent_secondary_state_candidate`, and the achievement comparison cannot evaluate `event021_begin_achievement_history` as a weighted surface.

The comparison results are MCP capability limits, not evidence that the parser wrappers have no effect. The five checks remain unresolved for actual infrastructure/availability propagation and any downstream weighted-target change. No manual route-weight fixture is used as gate proof, and no `random_owned_state` candidate list is invented.

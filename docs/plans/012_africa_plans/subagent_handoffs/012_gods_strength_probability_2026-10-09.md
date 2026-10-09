# Event 012 Strength-input probability baseline and comparison — 2026-10-09

Disposition: the read-only before-consumer baseline and the requested one-time same-scenario after comparison are complete. Both MCP analyses were partial because the scenario adapter did not resolve native country-scope and identity helpers.

The baseline probability inspection and evaluation used source revision 99b7ea7e9931bfb7c7596efde3d3d03b2b16dee7f4283205346843e8a4433719. The parent then wired census and army-sample producers and applied the factor consumer patch. The decision roots remain byte-identical to the pinned before source; the post-patch comparison used that pinned source against the current decision file.

No gameplay, AI, event, or other source files were edited by this audit. No Git or game operations were used.

## Scope and source identity

The only weighted roots audited are gods_of_africa_comply_demand and gods_of_africa_permanent_defiance in C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\decisions\012_africa_gods_decisions.txt, at lines 367–457 and 847–924. The second identifier is permanent_defiance; there is no defy_demand decision id.

The parent’s eight-file before manifest pins HEAD c158d857fc06feb39853b616aad9daf57f4b28c8. All eight before copies still match their manifest SHA-256 values. Three current files differ from their before copies: common\scripted_effects\012_africa_gods_effects.txt, common\scripted_effects\012_africa_world_order_effects.txt, and common\scripted_effects\012_africa_host_transfer_effects.txt. The broader host-transfer delta is outside this weighted audit; its exact before copy remains available in the manifest evidence.

The current decision source SHA-256 remains ae732079d66e081b0b6a13fbbe411b42936722009652639106d42d2b2144bfb9. The Strength constants and AI trigger file still match their before snapshots.

The current parent data-production paths initialize the measurement census at common\scripted_effects\012_africa_world_order_effects.txt:826, remember each world country before participant filtering at line 909, and finish the census at line 917. Named onboarding remembers the country through gods_of_africa_try_register_participant at common\scripted_effects\012_africa_gods_effects.txt:493. Army measurement runs at activation and due owner review at lines 625 and 149. These caller changes are preserved against the original before snapshots.

The consumer patch changes gods_of_africa_refresh_strength in common\scripted_effects\012_africa_gods_effects.txt. The current host-object guard calls gods_of_africa_measure_territorial_control, preserves the existing military/readiness/sustainment and political calculations, then invokes gods_of_africa_apply_strength_input_factors. Weighted scoring, penalties, smoothing, observer updates, and publication run only when gods_of_africa_strength_input_factors_applied is true; the invalid-sample branch sets gods_of_africa_strength_input_publication_blocked and publishes nothing.

The current refresh block is at lines 634–829. Its normalized SHA-256 is 82c8d982e4e5635ec24ce42bacb5240c2c1f54dc1f6eb4748f23aeb9c1fab41a; the before snapshot block at lines 630–817 is bd9f8fe87fe0ab68a737a776c1401fcf445658de2fb6cc10994a5f4c5288f8dc. The decision-root source, AI response constants, and AI trigger thresholds remain unchanged.

The existing outer Strength weights remain 25 military, 20 industry, 20 continent, 15 reach, 10 internal condition, and 10 Chaos. Current military arithmetic begins with division count divided by 20, optionally averages that value with continental-war readiness, clamps it, then applies the existing equipment/fuel sustainment factor with 0.6 equipment share, 0.4 fuel share, 0.4 floor, and 0.6 span. The parent-selected military competition factor and 50/50 political-to-secured-territory blend are now consumed by the refresh, behind the applied-input proof gate. The parent reports the deterministic helper-26 cases passed separately; they were not rerun here, and no numeric AI-weight patch is planned.

The parent’s accepted full-spec factor families are recorded at docs\specs\012_africa_is_one_gods_of_africa_specs\specs\012_gods_of_africa_full_spec.md:145–203. Current cross-file helper dependencies used by decision availability and AI posture are not all pinned by the original eight-file manifest. Baseline-time hashes for those files are recorded in child_evidence\source-identities.json; they are not a frozen historical helper tree.

The decision file contains no direct global.gods_of_africa_strength reference. Its helpers in common\scripted_triggers\012_africa_gods_triggers.txt map Strength below 40 to weak, 40 and above to strong, and 60 and above to dominant. This matches the spec’s working bands: Limited 0–19, Regional 20–39, Continental 40–59, Global 60–79, and Extreme 80–100. Wrath is low below 30 and high at 70 or above.

## Scenario set and completeness

The saved scenario set is docs\plans\012_africa_plans\subagent_handoffs\012_gods_strength_probability_2026-10-09_evidence\scenario-set.json. Its byte SHA-256 is c2c47a87fd7ec27b9a9ee42f362dd77a702f20d1193a9bce4811f85669efd9f5. The service scenarioHash is dd50ca9116e5f58779021027e9b9eda9749b543c76a6454a038db34c96a8edfc.

Each case uses actor GER, host and event target ETH, date 1936.1.1, an active light recognition demand, current participant and authority identities, the same non-war and non-faction profile, factories 120 versus 250, and Chaos zero. The set contains no helper-result booleans and no candidate override field.

| Scenario id | Global Strength | Wrath | Source band |
| --- | ---: | ---: | --- |
| LIMITED_W20_ACTIVE | 10 | 20 | Limited; weak; low Wrath |
| LIMITED_W70_ACTIVE | 10 | 70 | Limited; weak; high Wrath |
| REGIONAL_W20_ACTIVE | 30 | 20 | Regional; weak; low Wrath |
| REGIONAL_W70_ACTIVE | 30 | 70 | Regional; weak; high Wrath |
| CONTINENTAL_W70_ACTIVE | 50 | 70 | Continental; strong; high Wrath |
| DOMINANCE_EDGE_60_W70 | 60 | 70 | Global-band boundary; strong and dominant |
| EXTREME_W70_ACTIVE | 85 | 70 | Extreme; strong and dominant |

For every case, candidatePool is exactly the two audited roots and is complete only for that pair. Other decisions the AI may weigh are absent, so this is not a complete selection race. The fixed scenario facts include demand family, burden, payment capacity, participant and host generations, authority epoch, factories, war state, and Chaos. The cases do not declare a complete GER owned/controlled African-state graph or full native relation graph.

## MCP baseline and after-patch comparison

hoi4.probability_inspect succeeded for adapter decision_ai_will_do and the exact two-root source. It reported candidateCount 2, poolComplete true, requiredInputs empty, and no declared unsupported constructs. An empty requiredInputs list does not establish complete helper inputs.

The inspect JSON artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53c2fef140ee52a915bf69443814f9c2ae48ce4a9795e64899353491f63198df/edd36aa5d3d4e93070498d894229c914bdab98c4a30609cf5511fd44f040ac6d/probability-inspect-cd0846ce49fe.json, SHA-256 53c2fef140ee52a915bf69443814f9c2ae48ce4a9795e64899353491f63198df.

The corrected hoi4.probability_evaluate request returned PROBABILITY_ANALYZED_PARTIAL for seven scenarios and fourteen candidate-case rows. It reported zero eligible rows, fourteen excluded rows, 392 unresolved trace items, and zero candidate-level unresolved records. Its zero-valued matrix cells reflect excluded candidates; they are not valid source weights or a score comparison.

The baseline analysis id is probability-b128e9002ad9782ec8d2e9a3, source revision 99b7ea7e9931bfb7c7596efde3d3d03b2b16dee7f4283205346843e8a4433719, and sourceHash cd0846ce49fe3123c413b17d3ae9bccc92228a7b15eb5992ac6ab24197752d77. The authoritative 21,483,788-byte JSON is retained at hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/577e840cb2f59f2862f0f5fc4857ed51e0d1fff868730b35df6d9d3482d004e2/76c5765ed9831e78f6f41dc7880cdeb7ca53d1db932ba2a6d9bc526f739d53fa/probability-b128e9002ad9782ec8d2e9a3.json, SHA-256 577e840cb2f59f2862f0f5fc4857ed51e0d1fff868730b35df6d9d3482d004e2. The ranking, matrix, and unresolved views are attached to that evaluation; the unresolved SVG reports 392 explicit uncertainties, including undeclared capital_scope and any_of_scopes bindings and identity/array resolution gaps.

The one requested hoi4.probability_compare used the exact seven-case scenarioHash, the pinned before decision source via snapshotPath and expectedSourceHash, and the current decision source as after.path. It returned PROBABILITY_ANALYZED_PARTIAL with comparisonChanges 0, zero eligible rows, fourteen excluded rows, and 392 unresolved traces. The comparison SVG says “0 attributed candidate changes.” This matches the identical before/current decision-root bytes, but excluded rows provide no raw score delta.

The comparison analysis id is probability-8718583f6987112753970804 at source revision 1d00bd71a7d8803240c93e10d7932a23c6ada1d8bb9ece54bcf7f18883f5f090. Its authoritative JSON is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/755ab78a49be852dca6d129c79d88b3845f725b41b4a575586808790528a7bd7/fb48ebe99e79f227a1877b3d64348d8d9481c1c7efec03343ff8f68f97f2732a/probability-8718583f6987112753970804.json, SHA-256 755ab78a49be852dca6d129c79d88b3845f725b41b4a575586808790528a7bd7. Its comparison SVG is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/7dcf3fab2427da8dc29bd36e51abff5dabe758282a7b79a50aea42b13ca87a12/probability-probability-8718583f6987112753970804-comparison.svg.

This comparison tests the decision roots at fixed public Strength values. It does not calculate how the changed refresh arithmetic moves Strength from underlying country inputs. Cross-file helper dependencies are current inputs and are not frozen by the before decision snapshot, so this is not a whole-workspace arithmetic comparison.

A separate probability_render attempted after the data-production caller update and before the consumer patch returned PROBABILITY_ANALYSIS_STALE. It was not repeated. The later probability_compare itself generated comparison, matrix, and unresolved artifacts at its recorded revision.

The first evaluate request was rejected because scenarioSet was supplied as a string instead of the schema-required object. The corrected object evaluation consumed the one permitted corrected attempt. The single requested compare then completed as partial; no other probability analysis or stale-render retry was run.

## Source-derived score traces

The following values are direct arithmetic from the unchanged decision roots and constants, not MCP raw-score results or game observations. Each neutral-profile value assumes no held African core and no other unmodeled relationship modifier. The held-core column is a conditional source branch, not a helper override or a supplied MCP case.

| Scenario id | Comply, no-core profile | Permanent defiance, no-core profile | Comply if GER holds an ETH African core | Permanent defiance if GER holds an ETH African core |
| --- | ---: | ---: | ---: | ---: |
| LIMITED_W20_ACTIVE | 90 | 0 | 18 | 16 |
| LIMITED_W70_ACTIVE | 90 | 12 | 18 | 48 |
| REGIONAL_W20_ACTIVE | 90 | 0 | 18 | 16 |
| REGIONAL_W70_ACTIVE | 90 | 12 | 18 | 48 |
| CONTINENTAL_W70_ACTIVE | 337.5 | 12 | 67.5 | 48 |
| DOMINANCE_EDGE_60_W70 | 337.5 | 3.6 | 67.5 | 14.4 |
| EXTREME_W70_ACTIVE | 337.5 | 3.6 | 67.5 | 14.4 |

For the comply root, the neutral calculation is base 50 × light burden 2 × recognition family 1.5 × weak-Africa 0.6 below Strength 40 or strong-Africa 1.5 at Strength 40 or above. The fear factor 1.5 additionally applies only when Wrath is high and Africa is strong.

For permanent defiance, high Wrath contributes ×3 and an active demand contributes ×2. The dominant-Africa factor ×0.3 begins at Strength 60, the Global band’s lower boundary. Without a defiance motive the source’s zero modifier closes the weight; low Wrath with a light demand does not supply that motive.

A held African core makes the rival trigger true, applies the comply rival factor ×0.2, supplies a defiance reason, and applies the defiance held-core factor ×4. Under high Wrath this yields a conditional within-pair reversal at Limited and Regional Strength: 48 defiance versus 18 compliance. At Continental Strength the same branch remains 48 versus 67.5, and at Global or Extreme Strength it is 14.4 versus 67.5. The MCP could not resolve the core-state scope, so this reversal is a source-derived conditional, not a measured scenario result.

In the no-core high-Wrath branch, compliance exceeds defiance in every supplied band. The relative score ratio increases from 28.125 at Strength 50 to 93.75 at Strength 60 because the current dominant modifier reduces the defiance score at the Global-band boundary. This is score evidence only; it is not a selection probability and does not prove starvation against the full decision pool.

## Findings and recommendations

Both roots have positive finite base values and finite constant multipliers. Compliance has an explicit zero factor when the current demand cannot be paid or the host cannot receive it. Permanent defiance has a zero factor when defiance is invalid or lacks a current motive. The partial MCP analysis did not validate native eligibility.

The direct decision-root comparison attributes zero changes because the roots are byte-identical. The evaluator did not return usable raw scores or ranks because all rows were excluded. The source arithmetic shows a strong compliance tilt in the neutral high-Strength profile and a conditional reversal for a high-Wrath participant holding African core land at Limited or Regional Strength.

No global starvation, exact click probability, or full-pool rank claim is supported. No campaign repetition, timing, or snowball conclusion is supported by this direct decision-score review.

The consumer patch now calls the world-army and territorial measurements and gates weighted Strength publication on the factor helper’s proof flag. Keep the existing 25/20/20/15/10/10 weights and decision-root modifiers unchanged; no numeric AI-weight edit is recommended. The parent reports the deterministic helper-26 cases passed separately, so they were not repeated here.

## Material check limits

The connected tool inventory exposed probability_inspect, probability_evaluate, probability_compare, and probability_render. The baseline inspect succeeded, the baseline evaluate and after compare returned partial analysis, and the stale render result was not retried. This is not a child-tool inventory gap.

The remaining MCP limitation is native country-scope eligibility and score tracing: the adapter did not resolve capital_scope, identity and generation comparisons, participant-array bindings, and any_of_scopes. The source calculations provide conditional score branches without claiming native execution.

The before snapshot freezes the decision root, not the complete helper tree. The comparison therefore cannot establish a historical whole-workspace arithmetic delta. The public Strength values were fixed in the fixture, and the full selection pool was absent.

## Implementation blockers

No implementation blocker remains for the requested read-only before baseline and single after-root comparison. The owner’s consumer patch is present; no numeric AI patch is planned.

No implementation simplification was made by the auditor. The comparison is complete as a bounded decision-root check, not as a campaign-Strength or selection-probability result.

Skills read: chaos-redux-subagents and chaos-redux-decisions-missions. Neither skill was changed.

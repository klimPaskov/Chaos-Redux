# Event 016 Rocketry Native Decision AI Snapshot Comparison

**Disposition:** The bounded source-score audit and parent artifact review are complete.
Wider source-state coverage and balance acceptance remain unresolved because the saved scalar fixtures cannot express several simultaneous states and historical helper branches retain scope.88 warnings.
Normalized selection probabilities are outside this decision adapter's supported model, rather than an omitted metric that this audit could certify.

**Scope:** This read-only pass covers the four named Rocketry native-selection and release decisions in common\decisions\016_mengele_native_prototype_selection_decisions.txt using only the prepared before/after snapshots and the saved 15-case scenario set.

**Changes:** No gameplay source, fixtures, tests, scripts, or model files were changed.
No Git operations that mutate the index or repository were run, and no game was launched.

## Source and fixture identity

The source manifest is docs\testing\event016_native_selection_ai_20261007\source_manifest.json with SHA-256 ab2745b53026fa8764a37de998d9baa96809c87dca7b13c24ecdf0bfa6824b76.

The manifest binds logical source common\decisions\016_mengele_native_prototype_selection_decisions.txt to the parent baseline commit a4b0c089ab8ad406551ec361db5f8d2c02e52b88.

The before snapshot is docs\testing\event016_native_selection_ai_20261007\before_decisions.txt, SHA-256 bbe8c7969a20691e5f5ba6057386732bc55672b5f1a030ec34aba842776c4757.

The after snapshot is docs\testing\event016_native_selection_ai_20261007\after_decisions.txt, SHA-256 6f3daf43c813c05086957225c71d90a7e35ece4808a46c34640bc25e52a3b902.

The immutable scenario fixture is docs\testing\event016_native_selection_ai_20261007\scenarios.json, SHA-256 60d67844f56ddc7dd4812c8cb4a1cd3503b54e9a23b8dc76d6ef457b82912eae, scenario-set ID E016_ROCKET_NATIVE_SCALAR_STATES_20261007, and it contains exactly 15 scenarios.

Shared helpers and constants were analyzed from the current configured workspace, so this is the decision-file delta under the live helper/constant revision captured by each MCP analysis, not a complete historical workspace reconstruction.

## Audited candidates and interpretation

The complete declared candidate pool for this scoped surface is:

- mengele_event016_native_select_flying_bomb
- mengele_event016_native_select_jet_engine
- mengele_event016_native_release_flying_bomb
- mengele_event016_native_release_jet_engine

The pool was explicitly supplied to every probability call.
Inspection reported poolComplete=true, four discovered candidates, no required inputs, and zero unresolved findings for the before snapshot.

The adapter is decision_ai_will_do, with selectionRule=score_only, rawScore=true, and normalizedProbability=false.
It returns willingness scores and ranks, not normalized click or selection probabilities.

The decision wiki describes ai_will_do as a decision MTTH-style weight, while the general AI page describes score races and distinguishes ai_chance probability-proportional sampling.
The decision results below are therefore not probabilities or timing distributions.

The scenario set declares actor MCL, date 1939.1.1, flags, scalar project predicates, one technology prerequisite, and variable.mengele_event016_active_project_stage_entries^3.
There are no candidateOverrides, uncertain distributions, seeds, scheduled state changes, or declared external AI-strategy factors.

The live condition evaluator accepted the fixture's native scalar forms such as is_special_project_completed = sp:sp_air_jet_engine, is_special_project_being_researched = sp:sp_rockets_flying_bomb, none, has_dlc = Gotterdammerung, and has_tech = fighter2.
The parent also supplied a successful single-case snapshot pilot with score 10, available true, and zero unresolved findings.

The scalar adapter cannot represent both Rocketry projects complete, both technology prerequisites, or Gotterdammerung and By Blood Alone simultaneously.
None of those combined states was fabricated or claimed as covered.

The fixture does not declare political_power.
Zero-cost affordability is outside this probability pass, and the parent said a separate companion request will supply political_power=0 without modifying this 15-case file.

The source analyzer evaluates decision available gates but not visible or decision-category gates.
Eligibility in the following table must not be read as full visibility.

## Current score model and shared gates

Before and after, both selection decisions use brilliant_scientist_project_board.ai_high=10, a war modifier brilliant_scientist_project_ai.preferred_factor=2, and the low-factory modifier brilliant_scientist_project_ai.cautious_factor=0.5 when available project factories are at most three.

After the snapshot, each selection decision adds brilliant_scientist_project_board.ai_never=0 when its matching brilliant_scientist_mengele_ai_wants_*_source helper is false.
This zero suppressor is unchanged as a constant.

Before the snapshot, both release decisions use brilliant_scientist_value.zero=0.
After it, both use brilliant_scientist_project_board.ai_high=10 and multiply by ai_never=0 when the matching brilliant_scientist_mengele_ai_should_release_* helper is false.

The selection helpers require a valid provider, completed Rocketry theory, an incomplete prototype stage, an empty Rocketry receipt, and source-specific project or technology eligibility.

The release helpers require the matching native-selection flag, an empty Rocketry receipt, and that the selected native project is no longer being researched.
Release does not require the provider to remain valid.

The receipt gate treats an uninitialized provider receipt as empty or, when initialized, requires variable.mengele_event016_active_project_stage_entries^3 to equal the none stage value.

The low-factory predicate is brilliant_scientist_mengele_rocketry_prototype_low_factory_margin.
The provider and receipt helpers are shown in the source references below.

## After-snapshot results for all 15 scenarios

Every row below is score-only.
The reported rank is a source-local willingness rank among the four supplied candidates, not a normalized probability.

All 15 scenario records retain the same eight unresolved scope.88 analyzer warnings in historical helper branches.
The aggregate evaluate result reports eight unresolved items and zero unresolved candidate eligibility states.

| Scenario ID | Declared distinguishing state | Eligible candidates and after raw score/rank |
| --- | --- | --- |
| flying_bomb_research | Flying Bomb is being researched. Experimental rockets. Peace. Four available project factories. | select_flying_bomb: 10, rank 1. |
| jet_engine_research | Jet engine is being researched. Fighter 2. Peace. Four available project factories. | select_jet_engine: 10, rank 1. |
| sole_flying_bomb_source_researchable | No project active or completed. Experimental rockets makes Flying Bomb the sole researchable source. | select_flying_bomb: 10, rank 1. |
| sole_jet_engine_source_researchable | No project active or completed. Fighter 2 makes the jet engine the sole researchable source. | select_jet_engine: 10, rank 1. |
| held_flying_bomb_jet_complete | Flying Bomb selection is held and the jet engine project is complete. | release_flying_bomb: 10, rank 1. |
| held_jet_engine_flying_bomb_complete | Jet engine selection is held and the Flying Bomb project is complete. | release_jet_engine: 10, rank 1. |
| held_flying_bomb_jet_research | Flying Bomb selection is held while the jet engine project is being researched. | release_flying_bomb: 10, rank 1. |
| held_jet_engine_flying_bomb_research | Jet engine selection is held while the Flying Bomb project is being researched. | release_jet_engine: 10, rank 1. |
| held_flying_bomb_still_researching | The held Flying Bomb project is still being researched. | No candidate is eligible. No top outcome. |
| invalid_provider_held_flying_bomb_jet_complete | Flying Bomb selection is held, jet engine is complete, and the programme is closed. | Analyzer availability admits release_flying_bomb: 10, rank 1. Parent visibility evidence below says the category and decision are hidden. |
| paid_prototype_held_flying_bomb_jet_complete | Flying Bomb selection is held, jet engine is complete, and Rocketry receipt stage ^3 is 2. | No candidate is eligible. No top outcome. |
| held_flying_bomb_already_complete | Flying Bomb selection is held and Flying Bomb is already complete. | select_flying_bomb: 10, rank 1. release_flying_bomb: 0, rank 2. |
| flying_bomb_war_low_factory_margin | War is active and available project factories equal 3. | select_flying_bomb: 10, rank 1, from 10 × 2 × 0.5. |
| flying_bomb_peace_low_factory_margin | Peace and available project factories equal 3. | select_flying_bomb: 5, rank 1, from 10 × 0.5. |
| flying_bomb_war_spare_factory_margin | War is active and available project factories equal 4. | select_flying_bomb: 20, rank 1, from 10 × 2. |

## Before/after comparison

The before/after comparison used the exact same scenario-set ID and hash 4a608751bce9799cf3c21ed030ee12f328479f8711f15b62fed2475b94872b2f, the same four-candidate pool, and the same source selectors pinned to the two fixture hashes.

The compare reports five raw-score changes and no regressions.
Every changed release candidate increases from 0 to 10, has rankDelta=0, and has unresolvedDelta=0.

The five changed rows are held_flying_bomb_jet_complete / release_flying_bomb, held_jet_engine_flying_bomb_complete / release_jet_engine, held_flying_bomb_jet_research / release_flying_bomb, held_jet_engine_flying_bomb_research / release_jet_engine, and invalid_provider_held_flying_bomb_jet_complete / release_flying_bomb.

No selection-candidate score changed in these 15 scenarios.
The new source-wanted suppressors were not active on an eligible selection candidate in the saved cases.

The closed-program release score of 10 is an availability-only analyzer result and is not a gameplay defect: the parent decision inspection found the category and release decision invisible while available=true.

## AI validity, dominance, and remaining behavior

In the declared scalar states, the eligible selection candidate matches the active or sole researchable project, while a held selection receives a release score when the other Rocketry project is active or complete.

The scenario comparison found no rank changes among its five changed candidate rows.
It does not establish a global rank-reversal bound because no threshold sweep was requested.

There is no evidence of all four decisions being simultaneously eligible or of positive score on a source-excluded decision in this fixture.
The invalid_provider_held_flying_bomb_jet_complete row remains visibility-limited as described above.

Starvation, repeated decision execution, cooldown behavior, and exploit or snowball risk cannot be concluded from these single-state native decision scenarios because no cadence or state-transition sequence was declared.

The probability evaluation and comparison are partial because the selection helper expansion retains eight TRIGGER_UNRESOLVED items for numeric scope.88 in the historical German-program branches, including camp_admin_country_mengele_historical_gate and germany_controls_auschwitz_area.
The parent reports these are nonselected branches in the supplied MCL cases.

The parent-owned companion decision_inspect was reported partial and found: held_flying_bomb_jet_complete visible/available true.
invalid_provider_held_flying_bomb_jet_complete category and decision visible false but available true.
And paid_prototype_held_flying_bomb_jet_complete visible false/available false.

No artifact URI or revision for that parent companion was included in the supplied handoff context, so those visibility findings are parent-reported evidence rather than independently traceable MCP artifacts here.

## Recommendations and analysis limits

No gameplay weight or gate fix is recommended by this bounded pass.
Preserve the current centralized base 10, war factor 2, low-factory factor 0.5, and zero suppressor unless a broader campaign scenario produces contrary evidence.

If future coverage of the historical German branch is needed, supply a real scope binding for numeric scope.88 through an authorized scenario or adapter improvement.
Do not replace it with a fabricated flag, candidate override, or scalar proxy in this fixture.

The current result does not establish exact AI selection probability, long-horizon timing, global dominance, starvation, repetition, or whole-campaign balance.

hoi4.probability_sweep was not run because the parent bounded this follow-up to the saved inspect/evaluate/compare cases and explicitly prohibited optional matrix expansion.
Threshold and sensitivity behavior outside the three saved factory/war points remains unresolved.

hoi4.probability_simulate was not run because no uncertain input distributions were declared, and hoi4.probability_sequence was not run because this is a native decision score surface without a complete custom-pool cadence/state-transition manifest.

hoi4.probability_render was called for comparison, ranking, and unresolved views with the exact scenario hash, but returned PROBABILITY_ANALYSIS_STALE: the compare revision was f2b20a14cef407815fcea3befbf694f05abd89d98745afa356778239aa83e213, while the current workspace revision was 0247ef9c0768a54a53bf3922768e6c93d8fb2290c82a15bf32b1fdf6f4151c79.

The probability compare call itself returned ranking, comparison, waterfall, and unresolved SVG/PNG artifacts at the compare revision.
Those URIs are retained below, but the standalone render produced no fresh visual resources.

No threshold sweep, extra scenarios, candidate overrides, source patch, test, script, or gameplay fixture was added.

## MCP evidence

The installed adapter target was Operation Postern 1.19.2.0 checksum d245.
The workspace launcher identified Operation Postern v1.19.2.0.a729 (d245) and the adapter verification status was workspace_verified.

hoi4.probability_inspect returned PROBABILITY_SOURCE_INSPECTED, source revision b3924a3c55f6498542b9c3952387d7dc675be8c340a7f2e98e41431f61e511bf, analyzer source hash 4791d52e7c21e4c2b5f94c882cdb1a8e1ef370e44b351bb4aba46d5a7e0fc5ff, pool complete, and zero unresolved inputs.

Inspect JSON artifact SHA 8144339d67b38ffedd1f9f77fb64c6c732e0b6c94cde962e210e7a2568160363: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8144339d67b38ffedd1f9f77fb64c6c732e0b6c94cde962e210e7a2568160363/422530a9028fd1ed21536c8ebd82c3c8c7ee42fdc52b23e2adb2eefcfdf1fdc4/probability-inspect-4791d52c7e21.json`.

hoi4.probability_evaluate returned PROBABILITY_ANALYZED_PARTIAL, analysis ID probability-ddcc4ac66bec507e7793a82f, source revision ee6cb99e3066473b3e990455dea8bebdbc6307a92e0bbb4b34499ea0813d7667, analyzer source hash fad79a85620599d8e5b89c28c367058d449206ee803a4b7eb4d51dde2b702ce4, 15 scenarios, 60 candidate-scenario rows, 14 eligible rows, 46 excluded rows, eight unresolved items, and zero unresolved candidate-eligibility states.

The evaluate scenario hash is 4a608751bce9799cf3c21ed030ee12f328479f8711f15b62fed2475b94872b2f, and its four-candidate pool hash is a029507adbed32ab0ce22bd58e9dd33b8de02e014e32c2c4c0f000f541b2764a.

Evaluate JSON artifact SHA fdc724afd8fd3608ff3dd54d29db5d32a4f459c577fcb7de7832f8c71543cb13: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdc724afd8fd3608ff3dd54d29db5d32a4f459c577fcb7de7832f8c71543cb13/9a27e23ce54bc946ee9c2f9f2d6a3447bd224d4f60dfb5a5abcea2f5e0fde457/probability-ddcc4ac66bec507e7793a82f.json`.

Evaluate rendered ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b59742bc8272a1666efdb615951e6373ee8787ffe5c089a3453ac3ea2e7178e4/ac30eef403d9ac074a342635afebf70ce581112e4a98a3de2868e1a99c10a58e/probability-probability-ddcc4ac66bec507e7793a82f-ranking.svg`.

Evaluate rendered waterfall SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9b80d760f2647ac58fcd46bb45ce5140ace7bcccb656deed2ef83a2f1bde951/fb27a04077ce47d86a7f3841f8678b970052fe34f8bb238ac3aeabe917d76e9b/probability-probability-ddcc4ac66bec507e7793a82f-waterfall.svg`.

Evaluate rendered unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b79b27812d1a991be86ce0f7a7874ec2c09ad24fe423e72bb5c3eac7e426d05/3dd48f09940fcc55f92d4227932d4ce4439b1dcd77b6a598efddfb2a8ece034d/probability-probability-ddcc4ac66bec507e7793a82f-unresolved.svg`.

hoi4.probability_compare returned PROBABILITY_ANALYZED_PARTIAL, analysis ID probability-cc287668bc01503910b387e4, before analysis ID probability-dd6c663a42385cde95f3cc25, after analysis ID probability-ab6a4ff03cad803f554102de, source revision f2b20a14cef407815fcea3befbf694f05abd89d98745afa356778239aa83e213, the same scenario hash, five score changes, no regressions, and eight unresolved items.

Compare JSON artifact SHA 8676e8d30ea64a01f2ef58c7e41098f6f1ab4c497799b9d8e580a1435469b40c: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8676e8d30ea64a01f2ef58c7e41098f6f1ab4c497799b9d8e580a1435469b40c/7c0ed8f1a90334c8ef85088f9031bcc507f9ba3d0527b05536b16d4af112c227/probability-cc287668bc01503910b387e4.json`.

Compare rendered ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bded45bf1c5b3714ed564bcfb24bb69d7dfd84ca597363d062a409b7df28641f/1d84b3cd7b51f3402a06527d42a91a2d7f53ea401946a1e51ef4e53778729d1b/probability-probability-cc287668bc01503910b387e4-ranking.svg`.

Compare rendered comparison SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07196e4e35f640c6d707a25d90a1f9a6c0ef7f3817edd37fe1f4e26123ccac3f/d846449d92c6ba1140b494a6583c30f6208ed1e058cc16b06d9f88b0eab08878/probability-probability-cc287668bc01503910b387e4-comparison.svg`.

Compare rendered unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b79b27812d1a991be86ce0f7a7874ec2c09ad24fe423e72bb5c3eac7e426d05/b0e6fb40f0805fe735464b871d86267b1d2553bb6b225af65f767ffbe1852c2b/probability-probability-cc287668bc01503910b387e4-unresolved.svg`.

Standalone render stale-result artifact SHA f89831be80232c353db1d35a94a029433e4547521e48436845fb56f682267dbe: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f89831be80232c353db1d35a94a029433e4547521e48436845fb56f682267dbe/88b0461ce1d68a4a17a17d0a16d3b8c6e9c31b0f49e828d2f8789f5f340b874a/probability-cc287668bc01503910b387e4.json`.

The complete inspect, evaluate, and compare JSON artifacts were read through the configured MCP byte-range continuation until each returned range reached its declared total size.
The inspect was 38,329 bytes, evaluate 1,879,534 bytes, and compare 1,893,939 bytes.

## Source and reference citations

docs\testing\event016_native_selection_ai_20261007\before_decisions.txt decision blocks are at lines 56-102, with AI weights at lines 65, 77, 89, and 101.
The after snapshot blocks are at lines 59-105, with AI weights at lines 68, 80, 92, and 104.

Current helper source revisions reported by MCP are common\scripted_triggers\016_mengele_native_selection_decision_triggers.txt SHA 1c64198fdcc8d26f770f18a0d60cfe362a8d1681a17b030e48bc54c2e3d3da67 (AI wants/release predicates at lines 85-135), common\scripted_triggers\016_mengele_native_prototype_triggers.txt SHA c6571fa872dd74baf8d813b54c5fe1fdb122b76d8ae7b35822bd22ebcaf6d7cc (provider/receipt private gates at lines 31-36, selection gates at lines 90-114, and release gates at lines 142-152), common\scripted_triggers\016_mengele_project_stage_triggers.txt SHA 6675660ef5967de9fbf1a729b9e33bcef68fe05bb0542ef1ef8a080644ebf706 (provider validation at lines 16-56), common\scripted_triggers\016_mengele_conventional_stage_decision_triggers.txt SHA 1e361c5f85585c4eb51aa0ea7bb2345cc21287a2ea0c7858ce93263f737b2a38 (empty receipt at lines 51-59), and common\scripted_triggers\016_mengele_remaining_conventional_prototype_decision_triggers.txt SHA d482687f1139800d19c6ae7f6af53113211d74c16f4deb438e817320d7cd76fa (low-factory predicate at lines 69-71).

The current constant source revision is common\script_constants\016_brilliant_scientist_project_constants.txt, SHA a95301ed9cbc7bb8fcb751885165f62ae5aa8c6b315eadb0c5cdaf79350ce131.
The relevant definitions are ai_never at line 73, ai_high at line 76, preferred_factor at line 288, and cautious_factor at line 290.

The numeric scope.88 findings cite common\scripted_triggers\camp_administration_country_triggers.txt SHA a8f05edd52f148b358ea6b1bab88a83935b4984d0542500af6d4b56acb086482, lines 103-107, and common\scripted_triggers\germany_mengele_triggers.txt SHA 1874cb02ef0cb47e588468540c62750575fc8bfbeac01bcb7c6733372a43ebd5, lines 8-10.

Offline wiki reference Decision modding, AI section lines 357-374, revision 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162, states that decision ai_will_do is an MTTH-style weight and describes its base/modifier operations.

Offline wiki reference AI modding, MTTH blocks lines 26-37, revision 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818, explains score-race interpretation and separates it from event-option ai_chance proportional sampling.

Installed game documentation common\decisions\_documentation.md, lines 1-46, revision 5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019, distinguishes visible from available.
This supports the visibility limitation above.

The installed hoi4-agent-tools package is version 3.10.0.
Docs\probability.md SHA a392933e376396fe135e25711f513fe3b0f5f09d03847455c1a95948fed030c8 covers tool roles at lines 3-15, unresolved source conditions at line 24, result-field separation at lines 104-117, frozen snapshot selectors at lines 125-127, and render behavior at lines 133-135.

Relevant schema SHA-256 values are probability-inspect-input.schema.json 790b746f9d19b89464b82c1a836f99eacb64b208cf853896bc65185655b7282b, probability-evaluate-input.schema.json abb93070d30a1f6efe6205ce41d74d20d2e92d225b2ca9947209b0efe8e5ee0f, probability-compare-input.schema.json dc81d2dd55a59082f5a71aa93c7733e3be1dc20206f91de267839a879c0e94b8, probability-scenario-set.schema.json 3fa6aa8842af97358b7d1b98baacf2d850529b82c597c92919cdc30d258c9dd8, probability-render-input.schema.json 33eeb7a27f77a909659c5b88b1274894981702cff742e3f3825f2bc11cf71e8a, and probability-analysis-result.schema.json 9db57ad0375f3352b989fd9c9da96045a4e36202687d3e23bf6c91dd97f2d80a.

The applied repository skills were chaos-redux-subagents, chaos-redux-decisions-missions, chaos-redux-event-planning, and chaos-redux-mtth.
Chaos-redux-events was consulted for Event 016 context, and no skill was changed.


## Parent verification and recovery

The parent could not retrieve the original comparison through its resource reader or registered artifact path.
The auditor recovered the exact already-produced JSON without rerunning, and the parent independently checked the saved byte counts and SHA-256 values.
The recovered files are `docs/testing/event016_native_selection_ai_20261007/compare_analysis.json` and `after_analysis.json`.
The latter's exact artifact SHA-256 ends in `43cb13`, while `b702ce4` is the separate analyzer source-hash suffix.
`comparison_review.json` verifies the identical scenario hash, fifteen case IDs, five raw deltas of ten, unchanged ranks, unchanged unresolved counts, the 20/10/5 war/factory scores and exclusion of all four candidates in the paid case.
The comparison's empty regression list is a bounded analyzer result and does not prove whole-event balance.

The final parent visibility companion is `decision_visibility_evidence.json`, using the saved separate `political_power = 0` cases.
Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b94dc6d3d2af99349c38f729148f4d091aa2cc76512a7031aa4097a7bb1d223e/c5e317ef2758c64f3458671250848c58bfa63e97bb097d2803dfeece5f18ccfa/decision-6dbad1fd40b0ba43273dd5d7.json`.
At source revision fd8d588ddea5565cabbd92f15c8c233360c424b07550607de89313c338c1b2a5, all three actions have cost zero and affordable true.
Valid provider withdrawal is visible and available, the closed provider is invisible despite available true, and the paid case is both invisible and unavailable.
The report remains partial with state-88 warnings, which the parent retains without changing unrelated gameplay or adding a fabricated scope.

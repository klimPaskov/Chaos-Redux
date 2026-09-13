# Event 23 AI/probability audit — current

Disposition: implemented with partial MCP evidence

Overall campaign-balance conclusion: unresolved

Audit date: 2026-09-05

Workspace: mod_chaos_redux_ea3b2d67c2c0

Game version verified by the MCP probability adapter: Operation Postern v1.19.2.0.a729, checksum d245.

This is a read-only audit. No gameplay file, asset file, source weight, prerequisite, route gate, or tuning value was edited by this audit, and the dirty worktree was not reset or reverted.

## Audit basis

The required Chaos Redux subagent, events, MTTH, decisions/missions, and event-planning skills were read before the audit.

The required offline Paradox wiki pages were consulted, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

The relevant vanilla documentation under C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/ was consulted, including script concept, script constants, effects, modifiers, triggers, and dynamic variables documentation.

The mandatory weighted workflow was run through hoi4.probability_inspect, hoi4.probability_evaluate, hoi4.probability_sweep, hoi4.probability_compare, and hoi4.probability_render where the declared scenario contract permitted it.

The mandatory structural Event 23 workflow was run through hoi4.event_inspect and hoi4.event_render.

## Source snapshot and identifiers

The final local source snapshot used for source-only checks was:

- common/decisions/023_sov_nuclear_bombs_decisions.txt, SHA256 DC55183F9E49B849C6A2431BF7646D745B5B12C68B643535F3C55563929CB42A, 104746 bytes.
- common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt, SHA256 D893E91D1C1B43E1E08D47CE73BC58651FF552334924D52FB78D57B922BEF19C, 34894 bytes.
- common/mtth/023_sov_nuclear_bombs_mtth.txt, SHA256 DCB60B1AE6F08C09B0E3D22E9E2442432EB424E3ED2BB103517F0DF3BBD1DE09, 4088 bytes.
- common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt, SHA256 A4010965650E4EE1DB45103707670FFB2FD5478177BEB3DE2CE69319FBDB7387, 124088 bytes.
- events/023_soviet_nukes.txt, SHA256 EDE5FDF481B3C374DBE3200D03ED5278755902DB3B18CBEFD146E6F3E3675C32, 13366 bytes.
- common/script_constants/023_sov_nuclear_bombs_constants.txt, SHA256 649304189AF343D937C9B61EBB62FCA4C80D4C8081A2C8398057F3EFAA8127F1, 11983 bytes.
- docs/specs/023_sov_nuclear_bombs_specs/023_sov_nuclear_bombs_probability_scenarios.md, SHA256 B2DC932928C132FE7F16F78A51F44F4A1B45DCA8FEF34FE73E052CEFC92B9D65, 14946 bytes.

The scripted-effects file changed in the shared worktree while the earlier analyses were running. The refreshed random-list inspection and comparison below use the current A4010965 physical source hash, while older analyses are retained only as historical MCP evidence and are not used to certify the current source.

Audited Event 23 identifiers include chaosx.nr23.1, chaosx.nr23.2, chaosx.nr23.100, chaosx.nr23.101, chaosx.nr23.102, chaosx.nr23.106, chaosx.nr23.110, chaosx.nr23.120, chaosx.nr23.140, chaosx.nr23.150, chaosx.nr23.160, chaosx.nr23.161, chaosx.nr23.162, and chaosx.nr23.170.

The Event 23 random test source block is common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:687.

The Event 23 MTTH entries are common/mtth/023_sov_nuclear_bombs_mtth.txt:sov_nuclear_bombs_evolution_i_interval, common/mtth/023_sov_nuclear_bombs_mtth.txt:sov_nuclear_bombs_evolution_ii_interval, common/mtth/023_sov_nuclear_bombs_mtth.txt:sov_nuclear_bombs_evolution_iii_interval, and common/mtth/023_sov_nuclear_bombs_mtth.txt:sov_nuclear_bombs_evolution_iv_interval.

## Scenario contract

The scenario specification contains 43 named cases. All 43 IDs were represented in every all-scenario MCP request where the surface was evaluated.

The accepted scenarioSet schema was schemaVersion 1.0 with scenarios of the form { id, state: {}, flags: [] }. The source specification is prose-only and does not provide native MCP state maps, owner/controller bindings, wars, event targets, variables, technologies, flags, scheduled state changes, or external-factor distributions. Empty state and flag maps were therefore used to preserve every named scenario ID without inventing unsupported state. This makes scope-dependent eligibility and campaign-level selection conclusions incomplete.

The 43 represented scenario IDs are:

- P23_EVO1_HIDDEN_NORMAL
- P23_EVO1_PUBLIC_ACCELERATED
- P23_EVO1_MORATORIUM_DELAYED
- P23_EVO2_BREAKAWAY_ACCELERATED
- P23_EVO2_NO_TARGET_NORMAL
- P23_EVO3_NO_NUCLEAR_RIVAL_BLOCKED
- P23_EVO3_MAJOR_RIVAL_NORMAL
- P23_EVO3_ENEMY_USE_ACCELERATED
- P23_EVO4_GATE_BLOCKED
- P23_EVO4_COLLAPSE_ACCELERATED
- P23_TEST_PROOF_SECURE
- P23_TEST_CONCEALED_WEAK_COMMAND
- P23_TEST_PUBLIC_PREPARED
- P23_TEST_INVALID_SITE
- P23_TARGET_WARTIME_REAL_DISPUTE
- P23_TARGET_BREAKAWAY_CUSTODY
- P23_TARGET_RANDOM_WEAK_MINOR
- P23_COERCE_ISOLATED_LOSING_MINOR
- P23_COERCE_PROTECTED_STABLE_MINOR
- P23_COERCE_UNTESTED_SECRET
- P23_COERCE_EMPTY_THREATS
- P23_LIMITED_USE_BREAKAWAY_SEVERE
- P23_LIMITED_USE_BREAKAWAY_SETTLEMENT
- P23_LIMITED_USE_MINOR_NO_DISPUTE
- P23_PROFILE_VALID_MILITARY
- P23_PROFILE_RETALIATION_LIMITED
- P23_PROFILE_RETALIATION_COUNTERVALUE
- P23_FIRST_USE_TIER_800_BLOCKED
- P23_FIRST_USE_TIER_1000_STABLE_BLOCKED
- P23_FIRST_USE_TIER_1000_SEVERE_RARE
- P23_FIRST_USE_STANDDOWN_BLOCKED
- P23_FIRST_USE_INVALID_TARGET_BLOCKED
- P23_RETAL_CONFIRMED_USE
- P23_RETAL_FALSE_WARNING
- P23_RETAL_BROKEN_COMMAND
- P23_STANDDOWN_PRE_DETONATION
- P23_STANDDOWN_AFTER_LIMITED_EXCHANGE
- P23_STANDDOWN_AFTER_COUNTERVALUE
- P23_COLLAPSE_RECALL_SECURE_ROUTE
- P23_COLLAPSE_NEGOTIATE_STABLE_BREAKAWAY
- P23_COLLAPSE_RAID_IMMINENT_OPERATIONALIZATION
- P23_COLLAPSE_TINY_UNSTABLE_BREAKAWAY
- P23_COLLAPSE_OPERATIONAL_SUCCESS

The exact 12-candidate target pool supplied to the target-aware mission requests was:

1. sov_nuclear_bombs_operational_command
2. sov_nuclear_bombs_collapse_command
3. sov_nuclear_bombs_harden_storage_site
4. sov_nuclear_bombs_disperse_reserve_package
5. sov_nuclear_bombs_expand_fissile_production
6. sov_nuclear_bombs_survey_remote_test_state
7. sov_nuclear_bombs_select_coercion_target
8. sov_nuclear_bombs_redirect_strike_state
9. sov_nuclear_bombs_select_retaliation_target
10. sov_nuclear_bombs_select_disputed_depot
11. sov_nuclear_bombs_select_dismantlement_site
12. sov_nuclear_bombs_breakaway_request_return

The complete random-list pool was common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:687.entry.1, common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:687.entry.2, and common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:687.entry.3.

The doctrine event-option pool was chaosx.nr23.2.party, chaosx.nr23.2.military, chaosx.nr23.2.scientific_safety, and chaosx.nr23.2.dispersed_commands.

The coercion response event-option pool was chaosx.nr23.120.a, chaosx.nr23.120.b, chaosx.nr23.120.c, chaosx.nr23.120.refuse, chaosx.nr23.120.e, and chaosx.nr23.120.f.

The remaining eleven event options are singleton report-event choices with base ai_chance 100: chaosx.nr23.100.a, chaosx.nr23.101.a, chaosx.nr23.102.a, chaosx.nr23.106.a, chaosx.nr23.110.a, chaosx.nr23.140.a, chaosx.nr23.150.a, chaosx.nr23.160.a, chaosx.nr23.161.a, chaosx.nr23.162.a, and chaosx.nr23.170.a.

Candidate-pool and external-factor completeness:

- The random-list pool is complete, has no eligibility predicates, and has no undeclared external factor in the MCP request.
- The full mission request supplied all 80 candidates exposed by the refreshed mission inspector, but the scenario state and external-factor bindings are incomplete and the adapter is score-only.
- The 12-candidate target request is complete only as the requested target subset, not as a normalized mission selection pool, and nested target scopes remain unresolved.
- The four-option doctrine pool and six-option coercion pool are complete within their respective event-option races, but the full 21-option Event 23 source contains multiple categorical pools and cannot be treated as one normalized race.
- The eleven singleton report choices are complete one-candidate pools but provide no meaningful selection race.
- No simulation distribution, seed, sample count, cadence declaration, cooldown, recovery rule, cap, removal, reset, scheduled state change, or terminal-state manifest was declared.

## Probability inspection artifacts

The mandated first inspection was decision_ai_will_do against common/decisions/023_sov_nuclear_bombs_decisions.txt.

- Status ok, code PROBABILITY_SOURCE_DISCOVERED.
- Source revision 9770f43b72318eddea772211049896b01ee5b8741aefe72e7804d82b477ee137.
- MCP source hash 67372c687843c362a958ce2f836556cc1f87713136413b776a3506620c5a015e.
- The decision adapter found zero indexed candidates and 80 available candidates, suggested mission_ai_will_do, requiredInputs 0, and unresolved 0.
- Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/863fc0df9f39c81fc79ee652d4a64b5ecbacbaca874060a063b993c719193947/d29ad6385ecc2f6c02a2cd43eeb0ef2962736a4fdc04ba7727ba8a69ee95deac/probability-inspect-67372c687843.json

The exposed mission_ai_will_do inspection was then run against the same current decision source.

- Status ok, code PROBABILITY_SOURCE_INSPECTED.
- Source revision 21d94843b538e8bf82a1ab873eea446acba86b578e142298bbb5d004f1fc9bca.
- MCP source hash 4a99c9ab3acf08d12d39a8f511ccd31b483d59aac76377775162c85bc99696af.
- The mission adapter found 80 candidates, 0 currently resolved available candidates under the empty fixtures, requiredInputs 16, unresolved 0, and poolComplete false.
- Capabilities are eligibility true, rawScore true, normalizedProbability false, sequence false, and timeDistribution false.
- Selection rule is score_only, and the adapter limitation is that mission scores are not normalized without a documented complete selection rule.
- Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a482a7ffa53b1b13bdb1b6772226438eead6d551529a6b08ee211f458ea9ff1e/e7245abfd4c1b40f3fe44c26a865f42a64f7a279b3f022915140d60c2948b386/probability-inspect-4a99c9ab3acf.json

The event_option_ai_chance inspection was run against events/023_soviet_nukes.txt.

- Status ok, code PROBABILITY_SOURCE_INSPECTED.
- Source revision 002cd336c08e2ba9b1fcb022485fc804192df998add0a21a338927913d95ad30.
- MCP source hash a3644234353bdc6c0280e480c147079d2cc0a0776946870eee6c9edd08472dae.
- The adapter found 21 candidates, poolComplete false, requiredInputs 8, and unresolved 1.
- Capabilities are eligibility true, rawScore true, normalizedProbability true, sequence false, and timeDistribution false.
- Selection rule is proportional_categorical, and completePoolRequired is true.
- The unsupported construct is MULTIPLE_CATEGORICAL_POOLS.
- Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b40c6efb0853cddb4583b9bb5059df33c10ec42e7bff498655066646f9c2a0db/1c3e769a4043b496c152d2723c01036431a1203647482147cf3476ed9358f470/probability-inspect-a3644234353b.json

The random_list inspection was refreshed after the shared worktree changed.

- Status ok, code PROBABILITY_SOURCE_INSPECTED.
- Source revision 25fa4c398fa3dde33759f143b3beface1549be5abdc84df7f5bbaeb486918154.
- MCP source hash f61e7be135de8c5d96456c75ce5a1ddf7c93eec12521d12039ae6864babcc767.
- The inspection provenance records current physical source hash a4010965650e4ee1db45103707670ffb2fd5478177beb3de2ce69319fbdb7387.
- The adapter found all 3 entries, poolComplete true, requiredInputs 0, and unresolved 0.
- Capabilities are eligibility true, rawScore true, normalizedProbability true, sequence false, and timeDistribution false.
- Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/401b90dd16fad01724fece96d1e5c24bc5ff0a7e06e23b3f7dfbe3db999fb487/428a749803facd904188535c2d467d5145775a09e9170c2bcf18f18ea2a74e80/probability-inspect-f61e7be135de.json

The event_mean_time_to_happen inspection was run against the reusable Event 23 MTTH source.

- Status ok, code PROBABILITY_SOURCE_DISCOVERED.
- Source revision 1d3eb50c3b127d03cf02929ec89da17b33e8662ed591d4e8cc00f6a3d9f21399.
- MCP source hash 89b364cff8d70ba8114832f89e206c5a9f69ec8c28635880207ea785515f596c.
- Discovery reason is no_weighted_surfaces, with candidates 0, available 0, and unresolved 0.
- Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91603fac6047e342e379ed71352e195f7c29d574037f149c9cf92871f3e0dedf/88fffeb9d4a8477d8b5ca274ef4a11a8edc5037e0f825a2b80233e929ad59372/probability-inspect-89b364cff8d7.json

## Probability evaluation and comparison artifacts

### Full mission score surface

The full mission evaluation used all 43 named scenarios and the complete 80-candidate mission pool.

- Status ok, code PROBABILITY_ANALYZED_PARTIAL.
- Analysis id probability-616b30ef19c2a1e81af47bee.
- Source revision 21d94843b538e8bf82a1ab873eea446acba86b578e142298bbb5d004f1fc9bca.
- Source hash 4a99c9ab3acf08d12d39a8f511ccd31b483d59aac76377775162c85bc99696af.
- Scenario hash c3332756197e52726d051499097743d394721a0699a6080d1d9b46056059cd63.
- The evaluation contains 43 scenarios and 3440 candidate rows, with 253 unresolved items, 73 diagnostics, and 6 visual resources.
- The result is score-only and partial. It does not provide normalized mission selection probabilities, valid campaign ranks, or target dominance conclusions.
- JSON artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ab106f0ac4aa3f983998ff943a912eb1ab90129635d7597beb87823acabe5983/bada454a49621bf39663886af57c72d675fb3c0c4b414dd38f44edf06be7969c/probability-616b30ef19c2a1e81af47bee.json
- Ranking SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e583d1032aa536e89bc1f7ee0b75ce5cdef7fe1904f8d977aa64f7e069fae276/25376d5ab3524b68ee03cf2eb8b3a1b5ec59b114757d22a9855ef3ff37f3bb88/probability-probability-616b30ef19c2a1e81af47bee-ranking.svg
- Ranking PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ebc48673efdd36ad0e681fe0754865a7bb379d8a6b6ddb8d4fcf29c29365c8b4/a265f9bd35ba33bf293906fb2e58203b03b0cb8aa6cc39c09896a98b82d499b9/probability-probability-616b30ef19c2a1e81af47bee-ranking.png
- Matrix SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ec9852625836e9cf0d689a1b5661dbc54a74150a16cc64046fdeae7ba9e6a52/54df93f392c3f29759bcd5c486aa7850bac1dff355517d5cad7e23eb8d52dc3b/probability-probability-616b30ef19c2a1e81af47bee-matrix.svg
- Matrix PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d25183812977b463e3639cd664f4157de8c633119bb8863eb95a5a0872b0752/c9761ecf9d2c9fe4d88738c68499f76318e3f87722e69d9807b3b95f63041efe/probability-probability-616b30ef19c2a1e81af47bee-matrix.png
- Unresolved SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/215565bde9531e9995e34091b041b0bafa08c174c4a2fc4477ba30bf258f1b34/aa10915a07a12f2a66d96afb04e2771fc6a913cc2af06bfc6fef719325858666/probability-probability-616b30ef19c2a1e81af47bee-unresolved.svg
- Unresolved PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cffc4701240addd06e76c3a94d9243656b608afd3266fe69a82cbc3baffccf4d/bc25c35743838706a9d51d81e6d98b96ae5d9e858a67bb1bd44cc5ebaf369f47/probability-probability-616b30ef19c2a1e81af47bee-unresolved.png

### Target-aware mission subset

The target-aware evaluation used the exact 12-candidate target pool and the three target scenarios P23_TARGET_WARTIME_REAL_DISPUTE, P23_TARGET_BREAKAWAY_CUSTODY, and P23_TARGET_RANDOM_WEAK_MINOR.

- Evaluation status ok, code PROBABILITY_ANALYZED_PARTIAL.
- Evaluation analysis id probability-d21b64c58d7835ea6b8b8941.
- Evaluation source revision 21d94843b538e8bf82a1ab873eea446acba86b578e142298bbb5d004f1fc9bca.
- Evaluation source hash 4a99c9ab3acf08d12d39a8f511ccd31b483d59aac76377775162c85bc99696af.
- Scenario hash 55cf187473ac93c18f02985111251215db6f0af32b6baf8493bf9e5ad5f594d8.
- The evaluation contains 3 scenarios and 36 candidate rows, with 32 unresolved items and 2 diagnostics.
- Diagnostics show the reactor-entitlement factor 1.80 and remote-test survey factor 1.40 inactive under the empty fixtures. These are fixture diagnostics, not campaign conclusions.
- Evaluation JSON artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57183c7524db1c939b782a37db6c7ac05b4d4a1cb8f117beda14a8c7725fbc22/90a8f437e159df84721f31030c252f22fcce7bdba903a235174e414bf8494e1e/probability-d21b64c58d7835ea6b8b8941.json

The same-scenario target comparison used the same three IDs, exact 12-candidate pool, and scenario hash 55cf187473ac93c18f02985111251215db6f0af32b6baf8493bf9e5ad5f594d8.

- Status ok, code PROBABILITY_ANALYZED_PARTIAL.
- Comparison analysis id probability-071a46e9ee812baf5696daa2.
- Comparison source revision f12529c9f00c4e89628ac79128922fc240001964e7799aa38fad44f971e12708.
- Comparison source hash 4a99c9ab3acf08d12d39a8f511ccd31b483d59aac76377775162c85bc99696af.
- The comparison contains 3 scenarios and 36 candidate rows, with 32 unresolved items, 2 diagnostics, comparisonChanges 0, and 6 visual resources.
- comparisonChanges 0 is a same-source capability control, not a before/after balance delta.
- Rendered comparison JSON URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/705c2bdbfb45dfbd33e74fac8d6c379ab4eb3055cc4a0441ed34de5c4f629697/fecc7f540ad8e4a3e7c6210a7d85aaaf3fc9078d06829751d50ceae9afdeb48c/probability-071a46e9ee812baf5696daa2.json
- Ranking SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f6237867f572bd7c2faf4312e93112941f41d0f95ce623269c078504f68c78dc/db654126d0c320955608371f11c521856fb95959d047e065e1e8e6beb9a1f1e0/probability-probability-071a46e9ee812baf5696daa2-ranking.svg
- Ranking PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/473bdcde8db2c57c3abebb26c347671691bed2ca28a06799bfeba29f8fc86a93/229d917aa37a39c04087d59b30fd6107609f0f3724b6b80bd1944b88b6a9a4bb/probability-probability-071a46e9ee812baf5696daa2-ranking.png
- Matrix SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84a22f7caaa25fdc21f46113e5b93b273f7611d8eff605205e536e5986208676/ff70fbf64f1551c752dbdd7068dd20b247eff8863bf9c0c06ac1a9adbfd968a9/probability-probability-071a46e9ee812baf5696daa2-matrix.svg
- Matrix PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/beaa8527bba3fb53fecf19ad8e22478bb529d3da4a6975d3ab8bbb7ad7019827/3630f8d7ffaef8fe94bd2c1be917e91f6fb1651685d76103d15c30b3f60f9803/probability-probability-071a46e9ee812baf5696daa2-matrix.png
- Unresolved SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e445b7ff00b83d1287b4b7bcd4cb5f07141f2d36d93c4f2acdae55c7fd7fa39d/963101b33ab18824ec1bd905b1856b669362f3c906852e64630e46036741200e/probability-probability-071a46e9ee812baf5696daa2-unresolved.svg
- Unresolved PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ec177379f324fcb50fb8b3cd14c3f51a58311974cee84c5783af1aedf4d08cc/669010602e5db0f5426f98e92ea805cd03064392c2fdafbc34d74ddb67035ecf/probability-probability-071a46e9ee812baf5696daa2-unresolved.png

The initial target render request for probability-d21b64c58d7835ea6b8b8941 returned PROBABILITY_ANALYSIS_STALE with no artifact because the workspace revision had advanced. The later probability-071a46e9ee812baf5696daa2 render is the current target comparison render.

### Doctrine event-option race

The doctrine event-option evaluation used all 43 named scenarios and the complete four-option pool.

- Status ok, code PROBABILITY_ANALYZED_PARTIAL.
- Analysis id probability-b07a32239200698107f716aa.
- Source revision bf36c475638b30db327f9f18381ce9b450e79870c387b8f651a84b34eb5cb999.
- Source hash a3644234353bdc6c0280e480c147079d2cc0a0776946870eee6c9edd08472dae.
- Scenario hash 9bc9b31ac98ef15f00a72e55215809b34bb7f56bd01619b13f51334bce43661d.
- The evaluation contains 43 scenarios and 172 candidate rows, with 4 unresolved items, 1 diagnostic, and 6 visual resources.
- The one diagnostic is the source factor 1.40 for scientific_safety being inactive in all empty fixtures.
- Evaluation JSON artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae8426fcbde0d233e285ab0c93885a8dabdc2a2c47871310e406a34a792dd915/2d31db4b4ef8b6633771d3f637ef8479de8efd62a46ebcb4b389436e8a2e1fb2/probability-b07a32239200698107f716aa.json
- Ranking SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32f6735c5df379fdfcd05fbcf3c05084d8d013410c48d33e33e730adc08b8c01/d61e101c64895794e1c7c57eba8e3a8fa6538afa4a50bd251847ee7e42c75b94/probability-probability-b07a32239200698107f716aa-ranking.svg
- Ranking PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f70b3f216456636ea3efa52f8656fcc10d05fed7f014ec037acc71054b60477c/e0d06428c13fbb0550d9af949117472841edcc6b8c94613056ac1599004bd57b/probability-probability-b07a32239200698107f716aa-ranking.png
- Matrix SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06646367bcca8d99c7f41aa07c429cf47903e2e2d7ae0e231cc982b3e1858d17/52fa789b2322ec5a790b0ebec93ce075d73538dd145aa2bc8365f250fc731a24/probability-probability-b07a32239200698107f716aa-matrix.svg
- Matrix PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/118bd78cf432216fe73ad18170b386b8d51895cfed9234a2edb51e942879b569/251d67f7d9b72146816cee5b35faa6b6d954a4fc9461788c1634863a323fd4a7/probability-probability-b07a32239200698107f716aa-matrix.png
- Unresolved SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aecc785a69f86b0866200b6854aa7e2f195b89289ba59fd4d63f8c7c8d6d0283/4496ddd522faf0ad274faeb2db215149d99db9f0e87a66b45ab7adba195d5af0/probability-probability-b07a32239200698107f716aa-unresolved.svg
- Unresolved PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6c226368ada42b2d63a00038d2e42a170af58f01db8ec1415cd3fff15512063/beba4d52b9e5c36c609048b2d230fbc69d667efc83d5c14df18c2980c3d4580a/probability-probability-b07a32239200698107f716aa-unresolved.png

The same-scenario doctrine comparison used the same four candidates and scenario hash.

- Status ok, code PROBABILITY_ANALYZED_PARTIAL.
- Comparison analysis id probability-195e9f7dde78ee9d3e7f1a3e.
- Source revision bf36c475638b30db327f9f18381ce9b450e79870c387b8f651a84b34eb5cb999.
- Source hash a3644234353bdc6c0280e480c147079d2cc0a0776946870eee6c9edd08472dae.
- The comparison contains 43 scenarios and 172 candidate rows, with 4 unresolved items, 1 diagnostic, comparisonChanges 0, and 6 visual resources.
- JSON artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4b81d4073a482b7e6427613c084a5651566a47d007953387c88af52ad42a5d1/5ebebcf27334cdcf13d6f19569aa2e8bb1579858f18d7408b830d213ad2dedc9/probability-195e9f7dde78ee9d3e7f1a3e.json
- Ranking SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d30dda745613b55f1e9a8f5380fff164c5ab38bdb8dc48754c164af1a7c0293/beaf3d3c5dfdc4a30d16795af36a236bee5380028134f5697ecf0157c1f9e540/probability-probability-195e9f7dde78ee9d3e7f1a3e-ranking.svg
- Ranking PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c375539e120c10cc0e68c8e4cb0abb02f7fa5a3cffd19074d2214f19c8e71264/030ca84cc008080ab9b0a7b339a8afa0ffe6017e576242d3f3c460f4a63af25c/probability-probability-195e9f7dde78ee9d3e7f1a3e-ranking.png
- Matrix SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06646367bcca8d99c7f41aa07c429cf47903e2e2d7ae0e231cc982b3e1858d17/bb78e45d72a962f8d5984516893c80b14687ffdab19e6e2b3b3e7abb4f8542c7/probability-probability-195e9f7dde78ee9d3e7f1a3e-matrix.svg
- Matrix PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/118bd78cf432216fe73ad18170b386b8d51895cfed9234a2edb51e942879b569/43aee88566d809c7dd8f39a76d7adf693d6e52b7f40ced50175f32c1377e3d28/probability-probability-195e9f7dde78ee9d3e7f1a3e-matrix.png
- Unresolved SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aecc785a69f86b0866200b6854aa7e2f195b89289ba59fd4d63f8c7c8d6d0283/3d38b72f404fdc099d8638977b2121343df0d5ff4189a967b389376f78914ff6/probability-probability-195e9f7dde78ee9d3e7f1a3e-unresolved.svg
- Unresolved PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6c226368ada42b2d63a00038d2e42a170af58f01db8ec1415cd3fff15512063/502c2b1e4394654543b226f3223999bedd178baada4ae8cada283587782d9ada/probability-probability-195e9f7dde78ee9d3e7f1a3e-unresolved.png

### Coercion response event-option race

The coercion response evaluation used all 43 named scenarios and the corrected six-option pool, including chaosx.nr23.120.refuse. The earlier mistaken .120.d identifier was discarded because it is the description key, not an option identifier.

- Status ok, code PROBABILITY_ANALYZED_PARTIAL.
- Analysis id probability-1726ecb0463855e7b0f30a0b.
- Source revision d916a85abac834ad7d07b2b641f5af86147b2ba3f5420dbac3b7183963b76246.
- Source hash a3644234353bdc6c0280e480c147079d2cc0a0776946870eee6c9edd08472dae.
- Scenario hash 83daa1328cced71e8eab0eb33692674a59d1fa817ffc3cb12390ddabf97abd67.
- The evaluation contains 43 scenarios and 258 candidate rows, with 33 unresolved items, 51 diagnostics, and 6 visual resources.
- The adapter reported EVENT_OPTION_FALLBACK_NOT_PROVEN. The empty fixtures also caused dominant-outcome warnings that are not campaign evidence.
- Evaluation JSON artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/168ad6a03ae2f92d9a726fadb99d1025e227dfa5ec3f01462441b631b621dbcf/cc1b90d3d6cda0934cde5cf87dbba4297f8ac36cc2d4bbad0e7b5d355d1982a2/probability-1726ecb0463855e7b0f30a0b.json
- Ranking SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c0c14d7781821107dc97bf8243affb4f7d4d78d6488b5b0e76fb5937fa0f3e6/61301ce37c063492d306c4b48e2cf8e9aa447ba13d72b3a2ba95756f9a3f73b1/probability-probability-1726ecb0463855e7b0f30a0b-ranking.svg
- Ranking PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84186fabf959c4c77ec42b8c7f87886a544e08eb9b892e08299cec604ff6643c/070e6b528c4becfce3d0a3b86e1088436037fa3144aaecaa167af9969f3922eb/probability-probability-1726ecb0463855e7b0f30a0b-ranking.png
- Matrix SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba8438f6171ae06ffbd12fd990ee5878a4678410c454322293235864fb56dcd5/6a43219b7f1f05012edb60d8625b98529a338ab39f75d48fd65261517d6535eb/probability-probability-1726ecb0463855e7b0f30a0b-matrix.svg
- Matrix PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c77f068f07877bc15c72f3f5999461ce60252b27ee3c4f00afa82fac2cdaa263/cfba280525e514594f515a1caa8a924b4809b887bf4f81e1bbfc9c9512dc721b/probability-probability-1726ecb0463855e7b0f30a0b-matrix.png
- Unresolved SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/add4491edfe1ab803237226f587f18ced2c89c770be5e9d8cb56be2edc3f4a19/b5f696eb7c01b0d054bf2e44523fa727a008a76b66faeb755fc8dde1332049bd/probability-probability-1726ecb0463855e7b0f30a0b-unresolved.svg
- Unresolved PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57dd46b9910c2da350b0b7a0539b112607ff5496a2e5485ffb0a458b540c9720/da8e1aa3e0440d5b047894a8b4a11d38ff3774f6683fc960da545c8a6fe7d2ab/probability-probability-1726ecb0463855e7b0f30a0b-unresolved.png

The same-scenario coercion comparison used the same six candidates and scenario hash.

- Status ok, code PROBABILITY_ANALYZED_PARTIAL.
- Comparison analysis id probability-c55ad29319bbe7473e0df03d.
- Source revision d916a85abac834ad7d07b2b641f5af86147b2ba3f5420dbac3b7183963b76246.
- Source hash a3644234353bdc6c0280e480c147079d2cc0a0776946870eee6c9edd08472dae.
- The comparison contains 43 scenarios and 258 candidate rows, with 33 unresolved items, 51 diagnostics, comparisonChanges 0, and 6 visual resources.
- JSON artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/307416430c81568936b781706e9b3128fe502418234c4ac708bbea78badb7cc0/8d8974ca9b6c49761552db008094717f9ecb52febd247786c674516b941b74d4/probability-c55ad29319bbe7473e0df03d.json
- Rendered JSON URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47f337db6a897ff395a47518e471dd89cb2e5e744bc9ac37dcbfb7f3db96b405/6cfd74be8b22925b4b9a450441d43012eb170293938320f4b1668af8eb26974e/probability-c55ad29319bbe7473e0df03d.json
- Ranking SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/847284777301ceee1ee9103e173ae11fe77fcf4e8a729f03044f5873a584db22/92c2ed9d4238ec33144b31abdf3ad2dc069fcf0b5fe267ef9d24f69ad3cdc1b8/probability-probability-c55ad29319bbe7473e0df03d-ranking.svg
- Ranking PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb6874044b97f1bd88a7d1a10372d7fd5ceb58e80a5e663231f2ba7bbe734dbb/39c1101041340c4202ea08a4a4e60f27f8b5571d3ab36e83d72441bf206df65f/probability-probability-c55ad29319bbe7473e0df03d-ranking.png
- Matrix SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba8438f6171ae06ffbd12fd990ee5878a4678410c454322293235864fb56dcd5/64afc60241be83f3707a519c42fc7de76535548077fdf41bd7c3934bfa1d47e6/probability-probability-c55ad29319bbe7473e0df03d-matrix.svg
- Matrix PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c77f068f07877bc15c72f3f5999461ce60252b27ee3c4f00afa82fac2cdaa263/8e4925da3c0995c4bdc6a93b55ddfec2f6e54ac2147bb2277bb84a424b7b1db2/probability-probability-c55ad29319bbe7473e0df03d-matrix.png
- Unresolved SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/add4491edfe1ab803237226f587f18ced2c89c770be5e9d8cb56be2edc3f4a19/58c0e000d14ac0432e149bfcfd80260a65ba641333ab27ef2930556e21f2a441/probability-probability-c55ad29319bbe7473e0df03d-unresolved.svg
- Unresolved PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/57dd46b9910c2da350b0b7a0539b112607ff5496a2e5485ffb0a458b540c9720/8cea37a7250a6b915c988e15bf37f14ba9d32a26d3bffb58606f602e81288ef2/probability-probability-c55ad29319bbe7473e0df03d-unresolved.png

### Current random test-result pool

The refreshed current evaluation used all 43 named scenarios and the exact three-entry pool from source block :687.

- Status ok, code PROBABILITY_ANALYZED.
- Analysis id probability-6c79b8b6b092d67956f9446b.
- Source revision 25fa4c398fa3dde33759f143b3beface1549be5abdc84df7f5bbaeb486918154.
- Source hash f61e7be135de8c5d96456c75ce5a1ddf7c93eec12521d12039ae6864babcc767.
- Scenario hash 9000e0e234ddba2b8bfb95879721262b22e68f873b54a05563e46d0946f48cc7.
- The evaluation contains 43 scenarios and 129 candidate rows, with unresolved 0 and diagnostics 0.
- MCP proves the conditional result when the enclosing random_list executes: entry 1 success has raw value 70 and exact conditional probability 0.7, entry 2 failure has raw value 20 and exact conditional probability 0.2, and entry 3 accident has raw value 10 and exact conditional probability 0.1.
- This is conditional on reaching the random_list after the accepted test action. It is not the overall probability of a test, preparation, mission, or campaign outcome.
- Evaluation JSON artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dc56c76aa80054f0428d0c71b07aae2a9e68a665d5d8ac6cccbfdeda1b9f37fc/591a0973bd009fe25b90bbf0daac27470f788fd72ed983765dd39c292291a6de/probability-6c79b8b6b092d67956f9446b.json
- Ranking SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11e3abab7d2d97f0a57c23432a1a496ae703291856de606f93a138184ad54f02/c078bf42ca4f647ae6180b7b969c1356d039fce8d59975d36973943b28946c9c/probability-probability-6c79b8b6b092d67956f9446b-ranking.svg
- Ranking PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ef5e5e5b3d57567a801e9fe982b5de1c12ef645515d950ec0f7808bfae88ef8/a091fc8cf7ab53f94d28c83422122916e61dd2b10dd777983b2706fa65e0992d/probability-probability-6c79b8b6b092d67956f9446b-ranking.png
- Matrix SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/984555be694702e2b82f619db22e5e8288a7e5e3f034b4f502b7542dafc6005b/64970f74fb0de61a923dfdda22fdca82837580ee3aab0dc82f52f28e0d24844a/probability-probability-6c79b8b6b092d67956f9446b-matrix.svg
- Matrix PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16118c08b2624450b026286749bf4e57f7e2f6c74c3cd62e0e69864f81b074a7/af86adc8b516e2c050b00648a6a31d40bfa6ee09f2b77d7416cfcd0b1dd84821/probability-probability-6c79b8b6b092d67956f9446b-matrix.png
- Unresolved SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/8dfda07aa47e4b5d6756432eb13b00b6ced9cf9fc9fa8ec237a518dcc9abe2ca/probability-probability-6c79b8b6b092d67956f9446b-unresolved.svg
- Unresolved PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/9634d323f4c4ee12f6eacd3cbb7eb44cf323748851a7864a9c7c114974073f76/probability-probability-6c79b8b6b092d67956f9446b-unresolved.png

The same-scenario current random comparison reused all 43 IDs, the exact three-entry pool, and scenario hash 9000e0e234ddba2b8bfb95879721262b22e68f873b54a05563e46d0946f48cc7.

- Status ok, code PROBABILITY_ANALYZED.
- Comparison analysis id probability-4e9b653988a13f7218d41731.
- Source revision 25fa4c398fa3dde33759f143b3beface1549be5abdc84df7f5bbaeb486918154.
- Source hash f61e7be135de8c5d96456c75ce5a1ddf7c93eec12521d12039ae6864babcc767.
- The comparison contains 43 scenarios and 129 candidate rows, with unresolved 0, diagnostics 0, comparisonChanges 0, and 8 visual resources.
- comparisonChanges 0 is a same-source control and not an owner-patch balance delta.
- Comparison JSON artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/271ccc77245f895919610a204c27f64aa56a55f7f6c2ef817838fff979782de9/6dcada97477cf5cdc0482e74418b96083c22e2bddc5ded6e56e980efa23d815d/probability-4e9b653988a13f7218d41731.json
- Ranking SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b61d4c8e515abcba367ac4971e817dbc9cde0fb7beaff3a3d1b6d0b294a580ad/d63cb6c6278325b309589e64d3b7dd46cffd8d7b94c5dd4bc169bc2aae3bff58/probability-probability-4e9b653988a13f7218d41731-ranking.svg
- Ranking PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7af65c30b5c59c7e608cebf24a3ae3ad594ec7baa5e093f3a8156dfb4e3fd9b7/a85e4ce817dd9862a2fcf145ec70a618ead86a562383a06161e1c8906166451d/probability-probability-4e9b653988a13f7218d41731-ranking.png
- Matrix SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/984555be694702e2b82f619db22e5e8288a7e5e3f034b4f502b7542dafc6005b/80010d71fefcdbaebedbef0926ea9f44b7ac38f645790ae89be0f6ccf1f10106/probability-probability-4e9b653988a13f7218d41731-matrix.svg
- Matrix PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16118c08b2624450b026286749bf4e57f7e2f6c74c3cd62e0e69864f81b074a7/f4e40c1f4f878b4926e45ae52ebd6b19a55dc21b3676fd57404fb8708a9b147e/probability-probability-4e9b653988a13f7218d41731-matrix.png
- Comparison SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/d19b16596ff9d05cb8787e0b7004e5d71c00aaf24620bfb9447b184bafbd0e30/probability-probability-4e9b653988a13f7218d41731-comparison.svg
- Comparison PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1fd8e11d21dd2414c85f7412d454fa53b5b857ed9fb0953caa20f6277f498f/5846c632a39b8259ac9e690845ff934d5442d0b370f1f59f4b9e7962ba96d3d0/probability-probability-4e9b653988a13f7218d41731-comparison.png
- Unresolved SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/1b517f41a554290eedfd8cd0098d9bea8f7f7d9033ef277b74b4cd0bbe9dba9e/probability-probability-4e9b653988a13f7218d41731-unresolved.svg
- Unresolved PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/741e9e9423642ce8eb7607dbaccbbceeec8fa1c4ab1c760262892070e72be88c/dac11a47fdc9d0f7f1beb7c357e3ef5235be50f0b2e50d334f2ab7847973f0a2/probability-probability-4e9b653988a13f7218d41731-unresolved.png

## Sweep, simulation, and sequence status

The required probability_sweep route was attempted for the exact target pool, random pool, and event-option pools.

- Status error, code PROBABILITY_SWEEP_RANGE_REQUIRED.
- Exact blocker: every sweep path requires a scenario range, numeric alternatives, or numeric state value.
- The target attempt stopped at P23_TARGET_WARTIME_REAL_DISPUTE/base.
- The all-scenario attempts stopped at P23_EVO1_HIDDEN_NORMAL/base.
- No artifact URI was produced for these sweep attempts.
- No numeric ranges were invented because the specification does not declare alternatives or thresholds in the accepted scenarioSet schema.

probability_simulate was skipped because no uncertain-input distributions, correlations, seed, or sample count were explicitly declared.

probability_sequence was skipped because no complete custom-pool manifest declared cadence, cooldown, recovery, cap, removal, reset, timer transitions, and terminal states. The mission adapter also reports sequence false.

The MTTH evaluate request returned status error, code PROBABILITY_SURFACE_EMPTY, with no artifact and diagnostics 0 because reusable common/mtth entries are not indexed by the current event_mean_time_to_happen adapter.

## Structural Event 23 MCP evidence

The first focused hoi4.event_inspect scan for chaosx.nr23.1 with helper expansion returned status error, code INTERNAL_ERROR, with no artifact.

A focused roots retry with helper expansion disabled timed out after 180 seconds and returned no artifact.

The focused scan retry after the render cache was warm returned:

- Status ok, code EVENT_INSPECTED_PARTIAL.
- Artifact URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/925811e73d12a90206240f646f2bd69ca8ff2fb556e1d9ffb5198eeb7b6329f7/4b447528f3879ae8307916d989a33d97a6af0e5b7792f0b5614a46368c815b15/event-scan-4f0d4282fe03.json
- MCP revision 4f0d4282fe038e3e108db680198bd93fdb0b04abbe6171fd6b17f45f782fee6d.
- Graph hash c36ab4be400641a5e9e91a43c87986e826e15ec2273db1069a4a3b375ceacb25.
- Workspace-wide counts are events 9742, options 15167, entries 1152, helpers 0, unresolvedNodes 8716, terminals 7772, edges 38374, issues 2198, diagnostics 2198, and blockingDiagnostics 0.
- The structural result is partial and workspace-wide, not an Event 23-only proof.
- The graph issue code is EVENT_OPTION_DANGLING.
- The unresolved kinds include dynamic_helper 18, missing_event 19, missing_helper 8679, and partial_source 1.
- Event 23-related helper calls reported absent from the active MCP catalog include sov_nuclear_bombs_initialize_event_state, sov_nuclear_bombs_initialize_achievement_state, brilliant_scientist_record_nuclear_milestone, and sov_nuclear_bombs_resolve_coercion_response.
- Source-only search finds definitions for the first three at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:407, common/scripted_effects/023_sov_nuclear_bombs_achievement_effects.txt:9, and common/scripted_effects/016_brilliant_scientist_context_effects.txt:569, and finds sov_nuclear_bombs_resolve_coercion_response at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:917.
- These are analyzer/catalog coverage gaps, not source-only claims that the helpers do not exist.

The focused event overview render returned:

- Status ok, code EVENT_RENDERED_PARTIAL.
- Manifest URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7fdeb95c108e0e419d343bd4d39c82dd8c3fe139b153837467120641df2621c/65905283e098e6bc6788b7ef1e6bc1a52a2db0ecf661f80980f5e215ad6b0508/event-overview-4f0d4282fe03-manifest.json
- JSON URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce28bdad3823a85ba86cb238a8a95560df5739196e4179c1ab26dec7593c4079/5bb87d9e9320b95073a66426097c6902d69c5a8f6d8fa4d3314fd18c1e9e5a7d/event-overview-4f0d4282fe03.json
- SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c39f5b010cf82a70016136e02e0c55a5f5a74d0bfd511e482fd09128f17f700d/86692d0a9dc2d3da64e8b7773e97e574931402f871faee8629104b1c3d87ea54/event-overview-4f0d4282fe03.svg
- PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5fdfa68c4465e7fb2b1e0f7a3ad8988e45b7208c7b29f321cf41cdb3e33dfabb/5855795471d874e0001cdd0368f7bbd96fde1061b21c8560df8ef70c09fd5f79/event-overview-4f0d4282fe03.png

The focused event-options render returned status ok, code EVENT_RENDERED_PARTIAL.

- Manifest URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2bc940aaac60dde4287a61a88bd7a276590a92ab79fa3e2ea34848227d56434/11c44e995958e2a24e73d2d097285a0ebc7b6da8dc09395f6e0c5df6dbce0919/event-options-74d7ca0b0fda-manifest.json
- JSON URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d63292ac8f691080b16d373188ddb54b66d3d119c1cea16c1889482e591a2a3/5e917781c9e5da10e0de96f6bbd48f1e1b60c18fb41d549a0411169ab31b71c0/event-options-74d7ca0b0fda.json
- SVG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f81e4ab6842cbc013db3a0af36164981b09ba63714ae9f319c68560577c9af51/f16d62d11180d8cb52890c0c2b1d780b01c37f5b8c466e3f2f827bd01098f293/event-options-74d7ca0b0fda.svg
- PNG URI: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e80cf26af883964751f81c96409aea47c2d24c3aae6571f638f057c3eed70c74/3f688ecdbe917df6923ae4cf05c937cd197a13738fe38f4e39f571217f815e29/event-options-74d7ca0b0fda.png

The structural render remains partial because the package catalog omits helpers that source-only inspection finds, and its counts are workspace-wide with 2198 dangling-option issues.

## Source-only weighted-surface review

### Decision AI and target-aware decision scores

The current decision file exposes 80 ai_will_do blocks to the mission adapter. The decision_ai_will_do adapter itself indexed zero candidates, so no engine-backed decision score race or click probability is claimed.

The exact 12 target-bearing decision scores are:

- common/decisions/023_sov_nuclear_bombs_decisions.txt:72-88, sov_nuclear_bombs_operational_command, base constant:sov_nuclear_bombs_ai.command, wartime factor constant:sov_nuclear_bombs_ai.wartime_factor, zero before Evolution I, and target factors capital 1.80, airbase 1.35, and industrial 1.25.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:91-107, sov_nuclear_bombs_collapse_command, base constant:sov_nuclear_bombs_ai.collapse, wartime factor 1.40, and transferred-custody factor constant:sov_nuclear_bombs_ai.transferred_custody_factor.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:135-161, sov_nuclear_bombs_harden_storage_site, base 1.00, wartime factor 1.80, assigned-site factor constant:sov_nuclear_bombs_ai.assigned_site_factor, and target factors capital 1.80, airbase 1.35, and industrial 1.25.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:164-190, sov_nuclear_bombs_disperse_reserve_package, base 0.90, wartime factor 1.60, remote-site factor constant:sov_nuclear_bombs_ai.remote_site_factor, and airbase factor constant:sov_nuclear_bombs_ai.air_base_target_factor.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:222-237, sov_nuclear_bombs_expand_fissile_production, base 1.10, reactor-entitlement factor 1.80, remote-reactor factor constant:sov_nuclear_bombs_ai.reactor_site_factor, and industrial factor constant:sov_nuclear_bombs_ai.industrial_target_factor.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:297-312, sov_nuclear_bombs_survey_remote_test_state, base 1.30, test-failure factor 1.40, remote-site factor constant:sov_nuclear_bombs_ai.remote_site_factor, and airbase factor constant:sov_nuclear_bombs_ai.air_base_target_factor.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:418-433, sov_nuclear_bombs_select_coercion_target, base 1.00, wartime factor 1.30, and target factors capital 1.80, airbase 1.35, and industrial 1.25.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:615-630, sov_nuclear_bombs_redirect_strike_state, base 0.20, and target factors capital 1.80, airbase 1.35, and industrial 1.25.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:731-746, sov_nuclear_bombs_select_retaliation_target, base 1.30, target factors capital 1.80, airbase 1.35, and nuclear-major factor constant:sov_nuclear_bombs_ai.major_target_factor.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:792-807, sov_nuclear_bombs_select_disputed_depot, base 1.50, transferred-custody factor constant:sov_nuclear_bombs_ai.transferred_custody_factor, and capital factor 1.80.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:945-960, sov_nuclear_bombs_select_dismantlement_site, base 0.70, assigned-site factor constant:sov_nuclear_bombs_ai.assigned_site_factor, and industrial factor constant:sov_nuclear_bombs_ai.industrial_target_factor.
- common/decisions/023_sov_nuclear_bombs_decisions.txt:1097-1112, sov_nuclear_bombs_breakaway_request_return, base 1.00, transferred-custody factor constant:sov_nuclear_bombs_ai.transferred_custody_factor, and capital factor 1.80.

All twelve target-aware scores are positive in at least one source branch. The MCP could not bind nested FROM state scopes, event targets, owner/controller relations, registered state variables, or target flags under the empty scenario fixtures. Therefore target rank, target dominance, target starvation, and rank-reversal conclusions are unresolved.

The source validity layer does include state existence, impassable, ownership/control, state registry, missing/dismantled flags, infrastructure, route, war relation, nuclear-major, subject, capitulation, and event-target checks. Those checks are source evidence only until the named state fixtures bind them.

### Mission scores and activation

The complete mission adapter pool is 80 candidates. Important current base scores are:

- Audit and custody: audit_stockpile 1.20, centralize_release_authority 0.70, delegate_emergency_retaliation 0.70, custody_party 1.20, custody_military 1.20, custody_scientific_safety 1.50, and custody_dispersed_commands 1.00.
- Production and preparation: assemble_device_batch 0.80, prepare_delivery_crews 1.20, conduct_command_exercise 1.00, install_stronger_authentication 0.90, expand_fissile_production 1.10, and harden_storage_site 1.00.
- Test path: prepare_instrumented_proof_test 1.50, prepare_concealed_field_test 1.00, prepare_public_test constant:sov_nuclear_bombs_ai.demonstration, strengthen_test_evacuation 1.10, cancel_prepared_test 0.20, investigate_test_failure 1.60, and survey_remote_test_state 1.30.
- Coercion and settlement: close_coercion_target 0.05, send_private_signal 1.20, issue_public_ultimatum 1.10, stage_wartime_demonstration 0.80, prepare_limited_strike 0.60, accept_partial_settlement 0.90, adjust_demand 0.40, raise_demand 0.15, and back_down 0.25 with a credibility-below-10 factor 2.50.
- Authorization and retaliation: complete_technical_certification 1.00, overrule_safety_veto 0.10 with severe-gate factor constant:sov_nuclear_bombs_ai.severe_loss_factor, give_final_authorization 0.10 with the same severe-gate factor only when can_authorize_first_use is true, hold_strike 0.40, reduce_to_remote_demonstration 0.70, abort_and_recover_device 0.30, retaliation_window 0.60, limit_retaliation_profile 1.20, preserve_reserve 1.00, authorize_retaliation 0.30 with confirmed-enemy-use factor 1.60, and enter_atomic_moratorium constant:sov_nuclear_bombs_ai.moratorium with restraint factor 1.35 after enemy use.
- Recovery and collapse: emergency_hotline constant:sov_nuclear_bombs_ai.moratorium, propose_reciprocal_standdown 1.10, suspend_release_orders 1.00, recall_devices 1.10, secure_rail_corridor 0.90, negotiate_joint_custody 1.00, conduct_recovery_raid 0.20, disable_devices 1.40, destroy_compromised_site 0.30, restore_the_ledger 1.00, seal_reserve_batch 1.30, dismantle_batch 0.70 with scientific-safety factor 1.70, invite_observers 0.80, record_reciprocal_restraint constant:sov_nuclear_bombs_ai.restraint_factor, reactivate_arsenal 0.20, and collapse_command constant:sov_nuclear_bombs_ai.collapse.
- Breakaway: breakaway_secure_custody 1.30, breakaway_attempt_technical_access 0.40, breakaway_form_command 0.25, breakaway_integrate_delivery 0.10, breakaway_request_return 1.00, and the three operationalization missions at 0.20 each.

The timed mission identifiers and current base scores are:

- sov_nuclear_bombs_device_assembly_mission, 0.80.
- sov_nuclear_bombs_delivery_crews_mission, 0.70.
- sov_nuclear_bombs_command_exercise_mission, 0.60.
- sov_nuclear_bombs_proof_test_mission, constant:sov_nuclear_bombs_ai.demonstration.
- sov_nuclear_bombs_ultimatum_response_mission, 1.00.
- sov_nuclear_bombs_strike_preparation_mission, 0.40.
- sov_nuclear_bombs_retaliation_window_mission, 0.60.
- sov_nuclear_bombs_rail_corridor_security_mission, 0.70.
- sov_nuclear_bombs_breakaway_technical_access_mission, 0.20.
- sov_nuclear_bombs_breakaway_command_formation_mission, 0.20.
- sov_nuclear_bombs_breakaway_delivery_integration_mission, 0.20.
- sov_nuclear_bombs_joint_custody_transfer_mission, 0.70.
- sov_nuclear_bombs_dismantlement_inspection_mission, 0.80.

These timed missions are selectable_mission = no and available = always = no. Activation flags, active-state triggers, completion effects, cancellation, timeout, and mission cleanup determine their timing. The current MCP mission adapter has no timeDistribution or sequence capability, so timing drift, repetition, starvation, and terminal-state behavior remain unresolved.

### MTTH evolution timing

The source-only MTTH bases and factors are:

- evolution_i_interval: base 180 days, public arsenal factor 0.75, serious crisis factor 0.65, integrity below 40 factor 1.35, and atomic moratorium factor 1.50.
- evolution_ii_interval: base 240 days, collapse factor 0.75, war factor 0.85, public arsenal factor 0.75, integrity below 40 factor 1.35, and atomic moratorium factor 1.50.
- evolution_iii_interval: base 300 days, major exchange factor 0.60, confirmed enemy use factor 0.65, war factor 0.85, integrity below 40 factor 1.35, and atomic moratorium factor 1.50.
- evolution_iv_interval: base 360 days, collapse factor 0.70, major exchange factor 0.60, confirmed enemy use factor 0.65, reciprocal restraint factor 1.25, centralized authority factor 1.10, integrity below 40 factor 1.35, and atomic moratorium factor 1.50.

Source-only timing risks are present against the prose scenario expectations. P23_EVO1_HIDDEN_NORMAL describes a near-120-day center while the source base is 180 days without the public or crisis accelerators. P23_EVO3_MAJOR_RIVAL_NORMAL describes a two-major peace case, while the source evolution III world gate also requires an opened gate, active major exchange, or confirmed enemy use. P23_EVO4_COLLAPSE_ACCELERATED describes launch-preparation verification as sufficient, while the source evolution IV world gate requires an active major exchange, an opened IV gate, or at-war confirmed enemy use plus another nuclear major. The scheduler helper does not explicitly exclude atomic moratorium before scheduling the MTTH event; moratorium is represented as a delay factor and later stage/validity gates remain separate.

These are bounded source/spec mismatches, not exact timing distributions, because the current MCP cannot index the reusable common/mtth entries.

### Event ai_chance and selection

The doctrine race uses source bases constant:sov_nuclear_bombs_ai.doctrine for all four options. Party has a 1.25 communist factor. Military has the wartime factor constant:sov_nuclear_bombs_ai.wartime_factor. Scientific safety has a 1.50 democratic factor and a 1.40 test-failure factor. Dispersed commands has a 1.20 wartime factor and a 1.20 capital-threat factor.

The coercion response race has source bases 35, 25, 20, 20, 10, and 10 for a, b, c, refuse, e, and f respectively. All options require sov_nuclear_bombs_event_target_response_is_valid. Option b also requires demand above the minimum, option c requires not at war, and option f requires faction membership. No source-local dynamic modifier for target strength, losses, credibility, guarantee, intelligence, or delivery route is present in this race.

The eleven report events each have one option at base ai_chance 100. They are deterministic one-option reports rather than selection races.

The MCP can normalize a complete categorical pool in principle, but the current event source has multiple categorical pools and the nested event-target, war, government, subject, capitulation, tag, and faction predicates cannot bind to the empty scenario state. The narrowed doctrine and coercion pools were therefore evaluated separately, and no full 21-option Event 23 probability is claimed.

### Random test outcomes

The source block at common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:687 executes only when the accepted action type is test. Its three entries use constant:sov_nuclear_bombs_tuning.test_success_weight, test_failure_weight, and test_accident_weight.

The current constants are 70, 20, and 10. MCP exactly confirms 70 percent success, 20 percent failure, and 10 percent accident conditional on entering the list, across all 43 named scenarios, with zero unresolved and zero diagnostics.

Source consequences are failure integrity -8 and accident integrity -18 plus one accident count, test-accident flag, and serious-crisis flag. Accident schedules report event chaosx.nr23.102 and other test results schedule chaosx.nr23.101. These consequences are source-only because the enclosing test-selection and preparation probability is outside the three-entry pool.

## First-use gate audit

The source severe gate is common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:280-301, sov_nuclear_bombs_event_severe_first_use_gate.

It requires all of the following:

- Evolution IV active.
- Global chaos at least constant:sov_nuclear_bombs_evolution.first_use_chaos, currently 1000.
- War active.
- Strategic losses at least constant:sov_nuclear_bombs_evolution.first_use_min_strategic_loss, currently 3.
- Capital threat active.
- Front collapsed.
- Reserve exhausted.
- Confirmed enemy nuclear use or verified enemy launch preparation.
- No atomic moratorium.
- No soviet_first_use_recorded flag.
- A delivery route.
- Readiness at least constant:sov_nuclear_bombs_tuning.first_use_profile_readiness, currently 75.
- Integrity at least constant:sov_nuclear_bombs_tuning.minimum_integrity_for_release, currently 20.
- The action state resolves to a valid nuclear-major target.

The helper sov_nuclear_bombs_event_can_authorize_first_use at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:303-309 adds an owner/controller has_war_with ROOT check after the severe gate.

The Evolution III world gate at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:259-266 requires another nuclear major plus an opened Evolution III gate, active major exchange, or confirmed enemy use.

The Evolution IV world gate at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:268-278 requires another nuclear major plus active major exchange, an opened Evolution IV gate, or at-war confirmed enemy use.

The limited-strike validity helper at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:536-550 requires Evolution II, a selected state, targeted delivery route, readiness and integrity minima, a valid command target, owner/controller war with ROOT, and explicitly not a nuclear-major target.

The major-strike validity helper at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:552-561 requires Evolution III, a selected state, targeted delivery route, minimum test readiness, minimum release integrity, and a valid nuclear-major target.

The prepared-strike helper at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:577-587 accepts either a valid limited strike or a valid major strike with a major-exchange world gate or severe first-use authorization.

The prepared-strike chain at common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:590-611 requires actor validity, prepared and complete flags, action reservation, combat-strike action type, action context, no active project, no moratorium, no suspended release orders, a selected doctrine, centralized authority or delegated retaliation, reserved devices, a valid prepared strike, and fresh action context validity.

The final authorization mission score at common/decisions/023_sov_nuclear_bombs_decisions.txt:587-598 has base 0.10, multiplies by the severe-loss factor only when sov_nuclear_bombs_event_can_authorize_first_use is true, and multiplies by 0.00 only below Evolution III. Its availability requires the prepared-strike chain and technical certification, not the severe gate itself.

The source therefore does not prove the requested literal invariant for all Soviet combat first use. At Evolution III or later, a non-major valid limited strike can satisfy the prepared-strike chain, final authorization retains a positive base 0.10 without the severe gate, and common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:713-756 records soviet_first_use_recorded for an accepted combat_strike whenever confirmed enemy use is absent and that flag is not already set. The recording occurs before the nuclear-major branch at lines 760-768. This is a high-risk source-level path for a limited first combat strike below Evolution IV, Chaos 1000, strategic losses 3, and the other severe gates.

The source does appear fail-closed for a major-target first-use detonation through the major-target validity and major-exchange/severe-gate branches, but the MCP cannot bind the complete AI mission state to prove that campaign path quantitatively.

First-use conclusion classification: source-only bounded finding, not exact AI selection probability. The requested no-first-use guarantee is unresolved and should be treated as failing at the literal bookkeeping level unless the design intentionally distinguishes a limited coercive strike from first use.

## Risk findings and classifications

- Decision score race: score-only/unresolved. The decision adapter returned zero indexed candidates and the mission adapter exposed the scores.
- Full mission candidate pool: score-only partial. The exact 80-candidate pool was supplied, but 253 rows remain unresolved and the adapter cannot normalize scores or provide a selection probability.
- Target-aware modifiers: unresolved. The exact 12 pool was supplied, but all nested state/target eligibility and external relationships are not bound.
- Doctrine event options: unresolved partial. The four-option pool is complete, but 4 rows remain unresolved and the empty fixture disables one factor.
- Coercion event options: unresolved partial. The corrected six-option pool is complete, but 33 rows remain unresolved, 51 diagnostics are present, and fallback behavior is not proven.
- Singleton report options: source-only deterministic one-option reports.
- Random test outcomes: exact conditional result. The complete pool has zero unresolved and zero diagnostics, with 70/20/10 conditional probabilities.
- MTTH evolution timing: unresolved. The reusable MTTH entries are not indexed by the current adapter, and no time-distribution result exists.
- Dominance and starvation: unresolved for mission and event-option races because eligibility and complete campaign pools are not bound. Empty-fixture dominant-outcome warnings are not campaign evidence.
- Rank reversals and sensitivity: unresolved because sweeps require undeclared numeric alternatives or state ranges.
- Repetition, cooldown, recovery, timer reset, and terminal-state risks: unresolved in MCP because sequence and timeDistribution are unsupported and no complete state-transition manifest was declared.
- AI strategy factors: no Event 23-specific source was found under common/ai_strategy or common/ai_strategy_plans, so no strategy-factor MCP surface was available to evaluate.
- First-use exploit risk: high source-only risk for limited combat strike bookkeeping below the severe gate, as described above.
- Structural event graph: partial MCP evidence with catalog gaps and workspace-wide dangling-option diagnostics.

No exact selection probability is claimed for any mission or target-aware decision surface. No exact overall test outcome probability is claimed beyond the conditional three-entry random_list result.

## Recommended owner fixes, not applied

1. Add a native machine-readable scenario fixture for Event 23 that binds ROOT, THIS, PREV, FROM, saved scopes, event targets, state ownership/control, war relations, variables, flags, tags, nuclear technologies, reactor entitlement, and target nuclear counts for every named scenario.

2. Re-run the complete 80-candidate mission evaluation and the exact 12-candidate target subset after the fixture exists, then run a numeric probability_sweep for the declared readiness, integrity, target-value, loss, and crisis ranges.

3. Decide whether a limited non-major combat strike is intended to count as Soviet first use. If it is, require sov_nuclear_bombs_event_severe_first_use_gate in final authorization and release validation. If it is not, split limited-strike receipt bookkeeping from first-use bookkeeping and preserve a separate explicit major-first-use flag. Revalidate the target, route, reservation, and gate immediately before execution.

4. Align the MTTH scenario expectations with source bases and world gates, or update the accepted scenario specification. Explicitly decide whether an already-scheduled evolution event may mature during atomic moratorium, rather than relying on a delay factor alone.

5. Make coercion fallback behavior explicit and re-run the full categorical event-option analysis once the nested event-target fixture is available. Keep the corrected refuse identifier and do not treat .120.d as an option.

6. Supply a complete mission lifecycle manifest covering activation, timeout, cancellation, cleanup, cooldown, recovery, re-entry, cap, removal, reset, and terminal states before using probability_sequence or claiming repetition safety.

7. Add or document any intended Event 23 AI strategy-factor surface under common/ai_strategy so it can be inspected separately from decision scores and event options.

## Unresolved, skipped, and superseded evidence

- The empty scenario maps are the primary bounded-MCP limitation. They preserve all 43 names but cannot bind nested Clausewitz scopes or external factors.
- probability_sweep was blocked by PROBABILITY_SWEEP_RANGE_REQUIRED and produced no artifact.
- probability_simulate was skipped because uncertain inputs and a seed were not declared.
- probability_sequence was skipped because no complete custom-pool lifecycle manifest exists and the mission adapter reports sequence false.
- event_mean_time_to_happen evaluation returned PROBABILITY_SURFACE_EMPTY with no artifact.
- The initial event_inspect returned INTERNAL_ERROR with no artifact.
- The focused event roots retry timed out after 180 seconds with no artifact.
- The first target render returned PROBABILITY_ANALYSIS_STALE with no artifact; its current replacement render is the probability-071a46e9ee812baf5696daa2 target comparison render.
- Earlier mission runs with 79 and 81 candidates are superseded by the final complete 80-candidate result probability-616b30ef19c2a1e81af47bee.
- Earlier coercion requests containing chaosx.nr23.120.d were superseded by the corrected six-option pool containing chaosx.nr23.120.refuse.
- The current-source random refresh and current-source same-scenario comparison are probability-6c79b8b6b092d67956f9446b and probability-4e9b653988a13f7218d41731 respectively.
- The current handoff records source drift in the shared worktree and uses source-qualified MCP revisions rather than silently merging results from different source snapshots.

Remaining uncertainty is sufficient that the disposition remains implemented with partial MCP evidence and the overall campaign-balance conclusion remains unresolved.

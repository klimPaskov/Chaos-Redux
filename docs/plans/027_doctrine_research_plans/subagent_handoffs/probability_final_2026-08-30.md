# Event 027 Doctrine Research — final AI probability audit handoff

> **Superseded status notice (2026-09-01):** This dated probability handoff is preserved as historical evidence and is superseded as a current status authority by ../documentation_state.md. Its source snapshot and MCP artifact paths predate the current source reconciliation.

Audit date: 2026-08-30.

Audit role: read-only `chaosx_ai_probability_auditor`.

Status: **INCOMPLETE / BLOCKED FOR ACCEPTANCE**.

Acceptance: **NOT GRANTED**.

The four Doctrine Research chooser pools were inspected and evaluated across all named DR-A01 through DR-G03 scenarios, but the HOI4 probability adapter could not resolve the typed country, doctrine, and trigger fixture needed to produce normalized candidate probabilities. The shared repeatable Event 027 picker also produced no discoverable candidates because it is a manual accumulator over `global.all_events`, not a discoverable `random_list` pool. The required named-scenario evidence therefore remains unresolved.

No gameplay, AI, balance, event, focus, decision, technology, doctrine, trigger, effect, localisation, or runtime file was edited by this audit. This handoff is the only file created by this audit.

## 1. Scope and references

The repository rules in `AGENTS.md` were read before the audit. The complete specification directory `docs/specs/027_doctrine_research_specs/` was read, including all of the following files:

- `README.md`
- `027_doctrine_research_acceptance_criteria.md`
- `027_doctrine_research_achievement_prompt.md`
- `027_doctrine_research_asset_prompt.md`
- `027_doctrine_research_catalog_cluster_handoff.md`
- `027_doctrine_research_coding_prompt.md`
- `027_doctrine_research_doctrine_registry_matrix.md`
- `027_doctrine_research_goal_prompt.md`
- `027_doctrine_research_probability_scenarios.md`
- `027_doctrine_research_research_notes.md`
- `027_doctrine_research_review_and_closure.md`
- `027_doctrine_research_source_review.md`
- `027_doctrine_research_spec_part_1_core.md`
- `027_doctrine_research_spec_part_2_choice_flow.md`
- `027_doctrine_research_spec_part_3_evolutions_balance_ai.md`
- `027_doctrine_research_spec_part_4_presentation_assets_achievements.md`

The required repository skills were read before analysis: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-mtth`, `chaos-redux-event-planning`, and `chaos-redux-improvement-loop`. The current auditor prompt in `.codex/agents/chaosx_ai_probability_auditor.toml` was also read.

The current weighted source and related surfaces reviewed were:

- `common/scripted_effects/027_doctrine_research_ai_effects.txt`
- `common/scripted_effects/027_doctrine_research_effects.txt`
- `common/scripted_effects/027_doctrine_research_exact_mastery_effects.txt`
- `common/scripted_triggers/027_doctrine_research_triggers.txt`
- `common/script_constants/027_doctrine_research_constants.txt`
- `common/scripted_localisation/027_doctrine_research_scripted_localisation.txt`
- `common/on_actions/027_doctrine_research_on_actions.txt`
- `common/on_actions/027_doctrine_research_cxt_on_actions.txt`
- `common/ideas/027_doctrine_research_cxt_extension_ideas.txt`
- `events/027_doctrine_research.txt`
- `common/scripted_effects/chaosx_logic_effects.txt`
- `common/scripted_effects/chaosx_settings_effects.txt`
- `common/scripted_effects/chaosx_event_cluster_effects.txt`
- `common/scripted_triggers/chaosx_settings_triggers.txt`
- `common/script_constants/event_cluster_constants.txt`
- `common/scripted_triggers/cbrn_doctrine_triggers.txt`
- `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt`
- `common/on_actions/chaosx_on_actions_system.txt`

The Event 027 overview and previous probability/completion handoffs were reviewed, including `docs/events/027_doctrine_research/overview.md`, `docs/plans/027_doctrine_research_plans/mcp_evidence.md`, `docs/plans/027_doctrine_research_plans/subagent_handoffs/probability_baseline_2026-08-29.md`, and the current parent implementation/completion handoffs.

The required offline Paradox wiki pages were read for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, technology modding, doctrine modding, and achievements. The installed vanilla documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`, `common/doctrines/_documentation.md`, and the doctrine folder, grand-doctrine, track, and subdoctrine documentation.

## 2. Scenario contract and completeness

MCP workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Full scenario set: `DR_027_FINAL_2026_08_30`.

Full scenario hash: `2e0e1ba67d5dc17a2982d15c2c35568382f8e7d8d16badde45cbbbe94a6d8daa`.

The exact named scenarios covered were:

- DR-A01, DR-A02, DR-A03, DR-A04, DR-A05, DR-A06.
- DR-B01, DR-B02, DR-B03, DR-B04.
- DR-C01, DR-C02, DR-C03, DR-C04, DR-C05, DR-C06, DR-C07.
- DR-D01, DR-D02, DR-D03, DR-D04, DR-D05, DR-D06.
- DR-E01, DR-E02, DR-E03, DR-E04, DR-E05, DR-E06.
- DR-F01, DR-F02, DR-F03, DR-F04, DR-F05.
- DR-G01, DR-G02, DR-G03.

The scenario fixture declared the land, naval, air, special-forces, Chaos, doctrine-state, track, subdoctrine, batch, queue, DLC, CBRN, establishment, formation, repeatability, and cluster conditions needed by the scenario matrix. The current probability schema rejected nested `scopes`, `variables`, `externalFactors`, `setup`, `cadence`, and `terminalState` objects, so the submitted fixture used flat primitive state and flags. That format allowed scenario identity and declared values to be preserved, but it did not provide typed country scopes or native doctrine graph objects that the source triggers require.

The four `random_list` pools were supplied separately and are source-complete as AST pools. The external-factor and trigger state is not engine-complete, so candidate eligibility and effective weight resolution remain incomplete. No exact selection probability is inferred from the source list lengths or from unresolved rows.

## 3. Weighted surfaces and source pool mapping

The current AI file contains four separate `random_list` surfaces. The `.1` AST entry is the seed/metadata entry; the actual candidate rows begin at `.2`.

| Surface | Source location | Candidate paths | Source pool size | Pool result |
| --- | --- | --- | ---: | --- |
| Domain | `027_doctrine_research_ai_effects.txt:17` | `entry.2` through `entry.6` | 5 | Source-complete, country resolution unavailable |
| Grand Doctrine | `027_doctrine_research_ai_effects.txt:144` | `entry.2` through `entry.14` | 13 | Source-complete, country resolution unavailable |
| Track | `027_doctrine_research_ai_effects.txt:322` | `entry.2` through `entry.19` | 18 | Source-complete, country resolution unavailable |
| Subdoctrine | `027_doctrine_research_ai_effects.txt:1999` | `entry.2` through `entry.108` | 107 | Source-complete, country resolution unavailable |

A combined 143-entry inspect was also attempted. It returned `poolComplete: false` because it combined four separate random-list surfaces rather than representing one normalized selection race. It must not be used as a single probability pool.

All four random lists use `seed = random`. The engine surface is therefore weighted random selection among positive rows; the score components are not click probabilities and are not automatically normalized by the game outside the complete eligible candidate pool.

## 4. Mandatory probability inspect evidence

The required source-first call was:

`hoi4.probability_inspect({ source: { path: "common/scripted_effects/027_doctrine_research_ai_effects.txt" }, refresh: true, workspaceId: "mod_chaos_redux_ea3b2d67c2c0" })`.

Result: `PROBABILITY_SOURCE_DISCOVERED`; adapter suggestion `random_list`; 143 available/source-matched candidates; 0 current resolved candidates because no concrete country fixture was available. Source revision: `e663fe67d834add7b2a785c2ffaec9a4813d386c1fe631744c36550e9095cd94`. Source hash: `cd052de2ad2fecb7361df11f79ea993d995bb0e5f8b7f0ba5bcd4900b0b391e4`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3ac922f053f00afc2a6ef5aff901602a79c8ff1c8218371553949c1189be33e0/adc4a6666460c2035977189ee0d1f4f063053c95a552377adba42d91d321bf4e/probability-inspect-cd052de2ad2f.json`.

The source-complete per-surface inspect calls were:

| Surface | Call input | Result | Artifact |
| --- | --- | --- | --- |
| Domain | `random_list`, `027_doctrine_research_ai_effects.txt:17.entry.2` through `.6` | `PROBABILITY_SOURCE_INSPECTED`, `poolComplete: true`, 0 resolved candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f44a047cc3deb1628ed7e6164838c86e1dd318fc066c48b4e4f22eaf306ccf4/23ceab5bebe8b240b6a359ffc66d8f7afbe4ef4e0cc0728f69921b422d91359b/probability-inspect-cd052de2ad2f.json` |
| Grand Doctrine | `random_list`, `027_doctrine_research_ai_effects.txt:144.entry.2` through `.14` | `PROBABILITY_SOURCE_INSPECTED`, `poolComplete: true`, 0 resolved candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b7b890f01283d3396ed0bf4881157ea929cf6d2c71b7ea3f9c38bd1ff35ece3/7e0f5530ebd989fec8ba1fcf4def4f66b8fef5e815e3aac0c9b5aeea8a152a91/probability-inspect-cd052de2ad2f.json` |
| Track | `random_list`, `027_doctrine_research_ai_effects.txt:322.entry.2` through `.19` | `PROBABILITY_SOURCE_INSPECTED`, `poolComplete: true`, 0 resolved candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/beaf282170753cbe88e8d0a15cbaca64f84077aac984d9de2dcca5edf231b054/65f90806130de2e90970f177ebffebf658dc93cef947e1781f126053dfded078/probability-inspect-cd052de2ad2f.json` |
| Subdoctrine | `random_list`, `027_doctrine_research_ai_effects.txt:1999.entry.2` through `.108` | `PROBABILITY_SOURCE_INSPECTED`, `poolComplete: true`, 0 resolved candidates | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c80a00f6b98697d4a7986c88bf5a2569c9ade2661b1e8e4e4252f46a02d6505/9a04cb6eb8659e77e33ae7401b72756e156c6683a19eb56e2c33836859c9a8d9/probability-inspect-cd052de2ad2f.json` |
| Combined, not a valid single pool | All four ranges together | `poolComplete: false`, 143 source candidates, one unresolved pool descriptor | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1d04b7e0621f5b752e80386bcfcde7ebc92c021078e87cc5a68c47c6807a071b/25a42d7a3ebf27e72daea53223dad12939be118f70261d95711ae8efc03660dd/probability-inspect-cd052de2ad2f.json` |

## 5. Named-scenario evaluate results

Each call used adapter `random_list`, the current AI source, the complete per-surface candidate path range, all 37 scenarios in `DR_027_FINAL_2026_08_30`, `horizonDays: 1`, metrics `raw_value` and `conditional_probability`, and JSON/ranking/matrix/unresolved outputs.

| Surface | Analysis ID | Result | Scenarios | Candidate rows | Unresolved rows | Source revision returned |
| --- | --- | --- | ---: | ---: | ---: | --- |
| Domain | `probability-25f6718461e47bac667bcb1f` | `PROBABILITY_ANALYZED_PARTIAL` | 37 | 185 | 5 | `716d05cf6798bd521bc2bec405774d7548ed09c7cc24b9849831e343f615074b` |
| Grand Doctrine | `probability-4f7255bb14309f0470fdec0d` | `PROBABILITY_ANALYZED_PARTIAL` | 37 | 481 | 13 | `f8a25903bd22e8d041c0ea59f7d68621035841c75b7a3026d9e4ba4ce7aaec23` |
| Track | `probability-add7ca8ff5ba4172ccd0a96c` | `PROBABILITY_ANALYZED_PARTIAL` | 37 | 666 | 18 | `9d18e18a6454554a98bcb4105ff7fbf002afede42c1a6907817b872580e18f08` |
| Subdoctrine | `probability-eb7ad3a2a27e16ce73e2ae49` | `PROBABILITY_ANALYZED_PARTIAL` | 37 | 3,959 | 107 | `910d25d408e91f6ec638ae21b12632309ee2e570b7b0428abb42fec004c4cbd0` |

The latest four primary JSON artifacts were:

- Domain: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc4467c149257bfcd0382e1ac697a8908d52fa3ef4eadfd8e7c15c697a01be39/2feba52e47d9054a0afffce8f0896d767e6e69f56728edaad065fe66ea766b54/probability-25f6718461e47bac667bcb1f.json`.
- Grand Doctrine: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfbd96230e81cd3cea2bf635a02b80d323716c346c52fc0aa271235f882fafff/308e019d5a692a62ec4468b055e8f048727b502ebfa3f999819845392923abac/probability-4f7255bb14309f0470fdec0d.json`.
- Track: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/517b22059cacd66b8bbaae625fbfe470081e748d040cd6af3ef259e44009667f/2b290a8d3a5d8405aa9e6a39a352f6c986a9b78d4372510b7cc50aba41d4ce83/probability-add7ca8ff5ba4172ccd0a96c.json`.
- Subdoctrine: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e9cb4c919771ddf07b9eca5d9c24e040d8a06f4e75c29f0f78d31f7155e644ef/6f1034cfed927d9ff9430f54c48905cab1ca71c77736c555af52eff60e7fd939/probability-eb7ad3a2a27e16ce73e2ae49.json`.

The evaluate-attached rendered evidence was generated with each partial analysis. These resources are review evidence, not acceptance evidence, because unresolved rows prevent normalized conclusions:

- Domain ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26189dd7a758cb3bedca7cb5159740b6cc844a8650d6f85c2d2db51c81ffa919/dd6cf52f0b6436928155de18669760c1817b5a724bf7ce225ff2c6d90f0e34b2/probability-probability-25f6718461e47bac667bcb1f-ranking.svg`.
- Domain matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6fde69bb46c053ce160fd4ca3e71cedc32f5b96056cf37893f39179f039376b/b846a866e81bc656d50ba338838224ee902613444bb7d3bd70af93b6cfaa0751/probability-probability-25f6718461e47bac667bcb1f-matrix.svg`.
- Domain unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2f9aa7b978700a5160d30df0c31cbf192ad6cffa149af59c7e1ea6bbf681253/4d68bc457bf09728aaaa194941ac117bf4e503473f94052ea10788e5846e31f9/probability-probability-25f6718461e47bac667bcb1f-unresolved.svg`.
- Grand Doctrine ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e901749574d92ce8d011954bfe8cab29a0ec743e91b6aabfab5fc7cfd627a708/98b0d152b3a9009e3e2e75ce27228ae1fb4609c9ff1b1839d9be13165240f21c/probability-probability-4f7255bb14309f0470fdec0d-ranking.svg`.
- Grand Doctrine matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9df8ebe301ebb67ba0c5d91603cc711c648c50e7f750dc9fb0e47649b3e33191/708e471e9b4164ecd507a8814e14b36f4349e6eb4338ebbad521c5f1fe526095/probability-probability-4f7255bb14309f0470fdec0d-matrix.svg`.
- Grand Doctrine unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c30f7196f94bc96e28173ac382fe55633f999184faf94e750de70f17778751da/ec579ae6bdf988934951ea40f44bf688f24a14b5a63fea58b74e44bca2de3764/probability-probability-4f7255bb14309f0470fdec0d-unresolved.svg`.
- Track ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52efdf495de8c2e5bc69702427029dd9650d00e465ee78a10782ac905f525cde/0fed9642da6e6fcd1de44e4ec29640be7725c21f5d46633882883359c7d2a623/probability-probability-add7ca8ff5ba4172ccd0a96c-ranking.svg`.
- Track matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ada2f26501d5a6e8c9426635d06be7834fdddba229e25f35834fd5e22081d54/690b1e974416b6bd2f5e98704eab81a44bb4cbe190a73f55a1ec4855bce2f00a/probability-probability-add7ca8ff5ba4172ccd0a96c-matrix.svg`.
- Track unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d009a4eafb5a300059dedf555c58577b92e02bed1aa9308b8ff75987f970fdfa/e66e3d267864ed34c4092d0ab02c634223e9f09daa6d8a7383ad60faa8b6d92e/probability-probability-add7ca8ff5ba4172ccd0a96c-unresolved.svg`.
- Subdoctrine ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd9b109c7b82caa3c478ec43de2e49cbb7a4ed5d90d1f829f70c54069ba6b499/e5cbe50e55d6db2582b59cbc9254979244e929d6fd2d50b5a02e71b26b447e4a/probability-probability-eb7ad3a2a27e16ce73e2ae49-ranking.svg`.
- Subdoctrine matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5032e54c4b2025823da49c1e8d1ddd8782f56916a8d5cf5f3bc2c58bd0f893e3/cc4e627c42d8197b576e708d4ea1b1d9f8d28d233b7ce56a53e13a9bf57b6957/probability-probability-eb7ad3a2a27e16ce73e2ae49-matrix.svg`.
- Subdoctrine unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b6fad83455fc2aa785c8167eeeef214363ebabf9df4b8796a3d7136c5a63b3c/d2008d3f3a337a778e5df35ed2fab46d861f1545658cd9533b88dc1edc22b91a/probability-probability-eb7ad3a2a27e16ce73e2ae49-unresolved.svg`.

## 6. Threshold and sensitivity sweeps

Each sweep used the same 37-scenario hash and complete per-surface source pool, with three sweep steps, pairwise comparisons, rank-reversal detection, raw and conditional metrics, and JSON/sensitivity/threshold/unresolved outputs.

| Surface | Sweep ID | Result | Sweep points | Unresolved | Primary JSON |
| --- | --- | --- | ---: | ---: | --- |
| Domain | `probability-f1576edd8994b46631d34e50` | `PROBABILITY_ANALYZED_PARTIAL` | 222 | 5 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e000e12b302ed63ad58e4d23aad7023f38447d971c027c9e7f7b31e30d5931c/11a8b9c07965b8ad81f9f83d1ebf26834933e4dafd74ed5897fcc6593ec0dd61/probability-f1576edd8994b46631d34e50.json` |
| Grand Doctrine | `probability-dea96fc58cf60ff823acd005` | `PROBABILITY_ANALYZED_PARTIAL` | 111 | 13 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/345b69c1b94261eff2ff38bb055049f643d9f59776a9293a5323dda555d1d4ba/3d0d010978a8d0510263f3fc556510fa8f40ba0f69d41edc6b78a7816f7e7b89/probability-dea96fc58cf60ff823acd005.json` |
| Track | `probability-4d94fb72451e96c44cab2555` | `PROBABILITY_ANALYZED_PARTIAL` | 222 | 18 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/832c641a0f6f5234013498f46eff63fdec45a4d391bac3b6ad83619d279fecb7/f6478f2eaf7086eac048c3225f423c640ef916b6eff3b04b3a6b8c32f654988d/probability-4d94fb72451e96c44cab2555.json` |
| Subdoctrine | `probability-b22a4c39b67e7cf76ddfe77b` | `PROBABILITY_ANALYZED_PARTIAL` | 111 | 107 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99eea25b62fae23b5f9435ff2608bc3817c547df3d9f8a547df6283bcf9c0826/8b5460b378ab19587c5ff7716206fc58c1a6a026b965a6fa8a9c3e555b05bae9/probability-b22a4c39b67e7cf76ddfe77b.json` |

Rendered sensitivity, threshold, and unresolved evidence included:

- Domain sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6171c913505b4cd4dad95c0b9bbb99bda50931f1f3ba63125e0d8b9020a99e7/7e179b580563b36b670a1e9a19a2a8b3e635a213169492692e425fa0144a9c88/probability-probability-f1576edd8994b46631d34e50-sensitivity.svg`.
- Domain threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/5fe964160e82584e76d980cdab84eead0e9fa858d697fb668733e83268e5c9cd/probability-probability-f1576edd8994b46631d34e50-threshold.svg`.
- Domain unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2f9aa7b978700a5160d30df0c31cbf192ad6cffa149af59c7e1ea6bbf681253/aacef2952901f5664a3c94dc53b64252f0987e343c06a9130318852f33ece454/probability-probability-f1576edd8994b46631d34e50-unresolved.svg`.
- Grand Doctrine sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b098eff4f9577ebd5beb5aee32b9f77eb3c91a7a38c2c26647471d01796e61af/d813f62c8a5a304d9ccfb7cce45105e0f832a36fb16739ace34b5132b3eeb94d/probability-probability-dea96fc58cf60ff823acd005-sensitivity.svg`.
- Grand Doctrine threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/294b64854bb7f6d4cd3d3bf08e3a0b606aff47aa454a76e9badbe0d68852d409/probability-probability-dea96fc58cf60ff823acd005-threshold.svg`.
- Grand Doctrine unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c30f7196f94bc96e28173ac382fe55633f999184faf94e750de70f17778751da/80dacc0417a8c691eb1dca6597ba13a1c6fe68d1ac951c36367e0109b03dbd0e/probability-probability-dea96fc58cf60ff823acd005-unresolved.svg`.
- Track sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb3b998cdafee45f8547d445caee7b9a58907a171c524722dfc4010a4076ea8f/9eade200f0aee5b64caefe468b1119f4b999098d2f7e57d9b5915c5d6fcb2dd0/probability-probability-4d94fb72451e96c44cab2555-sensitivity.svg`.
- Track threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a6d32ffc270e06218fbe6e53b5f3d111d3f383d152a2e17fa057722f7cf35cc8/90b6c658ba0fec85fa626d429383329a22b3f9eb3bdf1e595b8d60d097e5445b/probability-probability-4d94fb72451e96c44cab2555-threshold.svg`.
- Track unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d009a4eafb5a300059dedf555c58577b92e02bed1aa9308b8ff75987f970fdfa/d523901f0e9c3765dc1e3d538cca8ae43bc64f1fbbefa639afc3fe1e244d7989/probability-probability-4d94fb72451e96c44cab2555-unresolved.svg`.
- Subdoctrine sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5f449cc2f9f604481e961024181bdfbc12d49cae1debf84f5ea3ca8aba8b91c/eb5733d363d5980be07087243e6d3564f943c9018964ed33672b44522c460ddb/probability-probability-b22a4c39b67e7cf76ddfe77b-sensitivity.svg`.
- Subdoctrine threshold: the MCP returned a threshold render for `probability-b22a4c39b67e7cf76ddfe77b`, but the cached render became stale before a stable URI could be retained.
- Subdoctrine unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b6fad83455fc2aa785c8167eeeef214363ebabf9df4b8796a3d7136c5a63b3c/683f4a246f40778af512f5bc4de6311b058a94fbbbaffdd8b36d700404882599/probability-probability-b22a4c39b67e7cf76ddfe77b-unresolved.svg`.

Because every sweep retained unresolved candidate rows, no threshold crossing, sensitivity ordering, or rank-reversal result is accepted as a balance conclusion.

## 7. Bounded simulation

The only simulation was explicitly bounded to the declared uncertain random selection input for DR-C04 and DR-E03.

Call: `hoi4.probability_simulate` with adapter `random_list`, track pool `027_doctrine_research_ai_effects.txt:322.entry.2` through `.19`, 2,000 pseudo-random samples, seed `270830`, 95% confidence, one-day horizon, raw and conditional metrics, and scenario set `DR_027_BOUNDED_RANDOM_2026_08_30` containing DR-C04 and DR-E03.

Scenario hash: `9ce1b81542d14829208544492f787094c6c78cac9aef843bac62f300858779a5`.

Result: `PROBABILITY_ANALYZED_PARTIAL`; 2 scenarios, 36 candidate rows, 18 unresolved rows, 2,000 samples, no diagnostics. This is not accepted sampled balance evidence because half of the candidate rows remained unresolved.

Artifacts:

- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5874ed61ddb3cded03c1344bb01c104be7446d91769df913d9867c14a6f5cd1/5b5fa15cb802d9338995e1baaca0ec4ef189ef99e5263ce2f60e24c5941eacea/probability-6e640061c27796a391caa947.json`.
- Ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cd3d47136928f11e66fa96edd2d110af585d79e92ff191d843ed7463c29eec7d/da8e0557bbd99b4d0b2988db69ea00c97e2e410c49fe4e2f79ff014be695518a/probability-probability-6e640061c27796a391caa947-ranking.svg`.
- Matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72075b179bef7d27849d9acd1b5e32283f6ef390a064ed6886b579fd30183748/0b952836001d9bfb11e4081b406fda094281de9f6cfc45f715951b5aa40d1d10/probability-probability-6e640061c27796a391caa947-matrix.svg`.
- Unresolved: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d009a4eafb5a300059dedf555c58577b92e02bed1aa9308b8ff75987f970fdfa/06342dd3eb43b3edec48b29aa9e50aae16dfc985a127f974bc9bf92074aa6cfd/probability-probability-6e640061c27796a391caa947-unresolved.svg`.

## 8. Baseline and final compare evidence

The required historical baseline could not be supplied to the MCP adapter. The requested baseline commit `4c5f0c928af1f8f69044e7ae4a237491ade4f8a5` is absent from the local repository, and `git log --all -- common/scripted_effects/027_doctrine_research_ai_effects.txt` has no history. The current Event 027 source files are untracked in the repository.

The following baseline attempts were rejected by the probability tool schema:

- `hoi4.probability_inspect({ source: { path: "common/scripted_effects/027_doctrine_research_ai_effects.txt", revision: "4c5f0c928af1f8f69044e7ae4a237491ade4f8a5" } })` returned `MCP error -32602: Unrecognized key: "revision" at source`.
- `hoi4.probability_compare({ before: { path: "common/scripted_effects/027_doctrine_research_ai_effects.txt", revision: "4c5f0c928af1f8f69044e7ae4a237491ade4f8a5" }, ... })` returned `MCP error -32602: Unrecognized key: "revision" at before`.
- Supplying the old probability artifact URI as `before` returned `MCP error -32602: Invalid input: expected object, received string at before`.

Current/current control compares were run with the same current source descriptor on both sides, the same full 37-scenario set, the same per-surface complete pool, and `refresh: false`. They prove only that identical inputs produce zero reported comparison changes; they are not before/after acceptance comparisons.

| Surface | Compare ID | Result | Candidate rows | Unresolved | Comparison changes | Primary JSON | Comparison evidence |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| Domain | `probability-639cd68ec61c770962b91627` | `PROBABILITY_ANALYZED_PARTIAL` | 185 | 5 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c12d5a82c7753691cf46b029de9b64d50c7c88c165eae2948e959e3f8eb7998/b3602eda4bbf3a191ff9e5529d1ba53a64abde8bd14051d0807031dd153677e5/probability-639cd68ec61c770962b91627.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/941ae299771da34fe2403a3de954d1160c98a07889ce61b2eced2c7c0beab4c9/probability-probability-639cd68ec61c770962b91627-comparison.svg` |
| Grand Doctrine | `probability-f5b04d3cf1191834dfbd863c` | `PROBABILITY_ANALYZED_PARTIAL` | 481 | 26 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af0dd0e8ddb029137a641130189641abe1dc036976816167f1c9c23d561becfb/9dd2e3ddb914618fb5c5453d8e782ba097d669e7e19ff9dfcb1001e7b31c8d6a/probability-f5b04d3cf1191834dfbd863c.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/eb397daf51f7b0d19a01979db89da49bce2b610a45bbc099f3ab3bb82f24c8cf/probability-probability-f5b04d3cf1191834dfbd863c-comparison.svg` |
| Track | `probability-6263dcf78e68649814650f8b` | `PROBABILITY_ANALYZED_PARTIAL` | 666 | 18 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/239c031769a3a39995d40f1db1bce2ff3ecff4ea431bb6b61603b72eb07c10a8/5ff62d25deb1bee0a9d4c8b1184db4f8535cfa408c38487cc8218ddbbfed90c5/probability-6263dcf78e68649814650f8b.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/d478ef38b2207a25119f7b2c05f12fbcf1d4cf2f96ea69e27f18d5466b3897d6/probability-probability-6263dcf78e68649814650f8b-comparison.svg` |
| Subdoctrine | `probability-92cdf9b80fa343714d56ddd4` | `PROBABILITY_ANALYZED_PARTIAL` | 3,959 | 107 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ea8dab67fc85dcada2ba4fdc107ab0319c014ad2878847e2adafddfad71baf8/86abfb05cd73e4ab18e32ba1be81d17a2efebf9a1e0e9ed0a4a1be0c80f999a1/probability-92cdf9b80fa343714d56ddd4.json` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/23e505046322829cdfa1d3fb6fba996321d76b0829481e679ad8a40f689edd3c/probability-probability-92cdf9b80fa343714d56ddd4-comparison.svg` |

The first full-output compare attempts for the Grand Doctrine, Track, and Subdoctrine surfaces encountered the exact MCP timeout `tool call failed for hoi4_agent_tools/hoi4.probability_compare; Caused by: timed out awaiting tools/call after 180s`. The Track and Subdoctrine compares were retried with minimal JSON/comparison/unresolved outputs and returned the partial artifacts recorded above. The timeout is retained as a tool limitation, not treated as a balance result.

## 9. Shared repeatable Event 027 and cluster picker

The shared picker was reviewed in `common/scripted_effects/chaosx_settings_effects.txt:4340+`, `common/scripted_effects/chaosx_logic_effects.txt:928-976`, `common/scripted_effects/chaosx_logic_effects.txt:311-329`, `common/on_actions/chaosx_on_actions_system.txt:154-162`, and the National Breakthroughs rows in `common/scripted_effects/chaosx_event_cluster_effects.txt`.

The source operation is a manual accumulator: it loops over active `global.all_events`, filters disabled, fired, non-repeatable, and unavailable events, calls the event weight evaluator, scales positive weights by 100, rounds them, sums them, rolls an integer from 1 through the total, and selects the first cumulative weight meeting the roll. Event 027 is registered in the global repeatable registry and cluster row 9001 is an optional National Breakthroughs member. Cooldown and cluster state are external to the source-local candidate list.

The source-only inspect call against `common/scripted_effects/chaosx_settings_effects.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason: no_weighted_surfaces`, 0 candidates, and 0 available candidates.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/81e4e7550d9d31be279052ca140dab64a7dfd297005ae03541a188760c9beb44/4cd4108b8b7ba3a72a20fd64586bb6f17cb1844ebf3483809d344dbb5f2b7689/probability-inspect-8b9bc3ba67d9.json`.

The explicit `custom_weighted_pool` inspect returned `PROBABILITY_SOURCE_INSPECTED`, 0 candidates, `poolComplete: false`, and 0 unresolved rows.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4d9f9b2258b5b3bb2e0369c4e56457b576331170de491447bf5c9abb325691e/022b493f66be64cfe9ddf6fa916828023c1cfb72911bf3e5eab1af50b1e76236/probability-inspect-8b9bc3ba67d9.json`.

The explicit `direct_random` inspect also returned no weighted surface and 0 candidates.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b9cc1225a8321b5f85ec16003aada87dea4c70145782295b3eb998aef9afacc7/ffd5353456c4954ab23833d4ebf876198653a3d13460e6cd7c08b8e69096f7e5/probability-inspect-8b9bc3ba67d9.json`.

The corresponding source inspect against `common/scripted_effects/chaosx_logic_effects.txt` returned no custom-pool candidates.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b02a7f2a3009502c8ca7c004b0622d159d7919e812d67a6642f07445fff737a/01c304e210b68a42dd94dd9276ee6a8f5bedba2979186fc4743beef4307b94a9/probability-inspect-c970c733c8f9.json`.

The cluster inspect also returned no discoverable custom pool candidates.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c25c2958b0090d82667cb7e11eff0c167b03ff0110c2e5106fec598077d9009/7b38e7a30a4fcdd18a597c2796094b98fdafc6aed8c7bb493cf65a3daf9eefd1/probability-inspect-7ed8b9859e5e.json`.

The 37-scenario custom-pool evaluation used `custom_weighted_pool`, the settings source, a 365-day horizon, raw/conditional/cumulative metrics, and JSON/ranking/matrix/timing/unresolved outputs. It returned `PROBABILITY_ANALYZED` with `analysisStatus: complete` but 0 candidates and diagnostic `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` with `candidatesFound: 0`. This is not a zero-probability result.

Analysis ID: `probability-9eb1e6c331e0ba44a287e955`.

Primary JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48a50e786f88635fb2a3d3695c15dcaa9d74bf569271d2b3d2a187675ad2fee8/f4ae0bd373037fd34c00045bf01da5c867af3620f1456ff11dc9292efe87976c/probability-9eb1e6c331e0ba44a287e955.json`.

Timing render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67b5a0ee447fe12f0e449495f6314c2e825bf12805a4c0a9037a433af0f09317/a15c429059c4c49079f04b8913fed8399b9413331309c062417d1d11831e850c/probability-probability-9eb1e6c331e0ba44a287e955-timing.svg`.

Unresolved render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d6cc34de4a6f32afd16a90b09c5631e732e81cfd45199abec74fe2209cf8029b/025d5423bc738cb5e4a1380c46ee63d1db5d54e87977b5153bd0e79bfd47c13f/probability-probability-9eb1e6c331e0ba44a287e955-unresolved.svg`.

The current/current custom-pool compare used all 37 named scenarios and a 365-day horizon. It returned `PROBABILITY_ANALYZED`, `analysisStatus: complete`, 0 candidates, 0 unresolved rows, `comparisonChanges: 0`, and the same `PROBABILITY_CANDIDATE_POOL_INCOMPLETE` diagnostic. It is not a valid before/after comparison.

Analysis ID: `probability-50c000751bb3c322676ae405`.

Primary JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/355334fefba44f8ff89325d6e1cc7cdf7bf467191f8bb8a1647bad2a188e81e2/ae99edd3477500359bbcbd6ced528b0306ddeac405a3f16cb488f627e4cba009/probability-50c000751bb3c322676ae405.json`.

Comparison render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/6f6d151312a0a13bf39e0a9d7016f8c16f7e778ecc780ad55096aa6142c98a8f/probability-probability-50c000751bb3c322676ae405-comparison.svg`.

Timing render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/67b5a0ee447fe12f0e449495f6314c2e825bf12805a4c0a9037a433af0f09317/46b817507ea3300b7a8933458a4548578cb2734f93e2823b238fcd8c19e6421a/probability-probability-50c000751bb3c322676ae405-timing.svg`.

## 10. Probability rendering and structural MCP results

The probability evaluate and sweep calls produced ranking, matrix, sensitivity, threshold, timing, and unresolved resources as recorded above. Explicit `hoi4.probability_render` calls against the older cached Grand Doctrine, Track, and Subdoctrine analyses returned `PROBABILITY_ANALYSIS_STALE` because the MCP workspace revision changed after analysis. The exact diagnostic was `Workspace sources changed after this analysis; run the analysis again before rendering`. The renderer returned JSON only and no fresh visual resources for those stale analyses. This is retained as a reproducibility/tool-state blocker, not treated as visual evidence of balance.

An immediate render after a fresh domain evaluate initially returned a partial analysis with no diagnostics and the same 37-scenario hash, but subsequent render calls again detected a changed workspace revision. The evaluate-attached domain resources listed above remain the direct rendered outputs from the successful evaluate call; no stale render is used as acceptance evidence.

The required structural Event 027 inspect call was corrected to the installed selector schema:

`hoi4.event_inspect({ selector: { kind: "event", eventId: "chaosx.nr27.1" }, mode: "lint", refresh: true, maxDepth: 5, maxNodes: 160, maxEdges: 260, workspaceId: "mod_chaos_redux_ea3b2d67c2c0" })`.

Result: `EVENT_INSPECTED_PARTIAL`, status `ok`, graph hash `97826fc586635cb6a00c040d9e2100715cf4a7b9965cac56c61ec2a499166a47`, 9,663 events, 15,064 options, 1,113 entries, 38,082 edges, 2,185 issues, 2,188 diagnostics, and 4 blocking diagnostics in the large-workspace projection. Direct Event 027 resolution was found, but the workspace emitted `MCP_INLINE_FILES_TRUNCATED` with 363 total and 64 returned files.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5e730a129cb8177c5ce1535bec69144bcbc29705bfe1cfc17144a35397f86973/2ed40e7ffc6e6b36a9e415f9804c4924ef2af86c05cd91b061cdda88663316e5/event-lint-7f40f09d5462.json`.

The corresponding Event 027 options render used `view: options`, `direction: both`, and `expandHelpers: false`. It returned `EVENT_RENDERED_PARTIAL` with validation false because large-workspace helper projections and lifecycle checks were deferred.

Render artifacts:

- Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b1acce7894572f55d74cf7ba193997e6f50ad5a66764913f53a327641ab2f59c/25ceba97b7f635faf0b0d684c2434fac3a1a3f99a5e66b52336710e966046c19/event-options-d4de198c1706-manifest.json`.
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2338d8a2bb204c7fed110981f63a7e1ca1d5d45b4965f985daf055884ae5b7e9/e7db20d859a2c016430fe2cdfdd07d64c9b3f60d9c9bc32ddbc677c0e87de379/event-options-d4de198c1706.json`.
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/270db7bf7b82b6a835fdc1d08d777a61bea69954b07ac440c9a7dc2ed068c7b9/8bdb32883f0139bfbec4a103ff642aea0c0127f0683a4e9027e8389f7e44be58/event-options-d4de198c1706.svg`.
- PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/404417bd12510ab0943ba0476d445fc1f6f52b571f094563bbfc7ecfdfa109c9/42760daa0b8d779679020cce665fced6bf589cf1bec14567a511643ddc190f49/event-options-d4de198c1706.png`.

The required technology/doctrine structural inspection was attempted with `hoi4.tech_inspect` in `scan` and `folders` modes for `land`, `naval`, `air`, and `special_forces`, and `hoi4.tech_render` for the land folder. Every call returned `SCAN_BYTE_LIMIT`, status `error`, and no graph artifact because the workspace scan exceeded the configured byte limit. No native doctrine graph, prerequisite, placement, unlock, or comparison claim is made from source-only review.

## 11. Source-level weight trace and risks

The following is score-only evidence from the current source and constants. It is not normalized probability evidence.

The shared tuning constants in `common/script_constants/027_doctrine_research_constants.txt:331-347` are base `1`, forces `2`, production `2`, war `2`, geography `2`, theater `2`, strategy `2`, completion `3`, owner readiness `3`, and continuity `2`.

`doctrine_research_ai_score_domains` in `common/scripted_effects/027_doctrine_research_effects.txt:4671+` initializes each domain to zero and applies validity gates. Army, Navy, Air, and Special Forces each have base, force, production, war, geography/coast, faction, track-availability/completion, the corresponding strategy flag, and owner-readiness contributions. Chaos has base, divisions, military production, war, plains/mountains, CBRN-viable-program readiness, and no Chaos strategy flag. The four strategy flags referenced by the domain scorer have no setter/producer found in the current source search, and no `doctrine_research_ai_strategy_chaos_warfare` flag exists.

`doctrine_research_ai_score_selected_grand` at `027_doctrine_research_ai_effects.txt:27-48` uses base, forces, production, war, geography, theater, owner readiness, and doctrine-specific force signals. It has no direct strategy or continuity factor.

`doctrine_research_ai_score_selected_track` at `027_doctrine_research_ai_effects.txt:162-191` uses base, forces, military and naval production, war, geography, faction/theater, last-transaction continuity, track-specific force signals, Special Forces readiness, and Chaos establishment readiness. It has no direct strategy factor.

Each subdoctrine scorer in `027_doctrine_research_ai_effects.txt:345-2109` gates selected domain and track plus active-incomplete or empty-valid state, then uses base, force fit, military factories, war, geography, theater, continuity, mastery-level continuity, and completion at mastery four. It has no direct strategy factor or native doctrine AI preference lookup.

The source contains a track identity risk. Army and Chaos each contribute the same four track tokens, `infantry`, `combat_support`, `armor`, and `operations`, in separate random-list rows. The triggers appear intended to gate by selected domain, but the analyzer could not prove that the token overlap cannot leak or double-count between domain families.

The source contains a subdoctrine duplication risk. The Special Forces rows at approximately lines 87-102 repeat the same eight output identities, `mountaineers_1/2`, `marines_1/2`, `paratroopers_1/2`, and `rangers_1/2`, in two separate random-list groups. Whether both rows can be simultaneously eligible is unresolved, so overrepresentation is a source-level risk rather than a measured probability finding.

The chooser initializes selected outputs to invalid state and uses a found flag. If every eligible score is zero or every candidate is invalid, the current source can leave an invalid selection. The parent caller’s zero-pool handling was not proven by the incomplete fixture and should be traced explicitly.

The shared picker multiplies weights by 100, rounds, removes scaled values below one, and performs a cumulative integer roll. Therefore a positive source weight below the scaling threshold can be excluded, and the actual normalized result depends on the complete global event list and its runtime filters. This behavior was not available as a complete MCP candidate manifest.

## 12. Findings by required audit category

| Category | Classification | Evidence and conclusion |
| --- | --- | --- |
| Score trace | Score-only | The source constants and component calls are identified above; they are not click probabilities. |
| Normalized domain probability | Unresolved | DR-A01 through DR-A06 and all other scenarios retain unresolved candidate rows. |
| Normalized Grand Doctrine probability | Unresolved | 13 unresolved rows per one-sided evaluate; no accepted ordering. |
| Normalized track probability | Unresolved | 18 unresolved rows per one-sided evaluate; no accepted ordering. |
| Normalized subdoctrine probability | Unresolved | 107 unresolved rows per one-sided evaluate; no accepted ordering. |
| Invalid-candidate zero participation | Unresolved | Trigger fixtures could not prove `has_doctrine`, native track/subdoctrine validity, DLC, CBRN, establishment, or target gates. |
| Intended ranking and rank reversal | Unresolved | Sweeps ran but retained unresolved rows; no threshold or rank-reversal conclusion is accepted. |
| Dominance and starvation | Unresolved | No complete eligible pool or normalized values were returned. Zero candidate results in the shared picker are an incomplete pool, not starvation proof. |
| Bounded randomness and repetition | Unresolved | The 2,000-sample run retained 18 unresolved rows; source-level duplicate identities and `seed = random` require a complete fixture. |
| Per-choice recalculation | Unresolved | No complete state-transition fixture proved recalculation after domain, grand doctrine, track, or subdoctrine selection. |
| Batch allocation | Unresolved | Batch fields were declared in scenarios, but no complete sequence manifest proved allocation and re-evaluation transitions. |
| Shared Event 027 timing/cooldown/recovery | Unresolved | The custom picker has no discoverable candidates and the complete global event/cluster manifest is unavailable. |
| MTTH | Not applicable to current source | No Event 027 MTTH entry was found; the current evolution cadence is a 90-day clock rather than an MTTH surface. |

## 13. Recommended owner fixes before acceptance

These are recommendations only. No fix was applied.

1. Preserve the four chooser pool boundaries in the MCP fixture or manifest and provide typed country scopes/native doctrine objects so `has_subdoctrine_in_track`, `has_doctrine`, naval-size, deployed-air, template, terrain, coast, DLC, CBRN, establishment, formation, and strategy-related triggers resolve. Re-run the same 37 scenario IDs and hash.
2. Add or document a source-owned strategy mapping and producer, especially for Chaos, Grand Doctrine, track, and subdoctrine selection. If only domain-level strategy is intended, make that boundary explicit and test it against the scenario specification.
3. Make track and subdoctrine candidate identity unambiguous, or provide MCP proof that selected-domain gates prevent Army/Chaos track overlap. Deduplicate or explicitly track-qualify the repeated Special Forces subdoctrine rows.
4. Provide a complete custom-pool manifest for `global.all_events` and the National Breakthroughs cluster containing event IDs, event type, current scaled weight, disabled/fired state, required Chaos tier, repeatability, cooldown, recovery, cap, cap reduction, cluster role/chance, removal/reset, timer cadence, and terminal states.
5. Restore or expose an exact historical baseline in an MCP-supported source object. The same 37 named scenarios, candidate pools, seeds, and external factors must be used for a real before/after compare.
6. Re-run evaluate, sweep, declared-uncertainty simulation, compare, and render after the typed fixture and baseline exist. Require exact, bounded, or sampled classifications with no unresolved candidate rows before making dominance, starvation, rank-reversal, or acceptance claims.
7. Trace all-zero domain, Grand Doctrine, track, and subdoctrine branches and the post-choice batch/branch-completion recalculation. Use a complete state-transition manifest before attempting `probability_sequence`.
8. Narrow the technology/doctrine MCP scan by folder or provide an equivalent adapter route so structural doctrine graph evidence can be obtained instead of relying on source inspection.

## 14. Skipped analyses, blockers, and remaining uncertainty

- `hoi4.probability_sequence` was not run. The required complete custom pool manifest was unavailable, including all global event candidates, runtime weights, disabled/fired state, caps, recovery, cooldowns, removals, resets, cluster membership, cadence transitions, and terminal states.
- The shared custom-pool evaluate and compare returning 0 candidates were not interpreted as zero chance, starvation, or safe exclusion. They carry `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`.
- Explicit `probability_render` calls against several cached analyses returned `PROBABILITY_ANALYSIS_STALE` because the MCP source revision changed between analysis and rendering. The stale artifacts are not used as final acceptance evidence.
- The technology and doctrine structural route returned `SCAN_BYTE_LIMIT` for all attempted folder scans and render, so native doctrine graph evidence is blocked.
- The delegated bounded probability-auditor subagent was started with the required read-only prompt but timed out and was shut down without returning a handoff. No conclusion from that subagent is used.
- Analyzer source revision and source-hash identities changed across successive read-only MCP calls even though this audit made no gameplay edits. The latest one-sided evaluations returned source hash `1cfd3c27a7bf4b57d6d28cc53f72e8e14145d47f1b01556581aae9e80cdebf27`, while the source-first inspect returned `cd052de2ad2fecb7361df11f79ea993d995bb0e5f8b7f0ba5bcd4900b0b391e4`. This reproducibility drift should be resolved or captured in the next final run.
- Because normalized named-scenario evidence, a valid baseline, and a complete shared-pool manifest are missing, the final status remains incomplete and no acceptance claim is made.

## 15. Change boundary

Only `docs/plans/027_doctrine_research_plans/subagent_handoffs/probability_final_2026-08-30.md` was created. The current untracked Event 027 gameplay sources and all pre-existing dirty repository files were preserved without modification by this audit.

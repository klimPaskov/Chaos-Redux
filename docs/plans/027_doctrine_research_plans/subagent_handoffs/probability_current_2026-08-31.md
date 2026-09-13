# Event 027 Doctrine Research current probability audit

> **Superseded status notice (2026-09-01):** This dated probability handoff is preserved as scenario-specific historical evidence and is superseded as a current status authority by ../documentation_state.md. Its artifact paths and source snapshot predate this ledger, and no acceptance conclusion is promoted from it.

Audit date: 2026-08-31.

Repository: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.

Audit mode: read-only.

Verdict: incomplete and unresolved.

The current source exposes four auditable `random_list` chooser layers. The initial identity-only fixture could not resolve the dynamic country-state expressions that produce their numeric weights, but a follow-up direct-server probe with the actual score-variable outputs did resolve the domain layer numerically. The source pools were complete at the syntax level, while the complete country-state and external-factor fixtures for the full named matrix were not yet complete. No full balance acceptance claim is justified by this run.

The direct local server is callable again. A six-scenario domain probe used the current source and the full candidate IDs `common/scripted_effects/027_doctrine_research_ai_effects.txt:19.entry.2` through `:19.entry.6`, declared the five output variables `doctrine_research_ai_score_army`, `doctrine_research_ai_score_navy`, `doctrine_research_ai_score_air`, `doctrine_research_ai_score_special_forces`, and `doctrine_research_ai_score_chaos_warfare`, and applied explicit validity overrides for the landlocked and no-candidate edge cases. It returned `PROBABILITY_ANALYZED`, `analysisId=probability-92b7288ac52f2cc38acdb23b`, `scenarioHash=7a46b362a1bfeb23974d2cc82decbc45ff9adc4834957ba91b3fb0133132b7c4`, 6 scenarios, 30 candidates, 0 unresolved rows, and 6 visual resources. Its JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a1e330c26fc053574857c0658c8b77c790bc27cc6de37d236acc8384d9c5cb38/9ab672b4462ba8869a235d0ea1a7e3e83cdaeecf2cea37bcacb8c4f50b5dfda6/probability-92b7288ac52f2cc38acdb23b.json`. This is typed scenario evidence, not live-game execution, and it does not replace the remaining B-G scenarios or the before/after comparison.

Only this handoff was written by this audit. No gameplay, localization, asset, workbook, or MCP configuration file was edited. The parent patch in `common/scripted_effects/027_doctrine_research_effects.txt` was not reverted or edited. No commit was created.

## Scope and required reading

The repository guidance in `AGENTS.md` was read before the audit.

The following local skills were read and applied:

- `.agents/skills/chaos-redux-subagents/SKILL.md` for bounded auditor ownership, read-only handoff rules, and `fork_context=false` semantics.
- `.agents/skills/chaos-redux-events/SKILL.md` for Event 027 event-chain and event-pool review.
- `.agents/skills/chaos-redux-mtth/SKILL.md` because the task is a weighted-timing and AI-weight audit, although Event 027's chooser is implemented as scored `random_list` selection rather than an MTTH block.

All files in `docs/specs/027_doctrine_research_specs/` were read as relevant Event 027 specification material:

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

The required offline wiki references were read from `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Technology modding, and Doctrine modding.

The relevant vanilla documentation was read from `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\`, including `script_concept_documentation.md`, `triggers_documentation.md`, `effects_documentation.md`, `modifiers_documentation.md`, `dynamic_variables_documentation.md`, `script_collection_input.md`, `script_collection_operator.md`, and `common\script_constants\documentation.md`.

No custom subagent was spawned because this was a bounded read-only audit against explicitly named files and scenarios. Therefore no inherited context was used, and the requested `fork_context=false` isolation rule was preserved by keeping the audit in the primary context.

## Audited source files and hashes

The following local SHA-256 values were collected from the current working tree before writing this handoff.

| File | Lines | Local SHA-256 | Audited role |
| --- | ---: | --- | --- |
| `common/scripted_effects/027_doctrine_research_ai_effects.txt` | 2113 | `6C4B7E9B776682496C2FB7ABAC627FAF22B72A56B7789FB3F38657AA733B9D39` | AI domain, Grand Doctrine, track, and subdoctrine scoring and selection. |
| `common/scripted_triggers/027_doctrine_research_triggers.txt` | 4103 | `0C88AFC1C8F51F0074ED6C6BB98CF0501219C3E0CD4F13A9E308D80FEB95669C` | Availability, validity, active-doctrine, and human/AI candidate gates. |
| `common/script_constants/027_doctrine_research_constants.txt` | 350 | `69F7412D01047D19638B49A215DB03847C8D7BADE0B68A0DADA563F8B0220C1B` | Event 027 registry and AI weight values. |
| `common/scripted_effects/027_doctrine_research_effects.txt` | 3572 | `CB5F51FB295ACFAF1815900D8ED4671528E8B27DB977FD78CB77C3E575207112` | Batch lifecycle, receipt recovery, human event flow, and AI resolution. |
| `events/027_doctrine_research.txt` | 4904 | `134FD2AEB6F1C2354D3758A46BBF13CA476FAA5567E52B2B0F4CBA09388FBEF7` | Event root and human choice pages. |
| `common/scripted_effects/chaosx_logic_effects.txt` | 1777 | `E2CEC7CD67096585A6B531D96A242C464965643459A06B14C9F459A52598F671` | Repeatable-event registration and recovery/cap logic. |
| `common/scripted_effects/chaosx_settings_effects.txt` | 5043 | `D5C6925F090843782E9C0025A1F3D41D5540513048722C5D6E5FB54091FEAA36` | Automatic event-pool weighted selection. |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | 6872 | `90AEA98CF84BA5B787DB34A0DEFC2528063F1C0F25AC8A28A07C4ACC95647247` | National Breakthroughs cluster mapping and member selection. |
| `common/script_constants/event_system_constants.txt` | 157 | `6C2AA4D003914F7B26A31261C073ABEE8014730C6097072DFE82B1E90C85CBAB` | Default event weight, recovery rate, and cap system constants. |
| `common/script_constants/event_cluster_constants.txt` | 871 | `15309AB8F095590D82CE98F85D679ADA26E31BD19892C9E2285F1D82EA402E3E` | Cluster identifiers and timing constants. |
| `docs/specs/027_doctrine_research_specs/027_doctrine_research_probability_scenarios.md` | 569 | `234B41494CB8AAA0929D88B36CB311D6F01CCC43C3E71EC48B3D49D7CFC45783` | Named scenario matrix and acceptance expectations. |

The repository HEAD during the audit was `83d385a20c9994afe3d2e1cf7d7704f5fa3c53d6`, dated `2026-08-31T15:46:34+03:00`. The four Event 027 implementation files are untracked in the working tree, so there is no committed historical AI-source snapshot that can serve as a genuine pre-patch baseline.

## MCP scenario contract

The exact scenario-set identifier reused for every fresh Event 027 AI-layer evaluation and comparison was `DR_027_FINAL_2026_08_30`.

The scenario IDs were supplied exactly as named in the specification and in the following order:

| Group | Scenario IDs | Declared focus |
| --- | --- | --- |
| A | `DR-A01`, `DR-A02`, `DR-A03`, `DR-A04`, `DR-A05`, `DR-A06` | Domain selection. |
| B | `DR-B01`, `DR-B02`, `DR-B03`, `DR-B04` | Grand Doctrine selection. |
| C | `DR-C01`, `DR-C02`, `DR-C03`, `DR-C04`, `DR-C05`, `DR-C06`, `DR-C07` | Track and branch selection. |
| D | `DR-D01`, `DR-D02`, `DR-D03`, `DR-D04`, `DR-D05`, `DR-D06` | Custom doctrine and Chaos Warfare selection. |
| E | `DR-E01`, `DR-E02`, `DR-E03`, `DR-E04`, `DR-E05`, `DR-E06` | Multi-choice and evolution sequence behavior. |
| F | `DR-F01`, `DR-F02`, `DR-F03`, `DR-F04`, `DR-F05` | Repeatable event and National Breakthroughs cluster selection. |
| G | `DR-G01`, `DR-G02`, `DR-G03` | Human parity, DLC validity, and invalid-adapter handling. |

All 37 IDs were included in each of the four AI chooser-layer `probability_evaluate` calls and each corresponding `probability_compare` call. Thus the per-layer evaluation matrix contains 37 scenarios, even though the Event-pool and cluster-specific F scenarios could not be evaluated through a complete custom-pool adapter.

The submitted scenario state for this fresh run was intentionally `state: {}` and `flags: []` for every named scenario. The prose scenario specifications do not provide a machine-readable fixture in the repository, and the current adapter schema rejected the nested `scopes`, `variables`, `externalFactors`, `setup`, `cadence`, and `terminalState` forms needed to represent those states. No country, doctrine, template, factory, fleet, air-wing, war, strategy, DLC, mastery, bank, timer, cluster, or event-weight values were invented.

Consequently, the scenario identity and candidate-pool dimensions are exact, but the runtime fixture is not engine-complete.

External-factor completeness is `false` for all four AI-layer runs.

Scheduled state changes, uncertainty declarations, cadence, and terminal-state declarations were not available to the adapter for this run.

The evaluation horizon was one day, with requested metrics `raw_value` and `conditional_probability` and JSON, ranking, matrix, and unresolved outputs. The one-day horizon did not convert the missing state into a timing result.

## Current chooser surfaces discovered

The first mandatory read-only `hoi4.probability_inspect` call used the current AI source selector `common/scripted_effects/027_doctrine_research_ai_effects.txt` and requested `doctrine_ai_will_do`. The adapter reported no direct `doctrine_ai_will_do` surface, suggested the compatible `random_list` adapter, and discovered 143 source candidate rows across four lists.

The accepted source descriptor was `{ path = "common/scripted_effects/027_doctrine_research_ai_effects.txt" }`. The initial selector-shape errors were resolved without changing source: `relativePath` is not accepted, a source string is not accepted, and an adapter-only request is rejected because the adapter requires a source.

The four current chooser layers are:

| Layer | Current source selector | Candidate pool supplied to MCP | Source candidates | MCP pool completeness | Runtime candidates in identity-only state |
| --- | --- | --- | ---: | --- | ---: |
| Domain | `common/scripted_effects/027_doctrine_research_ai_effects.txt:19` | `:19.entry.2` through `:19.entry.6`, inclusive | 5 | `true` | 0 resolved; 5 required numeric inputs. |
| Grand Doctrine | `common/scripted_effects/027_doctrine_research_ai_effects.txt:147` | `:147.entry.2` through `:147.entry.14`, inclusive | 13 | `true` | 0 resolved; 13 required numeric inputs. |
| Track | `common/scripted_effects/027_doctrine_research_ai_effects.txt:326` | `:326.entry.2` through `:326.entry.19`, inclusive | 18 | `true` | 0 resolved; 18 required numeric inputs. |
| Subdoctrine | `common/scripted_effects/027_doctrine_research_ai_effects.txt:2003` | `:2003.entry.2` through `:2003.entry.108`, inclusive | 107 | `true` | 0 resolved; 107 required numeric inputs. |

The source-level total is 143 candidates, but the four lists are not one combined selection pool. Each layer selects only within its own list.

The domain rows are Army, Navy, Air, Special Forces, and Chaos Warfare.

The Grand Doctrine rows are `new_mobile_warfare`, `superior_firepower`, `grand_battleplan`, `mass_assault`, `new_fleet_in_being`, `new_convoy_raiding`, `new_base_strike`, `new_strategic_destruction`, `new_battlefield_support`, `new_operational_integrity`, `special_forces_quantity`, `special_forces_quality`, and `chaos_warfare`.

The track rows are four Army tracks, four Navy tracks, four Air tracks, two Special Forces tracks, and four Chaos Warfare tracks. The repeated track names are deliberately domain-qualified by the source guards; the selectors above are authoritative for the complete pool.

The subdoctrine list contains the current 107 registered rows in source order, including the Army infantry, Army combat-support, Army armor, Army operations, Navy, Air, Special Forces, and Chaos Warfare registrations. The source selectors `:2003.entry.2` through `:2003.entry.108` were passed as the complete normalized candidate pool rather than a hand-picked subset.

The inspect artifacts were:

| Layer | Inspect artifact URI | Artifact SHA-256 | Analyzer source revision | Analyzer source identifier |
| --- | --- | --- | --- | --- |
| Domain | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/37d2f74bb021908e95c99ed62522ab84490c95eeb143b02126467b045d692a5e/92a132d1e05f98741ca3975448faff822e23841d06f3a3f5a63417a20660c2c3/probability-inspect-db288f956997.json` | `37d2f74bb021908e95c99ed62522ab84490c95eeb143b02126467b045d692a5e` | `50499daff1fb081d708313cc62425b79605808927187d81effc79d0ee75ddccf` | `db288f956997` artifact/source family. |
| Grand Doctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51b5f73dc11c89009476db778eacf840b095856a34576091ffe6cbf0ca8fa1d3/452f4fe39669a58ea9ec61da14bb2d9cb6ee74e830fa486355709da0575e2d72/probability-inspect-db288f956997.json` | `51b5f73dc11c89009476db778eacf840b095856a34576091ffe6cbf0ca8fa1d3` | `50499daff1fb081d708313cc62425b79605808927187d81effc79d0ee75ddccf` | `db288f956997` artifact/source family. |
| Track | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06df816d7e7e9b0fcaa2b60f8c3e9145d23707557646acbde62b181c249dbf7a/555b8e6611223866bc3b8258403f9138fec0ae212ce5f1d1de1fb14d219c58fc/probability-inspect-db288f956997.json` | `06df816d7e7e9b0fcaa2b60f8c3e9145d23707557646acbde62b181c249dbf7a` | `50499daff1fb081d708313cc62425b79605808927187d81effc79d0ee75ddccf` | `db288f956997` artifact/source family. |
| Subdoctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8b5be4c3fe238aaef1e55bfe83c4a3c8e0bf2936b934ad62a2517fa112b38e8e/b4a67c80638073a0245b12ae8f4b9c71ea14fd8620bd86adb7b0ba7ba32253d5/probability-inspect-db288f956997.json` | `8b5be4c3fe238aaef1e55bfe83c4a3c8e0bf2936b934ad62a2517fa112b38e8e` | `d75ea0a72a6ef5d05967f63a461a063cb230464dd4c1d92b877ef9a1b8e305fb` | `db288f956997` artifact/source family. |

The inspect model identifies `random_list` selection as `proportional_categorical`, with raw-score and normalized-probability capabilities enabled, complete-pool-required set to `true`, and timing and sequence capabilities unavailable for this adapter.

## Fresh probability evaluations

The following four evaluations used the same 37-scenario set, the same current source path, the same exact per-layer candidate pool, and the same identity-only state payload.

| Layer | Analysis ID | Scenario hash | Scenario count | Candidate rows | Unresolved rows | Diagnostics | Classification |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| Domain | `probability-41f58a186a7d5e7a792abe5a` | `b432a2ef233975b7c7536a278d4860edfd48fe599b6541fbdc997f95626ceafb` | 37 | 185 | 5 | 0 | Partial and unresolved. |
| Grand Doctrine | `probability-9216ad24fcd703de1e91f636` | `b432a2ef233975b7c7536a278d4860edfd48fe599b6541fbdc997f95626ceafb` | 37 | 481 | 13 | 0 | Partial and unresolved. |
| Track | `probability-689cb81df2925c9376353122` | `b432a2ef233975b7c7536a278d4860edfd48fe599b6541fbdc997f95626ceafb` | 37 | 666 | 18 | 0 | Partial and unresolved. |
| Subdoctrine | `probability-d701b05755f038cd8013b371` | `b432a2ef233975b7c7536a278d4860edfd48fe599b6541fbdc997f95626ceafb` | 37 | 3959 | 107 | 0 | Partial and unresolved. |

The JSON artifacts were:

| Layer | Evaluation artifact URI | Artifact SHA-256 | Analyzer source revision | Analyzer source identifier |
| --- | --- | --- | --- | --- |
| Domain | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bc3f57a7c43adc218fa166e0a7ced8ca96362705c10df14ac6267f5734e13833/591d76b255f44554efe3e18fefd782692ab507110915fa5d413a8b8899311e2a/probability-41f58a186a7d5e7a792abe5a.json` | `bc3f57a7c43adc218fa166e0a7ced8ca96362705c10df14ac6267f5734e13833` | `d75ea0a72a6ef5d05967f63a461a063cb230464dd4c1d92b877ef9a1b8e305fb` | `db288f956997` artifact/source family. |
| Grand Doctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a42b66ae6cf3e3bb7b7ff8b9b5abe9081d2342a7a58efcc784797bdf9fe135e/e5c8f0ce9409bba35ce5862ea11927ce6e1dd73cec011773a95a70722e205b48/probability-9216ad24fcd703de1e91f636.json` | `3a42b66ae6cf3e3bb7b7ff8b9b5abe9081d2342a7a58efcc784797bdf9fe135e` | `b3b99bd0bc7b7ef6e631d886616d331bba32eb33ba47102a3e1881e2798adc03` | `db288f956997` artifact/source family. |
| Track | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c0063f897e21fb2ca64e8071435b7621076551e578e25716f494236bde53b5f/bad5d104aac750bbf73d800343d75a03b53d519c4def18a709ca47ff206e62f0/probability-689cb81df2925c9376353122.json` | `0c0063f897e21fb2ca64e8071435b7621076551e578e25716f494236bde53b5f` | `b3b99bd0bc7b7ef6e631d886616d331bba32eb33ba47102a3e1881e2798adc03` | `db288f956997` artifact/source family. |
| Subdoctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3234ef963d16132a65c650a78a0e935b14ecb4c24ed0ad603629be7370f0de7/ae94ab9f44fbf0b96099baa7405166772025ee17c27b38e5349fe5a2042c85bc/probability-d701b05755f038cd8013b371.json` | `f3234ef963d16132a65c650a78a0e935b14ecb4c24ed0ad603629be7370f0de7` | `68f177e1441ffb80a0d7d9e6d0ebd97f75f9339b69216059eaaca8835bc570ff` | `db288f956997` artifact/source family. |

The domain evaluation's representative diagnostic was `VALUE_UNRESOLVED` for the five dynamic score expressions `doctrine_research_ai_score_army`, `doctrine_research_ai_score_navy`, `doctrine_research_ai_score_air`, `doctrine_research_ai_score_special_forces`, and `doctrine_research_ai_score_chaos_warfare`. The one-scenario probe used analysis ID `probability-5896272654469c03e4762e2b`, scenario hash `c47bed41905c24d325245f5df66461f3687075d42c6e73cc1f9df0e20a30dee5`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6526fba8faf686bea332bf76f3c975db50ce8e5c7f2b046d8be2c64953be17a5/269c096722bef2e0364080f2e2c3a1f12646040224a52fe35f00e2768f85f250/probability-5896272654469c03e4762e2b.json` with artifact SHA-256 `6526fba8faf686bea332bf76f3c975db50ce8e5c7f2b046d8be2c64953be17a5`.

The Grand Doctrine, track, and subdoctrine rows likewise remained unresolved at their dynamic score expressions, producing 13, 18, and 107 unresolved candidate rows respectively. Their `conditionalProbability`, `pathProbability`, and rank fields were null rather than numeric.

The adapter did not report these unresolved candidates as zero-weight candidates. The zero `availableCandidates` value in inspection means that no typed runtime fixture resolved, not that the choices were proven impossible or starved.

## Fresh current-source comparisons

The four comparison calls used identical current source descriptors for `before` and `after`, the same source selector, the same complete per-layer pool, the same 37 IDs, and the same scenario hash `b432a2ef233975b7c7536a278d4860edfd48fe599b6541fbdc997f95626ceafb`.

These are current/current controls, not historical pre-patch versus post-patch comparisons. The AI source is untracked and no genuine prior AI-source snapshot was available. The parent receipt-recovery change is in the effects file and is outside the AI source selector used by these probability adapters.

| Layer | Comparison/analysis ID | Candidate rows | Unresolved rows | Reported changes | Classification |
| --- | --- | ---: | ---: | ---: | --- |
| Domain | `probability-bc170ef548943d5dd5d5119a` | 185 | 5 | 0 | Current/current control only. |
| Grand Doctrine | `probability-2fffe74e91060934f135b380` | 481 | 13 | 0 | Current/current control only. |
| Track | `probability-301bb386da92a5c5ac726a5c` | 666 | 18 | 0 | Current/current control only. |
| Subdoctrine | `probability-2d586988355ddfe64b89fa6a` | 3959 | 107 | 0 | Current/current control only. |

The comparison JSON artifacts were:

| Layer | Comparison artifact URI | Artifact SHA-256 | Analyzer source revision |
| --- | --- | --- | --- |
| Domain | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/729acdc245917e46efee1901726ca4e9e3bbff8c6c1eaa180e9dc3093f505045/0988906abf42508495969ad02c194c039ee3634d74cc5da535b87ee06ba3f28b/probability-bc170ef548943d5dd5d5119a.json` | `729acdc245917e46efee1901726ca4e9e3bbff8c6c1eaa180e9dc3093f505045` | `c45c484235dce6745ed0187993da7dcff2ad5b8262a3ca5613db15099cca4ac0` |
| Grand Doctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efc22dbbeb76e6f3b162bd21bc89ac9f7631e665521c42eea68f08ff718d153c/f4696d6e295c28932782d681ec11efc2d756ebcca0bc0925f790064d3bfb650b/probability-2fffe74e91060934f135b380.json` | `efc22dbbeb76e6f3b162bd21bc89ac9f7631e665521c42eea68f08ff718d153c` | `cb6440868ed11ff295da7b93efc00ce57bbb1e0443679cc67b124418352af622` |
| Track | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2a31c21a9e3582f1cfcdc5838542ab99f6c74438c95f4136675fc185c1ee091a/ec000d22bf225a73525eed9dd6539728884be41f24e5b317cf572c4b6fafe88d/probability-301bb386da92a5c5ac726a5c.json` | `2a31c21a9e3582f1cfcdc5838542ab99f6c74438c95f4136675fc185c1ee091a` | `cb6440868ed11ff295da7b93efc00ce57bbb1e0443679cc67b124418352af622` |
| Subdoctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f246a7e35e2acc728e0cbee2fbc2b918e1a3f73223047dc0dd9ecc0dc2a33995/5c33ba60f74702b96aa4da9c7dcefbb336e03edcb1f87b45878a8b5b8b306346/probability-2d586988355ddfe64b89fa6a.json` | `f246a7e35e2acc728e0cbee2fbc2b918e1a3f73223047dc0dd9ecc0dc2a33995` | `68e9a8e8a69f61fa00aa8740eee0411233e9c938c992cfd97bdf4616cb903c9e` |

No comparison result demonstrates that the parent effects-file patch changed AI doctrine probabilities, because the compared source was unchanged on both sides and the adapter never resolved numeric scores.

## Rendered evidence and render blocker

The evaluate calls automatically produced ranking, matrix, and unresolved views for all four layers.

| Layer | Ranking URI | Matrix URI | Unresolved URI |
| --- | --- | --- | --- |
| Domain | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29b98e7ae05512f7703007ec4f2f01a08ea43f83d6d81f8b21ee1826fcb0e67a/752bf3a5d00494f9328a3ace685fc099ce0c776d13d294ed98b3da4cccd99149/probability-probability-41f58a186a7d5e7a792abe5a-ranking.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f1610276a68a68a71318eec2c2df918bd012b8292611bdf7d78b0d4aeef65f2/9cd9ff3136774fb80b83c085951e43d0a9186dac9eff396ccfe7f80c73af2017/probability-probability-41f58a186a7d5e7a792abe5a-matrix.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2f9aa7b978700a5160d30df0c31cbf192ad6cffa149af59c7e1ea6bbf681253/c8ad397d880610d954ce6c94d586f7a3cad38f7d2c1a81171dc89174ee9b28d1/probability-probability-41f58a186a7d5e7a792abe5a-unresolved.svg` |
| Grand Doctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b8eca4677c6e9b4dc6ec5bbbe0a7896f357ffaef9012d2dca523c56fbe2b293/e0d69610ae1f84e9d12a5bebb30b33d190da96d1460a06944662f3582922d444/probability-probability-9216ad24fcd703de1e91f636-ranking.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8fe8ebb6baac726c1c425f34d2fd51ede8a84b707e050310e4e8b08cf9928b7/658b5cd373ad3c284240804c68d74cb9cb8d4be28d905db9e9fb4e466579c528/probability-probability-9216ad24fcd703de1e91f636-matrix.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c30f7196f94bc96e28173ac382fe55633f999184faf94e750de70f17778751da/4c9915924dde9e3f92b7f4336301965385bc3dbd7a66f686b72584741370e3bc/probability-probability-9216ad24fcd703de1e91f636-unresolved.svg` |
| Track | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1b342d961ae690c4ad68dd1abe56a27476594ee39b4962d6ebd5365bcf60779b/98fd5dbcf92833d3d43d6e733e0a9de757240e182d7d5bf5780a71caa68c9128/probability-probability-689cb81df2925c9376353122-ranking.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77c92c8c8b37b22d0aa50aebd7c9a95acd05cd2c7429247cf5c73a6d42174ecb/b158a709a2f9c546b782d3f495806a468465c9a7dd6e0f6b85feb641a4723699/probability-probability-689cb81df2925c9376353122-matrix.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d009a4eafb5a300059dedf555c58577b92e02bed1aa9308b8ff75987f970fdfa/db8c429a352986dee03b5ee2056841ce92512c535b56560afa18c2e8280df225/probability-probability-689cb81df2925c9376353122-unresolved.svg` |
| Subdoctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c11bfc15221e887243c3c98e89d7fbb78319a5308cf727b5ff334001de4a9fe/12335356ae87fc994c5d57e42dd1194e345e6ada1882f8165075c99c624c6f66/probability-probability-d701b05755f038cd8013b371-ranking.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2193afe24595e2691a41cb2fa2b54d84eadc890c43200a042fcc0fb60dda2366/9e12b5367bfb3a262f5673adac31ceaa1000fec9369f1ad645e0ebd71e9d9c88/probability-probability-d701b05755f038cd8013b371-matrix.svg` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b6fad83455fc2aa785c8167eeeef214363ebabf9df4b8796a3d7136c5a63b3c/74c939ebb491a7eca608bd5e7d5138135d35f1ba1e4c3dbaf81ca2f8fa185b7a/probability-probability-d701b05755f038cd8013b371-unresolved.svg` |

Explicit `hoi4.probability_render` calls were made for all eight analysis IDs with the common expected scenario hash `b432a2ef233975b7c7536a278d4860edfd48fe599b6541fbdc997f95626ceafb`. Every call returned `PROBABILITY_ANALYSIS_STALE` with the diagnostic `Workspace sources changed after this analysis; run the analysis again before rendering`, status `ok`, and zero fresh visual resources. The automatically emitted evaluation views above are retained as analysis-time evidence, but they are not a fresh post-revision render.

The current-source refresh inspect attempted after the render pass also failed with the exact error `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect` followed by `Caused by: Transport closed`.

## Comparison render artifacts

The comparison calls automatically produced comparison views before the stale-render refresh attempt.

| Layer | Comparison SVG URI | Artifact family/hash prefix |
| --- | --- | --- |
| Domain | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/908991469b3d27f47dd211db1c1601066aa435f030a18dd2ac4881ff1decdfc4/probability-probability-bc170ef548943d5dd5d5119a-comparison.svg` | `2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49` |
| Grand Doctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/cc40841fe32cefbbccd02ab1c14e5ecd348218e62bc042449966b9cd6ab1065c/probability-probability-2fffe74e91060934f135b380-comparison.svg` | `2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49` |
| Track | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/9ae3bf519a730d4539c6a016b7c89d0c1765fb1214b713b8db9bddcd8429a75a/probability-probability-301bb386da92a5c5ac726a5c-comparison.svg` | `2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49` |
| Subdoctrine | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/f2c3adf96a9f071cf168317093c31519abdaa92449365c39513ad28bf84c43c3/probability-probability-2d586988355ddfe64b89fa6a-comparison.svg` | `2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49` |

## Scenario-by-scenario result matrix

The matrix below names every required scenario and records the current evidence state. `Unresolved` means the named scenario was submitted to the four AI-layer evaluators and controls, but the analyzer could not resolve the typed runtime state needed to decide its expected ordering or validity.

| Scenario IDs | Specification intent | Current MCP result |
| --- | --- | --- |
| `DR-A01` | Doctrine-less land major should rank Army above Air above Navy. | Unresolved; no numeric domain scores. |
| `DR-A02` | Island naval power should let Navy compete strongly or lead over Army. | Unresolved; no numeric domain scores. |
| `DR-A03` | Air-centered continental power should let Air lead or compete with a near-complete Army branch. | Unresolved; no numeric domain scores. |
| `DR-A04` | Landlocked minor should make Army lead and Navy invalid or near zero. | Unresolved numerically; source-only gate risk is recorded below. |
| `DR-A05` | Credible future maritime plan should raise Navy without making it unconditional. | Unresolved; no typed strategy-plan factors. |
| `DR-A06` | Complete ordinary domains should yield no candidate and close the batch without fallback. | Unresolved; no typed completion state. |
| `DR-B01` | Mobile armored army should rank a mobile or armored Grand Doctrine above infantry or static alternatives. | Unresolved; no numeric Grand Doctrine scores. |
| `DR-B02` | Manpower-rich infantry state should raise infantry, mass, defensive, or irregular alternatives. | Unresolved; no numeric Grand Doctrine scores. |
| `DR-B03` | Historical plan and force-composition conflict should be evaluated under both plans. | Unresolved; no typed plan-factor pair. |
| `DR-B04` | DLC-, country-, or action-invalid Grand Doctrine should have zero participation. | Unresolved; invalidity not bound to a typed country fixture. |
| `DR-C01` | Near-complete relevant armor branch should lead through completion and force fit. | Unresolved; no numeric track scores. |
| `DR-C02` | Near-complete irrelevant naval branch should lose to a relevant land branch. | Unresolved; no numeric track scores. |
| `DR-C03` | An empty operations or logistics branch should compete under severe supply problems. | Unresolved; no typed supply state or numeric track scores. |
| `DR-C04` | Four equal tracks should show bounded variation rather than a fixed winner. | Unresolved; no numeric track weights and no fresh simulation. |
| `DR-C05` | One dominant track should stack choices, finish, then recalculate. | Unresolved; no numeric track weights or sequence state. |
| `DR-C06` | A branch completed between choices must leave the second choice pool. | Unresolved; no native completion transition. |
| `DR-C07` | Banked mastery on an empty track should preserve banked progress and follow AI fit. | Unresolved; no banked-mastery or native-sequence fixture. |
| `DR-D01` | CBRN-ready country should let Chaos Warfare compete strongly or lead. | Unresolved; no typed CBRN owner state. |
| `DR-D02` | CBRN-unready country should exclude Chaos Warfare. | Unresolved; no typed establishment state. |
| `DR-D03` | Active Chaos Warfare with infantry formations should favor Hazard Assault Formations. | Unresolved; no numeric Chaos track scores. |
| `DR-D04` | Strong CBRN headquarters and contamination threat should favor Integrated CBRN Command. | Unresolved; no numeric Chaos track scores. |
| `DR-D05` | Special country without a coherent adapter should produce no fabricated doctrine reward. | Unresolved; adapter injection and country identity were not bound. |
| `DR-D06` | Special country with a valid owner-defined adapter should participate. | Unresolved; custom adapter was not supplied to the MCP fixture. |
| `DR-E01` | Two-choice Evolution I batch may adopt a Grand Doctrine, then select or advance a track. | Unresolved; sequence adapter was not used without complete state. |
| `DR-E02` | Three-choice mixed-services batch should recalculate after Navy adoption. | Unresolved; no typed queue and strategy state. |
| `DR-E03` | Four-choice broad curriculum should vary across close-score tracks. | Unresolved; no numeric weights and no fresh simulation. |
| `DR-E04` | Five-choice clear-fit branch should be able to complete. | Unresolved; no numeric weights or completion transition. |
| `DR-E05` | A queued three-choice Evolution II batch must not merge with an active one-choice batch. | Unresolved; queue state not supplied. |
| `DR-E06` | Evolution unlock during a batch must affect the next firing, not the active batch. | Unresolved; unlock timing not supplied. |
| `DR-F01` | Initial complete repeatable-event pool should report Event 027's normalized chance and ranking. | Unresolved; custom event pool adapter discovered no candidates. |
| `DR-F02` | After first firing, Event 027 should show bounded recovery and a lower cap. | Unresolved; custom event pool state and cadence absent. |
| `DR-F03` | Four-firing sequence should test recurrence, starvation, resets, caps, and cluster behavior. | Unresolved; sequence contract requires a complete pool manifest. |
| `DR-F04` | Optional National Breakthroughs participation should have bounded cluster-size behavior. | Unresolved; current source registers Event 027 as required, and no complete cluster pool was supplied. |
| `DR-F05` | A selected Event 027 cluster member should fire once without optional duplicate fanout. | Unresolved; cluster roll and member-state fixture absent. |
| `DR-G01` | Human-visible valid actions and AI candidates should be identical. | Unresolved; human/AI parity graph was not bound to a typed country. |
| `DR-G02` | DLC combinations should exclude unavailable content while preserving valid graph order. | Unresolved; no DLC matrix fixture. |
| `DR-G03` | Invalid adapter identity or mastery should fail closed without poisoning other domains. | Unresolved; invalid adapter was not injected into the adapter. |

No row in this table should be interpreted as a measured zero or as acceptance of the declared ordering.

## Source score and modifier trace

The current constants file defines the following additive values in `doctrine_research_ai_weight` at `common/script_constants/027_doctrine_research_constants.txt`:

| Weight key | Value |
| --- | ---: |
| `base` | 1 |
| `forces` | 2 |
| `production` | 2 |
| `war` | 2 |
| `geography` | 2 |
| `theater` | 2 |
| `strategy` | 2 |
| `completion` | 3 |
| `owner_readiness` | 3 |
| `continuity` | 2 |

At `common/scripted_effects/027_doctrine_research_effects.txt:3421`, every domain score starts at zero and is populated only when its `*_has_valid_action` trigger succeeds.

The ordinary Army, Navy, Air, and Special Forces domain branches add `base`, live force, production, war, geography, faction theater, completion, strategy, and an unconditional `owner_readiness` value when the domain is valid.

The Chaos Warfare branch adds `base`, live divisions, military production, war, plains or mountains geography, faction theater, completion, strategy, and `owner_readiness` only when `cbrn_chaos_warfare_ai_has_viable_program` succeeds.

At `common/scripted_effects/027_doctrine_research_ai_effects.txt:29`, Grand Doctrine candidates add the shared base and context factors, the selected-domain strategy signal, domain adoption readiness, and branch-specific force-fit bonuses.

At `common/scripted_effects/027_doctrine_research_ai_effects.txt:165`, track candidates add the shared context factors, strategy, same-domain-and-track continuity, and track-specific force-fit bonuses.

At `common/scripted_effects/027_doctrine_research_ai_effects.txt:349`, subdoctrine candidates repeat the context factors, add same-track continuity when the current transaction or native mastery level exists, and add completion value near the configured level threshold.

The numeric source trace is therefore additive score evidence only. Because all dynamic score effects were unresolved in the MCP evaluations, no candidate's numeric total or normalized probability was available.

## Selection semantics and sequence observations

The four AI chooser blocks use `random_list` with `seed = random` at lines 19, 147, 326, and 2003 of `027_doctrine_research_ai_effects.txt`.

The adapter identifies this operation as proportional categorical selection over the complete positive candidate pool. It is not a score race, a max-score click, or a human click probability.

The AI code initializes each candidate weight to zero, checks its validity, computes a score, stores the score, and submits all candidate weights to the corresponding `random_list`.

The AI resolver in `common/scripted_effects/027_doctrine_research_effects.txt:3504` clears and reselects after successful transactions. The loop has a configured `max_batch_choices` guard and increments its guard only after a successful transaction, while adoption-only outcomes clear the selection and continue. This is favorable structural evidence for recalculation, but the required typed multi-choice sequence was not analyzable by the probability adapter.

The source-level structure prevents an invalid candidate from being selected when its validity trigger is false by leaving its stored weight at zero. The MCP could not prove which candidates were valid in the named scenarios because the state fixture was empty.

## Findings and risks

### Finding 1: Navy and Air adoption gates are broader than DR-A04's intended validity boundary

At `common/scripted_triggers/027_doctrine_research_triggers.txt:133-143`, `doctrine_research_army_adoption_available`, `doctrine_research_navy_adoption_available`, and `doctrine_research_air_adoption_available` are respectively a no-existing-doctrine check plus `always = yes`.

The Navy adoption trigger does not require coastline, dockyards, fleet, naval production, or a naval plan.

The Air adoption trigger does not require aircraft, air wings, air production, or an air plan.

The domain scorer then adds `owner_readiness = 3` unconditionally for any valid ordinary Army, Navy, or Air domain at `027_doctrine_research_effects.txt:3427-3459`.

This is a source-only risk that matches the DR-A04 failure signal: a landlocked minor with no fleet can still receive a positive Navy domain score if the Navy domain is considered valid. The MCP did not resolve DR-A04's state, so the audit does not claim a measured Navy probability or a proven invalid-candidate selection.

Recommended owner review: decide whether Navy and Air should remain universally adoptable, or add a narrow capability or credible-plan gate to the corresponding adoption triggers and score branch. Any change must be followed by the same named-scenario baseline and compare pass.

### Finding 2: Invalid-candidate zero behavior is structurally present but not MCP-proven

Grand Doctrine, track, and subdoctrine chooser rows are guarded by `doctrine_research_selected_grand_doctrine_is_valid`, active-doctrine and domain checks, track-action availability, and selected subdoctrine validity checks.

The source initializes weights to zero before each validity test.

The adapter reported unresolved dynamic values rather than numeric zero values, so DR-B04, DR-D02, DR-D05, DR-D06, DR-G02, and DR-G03 remain unresolved for engine behavior.

### Finding 3: No measured dominance, starvation, rank reversal, repetition, or exploit conclusion

The evaluator returned no numeric ranks or probabilities for any layer.

The current/current comparisons returned zero reported changes, but this is expected for identical source selectors and is not evidence that unrelated scenarios are balanced.

No domain, Grand Doctrine, track, or subdoctrine can be called dominant or starved from this run.

No repetition or snowball rate can be claimed for multi-choice batches because the sequence state and numeric weights were unresolved.

### Finding 4: Event 027's repeatable-event surface is outside the available custom-pool adapter

`common/scripted_effects/chaosx_logic_effects.txt:325` registers Event 027 through `constant:doctrine_research_event.id` in `global.repeatable_events`.

`common/script_constants/event_system_constants.txt:39-42` defines default event weight 1000, major-event gain 150, cap reduction factor 0.5, and recovery rate 20.

`initialize_event_weights` in `chaosx_logic_effects.txt:402-414` initializes event weights and caps from the default event weight.

`update_repeatable_event_weights` at `chaosx_logic_effects.txt:1118-1183` restores eligible repeatable events from the inactive floor, adds the configured recovery rate, and caps the result at the event-specific cap.

`reduce_repeatable_event_cap` at approximately `chaosx_logic_effects.txt:1280-1290` halves the event cap after firing and resets the event weight to the inactive floor.

`select_weighted_random_event_id` at `chaosx_settings_effects.txt:4394-4475` scans `global.all_events`, removes invalid or zero-weight candidates, scales each candidate weight, sums the valid pool, rolls an integer from 1 through the total, and selects the first cumulative threshold crossing.

The three custom-pool inspections for `chaosx_settings_effects.txt`, `chaosx_logic_effects.txt`, and `chaosx_event_cluster_effects.txt` all reported incomplete pools with zero candidates and zero unresolved rows, so the absence of candidates is an adapter coverage result, not proof that the runtime pool is empty.

The custom-pool inspect artifacts were:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6125553558d61fa628047e2bfb0c3610dec4109074d189e04818d33150bc34b0/de04cff14ed071575ff17d575b5a70e9ca07ec5d5773e3fcec466297548450c7/probability-inspect-f12c120215a.json`, SHA-256 `6125553558d61fa628047e2bfb0c3610dec4109074d189e04818d33150bc34b0`, source revision `afcd1675a76b39d4e0c78b34ab904873d59f76b2a1e8c5970c597c19c4ced423`, for `chaosx_settings_effects.txt`.
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5193e10b8051071e2aaf71c64c8a9afeae044561640fd5c6d87f04be0d066965/9301f6635c9fd9ddfb523bc7851bf6ce17e1a5a5a232d79a8f3c81230a11b185/probability-inspect-e487789ee3eb.json`, SHA-256 `5193e10b8051071e2aaf71c64c8a9afeae044561640fd5c6d87f04be0d066965`, source revision `d2c355b57eb37c8ed19bd5a1832de9d59737cd4dcbaaebb0adec889ff28b8fb3`, for `chaosx_logic_effects.txt`.
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/15c29ca42075e2484fa77f364ef7de992a8c2d69c4b345280485a66a385d1c21/0d5ae83d075226841cbecbfef3569bf759307d64e113967151a7641c3eb6828f/probability-inspect-11eedf453a15.json`, SHA-256 `15c29ca42075e2484fa77f364ef7de992a8c2d69c4b345280485a66a385d1c21`, source revision `d2c355b57eb37c8ed19bd5a1832de9d59737cd4dcbaaebb0adec889ff28b8fb3`, for `chaosx_event_cluster_effects.txt`.

### Finding 5: Current cluster role conflicts with the F04 wording

`common/scripted_effects/chaosx_event_cluster_effects.txt:836-841` maps Event 027 to the National Breakthroughs cluster.

The National Breakthroughs member definition at approximately `chaosx_event_cluster_effects.txt:1830-1885` registers Event 027 with `event_cluster_member_role.required`.

DR-F04 describes Event 027 as an optional cluster member. The current source therefore has a specification/source mismatch that requires owner resolution before optional-participation probability can be assessed.

### Finding 6: Structural event evidence is partial and doctrine structural evidence is blocked

The accepted event inspector selector was `{ kind = "event", eventId = "chaosx.nr27.1" }`.

The accepted file-level event inspector selector was `{ kind = "file", sourcePath = "events/027_doctrine_research.txt" }`.

The root event at `events/027_doctrine_research.txt:10-20` is `chaosx.nr27.1`, hidden, triggered only, and immediately calls `doctrine_research_fire_global_batch`.

The accepted event inspection artifact for the file selector was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69e41710552a6e006bcbc489293bd53d5193ee1f1fc78c923e926554c5b1fad0/9872f8ff51056fa0951773802f718b30b9ce6af0f25efb42902896f0217d8e97/event-lint-2725045f62d1.json` with SHA-256 `69e41710552a6e006bcbc489293bd53d5193ee1f1fc78c923e926554c5b1fad0`, revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`, and graph hash `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`.

The accepted event-ID inspection artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5867f6197c76fe50d27306226a28afb834b097c2957b0cabc272c9041c59adca/4a160822d98b29642803453f261b399f551d9b161a8e6c516a52b96827c910fc/event-lint-2725045f62d1.json` with SHA-256 `5867f6197c76fe50d27306226a28afb834b097c2957b0cabc272c9041c59adca` and the same revision and graph hash.

The event inspector returned `EVENT_INSPECTED_PARTIAL` with 9722 events, 15150 options, 1133 entries, 30284 state accesses, 38320 edges, 2206 issues, and one blocking diagnostic because workspace-wide helper projections and lifecycle passes were deferred by the large scan.

The narrower event state-flow inspection timed out after 180 seconds with `timed out awaiting tools/call after 180s`.

The required `hoi4.event_render` call then failed with `tool call error: tool call failed for hoi4_agent_tools/hoi4.event_render` followed by `Caused by: Transport closed`.

The required `hoi4.tech_inspect` calls for the doctrine surface failed with `tool call error: tool call failed for hoi4_agent_tools/hoi4.tech_inspect` followed by `Caused by: Transport closed`, so no current doctrine structural artifact or technology render is claimed.

## Required comparison-report summary

| Surface | Baseline scenario IDs | Patched scenario IDs | Evidence type | Pool completeness | Intended ordering met | Remaining uncertainty |
| --- | --- | --- | --- | --- | --- | --- |
| Domain `random_list` | `DR-A01` through `DR-G03` | `DR-A01` through `DR-G03` | Fresh current-source evaluation plus current/current control compare. | Source pool complete at 5 rows; runtime and external factors incomplete. | Unresolved. | Five domain scores unresolved; no rank or probability. |
| Grand Doctrine `random_list` | `DR-A01` through `DR-G03` | `DR-A01` through `DR-G03` | Fresh current-source evaluation plus current/current control compare. | Source pool complete at 13 rows; runtime and external factors incomplete. | Unresolved. | Thirteen Grand Doctrine scores unresolved; no rank or probability. |
| Track `random_list` | `DR-A01` through `DR-G03` | `DR-A01` through `DR-G03` | Fresh current-source evaluation plus current/current control compare. | Source pool complete at 18 rows; runtime and external factors incomplete. | Unresolved. | Eighteen track scores unresolved; no rank or sequence result. |
| Subdoctrine `random_list` | `DR-A01` through `DR-G03` | `DR-A01` through `DR-G03` | Fresh current-source evaluation plus current/current control compare. | Source pool complete at 107 rows; runtime and external factors incomplete. | Unresolved. | 107 subdoctrine scores unresolved; no rank or probability. |
| Automatic repeatable-event pool | `DR-F01` through `DR-F05` | `DR-F01` through `DR-F05` | Source inspection only; custom-pool adapter discovery. | Incomplete; 0 candidates discovered. | Unresolved. | Complete `global.all_events` pool, per-event weights, active gates, recovery cadence, caps, and resets unavailable to adapter. |
| National Breakthroughs cluster | `DR-F04`, `DR-F05` | `DR-F04`, `DR-F05` | Event/cluster source inspection only. | Incomplete; Event 027 mapping visible, full cluster probability pool unavailable. | Unresolved. | Event 027 is currently `required` in source while F04 describes optional participation. |

The word “baseline” in this table means the fresh current-source evaluation requested by the parent, not a historical source snapshot. The word “patched” means the identical current-source control side of the compare. No true before/after source delta exists for the untracked AI source.

## Skipped analyses and exact blockers

### Probability sweep

The required domain sweep was attempted with the current AI source, all five domain candidate selectors, all 37 named scenarios, and sweep paths `num_divisions`, `num_of_military_factories`, `num_of_naval_factories`, and `has_war`, with three steps and pairwise/rank-reversal requests.

The call failed before producing an artifact with the exact error `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_sweep` followed by `Caused by: Transport closed`.

No threshold, sensitivity, or rank-reversal conclusion is claimed.

No typed numeric ranges were substituted after the transport failure.

### Probability simulation

No fresh `hoi4.probability_simulate` run was made because the explicit simulation scenarios DR-C04 and DR-E03 require a complete four-track state with numeric score inputs, and the current fixture only contained empty state and flags.

The earlier repository handoff's sampled artifact is not reused as current evidence because it predates this current-source audit and did not resolve the same fixture gap.

### Probability sequence

No `hoi4.probability_sequence` run was made because the complete repeatable event pool, cluster member pool, cadence, recovery, cap, removal, reset, and terminal-state contract were not available to the adapter.

### Explicit probability render refresh

All eight explicit `hoi4.probability_render` calls returned the stale-analysis diagnostic recorded above.

The automatic evaluator and comparator render artifacts are preserved, but a new source revision must be analyzed before they can be refreshed through the render endpoint.

### Event and doctrine structural renders

Event state-flow inspection timed out, event render hit transport closure, and technology/doctrine inspection hit transport closure. No source-only structural conclusion is used as a replacement for those missing MCP artifacts.

## Recommended owner follow-up without applying changes

1. Decide and document the intended Navy and Air adoption boundary for landlocked or capability-less countries, then review `doctrine_research_navy_adoption_available`, `doctrine_research_air_adoption_available`, and the matching domain score branches in `common/scripted_triggers/027_doctrine_research_triggers.txt` and `common/scripted_effects/027_doctrine_research_effects.txt`.

2. Provide a machine-readable MCP fixture or adapter manifest that binds country scopes, variables, flags, doctrine state, mastery, banked progress, templates, production, war, geography, strategy factors, DLC, and queue state for the prose DR-A01 through DR-G03 scenarios without inventing state in the audit.

3. Preserve a real pre-change AI-source snapshot if a future owner patch needs a meaningful before/after `probability_compare`; current/current controls cannot prove a tuning delta.

4. Supply a complete manifest for `global.all_events`, per-event weights and caps, automatic-pool validity factors, recovery cadence, cap reduction, event removal/reset rules, and National Breakthroughs member roles before rerunning DR-F01 through DR-F05 with `custom_weighted_pool` and, only then, `probability_sequence`.

5. Rerun the named domain sensitivity sweep with typed ranges after the probability server is available, and use the same `DR_027_FINAL_2026_08_30` ID and scenario hashes only if the fixture content is genuinely reproduced.

6. Rerun the event state-flow/render and doctrine/technology inspect/render routes after the MCP transport and large-workspace diagnostics are cleared.

## Final handoff state

Completed: required local guidance, Event 027 specs, source files, offline wiki pages, vanilla documentation, four current chooser-layer inspections, 37-scenario evaluations for every layer, same-source comparisons for every layer, automatic evidence rendering, explicit stale-render checks, custom event/cluster pool inspections, and source-level risk review.

Blocked: numeric runtime score resolution, exact probability and ranking evidence, threshold/sensitivity sweep, fresh seeded simulation, custom-pool normalization, sequence analysis, fresh probability render, event state-flow render, and doctrine structural inspect/render.

Uncertainty: all named scenarios remain unresolved for engine behavior; the source-only Navy/Air gate risk and Event 027 required-versus-optional cluster mismatch are review findings, not measured probability outcomes.

Final verdict: do not mark Event 027 Doctrine Research AI balance or probability acceptance complete from this audit. The parent needs a typed fixture/adapter route and a live MCP refresh before any dominance, starvation, rank-reversal, repetition, invalid-candidate, or human-parity claim can be closed.

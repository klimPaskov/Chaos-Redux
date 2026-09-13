# Event 027 Doctrine Research: Current AI Probability Audit

Audit date: 2026-09-01.

Audit role: read-only `chaosx_ai_probability_auditor`.

Audit status: incomplete and not an acceptance-completion claim.

No gameplay, AI, event, focus, decision, mission, technology, doctrine, scripted-effect, scripted-trigger, localisation, country, asset, or runtime file was edited by this audit.

The only requested write is this handoff document.

The repository was already dirty and is shared with other agents; the current Event 027 AI/effect/trigger/on-action files were read in their current working-tree state and were not reverted or normalized.

## Executive result

The live HOI4 probability route discovered the Event 027 AI surface as `random_list`, not as a direct `doctrine_ai_will_do` surface.

The four current `random_list` candidate pools are structurally complete at their declared source selectors: five domains, thirteen Grand Doctrines, eighteen tracks, and 107 subdoctrines.

The only resolved numeric results are DR-A01 through DR-A06 at the domain layer, using the declared primitive score fixture supplied to the analyzer.

Those domain results are exact conditional probabilities for the supplied raw scores and complete five-entry pool, but they are score-only evidence rather than native GER/JAP/USA/SOV/FRA/ITA country or doctrine-state proof.

The Navy-score sweep is a bounded score-only sensitivity result and demonstrates an Army-to-Navy rank reversal under the declared range.

Grand Doctrine, track, subdoctrine, multi-choice sequence, repeatable-event, National Breakthroughs cluster, DLC-matrix, human-parity, and invalid-adapter conclusions remain unresolved because the required native state, complete custom pools, or sequence contract was not available.

No genuine before-source snapshot exists for the current AI file, so `hoi4.probability_compare` was intentionally not run and no before/after claim is made.

The Event 027 structural MCP projections are partial, and the doctrine render is explicitly `sourceAccurate: false`; structural output is retained as supporting evidence only.

The Event 027 probability acceptance criteria are therefore not demonstrated by this audit.

## Required reading and evidence boundary

The following were read before source review: `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and the full `docs/specs/027_doctrine_research_specs/027_doctrine_research_probability_scenarios.md`, including its acceptance standard.

The required offline Paradox wiki core pages were consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Technology modding, and Doctrine modding.

Relevant vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` was consulted, including effects, triggers, script concepts, modifiers, dynamic variables, technology, and doctrine references.

The wiki and documentation establish the distinction used here: a `random_list` normalizes a complete positive-weight pool, while AI willingness scores, event option AI chance, MTTH, and direct random rolls are different operations.

No source-only scan is treated as normalized probability evidence.

## Audited source surfaces

The primary weighted source is `common/scripted_effects/027_doctrine_research_ai_effects.txt`.

The domain chooser is `doctrine_research_ai_choose_scored_domain` at lines 16-27, with the five-entry `random_list` at line 19.

The Grand Doctrine chooser is `doctrine_research_ai_choose_scored_grand` with its thirteen-entry `random_list` at line 147.

The track chooser has its eighteen-entry `random_list` at line 326.

The subdoctrine chooser has its 107-entry `random_list` at line 2003.

The current local source SHA-256 values are:

| File | Working-tree SHA-256 | Working-tree status |
| --- | --- | --- |
| `common/scripted_effects/027_doctrine_research_ai_effects.txt` | `6C4B7E9B776682496C2FB7ABAC627FAF22B72A56B7789FB3F38657AA733B9D39` | untracked |
| `common/scripted_effects/027_doctrine_research_effects.txt` | `CB5F51FB295ACFAF1815900D8ED4671528E8B27DB977FD78CB77C3E575207112` | untracked |
| `common/scripted_triggers/027_doctrine_research_triggers.txt` | `0C88AFC1C8F51F0074ED6C6BB98CF0501219C3E0CD4F13A9E308D80FEB95669C` | untracked |
| `common/on_actions/027_doctrine_research_on_actions.txt` | `0531B4AA65C5AA09D0BC893C35721ACA50734F1B8C6917724CA9F366F1C01404` | untracked |
| `events/027_doctrine_research.txt` | `134FD2AEB6F1C2354D3758A46BBF13CA476FAA5567E52B2B0F4CBA09388FBEF7` | modified |
| `common/script_constants/027_doctrine_research_constants.txt` | `69F7412D01047D19638B49A215DB03847C8D7BADE0B68A0DADA563F8B0220C1B` | existing working-tree source |
| `common/scripted_effects/chaosx_settings_effects.txt` | `D5C6925F090843782E9C0025A1F3D41D5540513048722C5D6E5FB54091FEAA36` | existing working-tree source |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | `69DD0F1080C319268EC75B8A4B26666E9C8059216D276C7949AF8B1A6070C107` | existing working-tree source |
| `common/scripted_effects/chaosx_logic_effects.txt` | `E2CEC7CD67096585A6B531D96A242C464965643459A06B14C9F459A52598F671` | existing working-tree source |
| `common/doctrines/grand_doctrines/chaos_warfare_grand_doctrine.txt` | `E4A1A7D003150F685F52D24B60FDAF7A25C40E85163272E7AACFFE9AECABCB83` | existing working-tree source |

The standalone `common/ai_strategy/027_doctrine_research_ai_strategy.txt` file is absent.

The current design instead exposes native observable strategy signals through `common/scripted_triggers/027_doctrine_research_triggers.txt` at lines 29-119.

## Probability MCP discovery and revisions

The mandatory first call was:

```text
hoi4.probability_inspect
adapter = doctrine_ai_will_do
source = common/scripted_effects/027_doctrine_research_ai_effects.txt
refresh = true
```

The result was `PROBABILITY_SOURCE_DISCOVERED`, status `ok`, workspace `mod_chaos_redux_ea3b2d67c2c0`, source revision `12845b524ada9b40db9744b05c8fb6abeea3183ff549ae7a133d9009ba1fa79b`, and MCP source hash `db288f9569977cf12980a03908f6138a328ee3963f8df522a8ebecc6565e50a4`.

The requested direct adapter had zero direct candidates; the available `random_list` surface had 143 candidates and 143 identifier matches.

The discovery artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56dbfe54c5c2de6e4477c988edeee20ad935bbfd8ad74accbd834bae53c62a03/da4c313a94b818708066ecfc0bac451f4bfaa99dfd59b966ffe84b7ce3d3eb39/probability-inspect-db288f956997.json`.

The focused `random_list` inspections used the same source revision and MCP source hash.

| Pool | Candidate selector | Count | Pool complete | Inspect artifact |
| --- | --- | ---: | --- | --- |
| Domain | `common/scripted_effects/027_doctrine_research_ai_effects.txt:19.entry.2` through `:19.entry.6` | 5 | yes | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8e0644c6f244fbf22328533294641c2375d6cb8f156d6525aa6b4637c6d9199/101d8091427f5b4d978247705ec1a1ae4fb5c870c62c6fe757ed3acf0f67038b/probability-inspect-db288f956997.json` |
| Grand Doctrine | `common/scripted_effects/027_doctrine_research_ai_effects.txt:147.entry.2` through `:147.entry.14` | 13 | yes | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8f147b529cd2c3e7ab50337df55ba94d0729933182420092fab59d5e1e5093d/8f2e03715d657236bb1f2c4a22a7bfd75c4d73974909dd68fe66fdfd9ac92092/probability-inspect-db288f956997.json` |
| Track | `common/scripted_effects/027_doctrine_research_ai_effects.txt:326.entry.2` through `:326.entry.19` | 18 | yes | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ef3172cc4f9c6d179089ced87aadab4f98fc30c9d6f64feb410fdf27ffb0e16b/08cf3554c5789ea1da68ecb25e2f84837f75e254a10d07f5d3bd0117e57dbb9d/probability-inspect-db288f956997.json` |
| Subdoctrine | `common/scripted_effects/027_doctrine_research_ai_effects.txt:2003.entry.2` through `:2003.entry.108` | 107 | yes | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0e6ca9adaf538dfeb654ec3f9d6b533cc3bb7dc7ebc169776e7b31be0a4b877/d1bb23e668fbb5c5bd6281a0782ee86457871685c05d65da0f798fb53fd39c60/probability-inspect-db288f956997.json` |

The pool counts above are complete source selectors, not proof that every row is valid in a particular country state.

## Scenario contract

The required scenario IDs were all submitted exactly: `DR-A01`, `DR-A02`, `DR-A03`, `DR-A04`, `DR-A05`, `DR-A06`, `DR-B01`, `DR-B02`, `DR-B03`, `DR-B04`, `DR-C01`, `DR-C02`, `DR-C03`, `DR-C04`, `DR-C05`, `DR-C06`, `DR-C07`, `DR-D01`, `DR-D02`, `DR-D03`, `DR-D04`, `DR-D05`, `DR-D06`, `DR-E01`, `DR-E02`, `DR-E03`, `DR-E04`, `DR-E05`, `DR-E06`, `DR-F01`, `DR-F02`, `DR-F03`, `DR-F04`, `DR-F05`, `DR-G01`, `DR-G02`, and `DR-G03`.

The main hybrid scenario set ID was `DR_027_CURRENT_2026_09_01`.

The domain and Grand Doctrine evaluations used scenario hash `390dc5338aec5ef7d29c44ba4ad73f4da4bb711216611426ce902e36706cab04`.

The track and subdoctrine evaluations used scenario hash `85a5e3f6476fd199fd2501612a5092442453aadd57fa2ca8066e6d769e103a6b` because those calls omitted the optional A-group labels while retaining the exact scenario IDs and declared states.

The A-group primitive score fixture was:

| Scenario | Actor string | Army | Navy | Air | Special Forces | Chaos Warfare | Candidate override declaration |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| DR-A01 | `GER` | 30 | 5 | 10 | 0 | 0 | all five score variables `true` |
| DR-A02 | `JAP` | 8 | 30 | 12 | 0 | 0 | all five score variables `true` |
| DR-A03 | `USA` | 15 | 8 | 30 | 0 | 0 | all five score variables `true` |
| DR-A04 | `SOV` | 18 | 0 | 8 | 0 | 0 | Navy `false`; other four `true` |
| DR-A05 | `FRA` | 20 | 18 | 8 | 0 | 0 | all five score variables `true` |
| DR-A06 | `ITA` | 0 | 0 | 0 | 0 | 0 | all five score variables `false` |

The score keys were `doctrine_research_ai_score_army`, `doctrine_research_ai_score_navy`, `doctrine_research_ai_score_air`, `doctrine_research_ai_score_special_forces`, and `doctrine_research_ai_score_chaos_warfare`.

The actor strings are fixture labels only and do not bind native country tags, force composition, production, war, geography, strategy, DLC, doctrine progress, or owner-system readiness.

The A02 and A03 values are declared analyzer inputs for this audit and must not be presented as native JAP or USA engine observations.

The B-G scenarios were submitted with empty state and flag maps because the current analyzer accepted the primitive A score fixture but did not accept a complete nested country/doctrine state binding for the downstream scenario matrix.

The empty B-G submissions intentionally preserve unresolved status rather than fabricating campaign facts.

## Main probability evaluations

All four evaluations used `adapter = random_list`, `horizonDays = 1`, metrics `raw_value` and `conditional_probability`, the complete focused candidate pool for that layer, and the 37 required scenario IDs.

| Layer | Result | Analysis ID | Candidates | Unresolved | Diagnostics | Primary evaluation artifact | Classification |
| --- | --- | --- | ---: | ---: | ---: | --- | --- |
| Domain | `PROBABILITY_ANALYZED_PARTIAL` | `probability-6058fa1e8107c2b94201c7cd` | 185 | 5 | 12 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d06ad37e2293cf8556376f88f0bfcfc3f36ba7347094b499bbeeb553e66d99b6/8267d26d43cc26eaae4ca63e69f6af0a0d8fe45daaa1cd5a357126dc0bd9a02e/probability-6058fa1e8107c2b94201c7cd.json` | A01-A05 exact score-only; A06 all-zero fallback unresolved; B-G unresolved |
| Grand Doctrine | `PROBABILITY_ANALYZED_PARTIAL` | `probability-f907e39117d8129dbcd9492e` | 481 | 13 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d51196f8d174e7e1c5bb235509c8c0c4852dc758e91bd0aa7bc694cfd7af5e1f/d8fd39a1feaa85bb826d4abb114aee73acdb886719ef4d1166ac1ea2bd3d6dc4/probability-f907e39117d8129dbcd9492e.json` | unresolved score inputs for the full matrix |
| Track | `PROBABILITY_ANALYZED_PARTIAL` | `probability-c41fe09b27de7a3cb6e93252` | 666 | 18 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/efba81bbbe62112c5654140a80e501286a9f4d3d58907df2b599ba25d6c727c8/49b974f0b948553b0b4c35afd9b89441a2c091d36c532c92419ee3b681ee62d5/probability-c41fe09b27de7a3cb6e93252.json` | unresolved selected-domain/Grand Doctrine state |
| Subdoctrine | `PROBABILITY_ANALYZED_PARTIAL` | `probability-8a26edec98218e1ac72b7cab` | 3959 | 107 | 0 | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f014e8173fb327fe839337d60d7a6593018b666e416bfa638cc7a5fad53bf83/850b872f1b07b4078e3d602e87f509bda356230b51efb5f54c789b3374618871/probability-8a26edec98218e1ac72b7cab.json` | unresolved selected-domain/Grand Doctrine/track state |

The shared source revision for these evaluations was `12845b524ada9b40db9744b05c8fb6abeea3183ff549ae7a133d9009ba1fa79b` with MCP source hash `db288f9569977cf12980a03908f6138a328ee3963f8df522a8ebecc6565e50a4`.

The unresolved totals are analyzer aggregate counts for unresolved score expressions, not a claim that exactly one row per scenario was unresolved.

The Grand Doctrine, track, and subdoctrine candidate pools are complete at the source-selector level, but the domain score fixture does not supply their selected-stage score inputs.

Consequently, no numeric downstream rank is reported for any Grand Doctrine, track, or subdoctrine scenario.

## Resolved domain values and rankings

For a fixed complete five-entry domain pool, the analyzer reports the normalized `conditional_probability` as raw candidate value divided by the positive pool total.

The following table reports only the declared A-group score fixture.

| Scenario | Raw score tuple `(Army, Navy, Air, SF, Chaos)` | Pool total | Rank order | Conditional probabilities |
| --- | --- | ---: | --- | --- |
| DR-A01 | `(30, 5, 10, 0, 0)` | 45 | Army > Air > Navy > SF > Chaos | Army `0.6666666667`; Air `0.2222222222`; Navy `0.1111111111`; SF `0`; Chaos `0` |
| DR-A02 | `(8, 30, 12, 0, 0)` | 50 | Navy > Air > Army > SF > Chaos | Navy `0.6`; Air `0.24`; Army `0.16`; SF `0`; Chaos `0` |
| DR-A03 | `(15, 8, 30, 0, 0)` | 53 | Air > Army > Navy > SF > Chaos | Air `0.5660377358`; Army `0.2830188679`; Navy `0.1509433962`; SF `0`; Chaos `0` |
| DR-A04 | `(18, 0, 8, 0, 0)` | 26 | Army > Air > Navy > SF > Chaos | Army `0.6923076923`; Air `0.3076923077`; Navy `0`; SF `0`; Chaos `0` |
| DR-A05 | `(20, 18, 8, 0, 0)` | 46 | Army > Navy > Air > SF > Chaos | Army `0.4347826087`; Navy `0.3913043478`; Air `0.1739130435`; SF `0`; Chaos `0` |
| DR-A06 | `(0, 0, 0, 0, 0)` | 0 | no meaningful rank; analyzer tie order only | all conditional probabilities `null` |

The A01-A05 results meet the scenario-spec ordering at the score-fixture level.

They do not prove that the native countries would produce those values.

The source-linked candidate traces for resolved rows report the wrapper eligibility as `implicit true`, with each candidate score supplied by the corresponding candidate override.

The trace provenance is the domain chooser at `doctrine_research_ai_choose_scored_domain[0]`, its `random_list[0]`, and the corresponding score helper at lines 21-25.

The candidate override mechanism did not execute the source `if` gates as native trigger evaluation.

In DR-A04 the Navy override was `false`, but the analyzer still rendered the Navy row as eligible with raw value zero.

In DR-A06 all five overrides were `false`, but all five rows remained eligible with raw value zero and the analyzer returned `PROBABILITY_ALL_ELIGIBLE_VALUES_ZERO`.

Therefore DR-A04 does not prove that Navy is invalid, and DR-A06 does not prove that the game closes the batch without a fallback.

The exact domain diagnostics were `PROBABILITY_STARVED_OUTCOME` for zero Special Forces and Chaos Warfare in DR-A01, DR-A02, DR-A03, and DR-A05; for zero Navy, Special Forces, and Chaos Warfare in DR-A04; and `PROBABILITY_ALL_ELIGIBLE_VALUES_ZERO` in DR-A06.

## Declared-range sweep

The justified sweep used a separate scenario set ID `DR_027_DOMAIN_SWEEP_2026_09_01` and scenario hash `bd308ee1170f5a44fea799593b8ac31c6acbea33204285993e5ba0f5c221f16d`.

The scenario was DR-A05 with the same declared `(20, 18, 8, 0, 0)` fixture, and the explicitly uncertain input was `doctrine_research_ai_score_navy` with range `[0, 30]`.

The sweep used seven points, `pairwise = false`, and `findRankReversals = true`.

The result was `PROBABILITY_ANALYZED`, status `ok`, analysis ID `probability-5ad00da090bfbbfb4a3a9bc2`, source revision `12845b524ada9b40db9744b05c8fb6abeea3183ff549ae7a133d9009ba1fa79b`, and MCP source hash `db288f9569977cf12980a03908f6138a328ee3963f8df522a8ebecc6565e50a4`.

The primary sweep artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69dae3e22cf6f701c56343efe1117921841aa77a547611a452ed2b0765c3a709/e8ae6a4ac7f57232efb332dd8a1ff206c45639ae51c75c742124fc57a82711ee/probability-5ad00da090bfbbfb4a3a9bc2.json`.

The sweep produced ten visual resources, including ranking, matrix, sensitivity, and threshold views.

The rendered SVGs are:

- Ranking: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56b2bb36a73a4cc76a89a326c47e1603bf63d1ea929b20db89b6a76ae39dab07/c49d45a4886d6caf41adf5226f669150b03ad534aacd97eab7ad6807afa9e311/probability-probability-5ad00da090bfbbfb4a3a9bc2-ranking.svg`
- Matrix: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d2bd8e68d05ceaa892fe425ae248334538d93a3429d9331d32401b1060d6938/e28a3bf9189bf313b5c2942e06ce27200da862144f3fc3635aa7484f735ce8fa/probability-probability-5ad00da090bfbbfb4a3a9bc2-matrix.svg`
- Sensitivity: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27a6d0aed77d70bfa477b18891a240d4c9c6775e2b43c1de5f4503eafceb62ee/34765fc3551a0150a02d86f735e53fa7cfbefa6dacffbc8e4d4f0ff659d45732/probability-probability-5ad00da090bfbbfb4a3a9bc2-sensitivity.svg`
- Threshold: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/941b38092aab743d94cfb645a1daf9f4b34245c82022667d08e5a4615a088f23/5156eda844c5fe0eb100db938b2ff0c1700bf1af0ce72f669b97374fcd91f17d/probability-probability-5ad00da090bfbbfb4a3a9bc2-threshold.svg`

The sweep reported `PROBABILITY_UNKNOWN_INPUT_DOMINATES_RESULT` for the Navy candidate over a probability interval of `[0, 0.5172413793]`.

It reported threshold-cliff diagnostics for Army between Navy values `[0, 5]` with delta `-0.1082251082`, for Navy between `[0, 5]` with delta `+0.1515151515`, and for Navy between `[5, 10]` with delta `+0.1116427432`.

At declared Navy score 20, Army and Navy both have raw value 20 and conditional probability `0.4166666667` each, with Air at `0.1666666667`.

At declared Navy score 25, Navy leads with probability `0.4716981132`, Army follows at `0.3773584906`, and Air is `0.1509433962`.

The analyzer reports the Army-to-Navy rank reversal between Navy values 20 and 25.

This is a bounded score-only sensitivity result, not a campaign-level rank-reversal claim.

No probability simulation artifact was produced.

The explicit `probability_simulate` attempt used the same declared Navy range, a fixed seed `270901`, and 1,000 pseudo-random samples, but the live MCP transport returned `tool call failed ... probability_simulate ... Transport closed`.

No sampled conclusion is made.

## Rendered probability evidence

The current evaluations were rendered with `hoi4.probability_render` after correcting an initial invalid scenario-hash argument.

The corrected render calls used the exact analysis IDs and expected scenario hashes listed above.

The render output was deterministic and retained source revision, source hash, scenario hash, candidate count, unresolved count, and diagnostics.

Domain render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/19fe7a4cd6c49ceec1695a143248a69b244c729d8fe4149b9a9d32a87684f0a9/d0f3d672f1b0fa32c64699763bdc384e07352f05b97f95c0f938e7aee94310c3/probability-6058fa1e8107c2b94201c7cd.json`.

Domain ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/560dd1baaca185144c5a6fcb43e9be512c29681a102132d22e35e57494c3be48/8e57396957d8759ca32c7aa17285c01835be8b933638a84c8c163aeeae02b417/probability-probability-6058fa1e8107c2b94201c7cd-ranking.svg`.

Domain matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0cf39fdd33acd95f7d05170bb587c533a77ffadf4ab8f65ed7bff7d2f906c714/0c1a55fe38ba59a761337b4e84e5c072ff64a143fdb3dc43ca4fd43e84c7d0ae/probability-probability-6058fa1e8107c2b94201c7cd-matrix.svg`.

Domain unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e2f9aa7b978700a5160d30df0c31cbf192ad6cffa149af59c7e1ea6bbf681253/e354052132d4799d1b6704f96044dc81bcdded902f1286a23f925aaa06b32f3a/probability-probability-6058fa1e8107c2b94201c7cd-unresolved.svg`.

Grand Doctrine render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/25aad0efa3cdda5ed352955136e2db3f567c9156c73c4e9fc196d36c98a86b0a/3b88645f64a223d234cab13e3a52a1d1b786ba63bb3c23a0e44633b05cb37c91/probability-f907e39117d8129dbcd9492e.json`.

Grand Doctrine ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82f0ec51b8aafb0bfcb41bc61ba2d49ef81c3401e5230433b33b927d45ae69eb/3ff5149f92364066540eabeb73c9c21a260d3f5778fbc398873f02cb2830968a/probability-probability-f907e39117d8129dbcd9492e-ranking.svg`.

Grand Doctrine matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8fe8ebb6baac726c1c425f34d2fd51ede8a84b707e050310e4e8b08cf9928b7/a8893e9e580b7d79df0227003a182e604599f2fc427d8b31efba062450785d00/probability-probability-f907e39117d8129dbcd9492e-matrix.svg`.

Grand Doctrine unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c30f7196f94bc96e28173ac382fe55633f999184faf94e750de70f17778751da/c6ed4b3b596e946c03d8091ad4ae635eb5743cf81efef44b1288cfd30dbae7df/probability-probability-f907e39117d8129dbcd9492e-unresolved.svg`.

Track render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee57511a58e791356aa20132264f54020e06082f7434f88e4fa936f17dcca2f3/02976df052dd910dc9fba8a25c528e1738ddc4fa3a05979a8739c7de1e103b2b/probability-c41fe09b27de7a3cb6e93252.json`.

Track ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d426915b492514eb2d60d53c89c0fbebcc1d8fd5c46bd7c1b5a75997fd2e9bc9/f9cf7ed10569dc89abef90a92f0150f2e4a8cf5f0aa828e4e857e20040c94b44/probability-probability-c41fe09b27de7a3cb6e93252-ranking.svg`.

Track matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77c92c8c8b37b22d0aa50aebd7c9a95acd05cd2c7429247cf5c73a6d42174ecb/1df2b81da578f3264955d780b3b59ab0e14fe4d63f2ead5c003cecbe7ab49c1f/probability-probability-c41fe09b27de7a3cb6e93252-matrix.svg`.

Track unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d009a4eafb5a300059dedf555c58577b92e02bed1aa9308b8ff75987f970fdfa/0384d57619254e2fc8d162f87545b0f9a2c52068eb38a5c11de118efa557367b/probability-probability-c41fe09b27de7a3cb6e93252-unresolved.svg`.

The track render URI above records the current source-linked render family; the analyzer also emitted the automatic render resources under the same analysis ID.

Subdoctrine render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f9126b98c7f7b9411faa760d163c514caa9194338ee3ba48df6f3254b6aa411a/b7ee74280f5f1fde7aa159e89458258a0e245d22d6791683ef8e337b2c738ba0/probability-8a26edec98218e1ac72b7cab.json`.

Subdoctrine ranking SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9759009e3202da6e68cf41fbe38a8a418ef48d7156af90cf2a1dc6a99631063a/7e023b487406c769c3d59f0f5d7fea5be55f188b61778b1bdf3e460416956683/probability-probability-8a26edec98218e1ac72b7cab-ranking.svg`.

Subdoctrine matrix SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2193afe24595e2691a41cb2fa2b54d84eadc890c43200a042fcc0fb60dda2366/c0ddb07f526239083e676fa34557a2d673cf3067ba6545c1bb0ab38f5bcb6cf7/probability-probability-8a26edec98218e1ac72b7cab-matrix.svg`.

Subdoctrine unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b6fad83455fc2aa785c8167eeeef214363ebabf9df4b8796a3d7136c5a63b3c/d7c447beeaca12f007547809cb5fd646ac3e31a2ce1ac711afce9f5b8a79facd/probability-probability-8a26edec98218e1ac72b7cab-unresolved.svg`.

## Candidate-pool and external-factor completeness

| Scenario group | Exact IDs | Corresponding source pool | Candidate pool completeness | External-factor completeness | Result classification |
| --- | --- | --- | --- | --- | --- |
| A | DR-A01 through DR-A06 | Domain `:19.entry.2` through `:19.entry.6` | complete five-row pool | incomplete native state; primitive score fixture only | exact score-only for A01-A05; A06 fallback unresolved |
| B | DR-B01 through DR-B04 | Grand Doctrine `:147.entry.2` through `:147.entry.14` | complete thirteen-row pool | empty state; no armor/manpower/plan/DLC bindings | unresolved |
| C | DR-C01 through DR-C07 | Track `:326.entry.2` through `:326.entry.19` | complete eighteen-row pool | no selected Grand Doctrine, mastery, banked progress, or transition state | unresolved |
| D | DR-D01 through DR-D06 | Domain/Grand/track/subdoctrine layers | static pools complete where inspected | no CBRN readiness, DLC, special-country adapter, or owner-system binding | unresolved |
| E | DR-E01 through DR-E06 | Downstream layers plus batch state | static pools complete where inspected | no batch size, active stage, queue, mastery, or between-choice state transition | unresolved |
| F | DR-F01 through DR-F05 | Event 027 repeatable pool and National Breakthroughs cluster | incomplete custom manifest; cluster/logic inspection failed | no global weights, cap, recovery, timer, cluster member, or terminal-state fixture | unresolved |
| G | DR-G01 through DR-G03 | Human/AI validity and DLC/adapter boundary | static AI lists complete; native human parity pool unavailable | no human-visible pool, DLC matrix, or injected adapter state | unresolved |

The four static AI random lists have complete candidate identities, but only the domain list has a complete set of numeric values under the declared fixture.

No conclusion about a positive weight on an impossible candidate is made because the accepted fixture did not execute native eligibility gates.

## Source configuration and modifier trace boundary

The source constants in `common/script_constants/027_doctrine_research_constants.txt` define `doctrine_research_ai_weight` at lines 334-350.

The source-only values are `base = 1`, `forces = 2`, `production = 2`, `war = 2`, `geography = 2`, `theater = 2`, `strategy = 2`, `completion = 3`, `owner_readiness = 3`, and `continuity = 2`.

These are configuration facts from source review, not MCP-evaluated country values.

The native domain score builder is `doctrine_research_ai_score_domains` at `common/scripted_effects/027_doctrine_research_effects.txt:3421-3483`.

It resets the five domain scores, checks domain action validity, adds binary force/production/war/geography/theater/completion/strategy signals, and adds owner readiness to each valid domain.

The ordinary adoption triggers at `common/scripted_triggers/027_doctrine_research_triggers.txt:133-165` use `NOT = { has_any_grand_doctrine = ... }` followed by `always = yes` for Army, Navy, and Air.

Special Forces additionally requires the relevant DLC and at least one special-forces technology.

Chaos Warfare additionally requires the CBRN capability and establishment-stock gates.

The source structure therefore presents a review risk for ordinary doctrine-less countries: Navy or Air can remain a valid action even without current fleet or air assets, while their score builder has a base/owner-readiness path whenever the action-validity trigger is true.

This is a source-review design warning, not a native probability conclusion, because the current MCP fixture did not evaluate those trigger branches.

The strategy signal wrappers at `common/scripted_triggers/027_doctrine_research_triggers.txt:34-119` are native observable force, doctrine, production, and CBRN checks rather than a separate Event 027 strategy file.

The AI active-batch resolver is `doctrine_research_ai_resolve_active_batch` at `common/scripted_effects/027_doctrine_research_effects.txt:3504-3527`.

The source calls `doctrine_research_ai_pick_choice` again after each successful transaction, which is consistent with the intended recalculation design.

No MCP sequence result proves that the recalculation excludes a branch completed between two choices.

The subdoctrine source maps the same Special Forces identities to two separate track-qualified sets: `doctrine_research_ai_subdoc_weight_87` through `_94` at `common/scripted_effects/027_doctrine_research_ai_effects.txt:1683-1793` and `_95` through `_102` at lines 1795-1937, with output mappings at lines 2092-2107.

This may be deliberate route qualification, but it is a source-level duplicate-identity risk until a native selected-track/subdoctrine evaluation proves that the same identity cannot be selected through an invalid or stale route.

## Findings

### Domain ordering and dominance

The declared A01-A05 fixture produces the expected top-level ordering: Army for A01, Navy for A02, Air for A03, Army for A04, and Army narrowly ahead of Navy for A05.

The largest resolved top-candidate probabilities are Army `0.6923076923` in DR-A04, Army `0.6666666667` in DR-A01, Navy `0.6` in DR-A02, and Air `0.5660377358` in DR-A03.

No resolved A-group candidate crossed the configured dominant-probability diagnostic threshold of `0.75`.

This does not establish campaign balance because the fixture values were supplied directly and external factors were incomplete.

### Starvation

The analyzer repeatedly flagged Special Forces and Chaos Warfare as zero-value outcomes in A01-A05, and also flagged Navy in A04.

These are exact zero values under the declared fixture, not proof that the native source always starves those domains.

The repeated zero pattern is still a tuning review signal because the specification expects conditional domains to remain available when their route is valid.

DR-A06 has no positive eligible value, and the analyzer returned null probabilities rather than proving the intended no-candidate batch closure.

### Invalid and impossible candidates

No candidate was proven to have positive weight while natively impossible.

The accepted candidate override representation did not remove a candidate from the pool when set to `false` and therefore cannot serve as an invalidity proof.

DR-B04, DR-D02, DR-D05, DR-G02, and DR-G03 remain specifically unresolved for invalid DLC, missing adapter, and fail-closed behavior.

### Rank reversal and threshold sensitivity

The declared Navy range produces an Army-to-Navy reversal between Navy scores 20 and 25.

The sweep also reports cliff-like changes over the lower intervals, so small changes in a Navy score can materially move normalized probabilities in the close Army/Navy fixture.

This is bounded score sensitivity only and is not a native country rank reversal.

### Repetition, cadence, and snowball risk

The source says the AI picker is rerun after each successful choice, but no complete MCP sequence was possible.

Therefore repetition, branch completion between choices, banked mastery preservation, batch-stage queueing, and safe five-choice stacking are unresolved.

No claim is made that the resolver either does or does not snowball into a completed branch.

## Repeatable-event and cluster pool inspection

The Event 027 repeatable registration is source-linked at `common/scripted_effects/chaosx_logic_effects.txt:313-364`, with the Event 027 ID added at line 325 through `constant:doctrine_research_event.id`.

The shared automatic selection implementation is source-linked at `common/scripted_effects/chaosx_settings_effects.txt:4340-4453`.

It evaluates candidates from the dynamic `global.all_events` array, resolves validity through shared helper calls, obtains event weight, scales and rounds it, and performs a cumulative integer roll.

The live `hoi4.probability_inspect` call for `adapter = custom_weighted_pool` against `common/scripted_effects/chaosx_settings_effects.txt` returned `PROBABILITY_SOURCE_INSPECTED`, status `ok`, `poolComplete: false`, zero candidates, and zero required inputs.

Its MCP source revision was `12845b524ada9b40db9744b05c8fb6abeea3183ff549ae7a133d9009ba1fa79b`, its MCP source hash was `f12c120215a4ca8a73b6191edeb3c7ae6a5cac780f934d2415542dfa3a59b306`, and its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c06be9d842a7ca4e6e568f255d2ae60b20933c4ae36ea8e5e31c7ded67265b4e/2579cc6ff66569e0c0a3952a4f73a362ae213cef75a6c1d4bdc9acf0c11beb8a/probability-inspect-f12c120215a4.json`.

The corresponding `custom_weighted_pool` inspections against `common/scripted_effects/chaosx_event_cluster_effects.txt` and `common/scripted_effects/chaosx_logic_effects.txt` returned `INTERNAL_ERROR` with message `Unexpected internal error`, no artifact, no source revision, and no candidate data.

Because the complete event and cluster candidate manifests were not available, `probability_evaluate` was not run for the F-group custom pools.

Because cadence, cooldown, recovery, cap, removal, reset, cluster membership, and terminal state were not exposed as a complete contract, `probability_sequence` was not run.

DR-F01, DR-F02, DR-F03, DR-F04, and DR-F05 are unresolved.

## Structural Event 027 and doctrine MCP evidence

The source root is `chaosx.nr27.1` at `events/027_doctrine_research.txt:12-20`.

The root is hidden and triggered-only and calls `doctrine_research_fire_global_batch` in its immediate block.

The Event Chain Viewer was called with selector `{ kind: "event", eventId: "chaosx.nr27.1" }`.

The fresh scan returned `EVENT_INSPECTED_PARTIAL`, status `ok`, revision `2725045f62d14f3536e32f1662ce2fae9f2fae9933ff462de6a8c867d1401570`, graph hash `e6c16ff300aa88dfed3e6f55481fdb8ad1e5bb697e6cf3ca888bd82178d7d62d`, 9,722 events, 15,150 options, 1,133 entries, 38,320 edges, 8,680 unresolved nodes, 2,206 issues, and one blocking diagnostic in the global projection.

The scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e18ab2c4edbafc1b0899a26325ffb3f531ee334b683923de6b915d2301a365c/e06efdc5fb0b8875ee8fc44b6bbee90ea6ecc45aaadf0415e3e666c21793dcd8/event-scan-2725045f62d1.json`.

The focused lint call returned the same partial revision and global counts, with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84840ff7eb054dd7b24fb82711b92790a929fdd4e2daa7e3d50c3b46f44573b4/8da703be5117f51c1ae2150a81ead24909c0eebc167bb0a5e1c99d94d367755c/event-lint-2725045f62d1.json`.

The Event Chain Viewer reported `MCP_INLINE_FILES_TRUNCATED` with 367 total paths and 64 inline paths, and deferred workspace-wide helper/lifecycle projections.

The options render returned `EVENT_RENDERED_PARTIAL` with the same revision and graph hash.

Its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a784191e208b9e5ee30fe22ac4d747d6223bf0d4e3cfd17e8b40c98db2d7189/9c6ac578a72306dc795cfdaa8465b9d3d958cd3b6064323d68ca3bb32a648c5e/event-options-2725045f62d1-manifest.json`.

Its JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/178c009b03117d5f6961a957fbef9a7d5a9773bf25ab358e074d3e1408fedbaf/a23c9c7c52340f23683c9336dbd3dec83d969064cc11bd3ca724377464d5d050/event-options-2725045f62d1.json`.

Its SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/be5342d5a7628db7ea870e32562d750d6db39d8e92a4cf56afdc23c412d631b2/26a0f71f2b54e1a7065382490f838e52a6f901accb477dc2cd3cc9245fd91018/event-options-2725045f62d1.svg`.

Its PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/209d5abc10ce8f722941d8e2a1e82af9903e7ea885f34a319a2fd258d1159819/7539463b7e0f2539a4fa8e6358fef3f7184129e8a27f158751e66a6c59350ba4/event-options-2725045f62d1.png`.

The options render reported `selectedNodes: 0` and `omittedNodes: 42456`, so it is not direct source-specific proof of Event 027 option reachability.

A later file-selector retry was blocked first by the render argument limit `maxNodes <= 240` and then by MCP `Transport closed` during the narrowed inspect/render retry.

The technology route was called with `hoi4.tech_inspect` in `scan` mode for folder `land`.

It returned `TECH_INSPECTED`, status `ok`, revision `7080c50bf1467579a159640153bbb2d43902b0b7a42a6c35daa41609a5124ed9`, graph hash `3a8197353f9acbc3271a5bbd54995b9887f067674e8d69285cb83dff0b574c68`, 679 technologies, 18 folders, 475 placements, 457 edges, 857 unlocks, 520,298 references, 1,302 issues, and three unresolved nodes.

The scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7e002cc1c9ee93bd9b8186160fc929a42bf47e509b27047417d0ceac15d576cd/bd93a2628cb0ceb87612a52178c8f73b7367902726dd529eb6b48cd1f1aa4c63/technology-scan-7080c50bf146.json`.

The scan validation was false because the projection reported 1,421 blocking technology diagnostics.

The doctrine render for folder `land` returned `TECH_RENDERED`, selected six nodes, omitted zero nodes, and explicitly reported `sourceAccurate: false`.

Its manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69319b1452c92ccb490113c2ff35837f6f085605c32c9e0561e9cb35e809dc36/6abd0aa4fe52f3f193b40cebb6e717a47fd2afa24231273f5feb4708a6cb64aa/technology-doctrine-7080c50bf146-manifest.json`.

Its JSON is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff10b5acacd42dd038d57347974a025e5ff21e18e5bc3e7d29818cc5986580a3/030827b01ce04af8486c8ecbd49386c58309d1e99952c29213b8baaee525064c/technology-doctrine-7080c50bf146.json`.

Its SVG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f4b1d78531041dab827aca19f1c8156f8a946a311356e083f8829885aea54945/af9d2ef442462083008088ad8e75e9d403f5d3df1f269e8809d5b6bc346dc024/technology-doctrine-7080c50bf146.svg`.

Its PNG is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7945b2bc3acf4ccc0cace4f91640955341bd003fb622adb74d981c7ca89100c/2f40938aade022a476f83ea76b8eaf172b3a85b839ca4c1483f32516c66ab6b7/technology-doctrine-7080c50bf146.png`.

A targeted `chaos_warfare` technology trace/render retry returned MCP `Transport closed`, so no node-specific native doctrine trace is claimed.

The structural Event and technology artifacts are useful review evidence but do not replace the unresolved probability inputs.

## Before/after comparison status

`hoi4.probability_compare` was not run.

The current AI source is untracked in the working tree and no genuine before-source file, cached source descriptor, or prior revision was available for this exact current surface.

Comparing the current source to itself would not be a before/after audit and would create false evidence.

No comparison ID exists.

The acceptance requirement for post-patch comparison is therefore open.

## Skipped analyses and exact reasons

`probability_simulate` was attempted only for the explicitly declared Navy-score uncertainty, with seed `270901` and 1,000 samples, but the MCP transport closed before an artifact was returned.

`probability_sequence` was skipped because the complete custom event/cluster pool, cadence, cooldown, recovery, cap, removal, reset, and terminal-state contract was not available.

`probability_evaluate` was not run for the custom event or cluster pools because `custom_weighted_pool` inspection reported `poolComplete: false` for the automatic-pool source and internal errors for the cluster and logic sources.

Native country/doctrine evaluations for B-G were not fabricated because the analyzer accepted only primitive score variables for the declared fixture and did not provide a complete native country, DLC, force, production, mastery, banked-progress, or owner-system binding.

The narrowed event file-selector inspection and targeted `chaos_warfare` technology inspection were not completed after the MCP transport closed.

No game process, save, or live campaign was launched.

## Recommended fixes for the parent to consider

These are read-only recommendations; none was applied by this auditor.

1. Preserve a real before-source snapshot of `common/scripted_effects/027_doctrine_research_ai_effects.txt`, then rerun `hoi4.probability_compare` with the same source selectors and the exact DR-A01 through DR-G03 scenario IDs after any owner-applied AI change.

2. Provide or restore a native typed country/doctrine fixture that binds country tag, force composition, factories, war, geography, strategy, DLC, active doctrine, mastery, banked mastery, selected domain, selected Grand Doctrine, selected track, owner-system readiness, and batch state without reducing those facts to manually supplied score variables.

3. Re-audit `common/scripted_effects/027_doctrine_research_effects.txt:3421-3483` together with `common/scripted_triggers/027_doctrine_research_triggers.txt:133-165` for the intended Navy/Air validity boundary, because the ordinary adoption triggers are unconditionally valid after doctrine absence while the scenario specification expects impossible or capability-free choices to be absent or near zero.

4. Define and validate the all-zero domain behavior at `common/scripted_effects/027_doctrine_research_ai_effects.txt:16-26` and the active-batch close path at `common/scripted_effects/027_doctrine_research_effects.txt:3504-3527`, so DR-A06 can be proven to close without a compensation reward or stale selection.

5. Expose a complete custom-pool manifest for the Event 027 repeatable pool and National Breakthroughs cluster, including every candidate, eligibility gate, current weight, cooldown, recovery, cap, removal, reset, scheduled state change, cluster participation factor, and terminal condition before running F01-F05 evaluation or sequence analysis.

6. Reconcile the track-qualified repeated Special Forces identities at `common/scripted_effects/027_doctrine_research_ai_effects.txt:1683-1937` and `2092-2107` with native selected-track and selected-subdoctrine identity validation before tuning their weights.

7. After a complete native fixture exists, rerun the downstream Grand Doctrine, track, and subdoctrine layers with the same IDs, then run DR-C04, DR-C05, DR-C06, DR-C07, and the E-group sequence contract to test variation, stacking, completion recalculation, banked mastery, and batch-stage isolation.

## Remaining blockers and uncertainty

The direct `doctrine_ai_will_do` adapter is not the active source surface; only the `random_list` adapter currently exposes the four chooser layers.

The domain pool has numeric score-only evidence, but native eligibility and country state are unresolved.

The Grand Doctrine, track, and subdoctrine layers have complete static candidate pools but unresolved scenario inputs and no numeric ranking proof.

The A06 no-candidate behavior is unresolved because the analyzer returned null probabilities for an all-zero eligible pool.

The F-group automatic and cluster custom pools are incomplete or unavailable to MCP, so no event timing, recurrence, starvation, or cluster distribution claim is supported.

The G-group human parity, DLC matrix, and invalid-adapter-injection cases are unresolved.

The structural Event 027 view is a large-workspace partial projection with global issues and no selected-node render proof.

The structural doctrine render is not source accurate and the targeted Chaos Warfare trace was lost to MCP transport closure.

There is no genuine before-source comparison artifact.

The simulation attempt has no result artifact because the MCP transport closed.

No acceptance completion is claimed.

## Final classification summary

| Conclusion | Classification |
| --- | --- |
| Five-entry domain pool exists and is complete at source selector level | exact MCP structural inspection |
| DR-A01 through DR-A05 domain ordering and normalized probabilities for supplied raw values | exact score-only |
| DR-A06 raw all-zero state | exact score-only input result; selection fallback unresolved |
| Navy range sensitivity and Army/Navy reversal between 20 and 25 | bounded score-only |
| Grand Doctrine ranks for DR-B01 through DR-B04 and downstream layers | unresolved |
| Track/subdoctrine variety, completion recalculation, banked mastery, and multi-choice sequence | unresolved |
| Event 027 repeatable timing and recovery | unresolved |
| National Breakthroughs cluster participation and fanout | unresolved |
| Human/AI parity, DLC matrix, and invalid adapter injection | unresolved |
| Event Chain Viewer evidence | structural partial |
| Doctrine technology-tree evidence | structural partial and source-inaccurate |
| Before/after balance comparison | skipped; no genuine baseline |
| Acceptance criteria | not demonstrated |

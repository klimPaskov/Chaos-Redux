# Event 016 Black Plague registry probability comparison

Date: 2026-08-09. This is a read-only MCP audit. No gameplay, AI, raid, event, or constants file was edited.

## Scope and source revisions

The audited CBRN surface is `grant_random_chaos_special_project_available_tech` in `common/scripted_effects/cbrn_project_effects.txt`, random-list source line 27. The audited Mengele surface is `make_random_directorate_special_project_researchable` in `common/scripted_effects/germany_mengele_effects.txt`, random-list source line 2286. The Mengele registry entries are weaponized zombies (entry 1), Black Plague (entry 2), cloning (entry 3), computation (entry 4), materials (entry 5), biomedical (entry 6), teleportation (entry 7), robotics (entry 8), paleogenetics (entry 9), xenobiological synthesis (entry 10), alien arms (entry 11), and temporal (entry 12).

The current working-tree file SHA-256 values are `D08B416BA003B4B22AC89905840DA80349CF0448E4A5E8D9C3DC02F0F204E309` for `cbrn_project_effects.txt`, `4B9ECDEEEDB8C72F0831B8789C19AFA0C077E1C15A0FE9AF563987118FCA96D6` for `germany_mengele_effects.txt`, and `A79258D0DCC20FE8F00285CE0000E301AD14527C3E880F2C19DD104B1B127C24` for `016_brilliant_scientist_portal_raids.txt`. The repository HEAD is `fb4207ad90a9ebb9020bd52f067c4a810ec8ee3d`.

`hoi4.probability_inspect` used adapter `random_list` against both scripted-effect files. The current CBRN inspect artifact is [probability-inspect-3122a369c161.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f8ad4c959223325a8ec350e24c8e9089b360386c78dbca7cd48be940705db7a9/d3e02a02ff57cb6cc810e05605ddcb7ec5ce6f01d674a46e388f5165d6c1bd8c/probability-inspect-3122a369c161.json). Its MCP source hash is `3122a369c161b1e23287c89e3d676bac2631ffc232e2f83bd65aa6688ec9ac7c`, source revision `fb5e848da435ab7e69b2ae4e47bed266937759c180a70cba331eceab620a3388`, complete pool is eight candidates, and required inputs are `has_tech` and `is_special_project_completed`.

The current Mengele inspect artifact is [probability-inspect-8cc2a5e03682.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ee8a0c3790d89823c272f90f426f533ad1909c6f5d52debf717d706fe8eb15d/a2f4d1320685ee5c85ba66bc4c6318e022556f47005aca1cc58f80b368f83714/probability-inspect-8cc2a5e03682.json). Its MCP source hash is `8cc2a5e0368231779a1f6f12b02365e9faae744d36cafa32fb39838eb71cb0fe`, source revision `fb5e848da435ab7e69b2ae4e47bed266937759c180a70cba331eceab620a3388`, and the file-wide discovery found 17 entries in three random-list pools. The complete 12-entry registry pool is the entries whose identifiers begin `common/scripted_effects/germany_mengele_effects.txt:2286.entry.`.

The random-list adapter documents proportional categorical sampling and exact bigint source arithmetic when the pool and trigger state are complete. It does not convert these values into AI willingness or player click probabilities.

## Baseline records and compare limitation

The recorded pre-change baseline identifiers supplied by the parent are CBRN all-open `probability-54fbd5ad022582ca6cb88789` with source revision prefix `d60af...`, CBRN anthrax-zero `probability-e822baa24bbcd8781f2a4a13`, Mengele all-11-at-100 `probability-2de44a7210ab89970ae1d289`, Mengele cloning-zero `probability-2b5c097c2d91a7a0c6e7e2fc`, and Mengele temporal-only `probability-80ef63108881156f06e081fa`. The recorded baseline CBRN inspect artifact is [probability-inspect-ec5c738320afa.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c3c779698c901db5beae1f5b16868e2054303f0e53ac06b724e0c333f480f9a5/df9ad9ef1ac48a6cc5149c366d63507c9a99a0f36ad257e02ce44c37bd843366/probability-inspect-ec5c738320afa.json).

`hoi4.probability_compare` was attempted with the baseline analysis identifiers as `before.identifier` and the current analysis identifier as `after.identifier`. The exact MCP result was `PROBABILITY_IDENTIFIER_NOT_FOUND` with blocker `No weighted source matched the requested identifier` for `probability-54fbd5ad022582ca6cb88789`. The cached baseline analyses are not available as weighted source identifiers in the current MCP workspace, so no valid before/after comparison artifact exists. The values below are a fresh current MCP analysis plus explicit baseline arithmetic, not a claimed MCP compare result.

## CBRN current scenarios

The complete candidate pool is:

| Entry | Source candidate | Base weight |
| --- | --- | ---: |
| 1 | anthrax | 10 |
| 2 | plague | 10 |
| 3 | tularemia | 8 |
| 4 | smallpox | 6 |
| 5 | zombie disease | 8 |
| 6 | Black Plague (`sp:black_plague_weaponization_program`) | 8 |
| 7 | sarin | 8 |
| 8 | soman | 6 |

### `cbrn_all_candidates_open`

The scenario declared `has_tech = "__none__"` and `is_special_project_completed = "__none__"` as sentinel values so no source gate matched. The eight-entry candidate pool was complete and the MCP result was exact, with pool total 64. The JSON artifact is [probability-820b02b87ead7c338434192d.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/769318320b277728dfdefd7d5922ad782424de6a45598dc3ffce7350f0f18fee/779ead74bdd5893153338b6df5c90eea7f32dc64a1aeae73b06e4604a8ef45ab/probability-820b02b87ead7c338434192d.json). The analysis ID is `probability-820b02b87ead7c338434192d`, source revision is `f0bbbdbcf316bfb835873d553a7b6d99190f685be674c98268057114ba340ca1`, and scenario hash is `3a66869c23777a141e47d24720197644143a37093a5134d8befa8ac06749d9a9`.

The exact normalized probabilities are anthrax 10/64 = 15.625%, plague 10/64 = 15.625%, tularemia 8/64 = 12.5%, smallpox 6/64 = 9.375%, zombie disease 8/64 = 12.5%, Black Plague 8/64 = 12.5%, sarin 8/64 = 12.5%, and soman 6/64 = 9.375%. No outcome dominates, and no outcome is starved in this all-open state.

The earlier three-scenario evaluation also produced [probability-c4e2748e614e7ebbacdc230c.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f5e1898c7f26668f03df9a47b294c89ebe637afa57d9db117f80cf958404b31/c9484c8f63c7301be383b49bc8904580037cf1673845dcaacbb419a03bb33fba/probability-c4e2748e614e7ebbacdc230c.json), a ranking SVG, and a matrix SVG under the same analysis ID. A later render returned `PROBABILITY_ANALYSIS_STALE` because the shared workspace revision changed from `f0bbbdb...` to `2b24e3837b3104d8a083d97600c2efbaaf56a05115381189e7074a382fd1b4b`; the stale render is not used as fresh evidence.

### `cbrn_anthrax_excluded`

The scenario declared `has_tech = "anthrax_bomb_delivery_systems"` and the completed-project sentinel. The complete pool remained eight entries, with anthrax raw value zero and pool total 54. The JSON artifact is [probability-44def47720a70f47656b251b.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397ebf3a764f65fd4daca82047f52d9b6b2cb99668aad6f231e9a31c8deb64bb/df4978601be90333a1278016c1596d41d5350c35a3420c6a27f425ce7410118d/probability-44def47720a70f47656b251b.json). The analysis ID is `probability-44def47720a70f47656b251b`, source revision is `f0bbbdbcf316bfb835873d553a7b6d99190f685be674c98268057114ba340ca1`, and scenario hash is `08052f464eb7f387cb2bb5ce094306e8449773a2d362e13dddfb2f80d92b03b3`.

The exact normalized probabilities are anthrax 0%, plague 10/54 = 18.5185%, tularemia 8/54 = 14.8148%, smallpox 6/54 = 11.1111%, zombie disease 8/54 = 14.8148%, Black Plague 8/54 = 14.8148%, sarin 8/54 = 14.8148%, and soman 6/54 = 11.1111%. MCP reported the expected `PROBABILITY_STARVED_OUTCOME` warning for the zero-valued anthrax entry and no unresolved outcomes.

For the recorded baseline, the seven-entry pool was 56 all-open and 46 after anthrax removal. Therefore the old all-open values were anthrax/plague 10/56 = 17.8571%, tularemia/zombie/sarin 8/56 = 14.2857%, and smallpox/soman 6/56 = 10.7143%; the old anthrax-excluded values were plague 10/46 = 21.7391%, tularemia/zombie/sarin 8/46 = 17.3913%, and smallpox/soman 6/46 = 13.0435%. These are baseline source arithmetic because the baseline MCP artifacts were not resolvable by the current compare route.

### One-candidate-left probe

The one-candidate-left intent was expressed as `cbrn_one_candidate_left_black_plague` with only entry 6 in `candidatePool` and both sentinels clear. MCP correctly withheld normalization with `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`; the artifact is [probability-b7e1648db97105a11fbfd191.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4101b282bb3de5093bbe68aa79cb32342f31827c4dec5da2cce8c9dfc6187c3a/5d8c5272d7ac9264c7a26c65b51ad9ea46beca027453fb39be5c0f879af125cf/probability-b7e1648db97105a11fbfd191.json). A full-pool state probe using a seven-token `has_tech` array returned `PROBABILITY_ANALYZED_PARTIAL` with seven `TRIGGER_UNRESOLVED` items because `has_tech` cannot compare the declared collection value.

Source arithmetic is 100% conditional on all other seven entries being ineligible, but no exact runtime 100% claim is made. The adapter accepts only one scalar token for this trigger in the successful exact cases and cannot represent the required multi-technology set.

The CBRN sensitivity attempt returned `PROBABILITY_SWEEP_RANGE_REQUIRED` with exact blocker `Every sweep path requires a scenario range, numeric alternatives, or numeric state value` for path `has_tech`; no threshold or rank-reversal result is claimed.

## Mengele current scenarios

`common/script_constants/germany_mengele_constants.txt:233-251` sets all 12 `directorate_special_project_availability` weights to 100, including `black_plague_weight = 100`. The current 12-entry candidate pool was supplied explicitly in every evaluation. The scenario state supplied numeric roll variables, but it did not supply all availability/completed country flags or the enclosing random-availability guard. MCP therefore emitted `PROBABILITY_MODIFIER_UNSATISFIED_IN_SCENARIOS` infos for the factor-zero flag modifiers. These results are exact for the declared numeric roll values and conditional on all those flag factors being inactive, not complete runtime-state proofs.

### `mengele_all_project_rolls_100`

All 12 roll variables were declared as 100. The JSON artifact is [probability-07e01082124d7f00f1e11a75.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79a464d9095ed523804324ffdeec2deadc216a7f377b87de59bb89936728998c/05d1e95ef21e32686413486569b78112c4b2cddaefebfb916705a7b5cd62f2d9/probability-07e01082124d7f00f1e11a75.json). The analysis ID is `probability-07e01082124d7f00f1e11a75`, source revision is `386e3111f33c151981209ef56db2622222793e9f6fd784691a9600834d34f541`, and source hash is `8cc2a5e0368231779a1f6f12b02365e9faae744d36cafa32fb39838eb71cb0fe`.

The MCP ranking rendered all 12 entries at 8.333% each, equivalent to 100/12. Black Plague is therefore tied with every other project in this synthetic all-open roll state and does not dominate. The recorded baseline with 11 projects at 100 was 1/11 = 9.0909% each, so adding the Black Plague entry dilutes every existing candidate by 0.7576 percentage points.

### `mengele_cloning_roll_0_others_100`

Cloning was declared 0 and the other 11 roll variables 100. The current ranking artifact is [probability-probability-57bfa8294eb87c295cbf779b-ranking.svg](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90351aae9175801ef16458a03ecaa65c72ea605cc1763db943f8237373776f32/97f5142edc73a0c1a945df84da6c074cff3c15d2571745c8cc99a5240a4d3fbf/probability-probability-57bfa8294eb87c295cbf779b-ranking.svg). The MCP result is exact for those numeric rolls: cloning is 0%, and each of the other 11 entries, including Black Plague, is 1/11 = 9.0909%. MCP emitted the expected `PROBABILITY_STARVED_OUTCOME` warning for cloning. The recorded 10-entry baseline after cloning was 10% each, so the current extra registry entry dilutes each surviving candidate to 9.0909%.

### `mengele_temporal_roll_100_others_0`

Temporal was declared 100 and the other 11 roll variables 0. The JSON artifact is [probability-bd241cc67e981b00e55a25ed.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06deaf361d4e045ed12e8344599754874ef7df4e6d6b5cfe1b40e01cc91d9b3d/6d1d593b551ecd707feb5018fff770b8adb106e864cb3f4c3d05fd2825c8653f/probability-bd241cc67e981b00e55a25ed.json), and the ranking SVG is [probability-probability-bd241cc67e981b00e55a25ed-ranking.svg](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f76a2aa1901f3bc8a2e3d5b1a44628e6aeef976e9e0afbed1c347dfbc689199/518497e309d3c8ff672ce2e6b1c77e014d86b025e1ca2823f9b2f5c89b8dfd2b/probability-probability-bd241cc67e981b00e55a25ed-ranking.svg). Temporal is 100% and every other entry is 0% under the declared numeric roll state. MCP reported the expected dominance and starvation warnings. The recorded baseline temporal-only result was also 100%, so the Black Plague addition does not change this deliberately forced scenario.

The required Mengele sensitivity attempt with path `state.directorate_special_project_cloning_roll` returned `PROBABILITY_SWEEP_RANGE_REQUIRED` because the path had no range. A second path-form probe without the `state.` prefix produced only one sweep point, so it is not a sensitivity result. The one-point sweep analysis is `probability-42a176561d4e32d76f6de5d0`; its sensitivity artifact is [probability-probability-42a176561d4e32d76f6de5d0-sensitivity.svg](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a35f420851fc2320685a97b19a81e087841c2c29633bf6d6ee97398e32cf05ba/b75f2a5d91a697df6e122347bf3443f7b3371be146fc913fc363b53c3f578fd5/probability-probability-42a176561d4e32d76f6de5d0-sensitivity.svg). No threshold or rank-reversal conclusion is made.

## Raid AI support

The native `ai_will_do` block in `common/raids/016_brilliant_scientist_portal_raids.txt:52-86` was probed with `hoi4.probability_inspect`, adapter `ai_strategy_factor`, against the exact raid source. MCP returned status `error`, code `INTERNAL_ERROR`, empty diagnostics, empty files-scanned list, and no artifact. The source contains raid-specific `ai_will_do`, not a supported focus, decision, mission, or strategy-factor surface. The route is therefore blocked and no raid score, rank, dominance, starvation, or target-validity probability conclusion is made.

## Findings, risks, and recommended owner follow-up

The Black Plague CBRN weight is 8, equal to the existing tularemia, zombie disease, and sarin entries. It lowers every pre-existing all-open probability because the denominator grows from 56 to 64, but it creates no dominant outcome. Anthrax exclusion similarly produces a stable weight ordering with plague highest at 18.5185%.

The Black Plague Mengele roll is 100, equal to every existing project weight. It changes an 11-way all-open tie from 9.0909% each to a 12-way tie at 8.3333% each. It changes the cloning-zero tie from 10 surviving projects at 10% each in the baseline to 11 surviving projects at 9.0909% each. Temporal-only remains 100%.

Positive-weight dead or completed choices cannot be ruled out by the current Mengele evidence because the MCP scenario did not carry the full set of availability/completed flags. The source has factor-zero gates for each such flag, but the adapter reported those modifiers as unsatisfied rather than proving a complete flag-free state. The owner should rerun with every availability and completed flag explicitly false and the enclosing `directorate_special_project_random_availability_granted` guard declared.

Repetition, cooldown, recovery, and terminal-state behavior were not sequence-proven. The random-list adapter advertises `sequence = false`, and no `probability_sequence` call is valid for these source pools. Source review shows availability/completion gates intended to suppress already granted projects, but that is not a substitute for a stateful sequence result.

The owner should preserve the current 8-weight CBRN entry unless a deliberate balance target changes it, add an MCP-compatible set-valued trigger representation for the one-candidate-left case, cache or expose the recorded baseline analyses as weighted source identifiers before the next compare pass, and provide a dedicated raid-AI probability fixture or adapter for the portal raid `ai_will_do` block.

## Skipped analyses and uncertainty

No valid historical `probability_compare` artifact was produced because the parent-recorded baseline identifiers are not present in the current MCP weighted-source cache. The exact MCP blocker is recorded above.

No exact CBRN one-candidate-left probability was claimed because MCP withheld normalization for the incomplete pool and could not compare a multi-token `has_tech` state. The 100% figure is source arithmetic only.

No raid AI probability, target race, or exploit conclusion was claimed because the native raid route returned `INTERNAL_ERROR` and the final adapter probe was terminated after hanging while trying unsupported alternate adapters.

The only file added by this subagent is this handoff Markdown file. Gameplay and source files remain untouched.

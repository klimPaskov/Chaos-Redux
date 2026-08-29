# Event 19 dynamic unit-provider probability audit — 2026-08-22

Status: read-only audit complete with MCP evidence partial where the provider registry is meta-dispatched. No gameplay, AI, event, decision, registry, localisation, or runtime file was edited by this audit.

## Executive finding

The provider API migration does not introduce a numeric weight change in the inspected Event 19 selection paths. The automatic native-provider selector remains a proportional random draw over eligible registry rows, while Evolution IV first-family reception remains a highest-weight score race. The selected-family request, sustainment, containment, and disperse decisions remain disabled for AI with `base = constant:infantry_spawn_factor.disabled`, whose source value is `0`.

The MCP analyzer cannot prove normalized provider odds because the registry is built through dynamic arrays and meta-dispatched callbacks. The complete provider candidate pool was declared as nineteen IDs, but `custom_weighted_pool` discovered zero candidates and returned `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`. The direct random-list adapter discovered the nineteen list entries, but all effect-derived temporary weights remained unresolved. No exact provider probability, dominance, starvation, rank reversal, or timing claim is made.

## Scope and source surfaces

The audit covered the following weighted or probability-bearing surfaces.

- Automatic native-provider selection: `common/scripted_effects/019_infantry_spawn_core_effects.txt:198-264`, symbol `infantry_spawn_select_native_registered_family`.
- Evolution IV first-family reception score race: `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:1090-1148`.
- Provider eligibility and management callbacks: `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:559-606`, `:766-948`, `common/scripted_effects/014_cannibalism_effects.txt:19440-19580`, and the provider callbacks registered by `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.
- Selected-family management and request/sustainment gates: `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:331-389`, `:770-805`, `:824-870`, and `:1244-1334`.
- Selected-family AI decisions: `common/decisions/019_infantry_spawn_decisions.txt:680-768`.
- Ordinary request-mode AI decisions: `common/decisions/019_infantry_spawn_decisions.txt:495-668`.
- Direct random-list axes: `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:1673-1780`.
- Custom equipment and presentation dispatch: `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt:4180-4200`, `common/scripted_effects/019_infantry_spawn_management_effects.txt:4551-4588`, and provider `event19_get_presentation`/`event19_publish_custom_equipment_tokens` callbacks.
- Static roll values and AI factors: `common/script_constants/019_infantry_spawn_constants.txt:1544-1554` and `:2020-2078`.

The complete provider pool supplied to the custom adapter was `501`, `502`, `503`, `504`, `505`, `506`, `507`, `508`, `509`, `510`, `511`, `512`, `513`, `514`, `518`, `520`, `521`, `522`, and `523`.

## Named scenarios and completeness

The nine required scenarios were submitted in `event19_dynamic_provider_registry_2026_08_22_final` with the complete nineteen-ID pool.

| Scenario ID | Declared state | Pool completeness | Result classification |
| --- | --- | --- | --- |
| `pre_evolution_iv` | Pre-Evolution IV, no saturation, ordinary mixed providers | Declared 19, adapter discovered 0 | Unresolved provider probability |
| `evolution_iv_low_saturation` | Evolution IV, low saturation | Declared 19, adapter discovered 0 | Unresolved provider probability |
| `evolution_iv_high_saturation` | Evolution IV, high saturation | Declared 19, adapter discovered 0 | Unresolved provider probability |
| `trainable_provider` | Evolution IV, trainable-provider mode | Declared 19, adapter discovered 0 | Unresolved provider probability |
| `spawn_only_provider` | Evolution IV, spawn-only mode | Declared 19, adapter discovered 0 | Unresolved provider probability |
| `provider_508` | Provider 508 unlocked | Declared 19, adapter discovered 0 | Unresolved provider probability |
| `provider_523` | Provider 523 active and registered as spawn-only | Declared 19, adapter discovered 0 | Unresolved provider probability |
| `ineligible_provider` | One provider marked ineligible | Declared 19, adapter discovered 0 | Unresolved provider probability |
| `malformed_missing_registry_row` | Registry row missing or malformed | Declared 19, adapter discovered 0 | Unresolved provider probability |

The state fields were explicit scenario declarations, not runtime execution. Evolution stage, saturation, provider mode, unlock/activity flags, native status, registry alignment, missing-row state, and external factors were not inferred from memory. The custom adapter reported `candidatesFound:0`, `unresolved:19`, and withheld normalized probabilities in all nine scenarios.

A narrow control-pressure pass was also run in `event19_registered_provider_control_pressure_523_addition_2026_08_22` with the same nineteen-ID pool and Provider 523 registered and active.

| Scenario ID | Declared control pressure | Result |
| --- | ---: | --- |
| `low_control_pressure_provider_523_added` | `0.0` | Custom pool unresolved; 0 candidates discovered |
| `medium_control_pressure_provider_523_added` | `0.5` | Custom pool unresolved; 0 candidates discovered |
| `high_control_pressure_provider_523_added` | `1.0` | Custom pool unresolved; 0 candidates discovered |

These three states prove only that the requested inputs were declared to the adapter. They do not prove that control pressure changes provider odds. Source review shows no control-pressure modifier in `infantry_spawn_select_native_registered_family`; the selector sums registry spawn weights after eligibility and draws from that sum.

## MCP artifacts and provenance

All artifacts below are read-only resources from workspace `mod_chaos_redux_ea3b2d67c2c0`.

### Probability inspection

- Custom provider source inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ea8ea4856d945a805f6f414c01d898b5c2a00463c9395564cd051827d18bc7ba/39a1855948c864d93ac4a74e9c28b4aff1f4cadee8d2a3b54866f2c8db948bf9/probability-inspect-653cce9f7279.json`; source revision `2a6d3c2ad32e7bddae9dd023bf05785dbdea18983451d75dacb93c93bc2a6985`; source hash `653cce9f727921cf8f09c1aedee9442f9bee07c2f8e8f831373e3bb700400bb3`; custom pool candidates `0`.
- Direct random-list inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f9b7d4bb06f4a64974aba18c63c9d90b26151e7bfe6fef63ff4503afa55caf6/ba6e7c7c2acfc34772525e7ee03887bbf67c196fc7f90c1009ff54804ff4157c/probability-inspect-e35eee038249.json`; source revision `ce75e3330c30e3d3e6c2ec7adc16cd1fc984d25bd859f12adf9a026ab3613b74`; source hash `e35eee0382498ef06213cba734a80f967b3b4128244f7456e3965a1998c97dd4`; 19 random-list entries and one unresolved input.
- Decision AI inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ce19ed4ad020b151faa1e7103701b6a1a93950f5fdb1905e6925f664353782d/44f16bcab77ae445ae28f6cafe9747272ef8aa1e47f2d128c135b3af95589555/probability-inspect-f1f83c730d7d.json`; source revision `ceb2e4e639b4deb30fc766bf9cd7ce07acc442f15edbef6849ebcc4c25db125b`; source hash `f1f83c730d7da66da77bf0166562f6e1d33b261d6ab72567777827196b4c787b`; 40 source decisions, score-only adapter.

### Provider-pool evaluations

- Required nine-scenario custom evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d23b9e763b047126b5e3558fb91995a6dbab242837a3923b8eddff32bded9f2/b4f8466ac7c9834cdb63850a0fc56d0798bb668ebc514640ca9c8fb87e3479fc/probability-a4b6e0d6d93da25cba9885b0.json`; analysis ID `probability-a4b6e0d6d93da25cba9885b0`; source revision `5b9fbe49eaba914f95e450d4f67f36085d76d200b598a6d1fa167719dc69470d`; source hash `653cce9f727921cf8f09c1aedee9442f9bee07c2f8e8f831373e3bb700400bb3`; scenario hash `a907814920f4d34564dc77e4cbdacdfb273b8c0b749feca5c61c7bd459aebbd8`; 9 scenarios, 0 candidates, 19 unresolved.
- Required custom ranking render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41f8b4cf218da9cc2fbd543cf51a87e6508269cb1a025b91e7bf6c542be6cf8d/6fe2825f108de82be543f4b1d6f95988a694e9a9964502e9df5deb35dcbf9e23/probability-probability-a4b6e0d6d93da25cba9885b0-ranking.svg`.
- Required custom matrix render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dda4ae4fbc238120a84eac39bc8160ba53ace0462287b1c1fb818e3938fee5bc/44e4c2c136276ec87e28094920ceb544fc2397eaa8dd2cd20597cbcee11f4488/probability-probability-a4b6e0d6d93da25cba9885b0-matrix.svg`.
- Required custom unresolved render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70a1c018bb701b4748866e2e5d330eadb5151d716f993e02db44b933d9da1d1a/00eaeb7e74a83693f86bb5d707843eddde0be83a46dab4727c68860605125f49/probability-probability-a4b6e0d6d93da25cba9885b0-unresolved.svg`.
- Narrow low/medium/high control-pressure and Provider 523 evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6d299347b3639755460ccf9ac21d2a1beaa3f906ace8f8dac0a693dbe94868a7/84edc78a991eab51a1dfd7fa7acc744a0153fb5d13465849b0f1ccea732a9f68/probability-374cd43ca5e37c6bedf8cbc9.json`; analysis ID `probability-374cd43ca5e37c6bedf8cbc9`; source revision `fe1bc23660e381c6f93222219b6c556759ca4741961e18d6e68ee7b15c638fe7`; source hash `653cce9f727921cf8f09c1aedee9442f9bee07c2f8e8f831373e3bb700400bb3`; scenario hash `b8219c5f20f5ee856d5e1f43f2dfa67445999cafc81fc3e1946f45850b6a8f3c`; 3 scenarios, 0 candidates, 19 unresolved.
- Narrow control-pressure ranking, matrix, and unresolved SVGs are respectively `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f5175e43b2e76a68de7ada9bc9d4d02a720dc32837ef84c520a87f632717a601/7c3fcf11675ddd42d045bc236ee8f1aa930f6fdd0d1e416985a88c4a8476455f/probability-probability-374cd43ca5e37c6bedf8cbc9-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5800c9e83095cd3cc79d139f0c0d5ff75746e2510916e4d963d8f7f3efc4b0c6/ac7581194c2c88566838847b75d4571d57e6e55559af635c77a3924a0dcb1977/probability-probability-374cd43ca5e37c6bedf8cbc9-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/70a1c018bb701b4748866e2e5d330eadb5151d716f993e02db44b933d9da1d1a/76b5eda86e59178564bb6610a16b6c4f98e828439e1b9514121a1f8415f0f14b/probability-probability-374cd43ca5e37c6bedf8cbc9-unresolved.svg`.

### Direct random-list evaluation

- Direct random/list evaluation over the four axes and three control states: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a59b9cbd6c6c49930a5c7ca1500a1f7bed7d28cde30a86ae7e7541da2d03234/d2521b1e5f026bc13fa3b431723a4a9ac23d25f181dc4a5c1a57812d2d08c49c/probability-8db0257891da5fd1769e4a15.json`; analysis ID `probability-8db0257891da5fd1769e4a15`; source revision `5b9fbe49eaba914f95e450d4f67f36085d76d200b598a6d1fa167719dc69470d`; source hash `e35eee0382498ef06213cba734a80f967b3b4128244f7456e3965a1998c97dd4`; scenario hash `3ecb6cf85a4671f369b46bd9cf4e093116b6e16d17b0b13c9de243e210783dda`; 3 scenarios, 57 candidate instances, 20 unresolved, `candidatesFound:19`.
- Direct random/list ranking, matrix, and unresolved SVGs are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9759588722d9013f87eef9533a00e75ca0e948e24efb7b7c75fdf2f1b9633ef5/ec76490591ac8f2d394387e7076d2d0bbd0304f6d95753220491735a875be427/probability-probability-8db0257891da5fd1769e4a15-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fc4f5e977223c9426fc43e6feb40a31af64035fc809e44e1429b807ca9b678e/9c62bc27cdbb5d2975beddf37afdc9d5de8e5871c8ac93f12ca1006057ff0e87/probability-probability-8db0257891da5fd1769e4a15-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a03bcc8beab9d366f6aa3b3f8d55c0e022af99601434e2360fb4e8c2d6904efe/efce5e0246579ed0e5d774fd2fd01b4c2750022d869692f8a5949aaf2c81fc04/probability-probability-8db0257891da5fd1769e4a15-unresolved.svg`.

### AI decision reachability evaluation

- Narrow request/sustain/contain/disperse evaluation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20ce50946fad151eb8fe3c0da4ac25867d7962f18a5775496d2f18094e21c6c1/811206b2e6532229fbd3f95c40c733b6b3a70cccb1411065d80ce4d49b24a1a6/probability-ff16397f124c707722cd8e31.json`; analysis ID `probability-ff16397f124c707722cd8e31`; source revision `cab5ee325fedf027f9f272619667824281268d4df53dc523c50e98013611b18e`; source hash `f1f83c730d7da66da77bf0166562f6e1d33b261d6ab72567777827196b4c787b`; scenario hash `1502b40706e8dd767136c35f6d1bf55c794f53d885ec4a382e520e6cada899b1`; 3 scenarios, 12 candidate instances, 42 unresolved, one `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` diagnostic for `infantry_spawn_request_selected_anomalous_family`.
- Narrow decision ranking, matrix, and unresolved SVGs are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a9921c959c500e4003fe2767c1ddb96c50ecf2f5dbef4b3fa510d1eacbb617d4/d85d6790f831b8b9b71f844427b3281dd02fb08073827b733a9ed6aad0c12995/probability-probability-ff16397f124c707722cd8e31-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26df980003e49e7314d451df818dfb165a49f83a1b6995263178ce75d6ec72e6/f4aa56ffeec2faa3b2b1772386212d3d2c4e930142db9629a08056ec20b25770/probability-probability-ff16397f124c707722cd8e31-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/64162208163251e6508111844bcff6b460dbf08add1f6eebb58319a2e3d28510/745f11b18b812fb7d4fe3bb314bce066ae8ee07331dbfbf05bd092a8902d3aa7/probability-probability-ff16397f124c707722cd8e31-unresolved.svg`.
- Broad request and selected-family decision evaluation over all nine named scenarios was `probability-71961e55b33059a802596db4`, source revision `28472b8caa7d6ff93c81ac9096c8ad41d77025b92c3f35b660762436e0a003fa`, scenario hash `722f15f6d6b172fcede63cae2641da0b1905e0cefa8645ab19e7cc739c36830f`, with 16 requested decisions, 144 candidate instances, 282 unresolved items, and ten never-eligible diagnostics for the ordinary request modes plus selected-family request.

### Structural Event 19 evidence

- `hoi4.event_inspect` lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/600a05f0443b4f2969f715c9b7dd35a19306d283ed8b80803d3637ca1910b8e1/04c26f0788d293ad7dc48f1f94df5cc5f618dbd62a00a36f03074ae6567ebbcb/event-lint-43f28961e452.json`; revision `43f28961e452ee9147c2bc9565b2a9f354c751e78f69c6892498ef3d90378e52`; graph hash `eee1d68305cdc84418fcf1034fce602d7df00a4eab2455f32de0d0374ebbcaf6`; status `EVENT_INSPECTED_PARTIAL`.
- `hoi4.event_render` unresolved manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d7d4288211886ba1a5cc86aa2c128764994794dba98285e708f72506ecb98ce1/0b82c42ce10bf15d4b666b9a9edc5ec3f4062e38a1f208975523d3c332cea2f5/event-unresolved-43f28961e452-manifest.json`.
- Event unresolved SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/18ff4799f1801ab38a8356e4bd693ce42d4ce1f8b4e3d0041f7c4ce7e35c37c8/25b581a7c13fff5c0106e1ca23ab4151465bf11ec25d139958b5920cabd3b9f4/event-unresolved-43f28961e452.svg`.

An explicit `hoi4.probability_render` request was also made for the custom nine-scenario analysis. It returned `PROBABILITY_ANALYSIS_STALE` because concurrent workspace changes advanced the current revision from `5b9fbe49eaba914f95e450d4f67f36085d76d200b598a6d1fa167719dc69470d` to `6c8703ac00cc5a23f9364b45df6b7ee9e9dca63262b311ed242847247dca3a86`. The evaluate calls themselves produced the ranking, matrix, and unresolved resources listed above.

## Source-derived weighting and validity findings

### Automatic provider selection

`infantry_spawn_select_native_registered_family` first requires an aligned registry, enabled row, native-draw permission, spawn permission, and supported visual contract. It then meta-dispatches `chaos_unit_family_provider_[PROVIDER]_event19_evaluate_eligibility` and includes only rows with `chaos_unit_family_candidate_native > 0`.

The selector sums `global.chaos_unit_family_spawn_weight_entries^index`, draws an integer from `1` through the inclusive total using `max = total + 1`, and subtracts each eligible row weight until the selected row is reached. This is exact source-derived proportional-categorical structure, not a highest-score race, but the MCP cannot resolve the provider pool or callback outputs and therefore cannot provide normalized odds.

No control-pressure modifier is applied in this selector. Low, medium, and high control pressure can affect request-mode random-list biases and decision availability elsewhere, but it does not directly change the registered provider spawn-weight sum in this function.

### Evolution IV first-family reception

The first-family reception loop uses the same static row and provider eligibility gates but retains the row with the greatest positive spawn weight. The comparison is strict `>`; equal weights preserve the first encountered row. This is an exact score/rank invariant and must not be reported as a probability. The selected row is frozen before the delayed reception event and is not substituted by a later provider callback.

### Provider 508

`chaos_unit_family_provider_508_register` sets availability to `spawn_only` and stores its constant spawn weight. Its eligibility callback returns eligible/native only after the Event 16 alien-infantry unlock gate. Its management callback has no training or separate sustainment payment path, and the landing path materializes a fixed cohort. The callback is therefore a deterministic eligibility gate plus a constant registry weight, not an independent AI weight.

### Provider 523

`chaos_unit_family_provider_523_register` sets availability to `spawn_only`, family-only lot policy, and the constant cannibal-irregular spawn weight. Its eligibility callback requires `cannibalism_system_active`, incomplete cleanup, and either a cannibalism country or Evolution IV. It sets `candidate_native` only for a cannibalism country, so Evolution IV can make Provider 523 eligible without making it a native automatic-draw candidate. Its management callback always leaves `can_train = 0`, enables spawn only while the system is active and cleanup is incomplete with an eligible state, and enables sustainment only when live divisions exist under the same active, not-cleaned-up conditions. This source contract prevents Provider 523 from entering a training branch, but MCP cannot calculate its normalized share of the provider pool.

### Trainable, spawn-only, ineligible, and malformed rows

Event 16 provider management distinguishes trainable clone/Aryan branches from spawn-only or resource-gated branches. Management flags are deterministic availability outputs (`can_train`, `can_spawn`, `can_sustain`, and `uses_training`), not provider selection weights.

An ineligible provider is excluded when its provider eligibility callback leaves `candidate_eligible` or `candidate_native` at zero. A malformed or missing registry row is blocked by alignment, index, enabled-row, contract, visual, and provider-ID validity checks before it can contribute weight. These are source-derived safety invariants; exact zero-probability claims remain unresolved when the adapter cannot execute the callback and row state.

### Direct random/list logic

The four independent axes are quality, coherence, combat target count, and support target count. Their base weights are the centralized constants `15/50/25/10`, `20/35/35/10`, `8/24/42/18/8`, and `15/25/25/20/10/5`. Control, congestion, request repetition, numbers, discipline, firepower, and related biases are added to temporary weight variables before each `random_list`.

The random-list adapter discovered the nineteen entries across the four lists, but the temporary effect-derived weight variables remained unresolved. The MCP therefore supplied no exact axis probabilities or sensitivity/rank results. The `set_temp_variable_to_random` target-count draws use the declared minimum and maximum-exclusive bounds; they are separate from provider-family selection.

### Presentation and equipment callbacks

The presentation callbacks publish name, request-cost, and sustainment-cost localisation tokens. The custom equipment callbacks publish or resolve equipment tokens for stockpile snapshots. Source review found no callback path that writes `chaos_unit_family_spawn_weight_entries`, candidate row weights, or decision `ai_will_do` values.

Presentation-token validity can remove a row from the visible management view or mark a ledger invariant failure, and equipment-token validity can block a later transaction, but these are post-eligibility validity gates. They do not create a positive weight for an invalid provider. Because the MCP cannot execute the callbacks, the absence of runtime callback failure is unresolved rather than proven by MCP.

## AI decision results

The narrow AI candidate pool was `infantry_spawn_request_selected_anomalous_family`, `infantry_spawn_sustain_selected_family_decision`, `infantry_spawn_seal_selected_family_breach_decision` (containment), and `infantry_spawn_disperse_selected_anomalous_lot_decision`.

All four source blocks use `ai_will_do = { base = constant:infantry_spawn_factor.disabled }`, and `infantry_spawn_factor.disabled = 0`. The decision adapter is `score_only`, with `normalizedProbability = false`; the raw score is not a click probability and no decision selection odds are claimed.

MCP reported `infantry_spawn_request_selected_anomalous_family` as never eligible across the three control-pressure scenarios. Its reachability result is an adapter diagnostic under the supplied state model, not a claim that every runtime campaign state makes it unavailable. Sustainment, containment, and disperse remained unresolved at selected-family trigger variables such as selected-row validity, GUI family index, transaction state, command power, and equipment/resource state.

The broad nine-scenario request and selected-family pass found the ordinary request modes at lines `495-668` and the selected-family actions at lines `680-768`. Ten never-eligible diagnostics covered the ordinary request modes plus selected-family request; the remaining selected-family decision triggers were unresolved. This is sufficient to establish disabled AI scores but not runtime reachability under a complete country state.

## Dominance, starvation, rank reversal, and exploit-risk assessment

No normalized provider probability, rank reversal, starvation rate, repetition rate, or dominance threshold was proven. The custom adapter lacked all nineteen candidates, and the random-list adapter lacked dynamic weights.

The source-derived ordering invariant is that an eligible native provider with a larger stored registry spawn weight has greater interval mass than a lower-weight eligible provider in the automatic selector. Provider 523 has no native interval in Evolution IV unless its native gate is separately true, even though its family may be eligible for management. Provider 508 has no interval until its unlock callback returns native eligibility. These are conditional structural statements, not normalized odds.

No presentation or equipment callback was found to inject an invalid candidate into either weighted pool. The remaining exploit risk is adapter/runtime coverage: a malformed callback, registry misalignment, or stale token can only be conclusively tested with a declarative callback manifest or runtime-backed MCP fixture.

## Sweep, compare, simulation, and sequence status

`hoi4.probability_sweep` was attempted for the custom provider pool and direct random-list dynamic weight paths. It returned `PROBABILITY_SWEEP_RANGE_REQUIRED` with the message `Every sweep path requires a scenario range, numeric alternatives, or numeric state value`; no threshold, sensitivity, or rank-reversal artifact was produced.

`hoi4.probability_compare` was intentionally not run. The migration contract specifies no numeric weight change, this audit applies no patch, and no before/after source pair exists. A comparison would not resolve the incomplete dynamic pool and would not add evidence for an unchanged weighting surface. If a future owner changes any weight, modifier, gate, or callback output, the same named scenarios must be rerun through `probability_compare`.

`probability_simulate` and `probability_sequence` were skipped because no uncertain distribution or complete cadence/cooldown/removal manifest was supplied. No timing-distribution claim is made.

## Recommended owner follow-up, without applying changes

- Add a read-only MCP provider manifest exposing all nineteen provider IDs, registry spawn weights, native/eligible flags, availability mode, and callback outputs for each named scenario.
- Expose numeric control-pressure ranges and callback-derived weight modifiers so `probability_sweep` can test low/medium/high breakpoints and rank reversals.
- Keep Provider 523's `spawn_only`, non-native Evolution IV eligibility, `can_train = 0`, and cleanup gates explicit in that manifest.
- Keep Provider 508's unlock/native gate and fixed-cohort spawn-only management path separate from training and sustainment weights.
- Add malformed-row and missing-callback fixtures that prove the row is excluded before any weight is accumulated.
- Re-run the same nine scenarios plus low/medium/high control-pressure scenarios after any source or manifest change, and use `probability_compare` only for a real before/after weight or gate change.

## Blockers and unresolved constructs

- `custom_weighted_pool` cannot discover the dynamic provider registry or meta-dispatched provider callbacks, returning `candidatesFound:0` and nineteen unresolved candidates.
- `random_list` discovers the four lists but cannot evaluate effect-derived temporary weight variables and therefore withholds normalized probabilities.
- Decision triggers require runtime country variables, arrays, GUI indices, resource values, and provider callback results that were not executable from the supplied scenario state.
- Event lint/render are bounded partial workspace analyses with deferred helper/lifecycle projections; the linked artifacts preserve the unresolved view.
- Concurrent workspace changes made explicit probability-render calls stale after evaluation. The evaluate artifacts and their source revisions, hashes, and scenario hashes are retained above.

No gameplay patch, source rewrite, commit, or destructive operation was performed by this audit.

# DHR diplomatic-reward and advisor probability baseline

Date: 2026-09-02

Status: prepatch baseline and corrected postpatch source comparison secured, read-only, partial and score-only where stated. No gameplay source, AI weight, cost, localisation, configuration, or balance file was edited by this auditor. No acceptance claim is made in this handoff.

## Scope and intended owner change

This audit covers the DHR focus tree and the two DHR political-advisor character definitions relevant to the diplomatic-reward plan. The planned owner change is limited to the `DHR_seat_the_human_delegates` and `DHR_open_the_translation_bureaus` focus rewards plus availability gates for `DHR_harmonic_envoy_rae_syl` and `DHR_shadow_listener_thel_ior`; focus count, layout, focus AI scores, advisor costs, advisor AI factors, traits, portraits, and localisation are intended to remain unchanged.

The intended postpatch advisor gates supplied by the plan are:

- `DHR_harmonic_envoy_rae_syl`: existing Covenant route and `dhrondan_human_delegates_seated` receipt.
- `DHR_shadow_listener_thel_ior`: `dhrondan_translation_bureaus_open` receipt and Imperial, Synod, or Covenant route.

The baseline therefore tests the named route and receipt states without treating focus selection scores as advisor appointment probabilities.

## Source retention

The initial standalone baseline used historical commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`; that commit is superseded for before/after comparison by the corrected immutable HEAD `957ae81cc6539c2e29beebe92f4c6523eea91532` recorded below.

| Surface | Path | Historical standalone baseline blob | Current prepatch raw SHA-256 used by evaluation |
| --- | --- | --- | --- |
| DHR focus tree | `common/national_focus/016_dhrondan_focus_tree.txt` | `48af75cf250f1d2c42b7e686ccb983876bc987c3` | `06772a28814d66eb83b10ca1d1ebe13c0791a754681077258f552949b2cf6baa` |
| DHR characters | `common/characters/016_dhrondan_characters.txt` | `f808699b6f98564287b7f1f2e80cc15068b10f3a` | `3799bcd6e49c646cef5f7429fef537978d0c42a2bdedd3beefbb6bfb8dd34292` |
| Focus scripted triggers | `common/scripted_triggers/016_dhrondan_focus_triggers.txt` | `ba2cf1c24ebef025b457ce683688f673e88ee32b` | `6f62ab464f3d887cb14de9823169e68b0a93d9f369f59b4dfd1d6db68e004c9d` |
| Focus scripted effects | `common/scripted_effects/016_dhrondan_focus_effects.txt` | `b867d667da1f4457f9da088a62a05fddbb469344` | `465548f7a580923efc475db0eb8b7df8de79d8257e936cae70233c23d5126352` |
| Focus constants | `common/script_constants/016_dhrondan_focus_constants.txt` | `1ede8f829f18a68b38c006ca63f891d4de21069f` | `d00841846bda43c3fbbd13045db3d6f33104d6bc3c46b1061151bf483980689d` |

The focus worktree source had seven unrelated concurrent additions around `DHR_resolve_the_enclave_crisis` relative to the historical standalone baseline; the target focus IDs and their AI blocks were not changed by that concurrent context. The corrected focus evaluation used the exact current pre-reward raw source hash shown above, while the historical commit blob remains standalone provenance only. The character source had no semantic worktree change relative to the retained baseline at capture time.

For the corrected postpatch comparison, the immutable before source is the exact `git show 957ae81cc6539c2e29beebe92f4c6523eea91532:common/national_focus/016_dhrondan_focus_tree.txt` body with Git blob `ca6ccf2f3b5ddd2b4d01527093747797dc723ea1`. The after source is the current focus path with Git blob `d4a4d8d72a86f427bfd23ce56eb62f6177410dc2` and raw SHA-256 `13ea41e8aed3a555c77840e00f2d62f4b93845589b7e9bea7ae8a9dfbf3dd624`. The earlier `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd` source comparison is superseded because it predates the accepted prepatch tree; the older `06772a28814d66eb83b10ca1d1ebe13c0791a754681077258f552949b2cf6baa` raw source remains standalone baseline provenance only, not the corrected compare input.

## MCP inspection and structural evidence

The mandatory first probability call was `hoi4.probability_inspect` with adapter `national_focus_ai_will_do` and source `common/national_focus/016_dhrondan_focus_tree.txt`. The initial discovery reported 88 candidates but no explicit pool, so a second inspect supplied the exact 88-focus candidate pool and returned `poolComplete=true`.

The initial focus inspect artifact is [probability-inspect-e7c8540c4e61.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca3854582c2202dcd90048a4af622b570c38e11c547e5270da987bda66329f4f/0301fe6937ff0d73e13affc9880b5dba146ae3399a0c0b3f9336fa3f358b1e96/probability-inspect-e7c8540c4e61.json).

The explicit-pool focus inspect artifact is [probability-inspect-e7c8540c4e61.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fbaf013a6c456a669d84f06bf9ab9e733e518e1fbc837ed6cd097d741a70856/e3350abd794257a5200e7fa9b3e9e008d6adcfb2b769abbea625b935fdb1fd5a/probability-inspect-e7c8540c4e61.json). It reports adapter `national_focus_ai_will_do`, 88 candidates, `poolComplete=true`, seven required inputs, zero unresolved inspect items, normalized source hash `e7c8540c4e61a8ea66a5b0b0d88305cacd1b8e566c4a36f9f1b15b8786e8ae14`, and source revision `cd07688dc26f8d989a9071e800368a543242cac1a4fad4dc78237adf32c7ff08`.

The DHR character source was inspected through the probability route without an invented advisor adapter. The result is [probability-inspect-a09cfa7da542.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/222c267cfe22fbb49dc8813366060d5144283b039cabb143ba8b589a4b480099/5e2dec880f81d4bd9eac90880aab1032d49940eb6d3a76e4aa8f66e8bb644458/probability-inspect-a09cfa7da542.json). It reports `discoveryReason=no_weighted_surfaces`, zero candidates, and no available adapters, with normalized character source hash `a09cfa7da542b65f7ce702a469b66c28bd25b58233594a3d555422a4b31858f5` and source revision `bfc06f6fab3f9eb4af5aad11400f4c1f6e35b8771ca1bea041b3f35a14389460`.

The structural focus inspect is [focus-inspect.7ce72b409a9bae95.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb693d42c369c3af70f43b84f15d1a67a7fc053b86f28e25b372b0cef1e2f6aa/5c45053818d4141a74015e0df11f50c88ea6b7a5accbc7fe5004a5e43dcd265f/focus-inspect.7ce72b409a9bae95.json). It reports tree `dhrondan_focus_tree`, 88 focuses, 102 connectors, layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`, and no layout crossings, intersections, or long connectors. The only diagnostic is an unrelated vanilla localisation reference for `continuous_restrict_freedom_desc`.

The read-only structural render produced [DHR focus SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289/56477df82ef711b8650ab4fa8c386646a3cddc1a8ef4bb7d6186edd21ff7c563/dhrondan_focus_tree.focus.svg), [DHR focus HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/748ffeb2a79bd6f5051fc503e32b4c2d57c50564f5937cf19f3317af5f5c33b0/3e47505d96599d50fb8cd205db0cdaaeb74a644d1c8b634c25f7e604b878cf1a/dhrondan_focus_tree.focus.html), and [DHR focus render JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a4528325a978d55a59d56cce288fd622747f3b7816f34c62538e5a3f6c41123/87c30881c3a322a94ba5e8f573e787400672459335f1bb26bae4ba7a6d448069/dhrondan_focus_tree.focus.json). The rendered dimensions are 6992 by 2788 with the same layout hash and only the unrelated vanilla localisation warning.

## Exact scenario fixture

The retained fixture is [E016_DHR_ADVISOR_REWARD_BASELINE_2026_09_02.scenarios.json](<C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/016_brilliant_scientist_plans/subagent_handoffs/E016_DHR_ADVISOR_REWARD_BASELINE_2026_09_02.scenarios.json>).
Parent promoted the unchanged fixture bytes from the temporary workspace after the comparison; its SHA-256 remains identical.

Fixture SHA-256: `e9902e866e322e9a13377091fee5079d4ac2c67ba7fe170485079766b1ecc1e5`.

The MCP scenario hash is `2db1f0f978c372b62d7261a12d480cce4302f2830f1a737ec68d1d35d7369f77`.

The fixture contains 11 named scenarios and declares `exists`, `is_subject`, neutrality government, peace, stability `0.60`, `world_end=false`, `terminal=false`, route/receipt flags, and political power. Event targets and scopes are empty.

The exact scenario IDs are:

- `E016_DHR_COVENANT_BEFORE_DELEGATES`
- `E016_DHR_COVENANT_AFTER_DELEGATES`
- `E016_DHR_IMPERIAL_BEFORE_TRANSLATION`
- `E016_DHR_SYNOD_BEFORE_TRANSLATION`
- `E016_DHR_COVENANT_BEFORE_TRANSLATION`
- `E016_DHR_IMPERIAL_AFTER_TRANSLATION`
- `E016_DHR_SYNOD_AFTER_TRANSLATION`
- `E016_DHR_COVENANT_AFTER_TRANSLATION`
- `E016_DHR_NO_REGIME`
- `E016_DHR_ADVISOR_UNAFFORDABLE_100PP`
- `E016_DHR_ADVISOR_FULL_SLOTS`

The `E016_DHR_ADVISOR_UNAFFORDABLE_100PP` row declares political power 99 against the 100 political-power advisor cost. The `E016_DHR_ADVISOR_FULL_SLOTS` row declares `political_advisor_slots_available=0` as a fixture annotation, but that is not a recognized source-backed country trigger in the current adapter and is therefore unresolved rather than proof of slot blocking.

The complete focus candidate pool supplied to both probability inspections and the evaluate is:

```text
DHR_beneath_an_alien_sky
DHR_count_the_landing_states
DHR_secure_the_scattered_enclaves
DHR_inventory_the_expedition_stores
DHR_restore_the_landing_beacons
DHR_bind_the_enclaves
DHR_reopen_the_orbital_channel
DHR_convene_the_two_world_throne
DHR_vael_ix_takes_the_throne
DHR_restore_the_ninth_diadem
DHR_bind_the_landing_lords
DHR_codify_imperial_service
DHR_raise_the_palace_guard
DHR_proclaim_the_right_of_return
DHR_crown_the_enclave_empire
DHR_the_unbroken_imperial_line
DHR_sera_qel_presents_the_calculus
DHR_audit_every_command_node
DHR_elevate_the_first_calculants
DHR_publish_the_survival_equations
DHR_assign_merit_by_projection
DHR_replace_decree_with_prediction
DHR_enthrone_the_synod
DHR_the_government_of_certainties
DHR_ilyr_ren_opens_the_chamber
DHR_seat_the_human_delegates
DHR_write_the_dual_citizenship_code
DHR_elect_the_landing_councils
DHR_guarantee_the_right_to_depart
DHR_submit_the_military_to_debate
DHR_ratify_the_two_world_covenant
DHR_the_chamber_of_two_skies
DHR_relight_the_field_laboratories
DHR_recover_the_laser_forges
DHR_convert_terrestrial_workshops
DHR_crystal_growth_chambers
DHR_the_twenty_element_substitution
DHR_standardize_alien_components
DHR_feed_the_landing_reserve
DHR_the_exoplanetary_materials_board
DHR_join_the_scattered_laboratories
DHR_a_two_world_research_complex
DHR_restore_the_predictive_staff
DHR_map_the_probability_front
DHR_encode_the_enemy_reaction
DHR_train_human_signal_teams
DHR_rebuild_the_expeditionary_cadres
DHR_fire_control_by_forecast
DHR_supply_before_the_order
DHR_the_thousand_branch_wargame
DHR_delegate_to_the_field_calculants
DHR_command_without_surprise
DHR_the_foreseen_counterstroke
DHR_perfect_predictive_warfare
DHR_reassemble_the_orbital_office
DHR_chart_terrestrial_air_corridors
DHR_adapt_the_gravity_fighters
DHR_salvage_the_shuttle_docks
DHR_link_airfields_to_the_relay
DHR_form_the_exile_flotilla
DHR_guard_the_descent_windows
DHR_make_near_space_ours
DHR_open_the_translation_bureaus
DHR_listen_to_the_human_airwaves
DHR_trade_in_impossible_materials
DHR_exchange_maps_for_access
DHR_seed_the_enclave_network
DHR_recruit_two_world_operatives
DHR_choose_our_terrestrial_partners
DHR_the_embassy_beyond_the_stars
DHR_define_the_two_worlds_question
DHR_restore_the_imperial_reaches
DHR_demand_the_origin_host
DHR_the_subject_world_protocol
DHR_calculate_the_reclamation_zones
DHR_subordinate_borders_to_need
DHR_administer_the_optimal_order
DHR_invite_the_enclave_congress
DHR_negotiate_the_origin_settlement
DHR_federate_the_two_worlds
DHR_begin_postwar_integration
DHR_a_place_in_the_world_order
DHR_the_enclaves_refuse_the_ledger
DHR_offer_a_shared_horizon
DHR_break_the_separatist_ciphers
DHR_resolve_the_enclave_crisis
DHR_reopen_the_homeworld_corridor
DHR_the_century_beyond_exile
```

## Bounded focus evaluation

The corrected bounded call was `hoi4.probability_evaluate` with adapter `national_focus_ai_will_do`, the current prepatch raw source hash `06772a28814d66eb83b10ca1d1ebe13c0791a754681077258f552949b2cf6baa`, the exact 88-focus pool, and the unchanged 11-row fixture. It requested `raw_value`, `conditional_probability`, JSON, ranking, matrix, and unresolved outputs.

The main result is [probability-03d7465215712f342ab36723.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/046fb78f33f0142908f150fb40e680b1cde1e75a54761ba9171c0e837cb45ca9/1f6cb3375328c3d87e65879828a0f372d5fd1989180dcebe8558eaa6c2f6a3c3/probability-03d7465215712f342ab36723.json).

The evaluate analysis ID is `probability-03d7465215712f342ab36723`, with partial status, normalized source hash `e7c8540c4e61a8ea66a5b0b0d88305cacd1b8e566c4a36f9f1b15b8786e8ae14`, source revision `8e647790570c2375786bb1cb7a87c52d2b3be875e439c0c2c94299cbc7457952`, scenario hash `2db1f0f978c372b62d7261a12d480cce4302f2830f1a737ec68d1d35d7369f77`, 11 scenarios, 968 candidate rows, 93 unresolved items, two diagnostics, and six visual resources.

The adapter describes the selection rule as `uniform_score_race`, not probability-proportional selection. It supports raw scores and normalized probability in principle, but requires a complete eligible pool plus declared prerequisite-completion and external strategy-plan factors. The returned candidate rows have `conditionalProbability=null` and support `external`, so this run is not exact normalized probability evidence.

The target focus rows produced these bounded baseline results:

| Focus | Baseline source behavior | Raw score | Fixture eligibility result | Classification |
| --- | --- | ---: | --- | --- |
| `DHR_seat_the_human_delegates` | `available = { dhrondan_focus_is_covenant = yes }` | 10 (`@dhr_ai_preferred`) | true in Covenant rows and false in Imperial, Synod, and no-regime rows | score-only/bounded; external factors unresolved |
| `DHR_open_the_translation_bureaus` | no translation-receipt or regime availability gate in baseline | 5 (`@dhr_ai_standard`) | true in all 11 declared rows, including before-translation and no-regime rows | score-only/bounded; external factors unresolved |

Both target rows retain one unresolved `FOCUS_EXTERNAL_FACTORS_UNDECLARED` item in each scenario. The complete evaluate also reports 88 external-factor unresolved items and five trigger-unresolved items across the whole pool. Two never-eligible warnings concern late crisis focuses in this fixture, `DHR_break_the_separatist_ciphers` and `DHR_offer_a_shared_horizon`, and are not findings against the diplomatic-reward change.

The ranking, matrix, and unresolved render artifacts are [ranking SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c87e41ad913152c31601cd9741dd24068148a6b2e69794dc17678054f722267/aa7f89f5bf62ec4fc95d4e7713c826acc7ae34b125158f2a4acf158a5dfa78dd/probability-probability-03d7465215712f342ab36723-ranking.svg), [matrix SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fc3eac7e7ab0ea75f198cb3edfdf0071b1b9306a55d19a8594f87d07d5ebda6/99d19e726185ab0472ca5712665d114e6120f906b0791ba8f65beec65bb17d0e/probability-probability-03d7465215712f342ab36723-matrix.svg), and [unresolved SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9aa61273cb65c0a395b7806417cd34e0c5bdf9e7341ff3dc343c534374c13b05/0ca25474b488376646f1c7e4a80c4dbc879c45c35f4a85f3f620229924390d08/probability-probability-03d7465215712f342ab36723-unresolved.svg).

No exact focus-selection probability, ranking dominance, starvation, rank reversal, repetition rate, timing distribution, or exploit-risk conclusion is supported by this partial run. The 88-focus pool is complete as a declared source pool, but the scenario does not provide all focus completion, ordered strategy-plan, prerequisite multiplier, and external-factor state required by the adapter.

## Corrected postpatch source comparison

The required current `hoi4.probability_inspect` used adapter `national_focus_ai_will_do`, the exact 88-focus pool, and `common/national_focus/016_dhrondan_focus_tree.txt` with `refresh = true`. It returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete = true`, 88 candidates, seven required inputs, zero inspect-unresolved items, normalized source hash `73a2e4be2fc959c6c44b1c263859833b6699c19b94feb85fcdc97361c13f6c15`, and source revision `64a9b88222b29fee28800c88f6498b8d614abf18b4049a304cb91656c92e0822`. The inspect artifact is [probability-inspect-73a2e4be2fc9.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c44396edba1de9f3ef4659dd7b2a58151c43d0f250dc063686e55c4164b603ea/6b20d10507c26dc3429875af2d6db1fa1e3ed302c75271435e67f14c652e1533/probability-inspect-73a2e4be2fc9.json).

One corrected `hoi4.probability_compare` used adapter `national_focus_ai_will_do`, the unchanged fixture and scenario hash `2db1f0f978c372b62d7261a12d480cce4302f2830f1a737ec68d1d35d7369f77`, the exact 88-focus pool, before `inlineClausewitz` from immutable HEAD `957ae81cc6539c2e29beebe92f4c6523eea91532`, and after path `common/national_focus/016_dhrondan_focus_tree.txt` with expected raw SHA-256 `13ea41e8aed3a555c77840e00f2d62f4b93845589b7e9bea7ae8a9dfbf3dd624`. It returned `PROBABILITY_ANALYZED_PARTIAL`, analysis ID `probability-b652045811f217a6b352130e`, source hash `73a2e4be2fc959c6c44b1c263859833b6699c19b94feb85fcdc97361c13f6c15`, source revision `660e7430fcffb37d446f8566b08f47efb4b2eb3cece38eb5d74083f12931ac4e`, the same scenario hash, 11 scenarios, 968 candidate rows, 186 unresolved items, two diagnostics, and `comparisonChanges = 0`.

The source diff against HEAD is limited to the two intended `completion_reward` lines at `DHR_seat_the_human_delegates` and `DHR_open_the_translation_bureaus`; the focus AI scores, candidate IDs, layout, and prerequisites are unchanged. The zero-change result is bounded evidence that this focus-source patch did not alter the inspected AI score or candidate-pool surface. It does not certify the non-weighted completion effects or advisor availability.

The comparison JSON is [probability-b652045811f217a6b352130e.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9929889f48e62ba3e66c3819b492540c9b9f89cf4aec8b64f01ba84aba030ff1/1ae53a6c9b0dffe3bbad2911625d9c7545965fb32b29e8716d19416616466af4/probability-b652045811f217a6b352130e.json). Rendered evidence includes [ranking SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9ab1d20fd06acf76106271c450b7d66e05c5083a887e440a9194312e32995d28/8b6d46b8aecee6dcdd14ccd22da3c87f91f70ff726260ab62f3da35121da5b1f/probability-probability-b652045811f217a6b352130e-ranking.svg), [matrix SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fc3eac7e7ab0ea75f198cb3edfdf0071b1b9306a55d19a8594f87d07d5ebda6/2ffafeaf97987752bdb17d4a0cf9f2eb4c78b5033cd591a1deecfbcdf36ca3f0/probability-probability-b652045811f217a6b352130e-matrix.svg), [comparison SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2450d67f32f665574260ffbd84f57cc7db1a9cf58aca09b66d13c1108a27cc49/a61bda86f88484757042d978d64eb224805ab5934264172937d04e7aacdc16cf/probability-probability-b652045811f217a6b352130e-comparison.svg), and [unresolved SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ae14ba39f4543c1e1cf3a1a924cbab79bbf4672f66896531396aa99a6035d2e/094d479abfe23f49d5febbebc5a0ae4c19208c655f9f2680579f65c2c4c85c6d/probability-probability-b652045811f217a6b352130e-unresolved.svg). The two comparison warnings are the same fixture-wide never-eligible late-crisis focuses, `DHR_break_the_separatist_ciphers` and `DHR_offer_a_shared_horizon`, and are unrelated to the two reward lines.

The comparison is source-scoped to the focus file. The before side retained the exact focus bytes, but helper and constant expansion remains workspace-backed, so this is not a historical helper-definition isolation proof. The focus adapter still reports a uniform score race rather than probability-proportional selection; all 968 rows remain subject to unresolved external factors and `conditionalProbability` is not evidence of a normalized campaign chance.

## Advisor availability result and limits

The character source is not a weighted candidate pool in the installed MCP service. The character probability inspect explicitly returned `no_weighted_surfaces` and no available adapters. No `character_selection`, advisor-appointment, political-power affordability, `available`, `allowed`, or political-advisor-slot-capacity probability adapter was exposed.

Source review records the baseline gates as follows, but these are source facts rather than engine probability results:

- `DHR_harmonic_envoy_rae_syl` is a `political_advisor` with `original_tag = DHR`, 100 political-power cost, AI factor 1, and baseline availability on the Covenant route only.
- `DHR_shadow_listener_thel_ior` is a `political_advisor` with `original_tag = DHR`, 100 political-power cost, AI factor 1, and baseline availability on Synod or Covenant only.
- The source uses `allowed`, `available`, `cost`, and `ai_will_do` character fields; native appointment is a recruitment/slot operation, not a weighted focus-selection pool in this service.

Consequently, the Covenant before/after delegates, three-regime before/after translation, absent-regime, political-power-99, and full-slot rows do not prove advisor availability or appointment outcomes. The political-power-99 row is useful as a retained future fixture, but the focus adapter does not consume advisor cost. The full-slot row contains an intentionally opaque fixture field and must not be read as a validated engine trigger.

## Recommendations and remaining uncertainty

The planned non-weighted reward and advisor-gate patch is present in the after source. The corrected compare found no change to the 88-focus pool or focus AI score surface. The advisor source remains outside the installed weighted adapters, so its availability change is source-scoped only.

The completed postpatch comparison reused this exact fixture, scenario hash, candidate pool, and immutable HEAD source bytes. A source-backed compare of the focus file detected no unintended AI-score or pool changes, but it cannot certify advisor appointment behavior.

Exact advisor eligibility evidence would require a supported character/advisor adapter or a typed runtime fixture that the MCP service recognizes for `available`, `allowed`, route flags, receipt flags, political-power affordability, and occupied political-advisor slots. Until then, advisor-gate conclusions remain source-scoped and unresolved at engine level.

Exact focus selection probabilities would require declared focus completion state, prerequisite state, ordered AI strategy-plan factors, and any external focus modifiers for every candidate. Do not normalize the returned score rows by hand.

No sweep, simulation, or sequence analysis was run because the required advisor adapter is absent and the focus evaluation has unresolved external and prerequisite inputs. No AI-weight change is recommended from this baseline.

## Simplifications, omissions, and blockers

The postpatch comparison is incomplete by design where the installed MCP route cannot evaluate character appointment or slot state and where focus external factors remain unresolved. Focus rows are score-only/bounded with explicit unresolved external factors, every conditional probability is null, and the comparison reports zero AI score or pool changes. No gameplay or balance simplification was applied by this auditor, and no completion or acceptance claim is made.

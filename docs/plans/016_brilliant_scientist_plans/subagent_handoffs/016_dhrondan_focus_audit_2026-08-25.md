# Event 016 D'Rhondan focus-tree audit handoff — 2026-08-25

Status: bounded read-only audit completed with one small localization-only correction.

The current D'Rhondan tree is structurally complete at 88 focuses, has the requested 8/24/10/12/8/8/12/6 category distribution, and passed the fresh HOI4 focus inspect/render/raster checks with no DHR layout diagnostics.

The only patch made in this audit corrects the wording of `DHR_paid_landing_reserve_effect`; no focus reward, route lock, icon, AI weight, decision, or country behavior was changed.

## Scope and references

The audited source is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\national_focus\016_dhrondan_focus_tree.txt` and its linked localization, icons, ideas, AI strategy, scripted effects and triggers, decisions, events, country, country tag, and character files.

I read `AGENTS.md`, the required offline Paradox wiki snapshots, relevant vanilla documentation and vanilla focus examples, the `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` skills, and the accepted Alien Infantry and Empire of D'Rhonda addendum at `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`.

Fresh structural MCP evidence came from `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster` against `common/national_focus/016_dhrondan_focus_tree.txt` with tree id `dhrondan_focus_tree`, normal review scale, padding 1, and 120 by 90 render spacing.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/59f99990f9d8ead0b0f5b094574e2319135bb0fa341e385f59ea133fff9cd751/fca4e2f24b157e1b32d4972454654a72198f57ff006bb2268a5647f1ca2f0720/focus-inspect.5cf1d337bc3cac06.json`.

The rendered HTML, SVG, JSON, and source-map artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e710f0b84eb6819a1e64297eb28801f9fa1271daa8d3c64785c6fd08ae7c0e1c/4b1bf9fa5cc0d45139f1cffc81b277863894a27f3eb5ee1ddaabb270ff1ce190/dhrondan_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/026668ec366fd5e634780088fe079cfaad5b1d0e0b7f46045ba01bc457f6bee7/93f97eafead7ec9cb22834412f623d6b8c0041a5190585ea0ced96515949c1c1/dhrondan_focus_tree.focus.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90b2ea0078cf3c08a0cc20bd77f18af76e2977da641565168c7b0396ab80be59/d3785803d7d129c17a2e7a9161eec7bbe51a6c3e36cd5fa5abe47c3f5afda476/dhrondan_focus_tree.focus.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0fe3e6cfbfa1a9b088b3febd0f7e860acdaa92b5fb52b5ff9fe479f77488095/9556f32ca9a480cd13b30e1b6a4df868957af365e1d3588e89c61cb4e131e8d7/dhrondan_focus_tree.focus.source-map.json`.

The raster artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7af40074fddfff1b375f2d99b3e6faa169144f2fcc6cdb2f4b02d6da210283e9/d90439e225621176d92958bc527fd2682ae8196b55e251d5e7d1b95c4c439756/dhrondan_focus_tree.focus.png`.

## Route coverage and exact counts

| Branch/category | Count | Focus id range and evidence |
|---|---:|---|
| Survival/opening | 8 | `DHR_beneath_an_alien_sky` through `DHR_convene_the_two_world_throne`, source lines 56–178. |
| Imperial political route | 8 | `DHR_vael_ix_takes_the_throne` through `DHR_the_unbroken_imperial_line`, source lines 184–293. |
| Synod political route | 8 | `DHR_sera_qel_presents_the_calculus` through `DHR_the_government_of_certainties`, source lines 297–406. |
| Covenant political route | 8 | `DHR_ilyr_ren_opens_the_chamber` through `DHR_the_chamber_of_two_skies`, source lines 410–519. |
| Laboratory | 10 | `DHR_relight_the_field_laboratories` through `DHR_a_two_world_research_complex`, source lines 523–645. |
| Army | 12 | `DHR_restore_the_predictive_staff` through `DHR_perfect_predictive_warfare`, source lines 649–795. |
| Orbital | 8 | `DHR_reassemble_the_orbital_office` through `DHR_make_near_space_ours`, source lines 804–901. |
| Diplomacy | 8 | `DHR_open_the_translation_bureaus` through `DHR_the_embassy_beyond_the_stars`, source lines 909–1002. |
| Expansion | 12 | `DHR_define_the_two_worlds_question` through `DHR_a_place_in_the_world_order`, source lines 1010–1162. |
| Crisis | 6 | `DHR_the_enclaves_refuse_the_ledger` through `DHR_the_century_beyond_exile`, source lines 1167–1247. |
| **Total** | **88** | The requested category distribution is exactly 8/24/10/12/8/8/12/6 when the three 8-focus political routes are grouped as one 24-focus political category. |

The three regime roots are exactly eight focuses each and use the intended mutually exclusive choice: `DHR_vael_ix_takes_the_throne` at line 191 excludes the Synod and Covenant roots, `DHR_sera_qel_presents_the_calculus` at line 304 excludes the Imperial and Covenant roots, and `DHR_ilyr_ren_opens_the_chamber` at line 417 excludes the Imperial and Synod roots.

The expansion branch is route-aware rather than duplicated: the Imperial descendants are `DHR_restore_the_imperial_reaches`, `DHR_demand_the_origin_host`, and `DHR_the_subject_world_protocol` at lines 1029–1055; the Synod descendants are `DHR_calculate_the_reclamation_zones`, `DHR_subordinate_borders_to_need`, and `DHR_administer_the_optimal_order` at lines 1068–1094; and the Covenant descendants are `DHR_invite_the_enclave_congress`, `DHR_negotiate_the_origin_settlement`, and `DHR_federate_the_two_worlds` at lines 1107–1133.

Each political route has seven route-gated descendants after its root, and each route has three route-gated expansion descendants, giving ten route-gated descendants per regime beyond the root.

## Layout, connectors, and prerequisite semantics

The fresh `hoi4.focus_inspect` result reports 88 nodes, 102 connectors, zero connector crossings, zero node intersections, zero long connectors, zero same-row spacing violations, and zero DHR diagnostics.

The inspected bounds are x=2–40 and y=0–22 with maximum horizontal span 7, maximum vertical span 3, maximum Manhattan span 9, total horizontal span 170, and no duplicate coordinates.

The fresh render and raster use layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`, rendered size 4706 by 2058, and match the inspect layout hash.

The prerequisite audit found 97 prerequisite blocks, all referenced focus ids resolve, and there are no unknown prerequisites or mutual-exclusion ids.

The three political root blocks intentionally use one prerequisite block for the opening convention and one mutual-exclusion block for the other two roots, so only one regime route can be selected.

The three political capstones `DHR_the_unbroken_imperial_line`, `DHR_the_government_of_certainties`, and `DHR_the_chamber_of_two_skies` intentionally use two prerequisite blocks for AND semantics, as does `DHR_standardize_alien_components`.

The cross-route `DHR_define_the_two_worlds_question` at line 1015 intentionally has one prerequisite block containing all three regime capstones, which is OR semantics and permits the selected regime to begin expansion.

The cross-route `DHR_begin_postwar_integration` at line 1144 intentionally has one prerequisite block containing the three route expansion capstones, which is OR semantics.

The crisis branch is correctly gated by `DHR_the_enclaves_refuse_the_ledger`; `DHR_offer_a_shared_horizon` and `DHR_break_the_separatist_ciphers` each require that opener and mutually exclude each other, while `DHR_resolve_the_enclave_crisis` at line 1219 requires either resolution choice.

No connector or prerequisite patch is recommended from this audit.

## Icons and asset coverage

| Asset family | Expected | Resolved | Evidence |
|---|---:|---:|---|
| Focus icon ids | 88 | 88 | `interface/016_dhrondan_focus_icons.gfx` defines one base and one shine sprite for every focus id. |
| Focus shine ids | 88 | 88 | All shine names follow the existing `GFX_goal_DHR_*_shine` convention and resolve in MCP render. |
| Focus texture references | 88 | 88 | All references target `gfx/interface/goals/016_dhrondan_focus/*.dds`; missing texture references: 0. |
| Focus DDS files by category | 8/8/8/8/10/12/8/8/12/6 | Same | Files under `gfx/interface/goals/016_dhrondan_focus/` match the route counts. |
| Focus-created idea sprites | 11 | 11 | Files under `gfx/interface/ideas/016_dhrondan_focus/` resolve from `common/ideas/016_dhrondan_focus_ideas.txt`. |

No repeated or missing focus icon ids were found, and the MCP inspect/render/raster passes resolved all DHR icons.

The only validation warning was the unrelated vanilla continuous-focus localization reference `continuous_restrict_freedom`; it is not a DHR node or DHR icon and is outside this task scope.

## Localization and reward review

`localisation/english/016_dhrondan_focus_l_english.yml` is UTF-8 with BOM and contains title and description keys for all 88 focus ids.

All seven custom effect tooltip references resolve: `DHR_paid_landing_network_effect`, `DHR_reclamation_declaration_effect`, `DHR_paid_landing_reserve_effect`, `DHR_world_order_contract_effect`, `DHR_integration_program_effect`, `DHR_enclave_crisis_begins_effect`, and `DHR_enclave_crisis_resolved_effect`.

The one mismatch found was the reserve tooltip for `DHR_feed_the_landing_reserve` at `common/national_focus/016_dhrondan_focus_tree.txt:604`; it said the focus authorized “one paid cohort request,” while the reward only sets persistent `dhrondan_landing_reserve_supply_priority` and the landing decision uses that flag as an AI factor rather than consuming it.

That wording was corrected in `localisation/english/016_dhrondan_focus_l_english.yml:14` under key `DHR_paid_landing_reserve_effect` to state that the focus marks the landing reserve as a priority for future paid cohort calls and grants no cohort itself.

The reward and title/description review found no remaining title-to-reward contradiction, missing focus localization, or unresolved custom tooltip reference.

The patch is localization-only and leaves the route behavior of `DHR_feed_the_landing_reserve` unchanged.

## Ideas, alien-training restriction, and country dependencies

`common/ideas/016_dhrondan_focus_ideas.txt` defines five political lifecycle variants, three predictive-warfare variants, and three off-world variants, for eleven focus-created spirits.

`common/scripted_effects/016_dhrondan_focus_effects.txt:12-119` clears each family before adding its next stage, so focus effects permit at most one political, one predictive, and one off-world spirit simultaneously, or three focus-created spirits total.

The focus tree and focus effects contain no `create_unit`, division-template creation, training, equipment-stockpile grant, or equipment-production effect; the overview at `common/scripted_effects/016_dhrondan_focus_effects.txt:3-7` explicitly preserves the no-normal-alien-training and no-free-guns contract.

The only focus-owned landing helper at `common/scripted_effects/016_dhrondan_focus_effects.txt:121-129` establishes the paid landing network, keeps training forbidden, and records the landing cost; the initial 2,000-laser payment and initial stores remain in `common/scripted_effects/016_dhrondan_country_effects.txt:267-301` and `common/scripted_effects/016_alien_infantry_api_effects.txt`.

The Imperial, Synod, and Covenant roots correctly call the existing regime installers at `common/scripted_effects/016_dhrondan_country_effects.txt:216-255`, and existing DHR characters at `common/characters/016_dhrondan_characters.txt` expose the expected route-specific leader, advisor, and high-command hooks.

The country package and tag wiring are present in `common/countries/Empire of D'Rhonda DHR.txt` and `common/country_tags/016_dhrondan_country.txt`; no country identity patch is recommended.

## AI behavior and probability evidence

`common/ai_strategy_plans/016_dhrondan_focus_ai.txt` contains one DHR opening plan and three route plans for Imperial, Synod, and Covenant, each with route enable/abort conditions and route-aware priorities.

The opening plan lists all eight survival focuses and aborts once a political route is chosen, while each route plan prioritizes its political, military, laboratory, diplomacy, expansion, and crisis themes.

Inline `ai_will_do` blocks exist for all 88 focuses, including route root weights at `common/national_focus/016_dhrondan_focus_tree.txt:194`, `:307`, and `:420`, and crisis weights at `:1190` and `:1209-1210`.

The route roots remain navigable under the current fallback weights: Imperial is favored during war and higher war support, Synod during peace and higher stability, and Covenant during peace with lower stability; crisis reconciliation is favored by Covenant, while cipher suppression is favored by Imperial or Synod.

The route strategy lists do not enumerate every generic support focus, so generic laboratory, orbital, diplomacy, or army support may be selected through inline base weights rather than an explicit route-plan priority; this is a route-AI tuning risk, not a missing route or dead focus.

Fresh `hoi4.probability_inspect` was run with the national-focus AI adapter against the current tree and returned 88 candidates with no unresolved source parsing diagnostics, but no scenario eligibility can be normalized without completion-history and route-state inputs.

Fresh `hoi4.probability_evaluate` was run for named opening, Imperial, Synod, Covenant, and low-chaos DHR scenarios with all 88 focus ids as the candidate pool; the result was `PROBABILITY_ANALYZED_PARTIAL` with 440 candidate rows, 126 unresolved rows, and 34 diagnostics because the supplied scenarios did not include the full focus completion history and eligibility state.

The linked partial analysis artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5d67da588e64baf97275c7f593bbcf341b5fc54e7a5a03085577f7922a24af1/83ba84c1f3399178d4ed99cfa73a32027fb8a1a53efe3fa590e98085309988b3/probability-1573763df949cf7752a4877b.json`.

The associated ranking, matrix, and unresolved views are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/903aad064956fd708a9f54862945379c7ed5601e3af070b7be72b13d9c9c1089/4156f8ee8a7da99c48a61c09691150906904df37b01c2d0d690df11c1006ab62/probability-probability-1573763df949cf7752a4877b-ranking.svg`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f45a046e4a00eb184be8cceff5298d9166a42ecfdc45aab669dbdd64155a52bf/520872c29333773a665849eac69d1a5f24da1ed7980e303f93a9932ab566385a/probability-probability-1573763df949cf7752a4877b-matrix.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7bbb67c42758f2ddae2f584aaca11857edc97b39ac687dea162205560bb3f00/1cbcdd62f809ebcd49ee8585b440c04d741c5d88b0bffc006533c2ff431a4f9/probability-probability-1573763df949cf7752a4877b-unresolved.svg`.

The unresolved rows for route descendants such as `DHR_enthrone_the_synod`, `DHR_crown_the_enclave_empire`, `DHR_offer_a_shared_horizon`, and `DHR_federate_the_two_worlds` are scenario-input limitations and must not be interpreted as dead focuses.

A three-point `war_support` sweep was also partial with the same 126 unresolved rows and 34 diagnostics; its JSON and sensitivity artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11bd07b387abe0913a7c916d5bb69c99c5c67237ceb41b172ef5749b6d7117d4/f5741bc15ca3b6d669a4aec4b3d4d3cd520754881fa542754a7720c48529590c/probability-69a92c76b235e287a0778949.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c3338cd9ac7b8d13ee1095af752b609c26918b42dfab754700c122531461a04/9c5f776cb4d48768caf32e96912c5ab4b59d22ecf31a05c2cefba55cf4c1069e/probability-probability-69a92c76b235e287a0778949-sensitivity.svg`.

The required `chaosx_ai_probability_auditor` custom-agent route was unavailable in this runtime, so no claim of a complete probability audit or exact normalized selection percentages is made.

## Missing, simplified, or unresolved content

The focus tree itself has no missing requested route, category, connector, icon, localization, prerequisite, exclusion, or inline AI block found by this audit.

The following downstream integration remains unresolved and should be owned by the main implementation pass rather than patched by this bounded audit.

- `DHR_define_the_two_worlds_question` at `common/national_focus/016_dhrondan_focus_tree.txt:1015-1018` sets `dhrondan_two_worlds_question_defined`, but no current decision, event, or formable consumer was found under `common/decisions`, `events`, or country/formable files.

- `DHR_a_place_in_the_world_order` at `common/national_focus/016_dhrondan_focus_tree.txt:1151-1159` calls `dhrondan_focus_open_world_order`, which sets `dhrondan_world_order_decisions_unlocked` and `dhrondan_world_order_claim_contract_ready` in `common/scripted_effects/016_dhrondan_focus_effects.txt:283-287`, but no current decision, mission, claim, or war-goal consumer was found.

- Route-specific markers `dhrondan_alien_components_standardized`, `dhrondan_laboratory_route_complete`, `dhrondan_predictive_warfare_perfected`, `dhrondan_orbital_office_reassembled`, and `dhrondan_access_map_exchange_ready` are set by focus rewards at `common/national_focus/016_dhrondan_focus_tree.txt:592`, `:641`, `:795`, `:812`, and `:953`, but have no current downstream consumers; these may be intentional future hooks, but their owner and acceptance behavior are not evidenced in the current package.

- The probability evaluation cannot establish route selection percentages until scenario focus-completion history, current regime flags, and candidate eligibility are supplied; its “never eligible” rows are therefore not accepted as dead-route findings.

These are integration and evidence gaps, not reasons to redesign the tree or add a new decision/formable chain in this audit.

## High-priority follow-up

1. The main agent should either wire the existing world-order marker flags into the promised decision/claim/formable consumer or explicitly document that those flags are reserved hooks, beginning with `DHR_define_the_two_worlds_question` and `DHR_a_place_in_the_world_order`.

2. The main agent should rerun the mandatory probability audit through `chaosx_ai_probability_auditor` when that route is available, using completed opening and regime focus histories and named peaceful, wartime, stable, and unstable DHR scenarios before changing any AI weights.

3. If route AI is judged too generic after complete-state probability analysis, add only narrowly scoped priorities for currently omitted support focuses in `common/ai_strategy_plans/016_dhrondan_focus_ai.txt`; do not alter root mutual exclusions or invent a new route family.

## Patch and validation record

Changed file: `localisation/english/016_dhrondan_focus_l_english.yml`.

Changed key: `DHR_paid_landing_reserve_effect`.

Changed focus id: `DHR_feed_the_landing_reserve` only through its tooltip reference; no focus source id or icon id changed.

Before the patch, the tooltip promised one paid cohort request even though the focus only set `dhrondan_landing_reserve_supply_priority`; after the patch it describes the priority marker and explicitly states that no cohort is granted by the focus.

Validation completed after the patch: the localization file remains UTF-8 with BOM, all 88 title/description pairs still resolve, the seven custom effect tooltip references still resolve, and the source-only reward scan still finds no normal alien training or free-gun loop.

Fresh MCP validation before the localization-only patch completed successfully for focus inspect, focus render, and focus raster with the layout and diagnostic results recorded above; the patch cannot change tree layout or icon resolution.

Fresh probability inspect/evaluate/sweep evidence is recorded above, but it is explicitly partial and is not a complete balance acceptance pass.

Skipped meaningful validation: no live Hearts of Iron IV launch was performed under the repository boundary, no exact normalized focus-selection percentages were claimed because complete scenario history was unavailable, and no additional MCP retries were made after the parent requested bounded termination.

No Git commit was created because the shared worktree contains unrelated changes from other agents; the parent should review and stage this handoff and the one localization change with its own scoped commit.

## Remaining route risks

The route lock, AND/OR prerequisite semantics, crisis mutual exclusion, icon resolution, localization coverage, spirit lifecycle cap, no-training/no-free-guns contract, existing decision hooks, and country route installers are all structurally evidenced and low risk.

The remaining risks are downstream world-order flags without current consumers, route-specific marker flags without current consumers, generic-support focus priority under the route strategy lists, and incomplete quantitative AI scenarios.

No broader tree redesign, new route family, new formable chain, or country identity change is recommended from this audit.

# Event 016 D’Rhondan focus-tree final audit — 2026-08-26

## Status and scope

This is a read-only source and evidence audit of `common\national_focus\016_dhrondan_focus_tree.txt`. No gameplay, AI, decision, trigger, effect, idea, localisation, interface, asset, country, or registry source was edited, and no Git commit was created. This handoff does not claim in-game completion or live consumer acceptance.

The audit covers the binding D’Rhondan addendum at `docs\specs\016_brilliant_scientist_specs\specs\016_alien_infantry_and_dhronda_addendum.md`, the accepted focus-system description at `docs\events\016_brilliant_scientist\systems\016_dhrondan_focus_tree.md`, the acceptance scenarios at `docs\plans\016_brilliant_scientist_plans\016_alien_dhrondan_acceptance_scenarios.md`, current DHR country/focus effects, triggers, ideas, localisation, AI plans, decision consumers, GFX registrations, binary manifests, and prior focus audits.

`AGENTS.md`, the offline Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, Interface modding, and AI focuses pages were read. Vanilla documentation under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\` and vanilla national-focus/AI precedents were consulted. The `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` skills were applied.

The current repository `HEAD` is `3fd004225caf3f10aab2ab052117245ab21143e7`; `18f7c7d67` is in its history. `git log 18f7c7d67..HEAD` contains no changes to the DHR focus, DHR focus AI, DHR focus effects, DHR ideas, DHR focus localisation, or DHR focus icon registration paths. The later DHR marker-consumer repairs are represented in the current decision and trigger sources.

## Route coverage and exact counts

The source has exactly 88 `focus` blocks, 88 unique DHR focus IDs, 88 unique coordinates, 88 completion rewards, 88 inline `ai_will_do` blocks, 88 `search_filters` blocks, 97 prerequisite blocks representing 102 prerequisite edges, five mutual-exclusion blocks, 33 `available` blocks, and ten navigation shortcuts.

| Route family | Count | Source identifiers | Source result |
| --- | ---: | --- | --- |
| Survival and landing network | 8 | `DHR_beneath_an_alien_sky` → `DHR_convene_the_two_world_throne` | Source-complete opening trunk. |
| Imperial Continuity | 8 | `DHR_vael_ix_takes_the_throne` → `DHR_the_unbroken_imperial_line` | Eight-focus Vael IX route with Imperial Mandate capstone. |
| Predictive Synod | 8 | `DHR_sera_qel_presents_the_calculus` → `DHR_the_government_of_certainties` | Eight-focus Sera Qel route with Synod Calculus capstone. |
| Two-World Covenant | 8 | `DHR_ilyr_ren_opens_the_chamber` → `DHR_the_chamber_of_two_skies` | Eight-focus Ilyr Ren route with Covenant Compact capstone. |
| Political total | **24** | Three mutually exclusive eight-focus regime routes | Matches the accepted political subtotal. |
| Laboratory economy | 10 | `DHR_relight_the_field_laboratories` → `DHR_a_two_world_research_complex` | Research, production, material substitution, paid-reserve, and one research-slot capstone. |
| Army and predictive warfare | 12 | `DHR_restore_the_predictive_staff` → `DHR_perfect_predictive_warfare` | Forecast, signals, logistics, command, and custom predictive-technology upgrade. |
| Orbital, air, and naval support | 8 | `DHR_reassemble_the_orbital_office` → `DHR_make_near_space_ours` | Relay, air, naval, dockyard, and landing-recovery support. |
| Diplomacy and intelligence | 8 | `DHR_open_the_translation_bureaus` → `DHR_the_embassy_beyond_the_stars` | Translation, access, partner, intelligence, and embassy hooks. |
| Expansion and world order | 12 | `DHR_define_the_two_worlds_question` → `DHR_a_place_in_the_world_order` | Three route-specific settlement lanes followed by shared integration. |
| Crisis and late game | 6 | `DHR_the_enclaves_refuse_the_ledger` → `DHR_the_century_beyond_exile` | Reconciliation/cipher fork, crisis resolution, corridor, and final hook. |
| **Total** | **88** | `8/24/10/12/8/8/12/6` | Exact accepted distribution. |

The exact route membership is:

- Survival: `DHR_beneath_an_alien_sky`, `DHR_count_the_landing_states`, `DHR_secure_the_scattered_enclaves`, `DHR_inventory_the_expedition_stores`, `DHR_restore_the_landing_beacons`, `DHR_bind_the_enclaves`, `DHR_reopen_the_orbital_channel`, `DHR_convene_the_two_world_throne`.
- Imperial: `DHR_vael_ix_takes_the_throne`, `DHR_restore_the_ninth_diadem`, `DHR_bind_the_landing_lords`, `DHR_codify_imperial_service`, `DHR_raise_the_palace_guard`, `DHR_proclaim_the_right_of_return`, `DHR_crown_the_enclave_empire`, `DHR_the_unbroken_imperial_line`.
- Synod: `DHR_sera_qel_presents_the_calculus`, `DHR_audit_every_command_node`, `DHR_elevate_the_first_calculants`, `DHR_publish_the_survival_equations`, `DHR_assign_merit_by_projection`, `DHR_replace_decree_with_prediction`, `DHR_enthrone_the_synod`, `DHR_the_government_of_certainties`.
- Covenant: `DHR_ilyr_ren_opens_the_chamber`, `DHR_seat_the_human_delegates`, `DHR_write_the_dual_citizenship_code`, `DHR_elect_the_landing_councils`, `DHR_guarantee_the_right_to_depart`, `DHR_submit_the_military_to_debate`, `DHR_ratify_the_two_world_covenant`, `DHR_the_chamber_of_two_skies`.
- Laboratory: `DHR_relight_the_field_laboratories`, `DHR_recover_the_laser_forges`, `DHR_convert_terrestrial_workshops`, `DHR_crystal_growth_chambers`, `DHR_the_twenty_element_substitution`, `DHR_standardize_alien_components`, `DHR_feed_the_landing_reserve`, `DHR_the_exoplanetary_materials_board`, `DHR_join_the_scattered_laboratories`, `DHR_a_two_world_research_complex`.
- Army: `DHR_restore_the_predictive_staff`, `DHR_map_the_probability_front`, `DHR_encode_the_enemy_reaction`, `DHR_train_human_signal_teams`, `DHR_rebuild_the_expeditionary_cadres`, `DHR_fire_control_by_forecast`, `DHR_supply_before_the_order`, `DHR_the_thousand_branch_wargame`, `DHR_delegate_to_the_field_calculants`, `DHR_command_without_surprise`, `DHR_the_foreseen_counterstroke`, `DHR_perfect_predictive_warfare`.
- Orbital: `DHR_reassemble_the_orbital_office`, `DHR_chart_terrestrial_air_corridors`, `DHR_adapt_the_gravity_fighters`, `DHR_salvage_the_shuttle_docks`, `DHR_link_airfields_to_the_relay`, `DHR_form_the_exile_flotilla`, `DHR_guard_the_descent_windows`, `DHR_make_near_space_ours`.
- Diplomacy: `DHR_open_the_translation_bureaus`, `DHR_listen_to_the_human_airwaves`, `DHR_trade_in_impossible_materials`, `DHR_exchange_maps_for_access`, `DHR_seed_the_enclave_network`, `DHR_recruit_two_world_operatives`, `DHR_choose_our_terrestrial_partners`, `DHR_the_embassy_beyond_the_stars`.
- Expansion: `DHR_define_the_two_worlds_question`, `DHR_restore_the_imperial_reaches`, `DHR_demand_the_origin_host`, `DHR_the_subject_world_protocol`, `DHR_calculate_the_reclamation_zones`, `DHR_subordinate_borders_to_need`, `DHR_administer_the_optimal_order`, `DHR_invite_the_enclave_congress`, `DHR_negotiate_the_origin_settlement`, `DHR_federate_the_two_worlds`, `DHR_begin_postwar_integration`, `DHR_a_place_in_the_world_order`.
- Crisis: `DHR_the_enclaves_refuse_the_ledger`, `DHR_offer_a_shared_horizon`, `DHR_break_the_separatist_ciphers`, `DHR_resolve_the_enclave_crisis`, `DHR_reopen_the_homeworld_corridor`, `DHR_the_century_beyond_exile`.

## Prerequisites, exclusions, and navigation

The three political roots at `common\national_focus\016_dhrondan_focus_tree.txt:185-193`, `:298-306`, and `:411-419` all require `DHR_convene_the_two_world_throne` and mutually exclude the other two roots. Every descendant of those routes has an explicit route `available` trigger, so a selected regime cannot accidentally complete another regime’s descendants.

The separate prerequisite blocks on `DHR_convene_the_two_world_throne`, all three political capstones, `DHR_fire_control_by_forecast`, `DHR_the_foreseen_counterstroke`, `DHR_make_near_space_ours`, and `DHR_the_embassy_beyond_the_stars` express intended AND gates under the documented HOI4 semantics. A single prerequisite block with multiple `focus` entries is OR, and is intentionally used by `DHR_define_the_two_worlds_question` at `:1027`, `DHR_begin_postwar_integration` at `:1156`, and `DHR_resolve_the_enclave_crisis` at `:1231`.

`DHR_offer_a_shared_horizon` and `DHR_break_the_separatist_ciphers` both require `DHR_the_enclaves_refuse_the_ledger` and mutually exclude each other at `:1191-1215`. The shared resolver accepts either selected response, then `DHR_reopen_the_homeworld_corridor` and `DHR_the_century_beyond_exile` continue the common late-game lane.

The tree begins at `DHR_beneath_an_alien_sky`, has ten shortcuts at `:41-50`, and uses the accepted ten family lanes. The current authored coordinates have no duplicate positions. The most recent successful focus inspection reported bounds `x=2..40`, `y=0..22`, maximum horizontal span 7, maximum vertical span 3, maximum Manhattan span 9, and 102 connectors with zero crossings, node intersections, or long connectors.

`DHR_salvage_the_shuttle_docks` now has a bounded `available` gate at `:846-857` requiring an owned, controlled coastal state with a free dockyard slot. This prevents a landlocked country from silently setting the salvage marker without the promised facility. No fallback reward was invented.

## Focus MCP evidence and exact blockers

An earlier successful `hoi4.focus_inspect` against `common\national_focus\016_dhrondan_focus_tree.txt` and `dhrondan_focus_tree` returned `FOCUS_INSPECTED` with status `ok`, 88 focuses, 102 connectors, zero crossing/intersection/long-connector diagnostics, and layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`. The exact inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7f094589a3899fd52e6b1d05e13777d76d9783faa3751b3887d7cfcf6d228ee/9c81fe28bc00eb91a4c4039c31272b633591ce197dbe936eb31832b8acf64570/focus-inspect.abe2c73eb5b5af0a.json`.

The matching successful `hoi4.focus_render` produced deterministic HTML, SVG, JSON, source-map, and plan artifacts with a `6992x2788` render and the same layout hash. Exact artifacts are:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e4cd067b810b70afd1e61b36eb95f401182898ce7c96ec72969bdb2fd782b475/d8110b9621d74d9306684aef2e6c7c17bfd42a1f813c4cab5968d0ab99d054fc/dhrondan_focus_tree.focus.html`.
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289/2512d737d80473f718e621de3ca8f39173afc86ccfb4cb3ccf19f48197e63223/dhrondan_focus_tree.focus.svg`.
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6213aa6ec9163c99ecaf94059b6385d1c7ea233f350724f58a09ebd4f3dca29/eeddeab9c47478dfc378a4a24471c263cfe162016ba0e58222962514ac5d6b8c/dhrondan_focus_tree.focus.json`.
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0fe3e6cfbfa1a9b088b3febd0f7e860acdaa92b5fb52b5ff9fe479f77488095/e4b08bc705121b0e43af06b4146307d2732b1058d0f43ef1bc338a27679b4f45/dhrondan_focus_tree.focus.source-map.json`.
- Plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2da7e5f94d34d46f7783ed1442d0f64f8934f730f66f57f70299b0121497c3b3/217f49da4dbf58ef4ba17a0f81c6ca9e47e922cfdbbe68c003c891c138a58c76/dhrondan_focus_tree.focus.plan.json`.

The same earlier result recorded only informational `MCP_INLINE_FILES_TRUNCATED` output and an unrelated vanilla `continuous_restrict_freedom_desc` localisation warning. Neither diagnostic names a DHR focus.

Current bounded retries were also recorded. A current `hoi4.focus_inspect` request with `mode=national`, `relativePath=common/national_focus/016_dhrondan_focus_tree.txt`, `treeId=dhrondan_focus_tree`, `laneSpacing=2`, and `nodeSpacing=2` remained running after the tool call yielded at 61 seconds and one further 11-second poll; it was manually terminated at approximately 72 seconds and returned no status, artifact, or diagnostics. A current `hoi4.focus_render` request with `mode=national`, the same relative path and tree ID, and `reviewScale=1` remained running for 31 seconds and was manually terminated without a result. These are caller-bounded partials, not server-generated timeout strings.

Prior current runs also recorded the exact server blocker `tool call failed for hoi4_agent_tools/hoi4.focus_inspect: timed out awaiting tools/call after 180s` and the equivalent `hoi4.focus_render` timeout. The prior successful artifacts above remain topology evidence because the later DHR commits changed reward/availability wiring but did not change the node coordinates or prerequisite graph. A fresh current post-availability render was not obtained, so current engine icon/layout resolution remains unrefreshed.

## Reward and marker audit

Rewards are varied across political power, command power, stability, war support, army/air/navy experience, technology bonuses, state construction, research capacity, route flags, lifecycle replacements, landing-recovery hooks, world-order hooks, crisis hooks, and the custom predictive-warfare technology upgrade. The source contains 88 completion rewards and no reward-only generic branch was identified. Repeated small political-power or stability values are paired with route-specific flags, helpers, or downstream contracts rather than appearing as the sole identity of a branch.

The focus source and `common\scripted_effects\016_dhrondan_focus_effects.txt` contain no `create_unit`, `add_equipment_to_stockpile`, `add_equipment_production`, division-template grant, normal alien-training effect, claim effect, core effect, or direct state-transfer effect. `DHR_perfect_predictive_warfare` calls the accepted custom technology-upgrade API. The landing boundary remains the shared paid Alien Infantry API with the exact 2,000 Alien Laser Weapons cost; `DHR_feed_the_landing_reserve` only marks AI priority and does not create a cohort.

The three focus-created spirit families are enforced by `common\scripted_effects\016_dhrondan_focus_effects.txt:13-119`: political, predictive military, and off-world corridor. Each transition clears its family before adding the next stage, so at most three focus-created spirits coexist.

Current marker consumers are present and supersede older handoffs that described them as dead flags.

| Producer focus/marker | Current consumer | Evidence |
| --- | --- | --- |
| `DHR_count_the_landing_states` → `dhrondan_landing_states_counted` | Paid landing AI modifier | `common\decisions\016_alien_infantry_landing_decisions.txt:63-65`. |
| `DHR_inventory_the_expedition_stores` → `dhrondan_expedition_stores_audited` | Paid landing AI modifier | `common\decisions\016_alien_infantry_landing_decisions.txt:67-69`. |
| `DHR_restore_the_landing_beacons` → `dhrondan_landing_beacons_restored` | Paid landing AI modifier | `common\decisions\016_alien_infantry_landing_decisions.txt:71-73`. |
| `DHR_secure_the_scattered_enclaves` → `dhrondan_scattered_enclaves_secured` | Enclave-supply bridge AI modifier | `common\decisions\016_dhrondan_country_decisions.txt:120-121`. |
| `DHR_standardize_alien_components` → `dhrondan_alien_components_standardized` | Paid landing AI modifier | `common\decisions\016_alien_infantry_landing_decisions.txt:75-77`; trigger `common\scripted_triggers\016_dhrondan_focus_triggers.txt:45-48`. |
| `DHR_reassemble_the_orbital_office` → `dhrondan_orbital_office_reassembled` | Paid landing AI modifier | `common\decisions\016_alien_infantry_landing_decisions.txt:79-81`; trigger `:60-63`. |
| `DHR_a_two_world_research_complex` → `dhrondan_laboratory_route_complete` | Enclave-supply availability and AI | `common\decisions\016_dhrondan_country_decisions.txt:89-93`, `:118-121`; trigger `common\scripted_triggers\016_dhrondan_country_triggers.txt:159-163`. |
| `DHR_perfect_predictive_warfare` → `dhrondan_predictive_warfare_perfected` | Reclamation availability, cancellation, and AI | `common\decisions\016_dhrondan_country_decisions.txt:27-31`, `:66-68`; trigger `common\scripted_triggers\016_dhrondan_country_triggers.txt:143-147`. |
| `DHR_exchange_maps_for_access` → `dhrondan_access_map_exchange_ready` | Covenant compact target-root gate | `common\decisions\016_dhrondan_country_decisions.txt:164-170`; trigger `common\scripted_triggers\016_dhrondan_focus_triggers.txt:65-68`. |
| `DHR_define_the_two_worlds_question` and `DHR_a_place_in_the_world_order` | World-order decision gates | `common\scripted_effects\016_dhrondan_focus_effects.txt:283-287`; `common\scripted_triggers\016_dhrondan_country_triggers.txt:120-138`; decision source `:15-168`. |
| `DHR_begin_postwar_integration` and crisis focuses | Integration and crisis consumers | `common\decisions\016_dhrondan_country_decisions.txt:75-113`, `:128-168`; trigger source `:159-170`. |

No current focus marker was found to be set-only after the route-consumer and survival-marker repairs. The five route-support markers remain source-backed decision contracts, not a reason to add duplicate decisions or new routes.

## Icon coverage

| Asset surface | Expected | Found | Evidence |
| --- | ---: | ---: | --- |
| Focus base sprites | 88 | 88 | `interface\016_dhrondan_focus_icons.gfx`. |
| Focus shine sprites | 88 | 88 | Matching `GFX_goal_DHR_*_shine` entries in the same GFX file. |
| Focus DDS files | 88 | 88 | `gfx\interface\goals\016_dhrondan_focus\` under ten documented family folders. |
| Focus DDS manifest entries | 88 | 88 | `docs\assets\016_brilliant_scientist\dhrondan_icon_asset_completion\metadata\focus_dds_validation.json`. |
| Unique focus DDS hashes | 88 | 88 | Manifest hash count is 88 unique; every item is 94x86 with alpha range 0..255. |
| Lifecycle idea sprites | 11 | 11 | `interface\016_dhrondan_focus_icons.gfx`, `common\ideas\016_dhrondan_focus_ideas.txt`, and `gfx\interface\ideas\016_dhrondan_focus\`. |

The static source check found every focus ID’s base icon, shine icon, DDS path, and family folder. The prior successful MCP inspect/render returned no DHR icon diagnostics. The current render retry timed out before a new engine resolution result.

## Localisation and reward mismatch list

`localisation\english\016_dhrondan_focus_l_english.yml` contains 88/88 focus title keys and 88/88 `_desc` keys, 11/11 lifecycle idea title/description pairs, and all seven custom focus-effect tooltip keys. The file is UTF-8 with BOM and uses no `:0` suffixes.

No current focus-name, description, reward, icon, or custom-tooltip mismatch was found. The earlier `DHR_feed_the_landing_reserve` wording defect was corrected under `DHR_paid_landing_reserve_effect` at localisation line 14; it now says that the focus marks future paid calls and grants no cohort. `DHR_rebuild_the_expeditionary_cadres` distinguishes human cadres from alien cohorts, and the corridor descriptions retain the per-cohort 2,000-laser cost. The dynamic landing cost is initialized in `common\scripted_effects\016_dhrondan_country_effects.txt:276-280` and sourced from the shared 2,000-equipment constant.

## AI behavior and probability evidence

All 88 focus blocks have inline `ai_will_do` values. `common\ai_strategy_plans\016_dhrondan_focus_ai.txt` contains one DHR opening plan and distinct Imperial, Synod, and Covenant route plans with route enable/abort conditions, ordered focus lists, and route-specific `focus_factors`. The opening plan lists all eight survival focuses and aborts after a political route is selected. The route roots are state-sensitive: Vael favors war or higher war support at `:194-198`, Sera favors peace and higher stability at `:307-311`, and Ilyr favors peace with lower stability at `:420-424`. Crisis choices are route-aware at `:1190-1220`.

The route plans omit some generic support priorities even though the corresponding focuses retain inline base weights. Examples are Imperial omitting several laboratory/diplomacy support priorities, Synod omitting most orbital/diplomacy support priorities, and Covenant omitting the army lane and some laboratory/orbital priorities. This is a route-priority tuning risk, not a dead route or missing AI block.

The mandatory named `chaosx_ai_probability_auditor` route is not callable in this runtime: `ALL_TOOLS` exposes the HOI4 probability tools but no callable custom-agent route with that identifier. A current direct `hoi4.probability_inspect` attempt with `adapter=national_focus_ai_will_do` and source object `{relativePath, treeId}` returned the exact schema error `MCP error -32602: Input validation error for hoi4.probability_inspect: Unrecognized keys: "relativePath", "treeId" at source`. An adapter-only retry returned `An adapter requires a source; provide a source alone to discover compatible adapters`. A source-string retry returned `Invalid input: expected object, received string at source`. The corrected source object `{path=common/national_focus/016_dhrondan_focus_tree.txt}` remained running for 31.2 seconds and was manually terminated without an artifact. No current probability evaluate, sweep, compare, or named-auditor result can therefore be claimed.

The latest prior direct national-focus probability evidence is partial and retained only as bounded context: inspect artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f1469cbac55712f783fdc91ec498b4b67f2d9dc1cbeb69d2e994983cce83bd9/e725b7f1b214121789545e44daa5b8d3a13deaa49835348fa3612469e001cc68/probability-inspect-9bf21fd9611b.json` reported an 88-candidate source pool, while the named-scenario evaluation artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5d67da588e64baf97275c7f593bbcf341b5fc54e7a5a03085577f7922a24af1/83ba84c1f3399178d4ed99cfa73a32027fb8a1a53efe3fa590e98085309988b3/probability-1573763df949cf7752a4877b.json` returned 440 candidate rows, 126 unresolved rows, and 34 diagnostics. Those artifacts do not prove exact focus-selection probabilities, route dominance, starvation, or live strategy-plan precedence.

The current DHR landing and rebellion probability handoffs also leave target-state, receipt, strategy-plan, and cadence inputs unresolved. No weighted AI patch was made, so no probability comparison was required or claimed.

## Missing, simplified, and unresolved content

No requested DHR focus route, category, focus ID, prerequisite, mutual exclusion, navigation shortcut, lifecycle hook, marker consumer, icon, localisation key, no-training boundary, or source AI block was found missing. The broader Kruger State Part 6 architecture describes different clone, machine, temporal, paleogenetic, xenobiological, singularity, and world-order families; those are not omissions from this DHR tree because the binding DHR addendum replaces them with the exact three-regime 88-focus contract.

The unresolved items are evidence or external-runtime limits:

- A fresh current `hoi4.focus_inspect` and `hoi4.focus_render` result after the latest availability/consumer state was not obtained because the bounded calls were manually terminated. Prior successful artifacts prove the unchanged topology only.
- The named `chaosx_ai_probability_auditor` route is unavailable, and direct current probability source/evaluate calls did not yield a usable current scenario result. Route-support priority remains unquantified.
- No live game, loaded focus UI, normal-zoom visual acceptance, tooltip interaction, paid-landing transaction, or runtime marker test was performed. These remain parent/user-owned acceptance surfaces.
- The country-scoped landing registry still needs the separate cross-provider/ownership-loss runtime matrix and legacy-save migration decision documented by the country package audit. This is not a focus-tree topology defect.

## High-priority follow-up

1. When the HOI4 MCP service is responsive, rerun `hoi4.focus_inspect` and `hoi4.focus_render` on the current source and record any post-availability diagnostics or changed layout hash.
2. Restore or expose `chaosx_ai_probability_auditor`, then run the named opening, wartime Imperial, stable-peace Synod, low-stability Covenant, crisis, and route-complete scenarios with complete focus histories, route flags, prerequisites, bypass state, strategy-plan state, and external factors. Use `hoi4.probability_evaluate`, threshold/sensitivity analysis, and an identical-scenario `hoi4.probability_compare` before changing weights.
3. Parent/user should perform live route, search-filter, normal-zoom, icon, tooltip, reward, lifecycle, landing-cost, and downstream-decision acceptance. This audit does not claim those results.
4. Keep the paid landing boundary and current marker consumers intact; do not add a free alien cohort, a duplicate decision, or a new focus route to address the unresolved probability/runtime evidence.

## Final disposition

Source-level audit result: the DHR focus tree is aligned with the accepted 88-focus architecture and exact `8/24/10/12/8/8/12/6` distribution, with mutually exclusive regime roots, intentional AND/OR prerequisite semantics, crisis choice locks, varied rewards, three lifecycle families, current marker consumers, complete static icon/localisation coverage, and inline/strategy-plan AI coverage.

The tree is not engine- or in-game-certified by this handoff. The unresolved MCP/probability/runtime limitations above must remain visible in the parent completion report.

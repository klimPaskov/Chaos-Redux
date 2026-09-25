# Event 016 D’Rhondan Focus Tree Current Audit

Date: 2026-09-25

Disposition: current-source audit completed with an actionable route-AI contract gap. Probability evidence and semantic reward review remain unresolved. No gameplay files were changed.

## Scope and evidence

Audited `common/national_focus/016_dhrondan_focus_tree.txt`, its focus AI strategy plan, DHR focus localisation and icon references, accepted DHR addendum/acceptance documents, and the 2026-08-22 and 2026-08-26 focus handoffs. The accepted design references are `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`, `docs/plans/016_brilliant_scientist_plans/016_alien_dhrondan_acceptance_scenarios.md`, and `docs/events/016_brilliant_scientist/systems/016_dhrondan_focus_tree.md`. Earlier handoffs were treated as historical context, not current validation.

The current focus MCP evidence is tied to source/data revision `56eb420d0b1010592c9196b615486cd156e04bdda829e9391cf77fcb3485d33d`; layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`.

`hoi4.focus_inspect` returned `FOCUS_INSPECTED`, status `ok`: 88 focuses, 88 resolved title keys, 102 connectors, and no DHR blocking diagnostics, connector crossings, node intersections, or long connectors. It reported x=2..40, y=0..22; maximum horizontal span 7, vertical span 3, Manhattan span 9. Its source/reference/layout validation passed.

`hoi4.focus_render` returned `FOCUS_RENDERED`, status `ok`, for the same tree and layout hash. It produced a 6992x2788 HTML render and SVG, JSON, source-map, and plan artifacts. No additional MCP calls were made after the parent requested a prompt handoff. The user's separate instruction prohibited model work.

Useful MCP artifacts:

- Inspect JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b171c9131142f04bf01b57dc06981603ab47d4d91f52368145ba67de0093521a/e1f59051ca0c1524525d9cdae2c90dfc3878dbefcbe0c64ccc3e192eb8bab73b/focus-inspect.56eb420d0b1010592c9196b615486cd156e04bdda829e9391cf77fcb3485d33d.json`
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a83c2ec50369dfba22ad44d9b8c764aad3aed368483b4b355d481c630f0b87b/763fba08193362ad6dbddfc20015d5b72988deb979ee7a4e834a84a81a9b5660/dhrondan_focus_tree.focus.html`
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289/1ecdd6858cbc35e4902c66d542ad466ec0f3fa4ceaa1e87a129beab46701843d/dhrondan_focus_tree.focus.svg`
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/424d134b212a6a1e72765c9b6ca546ff49aeb8f86971b619bf3e43c6b45537cc/7c094fa8f991c68e98842a3c9c6dcb1d54288248bcbbaf26d5e1bc611e799fed/dhrondan_focus_tree.focus.json`
- Render source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7fe92f97e96229e6d3d81e71c65ce15200a49ba8bfb6e7409a7d47895f544d72/8b0beec154759df0c965e56b0f0e2b787b50f4ac624b9b101460b7bb57818676/dhrondan_focus_tree.focus.source-map.json`
- Render plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0e2c9142474b96575d52ddcc3b79ce2784060893730aa59af717fa4838676d7/622dbc1b44143eddcd32b3a9bfa13da294d5fec6099c00cc6072815aee66da74/dhrondan_focus_tree.focus.plan.json`

The MCP response also contains an unrelated vanilla warning: `game:common/continuous_focus/generic.txt`, `continuous_restrict_freedom` lines 498–525, lacks `continuous_restrict_freedom_desc`. `MCP_INLINE_FILES_TRUNCATED` is informational; the inline file list was capped at 64 of 110 scanned paths. Neither is a DHR tree blocker.

Required offline wiki core pages and `National focus modding` were consulted, along with the listed focus-tree, event, decision/mission, asset, improvement-loop, and subagent skills. The installed vanilla documentation folder was enumerated, but its national-focus-specific documentation and a current vanilla focus precedent were not fully read in this audit; the earlier handoff’s vanilla precedent is historical evidence only. This documentation check is unresolved. No 3D model, model asset, or other asset production was touched.

## Route coverage

The accepted addendum calls for 88 focuses and the branch allocations below. Current source counts match those allocations; the MCP inspector reports all 88 focuses and no DHR layout or reference blocker.

| Route | Accepted/source count | Current source landmarks | Audit result |
|---|---:|---|---|
| Survival and landing network | 8 | `DHR_beneath_an_alien_sky` line 58 → `DHR_convene_the_two_world_throne` line 166 | Present |
| Imperial | 8 | `DHR_vael_ix_takes_the_throne` line 187 → `DHR_the_unbroken_imperial_line` line 281 | Present; route-AI condition gap below |
| Synod | 8 | `DHR_sera_qel_presents_the_calculus` line 300 → `DHR_the_government_of_certainties` line 394 | Present; route-AI condition gap below |
| Covenant | 8 | `DHR_ilyr_ren_opens_the_chamber` line 412 → `DHR_the_chamber_of_two_skies` line 507 | Present; route-AI condition gap below |
| Laboratory economy | 10 | `DHR_relight_the_field_laboratories` line 525 → `DHR_a_two_world_research_complex` line 635 | Present |
| Alien army and predictive warfare | 12 | `DHR_restore_the_predictive_staff` line 651 → `DHR_perfect_predictive_warfare` line 785 | Present |
| Orbital, air, and naval support | 8 | `DHR_reassemble_the_orbital_office` line 806 → `DHR_make_near_space_ours` line 905 | Present |
| Diplomacy and intelligence | 8 | `DHR_open_the_translation_bureaus` line 923 → `DHR_the_embassy_beyond_the_stars` line 1006 | Present |
| Expansion and world order | 12 | `DHR_define_the_two_worlds_question` line 1024 → `DHR_a_place_in_the_world_order` line 1165 | Present |
| Enclave crisis and late game | 6 | `DHR_the_enclaves_refuse_the_ledger` line 1180 → `DHR_the_century_beyond_exile` line 1258 | Present |

Current source shows mutually exclusive political capstones and descendants gated by the matching `dhrondan_focus_is_imperial`, `dhrondan_focus_is_synod`, or `dhrondan_focus_is_covenant` trigger family in `common/scripted_triggers/016_dhrondan_focus_triggers.txt:78-90`. Root examples: Vael’s `DHR_vael_ix_takes_the_throne` lines 187–198 excludes the Sera and Ilyr capstones; Sera’s `DHR_sera_qel_presents_the_calculus` lines 300–311 excludes Vael and Ilyr. Source inspection also found the Covenant root’s corresponding route exclusion. The tree converges into `DHR_define_the_two_worlds_question` at line 1024; the accepted design’s regime-capstone alternative is preserved as an OR gate. MCP reported no blocking prerequisite/reference diagnostics.

No omitted accepted route or clearly fake branch was proven. The tree header at `common/national_focus/016_dhrondan_focus_tree.txt:1-9` states that it does not create alien divisions or equipment and that it gates the paid landing contract, whose shared cost is 2,000 Alien Laser Weapons. This is consistent with the accepted landing-contract boundary.

## Actionable blocker: route AI does not encode the accepted distinctions

The DHR tree overview specifies Vael preference during war or at higher war support, Sera preference in peaceful/stable conditions, and Ilyr preference during peace with lower stability. Current root modifiers use only peace/war predicates:

| Focus ID | Current source | Current condition/effect | Accepted distinction not represented |
|---|---|---|---|
| `DHR_vael_ix_takes_the_throne` | `common/national_focus/016_dhrondan_focus_tree.txt:187-198` | Preferred base weight; factor 2 when `has_war = yes` | Higher war-support preference is absent |
| `DHR_sera_qel_presents_the_calculus` | `common/national_focus/016_dhrondan_focus_tree.txt:300-311` | Preferred base weight; factor 2 when `has_war = no` | Stability discrimination is absent |
| `DHR_ilyr_ren_opens_the_chamber` | `common/national_focus/016_dhrondan_focus_tree.txt:411-424` | Preferred base weight; factor 2 when `has_war = no` | Low-stability discrimination is absent; peaceful modifier matches Sera’s |

This is a source-to-accepted-design mismatch and should be resolved by the owning implementation agent. It is not a balance conclusion. Do not infer actual route selection likelihood from these multipliers or from `focus_inspect`.

### Current per-focus AI weight inventory

All 88 focus definitions have an `ai_will_do` weight in `common/national_focus/016_dhrondan_focus_tree.txt`; constants are declared at lines 16–20. This inventory records declared base weights only. It does not measure realized focus-selection probabilities.

| Weight token | Declared value | Focus count | Focus IDs |
|---|---:|---:|---|
| `@dhr_ai_preferred` | 10 | 39 | `DHR_inventory_the_expedition_stores`, `DHR_restore_the_landing_beacons`, `DHR_bind_the_enclaves`, `DHR_reopen_the_orbital_channel`, `DHR_vael_ix_takes_the_throne`, `DHR_restore_the_ninth_diadem`, `DHR_raise_the_palace_guard`, `DHR_proclaim_the_right_of_return`, `DHR_sera_qel_presents_the_calculus`, `DHR_audit_every_command_node`, `DHR_publish_the_survival_equations`, `DHR_replace_decree_with_prediction`, `DHR_ilyr_ren_opens_the_chamber`, `DHR_seat_the_human_delegates`, `DHR_elect_the_landing_councils`, `DHR_ratify_the_two_world_covenant`, `DHR_relight_the_field_laboratories`, `DHR_recover_the_laser_forges`, `DHR_the_twenty_element_substitution`, `DHR_feed_the_landing_reserve`, `DHR_join_the_scattered_laboratories`, `DHR_restore_the_predictive_staff`, `DHR_map_the_probability_front`, `DHR_rebuild_the_expeditionary_cadres`, `DHR_supply_before_the_order`, `DHR_command_without_surprise`, `DHR_the_foreseen_counterstroke`, `DHR_reassemble_the_orbital_office`, `DHR_chart_terrestrial_air_corridors`, `DHR_link_airfields_to_the_relay`, `DHR_guard_the_descent_windows`, `DHR_listen_to_the_human_airwaves`, `DHR_seed_the_enclave_network`, `DHR_choose_our_terrestrial_partners`, `DHR_restore_the_imperial_reaches`, `DHR_demand_the_origin_host`, `DHR_calculate_the_reclamation_zones`, `DHR_invite_the_enclave_congress`, `DHR_negotiate_the_origin_settlement` |
| `@dhr_ai_standard` | 5 | 26 | `DHR_bind_the_landing_lords`, `DHR_codify_imperial_service`, `DHR_crown_the_enclave_empire`, `DHR_elevate_the_first_calculants`, `DHR_assign_merit_by_projection`, `DHR_enthrone_the_synod`, `DHR_write_the_dual_citizenship_code`, `DHR_guarantee_the_right_to_depart`, `DHR_submit_the_military_to_debate`, `DHR_convert_terrestrial_workshops`, `DHR_crystal_growth_chambers`, `DHR_the_exoplanetary_materials_board`, `DHR_encode_the_enemy_reaction`, `DHR_train_human_signal_teams`, `DHR_the_thousand_branch_wargame`, `DHR_delegate_to_the_field_calculants`, `DHR_adapt_the_gravity_fighters`, `DHR_salvage_the_shuttle_docks`, `DHR_form_the_exile_flotilla`, `DHR_open_the_translation_bureaus`, `DHR_trade_in_impossible_materials`, `DHR_exchange_maps_for_access`, `DHR_recruit_two_world_operatives`, `DHR_subordinate_borders_to_need`, `DHR_offer_a_shared_horizon`, `DHR_break_the_separatist_ciphers` |
| `@dhr_ai_urgent` | 20 | 23 | `DHR_beneath_an_alien_sky`, `DHR_count_the_landing_states`, `DHR_secure_the_scattered_enclaves`, `DHR_convene_the_two_world_throne`, `DHR_the_unbroken_imperial_line`, `DHR_the_government_of_certainties`, `DHR_the_chamber_of_two_skies`, `DHR_standardize_alien_components`, `DHR_a_two_world_research_complex`, `DHR_fire_control_by_forecast`, `DHR_perfect_predictive_warfare`, `DHR_make_near_space_ours`, `DHR_the_embassy_beyond_the_stars`, `DHR_define_the_two_worlds_question`, `DHR_the_subject_world_protocol`, `DHR_administer_the_optimal_order`, `DHR_federate_the_two_worlds`, `DHR_begin_postwar_integration`, `DHR_a_place_in_the_world_order`, `DHR_the_enclaves_refuse_the_ledger`, `DHR_resolve_the_enclave_crisis`, `DHR_reopen_the_homeworld_corridor`, `DHR_the_century_beyond_exile` |

The separate `common/ai_strategy_plans/016_dhrondan_focus_ai.txt:1-173` has an opening plan and separate Imperial, Synod, and Covenant route plans. Its plan weights/factors are a second selection layer and are not represented in the per-focus inventory above. Their scenario effects have not been evaluated in this audit.

## Probability-auditor route and evidence status

At dispatch, the visible task/thread search found no existing DHR focus probability-audit task. One read-only task was then routed to `chaosx_ai_probability_auditor`, agent `01a0da01-5a02-7422-9c2b-2ea356f690c5` (“Probability Audit the 4th”), with no inherited context and an explicit request to inspect/evaluate/sweep all 88 focus weights and strategy plans under `dhr_opening_wartime`, `dhr_opening_peace_high_stability`, `dhr_opening_peace_low_stability`, `dhr_post_imperial`, `dhr_post_synod`, `dhr_post_covenant`, and `dhr_late_crisis`.

The routed task had not returned evidence when this handoff was completed. No current `hoi4.probability_inspect`, scenario evaluation/sweep, or `hoi4.probability_compare` artifact was available from that task. Its result and all scenario-specific route likelihoods remain unresolved. The historical 2026-08-22 probability note is partial and is not current evidence. Focus inspection/rendering is layout/reference evidence only; it does not establish balance. The parent should obtain the auditor’s evidence or record this as an outstanding probability-analysis gap before making any balance claim.

## Icon and localisation coverage

| Surface | Current evidence | Finding |
|---|---|---|
| Focus icon references | 88 focus definitions use 88 unique DHR icon tokens; current source inventory | No repeated token found |
| DHR icon DDS files | 88 matching DHR focus DDS files were found in the current asset inventory | Count aligns with focus references |
| MCP icon diagnostics | Current inspect/render returned no DHR missing-icon/reference diagnostic | No MCP-reported blocker |
| Direct GFX token-to-sprite mapping | Current local pattern check did not recognize the GFX naming form | Unresolved source-level cross-check; its parser result is not evidence of missing definitions |
| Focus title localisation | Current English file contains 88/88 focus title keys; MCP resolves 88/88 title keys | Covered |
| Focus description localisation | Current English file contains 88/88 `_desc` keys | Key coverage verified; full prose-to-reward semantic review unresolved |

Files: `interface/016_dhrondan_focus_icons.gfx`, the DHR focus icon DDS family, and `localisation/english/016_dhrondan_focus_l_english.yml`. No individual name/description/reward contradiction was verified in the bounded pass; a full per-focus semantic comparison against effects was not completed, so this is unresolved rather than a clean semantic sign-off.

## Missing/simplified content, rewards, and current warnings

- No missing accepted route or simplified route was demonstrated by the current 88-focus count, source branch inventory, and successful MCP inspect/render.
- No specific focus title/description versus reward mismatch was demonstrated. Full semantic review of all 88 reward blocks and localisation pairs remains unresolved.
- The accepted design’s 2,000 Alien Laser Weapons paid landing contract and no-free-alien-unit boundary are reflected in the focus-file header at lines 1–9. This source statement does not by itself validate every downstream decision/effect consumer.
- Current DHR MCP evidence has no blocking lint/layout finding. The only warning is the unrelated vanilla continuous-focus localisation key described above; the truncated MCP inline file inventory is informational.
- The installed vanilla documentation folder contains general script documentation but no listed national-focus-specific Markdown page. The required vanilla documentation/predecessor comparison was not completed in this pass and remains a documentation evidence gap, not a known DHR gameplay defect.

## Priority for parent review

1. Resolve the three route-condition gaps at the political roots (`DHR_vael_ix_takes_the_throne`, `DHR_sera_qel_presents_the_calculus`, `DHR_ilyr_ren_opens_the_chamber`) against the accepted war-support/stability distinctions. Any AI-weight or probability-bearing edit requires baseline and post-change probability audit through `chaosx_ai_probability_auditor` under matching named scenarios; this audit made no source edits.
2. Collect the already-routed auditor’s scenario-specific inspect/evaluate/sweep result. Until then, probability and balance are unresolved.
3. Complete direct GFX mapping and full reward/localisation semantic review if a complete icon/text sign-off is required.
4. Finish the current vanilla documentation and precedent check if required for the parent’s completion gate.

## Change boundary

Only this designated audit handoff is written by this task. No focus, localisation, AI plan, icon, model, or other gameplay/asset file was changed; nothing was staged or committed, and the game was not launched. Parent owns any implementation response.

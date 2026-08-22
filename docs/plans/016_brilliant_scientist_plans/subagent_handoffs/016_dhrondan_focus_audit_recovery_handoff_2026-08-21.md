# Empire of D'Rhonda Focus Audit and Recovery Handoff

Date: 2026-08-21

Owner: `/root/dhr_focus_audit_recovery`

Status: The requested narrow predictive-warfare API correction is applied. The accepted 88-focus topology is intact. Binary focus and idea textures remain an external asset blocker, and quantitative focus-AI evidence remains unresolved because the candidate-specific probability MCP route timed out.

## Changed files and identifiers

This audit changed only `common/national_focus/016_dhrondan_focus_tree.txt` and this handoff.

`DHR_perfect_predictive_warfare` at `common/national_focus/016_dhrondan_focus_tree.txt:783-798` now sets `chaosx_custom_technology_upgrade` to `constant:chaosx_custom_technology_upgrade.alien_predictive_warfare_weaponization` and calls `chaosx_grant_custom_technology_upgrade = yes` before the existing `dhrondan_focus_set_predictive_command = yes` helper and `dhrondan_predictive_warfare_perfected` flag.

No private custom-technology core helper, direct duplicate technology grant, route redesign, country file, decision file, event file, icon registry, or localisation entry was changed.

## Exact route coverage

The source parser and post-change `hoi4.focus_inspect` both report exactly 88 focuses.

| Route family | Count | Entry focus | Capstone focus | Result |
| --- | ---: | --- | --- | --- |
| Survival and landing network | 8 | `DHR_beneath_an_alien_sky` | `DHR_convene_the_two_world_throne` | Complete |
| Vael IX Imperial Continuity | 8 | `DHR_vael_ix_takes_the_throne` | `DHR_the_unbroken_imperial_line` | Complete |
| Sera Qel Predictive Synod | 8 | `DHR_sera_qel_presents_the_calculus` | `DHR_the_government_of_certainties` | Complete |
| Ilyr Ren Two-World Covenant | 8 | `DHR_ilyr_ren_opens_the_chamber` | `DHR_the_chamber_of_two_skies` | Complete |
| Laboratory economy | 10 | `DHR_relight_the_field_laboratories` | `DHR_a_two_world_research_complex` | Complete |
| Army and predictive warfare | 12 | `DHR_restore_the_predictive_staff` | `DHR_perfect_predictive_warfare` | Complete |
| Orbital, air, and naval support | 8 | `DHR_reassemble_the_orbital_office` | `DHR_make_near_space_ours` | Complete |
| Diplomacy and intelligence | 8 | `DHR_open_the_translation_bureaus` | `DHR_the_embassy_beyond_the_stars` | Complete |
| Expansion and world order | 12 | `DHR_define_the_two_worlds_question` | `DHR_a_place_in_the_world_order` | Complete |
| Enclave crisis and late game | 6 | `DHR_the_enclaves_refuse_the_ledger` | `DHR_the_century_beyond_exile` | Complete |
| **Total** | **88** |  |  | **Exact accepted count** |

The route roots are mutually exclusive at `common/national_focus/016_dhrondan_focus_tree.txt:185-191`, `:298-304`, and `:411-417`. Each root requires `DHR_convene_the_two_world_throne`, and each root excludes the other two regime roots. The crisis choices `DHR_offer_a_shared_horizon` and `DHR_break_the_separatist_ciphers` exclude one another at `:1181-1199`.

The source graph parser found one survival root, 88 reachable nodes, 102 prerequisite references, and no missing prerequisite or mutual-exclusion identifiers. The five intended lane leaves are `DHR_a_two_world_research_complex`, `DHR_perfect_predictive_warfare`, `DHR_make_near_space_ours`, `DHR_the_embassy_beyond_the_stars`, and `DHR_the_century_beyond_exile`; no non-root node is disconnected.

Separate prerequisite lines correctly express intended AND gates for `DHR_convene_the_two_world_throne`, each regime capstone, `DHR_standardize_alien_components`, `DHR_join_the_scattered_laboratories`, `DHR_fire_control_by_forecast`, `DHR_the_foreseen_counterstroke`, `DHR_make_near_space_ours`, `DHR_the_embassy_beyond_the_stars`, `DHR_begin_postwar_integration`, and the crisis resolver. Same-block regime-capstone and crisis-choice prerequisites retain intentional OR semantics, with mutual exclusions preventing simultaneous selection.

No fake branch, dead connector, bypass prerequisite, or route-lock gap was found in the accepted source. The layout engine reports 102 connectors, zero crossings, zero node intersections, and zero long connectors. Five same-row pairs are one column apart where the configured minimum is two; this is a non-blocking authored spacing warning already present in the accepted layout and was not rewritten because the bounded rewrite route rejected the current source as stale.

## Navigation and filters

The tree has ten shortcuts at `common/national_focus/016_dhrondan_focus_tree.txt:41-50`, covering the survival trunk, all three regime lanes, economy, army, orbital support, diplomacy, expansion, and crisis. Every one of the 88 focuses has a `search_filters` block and an `ai_will_do` block. The 14 registered search-filter tokens are vanilla tokens and are distributed across political, research, industry, stability, war-support, army, air, navy, manpower, trade, annexation, and character surfaces.

## Reward, unit, and spirit audit

The predictive capstone now has the following route behavior before and after the patch:

| Surface | Before | After |
| --- | --- | --- |
| Predictive lifecycle | Existing helper was present | Existing helper is preserved |
| Completion flag | `dhrondan_predictive_warfare_perfected` was present | Flag remains present |
| Reusable custom technology | No public upgrade call | Selector plus `chaosx_grant_custom_technology_upgrade = yes` grants the dependency-safe public upgrade |

`common/scripted_effects/016_dhrondan_focus_effects.txt:1-292` contains no `create_unit`, `add_equipment_to_stockpile`, `add_equipment_production`, production-line, division-template, or training effect. Building effects only add bounded state construction and the laboratory capstone adds one research slot. The landing boundary remains `DHR_reopen_the_orbital_channel` and `DHR_feed_the_landing_reserve`; the shared API cost is `constant:alien_infantry_landing.reserve_equipment`, exactly 2,000 laser weapons. The reserve focus only sets `dhrondan_landing_reserve_supply_priority` and does not create a unit, reserve equipment, or production line.

The three focus-created spirit families remain lifecycle-replaced rather than stacked: political settlement, predictive command, and off-world corridor. Each helper clears every idea in its family before adding the next stage, so at most three focus-created spirits can coexist.

No focus name or description/reward mismatch was found. Research, factories, command power, experience, political power, stability, war support, route flags, lifecycle ideas, and decision hooks are differentiated by branch identity rather than repeated generic payouts.

## Icon coverage

`interface/016_dhrondan_focus_icons.gfx` has exact one-to-one coverage for 88 focus icon tokens, 88 base sprite registrations, and 88 shine sprite registrations. No focus icon token is duplicated, and every shine registration intentionally reuses its matching base texture path.

| Family | Focus ids | Base sprites | Shine sprites | Unique goal DDS | Status |
| --- | ---: | ---: | ---: | ---: | --- |
| Survival | 8 | 8 | 8 | 8 | Registered; DDS absent |
| Imperial | 8 | 8 | 8 | 8 | Registered; DDS absent |
| Synod | 8 | 8 | 8 | 8 | Registered; DDS absent |
| Covenant | 8 | 8 | 8 | 8 | Registered; DDS absent |
| Laboratory | 10 | 10 | 10 | 10 | Registered; DDS absent |
| Army | 12 | 12 | 12 | 12 | Registered; DDS absent |
| Orbital | 8 | 8 | 8 | 8 | Registered; DDS absent |
| Diplomacy | 8 | 8 | 8 | 8 | Registered; DDS absent |
| Expansion | 12 | 12 | 12 | 12 | Registered; DDS absent |
| Crisis | 6 | 6 | 6 | 6 | Registered; DDS absent |
| Lifecycle ideas | 11 | 11 | n/a | 11 | Registered; DDS absent |
| **Total** | **88 focuses + 11 ideas** | **99 base** | **88 focus shine** | **99 unique** | **Separate asset handoff required** |

The 99 unique DDS paths are absent from the worktree by the accepted asset boundary. The post-change focus MCP diagnostics report 88 DHR focus texture errors plus 14 unrelated vanilla continuous-focus icon errors, for 102 blocking diagnostics. These are asset/reference diagnostics, not missing focus identifiers or duplicate registrations.

## Localisation and consumer audit

`localisation/english/016_dhrondan_focus_l_english.yml` contains 215 content keys plus the `l_english:` header, is UTF-8 with BOM, and contains all 88 focus names and all 88 focus descriptions. The predictive capstone keys at `:127-128` match the command-culture and dependency-safe technology reward. The paid landing tooltip at `:14` explicitly states that the request consumes no equipment and grants no free unit, matching the focus reward.

Stable focus-owned hooks have consumers as follows:

| Focus hook | Consumer evidence |
| --- | --- |
| `dhrondan_reclamation_declared` | `common/decisions/016_dhrondan_country_decisions.txt:11-50` enables `dhrondan_reclaim_landing_site` |
| `dhrondan_enclave_crisis_active` | `common/decisions/016_dhrondan_country_decisions.txt:59-91` enables enclave support and resolves the crisis |
| `dhrondan_integration_started` | `common/decisions/016_dhrondan_country_decisions.txt:91-126` enables reclaimed-state integration and Covenant compact flow |
| Route flags | `common/ai_strategy_plans/016_dhrondan_focus_ai.txt:39-173`, route triggers, and DHR character availability clauses |
| Achievement completion | `dhrondan_focus_award_achievement_hook` at `common/scripted_effects/016_dhrondan_focus_effects.txt:290-292` feeds the country achievement trigger |
| Public predictive upgrade | `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:105-206` and its documented selector table |
| DHR country events | `events/016_dhrondan_country_events.txt:1-113` owns `chaosx.nr16.48` through `.52` for sovereignty and compact outcomes |

`dhrondan_focus_has_landing_network` remains a stable landing hook, while `dhrondan_landing_reserve_supply_priority` is consumed by the shared landing decision's AI weighting. The generic landing decision remains receipt-gated through the public alien-infantry API, as specified by the shared owner contract.

## AI behavior and probability evidence

The retained focus AI surface is `common/ai_strategy_plans/016_dhrondan_focus_ai.txt`, containing one opening plan and three route plans. The opening plan aborts when any regime route exists. Each route plan is enabled and aborted by the corresponding `dhrondan_focus_is_imperial`, `dhrondan_focus_is_synod`, or `dhrondan_focus_is_covenant` trigger. The focus tree also supplies route-sensitive root and crisis weights, while all 88 focuses retain inline AI weights.

The duplicate `common/ai_strategy_plans/016_dhrondan_country_plans.txt` was not edited in this task because the parent assigned its removal to the country owner; the retained focus-plan file is the audited source of truth.

`hoi4.probability_inspect` with adapter `national_focus_ai_will_do` discovered all 88 available candidates, but the adapter reported `identifierMatches = 0` for the tree identifier and returned no evaluable candidate set. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00ca82592d2039f89ff9441ca4f769512db2ef346738cd30ebe01ee6dde53d03/eb26bee6db6ac0e395c63a43a53d073c5112c7ca71320262fa2501199d537681/probability-inspect-ded3f6f67e11.json`.

A bounded candidate-specific retry for `DHR_perfect_predictive_warfare` returned the exact MCP blocker `tool call failed for hoi4_agent_tools/hoi4.probability_inspect` followed by `Caused by: timed out awaiting tools/call after 180s`. No evaluate, sweep, compare, ranking, scenario hash, or normalized probability claim is made. The required `chaosx_ai_probability_auditor` route must complete named-scenario evaluation after the adapter accepts a candidate identifier.

## Mandatory MCP focus evidence

Post-change `hoi4.focus_inspect` succeeded with status `FOCUS_INSPECTED` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/499c1bbe8fcf31e45d8de679a08a0f7376c6e1858af8314a82cbb7eb06ff3e4d/1b294203b0f3916576bb3f729ae8867b30a9ebe0e7d6fe8c9a9a0072af5719ab/focus-inspect.81263a006d87199a.json`.

The inspect result reports `focusCount = 88`, layout hash `6f6605398964d2a7b6fa02d051bab7a888e980f816c3bc48f4f6738b10773556`, 102 connectors, zero crossings, zero node intersections, and zero long connectors. Validation remains false only because of 102 icon diagnostics described above.

Post-change `hoi4.focus_render` succeeded with HTML, SVG, JSON, source-map, and plan artifacts. Review artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35cc0efe7584fe43f477e65b21c7b486ed0b3cd8aaf55c0e3351b1c237478623/4954c631269af5e85542d2b951e0aca621615cf5e41b6dfd7c3c72bdf0951218/dhrondan_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c4618da253a5c04f4b7c9a2a8dafd785b7ec9917342a7bb08e1435dccee147f4/e12e62f27d8caef7a6ddc23657dd0dda2a00a232392e0d93018d7ce9b062184f/dhrondan_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2302fbc1c8e5cf1c38a81fce5486950c2217d898517d7a0ce9d52c2946d7e522/3897b8ed4f6d51cc8e27bade41ff96903b74904d93615312ffe45e83279921d0/dhrondan_focus_tree.focus.json`.

A bounded existing-tree `hoi4.focus_rewrite` retry was attempted with compact layout parameters after the API patch. It returned `REWRITE_SOURCE_STALE: Rewrite failed and automatic recovery could not be completed`, with `changedFiles: []`; the source hash and authored layout were unchanged. The installed tool surface exposes no `hoi4.focus_compare` route, so no comparison artifact is claimed.

## Validation and remaining risks

Meaningful checks completed were the source focus-block parser, exact route grouping, prerequisite and mutual-exclusion reference graph, icon-token/GFX registration comparison, localisation-key/BOM audit, public custom-technology API reference audit, paid-landing effect search, post-change focus inspect, post-change focus render, and probability source discovery.

Skipped meaningful checks are candidate-specific probability evaluation/sweep/compare because of the exact 180-second MCP timeout, focus compare because the route is not exposed, and live HOI4 runtime validation because game launch and live consumer acceptance belong to the parent/user.

Remaining risks are the 99 absent binary DDS assets, the unresolved candidate-specific AI probability evidence, the five non-blocking same-row spacing warnings, and the owner-boundary decision over whether the generic landing decision should consume the DHR landing-network hook. No broad route family, formable chain, country identity, or unrelated focus file was changed. No commit was created.

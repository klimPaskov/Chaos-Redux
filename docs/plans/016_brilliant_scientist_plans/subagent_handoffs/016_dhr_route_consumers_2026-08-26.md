# Event 016 D’Rhondan route-consumer patch handoff — 2026-08-26

> Historical route-consumer snapshot. The survival-marker section is superseded by `016_dhrondan_survival_marker_consumption_2026-08-26.md`, which wires the four opening survival markers into the live landing and enclave decision AI. The five route-support markers listed below were already consumed by the current decision and trigger sources when this snapshot was written.

Status: narrow world-order consumer patch applied and audited. The accepted 88-focus tree remains unchanged. Generic route-support AI priorities remain unresolved because the required `chaosx_ai_probability_auditor` route is not callable in this runtime.

## Scope and references

The audited focus source is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\common\national_focus\016_dhrondan_focus_tree.txt`.

The decision and trigger consumers are `common\decisions\016_dhrondan_country_decisions.txt` and `common\scripted_triggers\016_dhrondan_country_triggers.txt`.

I read `AGENTS.md`, the required offline Paradox wiki pages, the relevant vanilla documentation and focus examples, the `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, and `chaos-redux-subagents` skills, the accepted D’Rhonda focus specification at `docs\events\016_brilliant_scientist\systems\016_dhrondan_focus_tree.md`, the country decision contract at `docs\events\016_brilliant_scientist\systems\dhrondan_country.md`, and the previous accepted focus audit handoff at `docs\plans\016_brilliant_scientist_plans\subagent_handoffs\016_dhrondan_focus_audit_2026-08-25.md`.

## Changed files and identifiers

| File | Identifiers | Change |
|---|---|---|
| `common\scripted_triggers\016_dhrondan_country_triggers.txt` | `dhrondan_world_order_decisions_are_unlocked`, `dhrondan_world_order_claim_contract_is_ready`, `dhrondan_world_order_route_is_complete`, `dhrondan_reclamation_decision_can_complete` | Added stable country-scope consumers for the focus-owned world-order markers and required the claim contract when a reclamation is running. |
| `common\decisions\016_dhrondan_country_decisions.txt` | `dhrondan_reclaim_landing_site`, `dhrondan_establish_enclave_supply_bridge`, `dhrondan_integrate_reclaimed_landing_site`, `dhrondan_offer_two_world_compact` | Added the world-order unlock boundary to each existing decision. Reclamation uses the claim-specific contract, and enclave support uses the completed world-order route. |

No focus id, icon id, localisation key, reward value, route root, prerequisite, mutual exclusion, country identity, event id, formable, or AI weight was changed.

## Downstream marker coverage

| Marker | Producer | Consumer after patch | Status |
|---|---|---|---|
| `dhrondan_two_worlds_question_defined` | `DHR_define_the_two_worlds_question`, `common\national_focus\016_dhrondan_focus_tree.txt:1018` | `dhrondan_world_order_decisions_are_unlocked` | Consumed as the question-side unlock proof. |
| `dhrondan_world_order_decisions_unlocked` | `dhrondan_focus_open_world_order`, `common\scripted_effects\016_dhrondan_focus_effects.txt:283-287` | Integration and Covenant compact target-root triggers, plus the claim and route helper triggers | Consumed by existing decision surfaces. |
| `dhrondan_world_order_claim_contract_ready` | `dhrondan_focus_open_world_order`, `common\scripted_effects\016_dhrondan_focus_effects.txt:283-287` | `dhrondan_reclaim_landing_site` and `dhrondan_reclamation_decision_can_complete` | Consumed by the existing reclamation decision and its cancellation/revalidation path. |
| `dhrondan_world_order_route_complete` | `DHR_a_place_in_the_world_order`, `common\national_focus\016_dhrondan_focus_tree.txt:1159` | `dhrondan_establish_enclave_supply_bridge` through `dhrondan_world_order_route_is_complete` | Consumed by the existing crisis-support decision. |
| `dhrondan_reclamation_declared` | Imperial, Synod, and Covenant expansion focuses | Existing reclamation decision | Existing consumer preserved. |
| `dhrondan_integration_started` | `DHR_begin_postwar_integration` | Existing integration and Covenant compact decisions | Existing consumers preserved. |
| `dhrondan_enclave_crisis_active` / `dhrondan_enclave_crisis_resolved` | Crisis focuses and decision/effect resolution | Existing crisis decision and route effects | Existing consumers preserved. |
| `dhrondan_alien_components_standardized` | `DHR_standardize_alien_components`, line 592 | None | Still an unowned future support-route hook. |
| `dhrondan_laboratory_route_complete` | `DHR_a_two_world_research_complex`, line 641 | None | Still an unowned future support-route hook. |
| `dhrondan_predictive_warfare_perfected` | `DHR_perfect_predictive_warfare`, line 795 | None | Still an unowned future support-route hook. |
| `dhrondan_orbital_office_reassembled` | `DHR_reassemble_the_orbital_office`, line 812 | None | Still an unowned future support-route hook. |
| `dhrondan_access_map_exchange_ready` | `DHR_exchange_maps_for_access`, line 953 | None | Still an unowned future support-route hook. |

The five support-route markers have no accepted existing decision or event contract that can safely consume them. They remain documented as unresolved rather than being turned into new gates that would make optional support lanes mandatory.

## Route coverage

| Route family | Count | Entry | Capstone | Result |
|---|---:|---|---|---|
| Survival/opening | 8 | `DHR_beneath_an_alien_sky` | `DHR_convene_the_two_world_throne` | Complete |
| Political routes | 24 | `DHR_vael_ix_takes_the_throne`, `DHR_sera_qel_presents_the_calculus`, `DHR_ilyr_ren_opens_the_chamber` | `DHR_the_unbroken_imperial_line`, `DHR_the_government_of_certainties`, `DHR_the_chamber_of_two_skies` | Three mutually exclusive 8-focus routes complete |
| Laboratory | 10 | `DHR_relight_the_field_laboratories` | `DHR_a_two_world_research_complex` | Complete |
| Army/predictive | 12 | `DHR_restore_the_predictive_staff` | `DHR_perfect_predictive_warfare` | Complete |
| Orbital/air/naval | 8 | `DHR_reassemble_the_orbital_office` | `DHR_make_near_space_ours` | Complete |
| Diplomacy/intelligence | 8 | `DHR_open_the_translation_bureaus` | `DHR_the_embassy_beyond_the_stars` | Complete |
| Expansion/world order | 12 | `DHR_define_the_two_worlds_question` | `DHR_a_place_in_the_world_order` | Complete and now connected to existing decision unlocks |
| Crisis/late game | 6 | `DHR_the_enclaves_refuse_the_ledger` | `DHR_the_century_beyond_exile` | Complete |
| **Total** | **88** |  |  | **Exact accepted count preserved** |

## Icons, localisation, and reward mismatches

| Surface | Evidence | Finding |
|---|---|---|
| Focus icons | `interface\016_dhrondan_focus_icons.gfx`, `gfx\interface\goals\016_dhrondan_focus\`, and the focus render | All 88 focus ids have registered `GFX_goal_DHR_*` base/shine references. No DHR icon diagnostic was returned. |
| Lifecycle ideas | `gfx\interface\ideas\016_dhrondan_focus\` | The 11 lifecycle idea icons remain separate and registered. |
| Localisation | `localisation\english\016_dhrondan_focus_l_english.yml` | The accepted audit found all 88 title/description pairs and seven custom effect tooltip keys. No localisation key changed in this patch. |
| Rewards and names | `common\national_focus\016_dhrondan_focus_tree.txt:592,641,795,812,953,1018,1159` | Names describe production standards, research capacity, predictive warfare, orbital support, access exchange, and world-order contracts respectively. No mismatch was found. |

The fresh render reported only the unrelated vanilla warning that `continuous_restrict_freedom_desc` is missing from `game:common/continuous_focus/generic.txt`; this is outside Event 016 and was not changed.

## AI behavior gaps

`common\ai_strategy_plans\016_dhrondan_focus_ai.txt` has one opening plan and three route plans, with inline `ai_will_do` blocks for all 88 focuses.

The opening plan lists all eight survival focuses and aborts after a regime route is selected. Imperial explicitly lists predictive warfare, orbital security, reclamation, and cipher suppression. Synod explicitly lists laboratory, predictive warfare, calculated reclamation, and cipher suppression. Covenant explicitly lists diplomacy, research, orbital support, negotiated federation, and reconciliation.

The route plan lists omit generic support priorities that remain available through inline focus weights. Examples include the Imperial plan omitting `DHR_relight_the_field_laboratories` and `DHR_join_the_scattered_laboratories`, the Synod plan omitting most orbital and diplomacy support, and the Covenant plan omitting the army lane and several laboratory/orbital support focuses. This is a route-AI priority gap, not a dead focus gap.

A fresh `hoi4.probability_inspect` national-focus source pass returned 88 candidates with no source diagnostics at artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f1469cbac55712f783fdc91ec498b4b67f2d9dc1cbeb69d2e994983cce83bd9/e725b7f1b214121789545e44daa5b8d3a13deaa49835348fa3612469e001cc68/probability-inspect-9bf21fd9611b.json`.

The prior named-scenario evaluation remains partial with 440 candidate rows, 126 unresolved rows, and 34 diagnostics because completion histories and route-state eligibility were not supplied. Its analysis artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5d67da588e64baf97275c7f593bbcf341b5fc54e7a5a03085577f7922a24af1/83ba84c1f3399178d4ed99cfa73a32027fb8a1a53efe3fa590e98085309988b3/probability-1573763df949cf7752a4877b.json`.

The exact blocker is that `ALL_TOOLS` exposes the HOI4 probability MCP tools but no callable `chaosx_ai_probability_auditor` custom-agent route. Therefore no AI priority patch was applied and no before/after probability compare is claimed.

## MCP and validation evidence

The required read-only focus inspection completed after the patch with `FOCUS_INSPECTED`, no blockers, and no DHR layout diagnostics when run with lane/node spacing 2. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da7fe449678611a8ece139a327432e6a333f4ee03369a89e937e0a0cc284e051/a129e655022e1d5b0cc14144512e389ff69d0f9873e3fc26d631434d3588379f/focus-inspect.dd9cd68addd5b2ba.json`.

The required read-only focus render completed after the patch with `FOCUS_RENDERED` and no blockers. HTML, SVG, JSON, source-map, and plan artifacts are available from `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/91f17bf9c55fd6f44f5dad76824be7ffe0b5ad01dbac2a32b23bbec8b855207d/c60001456f25ec062f9af3318cdc9d73bce5b30074a84f6e47ccffa7b2f9872e/dhrondan_focus_tree.focus.html`, with sibling artifacts in the same render result.

Source checks found exactly 88 unique `DHR_` focus ids and no duplicate focus ids. The changed trigger names resolve at every decision callsite, and the world-order markers now have explicit decision consumers without changing focus count or route topology.

No Hearts of Iron IV process was launched. No live decision GUI or runtime state test was performed because the repository boundary assigns live consumer validation to the user.

## Before and after route behavior

Before the patch, valid descendant focus order implicitly made the four existing sovereignty decisions reachable while their focus-owned world-order markers remained unused.

After the patch, the same valid focus sequence reaches the same decisions and keeps all existing costs, effects, target checks, AI weights, and localisation. The decision surfaces now fail closed if the promised world-order unlock, claim contract, or completed route marker is absent, and a running reclamation is cancelled or rejected if its claim contract is absent.

## Remaining route risks and handoff

The five support-route marker flags remain reserved hooks without an accepted current consumer. Adding new decisions, claims, formables, or mandatory support-lane gates would exceed this bounded patch.

The generic route-support AI priorities remain unresolved until a callable `chaosx_ai_probability_auditor` can run named opening, wartime, stable-peace, and route-complete scenarios followed by a same-scenario `hoi4.probability_compare`.

The current focus render/inspect still uses the accepted graph and count. Layout polish beyond the accepted tree, ordinary decision GUI inspection, and live runtime validation remain outside this patch.

No Git commit was created because the shared worktree contains unrelated changes; the parent should review and stage only the two gameplay files and this handoff under `docs\plans\016_brilliant_scientist_plans\subagent_handoffs\016_dhr_route_consumers_2026-08-26.md`.

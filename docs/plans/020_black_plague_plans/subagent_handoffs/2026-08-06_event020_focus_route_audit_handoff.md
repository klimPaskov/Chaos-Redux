# Event 020 focus route audit handoff — 2026-08-06

Scope: the RTA Rat Nation tree and RTX Rat King tree, including route locks, prerequisite semantics, focus depth, icons, localisation coverage, origin-gated loading, and focus-side AI evidence.

## Disposition

The bounded route audit found two RTA prerequisite locks and corrected them in `common/national_focus/020_black_plague_rat_focus_tree.txt`. No RTX source change was needed. Both trees now have complete title/description/icon/cost/reward coverage in the audited files, and the final MCP inspect pass reports no Event 020 diagnostics. The shared MCP run still reports fourteen unrelated vanilla continuous-focus icon diagnostics; those are outside Event 020 ownership.

## Changed files and focus identifiers

| File | Focus identifiers | Change |
| --- | --- | --- |
| `common/national_focus/020_black_plague_rat_focus_tree.txt` | `black_plague_rat_route_convergence` | The prerequisite group at lines 737–740 now contains the Preserve and Consume focuses in one top-level group, which is the supported HOI4 OR form. The existing `available` OR gate remains as the player-facing route check. |
| `common/national_focus/020_black_plague_rat_focus_tree.txt` | `black_plague_rat_rivals_detected` | Lines 819–827 now require `black_plague_rat_route_convergence` in one prerequisite group and one of the four military methods in a second top-level group. This preserves AND between convergence and the selected method while using the supported top-level multi-focus OR form for the method choice. |

No localisation, icon, AI strategy, event, decision, idea, country-history, or GFX file changed in this pass.

## Route coverage table

| Required route surface | Implemented branch and identifiers | Status |
| --- | --- | --- |
| RTA awakening and survival | `black_plague_rat_first_warren` → `black_plague_rat_listen_to_the_drains` → `black_plague_rat_feral_quarantine` / `black_plague_rat_no_human_rations` | Present. The tree is origin-gated and the opening rewards set non-human initialization flags and Brood Mass rather than human industry. |
| RTA origin adaptation | Urban `black_plague_rat_urban_warren` → `black_plague_rat_cellar_cities` → `black_plague_rat_city_breachers`; Field `black_plague_rat_field_brood` → `black_plague_rat_grain_pockets` → `black_plague_rat_long_grass_ambush`; Dock `black_plague_rat_dock_brood` → `black_plague_rat_tide_pipes` → `black_plague_rat_wharf_raids`; War `black_plague_rat_war_brood` → `black_plague_rat_rail_hunters` → `black_plague_rat_frontline_burrows` | Present. The four origin terminals feed the shared capped-pulse trunk and distinct second lanes. |
| RTA hierarchy and Coherence | Mutually exclusive `black_plague_rat_four_mouths`, `black_plague_rat_choose_a_voice`, `black_plague_rat_read_the_marks`, with follow-ups `black_plague_rat_many_nests_one_signal`, `black_plague_rat_fang_above_the_warren`, and `black_plague_rat_stolen_route_memory` | Present. The three command methods remain mutually exclusive and remove `black_plague_rat_fractured_instinct` in their rewards. |
| RTA growth and mutation | `black_plague_rat_mass_swarm`, `black_plague_rat_giant_mutation`, and `black_plague_rat_burrow_warfare` | Present. The three mutation peaks are mutually exclusive and feed the economy lane. |
| RTA territorial plague economy | `black_plague_rat_preserve_the_herd` and `black_plague_rat_consume_the_state`, mutually exclusive, followed by `black_plague_rat_route_convergence` | Present after the correction. Both policy routes now reach convergence. |
| RTA military method | `black_plague_rat_flood_the_front`, `black_plague_rat_break_strongpoints`, `black_plague_rat_hunt_the_roads`, and `black_plague_rat_hold_the_nest`, mutually exclusive, followed by `black_plague_rat_rivals_detected` | Present after the correction. Every method now reaches rivalry and proto-sentience. |
| RTA rival absorption and proto-sentience | `black_plague_rat_challenge_weaker_brood` / `black_plague_rat_resist_stronger_brood` → `black_plague_rat_absorb_and_integrate` → `black_plague_rat_symbols_and_maps` → `black_plague_rat_command_between_nests` → `black_plague_rat_prepare_the_crown` | Present. The late lane sets candidate flags and Sentience/Coherence variables rather than directly creating RTX. |
| RTA shared depth trunk | `black_plague_rat_capped_pulses`, `black_plague_rat_pressure_matrix`, plus archetype second lanes `black_plague_rat_citadel_warrens`, `black_plague_rat_grain_tunnels`, `black_plague_rat_tide_court`, `black_plague_rat_frontline_command`, and `black_plague_rat_immune_blood` | Present. The capped-pulse `available` block requires one hierarchy follow-up and one origin terminal. |
| RTX coronation and transfer stabilisation | `black_plague_rat_king_the_royal_basin` → `black_plague_rat_king_crown_the_broods` → `black_plague_rat_king_listen_to_the_crown` → `black_plague_rat_king_first_royal_decree`, with refuge/capital branches and `black_plague_rat_king_the_four_registers` | Present. The initializer loads the tree only after the separate RTX country owns a valid royal basin. |
| RTX government route family | Mutually exclusive Absolute Crown (`black_plague_rat_absolute_crown` → `black_plague_rat_absolute_throne` → `black_plague_rat_crown_tax` → `black_plague_rat_court_of_teeth`), Council (`black_plague_rat_brood_council` → `black_plague_rat_council_seats` → `black_plague_rat_shared_hunger` → `black_plague_rat_warren_charter`), and Black Breath Hierophancy (`black_plague_rat_breath_hierophancy` → `black_plague_rat_black_breath_liturgy` → `black_plague_rat_omens_in_burrows` → `black_plague_rat_crown_of_ash`) | Present. Each route records a route flag and shared core-route completion. |
| RTX population policy | Crown preserve, Council selective harvest, and Hierophant empty-cities route | Present. Each policy is route-gated and mutually exclusive in the tree's intended government branch. |
| RTX military and plague mastery | `black_plague_rat_royal_armouries` → `black_plague_rat_crown_brutes`, `black_plague_rat_tunnel_columns`, `black_plague_rat_tail_guard`, `black_plague_rat_sea_brood` → `black_plague_rat_royal_template_lock` | Present. The armoury gate requires the four-register trunk and one completed government terminal; the template lock intentionally waits for all four royal templates. |
| RTX internal crises | `black_plague_rat_hunger_court`, `black_plague_rat_brood_succession`, `black_plague_rat_human_minds_in_chains`, and `black_plague_rat_refugee_memory` → `black_plague_rat_solve_the_first_crisis` | Present. All four crisis dimensions are required before resolution, matching the deep-tree failure-state design. |
| RTX government-specific depth | Crown lane through `black_plague_rat_crown_final_edict`; Council lane through `black_plague_rat_council_charter_of_nests`; Hierophant lane through `black_plague_rat_hierophant_terminal_omen` | Present. Each lane is gated by its selected government route and changes the royal variables. |
| RTX shared terminal and Evolution V preparation | `black_plague_rat_royal_node_watch`, `black_plague_rat_crown_strike_preparations`, `black_plague_rat_cartography_of_capitals`, `black_plague_rat_map_the_refuge_nodes`, `black_plague_rat_terminal_cryptography`, `black_plague_rat_dominion_over_roads`, `black_plague_rat_terminal_armature`, `black_plague_rat_terminal_sentience`, `black_plague_rat_terminal_cohesion`, and `black_plague_rat_earned_terminal_route` | Present. The final focus requires the global Evolution V route flag plus Sentience and Brood Cohesion thresholds. |

The current tree sizes are 52 RTA focus roles and 71 RTX focus roles. This meets the RTA architecture target of roughly forty to fifty roles within the accepted implementation tolerance and the RTX architecture lower bound of roughly seventy roles.

## Missing or simplified content

- No route family, mutual-exclusion branch, or terminal focus required by the two tree architecture sections was missing in the audited source.
- The focus-side rewards are intentionally abstract state/flag updates and existing event hooks rather than ordinary factories, manpower, equipment, or direct Rat King creation. The event, decision, and pulse consumers remain outside this narrow focus patch and are owned by the parent audit passes.
- The RTX tree has inline `ai_will_do` blocks on 14 of 71 focus roles, while the remaining route behavior is supplied by `common/ai_strategy/020_black_plague_rat_ai_strategy.txt`. This is a review risk rather than a source omission because the strategy plans are route-gated, but branch-selection dominance still needs the parent probability auditor's scenario analysis.

## Icon coverage table

| Tree | Focus roles | Unique icon families | Static sprite and shine coverage | Result |
| --- | ---: | ---: | --- | --- |
| RTA `black_plague_rat_focus_tree` | 52 | 13 | Every referenced `GFX_goal_black_plague_rat_*` has a matching `spriteType` and `_shine` sibling in `interface/020_black_plague_rat_identity.gfx`; MCP scanned all referenced Event 020 DDS files. | Complete. |
| RTX `black_plague_rat_king_focus_tree` | 71 | 14 | Every referenced `GFX_goal_black_plague_rat_*` has a matching `spriteType` and `_shine` sibling in the same `.gfx`; MCP scanned all referenced Event 020 DDS files. | Complete. |

The MCP diagnostics that remain are the fourteen unrelated vanilla continuous-focus palette icon references, not Event 020 focus icons.

## Localisation and reward mismatch list

The static key audit found zero missing title keys, zero missing `_desc` keys, zero duplicate focus IDs, and zero missing focus icon references for both trees. Every focus block has `search_filters`, `icon`, `cost`, and `completion_reward`. Sampled route rewards match their names: Preserve/Consume set policy flags and Brood Mass, military methods set distinct route flags and event hooks, government terminals set route flags and the appropriate Dominion/Sentience/Cohesion values, and the terminal route sets the Evolution V completion flags.

No localisation or reward mismatch was identified in this pass.

## AI behavior gaps

- The source-level AI strategy plans are route-aware for RTA archetype, second-lane, hierarchy, mutation/military, and RTX government routes in `common/ai_strategy/020_black_plague_rat_ai_strategy.txt:23-436`.
- Inline focus AI coverage is uneven. RTA has 35 of 52 focus blocks with `ai_will_do`; RTX has 14 of 71. Most RTX deep-lane and crisis focuses rely on default focus selection plus route strategy plans, so ordinary AI may not prioritize the intended crisis or terminal ordering without a scenario-weight audit.
- The current `hoi4.probability_inspect` source passes found 52 RTA candidates with five required inputs and 71 RTX candidates with six required inputs. Both candidate pools are incomplete, so the results are source-discovery evidence only and do not establish normalized focus probabilities or route dominance. The parent probability auditor should run named RTA archetype/economy/military scenarios and RTX government/crisis/terminal scenarios, then compare any proposed AI weights.

## High-priority fixes first

1. Keep the two RTA prerequisite corrections in `common/national_focus/020_black_plague_rat_focus_tree.txt:737-740` and `819-827`. Replacing the supported top-level multi-focus OR groups with nested `OR` blocks produces `FOCUS_PREREQUISITE_GROUP_MALFORMED` in the installed MCP parser and makes downstream focuses unreachable.
2. Have the parent probability auditor evaluate route-choice ordering for RTA preserve/consume and four military methods, plus RTX Crown/Council/Hierophancy and crisis/terminal choices. Do not infer probabilities from the incomplete source-inspection pool.
3. If the probability audit finds branch starvation, add only narrow focus `ai_will_do` modifiers or route strategy factors and rerun `hoi4.probability_compare`; do not redesign either tree in this pass.

## MCP evidence

### RTA final inspect

`hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `black_plague_rat_focus_tree` with 52 focuses, 50 connectors, zero crossings, zero node intersections, zero long connectors, and layout hash `9b62e3206ed26a11a48793a905db1d1593fa352057cabba3417f410c26256987`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/817d677799a5a990d6082baa01d3676768c73f332c96fd55f4d3625697b5c831/912df526abc60e2307d00720c044ea76f3146f2515d1a6c1672bb24567f19f2d/focus-inspect.d84c539a9abe5622.json`.

`hoi4.focus_render` returned `FOCUS_RENDERED` after the final source correction. The HTML and SVG artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c7778b72c41a32df5f19d19af9fa374c241c78fa82a5dcf7ff236f2a45d1b06/9f3228ffaf5f641e9e2e53e2f875dc5284ed5da38ca7bad11bb7af61b2666ca8/black_plague_rat_focus_tree.focus.html` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/80e08999ba7371a4acaee5f157dec05610ddb5a00a14317ec231931f03153d48/a8d12d1add1efc033e3425d5a900e5b04d3831b194e41f5b67a12c03ec72d7ed/black_plague_rat_focus_tree.focus.svg`.

### RTX inspect and render

`hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `black_plague_rat_king_focus_tree` with 71 focuses, 73 connectors, zero crossings, zero node intersections, zero long connectors, and layout hash `e80849e1e36f82f8f914954d387346b598d454ed170dc0cc6f63076bb6cff1a4`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16ebc5e6a9e2e4165a4a186e9cae6555664b9162edeca326d65f637a12baebb5/79632d2e9136881b61f66bcd1def68924eeffbb7ae4f1c427c142370e5292b56/focus-inspect.a89d4a7b76388f17.json`.

`hoi4.focus_render` returned `FOCUS_RENDERED`. The HTML artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61a187d2394aa2a2fe2924c82d8d722da75a354b57c5eb985ca2c659b97a9fc3/27b34ba3dd279517bac30bb5795a8fe014b243a6b32a33559ec5ab68cb9e56d0/black_plague_rat_king_focus_tree.focus.html` and the SVG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fa44d96a794c112f7a704d534ed498056f4e6dd70d0cda90e02b189202e8ebc2/df850fb42c11d10ecfb4d5b33598e9f24955a2b321f9db7bb452986bc924df73/black_plague_rat_king_focus_tree.focus.svg`.

### Probability source discovery

Current-source `hoi4.probability_inspect` with the `national_focus_ai_will_do` adapter returned no diagnostics and an incomplete pool of 52 RTA candidates with five required inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3561d40aa1d648104ecfc846ee850143f9e9f23fdd24d34cf7536311362b1ab/bdacb35b48c26bd5dd272c86cb6d1a7f55b522474d974fcdf2ac4172add9097b/probability-inspect-af981aca0589.json`.

The RTX source discovery returned no diagnostics and an incomplete pool of 71 candidates with six required inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b6b9dcbf7dba82a5984c04e42aaeaf42fae6a1caa7ba3083dbbc8e9590e4e055/48525d9f488ef5e17cce8b302d3f79e3182476eddda6bd9e8738ae42e568c7d6/probability-inspect-5cd85432168e.json`.

## Validation and limits

- The final RTA `hoi4.focus_inspect` and `hoi4.focus_render` passes were run after the parent restored the supported top-level multi-focus prerequisite syntax. Event 020 diagnostics were zero in the final inspect; the remaining diagnostics are the known vanilla continuous-focus palette references.
- Static PowerShell reconciliation found 52 RTA focus blocks and 71 RTX focus blocks, no duplicate IDs, no missing title or description keys, no missing icon or `_shine` definitions, and no focus lacking `search_filters`, `icon`, `cost`, or `completion_reward`.
- The source was not passed through `hoi4.focus_rewrite` because the accepted change is a two-block prerequisite correction and the authored layout is already stable; inspect and render provide the required post-change engine-tool evidence.
- No `hoi4.probability_evaluate`, `hoi4.probability_sweep`, or `hoi4.probability_compare` claim is made here because the parent probability auditor owns the named scenario analysis and both source pools are incomplete.
- No Hearts of Iron IV executable, save, or live focus-click test was run because live consumer validation belongs to the parent/user boundary.

## Remaining route risks

- RTX inline focus AI is sparse outside the three government roots, selected side lanes, crisis resolver, and terminal route. The route strategy plans are present, but scenario evidence is still needed to show the AI does not starve deep crisis or terminal branches.
- Focus-side flag consumers in Event 020 events, decisions, and scripted pulse logic are cross-file surfaces. This handoff confirms the focus producers and selected event hooks but does not replace the parent event, decision, scripted-system, localisation, asset, or live acceptance audits.
- MCP focus diagnostics continue to include fourteen unrelated vanilla continuous-focus icon references. They should not be attributed to the Event 020 trees.

Plan handoff path: this file, `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-06_event020_focus_route_audit_handoff.md`.

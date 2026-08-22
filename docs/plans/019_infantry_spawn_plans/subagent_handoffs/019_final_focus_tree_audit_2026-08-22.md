# Event 19 derivative focus tree final audit

Date: 2026-08-22

Scope: `common/national_focus/019_infantry_spawn_derivative_focus.txt`, its `.focus-plan.json` sidecar, and directly related Event 19 focus localisation and icon wiring. The audit was kept bounded to the `infantry_spawn_derivative_focus_tree` tree and did not modify unrelated concurrent work.

## Outcome

The tree contains 45 focuses, 54 connectors, and the complete 30-focus shared route plus five-focus zombie, ghost, and golem family overlays described by the Event 19 route map. Every family route remains behind its own route lock and every derivative package remains behind the package-active trigger. No source-level world-end, evolution, super-event, parent-tag, parent-count, parent-stage, or scripted-GUI route was found in the focus file.

I made one narrow geometry pass that moved six focuses into the intended authored lanes and synchronized the sidecar source hash and preferred coordinates. No localisation, icon, idea, decision, or scripted helper file was changed by this audit.

This is an audit handoff rather than a claim that every MCP advisory has been removed. The post-change MCP view is structurally clean, but two auto-layout detour diagnostics and intentional hidden-branch sibling-anchor diagnostics remain documented below.

## Files changed by this audit

| File | Change |
| --- | --- |
| `common/national_focus/019_infantry_spawn_derivative_focus.txt` | Six authored `x` coordinates adjusted; no focus IDs, prerequisites, rewards, AI weights, icons, or route gates changed. |
| `common/national_focus/019_infantry_spawn_derivative_focus.focus-plan.json` | Updated `sourceHash` and the six matching `preferredX` values; all other sidecar content retained. |
| `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_focus_tree_audit_2026-08-22.md` | This audit evidence and handoff. |

The working tree already contained concurrent edits to Event 19 scripted effects and localisation. Those files were inspected where needed and left untouched.

## Changed focus IDs and route behavior

| Focus ID | Before | After | Reason and behavior impact |
| --- | --- | --- | --- |
| `infantry_spawn_derivative_name_the_future_host` | `x = 0, y = 4` | `x = -1, y = 4` | Keeps the opening trunk on the authored center lane below `restore_a_chain_of_orders`; prerequisites and reward are unchanged. |
| `infantry_spawn_derivative_read_the_neighboring_frontiers` | `x = -1, y = 12` | `x = -2, y = 12` | Aligns the former-parent pressure lane with the method focus at `x = -2`; route gates and sequential ordering are unchanged. |
| `infantry_spawn_derivative_issue_the_submission_terms` | `x = -1, y = 13` | `x = -2, y = 13` | Keeps submission terms in the same visible lane as its predecessor; decision unlocks and AI weight are unchanged. |
| `infantry_spawn_derivative_absorb_the_conquered_districts` | `x = -1, y = 14` | `x = -2, y = 14` | Keeps district integration in the former-parent lane; no claims, cores, tags, or world-end effects are introduced. |
| `infantry_spawn_derivative_turn_the_host_outward` | `x = -1, y = 15` | `x = -2, y = 15` | Keeps the regional ambition lane aligned with its preceding integration focuses; reward and route lock are unchanged. |
| `infantry_spawn_derivative_become_the_regional_predator` | `x = -1, y = 16` | `x = -2, y = 16` | Aligns the terminal regional capstone with the expansion lane; its existing controlled-state, war-victory, former-parent, and family-completion gates remain intact. |

The source SHA-256 after the patch is `1e6aa2df3af4b1fd3d1ccf225dd78ae64702551a690c072eebffaa4a9d1bf155`. The sidecar SHA-256 is `3c9b1430d6e3665ed070a7393f5cd31cbf47d5ce83cc2003aebbaff7f749116a`.

## Route coverage

| Route segment | Focus coverage | Review result |
| --- | --- | --- |
| Event-created opening and survival | `hold_the_first_ground` through `name_the_future_host` (5) | Present. Package activation and derivative-country gating are preserved. |
| Hierarchy selection | `crown_the_claimant`, `one_voice_over_the_host`, `end_the_old_chain_of_rule` (3) | Present. The three roots are mutually exclusive; claimant availability uses the claimant trigger, while council/species roots exclude claimant breakaway. |
| Hierarchy support and shared coordination | `assign_command_estates`, `convene_the_host_council`, `bind_the_district_councils`, `no_host_abandoned`, `obey_the_family_instinct`, `mark_the_family_domain` (6) | Present. Child prerequisites are branch-local and no parent route counters or evolutions are touched. |
| Sustainment and method choice | `mark_the_muster_depots`, `reopen_captured_workshops`, `open_the_living_corridor`, `count_every_obligation`, `quiet_the_fragmented_columns`, `outlast_the_former_state`, `make_an_army_of_the_host`, and the three mutually exclusive method focuses (9) | Present. Shared sustainment leads to one of three methods; `make_an_army_of_the_host` accepts any mutually exclusive hierarchy capstone through one OR prerequisite block, which matches HOI4 semantics. |
| Former-parent survival and regional ambition | `a_method_fit_for_the_host`, `read_the_neighboring_frontiers`, `issue_the_submission_terms`, `absorb_the_conquered_districts`, `turn_the_host_outward`, `become_the_regional_predator` (6) | Present and sequential. The former-parent and controlled-territory gates remain in source. |
| Zombie derivative overlay | `zombie_scavenge_the_abandoned_barracks` through `zombie_a_realm_of_base_dead` (5) | Present. All five use zombie route locks and `allow_branch`; no parent progression or world-end route is referenced. |
| Ghost derivative overlay | `ghost_mark_the_first_anchors` through `ghost_a_pale_dominion` (5) | Present. All five use ghost route locks and `allow_branch`; no parent progression or world-end route is referenced. |
| Golem derivative overlay | `golem_recover_the_broken_coal` through `golem_a_march_of_living_stone` (5) | Present. All five use golem route locks and `allow_branch`; no parent progression or world-end route is referenced. |

The route map therefore has 45 total nodes and 35 visible nodes for each nonhuman derivative package (30 shared plus its five-focus family overlay). The claimant route intentionally uses the shared claimant hierarchy lane and claimant decisions instead of a claimant family overlay.

## Missing or simplified content

- No route named by the Event 19 route map is missing from the source.
- The expansion and submission/integration section is intentionally a sequential focus lane whose decision unlocks provide the interaction surface; it is not a two-arm visible fork. This is the existing route-map simplification and should be a parent design decision if a broader rework is desired.
- The claimant package intentionally has no zombie, ghost, or golem family overlay because its family ID is `none`; this preserves claimant isolation and is not a missing nonhuman route.
- No broad depth or reward-variety patch was justified in this bounded audit. The 45-focus tree is within the specified 25–35 focus-equivalent adapted-country scale.

## Icon coverage

| Surface | Coverage | Evidence |
| --- | --- | --- |
| Focus icon references | 45/45 focus blocks have unique `icon` references. | `common/national_focus/019_infantry_spawn_derivative_focus.txt` and `interface/019_infantry_spawn.gfx`. |
| Base and shine sprites | 45/45 base sprites and 45/45 shine sprites resolve. | `interface/019_infantry_spawn.gfx`. |
| DDS payloads | 45/45 DDS files exist, have valid DDS headers, and are 100x88. | `gfx/interface/goals/019_infantry_spawn/`. |
| Art subject constraint | Focus references resolve to army-scene assets; no focus source reference points to a human portrait focal figure. | Source and icon wiring audit. |

No icon ID was changed. No new art was requested because the existing Event 19 package has complete coverage.

## Localisation and reward review

All 45 focus title, description, and completion-tooltip keys resolve in the Event 19 English localisation file. All 45 `custom_effect_tooltip` reward keys resolve, and no reward-key mismatch was found. The localisation file retains UTF-8 BOM encoding.

One low-priority hover redundancy remains: `infantry_spawn_derivative_inventory_the_seized_districts` and `infantry_spawn_derivative_mark_the_muster_depots` both set `infantry_spawn_derivative_depot_operations_unlocked`, and both tooltips describe unlocking `Secure a Muster Depot`. This is an intentional convergent decision unlock rather than a missing reward. I did not alter the concurrently edited localisation surface.

No changed focus ID required a localisation rename, so no localisation keys or icon IDs changed in this audit.

## AI behavior and probability evidence

All 45 focuses expose non-zero `ai_will_do` blocks using the existing Event 19 AI constants. Focus-level availability and route locks are present for all shared, hierarchy, method, and family focuses. The source contains no focus AI edits in this patch.

`hoi4.probability_inspect` was run with adapter `national_focus_ai_will_do` against the Event 19 source. It found 45 candidates with eligibility and weight blocks but marked the analysis as scenario-dependent because package flags, route variables, prerequisites, external factors, and ordered AI strategy plans require runtime state.

`hoi4.probability_evaluate` was run with an explicit empty-state scenario. It returned `PROBABILITY_ANALYZED_PARTIAL`, withheld normalized probabilities because the candidate pool was incomplete, and recorded unresolved route/package inputs. This is a tooling scenario limitation, not evidence of a focus weight defect. The same source and scenarios were not sent through `hoi4.probability_compare` because no AI weight or probability-bearing gameplay value was changed.

The parent should retain the existing AI audit finding that dynamic runtime ranking requires a manifest scenario containing an active derivative package, each hierarchy/family route, former-parent pressure state, and complete prerequisite state. No new AI behavior gap was justified by this audit.

## MCP artifacts and diagnostics

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

Baseline `hoi4.focus_inspect` artifact: [focus-inspect baseline](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61765f94588dec94c6c1a937eda6ce3dfcb1bf6b96762a17ccb521952ae3af3d/d4677a09d2b86da782d33c6ab604acf29b7e6526e877d2e25aa890b6ee05e742/focus-inspect.9bd9653c72fa6583.json).

Post-change `hoi4.focus_inspect` artifact: [focus-inspect post-change](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/45d3a28019c52356e1a3b7783d9f8c78a1e0214b3ae05e5b0194dac0ea584966/6547363e4be71b2432da951f727377cd7157a4d49959e0236c352d24d1122985/focus-inspect.57567781e71ba0b4.json).

Post-change `hoi4.focus_render` artifacts: [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0d2c47fd69febe19e611b73b2a48b18acf78bc2cdc358f430341661319ada449/2ec22da3a3d6b3c2b5720978c55d706c9ef01457c7033b3c40be7cd917edf862/infantry_spawn_derivative_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed5121c8110e4ab427f32373b695b9f7fa54698c180daf8b2042859d280a7841/f4d42b0c4fa6fed59032024cb605cfe86fb9f9c786a2536a9856ee4b12d8d591/infantry_spawn_derivative_focus_tree.focus.svg), and [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66671713f05b9e821610ec2105baeacf560b0dcb7e99fc4c46239e514943b359/759832cc35acbfb5543d37909a6cdee3aaca5294f03a1d2a2abf822ae09dd2f4/infantry_spawn_derivative_focus_tree.focus.json).

Post-change `hoi4.focus_raster` artifacts: [PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dffe966802c24917a2deaf4922e1ff7895e283b63ad8662497037c0b2b6e110f/d60e7c0fbcd56beaa1b2f0b7f28b3045a9256b2913d126de413e22d7d47ace92/infantry_spawn_derivative_focus_tree.focus.png), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3e4179ca8392fb637d10dbb1dec5c4e6bac6556ab91f7f47a9a1d4ae932a593f/668ecd9258e673b548f71c67830d9e1e1f79b08b4c68efda345cf903ee8c0ad1/infantry_spawn_derivative_focus_tree.focus.svg), and [raster JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/66671713f05b9e821610ec2105baeacf560b0dcb7e99fc4c46239e514943b359/7c2249d7134e2aa5b2e4f25b5b6fd17bcdee4ee59a1610c6506d35f5561886c3/infantry_spawn_derivative_focus_tree.focus.json).

Probability inspection artifact: [AI probability source inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/72661f3181a1b8a1c01fe6f6af5218635877a851c1c38cde2918b34f34b6829a/e50aff5e39dad287d0ae38c9a4004985e5b455d13bc8e94b8bbc14a706295be2/probability-inspect-5d7ea783689b.json).

Partial probability evaluation artifact: [AI probability partial evaluation](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/799af1dc0524bd86e4afd8e95574204303bc3a953e8bb013bd7a878eb508831c/30048d67a0c2f27b4adc55c8fc173cc53b077f656245aad972010fa302a0ab6b/probability-f5fafb4dbfa6b12693985820.json).

The post-change inspect reported zero connector crossings, zero node intersections, and zero long connectors. It still reported two linear-detour diagnostics (`restore_a_chain_of_orders` to `name_the_future_host`, and `quiet_the_fragmented_columns` to `outlast_the_former_state`), four sibling-anchor deviations, one broad sibling asymmetry, and the unrelated generic vanilla `continuous_restrict_freedom_desc` localisation warning.

The opening detour remains even though the authored source and sidecar now use `x = -1` for both opening focuses because the MCP sidecar uses `autoPosition.mode = auto` and re-centers part of the layout. The sustainment detour would require moving `outlast_the_former_state` into the `x = 2` method lane, which conflicts with `arm_the_captured_auxiliaries` at the next row. Both issues are broader lane-layout decisions rather than safe one-line fixes.

## Validation and skipped validation

- Source parsing found 45 focus blocks, 45 unique IDs, 45 unique authored coordinates, zero unknown prerequisite or mutual-exclusion references, symmetric mutual exclusions, 15 `allow_branch` family nodes, and nine family route-specific locks.
- Source isolation checks found zero direct references to scripted GUI, country events, world-end, evolution, super-event, claims, cores, focus-tree reload, global flags, or tag changes.
- Localisation checks found all Event 19 title, description, tooltip, and reward keys, with no duplicate keys in the scanned localisation set.
- Icon checks found 45/45 source references, base sprites, shine sprites, and DDS payloads with valid 100x88 dimensions.
- `hoi4.focus_inspect` supplied the available diagnostics and validation pass; the installed focus MCP surface exposes no separate focus lint command.
- `hoi4.focus_render` and `hoi4.focus_raster` were both rerun after the source and sidecar patch.
- No `hoi4.focus_rewrite` was used because the needed change was a narrow authored-coordinate edit and a compact rewrite risked broad auto-layout churn.
- No live HOI4 run was performed, per repository policy.
- No probability comparison was run because this patch changed no AI weight or other probability-bearing value.
- A dedicated `chaosx_focus_tree_auditor` or `chaosx_ai_probability_auditor` child handoff could not be spawned in this runtime; the direct MCP probability inspection and source checks are recorded with their partial-runtime limitation.

## Remaining risks and parent decisions

1. Decide whether to accept the two remaining MCP linear-detour diagnostics or schedule a broader, sidecar-aware lane reflow. Do not churn more authored coordinates without first changing the auto-layout strategy or reviewing the full sustainment geometry.
2. Decide whether the convergent `Secure a Muster Depot` tooltip should be made more explicit in a future localisation-only pass. It is not a gameplay or reward defect.
3. Retain the existing sequential decision-backed expansion simplification unless the parent approves a broader route redesign.
4. Keep the unrelated generic vanilla continuous-focus localisation warning outside Event 19 scope.

No new improvement plan was written because the tree is not shallow and the remaining findings are either accepted route simplifications, auto-layout diagnostics, or parent-level design choices.

Handoff path: `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_final_focus_tree_audit_2026-08-22.md`.

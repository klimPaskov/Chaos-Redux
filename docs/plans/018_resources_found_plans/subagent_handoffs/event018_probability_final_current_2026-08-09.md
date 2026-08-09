# Event 018 probability audit handoff

Date: 2026-08-09

Status: CONDITIONAL

This is a read-only weighted-logic handoff for Event 018, Resources Found. No gameplay, AI, event, focus, decision, mission, or runtime file was changed. The result is conditional because several source scans are durable, while the required full campaign pools and typed runtime predicates remain incomplete or unavailable in the installed MCP adapter.

## Scope and source inventory

The audited weighted surfaces are:

| Surface | Adapter | Source |
| --- | --- | --- |
| Cave-country focus selection | `national_focus_ai_will_do` | `common/national_focus/018_resources_found_cave_focus_tree.txt` |
| Event option choices | `event_option_ai_chance` | `events/018_random_resource.txt` |
| Resource-field decisions | `decision_ai_will_do` | `common/decisions/018_resources_found_decisions.txt` |
| Pre-fire random pools | `random_list` | `common/scripted_effects/018_resources_found_prefire_effects.txt` |
| Cave brood random pool | `random_list` | `common/scripted_effects/018_resources_found_cave_effects.txt` |
| Mission scores | `mission_ai_will_do` | Event 018 decision sources queried by the adapter |
| Event MTTH | `event_mean_time_to_happen` | Event 018 event and scripted MTTH sources queried by the adapter |
| Direct random blocks | `direct_random` | Event 018 sources queried by the adapter |
| AI strategy factors | `ai_strategy_factor` | Event 018 AI sources queried by the adapter |

The Event 018 specifications require dynamic field-owner, foreign-buyer, claimant, cave-country, evolution, closure, and world-end behavior. Those inputs include ownership, control, state validity, resource deficit, war, terrain, safety, depth, disturbance, breach pressure, contracts, claims, neighbors, enemy profiles, evolution settings, and terminal-state flags.

## MCP structural evidence

The mandatory read-only structural pass is retained in the current validation record.

- Focus inspect reports 67 focuses, 81 connectors, and zero Event 018 layout diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6fde52f83f338e2239e0f7f4fc09397c692b5389d95f1be8389968c98161be8c/22a178972ecffca07fbcf0fcb776a265999116ac8f33922c8db3659dc5c65eaf/focus-inspect.6c0c228a72f5e3d4.json`.
- Focus render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1bbe413dc31ffc8000592b4d838f820e76b0f98253601d7bc68473317ef6a7a7/fe68dfef3c5b7d3783b866713a77fedd74180098f2ea4d4795cc1335e0446f7c/018_resources_found_cave_focus_tree.focus.svg`.
- The current source intentionally has no hostile-air availability gate on `DHO_harden_against_the_sky`. It is a proactive adaptation after `Surface Senses`, so a country that declines one hostile-air response event cannot strand the shared continental or world-end route. This is a route-design fact, not a proven balance defect.
- Event namespace inspection returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62c9fec699b991370524339b03e190f6d6bfeb78643095cab53d39da42f779eb/f1dc3a093411c304e1679770c7f21a1499181a07d68e12b72ac8faf67743b16c/event-scan-8c2577b32af5.json`.
- Event overview render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c08b6f85263b7016cf6a27f6fdabe9884f743cc8e0af4a2aec0cb4bb32a909b/b6017c9ae12897b112b9e300e8b99ea453da68e44852cd069f6ead80a3cc390c/event-overview-8c2577b32af5.svg`.
- Focused Event 018 state-flow artifacts cover `chaosx.nr18.1`, `.40`, `.50`, `.60`, `.80`, `.85`, and `.98` in `018_current_mcp_validation_2026-08-09.md`. The event analyzer deferred workspace-wide helper and delayed-delivery projection, so live event timing is not proven.

## Probability inspection evidence

All results below separate source inspection from campaign probability. A discovered candidate count is not a complete selectable pool unless the adapter proves completeness.

### Cave-country focus selection

The current focus source has 67 candidates and 13 required inputs. `poolComplete = false` because the complete available-focus pool depends on campaign focus prerequisites, bypasses, route state, strategy factors, and external engine state.

The retained full baseline evaluation was partial. `analysisId = probability-930fbfb6fb8e5dc271afcce4, scenarioHash = 2f1fcc325fa6593155874e496638bad4f14055f91c0bcefcb1b2662b157773cb`, with 54 unresolved inputs and 13 diagnostics.

Classification: partial score race evidence only. The focus adapter models independent focus scores, not weight divided by the sum of weights. No exact focus selection probability, route dominance claim, starvation claim, or live-AI ordering claim is made.

The prior 17-choice hierarchy, doctrine, adaptation, and world-end route comparison returned zero comparison changes after `Count Every Vein` and `Chamber Autonomy` were restored. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b244c9b7db10df5cf3310f8278860ba0cddc7b203b4c20cfa2a23c86c685e4cc/76fd0818fdfaa8b679534d5cc1cabf833c326fcea5dd3288c5873431b073d744/probability-d70f9208e81183f42c66164c.json`. The comparison is partial and proves no regression only in the declared scenarios.

Named focus scenarios retained for parent review are `focus_route_hierarchy`, `focus_route_doctrine`, `focus_route_adaptation`, and `focus_route_world_end`. Country control, variable, neighbor, enemy, terrain, and route predicates remain unresolved in the adapter.

### Event-option `ai_chance`

Inspection of `events/018_random_resource.txt` found 204 candidates, 18 required inputs, and one unresolved or unsupported source construct. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0c2d454067550af4b1e1bee70d08066f34635412b7aa9740a4e1c2a99ab0070c/0f0cdd753ef0395fc465a211d5d59f59116c5bca546769a30ff0ae9532db0770/probability-inspect-6999853c6a9d.json`.

Classification: source inspection only and unresolved. The option pool is not proven complete, so no normalized option probability or rank claim is valid. The unresolved construct must be preserved as an adapter limitation until a bounded complete option pool is evaluated.

### Resource-field decisions

Inspection of `common/decisions/018_resources_found_decisions.txt` found 113 candidates and 24 required inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b380d7e41215265d903aaab20f68440b10b15609ad5433120005167000dcdd47/1c4eb3b1c95fd4d5ef4a606ab8a7a6e3198cb36e22df5e59dc9241408aa6b4ee/probability-inspect-1ad8325d1d12.json`.

The full-source no-pool evaluation returned `INTERNAL_ERROR`. Bounded decision pools succeeded in the prior audit, but no durable complete-world pool artifact is retained here. Classification: bounded or score-only evidence, not normalized click probability. The adapter cannot prove target validity, cost affordability, cooldown, selected-field state, ownership, contracts, or evolution gates for the whole category.

### Pre-fire random pools

Current inspection of `common/scripted_effects/018_resources_found_prefire_effects.txt` found six candidates across three pools, four required inputs, one unresolved input, and `poolComplete = false`. Current source revision is `07279392e1e6e1d5c85fa5f1f7c2105171ad3c7fbbc139b1dda844964937f946`; source hash is `7674b88a5e7f22ad34e643f889509a56d7a9db0c76654d084e49130e7e421861`. Current inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c8b7c057a3effbcfbb72b6f0d4798ce21e61510000ad28cce5a5b0b28aae67f/0fa26164390baa53e5ecdbc1e640486b38b23b4491a46ed8dc736813f6c3eacd/probability-inspect-7674b88a5e7f.json`.

Two named bounded scenarios have exact evidence:

| Scenario id | Complete pool supplied | Result | Classification |
| --- | --- | --- | --- |
| `prefire_fresh_field` | `{fresh_field, enrich_active_field}` | Fresh-field support 60, enrichment support 40 | Exact bounded result |
| `prefire_enrichment_field` | `{fresh_field, enrich_active_field}` | Fresh-field support 60, enrichment support 40 | Exact bounded result |

The exact two-candidate evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bde1eac5999d06a940e1827622fff33e9726b14c65a07dafda5b0bc87c64606/8b6618fd38837987c2219f5f362d8c8bab9b99e5631b844e0dffac19e6d02da5/probability-852293bece395baaa19ff7bc.json`. It reports exact support of 0.6 and 0.4 for the supplied pool. This does not prove the other pre-fire pools or their external predicates.

The retained four-scenario request timed out after 180 seconds. A later maximum-enrichment request returned `Transport closed` without a result. No sweep or simulation was run.

### Cave brood random pool

The retained cave brood inspection found five candidates in one pool, a complete candidate pool, and no unresolved construct. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/413c66f9e64ac3bf58eca7b0b4fc14c53553bdf9a4b0457c74bd4e138b94b037/1316e8b64e0dfef5ebc94d88220b8f381a0f01d2782d5a114ec99d84410935bc/probability-inspect-ae4058423879.json`.

Named exact bounded scenarios:

- `cave_brood_default`: only the 50-weight default War-Brood entry is positive. Stone Phalanx and Feeding Chamber Guard entries are zero because their route unlocks are absent.
- `cave_brood_stone_guard`: raw weights are 50 default War-Brood, 15 Stone Phalanx, and 5 Feeding Chamber Guard. The complete pool, ranking, matrix, and unresolved views are retained in `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b12ec94d1d11c72b5ecff74a1d26c76d42b1b734026da49b3f3a828d1f6c918c/cacf15a98758a3e7ca44ec5d17dd47f40a325e5d69be5579858c940fb211b68a/probability-9cee6f54ecfaf0eb46501930.json`.

The dominance and starvation warnings are expected from zero-weight route-incompatible entries. They are not evidence that unavailable entries can be selected. No balance defect is proven by these warnings.

## Adapter limitations and unresolved surfaces

- Mission inspection returned `PROBABILITY_SURFACE_EMPTY` for Event 018. The implementation uses decision scores rather than mission scores for this surface, so no mission probability claim is made.
- Event MTTH inspection returned `PROBABILITY_SURFACE_EMPTY` for the queried Event 018 sources. The specification uses scripted MTTH variables and evolution pacing rather than a directly discoverable event `mean_time_to_happen` block. No exact timing claim is made.
- Direct-random and AI-strategy-factor no-pool requests sometimes returned `INTERNAL_ERROR`. Source-only review cannot substitute for the required MCP route.
- Focus, event-option, and decision no-pool requests also returned `INTERNAL_ERROR` during the recovery call. Retained artifacts above remain the durable evidence for those surfaces.
- Typed campaign-state predicates for control, ownership, neighbors, enemy profiles, terrain, variables, and evolution settings were not accepted by the adapter. Do not force them into scenarios or infer their values.
- No `probability_sweep`, `probability_simulate`, or `probability_sequence` result is claimed. No sweep was justified without a complete declared pool and typed state ranges. No simulation was justified because uncertain inputs were not declared. No sequence was justified because a complete cadence, recovery, cooldown, removal, reset, cap, and terminal-state manifest was not available.
- No durable standalone `probability_render` artifact was retained for incomplete focus, event-option, or decision analyses. The cave artifact retains ranking, matrix, and unresolved views. Structural focus and event render URIs are listed above.

## Findings and recommended fixes

No confirmed numeric AI-balance defect is proven by the available MCP evidence.

1. Keep the proactive `DHO_harden_against_the_sky` route gate as authored unless the focus owner supplies a typed hostile-air scenario that proves a safe conditional gate. Reintroducing an event-dependent gate risks route starvation.
2. Evaluate the complete 67-focus pool under named valid and invalid route states once the adapter accepts typed country, enemy, terrain, neighbor, and variable predicates. Positive score on an impossible focus must be hidden, bypassed, or weighted to zero.
3. Enumerate complete Event 018 option pools and resolve the one unsupported event-option construct before claiming option dominance or normalized `ai_chance`.
4. Split the 113 decision candidates into bounded phase and selected-field pools with validity, cost, cooldown, owner, contract, evolution, and closure predicates. Re-run `probability_evaluate`, `probability_sweep`, and `probability_render` after the adapter can type those predicates.
5. Evaluate each of the three pre-fire pools independently. Preserve the exact 60/40 result only for the declared two-candidate scenarios.
6. Keep the cave brood fallback weight and route unlock checks explicit. The current 50 versus 15 versus 5 result is acceptable as bounded evidence, but the owner should review whether the default fallback is intended to dominate when route unlocks are unavailable.

## Completion classification

`CONDITIONAL`.

Exact evidence exists for the declared two-candidate pre-fire pool and the complete cave brood pool. Structural focus and event MCP passes are partial but have zero Event 018 blocking diagnostics. Focus, event-option, decision, mission, MTTH, direct-random, and strategy-factor campaign conclusions remain partial or unresolved because of incomplete pools, unresolved inputs, adapter errors, and unavailable typed runtime predicates. Parent review and a future same-scenario probability compare remain required before any weighted source change or hard balance claim.

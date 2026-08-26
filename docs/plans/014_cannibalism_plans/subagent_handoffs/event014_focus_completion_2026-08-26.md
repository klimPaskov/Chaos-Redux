# Event 014 focus completion audit

Date: 2026-08-26

Decision: the current Event 014 focus source is complete for the requested route, layout, icon, localisation, reveal-gate, and special-unit checks. No gameplay, focus, GFX, or localisation patch was justified. The only new file from this audit is this handoff.

## Scope and authority

The owned source surface was `common/national_focus/014_cannibalism_focus.txt`, its directly linked focus icon registrations in `interface/014_cannibalism.gfx`, focus localisation in `localisation/english/014_cannibalism_l_english.yml`, and this handoff.

The source was checked against `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_5_focus_tree_architecture.md`, `docs/specs/014_cannibalism_specs/matrices/focus_route_matrix.md`, `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md`, and the Event 014 anti-spoiler and hidden-identity audits.

The required offline references were read from `paradox_wiki/` for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding. Relevant vanilla documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/` for effects, triggers, modifiers, script concepts, and constants, with vanilla national-focus precedents inspected in the installed game files.

## Route coverage

| Tree | Required | Current | Route coverage and source references |
| --- | ---: | ---: | --- |
| Unified CBL | 108 | 108 | Opening convergence at lines 43-151, three mutually exclusive warlord-disposition routes at lines 155-341, three mutually exclusive supreme-hierarchy routes at lines 342-558, Continental Larder and four methods at lines 559-864, army and special-unit progression at lines 865-1047, navy at lines 1048-1148, air at lines 1149-1242, intelligence and cells at lines 1243-1352, expansion at lines 1353-1410, counterwar at lines 1411-1463, and ordinary terminal preparation at lines 1464-1511. |
| Reusable Warlord | 68 | 68 | Six-focus survival trunk at lines 1546-1670, three four-focus hierarchy routes at lines 1671-1915, shared Larder and three methods at lines 1916-2133, military and special-unit progression at lines 2134-2315, four-focus Island, Siege, and March overlays at lines 2316-2564, regional expansion and infiltration at lines 2565-2727, and ten-focus Evolution II alignment, manipulation, and defiance routes at lines 2728-2935. |
| Original-ZZZ Wendigo overlay | 28 | 28 | Five merge-trunk focuses at lines 2974-3094, five winter-hunger focuses at lines 3095-3199, five paid Pack progression focuses at lines 3200-3298, five cannibal-inheritance focuses at lines 3299-3409, five transformation-countdown focuses at lines 3410-3527, and three alternate-terminal focuses at lines 3528-3605. |
| Total | 204 | 204 | All three top-level `focus_tree` blocks are present at lines 24, 1527, and 2953. |

The static source graph has zero dangling prerequisite or mutual-exclusion references. Unified has 103 prerequisite blocks and 103 prerequisite references plus 24 mutual-exclusion references. Warlord has 73 prerequisite blocks and 79 prerequisite references plus 18 mutual-exclusion references. Wendigo has 28 prerequisite blocks and 28 prerequisite references with no mutual-exclusion route group.

The grouped prerequisite semantics match the offline National focus modding reference. Repeated prerequisite blocks remain AND requirements, while same-block alternatives remain OR requirements at `cannibalism_warlord_discipline_the_warbands` (line 2137) and `cannibalism_warlord_raid_the_neighboring_states` (line 2568). The multi-parent gates at `CBL_open_the_continental_ledger` (line 129), `CBL_coordinate_the_three_armies` (line 1021), `cannibalism_warlord_name_the_first_lieutenants` (line 1632), and `ZZZ_wendigo_bind_the_warlord_commands` (line 3049) retain repeated blocks for AND semantics.

Unified branch-entry focuses such as `CBL_one_command`, `CBL_many_jaws`, `CBL_ritual_administration`, `CBL_continental_larder_doctrine`, `CBL_continents_as_supply_regions`, `CBL_integrate_the_warbands`, and `CBL_global_courier_network` intentionally use visible `available` gates with `has_completed_focus` checks instead of extra prerequisite edges. Their comments explain that the OR alternatives are kept in `available` to avoid crossing the three disposition columns. They are not dangling or free pre-reveal roots.

Mutual exclusions remain grouped symmetrically for the three disposition routes, three hierarchy routes, four unified Larder methods, three Warlord hierarchy routes, three Warlord Larder methods, and three Evolution II network choices. No Wendigo route is accidentally mutexed.

## Reveal and identity safety

The Unified tree country gate at lines 26-35 requires CBL, `cannibalism_unified_country`, `cannibalism_reveal_complete`, and excludes `cannibalism_wendigo_hannibal_country`. Its first focus repeats the same reveal gate in `allow_branch` and `available` at lines 52-63.

The Warlord tree country gate at lines 1529-1538 requires `is_cannibalism_warlord_country`, an active Warlord slot, opened Warlord decisions, and no release-pending flag, without naming the concealed leader.

The Wendigo tree country gate at lines 2957-2967 requires original tag ZZZ, `is_cannibalism_wendigo_hannibal_country`, `cannibalism_reveal_complete`, overlay availability, `ZZZ_hannibal_wendigo`, and no existing world end. Its root repeats the same post-reveal conditions at lines 2984-2998.

A current runtime-surface search returned zero `prison_host`, `Prison Host`, `origin_prison`, `warlord_prison_`, `lockhouse`, or `lock_house` identifiers across `common`, `events`, `history`, `interface`, `localisation`, and `gfx`. Legitimate `prisoner`, `prison`, and `prison/port cells` mechanics remain ordinary logistics or intelligence content rather than a retired fourth origin.

The exact Warlord focus title, description, and reward-tooltip values contain no Hannibal, Lecter, Wendigo, or Prison Host leak. The Unified and Wendigo names are intentionally post-reveal and are gated by their tree country conditions.

## Focus icon coverage

| Tree | Focus icon references | Unique base sprites | Shine sprites | Existing DDS files | Result |
| --- | ---: | ---: | ---: | ---: | --- |
| Unified CBL | 108 | 108 | 108 | 108 | Complete |
| Reusable Warlord | 68 | 68 | 68 | 68 | Complete |
| Wendigo overlay | 28 | 28 | 28 | 28 | Complete |
| Total | 204 | 204 | 204 | 204 | No missing, duplicate, or non-Event-014 focus icon mapping |

Every base icon has a matching `_shine` registration in `interface/014_cannibalism.gfx`, and every referenced texture path exists under `gfx/interface/goals/014_cannibalism/`. The source has no duplicate icon references. The GFX and localisation files were read-only inputs because they contain concurrent work from other agents and required no Event 014 focus correction.

## Localisation and reward mismatch list

No focus title, description, or custom reward-tooltip mismatch was found. A source-to-localisation scan found all 204 implicit title keys, all 204 `_desc` keys, and all 204 `custom_effect_tooltip` keys with non-empty values and no duplicate keys. `localisation/english/014_cannibalism_l_english.yml` has the required UTF-8 BOM.

Every focus calls one unique tree-specific helper in `completion_reward`, and all 204 helper identifiers resolve in `common/scripted_effects/014_cannibalism_effects.txt`. The helper naming matches the focus identifier for all three trees, so no reward is silently pointing at a neighbouring focus.

The special-unit progression remains coherent and paid. `CBL_map_the_origin_templates` at line 889 opens unified origin-specialist recruitment through `cannibalism_unlock_event014_unified_origin_specialists`. `CBL_raise_the_cannibal_legions` at line 913 opens paid Cannibal Legion recruitment through `cannibalism_unlock_event014_unified_legion`. `CBL_bone_guard_command` at line 949 opens paid Bone Guard recruitment, Bone Riders, and the Scavenged Elephant Column through `cannibalism_unlock_event014_unified_bone_guard`. Warlord equivalents are `cannibalism_warlord_train_the_origin_specialists` at line 2195, `cannibalism_warlord_form_the_feast_cohorts` at line 2176, and `cannibalism_warlord_raise_the_bone_guard` at line 2215. Wendigo Pack progression runs from `ZZZ_wendigo_drill_the_original_pack` at line 3204 through `ZZZ_wendigo_army_of_the_frozen_larder` at line 3280 and keeps paid capacity, support stages, and preserved-template contracts.

Targeted reward text agrees with these helper contracts. No focus directly grants free population, manpower, equipment, or units. The terminal descriptions at `CBL_final_global_mobilization`, `CBL_dismantle_the_ordinary_world`, and `ZZZ_wendigo_the_world_beneath_winter` explicitly preserve the existing paid/readiness or pulse-owned world-end boundaries.

## AI behavior gaps

All 204 focuses contain one `ai_will_do` block. Unified has 37 maximum, 32 urgent, 29 high, and 10 standard base priorities, with route/resource/terminal modifiers on all 108 focuses. Warlord has 9 maximum, 20 urgent, 30 high, and 9 standard base priorities, with modifiers on all 68 focuses. Wendigo has 3 maximum, 11 urgent, 13 high, and 1 standard base priorities, with route-aware modifiers on 26 of 28 focuses.

The two base-only Wendigo focuses are the structural transition nodes `ZZZ_wendigo_bind_the_two_hungers` at line 2978 and `ZZZ_wendigo_mark_the_irreversible_road` at line 3436. They are not route-choice starvation defects in the source review. The remaining Wendigo focuses use `ai_war_factor`, `ai_branch_factor`, `ai_countdown_factor`, `ai_low_authority_factor`, `ai_terminal_factor`, or `ai_low_network_factor` as appropriate.

No AI weight was changed. The custom `chaosx_ai_probability_auditor` is not present in the callable tool inventory, so a new auditor-routed scenario comparison could not be created in this bounded task. The previous Event 014 focus probability inspection artifact remains available in `event014_focus_final_audit_v4.md` and reported 204 candidates with zero unresolved source inputs, but it is not presented as a fresh custom-auditor balance certification. Because no AI patch was made, no before/after probability comparison is claimed.

## MCP inspection and render evidence

Workspace: `mod_chaos_redux_ea3b2d67c2c0`.

| Tree | `hoi4.focus_inspect` result | Layout evidence |
| --- | --- | --- |
| Unified | 108 focuses, 108 resolved titles, diagnostic count 0, validation `focus-diagnostics` passed. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78224453f8e94b32a4b6436a47307a7430f7261dc239fd298800fcc42aa6e659/b95b259c4fab1ac488575858b1860a912314ee2a4bb3fb368607d2c5a5cd3721/focus-inspect.17b65e78d15ff075.json` | Bounds x=8..44 and y=0..27, 103 connectors, 0 crossings, 0 node intersections, 0 long connectors, maximum horizontal span 8, maximum vertical span 3, and maximum Manhattan span 9. |
| Warlord | 68 focuses, 68 resolved titles, diagnostic count 0, validation `focus-diagnostics` passed. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cffd2706675214e69ace3091db7c9925d3e94097c2804d066598ce2abbd3e8ba/01a05ccad91d45e10ce9a9535df671ee058587c1137fdb14db6faa631bb859c2/focus-inspect.12c802fb5befdf46.json` | Bounds x=12..28 and y=0..25, 79 connectors, 0 crossings, 0 node intersections, 0 long connectors, maximum horizontal span 8, maximum vertical span 3, and maximum Manhattan span 10. |
| Wendigo | 28 focuses, 28 resolved titles, diagnostic count 0, validation `focus-diagnostics` passed. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c7304a06c2738756976f31a28377c47739977a30710d2849be5abf00ee3879c/879392e8115c01f84997330168e4b07e4d8be50ce47d7797816b719aea8069f1/focus-inspect.12c802fb5befdf46.json` | Bounds x=32..46 and y=0..10, 28 connectors, 0 crossings, 0 node intersections, 0 long connectors, maximum horizontal span 8, maximum vertical span 1, and maximum Manhattan span 9. |

The required `hoi4.focus_render` and `hoi4.focus_raster` calls both completed for all three trees. Raster PNG artifacts are:

- Unified: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b480972e006a20a5e28c8b7713bbb7aac76cfa03f2d76277f0fbcfefb37594af/d08ac669ca8f70823c2564ba5c1e63704ec0ff5ade723c5dac71bceb4707f84b/cannibalism_unified_focus_tree.focus.png` at 6640 by 3368 pixels.
- Warlord: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db189c17e054f1a25371794aa7aae7eb7b4c28f968d5f9f76fba2b2bc84d4ff6/92115a40b7f496fc7383c2ac1b6b318ca0aba9ae3f4d8cd117e0b6f419880ea9/cannibalism_warlord_focus_tree.focus.png` at 3120 by 3136 pixels.
- Wendigo: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f64cacab6386fd3f87a87209b3d5e16cc86955604b83cff34b99b64d1d2c654e/60d1c67724e686fc54e03d0f00b2e1f6a4e9e8c1a72240755472d1df5cf44c0f/cannibalism_wendigo_focus_tree.focus.png` at 2768 by 1396 pixels.

The companion render HTML, SVG, JSON, source-map, and plan artifacts were emitted for each tree under the same workspace. The first expanded Warlord render request exceeded the 180-second MCP response window, but its minimal render retry and raster request completed successfully. The only diagnostic repeated by the current MCP responses is the unrelated vanilla `continuous_restrict_freedom_desc` localisation warning from `game:common/continuous_focus/generic.txt`; no Event 014 focus diagnostic is attached to it.

## Missing or simplified content

No missing route, shallow fake branch, repeated generic reward, missing icon, missing localisation, pre-reveal identity leak, broken mutex, or missing special-unit unlock was confirmed. No fallback route, placeholder, new country, new formable chain, or unrelated file change was introduced.

The source has no `shortcut` blocks. This is recorded as a low-priority navigation follow-up rather than a confirmed layout defect because the current engine-backed inspections, renders, and rasters report clean geometry and the requested route surface remains fully reachable through the authored prerequisites and visible `available` gates. If focus navigation shortcuts are required for the final UX, they should be handled as a separate UI-scoped change with new localisation keys.

## High-priority fixes and blockers

| Priority | Finding | Disposition |
| --- | --- | --- |
| P0 | None in the Event 014 focus source. | No patch required. |
| P1 | Custom `chaosx_ai_probability_auditor` route is unavailable in this callable environment. | Keep quantitative route-dominance and starvation certification open for the parent or a runtime with that auditor. No AI weight was changed. |
| P2 | No registered `hoi4.focus_lint` or focus-compare route was exposed. | Current `focus_inspect` blocking validation and render/raster evidence are retained as the available MCP evidence. |
| P3 | No focus shortcuts are present. | Record as optional UX follow-up, not a gameplay or route blocker. |

## Changed files and validation

Changed files: `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_focus_completion_2026-08-26.md` only. No focus IDs, icon IDs, localisation keys, GFX definitions, AI weights, prerequisites, mutexes, or reward helpers changed.

Meaningful validation completed: three-tree source count and field audit, prerequisite and mutual-exclusion reference scan, reveal and retired-origin leak scan, focus-to-helper linkage scan, focus localisation/BOM/duplicate scan, icon-to-GFX-to-DDS scan, targeted special-unit reward trace, and current `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster` calls for all three tree IDs.

Skipped meaningful validation: no live Hearts of Iron IV launch per repository policy, no `hoi4.focus_rewrite` or post-change compare because no gameplay patch was made, no focus-specific lint route because it is not registered, and no custom probability-auditor comparison because that route is unavailable and no AI patch was applied.

No improvement-loop plan was written because the current route depth, reward variety, and cross-system hooks do not show a broad design gap. Parent review remains required before treating the Event 014 package as globally complete across its unrelated decisions, GUI, country, model, portrait, audio, and super-event surfaces.

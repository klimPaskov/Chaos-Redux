# Event 012 Africa Focus Final Handoff

Status: compact overlay and world-prerequisite audit complete for the Event 012 focus scope, with the continental MCP adapter timeout recorded for parent review.

Scope: `common/national_focus/012_africa_continental_focus_tree.txt` plus the six Event 012 external world files. The continental overlay coordinates were repaired without changing focus ids, route effects, prerequisites, mutual exclusions, rewards, AI weights, icons, or localisation. Five malformed external convergence gates remain repaired. Middle East required no source change because its convergence gate was already valid.

## Changed files

| File | Change |
| --- | --- |
| `common/national_focus/012_africa_continental_focus_tree.txt` | Restored the compact overlay base envelope, added conditional branch offsets for eight non-base overlay lanes, and retained the four opening-lane coordinate corrections. |
| `common/national_focus/012_africa_world_asia_focus.txt` | Replaced the nested `OR` wrapper at `africa_asia_food_river_and_monsoon_board` with one direct OR prerequisite block. |
| `common/national_focus/012_africa_world_europe_focus.txt` | Replaced the nested `OR` wrapper at `africa_europe_common_army_and_air_defence` with one direct OR prerequisite block. |
| `common/national_focus/012_africa_world_north_america_focus.txt` | Replaced the nested `OR` wrapper at `africa_north_america_resources_and_withdrawal_law` with one direct OR prerequisite block. |
| `common/national_focus/012_africa_world_oceania_focus.txt` | Replaced the nested `OR` wrapper at `africa_oceania_ocean_constitution_and_withdrawal_law` with one direct OR prerequisite block. |
| `common/national_focus/012_africa_world_south_america_focus.txt` | Replaced the nested `OR` wrapper at `africa_south_america_resource_and_debt_sovereignty_law` with one direct OR prerequisite block. |

`common/national_focus/012_africa_world_middle_east_focus.txt` was inspected and has no corresponding malformed gate, so it remains unchanged.

## Coordinate and route behavior before and after

The prior draft translated eight overlay families into independent x lanes extending to x = 176. That made the static graph wide and created long cross-tree connectors even though only one regional overlay is visible at runtime. The final source restores the authored six-focus template x coordinates `12, 8, 16, 8, 16, 12` for every regional family and adds a conditional `offset` block to the West Atlantic, Sahel-Lake Chad, Nile-Horn, Congo Basin, Great Lakes, Swahili-Indian Ocean, Southern Africa, and Madagascar-Islands families.

| Overlay predicate | Base x sequence | Conditional offset | Active x envelope | Active duplicate coordinates |
| --- | --- | ---: | --- | ---: |
| `africa_focus_uses_maghreb_sahara_overlay` | `12, 8, 16, 8, 16, 12` | `0` | `8..16` | `0` |
| `africa_focus_uses_west_atlantic_overlay` | `12, 8, 16, 8, 16, 12` | `1` | `9..17` | `0` |
| `africa_focus_uses_sahel_lake_chad_overlay` | `12, 8, 16, 8, 16, 12` | `2` | `10..18` | `0` |
| `africa_focus_uses_nile_horn_overlay` | `12, 8, 16, 8, 16, 12` | `3` | `11..19` | `0` |
| `africa_focus_uses_congo_basin_overlay` | `12, 8, 16, 8, 16, 12` | `4` | `12..20` | `0` |
| `africa_focus_uses_great_lakes_overlay` | `12, 8, 16, 8, 16, 12` | `5` | `13..21` | `0` |
| `africa_focus_uses_swahili_indian_ocean_overlay` | `12, 8, 16, 8, 16, 12` | `6` | `14..22` | `0` |
| `africa_focus_uses_southern_africa_overlay` | `12, 8, 16, 8, 16, 12` | `7` | `15..23` | `0` |
| `africa_focus_uses_madagascar_islands_overlay` | `12, 8, 16, 8, 16, 12` | `8` | `16..24` | `0` |

All nine predicates remain mutually exclusive through the existing `allow_branch` triggers. The offset trigger matches the corresponding `allow_branch` predicate on all 48 changed focuses. The existing `africa_refresh_continental_focus_tree_layout` helper continues to call `mark_focus_tree_layout_dirty` after compact-host promotion and the existing continental-tree load path marks the initial layout dirty.

The active overlay graph has 54 intra-overlay prerequisite edges, a maximum Manhattan edge length of 5, and no edge longer than 12. Static base-coordinate duplicates remain only between mutually exclusive route families, as in the authored vanilla-style branch pattern; every active overlay branch has six unique coordinates.

The four opening coordinate corrections are retained from the prior narrow repair:

| Focus id | Before | After |
| --- | --- | --- |
| `africa_repair_host_administration` | `x = 29, y = 1` | `x = 27, y = 1` |
| `africa_build_host_coalition` | `x = 35, y = 1` | `x = 43, y = 1` |
| `africa_prepare_host_security` | `x = 41, y = 1` | `x = 30, y = 1` |
| `africa_protect_first_partner` | `x = 40, y = 4` | `x = 43, y = 4` |

Their prerequisites, availability, rewards, and AI blocks are unchanged. The six grounded constitutional routes, hidden Covenant route, shared support lane, Charter League formation, and post-unification settlement remain behaviorally unchanged.

## Route coverage table

| Surface | Identifiers or source | Audit result |
| --- | --- | --- |
| Shared protection-first opening | `africa_identify_host_problem` through `africa_choose_constitutional_principle` | 16 focuses present and connected. |
| Regional overlays | Nine `africa_focus_uses_*_overlay` predicates | 9 families x 6 focuses = 54; all retain branch gates, distinct step variables, completion rewards, and AI blocks. |
| Full host signature | `africa_host_signature_confront_origin_crisis`, `africa_host_signature_use_origin_leverage`, `africa_host_signature_contain_origin_rival`, `africa_host_signature_prove_origin_mandate` | Four-focus full signature lane remains gated by `africa_focus_shows_full_host_signature`. |
| Compact host signature | `africa_compact_signature_secure_distinct_role`, `africa_compact_signature_prove_viable_host` | Two-focus compact lane remains gated by `africa_focus_shows_compact_host_signature`; the second focus records the first proof. |
| Federal route | `africa_federal_*` | 21 focuses, route-specific prerequisites, mutual exclusions, payoff helper, crisis handling, and AI. |
| Republic route | `africa_republic_*` | 21 focuses, route-specific prerequisites, mutual exclusions, payoff helper, crisis handling, and AI. |
| Crowns route | `africa_crowns_*` | 21 focuses, route-specific prerequisites, mutual exclusions, succession crisis, payoff helper, and AI. |
| People's Union route | `africa_union_*` | 21 focuses, route-specific prerequisites, mutual exclusions, payoff helper, crisis handling, and AI. |
| Military Command route | `africa_command_*` | 21 focuses, route-specific prerequisites, commander crisis, payoff helper, and AI. |
| Confederation route | `africa_confederation_*` | 21 focuses, route-specific prerequisites, free-rider crisis, payoff helper, and AI. |
| Covenant route | `africa_covenant_*` | 18 hidden/transformational focuses, route gate, covenant crises, payoff helper, and AI. |
| Shared support and post-unification | `africa_support_*`, `africa_charter_league_declared`, `africa_seat_the_first_member_council`, `africa_write_accession_law`, `africa_build_the_continental_secretariat`, `africa_fund_the_common_budget`, and final ratification focuses | 36 support focuses plus the formation/post-formation settlement remain connected. |
| External world packages | Asia 20, Europe 20, Middle East 20, North America 20, Oceania 20, South America 21 | Every tree has one static root, no unreachable focus, and no dangling prerequisite in the source graph. |

The payoff matrix `docs/specs/012_africa_specs/matrices/012_africa_focus_route_payoff_matrix.csv` contains 78 rows. Its audited route distribution is Shared opening 5, each of the six grounded routes 9, Covenant 9, and Shared support 10. The phase distribution is early 17, middle 40, late 10, capstone 7, hidden opening 2, and post-unification 2.

The host-country matrix contains 22 full rows and 29 compact rows. The existing scripted trigger has 22 full country tags and 30 compact accepted tags because the Ruanda-Urundi row is represented by two tags and three special signature-country flags cover Sao Tome, Seychelles, and Reunion. This is an existing alias representation, not a focus-tree change.

## Missing or simplified content

- No focus route, focus identifier, prerequisite, mutual exclusion, reward hook, decision hook, formable hook, crisis hook, or post-unification hook was removed or simplified.
- No new generic or copied focus content was added.
- No icon, portrait, asset, GUI, tag, ledger, or spreadsheet file was changed.
- The static source still reports duplicate base coordinates across mutually exclusive branches. This is intentional branch reuse; active branch coordinates are unique after conditional offsets.
- The MCP planner cannot represent the runtime branch predicate and therefore may report static fan/crossing diagnostics. The source graph and branch-offset audit are the authoritative evidence for the conditional overlay layout.

## Icon coverage table

| Surface | Result |
| --- | --- |
| Continental focus icons | All existing 276 focus icon references are retained; no icon id changed. |
| External world focus icons | All existing Asia/Europe/Middle East/North America/Oceania/South America icon references are retained; no icon id changed. |
| Asset and `.gfx` wiring | No asset or interface file was touched. Prior focus audits and the last valid continental MCP artifact reported resolved icon families. |

## Localisation and reward mismatch list

- Localisation keys were not changed. The existing focus ids and titles remain paired, and no new player-facing key was introduced.
- The prior focus audit recorded resolved titles for all continental nodes and no missing localisation diagnostic. The coordinate and prerequisite edits do not affect that result.
- Existing static repeated-reward diagnostics on the nine overlay milestone families remain helper-backed behavior, not new generic rewards. `africa_apply_overlay_focus_reward` receives the region-specific temporary step and calls the existing region/constitution payoff helpers.
- No reward or tooltip mismatch was introduced by this patch.

## AI behavior gaps

- Every touched focus retains its existing `ai_will_do` block. No AI weight or probability-bearing modifier changed.
- The existing route-aware overlay pressure modifiers and external world-package AI factors remain intact.
- No new probability audit was required for this patch because no weighted value changed. Parent review should route any later AI-factor edit through `chaosx_ai_probability_auditor` and the required probability compare.

## MCP inspect, render, and rewrite evidence

The last valid continental inspection is recorded in `docs/plans/012_africa_plans/subagent_handoffs/012_africa_focus_layout_repair_2026-08-06.md`: workspace `mod_chaos_redux_ea3b2d67c2c0`, revision `8f18248d78f6a40b02a171fbba295ede6524a45827eb62cf06b1640565ce34c3`, artifact `focus-inspect.8f18248d78f6a40b.json`, with 276 nodes, 348 connectors, and all focus titles resolved. Its render and scaled raster artifacts are linked from that handoff. That artifact predates this compact-offset source patch but covers the same route graph and icon/localisation surface.

Post-patch calls to `hoi4.focus_inspect` for the continental tree timed out twice at the MCP adapter boundary with `tool call failed ... timed out awaiting tools/call after 180s`. A post-patch `hoi4.focus_render` request also hit the code-mode host timeout/stale-generation condition. Per the task blocker rule, the last valid MCP artifact is retained and the source graph, branch-offset, and route checks above are recorded rather than treating source-only checks as new engine evidence.

The five repaired external trees have valid inspect/render evidence in `docs/plans/012_africa_plans/subagent_handoffs/012_africa_external_world_prerequisite_repair_2026-08-06.md`. Those artifacts report 20/20/20/20/21 nodes as applicable and no malformed or unreachable prerequisite diagnostic after the five direct prerequisite repairs. Middle East was included in the source graph audit and had no malformed convergence block.

`hoi4.focus_rewrite` was callable but rejected the authored patch attempt because it requires a complete schema-versioned plan containing `schemaVersion`, tree id/default, branch/lane groups, entry/shared focus ids, focus records, passthrough records, and provenance. I did not submit an empty or broad compact plan because that could replace the authored route layout. The source patch therefore remains narrow and reviewable; the exact rewrite validation blocker is recorded here.

## Meaningful validation

- Continental parser: 276 unique focus ids, 348 prerequisite edges, one root, zero unreachable focuses, and zero dangling prerequisite references.
- External parser: Asia 20, Europe 20, Middle East 20, North America 20, Oceania 20, and South America 21 unique focuses; each has one root, zero unreachable focuses, and zero dangling prerequisite references.
- Overlay branch audit: nine predicates x six focuses, 48 matching conditional offsets, six unique active coordinates per branch, active x envelope `8..24`, and maximum intra-overlay Manhattan edge length 5.
- External gate audit: no `prerequisite = { OR = {` remains in the six Event 012 world files; the five repaired ids resolve through direct OR blocks.
- Route census: six grounded routes at 21 focuses each, Covenant at 18, shared support at 36, and nine overlays at six focuses each.
- Matrix census: 78 payoff rows with the route and phase distribution recorded above.

Skipped meaningful validation: a fresh post-patch MCP continental inspect/render because the adapter timed out; standalone focus lint because no such MCP route is exposed; live HOI4/save validation because agents must not launch the game; probability compare because no AI weight changed.

## High-priority fixes and remaining risks

1. Parent should review the last valid continental MCP artifact against the compact-offset source patch once the adapter accepts a focus inspection again. The runtime branch refresh hook is present, but this handoff cannot claim new post-patch engine layout evidence.
2. The MCP planner may still report static connector-through-node and repeated-pattern diagnostics because it evaluates mutually exclusive branches together. Active branch metrics are bounded and unique, but the static diagnostic stream remains an adapter limitation.
3. The existing 22-full/29-compact matrix and the alias-expanded trigger representation should remain documented together. Do not remove the Ruanda-Urundi alias or special signature flags merely to force a raw tag count of 29.

No gameplay simplifications were made. Parent review and scoped commit integration remain required because the repository contains concurrent Event 012 work.

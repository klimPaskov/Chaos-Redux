# Event 006 focus layout repair v3 audit and blocker handoff

Date: 2026-07-25

Scope: bounded layout audit for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`.

## Result

No focus source patch is retained.

The restored baseline passes parsing and title, icon, and localisation resolution, but the MCP layout validator still reports 14 blocking connector diagnostics.

Three narrow coordinate candidates were tested and reverted because none reduced the blocking count and each created a new layout tradeoff.

No prerequisites, OR semantics, mutual exclusions, rewards, AI blocks, route locks, package gates, localisation, icons, decisions, events, or interface files were changed.

This is an audit/blocker handoff rather than a completion claim; resolving the remaining crossings needs a coupled planar reflow of several source lanes, not a safe one-node nudge.

## Files and identifiers

| Surface | Result |
| --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` | Restored unchanged after candidate tests. |
| `interface/006_independence_wave.gfx` and other interface files | Not edited. |
| Focus ids changed | None. |
| Localisation keys changed | None. |
| Icon ids changed | None. |
| Handoff file | `docs/plans/006_independence_wave_plans/subagent_handoffs/006_focus_layout_repair_v3_2026_07_25.md`. |

## Baseline MCP evidence

The final restored `hoi4.focus_inspect` result is status `ok`, revision `83e32e12014f7719d4a733858abbcf32c3f425382072fbb775f94867e945b842`, and layout hash `3e5996acbdbed97ab085d52cd058861f2fbd21acc896f859268b204a9c81a5a2`.

| Metric | Restored baseline |
| --- | ---: |
| Regular focus count | 176 |
| Continuous focus count | 14 |
| Connector count | 214 |
| Crossing count | 49 |
| Node intersection count | 18 |
| Long connector count | 26 |
| Total diagnostics | 148 |
| Blocking diagnostics | 14 |
| Bounds | x 1..97, y 0..19 |
| Same-row required spacing | 2 |
| Too-close pairs | 6 |
| Parser/unresolved focus errors | 0 |
| Unresolved icon or localisation errors | 0 |

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ee4a0c35297a96c804bd626c750d535b0c62991c517326405d99a877d7b99ff/1446796b510182eef353f57f08d1d277e8b7aeb8ec6abed6e3609fb6d5a96b7a/focus-inspect.83e32c12014f7719.json`.

The final restored `hoi4.focus_render` output is 17,200 by 2,440 pixels and uses the same layout hash.

Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a67ecb1df3a7a2585423e727346be07e8df26cdf887e350c1c34f73702d59a7f/0964d1188a620bf6e0cd63a79b3efb3fee6c91d05adfc7b9bb5caac3a8ef2c46/independence_wave_focus_tree.focus.html`.

Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d74054ceefae952e810f86c67444a78301b86cf14fd47387159136c514bfc1a/f610c411bee1db6ddeff156d0915bde2e8c127181ca385476c1b3957aa80fe34/independence_wave_focus_tree.focus.svg`.

Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe2c880743c2df60a053382268cc015db1647a056f11e83bae19c2bb0c6a7cce/485a9975171d70ee8060c8baa27fb35f6424e887c38949a4909b2f311199b340/independence_wave_focus_tree.focus.json`.

Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cf5eae494e7ec51138d3de0035184715c7318695043972133c2a9ba0d6b6862/905f72f647ba03ba564033ed3db9ca50ed0192ad990df5f7a24681cfe3b8558d/independence_wave_focus_tree.focus.source-map.json`.

Layout plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9822f2cf0d16f12f55e12f3bcd400211b47cf2b1729c818cc49b26f7ed2f0a68/66969b99ec13742127645f117213c2d4ff603caf88c61a39c761ad5dbe442c42/independence_wave_focus_tree.focus.plan.json`.

## Route coverage

| Route or lane | Source anchors | Coverage result |
| --- | --- | --- |
| Survival and state construction | Lines 59-275; `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` | Present with the intended state-building chain and no missing prerequisite identifiers found. |
| Economy and regional infrastructure | Lines 277-396; `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury` | Present; the economy chain is one of the layout collision clusters but its gameplay semantics were preserved. |
| Army, security, and military identity | Lines 398-665; `independence_wave_integrate_militia_commands` through the military capstones | Present with military identity and security branches; long/crossing connectors remain in the geometry. |
| Diplomacy, recognition, and patrons | Lines 667-811; `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service` | Present with the neutral/patron mutual exclusion and treaty-backed continuation intact. |
| Package-gated government settlement | Lines 813-1266; `independence_wave_prepare_first_assembly` plus package adapters | Present; comments and source include the distinct Saar municipal neutral commission route. |
| Former-host settlement | Lines 1269-1451; `independence_wave_define_former_host_policy` and four exclusive settlement branches | Present with exclusive living-host paths and collapsed-host ledger path intact. |
| Regional ambition and signature | Lines 1452-1524; `independence_wave_survey_regional_ambition` through `independence_wave_open_signature_extension` | Present with regional congress, integration authority, and signature extension anchors. |
| Independence network and league | Lines 1525-1708; `independence_wave_recognize_fellow_new_states` through five mutually exclusive proposals | Present; decision-owned votes and proclamation remain outside this layout-only scope. |
| Formable preparation and FORM-03 | Lines 1709-1905; `independence_wave_focus_discover_regional_identity` through the FORM-03 charter/industry branch | Present with the preparation chain and FORM-03 extension. |
| High-chaos sovereignty | Lines 1906-1965; `independence_wave_sponsor_further_ruptures` through `independence_wave_rewrite_charter_of_borders` | Present and gated from the regional ambition milestone as documented in source comments. |
| Package-owned branches | Lines 1966-2891; IW-001, IW-002, IW-004, IW-006, IW-008, IW-009, IW-010, IW-018, and IW-019 branches | Present; no package branch was removed or semantically altered. |
| Framework capstone | Lines 2892-2911; `independence_wave_secure_durable_sovereignty` | Present with treasury, defense institution, and permanent foreign service prerequisites. |
| Additive shared overlay and imported package focuses | Lines 2912 onward plus explicit imports at lines 40-56 | Present; imported IW-043, IW-058, IW-093, IW-098, COR, HBX, and HAW shared roots resolve in the MCP scan. |

## Blocking diagnostics and layout findings

The MCP validator reports 14 blocking diagnostics, comprising one crossing that is both avoidable and unsatisfied plus 13 additional unsatisfied crossing relations.

| Diagnostic count | Source lines | Connector relation | Crossing relation | Severity/result |
| ---: | --- | --- | --- | --- |
| 2 | 280-297 | `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_provinces_and_councils` | Crosses `independence_wave_inventory_the_state` -> `independence_wave_establish_emergency_revenue` | Blocking avoidable crossing and blocking unsatisfied crossing. |
| 3 | 319-336 | `independence_wave_complete_founding_settlement` -> `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states` | Each crosses `independence_wave_secure_food_and_fuel` -> `independence_wave_build_regional_transport_authority` | Three blocking unsatisfied crossings. |
| 3 | 442-461 | `independence_wave_complete_founding_settlement` -> the same three downstream roots | Each crosses `independence_wave_secure_national_depots` -> `independence_wave_recall_and_vet_officers` | Three blocking unsatisfied crossings. |
| 6 | 502-525 | `independence_wave_adopt_military_archetype_program` -> `independence_wave_adopt_border_defense`, `independence_wave_adopt_reclamation_doctrine`, `independence_wave_preserve_independent_command`, and `independence_wave_standardize_with_league` | Crosses `independence_wave_confirm_civilian_control` or `independence_wave_grant_military_autonomy` -> `independence_wave_found_professional_defense_institution`, plus the `independence_wave_build_professional_core` -> `independence_wave_found_professional_defense_institution` connector | Six blocking capstone fan-in crossings. |

The inspect result also reports nonblocking long-connector and through-node warnings, including `independence_wave_complete_founding_settlement` -> `independence_wave_map_internal_power_centers`, `independence_wave_inventory_the_state` -> `independence_wave_establish_emergency_revenue`, `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_militia_commands`, and the `independence_wave_complete_founding_settlement` -> `independence_wave_survey_regional_ambition` connectors through `independence_wave_activate_package_economic_program` and `independence_wave_adopt_military_archetype_program`.

## Narrow coordinate tests

All tests were applied only to the target source and reverted before the final inspect/render.

| Candidate | Metrics after temporary edit | Result |
| --- | --- | --- |
| Move `independence_wave_integrate_provinces_and_councils` x 24 -> 36 | 49 crossings, 18 node intersections, 29 long connectors, 151 diagnostics, 14 blockers | Reverted; added long connectors and unsatisfied layout noise without reducing blockers. |
| Move `independence_wave_adopt_border_defense` x 33 -> 37 and `independence_wave_adopt_reclamation_doctrine` x 35 -> 39 | 46 crossings, 24 node intersections, 26 long connectors, 148 diagnostics, 14 blockers | Reverted; aggregate crossings fell but node intersections rose and blocking count was unchanged. |
| Move `independence_wave_inventory_the_state` x 20 -> 28 | 54 crossings, 18 node intersections, 26 long connectors, 158 diagnostics, 14 blockers | Reverted; worsened crossings and diagnostics with no blocking improvement. |

Before and after route behavior are identical because no source change was retained.

## Icons, localisation, rewards, and AI

### Icon coverage

| Check | Result |
| --- | --- |
| Icon references in 189 focus/shared-focus blocks | 189 present. |
| Unique icon ids | 52. |
| Unique ids with base sprite | 52 of 52. |
| Unique ids with shine sprite | 52 of 52. |
| Missing icon diagnostics | 0. |
| Representative families | Founding, infrastructure, army integration, recognition, patron, former-host, regional formable, league, high-chaos, FORM-03, and package-specific `afx`, `ajx`, `arx`, `asx`, `bay`, and `rhi` families. |

### Localisation and reward mismatch list

No missing focus names or descriptions were found across the Event 006 focus localisation files for the 176 regular focus ids resolved by MCP.

All 189 focus/shared-focus blocks have `completion_reward`, and all 189 unique `custom_effect_tooltip` references resolve to localisation keys.

No missing icon/localisation diagnostics or obvious focus-name/reward-key mismatches were found in this bounded audit.

The audit did not rewrite player-facing text or perform a full prose balance pass because the requested surface is layout only.

### AI behavior gaps

All 189 focus/shared-focus blocks have `ai_will_do`, `available`, `completion_reward`, and `icon` fields, and the core focus weights use the shared `independence_wave_focus_ai` constants with route-aware modifiers.

Package-specific strategy files are present under `common/ai_strategy/`, including Brittany, IW-043/IW-058, IW-093/IW-098, Mediterranean, Pacific, Rhineland/Bavaria, rival bloc, Saar, Scotland/Wales, and Wallonia/Frisia.

No Event 006 entry was found under `common/ai_strategy_plans/` or `common/ai_focuses/`, so the core tree relies on per-focus weights rather than a dedicated core strategy plan.

This is a remaining AI risk, not a layout patch target; adding or redesigning strategy plans would exceed the bounded request.

## High-priority fix order for the parent

1. Reflow the coupled founding/economy/officer/regional-root cluster around `independence_wave_complete_founding_settlement`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, `independence_wave_secure_food_and_fuel`, `independence_wave_secure_national_depots`, `independence_wave_recall_and_vet_officers`, and the AJX/former-host/league roots in source lines 280-461.
2. Reflow the military capstone fan-in around `independence_wave_confirm_civilian_control`, `independence_wave_grant_military_autonomy`, `independence_wave_build_professional_core`, `independence_wave_found_professional_defense_institution`, and the four `independence_wave_adopt_*` military endpoints in source lines 502-525.
3. After blocking crossings are removed, shorten the nonblocking long connectors and eliminate the two through-node paths without changing prerequisites or route semantics.

A safe fix likely needs a coupled layout plan or a reviewed `hoi4.focus_rewrite` patch. The three tested one-node moves are not safe candidates.

## Validation and skipped checks

Meaningful validation completed: final `hoi4.focus_inspect` and `hoi4.focus_render`; source parser checks for 189 focus/shared-focus blocks and required fields; aggregate focus localisation coverage; aggregate custom tooltip coverage; and interface base/shine icon coverage.

The final MCP inspect and render still report 14 blocking diagnostics, so the result is intentionally handed off as unresolved geometry.

The additional pass attempted `hoi4.focus_rewrite` with `layoutMode = compact`, but its quality gate returned `FOCUS_COMPACT_QUALITY_BLOCKED` and applied no source rewrite; the manual candidates likewise failed to reduce blockers without introducing a different layout regression.

`hoi4.focus_raster` was not used because the rendered SVG/HTML and MCP diagnostics were sufficient for this source-layout audit.

The game was not launched, consistent with repository instructions; live runtime validation remains parent/user-owned.

## Simplifications, omissions, and blockers

No gameplay simplification, route omission, localisation fallback, icon fallback, AI placeholder, or interface change was introduced.

The remaining blocker is the 14-diagnostic planar layout cluster, which cannot be safely resolved by the tested local coordinate edits without a broader coupled reflow review.

No additional improvement plan was written because this handoff itself records the bounded blocker and the parent owns any broader layout redesign decision.

## Additional coupled reflow pass

The parent requested one further coordinated pass over the founding/economy/officer/regional roots and the military capstone fan-in.

The source was returned to the committed baseline after every trial, and the final baseline inspect confirms the original layout hash and 14 blocking diagnostics.

| Trial | Temporary geometry | MCP result | Decision |
| --- | --- | --- | --- |
| Root-only reflow | `independence_wave_ajx_appoint_neutral_commission_focus` 87 -> 30, `independence_wave_define_former_host_policy` 50 -> 34, and `independence_wave_recognize_fellow_new_states` 62 -> 36 | 84 crossings, 18 node intersections, 34 long connectors, 225 diagnostics, 14 blockers | Reverted; descendant connectors created a much denser crossing field. |
| Capstone compression | Compressed civilian/autonomy, arsenal, and border/reclamation pairs toward the military center while preserving all prerequisites | 57 crossings, 35 node intersections, 26 long connectors, 180 diagnostics, 14 blockers | Reverted; node intersections increased and blockers did not fall. |
| Capstone ordering variant | Reordered the same side branches to 40/42, 39/41, and 37/39 across rows 7-9 | 48 crossings, 21 node intersections, 26 long connectors, 148 diagnostics, 14 blockers | Reverted; one aggregate crossing fell but blocking count and diagnostic total were unchanged. |
| Central root/economy reflow | Moved the founding root to x24, economy lane to x22, and three regional roots to x26/30/34 | 86 crossings, 15 node intersections, 32 long connectors, 225 diagnostics, 14 blockers | Reverted; new crossings moved into the founding/economy parent fan-in. |
| Far-right economy lane | Moved the economy lane to x90 to clear the regional-root fan-out | 62 crossings, 36 node intersections, 26 long connectors, 210 diagnostics, 26 blockers, plus duplicate-coordinate/visible-overlap errors with RHI package focuses | Reverted immediately; introduced parser/layout errors and a higher blocker count. |
| Shifted lane group | Moved inventory/economy to x40, officer lane/capstone to x48, and regional roots to x30/34/38 | 137 crossings, 28 node intersections, 50 long connectors, 358 diagnostics, 14 blockers | Reverted; broad connector length and crossing regressions were unacceptable. |
| MCP compact rewrite | Existing tree with `layoutMode = compact` | `FOCUS_COMPACT_QUALITY_BLOCKED`; no files changed and no artifacts applied | Not retained; the quality gate rejected the automatic reflow. |

Final post-pass inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e40f19880aa4a7009a6d12927902ba7327c08d5f4396a716b3a8a0ea624031cc/d4c47dc200caa65ff5cfe55094bdc3b115a2f488248d82dcb5ce5c5e5962e407/focus-inspect.c4bfab849eef5d9e.json`.

The final post-pass revision is `c4bfab849eef5d9e045f18c4a6da5d9b42e7df7a995b5c54dca6923f4bbf44b8`, with layout hash `3e5996acbdbed97ab085d52cd058861f2fbd21acc896f859268b204a9c81a5a2`, 49 crossings, 18 node intersections, 26 long connectors, 148 diagnostics, and 14 blocking diagnostics.

No safe coupled reflow was found within the permitted source scope.

The remaining blocker is therefore explicit: the connector clusters are globally coupled to package-owned branches and the capstone fan-in, so local or compact coordinate rewrites either preserve the 14 blockers or produce materially worse crossings, overlaps, or duplicate coordinates.

The focus source remains unchanged relative to the prior handoff commit; only this handoff received the additional evidence.

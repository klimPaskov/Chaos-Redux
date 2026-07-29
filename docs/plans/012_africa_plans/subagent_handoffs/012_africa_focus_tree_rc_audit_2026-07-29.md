# Event 12 Africa focus-tree release-candidate audit

Date: 2026-07-29

Scope: the Event 12 continental, priority-member, and six dormant world-order focus trees, their loading helpers, focus-local AI, localisation, icon contracts, prerequisites, mutual exclusions, and reward helper references.

Status: audit handoff only. No gameplay, focus, localisation, or asset source was patched by this audit. The current world-order icon/GFX removal is an intentional parent release-candidate gate and is recorded as observed state, not as an audit edit.

## Files and references inspected

- common/national_focus/012_africa_continental_focus_tree.txt
- common/national_focus/012_africa_priority_member_focus.txt
- common/national_focus/012_africa_world_asia_focus.txt
- common/national_focus/012_africa_world_europe_focus.txt
- common/national_focus/012_africa_world_middle_east_focus.txt
- common/national_focus/012_africa_world_north_america_focus.txt
- common/national_focus/012_africa_world_oceania_focus.txt
- common/national_focus/012_africa_world_south_america_focus.txt
- common/scripted_effects/012_africa_effects.txt
- common/scripted_effects/012_africa_focus_route_effects.txt
- common/scripted_effects/012_africa_priority_member_effects.txt
- common/scripted_effects/012_africa_world_order_effects.txt
- common/scripted_triggers/012_africa_focus_route_triggers.txt
- common/scripted_triggers/012_africa_world_order_triggers.txt
- common/scripted_triggers/012_africa_ai_profile_triggers.txt
- common/ai_strategy_plans/012_africa_focus_plans.txt
- interface/012_africa.gfx
- interface/012_africa_priority_member_assets.gfx
- interface/012_africa_world_order.gfx (currently absent from the worktree by intentional RC gating)
- localisation/english/012_africa_focus_l_english.yml
- localisation/english/012_africa_priority_member_focus_l_english.yml
- localisation/english/012_africa_world_order_l_english.yml
- docs/events/012_africa/world_order.md

## Route coverage table

The current source contains 405 unique focus blocks: 276 continental, 8 priority-member, and 121 dormant world-order package focuses.

| Surface | Coverage | Source identifiers | Result |
|---|---:|---|---|
| Shared continental opening | 16 | africa_identify_host_problem through africa_choose_constitutional_principle in common/national_focus/012_africa_continental_focus_tree.txt:43-306 | Present and ordered before constitutional selection. |
| Regional overlays | 9 groups x 6 focuses = 54 | africa_maghreb_*, africa_west_atlantic_*, africa_sahel_*, africa_nile_*, africa_congo_*, africa_great_lakes_*, africa_swahili_*, africa_southern_*, and africa_madagascar_* in common/national_focus/012_africa_continental_focus_tree.txt:322-1247 | Every group has six focuses and an allow_branch predicate tied to its overlay trigger. |
| Host signatures | 6 | Four africa_host_signature_* IDs and two africa_compact_signature_* IDs in common/national_focus/012_africa_continental_focus_tree.txt:1269-1363 | Full and compact signatures are both present and gated. |
| Federal route | 21 | africa_federal_representation_before_merger through africa_federal_enforceable_limits | Full route depth; 16 body nodes use flat normal AI. |
| Republic route | 21 | africa_republic_civic_status_and_accession through africa_republic_accepted_beyond_capital | Full route depth; 16 body nodes use flat normal AI. |
| Council of Crowns route | 21 | africa_crowns_recognise_living_crowns through africa_crowns_bound_by_charter | Full route depth; 16 body nodes use flat normal AI. |
| People’s Union route | 21 | africa_union_coalition_of_revolution through africa_union_through_social_institutions | Full route depth; 16 body nodes use flat normal AI. |
| Continental Command route | 21 | africa_command_define_the_mandate through africa_command_of_africa | Full route depth; 16 body nodes use flat normal AI. |
| Continental Confederation route | 21 | africa_confederation_reserve_sovereignty through africa_confederation_in_concert | Full route depth; 15 body nodes use flat normal AI. |
| Hidden Covenant route | 18 | africa_covenant_recognise_the_impossible through africa_covenant_include_the_impossible | Hidden route depth is present; 12 body nodes use flat normal AI. |
| Shared support lanes | 36 | africa_support_* in common/national_focus/012_africa_continental_focus_tree.txt:5664-6612 | All support lanes are present and call Event 12 support reward helpers. |
| Formation and post-formation | 20 | africa_charter_league_declared through africa_one_continent_many_peoples | All final-band focuses are present and call formation/final helpers. |
| Priority-member overlay | 8 | africa_priority_define_compact_country, africa_priority_ratify_political_settlement, africa_priority_build_distinct_institution, africa_priority_secure_economic_function, africa_priority_negotiate_league_role, africa_priority_field_national_force, africa_priority_resolve_overlap_question, africa_priority_write_post_settlement_programme | Non-linear eight-focus package is complete, localised, iconed, and helper-wired. |
| Asia package | 20 | common/national_focus/012_africa_world_asia_focus.txt | Dormant shell parses; all 20 nodes currently have no icon field. |
| Europe package | 20 | common/national_focus/012_africa_world_europe_focus.txt | Dormant shell retained; all 20 nodes currently have no icon field. |
| Middle East package | 20 | common/national_focus/012_africa_world_middle_east_focus.txt | Dormant shell retained; all 20 nodes currently have no icon field. |
| North America package | 20 | common/national_focus/012_africa_world_north_america_focus.txt | Dormant shell retained; all 20 nodes currently have no icon field. |
| Oceania package | 20 | common/national_focus/012_africa_world_oceania_focus.txt | Dormant shell retained; all 20 nodes currently have no icon field. |
| South America package | 21 | common/national_focus/012_africa_world_south_america_focus.txt | Dormant shell retained; all 21 nodes currently have no icon field. |

Static reference checks found zero duplicate focus IDs, zero dangling focus or relative_position_id references, and 232 directional mutual-exclusion references forming reciprocal pairs with no asymmetric edge.

## Dormant world-order disposition and load safety

The current RC intentionally retains all six world-order focus files and their load_focus_tree branches while removing the 121 focus icon lines and the tracked interface/012_africa_world_order.gfx file. No generic or vanilla art fallback is used.

hoi4.focus_inspect parsed africa_asia_world_focus_tree with focusCount = 20 and status = ok; its Event 12 iconless nodes produce FOCUS_ICON_MISSING design warnings, not parser or load blockers. The same structural pattern is used by the other five dormant package files.

The package install path is gated by has_country_flag = africa_world_package_implementation_ready in common/decisions/012_africa_decisions.txt:1686 and common/scripted_triggers/012_africa_ai_profile_triggers.txt:782. No current Event 12 source sets that flag; the only references are six readiness checks. docs/events/012_africa/world_order.md:28 identifies it as an external implementation gate.

africa_world_install_current_package in common/scripted_effects/012_africa_world_order_effects.txt:465-541 now checks the readiness flag itself before any regional load_focus_tree branch. Its only six load_focus_tree references are in that gated helper. Retaining the dormant files and loaders preserves the reserved focus IDs, prerequisites, rewards, and future asset contract without exposing an iconless package in normal play.

The latest runtime change removes the old candidate-registration setters, adds the same readiness check to the candidate target selector, and exposes africa_scramble_close_continental_docket through common/decisions/012_africa_decisions.txt:1604-1611. The close-docket trigger/effect pair in common/scripted_triggers/012_africa_world_order_triggers.txt:235-251 and common/scripted_effects/012_africa_world_order_effects.txt:442-460 settles the Africa-only Scramble response when no ready package exists and clears the open world-order flag. This keeps the dormant package trees out of normal runtime while preserving nominated candidates for a future externally approved asset tranche.

Safest disposition: keep the dormant definitions and guarded loaders, keep the readiness flag false until the complete package art contract is delivered, and restore the exact icon/GFX/DDS/shine set atomically before any future package sets the flag. Removing the files and all loaders would discard already audited route logic and is unnecessary for parser safety.

## Missing or simplified content

- The six world-order packages are intentionally dormant and have no focus icons in the current RC. The future contract is 121 explicit focus sprites, 121 base DDS files, and 121 _shine sprite definitions; none should be replaced with generic art.
- interface/012_africa_world_order.gfx is currently deleted in the shared worktree, and gfx/interface/goals/012_africa/world_order/ is absent. These are intentional asset-gate blockers, not missing gameplay branches.
- The continental MCP layout validator reports 570 blocking diagnostics because the nine mutually exclusive overlay templates reuse authored coordinates. The same inspect reports 1,028 node intersections, 448 connector crossings, 55 same-row spacing violations, and 37 long connectors. These are renderer false positives unless branch exclusivity is proven; no coordinate rewrite was attempted.
- The priority-member inspect reports three long-connector warnings for africa_priority_define_compact_country to africa_priority_ratify_political_settlement, africa_priority_define_compact_country to africa_priority_secure_economic_function, and africa_priority_field_national_force to africa_priority_write_post_settlement_programme. No node intersections or focus-specific missing-art errors were found.
- The MCP inspect also reports 14 missing generic continuous-focus sprites and one generic continuous-focus description. Those diagnostics come from common/continuous_focus/generic.txt and are outside Event 12 focus scope.
- No route family, country identity, formable chain, or broad focus redesign was attempted.

## Icon coverage table

| Focus surface | Focus icon refs in current source | Base / shine definitions | Binary status | Disposition |
|---|---:|---:|---|---|
| Continental family | 13 unique family IDs reused across 276 focuses | 13/13 base and 13/13 shine in interface/012_africa.gfx | 13 DDS files in gfx/interface/goals/012_africa/ | Ready for the loaded continental tree. |
| Priority member | 8 unique IDs | 8/8 base and 8/8 shine in interface/012_africa_priority_member_assets.gfx | 8 DDS files in gfx/interface/goals/012_africa/priority_members/ | Ready for the priority overlay. |
| World-order packages | 0 current refs because all 121 icon lines are intentionally removed | Dormant future contract: 121 base and 121 shine in the absent interface/012_africa_world_order.gfx | 0/121 DDS files in absent gfx/interface/goals/012_africa/world_order/ | Keep dormant and gated; never add a fallback icon. |
| All Event 12 focus nodes | 21 current unique icon IDs across active trees | 21/21 base and 21/21 shine | 21 active DDS files | Current active trees are fully iconed; dormant world shells are intentionally iconless. |

## Localisation and reward mismatch list

All 405 focus IDs have title and _desc keys in the Event 12 localisation files. The eight tree title/description pairs are present for africa_continental_focus_tree, africa_priority_member_focus_tree, and all six world package tree IDs.

Every focus block has a cost, completion reward, and AI block. The 61 custom africa_* = yes/no helper tokens used by Event 12 focus files resolve to definitions in the Event 12 scripted effects/triggers. The 14 explicit Event 12 idea add/remove IDs resolve to common/ideas definitions.

No direct add_core, annex_country, transfer_state, create_country, join_faction, or set_relation effect appears in the owned focus files. Route and relationship outcomes dispatch through existing scripted reward helpers, so no static focus-name/reward mismatch was found.

One documentation wording risk remains: docs/events/012_africa/world_order.md correctly describes the readiness flag as an external gate, but its later package section describes the registry as implementation-ready because the architectures exist. That wording should be clarified if the dormant asset gate remains in the release candidate.

## AI behaviour gaps

common/ai_strategy_plans/012_africa_focus_plans.txt:26-489 has route-aware factors for the six visible constitutional routes, Covenant, support, crises, and formation. It does not have explicit overlay, world-package, priority-member, or host-playbook focus-factor sections.

The continental focus files contain 107 exact flat route-body blocks of ai_will_do = { factor = @africa_ai_normal }. These are design simplifications, not parser failures; they omit live route, phase, crisis, proof, relationship, and feasibility factors.

Asia, Europe, and Middle East use fixed @world_package_ai_* factors on all nodes, while North America has 11/20 fixed nodes, Oceania 10/20, and South America 11/21. The remaining nodes in those latter three files add package-mechanic modifiers, but no file has an explicit strategy-plan matrix for phase, target, or external-context selection. Because the package trees are dormant, this is not a current runtime failure, but it remains an AI-depth gap before the readiness flag is ever enabled.

Priority-member AI is present with two urgent, three high, and three normal factors in common/national_focus/012_africa_priority_member_focus.txt; no missing AI block was found.

Runtime AI probability sweeps were not run in this bounded audit. Parent validation should cover all nine overlays, six visible routes, Covenant reveal and revolt, compact eligibility, package readiness, host succession, and post-formation actions.

## High-priority fixes first

1. Keep africa_world_package_implementation_ready false until the 121 explicit world focus icons, GFX definitions, base DDS files, and _shine definitions are restored as one reviewed asset package.
2. Preserve the six dormant focus files and guarded load_focus_tree branches; do not delete their IDs or substitute fallback art. Keep the new readiness check in africa_world_install_current_package and the close-docket path intact.
3. Obtain branch-aware runtime layout proof for the nine overlay templates and refresh layout after overlay selection, Covenant reveal, compact promotion, formation, and host succession. Do not use hoi4.focus_rewrite for this authored coordinate contract.
4. Before enabling world packages, decide whether to deepen static continental/world AI factors and extend the AI strategy plan for overlays, priority members, world packages, and host playbooks.
5. Treat the 14 generic continuous-focus icon errors as a separate global asset issue unless the parent expands Event 12 scope.

## Patch details

Changed gameplay files: none.

Changed focus IDs: none.

Changed icon IDs or localisation keys: none.

Changed files from this audit: this handoff only.

## Validation evidence

- Current hoi4.focus_inspect for the continental tree returned FOCUS_INSPECTED, status = ok, focusCount = 276, resolvedTitleCount = 276, and 570 blocking layout diagnostics caused by static overlay coordinate reuse. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b6ee3bfe2054ed88ac0a29ce4e90d75298867d7194a776519db209f12370d7e/7c9c69fa97dfca049533e30a4ecf75f5999d610f7b42c1e7b673a63e6f2a391c/focus-inspect.a729d2214d026226.json.
- Current hoi4.focus_inspect for the priority tree returned FOCUS_INSPECTED, status = ok, focusCount = 8, no Event 12 icon or localisation errors, and three layout warnings. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e81a29a569f503bb1f431d8b78565e834c6db82aaa05f72cc572aced41234f4/46863c68c2d99e723f0bd606d7eefc9fd2306e809c3bdfbdc5de54872b3c7aa7/focus-inspect.bb915975fafa8a89.json.
- Current hoi4.focus_inspect for Asia returned FOCUS_INSPECTED, status = ok, focusCount = 20, and the Event 12 iconless nodes as warnings. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3970686b31ac78f543d18aac61c703733799e7684cc39de7a3510624ceb3f1d9/13331563f9adcc84f18a13ccd2fb9ae2220e8420fbab2569bcdc04027bd3e35a/focus-inspect.511347e63be67a88.json.
- Prior continental hoi4.focus_render produced deterministic HTML/SVG/JSON artifacts with the same layout hash and retained source links. HTML artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d0c2e6e380464f818f4091f6ef405bd257ae60b1b56d17a7db4ea8f2a8632d90/14d98e67d46fc8d72db4c94191ceeef4b2ae9226245b969c35b9e984a88ea66d/africa_continental_focus_tree.focus.html.
- Read-only structural checks found 405 unique IDs, no dangling focus references, no asymmetric mutual exclusions, all 405 title/description pairs, all focus costs/rewards/AI blocks, no missing Event 12 helper definitions, and no missing Event 12 idea definitions.

Skipped meaningful validation:

- No in-game launch or live save test was run because the parent owns runtime acceptance and agents must not launch Hearts of Iron IV.
- No weighted AI probability sweep was run because the dormant package gate and parent-owned runtime scenarios are prerequisites.
- No hoi4.focus_raster pass was run because no focus icon binaries were changed by this audit and the dormant world art package is intentionally absent.
- No hoi4.focus_rewrite or coordinate patch was run because static overlay coordinate reuse is intentional and branch-unaware renderer diagnostics do not justify changing authored layout.

## Remaining route risks

- common/scripted_effects/012_africa_effects.txt:1365-1386 and common/scripted_effects/012_africa_focus_route_effects.txt:11-32 both ensure the continental tree is loaded with keep_completed = no; parent runtime proof should confirm no duplicate loader call creates unintended progress loss.
- common/scripted_effects/012_africa_priority_member_effects.txt:258-290 intentionally skips replacement for countries with a meaningful non-generic tree; parent should verify each Event 006 niche carrier enters the expected branch.
- common/scripted_effects/012_africa_world_order_effects.txt:465-541 uses keep_completed = no for world package installation. It is currently unreachable through normal actions while the implementation-ready flag remains false, but future asset activation must test progress replacement and layout refresh.
- The static renderer cannot prove that allow_branch = { africa_focus_uses_*_overlay = yes } predicates are mutually exclusive at runtime. A branch overlap would make the authored coordinate reuse unsafe.
- Generic continuous-focus icon diagnostics remain unrelated but make MCP validation report false for every inspected national tree.

No simplification was silently introduced by this audit. The world-order iconless dormant disposition is explicit and is safe only while the implementation-ready gate remains false.

# Event 12 Africa focus-tree audit and bounded localisation patch

Date: 2026-07-24

Scope: the Event 12 continental tree, priority-member tree, six world-order focus files, focus localisation, focus icons, and focus-local AI references.

This is an audit handoff, not a completion claim. The route skeleton and static references are broad and internally connected, but world-order focus art, branch-aware layout proof, and route-aware AI depth remain open.

## Files inspected

- `common/national_focus/012_africa_continental_focus_tree.txt`
- `common/national_focus/012_africa_priority_member_focus.txt`
- `common/national_focus/012_africa_world_asia_focus.txt`
- `common/national_focus/012_africa_world_europe_focus.txt`
- `common/national_focus/012_africa_world_middle_east_focus.txt`
- `common/national_focus/012_africa_world_north_america_focus.txt`
- `common/national_focus/012_africa_world_oceania_focus.txt`
- `common/national_focus/012_africa_world_south_america_focus.txt`
- `common/ai_strategy_plans/012_africa_focus_plans.txt`
- `interface/012_africa.gfx`
- `interface/012_africa_priority_member_assets.gfx`
- `interface/012_africa_world_order.gfx`
- `localisation/english/012_africa_focus_l_english.yml`
- `localisation/english/012_africa_priority_member_focus_l_english.yml`
- `localisation/english/012_africa_world_order_l_english.yml`
- `docs/plans/012_africa_plans/012_africa_focus_architecture_handoff.md`

## Route coverage table

The current source contains 405 focus blocks: 276 continental, 8 priority-member, and 121 world-order package focuses. Inline one-line world focuses are included in this count.

| Surface | Current coverage | Evidence | Audit result |
|---|---:|---|---|
| Shared opening | 16 | `common/national_focus/012_africa_continental_focus_tree.txt:43-306` | All opening IDs are present; protection and first proof precede constitutional choice. |
| Regional overlays | 9 overlays x 6 focuses | `common/national_focus/012_africa_continental_focus_tree.txt:329-1261`; `allow_branch` uses `africa_focus_uses_maghreb_sahara_overlay`, `africa_focus_uses_west_atlantic_overlay`, `africa_focus_uses_sahel_lake_chad_overlay`, `africa_focus_uses_nile_horn_overlay`, `africa_focus_uses_congo_basin_overlay`, `africa_focus_uses_great_lakes_overlay`, `africa_focus_uses_swahili_indian_ocean_overlay`, `africa_focus_uses_southern_africa_overlay`, and `africa_focus_uses_madagascar_islands_overlay` | Every overlay has six gated focuses. Static coordinate reuse is intentional but not branch-aware to the MCP renderer. |
| Host signature | 4 full + 2 compact slots | `common/national_focus/012_africa_continental_focus_tree.txt:1269-1363` | All six dynamic signature slots exist and are gated by full/compact predicates. |
| Federal route | 21 | `africa_federal_representation_before_merger` at line 1383 through `africa_federal_enforceable_limits` at line 1976 | Full route depth is present; 16 body nodes use a flat normal AI factor. |
| Republic route | 21 | `africa_republic_civic_status_and_accession` at line 2004 through `africa_republic_submit_host_to_common_law` at line 2569 | Full route depth is present; 16 body nodes use a flat normal AI factor. |
| Crowns route | 21 | `africa_crowns_recognise_living_crowns` at line 2627 through `africa_crowns_bound_by_charter` at line 3213 | Full route depth is present; 16 body nodes use a flat normal AI factor. |
| People's Union route | 21 | `africa_union_coalition_of_revolution` at line 3244 through `africa_union_through_social_institutions` at line 3837 | Full route depth is present; 16 body nodes use a flat normal AI factor. |
| Command route | 21 | `africa_command_define_the_mandate` at line 3868 through `africa_command_limit_host_general_staff` at line 4443 | Full route depth is present; 16 body nodes use a flat normal AI factor. |
| Confederation route | 21 | `africa_confederation_reserve_sovereignty` at line 4504 through `africa_confederation_audit_host_secretariat` at line 5082 | Full route depth is present; 15 body nodes use a flat normal AI factor. |
| Hidden Covenant | 18 | `africa_covenant_recognise_the_impossible` at line 5142 through `africa_covenant_include_the_impossible` at line 5632 | Hidden route depth is present; 12 body nodes use a flat normal AI factor. |
| Shared support | 36 | `common/national_focus/012_africa_continental_focus_tree.txt:5664-6612` | All 36 support IDs exist and route through the support reward helper. |
| Formation and post-formation | 20 | `africa_charter_league_declared` at line 6642 through `africa_one_continent_many_peoples` at line 7109 | All 20 final-band IDs exist and use the final-focus helper family. |
| Payoff anchors | 78/78 | Rows 1-78 in `docs/plans/012_africa_plans/012_africa_focus_architecture_handoff.md:152-269` | Every accepted anchor resolves to a focus ID; no missing or duplicate anchors were found. |
| World-order packages | 20 Asia, 20 Europe, 20 Middle East, 20 North America, 20 Oceania, 21 South America | Six `common/national_focus/012_africa_world_*_focus.txt` files | All package focuses have prerequisites, rewards, AI blocks, and localisation, but most AI blocks are static package weights and their goal art is not delivered. |

## Missing or simplified content

- World-order goal art is unresolved. `interface/012_africa_world_order.gfx:5-161` defines 121 focus sprite names for the `GFX_goal_012_africa_continent_sponsorship_*`, `GFX_goal_012_africa_continent_union_*`, and `GFX_goal_012_africa_continental_representation_*` families, but `gfx/interface/goals/012_africa/world_order/` does not exist and all 121 referenced DDS files are absent. No generic or vanilla fallback was introduced.
- The same 121 world-order focus sprites have no `_shine` definitions. The 13 continental family sprites in `interface/012_africa.gfx` and the 8 priority-member sprites in `interface/012_africa_priority_member_assets.gfx` do have base and shine names.
- The MCP layout validator cannot prove mutually exclusive overlay visibility. It reports the nine static overlay templates as simultaneous duplicate coordinates even though each focus has a mutually exclusive `allow_branch` predicate. This produces 570 blocking diagnostics in the current inspect, including 1,028 node intersections, 448 connector crossings, 55 same-row spacing violations, and 37 long connectors.
- Continental AI remains simplified relative to the architecture contract. 107 route-body focuses use exactly `ai_will_do = { factor = @africa_ai_normal }` with no live route, phase, crisis, feasibility, or relationship modifier. The affected bands are federal lines 1425-1946, republic lines 2046-2567, crowns lines 2662-3184, union lines 3286-3808, command lines 3910-4441, confederation lines 4546-5080, and Covenant lines 5170-5601.
- World-order AI is also mostly static. Asia, Europe, and Middle East each have 20/20 focuses with a sole `@world_package_ai_*` factor; North America has 11/20, Oceania 10/20, and South America 11/21 of that static form. The only live modifiers are concentrated in the latter three files, and no world-order plan or overlay/playbook matrix appears in `common/ai_strategy_plans/012_africa_focus_plans.txt:4-489`.
- No broad route redesign was attempted. The existing route depth, helper calls, and branch gates were preserved, and the unresolved AI and art gaps are left for the parent implementation/asset owners.

## Icon coverage table

| Focus surface | Unique focus icon refs | Base sprite definitions | Shine sprite definitions | Binary status |
|---|---:|---:|---:|---|
| Continental family | 13 | 13/13 in `interface/012_africa.gfx` | 13/13 | DDS family exists under `gfx/interface/goals/012_africa/`. |
| Priority member | 8 | 8/8 in `interface/012_africa_priority_member_assets.gfx` | 8/8 | Eight priority-member DDS files exist under `gfx/interface/goals/012_africa/priority_members/`. |
| World-order packages | 121 | 121/121 in `interface/012_africa_world_order.gfx` | 0/121 | All 121 expected world-order goal DDS files are missing; the path is absent. |
| All Event 12 focus refs | 142 | 142/142 | 21/142 | The 121 missing shine definitions are an asset-package blocker, not a reason to redirect icons. |

## Localisation and reward mismatch list

- Before this patch, seven non-continental tree IDs lacked a complete tree title/description pair. The continental tree already had a pair.
- Patched keys are `africa_priority_member_focus_tree` and `africa_priority_member_focus_tree_desc` in `localisation/english/012_africa_priority_member_focus_l_english.yml:3-4`, plus `africa_middle_east_world_focus_tree`, `africa_middle_east_world_focus_tree_desc`, `africa_europe_world_focus_tree`, `africa_europe_world_focus_tree_desc`, `africa_asia_world_focus_tree`, `africa_asia_world_focus_tree_desc`, `africa_north_america_world_focus_tree_desc`, `africa_south_america_world_focus_tree_desc`, and `africa_oceania_world_focus_tree_desc` in `localisation/english/012_africa_world_order_l_english.yml:223,347-348,390-391,434,478,523`.
- All 405 focus IDs now have title and `_desc` localisation keys across the Event 12 localisation files.
- Every focus block has an icon, AI block, and completion reward. Static reference checks found no dangling prerequisites, relative positions, or mutual exclusions, and all 232 mutual-exclusion relations are symmetric.
- No direct `add_core`, `annex_country`, `transfer_state`, `create_country`, `join_faction`, or `set_relation` effect appears in the owned focus files. Route and relationship outcomes continue to dispatch through the existing scripted reward helpers, so no focus-name/reward mismatch was found in this static pass.

## AI behaviour gaps

The architecture requires phase-aware and route-aware AI, invalid-route factor zero, proof-failure recovery priority, crisis decision pairing, live Covenant pressure, and relationship-state-driven post-formation selection (`docs/plans/012_africa_plans/012_africa_focus_architecture_handoff.md:660-686`). The focus-local files satisfy the presence of AI blocks and route opener gates, but the following remain open:

- 107 continental route-body nodes are flat normal factors as listed above.
- Route plans in `common/ai_strategy_plans/012_africa_focus_plans.txt:26-489` cover constitutional routes, support, crisis, and formation factors, but there are no explicit overlay, world-order package, or 51-playbook focus-factor sections.
- World-order packages use static package factors for 92 of 121 focuses and lack a dedicated plan file for package feasibility, recognition pressure, treaty posture, or external-war context.
- Runtime AI scenario sweeps were not run in this subagent scope. Parent validation should exercise all nine overlays, six grounded routes, Covenant reveal/commitment/revolt, proof success and seven failures, compact eligibility, route crises 093-099, postwar action 100, action 101 recovery, and successor transfer.

## High-priority fixes first

1. Produce and wire the 121 world-order goal DDS files and their `_shine` sprite definitions. Preserve the explicit asset names in `interface/012_africa_world_order.gfx:5-161`; do not substitute generic textures.
2. Replace the 107 flat continental AI factors with route/phase/live-feasibility modifiers and extend `common/ai_strategy_plans/012_africa_focus_plans.txt` for overlays, world packages, and host playbook context.
3. Add branch-aware layout validation or per-overlay MCP renders. The source coordinate reuse is permitted only when the nine `africa_focus_uses_*_overlay` predicates are proven mutually exclusive at runtime.
4. After art and AI work, rerun `hoi4.focus_inspect`, `hoi4.focus_render`, and a live campaign acceptance matrix for loader, host succession, route commit, relationship transitions, and post-formation cleanup.

## Patch details and route behaviour

Changed files:

- `localisation/english/012_africa_priority_member_focus_l_english.yml`
- `localisation/english/012_africa_world_order_l_english.yml`
- This handoff file.

Changed focus IDs: none.

Changed icon IDs: none.

Before: all focus prerequisites, `allow_branch` predicates, mutual exclusions, completion rewards, and route helper calls were unchanged, but seven non-continental tree surfaces could display without a complete title/description pair.

After: those seven tree surfaces have direct public titles and descriptions, while route behaviour is unchanged. All 405 focus title/description pairs resolve, and no gameplay fallback was added.

## Validation evidence

- `hoi4_focus_inspect` returned `FOCUS_INSPECTED` with status `ok`, revision `0085b82d4c48f2003d67d0f9d6581e8f9c06ff461383b96355c6750936d2a874`, continental `focusCount = 276`, and validation `passed = false` only because of 570 layout diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c39526872381a5ec4012b3e0c64dd993c03ddcf3778ae39c3fac2f59eb3bd232/6e1603f81f4ab2952ee25d1a351bbb1a6ca3903b0cb814f31928a21d10b05b87/focus-inspect.0085b82d4c48f200.json`.
- `hoi4_focus_render` returned `FOCUS_RENDERED` with a deterministic HTML/SVG/JSON render and the same layout hash. HTML artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/98aa969f641a742b254272a5a9adde1bf3da9a7dbe69176511801c9edb426abe/42d6e59c21801f36939e17c906a9608dbc2c2574e3e5cb3fb29774f33e600502/africa_continental_focus_tree.focus.html`.
- Read-only structural audit found 405 focus blocks, zero duplicate IDs, zero dangling focus references, zero missing required focus fields, 78/78 architecture payoff anchors, 9 overlay groups of six, 232 symmetric mutual-exclusion relations, and zero focus title/description gaps.
- Both edited localisation files retain UTF-8 BOM bytes.

Skipped meaningful validation:

- No in-game or weighted AI campaign simulation was run because this subagent owns static focus surfaces and the parent owns runtime acceptance.
- No `hoi4.focus_raster` pass was run because no focus icon binaries changed and the world-order goal package is absent.
- No `hoi4.focus_rewrite` or coordinate patch was attempted because the renderer does not model mutually exclusive `allow_branch` visibility and changing the nine-template layout would exceed this bounded audit.

## Remaining route risks

- The direct loader in `common/scripted_effects/012_africa_effects.txt:1367-1386` relies on `africa_is_current_host`, `load_focus_tree = { tree = africa_continental_focus_tree keep_completed = no }`, and `africa_continental_focus_tree_loaded`; the tree header country selector at `common/national_focus/012_africa_continental_focus_tree.txt:27-33` is keyed to the loaded flag. This needs a parent-owned runtime proof for Event 6 niche-carrier loading and succession.
- Hidden Covenant and inactive overlays intentionally share static layout bands. A runtime layout refresh must run after route choice, proof resolution, Covenant reveal, compact promotion, formation transition, and host succession as required by the architecture handoff.
- The world-order package files have no dedicated AI plan and no delivered goal-art binaries, so their visible focus completion cannot be considered release-ready even though their script blocks and localisation are present.

No simplification was silently introduced. The bounded patch is limited to missing tree localisation; the art, AI, and branch-aware layout findings remain explicit blockers for parent review.

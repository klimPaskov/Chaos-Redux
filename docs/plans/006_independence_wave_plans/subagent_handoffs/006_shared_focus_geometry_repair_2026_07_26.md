# Event 006 shared focus geometry repair handoff

## Scope and status

This handoff covers a narrow coordinate-only repair in `common/national_focus/006_independence_wave_focus.txt` for the shared Event 006 tree and the accepted AGX overlay. Focus IDs, prerequisites, mutual exclusions, rewards, AI weights, localisation keys, and icon references were not redesigned or renamed. The overall Event 006 completion audit remains HOLD until the parent reruns the authoritative MCP inspection and render.

## Changed file and focus IDs

Changed file: `common/national_focus/006_independence_wave_focus.txt`.

Changed focus IDs and coordinates: `independence_wave_bind_the_first_oath` `(24,1) -> (12,1)`, `independence_wave_integrate_provinces_and_councils` `(24,2) -> (12,2)`, `independence_wave_complete_founding_settlement` `(20,3) -> (40,3)`, `independence_wave_confirm_civilian_control` `(33,7) -> (31,7)`, `independence_wave_grant_military_autonomy` `(35,7) -> (33,7)`, `independence_wave_raise_mass_reserve` `(37,8) -> (35,8)`, `independence_wave_build_professional_core` `(39,8) -> (36,8)`, `independence_wave_fund_domestic_arsenals` `(41,9) -> (37,9)`, `independence_wave_accept_foreign_arms` `(43,9) -> (39,9)`, `independence_wave_adopt_border_defense` `(33,10) -> (40,10)`, `independence_wave_adopt_reclamation_doctrine` `(35,10) -> (39,10)`, `independence_wave_standardize_with_league` `(37,11) -> (43,11)`, and `independence_wave_preserve_independent_command` `(39,11) -> (45,11)`.

The eight accepted AGX focus IDs remain at their reviewed coordinates `(100,1)`, `(99,2)`, `(101,2)`, and `(100,3..7)`.

## Route coverage

| Route surface | Before | After | Evidence |
| --- | --- | --- | --- |
| Founding settlement | Present, with `complete_founding_settlement` at `(20,3)` | Same IDs and three AND prerequisites, capstone at `(40,3)` | Source lines 119-205 |
| Economy and regional infrastructure | Present and unchanged | Same route and rewards; only shared capstone geometry moves relative to it | Source lines 217-510 |
| Officer integration | Present and unchanged | Same route and rewards; the bind/integrate spur moves to a free left lane | Source lines 119-191 and 411-451 |
| Professional defense | Present with five mutually exclusive branch pairs | Same five pairs, same OR-gated capstone, diagonal branch spacing | Source lines 528-676 |
| Former-host and recognition roots | Present and unchanged | Same three roots and descendants; only the founding capstone endpoint moves | Source lines 1215 onward and the regional branch blocks |
| AGX overlay | Accepted eight-focus overlay | Coordinates and IDs preserved exactly | Source lines 1610 onward |

## Geometry evidence

The previous authoritative MCP baseline reported 184 regular focuses, 223 connectors, 49 crossing diagnostics, 18 node intersections, 27 long connectors, and 14 blocking shared-layout diagnostics. The MCP transport was closed during this candidate validation, so no post-edit MCP metric is claimed here.

The repository parser and a coordinate-only segment audit were run against the patched file: 184 focus blocks, 184 unique IDs, 223 prerequisite connectors, zero duplicate coordinates, zero unresolved prerequisites, zero parent-below-child violations, zero collinear through-node intersections, and zero of the thirteen previously identified blocker connector pairs remain as proper crossings in the offline model. The offline model is not a substitute for the MCP engine's layout diagnostics.

The repaired geometry preserves the existing route semantics while changing only node positions. The founding capstone moves to the right of the economy/officer vertical spurs, and the defense branch is re-spaced across rows 7-11 so its incoming fan and capstone convergence no longer use the prior alternating zig-zag.

## Missing or simplified content

No focus content, route, reward, decision hook, formable hook, icon, localisation key, or AI branch was added, removed, or simplified by this patch. The broader shared-tree MCP HOLD and the exact-ten static-package reservation limitation remain outside this geometry-only handoff.

## Icon coverage

No icon references changed. All thirteen moved focus IDs retain their existing `GFX_goal_independence_wave_*` icons, and the accepted AGX overlay retains its existing generic Event 006 sprites. No new asset or `.gfx` registration is required.

## Localisation and reward mismatches

None introduced. Every moved focus retains its existing ID, description key, completion tooltip, reward block, and AI block. No localisation file changed.

## AI behavior gaps

None introduced. AI weights and focus filters were not edited. The parent should rerun the normal focus inspection after accepting the geometry to ensure no tree-level AI diagnostics are coupled to the layout rewrite.

## High-priority parent review

1. Rerun `hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt` with tree ID `independence_wave_focus_tree` and verify the exact MCP blocker count, crossing diagnostics, node intersections, and AGX preservation.
2. Rerun `hoi4.focus_render` and visually inspect the founding/economy/officer junction and the professional-defense fan before treating the patch as accepted.
3. If MCP reports new blocking crossings, keep the route IDs and prerequisite semantics unchanged and adjust only the moved coordinates or revert this candidate as a geometry-only change.
4. Complete the parent-owned Event 006 audit and live consumer validation; this handoff does not claim whole-event completion.

## Validation limits

`hoi4.focus_inspect` and `hoi4.focus_render` were attempted after the patch but both returned `Transport closed`; therefore MCP artifact links and post-edit engine diagnostics are unavailable in this turn. The source diff is coordinate-only, and the offline parser evidence above is the available review proof. No in-game run was performed.


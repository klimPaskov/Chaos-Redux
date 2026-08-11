# Event 012 Africa focus final audit — 2026-08-10

## Scope and disposition

This handoff certifies the continental focus tree, the six external continental package trees, and the priority-member focus tree against the Event 012 route matrices. The audit used the required offline wiki and vanilla documentation review, the `hoi4.focus_inspect` and `hoi4.focus_render` workflows, and an attempted `hoi4.focus_rewrite` cleanup. No focus ID, prerequisite, mutual exclusion, reward, AI weight, icon reference, or localisation key was added, removed, or renamed.

The authored layout is improved from the historical far-separated overlay placement: the nine mutually exclusive overlay templates now have compact authored lanes with conditional offsets that preserve their runtime overlay coordinates. The remaining MCP layout check is not closable safely inside this scope because the engine evaluates every conditional overlay connector simultaneously. The exact rewrite blocker is recorded below; no broad route redesign or fallback was introduced.

## Route coverage

| Surface | Evidence | Result |
| --- | --- | --- |
| Continental opening, signatures, convergence, and terminal support | `common/national_focus/012_africa_continental_focus_tree.txt`; MCP `focusCount=276` | Present |
| Regional overlays | 9 families × 6 focuses = 54 (`maghreb_sahara`, `west_atlantic`, `sahel_lake_chad`, `nile_horn`, `congo_basin`, `great_lakes`, `swahili_indian_ocean`, `southern_africa`, `madagascar_islands`) | Present; conditional offsets preserve runtime lanes |
| Grounded constitutional routes | 6 routes × 21 focuses = 126 | Present |
| Covenant constitutional route | 18 focuses | Present |
| Shared constitutional/support lanes | 36 focuses | Present |
| Main focus payoff matrix | `docs/specs/012_africa_specs/matrices/012_africa_focus_route_payoff_matrix.csv`; 78 rows = shared opening 5 + six grounded routes 9 each + Covenant 9 + shared support 10 | All accepted anchors are present |
| Host playbook matrix | `docs/specs/012_africa_specs/matrices/012_africa_host_country_playbook_matrix.csv`; 51 rows = 22 full + 29 compact | No route/file omission found |
| External packages | Asia 20, Europe 20, Middle East 20, North America 20, Oceania 20, South America 21 MCP focuses | All six trees inspect/render successfully |
| Priority member focus tree | `africa_priority_member_focus_tree`; MCP focusCount 8 | Inspect/render clean |

The source-level focus census found 277 `id` tokens including the tree declaration, 276 unique focus IDs, 325 prerequisite references, and zero dangling prerequisite IDs.

## Changed files and identifiers

Only the following gameplay files are changed in this audit worktree:

- `common/national_focus/012_africa_continental_focus_tree.txt`: authored `x`/`y` coordinates and conditional `offset` values only. The opening/trunk IDs repositioned are `africa_identify_host_problem`, `africa_build_host_coalition`, `africa_prepare_host_security`, `africa_secure_first_corridor`, `africa_select_first_partner`, `africa_write_first_guarantee`, `africa_protect_first_partner`, `africa_prove_the_first_obligation`, `africa_publish_the_first_obligation`, `africa_invite_regional_delegates`, `africa_convene_provisional_congress`, `africa_write_provisional_charter`, and `africa_choose_constitutional_principle`. The 54 overlay IDs retain their original runtime positions through the conditional offsets; no gameplay block was edited.
- `common/national_focus/012_africa_world_north_america_focus.txt`: merged duplicate `available` gates for `africa_north_america_storm_frontier_compact` into one fail-closed gate.
- `common/national_focus/012_africa_world_oceania_focus.txt`: merged duplicate `available` gates for `africa_oceania_deep_sea_covenant` into one fail-closed gate.
- `common/national_focus/012_africa_world_south_america_focus.txt`: merged duplicate `available` gates for `africa_south_america_sun_covenant` into one fail-closed gate.

The external gate merges preserve the completed-focus prerequisite, the high-chaos package flag, and the shared high-chaos variable threshold. No AI, reward, route trigger, icon, or localisation value changed.

## MCP evidence

### Continental tree

- `hoi4.focus_inspect` returned `FOCUS_INSPECTED`, revision `f59acc58a66caabc9cd04d51c6212b76c4e7f76855d6164aee203fef4ad5a2ae`, `focusCount=276`, and no missing mod icon/localisation diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74f399777e4aed59afacca2c194865022069ce5505a7c5e7882d9a8235ef0a6b/de70cc17f0d9389164194535ae328a8ef58fe10c1727cf71a33605267ec77532/focus-inspect.f59acc58a66caabc.json`.
- `hoi4.focus_render` returned `FOCUS_RENDERED` with HTML, SVG, JSON, source-map, and plan artifacts. HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9932c53969cbf3d7692ebb1e3906326986b6820bb9aa679ef04be47b66ca3c9e/08b8d695f845033d3b5cd96bb3192e5025fc39270a1741549f9f28c0009168b5/africa_continental_focus_tree.focus.html`; SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7742addf4f9bd2722da4859052bc87ff31f38f1ff2c4a34af0108ccca78e0227/36cadb3a4cd682227d163671f9e44b20a9b9cd531d87d96addbb4d0795024fdb/africa_continental_focus_tree.focus.svg`; JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/209696102fde60d96feda351d505cd5e76c628e74e0b64cbed1a55f5f8ef0c7d/7df015608aac94f46c1c0af23ebf16924fbd52322d0e7ba0e4c1ca6fb305e3c7/africa_continental_focus_tree.focus.json`.
- The inspect/render validation check still reports `focus-diagnostics: 14 blocking focus diagnostics`. The visible warnings are authored same-row spacing and connector intersections around the shared opening lanes and conditional overlay templates, plus the MCP design warning that the nine overlay reward helpers repeat a static pattern. The repeated reward warning is expected for the accepted nine-row payoff lattice: each overlay focus sets its regional step and dispatches the region/constitution-specific payoff helper in `common/scripted_effects/012_africa_effects.txt` and `012_africa_focus_route_effects.txt`.
- `hoi4.focus_rewrite` was attempted with `layoutMode=compact`, `horizontalSpacing=80`, `verticalSpacing=60`, `padding=2`, and `reviewScale=0.25`. It returned `FOCUS_LAYOUT_WORK_BUDGET_BLOCKED` before writing: phase `candidate connector pair examination`, `used=80000000`, `requested=1`, `maximumWork=80000000`. No source file was changed by the rewrite call.

### Exact 14-count blocker classification

The full linked render JSON contains 306 diagnostics. The validation message `14 blocking focus diagnostics` is the count of the 14 severity-`error` entries, all global game continuous-focus icon references. They are not Event 012 focus IDs, have no connector edges, and have no x/y coordinates:

| # | Code | Game focus ID | Missing sprite | Source |
| --- | --- | --- | --- | --- |
| 1 | `FOCUS_ICON_REFERENCE_MISSING` | `DEN_undermine_overlord_continuous_focus` | `GFX_focus_DEN_undermine_overlord_continuous_focus` | `game:common/continuous_focus/generic.txt:16` |
| 2 | `FOCUS_ICON_REFERENCE_MISSING` | `ETH_strengthen_the_black_lions` | `GFX_focus_ETH_continuous_strengthen_the_black_lions` | `game:common/continuous_focus/generic.txt:79` |
| 3 | `FOCUS_ICON_REFERENCE_MISSING` | `ETH_supporting_the_arbegnoch` | `GFX_focus_ETH_continuous_supporting_the_arbegnoch` | `game:common/continuous_focus/generic.txt:121` |
| 4 | `FOCUS_ICON_REFERENCE_MISSING` | `SWI_build_up_military_readiness` | `GFX_focus_SWI_continuous_build_up_military_readiness` | `game:common/continuous_focus/generic.txt:162` |
| 5 | `FOCUS_ICON_REFERENCE_MISSING` | `SWI_support_active_militias_continuous_focus` | `GFX_focus_SWI_continuous_support_active_militias` | `game:common/continuous_focus/generic.txt:207` |
| 6 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_naval_production` | `GFX_goal_continuous_naval_production` | `game:common/continuous_focus/generic.txt:254` |
| 7 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_air_production` | `GFX_goal_continuous_air_production` | `game:common/continuous_focus/generic.txt:280` |
| 8 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_non_factory_construct` | `GFX_goal_continuous_non_factory_construct` | `game:common/continuous_focus/generic.txt:306` |
| 9 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_reduce_training_time` | `GFX_goal_continuous_reduce_training_time` | `game:common/continuous_focus/generic.txt:347` |
| 10 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_suppression` | `GFX_goal_continuous_suppression` | `game:common/continuous_focus/generic.txt:375` |
| 11 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_repair` | `GFX_goal_continuous_repairments` | `game:common/continuous_focus/generic.txt:403` |
| 12 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_tech_share` | `GFX_goal_continuous_research` | `game:common/continuous_focus/generic.txt:431` |
| 13 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_boost_freedom` | `GFX_goal_continuous_boost_freedom` | `game:common/continuous_focus/generic.txt:476` |
| 14 | `FOCUS_ICON_REFERENCE_MISSING` | `continuous_restrict_freedom` | `GFX_goal_continuous_restrict_freedom` | `game:common/continuous_focus/generic.txt:501` |

The offline vanilla `interface/goals.gfx` defines the `GFX_goal_*` sprites, confirming that these 14 errors are MCP/global asset-index findings rather than missing Event 012 assets. No mod-local file should override unrelated vanilla continuous-focus content to suppress them. The Event 012 entries remain severity-`warning` layout/design diagnostics and are not the source of the 14-count validation failure.

For the visible Event 012 layout warnings in the final render, the authored coordinates are: `africa_maghreb_sahara_face_divided_sovereignty (26,1)` vs `africa_repair_host_administration (27,1)`; `africa_sahel_lake_chad_secure_food_and_water (30,1)` vs `africa_build_host_coalition (31,1)`; `africa_west_atlantic_a_mandate_from_ports_and_hinterlands (28,1)` vs `africa_prepare_host_security (29,1)`; `africa_west_atlantic_prove_the_atlantic_mandate (28,4)` vs `africa_secure_first_corridor (29,4)`; `africa_repair_host_administration (27,1)` vs `africa_west_atlantic_a_mandate_from_ports_and_hinterlands (28,1)`; `africa_maghreb_sahara_prepare_the_first_guarantee (20,2)` vs `africa_west_atlantic_open_port_and_inland_route (23,2)`; `africa_maghreb_sahara_seat_the_desert_council (20,3)` vs `africa_west_atlantic_make_export_wealth_public (23,3)`. The two fixed-endpoint crossing pairs are `africa_repair_host_administration (27,1) -> africa_choose_first_corridor (27,2)` against `africa_west_atlantic_a_mandate_from_ports_and_hinterlands (28,1) -> africa_west_atlantic_open_port_and_inland_route (23,2)`, and the same first edge against `africa_west_atlantic_a_mandate_from_ports_and_hinterlands (28,1) -> africa_west_atlantic_protect_the_first_neighbour (25,2)`. These warnings are branch-unaware overlay geometry; rewrite could not search beyond the fixed 80,000,000-work budget.

### External package trees

All six external trees and the priority tree returned successful `FOCUS_INSPECTED`/`FOCUS_RENDERED` responses. Their diagnostics were bounded to authored package layouts and did not report missing mod icons or localisation: Asia had three repeated-reward design warnings; Europe had five linear-detour/zigzag warnings; Middle East had four connector crossings and one detour; North America had three detours; Oceania had four detours; South America had one detour; and the priority tree was clean. The earlier South America rewrite attempt returned `REWRITE_SOURCE_STALE` without writing. These package detours are independent of the continental overlay geometry and are not route or logic defects.

## Icons, localisation, AI, and rewards

The continental inspector scanned all 13 family DDS icons under `gfx/interface/goals/012_africa/`, `interface/012_africa.gfx`, `localisation/english/012_africa_focus_l_english.yml`, and `localisation/english/012_african_union_l_english.yml`. The six external inspectors scanned the world-order interface/localisation surfaces. No missing icon, title, description, or localisation-key diagnostic was returned. No icon or localisation key changed in this audit.

Every continental focus retains an `ai_will_do` block and route-aware modifiers. AI/probability evidence remains owned by `chaosx_ai_probability_auditor`; no weight or probability patch was made here, so no probability target was invented and no probability compare was required for this layout-only pass.

## Remaining blocker and risk

The validation check remains false because the 14 severity-error entries are unrelated global vanilla continuous-focus icon-index findings listed above; they are not repairable in the Event 012 mod scope. Separately, the authored Event 012 layout still emits warning-level branch-unaware overlay crossings and spacing diagnostics. Conditional overlay offsets are evaluated as simultaneous authored connectors; the inspector explicitly reports fixed/relative endpoints and `movableFocusIds=[]` for the crossing pairs. Removing those warnings would require a broader redesign of the mutually exclusive overlay templates or the shared opening lanes, which would violate this narrow audit's requirement to preserve route semantics and runtime coordinates. The improvement-loop handoff records the same limitation as branch-unaware renderer evidence rather than a confirmed runtime defect.

No simplification, fallback, route omission, reward substitution, AI omission, icon placeholder, or localisation omission was introduced. Live Hearts of Iron IV execution was not run, per repository policy; live validation remains parent/user-owned. No commit or stage operation was performed.

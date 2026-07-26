# Event 006 shared focus geometry reflow handoff

Status: blocked; the runtime focus source remains unchanged because the authoritative MCP inspection did not reach zero blocking diagnostics.

## Scope and source state

The audited tree is `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt`.

The source file has no remaining working-tree diff after all reversible trials were restored, so no focus IDs, prerequisites, rewards, icons, localisation keys, AI weights, shared-focus imports, or route semantics were changed.

The final baseline contains 184 focuses and 223 connectors.

## Route coverage table

| Route family | Existing coverage | Geometry disposition |
| --- | --- | --- |
| Survival and state construction | Present in the shared tree | Unchanged; the founding capstone participates in all three fan crossings. |
| Package-gated government settlements | Present through the existing package focus groups | Unchanged; no package IDs were moved. |
| Economy, infrastructure, and administration | Present through `independence_wave_establish_emergency_revenue` and its descendants | Unchanged; the revenue/transport spine is one affected geometry lane. |
| Army, security, and military identity | Present through `independence_wave_integrate_militia_commands` and the professional-defense branch | Unchanged; the depot and professional-defense merge are affected geometry lanes. |
| Diplomacy, recognition, and patrons | Present in the existing diplomatic lane | Unchanged and not semantically audited in this geometry-only pass. |
| Former-host settlement and regional ambition | Present in the existing former-host and regional lanes | Unchanged; its fan endpoints are part of the crossing evidence. |
| Independence network, league, formable, signature, and high-chaos work | Present in the existing late tree and shared imports | Unchanged and outside this local geometry patch. |

## Blocking diagnostics at baseline

The post-revert `hoi4.focus_inspect` reports `14 blocking focus diagnostics`: one `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` and thirteen `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` diagnostics.

| Cluster | Blocking connectors | Source lines | Exact coupled reflow requirement |
| --- | --- | --- | --- |
| Opening economy/state handoff | `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_provinces_and_councils` crosses `independence_wave_inventory_the_state` -> `independence_wave_establish_emergency_revenue` | 280-301 | Reflow the oath/inventory parents and the integration/revenue children as one two-tier ordering, then recheck the revenue -> food -> transport and both capstone prerequisite fans. Moving either child alone inverted the next-tier ordering. |
| Founding capstone to economy transport | `independence_wave_complete_founding_settlement` -> each of `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states` crosses `independence_wave_secure_food_and_fuel` -> `independence_wave_build_regional_transport_authority` | 319-340 | Move the complete-founding fan and the secure-food/transport vertical lane together, keeping the government columns at x=3..28 and package columns at x=67+ clear. |
| Founding capstone to military depot spine | The same three complete-founding fan edges cross `independence_wave_secure_national_depots` -> `independence_wave_recall_and_vet_officers` | 441-465 | Reflow the depot/recall spine with its `integrate_militia_commands` parent and the complete-founding fan; an isolated depot shift creates new crossings from the capstone prerequisites. |
| Professional-defense merge | Six unsatisfied crossings involve `independence_wave_adopt_military_archetype_program` -> `independence_wave_adopt_border_defense`/`independence_wave_adopt_reclamation_doctrine`/`independence_wave_standardize_with_league` and branch options -> `independence_wave_found_professional_defense_institution` | 501-529 | Treat rows y=6..12 as one monotone branch layout, including all mutually exclusive pairs and the downstream sovereignty handoff. A local final-node move removed some pairings but created others; a 12-coordinate military reflow still left 14 blockers and raised connector/node metrics. |

## Candidate trial and rejection evidence

The largest deliberate trial moved only coordinates in the professional-defense cluster as a coupled set and preserved every script block other than x fields.

MCP still reported 14 blocking diagnostics for that trial, with 51 connector crossings, 20 node intersections, and 31 long connectors versus the baseline 49 crossings, 18 node intersections, and 27 long connectors.

Earlier two-anchor trials around the integration/revenue pair also failed to close the blocker set and introduced new capstone prerequisite crossings, so all candidate coordinates were reverted.

## Non-blocking layout findings retained for the parent

The baseline also reports long connectors from `independence_wave_complete_founding_settlement` -> `independence_wave_map_internal_power_centers` (17 columns), `independence_wave_inventory_the_state` -> `independence_wave_establish_emergency_revenue` (12 columns), and `independence_wave_bind_the_first_oath` -> `independence_wave_integrate_militia_commands` (14 columns).

Two non-blocking through-node findings remain on `independence_wave_complete_founding_settlement` -> `independence_wave_survey_regional_ambition`, intersecting `independence_wave_activate_package_economic_program` and `independence_wave_adopt_military_archetype_program`.

## Icon, localisation, reward, and AI audit disposition

| Surface | Result |
| --- | --- |
| Icons | No icon IDs changed; affected focuses retain their existing lane-specific icon references (`GFX_goal_independence_wave_infrastructure_authority`, `GFX_goal_independence_wave_army_integration`, and the existing political/chaos icons). |
| Localisation | No localisation keys changed and no focus-name or description mismatch was introduced. |
| Rewards | No completion rewards or scripted effects changed. |
| AI | No AI weights, route filters, or focus-selection behavior changed. |

These surfaces were intentionally not re-audited beyond confirming that the geometry trials did not edit them.

## MCP evidence

Post-revert inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8ce655b5301c8388c25e564eee0cdf31311803c01433542ec9499024abd4067/c24ce69bec317e62272add2d4c01a1012882b5c6a4b88fc9c9df8fa3f93aa844/focus-inspect.23d7d35aabb72ee6.json`.

Post-revert render artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d443f6d5492b2059ae921ee2de3968033a9efdbfe5daf80d9830b702fed20061/93ded6a2c322c198640de492b1f76a8261bfcb51073aca94f9ec4e2ae95a2ae0/independence_wave_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11c1c32334716d360aed8105602ef180f5f6e359d9b94dbadef434508ac4f5b7/d6976f4496b3fcc04ebb96989e6009e365a147fcf3f7733010ec393d0165808c/independence_wave_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20b450c4fde493c76a1f5e6f93acc68fb5e1dbc7b70f163deed4f2f4124df60e/6d1cf2da307a000447b69213403c47715598c9036063a01329c4da588bdbaeb5/independence_wave_focus_tree.focus.json`.

The post-revert layout hash is `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`, matching the pre-trial baseline.

## Validation and skipped checks

Meaningful checks run were `hoi4.focus_inspect` and `hoi4.focus_render` before trials and after the full revert, both against `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree`.

The final MCP validation remains `passed: false` with `14 blocking focus diagnostics`, confirming that no unreviewed candidate was retained.

`hoi4.focus_rewrite` was not used because compact rewriting would be a broad layout mutation outside this bounded coupled-cluster scope.

In-game validation was not run because repository guidance assigns live consumer testing to the parent/user.

## Remaining route risks and parent handoff

The tree remains runtime-valid at its baseline source state, but the 14 MCP blocking geometry diagnostics remain unresolved and may make the focus view visually ambiguous in affected lanes.

The next implementation attempt should solve the opening handoff, founding-capstone fan, depot spine, and professional-defense merge as one constrained layout problem, then rerun inspect and render before retaining any coordinate change.

This handoff is the plan path for the blocked geometry tranche: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_shared_focus_geometry_reflow_2026-07-26.md`.

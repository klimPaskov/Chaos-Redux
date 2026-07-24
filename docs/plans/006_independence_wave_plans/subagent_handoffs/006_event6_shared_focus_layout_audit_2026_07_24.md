# Event 006 shared focus layout audit

Date: 2026-07-24

Scope: `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`.

## Outcome

The shared tree was re-inspected and re-rendered after the previous layout pass. The source focus tree is unchanged. Two small coordinate probes were applied temporarily and then fully reverted because they reduced one aggregate count while increasing node intersections or introducing new crossings and spacing warnings. The final source therefore preserves the existing route logic, prerequisites, mutual exclusions, rewards, AI weights, icon references, and localisation.

The final inspect returned 176 regular focuses, 214 connectors, bounds `x=1..97` and `y=0..19`, layout hash `3e5996acbdbed97ab085d52cd058861f2fbd21acc896f859268b204a9c81a5a2`, 49 connector crossings, 18 node intersections, and 26 long connectors. The validator reports 14 blocking focus diagnostics. The render reports the same 14 blocking diagnostics at 17200 by 2440 pixels.

## Files and identifiers

| Surface | Result |
|---|---|
| `common/national_focus/006_independence_wave_focus.txt` | Unchanged; no gameplay source patch retained. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_shared_focus_layout_audit_2026_07_24.md` | This handoff is the only file added by this audit. |
| Focus tree | `independence_wave_focus_tree` |
| Focus IDs | All existing IDs preserved. No prerequisite, mutual-exclusion, reward, AI, icon, or localisation ID changed. |

## Inspect and render evidence

Final inspect artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c7d610b57b9bedb5fbf42c60c6eb6db571093cbea4718d868ec3e65fb62a5c8/6c4a311813f7e0141f0835c9ac100f5caf25ccf5d292ca7421a0107a23910c1a/focus-inspect.83e61b433cb72340.json`

Final render artifacts:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4445d785ad4bf66d15767136530b2aab227fad1ef72097d65c853f3d3ba4d725/e2c610f123d6cdfd0a5fb4759f33b1fcc6892af6a9fd96884419b4f2bcf62edc/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d74054ceefae952e810f86c67444a78301b86cf14fd47387159136c514bfc1a/c23b5cb03a159b65d6f9368c67bfbe342eed2d526f271a29408e4e3b257386b7/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/240e6f7e5c777c81dc2092da0b14716b8f91b527e20531daf98375256d1f11c2/e1c8ae9fb85fc2b7b66d49cb28c06e53d057504a8d6411408a77f1713c366062/independence_wave_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b66834bb2de543afaee08bad9cf110c48cb9447d9cf7ee57f2f0d169879d41e/01d67155500eb0fb20e51473f44fa5a9d0580e1b822d36577e8dcda3d3cd373d/independence_wave_focus_tree.focus.source-map.json`
- Layout plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84f0996962af15cda701b880b63c84c58f9e58bdd5531731a4e3215f4e94927d/352e2ea2b376d2b8a72ee46a0adb110483a2989514c0c6d39ecced0767870979/independence_wave_focus_tree.focus.plan.json`

## Coordinate probes

| Revision | Blocking diagnostics | Crossings | Node intersections | Result |
|---|---:|---:|---:|---|
| Baseline and final | 14 | 49 | 18 | Retained geometry. |
| Probe A: moved founding/oath endpoints, economy lane to `x=26`, and military opening lane to `x=32` | 14 | 45 | 28 | Rejected; fewer aggregate crossings but more node intersections and a new same-row spacing warning. |
| Probe B: additionally moved the first three economy nodes to `x=18` | 14 | 49 | 28 | Rejected; restored the crossing count while adding root/economy crossing pressure. |

The probes show that the remaining issues are coupled lane geometry problems, not safe one-focus coordinate corrections. The source was restored to the baseline hash before final inspection and render.

## Route coverage

The architecture specification is `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md`.

| Spec lane | Source evidence | Coverage |
|---|---|---|
| Survival and state construction | Founding administration IDs from `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` at approximately lines 62-216. | Present. The settlement chain remains the shared central spine. |
| Government and internal power | Constitutional, popular-council, traditional, emergency-command, patron/client, radical-sovereignty, and AJX settlement IDs in the government block around lines 817-1212. | Present. Route locks and mutual exclusions remain in source. |
| Economy, infrastructure, and administration | `independence_wave_inventory_the_state`, `independence_wave_establish_emergency_revenue`, `independence_wave_secure_food_and_fuel`, `independence_wave_build_regional_transport_authority`, and the continuation through `independence_wave_create_independent_treasury` around lines 280-397. | Present. The lane is gameplay-wired; only its connector geometry is noisy. |
| Army, security, and military identity | `independence_wave_integrate_militia_commands` through `independence_wave_preserve_independent_command` around lines 400-663, including the five-way convergence into `independence_wave_found_professional_defense_institution`. | Present. The convergence is the main military layout hotspot. |
| Diplomacy, recognition, and patrons | Foreign-office, guarantor, recognition, and treaty IDs around lines 670-812. | Present. No missing diplomacy route or unlock hook was found. |
| Former-host policy, borders, and expansion | `independence_wave_define_former_host_policy` at line 1274 and its continuation through the former-host and regional expansion block around lines 1273-1518. | Present. The lane is distinct from league/formable content. |
| Network, league, formables, and high-chaos sovereignty | `independence_wave_recognize_fellow_new_states` at line 1529 and the later league, formable, and high-chaos modules through approximately lines 1528-1970 and the late shared blocks around lines 2895-3115. | Present. No broad route family is missing within this layout scope. |
| Shared regional overlays | Shared package and regional overlay focus blocks at the top and late sections of the file, including the existing IW043, IW058, IW093, and IW098 families. | Present. No overlay was removed or disconnected by this audit. |

## Blocking layout diagnostics

The 14 blocking diagnostics are connector crossings. One physical crossing emits both the avoidable-crossing and unsatisfied-crossing diagnostics. Source line references below are the focus block start lines in `common/national_focus/006_independence_wave_focus.txt`.

| Diagnostic | Crossing | Source references |
|---|---|---|
| `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` | `independence_wave_bind_the_first_oath -> independence_wave_integrate_provinces_and_councils` crosses `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue`. | 119, 177, 100, 281 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | Same crossing as above. | 119, 177, 100, 281 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses `independence_wave_secure_food_and_fuel -> independence_wave_build_regional_transport_authority`. | 197, 1214, 300, 320 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses `independence_wave_secure_food_and_fuel -> independence_wave_define_former_host_policy`. | 197, 1214, 300, 1274 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses `independence_wave_secure_food_and_fuel -> independence_wave_recognize_fellow_new_states`. | 197, 1214, 300, 1529 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses `independence_wave_secure_national_depots -> independence_wave_recall_and_vet_officers`. | 197, 1214, 421, 442 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses `independence_wave_secure_national_depots -> independence_wave_define_former_host_policy`. | 197, 1214, 421, 1274 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus` crosses `independence_wave_secure_national_depots -> independence_wave_recognize_fellow_new_states`. | 197, 1214, 421, 1529 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_border_defense` crosses `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution`. | 483, 611, 527, 502 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_border_defense` crosses `independence_wave_grant_military_autonomy -> independence_wave_found_professional_defense_institution`. | 483, 611, 541, 502 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine` crosses `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution`. | 483, 625, 527, 502 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine` crosses `independence_wave_grant_military_autonomy -> independence_wave_found_professional_defense_institution`. | 483, 625, 541, 502 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_adopt_military_archetype_program -> independence_wave_preserve_independent_command` crosses `independence_wave_build_professional_core -> independence_wave_found_professional_defense_institution`. | 483, 653, 569, 502 |
| `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` | `independence_wave_adopt_military_archetype_program -> independence_wave_standardize_with_league` crosses `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution`. | 483, 639, 527, 502 |

## Nonblocking geometry warnings

The inspect/render output contains 19 warnings in total. The 14 rows above are the blocking subset. The other five are nonblocking layout-quality warnings:

- Long connector `independence_wave_complete_founding_settlement -> independence_wave_map_internal_power_centers` spans 17 columns and one row.
- Long connector `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue` spans 12 columns and one row.
- Long connector `independence_wave_bind_the_first_oath -> independence_wave_integrate_militia_commands` spans 14 columns and one row.
- Connector `independence_wave_complete_founding_settlement -> independence_wave_survey_regional_ambition` passes through `independence_wave_activate_package_economic_program`.
- The same connector passes through `independence_wave_adopt_military_archetype_program`.

These warnings are symptoms of the same broad fan-out and fixed endpoint geometry. They were not hidden by changing prerequisites or removing connectors.

## Missing or simplified content

No route, focus reward, decision/mission hook, idea, advisor, leader, flag, claim, core, war-goal, event, or formable unlock was omitted or simplified by this audit. No new route family was added because that would exceed the bounded layout scope. The only unresolved item is planar readability of the existing shared tree.

## Icon coverage

| Coverage surface | Result |
|---|---|
| Regular focus nodes | The MCP inspect resolved icon assets for all 176 regular focus nodes. No missing-icon diagnostic was emitted. |
| Shared focus blocks | Existing shared IW focus families retain their source-level icon assignments. No icon ID was changed. |
| Rendered icon references | The final render contains no missing icon asset diagnostic. |

## Localisation and reward mismatch list

No mismatch was found. The inspect resolved all 176 focus titles, and no missing localisation diagnostic was emitted. Existing focus descriptions and custom reward tooltips remain paired with their source IDs. No reward text or localisation key was changed.

## AI behavior gaps

No bounded-scope AI gap was found. Existing focus blocks retain their `available` and `ai_will_do` logic, including route-aware weights where present. No AI weight was changed because a coordinate-only patch must not rebalance route selection.

## High-priority fixes

1. If all 14 blocking diagnostics must be cleared, re-pack the founding fan-out, economy/officer lanes, and regional roots as coordinated clusters rather than moving one endpoint at a time. The affected anchors are `independence_wave_complete_founding_settlement`, `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_secure_food_and_fuel`, `independence_wave_secure_national_depots`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states`.
2. Reflow the professional-defense convergence as one cohort containing `independence_wave_confirm_civilian_control`, `independence_wave_grant_military_autonomy`, `independence_wave_build_professional_core`, `independence_wave_adopt_border_defense`, `independence_wave_adopt_reclamation_doctrine`, `independence_wave_standardize_with_league`, `independence_wave_preserve_independent_command`, and `independence_wave_found_professional_defense_institution`.
3. After the crossings are solved, shorten the three long connectors and remove the two through-node paths. Treat those changes as a follow-on geometry pass because solving them first increased crossings in the probes.
4. If the parent wants a fully planar tree, use a plan-mode or broader layout redesign with explicit approval. It will require moving coupled clusters and reviewing the rendered route hierarchy; it should not be implemented as isolated coordinate tweaks.

## Remaining route risks

The current gameplay graph is intact, but the fixed endpoint geometry still creates the 14 blocking crossings and five nonblocking warnings. Changing prerequisites, mutual exclusions, or hidden effects to suppress connector lines would change gameplay semantics and is outside this audit. Moving a single root can shift crossings into the shared overlay and formable lanes. A future broad reflow should therefore be reviewed with both `hoi4.focus_inspect` and `hoi4.focus_render` after every coupled-cluster change.

## Validation and limits

The required offline Paradox wiki pages, relevant vanilla focus documentation, `hoi4.focus_inspect`, and `hoi4.focus_render` were used. No gameplay runtime or save validation was run because the source focus tree was not changed. No plan handoff was created for a broader redesign; this file records the bounded audit and leaves any larger reflow to the parent decision.

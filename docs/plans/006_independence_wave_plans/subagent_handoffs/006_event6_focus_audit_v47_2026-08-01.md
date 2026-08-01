# Event 006 focus audit v47 handoff

Date: 2026-08-01

Scope: Event 006 national-focus route coverage, prerequisite semantics, mutual exclusions, rewards and costs, icon/localisation references, AI route behavior, shared-focus import reachability, and meaningful-tree preservation.

## Outcome

The shared-focus import list had a real route-visibility defect: the root imported only the IW-093 Asante and IW-098 Sokoto opening focuses, so their descendant shared focuses were not pulled into `independence_wave_focus_tree`. The root now imports the terminal and sibling terminal focuses for both packages. Static prerequisite traversal reaches all 111 Event 006 shared-focus definitions after the patch.

The direct tree remains structurally connected: all 184 direct focuses are reachable from `independence_wave_prepare_capital_administration`.

The tree still has the known MCP layout blocker set. `hoi4.focus_inspect` reports `validation.passed = false` with 14 blocking focus diagnostics; no layout rewrite was attempted because geometry redesign is outside this bounded patch.

## Changed file and focus ids

Changed file: `common/national_focus/006_independence_wave_focus.txt`.

Changed tree import ids: `independence_wave_iw093_prepare_form24_west_african_federation`, `independence_wave_iw093_proclaim_sovereign_asante_confederacy`, `independence_wave_iw093_authorize_veterans_guardianship`, `independence_wave_iw098_prepare_form25_sahel_confederation`, and `independence_wave_iw098_authorize_frontier_command`.

Before: only `independence_wave_iw093_seat_kumasi_administration` and `independence_wave_iw098_reconvene_emirate_council` were imported for these two shared branches, leaving 41 descendant definitions unreachable from the root import graph.

After: all 111 shared-focus definitions across `006_independence_wave_focus.txt`, `006_independence_wave_iw043_iw058_focus.txt`, `006_independence_wave_iw093_iw098_focus.txt`, and `006_independence_wave_pacific_focus.txt` are reachable from explicit root imports and prerequisite ancestry.

No focus block, localisation file, icon definition, decision, scripted effect, or AI file was otherwise changed.

## Route coverage table

| Lane | Evidence | Status |
| --- | --- | --- |
| Survival/state | Eight direct focuses from `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` at lines 66-218 | Covered |
| Government/internal power | Constitutional, popular council, traditional restoration, emergency military, patron-client, radical sovereignty, plus AJX municipal neutral commission; route locks and route-aware availability are in `006_independence_wave_focus.txt` lines 822-1274 and `006_independence_wave_focus_triggers.txt` | Covered |
| Economy/admin | Six-focus emergency revenue, supply, transport, customs, package program, treasury chain at lines 284-402 | Covered |
| Army/security | Militia/depot/officer/border chain, force archetype, five mutually exclusive choice pairs, professional-defense capstone at lines 405-669 | Covered |
| Diplomacy/recognition | Foreign office, missions, neighbor recognition, neutrality or patron balance, treaty-backed state, permanent foreign service at lines 675-816 | Covered |
| Former host/borders | Policy root, negotiated, guarded frontier, association, reclamation, and collapsed-host branches at lines 1279-1455 | Covered |
| Regional ambition/formables/high chaos | Regional survey, committees/congress, integration authority, signature extension, Form-03/04/05/12/13/18/24/25 package consumers, and radical lane at lines 1461 onward plus shared package files | Covered, subject to package admission/formable gates |
| Network/league | Recognition, civil-service exchange, aid corridor, arbitration, charter, founding members, congress, and five mutually exclusive charter proposals at lines 1533-1710 | Covered |
| Country/package overlays | Direct SCO/WLS/AJX/BRI/AFX/AGX/RHI/BAY/ARX/ASX groups plus imported COR/HBX/HAW/FIJ/IW-043/IW-058/IW-093/IW-098 groups | Covered after import patch |

## Missing or simplified content

- Fixed in this patch: IW-093 and IW-098 shared-focus descendants were not visible in the full tree because only opening focuses were imported.
- No remaining disconnected direct focus blocks were found; prerequisite traversal reaches 184 of 184 direct focuses.
- No remaining unimported shared-focus definitions were found; explicit root imports plus prerequisite ancestry reach 111 of 111 shared definitions.
- Package-specific focus blocks for several legacy carrier packages use generic `independence_wave_focus_ai.*` base weights and delegate route-specific production and restraint to the paired `common/ai_strategy/006_independence_wave_*.txt` profiles. This is an intentional split, but it remains a review point if acceptance later requires per-focus route modifiers.
- Geometry remains simplified only in the sense that the authored coordinates were preserved; no automatic compact rewrite was applied.

## Icon coverage table

The static scan found 312 direct/shared focus blocks, 121 unique icon references, and zero missing icon definitions in the scanned `interface/*.gfx` files.

| Core icon id | Focus references |
| --- | ---: |
| `GFX_goal_independence_wave_former_host_settlement` | 21 |
| `GFX_goal_independence_wave_army_integration` | 19 |
| `GFX_goal_independence_wave_infrastructure_authority` | 18 |
| `GFX_goal_independence_wave_founding_administration` | 17 |
| `GFX_goal_independence_wave_league_congress` | 14 |
| `GFX_goal_independence_wave_regional_formable` | 13 |
| `GFX_goal_independence_wave_high_chaos_sovereignty` | 12 |
| `GFX_goal_independence_wave_recognition_diplomacy` | 11 |
| `GFX_goal_independence_wave_constitutional_state` | 10 |
| `GFX_goal_independence_wave_patron_client` | 8 |
| `GFX_goal_independence_wave_military_emergency` | 7 |
| `GFX_goal_independence_wave_traditional_restoration` | 6 |
| `GFX_goal_independence_wave_popular_councils` | 4 |

All package-specific icon families, including IW-043, IW-058, IW-093, IW-098, Pacific, Form-03, AFX, RHI, BAY, ARX, ASX, and AJX, were defined in the scanned interface files and resolved by the static reference check.

## Localisation and reward mismatch list

No mismatch was found in the static scan.

- All 312 blocks have a matching title key and `_desc` key in the English localisation set.
- All `custom_effect_tooltip` keys referenced by these focus blocks resolve in the English localisation set.
- All 312 blocks have an `ai_will_do` block and a `completion_reward` block.
- All 312 focus costs use scoped constants rather than literal cost values.
- Rewards are lane- and package-specific through `independence_wave_focus_*` helpers and package focus effects; no focus was found with a missing reward hook.

## AI behavior gaps

The shared and core routes use route-aware modifiers for instability, war, patron dependency, host threat, recognition, league membership, military profile, and radical/high-chaos state. Package strategy files supply the deeper package behavior: IW-043/IW-058 include reserve/crisis and government routes, IW-093/IW-098 include host crisis and route profiles, Pacific includes survival/restraint/host-threat profiles, and Scotland/Wales/Brittany/Saar/Rhineland/Bavaria/Mediterranean packages include route and host policies.

The remaining review risk is that some package focus blocks themselves have only a base focus weight while the route-aware behavior lives in `common/ai_strategy`. This is not a missing AI profile, but it is less visible in the focus source than the core route modifiers.

## Exact MCP geometry diagnostics

Post-patch `hoi4.focus_inspect` reports 184 direct focuses, 223 connectors, 45 connector crossings, 7 node intersections, 28 long connectors, and `validation.passed = false` with 14 blocking focus diagnostics.

The returned raw diagnostics identify these authored-layout problems:

1. `FOCUS_LAYOUT_LONG_CONNECTOR`: `independence_wave_complete_founding_settlement -> independence_wave_map_internal_power_centers`, 17 columns.
2. `FOCUS_AVOIDABLE_CONNECTOR_CROSSING`: `bind_the_first_oath -> integrate_provinces_and_councils` crosses `inventory_the_state -> establish_emergency_revenue`.
3. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: the same survival/economy pair remains crossed because all endpoints are fixed or relative.
4. `FOCUS_LAYOUT_LONG_CONNECTOR`: `inventory_the_state -> establish_emergency_revenue`, 12 columns.
5. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `complete_founding_settlement -> ajx_appoint_neutral_commission_focus` crosses `secure_food_and_fuel -> build_regional_transport_authority`.
6. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `complete_founding_settlement -> define_former_host_policy` crosses `secure_food_and_fuel -> build_regional_transport_authority`.
7. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `complete_founding_settlement -> recognize_fellow_new_states` crosses `secure_food_and_fuel -> build_regional_transport_authority`.
8. `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE`: `complete_founding_settlement -> survey_regional_ambition` intersects `activate_package_economic_program`.
9. `FOCUS_LAYOUT_LONG_CONNECTOR`: `bind_the_first_oath -> integrate_militia_commands`, 14 columns.
10. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `complete_founding_settlement -> ajx_appoint_neutral_commission_focus` crosses `secure_national_depots -> recall_and_vet_officers`.
11. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `complete_founding_settlement -> define_former_host_policy` crosses `secure_national_depots -> recall_and_vet_officers`.
12. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `complete_founding_settlement -> recognize_fellow_new_states` crosses `secure_national_depots -> recall_and_vet_officers`.
13. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `complete_founding_settlement -> survey_regional_ambition` crosses `form_border_guard -> adopt_military_archetype_program`.
14. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `focus_build_permanent_foreign_service -> secure_durable_sovereignty` crosses `preserve_independent_command -> found_professional_defense_institution`.
15. `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`: `focus_build_permanent_foreign_service -> secure_durable_sovereignty` crosses `standardize_with_league -> found_professional_defense_institution`.
16. `FOCUS_LAYOUT_LONG_CONNECTOR`: `confirm_civilian_control -> found_professional_defense_institution`, 9 columns.
17. `FOCUS_LAYOUT_LONG_CONNECTOR`: `preserve_independent_command -> found_professional_defense_institution`, 9 columns.
18. `FOCUS_LAYOUT_LONG_CONNECTOR`: `adopt_military_archetype_program -> adopt_reclamation_doctrine`, 9 columns.
19. `FOCUS_LAYOUT_LONG_CONNECTOR`: `adopt_military_archetype_program -> standardize_with_league`, 11 columns.

The MCP validation summary counts 14 blocking diagnostics even though the raw diagnostics collection exposes 19 warning entries, so the linked artifact should remain the authoritative machine-readable record.

## Mutual exclusions and prerequisite semantics

The static scan found zero missing mutual-exclusion targets. Six one-sided exclusions are the AJX neutral-commission focus listing the six generic government route ids; the reverse declarations are intentionally unnecessary because every generic route lock also checks `independence_wave_government_route_locked`, and AJX's lock trigger checks the same flag.

Multiple-focus prerequisite blocks were reviewed against the Event 006 route design. The five defense capstone blocks are OR choice pairs combined as AND across blocks, treaty-backed state accepts either neutrality or balanced patrons, and package route consumers use OR where the branch alternatives are mutually exclusive.

## Validation and skipped checks

Meaningful checks run: `hoi4.focus_inspect` after patch, `hoi4.focus_render` after patch, shared-focus import reachability traversal, direct prerequisite reachability traversal, icon/localisation/tooltip/AI/reward static cross-check, cost-constant scan, and mutual-exclusion target scan.

Post-patch inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/17717287ee8f64253eb48ed4af0cfd1cd23de8383527ab025d00d70338424fd9/f473e3654292d37a6641a464b7f31e7d168b072c84ecb7e22125270cb7cd1dc4/focus-inspect.b8c9e24cc7c88c5f.json`.

Post-patch render artifacts: HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d9d92dec735778fa132574ccf85adac51d32bfe3a77d83c15ebcb73a1d4fa95/3217582e1253077bafd5841c893b09dd8e8df002235c733d0c412cc4ad348ba8/independence_wave_focus_tree.focus.html`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db058a79681af4beadd7012b103961104222162d8df430e7e294a1c47cbc39dd/7f10ee35ef2cb9e2034246987a476d0ee5eacab5321c6bc6d7251e511933d0e6/independence_wave_focus_tree.focus.svg`, and JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3042950478140a1c82191308cfec90826e3fa9bcb914a06a8ad3237c18f0356f/c6a057c93fae52d5483984b8fe92cf82e0cae8bdc0713a74bc89eb458782883d/independence_wave_focus_tree.focus.json`.

Skipped `hoi4.focus_rewrite` because the remaining defects are broad authored geometry and the task forbids a whole-tree redesign. Skipped in-game execution because repository guidance assigns live validation to the user.

## Remaining route risks and handoff

The import defect is patched, but parent review is still required for the 14 blocking geometry diagnostics, package admission/formable reachability outside the focus source, and whether focus-level generic AI bases are sufficient when paired strategy profiles own route weighting.

No separate improvement plan was written because the only gameplay defect found was local and patched; the geometry reflow is a parent-owned broad layout task.

# Event 006 focus geometry audit and reflow decision - 2026-08-01

## Decision

No source patch is safe in this bounded pass. `common/national_focus/006_independence_wave_focus.txt` remains unchanged because the current MCP blockers are coupled across the survival, economy, military, diplomacy, former-host, network, and package lanes, while each crossing-unsatisfied diagnostic reports `movableFocusIds = []` and preserves its endpoint IDs. A coordinate-only edit to any one endpoint would change the lane topology or pull an additive package branch across another route; a complete solution needs a coordinated reflow with inspect/render review after each coherent cluster.

## Scope and changed files

| Surface | Result |
| --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` | Read-only; 184 regular focuses and 23 shared-focus definitions were preserved. |
| `common/national_focus/006_independence_wave_pacific_focus.txt` | Read-only; 20 shared-focus package blocks were source-audited. |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` | Read-only; 48 shared-focus package blocks were source-audited. |
| `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` | Read-only; 43 shared-focus package blocks were source-audited. |
| Localisation and Event 006 `.gfx` files | Read-only; no missing title, description, tooltip, or icon definition was found. |
| Changed focus IDs | None. |
| New implementation | None; this file is the geometry blocker/reflow handoff. |

## Route coverage table

| Required route or lane | Current source evidence | Coverage |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration`, `independence_wave_name_provisional_authority`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, `independence_wave_establish_permanent_ministries`, `independence_wave_restore_regional_communications`, `independence_wave_integrate_provinces_and_councils`, and `independence_wave_complete_founding_settlement` (`common/national_focus/006_independence_wave_focus.txt:66-240`). | Present. |
| Internal power and government settlements | `independence_wave_map_internal_power_centers` and the constitutional, popular-council, traditional, emergency-military, guarantor/client, radical-sovereignty, and AJX neutral-commission branches (`common/national_focus/006_independence_wave_focus.txt:247-1260`). | Present; route locks and mutual exclusions remain in source. |
| Economy and administration | `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury` (`common/national_focus/006_independence_wave_focus.txt:307-421`). | Present. |
| Army, security, and professional defence | `independence_wave_integrate_militia_commands` through `independence_wave_found_professional_defense_institution` (`common/national_focus/006_independence_wave_focus.txt:428-551`). | Present; the ten y=8 military choices retain their pairwise mutual exclusions and five OR prerequisite groups at the capstone. |
| Diplomacy, recognition, and patrons | `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service` and `independence_wave_secure_durable_sovereignty` (`common/national_focus/006_independence_wave_focus.txt:698-838`, `:3152-3171`). | Present. |
| Former-host, borders, and regional expansion | `independence_wave_define_former_host_policy` and its negotiated, guarded, association, successor, and reclamation branches, followed by `independence_wave_survey_regional_ambition` (`common/national_focus/006_independence_wave_focus.txt:1301-1550`). | Present. |
| Network, league, formable, and high-chaos | `independence_wave_recognize_fellow_new_states`, the five league proposals, `independence_wave_focus_discover_regional_identity` through the FORM-03 chain, and `independence_wave_sponsor_further_ruptures` through `independence_wave_rewrite_charter_of_borders` (`common/national_focus/006_independence_wave_focus.txt:1556-1988`). | Present. |
| Country/package overlays and additive roots | SCO, WLS, AJX, BRI, AFX, AGX, RHI, BAY, ARX, ASX, COR, CAT, Pacific, IW-043/IW-058, and IW-093/IW-098 shared-focus blocks across the four source files listed above. | Present in source; package admission remains parent-owned. CAT remains additive and is not replaced by the full framework. |

No required route family, focus identifier, prerequisite branch, reward block, icon reference, localisation key, or AI block was missing in this bounded source audit.

## MCP geometry evidence

`hoi4.focus_inspect` on `independence_wave_focus_tree` with `common/national_focus/006_independence_wave_focus.txt` and default spacing returned `FOCUS_INSPECTED` with `validation.passed = false` and the check message `14 blocking focus diagnostics`. The current layout hash is `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`.

The inspected tree contains 184 regular focuses and 223 connectors, with bounds `x=1..101`, `y=0..19`, 45 crossings, 7 node intersections, 28 long connectors, 5 same-row pairs below the required two-column spacing, maximum horizontal span 80, maximum vertical span 6, total horizontal span 1228, and maximum Manhattan span 81.

The structural diagnostics are seven long-connector warnings, one avoidable crossing, ten crossing-unsatisfied diagnostics, and one through-node diagnostic, plus the informational inline-file truncation notice. The seven long connectors are `independence_wave_complete_founding_settlement -> independence_wave_map_internal_power_centers` (17 columns), `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue` (12), `independence_wave_bind_the_first_oath -> independence_wave_integrate_militia_commands` (14), `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution` (9), `independence_wave_preserve_independent_command -> independence_wave_found_professional_defense_institution` (9), `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine` (9), and `independence_wave_adopt_military_archetype_program -> independence_wave_standardize_with_league` (11).

The avoidable crossing is `independence_wave_bind_the_first_oath -> independence_wave_integrate_provinces_and_councils` against `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue` (`common/national_focus/006_independence_wave_focus.txt:306-323`). The first three crossing clusters are the founding-settlement fan from `independence_wave_complete_founding_settlement` to `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states` crossing `independence_wave_secure_food_and_fuel -> independence_wave_build_regional_transport_authority` (`:345-400`), and the same fan crossing `independence_wave_secure_national_depots -> independence_wave_recall_and_vet_officers` (`:468-487`). The fan also crosses `independence_wave_form_border_guard -> independence_wave_adopt_military_archetype_program` (`:509-526`). The final two crossing groups are `independence_wave_focus_build_permanent_foreign_service -> independence_wave_secure_durable_sovereignty` against the `independence_wave_preserve_independent_command` and `independence_wave_standardize_with_league` edges into `independence_wave_found_professional_defense_institution` (`:528-551`). The through-node diagnostic is `independence_wave_complete_founding_settlement -> independence_wave_survey_regional_ambition` through `independence_wave_activate_package_economic_program` (`:383-400`).

For every crossing-unsatisfied diagnostic, MCP reports `movableFocusIds = []` and lists all four endpoint IDs as preserved. The overlay-only files return `FOCUS_TREE_NOT_FOUND` when passed as standalone trees because they contain shared-focus blocks, so they require source-level review rather than a separate MCP tree render.

Latest render artifacts reproduce the same hash and diagnostics:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbf12014e0ce676dbf814525cb774e8b4d8e871e1eac5cbed18ccc9275cb3f17/4eea9d5a8bf2a72566324d6eaf1c6aaca50ccd38cb15a72a57cb5f49548e5140/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbf12014e0ce676dbf814525cb774e8b4d8e871e1eac5cbed18ccc9275cb3f17/4eea9d5a8bf2a72566324d6eaf1c6aaca50ccd38cb15a72a57cb5f49548e5140/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dbf12014e0ce676dbf814525cb774e8b4d8e871e1eac5cbed18ccc9275cb3f17/4eea9d5a8bf2a72566324d6eaf1c6aaca50ccd38cb15a72a57cb5f49548e5140/independence_wave_focus_tree.focus.json`

## Missing or simplified content

No route, focus, reward, icon, localisation, or AI content was omitted or replaced in this pass. The unresolved simplification is validator-clean geometry: the baseline still has 14 blocking diagnostics, and isolated coordinate shifts are unsafe. No CAT additive overlay or full-framework assignment boundary was changed.

## Icon coverage table

| Surface | Result |
| --- | --- |
| Four Event 006 focus source files | 318 icon references across 318 parsed focus/shared-focus blocks. |
| Used icon IDs | 121 unique IDs. |
| Sprite definitions | Every used icon has a matching definition in the Event 006/imported package `.gfx` files; all 121 also have a `_shine` reference. |
| Reuse finding | Reuse is intentional within route families such as army integration, infrastructure, former-host settlement, league congress, and package-specific icon families; no missing or accidental blank icon was found. |

## Localisation and reward mismatch list

- All 318 parsed focus/shared-focus IDs have a title key and `_desc` key in the Event 006 localisation inventory.
- All 318 parsed blocks have a `completion_reward`, a `custom_effect_tooltip`, and a corresponding tooltip localisation key.
- No direct focus-name/reward contradiction was found in the bounded source review.
- No localisation, reward, prerequisite, mutual-exclusion, or icon patch is justified while the four geometry clusters remain coupled.

## AI behavior gaps

Every parsed focus/shared-focus block has an `ai_will_do` block, and package roots use exact package gates. The tree header remains gated by `has_country_flag = independence_wave_full_focus_framework` and `is_independence_wave_active_country = yes`. However, 114 of the 207 blocks in the main framework file are base-only `ai_will_do` entries without a modifier, including generic late route selectors such as `independence_wave_recognize_fellow_new_states`, `independence_wave_survey_regional_ambition`, `independence_wave_focus_discover_regional_identity`, and several league/formable proposal nodes (`common/national_focus/006_independence_wave_focus.txt:1483-1728`). This is a tuning opportunity against the architecture requirement for route-aware selection, not a missing AI block or a reason to alter geometry here. Scenario-level focus selection and route probabilities were not simulated.

## High-priority fixes and minimal actionable plan

1. Reflow the opening handoff as one cluster: `independence_wave_bind_the_first_oath`, `independence_wave_integrate_provinces_and_councils`, `independence_wave_inventory_the_state`, `independence_wave_establish_emergency_revenue`, and their adjacent y=2 endpoints (`common/national_focus/006_independence_wave_focus.txt:145-323`). Preserve the AND prerequisite semantics and test whether the avoidable crossing falls without creating a same-row collision.
2. Reflow the founding fan and economy lane together: `independence_wave_complete_founding_settlement`, `independence_wave_secure_food_and_fuel`, `independence_wave_build_regional_transport_authority`, `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states` (`:223-400`). The three fan crossings cannot be solved by moving only a destination.
3. Reflow depot/recall with the same fan and military lane: `independence_wave_secure_national_depots`, `independence_wave_recall_and_vet_officers`, `independence_wave_form_border_guard`, and `independence_wave_adopt_military_archetype_program` (`:448-526`). Keep the military route’s fixed parent and package branch spacing under review.
4. Reflow the professional-defence merge as a monotone y=6..9 cluster: `independence_wave_adopt_military_archetype_program`, all ten y=8 military choice focuses, `independence_wave_found_professional_defense_institution`, `independence_wave_focus_build_permanent_foreign_service`, and `independence_wave_secure_durable_sovereignty` (`:509-551`, `:820-838`). Preserve all five OR prerequisite groups and every pairwise mutual exclusion.
5. After each coherent cluster, rerun `hoi4.focus_inspect` and `hoi4.focus_render`, compare crossings, node intersections, long connectors, same-row spacing, and the layout hash, and reject any candidate that improves a local edge while worsening global metrics.

## Validation and skipped checks

- Read the required offline Paradox wiki pages, relevant vanilla national-focus documentation, and all named Chaos Redux skills before auditing.
- Ran `hoi4.focus_inspect` and recorded the failed validation, layout hash, metrics, and blocker diagnostics above.
- Ran `hoi4.focus_render`; HTML, SVG, and JSON artifacts reproduce the same blockers and hash.
- Ran read-only source scans for focus/shared-focus IDs, title/description localisation, tooltip localisation, icon/shine coverage, completion rewards, AI blocks, and duplicate IDs.
- Confirmed target focus files remain unchanged after the audit; unrelated worktree edits were preserved.

Skipped `hoi4.focus_rewrite` because this is not a safe local rewrite and the MCP diagnostics identify no movable endpoints. Skipped raster inspection because structural inspect/render evidence is sufficient for this geometry decision. No game launch, save runtime test, package-admission proof, or AI probability simulation was run; those belong to the parent completion pass.

## Remaining route risks

- The tree is semantically complete but not validator-clean; visual readability and connector acceptance remain unresolved until the four clusters are reflowed together.
- Shared-focus imports resolve in the main source inventory, but live country/package admission is not proven by this source-level audit.
- Static localisation, icon, reward, and AI coverage does not substitute for prose review, route-choice balance, or runtime behavior.

## Parent handoff

Treat this as a no-patch blocker plan. The next implementer should reflow the four clusters in order, preserve all existing IDs, prerequisites, mutual exclusions, rewards, icons, localisation keys, AI weights, and CAT additive/full-framework boundaries, then rerun MCP inspect/render after each coherent tranche.

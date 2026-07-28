# Event 006 shared-focus geometry reflow decision - 2026-07-28

## Decision

No source patch is safe in this bounded pass. `common/national_focus/006_independence_wave_focus.txt` remains unchanged because the 14 MCP blockers are coupled across four lanes, and the previous coordinate-only candidate (`f8ca54d24`) increased global connector crossings from 49 to 60 and long connectors from 27 to 35 even though it reduced node intersections from 18 to 8. The candidate was reverted before this audit. A safe fix requires a coordinated reflow with inspect/render review after each coherent tranche.

## Scope and changed files

| Surface | Result |
| --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` | Not changed; all focus IDs, prerequisites, rewards, icons, localisation references, and AI weights remain intact. |
| `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` | Read-only only; not changed. |
| Localisation and Event 006 `.gfx` files | Read-only only; not changed. |
| Changed focus IDs | None. |
| New implementation | None; this file is the blocker/reflow handoff. |

## Route coverage table

| Required route or lane | Current source evidence | Coverage |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration`, `independence_wave_name_provisional_authority`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, `independence_wave_establish_permanent_ministries`, `independence_wave_restore_regional_communications`, `independence_wave_integrate_provinces_and_councils`, and `independence_wave_complete_founding_settlement` (`common/national_focus/006_independence_wave_focus.txt:66-219`). | Present. |
| Internal power and government settlements | `independence_wave_map_internal_power_centers` and the constitutional, popular-council, traditional, emergency-military, guarantor/client, radical-sovereignty, and AJX neutral-commission branches (`:225`, `:823-1260`). | Present; all seven route families and route locks are wired. |
| Economy and administration | `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury` (`:285-381`). | Present. |
| Army, security, and professional defence | `independence_wave_integrate_militia_commands` through `independence_wave_found_professional_defense_institution` (`:446-658`). | Present; five military choice pairs use one-of-each OR prerequisite blocks and mutual exclusions. |
| Diplomacy, recognition, and patrons | `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service` (`:676-798`). | Present. |
| Former-host, borders, and regional expansion | `independence_wave_define_former_host_policy` and its five policy families, followed by `independence_wave_survey_regional_ambition` and regional integration (`:1279-1515`). | Present. |
| Network, league, formable, and high-chaos | Fellow-state/network chain, league proposals, formable preparation and FORM-03 overlay, high-chaos chain, and `independence_wave_secure_durable_sovereignty` (`:1534-1956`, `:3130`). | Present. |
| Country/package overlays and shared roots | SCO, WLS, AJX, BRI, AFX, AGX, RHI, BAY, ARX, ASX overlays (`:1976-3111`) plus imported IW-093/IW-098 shared roots. | Present in source; live package admission remains parent-owned. |

No route family, focus identifier, prerequisite branch, or shared-root link was found missing in this geometry pass.

## MCP geometry evidence

`hoi4.focus_inspect` on tree `independence_wave_focus_tree` and `common/national_focus/006_independence_wave_focus.txt` returned `FOCUS_INSPECTED` with `validation.passed = false`. Current layout hash is `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`. Metrics are 184 regular focuses, 223 connectors, 49 crossings, 18 node intersections, 27 long connectors, bounds `x=1..101`, `y=0..19`, maximum horizontal span 80, maximum vertical span 6, total horizontal span 1172, and maximum Manhattan span 81. MCP reported no movable endpoint IDs for the unsatisfied diagnostics.

Latest inspect artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/28aca58d7385e2469d19957ddd849c3b772920b8bb4f15e0fcf227fade18f4c5/255136fe66cd53150479bf9fc5f35207912cf7182592302fcb6801b19a55e000/focus-inspect.740a53ca1ef6de81.json`

Latest render artifacts (same hash and blockers):

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d443f6d5492b2059ae921ee2de3968033a9efdbfe5daf80d9830b702fed20061/eb7bbe876e2c967c25fe2ac5ddb00e7c94bed5ce2d1a9b63ecb4c1604f60c109/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11c1c32334716d360aed8105602ef180f5f6e359d9b94dbadef434508ac4f5b7/8933970a852ac5fe8e9e29f76e343ebc0aa8bca5742bf95a259e86ae432bea43/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20b450c4fde493c76a1f5e6f93acc68fb5e1dbc7b70f163deed4f2f4124df60e/31260e9615fd6381dee156ceb30c2f233101ab080e703845481582c5663c7f7e/independence_wave_focus_tree.focus.json`
- Source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/62e25f36effa7c02058c9b4e0aa630a4e97a19c62e745fd88fb8e64bfa344a18/4ba2eaba1a6d8b2fb75f8197b22a06b6decb7dc1ae03c4afbcd6ddfc9ffb55b0/independence_wave_focus_tree.focus.source-map.json`
- Plan JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a7fab41df3ee3dc3bdf648be35f43eccb24f51ed65bf2b48f3d8943cc2c9cd6a/21701322e6ba52161080c1aa815674157ef86c062f4a680ac963efc8d6903215/independence_wave_focus_tree.focus.plan.json`

## Blocking clusters and minimal next action

1. **Opening economy/state handoff (`:284-301`).** `independence_wave_bind_the_first_oath -> independence_wave_integrate_provinces_and_councils` crosses `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue`. Reflow the oath/inventory parent row and integration/revenue child row together, then inspect downstream edges.
2. **Founding-settlement fan (`:323-340`).** Each of `independence_wave_complete_founding_settlement -> independence_wave_ajx_appoint_neutral_commission_focus`, `... -> independence_wave_define_former_host_policy`, and `... -> independence_wave_recognize_fellow_new_states` crosses `independence_wave_secure_food_and_fuel -> independence_wave_build_regional_transport_authority`. Move the fan and economy lane together.
3. **Depot/recall fan (`:446-465`).** The same three founding fan edges cross `independence_wave_secure_national_depots -> independence_wave_recall_and_vet_officers`. Reflow depot/recall with `independence_wave_integrate_militia_commands`, the founding fan, and the economy lane.
4. **Professional-defence merge (`:506-529`).** Six crossings involve `independence_wave_adopt_military_archetype_program`, `independence_wave_adopt_border_defense`, `independence_wave_adopt_reclamation_doctrine`, `independence_wave_standardize_with_league`, `independence_wave_preserve_independent_command`, and the two capstone edges from `independence_wave_confirm_civilian_control`/`independence_wave_grant_military_autonomy` (plus `independence_wave_build_professional_core`) to `independence_wave_found_professional_defense_institution`. Treat rows `y=6..12` as one monotone branch layout, preserving all five OR groups and pairwise mutual exclusions.

After these four clusters, review the nonblocking long/through-node edges: `complete_founding_settlement -> map_internal_power_centers` (17 columns), `inventory_the_state -> establish_emergency_revenue` (12), `bind_the_first_oath -> integrate_militia_commands` (14), and the founding fan over `independence_wave_activate_package_economic_program`/`independence_wave_adopt_military_archetype_program`.

## Missing or simplified content

No required route family, focus ID, icon reference, localisation key, completion reward block, or focus AI block was missing. No fallback route or simplified replacement was introduced. The material unresolved simplification is validator-clean geometry: the baseline still has 14 MCP blocking diagnostics, and isolated coordinate shifts are unsafe.

## Icon coverage table

| Surface | Result |
| --- | --- |
| Main and IW-093/IW-098 focus/shared-focus blocks | 240 unique blocks parsed; 184 regular focuses rendered and 56 shared-focus blocks resolved. |
| Used icon IDs | 87 unique IDs. |
| Sprite definitions | Every used icon has a regular sprite and matching `_shine` sprite in the Event 006/imported package `.gfx` files. |
| Missing/repeated icon finding | None. Reuse is intentional within established package/lane icon families. |

## Localisation and reward mismatch list

- No missing title or `_desc` key was found for the 240 parsed focus/shared-focus IDs.
- Every parsed block has `completion_reward` and `ai_will_do`.
- No direct focus-name/reward contradiction was found in the bounded source scan.
- No localisation, reward, prerequisite, mutual-exclusion, or icon patch is justified while the four geometry clusters remain coupled.

## AI behavior gaps

Every parsed focus/shared-focus block has an `ai_will_do` block. Government, military, patron, former-host, league, high-chaos, and package overlays retain route-aware gates/weights, and the tree header remains gated by `is_independence_wave_active_country = yes` and `independence_wave_full_focus_framework`. Scenario-level selection probabilities and route outcomes were not re-simulated here; this is a parent-owned runtime validation item, not a newly discovered missing AI block.

## Validation and skipped checks

- Read the required offline Paradox wiki pages, relevant vanilla national-focus documentation, shared-focus precedents, and all named Chaos Redux skills before auditing.
- Ran `hoi4.focus_inspect` and recorded the failed validation, layout hash, metrics, and 14 blocker diagnostics above.
- Ran `hoi4.focus_render`; HTML, SVG, and JSON artifacts reproduce the same blockers and hash.
- Ran read-only source scans for IDs, prerequisites, title/description localisation, icon/shine coverage, rewards, AI blocks, and duplicate identifiers.
- Confirmed the focus source is clean after the earlier candidate reversion; no gameplay, localisation, icon, or source file was changed by this handoff.

Skipped `hoi4.focus_rewrite` because this is not a safe local rewrite; it would mutate a broad coupled geometry surface. Skipped raster because structural inspect/render evidence is sufficient. No game launch, save runtime test, package-admission proof, or AI probability simulation was run; those belong to the parent completion pass.

## Remaining route risks

- The tree is semantically complete but not validator-clean; visual readability and connector acceptance remain unresolved until a coordinated reflow is tested.
- Shared-focus imports resolve in MCP, but live country/package admission is not proven here.
- Static localisation/icon/reward/AI coverage does not substitute for prose review, route-choice balance, or runtime behavior.

## Parent handoff

Treat this as a no-patch blocker plan. The next implementer should reflow the four clusters in order, run `hoi4.focus_inspect` and `hoi4.focus_render` after each coherent tranche, and reject any candidate that reduces one local crossing while increasing global crossings, node intersections, or long connectors. Preserve all existing IDs, prerequisites, mutual exclusions, rewards, icons, localisation keys, and AI weights.

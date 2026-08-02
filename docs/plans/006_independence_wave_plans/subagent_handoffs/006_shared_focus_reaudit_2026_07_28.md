# Event 006 shared focus re-audit - 2026-07-28

> **Superseded for current geometry routing (2026-08-03):** This dated re-audit preserves the restored pre-reflow layout and its 14-diagnostic hold. Use `006_focus_geometry_reflow_parent_2026_08_02.md` for the current source-clean geometry receipt and retain this body only as historical traceability.

## Status and scope

This is a read-only re-audit of the restored Event 006 shared focus framework. No gameplay, localisation, icon, plan, or source file was patched, and no file was staged or committed. The current geometry remains blocked by the same coupled layout diagnostics recorded in the 2026-07-26 geometry handoff.

Audited source surfaces were `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, the matching focus localisation under `localisation/english/006_independence_wave_focus_l_english.yml` and the wider `localisation` tree, and the Event 006 focus icon `.gfx` files. The review used the current source-of-truth map, the accepted focus architecture and lane-map specs, the AI strategy matrix, the 2026-07-26 geometry handoff, the offline HOI4 wiki and vanilla documentation, and vanilla shared-focus examples.

## Route coverage

| Required route or lane | Current implementation evidence | Coverage |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration`, `independence_wave_name_provisional_authority`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, `independence_wave_establish_permanent_ministries`, `independence_wave_restore_regional_communications`, `independence_wave_integrate_provinces_and_councils`, and `independence_wave_complete_founding_settlement` in `common/national_focus/006_independence_wave_focus.txt:66-219`. | Present. |
| Internal power and government settlements | `independence_wave_map_internal_power_centers` at `:225`, constitutional route at `:823-889`, popular-council route at `:903-944`, traditional route at `:958-1012`, emergency-military route at `:1026-1067`, guarantor/client route at `:1081-1136`, radical sovereignty route at `:1150-1203`, and the AJX municipal commission route at `:1219-1260`. | Present. Six main families plus the seventh AJX neutral-commission route are wired with route gates and pairwise route locks. |
| Economy and administration | `independence_wave_establish_emergency_revenue`, `independence_wave_secure_food_and_fuel`, `independence_wave_build_regional_transport_authority`, `independence_wave_establish_customs_service`, `independence_wave_activate_package_economic_program`, and `independence_wave_create_independent_treasury` at `:285-381`. | Present. |
| Army, security, and professional defence | `independence_wave_integrate_militia_commands`, `independence_wave_secure_national_depots`, `independence_wave_recall_and_vet_officers`, `independence_wave_form_border_guard`, `independence_wave_adopt_military_archetype_program`, paired military choices at `:532-658`, and `independence_wave_found_professional_defense_institution` at `:507`. | Present. The five military choice pairs use OR blocks for one-of-each semantics and mutual exclusions. |
| Diplomacy, recognition, and patrons | `independence_wave_establish_foreign_office`, `independence_wave_send_first_missions`, `independence_wave_seek_neighbor_recognition`, `independence_wave_declare_entrenched_neutrality`, `independence_wave_balance_the_first_patrons`, `independence_wave_become_treaty_backed_state`, and `independence_wave_focus_build_permanent_foreign_service` at `:676-798`. | Present. |
| Former-host, borders, and regional expansion | `independence_wave_define_former_host_policy` and the negotiated separation, guarded frontier, association, reclamation, and host-collapse branches at `:1279-1444`, followed by `independence_wave_survey_regional_ambition` and its regional congress/integration focuses at `:1461-1515`. | Present. The five former-host policy families converge into the regional ambition lane. |
| Network, league, formable, and high-chaos routes | Fellow-state recognition and network-to-league chain at `:1534-1630`, five league proposals at `:1643-1699`, formable preparation at `:1718-1758`, FORM-03 low-country overlay at `:1775-1875`, hidden high-chaos chain `independence_wave_sponsor_further_ruptures` through `independence_wave_rewrite_charter_of_borders` at `:1916-1956`, and final `independence_wave_secure_durable_sovereignty` at `:3130`. | Present. |
| Country/package overlays | Package-gated overlays for SCO, WLS, AJX, BRI, AFX, AGX, RHI, BAY, ARX, and ASX are in `006_independence_wave_focus.txt:1976-3111`; imported shared roots and IW-093/IW-098 shared focuses are in `006_independence_wave_iw093_iw098_focus.txt` and the explicit imports at the top of the main tree. | Present in source. AGX eight-focus package wiring has a separate PASS handoff; live runtime admission is still conditional and is not claimed here. |

The route graph therefore covers the accepted lane map without a missing branch family found in this bounded pass. The unresolved issue is spatial readability and validator acceptance, not a missing route or disconnected source identifier.

## Current MCP geometry evidence

`hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt` with tree `independence_wave_focus_tree` returned `FOCUS_INSPECTED` but `validation.passed = false` with 14 blocking focus diagnostics. The current layout hash is `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`. The rendered tree reports 184 regular focuses, 223 connectors, 49 crossings, 18 node intersections, 27 long connectors, bounds `x=1..101`, `y=0..19`, maximum horizontal span 80, maximum vertical span 6, total horizontal span 1172, and maximum Manhattan span 81.

The inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/393e04e947f4fc661c2f40dc9bf7f93b58d24674af5b3a62d334d4e52a9cb72e/4b9aaacb582816a655e3180ab64a5ab92a63b8c4b6f043ffdc1f523412f18e69/focus-inspect.85eee275dfa03e65.json`.

The render artifacts are:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d443f6d5492b2059ae921ee2de3968033a9efdbfe5daf80d9830b702fed20061/5280b9022dd0cdba4ef41c1828b644f30d4f17cdcd3196bf447c15fdee271b00/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/11c1c32334716d360aed8105602ef180f5f6e359d9b94dbadef434508ac4f5b7/d6d5110be2a2119c2fa46bde64325429ae7213075cee669b5d71232689d1445a/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/20b450c4fde493c76a1f5e6f93acc68fb5e1dbc7b70f163deed4f2f4124df60e/d91131f6c400d469da96464b7ec636fafa1645b41d6aa7778776c9b48efdcdd0/independence_wave_focus_tree.focus.json`

The render confirms the same 14 blockers and the same layout hash. MCP reported `movableFocusIds=[]` for the unsatisfied diagnostics, so an isolated endpoint shift is not a safe fix.

### Blocking diagnostics, in priority order

1. `FOCUS_AVOIDABLE_CONNECTOR_CROSSING` and the paired `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` at `006_independence_wave_focus.txt:284-301`: `independence_wave_bind_the_first_oath -> independence_wave_integrate_provinces_and_councils` crosses `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue`.
2. Three `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` diagnostics at `:323-340`: `independence_wave_complete_founding_settlement` to each of `independence_wave_ajx_appoint_neutral_commission_focus`, `independence_wave_define_former_host_policy`, and `independence_wave_recognize_fellow_new_states` crosses `independence_wave_secure_food_and_fuel -> independence_wave_build_regional_transport_authority`.
3. Three `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` diagnostics at `:446-465`: the same three founding-settlement fan edges cross `independence_wave_secure_national_depots -> independence_wave_recall_and_vet_officers`.
4. Six `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED` diagnostics at `:506-529` in the professional-defence merge: `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_border_defense` crosses each of `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution` and `independence_wave_grant_military_autonomy -> independence_wave_found_professional_defense_institution`; `...adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine` crosses both of those same capstone edges; `...adopt_military_archetype_program -> independence_wave_preserve_independent_command` crosses `independence_wave_build_professional_core -> independence_wave_found_professional_defense_institution`; and `...adopt_military_archetype_program -> independence_wave_standardize_with_league` crosses `independence_wave_confirm_civilian_control -> independence_wave_found_professional_defense_institution`.

Nonblocking layout findings are the 17-column connector `independence_wave_complete_founding_settlement -> independence_wave_map_internal_power_centers`, the 12-column connector `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue`, the 14-column connector `independence_wave_bind_the_first_oath -> independence_wave_integrate_militia_commands`, and through-node crossings from the founding settlement fan to `independence_wave_survey_regional_ambition` over `independence_wave_activate_package_economic_program` and `independence_wave_adopt_military_archetype_program`. These should be reviewed after the four blocking clusters, not treated as source or parser errors.

## Icon coverage

| Surface | Audit result | Evidence |
| --- | --- | --- |
| Focus/shared-focus blocks | 240 unique IDs across the main file and IW-093/IW-098 shared-focus file, with 184 regular focuses in the rendered tree and 56 shared-focus blocks. | Read-only parser over both source files. |
| Icon references | 87 unique icon IDs used by the 240 blocks. | Read-only parser. |
| Sprite definitions | Every used icon has a regular sprite and matching `_shine` sprite in the Event 006 or imported package `.gfx` files. | `interface/006_independence_wave.gfx`, `006_independence_wave_form03.gfx`, `006_independence_wave_form05.gfx`, `006_independence_wave_form48.gfx`, `006_independence_wave_iw043_iw058_focus_icons.gfx`, `006_independence_wave_mediterranean_assets.gfx`, `006_independence_wave_rhineland_bavaria_assets.gfx`, and `006_independence_wave_wallonia_frisia_assets.gfx`, plus the imported Pacific package definitions. |
| Missing or repeated focus icon finding | None found in this pass. | No undefined references or missing shine pairs were returned. Repetition was not judged a defect where a package or lane intentionally reuses an established icon family. |

## Localisation and reward mismatch list

- No missing focus title or `_desc` key was found for any of the 240 parsed focus/shared-focus IDs in the wider localisation tree.
- Every parsed focus/shared-focus block contains `completion_reward` and `ai_will_do`; no empty reward or missing AI block was found in this static pass.
- No direct focus-name-to-reward contradiction was identified from the bounded source scan. A full prose-quality review of every description and every effect payload was not repeated here, so this is not a claim that all narrative wording is perfect.
- No localisation, reward, icon, prerequisite, or mutual-exclusion patch was made because the current findings do not justify a narrow source change while the coupled layout remains unresolved.

## AI behavior gaps

The source scan found an `ai_will_do` block on every parsed focus/shared-focus block. Government, military, patron, former-host, league, high-chaos, and package overlays contain route-aware gates or weighting patterns, and the tree-level score is gated by `is_independence_wave_active_country = yes` and `independence_wave_full_focus_framework` in the tree header.

The accepted AI matrix is therefore represented in source, but scenario-level selection probabilities and route outcomes were not re-simulated in this geometry pass. No AI weights were changed. Runtime AI behavior remains an unresolved validation item for the parent completion audit, not a newly discovered missing block.

## Missing or simplified content

No required route family, focus ID, icon reference, localisation key, completion reward block, or focus AI block was missing in this pass. No fallback route or simplified replacement was introduced by this audit.

The one material unresolved simplification is the restored geometry baseline: the tree still has 14 MCP blocking layout diagnostics. Earlier isolated shifts were reverted because they worsened the coupled metrics; the current diagnostics explicitly provide no movable endpoint IDs. Clearing them requires a coordinated reflow of several lanes and fan-in/fan-out relationships, which is outside this bounded audit and must preserve the existing prerequisites, mutual exclusions, rewards, icons, localisation, and AI weights.

## Validation performed

- Consulted the required offline Paradox wiki focus, trigger, effect, modifier, localisation, scope, on-action, event, decision, idea, and AI references and the relevant vanilla national-focus documentation and shared-focus precedents.
- Ran `hoi4.focus_inspect` on the current tree and recorded the failed validation, layout hash, metrics, artifact, and exact 14 blocking diagnostics above.
- Ran `hoi4.focus_render` on the current tree and recorded HTML, SVG, and JSON artifacts; render reproduced the same blockers and hash.
- Ran a read-only source parser across the two focus source files and localisation/GFX trees for unique IDs, title/description coverage, icon definitions, shine sprites, reward blocks, AI blocks, and duplicate IDs.
- Confirmed no source or localisation changes were made during this re-audit.

## Skipped meaningful validation

`hoi4.focus_rewrite` was not used because the remaining issues are a broad coupled geometry problem rather than a safe local rewrite. `hoi4.focus_raster` was not needed because the structural inspect/render evidence already identifies the blocker clusters. No game launch, save-file runtime test, live country-admission proof, or probability simulation was performed; those belong to the parent's final validation surface.

## Recommended parent follow-up

1. Reflow the four blocking geometry clusters as a coordinated layout change, beginning with the opening economy/state crossing, then the founding-settlement fan, the depot fan, and the professional-defence merge.
2. Preserve all listed focus IDs, prerequisite semantics, mutual exclusions, completion rewards, icon IDs, localisation keys, and route-aware AI while reflowing.
3. Re-run `hoi4.focus_inspect` and `hoi4.focus_render` after each coherent reflow tranche and retain a before/after artifact comparison. Do not accept a local improvement that increases node intersections, crossings, or long-connector metrics elsewhere.
4. After geometry is clean, perform the parent-owned runtime admission and AI scenario checks, then run the separate focus-tree completion audit.

No separate improvement-loop plan was written because this tree is not shallow or missing a route family; the unresolved need is a coupled layout reflow. If that reflow exposes a new design gap, route it through the existing Event 006 improvement-loop plan rather than expanding this handoff.

## Remaining risks

- The rendered tree is structurally resolved enough for source inspection but not validator-clean, so the visual readability of the crossing clusters remains uncertain until a coordinated reflow is tested.
- The MCP inline inventory was truncated to 64 of 68 paths in both inspect/render responses; this did not produce a missing-reference diagnostic, but the parent should retain the linked artifacts as the authoritative evidence.
- Shared-focus imports resolved in the current inspect, but live country loading and package admission were not proven here.
- Static localisation/icon/reward/AI coverage does not substitute for prose review, route-choice balance, or in-game runtime behavior.

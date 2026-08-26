# Event 006 focus surface scan — 2026-08-26

Date: 2026-08-26

Owner: `/root/event6_focus_surface_scan`

Disposition: read-only audit; no gameplay, focus, localisation, icon, or AI source patch was justified.

## Scope and authority

This audit covers the accepted Part 4 focus architecture, the lane diagram, the current shared focus source, package overlays, package admission gates, and the latest available MCP evidence.

Primary design references are [006_independence_wave_spec_part_4_focus_tree_architecture.md](../../../specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md) and [006_focus_tree_lane_map.md](../../../specs/006_independence_wave_specs/diagrams/006_focus_tree_lane_map.md).

Current authority and admission boundaries are recorded in [006_source_of_truth_map.md](../006_source_of_truth_map.md), especially the 2026-08-26 MCP refresh and the 32-attested/40-adapter/161-unattested package boundary.

## MCP evidence

The required root-tree inspect completed successfully for `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree`.

- Status: `FOCUS_INSPECTED`.
- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Revision: `56ae3826618bdd9546c0024a330b8e8de695f7ddea36164f70082b7dd266c094`.
- Artifact: [focus-inspect.56ae3826618bdd95.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97b585dd45a20dcd85f9045f9b61e1a65ef479fb6bc8c625271cc93925550a69/70b013b9ea83aef8ed327d6eede218a8f9ed6ac959e60656efd5d7e332b74c67/focus-inspect.56ae3826618bdd95.json).
- MCP root surface: 184 focus nodes, 195 connectors, zero crossings, zero node intersections, zero long connectors, zero too-close pairs, and zero diagnostics.
- Layout bounds: x 1..121 and y 0..19; layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
- Validation passed; the only warning is the unrelated vanilla `game:common/continuous_focus/generic.txt` `continuous_restrict_freedom_desc` inventory warning.

The required root-tree render completed successfully.

- Status: `FOCUS_RENDERED`.
- HTML: [independence_wave_focus_tree.focus.html](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1387f679ebb46e99df9e4385f2d934232a98fdff7c3d1ee0a817d3b318cc0f0c/b42b7c0071a8698d866b3c08bb9b4a7ef3d4a58aad1e1fd564d35b0fd83a893e/independence_wave_focus_tree.focus.html).
- SVG: [independence_wave_focus_tree.focus.svg](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/790ac83c6f2cdb9816133b30e7a650f0e74f3823cf45efd0753fa9182ec87279/c72a975b5e3b2df66887974d08614c2abca3f459c4c41591776d9c31594c40c3/independence_wave_focus_tree.focus.svg).
- JSON: [independence_wave_focus_tree.focus.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4320385aee3822cf11b980888ec9d2d137de498426c8b6f8e966fbe233d5767a/7d6713d52fe3fc0b1ea92a5d3b83b2812be09044b2d8058d4406a6aa720a5296/independence_wave_focus_tree.focus.json).
- Source map: [independence_wave_focus_tree.focus.source-map.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b5ae8c4b5c523e1ac20d8e279d46be9f755dcacb54e4abeaf9478f18adbc9c3/60f77078a196c8f1b9adb2da487e7f8c1736f3f62eb24bd53e90368e139dbd7d/independence_wave_focus_tree.focus.source-map.json).
- Plan: [independence_wave_focus_tree.focus.plan.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b38c755b5d414f9ee053b0bc218fe9b7be3b4913e57eedcd5f6bd4d2f19da00/0651245e1327fb0ceeff2d53cd9b0ae75dc9f938395d5b016edef70858d67401/independence_wave_focus_tree.focus.plan.json).
- Render dimensions: 21424 x 2440; layout hash matches inspect; validation passed with the same unrelated vanilla warning.

The required overlay inspect/render calls were also run for both shared-focus-only source files.

| Surface | Inspect | Render | Interpretation |
| --- | --- | --- | --- |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` | `FOCUS_TREE_NOT_FOUND`: “The selected source contains no national focus tree” | `FOCUS_TREE_NOT_FOUND`: “The source file contains no focus tree” | Expected source shape; file contains `shared_focus` definitions imported by the root/carrier tree. |
| `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` | `FOCUS_TREE_NOT_FOUND`: “The selected source contains no national focus tree” | `FOCUS_TREE_NOT_FOUND`: “The source file contains no focus tree” | Expected source shape; file contains `shared_focus` definitions imported by the root/carrier tree. |

The two overlay failures are a tool-surface/transport limitation, not missing routes or malformed source. Root imports are in `common/national_focus/006_independence_wave_focus.txt` at lines 60-87, and the carrier imports are in `common/national_focus/iceland.txt` and `common/national_focus/austro_hungarian_releasable_shared.txt`.

## Route coverage

| Part 4 lane or route family | Current implementation | Evidence |
| --- | --- | --- |
| Survival/state formation | Covered by the opening trunk from `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement`. | `common/national_focus/006_independence_wave_focus.txt:103-300`; `can_complete_independence_wave_survival_capstone`. |
| Optional internal power struggle | Covered by `independence_wave_map_internal_power_centers` and its three power-center/compromise outcomes. | `common/national_focus/006_independence_wave_focus.txt:305-363`; `can_open_independence_wave_internal_power_struggle`. |
| Economy/administration | Covered by the six-node lane from `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury`. | `common/national_focus/006_independence_wave_focus.txt:370-489`; varied administration, supply, transport, customs, program, treasury, technology, and idea effects. |
| Army/security | Covered by the five-node trunk from `independence_wave_integrate_militia_commands` through `independence_wave_found_professional_defense_institution`, followed by the mutually exclusive row-8 choices. | `common/national_focus/006_independence_wave_focus.txt:496-794`; route choices include civilian control, military autonomy, mass reserve, professional core, arsenals, foreign arms, border defense, reclamation doctrine, league standardization, and independent command. |
| Diplomacy/recognition/patrons | Covered by `independence_wave_establish_foreign_office`, first missions, recognition, neutrality, patron balancing, treaty-backed state, and permanent foreign service. | `common/national_focus/006_independence_wave_focus.txt:805-946`; diplomacy and patron predicates in `common/scripted_triggers/006_independence_wave_focus_triggers.txt`. |
| Constitutional republic | Covered by `independence_wave_prepare_first_assembly` through `independence_wave_consolidate_constitutional_state`. | `common/national_focus/006_independence_wave_focus.txt:957-1040`; route lock and capstone included in `has_completed_independence_wave_government_settlement`. |
| Popular council/commonwealth | Covered by `independence_wave_organize_popular_councils`, cooperative administration, public guard, and council commonwealth. | `common/national_focus/006_independence_wave_focus.txt:1042-1100`; `can_lock_independence_wave_popular_council_route`. |
| Traditional restoration | Covered by traditional confirmation, legitimate authority, court/ministries, regional notables, and restored crown. | `common/national_focus/006_independence_wave_focus.txt:1103-1170`; `can_lock_independence_wave_traditional_authority_route`. |
| Emergency military | Covered by emergency command, militia subordination, military economy, and emergency state. | `common/national_focus/006_independence_wave_focus.txt:1173-1227`; emergency security/instability gates. |
| Patron client | Covered by guarantor talks, protected future, advisers/credits, loyal guarantor, and bargaining client. | `common/national_focus/006_independence_wave_focus.txt:1230-1298`; patron-count and client-lock predicates. |
| Radical sovereignty/high-chaos route | Covered by inherited-border rejection, founding myth, aligned movements, radical sovereignty, and the later high-chaos lane. | `common/national_focus/006_independence_wave_focus.txt:1301-1369` and `2097-2155`; `can_open_independence_wave_high_chaos_lane`. |
| IW-010 neutral commission | Covered by the package-gated AJX neutral commission branch and capstone. | `common/national_focus/006_independence_wave_focus.txt:1374-1430`; explicit `allow_branch` and `can_lock_independence_wave_ajx_neutral_commission_route`. |
| Former-host policy | Covered by negotiated separation, guarded frontier, association, reclamation, and collapsed-host successor ledger. | `common/national_focus/006_independence_wave_focus.txt:1439-1625`; each living-host root excludes the other three, while collapse is a separate no-living-host path. |
| Regional ambition | Covered by survey, local committees, congress, postwar integration authority, and signature extension. | `common/national_focus/006_independence_wave_focus.txt:1629-1705`; `can_open_independence_wave_regional_ambition`. |
| Network/league | Covered by recognition, civil-service exchange, aid corridor, arbitration, charter, founding members, congress, and mutually exclusive league proposals. | `common/national_focus/006_independence_wave_focus.txt:1710-1893`; network and league predicates in `006_independence_wave_focus_triggers.txt`. |
| Formable preparation | Covered by regional identity, union congress, formation terms, integration commission, and FORM-03 preparation branch. | `common/national_focus/006_independence_wave_focus.txt:1899-2092`; actual discovery/claims/formation remain decision-owned as specified. |
| Country/package overlays | Covered as shared-focus modules and imported carrier overlays, including IW043/IW058, IW093/IW098, ICE/AHR, COR/CAT, RHI/BAY, Mediterranean, and Pacific package consumers. | Root `shared_focus` blocks at `006_independence_wave_focus.txt:3398-4239`; module files; carrier imports and package triggers. |

No accepted Part 4 route family is absent from the current architecture. The single shared tree with gated overlays is the accepted design, not a fallback or a simplification.

## Missing or simplified content

- No safe focus source defect was found in the requested surface.
- Package admission remains intentionally partial and is a separate runtime boundary: 32 packages are content-attested, 40 have runtime adapters, 29 reservation groups are compatible, and 161 selectable rows remain unattested.
- The eight adapter-only rows remain fail-closed and must not be promoted by a focus-only patch: IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.
- IW043/IW058 and IW093/IW098 visual module MCP evidence cannot be obtained directly because those files intentionally contain no `focus_tree` wrapper. The root inspect/render and carrier source imports provide the valid current surface evidence.
- The MCP root inventory reports 184 materialized root focus nodes; source inventory across the root and shared modules is 184 direct `focus` definitions plus 43 root shared definitions, 48 IW043/IW058 shared definitions, and 43 IW093/IW098 shared definitions, for 318 unique focus/shared-focus definitions.
- No new route, formable chain, or package admission was invented or added.

## IW-095 package-local disposition

IW-095 Dahomey is needed as a future package-local first-footprint implementation, but it is not a safe local focus patch in this audit.

- The queued first-footprint addendum names IW-095 as the first implementation handoff and requires package-local identity, setup, mission, serialized projects, settlements, network/formable connection, assets, AI, cleanup, and audits before central admission.
- Current registry plumbing only publishes `iw_095`: `can_plan_independence_wave_package_iw_095` is in `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:736-743`, and the loader is in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1549-1562`.
- The generic DAH candidate gate still requires `independence_wave_package_content_ready`, but no DAH package source sets that flag; this correctly keeps the row fail-closed.
- The current focus callback lists contain no `DAH`, `iw095`, or `independence_wave_iw095_focus_*` call, and the current dispatch surfaces contain no IW-095 runtime adapter or content attestation. Adding one callback to the shared tree would therefore expose an incomplete package and bypass the accepted admission boundary.
- The dedicated package audit records the absent callback, package docket, assets, AI, origin-safe adapter, and central admission proof in [006_iw095_package_audit_2026-08-26.md](006_iw095_package_audit_2026-08-26.md).

The parent should keep IW-095 unadmitted, implement its package-local surfaces under the queued addendum, and only then add the central adapter/attestation and shared-focus callbacks in one reviewed admission tranche.

## Icon coverage

| Surface | Coverage | Result |
| --- | --- | --- |
| All root and shared focus definitions | 318/318 definitions have an icon reference. | Pass. |
| Unique Event 006 icon IDs | 121 unique IDs are referenced. | All have a normal sprite and a corresponding `_shine` sprite in the Event 006 GFX surface. |
| Root and shared GFX textures | All referenced texture files resolve. | `missingTextureFiles=0`. |
| IW043/IW058 package overlay family | All 48 shared definitions have resolved icon/shine pairs. | Pass; direct module render is unavailable only because there is no standalone tree. |
| IW093/IW098 package overlay family | All 43 shared definitions have resolved icon/shine pairs. | Pass; direct module render is unavailable only because there is no standalone tree. |
| Carrier/Pacific/CAT/COR/RHI/BAY/Mediterranean families | Definitions and icon references resolve through the root/shared source. | Pass in static source/GFX audit. |

Relevant GFX surfaces are `interface/006_independence_wave.gfx`, `interface/006_independence_wave_iw093_iw098_focus.gfx`, and `interface/006_independence_wave_small_assets.gfx`.

## Localisation and reward mismatch list

- Focus title and description coverage is complete for the 318 source definitions: `missingTitles=0` and `missingDescs=0` across `localisation/english/006_independence_wave*.yml`.
- Custom focus tooltip references resolve: `tooltipRefs=318` and `missingTooltips=0`.
- The 37 Event 006 English localisation files are UTF-8 with BOM.
- Reward helper references resolve: 331 assignment references were checked against `common/scripted_effects/*.txt`, with `missingEffectDefs=0`.
- Reward content is not a flat generic PP/stability chain. The static helper inventory includes administration, diplomatic steps, public settlement, security reform, stabilization, ambition, network cooperation, durable state, radicalization, league revisionism, client development, founding steps, and distinct league equality/development/defense bundles, plus package-specific effects and flags.
- No sampled focus name/reward contradiction was identified. Names such as the treasury, customs, border guard, foreign office, host policy, league, formable preparation, and high-chaos branches match their visible reward/effect families.
- No missing decision, mission, formable, idea, claim, war-goal, event, or existing unlock hook was found in the focus-specific surface. Formable execution remains in the existing decision hooks by design.

## AI behavior gaps

- All 318 source focus/shared-focus definitions have an `ai_will_do` block, icon, `available`, `completion_reward`, search filters, and coordinates.
- Root-tree AI uses the framework/active-country gate and the shared Event 006 focus AI constants in `common/national_focus/006_independence_wave_focus.txt` at the tree block near lines 37-39.
- Route-specific modifiers and package archetype/leader/host/patron/league/high-chaos signals are present in the focus blocks and supporting scripted triggers.
- Static AI presence and route wiring are therefore covered, but no fresh quantitative balance claim is made here.
- The required `chaosx_ai_probability_auditor` route is not exposed in this task context, and the current source-of-truth map records the typed probability route as blocked by `Transport closed`. No AI weight patch was made without the mandatory baseline/compare evidence.

## Prerequisite, bypass, and mutual-exclusion checks

- All 275 extracted focus references resolve to a known definition; no missing prerequisite, bypass, or relative-position target was found.
- Separate prerequisite blocks were preserved where Part 4 requires AND semantics, including `independence_wave_establish_permanent_ministries`, `independence_wave_integrate_provinces_and_councils`, and `independence_wave_complete_founding_settlement`.
- The 55 parsed mutual-exclusion owners have no asymmetric pairs. The four living-host roots explicitly exclude one another, and the government/league proposal choices retain their route locks.
- Package-gated branches use existing `allow_branch`/`available` predicates rather than bypassing admission, including the AJX neutral commission route and package-specific shared overlays.

## High-priority follow-up

1. Preserve the clean root geometry. The current MCP evidence is zero crossings, zero intersections, zero long connectors, and zero too-close pairs with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
2. Keep package admission fail-closed until the eight adapter-only rows receive complete content attestation and the central runtime admission list in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-200` is intentionally updated.
3. For future IW043/IW058 or IW093/IW098 visual evidence, inspect/render an imported carrier tree or a dedicated wrapper context; do not add a fake standalone tree solely to satisfy the MCP surface.
4. Restore the typed probability-auditor route before changing any focus AI weight or claiming balance improvement.

## Change record

- Changed gameplay files: none.
- Changed focus IDs: none.
- Changed localisation keys: none.
- Changed icon IDs: none.
- Route behavior before and after: unchanged; no patch was applied.
- The only new file is this dated audit handoff.

## Validation and skipped validation

Meaningful validation run:

- Fresh `hoi4.focus_inspect` and `hoi4.focus_render` on the root tree, with artifact links recorded above.
- Fresh inspect/render on both shared-focus-only modules, with the exact expected `FOCUS_TREE_NOT_FOUND` responses recorded above.
- Source inventory: 318 unique focus/shared-focus definitions, 318/318 `available`, `completion_reward`, `ai_will_do`, icon, search-filter, and coordinate surfaces.
- Reference inventory: 275 focus references with zero unresolved targets.
- Mutual-exclusion inventory: 55 owners with zero asymmetric pairs.
- Localisation inventory: 318 title/description pairs and 318 tooltip references with zero missing keys.
- Icon inventory: 121 unique IDs with normal/shine coverage and zero missing texture files.
- Reward helper inventory: 331 assignment references with zero missing scripted-effect definitions.

Skipped meaningful validation:

- No `hoi4.focus_rewrite` was run because no safe source patch existed.
- No `chaosx_ai_probability_auditor` baseline/compare was run because that required route is unavailable and the recorded typed probability transport is closed.
- No direct module raster/render evidence was claimed for the shared-focus-only files after their exact transport failure; the root/carrier architecture is the valid available evidence.
- No live game or save validation was run, per repository boundary; this handoff does not claim in-game behavior proof.

## Remaining route risks

- Runtime package admission remains partial and is the main execution risk, not a focus-tree geometry or localisation defect.
- Overlay-specific MCP evidence remains transport-limited until a supported carrier/wrapper surface is used.
- AI values have structural coverage but await a working probability-auditor route for scenario-specific balance evidence.
- Future parent merges should rerun root inspect/render and repeat the static route/mutex/icon/localisation checks before changing the closed tree surface.

No improvement plan was written because the accepted route architecture is present and no shallow or missing route family was established by this audit.

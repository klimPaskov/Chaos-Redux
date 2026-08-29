# Event 006 focus-tree audit current, 2026-08-29

## Scope and disposition

This read-only audit refreshes the Event 006 focus architecture against the current source, the accepted Part 4 focus specification, the generic-tree contract, and the latest current-source MCP receipts.

No gameplay, focus, localisation, icon, reward, AI, decision, mission, event, or carrier source was changed.

The focus surface is PASS for source coverage, route wiring, localisation and icon resolution, prerequisite references, mutual exclusions, and root-tree geometry.

The wider Event 006 release remains HOLD / PARTIAL because package admission, live runtime proof, and typed probability evidence remain separate gates.

## Current source inventory

| Source surface | Current content | Authority |
| --- | --- | --- |
| `common/national_focus/006_independence_wave_focus.txt` | 184 direct `focus` blocks, 43 full `shared_focus` blocks, and 27 main-tree `shared_focus = <id>` import roots | Main `independence_wave_focus_tree` declaration, regular lanes, package modules, carrier overlays, and merged Pacific blocks |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` | 48 shared-focus definitions | IW-043 Middle Volga and IW-058 Assyrian package modules |
| `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` | 43 shared-focus definitions | IW-093 Asante and IW-098 Sokoto package modules |
| Resolved Event 006 surface | 318 unique definitions and 345 raw entries when imports are counted | One `independence_wave_focus_tree`, not a set of country-specific Event 006 trees |

The standalone Pacific parser was removed by the 2026-08-26 source-layout merge, with its 20 shared-focus blocks retained under `# SOURCE: 006_independence_wave_pacific_focus.txt` at `common/national_focus/006_independence_wave_focus.txt:3880-4247`.

Current source hashes are `006_independence_wave_focus.txt` SHA-256 `86A6A9BE8132F9DF53DFA58733A776B55BF24CA91F8E4A169296953D360D832C`, `006_independence_wave_iw043_iw058_focus.txt` SHA-256 `FF73C22B4269F02CA831ABA89C7EDE443861A5260317DDD4F40DD0FD57E5A30F`, and `006_independence_wave_iw093_iw098_focus.txt` SHA-256 `91646A32C32D8CD6D9E29357BBF580FFACB82B52F06AF386A03491132A5AD807`.

## Required MCP evidence

The current root `hoi4.focus_inspect` receipt completed successfully for `independence_wave_focus_tree` and `common/national_focus/006_independence_wave_focus.txt`.

- Status: `FOCUS_INSPECTED`.
- Workspace: `mod_chaos_redux_ea3b2d67c2c0`.
- Revision: `56ae3826618bdd9546c0024a330b8e8de695f7ddea36164f70082b7dd266c094`.
- Artifact: [focus-inspect.56ae3826618bdd95.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/97b585dd45a20dcd85f9045f9b61e1a65ef479fb6bc8c625271cc93925550a69/70b013b9ea83aef8ed327d6eede218a8f9ed6ac959e60656efd5d7e332b74c67/focus-inspect.56ae3826618bdd95.json).
- Root graph: 184 materialized focus nodes, 195 connectors, zero crossings, zero node intersections, zero long connectors, zero too-close same-row pairs, and zero Event 006 diagnostics.
- Layout bounds: `x = 1..121`, `y = 0..19`.
- Layout hash: `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
- The only remaining diagnostic is the unrelated vanilla `game:common/continuous_focus/generic.txt` `continuous_restrict_freedom_desc` inventory warning.

The paired root `hoi4.focus_render` receipt completed successfully with validation passed and the same layout hash.

- HTML: [independence_wave_focus_tree.focus.html](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1387f679ebb46e99df9e4385f2d934232a98fdff7c3d1ee0a817d3b318cc0f0c/b42b7c0071a8698d866b3c08bb9b4a7ef3d4a58aad1e1fd564d35b0fd83a893e/independence_wave_focus_tree.focus.html).
- SVG: [independence_wave_focus_tree.focus.svg](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/790ac83c6f2cdb9816133b30e7a650f0e74f3823cf45efd0753fa9182ec87279/c72a975b5e3b2df66887974d08614c2abca3f459c4c41591776d9c31594c40c3/independence_wave_focus_tree.focus.svg).
- JSON: [independence_wave_focus_tree.focus.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4320385aee3822cf11b980888ec9d2d137de498426c8b6f8e966fbe233d5767a/7d6713d52fe3fc0b1ea92a5d3b83b2812be09044b2d8058d4406a6aa720a5296/independence_wave_focus_tree.focus.json).
- Source map: [independence_wave_focus_tree.focus.source-map.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b5ae8c4b5c523e1ac20d8e279d46be9f755dcacb54e4abeaf9478f18adbc9c3/60f77078a196c8f1b9adb2da487e7f8c1736f3f62eb24bd53e90368e139dbd7d/independence_wave_focus_tree.focus.source-map.json).
- Plan metadata: [independence_wave_focus_tree.focus.plan.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b38c755b5d414f9ee053b0bc218fe9b7be3b4913e57eedcd5f6bd4d2f19da00/0651245e1327fb0ceeff2d53cd9b0ae75dc9f938395d5b016edef70858d67401/independence_wave_focus_tree.focus.plan.json).
- Render dimensions: `21424 x 2440`.

Direct inspect and render of the two shared-focus-only module files returned `FOCUS_TREE_NOT_FOUND` because neither file contains a national `focus_tree` wrapper. This is an MCP surface limitation, not an absent route. The valid evidence is the root tree and the carrier imports.

No separate `hoi4.focus_lint` or `hoi4.focus_validate` route is exposed in the current runtime. The inspect diagnostics are the available focus lint-equivalent evidence.

The raster render path remains blocked by the 21424-pixel width ceiling. The HTML, SVG, JSON, source-map, and plan artifacts are available for review.

## Route coverage

| Required route or surface | Current implementation and identifiers | Status and exact source references |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement`, with `independence_wave_map_internal_power_centers` and three power-center outcomes | Implemented in `common/national_focus/006_independence_wave_focus.txt:103-366`, including `can_complete_independence_wave_survival_capstone` and `can_open_independence_wave_internal_power_struggle`. |
| Economy and administration | `independence_wave_establish_emergency_revenue`, food and fuel, regional transport, customs, package economy, and `independence_wave_create_independent_treasury` | Implemented in `common/national_focus/006_independence_wave_focus.txt:370-489` with administration, supply, transport, customs, technology, and treasury effects. |
| Army and security | Militia integration, depots, officer recall, border guard, military archetype, ten policy choices, and professional-defense capstone | Implemented in `common/national_focus/006_independence_wave_focus.txt:496-794`. The standardization and independent-command choices retain explicit archetype prerequisites and their mutual exclusions. |
| Diplomacy, recognition, and patrons | Foreign office, first missions, neighbor recognition, neutrality, patron balancing, treaty-backed state, and permanent foreign service | Implemented in `common/national_focus/006_independence_wave_focus.txt:805-946` with route-aware recognition and patron predicates. |
| Government settlements | Constitutional, popular-council, traditional, emergency-military, patron-client, radical-sovereignty, and IW-010 neutral-commission routes | Implemented in `common/national_focus/006_independence_wave_focus.txt:957-1430`. First commitments are route-locked and package-gated. |
| Former-host settlement | Negotiated separation, guarded frontier, association, reclamation conflict, and collapsed-host successor ledger | Implemented in `common/national_focus/006_independence_wave_focus.txt:1439-1625`. The four living-host choices are mutually exclusive and collapse has a separate branch. |
| Regional ambition | Survey, local committees, regional congress, postwar integration authority, and signature extension | Implemented in `common/national_focus/006_independence_wave_focus.txt:1629-1705` with `can_open_independence_wave_regional_ambition`. |
| Network and league | Recognition, civil-servant exchange, aid corridor, arbitration, charter, founding members, congress, and proposal branches | Implemented in `common/national_focus/006_independence_wave_focus.txt:1710-1893`. Decisions own votes and proclamations. |
| Formable preparation | Regional identity, union congress, formation terms, integration commission, and FORM-03 post-charter branch | Implemented in `common/national_focus/006_independence_wave_focus.txt:1899-2092`. Discovery, claims, consent, and formation remain decision-owned by design. |
| High-chaos and revisionist route | Further ruptures, coordinated reclamation, open sovereignty, charter rewrite, and durable-state payoff | Implemented behind route or World Collapse gates in `common/national_focus/006_independence_wave_focus.txt:2097-2155` and the framework capstone at `:3369-3392`. |
| IW-043 and IW-058 package modules | 48 shared definitions covering Middle Volga and Assyrian civic, economic, military, host, and terminal routes | Root imports are `common/national_focus/006_independence_wave_focus.txt:60-69`. Definitions are in `common/national_focus/006_independence_wave_iw043_iw058_focus.txt:18-786`. |
| IW-093 and IW-098 package modules | 43 shared definitions covering Asante and Sokoto survival, economy, government, host, security, and formable preparation | Root imports are `common/national_focus/006_independence_wave_focus.txt:72-87`. Definitions are in `common/national_focus/006_independence_wave_iw093_iw098_focus.txt:23-738`. |
| Package and regional signature modules | IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-014, IW-017, IW-018, and IW-019 package branches plus CAT, COR, RHI, BAY, and Pacific consumers | Implemented in `common/national_focus/006_independence_wave_focus.txt:2157-4247` with exact package gates and shared helper effects. |
| Additive carrier overlays | Overlay root, state services, release forces, foreign desk, former host, network, regional ambition, maturity, and ICE route consumers | Implemented in `common/national_focus/006_independence_wave_focus.txt:3394-3710`. Carrier imports are `common/national_focus/iceland.txt:28-44` and `common/national_focus/austro_hungarian_releasable_shared.txt:31-38`. |

No accepted Part 4 route family is absent from the current architecture.

## Missing or simplified content

No focus route, prerequisite, mutual exclusion, reward helper, localisation surface, icon wiring, or existing decision/formable unlock hook was proven missing by the current source and MCP evidence.

The one shared generic tree with gated package modules and additive carrier overlays is intentional and matches the accepted Part 4 architecture. It is not a fallback tree and no country-specific Event 006 tree was silently substituted.

The wider package-admission boundary remains incomplete at 32 content-attested selectable packages, 40 runtime adapters, 29 compatible reservation groups, and 161 unattested selectable rows. These are package evidence gaps, not safe focus-file patches.

The eight adapter-only rows remain fail-closed and must not be exposed by a focus-only change: IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.

IW-095 Dahomey remains package-local and fail-closed. The current registry exposes `can_plan_independence_wave_package_iw_095` in `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:736-743` and its loader in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1549-1562`, but the generic focus callback list has no `DAH`, `iw095`, or `independence_wave_iw095_focus_*` call. Adding one callback before the package-local identity, mission, asset, AI, cleanup, and admission evidence exists would bypass the accepted gate.

No improvement-loop plan was written because the accepted route architecture is present and no shallow accepted route was established by this audit.

## Icon coverage

| Surface | Coverage | Finding |
| --- | ---: | --- |
| All root and shared focus definitions | 318/318 | Every definition has an icon reference. |
| Unique Event 006 focus icon IDs | 121/121 | Every referenced normal sprite resolves in the Event 006 GFX surface. |
| Event 006 shine sprites | 121/121 | Every normal icon has a matching `_shine` sprite. |
| Event 006 focus texture files | 121/121 | Static texture resolution reports `missingTextureFiles = 0`. |

The current focus icon registries are `interface/006_independence_wave.gfx`, `interface/006_independence_wave_iw093_iw098_focus.gfx`, and `interface/006_independence_wave_small_assets.gfx`.

Family art is intentionally reused for route-consistent surfaces such as founding administration, army integration, infrastructure authority, former-host settlement, league congress, regional formables, high chaos, and recognition. This is a future visual-distinction opportunity, not a missing asset or unsafe wiring defect.

## Localisation and reward mismatch list

No current Event 006 focus title, description, custom tooltip, icon, or reward mismatch was identified.

- Title coverage: 318/318.
- Description coverage: 318/318.
- `custom_effect_tooltip` coverage: 318/318.
- Reward helper references: 331 checked, zero missing scripted-effect definitions.
- Localisation files under `localisation/english/006_independence_wave*.yml` retain UTF-8 BOM encoding.

The reward helper inventory covers administration, diplomatic steps, public settlement, security reform, stabilization, ambition, network cooperation, durable state, radicalization, league revisionism, client development, founding steps, and distinct league equality, development, and defense bundles, alongside package-specific effects.

No sampled focus name contradicted its reward. Treasury, customs, border guard, foreign office, host policy, league, formable preparation, and high-chaos names match their visible effect families.

No missing decision, mission, formable, idea, claim, war-goal, event, or existing unlock hook was found in the focus-specific surface. Formable discovery, claims, consent, and formation transactions remain owned by the existing decision and formable systems as specified.

## Prerequisite, bypass, and mutual-exclusion checks

The static reference inventory resolves all 275 extracted focus references with no missing prerequisite, bypass, or relative-position target.

The 55 parsed mutual-exclusion owners have no asymmetric pairs. The four living-host roots, government route choices, military choices, and league proposals retain their intended locks.

Separate prerequisite blocks remain separate where the design requires AND semantics, including `independence_wave_establish_permanent_ministries`, `independence_wave_integrate_provinces_and_councils`, and `independence_wave_complete_founding_settlement`.

The military standardization and independent-command choices retain their `independence_wave_adopt_military_archetype_program` prerequisite and their respective exclusions in `common/national_focus/006_independence_wave_focus.txt:758-796`.

## AI behavior gaps

All 318 source focus and shared-focus definitions have `ai_will_do` blocks, and the root tree remains gated by the active-country and full-framework contract.

Route-aware focus constants and modifiers are present in `common/national_focus/006_independence_wave_focus.txt` and the generic baseline profiles cover survival, recovery, consolidation, recognition, host, security, and capacity signals in `common/ai_strategy/006_independence_wave_generic.txt:35-104`.

Structural AI coverage is therefore complete, but no fresh quantitative balance claim is made.

The mandatory `chaosx_ai_probability_auditor` route is not callable in the current task context, and the recorded typed probability route is blocked by `Transport closed`. No probability baseline, same-scenario comparison, or AI weight patch is claimed.

Runtime focus candidate ranking, scheduling under competing lanes, package starvation, and save/load persistence remain untested because they require the unavailable probability route or live runtime evidence.

## High-priority fixes first

1. Preserve the current 184-node and 195-connector root geometry with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
2. Route any future focus AI or probability-bearing change through `chaosx_ai_probability_auditor` with named scenarios and a compare pass before editing weights.
3. Keep the eight adapter-only package rows and IW-095 fail-closed until their package evidence and central admission gates are complete.
4. For module-level visual evidence, inspect a supported carrier or wrapper tree that imports the shared-focus module. Do not create a fake standalone tree solely to satisfy the MCP surface.
5. Keep the unrelated vanilla `continuous_restrict_freedom_desc` warning outside the Event 006 focus fix set.

## Changed files and focus IDs

Only this documentation handoff was added: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_audit_current_2026-08-29.md`.

Changed gameplay files: none.

Changed focus IDs: none.

Changed localisation keys: none.

Changed icon IDs: none.

Route behavior before and after: unchanged.

## Validation and skipped validation

Meaningful validation completed for this refresh includes the current root `hoi4.focus_inspect` and `hoi4.focus_render` receipts linked above, source inventory across the three active focus files, reference resolution, mutual-exclusion symmetry, icon and texture resolution, localisation coverage, and reward-helper resolution.

The offline Paradox national-focus, data-structure, trigger, effect, modifier, localisation, scope, on-action, event, decision, idea, and AI references and the relevant vanilla documentation were consulted before the focus review.

`hoi4.focus_rewrite` was not run because no safe gameplay patch was identified.

The dedicated focus lint and validate routes are unavailable in the current runtime.

The shared-focus-only modules cannot be rendered directly because they intentionally contain no `focus_tree` wrapper.

The probability auditor baseline and compare were skipped because the route is unavailable and no AI weight was changed.

No live HOI4 launch, save/load test, or player-owned runtime receipt was performed, per repository boundaries.

## Remaining route risks and parent handoff

The main remaining risk is broader package admission, not missing generic focus content or root geometry.

Typed AI balance evidence remains blocked by the probability transport failure.

The shared IW-043/IW-058 and IW-093/IW-098 modules have valid root-import evidence but no direct module-level MCP layout receipt.

The raster render remains blocked by the renderer width ceiling even though the reviewable SVG and HTML artifacts passed.

Parent handoff: treat this audit as a no-patch focus closure for the current source and preserve the exact MCP artifacts above. Any future parent-owned graph or AI change should rerun root inspect/render and the bounded static route, icon, localisation, reward, and mutual-exclusion checks.

No gameplay simplifications, unapproved fallbacks, or route expansions were introduced.

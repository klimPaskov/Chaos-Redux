# Event 006 generic focus geometry audit v111

Date: 2026-08-03.

Scope: read-only audit of the single Event 006 generic focus tree, its three shared-focus modules, route coverage, prerequisite and mutual-exclusion semantics, icons, localisation, rewards, AI hooks, and the current MCP layout diagnostics.

Disposition: **AUDIT COMPLETE / NO SAFE LOCAL PATCH**.

The source remains unchanged because the current diagnostics are a coupled layout problem rather than an isolated coordinate defect.

## Current MCP evidence

The fresh read-only `hoi4.focus_inspect` call resolved `independence_wave_focus_tree` from `common/national_focus/006_independence_wave_focus.txt` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d67d405a1140bb33c11f0dfba41486cb9a1867e44f4db503936a022f456049d5/8b8b820ef2682f4b817c6c8cb32f3c2bf90d470eb6e424e95f731db91a4a677c/focus-inspect.8d506b31721db8eb.json`.

The fresh read-only `hoi4.focus_render` call produced the following review artifacts.

| Artifact | URI |
| --- | --- |
| HTML | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12160e902184c36255109203ac80a9392f349dfb03c93c194e5e6fc98c516ab5/1b758b1b1c34e93cd225f9902aa5754c862d75839f9550db7df54410b00fda24/independence_wave_focus_tree.focus.html` |
| SVG | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56b47295032754eacb221bca80e282cf17bd002465d6d4d72696920d1eb5a6b0/c58b1e940c37beef5178b1fa117b93560f3e4b03da2e12c791033ccedcbb0804/independence_wave_focus_tree.focus.svg` |
| JSON | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/316aa46d5899f4446f9593e367c691074f0fa6d3a9c446d4486a50d3279e17cf/ed37c527024624790c881a6204873a0740100fab297e1a3a8a5f95159090e871/independence_wave_focus_tree.focus.json` |
| Source map | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34caa01abdeb8caa03e051b25e8edd069edd662bd1331b5dfc95efa788b45b0b/b53bd0bc59fc126256e0fa80df7331b5ca2e706cc50f3ffff1e5f551b125c558/independence_wave_focus_tree.focus.source-map.json` |
| Plan metadata | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1e30fa59debc7b4a759b786ac27c745f62aae639e6929ce7b3e3c1e3618a547/9a18b4327ee04ae829d8ea41f41d35a647df9e58353f30599e2a6a3f42f3fd47/independence_wave_focus_tree.focus.plan.json` |

The current tree resolves 184 direct focus nodes and 223 prerequisite connectors with layout bounds `x=1..101`, `y=0..19` and layout hash `040dadcdd4577acbf06d6dc252cfa0ac751353b3d3f1eb3bf5b1f83ab642b776`.

The render remains validation **PARTIAL / HOLD** with 14 blocking diagnostics: 43 connector crossings, 7 node intersections, 28 long connectors, and 5 same-row pairs below the required two-column spacing.

The largest connector spans 80 columns.

The MCP marks the coupled crossing endpoints as fixed or relative and reports no movable focus IDs for those diagnostics.

## Route coverage

| Required route | Source coverage | Status and evidence |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` in `common/national_focus/006_independence_wave_focus.txt:100-243` | PASS at source level; completion is tied to centralized survival values and the DM-01/capital/capacity gates rather than a cosmetic reward. |
| Government settlements | Constitutional, popular-council, traditional, emergency-military, patron-client, radical-sovereignty, and AJX municipal-neutral-commission routes in `common/national_focus/006_independence_wave_focus.txt:845-1290` | PASS at source level; government opening commitments use reciprocal mutual exclusions and route-aware availability. |
| Economy, infrastructure, and administration | `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury` in `common/national_focus/006_independence_wave_focus.txt:318-421` | PASS at source level; regional and package selectors feed scripted effects and the treasury capstone. |
| Army, security, and military identity | `independence_wave_integrate_militia_commands` through `independence_wave_preserve_independent_command` in `common/national_focus/006_independence_wave_focus.txt:439-693` | PASS at source level; `independence_wave_found_professional_defense_institution` has five repeated prerequisite blocks, each an OR pair, preserving the intended AND-of-five-OR semantics. |
| Diplomacy, recognition, and patrons | `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service` in `common/national_focus/006_independence_wave_focus.txt:709-839` | PASS at source level; recognition, patron balance, neutrality, and foreign-service effects are route-aware. |
| Former-host settlement | Negotiated separation, guarded frontier, association, reclamation, and collapsed-host branches in `common/national_focus/006_independence_wave_focus.txt:1312-1474` | PASS at source level; living-host choices are mutually exclusive and the collapsed-host route is gated by `can_settle_independence_wave_host_collapse`. |
| Regional ambition and signature extensions | `independence_wave_survey_regional_ambition` through `independence_wave_open_signature_extension` in `common/national_focus/006_independence_wave_focus.txt:1494-1537` | PASS at source level; registered ambition families and mandate state gate the lane. |
| Network and League | Recognition, civil-service exchange, aid corridor, arbitration, congress, and five mutually exclusive proposal focuses in `common/national_focus/006_independence_wave_focus.txt:1567-1733` | PASS at source level; decisions retain vote and proclamation ownership. |
| Formable preparation | `independence_wave_focus_discover_regional_identity` through `independence_wave_establish_integration_commission`, followed by the FORM-03 post-charter chain in `common/national_focus/006_independence_wave_focus.txt:1751-1897` | PASS at source level; focus receipts prepare the formable system while discovery, claims, and formation remain in dedicated decision/adaptor code. |
| High-chaos sovereignty | `independence_wave_sponsor_further_ruptures`, `independence_wave_focus_coordinate_reclamation_fronts`, `independence_wave_proclaim_open_sovereignty`, and `independence_wave_rewrite_charter_of_borders` in `common/national_focus/006_independence_wave_focus.txt:1949-1978` | PASS at source level; World Collapse/radical/open-sovereignty gates and danger-milestone effects are present. |
| Shared package and signature modules | Main-tree package blocks in `common/national_focus/006_independence_wave_focus.txt:1998-3146`; IW-043/IW-058 in `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`; IW-093/IW-098 in `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`; Pacific in `common/national_focus/006_independence_wave_pacific_focus.txt` | PASS for source presence and exact package gates; package admission, identity, and formable readiness remain separate blockers. |
| Durable-state capstone | `independence_wave_secure_durable_sovereignty` in `common/national_focus/006_independence_wave_focus.txt:3163-3171` | PASS at source level; it requires economy, military, foreign-service, host, and value outcomes through `can_complete_independence_wave_durable_sovereignty`. |
| Additive carrier boundary | `independence_wave_overlay_take_stock_of_independence` and its overlay chain in `common/national_focus/006_independence_wave_focus.txt:3184-3424` | PASS as an intentional boundary; only the reviewed ICE carrier may use the additive overlay, and CAT remains an explicit full-framework minimal-tree carrier. |

The four source files contain 184 direct definitions, 134 full shared-focus definitions, and 27 simple import references, for 318 unique focus IDs and 345 raw entries including import lines.

## Missing or simplified content

- No route family is missing from the accepted one-tree contract, and no fallback tree or generic replacement was introduced.
- Geometry remains unresolved at the MCP validator level; the current rendered artifact proves the blocker but does not prove runtime focus selection, package admission, timing, or save/load behavior.
- No probability sweep was run for government, patron, League, formable, high-chaos, package, or CAT opener selection.
- CAT source content is connected but deliberately fail-closed for admission until its identity, flag, NAV/GLC adapter, and FORM-07 readiness gates are accepted.
- The additive carrier remains intentionally narrow and must not be broadened to hide package or meaningful-tree blockers.

## Geometry findings and high-priority fixes

The first coupled cluster is the opening/economy fan in `common/national_focus/006_independence_wave_focus.txt:257-421`.

`independence_wave_complete_founding_settlement -> independence_wave_map_internal_power_centers` is a 17-column connector.

`independence_wave_bind_the_first_oath -> independence_wave_integrate_provinces_and_councils` crosses `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue`, whose connector spans 12 columns.

The same economy row crosses the complete-settlement fan to AJX neutral commission, former-host policy, and fellow-state recognition, and the complete-settlement to `independence_wave_survey_regional_ambition` connector passes through `independence_wave_establish_customs_service`.

The second coupled cluster is the depot/professional-defense merge in `common/national_focus/006_independence_wave_focus.txt:439-693`.

`independence_wave_bind_the_first_oath -> independence_wave_integrate_militia_commands` spans 14 columns, while the ten-choice y=8 military cohort converges on `independence_wave_found_professional_defense_institution` at x=40/y=9.

That convergence creates crossings with the foreign-service/durable-sovereignty lane and long 9-column connectors from `independence_wave_confirm_civilian_control` and `independence_wave_preserve_independent_command`.

The remaining long connectors are `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine` at 9 columns and `independence_wave_adopt_military_archetype_program -> independence_wave_standardize_with_league` at 11 columns.

No isolated move is safe: the affected main nodes use fixed absolute coordinates, the shared package branches use `relative_position_id`, and MCP marks the coupled endpoints preserved with `movableFocusIds=[]`.

High-priority parent-owned fix order:

1. Reflow the opening/economy fan as one reviewed cluster while preserving all prerequisites, route gates, imports, rewards, and IDs.
2. Reflow the y=5..9 military/professional-defense merge together with the diplomacy and durable-capstone anchors.
3. Re-render and inspect the full tree after each candidate; retain the current source if a candidate trades crossings for node intersections or changes route visibility.
4. Do not use a compact rewrite as a local coordinate patch; the current compact attempt is quality-blocked and the source remains unchanged.

## Icon coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Focus icon references | 121 unique base icon IDs across 318 focus definitions | Four `common/national_focus/006_independence_wave*.txt` files |
| Base `.gfx` registration | 121/121 resolve | `interface/006_independence_wave*.gfx` |
| Shine sprites | 121/121 matching `_shine` names | Same interface scan |
| Missing or repeated icon issue | None found | No icon patch is justified by this audit |

## Localisation and reward mismatch list

- All 318 focus IDs and all 318 `_desc` keys resolve across 45 Event 006 English localisation files.
- All 318 `custom_effect_tooltip` keys used by focus rewards resolve.
- All 45 scanned Event 006 English localisation files begin with UTF-8 BOM bytes.
- No duplicate quoted localisation key was found in the scanned Event 006 English files.
- No exact normalised completion-reward body repeats across the 318 definitions.
- No title/description or reward-key mismatch was found by the bounded key scan.
- A complete semantic prose-to-effect review was not repeated in this geometry tranche; any mismatch not visible to key/reward-body checks remains an evidence gap rather than a claimed PASS.

## AI behavior gaps

- Every one of the 318 parsed focus definitions has an `ai_will_do` block.
- The generic focus constants in `common/script_constants/006_independence_wave_focus_constants.txt:62-78` provide none/cautious/standard/high/urgent weights plus preference, avoidance, and war-avoidance factors.
- Route-aware modifiers read package archetype, war/host state, former-host threat, patron dependency, government route, league state, and chaos flags in the focus sources and paired strategy files.
- Generic survival, recovery, and consolidation profiles are present in `common/ai_strategy/006_independence_wave_generic.txt:42-143`.
- The accepted AI matrix remains broader than source weights alone; no current scenario probability sweep proves relative selection order or route starvation for government, patron, League, formable, high-chaos, package, or CAT openers.
- Live or in-game AI behavior was not tested and remains outside this handoff.

## Validation and limits

Meaningful checks completed were the current MCP inspect/render, four-file focus block count and duplicate-ID scan, prerequisite/mutual-exclusion reference scan, OR/AND inspection of the five military capstone prerequisite pairs, icon-to-`.gfx` and shine scan, focus title/description/custom-tooltip localisation scan, reward-body uniqueness scan, and UTF-8 BOM scan.

Skipped `hoi4.focus_raster` because the rendered HTML/SVG/JSON/source-map artifacts were sufficient for this geometry audit and no pixel-level icon defect was reported.

Skipped `hoi4.focus_rewrite` because MCP identified a coupled layout with no movable endpoints for the reported crossings and a rewrite would exceed this narrow audit scope.

Skipped live game launch, save/load, and in-game AI validation because those are user/parent-owned surfaces and are outside the accepted Event 006 focus contract.

## Changed files and identifiers

No gameplay, focus, localisation, icon, or AI source file was changed.

Changed file: this handoff only, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_geometry_audit_v111_2026_08_03.md`.

Changed focus IDs: none.

Changed localisation keys: none.

Changed icon IDs: none.

No improvement-loop plan was written because the tree has broad route depth; the open work is a coordinated geometry tranche and parent-owned AI probability evidence, not a missing route family.

## Remaining route risks

- The 14 blocking diagnostics remain a visual/layout blocker even though route graph, localisation, icon, and reward source checks pass.
- Current source graph checks do not prove player-facing availability after ledgers, host state, package flags, or formable transactions change.
- CAT and other non-attested packages must remain fail-closed until their separate package evidence closes.
- No claim is made about runtime focus selection, AI completion order, save/load persistence, or player-owned rendering.

Parent handoff: use this receipt as the current narrowed generic-tree audit, preserve the source coordinates until a coordinated reflow is reviewed, and reconcile geometry and AI evidence into the current Event 006 completion documents.

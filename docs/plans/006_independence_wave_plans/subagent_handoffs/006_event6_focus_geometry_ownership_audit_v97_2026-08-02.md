# Event 006 focus geometry and ownership audit v97

Date: 2026-08-02.

Scope: current Event 006 focus sources, route coverage, prerequisite and exclusion semantics, static geometry after the v82 reflow, icon/localisation/AI coverage, and the resolved IW-014 CAT focus-ownership contract.

Disposition: **PARTIAL / HOLD**.

The source-level tree is broad and structurally connected, the v82 coordinate candidate remains the retained static after-state, and CAT now has an explicit full-framework minimal-tree contract. Current MCP inspection and rendering remain unavailable because the workspace scan exceeds `SCAN_BYTE_LIMIT`, so geometry completion and runtime route/probability evidence remain open.

No Event 006 package was admitted, no attestation was changed, and no fallback content was introduced.

## Evidence and current metrics

| Evidence surface | Current result | Boundary |
| --- | --- | --- |
| Four focus source files | 318 unique blocks: 184 regular and 134 shared; zero duplicate IDs; all blocks have `icon`, `completion_reward`, and `ai_will_do`. | Static source only. |
| Prerequisite and exclusion references | Zero unresolved prerequisite references and zero unresolved mutual-exclusion references. The all-source graph has two roots, `independence_wave_prepare_capital_administration` and `independence_wave_overlay_take_stock_of_independence`, and zero unreachable IDs in the bounded graph walk. | This is a source graph check, not a live focus-selection test. |
| v82 static after-state | 184 regular nodes, 223 prerequisite connectors, 53 straight-segment crossings, 2 point-on-segment through-node hits, 28 long connectors, 5 same-row gaps below two units, and zero duplicate coordinates. | This is the retained source-level geometry model recorded by `006_event6_focus_geometry_reflow_v82_followup_2026-08-01.md`, not a current MCP result. |
| Current `hoi4.focus_inspect` | `SCAN_BYTE_LIMIT`; `filesScanned=[]`, `diagnostics=[]`, `artifacts=[]`, and no layout hash. | Exact current blocker count is unknown. |
| Current `hoi4.focus_render` | `SCAN_BYTE_LIMIT`; no render artifact or diagnostics. | No post-v82 visual/layout artifact is available. |
| Historical successful MCP baseline | Layout hash `58cc490cf17dfbc7e1a5794c0eea060d3e2fe9f99da7cd175dd46f7daed261bf`; 184 regular nodes, 223 connectors, 45 crossings, 7 node intersections, 28 long connectors, 14 blocking diagnostics, bounds `x=1..101`, `y=0..19`. | This predates v82 and must not be presented as the current state. |

The fresh static parser confirms structure after the comment-only CAT clarification, but its generic segment-intersection thresholds differ from the v82 audit model. Its alternative geometry totals are therefore not used as authoritative metrics.

## Route coverage table

| Required route | Current implementation and identifiers | Status |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement` in `common/national_focus/006_independence_wave_focus.txt:89-243`; capstone checks are centralized in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:79-85`. | PASS at source level. |
| Government settlements | Constitutional, popular-council, traditional, emergency-military, patron-client, radical-sovereignty, and the IW-010 municipal-neutral-commission branch in `common/national_focus/006_independence_wave_focus.txt:845-1290`; opening commitments are reciprocally mutually exclusive at the route focus blocks. | PASS at source level; runtime route reachability remains untested. |
| Economy, infrastructure, and administration | `independence_wave_establish_emergency_revenue`, `independence_wave_secure_food_and_fuel`, `independence_wave_build_regional_transport_authority`, `independence_wave_establish_customs_service`, `independence_wave_activate_package_economic_program`, and `independence_wave_create_independent_treasury` in `common/national_focus/006_independence_wave_focus.txt:307-421`. | PASS at source level. |
| Army, security, and military identity | `independence_wave_integrate_militia_commands` through `independence_wave_preserve_independent_command` in `common/national_focus/006_independence_wave_focus.txt:428-693`; `independence_wave_found_professional_defense_institution` preserves five separate prerequisite blocks, each containing a paired alternative, for the intended AND-of-five-OR semantics. | PASS at source level. |
| Diplomacy, recognition, and patrons | `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service` in `common/national_focus/006_independence_wave_focus.txt:698-839`, with route and patron triggers in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:153-229`. | PASS at source level; no timing or probability sweep. |
| Former-host settlement | Negotiated separation, guarded frontier, association, reclamation, and collapsed-host branches in `common/national_focus/006_independence_wave_focus.txt:1301-1474`; living-host openers are mutually exclusive and collapsed-host access is centralized in `can_settle_independence_wave_host_collapse`. | PASS at source level. |
| Regional ambition and signature extensions | `independence_wave_survey_regional_ambition` through `independence_wave_open_signature_extension` in `common/national_focus/006_independence_wave_focus.txt:1483-1537`, gated by `can_open_independence_wave_regional_ambition`. | PASS at source level; package admission is separate. |
| Network and league | Recognition, civil-service exchange, aid corridor, arbitration, charter, founding members, congress, and five mutually exclusive proposals in `common/national_focus/006_independence_wave_focus.txt:1556-1733`; decisions remain the vote/proclamation owners. | PASS at source level. |
| Formable preparation and post-charter work | `independence_wave_focus_discover_regional_identity` through `independence_wave_establish_integration_commission` in `common/national_focus/006_independence_wave_focus.txt:1740-1790`, followed by FORM-03 post-charter focuses through line 1897. | PASS at source level; individual formable readiness remains open. |
| High-chaos sovereignty | `independence_wave_sponsor_further_ruptures`, `independence_wave_focus_coordinate_reclamation_fronts`, `independence_wave_proclaim_open_sovereignty`, and `independence_wave_rewrite_charter_of_borders` in `common/national_focus/006_independence_wave_focus.txt:1938-1978`. | PASS at source level; no high-chaos AI probability sweep. |
| Package overlays | Scotland, Wales, Saar, Brittany, Wallonia, Frisia, Rhineland, Bavaria, Sardinia, Sicily, COR, Pacific, IW-043/IW-058, and IW-093/IW-098 blocks in `common/national_focus/006_independence_wave_focus.txt:1998-3146` and the three Event 006 overlay focus files. | PASS for source presence; package admission and identity evidence remain outside this audit. |
| Post-formation overlay | `independence_wave_overlay_take_stock_of_independence` and the overlay chain in `common/national_focus/006_independence_wave_focus.txt:3173-3424`; `post_formation_overlay` preserves the full-framework flag in `common/scripted_effects/006_independence_wave_focus_effects.txt:39-72`. | PASS for already-owned full-framework formables; no meaningful-tree additive carrier is proven. |
| IW-014 CAT | Six CAT focuses at `common/national_focus/006_independence_wave_focus.txt:3534-3617`; setup assigns `constant:independence_wave_focus_assignment.full_framework` at `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt:316-317`. | PASS for the accepted source contract; CAT remains fail-closed for admission. |
| Africa boundary | `012_africa_continental_focus_tree.txt`, `012_africa_priority_member_focus.txt`, and `012_africa_world_europe_focus.txt` remain separate systems with no Event 006 imports. | PASS as an intentional boundary. |

## Missing or simplified content

- No current MCP inspect/render artifact exists because both calls stop at `SCAN_BYTE_LIMIT`; the current post-v82 blocker count and layout hash are therefore unavailable.
- The retained v82 static model still has 53 crossings, 2 through-node hits, 28 long connectors, and 5 close same-row pairs. The opening oath/economy fan and depot/professional-defence merge remain coupled risks documented by `006_event6_focus_geometry_reflow_v82_followup_2026-08-01.md:55-59`.
- Static source reachability does not prove route timing, save/load persistence, focus visibility, or AI selection order. No parent-owned probability sweep was run for government, patron, league, formable, high-chaos, package, or CAT branches.
- The additive carrier trigger remains deliberately narrow: `can_attach_independence_wave_additive_focus_carrier` in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:52-64` admits only the reviewed ICE carrier with `iceland_tree`. A generic flag cannot insert shared focuses into another owning tree.
- CAT is not an additive-carrier exception. Vanilla CAT exposes only `generic_focus` in `history/countries/CAT - Catalonia.txt` and completes generic focuses in its 1939 history block; the accepted contract is an explicit full-framework load after the minimal-tree review. CAT remains outside compile-time content attestation and FORM-07 remains fail-closed for the Iberian X identity, flag, NAV/GLC adapters, and readiness gates.
- The old v96 whole-event handoff and dated source-map sections still contain historical 'CAT design gap/additive' wording. The current top-level source-map authority and CAT package documentation resolve the contract; historical wording should be reconciled by documentation ownership before a whole-event completion claim.

No route family was replaced by a fallback, and no broad route redesign is proposed in this audit.

## Icon coverage table

| Check | Result | Evidence |
| --- | --- | --- |
| Focus icon references | 318 blocks use 121 unique `GFX_goal_independence_wave_*` base references. | Four current focus source files. |
| `.gfx` registration | 121/121 base references resolve. | `interface/006_independence_wave.gfx` and package-specific files under `interface/006_independence_wave_*_assets.gfx`, `006_independence_wave_*_focus*.gfx`. |
| Shine sprites | 121/121 base references have a matching `_shine` sprite. | Same interface scan. |
| Missing icon diagnostics | None in the bounded source scan. | No gameplay icon patch needed. |

## Localisation and reward mismatch list

- All 318 focus IDs and all 318 `_desc` keys resolve across the 45 Event 006 English localisation files, including `localisation/english/006_independence_wave_focus_l_english.yml` and package-specific focus localisation files.
- All 318 `custom_effect_tooltip` keys used by focus rewards resolve to localisation keys.
- Event 006 English localisation files inspected for this audit begin with UTF-8 BOM bytes (`EF-BB-BF`).
- No missing or duplicate focus key was found by the bounded key scan.
- No exact normalised completion-reward body repeats across the 318 blocks, so no mechanically duplicated generic reward group was found.
- A full semantic prose-to-effect review was not repeated in this geometry tranche; any mismatch not visible to key/reward-body checks remains an evidence gap rather than a claimed PASS.

## AI behavior gaps

- Every one of the 318 parsed blocks has an `ai_will_do` block.
- Route-aware source signals are present: package and route gates use `allow_branch`/`available`, and route modifiers read flags, war/host state, ledgers, and route commitments rather than using only a naked base weight.
- The source does not provide a completed scenario probability sweep for government settlement, patrons, league proposals, formables, high-chaos sovereignty, CAT, or the unadmitted additive carriers.
- CAT has focus AI blocks, but runtime AI evidence is intentionally unavailable while the package is fail-closed and outside attestation.

## CAT full-framework versus additive contract

| Surface | Current source | Contract decision |
| --- | --- | --- |
| Vanilla carrier | Vanilla CAT history preserves tag, state 165, flag, Companys, and generic-focus completions; no dedicated CAT focus tree/import exists in the installed vanilla files. | Preserve non-focus vanilla surfaces. |
| Assignment | `independence_wave_setup_iw_014_catalonia` sets `independence_wave_focus_assignment_input = full_framework` and calls `independence_wave_assign_focus_framework`. | Accepted minimal-tree full-framework ownership. |
| Shared roots | Six CAT roots are imported by `independence_wave_focus_tree` at `common/national_focus/006_independence_wave_focus.txt:75-82`. | They are part of the full Event 006 framework, not a generic-tree insertion. |
| CAT branch gate | `independence_wave_cat_secure_barcelona_port_focus` requires `can_use_independence_wave_full_focus_framework`; the remaining five focuses chain from it at `common/national_focus/006_independence_wave_focus.txt:3534-3617`. | Full framework must be assigned before CAT branch visibility. |
| Additive carrier | `can_attach_independence_wave_additive_focus_carrier` admits only ICE/`iceland_tree`. | Do not weaken or broaden it for CAT. |
| Admission | `has_prepared_independence_wave_iw_014_package_setup` requires the full-framework flag and assignment at `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:97-98`; the compile-time attestation OR list in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:72-88` intentionally omits IW-014. | Keep CAT and FORM-07 fail-closed until separate identity, flag, member-adapter, and readiness gates close. |

## High-priority next fixes

1. Rerun `hoi4.focus_inspect` and `hoi4.focus_render` when the scan-byte limit clears, and compare the current whole-tree totals against the pre-v82 MCP baseline. Preserve the four-coordinate v82 candidate unless the successful MCP pass demonstrates a regression.
2. If MCP still reports coupled geometry blockers, perform one coordinated lane reflow around the opening/economy fan and the y=5..9 depot/professional-defence merge. Preserve all focus IDs, prerequisites, mutual exclusions, rewards, icons, localisation, AI blocks, and package imports, and do not use `hoi4.focus_rewrite` for an isolated move.
3. Run parent-owned route/AI probability sweeps with complete candidate pools and named world-state scenarios before making ordering, dominance, starvation, timing, or balance claims.
4. Keep CAT on the explicit full-framework minimal-tree contract and outside attestation until FORM-07 identity, flag, NAV/GLC adapter, and readiness gates are independently accepted. Do not register CAT as an additive carrier.
5. Reconcile stale v96/source-map historical CAT wording after this handoff is promoted, without rewriting historical evidence or changing the gameplay contract.

## Changed files and focus IDs

- `common/national_focus/006_independence_wave_focus.txt`: comment-only clarification of CAT root imports and the CAT branch heading; no focus IDs, coordinates, prerequisites, rewards, icons, localisation keys, or AI blocks changed.
- This handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_geometry_ownership_audit_v97_2026-08-02.md`.
- Changed focus IDs: none.
- Changed localisation keys: none.
- Changed icon IDs: none.

## Validation and limits

Meaningful checks completed: required AGENTS/skills, offline Paradox wiki and vanilla documentation review; current structural focus parser; prerequisite and mutual-exclusion reference scan; graph reachability walk; icon-to-`.gfx` and `_shine` scan; focus title/description/custom-tooltip localisation scan; BOM scan of Event 006 English localisation files; and fresh MCP inspect/render calls.

The current MCP calls returned `SCAN_BYTE_LIMIT` with no files, diagnostics, artifacts, or layout hash, so no MCP PASS is claimed.

Skipped: `hoi4.focus_raster` because no current render artifact exists; focus rewrite because this audit is not a broad redesign and the current diagnostics are unavailable; scenario probability simulation because the MCP scan is blocked and the parent owns scenario evidence; game launch and live save/load observation because those are parent/user-owned validation surfaces.

No improvement-loop plan was written because the tree has broad route depth; the remaining issues are geometry evidence, carrier/admission boundaries, and probability/runtime proof rather than a shallow missing route family.

## Remaining route risks

- The current static graph does not prove player-facing availability after flags, route decisions, host state, or formable transactions change.
- The current MCP blocker inventory is unknown, so the v82 static improvement cannot be promoted to validator-clean completion.
- CAT's six-focus package is source-connected but intentionally not admitted; FORM-07 readiness and the compile-time attestation list must remain closed.
- Africa remains a separate focus system and has no Event 006 shared-focus graft by design.

Parent handoff: retain the v82 coordinate candidate, use this handoff as the current focus-specific audit, rerun MCP when the scan limit clears, and preserve CAT's full-framework minimal-tree contract while keeping admission fail-closed.

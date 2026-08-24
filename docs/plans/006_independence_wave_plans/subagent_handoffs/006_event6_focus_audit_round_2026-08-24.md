# Event 006 focus audit round — 2026-08-24

> Superseded for the current authored-warning count by `006_event6_focus_economy_lane_repair_2026-08-24.md`: this audit preserves the pre-spacing seven-warning receipt, while the post-change focus inspect/render records six warnings and remains **HOLD**.

## Scope and disposition

This is a source and HOI4-MCP audit of the shared `independence_wave_focus_tree` against the Event 006 focus-tree architecture, source map, and current graph receipts.

The tree is structurally usable within the accepted shared generic-tree scope, but this audit does not make a live-game completion claim.

No gameplay, localization, or icon source was changed in this round.

The seven authored layout warnings are retained because each requires a lane or cohort move rather than a safe one-node edit, and the custom probability-auditor route was unavailable for a quantitative AI balance comparison.

## Mandatory MCP evidence

The required focus inspection was run before any patch decision.

- `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, revision `9baedad2243a925221540a8f4dc8802632bda632591be390fd7c1add64d08822`.
- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52e18f12b0495b7397c2baa1f14596f666d1b5f4e049bf18b4f0d615e2dc8665/d18fd1712756145ecf530e3b94b4a110853707ab1fd7eaacbf923c16263d8535/focus-inspect.9baedad2243a9252.json`.
- The inspect saw 184 direct focus definitions, 195 connectors, zero crossings, zero node intersections, three long connectors, and seven authored Event 006 layout warnings.
- The inspect layout hash is `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.
- `hoi4.focus_render` returned `FOCUS_RENDERED` with the same layout hash and validation metrics at review scale `0.25`.
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78b37024026f3f73078e53241953d1aa9cf94a9006739d298935f0d7c33f91da/c54ad423cec2bafe5292bee822b59a17de22ee89f8bde1a6b938b9797bdf7e39/independence_wave_focus_tree.focus.html`.
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51f13ab156ec9e9689890320f8bd913e0d8698ea13ba52456a033b72ce4821e5/220e381fcc039b18deabb2d555d789f0044cca5f9e4bbb101a0b26cd9a443545/independence_wave_focus_tree.focus.svg`.
- Render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/db966a432fdc7d3426531a7cbe523012f719342cb3de024be564f19fd42f2128/70132da64a0253bfd3faee654177864098ec1d371ab19b6a475d7517820e95aa/independence_wave_focus_tree.focus.json`.
- Render source map: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/211192fc9ddfe52539625b0810118cbb3f199b07d2cb7bb38921a0ed7c7960f/0fd2b318e808abae397f3ad272b1ef9b08a6df8ca4fab9330e229ae813172056/independence_wave_focus_tree.focus.source-map.json`.
- Render plan: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0824ba95d6186a1028fc5281be2ec09b0aa71f5e9e7d1d55dc3a1cb37eb73862/56433ba32804d0c7202dcd8045c7a1c08b3aadebb99c4c512b959166d1445ca4/independence_wave_focus_tree.focus.plan.json`.

The inspect also reported an inline-source inventory truncation note and one unrelated vanilla continuous-focus localization diagnostic for `continuous_restrict_freedom_desc`.

### Layout warnings

All seven authored warnings point to existing geometry tradeoffs documented in `docs/plans/006_independence_wave_plans/subagent_handoffs/2026-08-22_event6_focus_layout_followup.md`.

| Edge | Source reference | Finding and disposition |
| --- | --- | --- |
| `independence_wave_secure_food_and_fuel` -> `independence_wave_build_regional_transport_authority` | `common/national_focus/006_independence_wave_focus.txt:411-428` | Linear detour; moving the child moves the customs continuation, so no safe one-node fix. |
| `independence_wave_activate_package_economic_program` -> `independence_wave_create_independent_treasury` | `common/national_focus/006_independence_wave_focus.txt:468-487` | Linear detour; the treasury position is constrained by the military cohort. |
| `independence_wave_form_border_guard` -> `independence_wave_adopt_military_archetype_program` | `common/national_focus/006_independence_wave_focus.txt:580-597` | Linear detour; moving the archetype parent would create a two-row military gap or require cohort movement. |
| `independence_wave_adopt_military_archetype_program` -> `independence_wave_standardize_with_league` | `common/national_focus/006_independence_wave_focus.txt:758-776` | Long rightmost choice edge; shortening it risks crossings. |
| `independence_wave_adopt_military_archetype_program` -> `independence_wave_preserve_independent_command` | `common/national_focus/006_independence_wave_focus.txt:778-796` | Long rightmost choice edge; same cohort constraint. |
| `independence_wave_define_former_host_policy` -> `independence_wave_inherit_successor_ledger` | `common/national_focus/006_independence_wave_focus.txt:1592-1610` | Long edge; the left position is occupied by `independence_wave_fortify_former_host_frontier`. |
| `independence_wave_build_postwar_integration_authority` -> `independence_wave_focus_discover_regional_identity` | `common/national_focus/006_independence_wave_focus.txt:1896-1908` | Linear detour; moving it breaks the continuation to `independence_wave_prepare_union_congress`. |

## Route coverage table

The route rows below are evaluated against the accepted shared-tree contract in `docs/events/006_independence_wave/systems/generic_focus_tree.md` and the architecture specification. “Covered” means the shared tree exposes the route and its gate/reward hooks in source; it is not a claim that every package admission or runtime scenario has been proven.

| Required route | Representative focus IDs and source | Audit result |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration`, `independence_wave_name_provisional_authority`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, `independence_wave_complete_founding_settlement` in `common/national_focus/006_independence_wave_focus.txt:100-279` | Covered with visible opening prerequisites, founding rewards, package hooks, and survival capstone gating. |
| Internal power and government | Constitutional lane at `:954-1035`; popular councils at `:1040-1095`; traditional restoration at `:1101-1166`; emergency command at `:1171-1221`; patron-client at `:1228-1294`; radical sovereignty at `:1299-1354`; Saar neutral commission at `:1368-1428` | Covered; six requested power directions plus the neutral commission adaptation are present and mutually exclusive at route entry. |
| Economy and administration | `independence_wave_secure_food_and_fuel`, `independence_wave_build_regional_transport_authority`, `independence_wave_activate_package_economic_program`, and `independence_wave_create_independent_treasury` in `:368-487` | Covered with emergency revenue, food/fuel, transport, customs, package, and treasury progression. |
| Army and security | `independence_wave_form_border_guard`, `independence_wave_adopt_military_archetype_program`, seven archetype children, `independence_wave_standardize_with_league`, `independence_wave_preserve_independent_command`, and `independence_wave_found_professional_defense_institution` in `:494-796` | Covered; military choice endpoints now visibly require the archetype parent, and the standardize/preserve pair is mutually exclusive. The capstone uses intentional OR-pair prerequisite blocks. |
| Diplomacy and recognition | `independence_wave_open_foreign_office`, `independence_wave_send_first_missions`, `independence_wave_seek_neighbor_recognition`, `independence_wave_declare_neutrality`, `independence_wave_balance_patron_relations`, `independence_wave_become_treaty_backed_state`, and `independence_wave_permanent_foreign_service` in `:802-947` | Covered with recognition, patron, neutrality, treaty-backed, trade/postal, and foreign-service hooks. |
| Former host and borders | `independence_wave_define_former_host_policy`, separation/frontier/association/reclamation choices, and `independence_wave_inherit_successor_ledger` in `:1437-1623` | Covered with route mutexes, host-ledger effects, guarded-frontier security, association, and collapse/reclamation hooks. |
| Regional ambition and formables | `independence_wave_survey_regional_identity`, `independence_wave_support_regional_committees`, `independence_wave_prepare_union_congress`, `independence_wave_build_postwar_integration_authority`, and `independence_wave_focus_discover_regional_identity` in `:1624-1700` and `:1896-2086` | Covered in the shared formable framework with registry/readiness gates and integration hooks. |
| Network and league | `independence_wave_recognize_fellow_new_states`, `independence_wave_exchange_civil_servants`, `independence_wave_open_aid_corridor`, `independence_wave_arbitrate_member_disputes`, `independence_wave_draft_league_charter`, `independence_wave_gather_league_members`, `independence_wave_convene_league_congress`, and the five proposal IDs in `:1707-1890` | Covered with network participation gates, charter/congress sequence, and five mutually exclusive league families. |
| High chaos | `independence_wave_sponsor_further_ruptures`, `independence_wave_coordinate_open_fronts`, `independence_wave_proclaim_open_sovereignty`, and `independence_wave_rewrite_regional_borders` in `:2094-2151` | Covered behind regional ambition plus collapse/open-sovereignty gates; effects write revisionist pressure and danger milestones. |
| Package and carrier overlays | 27 shared-focus import roots in `common/national_focus/006_independence_wave_focus.txt:50-93`; additional shared definitions in `006_independence_wave_iw043_iw058_focus.txt`, `006_independence_wave_iw093_iw098_focus.txt`, and `006_independence_wave_pacific_focus.txt` | Covered as additive package-aware overlays in the accepted generic-tree model, not as separate country trees. The source map still marks package admission as HOLD/PARTIAL. |

## Missing or simplified content

- No missing route family was found within the accepted shared generic-tree scope.
- The implementation is intentionally one shared tree with package overlays rather than a separate bespoke tree for every Event 006 country. This is a documented architecture choice in `docs/events/006_independence_wave/systems/generic_focus_tree.md`.
- The current source map records 32 content-attested selectable packages and 161 unattested selectable rows out of 193 non-overlay rows. This is an admission/evidence gap, not a focus graph defect.
- Eight adapter-only rows remain fail-closed in the source map: IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.
- No new route family or broad depth expansion was added because that would exceed this audit's safe patch scope. Use the improvement-loop planner if the parent elects to deepen those package admissions.

## Icon coverage table

| Surface | Result | References and risk |
| --- | --- | --- |
| Focus definitions with icon refs | 318/318 | Four focus files: `006_independence_wave_focus.txt`, `006_independence_wave_iw043_iw058_focus.txt`, `006_independence_wave_iw093_iw098_focus.txt`, `006_independence_wave_pacific_focus.txt`. |
| Unique icon IDs | 121 | Every referenced normal icon has a matching `_shine` definition in the Event 006 GFX files. |
| GFX texture targets | 449 checked, 0 missing | `interface/006_independence_wave*.gfx` texture paths resolve. |
| Repeated family icons | `former_host_settlement` 22; `army_integration` 19; `infrastructure_authority` 18; `founding_administration` 17; `league_congress` 14; `regional_formable` 13; `high_chaos_sovereignty` 13; `recognition_diplomacy` 11 | This is a differentiation/UX risk, not missing asset coverage. Parent review may prioritize unique package icons, but no safe icon substitution was evident in this round. |

## Localization and reward mismatch list

- Static key scan found all 318 focus title keys and all 318 `_desc` keys for the four Event 006 focus files.
- All 318 `custom_effect_tooltip` references resolve in the Event 006 localization files.
- Event 006 localization files retain UTF-8 BOM encoding.
- No focus name/description versus reward mismatch was found in the sampled survival, government, economy, military, diplomacy, former-host, league, formable, or high-chaos lanes.
- Rewards use the shared semantic palette in `common/scripted_effects/006_independence_wave_focus_effects.txt:336-480`, including founding, administration, public settlement, security reform, diplomacy, stabilization, ambition, radicalization, client development, durable state, network cooperation, and league-family effects.
- No localization patch is justified by this audit.

## Prerequisite, mutex, and route-lock findings

- The four focus source files contain 318 unique focus definitions with no duplicate IDs.
- All 375 parsed prerequisite references resolve.
- Fifty-five focus definitions use mutex blocks; all mutex references resolve and the mutex graph has zero asymmetric edges.
- The visible military endpoints `independence_wave_standardize_with_league` and `independence_wave_preserve_independent_command` each require `independence_wave_adopt_military_archetype_program` and mutually exclude the other endpoint at `common/national_focus/006_independence_wave_focus.txt:759-796`.
- The professional-defense capstone at `:600-643` intentionally uses separate prerequisite blocks for AND semantics and paired focus values inside each block for OR semantics. The offline focus-tree wiki confirms that one prerequisite block with multiple focus values is OR, while separate prerequisite blocks are AND.
- Route helpers in `common/scripted_triggers/006_independence_wave_focus_triggers.txt:308-360` fail closed for high-chaos, formable, network, league, and signature-module routes when their framework/readiness/registration gates are absent.
- No prerequisite, mutual-exclusion, bypass, or route-lock patch is required for the audited tree.

## AI behavior gaps

- All 318 parsed definitions have an `ai_will_do` block.
- Generic baseline profiles are present in `common/ai_strategy/006_independence_wave_generic.txt` for survival, recovery, and consolidation, with package-specific AI strategy files under `common/ai_strategy/006_independence_wave_*.txt`.
- Route-aware modifiers are visible in the source, including constitutional, traditional, emergency, patron, war, instability, and network signals. Formable/high-chaos route availability is gated by scripted triggers before selection.
- The required `chaosx_ai_probability_auditor` route and a same-scenario `hoi4.probability_compare` artifact were unavailable in this runtime. Therefore this handoff makes no quantitative focus-weight, MTTH, or scenario-balance claim.
- Parent HOLD: route the named AI scenarios through the probability auditor before changing any complex focus weight or claiming balance. The ICE two-stage target matrix remains source-level design evidence only (`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`).

## High-priority fixes first

1. Keep the seven layout warnings under parent review and only change them as a coordinated lane/cohort move. Do not apply isolated coordinate edits to the edges listed above.
2. Obtain the required probability-auditor route and run baseline/compare scenarios before altering route-aware AI weights.
3. Resolve the source-map package admission/evidence HOLD/PARTIAL state and the eight fail-closed adapter rows before making a whole-event completion claim.
4. If visual differentiation remains a UX concern, schedule a bounded icon-family pass using existing intended assets; no missing icon wiring was found here.

## Changes and validation

Changed files: this handoff only.

Changed focus identifiers: none.

Route behavior before and after: unchanged; no focus rewrite or source patch was applied.

Localization keys and icon IDs changed: none.

Meaningful validation completed: mandatory `hoi4.focus_inspect` and `hoi4.focus_render`; source-level balanced-block/duplicate/reference scan; prerequisite and mutex resolution scan; localization title/description/custom-tooltip scan; Event 006 icon and GFX texture resolution scan; offline Paradox focus-tree/AI wiki and vanilla documentation review.

Meaningful validation skipped: no live HOI4 session by design; no gameplay claim; no `hoi4.focus_rewrite` because no safe in-scope patch existed; no probability baseline/compare because the custom auditor route was unavailable; no broad package admission test because the source map marks those rows incomplete.

## Remaining HOLD items

- The seven authored layout warnings remain as documented geometry tradeoffs.
- Custom probability-auditor evidence and same-scenario compare remain required before any complex AI-weight change or quantitative balance statement.
- Package admission/evidence remains HOLD/PARTIAL for the 161 unattested rows and eight adapter-only rows listed above.
- MCP source inventory emitted `MCP_INLINE_FILES_TRUNCATED`; the direct inspect/render artifacts remain the authoritative layout receipts for this round.
- The unrelated vanilla continuous-focus localization diagnostic for `continuous_restrict_freedom_desc` is outside Event 006 focus ownership and was not changed.

## Handoff

Parent review should use this file together with `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, `docs/plans/006_independence_wave_plans/subagent_handoffs/2026-08-22_event6_focus_layout_followup.md`, and the MCP artifacts above.

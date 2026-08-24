# Event 006 focus audit round 2 — 2026-08-24

## Scope and disposition

This is a read-only audit of the Event 006 shared focus framework and its regional/package overlays against the accepted Event 006 focus specifications, the offline Paradox wiki snapshot, and the installed vanilla documentation.

No gameplay, focus, localization, icon, AI, package, or registry source was changed in this round.

The current source remains one accepted shared tree, `independence_wave_focus_tree`, with 318 focus definitions: 184 direct `focus` blocks and 134 `shared_focus` definitions across four source files, plus 27 main-tree shared-focus import roots. This is intentional architecture, not a missing bespoke tree.

The current acceptance disposition remains **HOLD / PARTIAL**. The latest successful post-economy-spacing receipt reports six authored layout warnings; fresh inspect and render calls in this round each timed out at 180 seconds. Package admission and whole-matrix AI probability evidence also remain incomplete.

## Authority and references reviewed

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md` defines the shared framework, route families, reward depth, overlays, AI, and compact layout contract.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md` defines package levels, the IW-043/IW-058 signature tranche, fourteen regional overlay families, carrier preservation, and fail-closed overlay admission.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md` defines focus acceptance, route-aware AI, asset/localization evidence, and the current HOLD boundary.
- `docs/events/006_independence_wave/systems/generic_focus_tree.md` and `docs/events/006_independence_wave/systems/iw043_iw058_signature_packages.md` define the source-of-truth tree/import and package-focus contracts.
- `docs/specs/006_independence_wave_specs/matrices/006_regional_overlay_matrix.csv` and `006_ai_strategy_matrix.csv` were checked against the source route and AI surfaces.
- Offline references reviewed: `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `Triggers - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, `Modifiers - Hearts of Iron 4 Wiki.md`, `Localisation - Hearts of Iron 4 Wiki.md`, `Scopes - Hearts of Iron 4 Wiki.md`, `On actions - Hearts of Iron 4 Wiki.md`, `Event modding - Hearts of Iron 4 Wiki.md`, `Decision modding - Hearts of Iron 4 Wiki.md`, `Idea modding - Hearts of Iron 4 Wiki.md`, `AI modding - Hearts of Iron 4 Wiki.md`, and `National focus modding - Hearts of Iron 4 Wiki.md`.
- Vanilla references reviewed under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, and `script_collection_input.md`.

## HOI4 MCP evidence and blockers

The required current national-tree calls were attempted against `common/national_focus/006_independence_wave_focus.txt` with tree ID `independence_wave_focus_tree`.

- `hoi4.focus_inspect` returned the exact blocker `tool call error: ... hoi4.focus_inspect ... timed out awaiting tools/call after 180s`.
- `hoi4.focus_render` returned the exact blocker `tool call error: ... hoi4.focus_render ... timed out awaiting tools/call after 180s`.
- These timeouts mean this round cannot claim a new engine-backed layout or route receipt.

The newest successful source-linked receipt is the post-`8f733518e` economy-lane spacing handoff in `006_event6_focus_economy_lane_repair_2026-08-24.md`.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0e68452933823b38c3ff01e63678e9bbf20ad112b9d71ab78a20e38b678c5a1/c8743fb75daf51bb07e272ab6ad802c5d1ec5e4d583a879bb37e771006db1250/focus-inspect.690e185771651b9d.json`.
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3864d32c4c50573e4c3de5f3eeb6422aab1b99d8f0fe478b5d54807dc31c2ae/d6073cf9d633d6f2e2e1cc3818b4d243a90547f94f7c66125508515ee712e776/independence_wave_focus_tree.focus.html`.
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/962730c91f6e0f38a4d0c2ac12cbe523ce7a3f7384a24152f02a61bd0099d53d/e9c07d867076318e0ef5ddf27b347d6b131ec00f767133807303ec867c57294e/independence_wave_focus_tree.focus.svg`.
- Metrics: 184 focuses, 195 connectors, zero connector crossings, zero node intersections, `longConnectorCount = 3`, and six authored Event 006 layout diagnostics.
- The unrelated vanilla continuous-focus diagnostics remain outside Event 006 ownership.

The parent-owned economy repair already moved `independence_wave_build_regional_transport_authority`, `independence_wave_establish_customs_service`, and `independence_wave_activate_package_economic_program` to the contiguous `x = 32`, `y = 4/5/6` lane. The retired `secure_food_and_fuel` to `build_regional_transport_authority` warning is not a current issue and is not repeated below.

The required weighted-logic route was covered by the current `chaosx_ai_probability_auditor` handoff `006_event6_probability_audit_round_2026_08_24.md`, but focus selection remains score-only and incomplete: the source inspection found 184 candidates with `poolComplete = false`, the named focus evaluation returned `PROBABILITY_ANALYZED_PARTIAL` with 1,033 unresolved items and 226 diagnostics, and the same-scenario compare returned `PROBABILITY_ANALYZED_PARTIAL` with zero comparison changes but the same 1,033 unresolved items and 226 diagnostics. The key focus artifacts are `probability-inspect-a7b3360d379f.json`, `probability-5157df1afa15b89c3fa9403f.json`, and `probability-9c3e17ba0ecee58955e1e17c.json` under the `hoi4-agent://` workspace artifacts recorded in that handoff. No quantitative focus balance claim is made.

## Route coverage table

| Accepted route family | Current focus IDs and source | Audit result |
| --- | --- | --- |
| Survival and state construction | `independence_wave_prepare_capital_administration`, `independence_wave_name_provisional_authority`, `independence_wave_inventory_the_state`, `independence_wave_bind_the_first_oath`, and `independence_wave_complete_founding_settlement` in `common/national_focus/006_independence_wave_focus.txt:100-279` | Covered with visible opening prerequisites, founding effects, package hooks, and a durable-state continuation. |
| Government and internal power | Constitutional `independence_wave_prepare_first_assembly` through `independence_wave_consolidate_constitutional_state`; popular `independence_wave_organize_popular_councils` through `independence_wave_proclaim_council_commonwealth`; traditional `independence_wave_prepare_traditional_confirmation` through `independence_wave_crown_the_restored_state`; emergency `independence_wave_establish_emergency_command` through `independence_wave_entrench_emergency_state`; patron-client `independence_wave_open_guarantor_talks` through `independence_wave_become_bargaining_client`; radical sovereignty in `:955-1366`; Saar neutral commission in `:1372-1428` | Covered; route entries use explicit availability and mutual-exclusion logic, including the neutral-commission adaptation. |
| Economy, infrastructure, and administration | `independence_wave_establish_emergency_revenue`, `independence_wave_secure_food_and_fuel`, `independence_wave_build_regional_transport_authority`, `independence_wave_establish_customs_service`, `independence_wave_activate_package_economic_program`, and `independence_wave_create_independent_treasury` in `:368-487` | Covered; the repaired contiguous transport/customs/program lane is current. One treasury detour remains a geometry warning. |
| Army, security, and military identity | `independence_wave_integrate_militia_commands`, `independence_wave_secure_national_depots`, `independence_wave_recall_and_vet_officers`, `independence_wave_form_border_guard`, `independence_wave_adopt_military_archetype_program`, the ten military choice focuses in `:642-796`, and `independence_wave_found_professional_defense_institution` in `:600-796` | Covered with researched force-profile, security, doctrine, command, and mutually exclusive endpoint rewards. The remaining geometry warnings are cohort/layout risks, not route omissions. |
| Diplomacy, recognition, and patrons | `independence_wave_establish_foreign_office`, `independence_wave_send_first_missions`, `independence_wave_seek_neighbor_recognition`, `independence_wave_declare_entrenched_neutrality`, `independence_wave_balance_the_first_patrons`, `independence_wave_become_treaty_backed_state`, and `independence_wave_focus_build_permanent_foreign_service` in `:803-947` | Covered with recognition, patron-balance, neutrality, treaty, and foreign-service effects. |
| Former host and borders | `independence_wave_define_former_host_policy`, the negotiated, guarded-frontier, association, reclamation, and collapse branches, and `independence_wave_inherit_successor_ledger` in `:1437-1623` | Covered with route mutexes, bilateral ledger helpers, host-state gates, and the separate collapsed-host branch. The long collapsed-host edge remains a layout warning. |
| Regional ambition and formables | `independence_wave_survey_regional_ambition`, `independence_wave_support_local_committees`, `independence_wave_call_regional_congress`, `independence_wave_build_postwar_integration_authority`, `independence_wave_focus_discover_regional_identity`, `independence_wave_prepare_union_congress`, `independence_wave_write_formation_terms`, and `independence_wave_establish_integration_commission` in `:1630-1700` and `:1897-2086` | Covered behind regional readiness, registry, claims, consent, and integration hooks. The postwar-to-discovery edge remains a geometry warning. |
| Network and league | `independence_wave_recognize_fellow_new_states`, `independence_wave_exchange_civil_servants`, `independence_wave_establish_aid_corridor`, `independence_wave_propose_network_arbitration`, `independence_wave_draft_league_charter`, `independence_wave_gather_founding_members`, `independence_wave_convene_league_congress`, and the five mutually exclusive proposal focuses in `:1708-1890` | Covered with network participation, aid, arbitration, charter, congress, and proposal-family gates. |
| Formables and high chaos | `independence_wave_sponsor_further_ruptures`, `independence_wave_focus_coordinate_reclamation_fronts`, `independence_wave_proclaim_open_sovereignty`, `independence_wave_rewrite_charter_of_borders`, and `independence_wave_secure_durable_sovereignty` in `:2095-2151` and `:3370-3387` | Covered behind high-chaos, regional, host, and durable-sovereignty gates; no unguarded high-chaos fallback was found. |

No accepted route family is missing from the shared framework. The one-tree architecture is an explicit Event 006 decision, and the current package-admission gap must not be misreported as a missing focus route.

## Regional and package overlay coverage

| Source file | Resolved overlay groups | Current route evidence |
| --- | --- | --- |
| `common/national_focus/006_independence_wave_focus.txt:50-93` | 27 import roots, including COR, HBX, HAW, FIJ, IW-043, IW-058, IW-093, IW-098, and CAT roots | Imports are explicit because vanilla shared-focus resolution pulls prerequisite ancestors but not disconnected descendant siblings. |
| `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` | 48 shared focuses: 23 IW-043 and 25 IW-058 | Opening, economy/security, constitutional, restoration/civic, emergency, host, and FORM-12/13/18 terminal branches use exact package triggers, custom tooltips, helper effects, and route mutexes. Main-tree imports at `:57-67` preserve disconnected economy/emergency spurs. |
| `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` | 43 shared focuses: 21 IW-093 and 22 IW-098 | Asante and Sokoto administration, economy, military, host, constitutional/traditional/emergency branches, and FORM-24/25 preparations are package-gated. Main-tree roots at `:69-84` import the terminal and sibling branches. |
| `common/national_focus/006_independence_wave_pacific_focus.txt` | 20 shared focuses: 7 HBX, 7 HAW, and 6 FIJ | Pacific arsenal, shipping, civic, coastwatch, labor, settlement, and island-compact branches use exact package gates and are imported from the main tree. |

Source checks found 318 unique focus IDs with no duplicates, 318 `ai_will_do` blocks, and 134 shared-focus definitions. The overlay source is structurally complete for the implemented package groups, but source presence is not central admission: the current ledger remains at 32 content-attested selectable packages, 161 unattested selectable rows out of 193 non-overlay rows, and eight adapter-only fail-closed rows (IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM).

The fourteen-family regional matrix is design coverage, not a whole-matrix runtime receipt. Carrier preservation, one-time activation, route-state, origin, identity, assets, cleanup, AI, and probability evidence remain package-specific acceptance obligations.

## Missing or simplified content

- No route family is missing within the accepted shared-tree scope.
- No bespoke per-country tree was added because the accepted Event 006 architecture explicitly requires one shared framework plus reviewed overlays.
- Six authored layout warnings remain after the economy-lane repair. The source-linked per-edge table is below; the latest post-repair handoff groups the diagnostics as a treasury detour, a military-archetype detour, three military-archetype long/choice connectors, a former-host connector, and a postwar/formable detour. The exact source-linked edge list available from the prior inspect is two military long edges plus the military parent detour; the category wording is retained as an MCP diagnostic-count uncertainty rather than silently normalized.
- Package admission remains HOLD/PARTIAL for the 161 unattested rows and eight adapter-only rows. This is an evidence and runtime-admission gap, not permission to create generic fallback focuses.
- The MCP source inventory can emit `MCP_INLINE_FILES_TRUNCATED`; the dated successful artifacts remain the usable layout evidence until inspect/render completes again.

### Current authored layout warnings

| Current edge | File and focus IDs | Current source geometry | Safe disposition |
| --- | --- | --- | --- |
| Treasury detour | `common/national_focus/006_independence_wave_focus.txt:450-487`, `independence_wave_activate_package_economic_program` -> `independence_wave_create_independent_treasury` | `x = 32, y = 6` -> `x = 28, y = 8` | Leave for a coordinated economy/military reflow; moving the treasury to `x = 32` collides with the row-8 military cohort and changes its durable-sovereignty alignment. |
| Military parent detour | `:561-597`, `independence_wave_form_border_guard` -> `independence_wave_adopt_military_archetype_program` | `x = 38, y = 5` -> `x = 36, y = 7` | Leave for the bounded military-cohort tranche; moving only the parent creates an avoidable gap to its direct children. |
| League-standardization long edge | `:581-776`, `independence_wave_adopt_military_archetype_program` -> `independence_wave_standardize_with_league` | `x = 36, y = 7` -> `x = 47, y = 8` | Leave until the entire military choice row is reflowed. |
| Independent-command long edge | `:581-796`, `independence_wave_adopt_military_archetype_program` -> `independence_wave_preserve_independent_command` | `x = 36, y = 7` -> `x = 49, y = 8` | Leave until the entire military choice row is reflowed; preserve the visible mutex and parent gate. |
| Collapsed-host long edge | `:1437-1610`, `independence_wave_define_former_host_policy` -> `independence_wave_inherit_successor_ledger` | `x = 50, y = 4` -> `x = 59, y = 5` | Leave; the nearer row-5 space is occupied by the living-host frontier branch. |
| Formable discovery detour | `:1675-1908`, `independence_wave_build_postwar_integration_authority` -> `independence_wave_focus_discover_regional_identity` | `x = 50, y = 11` -> `x = 52, y = 12` | Leave; moving discovery breaks its aligned continuation to `independence_wave_prepare_union_congress`. |

## Icon coverage table

| Surface | Current result | Evidence and risk |
| --- | --- | --- |
| Event 006 focus definitions | 318/318 have an icon reference | Four focus source files listed above. |
| Unique Event 006 focus icon IDs | 121 normal IDs | Every referenced normal ID has a matching `_shine` registration in the Event 006 GFX surfaces. |
| Event 006 GFX texture targets | 449 checked, 0 missing in the latest static audit | No missing focus texture or GFX path was found. |
| IW-043/IW-058 package families | 20 unique package icon families with matching shine sprites | `interface/006_independence_wave_iw043_iw058_focus_icons.gfx` and `gfx/interface/goals/006_independence_wave/volga_assyria/`. |
| Repeated generic families | `former_host_settlement` 22, `army_integration` 19, `infrastructure_authority` 18, `founding_administration` 17, `league_congress` 14, `regional_formable` 13, `high_chaos_sovereignty` 13, `recognition_diplomacy` 11 | Differentiation/UX risk only; no safe existing replacement was proven and no asset generation is in scope for this audit. |

## Localization and reward mismatch list

Current source scans over the four focus files found 318 focus IDs, 318 custom-effect tooltip references, zero duplicate IDs, zero missing title keys, zero missing `_desc` keys, and zero missing tooltip keys across the 73 Event 006 English localization files. The localization sources retain UTF-8 BOM encoding.

The shared effect palette in `common/scripted_effects/006_independence_wave_focus_effects.txt:336-480` covers founding, administration, public settlement, security, diplomacy, stabilization, ambition, radicalization, client development, network cooperation, league-family, and durable-state outcomes. The prior route audit found no name/description versus reward mismatch in the survival, government, economy, military, diplomacy, host, league, formable, or high-chaos samples.

No localization, reward, icon, prerequisite, mutex, bypass, or route-lock patch is justified by this round.

## AI behavior gaps

- All 318 focus definitions have `ai_will_do` blocks.
- Generic AI profiles in `common/ai_strategy/006_independence_wave_generic.txt` provide survival, recovery, consolidation, war restraint, and route signals; package strategy files add exact package, crisis, patron, host, league, and route gates.
- Focus source contains route-aware modifiers for constitutional, traditional, emergency, patron, war, instability, network, formable, and high-chaos state. Focus availability and scripted route helpers fail closed for impossible package/formable/league/high-chaos routes.
- Focus probability remains unresolved for balance purposes. The probability-auditor source inspection and partial evaluations require a country-specific available pool, prerequisite-completion map, external patron/former-host state, package identity, and strategy state before ranking conclusions. Do not change focus weights or claim route balance from the global 184-focus ranking.

## High-priority fixes first

1. Resolve the military cohort geometry in one parent-owned layout tranche, preserving all IDs, prerequisites, mutexes, effects, AI, localization, and icons.
2. Reinspect the treasury detour and the two non-military warnings only after the military cohort result is known; do not move convergence or formable-anchor nodes in isolation.
3. Run the named focus scenarios through `chaosx_ai_probability_auditor` with a complete country-specific pool and same-scenario before/after comparison before any AI-weight change.
4. Keep the 161 unattested package rows and eight adapter-only rows fail-closed until each package meets the accepted identity, host, map, force, rights, asset, AI, cleanup, and probability contract.

## One bounded focus tranche advancing accepted design

### Military archetype choice-cohort reflow

The next bounded tranche should be a layout-only reflow of the military archetype cohort in `common/national_focus/006_independence_wave_focus.txt`.

Exact focus IDs are `independence_wave_form_border_guard` (line 561), `independence_wave_adopt_military_archetype_program` (line 581), `independence_wave_found_professional_defense_institution` (line 600), `independence_wave_confirm_civilian_control` (line 642), `independence_wave_grant_military_autonomy` (line 656), `independence_wave_raise_mass_reserve` (line 670), `independence_wave_build_professional_core` (line 684), `independence_wave_fund_domestic_arsenals` (line 698), `independence_wave_accept_foreign_arms` (line 712), `independence_wave_adopt_border_defense` (line 726), `independence_wave_adopt_reclamation_doctrine` (line 740), `independence_wave_standardize_with_league` (line 759), and `independence_wave_preserve_independent_command` (line 779).

The tranche should treat the parent, its row-8 choice cohort, and the professional-defense convergence as one geometry unit. It must preserve the visible parent prerequisites where present, the `available` parent/route gates including the deliberate tooltip-only parent gate on `independence_wave_adopt_reclamation_doctrine`, all choice mutual exclusions, and every completion reward/helper. It should not add a route, package, reward, AI factor, localization key, or asset.

The tranche advances the accepted design by making the required military identity route compact and legible while retaining the current eight/ten choice semantics and downstream capstone. It is not safe to apply as an isolated coordinate edit because the current receipts explicitly identify the parent detour and rightmost choice edges as a single military cohort tradeoff.

Required evidence before acceptance is a successful pre-change and post-change `hoi4.focus_inspect` plus `hoi4.focus_render` for the same tree, with zero crossings and zero node intersections preserved, no isolated choice focus, no new authored warnings, and a reduced authored-warning count or a documented reason for any retained warning. A source prerequisite/mutex/tooltip/icon scan must accompany the render. No probability compare is required for a coordinate-only patch, but any AI-weight edit reopens the mandatory probability-auditor route.

This tranche is identified only; no `hoi4.focus_rewrite` was attempted because both current inspect/render calls timed out and no safe coordinate proposal was available in this round.

## Changes, validation, and remaining blockers

Changed gameplay files: none.

Changed focus IDs: none.

Changed localization keys or icon IDs: none.

Static validation completed: current focus-ID/duplicate scan, `ai_will_do` count, custom-tooltip key parity, title/description key parity, icon-reference/GFX-definition parity, source route review, package import review, and prerequisite/mutex reference review.

MCP validation completed: mandatory current `hoi4.focus_inspect` and `hoi4.focus_render` attempts, both recorded as exact 180-second timeout blockers; the latest successful post-economy-spacing inspect/render artifacts are preserved above.

Probability validation completed: the named `chaosx_ai_probability_auditor` handoff was reviewed; source-qualified focus inspection and partial named-scenario evaluation/compare artifacts are recorded, but they do not close the incomplete pool or support a quantitative balance claim.

Skipped meaningful validation: no `hoi4.focus_rewrite` because no safe patch was authorized by the available engine evidence; no live game or save validation by design; no broad package admission test because the current ledger remains fail-closed; no focus weight change was made.

Remaining route risks are the six authored layout warnings, incomplete country-specific focus probability pool, 161 unattested selectable packages, eight adapter-only rows, and the inability to refresh current engine artifacts due to the two 180-second MCP timeouts.

No separate improvement-loop plan was written because the tree is not shallow within the accepted shared-tree scope and the identified next step is a bounded layout cohort rather than a new route family.


# Event 006 focus-gap inventory — 2026-09-03

## Status

This is a read-only audit of the Event 006 focus framework and its shared-focus overlays. No gameplay, localisation, icon, or AI source file was changed, and no commit was created. The worktree was already dirty, so unrelated concurrent changes were preserved.

The audit covers `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`, `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, their Event 006 localisation and GFX registries, `common/scripted_triggers/006_independence_wave_focus_triggers.txt`, `common/scripted_effects/006_independence_wave_focus_effects.txt`, the central Event 006 decision registry, the accepted Part 4 focus architecture, and the accepted focus lane map.

Required offline Paradox wiki pages and the relevant vanilla national-focus documentation were consulted. Vanilla `common/national_focus/generic.txt` was used as a syntax precedent for `focus_tree`, `initial_show_position`, `relative_position_id`, `mutually_exclusive`, `search_filters`, and `ai_will_do`.

## MCP evidence

The authoritative main-tree inspect was run against `common/national_focus/006_independence_wave_focus.txt` with tree id `independence_wave_focus_tree`.

* `focusCount = 184` direct focuses, `branchCount = 0`, and `resolvedTitleCount = 184`.
* `195` connectors were resolved with zero crossings, zero node intersections, zero long connectors, and zero same-row spacing violations.
* The layout bounds are columns `1..121` and rows `0..19`, with layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`.
* The inspect validation passed with no Event 006 blocking diagnostic. The only warning is the unrelated vanilla `continuous_restrict_freedom_desc` reference.
* Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7852b802bbc412b11fe1cbcf230dee9a50fa8c7d1185731607e4225f9227cebc/4acdb762ff081604b409504b0b5c94feb75d379b884a4c52235fc59b4537bd72/focus-inspect.fe072cf27a0069b4.json`.

The production render also passed with the same layout hash and no blocking diagnostic.

* HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c904d3fa0fd6d520384359486d318966899cde16b4b63c47d406b8a60cabdc18/a68e27b940ad4ae80bd44fd1e585578b2b092b631a2990865344306b0bd43bc8/independence_wave_focus_tree.focus.html`.
* SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/790ac83c6f2cdb9816133b30e7a650f0e74f3823cf45efd0753fa9182ec87279/9617cbd640445314ed843c28369750904fa5369579099cc800d8e8b5089586e0/independence_wave_focus_tree.focus.svg`.
* JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a88758d9b59353c91553163f9cfae1bb68319233737b1af4833670b578a1985b/363c454ea45bbe76007eabac41a6f7e2de63a68275879054afc919fd6bc5ad73/independence_wave_focus_tree.focus.json`.

The two overlay-only sources were inspected separately. `006_independence_wave_iw043_iw058_focus.txt` and `006_independence_wave_iw093_iw098_focus.txt` each return `FOCUS_TREE_NOT_FOUND` with the message `The selected source contains no national focus tree`; they contain `shared_focus` definitions only. This is expected overlay behavior and is not a source defect.

The weighted-surface discovery pass was run against the current main source with adapter `national_focus_ai_will_do`.

* The source was discovered successfully with `184` candidates, `0` available candidates without a typed world state, `requiredInputs = 17`, and `poolComplete = false`.
* Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99b52c0a49a424c62e99b029a56c1a5f759487c23647e057a808a4006b4bd4e1/3960e662f85eb94bb32471e9562f1f378f1c60ed3ff408ea437aaa5a9a4d41c4/probability-inspect-3fa1ff409553.json`.
* No callable `chaosx_ai_probability_auditor` route is exposed in this runtime. Typed scenario evaluation and the mandatory same-scenario compare therefore remain unresolved and are explicitly handed to the parent.

## Route coverage table

The main tree contains 184 direct focus blocks. The three Event 006 source files contain 318 distinct focus/shared-focus blocks in total; the additional 134 are shared definitions and package overlays used by the one tree.

| Lane or route family | Source coverage | Representative ids and source range | Audit result |
| --- | ---: | --- | --- |
| Survival and state construction | 8 focuses | `independence_wave_prepare_capital_administration` through `independence_wave_complete_founding_settlement`, `006_independence_wave_focus.txt:99-302` | Complete trunk with capital, authority, inventory, oath, ministries, communications, provincial compacts, and founding capstone. |
| Optional internal power struggle | 4 focuses | `independence_wave_map_internal_power_centers`, `independence_wave_favor_first_power_center`, `independence_wave_broker_internal_power_compromise`, `independence_wave_favor_second_power_center`, `006_independence_wave_focus.txt:303-366` | Correctly package-gated and multi-outcome. |
| Economy, food, transport, customs, and treasury | 6 focuses | `independence_wave_establish_emergency_revenue` through `independence_wave_create_independent_treasury`, `006_independence_wave_focus.txt:367-492` | Complete lane with varied material, technology, capacity, and treasury rewards. |
| Army and military identity | 16 focuses | `independence_wave_integrate_militia_commands` through `independence_wave_preserve_independent_command`, `006_independence_wave_focus.txt:493-801` | Complete civilian/military, mass/professional, domestic/foreign, defense/reclamation, and league/independent choices. One missing visual prerequisite is listed below. |
| Diplomacy, recognition, and patrons | 7 focuses | `independence_wave_establish_foreign_office` through `independence_wave_focus_build_permanent_foreign_service`, `006_independence_wave_focus.txt:802-952` | Complete recognition, neutrality, patron-balancing, treaty, and permanent-service lane. |
| Government settlements | 27 normal-route focuses plus 4 Saar focuses | Constitutional, Popular Council, Traditional, Emergency Military, Patron Client, Radical Sovereignty, and Saar neutral commission, `006_independence_wave_focus.txt:953-1433` | All seven accepted settlement families are represented, mutually exclusive, package-gated, and mechanically distinct. |
| Former-host settlement | 13 focuses | `independence_wave_define_former_host_policy` through `independence_wave_settle_empty_claim`, `006_independence_wave_focus.txt:1434-1628` | Negotiated, guarded, association, reclamation, and collapsed-host paths are present and ledger-backed. |
| Regional ambition and signature extension | 5 focuses | `independence_wave_survey_regional_ambition` through `independence_wave_open_signature_extension`, `006_independence_wave_focus.txt:1629-1705` | Complete shared ambition entry and package-owned signature hook. |
| Network and league | 12 focuses | `independence_wave_recognize_fellow_new_states` through five charter proposals, `006_independence_wave_focus.txt:1706-1895` | Complete network, civil-service, aid, arbitration, charter, member-gathering, congress, and five proposal families. Votes and proclamation are intentionally decision-owned. |
| Formable preparation and FORM-03 extension | 10 focuses | `independence_wave_focus_discover_regional_identity` through `independence_wave_form03_submit_low_countries_compact`, `006_independence_wave_focus.txt:1896-2091` | Complete generic preparation plus FORM-03 package extension. The direct League-to-formable visual edge is simplified; see below. |
| Hidden high-chaos sovereignty | 4 focuses | `independence_wave_sponsor_further_ruptures` through `independence_wave_rewrite_charter_of_borders`, `006_independence_wave_focus.txt:2092-2156` | Present, hidden by `allow_branch`, and gated by world collapse, radical route, or open-sovereignty evolution. |
| Package and regional modules | 67 direct focuses plus shared package definitions | Scotland, Wales, Saar, Brittany, Wallonia, Frisia, Rhineland, Bavaria, Sardinia, Sicily, and other package anchors, `006_independence_wave_focus.txt:2157-3368` and the two overlay sources | Broad package coverage is present; no bespoke second tree is introduced. |
| Framework capstone and retained-tree overlays | 1 capstone plus 43 shared overlay focuses | `independence_wave_secure_durable_sovereignty`, `006_independence_wave_focus.txt:3369-3563` | Full-tree capstone and additive retained-tree contract are wired. |

## Missing or simplified content

### P1 candidate: reclamation choice has a missing source prerequisite connector

`independence_wave_adopt_reclamation_doctrine` at `common/national_focus/006_independence_wave_focus.txt:743-759` has `available = { has_completed_focus = independence_wave_adopt_military_archetype_program ... }`, but it has no `prerequisite = { focus = independence_wave_adopt_military_archetype_program }`. Its sibling choices at `:646`, `:660`, `:674`, `:688`, `:702`, `:716`, `:730`, and `:763` all carry the archetype prerequisite. The completion gate is therefore functionally safe for a human player, but the missing connector weakens the visible route graph and AI prerequisite semantics. A one-line prerequisite addition is source-correct and bounded, but was deliberately not applied in this read-only audit.

### Potential lane-map simplification: League-to-formable is indirect

`independence_wave_focus_discover_regional_identity` at `common/national_focus/006_independence_wave_focus.txt:1900-1911` has only `prerequisite = { focus = independence_wave_build_postwar_integration_authority }`; no League focus is a direct prerequisite. This omits the explicit `L -> F` edge drawn in `docs/specs/006_independence_wave_specs/diagrams/006_focus_tree_lane_map.md`. It is not a confirmed runtime defect because the source explicitly states that decisions own discovery at `:1896-1897`, DM-53 `independence_wave_discover_regional_identity` is wired at `common/decisions/006_independence_wave_decisions.txt:3456`, and `has_independence_wave_formable_discovery_gate` accepts `revealed_by_league_state` through `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:804-831`. Parent review should decide whether the lane map requires a visible focus edge or whether this decision-owned indirection is the accepted contract.

### Failure-state presentation is not a separate government focus branch

The normal government route set at `common/national_focus/006_independence_wave_focus.txt:953-1433` contains six general settlements plus the Saar neutral commission, but no dedicated focus ids for route failure, coup, or fractured settlement. Crisis/failure behavior is represented in the shared decision/effect systems and in the Emergency Military, former-host collapse, and high-chaos branches. This is a design simplification to keep queued unless Part 4 requires failure to be a visible focus branch rather than a decision/effect outcome.

### League institutional follow-through is intentionally decision-owned

The focus source comment at `common/national_focus/006_independence_wave_focus.txt:1706-1708` says that the focus lane publishes proposals while decisions own votes and proclamation. The ownership is present: DM-45 founding congress is at `common/decisions/006_independence_wave_decisions.txt:2674`, DM-46 charter pillar adoption and formal proclamation at `:2728`, DM-47 leadership challenge at `:2823`, and member invitation/acceptance actions are in `common/decisions/006_independence_wave_shared_decisions.txt:256-349`. Secretariat, membership, leadership, and proclamation are therefore not missing focus wiring.

## Icon coverage table

| Surface | Static result | Evidence |
| --- | --- | --- |
| Main and overlay focus references | 318 source icon tokens, 121 unique ids | Parsed from all three focus sources. |
| GFX registration | 0 missing definitions | Every unique icon id is defined in `interface/006_independence_wave.gfx`, `interface/006_independence_wave_small_assets.gfx`, or `interface/006_independence_wave_iw093_iw098_focus.gfx`. |
| Shine siblings | 0 missing `_shine` ids | Every source icon has a matching shine definition. |
| Texture files | 0 missing referenced textures | Every base icon definition resolves to an existing DDS texture. |
| MCP render asset scan | Main generic and package textures resolved | The inspect/render artifacts scan the generic family, FORM-03, AFX, Rhineland/Bavaria, Mediterranean, Pacific, and IW-093/IW-098 goal textures. |

The wiring is complete, but icon reuse is visually repetitive. The most reused families are `GFX_goal_independence_wave_former_host_settlement` (22), `..._army_integration` (19), `..._infrastructure_authority` (18), `..._founding_administration` (17), `..._league_congress` (14), `..._regional_formable` (13), `..._high_chaos_sovereignty` (13), and `..._recognition_diplomacy` (11). This is a quality/design gap against the Part 4 direction that coordinated route icons should not all be identical, not an asset-wiring failure. It should be handled as a separate icon-art tranche rather than by changing focus ids in this audit.

## Localisation and reward mismatch list

No structural localisation gaps were found.

* All 318 focus/shared-focus blocks have title and description keys in the union of the 37 Event 006 English localisation files.
* All 318 `custom_effect_tooltip` references resolve to localisation keys.
* All 318 blocks contain a `completion_reward` and a custom effect tooltip.
* The main direct tree uses route-specific reward bundles and callbacks; package, Saar, FORM-03, IW-043/IW-058, and IW-093/IW-098 blocks use package-owned effects where appropriate. The static pass found no title/description/tooltip key mismatch.

The semantic wording pass was structural plus targeted sampling, not a prose adjudication of every one of 318 descriptions. Parent review should still spot-check any reward changed in a future implementation tranche.

## AI behavior gaps

The direct main tree has `ai_will_do` on all 184 focuses. Static parsing finds 92 base-only blocks and 92 blocks with at least one modifier. Base values are `high = 112`, `urgent = 57`, `standard = 12`, and `cautious = 3`. Only 30 direct blocks reference `has_completed_focus` or `has_focus` inside their AI block, and many economy, diplomacy, formable, package, and late identity focuses rely on a bare high/urgent base after their availability gates.

The route-choice AI is materially better than the generic nodes. Examples include military route modifiers at `common/national_focus/006_independence_wave_focus.txt:646-795`, charter proposal modifiers at `:1824-1894`, high-chaos world-collapse modifiers at `:2097-2155`, and package-specific route roots throughout `:2157-3368`. This prevents calling the tree AI-empty.

The remaining gap is route-aware selection depth. The accepted AI matrix asks the generic profile to read package, government posture, legitimacy, patron dependence, host threat, league route, and chaos state, but the shared tree has no dedicated `focus_factors` surface and 92 nodes are base-only. The current probability inspect cannot evaluate dominance or starvation without typed world-state fixtures, and the named `chaosx_ai_probability_auditor` route is not callable in this runtime. Existing Event 006 probability handoffs also record unresolved focus evaluations, so no balance conclusion is claimed here.

## High-priority fixes first

1. Add the missing `independence_wave_adopt_military_archetype_program` prerequisite to `independence_wave_adopt_reclamation_doctrine` at `common/national_focus/006_independence_wave_focus.txt:743` and rerun focus inspect/render. This is the only clearly local source fix found.
2. Parent-review the strict `L -> F` lane-map requirement. If a direct focus edge is mandatory, design one guarded OR prerequisite or a named bridge that preserves the decision-owned discovery contract; do not blindly add a second formable route.
3. Provide typed focus-AI fixtures for fragile survival, constitutional, patron-dependent, league internationalist, radical/high-chaos, former-host revanchist, and formable-pursuer states, then route `probability_inspect`, `probability_evaluate`, and same-scenario `probability_compare` through `chaosx_ai_probability_auditor` before changing weights.
4. After balance evidence exists, add only route-aware modifiers that improve package/government/patron/league selection without making high-chaos or reclamation the generic default.
5. Treat repeated generic family icons as a separate visual tranche; all current references are registered and renderable.

## One bounded implementation tranche for the parent

Execute a shared route-reachability and AI-evidence tranche with no new route family:

1. Apply the one-line reclamation prerequisite fix and capture before/after focus inspect/render artifacts.
2. Verify the formable discovery decision path against the League-state discovery mode. If the direct `L -> F` edge is required by acceptance, make one minimal guarded bridge; otherwise document the decision-owned indirection in the accepted lane-map record.
3. Build the seven named typed AI fixtures and run the required probability inspect/evaluate/compare workflow through the probability auditor. Keep unchanged weights where the evidence does not show starvation, invalid-route selection, or suicide-war pressure.
4. Spot-check the changed focus title, description, tooltip, reward callback, icon, mutual exclusion, and `allow_branch` behavior, then rerun the main-tree MCP inspect/render.

This tranche is bounded to one existing focus prerequisite, one reachability decision, and evidence-backed AI modifiers. It does not add a new government route, formable chain, or bespoke country tree.

## Remaining limits and simplifications

* No source patch was applied because the parent requested a read-only inventory and the missing connector is functionally gated already.
* The custom probability-auditor route was unavailable; current direct discovery confirms the surface but cannot substitute for typed scenario evaluation and compare.
* Overlay-only `FOCUS_TREE_NOT_FOUND` is an expected shared-focus limitation and must not be filed as a source defect.
* The MCP inspect warning for vanilla `continuous_restrict_freedom_desc` is unrelated to Event 006.
* No live HOI4 run was performed; live consumer validation remains parent/user-owned.

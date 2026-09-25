# Event 006 Independence Wave focus framework audit — 2026-09-25

## Disposition

Read-only audit of the accepted focus architecture, lane map, regional overlay matrix, AI strategy matrix, and current focus receipts. No gameplay, localization, GFX, or asset source was changed, and no focus ID changed.

The scoped framework is broadly implemented with substantial route depth. One discovery-gate semantic gap needs parent disposition: the `revealed_by_league_state` formable mode accepts League-route eligibility before a caucus, charter, or member vote. No literal League-to-formable focus prerequisite is required by the accepted lane map.

## Scope and references

Reviewed `common/national_focus/006_independence_wave_focus.txt`, `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`, and `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`.

Cross-referenced `common/scripted_triggers/006_independence_wave_focus_triggers.txt`, `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`, `common/scripted_effects/006_independence_wave_focus_effects.txt`, `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`, and `common/decisions/006_independence_wave_decisions.txt` only where needed to verify focus gates and ownership of League/formable transactions.

Compared the sources with Part 4 focus architecture, Part 5 package and regional overlay design, Part 6 discovery and League rules, Part 7 AI and focus acceptance, `diagrams/006_focus_tree_lane_map.md`, `matrices/006_regional_overlay_matrix.csv`, and `matrices/006_ai_strategy_matrix.csv` under `docs/specs/006_independence_wave_specs/`.

Read the current receipts `006_event6_focus_prerequisite_repair_2026-09-08.md`, `006_event6_focus_mcp_review_2026-09-20.md`, and `006_event6_focus_geometry_refresh_2026-09-25.md`. Treated `006_event6_focus_gap_inventory_2026-09-03.md` as historical only; its missing reclamation connector finding is superseded by the 2026-09-08 repair and current inspect result.

Applied `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, `.agents/skills/chaos-redux-improvement-loop/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

Consulted the required offline Paradox wiki focus-modification reference and the required core wiki snapshots for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding. For vanilla precedent and engine documentation, consulted the installed `documentation` references and `common/national_focus/generic.txt`, including the `army_effort` to `equipment_effort` prerequisite pattern. No Paradox wiki web page was used.

## Current MCP evidence

Fresh `hoi4.focus_inspect` and `hoi4.focus_render` calls completed for `independence_wave_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

The fresh inspect returned source revision `519001605a2e45334e8a30932ef9ce0f39f3ca5f5a2876ebdee4de14705458c4`. This differs from the supplied current receipt revision `a634332e13a8b44e25db76bf1bf537dc72ee4e8d7d43adf64057443d1ccda7c5`; both report layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7` and the same 184-focus, 196-connector geometry counts. No source edits were made during this audit to explain the revision difference.

The fresh inspect reports zero crossings, zero intersections, and zero same-row violations. It reports one nonblocking `FOCUS_LAYOUT_LONG_CONNECTOR` from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine`, spanning 10 columns and one row. This is the accepted edge already documented in the 2026-09-25 geometry receipt. The other diagnostic is the unrelated vanilla `continuous_restrict_freedom_desc` localization warning. Focus diagnostics passed with no blocking findings.

The renderer produced a 16,068 × 1,830 review view at `reviewScale = 0.75`. The inspect artifact is [focus-inspect.519001605a2e.json](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4167eb3cdb5b8d2c967a16a52d9628f0c7e0757f99c91ee45462c4068f659e14/85d9574e86c258f977cee7032d0039b832878d9b38fc7bfd40a3bbec31001cfc/focus-inspect.519001605a2e.json). The rendered [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2b282094ed9cf36d4fb4add8a8b80205a8cd8d12e2e396c2e4f1f9f48302602/ca5d3e729d6c11d1c3b6d62d9b0fe52e1921275e6f42d74c2af338f4f392497b/independence_wave_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/352b090f1cd955f9cbb30a41e0ae581761c08f51f20d788d63598a7bd7d4c3e2/03fb7b9cfde3477904a192536a3899c4a74cb19a3046515d1f799e4a47e030e6/independence_wave_focus_tree.focus.svg), and [source map](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3399c1787ce11663b0cff1d310af0f9e643d3790b82df1e8f97a3b0538a7aa39/01066ae01b94daff27ffa91792c9376da171235eaeb10be813e3fe7bd4e7794a/independence_wave_focus_tree.focus.source-map.json) are available for review.

The two overlay files contain `shared_focus` definitions rather than standalone `focus_tree` blocks. Separate inspect calls against each overlay with `treeId = independence_wave_focus_tree` returned `FOCUS_TREE_NOT_FOUND` and no artifacts. Consequently, the current 184-node inspect/render geometry does not establish package-overlay layout safety. Source graph review below establishes import reachability, not overlay geometry.

No standalone `hoi4.focus_lint` route was exposed. The diagnostics and validation returned by `hoi4.focus_inspect` are the lint evidence used here. No raster was opened, so this handoff makes no pixel-level visual claim.

## Route coverage

| Accepted lane or route | Current implementation evidence | Coverage |
|---|---|---|
| Survival and state construction | `independence_wave_prepare_capital_administration` opens `name_provisional_authority`, `inventory_the_state`, and `bind_the_first_oath`; `independence_wave_complete_founding_settlement` requires ministries, communications, and provincial/council integration (main focus file, lines 102–307). | Present with a real multi-branch trunk and an AND convergence at the capstone. |
| Government and internal power | Constitutional, popular council, traditional restoration, emergency military, patron-client, and radical sovereignty settlements are present; the optional Ajx neutral commission is package-gated. Route-lock focuses exclude competing settlements (main focus file, lines 968–1435). The optional power-struggle layer maps and mutually excludes its three outcomes (lines 311–372). | Present; distinct route groups and route locks are implemented. Package availability gates hide inapplicable choices. |
| Economy, infrastructure, and administration | Emergency revenue → food/fuel → transport authority → customs → package economic program → independent treasury (lines 378–499). | Present with a six-focus progression and varied state, industry, and administration rewards. The opening focus is gated on the inventory focus through `available`, not a visible prerequisite edge. |
| Army, security, and military identity | Militia integration, depots, officer recruitment, border guard, military archetype program, and alternative doctrine choices are present (lines 505–809). Reclamation has the visible prerequisite from the archetype program (lines 751–780). | Present with the accepted long connector and route-choice exclusions. |
| Diplomacy, recognition, and patrons | Foreign office → first missions → neighbor recognition → patron/neutrality alternatives → treaty and permanent service capstones (lines 816–958). | Present. The opening focus is gated on provisional authority through `available` rather than a visible prerequisite. |
| Former host, borders, and expansion | `independence_wave_define_former_host_policy` opens separation, guarded frontier, association/reunion, reclamation, and host-collapse handling (lines 1449–1636). | Present with route-specific triggers and mutual exclusions for living-host settlements. |
| Regional ambition | `independence_wave_survey_regional_ambition` leads to local committees and a regional congress, which converge at postwar integration authority (lines 1642–1711). Package signature extensions are separately gated. | Present as a shared lane plus package data. The root is gated by founding completion and package registration in `available`/`allow_branch`, not by a visible prerequisite edge. |
| Independence network and League | Recognition, civil-service exchange, aid corridor, arbitration, charter, founding-member preparation, congress, and charter proposals are present (lines 1720–1903). Focus source comments assign votes and proclamation to decisions. | Present; focus stages feed the League decision/state machine rather than silently completing votes. |
| Formable discovery and preparation | `independence_wave_focus_discover_regional_identity` requires `independence_wave_build_postwar_integration_authority`; the shared focus chain prepares congress, terms, and an integration commission (lines 1909–1960). DM-53 owns discovery; DM-54/DM-55 own preparation and commitment (decisions file, around lines 3714–3860). | Present and decision-linked. League-state discovery has the qualification described below. |
| High-chaos and late identity | Hidden sovereignty begins at `independence_wave_sponsor_further_ruptures` and converges through `independence_wave_rewrite_charter_of_borders`, which marks high-chaos sovereignty complete and refreshes the FORM-48 reveal hook (main focus file, lines 2101–2164). Formable commitment is decision-owned; post-formation focuses are provided by additive/package modules. | High-chaos route is present with reveal/route gating. No single generic “late identity” focus is defined in the inspected source; state outcomes and post-formation overlays act as endpoints. The diagram does not require a focus with a specific ID, but full post-formation coverage is outside this source scope. |
| Retained-tree and signature overlays | The main tree imports 27 shared-focus roots; all 27 resolve in the three audited source files. A static prerequisite-graph walk reaches all 48 IW-043/IW-058 and all 43 IW-093/IW-098 shared-focus definitions from those imports. | Present and source-wired in this scope. Their MCP geometry remains unverified because the inspector does not accept the overlay files as standalone trees. |
| Fourteen regional overlay matrix | The generic tree supplies the common ambition and package-adapter framework. This audit read the accepted 14-row matrix but was limited to the three named focus files and cross-reference triggers/effects. | No absence claim is made for regional focus modules in other source files; full matrix-to-source coverage is unresolved outside this bounded source scope. |

## Missing or simplified content

No required lane or major route is missing from the generic focus source or the specifically named IW-043/IW-058 and IW-093/IW-098 overlay sources. Their branches contain multiple steps and route-specific effects rather than terminal placeholder focuses.

The map explicitly says it depicts branch relationships and leaves final coordinates and focus count to implementation. Part 4 also says the route diagram is a design guide, not an exact coordinate map. Therefore, `independence_wave_focus_discover_regional_identity` does not need `prerequisite = { focus = independence_wave_convene_league_congress }`. The actual focus prerequisite on postwar integration authority is coherent with the ambition-to-formable route, while the League-to-formable relation is represented by discovery state and decision eligibility. The audited generic source has no one-focus late-identity convergence node; formable transactions, high-chaos completion state, and additive post-formation modules represent late outcomes. Whether every accepted formable package has the promised post-formation play requires broader integration evidence than these scoped focus files provide.

Several shared-lane roots use availability gates instead of visible focus prerequisites: `independence_wave_establish_emergency_revenue` requires completed inventory; `independence_wave_integrate_militia_commands` requires the first oath; `independence_wave_establish_foreign_office` requires provisional authority; `independence_wave_prepare_first_assembly` and `independence_wave_survey_regional_ambition` require founding settlement; `independence_wave_recognize_fellow_new_states` requires founding settlement and network participation; and `independence_wave_sponsor_further_ruptures` requires ambition completion and high-chaos eligibility. These gates implement the route behavior. They do not produce prerequisite connectors, so progression is less explicit visually. The accepted lane map alone does not make those exact source edges mandatory. Any proposed edge would change the focus candidate pool and must be sequenced with baseline and same-scenario `hoi4.probability_compare` evidence from `chaosx_ai_probability_auditor`.

## League-to-formable finding

**Connection:** the behavior is wired, but the strict accepted meaning of “revealed by league state” is broader than the source gate currently enforces.

`independence_wave_focus_discover_regional_identity` is available after regional power phase and full selected-family readiness (`common/scripted_triggers/006_independence_wave_focus_triggers.txt:330–338`); completing it sets `independence_wave_unlock_formable_discovery` (`common/national_focus/006_independence_wave_focus.txt:1909–1919`). DM-53 then requires recognized-or-later status, the unlock, a registered valid family, full commit readiness, no prior discovery, and the family discovery-mode gate (`common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:833–848`; `common/decisions/006_independence_wave_decisions.txt:3714 onward`).

For `revealed_by_league_state`, `has_independence_wave_formable_discovery_gate` accepts any of `independence_wave_league_member`, `independence_wave_league_route_available`, or `independence_wave_formable_league_reveal_ready` (`common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:804–830`). `independence_wave_focus_allow_league_route` sets `independence_wave_league_route_available` directly (`common/scripted_effects/006_independence_wave_focus_effects.txt:276`), and package setup effects call it before a formal League membership is established. Part 6 instead describes this discovery mode as opened by a regional caucus, charter, or member vote. Thus DM-53 can become visible on eligibility alone for families assigned discovery mode 4, subject to the other readiness gates.

This is a decision-visibility/route-semantics issue, not evidence that a literal focus edge is missing. If the accepted phrase means actual League state, the narrow follow-up is to make the `revealed_by_league_state` branch require a caucus, charter, member vote, or explicit reveal receipt rather than `independence_wave_league_route_available`. Keep any such edit in parent sequencing; no source edit was made here. The Mediterranean Island League exception remains explicit: DM-53 excludes that family because its sovereign charter is the authoritative transaction (`...formable_registry_triggers.txt:838–845`).

## Icon coverage

| Source | Focus definitions | Unique focus icon IDs | Registration and texture result |
|---|---:|---:|---|
| `006_independence_wave_focus.txt` | 227 (184 `focus` + 43 `shared_focus`) | 66 | All custom IDs have a sprite, shine sprite, and existing texture. |
| `006_independence_wave_iw043_iw058_focus.txt` | 48 | 20 | All custom IDs have a sprite, shine sprite, and existing texture. |
| `006_independence_wave_iw093_iw098_focus.txt` | 43 | 35 | All custom IDs have a sprite, shine sprite, and existing texture. |
| **Total scanned source definitions** | **318** | **121** | **0 missing sprite definitions, shine definitions, or referenced textures.** |

Focus icons repeat by thematic family, with 121 unique IDs across 318 definitions. The most reused are `GFX_goal_independence_wave_former_host_settlement` (22 focuses), `...army_integration` (19), `...infrastructure_authority` (18), `...founding_administration` (17), and `...league_congress` (14). Source review did not establish a route/reward misassignment. Without raster inspection, art-level distinctness and visual defects remain unreviewed.

## Localization and reward mismatch list

A static key census across the three focus sources found title and `_desc` entries for all 318 unique focus/shared-focus IDs in English localization. All 318 definitions also contain `completion_reward`, `ai_will_do`, and `search_filters` blocks. The icon scan found no missing custom focus icon wiring.

No confirmed title/reward mismatch was found in the route nodes checked. In particular, “Convene the League Congress” says it opens the Congress proposal stage and its focus effect sets the readiness flag; the comments and decision surface assign votes and proclamation to the League decisions. “Discover the Regional Identity” opens the grounded union path and its decision rather than claiming to proclaim the formable immediately.

This was a structural key/reward wiring check plus route-focused text sampling, not a line-by-line editorial review of all 318 descriptions. No player-facing localization was changed.

## AI behavior gaps

All 318 definitions in the three scoped files contain an `ai_will_do` block; all 318 also carry search filters. Source examples show route and condition modifiers, including threat, government route, League membership, regional power, and World Collapse conditions.

This handoff does not make scenario probability, candidate ordering, route starvation, or balance claims. The mandatory `chaosx_ai_probability_auditor` baseline and same-scenario comparison are a separate in-progress audit; its evidence must be merged by the parent before any focus eligibility or AI weight change is accepted.

## High-priority findings for parent

1. Resolve the meaning of `revealed_by_league_state` in `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:814–819`. Current behavior accepts `independence_wave_league_route_available` before actual caucus/charter/member-vote state. This can reveal a formable too early relative to Part 6. No direct League focus prerequisite is required by the accepted diagram.
2. Keep the 10-column reclamation edge as accepted unless the parent changes the route design. The fresh diagnostic matches the existing geometry and prerequisite repair receipts.
3. Confirm how late identity/post-formation focus depth is evidenced across every accepted formable package. The scoped generic source ends in state/decision-owned outcomes and package overlays rather than one common terminal focus.
4. Obtain a supported MCP geometry view for the shared-focus overlays or document the package-specific geometry limitation. Attempts to inspect either shared-focus-only source returned exact blocker `FOCUS_TREE_NOT_FOUND`; the main tree renderer does not certify those overlay nodes.
5. Merge the separate AI probability auditor's scenario evidence before changing focus eligibility, focus candidate weights, or route AI.

## Validation performed and limits

- Ran fresh `hoi4.focus_inspect` and `hoi4.focus_render` for `independence_wave_focus_tree`; inspect diagnostics passed with the nonblocking accepted reclamation edge and unrelated vanilla localization warning listed above.
- Ran static source checks over all focus/shared-focus blocks in the three scoped files for duplicate IDs, AI blocks, reward blocks, search filters, English title/description keys, custom icon definitions, shine definitions, and referenced texture existence; no structural gaps were found in those checks.
- Checked import IDs and prerequisite reachability for the 27 main-tree shared-focus imports; all resolve, and the 91 nodes in the two named overlay files are reachable from those imports.
- Separate overlay MCP inspection returned `FOCUS_TREE_NOT_FOUND`; therefore those nodes have source-level wiring evidence but no MCP layout/render evidence.
- No raster was inspected, so pixel-level review is not claimed. No HOI4 session was launched. Live-game validation remains user-owned.
- The 14-row regional overlay matrix was reviewed as accepted design, but regional focus source files outside the three named files were not audited; their per-row implementation remains unresolved by this bounded handoff.
- No source tests were added or run. No source edit, localization edit, asset edit, or commit was made.

## Changed file and handoff

Only this audit handoff is new: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_focus_tree_audit_2026-09-25.md`.

No focus IDs, route behavior, localization keys, or icon IDs changed. No improvement plan was created because no broad missing route was established within the inspected source scope.

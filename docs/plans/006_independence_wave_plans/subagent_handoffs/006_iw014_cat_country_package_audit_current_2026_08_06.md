# IW-014 CAT current country-package audit

Date: 2026-08-06 (Europe/Kyiv).

Scope: bounded country-package audit for Event 006 IW-014 Catalonia (`CAT`) after the standalone-admission and FORM-07 late-binding decisions. This audit covers the currently admitted vanilla carrier, its state and setup contract, the shared focus assignment, decisions, ideas, localisation, assets, AI, formable guards, and cleanup. It does not promote FORM-07, NAV, or GLC and does not redesign the package.

## Verdict

CAT is source-complete for the accepted standalone Event 006 carrier contract. The package uses the vanilla `CAT` tag, vanilla Catalonia history and flag, state 165, and the vanilla `CAT_lluis_companys` character. The package has a package-local setup/final/cleanup chain, five route-government installers, five reinforcement paths, a full shared Event 006 focus assignment with a six-node CAT branch, one timed mission, eleven serialized project decisions, seven lifecycle ideas, CAT localisation, and four CAT AI strategy layers.

No narrow gameplay, localisation, asset-wiring, or country-identity patch is recommended from this audit. FORM-07 remains fail-closed: CAT may register the Iberian family for its regional ambition ledger, but discovery, the focus branch, member invitations, and formation still require the shared formable commit-readiness contract.

## Country-package coverage checklist

| Surface | Result | Current evidence |
| --- | --- | --- |
| Tag registration | PASS | Vanilla `common/country_tags/00_countries.txt:200` maps `CAT` to `countries/Catalonia.txt`; the mod has no duplicate CAT country definition. |
| Carrier identity | PASS | Vanilla Catalonia country/history/characters remain the carrier; `CAT_lluis_companys` is required by `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt:29-34`. |
| State and capital | PASS | State 165 is the exact IW-014 anchor and CAT capital; setup requires the anchor to be owned and controlled and the capital scope to resolve to state 165. |
| Reservation and former host | PASS | IW-014 uses package id `independence_wave_package_id.iw_014`, reservation group `RG-165`, the Mediterranean/Iberia regional pool, and a protected former-host relationship. |
| Politics and parties | PASS | `independence_wave_initialize_cat_politics` and the five route installers set the accepted starting and route party names and popularity distributions. |
| Leader and portrait | PASS | The vanilla male Lluís Companys character and vanilla sourced portrait are preserved; no opposite-gender name/portrait pairing or runtime archive reference was found. |
| Flag and cosmetic identity | PASS | The vanilla Catalonia flag family remains authoritative; no new CAT flag or cosmetic tag is introduced. |
| Advisors and high command | PASS / none required | The accepted IW-014 package does not add an advisor or high-command portrait/icon surface. |
| Focus assignment | PASS | CAT setup assigns `independence_wave_focus_tree` under the accepted full-framework minimal-tree exception; six CAT focuses are defined at `common/national_focus/006_independence_wave_focus.txt:3736-3818`. |
| Decisions and mission | PASS | `common/decisions/006_independence_wave_catalonia_decisions.txt` contains one 420-day founding mission and eleven serialized projects with costs, timers, cancellation, completion, and failure effects. |
| Ideas | PASS | Seven CAT ideas are defined in `common/ideas/006_independence_wave_catalonia_ideas.txt`; all are limited to `original_tag = CAT`. |
| Localisation | PASS | CAT category, mission, all eleven projects, route parties, ideas, six focuses, tooltips, and effect text are covered by `localisation/english/006_independence_wave_catalonia_l_english.yml`. |
| Starting force/industry/technology | PASS within scope | The accepted package preserves vanilla CAT history and overlays the p14 force mapping, inheritance paths, and CAT industrial/assembly ledgers; no new technology tree is introduced. |
| AI | SOURCE PASS / quantitative hold | CAT strategy source is present and guarded by setup/lifecycle flags; the installed probability adapter cannot discover the `ai_strategy_factor` blocks, so no quantitative strategy ranking is claimed. |
| Cleanup and rollback | PASS | `independence_wave_cleanup_iw_014_catalonia` removes the mission, eleven decisions, seven package ideas, ledgers, route/setup/lifecycle flags, and formable registration variables without editing vanilla history or portraits; shared focus cleanup clears the discovery-unlock flag. |
| Formable safety | PASS / FORM-07 closed | CAT setup calls family registration only; `can_open_independence_wave_formable_branch` and later transaction gates require `has_independence_wave_formable_commit_readiness = yes`. No FORM-07 identity-contract writer is present. |

## File-surface checklist

The owning surfaces currently reviewed are:

- `common/scripted_triggers/006_independence_wave_catalonia_package_triggers.txt` for exact CAT identity, state 165, package, route, ledger, focus, force, AI, and complete-setup proofs.
- `common/scripted_effects/006_independence_wave_catalonia_package_effects.txt` for setup, politics, five route installers, focus rewards, formable-discovery unlock gating, validation, and cleanup.
- `common/script_constants/006_independence_wave_catalonia_constants.txt` for accepted popularity, ledger, crisis, and AI tuning values.
- `common/decisions/categories/006_independence_wave_catalonia_categories.txt` and `common/decisions/006_independence_wave_catalonia_decisions.txt` for the category, mission, and eleven project entries.
- `common/ideas/006_independence_wave_catalonia_ideas.txt` for the seven lifecycle and route ideas.
- `common/ai_strategy/006_independence_wave_catalonia.txt` for industrial survival, former-host restraint, settled-industry, and emergency-command layers.
- `common/national_focus/006_independence_wave_focus.txt`, `common/scripted_effects/006_independence_wave_focus_effects.txt`, and `common/scripted_triggers/006_independence_wave_focus_triggers.txt` for full-framework assignment, CAT focus nodes, and formable branch protection.
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` and `common/scripted_triggers/006_independence_wave_form07_triggers.txt` for shared readiness and FORM-07 identity gates.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` and the region-02 package loader/triggers for central IW-014 admission and state reservation.
- `localisation/english/006_independence_wave_catalonia_l_english.yml` for all CAT player-facing strings.
- Vanilla `common/country_tags/00_countries.txt`, `common/countries/Catalonia.txt`, `history/countries/CAT - Catalonia.txt`, `common/characters/CAT.txt`, and `history/states/165-Catalonia.txt` for preserved carrier identity and map precedent.

## Map and state setup

Vanilla state 165 is coherent for the accepted carrier contract. It has owner `SPR`, cores `CAT` and `SPR`, capital province `9764`, category `large_city`, manpower `3,036,537`, coal `2`, victory points `9764 = 30`, `6966 = 1`, and `6927 = 1`. Province `9764` has naval base level 4; the state has air base level 2, arms factory level 1, industrial complex level 1, and infrastructure level 4. IW-014 setup requires the state-165 anchor and capital to be owned/controlled by CAT after release and retains the vanilla state definition.

The mandatory read-only map inspection for state 165 passed state definitions, geometry, membership, and network checks in the bounded record. The same workspace reports global position/locator failures (`MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`) across unrelated states, with diagnostics truncated; no state-165-specific map failure was returned. No map write was performed.

Map artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3bfa50a56201133050b0349ba80709f10e226536834ad51ad54dc37ae66d9a1b/dcb3336cfaf1c61ff636662175046098ec1999103e82940739d4598aaef610b4/map-inspect.edd84392c34b969c.json`.

## Politics, leader, portrait, flag, advisor, and party review

The accepted constants are present in `common/script_constants/006_independence_wave_catalonia_constants.txt:15-50`: opening popularity `45/30/20/5`, constitutional `70/15/15/0`, popular `20/65/10/5`, traditional `25/10/60/5`, emergency `15/10/65/10`, patron `50/15/30/5`, industrial cohesion `38`, assembly legitimacy `42`, and stable threshold `60`. The founding mission window is `420` days at line 67.

The route installers promote the same vanilla `CAT_lluis_companys` character with route-appropriate ideology metadata. This is consistent with the accepted single historical carrier identity and does not create a personal random-name pool. The character is male-presenting and no female metadata or opposite-gender name pool is attached. No advisor, high-command, or custom portrait icon is required by the package.

Cleanup removes CAT package ideas, route flags, ledgers, setup/lifecycle flags, and formable family registration variables. The shared `independence_wave_clear_focus_runtime` effect clears `independence_wave_unlock_formable_discovery`; therefore the absence of a CAT-local clear for that shared flag is not a cleanup defect.

## Focus, decision, idea, and asset review

The CAT branch is six connected shared-focus nodes: `independence_wave_cat_secure_barcelona_port_focus`, `independence_wave_cat_integrate_factory_workers_focus`, `independence_wave_cat_reconcile_assembly_focus`, `independence_wave_cat_settle_iberian_charter_focus`, `independence_wave_cat_open_mediterranean_corridor_focus`, and `independence_wave_cat_ratify_catalan_sovereignty_focus`. Their prerequisites, route/host/network/stable gates, completion rewards, and localisation are present. The first CAT branch node requires the full framework in `allow_branch`; CAT setup itself requires that framework before marking setup complete.

The CAT decision category is setup-gated and exposes the two live ledgers in its description. The Mediterranean Network project and focus both require network/League state, and the project cancellation path checks that the League route remains available. The founding mission is not directly available to the player and resolves on stable ledgers or applies the documented failure loss on timeout/invalidation. The eleven projects serialize through the CAT active-project trigger.

The package reuses existing Event 006 focus/decision icons and vanilla CAT visual identity. No generated portrait, custom flag, advisor icon, or runtime reference into the durable portrait archive is present or required.

## Starting military, technology, industry, supply, and production review

IW-014 does not replace vanilla CAT history. Vanilla CAT begins with its existing history technology and production setup, including the vanilla capital/state and 20 convoys; the Event 006 adapter applies the accepted p14 force profile and navy/air inheritance contract through the shared force system. The CAT package adds no unsupported equipment type, technology node, or bespoke division template. A live release and supply/production observation remain outside this source audit.

## AI and probability evidence

The required probability route was run against the current CAT decision, mission, and shared focus sources.

- `decision_ai_will_do` on `common/decisions/006_independence_wave_catalonia_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED`, one candidate, nine required inputs, zero unresolved inputs, and `poolComplete = false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b488df4f777380e6ea37d6489f4585377a10c6ef6b2a1de318d030b9529e9ea9/0e277846a5551abf373a393d07251be98c0cc87a92b90151b22050bb06a65de7/probability-inspect-505bfbb388f5.json`.
- `mission_ai_will_do` on the same decision source returned `PROBABILITY_SOURCE_INSPECTED`, eleven candidates, thirteen required inputs, zero unresolved inputs, and `poolComplete = false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94c8733c42a5147dffdcf09df53c0e307966f59df89237e513a3ccfbc34f0a56/9ec0cc582d40e61343b5f97eb71e8749384b0d1d0797f8d4ce54aa0ef643a873/probability-inspect-505bfbb388f5.json`.
- `national_focus_ai_will_do` on `common/national_focus/006_independence_wave_focus.txt` returned `PROBABILITY_SOURCE_INSPECTED`, 184 candidates, 15 required inputs, zero unresolved inputs, and `poolComplete = false`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8c357a4b8dd920d325f45228e0a5fb3c7df90217239cde20b52224846401d6d3/34f6f08a1c45e15dcb8df40d7399d4873e8d9e52af0d22ff41a2f3af9946364a/probability-inspect-21f8aab08229.json`.
- `ai_strategy_factor` on `common/ai_strategy/006_independence_wave_catalonia.txt` returned the exact blocker `PROBABILITY_SURFACE_EMPTY` / `No weighted blocks matched this request`; no quantitative CAT strategy ranking is claimed.

No weighted source was changed in this audit, so no probability compare was required. The incomplete pools are score-discovery evidence only and do not prove click probabilities, route dominance, survival, or live AI behavior.

## Mandatory HOI4 MCP evidence

Event inspection and rendering were run for `chaosx.nr006.1`. The scan and downstream trace both returned `EVENT_INSPECTED_PARTIAL` with the workspace-wide inline-file truncation diagnostic, but no CAT-specific event blocker. Scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/378d3c4ee3c8f3a58dc1043507484bd11a253fccd99bec3b8fa7af6ae5d4e980/ddc051810d990b7b5545c53b3f10cb1d2e41fdee21b8b49661f96f82b6756874/event-scan-be8a459e7129.json`. Downstream trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/577d3b5f5e30511e2475b3bf03702bb3808e4c73dacc631a741f5bc24c2767ef/53c9a25caa0ee66345022347f422986547bdea0c7a4f2769af2667206d8679e8/event-trace-be8a459e7129.json`. The bounded render returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics; manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d13e8ace3593a107775e82e91547b993ddfa22d042e074d99d2498c1b545e0ad/c3fed9d12336b336608e0ed3475d7d327361e8882903aed890de2960adb06a92/event-neighborhood-be8a459e7129-manifest.json`.

Focus inspection/rendering of `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt` returned 184 focuses, 193 connectors, zero crossings, zero node intersections, and one long connector. The MCP validation still reports 14 blocking diagnostics from unrelated vanilla continuous-focus sprite/spacing surfaces; no CAT branch icon or CAT-specific missing asset was identified. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbb287c7151a113ae021f5500333d37bccb685f67fa3b17b229d036c1b31d0f0/37b3b57a5d7129be4337bb91d1d7dfc3c1dec8fc7dc00eb89f282e3077813898/focus-inspect.d527cf63a0416797.json`. Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a31010c754ceba648ce78289a8b3b2539154ddc58ac4ab4bd754a21d669eafe3/72960869ddd828ee551b49003d6dc31cbb0c2e4bd589fb6b544ebbad0073135e/independence_wave_focus_tree.focus.svg`.

The installed HOI4 MCP exposes no country-package inspection route. This is an exact tooling blocker; the vanilla/source country review above is not being presented as equivalent engine evidence. The installed package also exposes no Technology Tree Viewer. CAT has no custom technology surface, so no CAT technology rewrite or tree claim is made; the absence of a viewer remains unresolved.

## Missing, stale, or blocked surfaces

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:17` correctly lists IW-014 as admitted, but line 477 still says the CAT implementation is outside runtime attestation. This is a documentation contradiction for the parent documentation pass, not a gameplay defect. No concurrent documentation file was patched here.
- The current probability adapter cannot inspect CAT `ai_strategy_factor` blocks. AI strategy behavior is therefore source-present but quantitatively unresolved.
- Event and focus MCP results are workspace-partial because of global inline-file truncation and unrelated global diagnostics. State 165 has no CAT-specific map diagnostic.
- Country-package MCP and Technology Tree Viewer routes are unavailable. No source-only substitute is claimed for either missing engine route.
- Live release, save/load, supply, production, host persistence, and player-owned AI behavior remain user-owned runtime QA and are not claimed here.

## Changes and validation

Changed gameplay files: none.

Changed documentation file: this handoff only.

No map write, focus rewrite, GUI write, event write, country history edit, portrait production, flag production, or technology edit was performed. No broad identity redesign, FORM-07 promotion, or fallback was introduced.

The meaningful checks were the current CAT source review, vanilla carrier/state review, decision/mission/focus probability inspections above, Event 006 event inspection/rendering, shared focus inspection/rendering, and state-165 map inspection. Hearts of Iron IV was not launched.

The current repository scripts also passed `python -B .tools/audit_chaosx_country_tags.py --surface-scan` with zero external country-definition and identity-surface collisions, and `python -B .tools/audit_event6_allocator.py` with 149 publishers, 23 attested packages, 22 compatible reservation groups, and the 20-package static standalone witness.

## Parent handoff

Treat CAT as standalone source-complete under the accepted IW-014 contract. Keep FORM-07 fail-closed and route the stale source-of-truth-map sentence through the documentation curator. Preserve the unresolved probability, country-MCP, Technology Viewer, global focus diagnostics, global map diagnostics, and live-runtime boundaries in any broader Event 006 completion report.

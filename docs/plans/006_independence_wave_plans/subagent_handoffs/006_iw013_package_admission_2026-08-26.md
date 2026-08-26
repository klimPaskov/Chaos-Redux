# Event 006 IW-013 NAV package admission audit

Date: `2026-08-26`.

Status: **NOT ADMITTED / FAIL-CLOSED**.

This is a bounded country-package admission audit for Event 006 package `IW-013` on the `NAV` carrier. The current package has a source-wired adapter, a current-map compact anchor, shared gameplay surfaces, and mechanically complete asset ladders, but the accepted package gates are not all satisfied. No gameplay, central-registry, country, history, map, flag, portrait, localisation, AI, decision, focus, spreadsheet, or manifest file was changed by this audit except for this handoff.

## Decision

IW-013 cannot be safely admitted to the automatic Event 006 ladder or fixed Join registry in its current state. The package remains adapter-only and fail-closed because central content attestation excludes `iw_013`, the current Basque compact flag identity and rights review remain unresolved, the latest NAV portrait still carries a source-rights caveat, and fresh required HOI4 probability evidence could not be obtained because the MCP transport is closed. The accepted research matrix also still names state `172` as the compact anchor while the current installed-map binding and runtime package triggers use state `792` País Vasco, so the package authority record needs reconciliation before admission.

The shared generic focus framework and existing vanilla NAV history are accepted package surfaces, not an invented fallback. No new country shell, replacement tag, generic leader, generic flag, or copied route identity was introduced.

## Scope and non-actions

- Audited only `IW-013` / `NAV` / Basque Country.
- Preserved concurrent worktree changes from other agents.
- Did not operate RunPod, launch Hearts of Iron IV, load a save, or make a live-game claim.
- Did not write the map or request a map rewrite because the current binding already records the compact anchor and optional extensions, while admission is blocked upstream by content gates.
- Did not add `iw_013` to central attestation or the fixed Join order because doing so would open an incompletely admitted package.
- Did not copy or promote vanilla `NAV.tga`, `NAV_democratic.tga`, or any review/archive asset into a new runtime basename.
- Did not edit the stale player-facing package summary because that is a documentation reconciliation item for the parent review rather than a gameplay patch in this blocked audit.

## Accepted gate checklist

| Gate | Current evidence | Result |
| --- | --- | --- |
| Tag and identity | Vanilla `common/country_tags/00_countries.txt:201` maps `NAV` to `countries/Navarra.txt`; `common/countries/Navarra.txt` and vanilla `history/countries/NAV - Navarra.txt` remain the carrier shell. Current package identity is Basque Country on state `792`, not a new tag. | Source-covered, but identity authority is unresolved because the accepted matrices still describe `172` as the compact Basque anchor. |
| Current map anchor and host | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:14` records compact `792` País Vasco, optional `172` Navarra and `806` Pyrénées-Atlantiques, reservation group `RG-172`, host `SPR`, and protected host state `41`. `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:33-50,153-194` requires state `792` ownership/control, capital status, a distinct protected former host, and the NAV roster. | Source contract is coherent with the current binding; engine map inspect/render evidence is blocked by the HOI4 MCP transport failure. No map write was justified. |
| Region, depth, archetype, reservation | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:356-365,529-537` publishes Mediterranean/Iberia, regional, industrial-breakaway, `RG-172`, anchor `792`, and optional extensions `172` and `806`. | Source-covered; selection remains gated by central attestation. |
| Vanilla leader and additive command roster | Vanilla country leader `Ramón Ormazábal Tife` is preserved. `common/characters/006_independence_wave_characters_registry.txt:243-260` defines male `NAV_independence_wave_jose_antonio_aguirre` with `GFX_portrait_NAV_jose_antonio_aguirre` and corps-command traits. `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:71-78` requires both the vanilla leader and active corps commander. | Source-covered; no opposite-gender name or portrait pairing found. |
| Portrait consumer and output | `interface/006_independence_wave_portraits_registry.gfx:146-147` points to the stable NAV DDS path. `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md:1-16,55-71` records the supplied painted output as `styled_final` and byte-identical to the runtime DDS. | Pixel, framing, and consumer checks pass, but the attributed source remains `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` because the Commons page and machine-readable licence versions disagree and no independent rights reviewer is assigned. |
| Neutral and route flags | Vanilla `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\flags\NAV.tga` is a Navarrese red-field and gold-chain design, while the current compact identity is Basque state `792`. The mod has four route ladders in `gfx/flags/{,medium,small}/NAV_INDEPENDENCE_WAVE_*.tga`; their manifest is `docs/assets/006_independence_wave/iw013_nav_flags_2026_08_13/manifest.md:3-18,22-33`. | Mechanical TGA/DDS coverage passes, but the neutral carrier identity and route-art rights/ShareAlike decision remain unresolved. Existing route variants are alternate-history designs and are not a neutral sourced replacement. |
| Politics, parties, and cosmetic routes | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:160-245,428-470` sets democratic setup, all four NAV party names, five route governments, ledgers, and cleanup. `common/countries/cosmetic.txt:1855-1875` defines the four route cosmetic tags. | Source-covered. |
| Ideas and lifecycle | `common/ideas/006_independence_wave_ideas_registry.txt:1554-1604` defines NAV contested, compact, constitutional, workers, municipal, frontier, and protected-compact ideas with `original_tag = NAV` gates. The setup and cleanup effects own the corresponding lifecycle flags and ideas. | Source-covered. |
| Shared focus framework | `common/scripted_effects/006_independence_wave_focus_effects.txt:29-84` assigns `independence_wave_focus_tree`; `common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-68` defines the full framework contract. `common/national_focus/006_independence_wave_focus.txt:15-60` contains the shared tree. | Source contract is present and intentionally shared; required focus inspect/render calls were attempted but blocked by MCP transport closure. |
| Decisions and founding mission | `common/decisions/006_independence_wave_iberian_decisions.txt:13-202` defines the NAV founding mission and ten visible paid projects with route, host, capital, failure, and AI hooks. `localisation/english/006_independence_wave_iberian_l_english.yml:63-95,133-177` supplies category, decision, party, leader, and idea text. | Source-covered; current AI score evidence is not engine-verified. |
| Force, technology, industry, and supply | `common/scripted_effects/006_independence_wave_force_package_effects.txt:241-370` owns the dynamic force mapping. Constants record `p13` mountain-frontier values, including tradition `67`, reinforcement/profile value `709`, and no sensitive research flag in `common/script_constants/006_independence_wave_constants_registry.txt:2328,2542,2756,7586`. Vanilla NAV history supplies the starting technology, convoys, and 1936 setup in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\NAV - Navarra.txt`. | Source-covered; technology inspect/render was attempted but blocked, and the installed package exposes no dedicated Technology Tree Viewer. |
| AI and diplomacy | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:832-865` defines NAV mountain survival, host restraint, settled industry, and emergency command strategies. `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:445-468` initializes ledgers, host routes, network/League/formable registration, and the NAV AI profile. | Source-covered but admission-blocked until a fresh mandatory probability pass is available. |
| Formable route | `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:37,90-93,201-211` and `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:828,936` bind FORM-07 to NAV state `792` and the CAT/NAV/GLC member set. | FORM-07 remains separately fail-closed for its own identity, flag, and all-member integration gates. NAV admission must not claim FORM-07 readiness. |
| Adapter and setup dispatch | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` includes the `iw_013` adapter, and `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:519-522` dispatches setup to `independence_wave_setup_iw_013_basque`. | Adapter and setup dispatch are present. |
| Central content attestation | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` lists the attested package IDs but does not include `iw_013`. Normal and scenario preflight require this trigger at lines `207-210` and the corresponding scenario block. | **Blocked.** |
| Planner allocation and capacity | `common/scripted_effects/006_independence_wave_package_planner_effects.txt:95-115` refuses reservation mutation without content attestation, and lines `484-529` leave allocation weight at zero until the same attestation passes. The allocator audit reports `IW013` as adapter-only fail-closed. | **Blocked by attestation; no independent capacity defect isolated.** |
| Join registry | `common/scripted_effects/006_independence_wave_join_effects.txt:211-248` contains the fixed attested Join order and omits `iw_013`. | Correct fail-closed behavior while NAV is unattested. |
| Asset manifests and runtime references | Flag records are under `docs/assets/006_independence_wave/iw013_nav_flags_2026_08_13/`; portrait records are under `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/`. `gfx_handoff.md` keeps runtime references in `gfx/` and does not point into `docs/assets/`. | Mechanical manifests exist, but rights and identity gates remain open. |

## File surface checklist

| Surface | Concrete files and identifiers | Audit result |
| --- | --- | --- |
| Carrier registration | `common/country_tags/00_countries.txt:201`; vanilla `countries/Navarra.txt`; vanilla `history/countries/NAV - Navarra.txt` | Existing registered carrier, no new country shell required. |
| Runtime setup and cleanup | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:428-472,519-522,537-588,632-635`; identifiers `independence_wave_setup_iw_013_basque`, `independence_wave_cleanup_iw_013_basque` | Present and generation-scoped. |
| Runtime triggers | `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:9-13,33-50,71-78,153-249,263-270` | Present, current-anchor aligned, and fail-closed on missing setup or attestation. |
| Region registry | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:356-365,471-474,529-559`; `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:124-129` | Present with anchor `792`, optional `172|806`, and `RG-172`. |
| Central dispatch and admission | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:58,159-202,207-210,383-386,554-556` | Adapter and exact NAV branches present; attestation branch absent. |
| Join and capacity | `common/scripted_effects/006_independence_wave_join_effects.txt:211-248`; `common/scripted_effects/006_independence_wave_package_planner_effects.txt:95-115,484-529` | Correctly closed until attestation. |
| Leader and portrait | `common/characters/006_independence_wave_characters_registry.txt:243-260`; `interface/006_independence_wave_portraits_registry.gfx:146-147`; `gfx/leaders/006_independence_wave/portrait_NAV_jose_antonio_aguirre.dds` | Existing male corps-command consumer and runtime file pass mechanical portrait checks; rights caveat remains. |
| Flag and cosmetic identity | `common/countries/cosmetic.txt:1857-1875`; `gfx/flags/{,medium,small}/NAV_INDEPENDENCE_WAVE_{CIVICX,AGRARIANX,SOCIALISTX,EMERGENCYX}.tga`; vanilla `NAV.tga` | Complete route ladders, unresolved neutral Basque carrier identity and rights. |
| Politics and localisation | `localisation/english/006_independence_wave_iberian_l_english.yml:3-177`; party keys `NAV_independence_wave_*`; cosmetic keys `NAV_INDEPENDENCE_WAVE_*` | Direct NAV package localisation is present. |
| Ideas and decisions | `common/ideas/006_independence_wave_ideas_registry.txt:1554-1604`; `common/decisions/006_independence_wave_iberian_decisions.txt:13-202` | Package identifiers and visible text surfaces are present. |
| Focus | `common/national_focus/006_independence_wave_focus.txt:15-60`; `independence_wave_focus_tree`; setup assignment in `common/scripted_effects/006_independence_wave_focus_effects.txt:29-84` | Shared framework present; engine render evidence unavailable. |
| Forces and constants | `common/scripted_effects/006_independence_wave_force_package_effects.txt:241-370`; `common/script_constants/006_independence_wave_constants_registry.txt:2328,2542,2756,7586` | `p13` mapping and package id present. |
| AI | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:832-865`; constants for NAV priorities around lines `4110-4206` | Source strategies present; probability evidence incomplete. |
| Formable | `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt:37,90-93,201-211`; `common/scripted_effects/006_independence_wave_formable_registry_effects.txt:828,936` | FORM-07 is a separate fail-closed dependency. |
| Source manifests | `docs/assets/006_independence_wave/iw013_nav_flags_2026_08_13/manifest.md`; `docs/assets/006_independence_wave/source_placeholder_2026_08_05_iberian/manifest.md`; portrait and flag dated handoffs | Evidence shelves exist and runtime paths do not target the durable archive. Rights review remains open. |

## Missing or stale package surfaces

1. Central content attestation has no `iw_013` branch in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202`.
2. The fixed attested Join order has no `iw_013` entry in `common/scripted_effects/006_independence_wave_join_effects.txt:211-248`.
3. These are intentional fail-closed omissions while the country package is not admitted, not safe omissions to patch unconditionally.
4. `docs/events/006_independence_wave/iberian_registered_packages.md:48-52` still describes NAV as `source_placeholder` with no styled-final request, while the dated portrait handoff and manifest now record the installed NAV output as `styled_final` with user-supplied evidence. This stale documentation must be reconciled by the parent before a final package status is published.
5. `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:14`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:14`, and `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:18` still describe `172` as the compact Basque anchor, while `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:14` and runtime triggers use `792`. The current authority reconciliation handoff says `792` is the installed compact anchor and `172|806` are optional extensions, but the accepted matrix needs an explicit source-of-truth decision.

## Map and state setup issues

The current installed-map binding is the coherent runtime contract for this package: state `792` País Vasco is the compact anchor, `172` Navarra and `806` Pyrénées-Atlantiques are optional extensions, and `RG-172` is only the retained reservation-group identifier. `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:364-365,529-537` and `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:33-50,153-194` use that current contract.

The former host recorded by the current binding is `SPR`, with host state `41` retained outside the compact release. Static allocator evidence confirms protected host-state handling for `SPR=41`. No state ownership, controller, capital, port, railway, supply, victory-point, resource, or building rewrite was made.

The required `hoi4.map_inspect` call for states `792`, `172`, and `806` and the required `hoi4.map_render` call with state, coast, port, victory-point, resource, building, supply, railway, and adjacency overlays both failed with the exact MCP error `tool call error: tool call failed for hoi4_agent_tools/hoi4.map_inspect` or `hoi4.map_render`, followed by `Caused by: Transport closed`. This is an engine-evidence limitation, not evidence that the source map is invalid.

## Politics, leader, portrait, flag, advisor, and party issues

The vanilla NAV carrier keeps `Ramón Ormazábal Tife` as the country leader and the package adds the real male `José Antonio Aguirre` only as a corps commander. The character metadata, portrait consumer, and male identity pairing are coherent. No advisor or institutional portrait consumer is declared by this package, so no advisor icon or opposite-gender name-pool issue was found.

The setup writer initializes democratic popularity, civilian economy, export focus, volunteer-only, four NAV party names, five route availability flags, NAV ledgers, and the route cosmetic carrier. The corresponding party, idea, leader, decision, category, and tooltip localisation is present in `localisation/english/006_independence_wave_iberian_l_english.yml`.

The supplied NAV portrait passes the exact existing `army.large` consumer, dimensions, framing, DDS, and runtime-byte checks documented in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_user_supplied_portrait_final_audit_2026-08-26.md`. Its archived source-rights record remains `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` because the Commons page and machine-readable licence versions disagree and no independent rights reviewer is assigned. The portrait therefore does not provide an unconditional package-admission gate.

The current no-suffix vanilla `NAV.tga` is defensible for Navarre but not as a neutral Basque carrier for the current state-792 identity. The four route ladders are mechanically valid and remain correctly wired to `NAV_INDEPENDENCE_WAVE_CIVICX`, `NAV_INDEPENDENCE_WAVE_AGRARIANX`, `NAV_INDEPENDENCE_WAVE_SOCIALISTX`, and `NAV_INDEPENDENCE_WAVE_EMERGENCYX`, but the flag provenance handoff records them as generated alternate-history designs with unresolved attribution/ShareAlike acceptance. No flag promotion or replacement is safe until the parent chooses the identity and rights policy.

## Focus, decision, idea, and asset issues

The setup path assigns the shared `independence_wave_focus_tree` only after the package-specific full-framework contract is available. The package does not contain a bespoke NAV focus tree, which matches the accepted reuse-carrier design. The focus source, setup assignment, full-framework trigger, and localisation identifiers are present, but the required focus inspect/render calls were blocked by MCP transport closure.

The NAV founding mission and ten visible paid projects have concrete costs, capital/control requirements, cancellation and failure paths, host and route dependencies, and AI scores. All direct NAV decision and tooltip keys are present. Their weighted AI evidence remains subject to the probability blocker below.

The NAV idea lifecycle covers contested fueros, mountain-industrial compact, constitutional fueros, workers arsenal council, municipal fueros, frontier command, and protected Pyrenean compact. All package-owned idea pictures are present in the shared idea registry. No icon or decision asset gap was found in static source review.

The route flag manifest records complete normal, medium, and small TGA ladders and machine-readable header/round-trip QA. The manifest explicitly keeps review DDS files under `docs/assets/` and runtime references under `gfx/`. Mechanical coverage does not resolve the historical identity or rights gate.

## Starting military, technology, industry, supply, and production issues

The package preserves the vanilla NAV 1936 country history and adds the accepted dynamic `p13` mountain-frontier force mapping after the leader and command-roster checkpoint. The force mapping loader, package id, military tradition, reinforcement/profile constants, and research sensitivity flags are present. Vanilla history supplies the carrier's starting infantry, mountaineer, support, artillery, anti-air, convoy, and 1936 industry/technology setup in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\NAV - Navarra.txt`.

No source-level missing equipment, division-template, technology, research-slot, production-line, manpower, convoy, train, fuel, or supply-capacity reference was isolated in this bounded audit. The engine technology route could not be rendered because `hoi4.tech_inspect` and `hoi4.tech_render` returned `Transport closed`, and the installed package exposes no dedicated Technology Tree Viewer. This means the package has source coverage but not a current engine-render acceptance claim.

## AI, diplomacy, and playability issues

The NAV AI strategy registry contains mountain survival, host restraint, settled industry, and emergency command strategies with explicit enable/abort conditions and priority constants. The setup effect enables the NAV AI profile only after the package checkpoint. Host routes, network/League registration, and formable-family registration are source-wired and use the current package flags.

The fresh mandatory probability inspect for NAV decision AI was attempted with source `common/decisions/006_independence_wave_iberian_decisions.txt`, identifier `independence_wave_nav_iberian_category`, adapter `decision_ai_will_do`, and returned the exact error `tool call error: tool call failed for hoi4_agent_tools/hoi4.probability_inspect` followed by `Caused by: Transport closed`. Equivalent current inspections for the NAV founding mission, shared focus tree, and NAV AI strategy were not available after the same transport failure.

The prior dated probability handoff `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_nav_probability_audit_current_2026_08_13.md` remains useful bounded evidence only. It records inspect artifact `probability-73e99faee897386552185dd7`, current-to-current compare artifact `probability-41cd9447b480a220c6cb1727`, `poolComplete=false`, `110` unresolved inputs, and no quantitative balance claim. The prior Iberian strategy inspect found no weighted strategy surface. These dated artifacts cannot substitute for current engine evidence, so no AI or probability patch was made.

## Central adapter, attestation, dispatch, capacity, and Join status

The central adapter contract includes `iw_013` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:58`. Normal preflight also has the exact `iw_013` plus `original_tag = NAV` branch at lines `383-386`, and scenario preflight has the exact NAV package branch at lines `554-556`. The region registry can publish and reserve the candidate through `792`, `172`, and `806`.

The central content attestation trigger at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` does not include `iw_013`. Both normal preflight at lines `207-210` and the scenario preflight block require this attestation before the exact package branch can succeed. The planner reservation and allocation effects also require the same predicate before mutating state or assigning nonzero candidate weight. The fixed Join probe intentionally iterates only the attested package IDs and omits `iw_013` at `common/scripted_effects/006_independence_wave_join_effects.txt:211-248`.

The allocator static validator passed its global invariants but explicitly reported `runtime adapters: 40; adapter-only fail-closed IDs: IW013, IW015, IW043, IW058, IW093, IW098, IW177, IW179`. This is the expected current admission state for NAV, not evidence that the missing attestation can be bypassed.

No central capacity, dispatch, adapter, or Join patch was applied. Adding only an attestation branch or only a Join entry would create a partially admitted package and violate the accepted gate boundary.

## Static validation evidence

The following read-only checks were run from the mod root on `2026-08-26`.

| Command | Result and useful evidence |
| --- | --- |
| `python -B .tools/audit_event6_country_api.py` | Passed: `broad=242 unique tags; resolved=191 unique carriers; Soviet=34; Africa=45; missing=0; duplicates=0; IW-031-crosswalk=pass`. |
| `python -B .tools/audit_event6_flags.py --strict` | Passed: `registered Event 006 tags: 102; complete flag families: 102; incomplete flag families: 0`. This validates mechanical family coverage, not NAV identity or rights. |
| `python -B .tools/audit_event6_allocator.py` | Passed global invariants and reported `runtime adapters: 40`, `attested packages: 32`, and `adapter-only fail-closed IDs: IW013,...`. |
| `python -B .tools/audit_event6_scenario_matrix.py` | Passed all 32 SCN-008 cells and recorded eight edge-case receipts. |
| `python -B .tools/audit_event6_form16.py` | Passed the unrelated FORM-16 contract and preserved its existing fail-closed predicates; no FORM-16 mutation was made. |
| `python -B .tools/archive/audit_chaosx_country_tags.py --repo-root . --surface-scan` | Passed: `Protected Event 006/Soviet tags: 136; external country-definition collisions: 0; external identity-surface collisions: 0; random-event roots skipped: 1`. The explicit `--repo-root .` is required because this archived validator defaults to its own `.tools` parent. |

No static validator result authorizes package admission while the central attestation and asset/probability gates remain open.

## Required HOI4 MCP evidence and limitations

The following read-only routes were attempted against workspace `mod_chaos_redux_ea3b2d67c2c0`.

| Route | Request | Result |
| --- | --- | --- |
| `hoi4.focus_inspect` | National tree `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree` | Failed with `tool call error: tool call failed for hoi4_agent_tools/hoi4.focus_inspect` and `Caused by: Transport closed`. |
| `hoi4.focus_render` | Same tree and source | Failed with `Transport closed`. |
| `hoi4.event_inspect` | Lint `events/006_independence_wave.txt` | Failed with `Transport closed`. The source root remains `chaosx.nr6.1` in `events/006_independence_wave.txt:1-12`. |
| `hoi4.event_render` | Overview for the same event source | Failed with `Transport closed`. |
| `hoi4.map_inspect` | States `792`, `172`, and `806`, including overview | Failed with `Transport closed`. |
| `hoi4.map_render` | State layer with coast, port, victory-point, resource, building, supply, railway, and adjacency overlays | Failed with `Transport closed`. |
| `hoi4.tech_inspect` | Current technology scan | Failed with `Transport closed`. |
| `hoi4.tech_render` | Technology summary | Failed with `Transport closed`. The installed package currently exposes no dedicated Technology Tree Viewer, which remains an unresolved limitation even when the transport recovers. |
| `hoi4.probability_inspect` | NAV decision AI source and adapter | Failed with `Transport closed`. No current evaluation, sweep, simulation, or compare was run after the inspect failure. |

The HOI4 MCP server first timed out during a parallel inspection attempt and subsequently returned `Transport closed` on each individual retry. These are exact tool blockers, not source-only passes. No map, focus, event, technology, or probability surface is reported as engine-validated here.

## Smallest next owner patch and admission order

1. Parent must choose and record the authoritative identity for the current state-792 Basque compact route, or deliberately reclassify the carrier as Navarra. Reconcile the accepted candidate/research/anchor matrices with `006_current_installed_map_package_bindings.csv:14`; do not silently move the runtime anchor back to `172`.
2. If state `792` remains Basque, parent must accept a route-specific generated flag design and an explicit attribution/ShareAlike policy, or supply an independently defensible sourced runtime design. Do not copy `NAV.tga` or promote `NAV_democratic.tga` as a neutral replacement.
3. Obtain an independent rights/package review for the NAV Aguirre portrait source caveat, while retaining the existing user-supplied styled-final DDS and stable consumer wiring.
4. Re-run the mandatory `chaosx_ai_probability_auditor` workflow when the HOI4 MCP transport is available, using the same named NAV decision, founding-mission, focus, AI-strategy, and Event 006 scenario fixtures. Do not claim balance or ranking from the dated unresolved artifacts.
5. After identity, flag, portrait, and current probability gates close, the smallest central admission change is to add `constant:independence_wave_package_id.iw_013` to the OR list in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202`, then add `iw_013` to the fixed attested order in `common/scripted_effects/006_independence_wave_join_effects.txt:211-248`. The existing adapter, exact normal/scenario NAV branches, region loader, reservation wrapper, setup dispatch, and cleanup paths should be revalidated rather than duplicated.
6. Re-run allocator, scenario, country API, flag, and formable audits plus fresh focus/event/map/technology/probability MCP evidence before any admission claim. FORM-07 remains a separate package-family gate and must not be inferred from NAV admission.
7. Reconcile `docs/events/006_independence_wave/iberian_registered_packages.md:48-52` with the current portrait handoff before promoting any final package status.

## Changed files and identifiers

Changed files: only `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_package_admission_2026-08-26.md`.

Changed tags: none.

Changed states: none.

Changed leaders, characters, portraits, parties, ideas, focus tree ids, decisions, missions, cosmetic tags, formable ids, central adapters, attestation rows, capacity rows, Join rows, or map data: none.

No staging or commit was performed. Parent owns final review and commit.

## Remaining risks, omissions, and blockers

- Package admission is incomplete and intentionally remains fail-closed.
- Current engine evidence for focus, event, map, technology, and probability surfaces is unavailable because the HOI4 MCP transport is closed.
- The installed package exposes no dedicated Technology Tree Viewer.
- NAV flag identity and runtime-art rights remain unresolved for the current Basque state-792 identity.
- NAV Aguirre portrait pixels and wiring pass, but source-rights review remains caveated and independent review is missing.
- Accepted matrices and current runtime binding disagree on compact anchor `172` versus `792`; this is a source-of-truth reconciliation blocker, not permission to write the map.
- FORM-07 remains separately fail-closed and is not part of this NAV admission patch.
- The stale Iberian package summary still describes the old NAV portrait state and must be reconciled by the parent.
- No fallback, generic substitute, copied vanilla asset, broad identity redesign, new focus route, new country package, or major balance change was used.

## Completion statement

The bounded IW-013 audit is complete as an actionable **not admitted** handoff. Source coverage is broad and static validators pass their global contracts, but the package cannot be admitted without the identity/flag decision, rights review, current probability evidence, and central attestation/Join promotion performed by the parent after those gates close.

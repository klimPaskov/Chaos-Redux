# Event 006 IW-024 Banat and IW-032 Slavonia country-package audit

Date: 2026-08-06  
Scope: `IW-024` Banat (`AXX`) and `IW-032` Slavonia (`BFX`) in the Balkans/Danube release pool.  
Owner: `chaosx_country_package_auditor`  
Verdict: **HOLD / not admitted to the runtime package pool**.

## Executive verdict

`AXX` has a valid country shell, localisation, current-map Banat anchor state `82`, and a reviewed runtime flag ladder, but it has no package dispatch adapter, content attestation, setup/final/cleanup path, leader or portrait package, decisions, ideas, or country-specific AI strategy. Its generic region planner row is therefore research visibility only: the central allocation-weight and reservation helpers require content attestation and return zero/not-ready for this package. State `764` is an optional West Banat extension and is not a safe primary anchor because it is also used by the Vojvodina overlay family.

`BFX` has a valid country shell, localisation, and a reviewed runtime flag ladder, but the installed map has no authoritative unique Slavonia state. It has no region planner row, package adapter, content attestation, setup/final/cleanup path, leader or portrait package, decisions, ideas, focus adapter, or country-specific AI strategy. The scenario unbound helper explicitly records `IW-032`/`BFX` as blocked.

Neither country may copy the Transylvania (`TRA`, `IW-023`) package identity. The shared Event 006 focus framework can be reused mechanically only after each country receives its own researched tag/anchor/host/source/leader/force/idea/decision/AI/cleanup adapter and content-attestation proof. FORM-08 currently admits only TRA state `84` and AXX state `82` after the sibling geography guard, while its runtime minimum remains three members/consents/anchors, so the formable is not operationally satisfiable with the current two-member gate.

## Country-package coverage checklist

| Surface | IW-024 Banat (`AXX`) | IW-032 Slavonia (`BFX`) |
|---|---|---|
| Tag registration and country definition | Partial pass: registered shell only | Partial pass: registered shell only |
| History, politics, party, law setup | Dormant neutral shell only; runtime replacement is absent | Dormant neutral shell only; runtime replacement is absent |
| Current-map anchor | State `82` (Banat) is confirmed; state `764` is optional extension | No unique current-map Slavonia anchor; unbound |
| Region planner | Generic `can_plan_iw_024` and load/reserve shell exist | No `can_plan_iw_032`, load, or reserve row |
| Package dispatch/content attestation | Missing | Missing |
| Setup/final validation/cleanup | Missing | Missing |
| Focus loading and route ownership | No package adapter; generic tree is not admission proof | No package adapter; generic tree is not admission proof |
| Decisions and missions | Missing | Missing |
| Ideas and lifecycle | Missing | Missing |
| Leaders, characters, advisors, portraits | Missing | Missing |
| Flags | Runtime ladder is handed off; older source-research prose is stale | Runtime ladder is handed off; older source-research prose is stale |
| Country-specific AI strategy/probability | Missing; attestation-gated allocator weight is zero/not-ready | Missing; no allocator surface |
| Starting forces, technology, industry, supply, production | No country-specific runtime setup | No country-specific runtime setup |
| FORM-08 participation | Helper has an AXX state `82` branch, but AXX package readiness is absent | Explicitly outside the current geography guard |

## File-surface checklist and concrete findings

### Tags, country definitions, history, and localisation

- `common/country_tags/006_independence_wave_countries.txt:25` registers `AXX = "countries/006_independence_wave_AXX.txt"` and `:28` registers `BFX = "countries/006_independence_wave_BFX.txt"`.
- `common/countries/006_independence_wave_AXX.txt:1-11` and `common/countries/006_independence_wave_BFX.txt:1-11` contain graphical cultures and colours only; their headers state that runtime must supply territory, capital, politics, leaders, forces, ideas, focus, and AI.
- `history/countries/AXX - Banat.txt:1-16` and `history/countries/BFX - Slavonia.txt:1-16` are dormant neutral shells with elections disabled and no package-specific starting setup. The current working tree contains these neutral-shell edits from the parent work; this audit did not alter or revert them.
- `localisation/english/006_independence_wave_countries_l_english.yml:156-171` covers Banat/Banatian name keys and `:207-222` covers Slavonia/Slavonian name keys.
- `audit_chaosx_country_tags.py --surface-scan` reported `Protected Event 006/Soviet tags: 136; external country-definition collisions: 0; external identity-surface collisions: 0; random-event roots skipped: 1`. No tag remapping is warranted.

### Map and state setup

- Vanilla `history/states/82-Banat.txt` defines state `82` with owner `ROM`, Banat victory point province `9606`, provinces `646 662 3649 9606 11592 11608`, and ROM/TRA cores. This is the reviewed AXX anchor.
- Vanilla `history/states/764-West Banat.txt` defines state `764` with owner/controller `YUG`, victory point province `3614`, provinces `614 3614 6643 11787`, and YUG/SER/TRA cores. It is an optional extension and overlaps the Vojvodina-family geography; it must not replace state `82` as the AXX anchor without a new crosswalk decision.
- Vanilla `history/states/109-Eastern Croatia.txt` is a broad Croatia state with YUG ownership and CRO/YUG cores, not an attested Slavonia state. No unique BFX anchor is available on the current map.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` records IW-024 as `ready_unique_state_confirmed` at state `82` and IW-032 as `disabled_no_unique_current_state`/`unbound`.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt:1101-1107` records IW-032 and BFX in the scenario unbound/blocked arrays.
- Required MCP map inspection was run in workspace `mod_chaos_redux_ea3b2d67c2c0` for states `82, 764, 84, 76, 106, 970, 802`; status `MAP_INSPECTED`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/607cb65e72df872f6b7a4088d35f4efdc1b15839f05a2b58613f63fabf343ec2/a6a97135cfdbdadbcef1198bcd4e5a00463940c4f33dd8c51a00ed7aeb1159ce/map-inspect.8d2d804287013e4a.json`. State membership and connected map data were returned; the tool also reported unrelated global invalid building-position and floating-harbor diagnostics.
- Required MCP map rendering was run with state overlays, coastlines, victory points, resources, state buildings, supply nodes, and railways; status `MAP_RENDERED`, validation passed, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e055b7b04365920a70aa5119fb6979a3b584c1d81b1da3350217b13f7464b750/f2e83942bc337ed0920374f81ac7ad020304131ebaf086fc364bbcfec5bffb39/map-state.png`.

### Planner, dispatch, setup, and cleanup

- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt:20-27` exposes a generic `can_plan_iw_024` gate for AXX/state `82`, but it is not an exact package content contract. There is no `can_plan_iw_032` trigger.
- `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt:18-28` loads IW-024 as group `rg_danube_borderland`, region `balkans_danube`, depth `standard`, archetype `mountain_or_frontier`, disposition `automatic_if_unique_state`, candidate `AXX`, anchor `82`, and primary host `owner`. No IW-032 load effect exists.
- `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt:107-126` gives IW-024 an automatic weight row and `:129-137` gives it reserve helpers for state `82` with optional state `764`; no IW-032 weight or reserve exists.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt:274-283` includes IW-024 in a ranked scenario list, but `:1101-1107` explicitly marks IW-032/BFX unbound.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-49` has no IW-024 or IW-032 adapter IDs. The content-attestation list at `:51-130` and exact runtime preflight at `:135-279` likewise omit both packages.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-95` central setup, final validation, and cleanup dispatch only known adapters such as TRA, MAC, and BOS; AXX/BFX are absent.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:43-74` requires a runtime adapter and preflight readiness before execution. `:321-350` counts a package as prepared only after dispatch setup succeeds, so neither country can reach durable execution.
- `common/scripted_effects/006_independence_wave_package_planner_effects.txt:95-142` and `:481-526` gate reservation and allocation weight on content attestation. IW-024 therefore remains zero/not-ready in the central allocator despite its generic research row. This audit did not convert the generic row to `always = no`, because that would change research/scenario visibility without a parent design decision.

### Politics, leaders, portraits, flags, advisors, and parties

- Neither country has a package-specific leader, character, advisor, high-command, commander, portrait, party, or election file. Searches across `common/characters`, `common/leaders`, `gfx/leaders`, `interface`, `common/ideas`, and `common/ai_strategy` found no AXX/BFX-specific package surfaces.
- The neutral dormant history is not a playable political setup and cannot satisfy the runtime country-package contract by itself.
- Runtime flag ladders are present at `gfx/flags/AXX.tga`, `gfx/flags/AXX/medium/AXX.tga`, `gfx/flags/AXX/small/AXX.tga` and ideology variants, with equivalent BFX paths. `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/gfx_handoff.md:7-15`, `metadata/flag_validation.json`, and `manifest.md:7-12` mark both ladders `handed_off` with 82x52, 41x26, and 10x7 outputs.
- Older source-research documents still say Banat/Slavonia flags are blocked, including `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:46`, `006_generated_flag_blockers.md:5,13`, and `docs/assets/006_independence_wave/mediterranean_danube_flag_sources_2026_07_15/README.md:25`. Treat those statements as stale provenance/status prose, not as evidence that the current runtime TGA ladders are missing.
- No portrait-worker evidence exists for either country. Any fictional personal leader would require an explicit portrait-worker handoff, gender-consistent regional name pool, metadata, processed master/runtime outputs, and portrait-specific wiring before admission.

### Focus, decisions, ideas, technology, and assets

- Required MCP focus inspection of `common/national_focus/006_independence_wave_focus.txt`/`independence_wave_focus_tree` returned `FOCUS_INSPECTED`/`ok` for the generic 184-node tree. Required focus rendering returned `ok` for the generic 21424x2440 layout. The evidence proves the shared tree exists, not that AXX/BFX own a route or have a package adapter.
- `common/scripted_effects/006_independence_wave_focus_effects.txt:29-84` loads the full framework only through an assignment adapter, while `common/scripted_triggers/006_independence_wave_focus_triggers.txt:32-86` requires a full/additive contract and admits only reviewed additive carriers. AXX/BFX do not satisfy those contracts.
- No AXX/BFX decision, mission, idea, icon, or country-specific focus node files exist. The generic force constants in `common/scripted_effects/006_independence_wave_force_package_effects.txt` and `common/script_constants/006_independence_wave_force_package_constants.txt` include numeric p24/p32 profiles, but no country setup adapter consumes them.
- No country-specific starting technology, industry, production, army, navy, air force, equipment, manpower, supply, railway, port, or fuel setup exists. The dormant histories intentionally contain no such setup.
- The installed package exposes no Technology Tree Viewer. Technology-tree engine evidence is therefore an unresolved limitation, not a pass; no technology promotion claim is made.

### AI and playability

- No `common/ai_strategy/006_independence_wave_banat.txt` or Slavonia equivalent exists, and no country-specific focus/decision AI profile is wired.
- The central allocator’s dynamic weights and reservation are content-attestation-gated, so no meaningful AXX/BFX selection probability, dominance, starvation, timing, or live-AI claim is justified from source alone.
- The required `chaosx_ai_probability_auditor` pass found no AXX/BFX strategy file and no country-specific decision, mission, focus, or strategy surface. The generic strategy probe returned `PROBABILITY_SURFACE_EMPTY` with `No weighted blocks matched this request`; expected Banat and Slavonia strategy paths returned `PROBABILITY_SOURCE_NOT_FOUND`.
- AXX is present in the complete Region-03 random-list selector only as entry 2 (`iw_024`) and is conditionally proportional to whatever upstream weight is declared. This does not prove a live-world rate because gate state, capacity, host, anchor, and candidate-allocation outputs were not supplied.
- BFX/IW-032 is absent from the complete Region-03 selector and has no `prepare_weight_iw_032` or candidate entry, so its current automatic selection probability is exactly zero by source-pool exclusion. That is an unimplemented/blocked package surface, not a balance result.

### Mandatory AI/probability auditor evidence

- `hoi4.probability_inspect` with adapter `random_list` against `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt`/`independence_wave_select_region_03_automatic_package` returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, `candidates=8`, `requiredInputs=8`, and `unresolved=0`. Source revision: `ec3fd2a80e7a70b9556167d7964ea4a6ca11c336c250f9d541ce887e4e054099`; source hash: `ff114c943badadd55246dac02b8e5ec434090d0339957dd696559afa17b360bf`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b983da7c81c4095360b663b6858b615a00997d6e08fe2dc53cd849459ac3d2d/0f93c966a3a3581e89f0c288e660be4bef00a24ef1368ec49bdefaccaa87b632/probability-inspect-ff114c943bad.json`.
- Declared-weight evaluations were exact only conditional on the supplied weights: AXX was `1.0` when it was the sole positive entry, `1/3` in an AXX/MAC/BOS three-entry pool, `1/8` in an all-eight equal pool, and `0` when its declared weight was zero. These scenarios are not live-world selection rates.
- The AXX-only evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ef834e5c004d9a3d9b2edaaf938e6420680eb9ec4e4246c20e6ec4a257d745c/b21dd19855536596fa5cc1b0a598b670be8e34c23161c7c2fc6d6952067b4736/probability-b55ef39c73accfba7b228102.json`.
- The AXX/MAC/BOS evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df2455354c583483668bbe7e828eadbff7d56f783c850430b80e77adb9c479fa/5e413101eb8e64daa80a4b7c82a5077efafda7422557bd7638a1ca06661edc35/probability-f6af272d0bba37d81b10743f.json`.
- The AXX-blocked evaluation artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b37188b45f1c1a1c25fe0e14eef3360bd795f3b70a982bb6dd6abbd53877076/815056337e6fa75ee856c7241bd2335c1ccefde997a1ea36c202506dc1ff935b/probability-da5f4cc24393e1c454b50b68.json`.
- No `probability_compare`, sweep, simulation, sequence, timing distribution, or same-scenario before/after run was justified because there is no owner-applied package patch and no complete live transition manifest. Do not claim normalized AI balance, survival, route dominance, timing, repetition, or exploit safety.

## FORM-08 interaction

- Current `common/scripted_triggers/006_independence_wave_form08_triggers.txt:13-40` admits only TRA state `84` and AXX state `82` after the sibling geography guard. `common/scripted_effects/006_independence_wave_form08_effects.txt:1-12` and `:81-87` likewise cover TRA `84/76` and AXX `82`; MAC/state `106` has been removed by the sibling patch.
- FORM-08 readiness still requires the constants for minimum members, consents, and anchors, all equal to three. With only two current eligible branches, and AXX package readiness absent, FORM-08 cannot satisfy its own readiness proof.
- `docs/systems/006_independence_wave_form08_danubian_confederation.md:3,13,29,37` still describes the broader TRA/AXX/MAC and named Slavonia/Vojvodina scope and should be reconciled by the parent documentation pass; this audit did not edit that source-of-truth document.

## Archetype and reuse decision

The TRA package is identity-specific and cannot be copied for AXX or BFX. TRA owns exact tag/capital/host checks, a command roster, additive decisions, ideas, AI strategy, force setup, focus assignment, and cleanup in `common/scripted_triggers/006_independence_wave_transylvania_package_triggers.txt`, `common/scripted_effects/006_independence_wave_transylvania_package_effects.txt`, `common/decisions/006_independence_wave_transylvania_decisions.txt`, `common/ideas/006_independence_wave_transylvania_ideas.txt`, and `common/ai_strategy/006_independence_wave_transylvania.txt`. Macedonia provides the same identity-specific pattern at state `106`. AXX/BFX may reuse generic helper mechanics and the shared focus framework only after a separate researched adapter and content-attestation proof are implemented.

## Required MCP evidence

- Event inspect `chaosx.nr6.1`, `state_flow`, bounded depth/nodes: status `EVENT_INSPECTED_PARTIAL`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/42071ef03f77bbceff195372600ec571a6effd7c7224d32ab2bc87e60ba96256/734a87e63bff840f64f8beb2772c6dbc2fdb577623e4c7d9bb279d86bd2492b0/event-state_flow-be8a459e7129.json`.
- Event render `chaosx.nr6.1`, overview/downstream: status `EVENT_RENDERED_PARTIAL`; manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/325218c3e0bd69803977270ddf9996613c077459830c5d8f6cd5485cd1a3c48d/a67417b3fc1fb362726df5d99e133d2697e844f1c595862b0b6479e4c5ff0a3f/event-overview-be8a459e7129-manifest.json`, JSON `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/325218c3e0bd69803977270ddf9996613c077459830c5d8f6cd5485cd1a3c48d/a67417b3fc1fb362726df5d99e133d2697e844f1c595862b0b6479e4c5ff0a3f/event-overview-be8a459e7129.json`, SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/325218c3e0bd69803977270ddf9996613c077459830c5d8f6cd5485cd1a3c48d/a67417b3fc1fb362726df5d99e133d2697e844f1c595862b0b6479e4c5ff0a3f/event-overview-be8a459e7129.svg`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/325218c3e0bd69803977270ddf9996613c077459830c5d8f6cd5485cd1a3c48d/a67417b3fc1fb362726df5d99e133d2697e844f1c595862b0b6479e4c5ff0a3f/event-overview-be8a459e7129.png`.
- Focus inspection/render: status `ok` for the generic `independence_wave_focus_tree`; the MCP surface contains no AXX/BFX adapter or country-owned route.
- Map inspection/render: statuses `MAP_INSPECTED` and `MAP_RENDERED` with the artifacts listed in the map section above.
- The event/focus renders are bounded partial views of large shared surfaces and are not claims that the whole Event 006 graph or generic tree is complete for these countries.

## Patch status and remaining blockers

No gameplay patch was applied. The generic IW-024 planner gate was intentionally preserved because central weight/reservation already require content attestation and a forced `always = no` change would alter research and scenario visibility without a design decision. No tag, map, country history, focus, decision, idea, AI, portrait, or flag wiring was changed.

Admission remains blocked by the missing AXX/BFX package adapters and content attestation, missing identity-specific setup and cleanup, missing leaders/portraits/parties/ideas/decisions/AI, and (for BFX) missing unique geography. A future implementation plan should live under `docs/plans/006_independence_wave_plans/` and must resolve the installed-map crosswalk before any BFX package is designed.

Simplifications and omissions: no package promotion, no runtime/game test, no Technology Tree Viewer evidence, no portrait production, and no balance claim were made. These are deliberate blockers, not completed surfaces.

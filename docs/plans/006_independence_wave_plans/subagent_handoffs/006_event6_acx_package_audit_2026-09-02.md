# Event 006 ACX Cornwall package audit — 2026-09-02

Date: 2026-09-02 (Europe/Kyiv).

Owner: `/root`.

Subagent: `/root/event6_acx_audit_0902`.

Scope: Source-only readiness audit for IW-003 Cornwall (`ACX`) against the current Event 006 accepted specifications, research rows, installed-map binding, runtime package registries, identity and asset manifests, package gameplay surfaces, and Event 006 admission/Join contracts.

## Disposition

**HOLD / fail-closed.** ACX is not a selectable or admitted Event 006 package in the current checkout.

The accepted research and candidate rows retain the planning baseline `state 123` / `RG-123`, but the current installed-map binding explicitly overrides that planning row to `disabled_no_unique_current_state` and `unbound`.

The current source has only an ACX country tag, graphical-culture/color shell, neutral dormant history, country-name localisation, broad registry constants, blocked-row bookkeeping, and readiness-only flag/portrait files.

ACX has no current unique map anchor, package-local adapter, content attestation, region loader/weight/reservation contract, setup/final-validation/cleanup dispatch, deterministic Join entry, character consumer, portrait `.gfx` consumer, package focus route, package decisions/ideas, starting force/technology/industry/supply setup, or AI strategy surface.

No map, allocator, central admission, Join, gameplay, localisation, flag, portrait, or other source file was changed by this audit.

The only file added by this pass is this dated handoff; no staging or commit was performed.

## Authority and method

The current authority is `docs/specs/006_independence_wave_specs/quality/package_manifest.md`, which records Event 006 at 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows out of 193 non-overlay rows, with automatic ladder `3/4/5/7/10` and World Collapse at `10`.

The package contract is `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`; the Level 1 package requirements include a unique anchor, viable capital, host survival, country identity, leadership, forces, ideas, focus/decision/localisation coverage, flags, and AI/playability evidence.

The IW-003 research row is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:4`.

The IW-003 candidate row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:4`.

The current binding authority is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:4`.

The required offline Paradox wiki pages were consulted before source inspection, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, State modding, Map modding, Character modding, Portrait modding, Cosmetic tag modding, National focus modding, Technology modding, and Division modding.

The required vanilla documentation was consulted from `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, and `script_concept_documentation.md`.

The applied repository guidance was `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-event-assets`, and `chaos-redux-comfyui`; no skill was created or updated.

## Country package coverage checklist

| Surface | Status | Evidence and exact identifiers |
| --- | --- | --- |
| Tag registration | Partial | `common/country_tags/006_independence_wave_countries.txt:15` maps `ACX` to `countries/006_independence_wave_ACX.txt`; this is a dormant shell registration, not admission. |
| Country definition | Partial | `common/countries/006_independence_wave_ACX.txt:8-11` contains only `commonwealth_gfx`, `commonwealth_2d`, and `rgb { 54 73 92 }`; runtime territory, capital, politics, leaders, forces, ideas, focus, and AI are absent. |
| Country history | Partial | `history/countries/ACX - Cornwall.txt:9-16` sets only neutrality, `elections_allowed = no`, and 100 neutrality popularity; there is no capital, ownership, cores, units, technology, production, industry, supply, or starting setup. |
| Unique current-map anchor | Blocked | Current binding row `IW-003` is `disabled_no_unique_current_state` / `unbound`; no legal current Cornwall state is available. |
| Host survival and transfer | Blocked | No ACX execution package can be selected, so host-retention, ownership transfer, former-host, capital, and release receipts are not evaluable for this package. |
| Politics and parties | Partial | Neutral dormant history exists, but no ACX party definitions, party names, popularity/stability/war-support tuning, laws, elections, diplomacy, subjects, guarantees, or route setup exist. |
| Leadership and characters | Missing | No `ACX` entry appears in `common/characters/006_independence_wave_characters_registry.txt`; no leader, advisor, high-command, commander, trait, roster checkpoint, or institutional-name consumer exists. |
| Portrait wiring | Readiness only | Two 156x210 DDS candidates exist under `gfx/leaders/006_independence_wave/`, but `interface/006_independence_wave_portraits_registry.gfx` has no ACX sprite and no character consumes either file. |
| Flag identity | Readiness only | Unsuffixed normal/medium/small `ACX.tga` files exist and the St Piran motif is documented as a researched civic design; the package has no accepted sovereign-identity/attestation receipt. |
| Localisation | Partial | `localisation/english/006_independence_wave_countries_l_english.yml:3-18` covers ACX country/adjective and ideology aliases; there are no ACX leader, party, advisor, idea, focus, decision, mission, or tooltip keys because those objects do not exist. |
| Ideas and national spirits | Missing | No ACX hit exists in `common/ideas/006_independence_wave_ideas_registry.txt`; no starting weakness, lifecycle, icon, or recovery path exists. |
| Focus route | Missing | No ACX focus branch or assignment exists; only the shared generic tree is present. |
| Decisions and missions | Missing | No ACX decision category, decision, mission, timed objective, icon, or route unlock exists. |
| Forces and OOB | Missing | No ACX OOB, division template, army, navy, air force, equipment, manpower, reinforcement, or military-tradition setup exists. |
| Technology and research | Missing | No ACX research slots, starting technologies, doctrine, equipment research, or technology-tree dependency exists. |
| Industry and supply | Missing | No ACX factories, buildings, railways, ports, depots, supply, trains, convoys, fuel, or production lines are assigned. |
| AI and playability | Missing | No ACX `ai_strategy`, focus AI, decision AI, diplomacy AI, template, front, or survival behavior exists. |
| Formables and cosmetic routes | Unresolved | No ACX-specific formable or route consumer is admitted; broad formable registries do not substitute for a package identity/territory contract. |
| Research/manifests | Partial | The research and asset manifests describe ACX as a readiness candidate, but there is no complete package manifest, admission receipt, or rights-cleared live consumer. |

## File surface checklist

| File or surface | Finding |
| --- | --- |
| `common/country_tags/006_independence_wave_countries.txt:15` | ACX tag registration exists. |
| `common/countries/006_independence_wave_ACX.txt:1-11` | Country shell owns only graphical cultures and color. |
| `history/countries/ACX - Cornwall.txt:1-16` | Neutral dormant loader only. |
| `history/states/` in the mod | No local state override exists. |
| `common/script_constants/006_independence_wave_constants_registry.txt:7499` | `independence_wave_package_id.iw_003 = 3` exists; broad tag lists at `:807`, `:811`, `:836`, `:844`, and `:906` are classifier/registry data, not admission. |
| `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:10-14` | Explicitly says IW-003 is absent because no unique Cornwall anchor exists. No `can_plan_independence_wave_package_iw_003` block exists. |
| `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:10-14` | Region 01 loader list starts with IW-001 and contains no ACX/IW-003 loader. |
| `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:213-264` | Weight preparation contains IW-001, IW-002, IW-004 through IW-010, and IW-012, but no `independence_wave_prepare_weight_iw_003`. |
| `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:271-359` | Reservation functions contain other region-01 packages, but no `independence_wave_reserve_package_iw_003`. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-157` | Runtime adapter OR-list has no IW-003 package ID. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:159-202` | Content-attestation OR-list has no IW-003 package ID. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-225` | Preflight requires adapter and content-attestation predicates that ACX does not satisfy. |
| `common/scripted_effects/006_independence_wave_effects.txt:3640-3746` | Central setup, final-validation, and cleanup dispatchers call other package wrappers and have no ACX branch. |
| `common/scripted_effects/006_independence_wave_join_effects.txt:236-271` | Deterministic Join probes the fixed attested package sequence and omits IW-003. |
| `common/scripted_effects/006_independence_wave_scenario_effects.txt:1131-1132` | The scenario reset explicitly appends `iw_003` and `ACX` to blocked-row arrays. |
| `common/scripted_triggers/006_independence_wave_triggers.txt:596-945` | Runtime-ready wrappers exist for admitted or scenario packages, but no `is_independence_wave_runtime_automatic_package_iw_003_ready` wrapper exists. |
| `common/scripted_triggers/006_independence_wave_package_triggers.txt:309-314` | ACX is in the broad Event 006-owned-tag classifier only; that classifier does not prove package readiness. |
| `common/characters/006_independence_wave_characters_registry.txt` | No ACX character or leader identifier. |
| `interface/006_independence_wave_portraits_registry.gfx` | No `ACX` or `GFX_portrait_ACX_*` sprite. |
| `common/ideas/006_independence_wave_ideas_registry.txt`, `common/decisions/006_independence_wave_decisions.txt`, `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` | No ACX package-local ideas, decisions, missions, category, AI strategy, or strategy factor. |
| `common/national_focus/006_independence_wave_focus.txt` | Shared tree only; no ACX branch or assignment. |
| `docs/plans/006_independence_wave_plans/package_bindings/006_force_package_mapping.csv:4` | Planning row describes coastal guards/mining militia, but no corresponding executable ACX force package exists. |

The unrelated `common/scripted_effects/fallout_consolidated_effects.txt:71070` and `:71304` ACX references belong to the generic Fallout fracture template and are not Event 006 ACX package evidence.

## Map and state setup

The current read-only map inspection used `query = "Cornwall"`, `stateIds = [123]`, and province IDs `540, 3422, 3463, 6526, 9562, 11406`.

The current map reports 13,414 province definitions, 1,081 states, 304 strategic regions, and 534 ports.

The query returned `queryMatchCount = 0`; no current state name resolves to Cornwall.

Requested state `123` resolves, but the vanilla state is `STATE_123 = "South-West England"` and contains provinces `540 3422 3463 6526 9562 11406`.

The vanilla source is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\123-Cornwall.txt`; it is owned by ENG, has victory points at 540 and 6526, and includes shared buildings and a naval base at 540.

The audited Cornwall-only geometry is province `6526` (Truro), while province `540` (Plymouth) and province `11406` remain in state 123 with the other South-West England provinces.

The accepted map feasibility record states that legal next state ID `1082` collides in eleven installed Workshop mods, every ID through `2525` is claimed, and first unused ID `2526` would create an invalid gap.

State 123 is therefore not a legal unique Cornwall anchor, and no fallback state, filler ID, renumbering, or invented map anchor is authorized.

No map rewrite or state reassignment was attempted.

## Politics, leadership, portraits, flags, advisors, and parties

The ACX history loader sets neutrality to 100 and disables elections, but no Event 006 government route, party names, laws, stability, war support, diplomacy, subjects, guarantees, faction state, or cleanup exists.

The accepted research row requires a provisional assembly, cabinet, municipal council, or congress with regionally sourced institutional names, and requires sourced real male officeholders or authentic archival material for the actual institution.

The current portrait manifests contain readiness-only sourced treatments for Arthur Thomas Quiller-Couch as a Cornish civic candidate and Richard Fortescue Phillimore as a Cornish coastal commander.

The Quiller-Couch handoff explicitly says the role adaptation is not proof that he held a named 1936 Cornwall provisional office, so it cannot independently clear the institutional leadership gate.

The stable runtime DDS paths are `gfx/leaders/006_independence_wave/portrait_ACX_cornish_port_and_mines_committee.dds` and `gfx/leaders/006_independence_wave/portrait_ACX_cornish_coastal_commander.dds`.

The source-placeholder manifest records the committee DDS SHA-256 as `2b3b98f4621bc43f0f517a28f984337755bf193746d0dadcedffeb4f2cd9a0b8` and the commander DDS SHA-256 as `b6b84c64e16c6112ff117300b6271a3e50e239acc663cf5fc7c7641673ed50e6`.

No character or `.gfx` consumer exists, so no leader metadata is available for a female/male portrait-name check; no opposite-gender pairing was found in live wiring because there is no live ACX wiring.

The flag source/research handoffs document a black field with a centered white St Piran's Cross as a researched Cornish civic motif fitted to the HOI4 `82x52` ladder.

The unsuffixed files `gfx/flags/ACX.tga`, `gfx/flags/medium/ACX.tga`, and `gfx/flags/small/ACX.tga` exist with SHA-256 values `e44993e121278c5d5dd72d51cd78d47c66f34f256e12e3c80e4fc11af70cfaad`, `38aa26dad200038e0bb3db84d651227312ea9941e31505f49541cb100b2fe1fb`, and `c47d991628fe98cc8b7c6c669521530319cc4b8f35b06c5aff23a93dd0bfa718` respectively.

The flag evidence is a civic/readiness identity, not an accepted sovereign 1936 flag or runtime admission receipt.

The current asset audit also records 48 unapproved ideology-suffix aliases across ACX, AFX, AGX, and AJX; those aliases are not an authorization to use ACX or to create route-specific flag consumers.

## Focus, decisions, ideas, and assets

The read-only focus inspection of `common/national_focus/006_independence_wave_focus.txt` and tree `independence_wave_focus_tree` returned 184 focuses, 195 connectors, zero focus diagnostics, and only the unrelated missing vanilla localisation warning `continuous_restrict_freedom_desc`.

The shared tree render is structural evidence for the generic framework only; it does not establish an ACX branch, assignment, localisation, AI path, or package route.

No ACX focus ID, package-specific focus reward, decision, mission, idea, icon, category, or promised unlock is present.

The existing flag and portrait files are archived or runtime readiness candidates only; no ACX asset is wired to a live consumer.

No ACX event-owned GUI exists, so no GUI inspection/render was applicable; the shared Event 006 Statehood Ledger is outside the country-owned ACX surface.

## Starting military, technology, industry, supply, and production

The dormant ACX history has no OOB, division template, unit, equipment stockpile, manpower setup, research slot, technology, doctrine, production line, factory, railway, port, depot, convoy, train, fuel, or supply setup.

The force mapping row in `006_force_package_mapping.csv` is planning metadata and cannot be treated as an executable coastal-guards/mining-militia package.

The read-only technology scan found no ACX-specific technology dependency or source reference.

The installed Technology MCP scan is global rather than ACX-specific and returned 679 technologies, 18 folders, 475 placements, 457 edges, 857 unlocks, 1,302 issues, and 3 unresolved items; the render marked `sourceAccurate = false` with 1,421 global blocking technology diagnostics.

The installed package exposes no Technology Tree Viewer, so no technology-tree consumer claim is available for ACX.

## AI and probability

No ACX AI strategy block, strategy factor, focus AI, decision AI, diplomacy profile, template, front behavior, or survival behavior exists.

The mandatory direct `hoi4.probability_inspect` custom-pool pass used source `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` and candidate pool `iw_003`, `ACX`.

It returned `PROBABILITY_SOURCE_INSPECTED` with zero active candidates, zero available candidates, `poolComplete = false`, and two unresolved candidate entries, both `CANDIDATE_NOT_FOUND` for `iw_003` and `ACX`.

The custom-pool artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/483727b25e61cdb1e0ea892fc9454dd492192e91966dff212f1d1be78a2e5b9e/b06a798650264bc89fd4a5323976a93ebbb0c9592df45fda47ed732a63d0de96/probability-inspect-eb4ff7688ee4.json`.

The direct `ai_strategy_factor` inspection of `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero candidates, zero required inputs, and zero unresolved diagnostics.

The AI-strategy artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f992c00c29dbd0112b4806af07e40fa781bd0fd0f4af48c5ad16ed51251e3992/a756881bfa78b14ed3d9474b158fc147193c99ccb0a5863846cde23a918aafd0/probability-inspect-c5fef71b5a54.json`.

No probability evaluation, sweep, simulation, or comparison was run because there is no ACX weighted surface or owner patch to compare.

No callable `chaosx_ai_probability_auditor` route was exposed in this runtime; direct MCP inspection is not equivalent auditor evidence, and no quantitative AI or balance claim is made.

## Event 006, admission, attestation, and Join surfaces

The Event 006 source root remains `chaosx.nr6.1`.

The read-only event scan returned `EVENT_INSPECTED_PARTIAL` after workspace-scale helper/lifecycle deferral; it did not establish an ACX event branch or package consumer.

The event trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43df026f60f7b50b4f9478d00e27ca4cc8540e6310097c66b4b7ecb684288848/aee549c6309b7befecab6a9955d41b291ce4e2dce701b8f16d7e763acfc9a985/event-trace-2725045f62d1.json`.

The event overview render artifact manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/33d930575710c63fd8f5e4df7726ac400081d0e0f12e4c0a8bd1e10e7d19fb30/b68d6fd4de543b08108879656ed4f12857424a51fbce2f497f2dfff444abcfa4/event-overview-2725045f62d1-manifest.json`.

The package dispatch trigger registry has no IW-003 adapter or attestation branch, and its preflight predicate requires both absent branches.

The central setup, final-validation, and cleanup dispatchers have no ACX wrapper call.

The region trigger/effect registries have no ACX plan predicate, loader, automatic weight, or reservation function.

The deterministic Join probe omits IW-003 from the fixed attested sequence.

The scenario reset deliberately records `iw_003` and `ACX` in blocked-row arrays, confirming fail-closed treatment rather than an accidental omission.

## Read-only MCP evidence

The map inspection returned `MAP_INSPECTED` at revision `bfaf7becc0c8c796e4a90a965eb38ab8db5b7a4bde2e0f4219c810810172632f` and found no Cornwall query match.

The map inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f684689df0400ce55cef968a72d2b90d83dc4d51a7e55cc8afa5e0bae244799/e0673b433c731baa7d03297ab252b6c9c4782065816dbc6ac1447935df6e83d4/map-inspect.bfaf7becc0c8c796.json`.

The map render returned `MAP_RENDERED` with validation passing for the rendered state/overlay view; its PNG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7c61c3ec5ca46dd68658d390c220b5a7c89b0a3623f87dcd32a33f99b1771171/f26908ba1857251da672f9bc0e3cf6a068b715577654a2f3b214d2a4ecfdb8a7/map-state.png`.

The map inspection overall remained partial because unrelated workspace diagnostics include 1,332 `MAP_PORT_ADJACENT_SEA_INVALID` entries, 1,323 `MAP_BUILDING_POSITION_INVALID` entries, and malformed localisation at `localisation/english/039_murder_mystery_l_english.yml:389`; these were not edited.

The focus inspection returned `FOCUS_INSPECTED` with 184 focuses, 195 connectors, zero diagnostics, and no ACX branch.

The focus inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/35b1f84dd797813ac049a2e91f5bd27af5fe6f4c8f0759474b7f215af915ff85/a53a900e03ad2697c199b9310ee3e560404ab7e3d572be3d7ec4c60b5de61213/focus-inspect.04bfe5d11c3d3b54.json`.

The focus render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a0e0bc769460f88d7363eed1e3e015b809c0c67b732001dc476e845f7a255d1/2e83bfe04cfc5679dc04d0b13cf6d9c4a5ad74c216d1a4fca3cc9a8d8c43a661/independence_wave_focus_tree.focus.html`.

The technology inspection returned `TECH_INSPECTED` only for the global technology graph and did not provide ACX-specific evidence.

The technology scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ae20a31bc164adffa8df56c6690843925b3795f24f3434ed3277ec9b370e14e0/3d7be4f7ee31814a920505bbc061b402707e63fa49598fea6554e7a28abb7d84/technology-scan-2de5d7ac62a5.json`.

## Required next owners

1. The map/state owner must establish and independently audit a legal, contiguous, unique current-map Cornwall anchor and prove former-host survival without inventing a state, using the existing map binding workflow and no fallback identity.

2. The country-package owner must then complete the ACX Level 1 package: capital/territory, politics and parties, institutionally named leadership, source-cleared portrait consumers, accepted flag identity, ideas, forces/OOB, technology/industry/supply setup, localisation, cleanup, AI, and any required decisions/focus route.

3. `chaosx_portrait_creator` must resolve the actual institutional/person identity and provenance gate, then add portrait-specific `.gfx` and character wiring only after a package owner accepts the role and map gate.

4. The flag/identity owner must resolve civic-versus-sovereign presentation and document the accepted period design without treating unapproved ideology suffix aliases as route assets.

5. The package adapter/attestation owner may reopen region loader/weight/reservation, runtime adapter, central setup/final-validation/cleanup, preflight, and Join only after the map and complete package receipts exist.

6. The parent must rerun current map, event, focus, technology, probability, country-package, asset, and central-attestation audits after those receipts; no current evidence supports promotion now.

## Validation, uncertainty, and remaining risks

Source scans found no ACX references in the character, idea, decision, focus, portrait-GFX, or AI strategy surfaces listed above, apart from the broad classifier and unrelated Fallout template references explicitly noted.

The strict Event 006 flag-family script reports 102 registered tags and 102 complete flag families, but that aggregate result does not attest ACX identity or package admission.

The country-tag surface-audit script named in older handoffs is absent at `.tools/audit_chaosx_country_tags.py`, so the full scripted collision scan was not rerun in this pass.

The installed tag-collision artifact `docs/plans/006_independence_wave_plans/006_installed_tag_collision_audit_2026_08_06.json` is stale relative to this audit and must be regenerated before any future admission.

The event MCP results are partial because workspace-scale helper/lifecycle passes were deferred, and the technology MCP result is global and diagnostically blocked; neither result upgrades ACX readiness.

The current map and source evidence are sufficient to keep ACX fail-closed, but not sufficient to design or choose a replacement anchor, infer host survival, or claim gameplay balance.

No live Hearts of Iron IV run or save/release test was performed; that validation remains outside this read-only subagent scope.

## Simplifications, omissions, and blockers

No gameplay, map, allocator, admission, Join, asset, or localisation patch was made.

No fallback state, invented map anchor, tag substitution, central attestation bypass, generic leader relabelling, or whole package was created.

No probability comparison or quantitative AI claim was made because ACX has no active weighted surface and the named custom auditor route is unavailable.

No technology-tree completion claim was made because ACX has no technology source and the installed package has no Technology Tree Viewer.

The package remains incomplete until the current-map binding, identity/portrait, flag, package gameplay, AI, attestation, and Join gates are independently resolved.

## Changed files

`docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_acx_package_audit_2026-09-02.md` was added as the dated audit handoff.

No other files were changed by this subagent.

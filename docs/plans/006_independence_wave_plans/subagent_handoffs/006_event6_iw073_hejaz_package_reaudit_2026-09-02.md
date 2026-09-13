# Event 006 IW-073 Hejaz (`CUX`) package re-audit

Audit date: 2026-09-02.

Owner scope: read-only country-package re-audit for the current installed-map binding of IW-073 Hejaz (`CUX`). This handoff records current source, engine, asset, and gate evidence. It does not admit IW-073, widen a central OR-list, change the allocator, edit the map, alter the shell consolidation, or stage/commit any change.

## Disposition

**NO-CHANGE / PACKAGE-LOCAL / EVIDENCE-BLOCKED / FAIL-CLOSED.** The installed map anchor and compact states are coherent, and CUX is registered as a dormant Event 006 carrier, but the country remains a loader shell without the Level 2 identity, rights, runtime, gameplay, and central admission surfaces required for a safe tranche. No narrow package-local patch can make the package playable without inventing identity or bypassing the accepted gates.

The working-tree shell consolidation currently routes CUX through `common/countries/006_independence_wave_shared_middle_eastern.txt`. That consolidation is owned by another workstream and remains untouched by this audit. The old per-tag shell is staged/deleted in the dirty working tree; this handoff does not restore it or resolve that unrelated merge state.

## Sources and required references consulted

- `AGENTS.md` and the country-package instructions in the parent task.
- `.agents/skills/chaos-redux-subagents/SKILL.md`.
- `.agents/skills/chaos-redux-events/SKILL.md`.
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`.
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`.
- `.agents/skills/chaos-redux-event-assets/SKILL.md`.
- `.agents/skills/chaos-redux-comfyui/SKILL.md`.
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`.
- Offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, Map modding, and State modding in `paradox_wiki/`.
- Vanilla documentation under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including effects, triggers, modifiers, script concepts, dynamic variables, country, focus, decision, idea, AI, and map/state references where applicable.
- Vanilla `history/countries/SAU - Saudi Arabia.txt` and `common/characters/SAU.txt` as the nearest complete Arabian-country precedent.
- Vanilla state files `history/states/679-Hejaz.txt`, `history/states/856-Asir-Makkah.txt`, and `history/states/855-Tabuk.txt`.

The vanilla precedent has `capital = 292`, `oob = "SAU_1936"`, starting technologies, convoys, a recruited character roster, and fully formed politics. It is evidence for the expected setup shape only; its Saudi identity, characters, portraits, and advisors are not safe CUX substitutes.

## Accepted IW-073 contract

| Field | Accepted value | Current evidence |
| --- | --- | --- |
| Candidate | `IW-073`, Hejaz, Level 2 | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:74` |
| Carrier tag | `CUX` | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:74` and `common/country_tags/006_independence_wave_countries.txt:41` |
| Region and archetype | Levant and Arabia; holy-city and port state | Candidate registry row 74 |
| Reservation group | `RG-ARABIA-HEJAZ-NAJD` | Candidate registry row 74 and current binding row 74 |
| Anchor | State `679`, Madinah | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:74` |
| Compact footprint | `679|856`, Madinah and Asir-Makkah | Current binding row 74 |
| Optional extension | `855`, Tabuk | Current binding row 74; not an automatic release state |
| Former host | `SAU`, host capital state `292` protected | Current binding row 74 and `006_current_map_reservation_groups.csv:65` |
| Formable direction | `FORM-20`, Arabian Federation | `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md` and registry row 74 |
| Package id | `iw_073 = 73` | `common/script_constants/006_independence_wave_constants_registry.txt:7569` |
| Region group id | `rg_arabia_hejaz_najd = 64` | `common/script_constants/006_independence_wave_constants_registry.txt:7991` |
| Required identity | Period-correct civic, municipal, customs, pilgrimage, railway, merchant, local-defense, or dynastic institution | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:74` |
| Portrait rule | Sourced real male officeholder or authentic institutional material; no invented/generated grounded claimant | Research resolution row 74 and accepted Event 006 direction |
| Symbol rule | Period civic flag from researched regional motifs; no invented historic standard presented as authentic | Research resolution row 74 and `006_event6_iw073_hejaz_symbol_source_gate_2026-08-28.md` |

The Level 2 contract also requires country-specific focus/decision/problem/institution paths, a distinctive starting problem, a regional leadership or formable angle, force setup, ideas, AI behavior, localisation, cleanup, and complete central transaction wiring. Those surfaces remain absent.

## Country package coverage checklist

| Surface | Status | Evidence and finding |
| --- | --- | --- |
| Tag registration | Present, dormant | `common/country_tags/006_independence_wave_countries.txt:41` maps `CUX` to the current shared middle-eastern shell. Registration is not admission or content attestation. |
| Country shell | Present, loader-only | `common/countries/006_independence_wave_shared_middle_eastern.txt` supplies `middle_eastern_gfx` and `middle_eastern_2d`, lists CUX as IW-073, and contains no politics, leader, force, idea, focus, or AI setup. |
| Country history | Present, neutral loader | `history/countries/CUX - Hejaz.txt` sets neutrality to 100 and elections off only. Its comments explicitly defer territory, capital, politics, leaders, forces, ideas, focus loading, and AI to runtime formation. |
| Runtime package loader | Partial candidate plumbing | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1508-1521` loads `iw_073`, tag `CUX`, region metadata, and anchor event targets. This is planner metadata, not executable country setup. |
| Candidate trigger | Present, generic availability | `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:624-631` checks plan openness, duplicate package/group exclusion, CUX tag availability, and state 679 availability. It does not validate CUX content. |
| Central adapter | Missing | No `iw_073` or CUX branch exists in the central package dispatch adapter list. |
| Content attestation | Missing | No CUX/IW-073 branch exists in the central content-attestation OR-list. |
| Normal/scenario preflight | Fails closed | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` requires an adapter and content attestation in addition to origin and dormant-scope checks. CUX cannot pass. |
| Execution setup | Missing | No CUX runtime setup branch was found for transfer, capital, politics, leaders, ideas, forces, production, or AI. |
| Final validation and cleanup | Missing | No CUX package-specific final validation, cleanup, release, subject, annexation, or bilateral host handling was found. |
| Deterministic Join | Missing | No IW-073/CUX Join branch was found. A central Join or admission patch would be an unsafe gate bypass while the package is incomplete. |
| Cross-origin ownership | No competing owner found | The bounded Event 005/Event 012 search found no other CUX package owner. This does not authorize borrowing Saudi, Hashemite, or unrelated event content. |
| Formable | Contract only | `FORM-20` is specified but no complete IW-073 formable route is wired or independently validated. |

## File surface checklist

### Present or partially present

- `common/country_tags/006_independence_wave_countries.txt:41` — CUX registration, currently bound to the shared shell.
- `common/countries/006_independence_wave_shared_middle_eastern.txt` — graphical cultures and retained CUX identity comment only.
- `history/countries/CUX - Hejaz.txt` — neutral no-election loader history.
- `localisation/english/006_independence_wave_countries_l_english.yml:411-426` — CUX country name, definite name, adjective, and ideology aliases.
- `common/countries/colors.txt:1366` — CUX colour override in the working tree’s consolidated colour surface.
- `gfx/flags/CUX.tga`, ideology variants, medium variants, and small variants — runtime flag ladder exists.
- `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02_chunk_cox_ebx/source_png/CUX_hejaz_imagegen_raw.png` and `references/CUX_hejaz.png` — source/design flag handoff only.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:74` — current map binding.
- `docs/plans/006_independence_wave_plans/006_current_map_reservation_groups.csv:65` — reservation group and host-protection contract.
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:74` — design-level Hejaz force mapping, not runtime setup.

### Missing or stale for a playable package

- No CUX-owned `common/characters` definition, country leader, provisional institution, advisor, high command, commander, or trait wiring.
- No CUX portrait consumer, portrait-specific GFX registration, rights-cleared source receipt, or accepted male officeholder/institution portrait.
- No CUX-owned ideas or national spirits, lifecycle effects, idea icons, or starting-problem recovery path.
- No CUX-owned decision category, decision, mission, timed objective, or decision icon.
- No CUX-specific focus callbacks, route gates, country focus group, or focus-localisation/icon surface.
- No CUX AI strategy, focus selection, template selection, diplomacy, front, or reinforcement behavior.
- No CUX production, OOB, division-template, manpower, stockpile, convoy, train, fuel, supply, navy, or air setup.
- No CUX-specific event, event option, event target cleanup, transfer, release, puppet, annexation, or subject cleanup.
- No CUX party names, leader names, advisors, ideas, focuses, decisions, or tooltips beyond the country name aliases.
- No accepted evidence that the supplied CUX flag is a period-correct 1936 Hejaz standard. The symbol handoff explicitly treats it as a source/design asset handoff, not identity admission.

The registry and generic arrays contain CUX because it is a reserved candidate. The presence of CUX in `all_resolved_carrier_tags`, `event6_owned_new_tags`, `selectable_bound_tags`, `event6_owned_bound_tags`, and the Levant/Arabia region list in `common/script_constants/006_independence_wave_constants_registry.txt` does not establish content readiness.

## Map and state setup

### Static installed-map contract

The current installed-map binding is internally coherent for a compact release:

- Anchor state `679` is Madinah and remains owned/core to `SAU` at game start.
- Compact state `856` is Asir-Makkah and remains owned/core to `SAU` at game start.
- Optional state `855` is Tabuk and remains an extension/claim/diplomacy/integration state, not an automatic release state.
- Former host `SAU` keeps capital state `292` protected.
- Reservation group `RG-ARABIA-HEJAZ-NAJD` covers `292|679|855|856|857` and permits at most one automatic package in this coarse group.
- State 679 contains vanilla province `12758` (Medina) and state 856 contains province `5037` (Mecca) and port province `12883`.
- The mod has no static override for these vanilla states, so a future package must perform an origin-gated runtime transfer and preserve the host remnant rule.

### Read-only HOI4 MCP map evidence

`hoi4_map_inspect` was run against states `679`, `856`, and `855` in the current workspace. The result was `MAP_INSPECTED`, workspace `mod_chaos_redux_ea3b2d67c2c0`, revision/shared revision `9ecfc1f41da23dc6ddfe554f06e7f835c747b22b25427fe91d6976853e9cc823`, with valid state/region membership, networks, adjacencies, supply, railways, and no unknown or missing province IDs for the selected states.

The positions/locators validation failed only on workspace-wide unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics in `mod:map/buildings.txt`, including an example at line 26352 for state 12/province 1885. The selected CUX states did not produce a CUX-specific map blocker. The inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7354866debab9fd519d826e4c3a6cf3ac118518caf2ba12b9fe7fd3f422817ab/b01eb0da974558a1193c894d6525612f02afbdd0cbe2b74fc32f09fed71a054b/map-inspect.9ecfc1f41da23dc6.json`.

`hoi4_map_render` produced a validated state-layer render with coastlines, ports, victory points, resources, buildings, supply nodes, railways, and adjacencies. Useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c8a38f2a0c09e2af8e7995c5a27803696c79c642b4d19a9fb7e001d8d2e9ae9/b4271e1375a714b38b0686094c8c506c8484efa91f8f1293aaafd75056b8a550/map-state.png` and its adjacent `map-state.json`/`map-state.html` artifacts from the same render.

No map write was attempted. Therefore no map dry-run, review, apply, post-validation, or rollback receipt exists or is needed for this no-change audit.

## Politics, leadership, portraits, flags, advisors, and parties

`history/countries/CUX - Hejaz.txt` starts the carrier at 100% neutrality with elections disabled and provides no capital or active leader. This is safe as a dormant loader record but not playable setup.

No CUX character definition, leader id, advisor, commander, high command, party name, party popularity, law, stability, war support, or diplomacy behavior exists. No CUX leader or institution portrait consumer exists. The accepted research row requires a period-correct civic or dynastic institution and a sourced real male officeholder or authentic institutional material; neither is currently accepted.

Vanilla SAU supplies `SAU_abdulaziz_ibn_saud` plus several Saudi advisors and generic Arabian portrait fallbacks, but those are Saudi-owned identities and cannot be copied into CUX. The Event 006 Lawrence-related assets are unrelated and cannot stand in for a Hejaz officeholder or institution. Under the portrait skill and accepted Event 006 direction, no generated grounded claimant or opposite-gender pairing is permissible.

The CUX flag ladder is present, but the separate symbol gate dated 2026-08-28 records only a source/design handoff. Its red-hoist triangle with black/green/white bands must not be presented as an authenticated 1936 Hejaz standard without the missing identity/rights decision. No flag patch is safe in this tranche.

## Focus, decisions, ideas, and assets

The shared dependency was inspected and rendered through the read-only HOI4 MCP focus routes. `hoi4_focus_inspect` on `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree` returned `FOCUS_INSPECTED`, validation true, 184 focuses, 196 connectors, no crossing or intersection diagnostics, and one long-connector warning. The warning is `independence_wave_adopt_military_archetype_program -> independence_wave_adopt_reclamation_doctrine` across 10 columns at source lines 742-760 and is not CUX-owned. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca7e814ee85cbe6743dcbb8c74fcecadc5885b55587c315267300f13999c9f3c/8ffcccb46427863b23b931c6074986fd7f3bc9b7e4cdb3bbc3d2d78560b85317/focus-inspect.8665217aa8ee7699.json`.

`hoi4_focus_render` returned `FOCUS_RENDERED`, validation true, layout hash `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, and dimensions `21424x2440`. Its HTML/SVG/JSON/source-map/plan artifacts are under the corresponding `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/` render records. No CUX-specific callback, route gate, icon, or localisation was found in the shared tree.

The current focus dependency is therefore usable as an engine surface but not evidence of a CUX package. The unrelated vanilla localisation diagnostic `continuous_restrict_freedom_desc` and the long connector are not patched here.

The shared decision file `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` contains CUX in broad target lists at lines 774, 1454, and 1821, but the decision visibility and root triggers are IW-043/IW-058-specific. Those entries do not grant CUX a decision family and must not be treated as Hejaz content.

No CUX ideas, starting national spirit, idea icon, decision icon, focus icon, event icon, or package-specific asset manifest was found. Adding generic assets or Saudi material would be an unauthorized fallback.

## Starting military, technology, industry, supply, and production

No CUX OOB, division template, starting army, navy, air force, equipment stockpile, manpower setup, research slot, technology setup, production line, convoy count, train stockpile, fuel, supply, rail, port, or building setup exists. `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:74` is a design mapping only and explicitly leaves navy/air and 3D content out of the initial Hejaz package while opening reconnaissance, engineers, desert logistics, artillery, and coastal signals through route security.

State 856 has a vanilla naval base at province `12883`, while states 679 and 855 have no package-specific buildings in the mod. The future runtime transfer must account for the port and pilgrimage-route logistics without claiming the optional Tabuk extension automatically.

No CUX technology dependency is referenced by current package code. The installed package exposes no Technology Tree Viewer, so technology-tree visual proof is an unresolved limitation by contract. No technology patch was attempted.

## AI and playability

No CUX AI strategy, AI focus behavior, research selection, template selection, decision score, diplomacy, front behavior, reinforcement behavior, or host/patron strategy exists. The generic planner weight wrapper is not a country AI package.

The mandatory `chaosx_ai_probability_auditor` route is unavailable in the installed tool inventory, and no collaboration/spawn interface was exposed for routing the required auditor. Direct HOI4 probability source discovery was run only to document that limitation:

- `hoi4_probability_inspect` against `independence_wave_prepare_weight_iw_073` returned `PROBABILITY_SOURCE_DISCOVERED`, source revision `8b5711e2e0ecd7a161c2877f8942ddf35890490c942fb1400f9658922fec00f6`, source hash `17e35c209602f859bd3e5b71bd6b394aa613d7d8686e0d07f1d8ee3b803585e6`, zero resolved candidates, 126 available candidates, and `identifier_not_found` with a suggestion to use `random_list`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6aeefbf05879f965091a67d2af044b05390d23fabaf4f3a2a66b6842cc451d4d/35fcc8f0e0c6f879b7a657d7b509829e8c006a9a9d4ba10bb311c7c622ff2b73/probability-inspect-17e35c209602.json`.
- A second `random_list` discovery against `independence_wave_select_region_07_automatic_package` returned the same source revision/hash, zero resolved candidates, 126 available candidates, and `identifier_not_found`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e97957a5675bc985cf53c8d922863ad719767adff7e3e0687e031e01e06842fd/b5d9fc09c5dc18993d9e4f200576700d6892f297305a67c91906b268926d88e6/probability-inspect-17e35c209602.json`.

These are source-discovery receipts only. They are not an auditor baseline, scenario sweep, evaluation, simulation, or probability compare, and no balance claim is made. A probability compare is not appropriate without a package patch, named scenarios, and the required auditor owner route.

## Event and dispatch evidence

The narrow current `hoi4_event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL`, status ok, revision `18bf807c8be35655138be368b38a6ff43f90d4c9ac0a1470ca1d9d44f43afd8f`, with no blocking diagnostics. The workspace-wide projection reported 9,725 events, 15,153 options, 8689 unresolved references, and 2205 deferred diagnostics; helper/lifecycle projections were deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a67d3c0e344c6fcbe9c9057f3bceaf0257ce396d4ac528cd4dc7645aaf347804/aa90e413eec0ab5f986091c65f467a2bdf807de00680e6c666dabac62c4f6e50/event-lint-18bf807c8be3.json`.

The matching `hoi4_event_render` overview returned `EVENT_RENDERED_PARTIAL`, no blockers, three selected nodes, and helper/lifecycle omission. Useful manifest/JSON/SVG/PNG artifacts are under the event overview records for revision `18bf807c8be3`, including `event-overview-18bf807c8be3.png`. A prior broad event scan timed out after 180 seconds; that exact timeout is recorded as an engine-tool limitation, not treated as evidence of missing CUX content.

No CUX/IW-073 event node, option, event target, execution branch, or cleanup callback exists in the current bounded search. The absence of a country adapter and attestation remains the decisive fail-closed result.

## Why no patch is safe

1. A tag, colour, localisation, or shared-shell edit would not solve the missing Level 2 package and would overlap the active shell-consolidation worktree.
2. Adding CUX to central adapter, attestation, preflight, capacity, scenario, or Join lists would expose an incomplete country and bypass the accepted fail-closed boundary.
3. Adding a generic Saudi/Arabian leader, advisor, portrait, party, idea, force setup, or flag interpretation would violate the identity and rights requirements.
4. Adding a whole focus route, decision family, starting force, or runtime lifecycle would be broad package construction explicitly outside a narrow re-audit tranche.
5. Any AI factor or allocator change requires a baseline and compare pass owned by `chaosx_ai_probability_auditor`, which is unavailable here.
6. A map rewrite is neither necessary nor authorized; the current inspected states are coherent and map ownership remains parent scope.

Accordingly, this audit makes no gameplay or central-gate patch and does not write a plan for a fallback package. The correct state is to keep IW-073 in the package-local queue.

## Reopen conditions and future tranche boundary

The next owner must first resolve an identity/rights receipt for a period-correct Hejaz civic, municipal, customs, pilgrimage, railway, merchant, local-defense, or dynastic institution and an accepted sourced real male officeholder or authentic institutional portrait source. The supplied CUX flag source handoff must be reconciled with that identity decision before it can support admission.

After that gate, a package-local tranche may implement the accepted shared Statehood adapter and exact named content, origin-gated by `liberation_origin.independence_wave`, package `iw_073`, anchor 679, compact state 856, and `RG-ARABIA-HEJAZ-NAJD`:

- Founding mission `independence_wave_iw073_secure_pilgrimage_calendar`.
- Projects `iw073_reopen_red_sea_customs`, `iw073_guard_rail_and_pilgrimage_routes`, `iw073_convene_municipal_delegates`, and `iw073_organize_holy_city_guard`.
- Mutually exclusive settlements `iw073_ratify_civic_shura`, `iw073_accept_dynastic_council`, and `iw073_authorize_emergency_command`.
- Network mission `iw073_open_arabian_congress_mission`.
- Desert mobility, local levies, foreign-trained regulars, pilgrimage-route security, port/customs, and host-remnant behavior using the shared bilateral helper.

The parent-owned implementation and audit must then add the CUX package lifecycle, parties/leader/institution, ideas and assets, starting forces and recovery paths, decisions, shared-tree callbacks, AI/diplomacy, cleanup, central adapter/attestation/preflight/capacity/SCN-008/Join branches, and `FORM-20` only after the complete package passes. A fresh probability baseline and compare must be routed through `chaosx_ai_probability_auditor` before any weighted behavior is claimed.

## Remaining risks, omissions, and blockers

- IW-073 remains unavailable to Event 006 runtime by design; the event-wide `32/29/40/161` boundary is unchanged.
- CUX has no accepted identity/rights-cleared roster, portrait consumer, or leader/institution source.
- CUX has no runtime gameplay package, starting forces, ideas, decisions, focus callbacks, AI, or cleanup.
- The supplied flag is an asset/source handoff, not an authenticated 1936 package identity.
- Current map evidence is read-only and does not authorize a transfer; unrelated workspace building/port locator diagnostics remain outside this package.
- Focus evidence is for the shared dependency only and includes one unrelated long connector warning.
- Event MCP evidence is partial because helpers/lifecycle are deferred, and the broad scan timed out.
- The installed package exposes no Technology Tree Viewer.
- The required `chaosx_ai_probability_auditor` route is unavailable; direct probability discovery is not equivalent evidence.
- No fallback, generic substitute, central-gate bypass, map write, gameplay patch, or staged/committed change was made.

## Parent handoff

Keep IW-073 in the package-local queue and preserve the current fail-closed admission boundary. Use this re-audit with the prior source and symbol gates:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw073_hejaz_package_source_gate_2026-08-28.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_iw073_hejaz_symbol_source_gate_2026-08-28.md`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_country_shell_merge_audit_2026-09-02.md`.

No implementation patch is being handed off. The only file added by this re-audit is this dated evidence handoff, and it is intentionally unstaged and uncommitted.

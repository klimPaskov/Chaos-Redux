# IW-020 Venice (ATX) country-package audit

Date: 2026-08-03

Scope: current Event 006 country-package, dispatch, map-binding, focus, AI, force, localisation, leader, portrait, flag, and attestation surfaces for `IW-020` Venice (`ATX`).

## Verdict

**HOLD / FAIL-CLOSED.** ATX is a valid dormant registry candidate with a valid current-map anchor binding, but it cannot safely execute as a full Event 006 country package in the current source state.

The immediate runtime blocker is not a missing planner row. The package publisher and anchor reservation are present, but no ATX package adapter supplies setup, final validation, cleanup, political identity, starting state, force application, focus assignment, or AI wiring.

The admission gate is correctly closed. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` does not admit `iw_020` in either the adapter whitelist or the content-attestation whitelist, and the common planner requires content attestation before allocation weight, reservation, and preflight can succeed. No attestation change is authorized by this audit.

The specific unresolved research gates are Venice leadership/portrait provenance and symbol ownership/provenance. The accepted research row requires a sourced real male officeholder or authentic archival material for the actual institution and a source-specific symbol review. A generated one-person leader, invented doge or admiral, or unreviewed historic flag would be a country-package blocker.

## Accepted identity and map evidence

| Surface | Current evidence | Disposition |
| --- | --- | --- |
| Package identity | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row `IW-020`: Venice, `ATX`, high-chaos-only, Mediterranean and Iberia, anchor 160, reservation group `RG-160` | Accepted registry direction; not gameplay admission |
| Research resolution | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` row `IW-020` requires a provisional assembly/cabinet/municipal council/congress, sourced real male officeholders or authentic institutional material, and attested symbols with ownership documentation | Research incomplete; block package until evidence is recorded |
| Tag registration | `common/country_tags/006_independence_wave_countries.txt:22` maps `ATX` to `countries/006_independence_wave_ATX.txt`; the 2026-08-01 collision audit records `ATX` as Venice | Tag slot is present; rerun the full installed-environment collision audit before final admission |
| Current-map binding | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:21` binds `IW-020` to state `160` (Veneto), compact anchor, `160=ITA`, `ITA=2`, with the host-remnant test passing in the accepted binding snapshot | Map binding is usable as a future release anchor; no map rewrite is needed now |
| Vanilla state | `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/160-Veneto.txt` is an ITA-owned large-city state with Venezia victory point, naval base, dockyard, and industrial infrastructure | Static anchor is coherent; runtime ownership/capital transfer remains unimplemented |

## Country package coverage checklist

| Surface | Status | Concrete evidence and gap |
| --- | --- | --- |
| Country definition | Shell only | `common/countries/006_independence_wave_ATX.txt` defines graphical cultures and color, but no leaders, ministers, ideas, or setup. This is intentional only if a runtime adapter exists; ATX has none. |
| Country history | Loader only | `history/countries/ATX - Venice.txt` contains only neutral politics and 100% neutrality. It cannot provide a playable package by itself and should not be expanded as a shortcut for missing event-created setup. |
| Registry and constants | Present | `ATX` is in the Event 006 country registry and package constant `iw_020 = 20`; registry membership does not imply admission. |
| Region publisher | Present but inert for execution | `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt:86-95` publishes `independence_wave_load_package_iw_020` for `ATX` and state `160`; `:152-155`, `:174`, and `:198-220` expose high-chaos weight and reservation calls. |
| Candidate trigger | Present but not sufficient | `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt:72-79` checks plan slot, `ATX` availability, and anchor `160`; it does not prove package content. |
| Weight/reservation safety | Correctly fail-closed | `independence_wave_calculate_candidate_allocation_weight` in `common/scripted_effects/006_independence_wave_package_planner_effects.txt` only assigns weight after `has_independence_wave_runtime_package_content_attestation_for_execution_id = yes`; the reservation transaction rejects un-attested packages. |
| Runtime adapter | Missing | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` calls the Mediterranean dispatcher, but `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:882-886` only dispatches `IW-017`, `IW-018`, and `IW-019`. There is no `IW-020` setup branch. |
| Final validation | Missing | `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:888-900` validates only `IW-017` through `IW-019`; no ATX ownership, control, host-survival, force, focus, or route proof exists. |
| Cleanup | Missing | `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:1078-1082` cleans only Corsica, Sardinia, and Sicily. No ATX flags, ideas, claims, decisions, characters, or variables have a package cleanup path. |
| Adapter attestation | Intentionally absent | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-58` has no `iw_020` branch in `has_independence_wave_runtime_package_adapter_for_execution_id`. |
| Content attestation | Intentionally absent | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:73-90` attests exactly the current 14 packages and omits `iw_020`; `is_independence_wave_runtime_package_preflight_ready` at `:95-98` requires both adapter and content attestation. |
| Politics and parties | Missing | No ATX party names, route parties, elections, ruling-party transition, stability, war-support, or diplomacy setup exists beyond the neutral loader. Accepted registry routes are republican oligarchic, constitutional, labor, and military, but none are implemented. |
| Leaders and characters | Missing and research-blocked | No ATX entry exists in `common/characters/`, no ATX leader/commander portrait exists under `gfx/leaders/006_independence_wave/`, and no leader localisation or role metadata exists. The accepted leadership direction requires sourced male officeholders or authentic institutional archival material. |
| Portrait provenance | Blocked | Venice is a grounded polity. Generated fictional one-person portraits are not an acceptable substitute for a sourced officeholder or authentic institutional material. No source package, crop evidence, runtime DDS, character consumer, or portrait handoff exists for ATX. |
| Flag ladder | Physical files present, provenance gate open | `gfx/flags/ATX.tga`, ideology variants, and medium/small ladders exist, and `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/manifest.md:8` marks the tranche `handed_off`. The current authority still blocks `IW-020` in Group C of `docs/plans/006_independence_wave_plans/asset_research/006_generated_flag_blockers.md:17-21` pending exact symbol owner, date, function, route, license, and attribution review. The Wikipedia-only design row is not sufficient admission evidence. |
| Ideas and lifecycle | Missing | No ATX crisis idea, mature state compact, route ideas, icon definitions, swap/remove logic, or cleanup exists. |
| Decisions and missions | Missing | No ATX founding mission, timed project family, route settlements, costs, cancellation, or rollback exists. |
| Focus ownership | Unassigned | The shared tree `independence_wave_focus_tree` is defined in `common/national_focus/006_independence_wave_focus.txt:34-60`, and `common/scripted_effects/006_independence_wave_focus_effects.txt:33-61` can assign the full framework. No ATX adapter calls `independence_wave_assign_focus_framework` with `full_framework`, so ATX cannot prove the generic focus contract. |
| Focus route content | Missing | No Venice-specific focus module or route gates exist. The Mediterranean focus/decision sources currently cover only the Corsica, Sardinia, and Sicily package ids. A generic tree's existence is not package completion. |
| AI | Unassigned | `common/ai_strategy/006_independence_wave_generic.txt:36-42` and the recovery/consolidation profiles require `independence_wave_generic_ai_profile` plus active Event 006 flags. No ATX setup sets those flags. `common/ai_strategy/006_independence_wave_mediterranean.txt` has package-specific profiles for `COR`, `ARX`, and `ASX`, but no ATX branch. |
| Starting forces | Design mapping only | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:21` freezes `coastal_maritime`, military tradition `64`, navy inheritance `yes`, air inheritance `yes`, and five reinforcement pathways for `IW-020`. `common/script_constants/006_independence_wave_force_package_constants.txt` contains `p20` values, but no ATX adapter loads or applies that mapping. |
| Technology, equipment, and production | Missing runtime setup | No ATX starting technologies, research slots, laws, equipment stockpiles, production lines, trains, convoys, fuel, supply capacity, or dynamic force call is attached to ATX. The generic force transaction cannot run until an adapter passes its setup and mapping probes. |
| Industry, supply, and map coherence | Static anchor only | State `160` supplies a viable port, naval base, dockyard, factories, and victory points, but no runtime capital/ownership/controller/claim/core/host ledger transaction exists for ATX. The accepted compact anchor must remain the only release territory until later researched claims or integration are implemented. |
| Localisation | Base names only | `localisation/english/006_independence_wave_countries_l_english.yml:122-137` covers `ATX`, `ATX_DEF`, `ATX_ADJ`, and ideology name/adjective variants. No ATX party, leader, idea, focus, decision, mission, AI, route, or debug keys exist. |
| Assets and documentation | Partial registry evidence only | The flag tranche and generic Event 006 docs exist, but no complete ATX asset manifest, leader/portrait handoff, focus/idea/decision icon coverage, Venice package design document, or post-wire audit exists. |

## Politics, leader, portrait, flag, advisor, and party issues

The accepted Venice identity is a modern institutional bridge to historical Venetian civic memory, not an automatic medieval restoration. The package research row directs a provisional assembly, cabinet, municipal council, or congress and explicitly blocks the package when a sourced officeholder or authentic institutional archival source cannot be established.

No ATX character exists in `common/characters/006_independence_wave_mediterranean_characters.txt` or any other character file. No ATX leader trait, portrait sprite, DDS, source master, crop record, or runtime character consumer exists. Do not create a generic “Doge” or “Admiral” merely to satisfy the leader slot, and do not use a generated one-person portrait for this grounded polity.

The ATX flag ladder is a production artifact, not a cleared identity. `docs/plans/006_independence_wave_plans/asset_research/006_generated_flag_blockers.md:19-21` still lists Venice in Group C and requires a source-specific review of the winged Lion of Saint Mark design. The review must identify whether the symbol is a state standard, civic flag, religious symbol, municipal arm, route emblem, or another institution-owned mark before a baseline flag or route flag is assigned.

No advisors, high command, commanders, party names, election rules, popularity transitions, or route-specific government identities are wired. The accepted route set must remain a design input until source and gameplay surfaces are complete.

## Focus, decision, idea, and asset issues

The shared generic focus tree is a valid source surface, but the package contract requires an adapter to assign it and set both `independence_wave_generic_focus_tree_assigned`/`independence_wave_full_focus_framework` and `independence_wave_generic_ai_profile`. No ATX path sets those flags, and the common final validation would reject any future adapter that reports success without the focus contract.

The existing Mediterranean package adapter is intentionally scoped to Corsica, Sardinia, and Sicily. Adding a bare `IW-020` branch without ideas, missions, route gates, starting setup, cleanup, and a reviewed Venice identity would create the generic shallow package prohibited by the Event 006 contract.

The force table is more complete than the country package: `p20` constants and the mapping row are already present, including navy and air inheritance and five reinforcement paths. They remain inert until an ATX setup calls the force probe/loader and then the shared dynamic starting-force transaction.

## AI and playability issues

ATX has no package-specific AI profile, no generic-profile activation flag, no route weights, no naval/coastal production policy, no host-threat restraint, and no decision or focus AI behavior. The generic AI source is identity-neutral and cannot make ATX playable without a real package setup and public-value initialization.

Because the country history is a neutral loader and no runtime adapter runs, ATX currently has no capital assignment, forces, technologies, production, supply, state-control proof, former-host relation, recognition, stability, war-support, or cleanup behavior. A dormant ATX tag is safe; a released ATX country is not.

## Smallest safe implementation tranche

1. Close the research gate first by adding an accepted Venice source dossier that identifies the exact symbol owner, date, historical function, route ownership, license, and attribution for the baseline and any route variants.
2. Close the leadership gate with a sourced real male Venetian officeholder or authentic archival material for the actual provisional institution, including role/date/source/provenance and a portrait handoff if a person is used. Keep institutional names for council/assembly bodies and do not invent a personal commander.
3. Prepare a complete ATX adapter contract covering setup, compact anchor ownership/capital, host remnant protection, politics/parties, crisis and mature ideas, route decisions/missions, `full_framework` focus assignment, generic/package AI, force mapping/load, final validation, and cleanup. This is broad country-package implementation work and is not a safe local patch for this audit.
4. Add the Mediterranean dispatcher branches and ATX-specific source surfaces only after steps 1-3 are reviewed. Add `iw_020` to the central adapter/content-attestation lists only after the full static and post-wire country-package audit passes.
5. Recheck the installed tag collision snapshot, state 160 binding, host survival, force probe (`p20`), generic focus contract, AI profile, localisation, assets, and cleanup before any attestation change.

## Validation and limits

The audit read the required repository guidance, Event 006, focus-tree, and asset skills, the required offline Paradox wiki pages, and the relevant vanilla documentation before inspecting source surfaces.

Static source inspection covered the ATX shell/history, tag registry, package constants, region publisher/trigger, planner attestation gate, package dispatchers, generic focus/AI surfaces, force constants/mapping, localisation, flags, asset ledgers, research resolution, and current installed-map binding.

Read-only `hoi4_map_inspect` for state `160` returned `MAP_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdc5c3cedc79554b66d12af08a8af4bdca1ee30c25705038ff82b4224d1d016e/2a482d166fde327f8474b38bf1ddcaf0a79e8d505060b41c0aec8cbc3536f8a/map-inspect.ca6031af3ba6b437.json`. The artifact confirms the installed map root and state inventory, but the global inspection also reports unrelated map-position and floating-harbor diagnostics, so it is not a clean whole-map pass and does not justify a map rewrite for ATX.

No ATX focus, event, decision, or technology MCP render was claimed because the ATX runtime package and package-specific focus/technology surfaces do not exist yet. The installed MCP package exposes no Technology Tree Viewer; technology acceptance remains an unresolved limitation for a future complete package audit.

No Hearts of Iron IV process was launched and no live/save-load validation was attempted.

## Changed files and simplifications

This audit changed only this handoff file. No gameplay file, country shell, history file, dispatcher, trigger, attestation list, flag, portrait, localisation, map, or asset was modified.

No simplification, fallback, generic leader, unresearched symbol, admission bypass, or attestation reclassification was made.

## Parent handoff

Keep `IW-020` in the registry and map-binding ledgers, but leave it unadmitted and high-chaos-only. The current fail-closed allocator behavior is safe and should remain unchanged until the Venice source/leadership gates and the complete runtime package are independently implemented and audited.

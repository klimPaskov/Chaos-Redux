# Event 006 IW-029 Bosnia country-package audit — 2026-08-06

## Status

IW-029 (Bosnia, carrier `BOS`) is HOLD / fail-closed. The region-03 planner knows the package, anchor, and reservation group, but the package is not an admitted runtime country package. No gameplay file was changed in this audit. This handoff is the only file added.

The current central admission surface contains no `iw_029` package adapter, no `iw_029` content attestation, and no BOS package setup or cleanup call. The shared candidate gate also requires `independence_wave_package_content_ready`, but no repository effect currently sets that flag. Adding the flag alone would violate the package readiness contract and was not attempted.

## Identity and registry coverage

| Surface | Evidence | Result |
|---|---|---|
| Tag registration | Vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:189` maps `BOS` to `countries/Bosnia.txt`; vanilla country definition has eastern-European graphical culture and color only. | Reusable vanilla tag exists. No mod country-definition override exists. |
| Registry constants | `common/script_constants/006_independence_wave_package_constants.txt:80` defines `iw_029 = 29`; `:485` defines `rg_104 = 3`; `common/script_constants/006_independence_wave_country_registry_constants.txt:22,30,47,63,129` includes `BOS` in resolved/registered/bound and Balkans-Danube groups. | Registry/API membership is present, but this is not content readiness. |
| Research contract | `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:30` requires sourced local institutions and a defensible sourced real male leader or authentic institution, and explicitly blocks the package until that evidence exists. | Leader/institution source gate remains open. |
| Candidate row | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:30` identifies Bosnia as a Level 2 multiethnic mountain state with mountain infantry and regular defectors, Sarajevo/Bosnian core, and Balkan/Danubian ambitions. | Design direction exists; implementation does not. |

## Region, map, and host setup

The region-03 loader and reservation publisher are present in `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt:73-83,113-146`, and the candidate gate is present in `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt:56-63`. `BOS` points to state 104 and optional extension state 804, reservation group `RG-104`.

The current binding ledger `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:30` records `104=YUG|804=YUG`, BOS cores on 104 and 804, and a YUG host-remnant count of 107 states. `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:4` repeats the 104/804 compact-anchor rule and protected-host requirement.

Vanilla state history confirms the binding: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/104-Bosnia.txt:2-36` has owner YUG, BOS and YUG cores, Sarajevo victory points, infrastructure 3, two industrial complexes, an air base, aluminium, coal, and local supplies; `804-Herzegovina.txt:2-31` has owner YUG, BOS/YUG/HRZ cores, one victory point, infrastructure 2, aluminium, and no local supplies. No mod state history overrides these states.

Read-only MCP map evidence inspected states 104 and 804 successfully. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10ea072ded18f43bba714f874a87a7f8a424261cc99c148954302cf21d647dea/178f35e3e74e863b068e06ffddabfbd8d8f0e5017be2082607d4f9630e43261c/map-inspect.9589ad18ae326c0c.json`. State/region membership, bitmap geometry, networks, adjacencies, supply nodes, and railways passed. The global map inspector remains red because unrelated `map/buildings.txt` contains 1,323 invalid building positions and 1,331 invalid floating-harbor sea-adjacency records; no Bosnia-specific geometry defect was reported. State-layer render passed: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c8a38f2a0c09e2af8e7995c5a27803696c79c642b4d19a9fb7e001d8d2e9ae9/76be5a8587047afc61d3737309aa042f08bfbd656a5eaa8cbd3ecea643b836ff/map-state.png`.

No `hoi4.map_rewrite` was run. The current task has no approved map mutation, and the existing compact anchor plus host-protection contract is safe to preserve until a complete adapter exists.

## Politics, leaders, portraits, flags, and parties

Vanilla `history/countries/BOS - Bosnia.txt:1-83` supplies capital 104, three research slots, generic Yugoslav-clone starting technologies, democratic ruling party, 1936 election, and popularity democratic 33 / neutrality 33 / communism 34. It contains no BOS units, production lines, leader roster, characters, advisors, commander roster, Event 006 ideas, or Event 006 diplomacy.

The installed vanilla country/leader/character sources contain no BOS-specific character or country-leader definition. There is no defensible sourced real male leader or exact archival institution portrait in the current package surface. The research row therefore remains a blocking identity issue; no invented name, opposite-gender name pool, generic portrait, or generated institutional portrait was installed.

Vanilla provides complete reusable flag families `BOS_communism`, `BOS_democratic`, `BOS_fascism`, and `BOS_neutrality` in normal, medium, and small sizes under the installed game `gfx/flags` folders. The mod has no BOS flag override. `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:74-76` allows Group A base-flag reuse only after identity and route review, and the package-specific research row still requires provenance for any route variant. No portrait, advisor icon, or commander asset is wired for BOS.

Vanilla English localisation covers `BOS`, party names, adjectives, and cosmetic variants in `localisation/english/countries_l_english.yml:3011-3027` and related cosmetic localisation. There is no IW-029 route, provisional-government, leader, advisor, decision, mission, or focus localisation in the mod.

## Focus, decisions, ideas, technology, forces, and economy

The shared tree `independence_wave_focus_tree` is structurally present, but it does not grant BOS a focus contract. `common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-66` requires the full-tree flags plus `has_focus_tree = independence_wave_focus_tree`, or a reviewed additive carrier; `common/scripted_effects/006_independence_wave_focus_effects.txt:33-62` assigns those flags only through an admitted package adapter. BOS has no such assignment. The central final-validation barrier in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:38-64` would reject a package lacking this focus contract and the generic AI profile.

Read-only focus MCP inspection succeeded for `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, with 184 nodes and 193 connectors. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ada913c4a0200681251b701941d86f7130f78c7a601fee08e6d7304c28c16793/52c930b9c682a9e96c86fb9e7cb5900bd7f038e8b6b12d6727c378c469f24f50/focus-inspect.08877a307b338d93.json`. The inspector reports 14 blocking missing vanilla generic-focus icon diagnostics and five Event 006 layout warnings; these are shared-tree diagnostics, not evidence of a BOS assignment. Render artifacts are available at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d0a9699de3bed2979acd7edfaec33d0329bb3b929bf39b4713db192ea82735c/f6f927b1a96645bafd04e8a1c5a79de09920c97466bbd66aef714ccbb8fb33ac/independence_wave_focus_tree.focus.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3/a7cdc0c10c7a60567c2b5b990ae9269e6a6e7b02f67beeffcd60d6a17a98cdf0/independence_wave_focus_tree.focus.svg`.

No BOS/IW-029-owned decision, mission, idea, starting spirit, AI strategy, force setup, unit template, production setup, or Event 006 technology adapter exists under `common/decisions`, `common/ideas`, `common/ai_strategy`, `common/units`, `history/units`, or `common/technologies`. BOS mentions in broad shared target lists, vanilla formables, or `austro_hungarian_releasable_shared.txt` are not a Bosnia package. The force plan `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:30` still requires mountain infantry and regular defectors, depot and militia integration, unified mountain logistics/hospitals, and a multi-community officer-vetting board; none is wired.

Vanilla history gives BOS three research slots and generic starting technologies only. The installed package exposes no Technology Tree Viewer, so no technology-tree engine artifact can be supplied; this remains an unresolved limitation rather than a completion claim.

## Dispatch, admission, AI, diplomacy, and cleanup blockers

`common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:14-31,38-55,68-89` calls only the existing package setup, final-validation, and cleanup adapters; there is no Bosnia/IW-029 call. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-83` has no `iw_029` runtime adapter branch, and `:88-122` has no `iw_029` content-attestation branch. The preflight at `:125-130` requires both branches, so IW-029 cannot pass preflight or commit a release.

The shared planner also checks `has_independence_wave_runtime_package_content_attestation_for_execution_id = yes` before reservation (`common/scripted_effects/006_independence_wave_package_planner_effects.txt:106` and `:519`). The candidate trigger requires `has_country_flag = independence_wave_package_content_ready` (`common/scripted_triggers/006_independence_wave_package_triggers.txt:46-49`), but the repository has no setter for that flag; the only occurrences are this gate and a fail-closed comment. Therefore the apparent region-03 candidate cannot become a live country.

The generic AI file requires the generic focus flags and `independence_wave_generic_ai_profile` before any strategy profile can enable. No BOS adapter sets these flags or supplies Bosnia-specific route weights, diplomacy, host relation, patron, formable, or cleanup behavior. A read-only probability inspection of `common/ai_strategy/006_independence_wave_generic.txt` returned exact blocker `PROBABILITY_SURFACE_EMPTY: No weighted blocks matched this request`; no AI ranking or survival claim is made. The region-03 custom-pool inspection returned `PROBABILITY_SOURCE_INSPECTED` with zero discovered candidates and eight unresolved inputs, `poolComplete = false`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/227d6a69147c51cb9e88ced984fded9a5b2d115381ce64a16a24ce6664f6b913/8da4ae9d4096b7be8df8559aafea888965f06c5821be50692eb39a8b32176330/probability-inspect-ff114c943bad.json`. No normalized package-selection probability is claimed.

## Event MCP evidence

The read-only Event Chain Viewer inspected root `chaosx.nr6.1` and returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/341091c4a9cb4dd4398c4eb5cb87845dbe6472213f7c56ee62a04d03e45e522c/3512af83729e5f2653a604b578eacdabc451c7466cfca4f3c98134c5cd4eb5c5/event-scan-04e76dcf50ae.json`. Deterministic overview render returned `EVENT_RENDERED_PARTIAL`; overview JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0a4529e1f560eb1199c280a1a0976b62bd60bb081bf7cf65daa77afc8d0d7fda/13b4d7564b877a759c0b3610663caa151d81f9dc2b62d382e9b7aca97c3767a9/event-overview-04e76dcf50ae.json`. The result explicitly deferred workspace-wide helper projections; this is a viewer boundary, not evidence that IW-029 is complete.

## Coverage checklist

| Required package surface | Current state |
|---|---|
| Tag, country definition, registry, anchor, reservation group | Present as reusable/registry metadata. |
| State ownership, cores, capital, host remnant, map geometry | Vanilla 104/804 binding is coherent; no Bosnia map defect; runtime reservation remains unadmitted. |
| Provisional government, party setup, elections, laws, diplomacy | Only vanilla dormant BOS politics; no Event 006 package layer. |
| Leader, characters, commanders, advisors, portraits | Missing defensible sourced leader/institution and all BOS package wiring; blocking. |
| Flags and localisation | Vanilla base flags and country localisation exist; no Event 006 route variants or package strings. |
| Focus tree and AI | Shared tree exists, but BOS has no assignment/carrier and no BOS AI profile. |
| Decisions, missions, ideas, spirits | No BOS/IW-029-owned surfaces. |
| Forces, templates, equipment, production, supply | No Event 006 setup; force-mapping requirements remain unimplemented. |
| Technology and research | Vanilla three-slot/technology baseline only; no package technology surface and no Technology Tree Viewer. |
| Host relations, cleanup, release/annexation/puppet behavior | No Bosnia adapter, final validation, or cleanup path. |
| Asset provenance and manifests | Reusable flags only; no leader/portrait/commander package. |

## Required next work and disposition

Do not add a readiness flag, invent a leader, reuse an unreviewed portrait, remap BOS, seize a different anchor, or create a shallow fallback package. A future implementation tranche must provide a sourced male period leader or exact archival institution, portrait and role wiring, Bosnia-specific setup/forces/ideas/decisions/AI/diplomacy/host/cleanup, full or explicitly reviewed safe focus assignment, package localisation/assets, and the central `iw_029` adapter, preflight, content-attestation, final-validation, and cleanup branches. Only after independent package and asset audits should the parent add attestation and rerun the same map, focus, event, and probability evidence.

## Validation and limits

`python -B .tools/audit_chaosx_country_tags.py --surface-scan` passed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions. No gameplay source was patched, no map write was attempted, and Hearts of Iron IV was not launched. Live execution, save/load, and player-owned in-game validation remain outside this audit.

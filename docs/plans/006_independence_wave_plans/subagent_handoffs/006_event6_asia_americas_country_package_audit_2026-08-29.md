# Event 006 Asia and Americas country package audit

Date: 2026-08-29.

Scope: IW-136 Sindh (SIN), IW-140 Hyderabad (HYD), IW-141 Mysore (MYS), IW-170 Inner Mongolia (MEN), IW-175 Samoa (SAM), IW-180 Quebec (QUE), IW-192 Yucatan (YUC), and exact package-local adapters for these rows.

Disposition: BLOCKED and fail-closed; no target row is admitted, promoted, or made selectable by this audit.

This handoff records a source-backed audit only. No gameplay file, central registry, dispatch file, localization file, flag, portrait, focus icon, idea icon, or map file was changed.

## Authority and evidence reviewed

The accepted Event 006 package contract was reviewed in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`, and `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`.

The Event 021 country-package handling rules were reviewed in `docs/specs/021_random_civil_war_specs/021_random_civil_war_spec_part_7_event_006_country_packages_and_focus_handling.md`, `docs/specs/021_random_civil_war_specs/021_random_civil_war_spec_part_8_country_package_acceptance_and_runtime_invariants.md`, and `docs/specs/021_random_civil_war_specs/021_random_civil_war_spec_part_9_country_package_source_and_asset_provenance.md`.

The current package authority and installed-map bindings were reviewed in `docs/specs/006_independence_wave_specs/quality/package_manifest.md`, `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.

Required offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localization, scopes, on actions, events, decisions, ideas, AI, country creation, national focuses, states, maps, characters, portraits, cosmetic tags, technology, and divisions.

Vanilla documentation was consulted in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/`, including `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and the available character, decision, AI strategy, and script-constant documentation.

Vanilla country definitions, country histories, characters, flags, states, and formable decision references were inspected under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.

## Country package coverage checklist

| Row | Carrier and package | Contract profile | Installed anchor and host | Coverage disposition |
|---|---|---|---|---|
| IW-136 | SIN / `iw_136` | Level 2, provisional FFX, South Asia and Himalaya, regional depth, lower-Indus river and port role | State 443 Sind; current owner RAJ; RAJ capital 439; reservation `RG-443` | Generic wrapper only; no complete identity, roster, assets, package behavior, or attestation |
| IW-140 | HYD / `iw_140` | Level 2, provisional FJX, South Asia and Himalaya, princely-state role, Deccan federation direction | State 427 Hyderabad; current owner RAJ; RAJ capital 439; reservation `RG-SOUTH-INDIA` | Generic wrapper only; no complete identity, roster, assets, package behavior, or attestation |
| IW-141 | MYS / `iw_141` | Level 2, provisional FKX, South Asia and Himalaya, princely/regional role, Dravidian/southern federation direction | State 425 Mysore; current owner RAJ; RAJ capital 439; reservation `RG-SOUTH-INDIA` | Generic wrapper only; no complete identity, roster, assets, package behavior, or attestation |
| IW-170 | MEN / `iw_170` | Level 2, provisional GNX, East/Southeast Asia and Oceania, frontier autonomous role, Mongolic federation direction | States 621 Suiyuan and 746 Ordos; current owner SHX for both; SHX capital 615; reservation `RG-INNER-ASIA` | Generic wrapper only; vanilla MEN is a different Mengkukuo/Japanese-puppet package; no Event 006 identity or attestation |
| IW-175 | SAM / `iw_175` | Level 2, provisional GSX, East/Southeast Asia and Oceania, island role, Polynesian league direction | State 726 Samoa, optional extension 1072 American Samoa; owners NZL and USA; capitals 284 and 361; reservation `RG-PACIFIC-ISLANDS` | Generic wrapper only; split-state transaction, identity, assets, package behavior, and attestation are absent |
| IW-180 | QUE / `iw_180` | Level 2, provisional GXX, Americas and Caribbean, mature regional role, Canadian or Francophone compact direction | Current anchor 468 Saint Lawrence; compact 468, 860, 861, 862, 863; extended 466 Nord du Quebec; owner CAN; CAN capital 276; reservation `RG-466` | Generic wrapper only; current map rebind is recorded, but no complete identity, roster, assets, package behavior, or attestation |
| IW-192 | YUC / `iw_192` | Level 2, provisional HJX, Americas and Caribbean, peninsular republic role, Maya/Caribbean federation direction | State 474 Yucatan; current owner MEX; MEX capital 277; reservation `RG-MESOAMERICA-CARIBBEAN-COARSE` | Generic wrapper only; no complete identity, roster, assets, package behavior, or attestation |

Every row is marked Level 2 in the candidate registry, so the Level 2 requirements apply: a focus group, bespoke decisions, a starting problem, a unique sourced leader or institution, an ambition or formable direction, incidents, complete assets, and a complete Event 006 package contract.

None of the seven rows has evidence for all Level 2 requirements, so none can safely receive `independence_wave_package_content_ready` or central runtime attestation.

## File surface checklist

| Required surface | Result for the seven rows | Evidence |
|---|---|---|
| Country tag registration | Vanilla carriers exist; the Event 006 mod tag file reserves X-ending tags only and does not register these carrier tags | `common/country_tags/00_countries.txt`; `common/country_tags/006_independence_wave_countries.txt` |
| Country definitions | Vanilla definitions exist with colors and graphical cultures; no Event 006 country shells exist | Vanilla `common/countries/Sindh.txt`, `Hyderabad.txt`, `Mysore.txt`, `Mengkukuo.txt`, `Samoa.txt`, `Quebec.txt`, `Yucatan.txt`; mod `common/countries/` |
| Country history | Vanilla baseline history exists; no mod Event 006 country history exists for any target | Vanilla `history/countries/SIN - Sindh.txt`, `HYD - Hyderabad.txt`, `MYS - Mysore.txt`, `MEN - Mengkukuo.txt`, `SAM - Samoa.txt`, `QUE - Quebec.txt`, `YUC - Yucatan.txt`; mod `history/countries/` |
| State and map overrides | No mod state override exists; installed binding ledger is the only current map evidence | Vanilla `history/states/443-Sind.txt`, `427-Hyderabad.txt`, `425-Mysore.txt`, `621-China 18.txt`, `746-Ordos.txt`, `726-Samoa.txt`, `466-Quebec.txt`, `468-Nunavut.txt`, `474-Yucatan.txt`; `006_current_installed_map_package_bindings.csv` |
| Package loaders and triggers | Exact `iw_136`, `iw_140`, `iw_141`, `iw_170`, `iw_175`, `iw_180`, and `iw_192` wrappers exist, but they only load generic planner metadata and require the shared readiness gate | `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt`; `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt` |
| Exact package-local adapters | None found beyond the generic regional loader, trigger, and weight wrappers | Exact-ID search across package, dispatch, adapter, and registry surfaces |
| Characters and roster | No Event 006 character IDs or recruitment blocks exist for the seven carriers | `common/characters/006_independence_wave_characters_registry.txt`; `history/general/006_independence_wave_character_recruitment_registry.txt` |
| Portrait wiring | No exact target portrait entries exist in the mod registry; no portrait-worker evidence exists | `interface/006_independence_wave_portraits_registry.gfx`; exact target-ID/tag search in mod interface and asset manifests |
| Flags and symbols | No mod flag family exists for the seven target tags; vanilla base-flag presence is not Event 006 symbol provenance | Vanilla `gfx/flags/`; mod `gfx/flags/` and flag registries |
| Localization | No Event 006 party, leader, advisor, idea, focus, decision, mission, cosmetic, or debug localization keys exist for the targets | Exact tag/package-ID search in mod `localisation/english/` |
| Focus tree | Shared generic tree exists but is assigned only after full-framework setup; no target-specific callbacks or route content exist | `common/national_focus/006_independence_wave_focus.txt`; `common/scripted_effects/006_independence_wave_focus_effects.txt` |
| Decisions and missions | No target package-local Event 006 decision or mission category exists; broad candidate lists and vanilla formables are not package evidence | Mod Event 006 decision files; vanilla `common/decisions/formable_nation_decisions.txt`; `common/decisions/categories/zzz_chaosx_formable_state_puzzle_categories.txt` |
| Ideas and starting problem | No target package-specific ideas, lifecycle, icon, or starting-problem evidence exists | Exact target-ID search in mod `common/ideas/`, scripted effects, decisions, and localization |
| AI | No target Event 006 AI profile or strategy surface exists | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`; exact package/tag search |
| Event integration | Shared Event 006 event and log systems exist, but no target-specific shell, outcome, or incident event is wired | Mod Event 006 event, log, and details surfaces; exact target-ID search |
| Cleanup and host restoration | Binding ledger states host remnants survive, but no target-specific release transaction, cleanup, Join, or former-host handoff is evidenced | `006_current_installed_map_package_bindings.csv`; package dispatch and runtime effect registries |

## Map, state, and former-host findings

SIN is bound to current state 443 Sind and retains RAJ as owner of the installed state before release. The state has SIN and PAK cores in vanilla, a 25-VP city province, a naval base, infrastructure, and a small industrial footprint, but no Event 006 transaction establishes the intended lower-Indus compact, controller, capital, rights, or former-host remnant behavior.

HYD is bound to current state 427 Hyderabad and retains RAJ as owner. The state has HYD as a vanilla core, chromium and steel, a 15-VP city, infrastructure, industry, and an airbase, but no Event 006 transaction establishes the intended princely compact, capital, rights, or former-host behavior.

MYS is bound to current state 425 Mysore and retains RAJ as owner. The state has MYS as a vanilla core, chromium and steel, two victory points, infrastructure, a small industrial footprint, and a naval base, but no Event 006 transaction establishes the intended princely compact, capital, rights, or former-host behavior.

MEN is reserved against states 621 and 746, both currently owned by SHX and carrying several vanilla Chinese, PRC, and MEN core relationships. The generic Event 006 loader records state 621 as its compact anchor, while the installed binding ledger records 621 and 746 together, so a future package implementation must reconcile the loader with the two-state compact before admission.

SAM is bound to state 726 with optional American Samoa extension state 1072. The installed map has different owners and capitals for the two states, and the ledger marks the binding `expanded_with_current_splits`; a future release transaction must prove exact split handling, controller and owner transitions, supply and naval behavior, and restoration of NZL and USA remnants.

QUE is the clearest current map rebind. The candidate and research rows use baseline state 466, while the installed binding and generic loader use current anchor 468 Saint Lawrence, compact states 468, 860, 861, 862, and 863, and extended state 466 Nord du Quebec. The package must preserve this current anchor and prove the 466 extension and CAN remnant behavior before admission.

YUC is bound to current state 474 and retains MEX as owner. The state has YUC as a vanilla core, a small population, an airbase, and two naval bases, but no Event 006 transaction establishes the intended peninsula compact, capital, rights, or former-host behavior.

Reservation capacity is a hard gate. `RG-443` contains IW-136 only; `RG-SOUTH-INDIA` contains IW-140, IW-141, IW-142, IW-143, and IW-144 and has one automatic slot; `RG-INNER-ASIA` contains IW-169 and IW-170 and has one automatic slot; `RG-PACIFIC-ISLANDS` contains IW-175, IW-176, IW-177, and IW-179 and has one automatic slot; `RG-466` contains IW-180 only; and `RG-MESOAMERICA-CARIBBEAN-COARSE` contains IW-191 through IW-195 and has one automatic slot.

The collision ledger records state 425 shared by IW-141 and IW-144 and state 427 shared by IW-140 and IW-144 inside `RG-SOUTH-INDIA`. No target row can bypass reservation capacity or state ownership checks through its generic wrapper.

The binding ledger marks all seven rows `ready_if_tag_not_living` and records a surviving host remnant, but this is a planning precondition rather than proof of a working release, transfer, annexation, puppet, or cleanup transaction.

## Politics, leaders, portraits, flags, advisors, and parties

Vanilla SIN starts with neutrality popularity D30, C5, N60, F5, two research slots, and no dedicated character roster. Vanilla HYD starts with neutrality D30, C5, N60, F5, three research slots, and only a Graveyard of Empires conditional recruitment of the RAJ character Mir Osman Ali Khan. Vanilla MYS starts with neutrality D20, C15, N60, F5, two research slots, and only a Graveyard of Empires conditional recruitment of the RAJ character Maharaja Jayachamarajendra Wadiyar.

Vanilla MEN is the Mengkukuo/Japanese-puppet country with a 1936 roster and `MEN_1936` order of battle, so its existing leaders and portraits cannot be treated as the Event 006 Inner Mongolia identity without an accepted source and sensitivity review.

Vanilla SAM starts democratic D50, F6, C6, N38 with 20 convoys and no dedicated Event 006 roster. Vanilla QUE starts democratic D70, F10, C15, N5 with Canadian order-of-battle and ship-variant content. Vanilla YUC starts democratic D60, C30, N10, F0 with the Mexican order of battle. These are baseline carrier histories, not complete Event 006 political packages.

No target-specific Event 006 party names, government pool, popularity setup, election behavior, laws, advisors, high command, commanders, or diplomatic recognition rules were found.

The research resolution rows require a sourced real male period leader for a registered tag when valid and not active elsewhere, or authentic archival material for the actual institution when that route is necessary. No defensible Event 006 leader or institution source is present for any of the seven rows, so no leader or portrait may be invented or borrowed as a fallback.

No portrait production, source placeholder, final user-supplied portrait, portrait manifest, identity/framing review, or runtime-vs-archive separation evidence exists for these carriers. Any future character portrait work must be routed through `chaosx_portrait_creator` and must satisfy the accepted source or fictional-production mode.

Vanilla SIN, HYD, MYS, and QUE have ideology-specific flag variants but no vanilla base flag file. Vanilla MEN has a base flag and an autonomy-neutrality variant, and vanilla SAM has a base flag plus democratic, fascist, and communist variants. Existing MEN or SAM files are not accepted Event 006 symbols without proof that they match the released identity and origin. No Event 006 flag provenance, emblem review, or rights decision exists for any target.

## Focus, decision, idea, and asset findings

The shared `independence_wave_focus_tree` in `common/national_focus/006_independence_wave_focus.txt` is gated by the full Event 006 framework and is loaded by `common/scripted_effects/006_independence_wave_focus_effects.txt` only after release assignment supplies the required setup. No target-specific focus group, route callback, branch localization, icon mapping, AI focus behavior, or package-owned focus reward exists for SIN, HYD, MYS, MEN, SAM, QUE, or YUC.

No package-local Event 006 decisions, missions, timed objectives, or decision icons exist for the seven rows. Existing vanilla formable references are not substitutes: SIN and HYD/MYS occur in vanilla Hindustan routes, SAM occurs in Polynesia routes, MEN occurs in a Greater Mongolia route, and QUE/YUC have no corresponding vanilla formable route in the inspected surfaces. None of these references proves the Event 006 package direction, FORM-32 Indus Federation, Deccan or Dravidian federation, Mongolic federation, Polynesian league, Canadian or Francophone compact, or Maya/Caribbean federation behavior.

No target-specific starting ideas, national-spirit lifecycle, starting weakness remediation, idea icons, focus icons, decision icons, event art, or package asset manifest exists. Generic force and disposition constants in `common/script_constants/006_independence_wave_constants_registry.txt` provide planner metadata only and do not satisfy package content, asset provenance, or runtime wiring.

## Starting military, technology, industry, supply, and production findings

The vanilla carrier histories provide only their normal baseline setup. SIN has infantry, recon, support, mountaineer, truck, motorized, and Great War artillery technology with two research slots and conditional DLC equipment. HYD and MYS have generic infantry, naval, and tank technology with two or three slots and conditional RAJ characters. MEN has generic technology and its existing Mengkukuo order of battle. SAM has infantry technology and convoys. QUE has Canadian generic land, naval, tank, doctrine, order-of-battle, and ship-variant content. YUC has Mexican generic land and naval content with the Mexican order of battle.

No Event 006 package defines starting divisions, templates, manpower allocation, equipment stockpiles, reinforcement policy, production lines, trains, fuel, convoys beyond carrier history, supply capacity, research-slot adjustments, or force-growth effects for any target.

The generic regional loader and force metadata constants cannot be promoted to complete package content. Doing so would create an unsupported generic fallback and could also produce an invalid state for the MEN two-state and SAM/QUE split bindings.

## AI and playability findings

`common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` has no exact AI profile for SIN, HYD, MYS, MEN, SAM, QUE, or YUC. Vanilla AI references to MEN in Soviet, German, and Chinese strategies concern Mengkukuo and are not Event 006 package behavior.

The generic prepare-weight wrappers in `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` call the corresponding `can_plan_independence_wave_package_iw_*` trigger and calculate planner weights, but they do not define target survival, focus choice, diplomacy, templates, decision behavior, front behavior, or recognition strategy.

`common/scripted_effects/006_independence_wave_scenario_effects.txt` ranks the seven target IDs in scenario ordering, but ranking is not an AI package profile or admission witness.

No probability baseline or comparison evidence exists for these rows. The mandatory `chaosx_ai_probability_auditor` route could not be run because the installed callable tool surface exposes no `hoi4.probability_inspect`, `hoi4.probability_evaluate`, or `hoi4.probability_compare` method. No AI weight or probability patch was made.

## Central gating, dispatch, and cleanup findings

`common/scripted_triggers/006_independence_wave_package_triggers.txt` defines `is_independence_wave_candidate_tag_available` as requiring both `is_independence_wave_candidate_origin_available = yes` and `has_country_flag = independence_wave_package_content_ready`.

The exact regional wrappers for IW-136, IW-140, IW-141, IW-170, IW-175, IW-180, and IW-192 all call that shared candidate-availability gate. Their exact loaders save the registered carrier and anchor scopes and assign generic package metadata, but none supplies the missing readiness evidence.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` contains a runtime package-content-attestation OR list for 32 other package IDs. None of `iw_136`, `iw_140`, `iw_141`, `iw_170`, `iw_175`, `iw_180`, or `iw_192` appears in that list.

`is_independence_wave_runtime_package_preflight_ready` requires a dormant country scope, a runtime adapter, content attestation, and origin safety. No exact target runtime adapter, attestation, release preflight, Join behavior, former-host handoff, incident cleanup, annexation cleanup, puppet cleanup, or final outcome cleanup exists.

The central readiness and dispatch gates were intentionally not widened. The exact target rows must not be added to an attestation OR list or granted a ready flag until their package-local evidence, map transaction, identity, assets, AI, and runtime cleanup are complete.

## Mandatory MCP and technology-viewer status

The installed callable tool inventory was inspected for the required HOI4 routes. It exposed only `mcp__blender_hoi4__...` 3D tools and no `mcp__hoi4...` focus, event, map, GUI, technology, or probability tools.

Consequently, the required read-only `hoi4.focus_inspect` and focus render, `hoi4.event_inspect` and event render, `hoi4.map_inspect`, and probability inspection/evaluation/comparison passes could not be performed for these country-linked surfaces.

The installed package currently exposes no Technology Tree Viewer. Technology dependency review therefore remains source-only and unresolved at the engine-evidence level.

Retained project audit notes record `ARTIFACT_MANIFEST_INTEGRITY_FAILED` and zero usable artifact receipts for the unavailable MCP route. This is an environment/tool blocker, not evidence that any target package is complete.

## Focused validation performed

`python .tools/audit_event6_country_api.py` passed with `broad=242`, `resolved=191`, `missing=0`, `duplicates=0`, and `IW-031-crosswalk=pass`. This validates the broad carrier API and does not admit the seven rows.

`python .tools/audit_event6_allocator.py` passed its allocator, reservation, adapter, static witness, protected-remnant, and pre-event retirement checks. The report still shows 40 runtime adapters and 32 attested packages, with none of the seven targets attested.

`python .tools/audit_event6_flags.py` passed with 102 registered Event 006 tags and 102 complete flag families. The seven vanilla carrier tags are not Event 006 registered X-ending tags, and this result does not establish target symbol provenance.

The focused exact-ID searches across mod country, history, character, recruitment, AI, localization, interface, flag, decision, idea, focus, event, and adapter surfaces found no target-specific package modules beyond the generic regional wrappers described above.

## Recommended next work before any admission

1. Complete source, rights, and partition-sensitivity review for each target, including a defensible period-fit male leader or institution and a symbol origin decision.

2. Route every required character portrait through `chaosx_portrait_creator`, with source or fictional evidence, master/runtime outputs, wiring, manifest, and final-versus-placeholder status.

3. Define package-local identity, party/government pool, starting problem, focus group, decisions, ideas, incidents, force/economy profile, AI profile, localization, and asset ownership for each row, keeping the regional identity distinct and avoiding generic claimant fallbacks.

4. Reconcile installed state bindings before implementation, especially MEN's 621/746 compact, SAM's 726/1072 split, and QUE's baseline 466 versus current 468 anchor.

5. Implement and test an exact package-local release transaction that preserves the former host, applies the accepted compact and optional extended territory, handles capital and cores, and cleans up every target outcome.

6. Only after package evidence is complete, add the narrow runtime adapter, attestation, preflight, focus assignment, Join, cleanup, and formable/ambition wiring required by the central contract.

7. Re-run the mandatory HOI4 focus, event, map, technology, and probability MCP inspections when the required server routes are available, including the same named probability scenarios for baseline and comparison.

## Simplifications, omissions, and blockers

No gameplay, central gating, asset, localization, or map patch was made because every available change would either invent unsupported country identity or widen a fail-closed gate without complete package evidence.

No leader, portrait, flag, party, focus, decision, idea, AI, military, economy, supply, formable, or cleanup fallback was invented or borrowed from a different vanilla carrier.

No exact package-local adapter was found beyond generic regional wrappers, and no target row was promoted to the admitted package set.

The seven rows remain incomplete and blocked by missing source/rights/identity evidence, missing package-local content and runtime adapters, missing asset provenance, missing AI probability evidence, unresolved map transaction details, and unavailable HOI4 MCP/Technology Tree Viewer routes.

Handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_asia_americas_country_package_audit_2026-08-29.md`.

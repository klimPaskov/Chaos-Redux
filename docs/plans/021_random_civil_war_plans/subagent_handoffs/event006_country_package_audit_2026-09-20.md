# Event 021 Event 006 country-package registry audit

Date: 2026-09-20

Disposition: HOLD / PARTIAL, read-only audit only.

This handoff records the current source and tool evidence for Event 021 reuse of the Event 006 Independence Wave country-package registry. No gameplay file was changed. This is not a completion claim.

## Scope and evidence labels

The audit covered AGENTS.md, the required Chaos Redux event, focus-tree, decision/mission, event-asset, portrait, and subagent instructions, the relevant offline Paradox wiki pages, the available vanilla documentation, the Event 006 package matrix and implementation, the Event 006 adapter registry and triggers, the Event 021 parent/effects/triggers/event files, current asset and country-package handoffs, and the current read-only HOI4 MCP routes.

Evidence labels used below are:

- Source-proven: established by current source inspection, a deterministic repository audit, or a successful read-only MCP response.
- Runtime-unverified: the source contract exists, but no live country materialization, save/reload, or in-game consumer receipt was available.
- Stale: useful historical evidence that is superseded by a newer current handoff or source revision.
- Incomplete: the surface exists but does not yet establish the requested acceptance claim.
- Blocked: the required route returned an error, the required artifact is absent, or the evidence cannot be obtained in this audit window.

## Executive result

The current Event 021 registry and Event 006 content-attestation list have exact 32-row parity. All 32 admitted IDs have an Event 021 adapter trigger, an Event 006 dynamic package loader, an Event 021 primary anchor, a carrier/release crosswalk, and a package setup function in current source.

The adapter path is source-proven to be separate from the normal Event 006 activation and commit path. It prepares reversible country-local state, uses an Event 021 origin record, and does not call the normal Event 006 generation allocator, origin-history writer, league/network activation, released-package writer, evolution synchronizer, or normal Event 006 commit path.

The selection and package setup dispatch are dynamic, but the Event 021 carrier and primary-anchor identity crosswalk is a static 32-branch adapter registry. This is a bounded fail-closed implementation, not proof of a generic computed carrier map.

Actual runtime execution remains unverified for all 32 packages. There is no current live receipt proving that every package materializes its leader, flags, politics, ideas, focus assignment, force package, reinforcement, formable behavior, decisions, AI behavior, assets, former-host transfer, cleanup, and save/reload persistence without an engine-side defect.

The inherited Event 006 implementation is itself HOLD / PARTIAL. Its current evidence records 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. The central Event 006 handoff still lists unresolved portrait, flag provenance, dynamic GUI, formable/League reachability, route-cost, audio, and typed-probability gates.

## Admission and fail-closed parity

Authoritative sources:

- docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv
- docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv
- common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt
- common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt
- common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt
- common/scripted_effects/006_independence_wave_package_region_effects_registry.txt
- common/scripted_effects/006_independence_wave_scenario_effects.txt
- common/scripted_effects/021_random_civil_war_parent_effects.txt
- common/scripted_effects/021_random_civil_war_effects.txt
- common/scripted_triggers/021_random_civil_war_triggers.txt
- common/scripted_triggers/021_random_civil_war_parent_triggers.txt

The current Event 021 adapter registry array contains exactly these 32 IDs, with no duplicate and no content-attestation mismatch:

IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-024, IW-026, IW-027, IW-028, IW-029, IW-030, IW-031, IW-033, IW-038, IW-040, IW-041, IW-044, IW-045, IW-070, IW-071, IW-072, IW-173, IW-184.

The broader Event 006 adapter dispatch list contains 40 IDs. The eight adapter-only IDs outside the 32 content-attested registry are:

IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, IW-179.

These eight are source-proven fail-closed because they are not in the Event 021 complete-package array and do not satisfy the Event 006 content-attestation branch.

The Event 006 preflight requires the dormant-country scope, adapter admission, content attestation, no Soviet origin, and no active Event 006 origin. Event 021 additionally requires a normal human country, an Event 021 package identifier, a valid identity adapter, an origin adapter, no collision, a valid route, and the package setup proof contract.

The actual nonhuman exclusion is inherited from common/scripted_triggers/chaosx_dynamic_triggers.txt, where is_actual_nonhuman_country is defined, and from common/scripted_triggers/021_random_civil_war_triggers.txt, where random_civil_war_is_normal_human_country and event021 package admission require the country to be normal human. Incomplete packages fail closed through content attestation, package preflight, setup completion, focus contract, AI profile, force mapping, and identity checks.

## Complete 32-row carrier, anchor, release, and setup crosswalk

The table below is the current source crosswalk used by the Event 021 adapter. “Source-proven” means the mapping and setup identifier resolve in source. It does not prove live materialization.

| Package | Carrier tag | Event 021 primary anchor | Setup function | Setup source |
| --- | --- | ---: | --- | --- |
| IW-001 | SCO | 121 | independence_wave_setup_iw_001_scotland | common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt |
| IW-002 | WLS | 122 | independence_wave_setup_iw_002_wales | common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt |
| IW-004 | BRI | 14 | independence_wave_setup_iw_004_brittany | common/scripted_effects/006_independence_wave_western_package_effects.txt |
| IW-006 | AFX | 34 | independence_wave_setup_iw_006_wallonia | common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt |
| IW-007 | AGX | 36 | independence_wave_setup_iw_007_frisia | common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt |
| IW-008 | RHI | 51 | independence_wave_setup_iw_008_rhineland | common/scripted_effects/006_independence_wave_rhineland_bavaria_saar_package_effects.txt |
| IW-009 | BAY | 52 | independence_wave_setup_iw_009_bavaria | common/scripted_effects/006_independence_wave_rhineland_bavaria_saar_package_effects.txt |
| IW-010 | AJX | 42 | independence_wave_setup_iw_010_saar | common/scripted_effects/006_independence_wave_rhineland_bavaria_saar_package_effects.txt |
| IW-012 | ICE | 100 | independence_wave_setup_iw_012_ice | common/scripted_effects/006_independence_wave_western_package_effects.txt |
| IW-014 | CAT | 165 | independence_wave_setup_iw_014_catalonia | common/scripted_effects/006_independence_wave_western_package_effects.txt |
| IW-017 | COR | 1 | independence_wave_setup_iw_017_corsica | common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt |
| IW-018 | ARX | 114 | independence_wave_setup_iw_018_sardinia | common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt |
| IW-019 | ASX | 115 | independence_wave_setup_iw_019_sicily | common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt |
| IW-023 | TRA | 84 | independence_wave_setup_iw_023_transylvania | common/scripted_effects/006_independence_wave_balkan_package_effects.txt |
| IW-024 | AXX | 82 | independence_wave_setup_iw_024_banat | common/scripted_effects/006_independence_wave_balkan_package_effects.txt |
| IW-026 | MAC | 106 | independence_wave_setup_iw_026_macedonia | common/scripted_effects/006_independence_wave_balkan_package_effects.txt |
| IW-027 | BAX | 184 | independence_wave_setup_iw_027_thrace | common/scripted_effects/006_independence_wave_balkan_package_effects.txt |
| IW-028 | BBX | 185 | independence_wave_setup_iw_028_epirus | common/scripted_effects/006_independence_wave_balkan_package_effects.txt |
| IW-029 | BOS | 104 | independence_wave_setup_iw_029_bosnia | common/scripted_effects/006_independence_wave_balkan_package_effects.txt |
| IW-030 | MNT | 105 | independence_wave_setup_iw_030_montenegro | common/scripted_effects/006_independence_wave_balkan_package_effects.txt |
| IW-031 | KOS | 802 | independence_wave_setup_iw_031_kosovo | common/scripted_effects/006_independence_wave_kosovo_package_effects.txt |
| IW-033 | KAR | 146 | independence_wave_setup_iw_033_karelia | common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt |
| IW-038 | RUT | 73 | independence_wave_setup_iw_038_ruthenia | common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt |
| IW-040 | KUB | 234 | independence_wave_setup_iw_040_kuban | common/scripted_effects/006_independence_wave_kuban_package_effects.txt |
| IW-041 | CRI | 137 | independence_wave_setup_iw_041_cri | common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt |
| IW-044 | TAT | 249 | independence_wave_setup_iw_044_tatarstan | common/scripted_effects/006_independence_wave_tatarstan_package_effects.txt |
| IW-045 | BSK | 651 | independence_wave_setup_iw_045_bashkiria | common/scripted_effects/006_independence_wave_bashkiria_mari_package_effects.txt |
| IW-070 | ARM | 230 | independence_wave_setup_iw070_armenia | common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt |
| IW-071 | GEO | 231 | independence_wave_setup_iw071_georgia | common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt |
| IW-072 | AZR | 229 | independence_wave_setup_iw072_azerbaijan | common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt |
| IW-173 | HAW | 629 | independence_wave_setup_iw_173_hawaii | common/scripted_effects/006_independence_wave_pacific_package_effects.txt |
| IW-184 | HBX | 378 | independence_wave_setup_iw_184_california | common/scripted_effects/006_independence_wave_pacific_package_effects.txt |

The adapter registry effect contains the explicit package-to-carrier capture and release branches. The release branch only releases the carrier when it does not already exist. The adapter trigger contains the corresponding 32 state/tag branches, each requiring ROOT ownership, population above the Event 021 minimum, infrastructure above zero, and a dormant carrier scope.

The Event 006 candidate matrix has broader reservation anchor groups for some packages than the Event 021 primary adapter anchor. IW-001 is listed as 121|120|133 while the adapter uses 121. IW-009 is listed as 52|53|54 while the adapter uses 52. IW-023 is listed as 84|76 while the adapter uses 84. IW-031 has a blank baseline anchor field in the CSV while the current adapter uses 802. These are reconciliation and runtime-coverage items, not automatically source defects, because the adapter may intentionally choose one primary anchor from a multi-state package reservation group.

## Dynamic selection and package identity

common/scripted_effects/021_random_civil_war_parent_effects.txt, in event021_parent_find_event6_package, loops the global Event 021 complete-package array, skips scenario-reserved packages, stores the temporary package ID, calls independence_wave_scenario_load_dispatch_package, and checks the loader-produced candidate anchor for ownership, control, population, infrastructure, capital, and reservation constraints.

common/scripted_effects/006_independence_wave_scenario_effects.txt, in independence_wave_scenario_load_dispatch_package, dispatches the temporary package identifier through numeric meta-effect branches to the matching independence_wave_load_package_iw_* loader.

common/scripted_effects/006_independence_wave_package_region_effects_registry.txt contains the 32 loader definitions. Each loader sets the candidate package ID, reservation group, region, depth, archetype, disposition, tag flag, candidate-country event target, exact anchor event target, and primary host.

The resulting identity flow is therefore dynamic for package selection, loader output, setup dispatch, and validation, while the package-to-carrier and primary-anchor adapter identity is explicitly enumerated. The source does not prove that a generic computed tag table replaces that crosswalk.

## Event 006 lifecycle and mutation boundary

common/scripted_effects/006_independence_wave_effects.txt, in independence_wave_prepare_origin_state around lines 696-845, writes reversible country-local generation, package, region, depth, territory, force, chaos, archetype, date, host, anchor, and lifecycle state.

When random_civil_war_event6_adapter_preparing exists, the shared preparation effect copies the Event 021 generation and does not advance global.independence_wave_next_generation_id or call independence_wave_registry_record_event6_origin. The normal branch performs those Event 006 operations, but the Event 021 adapter branch does not.

independence_wave_prepare_event021_adapter_origin is a separate adapter entry point. It requires the Event 021 adapter preparation and package-ready flags and calls only the shared reversible preparation.

The normal Event 006 activation and commit effects are separate. independence_wave_activate_prepared_country_origin opens the normal league, active-country, network-member, and host-ledger state. independence_wave_commit_prepared_country_origin writes Event 006 historical arrays, released package IDs, and evolution synchronization. The Event 021 adapter path does not call those normal activation or commit effects.

common/scripted_effects/021_random_civil_war_effects.txt records Event 021-specific origin state in event021_record_event6_origin using random_civil_war_event6_origin_recorded, random_civil_war_origin_kind = event006, and the Event 021 generation/date variables. It does not invoke the normal Event 006 origin initializer.

This is source-proven as a call-path boundary against Event 006 fired state, repeatable weight, cap, fire count, normal evolution history, normal released-package history, normal league enrollment, and normal network enrollment. It remains runtime-unverified because no live save receipt or engine state dump was available.

## Event 021 origin, opening, cleanup, and save/reload boundaries

events/021_random_civil_war.txt defines chaosx.nr21.1 as the hidden triggered-only Event 021 parent entry, chaosx.nr21.8 as the Event 021 report event, and chaosx.nr21.10 as the hidden cleanup event. Event 021 does not fire chaosx.nr6.1 as its package origin.

event021_parent_prepare_event6_adapter_actor in common/scripted_effects/021_random_civil_war_parent_effects.txt sets the Event 021 adapter preparation flags, copies the generation/severity/archetype/front/crisis/package/anchor/region/depth values, maps severity to force and chaos, maps state count to territory level, saves former-host and anchor targets, prepares Event 006 admission, calls the Event 006 adapter origin effect, and dispatches package setup.

The setup proof trigger in common/scripted_triggers/021_random_civil_war_parent_triggers.txt requires the origin-prepared flag, package setup completion, command roster readiness, force mapping loaded and applied, a full or additive focus assignment, the generic focus contract, a generic AI profile, setup anchor and former-host targets, a current-generation force package, and the absence of Event 006 active-origin, network, and league flags.

event021_parent_start_event6_front around line 4255 commits the Event 021 front only after the adapter setup is complete, the actor can declare war on the host, the anchor transfer is valid, and the Event 021 front/force receipts are written. event021_parent_try_event6_secondary_front around line 4094 rehydrates the frozen plan and rechecks the anchor before rerunning adapter preparation.

event021_parent_finalize_event6_actor around line 6873 intentionally preserves the surviving Event 006 package identity, focus, ideas, force package, and Event 021 origin receipt while clearing Event 021 reconstruction state. event021_parent_cleanup_crisis around line 6958 clears Event 021 scenario, front, decision, idea, exposure, route, host temporary state, and global Event 021 targets.

There is a source cleanup risk in failure paths. event021_parent_abort_event6_opening around line 3930 and event021_parent_abort_event6_secondary_front around line 4042 clear Event 021 state and annex a newly created actor, but do not call independence_wave_dispatch_package_cleanup before annexing or retaining a pre-existing carrier. If a pre-existing carrier reaches partial package setup, its package ideas, flags, decisions, force/package variables, or other setup residue are not source-proven to be removed by these abort paths.

event021_parent_clear_event6_package_transaction around line 4006 clears pending package variables, planned package/region/depth/archetype variables, global Event 021 targets, route state, selected flags, and candidate variables. This is a transaction cleanup receipt, not proof that all package-owned country content is cleaned from a pre-existing carrier.

No save/reload boundary receipt is available for the 32-package path. Persistence of the separate Event 021 origin, idempotence of leaders/flags/focus/ideas/units/technology/decisions/formations, and cleanup after reload remain runtime-unverified.

## Country package coverage checklist

### Country tags, map states, carriers, and duplicate identities

Source-proven:

- The Event 006 country API audit passed with 242 broad unique tags, 191 resolved carrier tags, 34 Soviet entries, 45 Africa entries, missing=0, duplicates=0, and IW-031 crosswalk=pass.
- The strict allocator audit reports 40 runtime adapters, eight adapter-only fail-closed IDs, 32 attested packages, 29 compatible reservation groups, and the protected former-host witness states BEL=6, ENG=126, FIN=111, FRA=16, GER=64, HOL=7, ITA=2, ROM=46, SOV=219, SPR=41, USA=361.
- The strict flag audit reports 102 registered Event 006 tags, 102 complete flag families, and zero incomplete flag families.

Runtime-unverified:

- Current save ownership, controller state, capitals, victory points, ports, resources, buildings, supply nodes, railways, and live carrier collision behavior for every selected anchor.
- Repeated or nested Event 021 execution after a save/reload.

The map MCP resolved the selected anchor IDs as source/catalog entries, but it did not provide current campaign ownership or controller state.

### Leaders, characters, portraits, advisors, and parties

Source-proven:

- The Event 006 package setup and character/leader registries are part of the shared package setup and final-validation path.
- The current portrait consumer handoff finds 38 of 51 supplied DDS candidates with safe exact source-to-runtime consumers, 64 unique current GFX portrait mappings, no duplicate portrait names/textures, and 64 resolved texture paths.

Incomplete or runtime-unverified:

- Thirteen grounded portrait rows remain unmapped and fail closed in the central Event 006 evidence.
- No current package-by-package live consumer receipt proves that each admitted carrier receives the intended leader, advisor, high command, commander, trait, portrait path, gender metadata, and name pool.
- This audit found no specifically proven opposite-gender portrait/name pairing for the 32 admitted packages, but absence of a discovered pair is not runtime proof of correct character materialization.
- Grounded source placeholders remain source-only until the required HOI4-style final portrait is supplied. No RunPod operation was performed and no portrait production claim is made.
- Party names, ideology routes, election/law state, stability, war support, diplomacy, guarantees, subjects, and faction behavior are source-linked through package setup but not live-consumer verified for all 32.

### Flags, cosmetic identities, and localisation

The strict flag-family validator passes 102 families, but the current Event 006 handoff still lists unresolved flag provenance and alias ownership. This means family completeness is source-proven while final provenance and runtime cosmetic identity acceptance remain incomplete.

Country, adjective, party, leader, advisor, idea, focus, decision, tooltip, cosmetic-tag, and debug localisation are covered by the shared package and asset surfaces in source, but no fresh all-32 rendered localisation/consumer receipt was available.

### Focus trees and focus assignment

The shared Event 006 focus tree is common/national_focus/006_independence_wave_focus.txt with the package assignment and setup effects in common/scripted_effects/006_independence_wave_focus_effects.txt and the package setup validation in the Event 006 effects.

The current read-only focus inspection reports 184 focuses and 196 connectors with zero connector crossings, intersections, or too-close diagnostics. It reports one authored FOCUS_LAYOUT_LONG_CONNECTOR warning for independence_wave_adopt_military_archetype_program to independence_wave_adopt_reclamation_doctrine spanning ten columns and one row. It also reports an unrelated vanilla missing continuous_restrict_freedom_desc warning.

Event 021 setup requires either the full framework plus assignment or an additive overlay plus assignment, the generic focus contract, and package setup proof. There is no current live assignment, route-availability, icon-consumer, focus-choice, or save/reload receipt for each admitted carrier.

### Politics, ideas, decisions, and missions

The current Event 006 decision inventory reports 80 accepted rows, 80 definitions, 80 visibility/activation gates, 80 availability gates, 80 AI blocks, and terminal lifecycle markers. The active decision sources are common/decisions/006_independence_wave_decisions.txt, common/decisions/006_independence_wave_formable_decisions.txt, common/decisions/categories/006_independence_wave_categories.txt, the package-specific common/decisions/006_independence_wave_*_decisions.txt files, common/scripted_triggers/006_independence_wave_decision_triggers.txt, and common/scripted_effects/006_independence_wave_decision_effects.txt.

There is no standalone common/decisions/006_independence_wave_missions.txt; mission behavior is embedded in decision files. That is an inherited documentation and surface-discovery limitation, not proof of missing runtime missions.

The current decision handoff identifies a P1 gate gap in DM-03 independence_wave_register_population because it lacks accepted anchor and local-peace requirements. It also identifies formable revolutionary/military commit costs exposing seven spendable groups, unresolved GUI and Statehood Ledger/formable-state-puzzle warnings, incomplete weighted AI evidence, and an incomplete cleanup-timer inventory.

Starting ideas, national spirits, political setup, party popularity, laws, and decision unlocks are carried through shared package setup and final validation, but their all-32 live behavior, icon consumers, retirement timing, and post-abort cleanup remain runtime-unverified.

### Formables, recognition, League, and network state

The Event 006 formable registry explicitly separates formable readiness from package admission. Package admission does not itself assign a cosmetic tag or prove formable reachability.

FORM-09 is documented as operational for BBX and BAX with BLX cosmetic handling. FORM-16 is separately documented for ARM, GEO, and AZR. FORM-48 is blocked because FSM is adapter-only and not content-attested. HAW and HBX admission alone does not satisfy FORM-48.

The Event 021 adapter path is source-proven not to auto-enroll the carrier in the normal Event 006 League or network. Formable reachability, recognition, diplomatic completion, and any post-war League state are runtime-unverified.

### Forces, reinforcement, technology, industry, supply, and production

The Event 021 package setup proof requires command roster readiness, force mapping loaded and applied, a current-generation force package, and the appropriate package setup/validation dispatchers. This source contract covers the intended force and reinforcement handoff.

No live receipt verifies starting divisions, templates, manpower, equipment stockpiles, technologies, research slots, production lines, trains, convoys, fuel, ports, railways, supply capacity, or post-transfer reinforcement behavior for all 32 packages.

No separate Event 006 country technology tree was found. The current package surface uses the shared focus/doctrine and technology bonuses rather than a package-specific technology tree. The read-only technology MCP inspect and render routes are available, but they prove tool/source visibility only, not package-specific runtime state.

The installed hoi4-agent-tools package check reports version 3.0.7 and standalone_viewer_in_package=false. External standalone Technology Tree Viewer installations were not inventoried. The exposed technology MCP route must not be treated as proof that a standalone viewer is installed.

### AI, weighted logic, and playability

The Event 006 AI registry source common/ai_strategy/006_independence_wave_ai_strategy_registry.txt was discovered by hoi4.probability_inspect with status PROBABILITY_SOURCE_DISCOVERED, source revision 58533f298991f38b9e018af029b4679ffb3bb3be131b77132b7e5447da3566f9, source hash b84ee2ca17f45793196641dd0d383779fb2e36ab29da6a1ee2d90912ec82deb6, discoveryReason=no_weighted_surfaces, candidates=0, available=0, requiredInputs=0, unresolved=0, and no available adapters.

The Event 021 AI source common/ai_strategy/021_random_civil_war_ai_strategy.txt returned MCP status INTERNAL_ERROR with blocker Unexpected internal error. The same direct probability route against common/scripted_effects/021_random_civil_war_parent_effects.txt returned INTERNAL_ERROR.

The mandatory chaosx_ai_probability_auditor pass was bounded and did not return a completed receipt before this handoff was written. It was not retried. The inherited Event 006 probability handoffs report an outer 14-entry pool only, an incomplete nested 126-candidate pool, no normalized package probabilities, and incomplete decision, mission, focus, AI, MTTH, technology, and doctrine weighting evidence.

Consequently, no package-normalized Event 021 probability, AI strategy factor, focus choice, decision score, front behavior, diplomacy behavior, or survival/playability claim is complete.

### Assets and reuse claims

Source-proven:

- The Event 006 asset refresh reports 324 Event 006 DDS files, 64 registered portraits, 121 focus icons, 43 idea/national-spirit icons, 69 decision/category icons, 16 report/news/super-event scenes, eight animation assets, 48 achievement states, and 104 state-puzzle pieces.
- The current GFX census reports 1,391 identifiers across six relevant registries with zero duplicate identifiers or missing textures after the current decoder pass.
- The current portrait consumer gate reports 38 safe exact consumers and 13 unmapped grounded rows.

Incomplete or runtime-unverified:

- Final asset acceptance for all admitted package leaders and carrier identities.
- Flag provenance and alias ownership.
- Dynamic GUI state, click, and blendframe behavior.
- Asset reuse in a live Event 021 package consumer after release, save, reload, and cleanup.
- Audio audition and runtime report/news/super-event consumer proof.

No archive reference was found in the current runtime GFX census, but no live consumer session was available.

## Static validation evidence

The following read-only validators returned exit code 0 during this audit:

- python -B .tools/audit_event6_allocator.py --strict: Event 006 allocator audit passed; 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 40 runtime adapters, eight adapter-only fail-closed IDs, 32 attested packages, 29 compatible reservation groups, and the expected automatic/scenario counts.
- python -B .tools/audit_event6_country_api.py: broad=242 unique tags, resolved=191 unique carriers, Soviet=34, Africa=45, missing=0, duplicates=0, IW-031-crosswalk=pass.
- python -B .tools/audit_event6_flags.py --strict: registered Event 006 tags=102, complete flag families=102, incomplete flag families=0.
- python -B .tools/audit_event6_scenario_matrix.py: SCN-008 matrix audit passed 32 cells and eight edge cases; publication commit, ledger, and result counts are one each; failed branch logs/dispatch=0.

These validators are source/static evidence. They do not establish live engine behavior, save/reload behavior, or package-specific visual acceptance.

## Current HOI4 MCP evidence and blockers

| Surface | Result | Current evidence or blocker |
| --- | --- | --- |
| Event 006 focus inspect | Source-proven | FOCUS_INSPECTED, source revision c436f2f19c1c7cdfb0c3286a168fa3ddaddfa27f5c32672c1e4a0a72fe4df8eb, 184 focuses, 196 connectors, zero crossings/intersections/too-close diagnostics, one authored long-connector warning. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/31ae75368c352d4f30abd9ed39b3a80d0b52ce98a7e120bf32d346fdde1e0c69/34ab25c79b102488f09cde67e165cc0193a36a103d1c52a892d3709c53043e16/focus-inspect.c436f2f19c1c7cdf.json |
| Event 006 focus render | Source/render evidence | FOCUS_RENDERED with SVG artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/352b090f1cd955f9cbb30a41e0ae581761c08f51f20d788d63598a7bd7d4c3e2/c2907d891c67154463b2aecdf40e3c5d2f8772bbd4f4972f4b409fc041bb4dfa/independence_wave_focus_tree.focus.svg. No live focus assignment or save receipt. |
| Event 021 state-flow inspect | Blocked | hoi4_event_inspect for chaosx.nr21.1 with downstream state-flow query returned INTERNAL_ERROR with blocker Unexpected internal error and no artifact. |
| Event 021 event render | Partial source evidence | hoi4_event_render returned EVENT_RENDERED_PARTIAL. It reported inline source truncation because 371 files were scanned and 64 were inline. It did not provide runtime execution evidence. |
| Event 006/Event 021 map inspect | Incomplete | Selected source anchor entries resolved with zero unknown/missing geometry in the bounded rerun, but global diagnostics were truncated with 2,654 omitted errors, including MAP_BUILDING_POSITION_INVALID and MAP_PORT_ADJACENT_SEA_INVALID in mod:map/buildings.txt. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b73666413d35e6b8d9455230c6f2feb7b367c59fcaddc9f52e68b942dcb22da/6ace95699530a446a881cdd3a52ea194597094988ae5d5d1a477418cd1de1533/map-inspect.291a30cd67b7e0f1.json |
| Event 021 map render | Source/render evidence | MAP_RENDERED for the requested state layer and overlays. It does not prove current save ownership, controller, supply, or transfer behavior. |
| Technology inspect/render | Source/tool evidence | TECH_INSPECTED and TECH_RENDERED succeeded. The route is available, but no custom Event 006 package technology tree or live carrier technology state was proved. |
| Event 006 probability inspect | Incomplete | PROBABILITY_SOURCE_DISCOVERED with no weighted surfaces or adapters for the Event 006 AI registry. Artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1013cb19fa83e49bd4d73006d7c70b89f70aa3d36074d8594ed27ba5e7bd1128/0387ac7da975789868d13f691bd5d32d6444038fb86144b1961c88300ca5f8f7/probability-inspect-b84ee2ca17f4.json |
| Event 021 probability inspect | Blocked | Direct inspect of common/ai_strategy/021_random_civil_war_ai_strategy.txt returned INTERNAL_ERROR with blocker Unexpected internal error. |
| Standalone Technology Tree Viewer | Verified package gap | Installed hoi4-agent-tools 3.0.7 reports standalone_viewer_in_package=false; external viewer installations were not inventoried. |

The Event 021 event render artifact was also produced, but the state-flow inspector error and source truncation mean it is structural source evidence only. The current Event 006 focus handoff remains the authoritative newer focus receipt over older focus artifacts.

## File surface checklist

| Surface | Current source | Status |
| --- | --- | --- |
| Event 006 accepted package matrix | docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv | 32 content-attested package rows are source-attested; broader selectable registry is not fully attested. |
| Installed map bindings | docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv | Current package/host/anchor binding evidence exists; former-host and alternative-anchor semantics need runtime proof. |
| Event 006 adapter registry | common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt | 32 complete IDs and explicit capture/release crosswalk source-proven. |
| Event 006 adapter triggers | common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt | 32 dormant package branches source-proven. |
| Event 006 dispatch and attestation | common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt | 40 adapter IDs, 32 content IDs, eight adapter-only fail-closed IDs. |
| Dynamic package loader | common/scripted_effects/006_independence_wave_scenario_effects.txt | Numeric/meta dispatch source-proven. |
| Package loader registry | common/scripted_effects/006_independence_wave_package_region_effects_registry.txt | 32 loader identities source-proven. |
| Event 006 lifecycle | common/scripted_effects/006_independence_wave_effects.txt | Adapter preparation is separate from normal activation and commit; central Event 006 remains partial. |
| Event 021 parent | common/scripted_effects/021_random_civil_war_parent_effects.txt | Dynamic selection, setup, front, finalize, abort, and transaction clear paths inspected. |
| Event 021 effects and triggers | common/scripted_effects/021_random_civil_war_effects.txt; common/scripted_triggers/021_random_civil_war_triggers.txt; common/scripted_triggers/021_random_civil_war_parent_triggers.txt | Admission, identity, origin, setup, collision, and cleanup contracts inspected. |
| Event 021 root events | events/021_random_civil_war.txt | chaosx.nr21.1, chaosx.nr21.8, and chaosx.nr21.10 identified. |
| Focus tree and assignment | common/national_focus/006_independence_wave_focus.txt; common/scripted_effects/006_independence_wave_focus_effects.txt | MCP structural evidence available; live assignment not verified. |
| Decisions and categories | common/decisions/006_independence_wave_decisions.txt; common/decisions/006_independence_wave_formable_decisions.txt; common/decisions/categories/006_independence_wave_categories.txt | 80-row source inventory; DM-03 and cost/GUI/cleanup gaps inherited. |
| Formables | common/scripted_effects/006_independence_wave_formable_registry_effects.txt; common/decisions/006_independence_wave_formable_decisions.txt | Admission and formable readiness are separate; FORM-48 remains blocked by FSM. |
| AI | common/ai_strategy/006_independence_wave_ai_strategy_registry.txt; common/ai_strategy/021_random_civil_war_ai_strategy.txt | Event 006 weighted surfaces absent; Event 021 probability route blocked. |
| Portrait and asset evidence | docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_portrait_consumer_gate_2026-08-31.md; docs/events/021_random_civil_war/owned_asset_crosswalk.md; docs/events/021_random_civil_war/reused_asset_individual_review.md | 38/51 safe portrait consumers; 13 unmapped; final/runtime acceptance incomplete. |
| Current Event 006 validation | docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_validation_refresh_2026-09-19.md | Current inherited disposition is HOLD / PARTIAL. |
| Event 006 parity matrix handoff | docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_admitted_package_parity_matrix_2026-09-03.md | Useful parity and row-level source map; older than the 2026-09-19 validation refresh. |

## Stale, incomplete, and blocked evidence

The 2026-09-03 Event 006 parity handoff is retained as a row-level source map but is stale relative to the 2026-09-19 Event 006 validation refresh and the 2026-09-20 focus MCP receipt.

The older Event 006 probability and event receipts remain historical. They establish that the outer/nested package probability and Event 006 state-flow routes were previously incomplete or errored, but they are not current runtime proof.

The Event 021 state-flow inspector currently returns INTERNAL_ERROR. The Event 021 AI probability route currently returns INTERNAL_ERROR. The bounded chaosx_ai_probability_auditor call did not return a completed receipt and was not retried.

The map inspector currently reports global diagnostics truncation and unrelated building/port geometry errors. No selected-anchor-specific map defect was established in the bounded result, but current campaign ownership and controller state remain unavailable.

The final package-level portrait, flag provenance, dynamic GUI, formable/League reachability, route-cost, audio, normalized probability, live AI, live force, and save/reload evidence remains incomplete or runtime-unverified.

The Event 021 abort-path package-cleanup omission is a source-level risk that must be resolved or explicitly accepted by the parent before any completion claim.

## Parent review boundary

This handoff is an audit result, not a gameplay patch and not a completion report. The parent should retain the HOLD / PARTIAL disposition until it has a reviewed decision on the abort cleanup gap, a completed typed probability audit, and current runtime evidence for package materialization, former-host transfer, collision handling, cleanup, and save/reload persistence.

No gameplay source, assets, matrices, or existing handoffs were modified by this audit. The only intended new file is this handoff.

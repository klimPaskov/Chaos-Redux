# Event 006 IW-108 Buganda country-package re-audit

Date: 2026-09-02

Scope: bounded source, installed-map, and engine-facing audit of IW-108 Buganda (`UGA`) for Event 006 Independence Wave, including the Event 012 ownership collision, identity and rights gate, state 548 setup, roster and asset provenance, package-local gameplay surfaces, central adapter and attestation, SCN-008, and Join.

Decision: FAIL-CLOSED / NO GAMEPLAY CHANGE.

No accepted non-generic package-local tranche is safe to patch. Event 012 currently owns UGA/Buganda origin, package identity, sovereign, portrait consumer, ideas, decisions, focus tree, force preparation, and lifecycle cleanup, while Event 006 has only dormant planning metadata for IW-108 and has no resolved identity/rights packet or package implementation to reconcile with that owner. Event 012 is evidence of an ownership collision, not an Event 006 fallback.

## Authority and reference review

The repository guidance and applicable skills were read before inspection: `AGENTS.md`, `.agents\skills\chaos-redux-subagents\SKILL.md`, `.agents\skills\chaos-redux-events\SKILL.md`, `.agents\skills\chaos-redux-focus-trees\SKILL.md`, `.agents\skills\chaos-redux-decisions-missions\SKILL.md`, `.agents\skills\chaos-redux-event-assets\SKILL.md`, `.agents\skills\chaos-redux-comfyui\SKILL.md`, and `.agents\skills\chaos-redux-improvement-loop\SKILL.md`.

The required offline references were consulted in `paradox_wiki\`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, State modding, Map modding, and Technology modding. Relevant vanilla documentation was read from `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\`, including `script_concept_documentation.md`, `effects_documentation.md`, `triggers_documentation.md`, country-creation guidance, and the script-constants documentation.

The accepted package and admission sources remain `docs\specs\006_independence_wave_specs\specs\006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `docs\specs\006_independence_wave_specs\research\006_package_research_resolution.csv`, `docs\specs\006_independence_wave_specs\matrices\006_candidate_country_registry.csv`, `docs\plans\006_independence_wave_plans\package_bindings\006_current_installed_map_package_bindings.csv`, `docs\plans\006_independence_wave_plans\package_bindings\006_current_map_reservation_groups.csv`, and `docs\plans\006_independence_wave_plans\006_force_package_mapping.csv`.

Earlier ownership evidence is recorded in `docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_iw108_buganda_ownership_source_gate_2026-08-27.md` and `docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_iw108_buganda_country_package_audit_2026-08-30.md`. The accepted tranche addenda still state that IW-108 is not patchable until ownership and source gates are resolved: `docs\plans\006_independence_wave_plans\006_event6_next_safe_tranche_improvement_addendum_2026-08-29.md` and `docs\plans\006_independence_wave_plans\006_event6_first_footprint_admission_improvement_addendum_2026-08-26.md`.

## Accepted IW-108 contract versus current implementation

The registry binds IW-108 to Buganda, `UGA`, reuse of the registered tag, state `548`, reservation `RG-GREAT-LAKES-COARSE`, and the East Africa/Horn/Great Lakes region. The accepted design names the Buganda/Kabaka/Lukiiko/land/lake/protectorate conflict, the founding focus `independence_wave_iw108_convene_buganda_settlement`, serialized projects `iw108_reconvene_lukiiko`, `iw108_review_land_obligations`, `iw108_restore_lake_transport`, and `iw108_organize_territorial_guard`, settlements `iw108_ratify_lukiiko_ministry`, `iw108_confirm_kabaka_council`, and `iw108_authorize_protectorate_command`, plus `iw108_open_great_lakes_delegation` and FORM-27 Great Lakes Federation.

Those identifiers are accepted design obligations only. None of the package-local IW-108 gameplay identifiers are implemented in Event 006 source, and they must not be filled by copying the Event 012 Buganda route.

## Country-package coverage checklist

| Surface | Current evidence | Status and blocker |
| --- | --- | --- |
| Identity and tag | `docs\specs\006_independence_wave_specs\matrices\006_candidate_country_registry.csv:109` and `docs\specs\006_independence_wave_specs\research\006_package_research_resolution.csv:109` bind IW-108 to Buganda and `UGA` with `reuse_registered_tag`. Event 006 planning loads `iw_108` and maps `UGA` to the liberation candidate in `common\scripted_effects\006_independence_wave_package_region_effects_registry.txt:2138-2153`. | PARTIAL. The registered tag is available, but Event 012 owns the live UGA/Buganda origin and package predicates, so an Event 006 identity/rights contract is not resolved. |
| Territory and anchor | State `548` is the accepted fixed anchor and compact release state in `docs\plans\006_independence_wave_plans\package_bindings\006_current_installed_map_package_bindings.csv:109`; `common\scripted_effects\006_independence_wave_package_region_effects_registry.txt:2360-2367` reserves the anchor and `:2423-2432` includes IW-108 in the region candidate list. | PARTIAL. Installed state/map evidence exists, but there is no Event 006 transaction, capital setter, extension policy, host-remnant receipt, or rollback path for IW-108. A direct allocation probe returned `MAP_STATE_ID_COLLISION`; this was a tool-input collision and was not treated as a map rewrite or as proof of a map defect. |
| Historical identity, rights, and 1936 roster | The accepted research requires an exact Buganda identity, period royal/customary institution, provisional cabinet, and rights/autonomy treatment, with a sourced real male leader or authentic archival institution. Event 012 currently uses Daudi Cwa II and its Buganda package predicates. | BLOCKED. The Event 006 identity/rights packet is unresolved and would collide with Event 012's active identity and roster. No new leader or institutional body may be invented in this audit. |
| Flag family | Vanilla supplies only ideology-specific UGA flags under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\flags\UGA_*.tga`; no mod-owned UGA flag family exists under `gfx\flags\`. | BLOCKED. The accepted Buganda flag review remains open; Event 006 has no approved route-specific flag and cannot silently reuse an unresolved Event 012 or vanilla identity. |
| Politics, parties, and leader | Event 012 defines Buganda council, civic, and producer parties and the shared `africa_priority_buganda_sovereign` in `common\scripted_effects\012_africa_priority_member_character_effects.txt:111-118`, `:324-331`, and `:537-544`; the character is defined in `common\characters\012_africa_priority_member_characters.txt:71-78` and recruited for UGA in `history\general\012_africa_priority_member_character_recruitment.txt:26`. | BLOCKED for Event 006. The existing Event 012 ruler and party set are already owned and cannot be claimed by IW-108 without a parent-approved reconciliation of origin, rights, active-country ownership, and cleanup. |
| Starting problem and ideas | Event 012 owns `africa_priority_buganda_starting_problem` and `africa_priority_buganda_mature_compact` in `common\ideas\012_africa_priority_member_ideas.txt:64-69` and `:180-185`, with Buganda-specific modifiers and pictures. | BLOCKED. No Event 006-owned ideas or lifecycle exist, and promoting Event 012 ideas would duplicate ownership and risk applying them outside the accepted IW-108 setup. |
| Focus tree | Event 012's `africa_priority_member_focus_tree` is an eight-focus, tree-local clean tree with Buganda-aware AI and localisation. Event 006's `common\national_focus\006_independence_wave_focus.txt` contains no `iw108`, `iw_108`, or Buganda callback. | BLOCKED. The accepted Event 006 founding focus and route do not exist; adding or copying a tree is outside this bounded audit and would be a new route design. |
| Decisions and missions | Event 012 owns `africa_priority_buganda_advance_mechanic`, `africa_priority_buganda_reinforce_force`, and `africa_priority_buganda_post_settlement_action` in `common\decisions\012_africa_priority_member_decisions.txt:218-232`, `:481-496`, and `:747-761`. | BLOCKED. No Event 006 Buganda decision family, costs, state targets, activation, or cleanup exists. The Event 012 decisions cannot be reused as an Event 006 fallback. |
| Starting military and force identity | Vanilla UGA history `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\countries\UGA - Uganda.txt:1-90` has capital `548`, `infantry_weapons = 1`, and zero convoys, without a Buganda-specific 1936 OOB. Event 012 has its own force preparation and Buganda guard/transport branches. | BLOCKED. The accepted colonial-veteran/local-guard/lake-unit package has no Event 006 template, equipment, manpower, officer, or generation receipt. No force or balance patch is safe without an accepted source-backed setup. |
| Technology, industry, supply, and production | Vanilla UGA begins with `infantry_weapons = 1`, `set_convoys = 0`, state 548 infrastructure 2 and rubber 3, with no Event 006 production or supply contract. | PARTIAL/BLOCKED. The base is inspectable, but Event 006 does not define Buganda-specific technology, industry, rail, port, supply, fuel, trains, or production setup. |
| AI and playability | Event 006 has no IW-108 AI profile, focus callback, decision weights, or strategy factors. The callable tool inventory has no `chaosx_ai_probability_auditor`. Source-only discovery found Event 012 focus and decision pools, not an Event 006 IW-108 pool. | BLOCKED. The mandatory named auditor route is unavailable, so no quantitative AI/probability claim or weighted patch was made. Event 012 weights do not establish Event 006 playability. |
| Lifecycle and cleanup | Event 012 owns UGA setup and `africa_priority_member_cleanup_runtime` in `common\scripted_effects\012_africa_priority_member_effects.txt:2331-2361`, retaining its own lifetime proof while clearing active state. Event 006 has no `iw_108` Join or cleanup branch. | BLOCKED. No Event 006 create/transfer/annex/puppet/cleanup/rollback contract exists, and calling Event 012 cleanup would be an ownership violation. |
| Runtime adapter and publisher | Event 006 loader/planner/reservation metadata exists in `common\scripted_effects\006_independence_wave_package_region_effects_registry.txt:2138-2153`, `:2268-2277`, and `:2360-2367`; `can_plan_independence_wave_package_iw_108` is in `common\scripted_triggers\006_independence_wave_package_region_triggers_registry.txt:807-814`. | BLOCKED. `has_independence_wave_runtime_package_adapter_for_execution_id` in `common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt:10-62` has no IW-108 branch, and there is no IW-108 adapter in `common\scripted_effects\006_independence_wave_effects.txt`. |
| Attestation, SCN-008, and Join | Event 006 content attestation in `common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt:159-190` currently covers 32 packages and omits IW-108; the SCN-008 rank/ledger remains dormant metadata, and `common\scripted_effects\006_independence_wave_join_effects.txt` has no `iw_108` reference. | BLOCKED. IW-108 must not be added to the central OR-lists, SCN-008 admission, or Join until the complete package contract and owner reconciliation are accepted. |
| Localisation and assets | Event 012 has Buganda leader, party, focus, idea, and decision strings in `localisation\english\012_africa_priority_member_characters_l_english.yml` and `localisation\english\012_africa_priority_member_focus_l_english.yml`. Event 006 has no IW-108 package-local localisation or asset manifest. | BLOCKED. Existing Event 012 strings are not Event 006 coverage; no generic copy or unreviewed flag/portrait is permitted. |
| GUI | No Buganda-owned scripted GUI was found; Event 012 uses ordinary decision/event surfaces, while shared Event 012 Charter/event-log/settings UI is outside the bounded package. | NOT APPLICABLE for this patch. No GUI rewrite or render was performed. |

## File-surface checklist and concrete findings

| File surface | Current identifiers/findings |
| --- | --- |
| Event 006 package registry | `common\scripted_effects\006_independence_wave_package_region_effects_registry.txt`: `independence_wave_load_package_iw_108`, reservation group `rg_great_lakes_coarse`, region `east_africa_horn_great_lakes`, anchor/compact state `548`, registered candidate tag `UGA`. This is planning metadata only. |
| Event 006 planner trigger | `common\scripted_triggers\006_independence_wave_package_region_triggers_registry.txt`: `can_plan_independence_wave_package_iw_108`. It checks availability and reservation state but does not create or configure Buganda. |
| Event 006 dispatch | `common\scripted_triggers\006_independence_wave_package_dispatch_triggers.txt`: no `iw_108` in runtime-adapter or content-attestation OR-lists. |
| Event 006 focus | `common\national_focus\006_independence_wave_focus.txt`: no `independence_wave_iw108_convene_buganda_settlement`, `iw108_*`, or Buganda callback. |
| Event 006 effects and Join | `common\scripted_effects\006_independence_wave_effects.txt` and `common\scripted_effects\006_independence_wave_join_effects.txt`: no IW-108 package adapter, Join identity, or cleanup branch. |
| Event 012 identity and lifecycle | `common\scripted_effects\012_africa_priority_member_effects.txt`: Buganda origin/package predicates and registration, starting ideas, force identity, route progression, and cleanup. These are the collision owner, not an Event 006 implementation. |
| Event 012 character and portrait | `common\characters\012_africa_priority_member_characters.txt`, `history\general\012_africa_priority_member_character_recruitment.txt`, and `interface\012_africa_priority_member_characters.gfx`: `africa_priority_buganda_sovereign` -> `portrait_012_africa_priority_buganda_sovereign_source_locked.dds`. The source-locked Daudi Cwa II material remains a user-review gate. |
| Event 012 decisions and ideas | `common\decisions\012_africa_priority_member_decisions.txt` and `common\ideas\012_africa_priority_member_ideas.txt`: Buganda mechanic, force, post-settlement decisions, starting problem, and mature compact. Do not duplicate or reassign these from this audit. |
| Vanilla tag/country/history | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\country_tags\00_countries.txt:147` maps `UGA` to `countries/Uganda.txt`; `common\countries\Uganda.txt` is a generic African country shell; `history\countries\UGA - Uganda.txt` has no Buganda-specific ruler/OOB. |
| Vanilla state/map | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\history\states\548-Uganda.txt`: state 548, owner/controller ENG, core UGA, capital VP `12989`, infrastructure 2, rubber 3, seven provinces, manpower 3,515,625, and no local supply stock. |
| Flags and portrait files | `gfx\flags\` has no mod-owned UGA family; vanilla UGA ideology flags are present. Event 012 source-locked and runtime Buganda portraits are both 131,168-byte DDS files with distinct hashes recorded in the 2026-08-27 handoff. |
| Documentation/ownership | `docs\events\012_africa\overview.md` and `docs\events\012_africa\portrait_runtime_gate.md` explicitly keep Event 012 independent of Event 006 and identify Buganda's source-locked placeholder/review state. |

## Map and state setup

The read-only map inspection found state 548 in the installed map and placed its provinces in the Lake Victoria strategic-region context, including province `12989` as the vanilla Kampala victory point. The rendered state view included coastlines, ports, victory points, resources, state buildings, supply nodes, and railways and passed the renderer's offline representation validation.

The selected state is not evidence of a playable Event 006 package. The map inspector still reported global positions/locators failures and truncated workspace diagnostics, including `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID`; these were not isolated to state 548 and no map write was attempted. No `hoi4.map_rewrite` dry-run, apply, post-validation, or rollback evidence exists because the package has no accepted map mutation and map writes remain parent scope.

The accepted reservation rule is one automatic package from `RG-GREAT-LAKES-COARSE` per wave, with host-protected-state handling. The current sources provide only reservation metadata and do not provide the Event 006 host-remnant, capital, transfer, claims, cores, rail, port, supply, or recovery transaction required to make the state safe.

## Politics, leader, portrait, flag, advisor, and party issues

The exact accepted identity is Buganda as a kingdom or constitutional state centered on Kampala/Buganda, not generic Uganda. The package calls for Kabaka, Lukiiko, customary/land institutions, a provisional cabinet, veterans, schools, labor, and an assembly with rights and autonomy routes. The current Event 012 ruler is Daudi Cwa II of Buganda, a real grounded male identity sourced from 1913 Jules Leclercq public-domain material, but the source-locked repaint and likeness/style crosswalk still require user review. The portrait worker has not supplied a reviewed Event 006 identity/rights packet, so no new portrait or character wiring is authorized.

Event 012 defines Buganda's council, civic, and producer party names against the same sovereign and owns their package predicates. Vanilla UGA has generic advisor records with missing-large-portrait TODOs and no Buganda-specific 1936 roster. Event 006 has no accepted party/advisor/leader path and no approved flag route; the existing vanilla ideology flags and Event 012 portrait cannot be reported as Event 006 asset coverage.

## Focus, decision, idea, and asset issues

The Event 012 focus render and inspection show an eight-focus `africa_priority_member_focus_tree` with tree-local diagnostic count zero and Buganda-aware route logic. The Event 006 focus render covers the large shared `independence_wave_focus_tree`, but its source has no IW-108 callback or founding focus. The Event 006 tree has one long-connector warning at `common\national_focus\006_independence_wave_focus.txt:742-760`; this is a shared-tree warning, not a Buganda package implementation.

Event 012's three Buganda-specific decisions and two Buganda ideas are already active consumers with their own triggers, costs, modifiers, icons, and cleanup. Event 006 lacks all accepted IW-108 project/settlement/delegation identifiers, localisation, icons, and lifecycle. A package-local tranche would therefore be a new route implementation and broad identity work, not a safe local repair.

## Starting military, technology, industry, supply, and production issues

The installed vanilla UGA start provides only state 548, infantry weapons level 1, zero convoys, and generic history setup. It has no verified Buganda force template, colonial veteran/local guard/lake-unit roster, equipment stockpile, manpower allocation, officer corps, production line, train/fuel/supply setup, naval or air setup, or source-backed 1936 technology package. Event 012's guard/transport setup is a separate owner and cannot be promoted as Event 006 content. No balance or starting-force patch was made.

The technology scan was run against vanilla `infantry_weapons` as an engine-facing reference, not as a Buganda package claim. No Event 006 technology dependency exists beyond the vanilla history entry.

## AI and playability issues

Event 006 contains no IW-108 AI strategy, focus selection callback, decision score, mission score, or weighted package profile. The required callable `chaosx_ai_probability_auditor` route is absent from the installed tool inventory, so the mandatory probability-owner pass cannot be completed. Read-only probability source discovery confirms Event 012's eight focus candidates and three Buganda decisions, but the Event 006 region source does not expose an IW-108 candidate pool for typed AI evaluation. No probability evaluate, compare, sweep, or balance claim was made.

Without an Event 006 force, route, admission, and cleanup contract, survival or role-playability cannot be asserted from the generic shared tree or Event 012 behavior.

## Read-only MCP evidence

The following artifacts are useful evidence for this re-audit; they are not write or admission receipts.

| Surface | Result and artifact |
| --- | --- |
| Event 012 trace | `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, workspace-wide trace deferred helper/lifecycle projections: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/06d539e92c5f5ddacbfb7e86db6cd80985a04857694f30c82491fc18443ffcea/60afc633eb6c3894687967a6ff476ec94ebb9e9577f0ead84e2ecf1ccba122f4/event-trace-18bf807c8be3.json`. |
| Event 006 trace | `EVENT_INSPECTED_PARTIAL`, same workspace-wide helper/lifecycle deferral: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93c904505cc4c7d73c71d656f305d5d3524a719f7bb8e11c72d34a9ec1cd64ac/1d24e2fe2c28a497693d79befa02af69c68f270f7c8d7a32c65365c7d36fb935/event-trace-18bf807c8be3.json`. |
| Event 012 options | `EVENT_RENDERED_PARTIAL`, same workspace-wide helper/lifecycle deferral: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd053d198ef30dfd6bc05bfff91ceba7a3a7c233de8b1772af99111b3c9f6998/34267d5d2c18260c4c1c5fdbd6ba382cf5abf7a5308cdb1a6defb70da7b24437/event-options-18bf807c8be3-manifest.json`. |
| Event 006 overview | `EVENT_RENDERED_PARTIAL`, same workspace-wide helper/lifecycle deferral: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d427cf01d5c548e9da8ffe91c5e249407e3acbb01bd2675245f4d51ad96d8324/f8d810a8c4251c37c574488c8ec6597d720366fc3a094ecce14b0492083d3cb5/event-overview-18bf807c8be3-manifest.json`. |
| Event 012 focus | `FOCUS_INSPECTED`, eight focuses, zero tree-local diagnostics: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/10b25000d140d9c6c3eb3d4f47a5b5ed813fc5ff0d214aa76d9d5274ab6b1ad4/bed5c85e49be50178b3e2e372de5dfe72ed392e27a04d016f4e70d09bddf0872/focus-inspect.62404ba8be479ff1.json`; rendered HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1bb907a6dd2dd46ca4fbb86574f02795a8e66e4639694317dcfe84bdcd52734/e465be7bd40a9fba0e1a5cbdf4e82084bbd6eb0ca4854fc8939d48e427ab404a/africa_priority_member_focus_tree.focus.html`. |
| Event 006 focus | `FOCUS_INSPECTED`, 184 focuses, one shared-tree long-connector warning; rendered HTML passed: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f834d949568cb0b86e4de4310656286aef043f5d962cb5f8420d1fb6b2f1add5/bc47456e55fe9dd1afd8818bd116ea42f878ef14d12e3b2360d231b68eb3b52a/independence_wave_focus_tree.focus.html`. |
| Technology reference | `TECH_INSPECTED` and `TECH_RENDERED` for vanilla `infantry_weapons`, with 1,427 workspace-wide blocking technology diagnostics and `sourceAccurate: false`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/676623e0a22a9494397003cd2217def8ec22bc012f959616d25a0a446518e88f/3255880f3b14568301fb24411b3f092139565edb597169716c96f9e04083c500/technology-scan-a1417861a875.json`. |
| Map state inspect | State 548 selected in installed map; global positions/locators diagnostics remain, with no state-specific rewrite: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f43aba7680af1ccaac2ae8a0d30193b708e80381aa88c073d46c962e6c4c34e5/84fcedc5c7bbecf116bbb6a1f14ca962e1e6287b24b51715e3f27027b1f616b4/map-inspect.9ecfc1f41da23dc6.json`. |
| Map state render | State-layer render with coastlines, ports, victory points, resources, buildings, supply nodes, and railways passed offline representation validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b11da464a58a00f392d20160c03b0af4a5e89f3dc88629a12e57291b26e12dba/292a62d38d1456175f46ae7f1ee0f94754253fc33c53f3c104dc8bf0c2bf27f3/map-state.png`. |
| Probability source | Event 006 registry discovery and candidate probe found no typed IW-108 AI pool; Event 012 focus and decision source pools were complete for their own consumers. The named `chaosx_ai_probability_auditor` callable is unavailable, so no evaluation artifact is claimed. |

The global focus inspector also reported an unrelated workspace syntax error at `game:common/national_focus/TSR_lingguang_incident_joint_branch.txt:469` (`SOURCE_UNEXPECTED_RIGHT_BRACE`), and the Event 006 tree has a long connector at `common\national_focus\006_independence_wave_focus.txt:742-760`. These diagnostics are recorded as workspace context and are not silently attributed to IW-108.

## Focused validators

Fresh current-checkout runs exited 0 for `python -B .tools\audit_event6_allocator.py`, `python -B .tools\audit_event6_country_api.py`, `python -B .tools\audit_event6_flags.py --strict`, and `python -B .tools\audit_event6_scenario_matrix.py`. They report the existing Event 006 allocator boundary, 242 broad tags with 191 resolved carriers and no missing/duplicate carriers, 102 complete Event 006 flag families, and a passing SCN-008 scenario matrix with 32 attested package cells and eight edge-case receipts. Earlier 2026-08-30 checks also passed `audit_event6_form16.py` and `audit_event6_gui_matrix.py`; no IW-108-specific validator exists.

These validators confirm that the shared admission boundary remains intact; they do not prove IW-108 package completeness.

## Changed files and before/after behavior

Changed file: `docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_iw108_buganda_country_package_reaudit_2026-09-02.md`.

No country, state, map, focus, decision, idea, character, portrait, flag, AI, adapter, attestation, SCN-008, Join, or cleanup source file was changed. No tag, state ID, leader ID, party ID, focus tree ID, localisation key, formable ID, or map allocation was changed.

Before and after behavior are intentionally identical: IW-108 remains dormant planning metadata, is not Event 006 runtime-adapter ready, is not content-attested, is not admitted to SCN-008, and has no Event 006 Join path. Event 012 remains the sole current UGA/Buganda gameplay owner.

## Skipped meaningful validation

No `hoi4.map_rewrite`, `hoi4.focus_rewrite`, event rewrite, or map apply was run because there is no accepted package-local mutation and map writes are parent scope. No GUI inspect/render was run because no IW-108-owned scripted GUI exists. The installed package exposes no Technology Tree Viewer, so technology-tree viewer evidence remains an unresolved limitation; the vanilla technology scan/render above is not a substitute for that missing viewer. No `chaosx_ai_probability_auditor` route is callable, so no mandatory probability compare/evaluate/sweep could be completed. The game was not launched and no user live-runtime validation is claimed.

## Next safe owner and admission order

1. Parent resolves the nonduplicating UGA/Event 012 ownership boundary, exact Buganda identity and 1936 role, host protection, rights/autonomy semantics, portrait provenance/likeness review, and accepted flag route.
2. Route the grounded leader/portrait work to `chaosx_portrait_creator` after the identity and rights packet is accepted; do not create an invented leader or opposite-gender pairing.
3. Parent implements and reviews the IW-108-specific force and starting setup, focus callback, projects, settlement decisions, ideas, localisation, AI profile, lifecycle/cleanup, adapter, attestation, SCN-008 publication, Join, and current-map package safety in that order.
4. Only after those receipts exist should central Event 006 admission be considered. Event 012 consumers must not be copied, widened, or reassigned without an explicit ownership reconciliation.

## Simplifications, omissions, and blockers

No fallback, generic content, Event 012 reuse, map write, admission, attestation, Join publication, or probability claim was made. The remaining blockers are the unresolved Event 012 ownership collision; missing Event 006 identity, rights, roster, flag, force, focus, decision, idea, localisation, AI, lifecycle, adapter, attestation, SCN-008, and Join surfaces; the unresolved source-locked Buganda portrait/flag review; absent `chaosx_ai_probability_auditor`; partial workspace-level Event MCP results; the unavailable Technology Tree Viewer; and global map/technology diagnostics. No new improvement plan was written because the accepted design and prior HOLD/NOT-PATCHABLE conclusion remain unchanged; this document is the dated no-change handoff.

No staging or commit was performed, preserving other agents' edits.

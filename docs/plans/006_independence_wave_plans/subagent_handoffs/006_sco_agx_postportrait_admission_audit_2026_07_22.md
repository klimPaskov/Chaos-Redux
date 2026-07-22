# IW-001 SCO / IW-007 AGX post-portrait country-package audit

Date: `2026-07-22`

Status: `static_package_audit_complete_runtime_admission_blocked_sco_identity_collision`

Scope: bounded country-package audit of Scotland (`SCO`, IW-001) and Frisia
(`AGX`, IW-007) against the accepted Event 006 country-package, map, focus,
decision, force, formable, localisation, AI, and sourced-portrait contracts.
Portrait masters, DDS files, manifests, sprite registrations, tag-audit files,
the consolidated Event 006 documentation, and the runtime content-attestation
gate were read-only surfaces for this audit. No portrait or manifest change was
made. No package was re-admitted.

Later visual correction: the user rejected the entire non-protected sourced
treatment family because it still reads as archival photography rather than
HOI4-painted portrait art. The source/ownership findings below remain valid, but
AGX is not visually ready: Kalma and Reenalda require identity-preserving
refinishing. Cunninghame Graham also requires refinishing, while Ironside still
requires a different sourced identity.

## Disposition

The mechanics and setup surfaces are present for both packages. AGX passes the
static package audit. SCO is mechanically covered but its selected commandant
identity is not portrait-admissible: vanilla England already owns and recruits
`ENG_edmund_ironside` at the 1936 start. The Event 006 sourced-person rule
requires an identity that is not already active elsewhere, so SCO remains
blocked until a different sourced male command identity and its corresponding
portrait are reviewed. A generated or generic replacement is not permitted.

Both packages remain blocked from automatic runtime execution and SCN-008. The
authoritative content attestation is deliberately empty:

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:42-44`

```text
has_independence_wave_runtime_package_content_attestation_for_execution_id = {
	always = no
}
```

Runtime and scenario preflight require that attestation. This handoff therefore
does not change the gate or re-admit either package.

| Package | Country | Static package audit | Portrait identity | Runtime / SCN-008 admission | Recommendation |
| --- | --- | --- | --- | --- | --- |
| IW-001 | `SCO`, Scotland | Mechanically covered | **Blocked**: active vanilla `ENG_edmund_ironside` collision | Blocked by empty attestation | Do not admit; replace the Ironside identity through the sourced-portrait workflow |
| IW-007 | `AGX`, Frisia | Pass | Pass: no exact active vanilla person collision found | Blocked by empty attestation | Do not admit until the parent changes the authoritative gate after all visual reviews |

## Country-package coverage checklist

| Surface | IW-001 SCO | IW-007 AGX | Evidence |
| --- | --- | --- | --- |
| Registered/reused tag identity | Pass | Pass | `common/country_tags/006_independence_wave_countries.txt:17` registers `AGX`; `SCO` is the accepted vanilla-tag reuse. Package predicates use exact original tags. |
| Package identity and setup precondition | Pass | Pass | `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt:8-43` and `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:14-65` require exact package IDs, NWE region, depth/archetype, anchor, capital, and living former host. |
| Anchor and host survival | Pass | Pass | IW-001 anchors state `121` and preserves host ENG state `126`; IW-007 anchors state `36` and preserves host HOL state `7`. Reservation and host-survival helpers trim only approved optional states. |
| Command roster | Pass mechanically; identity blocked | Pass | SCO roster/proof at `...scotland_wales_package_triggers.txt:46-49`; AGX roster/proof at `...wallonia_frisia_package_triggers.txt:72-75`. Both commandants are corps commanders. |
| Advisor roster | Pass | N/A by accepted Level-1 contract | SCO recruits the three NWE offices in `common/characters/006_independence_wave_nwe_advisors.txt:129-185`; AGX has no custom advisors, which is permitted for IW-007 and does not authorize advisor icons. |
| Politics and route government | Pass | Pass | SCO constitutional/popular/traditional/emergency route adapters; AGX constitutional/popular-council/patron adapters. AGX's cultural/labor council concept is represented by the existing `popular_council` engine route, not a new route family. |
| Starting ideas and lifecycle | Pass | Pass | `common/ideas/006_independence_wave_scotland_wales_ideas.txt` supplies SCO lifecycle/route ideas; `common/ideas/006_independence_wave_wallonia_frisia_ideas.txt` supplies AGX exposed-waterline, dike/coast-authority, and route ideas. |
| Decisions and mission | Pass | Pass | SCO has eleven package projects plus its state category; AGX has nine waterline projects plus the `independence_wave_agx_hold_the_waterline` mission and waterline category. |
| Focus assignment | Pass, plus bespoke Level-2 branch | Pass, accepted Level-1 shared framework | `independence_wave_assign_focus_framework` loads `independence_wave_focus_tree`; SCO adds five country focuses. AGX has no bespoke focus IDs by design; the accepted Level-1 contract is full shared survival framework + NWE overlay + package archetype/decisions. |
| Regional ambition and formables | Pass | Pass | SCO registers Celtic Cooperation (`FORM01`) and North Atlantic Compact (`FORM02`) candidates; AGX registers Low Countries Federation (`FORM03`) readiness and the North Sea coastal link. |
| Forces, technology, industry, supply | Pass | Pass | Dynamic force layer inherits former-host technology/slots, derives strength from map/host inputs, creates templates/divisions, and seeds equipment/convoys/fuel. SCO maps territorial-defense/tradition p1; AGX maps coastal-maritime/tradition p7. |
| AI and playability | Pass | Pass | `common/ai_strategy/006_independence_wave_scotland_wales.txt` and `...wallonia_frisia.txt` contain package/setup-gated survival, restraint, host-threat, and route profiles with abort conditions. |
| Localisation | Pass | Pass | English country, party, leader, idea, decision/mission, category, effect-tooltip, and SCO bespoke-focus keys are present. The two package localisation files are UTF-8 with BOM. |
| Cleanup and rollback | Pass | Pass | Package cleanup effects remove package decisions, ideas, flags, variables, AI/setup state, and formable/runtime markers without touching the shared attestation. |

## File-surface checklist

The following sources were read and cross-checked. No gameplay source file was
changed.

- `common/country_tags/006_independence_wave_countries.txt` and `common/countries/006_independence_wave_AGX.txt` — AGX tag registration and country definition; SCO continues the vanilla registered-tag path.
- `history/countries/AGX - Frisia.txt` and vanilla `history/countries/SCO - Scotland.txt` — dormant/start history, baseline ideas/technology, capitals, and character recruitment.
- `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt` — IW-001 identity, command/advisor roster, waterline/pressure proof, routes, formables, lifecycle, force, AI, prepared, and complete proofs.
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt` — IW-007 identity, anchor/host, command roster, waterline, route, FORM-03, lifecycle, force, AI, prepared, and complete proofs.
- `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt` — SCO characters, politics, route settlements, founding pressure, full focus assignment, dynamic force/AI hooks, focus callbacks, and cleanup.
- `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt` — AGX politics, waterline initialization, route settlements, full focus assignment, force/AI hooks, FORM-03 readiness, and cleanup.
- `common/characters/006_independence_wave_wallonia_frisia_characters.txt` and `common/characters/006_independence_wave_nwe_advisors.txt` — AGX sourced character roles and SCO asset-neutral advisor offices.
- `common/decisions/006_independence_wave_scotland_wales_decisions.txt`, `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`, and their category files — project actions, route actions, waterline mission/category, cancellation, costs, and tooltips.
- `common/ideas/006_independence_wave_scotland_wales_ideas.txt` and `common/ideas/006_independence_wave_wallonia_frisia_ideas.txt` — lifecycle, route, allowed scopes, modifiers, and icons.
- `common/national_focus/006_independence_wave_focus.txt` and `common/scripted_effects/006_independence_wave_focus_effects.txt` — shared framework and the five SCO Level-2 focus IDs.
- `common/ai_strategy/006_independence_wave_scotland_wales.txt` and `common/ai_strategy/006_independence_wave_wallonia_frisia.txt` — package-gated survival and route behavior.
- `common/scripted_effects/006_independence_wave_force_effects.txt`, `common/scripted_triggers/006_independence_wave_force_triggers.txt`, and the force constants/mapping files — host-inherited technology/slots, dynamic budgets/templates/stockpiles, and profile p1/p7 application.
- `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` — IW-001/IW-007 loader, automatic-ready, runtime/scenario preflight, capacity, and fail-closed attestation.
- `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt`, `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`, `common/scripted_triggers/006_independence_wave_form03_triggers.txt`, and `common/scripted_effects/006_independence_wave_form03_effects.txt` — Celtic/North Atlantic and Low Countries readiness, carrier/anchor, integration, autonomous-member, and cleanup contracts.
- `interface/006_independence_wave_region_01_portraits.gfx` and `gfx/leaders/006_independence_wave/` — four exact full-portrait consumers were verified read-only; no `_small` or dossier consumer exists.
- `localisation/english/006_independence_wave_scotland_wales_l_english.yml`, `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`, and `localisation/english/006_independence_wave_countries_l_english.yml` — country, party, leader, idea, decision/mission, category, effect, and focus text.
- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `.../spec_part_4_focus_tree_architecture.md`, `.../matrices/006_candidate_country_registry.csv`, and `.../research/006_package_research_resolution.csv` — accepted level, focus, identity, map, and source contracts.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, `006_current_map_reservation_groups.csv`, and `006_current_map_state_collisions.csv` — installed state ownership, reservation groups, and Event 005 collision evidence.
- Vanilla references: `history/states/121-Scottish Lowlands.txt`, `120-Scottish Highlands.txt`, `133-Strathclyde.txt`, `36-Friesland.txt`; vanilla `common/characters/SCO.txt`, `common/characters/ENG.txt`; vanilla `history/countries/ENG - Britain.txt`; and vanilla state/tag/flag registrations.

## Missing or stale country-package surfaces

- **SCO sourced-person blocker:** `localisation/english/006_independence_wave_scotland_wales_l_english.yml:3` presents `SCO_independence_wave_territorial_commandant` as Edmund Ironside, while vanilla defines `ENG_edmund_ironside` at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/ENG.txt:1297-1310` and recruits it for active ENG at `.../history/countries/ENG - Britain.txt:667`. The same person is therefore active in the host's vanilla character roster. Do not clear this by changing only the localisation or by reusing the same portrait; source a different male command identity and replace the portrait through the parent-owned asset workflow.
- **SCO other identity check:** no exact `Cunninghame Graham` token or literal full-name hit was found in vanilla character definitions, country histories, or localisation. Generic `Graham` name-pool entries are not an active-person collision. `SCO_independence_wave_civic_convention` remains mechanically/source covered pending the Ironside replacement.
- **AGX identity checks:** no exact `Douwe Kalma` or `Pieter Reenalda` token or literal full-name hit was found in vanilla character definitions, country histories, or localisation. Both AGX character tokens are male, sourced, and package-owned. `AGX_friesland_coastal_commander` is intentionally army/corps-command only; it does not need a civilian country-leader role.
- **AGX no advisor art:** IW-007's Level-1 contract has no custom advisor roster requirement. Its absence is intentional, and no advisor icon, dossier portrait, or `_small` asset may be invented for this audit.
- **AGX no bespoke focus IDs:** the registry marks IW-007 Level 1. Its full shared focus framework, NWE overlay, archetype decisions, waterline problem, sourced leaders, and FORM-03 angle satisfy the accepted minimum. This is an intentional Level-1 scope decision, not a missing-tree defect.
- **Stale shared comment:** `common/scripted_triggers/006_independence_wave_package_triggers.txt:139` describes AFX/AGX as admitted through exact content attestations, but the authoritative dispatch trigger remains `always = no`. The comment is contradictory documentation; it was not patched because the shared dispatch/gate surface is outside this bounded package audit.

## Map and state setup

- IW-001 uses the compact anchor state `121` (Scottish Lowlands), with approved optional/extended states `120` (Scottish Highlands) and `133` (Strathclyde) in `RG-121-120-133`; the package capital remains state `121`. Vanilla state history provides SCO/ENG cores, ports, dockyards, airbases, infrastructure, resources, VPs, and supply-relevant data. Host ENG retains protected state `126` under the binding and host-survival ceiling.
- IW-007 uses compact anchor state `36` (Friesland) in `RG-36`, capital state `36`. Vanilla state history supplies HOL ownership/core, the port/naval base, city/VP, industry, manpower, infrastructure, and local supply. Host HOL retains protected state `7`.
- `006_current_map_state_collisions.csv` contains no SCO/AGX collision row. Loader effects use exact IW-001/IW-007 IDs, region NWE, archetype `port_or_island`, anchors `121`/`36`, and former hosts ENG/HOL. Event 005 helpers reject opening-core/base-republic collisions and package-group duplicates.
- No map rewrite is proposed. A live map/MCP renderer was not available in this subagent, so this is source/binding evidence rather than an in-game map-render claim.

## Politics, leaders, portraits, flags, advisors, and parties

- SCO setup creates the civic convention and territorial commandant characters with explicit male metadata. The civic convention is promoted across centrism/socialism/oligarchism route settlements; the commandant takes the despotism emergency route and corps-command role. Three SCO advisor offices have traits, costs, availability, and AI hooks but no custom portrait assets.
- AGX recruits `AGX_friesland_coastal_council` (`Douwe Kalma`) and `AGX_friesland_coastal_commander` (`Pieter Reenalda`) from `history/countries/AGX - Frisia.txt:17-18`. Both are explicit male sourced identities; the commander is army/corps-command only. AGX politics cover constitutional, popular-council/labor, and patron-harbor settlements.
- The exact full portrait consumer set is limited to `GFX_portrait_AGX_friesland_coastal_council`, `GFX_portrait_AGX_friesland_coastal_commander`, `GFX_portrait_SCO_independence_wave_civic_convention`, and `GFX_portrait_SCO_independence_wave_territorial_commandant` in `interface/006_independence_wave_region_01_portraits.gfx`. No Event 006 advisor, dossier, or `_small` consumer remains.
- AGX has its own normal/medium/small flag triplets (`gfx/flags/AGX.tga`, `gfx/flags/medium/AGX.tga`, `gfx/flags/small/AGX.tga`). SCO correctly reuses the vanilla registered-tag flag triplets; no flag overwrite is required.
- Party names, country/adjective variants, leader names, route names, ideas, and advisor offices are localized. No opposite-gender metadata or name-pool pairing was found.

## Focus, decision, idea, and asset surfaces

- SCO has five bespoke Level-2 focuses: `independence_wave_sco_reconnect_central_belt_focus`, `independence_wave_sco_charter_north_atlantic_shipping_focus`, `independence_wave_sco_settle_crown_and_convention_focus`, `independence_wave_sco_convene_celtic_maritime_conference_focus`, and `independence_wave_sco_found_north_atlantic_state_service_focus` (`common/national_focus/006_independence_wave_focus.txt:1971-2033`). Prerequisites, route/network locks, AI weights, completion callbacks, icons, and localisation are present.
- SCO's eleven active projects are `reconnect_central_belt`, `organize_firth_convoys`, `settle_british_asset_ledgers`, `unify_territorial_command`, `ratify_constitutional_convention`, `charter_workers_commonwealth`, `settle_crown_and_convention`, `establish_emergency_directorate`, `choose_celtic_cooperation`, `choose_north_atlantic_compact`, and `convene_maritime_conference`. Its lifecycle ideas are `sco_divided_coastal_command` and `sco_north_atlantic_state_service`; route ideas/localisation are present.
- AGX has nine active waterline projects: `inspect_pump_stations`, `organize_harbor_watch`, `secure_inland_rail_link`, `train_dike_guards`, `reconcile_water_board_records`, `form_constitutional_water_board`, `ratify_coastal_labor_councils`, `install_patron_harbor_mandate`, and `convene_north_sea_coastal_conference`. `independence_wave_agx_hold_the_waterline` is the hidden mission/action. Lifecycle ideas are `agx_exposed_waterline` and `agx_dike_and_coast_authority`; route ideas/localisation are present.
- AGX receives the shared full focus framework and NWE overlay through `independence_wave_assign_focus_framework`; no AGX-specific focus block is required by its accepted Level-1 contract. No generated or generic visual fallback was introduced.

## Starting military, technology, industry, supply, and production

- Both packages intentionally avoid bespoke country-history OOBs and hardcoded major production. `006_independence_wave_force_effects.txt` derives the opening budget from host divisions, manpower, factories, infrastructure, rail/ports, supply, and host-war state; it inherits former-host opening technology and research/industrial slots, defines a bounded template, creates divisions, and adds equipment, trains, convoys, and fuel.
- IW-001 loads the territorial-defense/tradition p1 force mapping; IW-007 loads coastal-maritime/tradition p7. Force trigger proofs require the exact package profile, command roster, host event target, generation, and duplicate-application guard.
- Vanilla map history supports the intended starts: Scotland's anchor/extension includes ports, dockyards, airbases, infrastructure, Scottish cores, and local resources; Friesland's anchor includes a port/naval base, industry, city/VP, manpower, infrastructure, and local supply. No balance expansion or force shortcut was added.

## AI, diplomacy, formables, host relations, Event 005, and SCN-008

- SCO AI profiles cover maritime survival, founding restraint, former-host threat, constitutional state policy, labor state policy, traditional state policy, and emergency state policy. AGX profiles cover coastal survival, founding restraint, former-host threat, and civic coastal policy. All are package/setup gated and abort when disabled.
- Former-host negotiations, guarded-frontier/association routes, capital-control cancellation, project cancellation, subject/war cleanup, and network membership are wired through shared decisions and package cleanup. AGX's reclamation route is intentionally excluded by its prepared proof; SCO enables its four accepted host routes.
- FORM-01/FORM-02 readiness and integration require SCO state `121`, the correct family/candidate flags, connected members, and strict anchor/identity checks. FORM-03 readiness and integration require AGX state `36`, Low Countries Federation family, the readiness attestation/progression, North Sea link, consent, and connected members. No formable package grants extra territory outside its contract.
- Event 005 capacity/collision helpers reject SCO/AGX opening-core/base-republic conflicts, exact anchor/host overlaps, and reservation-group duplicates. Scenario and runtime preflight recognise exact package IDs/tags but stop at the empty attestation.

## Meaningful validation evidence

- The installed vanilla scan found an exact active-person collision only for SCO's selected Ironside identity: `common/characters/ENG.txt:1297-1310` defines `ENG_edmund_ironside`; `history/countries/ENG - Britain.txt:667` recruits it for ENG; English localisation resolves it as `Edmund Ironside` (`localisation/english/ideas_l_english.yml:278`). No exact vanilla character/history/localisation hit was found for `Cunninghame Graham`, `Douwe Kalma`, or `Pieter Reenalda`.
- Mechanical localisation check: all eleven SCO project IDs, all nine AGX project IDs, the AGX waterline mission/category, and the SCO state category have matching English localisation; the SCO bespoke five-focus IDs have title, description, and tooltip keys. Both package localisation files report UTF-8 BOM.
- Exact portrait-consumer search found four full portrait sprite consumers and zero Event 006 `_small`/dossier/advisor portrait consumers. Character, effect, trigger, and history recruitment tokens agree for AGX; SCO command/advisor tokens agree mechanically, subject to the Ironside identity blocker.
- Package IDs/tags/anchors, force mappings, route flags, formable flags, cleanup markers, map reservation groups, and Event 005 exclusions were cross-checked against the accepted registry and package binding tables.
- Offline Paradox wiki core pages and the country/focus/decision/idea/AI pages were consulted together with the required vanilla documentation and vanilla country/state/character precedents.
- No live HOI4 load, save test, MCP render, or installed Technology Tree Viewer validation was available. The installed package exposes no Technology Tree Viewer; that remains an unresolved limitation and is not a claim of runtime readiness.

## Changed files and identifiers

Changed files: **only this handoff**. No gameplay, localisation, interface, GFX, manifest, spec, resume-packet, map, or tag-audit file was changed.

Identifiers checked: package IDs `IW-001`, `IW-007`; tags `SCO`, `AGX`; anchors `121`, `120`, `133`, `36`; reservation groups `RG-121-120-133`, `RG-36`; hosts ENG/HOL; leaders `SCO_independence_wave_civic_convention`, `SCO_independence_wave_territorial_commandant`, `AGX_friesland_coastal_council`, `AGX_friesland_coastal_commander`; vanilla collision token `ENG_edmund_ironside`; FORM-01/02/03 candidate/readiness flags; SCO force profile p1 and AGX profile p7.

## Blockers, uncertainty, and follow-up

1. **Authoritative admission blocker:** `has_independence_wave_runtime_package_content_attestation_for_execution_id` is intentionally `always = no`; runtime and SCN-008 preflight cannot execute either package. Do not change it as part of this audit.
2. **SCO identity blocker:** Edmund Ironside is already an active vanilla ENG character/advisor at the campaign start. The parent must select and source a different real male command identity, wire its reviewed portrait, and rerun the sourced-person audit before SCO can portrait-pass. No localisation-only rename, generated portrait, generic portrait, or fallback is allowed.
3. **Documentation contradiction:** the stale shared comment claiming AFX/AGX are admitted through exact attestations remains unresolved outside this scope; the authoritative gate still wins.
4. **Intentional Level-1 scope:** AGX's lack of a bespoke focus branch and custom advisor art is accepted by the registry/spec and is not a simplification requiring a fallback.
5. **Validation boundary:** no live runtime or Technology Tree Viewer proof was available; parent should perform the normal live-load and SCN-008 preflight after the identity and attestation gates are resolved.

Simplifications/omissions: no gameplay fallback or visual substitute was used. AGX remains statically complete under its Level-1 contract; SCO remains incomplete for portrait admission solely because of the active vanilla Ironside identity collision. Neither package was re-admitted.

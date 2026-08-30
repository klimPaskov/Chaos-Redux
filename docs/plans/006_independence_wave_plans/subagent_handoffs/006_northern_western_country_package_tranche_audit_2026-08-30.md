# Event 006 Northern/Western Europe country-package tranche audit

Date: 2026-08-30

Disposition: no gameplay patch. The nine requested packages have package-local source contracts and current static bindings. The remaining gaps are runtime, MCP, or whole-event evidence gaps, so changing country gameplay here would be unsafe and outside this bounded tranche.

## Scope and authority

Audited IW-001 Scotland, IW-002 Wales, IW-004 Brittany, IW-006 Wallonia, IW-007 Frisia, IW-008 Rhineland, IW-009 Bavaria, IW-010 Saar, and IW-012 Iceland against `docs/specs/006_independence_wave_specs/`, `docs/events/006_independence_wave/`, the current package-binding and reservation-group CSVs, the existing package handoffs, the offline Paradox wiki pages, and the installed vanilla country/history/character/focus/documentation files.

The relevant regional overlay is Northern/Western Europe. Current reservation groups are RG-121-120-133, RG-122, RG-14, RG-34, RG-36, RG-RHINE-SAAR, RG-52-53-54, and RG-100. All nine IDs appear in the current runtime content-attestation dispatch registry.

## Country package coverage checklist

| ID | Tag | Depth / archetype | Anchor and reservation | Static package evidence | Disposition |
| --- | --- | --- | --- | --- | --- |
| IW-001 | SCO | regional / port_or_island | State 121, extension 120/133; RG-121-120-133 | `is_independence_wave_sco_package`, `can_initialize_independence_wave_iw_001_package`, roster/advisor and prepared-package triggers | Present; no safe patch |
| IW-002 | WLS | regional / mountain_or_frontier | State 122; RG-122 | `is_independence_wave_wls_package`, `can_initialize_independence_wave_iw_002_package`, roster/advisor and prepared-package triggers | Present; no safe patch |
| IW-004 | BRI | regional / port_or_island | State 14; RG-14 | `is_independence_wave_bri_package`, `can_initialize_independence_wave_iw_004_package`, roster/advisor and prepared-package triggers | Present; no safe patch |
| IW-006 | AFX | regional / industrial_breakaway | State 34; RG-34 | `is_independence_wave_afx_package`, `can_initialize_independence_wave_iw_006_package`, roster/advisor and prepared-package triggers | Present; no safe patch |
| IW-007 | AGX | standard / port_or_island | State 36; RG-36 | `is_independence_wave_agx_package`, `can_initialize_independence_wave_iw_007_package`, roster/advisor and prepared-package triggers | Present; no safe patch |
| IW-008 | RHI | regional / industrial_breakaway | State 51, optional state 42; RG-RHINE-SAAR | `is_independence_wave_rhi_package`, `can_initialize_independence_wave_iw_008_package`, roster/advisor and prepared-package triggers | Present; no safe patch |
| IW-009 | BAY | regional / agrarian_regional | States 52/53/54; RG-52-53-54 | `is_independence_wave_bay_package`, `can_initialize_independence_wave_iw_009_package`, roster/advisor and prepared-package triggers | Present; no safe patch |
| IW-010 | AJX | regional / industrial_breakaway | State 42; RG-RHINE-SAAR | `is_independence_wave_ajx_package`, `can_initialize_independence_wave_iw_010_package`, roster/advisor and prepared-package triggers | Present; no safe patch |
| IW-012 | ICE | standard / port_or_island | State 100; RG-100 | `is_independence_wave_ice_package`, `can_initialize_independence_wave_iw_012_package`, vanilla `iceland_tree`, roster and prepared-package triggers | Present; no safe patch |

## File surface checklist

The inspected source surfaces are:

- Registration and country shells: `common/country_tags/006_independence_wave_countries.txt`, `common/countries/006_independence_wave_AFX.txt`, `common/countries/006_independence_wave_AGX.txt`, and `common/countries/006_independence_wave_AJX.txt`.
- Reused vanilla country/history surfaces: SCO, WLS, BRI, RHI, BAY, and ICE; new AFX/AGX/AJX history files are `history/countries/AFX - Wallonia.txt`, `history/countries/AGX - Frisia.txt`, and `history/countries/AJX - Saar.txt`.
- Package effects and triggers: `common/scripted_effects/006_independence_wave_effects.txt`, `common/scripted_effects/006_independence_wave_western_package_effects.txt`, `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt`, `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt`, `common/scripted_triggers/006_independence_wave_rhineland_bavaria_saar_package_triggers.txt`, and `common/scripted_triggers/006_independence_wave_western_package_triggers.txt`.
- Dispatch and force contracts: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt`, and the corresponding force-package effects and constants.
- Focus and decision surfaces: `common/national_focus/006_independence_wave_focus.txt`, vanilla snapshot `common/national_focus/iceland.txt`, and the Scotland/Wales, Wallonia/Frisia, Rhineland/Bavaria/Saar, and Western decision files under `common/decisions/`.
- Character and setup surfaces: `common/characters/006_independence_wave_characters_registry.txt` and `history/general/006_independence_wave_character_recruitment_registry.txt`.
- AI, ideas, localisation, and assets: `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, the Event 006 idea files, `localisation/english/006_independence_wave_*`, and the existing Event 006 flag/portrait/focus/idea assets and manifests.

No missing package-local registration, focus loading, party/name key, leader/advisor roster, flag, or existing-asset wiring defect was evidenced in this tranche.

## Map and state setup

The installed binding CSV confirms state ownership/host expectations: Scotland 121 with 120/133 extension, Wales 122, Brittany 14, Wallonia 34, Frisia 36, Rhineland 51 with Saar's 42 pair constraint, Bavaria 52/53/54, Saar 42, and Iceland 100. Package triggers require the anchor to be owned and controlled by the initializing country and to be the country capital, with former-host guards where applicable.

The read-only `hoi4.map_inspect` pass covered states 14, 34, 36, 42, 51, 52, 53, 54, 100, 120, 121, 122, and 133. State/region membership and network/adjacency checks passed for the inspected package anchors. The aggregate report retained unrelated global diagnostics (`MAP_PORT_ADJACENT_SEA_INVALID`, `MAP_BUILDING_POSITION_INVALID`, and an unrelated localisation BOM issue) and therefore is not evidence for a package-local map repair. No map rewrite or allocation was performed.

## Politics, leaders, portraits, flags, advisors, and parties

The package-local triggers require the intended civic/institutional leader and corps-commander roster for each new or reused package. Existing handoffs and the package docs provide grounded real-male identity/source evidence for the NWE leaders and commanders; ICE reuses vanilla characters and portraits. No female leader/commander or opposite-gender portrait/name pairing was introduced. Existing Event 006 flag and portrait wiring is reused; ICE has no new asset requirement.

The sources already carry the package party/name and country/adjective localisation surfaces. No narrow correction was supportable without changing the accepted identity or portrait evidence boundary.

## Focus, decisions, ideas, and assets

The Event 006 focus tree contains the country branches for SCO, WLS, BRI, AFX, AGX, RHI, BAY, and AJX in `006_independence_wave_focus.txt`. The ICE package preserves vanilla `iceland_tree` and adds the Event 006 overlay plus four ICE route focuses in `common/national_focus/iceland.txt`. Package decisions, starting ideas, lifecycle flags, route gates, formable guards, and localisation are present in their package files and prepared-package triggers.

Read-only focus inspection of `independence_wave_focus_tree` returned 184 focuses and 195 connectors with zero layout/geometry diagnostics. Read-only render produced HTML/SVG/JSON artifacts. ICE inspection returned 89 focuses and 104 connectors, but reported seven blocking `FOCUS_GAMEPLAY_REFERENCE_MISSING` entries for vanilla character `idea_token` keys (`ICE_bjorn_thordharson`, `ICE_hermann_jonasson`, `ICE_isleifur_hognason`, `ICE_einar_olgeirsson`, `ICE_gisli_sigurbjornsson`, `ICE_brynjolfur_bjarnason`, and `ICE_werner_gerlach`). Each key exists in the installed vanilla `common/characters/ICE.txt`; the warning is an MCP cross-file resolution limitation against the intentionally preserved vanilla tree, not a basis for duplicate ideas or vanilla-tree edits.

The shared status GUI rendered successfully for the default scenario, but the required GUI inspect call timed out. Render diagnostics concern unshown shared states, static fallbacks for animated shared seals, and one legitimacy-icon clipping warning; none is a package-local NWE surface that can be safely corrected here.

## Military, technology, industry, supply, and production

The package triggers and force mappings already declare the requested role-specific profiles and military traditions: SCO p1 territorial defense, WLS p2 mountain frontier, BRI p4 coastal maritime, AFX p6 industrial security, AGX p7 coastal maritime, RHI p8 regular defectors, BAY p9 regular defectors, AJX p10 industrial security, and ICE p12 coastal maritime. Reinforcement, navy inheritance, and package-specific starting ideas are wired through the shared setup contracts. Existing vanilla histories remain authoritative for reused countries; no Event 006 custom technology tree is required or evidenced.

No fixed army, equipment, production, state building, supply, or technology patch was made because doing so would override the dynamic package setup and exceed the source-backed narrow-gap mandate.

## AI and playability

Package-specific AI strategy and focus/mission sources are present, including route and survival hooks. The required `chaosx_ai_probability_auditor` callable was not available in the installed tool set. Direct read-only probability source inspection found the relevant focus/mission candidates but returned incomplete pools (`poolComplete=false`, no available runtime candidates in the inspected source contexts); no evaluate or same-scenario compare was possible. Consequently this audit makes no quantitative AI-weight, MTTH, or balance claim, and no AI weight was changed.

Runtime release allocation, host-survival, save/load, formable-congress, and live AI behavior remain unverified. HOI4 was not launched, as required by the repository workflow.

## Evidence and tooling blockers

Useful read-only artifact references from this tranche:

- Event 006 focus inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f05c61919a44e55642f62da9c034825a9d907af8fa147f13cc088a03691ba494/4e690f62e7706fc3026ec0eb489566ff5edfd4d3eaf0d07f5516bb2ac99f72b8/focus-inspect.1a333b0aca6e74f2.json`.
- ICE focus inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/27265dd33696096e167ab03b6ff51601571f199d4d3257b7cffd9358a2dbf4a0/fbc857ff3c4abab6b7c32d7098eb15441c0cba058539c69a03e49c0526c041d0/focus-inspect.1a333b0aca6e74f2.json`.
- NWE map inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5f8b1db3271f185d5ba113325fadc01102de2019d769f875680fcafcbc4064a/4fe2c20e2c3a39b1c5252f571aa7778003ed2da6125631fa8586427801893afa/map-inspect.573b0c93f3557e0a.json`.
- NWE map render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd8b53eb2549add50b207cbe2fd618aafa44f6729a7363de31f02dba24b7b466/222dc8eb23b6da54fdd9b94af7c107d190035f17e7cac47017f1f9b88d00f2e/map-state.png`.
- Shared GUI render validation: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3f7ff7b4bfc368633fa7825c564573c341d972a9d836ac23c2bb2ef5a6b3ec3/independence_wave_status_window-validation.json`.
- Focus/mission probability source inspections were completed for the package source groups, but the required named auditor and compare route were unavailable.

Event inspection was partial because the workspace-wide graph deferred helpers/lifecycle analysis. Event render with the correct selector `selector:{kind:"event",eventId:"chaosx.nr006.1"}` timed out after 180 seconds. Technology inspection/render was blocked by `SCAN_BYTE_LIMIT`; the installed package exposes no Technology Tree Viewer. GUI inspect also timed out after 180 seconds. These are recorded limitations rather than grounds for gameplay changes.

## Simplifications, omissions, and blockers

No unapproved fallback, placeholder, identity redesign, generic replacement, or gameplay simplification was made. No gameplay or asset files were changed. The sole change from this tranche is this audit handoff. Runtime and weighted-probability evidence remains open for the parent integration pass, and the ICE vanilla `idea_token` cross-file diagnostics should remain tracked as an MCP resolution limitation unless a future tool update resolves them.

No additional plan handoff was written because the audit found no broad identity redesign or package implementation gap requiring a new plan.

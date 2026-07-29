# Event 006 IW-001/IW-002 Gameplay Handoff — 2026-07-15

## Scope

Implemented the bounded gameplay package pair for IW-001 Scotland (`SCO`) and IW-002 Wales (`WLS`). No commit was created. The package reuses vanilla registered tags and installed flags, uses the reviewed full Event 006 focus framework, and does not edit country history, state history, vanilla character files, vanilla flags, or `WLS_restore_y_wladfa_decision`.

## Files changed

Package-owned files added:

- `common/script_constants/006_independence_wave_scotland_wales_constants.txt`
- `common/ideas/006_independence_wave_scotland_wales_ideas.txt`
- `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt`
- `common/decisions/categories/006_independence_wave_scotland_wales_categories.txt`
- `common/decisions/006_independence_wave_scotland_wales_decisions.txt`
- `common/ai_strategy/006_independence_wave_scotland_wales.txt`
- `localisation/english/006_independence_wave_scotland_wales_l_english.yml`
- `docs/events/006_independence_wave/northern_western_europe_packages.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_sco_wls_gameplay_handoff_2026_07_15.md`

Shared files edited:

- `common/national_focus/006_independence_wave_focus.txt` — ten origin-gated package focuses.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` — Scotland/Wales setup, validation, and cleanup adapter calls.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` — IW-001/IW-002 adapter IDs and content-ready-gated dormant preflight branches.

## Runtime identifiers

### Package and proof triggers

- `is_independence_wave_sco_package`
- `is_independence_wave_wls_package`
- `can_initialize_independence_wave_iw_001_package`
- `can_initialize_independence_wave_iw_002_package`
- `has_independence_wave_sco_command_roster`
- `has_independence_wave_wls_command_roster`
- `has_stable_independence_wave_sco_state`
- `has_stable_independence_wave_wls_state`
- `has_prepared_independence_wave_iw_001_package_setup`
- `has_prepared_independence_wave_iw_002_package_setup`
- `has_complete_independence_wave_iw_001_package_setup`
- `has_complete_independence_wave_iw_002_package_setup`

### Setup and transaction effects

- `independence_wave_setup_iw_001_scotland`
- `independence_wave_setup_iw_002_wales`
- `independence_wave_dispatch_scotland_wales_package_setup`
- `independence_wave_dispatch_scotland_wales_package_final_validation`
- `independence_wave_dispatch_scotland_wales_package_cleanup`
- `independence_wave_validate_iw_001_scotland`
- `independence_wave_validate_iw_002_wales`
- `independence_wave_cleanup_iw_001_scotland`
- `independence_wave_cleanup_iw_002_wales`

### Guarded runtime characters

- `SCO_independence_wave_civic_convention`
- `SCO_independence_wave_territorial_commandant`
- `WLS_independence_wave_national_council`
- `WLS_independence_wave_mountain_commandant`

No explicit portrait block is wired to any generated character.

### Visible package values

- `independence_wave_sco_shipping_authority`
- `independence_wave_wls_north_south_integration`
- `independence_wave_wls_bilingual_service`

### Ideas

Scotland:

- `sco_divided_coastal_command`
- `sco_north_atlantic_state_service`
- `sco_constitutional_convention`
- `sco_workers_commonwealth_charter`
- `sco_crown_and_convention_settlement`
- `sco_emergency_territorial_directorate`

Wales:

- `wls_divided_valleys_administration`
- `wls_bilingual_coal_and_rail_compact`
- `wls_constitutional_national_council`
- `wls_workers_valleys_charter`
- `wls_cultural_guardians_settlement`
- `wls_emergency_mountain_directorate`

### Decisions

Scotland:

- `independence_wave_sco_reconnect_central_belt`
- `independence_wave_sco_organize_firth_convoys`
- `independence_wave_sco_settle_british_asset_ledgers`
- `independence_wave_sco_unify_territorial_command`
- `independence_wave_sco_ratify_constitutional_convention`
- `independence_wave_sco_charter_workers_commonwealth`
- `independence_wave_sco_settle_crown_and_convention`
- `independence_wave_sco_establish_emergency_directorate`
- `independence_wave_sco_choose_celtic_cooperation`
- `independence_wave_sco_choose_north_atlantic_compact`
- `independence_wave_sco_convene_maritime_conference`

Wales:

- `independence_wave_wls_reconnect_north_south_rail`
- `independence_wave_wls_settle_bilingual_services`
- `independence_wave_wls_guard_coalfield_corridors`
- `independence_wave_wls_settle_british_property_board`
- `independence_wave_wls_ratify_national_council`
- `independence_wave_wls_charter_workers_valleys`
- `independence_wave_wls_settle_cultural_guardians`
- `independence_wave_wls_establish_emergency_directorate`
- `independence_wave_wls_convene_celtic_council`

### Package focuses

Scotland:

- `independence_wave_sco_reconnect_central_belt_focus`
- `independence_wave_sco_charter_north_atlantic_shipping_focus`
- `independence_wave_sco_settle_crown_and_convention_focus`
- `independence_wave_sco_convene_celtic_maritime_conference_focus`
- `independence_wave_sco_found_north_atlantic_state_service_focus`

Wales:

- `independence_wave_wls_reconnect_north_and_south_focus`
- `independence_wave_wls_charter_coal_and_rail_focus`
- `independence_wave_wls_establish_bilingual_service_focus`
- `independence_wave_wls_secure_mountain_corridors_focus`
- `independence_wave_wls_convene_celtic_council_focus`

## Package behavior

IW-001 publishes full focus assignment, four accepted government routes, all four former-host routes, `traditional_authority_vs_assembly`, league access, FORM01 and FORM02 candidacy, the Celtic family as its initial selection, and a pre-discovery decision to select the North Atlantic family. Its exact force proof expects p1 territorial defense, tradition 68, and the existing package inheritance flags.

IW-002 publishes full focus assignment, the same four accepted government routes, all four former-host routes, `labor_councils_vs_ministries`, league access, and FORM01 Celtic candidacy. Its exact force proof expects p2 mountain frontier and tradition 58.

The shared full-framework tree retains all general statehood lanes. The added package branches make Scottish maritime authority and Welsh north-south/bilingual state construction visible and playable rather than relying on generic copied rewards.

## Preservation proof

- No `history/countries`, `common/countries`, `common/characters`, `gfx/flags`, `gfx/leaders`, or `interface` file was changed for this package.
- No package effect sets `independence_wave_package_content_ready`.
- No package effect assigns a portrait or alters an existing character.
- No package file references `WLS_restore_y_wladfa_decision`; the vanilla decision remains independently visible under its own rules.
- Setup requires the exact dormant tag and package ID and therefore cannot replace an already living Scotland or Wales.
- No broad daily, weekly, or monthly country iteration was added.

## Validation evidence

Completed source validation in the shared workspace:

- all package Clausewitz files and the edited full focus tree have balanced structural blocks;
- all 77 package calls to Event 006 scripted effects/triggers resolve to a defined identifier, with no duplicate Scotland/Wales top-level scripted identifiers;
- all 111 required package localisation keys are present exactly once, the file is UTF-8 with BOM, and no key uses `:0` or leading whitespace;
- all 20 package decisions have an explicit custom cost proof, payment effect, and centralized duration; all active projects are included in their package serialization trigger;
- all ten package focus IDs are unique, origin-gated, localized, and connected to a defined package callback;
- the exact source proofs retain IW-001 anchor 121, p1 territorial-defense profile, tradition 68, and IW-002 anchor 122, p2 mountain-frontier profile, tradition 58;
- the package source contains no readiness grant, explicit portrait assignment, state/country/history override, broad periodic country iteration, unsupported comparison operator, or scoped temporary-variable access;
- a repository search confirms `WLS_restore_y_wladfa_decision` remains owned only by vanilla `common/decisions/WLS.txt`; no gameplay package file references it; and
- `.tools/audit_event6_allocator.py` still passes all 149 publishers and the anchor/compact/extended reservation order after the shared dispatch registration.

The following runtime scenarios remain the parent/final package audit cases once approved visual content makes the packages allocatable:

1. IW-001 publishes SCO at state 121, creates one guarded civic institution and one corps commander, loads the full tree, applies p1 forces, shows Scottish pressures and decisions, and offers Celtic/North Atlantic family selection.
2. IW-002 publishes WLS at state 122, creates one guarded national council and one corps commander, loads the full tree, applies p2 forces, shows both Welsh pressures and decisions, and leaves `WLS_restore_y_wladfa_decision` governed solely by vanilla.
3. Re-running guarded roster preparation creates no duplicate character tokens.
4. Final setup proof fails if the anchor, tag, package ID, force mapping, roster, route matrix, AI flag, or array membership is incorrect.
5. Cleanup removes package decisions, ideas, values, route outcomes, ambitions, and setup flags without touching vanilla files or characters.

Balance review confirms that Scotland can cross its 65 Shipping Authority threshold through either its first three package projects or its five-focus branch. Wales can cross both 65 thresholds through its focus branch, or through its four founding projects while the living former-host settlement remains available. The four route settlements require shared 75/120-day light or standard commitments, core state projects take 75-180 days, and regional congresses take 300 days with the shared strategic cost. No project grants a free division or repeatable equipment reserve.

## Readiness and blockers

`independence_wave_package_content_ready` is intentionally absent for both tags. Runtime setup cannot execute through normal allocation until the content-ready gate is separately granted after the following blockers are resolved:

1. Scotland needs approved unique researched/HOI4-styled large and small visuals for its civic authority and territorial commander, with provenance and sprite wiring.
2. Wales needs approved unique researched/HOI4-styled large and small visuals for its national council and mountain commander, with provenance and sprite wiring.
3. Generic vanilla advisor portraits and engine-selected generated portraits are not accepted readiness proof.
4. No researched package-specific advisor board or advisor portrait set was delivered. Preserved vanilla generic advisors may remain supplementary appointments, but they cannot satisfy the package cabinet/command-art gate.
5. Scotland's installed Saltire family is accepted for civic reuse; no Lion Rampant variant is wired, and any later use must remain traditional-route-only. Wales's final asset audit must preserve the installed flag's explicit 1959-layout caveat; no invented 1936 fallback is authorized.
6. FORM01 Celtic Cooperation State and FORM02 North Atlantic Compact still lack family-specific consumers for the shared `independence_wave_formable_commit_pending` request.
7. The parent integration pass still needs to reconcile the package-specific regional conference decisions with the shared DM-54 active-formable-operation lock, then fold the accepted wording into `docs/events/006_independence_wave/overview.md` and the Event 006 matrices/spreadsheet surfaces before claiming whole-event completion.

No portrait or flag fallback was wired or accepted. Gameplay code is ready for parent review and merge, but package release readiness remains blocked by the listed asset, advisor, and shared formable-consumer work.

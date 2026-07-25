# IW-006 Wallonia post-wire country-package audit

Audit date: 2026-07-25

Scope: fresh post-wire audit of the Event 006 Wallonia package (IW-006, tag AFX) after the independently approved Louis Hubert baron Ruquoy/Rucquoy commander portrait promotion. This handoff is audit-only. No gameplay, asset, localisation, map, or source-of-truth files were patched by this subagent.

## Verdict

**PASS for the AFX runtime country-package surfaces, with one source-contract discrepancy and documentation/validation follow-up risks.** The package has a coherent registered tag, state-34 release anchor, politics and leader roster, dynamic starting-force contract, full focus assignment, bespoke decisions and incidents, lifecycle ideas, AI strategy, FORM-03 carrier registration, localisation, flags, focus/report art, and the promoted commander portrait. No live runtime surface was found that still points at the retired generated portrait or requires a missing commander-small/advisor/dossier derivative.

The parent may restore IW-006 to the exact Event 006 content-attestation set after reviewing this handoff. The documentation and validation risks below should be reconciled before treating the asset manifest as a clean evidence authority.

## Country-package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Tag registration and country definition | PASS | common/country_tags/006_independence_wave_countries.txt:16 maps AFX to countries/006_independence_wave_AFX.txt; common/countries/006_independence_wave_AFX.txt:1-11 supplies culture and colour. Installed-tag audit records zero Event 006 collisions. |
| Country history and opening ideas | PASS | history/countries/AFX - Wallonia.txt:1-18 recruits AFX_walloon_provisional_assembly and AFX_walloon_reserve_commander and keeps the shell intentionally runtime-initialised. It starts with civilian_economy, export_focus, and volunteer_only. |
| Anchor state, capital, controller, and former host | PASS | common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:69-82,273-280 binds IW-006 to state 34, reservation group RG-34, tag AFX, and the live owner as former host. common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:74-111 requires state 34 as the owned/controlled capital anchor and a surviving non-AFX former host. Frozen execution transfers the planned state owner and controller in common/scripted_effects/006_independence_wave_execution_effects.txt:268-300. |
| Cores and release safety | PASS | common/scripted_effects/006_independence_wave_execution_effects.txt:153-245 masks only unplanned historical cores, adds planned package cores, releases the fixed tag from the former host, then restores masked cores. FORM-03 explicitly forbids transferring or coring states 6, 7, 8, 35, 977, and 980 in common/scripted_effects/006_independence_wave_form03_effects.txt:1-11. |
| Politics, parties, and route governments | PASS | common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:197-214,271-325 initialise a democratic provisional authority and install mutually exclusive constitutional, labour, emergency-military, or patron governments with route-specific leaders and ideas. All AFX party keys are present in localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:8-24. |
| Leader roster and portrait metadata | PASS | common/characters/006_independence_wave_wallonia_frisia_characters.txt:37-65 defines male AFX_walloon_provisional_assembly and male AFX_walloon_reserve_commander; the latter has civilian and army portraits plus is_corps_commander coverage and no female metadata. history/countries/AFX - Wallonia.txt:18 recruits the stable commander token. |
| Focus tree assignment | PASS | common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:596-601 requests full_framework; common/scripted_effects/006_independence_wave_focus_effects.txt:29-46 loads independence_wave_focus_tree. The AFX Level 2 overlay is common/national_focus/006_independence_wave_focus.txt:2268-2449, with one root plus seven vertical Sambre-Meuse focuses. |
| Decision and mission family | PASS | common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:9-307 defines one founding mission, four industrial/host/security projects, four mutually exclusive government formalisation decisions, and the paid Meuse conference. Category visibility is origin-locked in common/decisions/categories/006_independence_wave_wallonia_frisia_categories.txt:7-10; cleanup removes every AFX decision and mission at common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:727-740. |
| Ideas and lifecycle | PASS | common/ideas/006_independence_wave_wallonia_frisia_ideas.txt:39-109 defines the disrupted belt, mature Sambre-Meuse covenant, and four route ideas. independence_wave_refresh_afx_industrial_lifecycle and independence_wave_remove_afx_package_ideas own replacement and cleanup in common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:1-150. |
| Incidents and event integration | PASS | events/006_independence_wave_wallonia_frisia.txt:12-183 contains chaosx.nr6.18, .19, and .20, each with AFX-specific triggers, two AI-weighted options, effect tooltips, and report art. Scheduler hooks are at common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:532-576. |
| FORM-03 regional leadership path | PASS | AFX registers the Low Countries family and candidate in common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:611-617. Exact AFX carrier/anchor and route checks are in common/scripted_triggers/006_independence_wave_form03_triggers.txt:15-71,202-228; readiness flags are set by common/scripted_effects/006_independence_wave_form03_effects.txt:14-25. Formation remains consent-, connection-, recognition-, and ratification-gated. |
| AI and playability | PASS | common/ai_strategy/006_independence_wave_wallonia_frisia.txt:9-76 supplies AFX survival, founding restraint, host-threat, emergency-command, and civic-industrial strategies. Decision AI weights use shared constants and react to continuity, host threat, and route choice. |

## File-surface checklist

| Surface | Files and identifiers checked | Result |
| --- | --- | --- |
| Registration | common/country_tags/006_independence_wave_countries.txt; common/countries/006_independence_wave_AFX.txt; history/countries/AFX - Wallonia.txt | PASS; no stale tag or filename reference. |
| Characters | common/characters/006_independence_wave_wallonia_frisia_characters.txt; AFX_walloon_provisional_assembly; AFX_walloon_reserve_commander | PASS; both male, institutional civic name plus sourced real commander, stable token retained. |
| Portrait GFX | interface/006_independence_wave_region_01_portraits.gfx:9-15; GFX_portrait_AFX_walloon_provisional_assembly; GFX_portrait_AFX_walloon_reserve_commander | PASS; both full-size DDS paths exist. No _small reference exists in live source. |
| Country and package localisation | localisation/english/006_independence_wave_countries_l_english.yml:21-35; localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:3-174 | PASS; country name/adjective, parties, leaders, ideas, decision text, incident text, focus names/descriptions/tooltips are covered. |
| Focus GFX | interface/006_independence_wave_wallonia_frisia_assets.gfx:9-25; eight GFX_goal_independence_wave_afx_* sprites | PASS; all eight focus DDS files exist. |
| Report/event GFX | interface/006_independence_wave_wallonia_frisia_assets.gfx:27-29; GFX_report_event_006_afx_industrial_authority, ...basin_government, ...meuse_ambition | PASS; all three report DDS files exist. |
| Flags | gfx/flags/AFX.tga, gfx/flags/medium/AFX.tga, gfx/flags/small/AFX.tga | PASS; Pillow reports 82x52, 41x26, and 10x7 RGBA triplets. Current authority docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md:5-17,29-45,156-165 records the 1913 Walloon coq hardi design and no flag-only blocker. |
| Advisors and derivatives | common/characters/006_independence_wave_nwe_advisors.txt; live common, history, interface, and gfx searches for AFX advisor/dossier/operative/_small/fallback | PASS by design; no advisor, operative, dossier portrait, commander-small, female, generic, or fallback surface is referenced or required. |

## Map and state setup findings

Vanilla C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/34-Wallonie.txt:1-43 confirms the anchor is state 34, initially owned/core to BEL, with Namur (3516), Liège (11519), Charleroi (9536), 22 steel, 5 coal, infrastructure 3, one arms factory, four industrial complexes, and one air base. The Event 006 loader intentionally treats this as the frozen Walloon industrial anchor rather than adding a mod state file.

The generic execution pass transfers every frozen state in the package plan to the released country and sets both owner and controller (common/scripted_effects/006_independence_wave_execution_effects.txt:268-300). AFX setup then requires the transferred state-34 anchor and capital, while the former host remains a live non-AFX country for ledger/host decisions. The current package reservation requests state 34 only, so there is no hidden compact or extended AFX territory claim in the package adapter.

The read-only hoi4.map_inspect call returned MAP_INSPECTED, but the workspace-wide map scan reported 2,654 omitted errors (building-position and floating-harbor diagnostics) unrelated to AFX and did not provide a clean bounded state record in the inline response. No map write was attempted. The source-level state and release checks above are therefore the authoritative AFX map evidence for this handoff; a clean map-wide validation remains unresolved outside this package scope.

## Politics, leader, portrait, flag, advisor, and party findings

- The provisional civic leader is the institutional/historical Jules Destrée token (AFX_walloon_provisional_assembly), while the emergency route promotes the male AFX_walloon_reserve_commander token to despotism. This preserves the male-only grounded-package rule and does not pair a female portrait/name with a male character or vice versa.
- The player-facing commander name is now Louis Hubert baron Ruquoy and the emergency decision text identifies the alternate-history role as a retired Hainaut-born general recalled to the Walloon reserve (localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4,90-91). The historical source audit records his retirement by 1927; the role must remain a reserve/senior-security appointment rather than a documented 1936 General Staff posting.
- The promoted runtime DDS gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds is byte-identical to the trial package DDS and decodes pixel-identically to the approved 156x210 candidate PNG. Candidate file SHA-256 is FAFFBFE12921431353C962215C04F8E69FF40B8CAA083C61FC8F46719A477EC0; candidate/runtime decoded RGBA SHA-256 is BEDF59BAA7F114D9446EE1AF9A5C245C44E78A3D68387EF615945E45BD115259; runtime DDS SHA-256 is 0AD247810F8E98AFADE0362CFAC275A68DB401DC4BEBF18B8343B8F77067DFFF.
- The three AFX flag ladders are present and match the current flag-only authority. No ideology or cosmetic flag variants are expected.
- There is no AFX advisor surface in the current package. This is consistent with the Event 006 asset coverage note that current Event 006 has no advisor/dossier/_small portrait assets.

## Focus, decision, idea, and asset findings

The eight AFX focuses form a complete Level 2 Sambre-Meuse route: independence_wave_afx_charter_sambre_meuse_authority_focus, independence_wave_afx_bind_mines_rails_furnaces_focus, independence_wave_afx_codify_basin_government_focus, independence_wave_afx_integrate_industrial_reserve_focus, independence_wave_afx_settle_industrial_succession_focus, independence_wave_afx_open_meuse_network_office_focus, independence_wave_afx_mandate_meuse_conference_focus, and independence_wave_afx_prepare_low_countries_dossier_focus (common/national_focus/006_independence_wave_focus.txt:2273-2448). Prerequisites, route/host/network availability, idempotent hidden rewards, AI weights, localisation, and icon registrations are present.

The AFX decision category has ten entries including the founding mission, with costs, timers, cancellation on capital loss/package loss, custom cost text, effect tooltips, and AI weights. The four government decisions are mutually exclusive through has_independence_wave_afx_route_government; the Meuse conference is gated behind continuity, recognition, network, government mandate, and a paid strategic project.

The idea lifecycle starts with afx_disrupted_industrial_belt, advances to afx_sambre_meuse_industrial_covenant at stable continuity, and swaps in one route idea (afx_constitutional_compact, afx_workers_industrial_charter, afx_emergency_works_command, or afx_patron_industrial_mandate). Cleanup removes every AFX idea and flag.

## Starting military, technology, industry, supply, and production findings

The force mapping matches the accepted IW-006 row in docs/plans/006_independence_wave_plans/006_force_package_mapping.csv for package iw_006, profile industrial_security, reinforcement mask 589, and no navy/air inheritance, but the accepted row specifies military tradition 61 while common/script_constants/006_independence_wave_force_package_constants.txt:297 sets runtime constant p6 to 60. common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:210 consumes that p6 constant, so the live AFX force validation and budget path use 60. This one-point source/spec discrepancy needs parent resolution; it is not silently changed by this audit. Mask 589 decodes to exactly five approved pathways: integrate_militias, secure_depots, convert_defectors, factory_rail_guards, and professional_officers.

common/scripted_effects/006_independence_wave_force_effects.txt:869-888 applies the generation-locked opening force only after a valid profile, tradition, command roster, five-pathway program, generation, anchor, and former-host checks. The industrial-security template at lines 495-521 contains infantry, artillery brigade, engineer support, and artillery support. Opening materialisation at lines 718-788 creates divisions at the anchor and adds infantry, support, conditional artillery, trains, trucks, convoys where applicable, and fuel. Lines 790-803 inherit former-host technology and enforce minimum/industrial research slots.

There are no static AFX production-line definitions in history/countries/AFX - Wallonia.txt; this is intentional for the shared dynamic force architecture. The vanilla anchor contributes its state buildings and the force allocator supplies generation-specific opening stockpiles and templates. If the design later requires an explicit starting production queue rather than this dynamic stockpile contract, that is a balance/design change outside this audit and should not be silently added.

## AI and playability findings

The survival strategy prioritises army, infantry/support/artillery/train production, arms factories, infrastructure, and switches to emergency army/bunker priorities under severe former-host threat. Founding restraint avoids wars while the package is fragile; the civic-industrial policy resumes restraint and industrial construction after a route government is installed. AFX decisions and incidents use shared AI constants with continuity, route, league, and threat modifiers.

The main playability caveat is historical role framing: Ruquoy is a retired real commander placed in an alternate-history Walloon reserve appointment. The second caveat is that the dynamic force package has no navy/air inheritance for this industrial-land profile, which matches the accepted mapping rather than a missing feature; the separate one-point military-tradition discrepancy is recorded below.

## Missing or stale surfaces and residual risks

1. Current portrait manifest token typo (documentation-only): docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wallonia_ruquoy_trial_01/manifest.md:14 calls the existing character AFX_independence_wave_walloon_reserve_commander, but the live token is AFX_walloon_reserve_commander in common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-62, history/countries/AFX - Wallonia.txt:18, and common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:68-69.
2. Current portrait manifest decoded-candidate hash mismatch (documentation-only): the same manifest reports 594904EE... at line 71, while independent reopening of the candidate PNG, final DDS, and runtime DDS produces BEDF59BA... for the decoded RGBA payload, with byte-identical final/runtime DDS and equal decoded pixels. The file SHA values remain consistent. The runtime asset is therefore verified, but the manifest evidence row should be corrected or explicitly annotated.
3. Superseded flag blocker wording: docs/plans/006_independence_wave_plans/asset_research/006_generated_flag_blockers.md:13 still lists IW-006 Wallonia as blocked, while the current flag-only authority docs/assets/006_independence_wave/northern_western_europe_generated_art_manifest.md:5-17,29-45,156-165 records the AFX triplet as complete and reports no flag-only blocker. This is a stale documentation surface, not a missing runtime flag.
4. Historical handoff references: older portrait handoffs under docs/plans/006_independence_wave_plans/subagent_handoffs/ mention the retired Marcel Delcourt identity, a generated commander, or a historical _small derivative. Live source searches found none of those consumers. They should remain clearly historical/superseded or be curated later; they do not block the current AFX package.
5. IW-006 force tradition source/spec discrepancy: docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:6 records military_tradition_score 61, while common/script_constants/006_independence_wave_force_package_constants.txt:297 defines p6 as 60 and common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:210 validates against p6. Parent should decide whether the accepted mapping row or runtime constant is authoritative before final attestation; no gameplay patch was made here.
6. Read-only MCP limits: the focus inspection returned FOCUS_INSPECTED with no blockers but the complete shared tree validation is false because the 176-focus tree has 14 blocking global layout diagnostics; no selected AFX focus was named in the returned diagnostics. The map inspection returned a workspace-wide diagnostic truncation with 2,654 omitted errors unrelated to AFX. The installed tool set exposes no Technology Tree Viewer, so technology-tree inspection remains an unresolved limitation.

## Validation evidence

Meaningful checks run from the mod root:

    @'
    from PIL import Image
    from pathlib import Path
    import hashlib
    for p in [Path('docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wallonia_ruquoy_trial_01/processed_png/portrait_AFX_walloon_reserve_commander.png'),Path('gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds'),Path('docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wallonia_ruquoy_trial_01/final_dds/portrait_AFX_walloon_reserve_commander.dds')]:
        im=Image.open(p).convert('RGBA')
        print(p, im.size, hashlib.sha256(im.tobytes()).hexdigest().upper())
    '@ | python -

Output: all three images are 156x210; all three decoded RGBA hashes are BEDF59BAA7F114D9446EE1AF9A5C245C44E78A3D68387EF615945E45BD115259. PowerShell file checks report the runtime DDS and package DDS are each 131168 bytes and the exact runtime/package SHA is 0AD247810F8E98AFADE0362CFAC275A68DB401DC4BEBF18B8343B8F77067DFFF.

Additional static checks compared all AFX tag/character/sprite/focus/decision/idea/AI/localisation references, verified all eight focus DDS, three report DDS, two portrait DDS, and three flag TGA ladders exist, decoded AFX flag dimensions with Pillow, and confirmed no live _small, advisor, dossier, operative, female, generic, or fallback portrait reference.

Read-only MCP evidence:

- Focus inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b3ffdd932241beb43437ca660516ad13ae55fdae83baa2ee62a65bb382b44906/425f5e8c7f9a6941b834d6bddbbee462f4844d9bb84cd751a0cd1e40091d92ce/focus-inspect.dfe1fff510afabd2.json. Status FOCUS_INSPECTED, no returned blockers.
- Map inspection artifact: hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/955d055e06761ea328b747e93d5daa1d441d95523f4c4ef095ab78b6b58f36c2/419950397f5dbb56a17bea39eeb99bb710d6bd74537a4067d5da65bdd6247183/map-inspect.8578f9bd46454d3b.json. Global map diagnostics were truncated and are not attributed to AFX.

Skipped meaningful validation: no Hearts of Iron IV process was launched, consistent with repository instructions. No Technology Tree Viewer is installed. No map rewrite was needed or authorised for this country-package audit.

## Patch and handoff record

- Changed files by this subagent: only this handoff file.
- Changed tags, state IDs, leaders, parties, focus IDs, localisation keys, formable IDs: none.
- Before/after gameplay behaviour: unchanged by this subagent. The parent-owned portrait promotion observed by this audit keeps the stable AFX_walloon_reserve_commander and GFX_portrait_AFX_walloon_reserve_commander consumers while changing the display identity to Louis Hubert baron Ruquoy and replacing the runtime DDS with the independently approved source-locked repaint.
- Fallbacks or simplifications introduced: none. No gameplay fallback, placeholder portrait, generic portrait, or replacement focus/decision route was used.
- Remaining action: parent should resolve the IW-006 tradition source/spec discrepancy and review the documentation/validation risks above, then use this handoff as the fresh IW-006 package-audit evidence for exact Event 006 attestation.

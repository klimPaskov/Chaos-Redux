# Event 006 IW-043 / IW-058 country-package audit v47

Date: 2026-08-01 (Europe/Kyiv).

Scope: current country-package coverage for IW-043 Volga Bulgaria on the vanilla CHU carrier and IW-058 Assyria on the vanilla ASY carrier after the parent-owned CHU Luka Semyonovich Spasov runtime portrait promotion. This audit covers country identity, anchors and reservations, host survival, politics, leaders and portraits, parties, focuses, decisions, ideas, forces, technology and industry inheritance, supply, AI, diplomacy, formables, localisation, cleanup, and central runtime admission. It does not admit either package and does not alter shared dispatch gates.

## Result

The gameplay package surfaces are structurally present for both packages, but IW-043 and IW-058 remain fail-closed and must not be admitted to normal Event 006 execution or SCN-008. The central content-attestation trigger still omits `iw_043` and `iw_058`, and the grounded portrait roster is not complete enough for either package.

The current IW-058 terminal settlement guards are mutually exclusive. The earlier cross-mode concern is not present in the current source: `has_independence_wave_iw058_open_terminal_settlement_choice` rejects both terminal receipts and both completed modes, `can_finalize_independence_wave_iw058_form18_terminal_settlement` rejects the autonomy receipt/completion and mode, and `can_finalize_independence_wave_iw058_sovereign_autonomy_terminal_settlement` rejects the federation receipt/completion and mode in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:1200-1244`.

No gameplay, country, focus, decision, AI, character, GFX, DDS, or localisation patch was made by this audit. The only intended change is this handoff document.

## Country package coverage checklist

| Surface | IW-043 CHU | IW-058 ASY | Evidence and finding |
| --- | --- | --- | --- |
| Tag and carrier identity | PASS with shared-carrier guard | PASS | `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:19-58` binds IW-043 to `original_tag = CHU` and IW-058 to `original_tag = ASY`; the mod deliberately reuses vanilla carriers instead of adding country-tag shells. The read-only tag audit correctly reports CHU shared by IW-043 Volga Bulgaria and IW-046 Chuvashia, and the package trigger's `has_valid_independence_wave_chu_package_mutex` / `..._for_setup` guards reject simultaneous CHU package flags (`...package_triggers.txt:80-115`). |
| Origin safety and release identity | PASS structurally | PASS structurally | `can_initialize_independence_wave_iw043_package` and `can_initialize_independence_wave_iw058_package` require `independence_wave_origin_prepared`, Event 006 origin, signature depth, the exact region/archetype, setup package id, saved anchor/host targets, and the expected capital state (`...package_triggers.txt:932-978`). The central dispatch preflight has exact CHU/IW-043 and ASY/IW-058 pairs (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:142-150`). |
| Anchor and reservation | PASS | PASS | IW-043 requires states 249 and 256 for the full opening anchor and state 249 for compact validation; IW-058 requires state 676 (`...package_triggers.txt:895-912`). Reservation research records `RG-MIDDLE-VOLGA-KAZAN` as 249|256 and `RG-NORTHERN-MESOPOTAMIA` as 676|421 in `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`. |
| Former-host survival | PASS structurally | PASS structurally | Setup requires a saved non-self former-host event target and package effects retain guarded host-negotiation, association, reclamation, and security settlement routes. No unconditional annexation or broad world iteration was found in the package effects. |
| Starting values and setup | PASS structurally | PASS structurally | `independence_wave_setup_iw043_middle_volga` and `independence_wave_setup_iw058_assyria` initialize bounded package variables, opening ideas, force receipts, cosmetics, political/institutional surfaces, full focus framework, route registrations, and adapter flags in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt:1280-1491`. |
| Final validation and cleanup | PASS structurally | PASS structurally | `independence_wave_validate_iw043_package` and `independence_wave_validate_iw058_package` require setup receipts, full focus framework, routes, mutexes, bounded values, and compact anchors (`...package_effects.txt:1493-1600`). Package cleanup effects remove package decisions, ideas, roles, formable ledgers, event targets, flags, variables, cosmetics, and focus runtime without transferring unrelated countries. |
| Central runtime admission | BLOCKED | BLOCKED | `has_independence_wave_runtime_package_adapter_for_execution_id` contains both package ids, but `has_independence_wave_runtime_package_content_attestation_for_execution_id` contains only 13 other ids and omits `iw_043` and `iw_058` (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:11-82`). Both normal and scenario preflights call the missing content attestation (`...dispatch_triggers.txt:86-89` and `184-185`), so neither package can execute or enter SCN-008. |

## File-surface checklist

The package source surface is present in the following files.

- `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt` contains exact country checks, anchor/host checks, setup surfaces, value bounds, route mutexes, formable readiness, terminal settlement guards, and cleanup-related receipts.
- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt` contains setup, political and institutional surfaces, force receipts, route effects, formable adapters, validation, and cleanup for `iw_043` and `iw_058`.
- `common/script_constants/006_independence_wave_iw043_iw058_constants.txt` centralizes start values, thresholds, force shares, political profiles, and AI tuning.
- `common/characters/006_independence_wave_iw043_iw058_characters.txt` defines four CHU and four ASY male civilian-large consumers, each with a stable `GFX_portrait_*` sprite.
- `interface/006_independence_wave_iw043_iw058_portraits.gfx` defines all eight stable portrait sprites and their DDS paths.
- `common/ideas/006_independence_wave_iw043_iw058_ideas.txt`, `common/decisions/categories/006_independence_wave_iw043_iw058_categories.txt`, and `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` provide package-scoped ideas, two decision categories, and 38 package decisions/missions (40 top-level blocks including the two categories).
- `common/national_focus/006_independence_wave_focus.txt` imports the shared tree, while `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` contains 48 package focuses (23 IW-043 and 25 IW-058).
- `common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt` contains seven CHU profiles and nine ASY profiles, all gated by `original_tag`, exact package setup, route, reserve, crisis, or terminal-mode conditions.
- `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml`, `..._focus_l_english.yml`, `..._decisions_l_english.yml`, `..._categories_l_english.yml`, and `..._events_l_english.yml` cover the package names, parties, leaders, ideas, focus text, decision text, category text, and event text.

## Map, state, and starting setup

Vanilla state files remain the carrier source: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/249-Kazan.txt`, `256-Cheboksary.txt`, and `676-Mosul.txt`. Vanilla CHU history starts with capital state 256 and its standard Soviet-era technology/politics in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/CHU - Chuvashia.txt`; vanilla ASY starts with capital state 676 and its standard starting technology/politics in `.../history/countries/ASY - Assyria.txt`. The Event 006 package initialization explicitly requires CHU capital state 249 after the execution transfer and ASY capital state 676.

The read-only map inspection returned `MAP_INSPECTED` with status `ok` and validation pass for province definitions, state geometry, state-region links, networks, and positions. The artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9c75c926c558786cd02023643ea70faf9eecb7a51f328f95d155a4feabc6ef6a/3601a00555b566ec639e29697d526049439dfd78e20ddfd41a5c1305f4ea4f87/map-inspect.1c6c62d19b7c80d5.json` (1081 states; selected review states 249, 256, and 676). No map rewrite was necessary or authorized.

## Politics, leaders, portraits, flags, advisors, and parties

### CHU / IW-043

- `CHU_independence_wave_middle_volga_congress` remains localised as Mirsaid Sultan-Galiev and uses the existing accepted consumer.
- `CHU_independence_wave_federal_presidium` is localised as Galimzhan Ibrahimov and has the parent-promoted runtime DDS documented in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_galimzhan_portrait_v2_runtime_promotion_2026_07_28.md`. Its current DDS SHA-256 is `977e0f8d359930f75e01e380a36893ef6a8f25a5b1ce5bbd8cc3c2f3abf6b5f5`.
- `CHU_independence_wave_river_security_directorate` is now localised as the sourced real male Luka Semyonovich Spasov (`localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml:8-9`). The current runtime DDS is `gfx/leaders/006_independence_wave/portrait_CHU_independence_wave_river_security_directorate.dds`, 131168 bytes, SHA-256 `D4D6204767FCFDA3A992D33D0C046C4DF22546C8DB2833857DA96EE3261E0213`, and the stable sprite remains `GFX_portrait_CHU_independence_wave_river_security_directorate`. The independent v45 visual audit is a PASS for identity, rights, era, crop, likeness, ownership, and one-civilian-large consumer boundary; the parent promotion is recorded in commit `43a627f42` and `docs/assets/006_independence_wave/chu_river_security_replacement_v41_2026_07_29/manifest.md`.
- `CHU_independence_wave_bolgar_civic_presidium` remains the unresolved roster row. Musa Dzhalil still has an unresolved museum/rights review, and Karim Tinchurin has a source-ready candidate under `docs/assets/006_independence_wave/iw043_iw058_portrait_rights_research_2026_07_29/` but no parent-approved processed/DDS runtime promotion. This single missing Bolgar consumer keeps the CHU visual roster incomplete.
- All four CHU records are explicitly `gender = male` and use only `civilian.large`; there are no advisor, high-command, commander, operative, dossier, or opposite-gender portrait consumers.

### ASY / IW-058

- `ASY_independence_wave_provisional_national_council` uses the existing sourced Gallo Shabo identity. Reusing `ASY_gallo_shabo` for the separate Civic National Assembly would be an exact same-project identity reuse and requires an explicit parent role decision; it is not an automatic roster clearance.
- `ASY_independence_wave_concordat_council` remains unresolved despite the later v41 research note. `docs/assets/006_independence_wave/asy_portrait_replacements_v41_2026_07_29/manifest.md` claims authoritative Commons/PD-Syria rights resolution for Ignatius Afram I Barsoum, while `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw058_portrait_visual_audit_v38_2026_07_29.md` still records the rights gate as FAIL. The current runtime DDS `gfx/leaders/006_independence_wave/portrait_ASY_independence_wave_concordat_council.dds` is SHA-256 `8CFD82ACEE444E9C026FAB0688DF7F5C797D8D4E237F3CAF72F7575EBD77C085`, while v41's stated runtime hash is `86616a420cf00473d5422c140337b600b9542cfcf4456d34d959de41cd05b48f`; `git log` shows only the original package commit for the current DDS and no explicit Barsoum promotion commit. This is an evidence/runtime mismatch and must remain blocked until the parent reconciles rights, candidate, and runtime hash.
- `ASY_independence_wave_civic_national_assembly` remains blocked. Rev. Joel E. Werda/Warda fails the portrait-detail and historical 1936 life/office gates; Gallo Shabo is only a possible same-person reuse and is role-framed as a military/community leader rather than a documented 1936 civic-national officeholder.
- `ASY_independence_wave_levies_guardianship` remains blocked. Malik Ismail II lacks a resolved exact 1936 date/active-role gate; Agha Petros died in 1932 and is Kaiserreich-owned; Malik Khoshaba is rejected by the Kaiserreich exact-person owner `ASY_khoshaba_yosip`; Shamoun Hanne Haydo is rights-blocked.
- All four ASY records are explicitly `gender = male` and use only `civilian.large`; no opposite-gender pool or advisor/small-art consumer is present.

Party names and ideology/political setup are package-scoped in `localisation/english/006_independence_wave_iw043_iw058_country_core_l_english.yml:76-107` and applied by the package political-surface effects. No party, leader-id, or cosmetic-tag collision was found in the package source.

## Focus, decision, idea, and asset coverage

The 48 package focuses are route-gated by `is_independence_wave_iw043_country` or `is_independence_wave_iw058_country` and have localisation coverage across all localisation files. A read-only cross-file check found 48 focus ids and zero missing focus localisation keys. The MCP focus inspection found the package roots and a 184-focus shared tree, but its whole-tree validation is false because of 14 shared layout diagnostics (`FOCUS_LAYOUT_LONG_CONNECTOR`, `FOCUS_AVOIDABLE_CONNECTOR_CROSSING`, `FOCUS_LAYOUT_CONNECTOR_CROSSING_UNSATISFIED`, and `FOCUS_LAYOUT_CONNECTOR_THROUGH_NODE`). These diagnostics are not confined to IW-043/IW-058 and no broad shared-tree layout patch is justified in this country audit. The focus artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f4a6151122db34e250dd1567292d80b179017f6b9b291c5b8294f3751be913d/a27a758ab544106f08be92b8396839a72c6b39709e917f5d0c515f73c582260a/focus-inspect.35352a69d0aa6e61.json`.

The two decision categories are `independence_wave_iw043_middle_volga_congress_category` and `independence_wave_iw058_council_of_communities_category` (`common/decisions/categories/006_independence_wave_iw043_iw058_categories.txt:12-26`). The 38 package decisions and missions cover both opening contracts, route actions, host actions, crises, FORM-12/13/18 work, and the IW-058 sovereign autonomy transaction. The current terminal guards reviewed above prevent sequential federation/autonomy settlement. Starting ideas and lifecycles are package-scoped in `common/ideas/006_independence_wave_iw043_iw058_ideas.txt`, with IW-043 opening ideas `independence_wave_iw043_congress_in_session_idea`, `independence_wave_iw043_disrupted_river_economy_idea`, and `independence_wave_iw043_provisional_river_guard_idea`, and IW-058 opening ideas `independence_wave_iw058_provisional_council_idea`, `independence_wave_iw058_exposed_mosul_corridor_idea`, and `independence_wave_iw058_fragile_diaspora_links_idea`.

Flags, leader sprites, idea icons, focus icons, and decision icons are wired to stable package paths. The remaining asset blockers are portrait evidence and runtime promotion, not missing `.gfx` declarations.

## Forces, technology, industry, supply, and production

The package has dynamic force mapping and generation receipts through `independence_wave_load_force_package_mapping`, `independence_wave_apply_dynamic_starting_force`, `independence_wave_record_iw043_force_receipts`, and `independence_wave_record_iw058_force_receipts` in `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`. Setup and final validation require the current-generation force package and designated formation generation before package completion. The package constants centralize the force shares and equipment/production tuning.

Vanilla CHU and ASY history provide the inherited 1936 research slots, technologies, doctrines, politics, and starting production baseline; the package does not overwrite country-history files. A Technology Tree Viewer is not exposed by the installed HOI4 MCP package, so technology-tree inspection and rendered prerequisite comparison remain an unresolved validation limitation. No technology rewrite was made.

Anchor-state supply and transport surfaces are represented by the package's river/corridor variables, railway/ferry decisions, rail/ferry focus rewards, train/convoy production AI, and state 249/256/676 checks. No standalone package-owned port, railway, resource, or map mutation was found that would justify a country-local patch.

## AI, diplomacy, formables, and playability

The seven CHU profiles (`independence_wave_iw043_foundation`, `..._reserve_recovery`, `..._tracked_crisis`, `..._federal_route`, `..._restoration_route`, `..._emergency_route`, and `..._civilian_normalization`) and nine ASY profiles (`independence_wave_iw058_foundation`, `..._reserve_recovery`, `..._tracked_crisis`, `..._church_compact_route`, `..._civic_assembly_route`, `..._guardianship_route`, `..._civilian_normalization`, `..._federal_settlement`, and `..._sovereign_autonomy`) are exact-carrier and setup/route/crisis gated. They use bounded constants and abort when their enable gates fail; no world scan is used.

FORM-12, FORM-13, and FORM-18 adapters are registered in package effects and readiness triggers, with CHU route mutexes and ASY terminal-mode mutexes. Exact package availability wrappers exist for both reused carriers, but the central attestation omission keeps every formable route unreachable through normal package dispatch. This is intentional fail-closed behavior, not a missing formable implementation.

The package is playable in source design once admitted: setup establishes a full focus framework, bounded opening values, force receipts, opening ideas, route decisions, AI profiles, and cleanup. Live consumer/gameplay validation remains parent/user-owned and was not attempted.

## MCP and static validation

- Read-only map inspection passed structural validation for 1081 states, province definitions, geometry, state-region links, networks, and positions; artifact recorded above.
- Read-only focus inspection found all package roots and 184 total focuses but returned false whole-tree validation because of 14 shared layout diagnostics; no package-local geometry fix was made.
- Read-only event inspection of `chaosx.nr006.4301` returned `EVENT_INSPECTED_PARTIAL`, focused scan status `ok`, and no blocking diagnostics; lifecycle/helper projections were deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1350f6051426b232ed3b3a9300b46920e1c0d2ad4fc8291984669f6108747118/86fd76b0f0cf0ae8b50b926f4e8dd9b03ed1313a4174ed8684d3ae2ae58d2416/event-scan-a0a45e8454b8.json`.
- `python -B .tools/audit_event6_allocator.py` completed successfully and reported 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, and 13 content-attested packages; IW-043 and IW-058 were not in the attested set.
- `python -B .tools/audit_hoi4_country_tags.py --workshop-root C:\__chaosx_missing_workshop__ --local-mod-root C:\__chaosx_missing_local_mods__` completed read-only against the repository and vanilla roots with `collisions=0`, `custom_cosmetic_collisions=0`, and `identity_matches=50`; its `shared_reused_tag_reviews` records CHU/IW-043 as `content_attested=false` and `runtime_status=fail_closed`. A full installed-Workshop/local-mod scan was not used in this pass because the unconstrained scan exceeded the bounded audit window.
- A read-only cross-file localisation check found all 48 package focus ids in localisation and no missing focus keys.
- The required offline Paradox wiki pages and relevant vanilla country/state/history documentation were read before this audit; no live game launch or in-game validation was attempted.

## Missing, stale, or contradictory surfaces

1. `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:65-82` omits `iw_043` and `iw_058` from content attestation even though adapter and exact tag-pair branches exist. Parent-owned central admission must stay closed until complete portrait and package audits are reconciled.
2. CHU Bolgar Civic Presidium lacks an admitted sourced portrait consumer. Musa Dzhalil rights remain unresolved and Karim Tinchurin has no runtime DDS promotion.
3. ASY Barsoum evidence is contradictory across v38 and v41 handoffs, and the live DDS hash does not match v41's recorded runtime hash. Treat the current `ASY_independence_wave_concordat_council` consumer as unresolved until an independent rights/runtime audit and explicit promotion reconcile the records.
4. ASY Civic National Assembly and Levies Guardianship remain blocked by identity, date, role, rights, or exact-person collision gates listed above.
5. The focus MCP artifact still reports shared-tree geometry diagnostics. This is a shared focus-tree surface, not a country-local package defect, and it was intentionally left untouched.
6. Technology Tree Viewer is unavailable in the installed MCP package, so technology prerequisites and rendered tree placement were not independently inspected.

## Changed files and patch status

Changed files: this handoff only.

Changed tags, states, leaders, parties, focus ids, localisation keys, and formable ids: none.

Before/after gameplay behavior: unchanged. The package remains fail-closed before and after this audit; no central attestation, portrait, map, or country setup was broadened.

No plan handoff was created because the remaining work is bounded portrait rights/runtime reconciliation and parent-owned central admission review, not a country identity redesign or new focus/formable suite.

## Remaining setup and identity risks

Both packages must remain outside the runtime attestation set until the CHU Bolgar row and all ASY portrait rows pass their sourced identity, 1936 role, rights, collision, crop, runtime DDS, and post-wiring audits. The parent should reconcile the stale Barsoum v38/v41 evidence and current DDS hash before considering IW-058 admission. The parent should not add `iw_043` or `iw_058` to the central content-attestation trigger merely because Spasov, Galimzhan, or the gameplay scaffolding is complete.

Simplifications or omissions: no gameplay simplification was introduced. The only intentionally incomplete surfaces are the documented portrait/admission blockers and the unavailable Technology Tree Viewer validation.

# IW-001 Scotland country-package re-audit

Date: 2026-07-24

Auditor scope: additive vanilla `SCO` carrier for Independence Wave Event 6, including the current sourced portrait runtime commit `667a4a92e`.

## Verdict

The IW-001 Scotland package passes the country-package content audit after the runtime portrait replacement in `667a4a92e`.

The package is not currently admitted to the readiness-controlled automatic pool because `has_independence_wave_runtime_package_content_attestation_for_execution_id` omits `constant:independence_wave_package_id.iw_001` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:44-50`.

This is a parent-owned admission-gate hold, not a Scotland gameplay or asset defect.

Recommendation: promote IW-001 into the compile-time content-attestation `OR` after the parent updates the source-of-truth admission notes and performs its shared-gate validation, then admit it only when the exact `SCO` tag is not living and the existing readiness predicate passes.

No broad redesign, fallback, or country-gameplay patch was made in this re-audit.

## Country-package coverage checklist

- Identity and tag: PASS. Vanilla `SCO` remains registered by `common/country_tags/00_countries.txt` and resolves to `common/countries/Scotland.txt`; no duplicate Event 6 tag or replacement of the existing vanilla identity was found.
- Event origin isolation: PASS. IW-001 uses `original_tag = SCO`, package id `iw_001`, Northern and Western Europe region, regional depth, and `port_or_island` archetype in `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt`.
- Event 6 entry and hidden setup: PASS. Canonical `chaosx.nr6.1` remains in `events/006_independence_wave.txt`, and hidden `chaosx.nr6.10` recruits the three IW-001 advisors only behind the exact package predicate.
- Host survival and release: PASS by static review. Frozen release and ownership paths use `common/scripted_effects/006_independence_wave_execution_effects.txt` and `common/scripted_effects/006_independence_wave_package_planner_effects.txt`; the installed binding protects an ENG remnant at host capital state `126` and trims optional states before the anchor.
- State and capital setup: PASS. Binding anchor is state `121` Lothian with compact `121|133` and extension `120|136|933`; the candidate capital is state `121` and Edinburgh VP `9392` is present in the vanilla state file.
- Politics and government routes: PASS. Civic convention, workers commonwealth, crown and convention, and emergency territorial directorate routes are installed by `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt` with male metadata and route ideas.
- Leader and command roster: PASS. `SCO_independence_wave_civic_convention` and `SCO_independence_wave_territorial_commandant` are generated only for the IW-001 setup and use explicit male metadata; the commandant also receives the corps-commander role.
- Portrait and flag coverage: PASS after runtime commit. Two full-size sourced leader sprites are wired, vanilla Scotland flags are reused, and no Event 6 `_small`, advisor, dossier, or female portrait consumer is active.
- Advisors and parties: PASS. The three IW-001 advisor offices, traits, costs, availability, AI factors, party names, and leader strings are covered by the package character, trait, and localisation files.
- Focus tree: PASS by static review. The five bespoke SCO focus ids are localized, icon-wired, availability-guarded, prerequisite-linked, and loaded through the Event 6 framework without replacing the vanilla tree globally.
- Decisions and missions: PASS for the specified project surface. Eleven SCO projects, route actions, formable actions, cancellation, cost, tooltip, and AI logic are present; no separate IW-001 mission block is required by the current package surface.
- Ideas and mechanics: PASS. `sco_divided_coastal_command`, `sco_north_atlantic_state_service`, route ideas, state-pressure lifecycle, traditional-authority-versus-assembly power struggle, ambitions, league membership, and cleanup paths are wired.
- Starting military, technology, industry, supply, and production: PASS by design. No bespoke country history or OOB is required because the dynamic force package derives a bounded territorial-defense start from the frozen host and anchor state; p1 mapping, tech inheritance, stockpile, convoy, port, rail, supply, and production factors are defined in the force package effects and constants.
- AI and playability: PASS by static review. Maritime survival, founding restraint, former-host threat, constitutional, labor, traditional, emergency, coastal defense, production, and infrastructure strategy factors are present.
- Formables and diplomacy: PASS by static review. Celtic cooperation and North Atlantic family registration, FORM-01 and FORM-02 strict state and port checks, host negotiation, guarded frontier, association, reclamation, cleanup, and preservation checks are present.

## File surface checklist

| Surface | Evidence | Result |
| --- | --- | --- |
| Tag and vanilla identity | `common/country_tags/00_countries.txt`, `common/countries/Scotland.txt`, `history/countries/SCO - Scotland.txt` | PASS, additive reuse |
| IW-001 setup and cleanup | `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt`, `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt` | PASS |
| Release and host safety | `common/scripted_effects/006_independence_wave_execution_effects.txt`, `common/scripted_effects/006_independence_wave_package_planner_effects.txt`, `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` | PASS |
| Events | `events/006_independence_wave.txt` | PASS |
| Focuses | `common/national_focus/006_independence_wave_focus.txt` | PASS |
| Decisions | `common/decisions/006_independence_wave_scotland_wales_decisions.txt`, `common/decisions/categories/006_independence_wave_scotland_wales_categories.txt` | PASS |
| Ideas | `common/ideas/006_independence_wave_scotland_wales_ideas.txt` | PASS |
| Characters and traits | `common/characters/006_independence_wave_nwe_advisors.txt`, `common/country_leader/006_independence_wave_nwe_advisor_traits.txt` | PASS |
| AI | `common/ai_strategy/006_independence_wave_scotland_wales.txt` | PASS |
| Formables | `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt`, `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`, `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` | PASS |
| Localisation | `localisation/english/006_independence_wave_scotland_wales_l_english.yml`, `localisation/english/006_independence_wave_nwe_advisors_l_english.yml` | PASS |
| Focus, idea, decision icons | `interface/006_independence_wave.gfx`, `gfx/interface/ideas/006_independence_wave`, shared Event 6 interface assets | PASS |
| Leader sprites | `interface/006_independence_wave_region_01_portraits.gfx`, `gfx/leaders/006_independence_wave` | PASS after `667a4a92e` |
| Dispatch admission | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | HOLD for IW-001 attestation |

## Map, state, and host setup

The installed IW-001 binding is `SCO`, `fixed_anchor_compact`, anchor state `121`, compact states `121|133`, extended states `120|136|933`, host `ENG`, protected host capital `126`, and reservation `RG-121-120-133`.

Vanilla state evidence confirms state `121` Lothian has Edinburgh VP `9392`, SCO and ENG cores, and the expected naval and building setup; states `120`, `133`, `136`, and `933` also retain the intended ENG and SCO core relationship.

The host-loss planner reserves the host remnant and trims extension before compact territory and the anchor, so release cannot silently remove the protected ENG capital remnant.

The binding prose still says “Highlands, Ayrshire, and Shetland” while the runtime extension is state `136` Aberdeenshire in `006_current_installed_map_package_bindings.csv`; this is a stale documentation phrase only and does not change the installed state list.

## Politics, leaders, portraits, flags, advisors, and parties

`independence_wave_prepare_sco_institutional_roster` creates `SCO_independence_wave_civic_convention` with male gender, centrism, socialism, and oligarchism country-leader roles, plus `SCO_independence_wave_territorial_commandant` with male gender, despotism, and corps-commander skills.

The commandant uses `GFX_portrait_SCO_independence_wave_territorial_commandant` for both civilian large and army large roles, which is intentional for the full-size leader surface and does not infer an advisor or dossier portrait.

The three advisor tokens are `SCO_independence_wave_shipping_authority_commissioner`, `SCO_independence_wave_industrial_reconstruction_secretary`, and `SCO_independence_wave_territorial_defense_planner`; all have package availability, traits, costs, AI factors, and localisation.

Existing vanilla SCO identity, vanilla flags, and vanilla characters are preserved; the Event 6 package does not replace vanilla `ENG_edmund_ironside` or invent a new vanilla identity.

## Portrait provenance and runtime proof

The civic portrait consumer is `SCO_independence_wave_civic_convention` with sprite `GFX_portrait_SCO_independence_wave_civic_convention`; the independent trial-04 audit identifies real subject Robert Bontine Cunninghame Graham, public-domain Commons/HathiTrust provenance, source master 813x1101, and exact crop `(120,120,700,900)`.

The territorial commandant consumer is `SCO_independence_wave_territorial_commandant`; the independent trial-01 audit identifies Major-General Sir Victor Morven Fortune, public-domain Commons/IWM provenance, source master 200x250, and exact crop `(0,0,200,250)`.

Fortune's low source resolution, 1940 source date, mild possible de-aging, reconstructed cap-badge detail, full-size leader export mode, and Montgomery commander style reference are explicitly disclosed in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_sco_fortune_trial01_source_locked_visual_provenance_audit_2026_07_23.md` and remain acceptable because the identity and role are preserved.

The current runtime DDS `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_civic_convention.dds` is 156x210 legacy BGRA, 131168 bytes, SHA-256 `61C08E14A90FFE6522781B7AD74CF0AF36B7C11426A6FAEF85A3B1887346DA53`.

The current runtime DDS `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` is 156x210 legacy BGRA, 131168 bytes, SHA-256 `71531A64CDEAF535EC6F93E4FC00B30AFBDD46929B3B104C7A47E83A65FE3F1A`.

Pillow decoding of both DDS files produced the approved 156x210 RGBA PNG pixels byte-for-byte, confirming the runtime conversion rather than only filename or header agreement.

Only the two full-size SCO runtime DDS files are present under `gfx/leaders/006_independence_wave`; no active `_small`, female, generated identity, advisor, dossier, or alternate portrait consumer was found.

## Focus, decision, idea, and asset findings

The five bespoke focus ids are `independence_wave_sco_reconnect_central_belt_focus`, `independence_wave_sco_charter_north_atlantic_shipping_focus`, `independence_wave_sco_settle_crown_and_convention_focus`, `independence_wave_sco_convene_celtic_maritime_conference_focus`, and `independence_wave_sco_found_north_atlantic_state_service_focus`; each has package availability, prerequisites, localisation, and a shared icon.

The eleven active SCO projects are `reconnect_central_belt`, `organize_firth_convoys`, `settle_british_asset_ledgers`, `unify_territorial_command`, `ratify_constitutional_convention`, `charter_workers_commonwealth`, `settle_crown_and_convention`, `establish_emergency_directorate`, `choose_celtic_cooperation`, `choose_north_atlantic_compact`, and `convene_maritime_conference`.

The default Celtic family selection is intentional in IW-001 setup, while the North Atlantic family remains an alternate choice; the prepared trigger accepts either selected family and the strict FORM-01 and FORM-02 checks require the correct SCO anchor, compact control, and port conditions.

No missing SCO icon or localisation key was found in the current source surface, and the Scotland/Wales localisation file has a UTF-8 BOM.

## Starting forces, technology, industry, supply, production, and AI

IW-001 intentionally has no bespoke `history/countries/SCO` OOB or country-history replacement; the dynamic force package loads p1 territorial-defense mapping from `common/scripted_effects/006_independence_wave_force_package_effects.txt` and `common/script_constants/006_independence_wave_force_package_constants.txt`.

The p1 mapping supplies military tradition 70, five reinforcement pathways, navy and air inheritance, bounded manpower and equipment, inherited technology and research slots, and production and supply scaling from the frozen host and package states.

The AI file provides maritime survival, founding restraint, former-host threat, constitutional, labor, traditional, emergency, coastal defense, infrastructure, dockyard, convoy, train, and infantry production behavior.

## Missing, stale, or blocked surfaces

1. Admission hold: `has_independence_wave_runtime_package_content_attestation_for_execution_id` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:44-50` currently recognizes only IW-004, IW-007, and IW-017, so the exact `iw_001` package cannot pass the readiness-controlled automatic-pool gate even though its adapter and exact `SCO` preflight branch exist at `:57-66`.
2. Documentation cleanup: the installed binding prose names Ayrshire while the runtime extension includes Aberdeenshire state `136`; update the wording when the parent reconciles the source-of-truth map.
3. Runtime limitation: no live game, HOI4 MCP render, event compare, focus render, or map rewrite was run in this isolated audit; the installed package exposes no Technology Tree Viewer, so technology-tree runtime inspection remains unresolved.

No country-package gameplay or asset blocker was found beyond the parent-owned admission attestation hold.

## Validation performed

- Read the required repository instructions, Event 6, asset, subagent, focus-tree, and decisions skills before inspection.
- Consulted the required offline Paradox wiki core pages and relevant country, focus, decision, event, idea, portrait, division, equipment, technology, and graphical-asset pages.
- Consulted vanilla country, tag, state, history, character, focus, and documentation precedents for SCO, ENG, release, leader, and dynamic force behavior.
- Checked exact tag and package references across the Event 6 source surface with static search and confirmed no duplicate Event 6 SCO package or unrelated non-Event-6 SCO override.
- Checked focus ids, decision ids, idea ids, advisor ids, leader ids, portrait sprite names, and localisation coverage against their consumer files.
- Checked current runtime DDS dimensions, format masks, byte lengths, SHA-256 values, and pixel equivalence to the approved portrait PNG masters.
- Reviewed both independent portrait provenance audits and confirmed all Fortune disclosures remain recorded and acceptable.

## Changed files and handoff

This re-audit changed only this handoff file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw001_scotland_country_package_reaudit_2026_07_24.md`.

No tags, state ids, leaders, parties, focus ids, localisation keys, formable ids, gameplay scripts, GFX files, or runtime assets were changed by this audit.

Parent follow-up is limited to promoting `iw_001` in the shared runtime content-attestation trigger, reconciling the stale binding phrase, updating the source-of-truth admission notes, and performing the parent-owned shared-gate validation.

No fallback or simplification was used.

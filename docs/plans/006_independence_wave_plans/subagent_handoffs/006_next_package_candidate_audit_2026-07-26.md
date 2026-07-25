# Event 006 next package candidate audit

Date: 2026-07-26  
Owner: country-package audit subagent  
Scope: read-only candidate comparison after the IW-179 sourced-portrait retry  
Disposition: no package promotion, gameplay edit, GFX edit, portrait production, or attestation edit was made.

## Executive result

No candidate currently passes the complete grounded male portrait, source, flag, package, and runtime-attestation gate. The ranking below is a conditional work queue for the parent agent, not an admission recommendation.

1. **IW-173 Hawaii / HAW / state 629 / RG-629** is the strongest existing-package candidate and the cleanest way to add a tenth distinct reservation group, but it remains blocked by the failed David Kalakaua Kawananakoa likeness trial and by the generic portrait mappings of the complete vanilla HAW leader roster.
2. **IW-177 Fiji / FIJ / state 636 / RG-PACIFIC-ISLANDS** is the strongest new-package candidate. Its single-state binding, four ideology flag triplets, force value 53, and high research confidence are better than Samoa's current map and force profile. It still has no Event 006 country-package implementation beyond planner and reservation surfaces and has no sourced male leader or exact institutional portrait evidence in the repository.
3. **IW-175 Samoa / SAM / state 726 / RG-PACIFIC-ISLANDS** is viable only as the alternative Pacific-group admission to Fiji. It has high research confidence and a clean anchor, but its optional American Samoa extension crosses NZL and USA hosts, its force value is 50, and it has the same missing package and sourced-leadership surfaces.

IW-179 Micronesia is not a fourth candidate. It remains the best Pacific implementation architecture, but the 2026-07-26 source retry found no production-safe Henry Nanpei or equivalent real male Micronesian portrait. Do not use the current fictional Elias Kihleng consumer or any blocked thumbnail as a substitute.

Because Fiji, Samoa, and Micronesia share RG-PACIFIC-ISLANDS, at most one of them can be an automatic package in the same wave. HAW's RG-629 is separate. No two Pacific-group IDs should be counted as two distinct groups.

## Current registry and attestation state

The authoritative candidate matrix docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv contains 206 rows. The research resolution matrix docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv also contains 206 rows. Each of IW-173, IW-175, IW-177, and IW-179 has exactly one row in both matrices.

The current canonical content-attestation trigger is has_independence_wave_runtime_package_content_attestation_for_execution_id in common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:55-68. Its exact set remains IW-001, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-017, IW-019, and IW-184. None of IW-173, IW-175, IW-177, or IW-179 is in that OR block.

The ten attested IDs occupy nine distinct reservation groups because IW-008 and IW-010 both use RG-RHINE-SAAR. Admitting HAW would add RG-629; admitting one of Fiji, Samoa, or Micronesia would add RG-PACIFIC-ISLANDS. The allocator and scenario preflight both reuse the same exact attestation trigger, so a registry row, scenario rank, adapter, or positive map binding cannot admit an un-attested candidate.

The central planner guard at common/scripted_effects/006_independence_wave_package_planner_effects.txt:95-107 requires the content attestation before reservation work. Candidate weight calculation at common/scripted_effects/006_independence_wave_package_planner_effects.txt:481-526 also requires it before a base weight is assigned. The Samoa and Fiji helper functions in common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:519-539 rely on this central calculator; their local wrappers are not proof of content readiness.

## Candidate comparison

| Rank | Package and tag | Binding and group | Existing country-package depth | Grounded source state | Map, flag, and collision state | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | IW-173 Hawaii, HAW | Fixed compact anchor 629, RG-629, automatic if tag is not living | Dedicated Pacific ideas, decisions, focus branch, AI, setup/lifecycle, cleanup, FORM-48 membership, localisation, and flag reuse already exist | Blocked. David Kalakaua Kawananakoa's 1925 source failed the independent likeness gate. Vanilla also exposes Joseph Poindexter and Charles Fujimoto with generic sprites; the complete visible personal roster has not passed the current source-only rule | Map binding is ready and the 2026-07-26 collision audit reports zero reserved/custom collisions. Vanilla HAW normal, medium, and small base flags exist; neutrality, fascism, and communism variants exist, while a democratic-specific variant is absent | First conditional candidate. Re-open only after a stronger sourced roster and full package re-audit |
| 2 | IW-177 Fiji, FIJ | Fixed compact anchor 636, RG-PACIFIC-ISLANDS, automatic if tag is not living | Only region-13 planner, load, reservation, and scenario-ranking hooks exist. No Event 006 Fiji character, leader, AI, idea, decision, focus, setup, cleanup, or localisation package exists | No Fiji-specific source row or production-safe sourced male/institutional portrait exists in the current asset ledger. Research resolution requires a sourced real male period leader or exact archival material for the founding federal institution | Single state 636 is owned by ENG and has no optional cross-host extension. Vanilla FIJ has complete normal, medium, and small neutrality, democratic, fascist, and communist flag triplets. Collision audit has no FIJ hit | Best new-package candidate, but broad package implementation and source research are required before any admission work |
| 3 | IW-175 Samoa, SAM | Fixed compact anchor 726, optional 1072, RG-PACIFIC-ISLANDS, automatic if tag is not living | Only region-13 planner, load, reservation, and scenario-ranking hooks exist. No Event 006 Samoa character, leader, AI, idea, decision, focus, setup, cleanup, or localisation package exists | No Samoa-specific source row or production-safe sourced male/institutional portrait exists in the current asset ledger. Research resolution requires a sourced real male period leader or exact archival material for the provisional institution | State 726 is owned by NZL and optional state 1072 by USA. Vanilla SAM normal, medium, and small base flags exist with democratic, fascist, and communist variants; a neutrality-specific variant is absent. Collision audit has no SAM hit | Third conditional candidate and mutually exclusive alternative to Fiji within RG-PACIFIC-ISLANDS |

## IW-173 Hawaii audit

### Registry, map, politics, and force

The registry row is IW-173, resolved tag HAW, anchor state 629, RG-629, automatic pool disposition automatic_pool_ready_if_not_living, and high research readiness. The resolution row defines a period royal, customary, or historical institution joined to a provisional cabinet, municipal administration, veterans, schools, labor, and an assembly. The map binding in docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv keeps state 629 compact and treats 630, 631, 642, and 727 as optional extensions. All five current owners are USA and the host survival witness is USA capital 361.

The vanilla file C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/HAW - Hawaii.txt:59-87 creates three personal country leaders: David Kalakaua Kawananakoa with GFX_portrait_David_Kalakaua_Kawananakoa, Joseph Poindexter with GFX_portrait_Joseph_Poindexter, and Charles Fujimoto with GFX_portrait_Charles_Fujimoto. The installed vanilla interface maps those tokens to Portrait_Asia_Generic_land_5.dds, Portrait_USA_Generic_land_1.dds, and Portrait_Asia_Generic_1.dds respectively. Event 006 currently preserves this roster through has_independence_wave_haw_preserved_vanilla_leadership in common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:37-44 and does not replace the vanilla leaders.

The current force row is IW-173 in docs/plans/006_independence_wave_plans/006_force_package_mapping.csv. It defines coastal guards, sailors, and local infantry, coastal_maritime, force value 62, inherited navy and air, and a civilian island staff direction. The package has a dedicated HAW lifecycle and cleanup path in common/scripted_effects/006_independence_wave_pacific_package_effects.txt:509-557 and :674-709.

### Existing package surfaces

The package-specific surfaces are present and coherent: common/ai_strategy/006_independence_wave_pacific.txt contains independence_wave_haw_island_shipping_survival, independence_wave_haw_founding_restraint, and independence_wave_haw_host_threat; common/ideas/006_independence_wave_pacific_ideas.txt contains haw_exposed_island_supply and haw_island_shipping_compact; common/decisions/006_independence_wave_pacific_decisions.txt:170-280 contains the HAW shipping, coastwatch, base-account, and delegation projects; common/national_focus/006_independence_wave_pacific_focus.txt:145-263 contains the HAW focus route; and localisation/english/006_independence_wave_pacific_l_english.yml contains the HAW category, ideas, decisions, and focus strings. No HAW custom portrait sprite or DDS exists in interface/006_independence_wave_pacific_portraits.gfx or gfx/leaders/006_independence_wave.

### Portrait and source blocker

The source and independent-review handoffs docs/plans/006_independence_wave_plans/subagent_handoffs/006_hawaii_kawananakoa_trial01_independent_audit_2026_07_24.md and 006_hawaii_kawananakoa_source_clearance_retry02_2026_07_24.md both record a no-pass disposition. The 1925 archival source is correctly attributed and rights-documented, but clipped facial highlights force reconstruction and fail exact likeness. No processed DDS or runtime override was authorized.

A future HAW admission must either provide a stronger, rights-cleared, identity-preserving male source for the actual opening leader and re-audit every visible personal HAW leader, or make a separately reviewed package design decision that prevents unsupported alternate personal leaders from being visible. The latter is a gameplay/package change and is not authorized by this audit. A generic portrait, an invented HAW officeholder, an unreviewed existing leader, or a generated substitute is not acceptable.

### HAW file and identifier checklist

- Tag and map: HAW, state 629, optional states 630, 631, 642, and 727, RG-629.
- Vanilla leaders and consumers: David Kalakaua Kawananakoa / GFX_portrait_David_Kalakaua_Kawananakoa; Joseph Poindexter / GFX_portrait_Joseph_Poindexter; Charles Fujimoto / GFX_portrait_Charles_Fujimoto.
- Event 006 package predicate: is_independence_wave_haw_package in common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt:17-21.
- HAW ideas: haw_exposed_island_supply, haw_island_shipping_compact.
- HAW decision IDs: independence_wave_haw_secure_island_shipping_lanes, independence_wave_haw_reconcile_shipping_registers, independence_wave_haw_organize_island_coastwatch, independence_wave_haw_settle_base_and_property_accounts, independence_wave_haw_authorize_pacific_delegation.
- HAW focus IDs: independence_wave_haw_reconcile_shipping_registers_focus, independence_wave_haw_organize_island_coastwatch_focus, independence_wave_haw_seat_island_government_compact_focus, independence_wave_haw_bind_shipping_supply_and_coastwatch_focus, independence_wave_haw_settle_base_and_property_accounts_focus, independence_wave_haw_ratify_autonomous_pacific_mandate_focus, independence_wave_haw_dispatch_pacific_delegation_focus.
- Required future asset consumer boundary: one reviewed full-size country-leader consumer only unless a future source audit explicitly clears more roles. No advisor, dossier, operative, commander, or _small derivatives.

## IW-177 Fiji audit

### Registry, map, politics, and force

The registry row is IW-177, resolved tag FIJ, anchor state 636, RG-PACIFIC-ISLANDS, automatic pool disposition automatic_pool_ready_if_not_living, and high research readiness. The resolution row requires a founding congress of named member regions or communities with representation, veto, autonomy, revenue, and defense clauses before wider federation.

The map binding keeps only state 636, owned by ENG with capital 126. The host survives the compact reservation, the state history file is 636-Fiji.txt, and there are no missing current state IDs. The vanilla country history C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/FIJ - Fiji.txt starts with capital 636, 20 convoys, democratic ruling party, democratic 50, fascism 6, communism 6, and neutrality 38. It has no country leader and no OOB, so a future Event 006 package must supply a grounded provisional leadership/institution contract and a non-empty force setup through the generic force pipeline.

The force row is IW-177 in 006_force_package_mapping.csv: coastal guards and local infantry, coastal_maritime, force value 53, inter-island mobility with scattered forces, fuel scarcity, and a small replacement pool. The officer direction is period-valid registered-tag officers or an institutional federal island staff with local guard liaison.

### Existing and missing surfaces

The only exact IW-177 gameplay references are the planner trigger and load/reservation functions in common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt:176-183 and common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:294-306, :530-539, and :764-770, plus the scenario ranking entries in common/scripted_effects/006_independence_wave_scenario_effects.txt:251-252. There is no is_independence_wave_fij_package, Fiji character, leader, AI strategy, idea, decision, focus, setup, cleanup, Event 006 localisation, portrait GFX, or DDS surface.

Vanilla FIJ flag assets are unusually complete for this comparison: normal, medium, and small FIJ_communism.tga, FIJ_democratic.tga, FIJ_fascism.tga, and FIJ_neutrality.tga all exist in the installed game. The asset coverage ledger treats IW-177 as Group A registered base reuse, so existing flags may be retained only after identity and opening-route confirmation. No flag collision was found in the current audit.

### Required gate work

A Fiji candidate needs a sourced real male period leader or source-locked archival material of the actual founding federal institution. The source must include identity, date, role, community/region fit, ownership, and explicit reuse evidence. A collective leader token is allowed only when the body is genuinely collective and the archival image is authentic, all-male, and attributable to that exact institution. The current repository contains no Fiji-specific source row, so this is a research blocker, not a pending asset conversion.

After source clearance, the parent would still need a complete FIJ package: a country character or institutional leader consumer, male metadata, localisation, package-specific setup and cleanup, AI strategy, ideas, decisions or missions, focus or generic-tree guard, force receipt, starting technology/industry/supply audit, host survival, scenario preflight, and exact runtime attestation. None of those implementation surfaces is present today.

## IW-175 Samoa audit

### Registry, map, politics, and force

The registry row is IW-175, resolved tag SAM, anchor state 726, RG-PACIFIC-ISLANDS, automatic pool disposition automatic_pool_ready_if_not_living, and high research readiness. The resolution row describes a port, municipal, customs, shipping, merchant, labor, and local-defense provisional government, with traditional or dynastic authority only when period-correct.

The map binding keeps state 726 compact and treats state 1072 American Samoa as optional. State 726 is owned by NZL, state 1072 by USA, and the host capitals are NZL 284 and USA 361. The vanilla country history C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/SAM - Samoa.txt starts with capital 726, 20 convoys, democratic ruling party, democratic 50, fascism 6, communism 6, and neutrality 38. It has no country leader and no OOB, so a future Event 006 package must supply a grounded provisional leadership/institution contract and a non-empty force setup through the generic force pipeline.

The force row is IW-175 in 006_force_package_mapping.csv: coastal guards and local infantry, coastal_maritime, force value 50, engineers/recon/coastal signals first, no inherited navy or air, and an island-depot and shipping dependency. The officer direction is period-valid registered-tag leadership or an institutional island defence council with locally vetted officers.

### Existing and missing surfaces

The only exact IW-175 gameplay references are the planner trigger and load/reservation functions in common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt:167-174 and common/scripted_effects/006_independence_wave_packages_region_13_effects.txt:279-292, :519-528, and :754-762, plus the scenario ranking entry in common/scripted_effects/006_independence_wave_scenario_effects.txt:251-252. There is no is_independence_wave_sam_package, Samoa character, leader, AI strategy, idea, decision, focus, setup, cleanup, Event 006 localisation, portrait GFX, or DDS surface.

Vanilla SAM normal, medium, and small base SAM.tga files exist, with democratic, fascist, and communist variants. A neutrality-specific SAM variant is absent. The asset coverage ledger treats IW-175 as Group A registered base reuse, so the base flag may be retained only when the released identity and opening route are confirmed. No flag collision was found in the current audit.

### Required gate work

A Samoa candidate needs a sourced real male period leader or source-locked archival material of the actual provisional institution. The source must distinguish chiefly, colonial, municipal, labor, and shipping roles rather than inventing a generic Polynesian officeholder. No Samoa-specific source row is currently present in the real portrait and symbol ledger.

After source clearance, the parent would need the same complete package surface as Fiji, plus an explicit decision about whether American Samoa state 1072 is only an optional extension or should remain outside the first release. The cross-host NZL/USA survival proof must be rerun after any extension change. No Samoa promotion is authorized by this audit.

## IW-179 Micronesia baseline and failure disposition

IW-179 has the same RG-PACIFIC-ISLANDS group and anchor 684, but it is not a current candidate after the source retry. Its implementation surfaces are the strongest of the three Pacific island packages: FSM_independence_wave_inter_island_congress_chair in common/characters/006_independence_wave_pacific_characters.txt:31-43, the portrait sprite GFX_portrait_FSM_independence_wave_inter_island_congress_chair in interface/006_independence_wave_pacific_portraits.gfx:16-18, FSM ideas, eight FSM settlement decisions, Pacific AI, setup/lifecycle/cleanup, localisation, FORM-48 membership, and force row 46.

The current localisation names the fictional leader Elias Kihleng at localisation/english/006_independence_wave_pacific_l_english.yml:13-14. The source retry docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw179_micronesia_henry_nanpei_source_retry_2026_07_26.md records PN01036 as image-unavailable, HF01005 as a 120x168 thumbnail with unresolved rights, and the UHM Mok item as identity/era-incompatible. No crop, repaint, PNG, DDS, or runtime source was produced. Do not upscale HF01005, do not feed it to ImageGen, and do not retain Elias Kihleng as grounded evidence.

## Country package coverage checklist

| Surface | HAW IW-173 | FIJ IW-177 | SAM IW-175 | FSM IW-179 baseline |
| --- | --- | --- | --- | --- |
| Registered tag, anchor, reservation group | Present; HAW, 629, RG-629 | Present; FIJ, 636, RG-PACIFIC-ISLANDS | Present; SAM, 726, RG-PACIFIC-ISLANDS | Present; FSM, 684, RG-PACIFIC-ISLANDS |
| Current map ownership and host survival | Ready; USA retains capital 361 | Ready; ENG retains capital 126 | Ready; NZL/USA retain capitals 284/361 | Ready; JAP retains capital 282 |
| Existing Event 006 leader consumer | Vanilla three-person roster, all currently generic sprites | None | None | Custom chair exists but is fictional and blocked |
| Existing focus/decision/idea/AI package | Present | Absent | Absent | Present for additive FSM route |
| Existing flag family | Group A base reuse; democratic-specific variant absent | All four ideology variants | Base plus democratic/fascist/communist; neutrality-specific absent | Base plus communist/fascist; democratic/neutrality-specific absent |
| Sourced male portrait evidence | Failed HAW trial; no runtime asset | None in current ledger | None in current ledger | Failed source retry |
| Exact runtime content attestation | Absent | Absent | Absent | Absent |

## Required evidence before any future promotion

1. Confirm the package identity, tag, anchor, reservation group, current owner, host protected-state witness, and full collision scan against the current map and installed Workshop set.
2. For every visible personal leader or commander, obtain an unchanged attributed archival source with a defensible rights chain, an exact source-pixel crop and equality JSON from extract_portrait_source_crop.py, a source-locked identity-preserving repaint, deterministic 156x210 processing, an independent likeness/style/provenance PASS, and a final DDS hash that matches the approved PNG. Do not create advisor, dossier, operative, commander, or _small derivatives unless the package audit explicitly proves a separate full-size consumer and source.
3. For a collective leader, prove that the office is genuinely collective and use authentic all-male archival material of that exact institution. An invented council, generic crowd, or unnamed archive photograph does not satisfy the grounded gate.
4. Reuse a vanilla flag triplet only after confirming that the flag's identity and origin match the released package and route. Record the normal, medium, and small files and any ideology-specific gaps in the asset manifest.
5. Complete country gameplay surfaces: character and leader metadata, party and politics, starting ideas and lifecycle, decisions/missions, focus or generic-tree guard, AI, force receipt, technology, industry, supply, production, localisation, cleanup, scenario adapter, and formable/route membership where applicable.
6. Add the exact package ID to the canonical attestation OR block only after the source, asset, country-package, map, and post-wire audits pass. Re-run automatic weight, ordinary release, joint Event 005, scenario, and allocation-group checks. Do not use the legacy generic readiness flag.

## Collision and static-check evidence

The current collision report docs/plans/006_independence_wave_plans/tag_audit/006_installed_tag_collision_audit_2026_07_26.md records 206 registry rows, 102 reserved Event 006 tags, 91 registered vanilla-tag reuse rows, zero reserved-tag collisions, and zero custom cosmetic collisions. The companion CSVs 006_installed_tag_collisions_2026_07_26.csv and 006_installed_custom_cosmetic_collisions_2026_07_26.csv contain headers but no collision rows. No SAM, FIJ, HAW, or FSM entry appears in the manual fuzzy-identity dispositions.

The following task-specific checks were run from the mod root:

- Import-Csv counts: registry 206, research resolution 206, current map bindings 206. Each of IW-173, IW-175, IW-177, and IW-179 has one row in each source.
- Registry crosswalk: HAW/629/RG-629, SAM/726/RG-PACIFIC-ISLANDS, FIJ/636/RG-PACIFIC-ISLANDS, and FSM/684/RG-PACIFIC-ISLANDS match the map-binding CSV and reservation-group CSV.
- Canonical attestation extraction: none of IW-173, IW-175, IW-177, or IW-179 appears in the exact OR block at 006_independence_wave_package_dispatch_triggers.txt:55-68.
- Dedicated-surface scan: exact IW-175 and IW-177 hits are limited to region-13 planner/load/reservation code and scenario ranking. No Samoa or Fiji character, leader, AI, idea, decision, focus, setup, cleanup, Event 006 localisation, portrait GFX, or DDS surface was found.
- Vanilla flag scan: FIJ has 12/12 normal, medium, and small files for the four ideology variants; SAM has 9/12 including all three base files; HAW has 9/12 including all three base files; FSM has 6/12 including all three base files. The asset ledger's Group A rule authorizes base reuse only after identity and route confirmation.
- Vanilla country history scan: SAM and FIJ have no create_country_leader and no OOB; HAW creates the three personal leaders listed above; FSM has no usable vanilla political leader and depends on its Event 006 custom chair.

## Recommendation and blockers

If the parent needs one next implementation target, use IW-173 HAW only as a conditional source-research target, because it has the complete package surfaces and a separate RG-629 group. It is not ready for runtime attestation. The parent should not edit HAW history or force a generic portrait while seeking a stronger source.

If the parent instead wants a new package design rather than a source-repair tranche, use IW-177 Fiji before IW-175 Samoa. Fiji has the cleaner single-state map, complete flag variants, and slightly stronger force row. It still requires a broad country package and a sourced male or exact institutional leader, so it cannot be promoted as a small patch.

Keep IW-175 Samoa as the mutually exclusive backup for the Pacific group. Do not plan Samoa and Fiji as simultaneous automatic admissions. Resolve the 1072 American Samoa extension and the absent neutrality-specific flag variant during package design.

Keep IW-179 FSM blocked until a new full-resolution, rights-cleared, identity-valid male Micronesian source arrives. Its existing gameplay package is useful as a structural precedent, not as evidence of visual readiness.

### Simplifications, omissions, and blockers

- No candidate is currently fully gate-ready; this handoff does not claim admission.
- No Samoa or Fiji package implementation exists beyond planner, reservation, and scenario-ranking hooks.
- HAW's current vanilla leader roster uses generic sprites, and its only tested sourced replacement failed independent likeness review.
- FSM's current leader localisation and DDS are fictional/blocked and remain untouched.
- No new portrait source, flag, GFX, DDS, character, focus, decision, AI, localisation, or gameplay file was created or edited.
- Live Hearts of Iron IV execution and consumer validation were not run, as required by repository policy; all findings are static and source-ledger based.

# IW-018 ARX Sardinia country-package audit v60

Date: 2026-08-01.

Scope: ARX country registration, Sardinian anchor and host setup, politics and characters, portraits and flags, focus and decision surfaces, ideas, dynamic force package, AI, localisation, cleanup, and Event 006 runtime admission.

Status: The ARX gameplay package has broad Level 1 coverage, but runtime admission is closed and the package must not be promoted or wired with candidate portraits.

## Executive result

- `ARX` is registered at `common/country_tags/006_independence_wave_countries.txt` and points to `common/countries/006_independence_wave_ARX.txt`.
- The dynamic package retains the accepted IW-018 identity, Sardinian anchor state `114`, normal host `ITA`, Mediterranean region, Civic Cohesion framework, six-focus module, decision mission, FORM-05 ambition, and dynamic force profile `p18`.
- The exact execution blocker is `has_independence_wave_runtime_package_content_attestation_for_execution_id` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`: the adapter list includes `iw_018`, but the compile-time content-attestation OR list omits `constant:independence_wave_package_id.iw_018`.
- `is_independence_wave_runtime_package_preflight_ready` and `is_independence_wave_scenario_preflight_ready` both require that attestation, so automatic release and scenario dispatch fail closed for IW-018 even though an IW-018 scenario branch exists.
- The character and GFX roster is not source-approved for promotion. Existing DDS files are present for Emilio Lussu, Vittorio Pala, and Gavino Piras, but the current source-of-truth and source handoffs keep the Lussu likeness review open, the Pala crown role and owner unresolved, and the Piras/Vernè commander candidate-only.
- No narrow safe gameplay patch is appropriate. Adding IW-018 to the attestation registry or wiring candidate portraits would bypass the accepted fail-closed admission contract.

## Country package coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Tag and country shell | Covered | `ARX`, `common/country_tags/006_independence_wave_countries.txt`; western European graphical culture and colour in `common/countries/006_independence_wave_ARX.txt`. |
| Static history | Covered by design | `history/countries/ARX - Sardinia.txt` sets vanilla laws and recruits the five intended characters; territory, OOB, production, and technologies are assigned by the runtime package. |
| Anchor and host | Covered in runtime contract | `independence_wave_setup_iw_018_sardinia` and `has_prepared_independence_wave_iw_018_package` require state `114` ownership/control, `ITA` as protected former host, and capital state `114`. |
| Release and rollback | Covered in runtime contract | IW-018 adapter, anchor transfer, protected-host-state check, dynamic ledger, and cleanup are implemented in the Event 006 package effects and dispatch triggers. |
| Government and parties | Covered | Constitutional assembly, labour, crown consultative, and mountain guard installers set politics, party names, leaders, route ideas, and exclusions. Patron and radical routes are explicitly excluded. |
| Leader and commanders | Partially covered, admission blocked | `ARX_sardinian_provisional_assembly`, `ARX_sardinian_crown_consultative_council`, and `ARX_gavino_piras` are wired in characters; grounded portrait/source approval is incomplete. |
| Advisors | Covered without custom art | `ARX_michele_corda` and `ARX_efisio_satta` are portraitless advisors with scoped availability and correct IW-018 setup gates. No advisor sprite is required by the package contract. |
| Focus tree | Covered | Six ARX focuses in `common/national_focus/006_independence_wave_focus.txt`, with prerequisites, route gates, reward effects, icons, and localisation. |
| Decisions and mission | Covered | ARX category, one timed mission, and eight project decisions in `common/decisions/006_independence_wave_mediterranean_decisions.txt`, each with ARX, capital-control, project-lock, cost, completion, timeout, and failure logic. |
| Ideas | Covered | Crisis, reconstruction, constitutional, labour, crown, and mountain guard ideas in `common/ideas/006_independence_wave_mediterranean_ideas.txt`, all ARX-scoped and localised. |
| Dynamic force | Covered by runtime dependency | `p18` maps to coastal-maritime profile, military tradition `52`, five reinforcement paths, navy inheritance, no air inheritance, and current-generation mapping checks. |
| Economy and logistics | Covered by runtime dependency | Host-tech/research inheritance and dynamic stockpile/division generation are supplied by `006_independence_wave_force_effects.txt`; static history intentionally has no OOB or production lines. |
| AI | Covered | Survival, founding restraint, host-threat emergency, civic-maritime, and crown/guard strategies are present in `common/ai_strategy/006_independence_wave_mediterranean.txt`. |
| Flags and icons | Covered | ARX base and ideology flags, two ARX focus icons, two decision icons, shared Mediterranean idea icons, and report sprite paths exist. |
| Localisation | Covered | Country, party, character, advisor, focus, decision, mission, idea, tooltip, and report keys are present in the Mediterranean English localisation file. |
| FORM-05 and league | Covered in runtime contract | ARX setup assigns Mediterranean island league family, ambition and league state, and the `authorize_form05_delegation_focus` reward remains gated by network membership. |
| Cleanup | Covered | `independence_wave_cleanup_iw_018_sardinia` removes ARX decisions, mission, ideas, route and project flags, variables, lifecycle state, and setup flags. |

## File surface checklist

### Identity, history, and map

- `common/country_tags/006_independence_wave_countries.txt`: `ARX = "countries/006_independence_wave_ARX.txt"`.
- `common/countries/006_independence_wave_ARX.txt`: ARX graphical culture and colour shell; runtime owns the dynamic country state.
- `history/countries/ARX - Sardinia.txt`: vanilla `civilian_economy`, `export_focus`, `volunteer_only`, and the five ARX character recruitments.
- Vanilla reference `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/114-Sardinia.txt`: state `114` has Sardinian provinces, `ITA` ownership, ITA/SPM cores, two ports, airbase, one industrial complex, infrastructure, victory points, and coal.
- No Chaos Redux static state/map override was found for state `114`; the runtime adapter owns transfer and rollback. No static map defect was found in this audit.

### Politics, characters, and assets

- `common/characters/006_independence_wave_mediterranean_characters.txt`: `ARX_sardinian_provisional_assembly`, `ARX_sardinian_crown_consultative_council`, `ARX_gavino_piras`, `ARX_michele_corda`, and `ARX_efisio_satta`.
- `interface/006_independence_wave_mediterranean_portraits.gfx`: `GFX_portrait_ARX_independence_wave_emilio_lussu`, `..._vittorio_pala`, and `..._gavino_piras` full-size sprite definitions only.
- `gfx/leaders/006_independence_wave/portrait_ARX_independence_wave_emilio_lussu.dds`, `..._vittorio_pala.dds`, and `..._gavino_piras.dds` exist as 156x210 uncompressed DDS files, but their byte identity to an approved source/repaint package is not established by the current handoffs.
- `gfx/flags/ARX.tga`, `ARX_communism.tga`, `ARX_democratic.tga`, `ARX_fascism.tga`, and `ARX_neutrality.tga` exist.
- `common/ideas/006_independence_wave_mediterranean_ideas.txt`, `interface/006_independence_wave_mediterranean_assets.gfx`, and the associated focus, decision, idea, and report DDS files provide complete icon coverage.

### Focus, decisions, and runtime package

- `common/national_focus/006_independence_wave_focus.txt`: `independence_wave_arx_reconcile_municipal_ledgers_focus`, `...restore_cagliari_shipping_office_focus`, `...organize_mountain_guards_focus`, `...settle_italian_property_focus`, `...convene_island_settlement_focus`, and `...authorize_form05_delegation_focus`.
- `common/decisions/006_independence_wave_mediterranean_decisions.txt`: `independence_wave_arx_sardinia_category`, `...hold_island_authority_together`, and the eight ARX project decisions for ledgers, shipping, guards, constitution, labour, crown, mountain guard, and maritime congress.
- `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt`: route installers, IW-018 setup, focus rewards, Form-05 reward, and ARX cleanup.
- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt`: ARX package identity, roster, setup preflight, prepared proof, and complete proof.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`: adapter and scenario branches are present, but content attestation excludes IW-018.
- `common/script_constants/006_independence_wave_force_package_constants.txt`: `p18` coastal-maritime profile, tradition `52`, reinforcement mask `647`, inheritance mask `1`, and no air inheritance.
- `common/scripted_effects/006_independence_wave_force_effects.txt`: dynamic divisions, equipment, host-tech/research inheritance, and navy/air transfer.

## Findings and blockers

### Runtime admission

`has_independence_wave_runtime_package_adapter_for_execution_id` recognizes `iw_018`, and the scenario preflight has an IW-018 tag branch, but `has_independence_wave_runtime_package_content_attestation_for_execution_id` has no IW-018 OR arm.

Because `is_independence_wave_runtime_package_preflight_ready` requires both adapter and content attestation, normal activation cannot pass, and the scenario preflight also fails its top-level attestation requirement.

This is a deliberate fail-closed gate until the source roster and complete runtime evidence are accepted. It is not a safe local patch for this audit.

### Portrait and role admission

- `ARX_sardinian_provisional_assembly` uses the Emilio Lussu name and existing full-size sprite. The v15 source handoff is source-only and marks the likeness/era review open; the source-of-truth map records the earlier 1916 repaint trial as failed likeness and unwired. The contradictory resume-packet sentence claiming that Lussu is sourced, processed, and wired must be reconciled before visual admission.
- `ARX_sardinian_crown_consultative_council` uses `ARX_vittorio_pala`. The current crown candidate is Luigi Arborio Mella di Sant'Elia, but the exact 1936 owner/role fit is unresolved, and the handoff records the candidate as review-only.
- `ARX_gavino_piras` is a corps commander using the existing Gavino Piras full-size sprite. Vittorio Vernè is only a source-locked candidate in the v13 audit and is not wired; Giuseppe Valle is already owned by Kaiserreich as `SRD_giuseppe_valle`, while Pizzorno is below the accepted portrait quality threshold.
- Do not replace characters, add candidate DDS files, add a generated portrait fallback, or add IW-018 to attestation until a source-locked roster, role review, repaint audit, byte-match, and runtime evidence are accepted.

### Map and state setup

No static map or state defect was found. State `114` is a valid Sardinian one-state anchor with the expected Italian host, port and infrastructure footprint, and the runtime contract checks ownership, controller, capital, and protected host ownership before completion.

The remaining risk is runtime-only transfer/rollback evidence, which belongs to the parent completion pass and must not be substituted with a static state override.

### Politics, parties, and playability

The four route installers are coherent with the accepted Mediterranean design: constitutional and labour routes promote the provisional assembly, the crown route promotes the consultative council, and the mountain route promotes Gavino Piras. Route ideas, party names, ideology setup, exclusions, power struggle, cohesion, league, ambition, and FORM-05 state are all represented.

The two portraitless advisors are correctly scoped to ARX and IW-018 setup completion. No missing advisor art is a package defect because the accepted contract does not require custom advisor sprites.

### Focus, decisions, ideas, and localisation

The six-focus module has route-aware prerequisites, shared framework gating, reward effects, and complete icon/localisation coverage. The ARX decision category has the timed mission and eight project decisions with costs, capital-control checks, active-project locking, completion, timeout, and failure cleanup.

The six ARX idea surfaces and their names/descriptions are localised. No focus, decision, idea, party, country, character, advisor, or report localisation gap was found.

### Military, technology, industry, supply, and production

Static ARX history intentionally contains no OOB, production lines, equipment stockpiles, or technology list. The runtime force system supplies the `p18` coastal-maritime opening force, five reinforcement pathways, host technology/research inheritance, stockpiles, and approved navy inheritance while disabling air inheritance.

The p18 mapping and postproof require current-generation force state and exact pathway flags. No ARX-specific force mapping defect was found; confidence remains dependent on the runtime transaction being admitted and exercised by the parent.

### AI

The ARX survival strategy builds the expected island infantry, support, artillery, train, convoy, infrastructure, and dockyard profile. Founding restraint, host-threat emergency, civic-maritime, and crown/guard route strategies are present, and no stale ARX strategy reference was found.

### Documentation consistency

`006_independence_wave_resume_packet.md` currently says that Emilio Lussu is sourced, processed, and wired, while `006_source_of_truth_map.md` and the v15 source handoff preserve the old failed likeness trial and source-only status. This is a documentation contradiction, not evidence that the portrait is approved. The parent or documentation curator should reconcile it before an admission decision.

## Validation performed

- Read the required offline Paradox wiki pages and relevant vanilla country/state, effects, trigger, and script-constant documentation before auditing.
- Checked all listed ARX gameplay and asset files exist and traced the exact ARX identifiers through tag registration, history recruitment, characters, GFX, focus, decision, idea, AI, setup, cleanup, and dispatch surfaces.
- Verified the three ARX leader/commander DDS files are 156x210 uncompressed DDS files and confirmed the expected ARX flags and focus/decision/idea icon paths exist.
- Compared the ARX setup and prepared-proof trigger requirements with the p18 force constants and dynamic force effects.
- Read the vanilla state `114-Sardinia.txt` and confirmed no static map override is needed for the accepted runtime transfer design.
- No in-game launch or live consumer validation was performed, as required by repository instructions.

## Changes made

- Added this audit handoff only: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw018_arx_country_package_audit_v60_2026_08_01.md`.
- No gameplay, character, GFX, DDS, localisation, map, or attestation files were changed.

## Simplifications, omissions, and blockers

- IW-018 remains excluded from runtime content attestation and therefore is not executable through normal or scenario preflight.
- No candidate crown or commander portrait was promoted, and no generated/fallback portrait was added.
- Lussu source and likeness admission remains unresolved despite existing runtime DDS/GFX files.
- No custom advisor art, small portraits, dossier sprites, or commander miniatures were added because they are not required by the accepted ARX contract.
- Runtime transfer, dynamic force transaction, and post-release rollback still require the parent’s normal task-specific validation after the source roster and attestation gate are legitimately cleared.

## Recommended parent sequence

1. Reconcile the Lussu status in `006_independence_wave_resume_packet.md`, `006_source_of_truth_map.md`, and the v15 source handoff.
2. Obtain an accepted crown-route owner/role source and a commander source that clears ownership, role, provenance, crop, and likeness review; keep Vernè and Pinna candidate-only unless independently cleared.
3. Produce source-locked processed assets, independent visual audits, DDS byte-match evidence, and character/GFX wiring evidence without changing the ARX gameplay identity.
4. Re-run the country-package and runtime admission audits, then add IW-018 to the compile-time content-attestation registry only after all evidence is accepted by the parent.


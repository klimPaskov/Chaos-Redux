# Event 006 Europe, Mediterranean, Volga, and Near East Country Tranche Audit

Date: 2026-08-29.

Owner: `/root/event6_country_tranche_europe_med`.

Scope: IW-014 Catalonia/CAT, IW-015 Galicia/GLC, IW-043 Volga Bulgaria/CHU, IW-046 Chuvashia/CHU, IW-057 Far Eastern Republic/FER, IW-058 Assyria/ASY, IW-060 Kurdistan/KUR, IW-081 Lebanon/LEB, and IW-082 Palestine/PAL.

## Superseded note (2026-08-31)

The IW-015 row below is a pre-repair snapshot. Use `subagent_handoffs/006_event6_glc_no_additive_roster_repair_2026-08-30.md` for the current no-additive Castelao ownership decision and roster evidence. Retain this handoff for dated tranche provenance, but do not use its duplicate-Castelao ownership wording or its dated MCP-unavailable statement as current authority.

Verdict: no gameplay or central-registry patch is safe in this tranche. IW-014 is already source-complete and centrally attested. IW-015, IW-043, and IW-058 have package-local source and adapters but remain fail-closed at content attestation and join admission. IW-057 and IW-060 have package-local mechanics but remain package-local pending identity, rights, map, probability, and central-admission evidence. IW-046, IW-081, and IW-082 have planner, loader, and reservation rows but no executable Event 006 package-local source sufficient for admission.

## Authority and method

The primary design authorities were `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_6_formables_league_and_scenario.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`, `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, and `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`.

The current source-of-truth authority was `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` dated 2026-08-29, supplemented by the current country tranche audits under `docs/plans/006_independence_wave_plans/subagent_handoffs/`.

Required repository guidance and the Event 006, focus-tree, decisions-missions, event-assets, ComfyUI portrait, improvement-loop, and subagent skills were read before this audit. Offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, country creation, national focuses, technology, divisions, states, and maps were consulted. Vanilla HOI4 documentation and the corresponding vanilla country, history, character, focus, idea, flag, and AI files under `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` were used for syntax and carrier precedent.

The required `hoi4-agent-tools` MCP route is unavailable in this runtime. `C:/Users/klimp/AppData/Roaming/npm/hoi4-agent-tools.cmd --help` fails with `ERR_MODULE_NOT_FOUND` because `node_modules/hoi4-agent-tools/node_modules/@modelcontextprotocol/sdk/dist/esm/server/mcp.js` is missing. Therefore this handoff makes no fresh MCP focus, event, map, technology, GUI, or probability claim. Existing dated handoffs are treated only as bounded historical artifacts, not as current engine evidence. The installed package exposes no Technology Tree Viewer.

## Country package coverage checklist

| Package | Carrier and exact anchor | Reservation and host binding | Package-local source | Current admission | Main blocker |
| --- | --- | --- | --- | --- | --- |
| IW-014 | CAT, state 165 Catalonia | RG-165, SPR former host, capital 41 | Iberian package effects/triggers, decisions, shared ideas/AI/focus, CAT leader/history carrier | PASS; central adapter, attestation, and Join are present | FORM-07 remains a separate fail-closed formable contract; no package defect found |
| IW-015 | GLC, state 171 Galicia | RG-171, SPR former host, capital 41 | Iberian package effects/triggers, decisions, shared ideas/AI/focus | HOLD; adapter only | Duplicate real-person Castelao consumer and unresolved rights/ownership; attestation, capacity, and Join are absent |
| IW-043 | CHU, states 249 Kazan and optional 256 Chuvashia | RG-MIDDLE-VOLGA-KAZAN, SOV former host, capital 219 | IW043/IW058 package effects/triggers/focus/decisions/localisation, shared ideas/AI/characters | HOLD; adapter only, high-chaos-only | Four-institution roster is not fully rights-cleared; attestation, capacity, and Join are absent |
| IW-046 | CHU, state 256 Chuvashia | RG-MIDDLE-VOLGA-KAZAN, SOV former host, capital 219 | Region planner/loader/reservation and shared CHU mutex only | HOLD; no package adapter or attestation | No package-local setup, force application, focus/decision/idea/AI/character/cleanup source |
| IW-057 | FER, ordered state 408 Vladivostok or 409 Khabarovsk | RG-408-409, SOV former host, capital 219 | Far Eastern package effects/triggers/decisions, shared ideas/AI/focus/localisation | HOLD; package-local only | No Event 006 roster, portrait rights, flag/cosmetic packet, or central admission; Event 005 FEV art is not reusable |
| IW-058 | ASY, state 676 Mosul | RG-NORTHERN-MESOPOTAMIA, IRQ former host, capital 291 | IW043/IW058 package effects/triggers/focus/decisions/localisation, shared ideas/AI/characters | HOLD; adapter only, high-chaos-only | Civic Assembly and Levies/Guardianship visual consumers remain rights/identity unresolved; attestation, capacity, and Join are absent |
| IW-060 | KUR, runtime state 1001; research row state 421 | RG-NORTHERN-MESOPOTAMIA, current installed split, vanilla capital 800 | Kurdistan constants/triggers/effects/ideas/decisions/category/AI/localisation and shared focus callbacks | HOLD; package-local only | Runtime/public anchor mismatch, no neutral rights-cleared flag, no rights-cleared Event 006 portrait, and no central admission |
| IW-081 | LEB, state 553 Lebanon | RG-LEVANT-MESOPOTAMIA-COARSE, protected sole-state host, capital 553 | Region planner/loader/reservation and vanilla carrier only | HOLD; no package-local source | No Event 006 package effects, roster, decisions, ideas, AI, focus callbacks, localisation, or cleanup |
| IW-082 | PAL, state 454 Palestine/installed `454-Israel.txt` | RG-LEVANT-MESOPOTAMIA-COARSE, protected sole-state host, capital 454 | Region planner/loader/reservation and vanilla carrier only | HOLD; no package-local source | No Event 006 package effects, roster, decisions, ideas, AI, focus callbacks, localisation, or cleanup |

The candidate and research matrices confirm these identities, anchors, force profiles, political routes, leadership requirements, and regional sensitivity rules. The current installed-map binding ledger is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`; its `rebound_to_current_split` status for KUR must not be silently replaced by the public research anchor.

## File surface checklist

Shared runtime surfaces inspected:

- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` contains the current adapter and content-attestation gates.
- `common/scripted_effects/006_independence_wave_join_effects.txt` contains the fixed-order attested Join probe; only IW-014 is present from this tranche.
- `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt` contains the target loaders, weight wrappers, and reservations for all nine IDs.
- `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt` contains planner wrappers for all nine IDs, but planner visibility is not admission.
- `common/national_focus/006_independence_wave_focus.txt` is the shared Event 006 generic tree. `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` is the CHU/ASY extension.
- `common/decisions/006_independence_wave_iberian_decisions.txt` serves CAT/GLC. `common/decisions/006_independence_wave_far_eastern_decisions.txt` serves FER. `common/decisions/006_independence_wave_frontier_decisions.txt` serves KUR. `common/decisions/006_independence_wave_iw043_iw058_decisions.txt` serves CHU/ASY.
- `common/ideas/006_independence_wave_ideas_registry.txt` and `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` contain shared ideas and AI layers.
- `common/characters/006_independence_wave_characters_registry.txt` and `history/general/006_independence_wave_character_recruitment_registry.txt` contain the Event 006 character definitions and startup recruitment. FER is intentionally absent from the current startup registry.
- `common/on_actions/006_independence_wave_on_actions_registry.txt` contains shared lifecycle callbacks.
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` are the force and installed-map binding authorities.

Package-local surfaces found:

- CAT/GLC: `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`, `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`, `common/decisions/006_independence_wave_iberian_decisions.txt`, `localisation/english/006_independence_wave_iberian_l_english.yml`, and shared ideas/AI/focus callbacks.
- CHU/ASY: `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`, `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`, `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`, `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`, `localisation/english/006_independence_wave_iw043_iw058_l_english.yml`, and the corresponding shared ideas/AI/characters/recruitment surfaces.
- FER: `common/scripted_effects/006_independence_wave_far_eastern_package_effects.txt`, `common/scripted_triggers/006_independence_wave_far_eastern_package_triggers.txt`, `common/decisions/006_independence_wave_far_eastern_decisions.txt`, `localisation/english/006_independence_wave_far_eastern_l_english.yml`, and shared ideas/AI/focus callbacks.
- KUR: `common/script_constants/006_independence_wave_kurdistan_constants.txt`, `common/scripted_effects/006_independence_wave_kurdistan_package_effects.txt`, `common/scripted_triggers/006_independence_wave_kurdistan_package_triggers.txt`, `common/ideas/006_independence_wave_kurdistan_ideas.txt`, `common/decisions/006_independence_wave_kurdistan_decisions.txt`, `common/decisions/categories/006_independence_wave_kurdistan_categories.txt`, `common/ai_strategy/006_independence_wave_kurdistan.txt`, `localisation/english/006_independence_wave_kurdistan_l_english.yml`, and shared focus callbacks.

Absent package-local source confirmed:

- IW-046 has no package-local effects, triggers, setup, final validation, cleanup, decisions, ideas, AI, characters, focus callbacks, or localisation beyond the shared CHU mutex and region registry rows.
- IW-081 has no Event 006 package-local source beyond the shared region planner/loader/reservation and the vanilla LEB carrier.
- IW-082 has no Event 006 package-local source beyond the shared region planner/loader/reservation and the vanilla PAL carrier.

No parser-path or generated runtime file was removed. Existing merged receiver paths remain authoritative.

## Missing or stale country-package surfaces

The current source-of-truth map records 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. The current adapter-only set is exactly IW-013, IW-015, IW-043, IW-058, IW-093, IW-098, IW-177, and IW-179; this tranche confirms that IW-015, IW-043, and IW-058 remain in that set.

The central adapter list at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-63` includes IW-015, IW-043, and IW-058 but not IW-046, IW-057, IW-060, IW-081, or IW-082. The content-attestation list at the same file around lines 159-202 includes IW-014 but none of the other eight target IDs. The preflight around lines 204-213 requires both adapter and content attestation, so no listed planner row can bypass the gate.

The Join chain at `common/scripted_effects/006_independence_wave_join_effects.txt:248` probes IW-014 from this tranche and does not contain the other eight IDs. Adding a central attestation, capacity, or Join entry without closing the package-specific source and asset receipts would weaken the intended fail-closed contract, so no central change was made.

The current GLC audit contains older source-placeholder wording while its supplied Castelao runtime asset is marked `styled_final` with `PASS_WITH_CAVEAT / NEEDS_USER_REVIEW` rights. This is documentation drift, not grounds for a gameplay edit. Older CAT history paragraphs also remain dated in broader documents; neither was rewritten in this bounded audit.

## Map, state, anchor, former-host, and capital audit

The exact current force/binding evidence is:

- IW-014 is fixed to state 165 Catalonia, with SPR retaining capital 41 while the anchor is reserved.
- IW-015 is fixed to state 171 Galicia, with SPR retaining capital 41 while the anchor is reserved.
- IW-043 uses state 249 Kazan and may try state 256 Chuvashia, with a one-package RG-MIDDLE-VOLGA-KAZAN mutex. IW-046 uses state 256 in that same mutex, so both must remain mutually exclusive.
- IW-057 uses an ordered one-of anchor from states 408 Vladivostok and 409 Khabarovsk. The ordered event-target binding must remain intact; no fixed-state shortcut was introduced.
- IW-058 uses state 676 Mosul, with IRQ retaining capital 291 while the anchor is reserved.
- IW-060 currently uses installed state 1001, while the research matrix and FORM-18 public row name state 421 and vanilla KUR history uses capital 800. This is an unresolved binding decision, not a harmless localisation difference.
- IW-081 uses protected sole-state state 553 Lebanon and must reject a release if its host/capital safety contract is not preserved.
- IW-082 uses protected sole-state state 454, whose installed history is `454-Israel.txt`, and must reject a release if its host/capital safety contract is not preserved.

No map rewrite was attempted. The current MCP server cannot start, so there is no fresh connected province/state/supply/railway/adjacency inspection or render to report. Dated prior handoffs may be consulted by the parent for historical context but do not replace a fresh map receipt.

## Politics, leaders, portraits, flags, advisors, and parties

CAT is the only package in this tranche whose current source and rights audit supports admission. Its vanilla CAT carrier retains `CAT_lluis_companys`, state 165, and the existing flag family; no duplicate Event 006 personal portrait was added.

GLC retains the vanilla history and leaders Fuco Gómez, Alfonso Daniel Castelao, Vicente Martínez Risco, and Santiago Casares Quiroga. The Event 006 registry also recruits `GLC_independence_wave_alfonso_daniel_castelao` as a separate corps commander with a separate portrait. This is a duplicate real-person identity and has no approved guarded transfer or ownership packet. The safe choices are a guarded vanilla transfer, a distinct sourced Galician commander, or a roster/force-contract redesign; no choice is inferred here.

IW-043 exposes four male institutional consumers in `common/characters/006_independence_wave_characters_registry.txt:282-319`, recruited by `history/general/006_independence_wave_character_recruitment_registry.txt:75-81`: `CHU_independence_wave_middle_volga_congress`, `CHU_independence_wave_federal_presidium`, `CHU_independence_wave_bolgar_civic_presidium`, and `CHU_independence_wave_river_security_directorate`. Galimzhan Ibrahimov has a promoted runtime receipt, Luka Semyonovich Spasov has a bounded visual/provenance pass, while Mirsaid Sultan-Galiev and Karim Tinchurin remain source/rights/date gated. Presence of DDS/GFX files alone is not admission evidence.

IW-058 exposes four male institutional consumers in `common/characters/006_independence_wave_characters_registry.txt:322-360`: `ASY_gallo_shabo`, `ASY_independence_wave_concordat_council`, `ASY_independence_wave_civic_national_assembly`, and `ASY_independence_wave_levies_guardianship`. Barsoum has the current promoted portrait receipt. Werda is blocked by resolution/later-life/1936 continuity concerns, and Haydo/Malik remain rights/role gated. The Civic Assembly and Levies/Guardianship consumers need the portrait worker and a post-wire audit before admission.

FER has no Event 006 character, portrait, flag, or cosmetic packet. Nikiforov and Krasnoshchyokov remain research candidates only. The Event 005 FEV art and `GFX_portrait_FER_far_eastern_republic_council` are explicitly not reusable as FER evidence.

KUR retains vanilla historical leaders and commanders as carrier content, but no Event 006 KUR portrait or GFX override is rights-cleared. The package requires `independence_wave_iw_060_identity_rights_cleared` and an accepted roster receipt. No neutral 1936 pan-Kurdish flag is accepted; the Barzanji 1922-24 symbol route remains `needs_user_review` and cannot be treated as a fallback.

LEB and PAL have vanilla carriers and vanilla normal/medium/small flag families, but no Event 006 sourced male or institutional leadership packet, exact symbol review, or package-owned flag/cosmetic rights receipt. Vanilla assets do not imply Event 006 rights.

No advisors, high-command members, or commanders were invented. No custom Event 006 advisor icon is claimed. All reviewed Event 006 portrait direction remains male-only under Part 7; no female metadata or opposite-gender name pool was introduced.

## Focus, decision, idea, and asset issues

CAT has the shared generic focus tree, package callbacks, six package-relevant focus nodes, eleven decisions, one 420-day mission, seven ideas, and four AI layers recorded by its current source-complete audit.

GLC has the shared generic focus tree, p15 territorial-defense force mapping, eleven project/decision surfaces, package AI blocks, and cleanup source, but it cannot load through central release until the Castelao identity/rights issue and full admission receipts are resolved.

IW-043 and IW-058 have dedicated extension focus, decision, idea, localisation, cleanup, and AI source. The extension focus is not standalone and depends on the shared generic tree. Their FORM-12/13 and FORM-18 downstream adapters are present but remain guarded by package admission and exact anchor/consent contracts.

FER has the shared generic focus callbacks, eleven project/mission candidates, four AI blocks, and p57 regular-defectors force effects. Its settled-compact and coastal-emergency weighted paths omit setup/current-generation guards in the current audit; this is a probability-owner follow-up, not a safe local patch without the mandatory probability route.

KUR has package-local focus callbacks, an 11-project decision suite, five route installers, ideas, AI, constants, localisation, and generation-safe cleanup. These surfaces do not solve its unresolved identity, rights, and runtime/public anchor mismatch.

IW-046, IW-081, and IW-082 have no country-specific focus, decision, idea, asset, or cleanup package to audit beyond their region registry rows. They require package design/source before any central admission work.

No dedicated event-owned scripted GUI is introduced by these packages. No visual asset was generated, copied, or rewired in this audit.

## Starting military, technology, industry, supply, and production

The force mapping rows in `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` are present and read as follows: CAT p14 `regular_defectors` with tradition 72 and navy/air inheritance; GLC p15 `territorial_defense` with tradition 50 and no navy/air inheritance; IW-043 p43 `river_jungle` with tradition 62 and no navy/air inheritance; IW-046 p46 `river_jungle` with tradition 48 and no navy/air inheritance; FER p57 `regular_defectors` with tradition 67 and navy/air inheritance; ASY p58 `foreign_volunteers` with tradition 60 and no navy/air inheritance; KUR p60 `mountain_frontier` with tradition 72 and no navy/air inheritance; LEB p81 `mountain_frontier` with tradition 56 and no navy/air inheritance; PAL p82 `foreign_volunteers` with tradition 57 and no navy/air inheritance.

CAT, GLC, CHU, FER, ASY, and KUR have source-level setup/effects or vanilla carrier histories sufficient for their respective package audits, subject to the admission blockers above. IW-046 has only a p46 mapping row and no setup implementation. LEB and PAL have only vanilla carrier histories and region bindings, not Event 006 starting-force or economy implementation.

No Event 006 custom technology or doctrine is claimed for this tranche. Vanilla carrier research and OOB history were inspected for precedent, including CAT state 165, GLC state 171, CHU state 256, FER dormant state 563, ASY state 676, KUR capital 800, LEB state 553, and PAL state 454. The installed package exposes no Technology Tree Viewer, and the `hoi4-agent-tools` startup failure prevents fresh technology-tree evidence.

No map, industry, railway, port, supply, production-line, equipment, or stockpile write was made. Existing force profiles are not evidence that an unadmitted package is executable.

## AI and playability

CAT, GLC, IW-043, IW-058, FER, and KUR have source-level AI strategy or decision-weight blocks in the shared/package registries. The current typed probability audit is incomplete because the mandatory `chaosx_ai_probability_auditor` route is not callable in this runtime and the HOI4 MCP server cannot start. No AI weight or strategy-factor patch was made.

FER's current audit identifies missing setup/current-generation guards on the settled-compact and coastal-emergency weighted surfaces. This remains a known playability risk and must receive a baseline/compare probability audit before any owner-applied adjustment.

IW-046, LEB, and PAL have no package-owned AI behavior beyond generic planner scoring, so they cannot be called playable packages. KUR's package logic cannot be considered executable while identity, rights, and anchor binding remain unresolved. The shared generic focus behavior is similarly not a substitute for country-specific admission.

## Validation evidence

The following focused validators were run on 2026-08-29 from the mod root and passed:

- `python -B .tools/audit_event6_allocator.py` reported 149 publishers, 126 automatic/high-chaos selectable packages, 40 runtime adapters, 8 adapter-only fail-closed IDs, 32 attested packages, 29 compatible reservation groups, and 20 static standalone witnesses.
- `python -B .tools/audit_event6_country_api.py` reported 242 broad unique tags, 191 resolved unique carriers, zero missing, zero duplicates, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict` reported 102 registered Event 006 tags and 102 complete flag families.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 scenario/intensity cells and 8 edge-case receipts.
- `python -B .tools/audit_event6_form16.py` passed the FORM-16 contract without changing its fail-closed readiness predicates.
- `python -B .tools/audit_event6_gui_matrix.py` passed the Statehood Ledger semantic source matrix; runtime rendering/save-load evidence remains unclaimed.

No fresh HOI4 MCP inspection or render was possible because the installed server fails before startup with the missing SDK module described above. No live HOI4 launch was attempted. No probability compare was run because the required auditor/MCP route is unavailable. No map write or rollback evidence exists because no map write was requested or made.

## Change record and before/after behavior

No gameplay file, central registry, dispatch gate, Join order, focus, decision, idea, AI, portrait, flag, map, history, or asset file was changed. Before and after behavior is therefore identical: CAT remains the sole fully admitted package from this tranche; every other target remains fail-closed at the existing planner, adapter, attestation, identity, rights, or source boundary.

The only change is this dated audit handoff under `docs/plans/006_independence_wave_plans/subagent_handoffs/`.

## Simplifications, omissions, and blockers

No unapproved simplification, invented leader, invented flag, portrait fallback, generic rights fallback, map rewrite, central admission, AI balance adjustment, or content substitution was made.

Remaining blockers are package-specific: GLC duplicate Castelao ownership/rights; IW-043 incomplete sourced roster receipts; IW-046 absent package source; FER absent roster/portrait/flag/central admission; ASY incomplete Civic Assembly and Levies/Guardianship portrait and rights receipts; KUR public-versus-runtime anchor mismatch and missing identity/flag/portrait rights; LEB and PAL absent package source and leadership/symbol receipts; and the unavailable HOI4 MCP/probability/technology inspection routes.

## Parent handoff

Preserve CAT's current central attestation and Join entry. Do not add attestation, capacity, or Join entries for GLC, IW-043, or ASY until their current rights and full package audits are closed. Do not promote FER or KUR from package-local status. Treat IW-046, LEB, and PAL as design/source gaps rather than executable packages. Keep RG-MIDDLE-VOLGA-KAZAN and RG-NORTHERN-MESOPOTAMIA mutually exclusive and do not silently rebind KUR from installed state 1001 to public state 421. Obtain a working `hoi4-agent-tools` installation and the typed probability auditor before quantitative AI, focus, event, map, or technology completion claims.

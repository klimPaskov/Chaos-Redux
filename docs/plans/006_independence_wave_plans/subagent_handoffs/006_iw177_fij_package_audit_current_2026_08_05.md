# IW-177 FIJ country-package audit and admission handoff (2026-08-05)

## Verdict

**FAIL-CLOSED / no gameplay patch.** FIJ/IW-177 is internally wired as an adapter package, but it is not source-complete for central runtime content attestation. The live Event 006 authority therefore keeps IW-177 outside the content-attested set and keeps FORM-39 fail-closed.

There is no safe narrow patch that can admit standalone FIJ while the only role-matching portrait source is explicitly circa 1940s and the period-valid alternate has unresolved role, halftone, and attribution limitations. Adding IW-177 to `has_independence_wave_runtime_package_content_attestation_for_execution_id` would bypass an unresolved source gate and is not authorized.

The only file added by this audit is this dated handoff. No FIJ gameplay, country history, state, tag, GFX, DDS, localisation, focus, decision, idea, AI, formable, or central admission file was changed.

## Current authority and scope

The current Event 006 source-of-truth map and authority reconciliation handoff classify IW-177 FIJ as **adapter-only / blocked**. The current compile-time content-attested set is IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-014, IW-017, IW-018, IW-019, IW-023, IW-173, and IW-184; IW-177 is intentionally absent.

The central dispatch adapter still lists `constant:independence_wave_package_id.iw_177` and the FIJ preflight branch still requires `original_tag = FIJ`. The central content-attestation trigger does not list IW-177, so the preflight cannot pass even though the package adapter and scenario branch remain registered for later review.

The audit covers the country carrier, vanilla state/history setup, package setup and cleanup, leader and portrait consumers, flags, parties and politics, focus and decision surfaces, ideas, force/industry setup, AI strategy, localisation, and the separate FORM-39 route contract.

## Country package coverage checklist

| Surface | Result | Evidence and identifiers |
| --- | --- | --- |
| Tag registration and identity | PASS for dormant adapter; not centrally admitted | Vanilla `FIJ` remains in `common/country_tags/00_countries.txt`; `is_independence_wave_fij_package` requires `original_tag = FIJ` and package `IW-177`. |
| State ownership, capital, core, port, and map | PASS for current carrier contract | Vanilla state `636` is Fiji's capital, owned by ENG with a FIJ core in the baseline; IW-177 requires state `636` to be the owned-and-controlled anchor and capital. No Event 006 map rewrite is present. |
| Package setup and lifecycle | PASS as adapter source | `independence_wave_setup_iw_177_fiji` initializes laws, politics, ledgers, focus assignment, route exclusions, formable-family selection, force mapping, AI profile, and lifecycle flags. |
| Cleanup and release safety | PASS as adapter source | `independence_wave_cleanup_iw_177_fiji` removes the six decisions and mission, FIJ ideas, ledger variables, setup/lifecycle/AI flags, formable-family selection, the route-adapter flag, and the temporary FIJ leader. |
| Politics and parties | PASS for dormant package | FIJ setup applies the centralized Pacific baseline laws and sets four FIJ party names with democratic, communist, neutrality, and fascist popularity values from `006_independence_wave_pacific_constants.txt`. |
| Origin leader and role | PARTIAL / source-gated | `FIJ_independence_wave_founding_congress_chair` exists as the ruling country-leader consumer and is male in `common/characters/006_independence_wave_pacific_characters.txt`; the current visible identity is Ratu Sir Lala Sukuna, but the retained source is circa 1940s. |
| Portrait consumer | PROVISIONAL only | `GFX_portrait_FIJ_independence_wave_founding_congress_chair` points to the existing 156x210 DDS, but the source manifest marks it `needs_user_review` and `provisional_pending_source_date_and_package_admission`. |
| Flags | PASS for carrier; no new FIJ flag required | The package reuses installed vanilla FIJ normal, medium, and small ideology triplets. No new FIJ flag asset is required or authorized by the current source review. |
| Advisors, operatives, commanders, and small portraits | PASS / none requested | No FIJ advisor, operative, commander, dossier, or small portrait consumer is required by the package. Do not invent one to close the leader gate. |
| Focus tree assignment | PASS as dormant source | FIJ uses the full `independence_wave_focus_tree` through `generic_focus` with the assignment contract and six connected FIJ country nodes. |
| Decisions and mission | PASS as dormant source | One mission and six FIJ decisions are registered under `independence_wave_fij_founding_congress_category`; all are gated by IW-177 setup and the FIJ package trigger. |
| Ideas and lifecycle | PASS as dormant source | `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact` are allowed only for the FIJ package and are transitioned or removed by the FIJ lifecycle effects. |
| Force, technology, industry, and supply | PASS as bounded source contract | The setup requires the IW-177 force mapping, `coastal_maritime` profile, p177 tradition/force values, FIJ civilian-economy/volunteer setup, and the Pacific command structure before dynamic starting-force materialization. No new technology tree is authored. |
| AI and playability | PASS as source wiring; live behavior unverified | Three FIJ AI strategy blocks cover coastal-congress survival, founding restraint, and host threat, with constants for army, infantry, support, convoy, fuel, infrastructure, dockyard, bunker, and war-avoidance priorities. |
| Localisation | PASS for current source keys | The FIJ Pacific localisation file contains country party names, the Sukuna leader name/description, category, mission, decision, focus, idea, and tooltip keys and is UTF-8 with BOM. |
| FORM-39 / Melanesian Federation | FAIL-CLOSED by design | FIJ selects `independence_wave_formable_family.melanesian_federation` during its package setup, but the route adapter is not set. FORM-39 requires exact FIJ/PNG/WPG member research, consent, anchors, MFX reservation, reviewed flat flag, and identity-review gates. |

## File surface checklist

The following live surfaces were inspected and remain aligned for the dormant package:

- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`: FIJ identity, origin-leader, state 636 anchor, four government routes, host routes, ambition/formable selection, force mapping, AI profile, lifecycle, and final setup checks.
- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`: FIJ setup, politics, ledger/lifecycle effects, dispatch, final validation, and cleanup.
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt`: IW-177 package load and state 636 / Pacific reservation-group mapping.
- `common/scripted_triggers/006_independence_wave_packages_region_13_triggers.txt`: IW-177 state/region/anchor availability.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`: central adapter and preflight/scenario dispatch; IW-177 adapter is present but content attestation is absent.
- `common/characters/006_independence_wave_pacific_characters.txt`: `FIJ_independence_wave_founding_congress_chair`, male country-leader metadata, and provisional GFX consumer.
- `interface/006_independence_wave_pacific_portraits.gfx`: `GFX_portrait_FIJ_independence_wave_founding_congress_chair` -> `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds`.
- `common/national_focus/006_independence_wave_focus.txt` and `common/national_focus/006_independence_wave_pacific_focus.txt`: shared generic-tree import and six FIJ nodes.
- `common/decisions/categories/006_independence_wave_pacific_categories.txt` and `common/decisions/006_independence_wave_pacific_decisions.txt`: FIJ category, mission, and six decisions.
- `common/ideas/006_independence_wave_pacific_ideas.txt`: the three FIJ package ideas and lifecycle transitions.
- `common/ai_strategy/006_independence_wave_pacific.txt`: three FIJ strategy profiles and constants.
- `common/script_constants/006_independence_wave_pacific_constants.txt` and `common/script_constants/006_independence_wave_force_package_constants.txt`: FIJ political/ledger/mission/AI tuning and p177 force values.
- `localisation/english/006_independence_wave_pacific_l_english.yml`: all current FIJ player-facing keys.
- `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/`: source manifest, exact crops, visual evidence, and provisional DDS/GFX handoff.
- `common/scripted_triggers/006_independence_wave_form39_triggers.txt` and `common/scripted_effects/006_independence_wave_form39_effects.txt`: separate FORM-39 member, readiness, mutation, and cleanup contracts.

## Exact missing or stale surfaces

### Central admission gate

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:27` lists IW-177 in `has_independence_wave_runtime_package_adapter_for_execution_id`.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:79-101` lists the current content-attested packages and omits IW-177. This omission is the correct fail-closed state until the visual/source and package audit gates pass.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:183-186` keeps the exact FIJ preflight identity branch, but it cannot be reached through `is_independence_wave_runtime_package_preflight_ready` without content attestation.

The scenario dispatch branch at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:305-306` remains registered for IW-177 and still checks exact FIJ availability; it is not a promotion.

### Portrait source and processing

The current source authority is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fij_source_research_current_2026_08_03.md` and the retained manifest `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/source_manifest.json`.

Ratu Sir Lala Sukuna is the strongest identity and role match for the existing founding-congress-chair concept, but the National Archives of Fiji source is explicitly circa 1940s and therefore outside the strict 1936 baseline. The existing identity-preserving repaint, 156x210 candidate, visual audit, and provisional DDS do not waive the date gate.

Pt. Vishnu Deo has a period-valid October 1929 source, but the candidate is not a Legislative Council member during the 1936 baseline, the surviving image is an anonymous halftone, and the role/rights/likeness decision is unresolved. It cannot silently replace Sukuna while keeping the current council-chair localisation.

The user-approved unchanged sourced-crop policy would allow a source placeholder path of exact source crop -> deterministic 156x210 -> DDS once identity, date/era, rights, crop, and independent review gates pass. It does not waive the unresolved Sukuna date or Vishnu Deo role/attribution gates.

### FORM-39 route and identity

`common/scripted_triggers/006_independence_wave_form39_triggers.txt:105-113` requires `independence_wave_fij_melanesian_route_adapter_complete`, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, `independence_wave_form39_identity_review_complete`, and the exact researched FIJ/PNG/WPG member packages before readiness can be registered.

The exact member/anchor contract is FIJ state 636, PNG state 523, and WPG state 669. `docs/events/006_independence_wave/form39_melanesian_federation.md` records that the route is negotiated and exact-member only; generic pan-Papuan substitutes and geographic scans are forbidden.

The MFX flat flag package under `docs/assets/006_independence_wave/form39_melanesian_federation_identity_2026_07_27/` remains `needs_user_review`. MFX is a candidate/reservation identity, not an approved runtime tag. No advisor or dossier icon is required.

The FIJ package setup intentionally selects the Melanesian family but does not set the route-adapter flag. FIJ cleanup clears that flag if a later route adapter is researched and used. No standalone FIJ patch should set it early.

## Map and state setup

The vanilla carrier remains coherent: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/FIJ - Fiji.txt` uses capital `636`; vanilla state `636-Fiji.txt` is owned by ENG, has a FIJ core, and contains Fiji's port and victory point. The package requires that anchor to be owned and controlled by the active FIJ country and that its capital remain state 636.

No Event 006 map rewrite, railway rewrite, supply rewrite, state split, or new FIJ history file is present. The IW-177 package uses the current map and the Pacific reservation group. Map/state mutation for FORM-39 remains separately gated and anchor-only.

## Politics, leader, portrait, flag, advisor, and party issues

The package initializes democratic, communist, neutrality, and fascist popularity from central FIJ Pacific constants and installs the four FIJ party-name pairs in `independence_wave_initialize_fij_politics`.

The leader key `FIJ_independence_wave_founding_congress_chair` is present, has male metadata, and is consumed as the ruling FIJ origin leader. The visible localisation currently names Ratu Sir Lala Sukuna, matching the strongest role candidate but not the unresolved source date.

The portrait sprite and DDS are present only as provisional consumers. The DDS is 156x210, 131168 bytes, and currently hash `31fea5eb5c7c4b6f34ec138ed6a3168a7c6c39755a992bd6abf0296c5838d2c6`; this confirms dimensions and wiring, not admission.

The carrier reuses vanilla FIJ flags and needs no new flag asset. There is no advisor, operative, commander, dossier, or small portrait request in the FIJ package, and none should be fabricated to close the source gate.

## Focus, decision, idea, and asset issues

The shared `independence_wave_focus_tree` imports the FIJ country surface and the package assigns it through the full-framework contract. The six bespoke FIJ focuses are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus`.

The FIJ decision category is `independence_wave_fij_founding_congress_category`. Its timed mission is `independence_wave_fij_hold_constituent_congress_together`, and its six decisions are `independence_wave_fij_convene_constituent_congress`, `independence_wave_fij_register_communal_veto`, `independence_wave_fij_open_labor_shipping_board`, `independence_wave_fij_settle_colonial_accounts`, `independence_wave_fij_charter_coastal_guard`, and `independence_wave_fij_ratify_island_compact`.

The three package ideas are `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact`. The country localisation file covers their names, descriptions, focus text, decision text, mission text, tooltips, party names, and leader strings.

No FIJ icon or asset gap was found in the current source audit. The remaining asset issue is admission provenance, not missing art wiring.

## Starting military, technology, industry, supply, and production issues

The vanilla FIJ baseline is intentionally retained: capital 636, basic infantry equipment, convoy stock, no custom OOB, democratic 1936 elections, and the vanilla state 636 naval base and supply geography.

The IW-177 setup requires the Pacific command structure, command roster readiness, force mapping package `IW-177`, `coastal_maritime` profile, p177 force/tradition tuning, civilian-economy and volunteer laws, and dynamic starting-force application. The force constants include p177 tradition/force value `53`, reinforcement mask `659`, navy-only inheritance mask `1`, and research-sensitive value `0`.

No technology tree is added by the FIJ package. The installed MCP package exposes no Technology Tree Viewer, so technology-tree inspection remains an unresolved tooling limitation; this audit does not claim technology render or live materialization proof.

No major army, navy, air-force, equipment, manpower, production-line, railway, or supply expansion was introduced by this audit. Live starting-force materialization, industry balance, fuel/convoy behavior, and save/load persistence remain user-owned runtime checks after admission.

## AI and playability issues

The FIJ AI surface is source-complete for the dormant adapter. `independence_wave_fij_coastal_congress_survival` prioritizes army, infantry, support, convoys, fuel, infrastructure, and dockyards; `independence_wave_fij_founding_restraint` discourages early wars while Fiji is weak; and `independence_wave_fij_host_threat` adds coastal defense when the former host becomes a severe threat.

The static AI blocks use valid FIJ package flags and constants, but this audit does not claim live focus selection, production behavior, host-survival timing, force materialization, or post-load persistence. Those checks require an admitted package and a player-owned runtime observation.

## Validation performed

The scoped country-tag surface audit was run with `python -B .tools/audit_chaosx_country_tags.py --surface-scan`; it reported 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.

The central dispatch scan confirmed IW-177 appears in the adapter list at line 27 and has no entry in the content-attestation block at lines 79-101. The FIJ package setup trigger contains no `independence_wave_fij_melanesian_route_adapter_complete` requirement, confirming standalone FIJ setup and FORM-39 route readiness remain separate.

The provisional DDS header and hash were checked directly: `DDS ` magic, width 156, height 210, 131168 bytes, and hash `31fea5eb5c7c4b6f34ec138ed6a3168a7c6c39755a992bd6abf0296c5838d2c6`. The GFX sprite path exists and points to that DDS.

The FIJ English localisation file was checked for UTF-8 BOM and the leader key; both are present.

Read-only focus inspection was attempted through the installed HOI4 agent tools, but the generic tree response exceeded the retained output window. Static focus source coverage and the earlier focus audit remain the usable evidence for this handoff.

## Skipped meaningful validation

No Hearts of Iron IV process was launched, and no game log, live save, save/load cycle, allocator run, host-transfer observation, AI timing observation, force-materialization observation, FORM-39 consent scenario, or in-game focus render is claimed.

No technology-tree render was performed because the installed package exposes no Technology Tree Viewer. No FORM-39 flag or identity review was repeated because the package remains `needs_user_review` and the route is intentionally fail-closed.

## Before/after and remaining risk

Before this audit, FIJ was adapter-only with a provisional leader DDS/GFX consumer, unresolved source/date evidence, and FORM-39 late-binding gates. After this audit, the same fail-closed state is documented with current authority and targeted validation; no runtime behavior or admission gate changed.

The next safe admission files are the current source manifest and independent portrait audit under `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/`, a user-approved pre-1937/1936-attributed Sukuna-equivalent source or an explicitly accepted era exception, and the named FORM-39 FIJ/PNG/WPG route-adapter research/consent package. Only after those gates pass should the parent consider adding IW-177 to the central content-attestation list and performing a fresh post-wiring audit.

## Parent handoff

No gameplay patch is recommended or made. Keep `IW-177` outside central content attestation, keep the provisional Sukuna DDS/GFX consumer marked source-only, preserve vanilla FIJ flags and state/history, and keep FORM-39 unreachable until its exact member, consent, collision, flag, identity, and route-adapter gates are independently attested.

No simplification, fallback, generic leader, opposite-gender name pairing, new advisor art, or unapproved identity substitution was introduced.

# Event 006 country registration and playable-package audit v103

Date: 2026-08-02

Scope: Current Event 006 country registration, dormant history, map binding, package setup, opening forces, ideas, characters and portraits, AI, diplomacy and former-host relations, generic focus ownership, and fail-closed admission.

Authority: `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md`, `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, and current whole-event evidence `subagent_handoffs/006_event6_current_completion_evidence_v102_2026_08_02.md`.

## Disposition

The current country package surface is structurally covered for the fourteen exact content-attested packages, with one narrow inert-history ownership defect repaired in this audit.

The whole event remains `HOLD / PARTIAL`: 14 of 193 non-overlay rows are content-attested, 179 selectable non-overlay rows remain unattested, focus geometry retains 14 blocking diagnostics, several formable and source gates remain closed, `6001` audio remains rights-blocked, and live engine execution is not claimed.

No admission gate, allocator weight, reservation rule, package identity, formable gate, or generic-focus requirement was weakened.

## Country package coverage checklist

| Surface | Finding | Current authority |
| --- | --- | --- |
| Candidate registration | The canonical registry has 206 rows: 193 selectable non-overlay candidates and 13 route overlays. The country-tag file reserves 102 Event 006 `X` tags and explicitly reuses 91 registered vanilla tags, while overlays reserve no standalone Event 006 tag. | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`; `common/country_tags/006_independence_wave_countries.txt`; `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md` |
| Current content attestation | Exact admitted IDs are IW-001, IW-002, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-017, IW-018, IW-019, IW-173, and IW-184. The central trigger is consumed by normal execution and SCN-008 preflight. | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:72-88,94-196,205-300` |
| Package dispatch | Setup, final-validation, and cleanup dispatchers cover the regional families for all admitted IDs and the reviewed but unadmitted package adapters. | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:15-73` |
| Exact tag identity | Attested bindings are SCO, WLS, BRI, AFX, AGX, RHI, BAY, AJX, ICE, COR, ARX, ASX, HAW, and HBX. Exact preflight checks pair each package ID with its immutable tag or fixed-origin proof. | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:101-194`; package-specific trigger files |
| Dormant histories | Every Event 006 `X` registration has a matching `history/countries/<TAG> - ...txt` file or uses the shared inert reservation history. Existing vanilla carriers intentionally retain vanilla histories and are initialized through runtime adapters. | `common/country_tags/006_independence_wave_countries.txt`; `history/countries/` |
| Inert reservations | All 17 `* - Unresearched Reservation.txt` files now contain only neutral dormant politics/popularity and no recruited characters, leaders, portraits, forces, or package state. They remain blocked by package readiness and cannot enter the allocator. | `history/countries/* - Unresearched Reservation.txt`; `common/countries/006_independence_wave_unresearched_reservations.txt`; `common/scripted_triggers/006_independence_wave_package_triggers.txt` |
| Map anchors | Current bindings have non-missing anchors and state IDs for all 14 admitted packages. Anchors are 121, 122, 14, 34, 36, 51, 52, 42, 100, 1, 114, 115, 629, and 378. | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` |
| Reservation groups | The 14 admitted packages use 13 compatible groups. IW-008/RHI state 51 and IW-010/AJX state 42 intentionally share `RG-RHINE-SAAR` at pair capacity two with distinct anchors. | `.tools/audit_event6_allocator.py`; `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv` |
| Host survival | Binding rows record current host owners and capital remnants. The shared planner reserves hosts before candidates, reserves all anchors before optional territory, and applies the protected-state and Event 005/Soviet-origin exclusions. | `common/scripted_effects/006_independence_wave_package_planner_effects.txt`; `common/scripted_effects/006_independence_wave_execution_effects.txt`; `common/scripted_triggers/006_independence_wave_triggers.txt` |
| Generic focus ownership | Every admitted full-framework setup calls `independence_wave_assign_focus_framework` with the full-framework input and the central final validator requires `has_independence_wave_generic_focus_contract` plus `independence_wave_generic_ai_profile`. IW-012 ICE remains the reviewed additive carrier exception. | `common/scripted_effects/006_independence_wave_focus_effects.txt:33-75`; `common/scripted_triggers/006_independence_wave_focus_triggers.txt:55-79`; `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:47-62` |
| Fail-closed admission | Candidate allocation gives positive weight only to the central content-attestation set and preflight requires exact package/tag identity, absence, origin separation, and current reservation state. IW-030, IW-043, IW-058, IW-093, IW-098, IW-173-adjacent unadmitted routes, IW-177, IW-179, and IW-184-adjacent routes remain blocked unless their current exact gates pass. | `common/scripted_effects/006_independence_wave_package_planner_effects.txt`; `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` |

### Attested package binding table

| ID | Tag | Anchor | Compact | Extension | Reservation group | Initial host |
| --- | --- | ---: | --- | --- | --- | --- |
| IW-001 | SCO | 121 | 121, 133 | 120, 136, 933 | RG-121-120-133 | ENG |
| IW-002 | WLS | 122 | 122 | none | RG-122 | ENG |
| IW-004 | BRI | 14 | 14 | none | RG-14 | FRA |
| IW-006 | AFX | 34 | 34 | none | RG-34 | BEL |
| IW-007 | AGX | 36 | 36 | none | RG-36 | HOL |
| IW-008 | RHI | 51 | 51 | 42 | RG-RHINE-SAAR | GER |
| IW-009 | BAY | 52 | 52, 53, 54 | none | RG-52-53-54 | GER |
| IW-010 | AJX | 42 | 42 | none | RG-RHINE-SAAR | GER |
| IW-012 | ICE | 100 | 100 | none | RG-100 | ICE |
| IW-017 | COR | 1 | 1 | none | RG-1 | FRA |
| IW-018 | ARX | 114 | 114 | none | RG-114 | ITA |
| IW-019 | ASX | 115 | 115 | none | RG-115 | ITA |
| IW-173 | HAW | 629 | 629 | 630, 631, 642, 727 | RG-629 | USA |
| IW-184 | HBX | 378 | 378 | none | RG-378 | USA |

## File surface checklist

| Surface | Files and identifiers | Finding |
| --- | --- | --- |
| Tag definitions | `common/country_tags/006_independence_wave_countries.txt`; `common/countries/006_independence_wave_<TAG>.txt`; `common/countries/006_independence_wave_unresearched_reservations.txt` | 102 custom reservations parse to existing country definitions. The five current Event 006-owned active definitions visible in the attested set are AFX, AGX, AJX, ASX, and HBX; reused carriers do not receive duplicate vanilla definitions. |
| History | `history/countries/<TAG> - ...txt`; vanilla histories for SCO/WLS/BRI/RHI/BAY/ICE/COR/HAW | Custom shells provide neutral dormant defaults or package-owned static character recruitment where explicitly reviewed. Runtime package effects own territory, capital, politics, ideas, forces, focus, and AI. |
| Runtime registry | `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`; `common/scripted_effects/006_independence_wave_country_registry_effects.txt`; `common/script_constants/006_independence_wave_country_registry_constants.txt` | Tag membership and origin predicates are exact and separated from readiness. Event 005/Soviet and Event 012 origin guards remain present. |
| Package planner | `common/scripted_effects/006_independence_wave_package_planner_effects.txt`; `common/scripted_triggers/006_independence_wave_package_triggers.txt` | Static force-map probe, package-attestation gate, host-first/anchor-first reservation, optional territory trimming, and rollback boundaries are present. |
| Package dispatch | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`; `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | Adapter, setup, final validation, cleanup, normal preflight, and scenario preflight are source-aligned for the current 14-ID set. |
| Forces | `common/scripted_effects/006_independence_wave_force_effects.txt`; `common/scripted_effects/006_independence_wave_force_package_effects.txt`; `common/script_constants/006_independence_wave_force_package_constants.txt`; `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` | All 206 registry rows have force-map constants and five bounded reinforcement-pathway bits. The admitted IDs resolve to p1, p2, p4, p6, p7, p8, p9, p10, p12, p17, p18, p19, p173, and p184. |
| Shared focus | `common/scripted_effects/006_independence_wave_focus_effects.txt`; `common/scripted_triggers/006_independence_wave_focus_triggers.txt`; `common/national_focus/006_independence_wave_focus.txt` and package overlay modules | Full framework is loaded only through the guarded assignment effect. Additive overlays require a reviewed carrier, and no country may pass final package validation without a usable generic focus contract and generic AI profile. |
| Politics and ideas | Package `*_package_effects.txt`, `common/ideas/006_independence_wave_*_ideas.txt`, package constants, and Event 006 localisation | Attested packages publish explicit baseline laws/popularity, route party names, route ideas, lifecycle ideas, and cleanup. |
| Characters and portraits | `common/characters/006_independence_wave_*_characters.txt`; package `.gfx`; `gfx/leaders/006_independence_wave/`; `docs/assets/006_independence_wave/` | Current admitted identities are reviewed male sourced or institutional roles under the selected no-female/no-custom-advisor-art rule. Non-admitted portrait shelf rows remain evidence-only. |
| AI | `common/ai_strategy/006_independence_wave_generic.txt`; package AI strategy files | Generic survival, recovery, and consolidation profiles require active Event 006 focus ownership and the generic AI flag. Package files add route, host-threat, founding-restraint, and regional behavior. |
| Diplomacy and former host | `common/scripted_triggers/006_independence_wave_triggers.txt`; package diplomacy effects/triggers; `common/decisions/006_independence_wave_decisions.txt` | Host negotiation, guarded frontier, association, reclamation, patron, Network, and League routes are package-gated and ledger-backed. |

## Missing or stale package surfaces

1. The current attestation boundary is intentionally narrow: 179 selectable rows remain unattested and must not be promoted from shell, map binding, force constants, or portrait-shelf presence alone.

2. IW-043 CHU and IW-058 ASY have implemented adapters but remain outside the exact content-attestation set because grounded leader/portrait and related readiness gates are unresolved.

3. IW-093 DOX and IW-098 SOK remain fail-closed for grounded leader/commander source, period flag evidence, FORM-24/FORM-25 adapters, the Kumasi province-versus-state capital proof, and the current IW-098 baseline ledger rebound.

4. IW-179 FSM remains explicitly withdrawn until its sourced real male Micronesian identity gate is set; the retained fictional chair must not be used as a fallback.

5. FORM-07, FORM-12, FORM-13, FORM-18, FORM-24, FORM-25, FORM-39, FORM-42, and FORM-48 remain family-specific readiness or member-completeness boundaries where their current audits say so.

6. The current generic focus render has 184 direct focuses and 223 prerequisite connectors but retains 14 blocking geometry diagnostics; no isolated package patch is safe from this audit.

7. The installed MCP package exposes no Technology Tree Viewer, so technology-tree rendering and compare evidence remain unresolved rather than inferred from source.

8. HAW documentation still has stale withdrawn/unwired wording in package prose, resume metadata, and export metadata even though the current HAW source and portrait audit are admitted. This is documentation cleanup, not a gameplay admission defect.

9. Older package handoffs that describe pre-attestation HOLD states are historical and must not override the current central 14-ID authority.

## Map, state, and setup issues

The current installed binding CSV reports no missing current state IDs for the 14 admitted rows.

The host owners are ENG, FRA, BEL, HOL, GER, ICE, ITA, and USA as listed in the binding table, and the planner protects former-host capitals/remnants before optional territory is published.

The shared RG-RHINE-SAAR pair is intentional and source-validated for RHI state 51 and AJX state 42; no duplicate anchor is introduced.

No static map or state defect was found in the current package binding surface.

Runtime release, ownership transfer, host survival under actual allocation, and save/load behavior remain unobserved by this audit.

## Politics, leaders, portraits, flags, advisors, and parties

The admitted package effects set baseline laws/popularity and route party names rather than relying on generic country strings.

SCO/WLS, AFX/AGX, RHI/BAY, AJX, ICE, COR/ARX/ASX, HAW, and HBX have package-specific institutional or sourced male leadership consumers and role-scoped cleanup.

The HAW route preserves vanilla David Kalakaua Kawananakoa as ruling leader and adds Samuel Wilder King only as an additive non-ruling civilian-large role.

The current ARX roster preserves stable script compatibility for `ARX_gavino_piras` while exposing sourced Vittorio Verne for the reviewed commander role; blocked identities are not silently relabelled as new people.

No opposite-gender portrait/name pairing or Event 006 custom advisor portrait registration was found in the admitted package surface.

The current portrait shelf is traceability-only for unadmitted candidates; physical DDS/PNG presence does not bypass identity, rights, role, or package admission gates.

Repaired defect: `history/countries/DJX - Unresearched Reservation.txt` previously recruited `KRG_warren_kruger`, nine `africa_priority_*` sovereigns, and 24 `utopia_manifesto_*` characters into IW-088's inert reservation history. That would give an unresolved Event 006 reservation unrelated cross-package character ownership at load time. The file now owns no characters and remains neutral/fail-closed.

## Focus, decision, idea, and asset issues

Every admitted setup calls `independence_wave_assign_focus_framework = yes` with `independence_wave_focus_assignment.full_framework` and publishes package route, host, ambition, League, and formable hooks.

IW-012 ICE is the reviewed additive carrier and requires `independence_wave_focus_carrier_registered` plus vanilla `iceland_tree`; other admitted rows use the shared `independence_wave_focus_tree`.

Package decision and mission files, ideas, icons, and localisation are present for the admitted rows, with exact package cleanup dispatch.

Unadmitted package-specific focus and decision surfaces remain visible only behind their current package, formable, source, or attestation gates.

No country-specific focus-tree creation or generic-tree expansion is justified by this package audit.

## Starting military, technology, industry, supply, and production issues

The shared force loader resolves package profile, tradition, reinforcement mask, inheritance mask, and research sensitivity from the 206-row constant table and applies dynamic opening stockpiles and formations after package setup.

The admitted packages have five bounded reinforcement pathways each, with profile-specific navy/air inheritance and host-technology/research-slot handling where the package contract requires it.

No static empty-army or missing-force-map defect was found for the 14 admitted IDs.

No Technology Tree Viewer is installed, so no technology-tree conclusion beyond source-level inheritance checks is claimed.

Live force materialisation, stockpile values, supply behavior, production lines, and save/load persistence remain unobserved.

## AI and playability issues

The generic AI profiles are active only for Event 006 countries with full or reviewed additive focus ownership and `independence_wave_generic_ai_profile`.

Package AI files cover survival, founding restraint, host threat, route politics, maritime/island, industrial, mountain, and regional priorities for the admitted package families.

Host and diplomacy behavior remains ledger-backed and uses recognition, dependency, former-host outcomes, patron influence, Network standing, and League routes.

No AI path was found that bypasses the current generic-focus or content-attestation barriers.

Live AI focus selection, front behavior, diplomacy, and long-run survival were not tested.

## Changed files and identifiers

- `history/countries/DJX - Unresearched Reservation.txt:4-17`: replaced the cross-package character block with an explicit inert-history ownership comment and retained only neutral politics/popularity; all 34 unrelated `recruit_character` entries were removed.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_country_package_audit_v103_2026_08_02.md`: recorded this audit, current package table, patch rationale, validation, and remaining blockers.
- No tags, state IDs, leaders, parties, focus IDs, localisation keys, formable IDs, admission branches, allocator weights, or assets were added or changed.

## Validation performed

- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable rows, 138 SCN-008 ranked rows, 14 attested packages across 13 compatible reservation groups, the RG-RHINE-SAAR pair capacity, and the 6/8/10/14/20 ladder.
- `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 mode/intensity cells and 8 required edge cases.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` passed with 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.
- A static registration scan found 102 Event 006 tag entries, 85 concrete country-definition files, 17 shared inert reservations, and no missing history file for a registered tag.
- A static inert-history scan found zero `recruit_character` lines in all 17 unresearched reservation histories after the DJX repair.
- A static attestation scan confirmed the exact 14 IDs in `has_independence_wave_runtime_package_content_attestation_for_execution_id` and the matching exact-tag/preflight branches.

## Skipped meaningful validation

HOI4 was not launched and no live allocator, force-materialisation, ownership-transfer, save/load, AI, or cleanup run was performed.

No map write or MCP map rewrite was used because the current binding and reservation artifacts show no static package-local map defect.

No focus rewrite was used because the current geometry diagnostics are coupled shared-tree findings and no safe isolated package coordinate patch was identified.

Technology-tree rendering/compare was skipped because the installed package exposes no Technology Tree Viewer.

## Remaining setup, identity, and admission risks

The whole-event 14/20 capacity promise remains fail-closed below admitted package and reservation capacity.

The shared focus geometry, formable readiness, sensitive identity/flag evidence, 6001 audio rights/runtime, GUI/live evidence, and catalog completion remain parent-owned blockers.

No fallback portrait, synthetic admission, generic leader, advisor icon, or shallow package substitute was introduced.

Plan handoff path: this file.

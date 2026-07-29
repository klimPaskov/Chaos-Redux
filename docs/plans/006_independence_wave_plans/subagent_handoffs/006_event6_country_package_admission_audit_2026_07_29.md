# Event 006 country package admission audit

Date: 2026-07-29.

Audited revision: `cbe1c9e7a`.

Scope: Event 006 country packages, admission and adapter surfaces, current-map bindings, leadership and asset gates, and separation from Soviet Collapse origins.

Excluded by the scoped rule: CBB, CBD, Fallout, Random Events, and unrelated country systems. `REV`, `ZIN`, and `ZZZ` remain outside the Event 006 and Soviet protected sets.

## Decision

No gameplay patch is justified by this audit.

The current static content-attestation set remains exactly eleven packages: IW-001, IW-004, IW-006, IW-007, IW-008, IW-009, IW-010, IW-012, IW-017, IW-019, and IW-184.

The adapter list is broader than the admission list by design. It contains twenty IDs, while the content-attestation and preflight contract admits only the eleven IDs above. Presence of a regional dispatcher, focus file, or generic readiness wrapper is not admission evidence.

Live allocator, reservation, dispatch, force materialization, focus visibility, AI timing, formable execution, cleanup, and save/load evidence remain open. The installed MCP exposes no Technology Tree Viewer, so package-specific technology runtime proof remains unresolved.

## Coverage checklist

| Surface | Result | Evidence |
| --- | --- | --- |
| Registry and tag policy | Covered statically | `common/country_tags/006_independence_wave_countries.txt`; `common/script_constants/006_independence_wave_package_constants.txt`; `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` |
| Adapter and admission gates | Covered statically | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-72` |
| Origin separation | Covered statically | `common/scripted_triggers/chaosx_liberation_release_triggers.txt:92-105`; `common/scripted_effects/006_independence_wave_country_registry_effects.txt:11-25`; `common/scripted_effects/005_soviet_collapse_effects.txt:5704-5718` |
| Territory and history | Static anchors and host guards present | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`; custom X history files listed below |
| Forces, ideas, and starting setup | Static package mappings present for the attested set | `common/scripted_effects/006_independence_wave_force_package_effects.txt`; package effect and idea files listed below |
| Leaders, portraits, and flags | Attested package source gates recorded; unadmitted source blockers remain fail-closed | `interface/006_independence_wave*.gfx`; `docs/assets/006_independence_wave/`; package character files |
| Focus trees and decisions | Static loaders and package routes present where attested | `common/national_focus/006_independence_wave_focus.txt`; package focus files; `common/decisions/006_independence_wave_*.txt` |
| AI, diplomacy, host, and cleanup | Static strategy and settlement hooks present | `common/ai_strategy/006_independence_wave_*.txt`; `common/scripted_effects/006_independence_wave_*_package_effects.txt`; runtime timing still open |
| Formables | Registry and fail-closed gates present | `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`; `common/decisions/006_independence_wave_formable_registry_decisions.txt`; FORM-24, FORM-25, and FORM-39 remain blocked |
| Vanilla-country exclusion | No external direct-definition or identity-surface collision | `.tools/audit_chaosx_country_tags.py --surface-scan` |

## Current static attestation set

| Package | Tag policy and tag | Anchor and reservation group | Host | Static package state |
| --- | --- | --- | --- | --- |
| IW-001 Scotland | registered reuse `SCO` | 121, compact 121\|120\|133, `RG-121-120-133` | ENG | Content-attested. Runtime allocation and host survival remain open. |
| IW-004 Brittany | registered reuse `BRI` | 14, `RG-14` | FRA | Content-attested. Runtime allocation and host survival remain open. |
| IW-006 Wallonia | new Event 006 X tag `AFX` | 34, `RG-34` | BEL | Content-attested. Custom history and flag are present. |
| IW-007 Frisia | new Event 006 X tag `AGX` | 36, `RG-36` | HOL | Content-attested. Custom history and flag are present. |
| IW-008 Rhineland | registered reuse `RHI` | 51, `RG-RHINE-SAAR` | GER | Content-attested. Shares the reservation group with IW-010 but has a distinct anchor. |
| IW-009 Bavaria | registered reuse `BAY` | 52\|53\|54, `RG-52-53-54` | GER | Content-attested. Runtime allocation and host survival remain open. |
| IW-010 Saar | new Event 006 X tag `AJX` | 42, `RG-RHINE-SAAR` | GER | Content-attested. Mutex with IW-008 is required at runtime. |
| IW-012 Icelandic emergency republic | registered reuse `ICE` | 100, `RG-100` | ICE | Adapter and route arbitration are source-closed. Binding is `ready_if_tag_not_living`; state 100 protects the vanilla host, so the exact host-survival gate must reject an unsafe release. |
| IW-017 Corsica | registered reuse `COR` | 1, `RG-1` | FRA | Content-attested. Runtime allocation and host survival remain open. |
| IW-019 Sicily | new Event 006 X tag `ASX` | 115, `RG-115` | ITA | Content-attested. Custom history and flag are present. |
| IW-184 California | new Event 006 X tag `HBX` | 378, `RG-378` | USA | Content-attested after William D. Stephens source and portrait review. Runtime portrait hash recorded as `A158A968A1E67F2F83720D1B9201369542C3AAF7318A8C6332D659D91382CAD1`. |

The custom history files for the attested new tags are `history/countries/AFX - Wallonia.txt`, `AGX - Frisia.txt`, `AJX - Saar.txt`, `ASX - Sicily.txt`, and `HBX - California.txt`.

Registered reuse tags do not receive duplicate mod history files or duplicate country definitions. Their vanilla history, flags, and meaningful trees are preserved until an origin-gated package setup runs.

## File-surface checklist

The registry and adapter surfaces are present in `common/country_tags/006_independence_wave_countries.txt`, `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt`, `common/scripted_effects/006_independence_wave_country_registry_effects.txt`, `common/collections/chaosx_country_collections.txt`, and `common/collections/006_independence_wave_country_collections.txt`.

The Event 006 execution contract is present in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_triggers/006_independence_wave_package_triggers.txt`, `common/scripted_triggers/006_independence_wave_triggers.txt`, `common/scripted_effects/006_independence_wave_execution_effects.txt`, and `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`.

The package-specific trigger and effect surfaces are present in the following files.

- `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt` and `common/scripted_effects/006_independence_wave_scotland_wales_package_effects.txt` for IW-001 and IW-002.
- `common/scripted_triggers/006_independence_wave_brittany_package_triggers.txt` and `common/scripted_effects/006_independence_wave_brittany_package_effects.txt` for IW-004.
- `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt` and `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt` for IW-006 and IW-007.
- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt` and `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt` for IW-008 and IW-009.
- `common/scripted_triggers/006_independence_wave_saar_package_triggers.txt` and `common/scripted_effects/006_independence_wave_saar_package_effects.txt` for IW-010.
- `common/scripted_triggers/006_independence_wave_ice_package_triggers.txt` and `common/scripted_effects/006_independence_wave_ice_package_effects.txt` for IW-012.
- `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt` and `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt` for IW-017, IW-018, and IW-019.
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` and `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` for IW-173, IW-177, IW-179, and IW-184.
- `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt` and `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt` for IW-043 and IW-058.
- `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt` and `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt` for IW-093 and IW-098.

The shared force and content surfaces are `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt`, `common/scripted_effects/006_independence_wave_force_package_effects.txt`, `common/national_focus/006_independence_wave_focus.txt`, `common/decisions/006_independence_wave_decisions.txt`, and `common/ideas/006_independence_wave_ideas.txt`.

Package-specific content files exist for the attested routes in `common/national_focus/006_independence_wave_iw043_iw058_focus.txt`, `common/national_focus/006_independence_wave_pacific_focus.txt`, and `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, with package decision and idea files for the regional groups. The group files are `006_independence_wave_scotland_wales`, `006_independence_wave_brittany`, `006_independence_wave_wallonia_frisia`, `006_independence_wave_rhineland_bavaria`, `006_independence_wave_saar`, `006_independence_wave_ice`, `006_independence_wave_mediterranean`, `006_independence_wave_pacific`, `006_independence_wave_iw043_iw058`, and `006_independence_wave_iw093_iw098`.

Character and portrait registration is split across `common/characters/006_independence_wave_nwe_advisors.txt`, `common/characters/006_independence_wave_wallonia_frisia_characters.txt`, `common/characters/006_independence_wave_saar_characters.txt`, `common/characters/006_independence_wave_mediterranean_characters.txt`, `common/characters/006_independence_wave_pacific_characters.txt`, `common/characters/006_independence_wave_iw043_iw058_characters.txt`, and `common/characters/006_independence_wave_iw093_iw098_characters.txt`.

Portrait and flag registration is in `interface/006_independence_wave.gfx`, `interface/006_independence_wave_region_01_portraits.gfx`, `interface/006_independence_wave_brittany_portraits.gfx`, `interface/006_independence_wave_mediterranean_portraits.gfx`, `interface/006_independence_wave_pacific_portraits.gfx`, `interface/006_independence_wave_iw043_iw058_portraits.gfx`, `interface/006_independence_wave_iw093_iw098_portraits.gfx`, and `gfx/flags/`.

No Event 006 custom advisor icon path was found. `common/characters/006_independence_wave_nwe_advisors.txt` provides advisor characters without introducing custom advisor sprites.

## Findings by required surface

### Registry, adapter, and readiness

The twenty-ID adapter OR block is at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-32`. It includes the eleven attested IDs plus IW-002, IW-018, IW-043, IW-058, IW-093, IW-098, IW-173, IW-177, and IW-179.

The eleven-ID content-attestation block is at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:59-73`. `is_independence_wave_runtime_package_preflight_ready` at `:78-84` requires an unused target tag, an adapter, an attestation, and no Event 006 or Soviet active origin.

The automatic wrappers in `common/scripted_triggers/006_independence_wave_triggers.txt` for IW-002 and IW-018 therefore remain adapter surfaces, not admission proof. The same applies to the unadmitted CHU, ASY, Pacific, Asante, and Sokoto wrappers.

### Territory, history, and map safety

Static anchors, compact and extended states, hosts, and reservation groups are recorded in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`.

IW-008 RHI and IW-010 AJX share `RG-RHINE-SAAR` but have anchors 51 and 42. The package and anchor mutex must remain package-ID-aware and must not dispatch by tag alone.

IW-043 CHU uses states 249 and 256 in `RG-MIDDLE-VOLGA-KAZAN`. IW-046 Chuvashia shares the CHU carrier at state 256, so the package mutex and anchor identity are mandatory.

IW-098 SOK has registry baseline state 558 but the installed binding records current-map anchor 902. This rebind is documented, but current ownership, controller, capital, supply, railway, port, and release behavior are not runtime-proven.

IW-012 ICE uses state 100 and the same vanilla carrier that can be a living host. Its binding is intentionally `ready_if_tag_not_living`; the host-survival gate must reject a release that would erase the 1936 ICE host.

IW-003 Cornwall has no legal current-map state binding and remains hard blocked. IW-005 Flanders is a living-BEL overlay and is not a selectable country package. Neither has a fallback release path.

No duplicate mod history file was added for reused vanilla carriers. Only the five custom X attested packages listed above have Event 006 country and history files.

### Forces, technology, industry, and supply

Static force profiles and reinforcement pathways are mapped through `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt` and `common/scripted_effects/006_independence_wave_force_package_effects.txt`. The package triggers assert package-specific force profile, military tradition, ideas, and expected reinforcement pathway count.

The audit found no live allocator result, army or navy materialization, stockpile, manpower, production line, train, fuel, supply, port, or railway proof. These are parent-owned runtime checks.

The installed MCP has no Technology Tree Viewer. Package-specific technology placement, prerequisite, unlock, and research runtime evidence therefore remains unresolved rather than inferred from the presence of generic package files.

### Politics, leaders, portraits, flags, parties, advisors, and ideas

The attested packages have static route variables, party setup, lifecycle ideas, government branches, institutional or sourced leader consumers, and package-specific flag or vanilla-carrier preservation surfaces in their group effect, character, idea, and localisation files.

The sourced-only portrait gate is still in force. The grounded generated portrait shelf is not an admission substitute. Institutional bodies use institutional names, while any real-person consumer must retain its source, date, role, likeness, and gender metadata review.

Custom Event 006 flags are present for AFX, AGX, AJX, ASX, and HBX. Reused SCO, WLS, BRI, RHI, BAY, ICE, COR, CHU, ASY, FIJ, FSM, and HAW carriers preserve their vanilla flag definitions until an origin-gated package setup runs. Exact DOX, SOK, and FORM-39 identity flags remain blockers for their unadmitted packages.

No custom advisor icons are authorized or required by the current package design.

### Focus trees, decisions, and assets

The attested set has shared framework focus loading plus the package route files listed in the file-surface checklist. IW-012 uses the vanilla `iceland_tree` with an additive overlay and four mutually exclusive routes. No package may overwrite a meaningful vanilla tree without its origin and focus-assignment gate.

Static decision files, project ledgers, route locks, former-host settlement hooks, and cleanup effects are present for the attested groups. Their visible focus, decision availability, and route timing remain runtime-open.

The current portrait shelf contains source-derived masters and manifests, but no runtime proof that every target is materialized in a new save. There are no custom Event 006 advisor icon requests in the current manifests.

### AI, diplomacy, host survival, ambitions, formables, and cleanup

Static AI strategy files exist for the regional package groups, including `common/ai_strategy/006_independence_wave_iw043_iw058_ai_strategy.txt` and `common/ai_strategy/006_independence_wave_iw093_iw098_ai_strategy.txt`. Host ledgers and settlement effects use living-former-host checks in the package effect files.

The registry and formable files are present, but formable reachability is not equivalent to package admission. FORM-01 through FORM-05 are the currently promoted family surfaces. FORM-12, FORM-13, and FORM-18 are CHU or ASY contracts but remain blocked with their packages. FORM-24 Asante and FORM-25 Sokoto remain incomplete. FORM-39 requires named FIJ, PNG, and WPG members, a Melanesian X or MFX identity package, consent transactions, and a completed flag review. FORM-48 is implemented for HBX, HAW, and FSM but unreachable while HAW and FSM remain unadmitted. FORM-42 and FORM-06 through FORM-47 remain fail-closed unless their package and identity contracts are complete.

Cleanup effects clear the Event 006 active-origin flag and mark origin ended through `independence_wave_registry_clear_event6_origin`. No cleanup runtime proof exists for annexation, return, puppet, transfer, or save/load sequences.

## Ranked unadmitted blockers

| Rank | Package and binding | Static surfaces | Blocking country-package issue |
| --- | --- | --- | --- |
| 1 | IW-043 CHU Volga Bulgaria, states 249\|256, `RG-MIDDLE-VOLGA-KAZAN` | Package effects and triggers, ideas, full focus overlay, decisions, AI lanes, host and ambition hooks, FORM-12 and FORM-13, flags, localisation, and icons exist | Four-role institutional roster is not source-cleared. Shamil Usmanov civic role is blocked by the 187x250 source. Ahmet Zeki Velidi Togan river-security role still needs rights, date, and role review. Galimzhan v2 is promoted and Mirsaid is source-ready. Evidence: `docs/assets/006_independence_wave/iw043_iw058_portrait_source_research_2026_07_28/manifest.md` and `006_iw043_iw058_country_package_final_audit_2026_07_18.md`. |
| 2 | IW-058 ASY Assyria, state 676, `RG-NORTHERN-MESOPOTAMIA` | Shared CHU/ASY package effects and triggers, ideas, focus, decisions, AI, host, and formable hooks exist | Active rights or date baseline are unclear for Mar Benyamin Shimun XXI and Mar Eshai Shimun XXIII. Naum Faiq and Agha Petros are source-ready only after a legacy-continuity decision because they died before the 1936 baseline. Full four-role roster and re-audit are required. |
| 3 | IW-177 FIJ Fiji, state 636, `RG-PACIFIC-ISLANDS` | Pacific setup and cleanup, Sukuna leadership consumer, force, industry, ideas, focus, six decisions, AI, host, flags, localisation, and source portrait surfaces exist | Ratu Sukuna portrait is circa the 1940s rather than a resolved 1936 baseline. FORM-39 has no complete named FIJ, PNG, and WPG member or consent transaction, no complete Pacific X or MFX identity package, and no completed flat-flag review. |
| 4 | IW-093 DOX Asante, state 274, `RG-GHANA-ASANTE-FANTE` | Combined DOX/SOK focus, decisions, ideas, force, command, Prempeh politics, host, AI, cleanup, icons, and localisation surfaces exist | Prempeh II visual approval is open. Generated commanders and invented identities require sourced replacements. The exact Asante flag is unresolved. FORM-24 member and sovereignty conditions are incomplete. |
| 5 | IW-098 SOK Sokoto, baseline 558 and current binding anchor 902, `RG-NIGERIA-COARSE` | Combined package surfaces exist | Muhammad Dikko portrait style is not production-safe. Vanilla Siddiq is generic. Hasan, Siddiq, and Bello Rabah need sourced real portraits. Exact flag and FORM-25 member or sovereignty contract remain incomplete. |
| 6 | IW-002 WLS Wales, state 122, `RG-122`; IW-018 ARX Sardinia, state 114, `RG-114` | Gameplay, generic adapters, route effects, and package files are retained | Visual admission was withdrawn. A production-safe, source-cleared full roster and final package asset review are missing. Their adapter wrappers must not be treated as admission. |
| 7 | IW-173 HAW Hawaii, state 629, `RG-629`; IW-179 FSM Micronesian federation, state 684, `RG-PACIFIC-ISLANDS` | Pacific and FORM-48 surfaces exist | HAW lacks a resolved leader source, rights, and likeness baseline. FSM has no production-safe Henry Nanpei source. Both remain fail-closed, so FORM-48 remains unreachable. |

Other Volga, Urals, Siberia, and Far East rows, including IW-033, IW-034, IW-036, IW-040, IW-041, IW-044, IW-045, IW-046, IW-047, IW-048, IW-050, IW-051, IW-052, IW-053, and IW-057, have registry or region binding only. They do not have complete adapter, focus, decision, AI, asset, and current-admission proof and must not be promoted from the registry alone.

## Soviet Collapse origin separation

`is_independence_wave_registry_event6_origin` delegates to `is_independence_wave_active_origin_country`, while `is_independence_wave_registry_soviet_origin` delegates to `is_soviet_collapse_active_origin_country` in `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:11-16`.

`is_independence_wave_active_origin_country` requires the Event 006 active flag and `liberation_origin = independence_wave`. `is_soviet_collapse_active_origin_country` requires the Soviet active flag and `liberation_origin = soviet_collapse`, and rejects an Event 006 active flag in `common/scripted_triggers/chaosx_liberation_release_triggers.txt:92-105`.

Event 006 preflight rejects `soviet_collapse_active_origin` and `liberation_origin = soviet_collapse` at `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:78-84`. Soviet origin setup refuses an Event 006 active origin at `common/scripted_effects/005_soviet_collapse_effects.txt:5704-5718`.

The 34 Soviet carriers remain a separate static collection at `common/collections/chaosx_country_collections.txt:53-55`. Event 006 collections and Soviet collections are views over fixed arrays and do not grant package or origin readiness.

Within the current Volga and Soviet boundary, IW-043 CHU is the only unadmitted Event 006 package with a complete current package surface candidate. IW-046 Chuvashia shares the CHU carrier at state 256 and is controlled by a package and anchor mutex. A Soviet-created CHU or any Soviet-origin carrier must be rejected by the Event 006 preflight even if the tag appears in the registry.

## Vanilla and collision audit

The scoped command was run from the mod root:

`python -B .tools/audit_chaosx_country_tags.py --surface-scan`

Result: 136 protected Event 006 or Soviet tags, zero external country-definition collisions, zero external identity-surface collisions, and one skipped Random Events root.

The audit intentionally excludes CBB, CBD, Fallout, and Random Events namespaces. It preserves the documented remap table `ALA->AAX`, `ALN->ABX`, `APX->INX`, `BAC->ADX`, `BSC->AEX`, `KHW->ANX`, `KRS->AOX`, `KZR->INX`, `MRC->IMX`, `OGB->IJX`, `RMC->IKX`, and `TSC->ILX`. `REV`, `ZIN`, and `ZZZ` are outside the protected set and were not remapped.

## Changed files and validation

Changed file: this handoff only.

No country tag, country definition, history, state, leader, portrait, flag, idea, focus, decision, AI, formable, or scripted gameplay file was changed.

Meaningful validation completed: scoped installed-surface collision audit, static comparison of the adapter and eleven-ID attestation blocks, source review of origin gates and registry collections, package binding review, custom X history and flag inventory, and package file-surface inventory.

Skipped meaningful validation: no Hearts of Iron IV process was launched, no save was created, and no live allocator, map, force, focus, AI, formable, cleanup, or save/load scenario was run. The Technology Tree Viewer is not installed, so technology runtime validation could not be performed.

## Remaining setup and identity risks

The whole Event 006 package system remains incomplete and fail-closed below the attested set.

The parent must retain package-ID and anchor dispatch for shared carriers, especially CHU and RHI/AJX. Tag-only dispatch would misroute simultaneous candidates.

The parent must not promote a package based only on an adapter, registry row, focus file, or static flag. Source clearance, exact map state, host survival, force materialization, route visibility, AI timing, formable contracts, cleanup, and runtime evidence are still required.

No simplification or fallback was introduced by this audit.

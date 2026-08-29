# Event 006 country-package audit — current worktree, 2026-08-29

## Disposition

Event 006 remains HOLD / PARTIAL for country-package readiness. This is a read-only country-package audit; no gameplay, registry, map, asset, or AI files were changed.

The current accepted boundary is 32 content-attested selectable packages across 29 compatible reservation groups, 40 runtime adapters, and 161 selectable non-overlay rows that remain unattested. The candidate registry contains 206 rows in total, consisting of 193 non-overlay selectable rows and 13 vanilla-route overlay rows, with 191 unique resolved carrier tags.

The current preflight contract is fail-closed: `is_independence_wave_runtime_package_preflight_ready` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` requires both a runtime adapter and a content attestation. A tag reservation, state binding, or generic focus route alone does not make a country package executable.

## Country-package coverage checklist

| Surface | Current evidence | Status and audit meaning |
|---|---|---|
| Candidate breadth | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`: 206 rows, 193 non-overlay selectable, 13 overlay-only, 191 unique resolved carriers | Registry breadth exists, but only 32 selectable non-overlay rows have current content attestation. |
| Tag registration | `common/country_tags/006_independence_wave_countries.txt`: 102 Event 006 X-ending reservations; 91 rows reuse 89 registered vanilla carriers; 13 overlays reserve no standalone tag | Static registration and collision checks are clean within the maintained Event 006/Soviet scope; registration is not package admission. |
| Country definitions | `common/countries/006_independence_wave_*.txt`: 85 named X definitions plus `006_independence_wave_unresearched_reservations.txt` | 17 unresolved identities remain parser-safe inert reservations and have no usable identity package. |
| Country history | 102 tag-prefix history files under `history/countries/` | All tags have a matching history filename, but the 17 unresolved reservation files are inert and do not prove capital, politics, roster, or OOB readiness. |
| State bindings | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`: 206 rows, no missing current state IDs | 138 selectable rows are bound, 55 are unbound, 27 are disabled because no unique current state exists, and 13 are nonselectable overlays. |
| Runtime adapters | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` and central dispatcher in `common/scripted_effects/006_independence_wave_effects.txt` | 40 exact adapter IDs are present; eight are adapter-only and still fail the content-attestation gate. |
| Content attestations | `has_independence_wave_runtime_package_content_attestation_for_execution_id` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` | 32 exact IDs are admitted by the current package contract; no other selectable package may pass package preflight. |
| Character recruitment | `history/general/006_independence_wave_character_recruitment_registry.txt` | 25 guarded country blocks and 54 `recruit_character` calls cover the current researched roster; IW-057 FER is intentionally absent and remains a roster/package gap. |
| Focus route | `common/national_focus/006_independence_wave_focus.txt`, `006_independence_wave_iw043_iw058_focus.txt`, and `006_independence_wave_iw093_iw098_focus.txt` | HOI4 focus MCP inspection found 184 focuses and 195 connectors with no layout diagnostics; this does not establish package breadth, AI balance, or per-row loading. |
| Decisions and missions | 80-row source crosswalk in `common/decisions/` and matching Event 006 localisation | Source coverage is present for accepted clusters, but package-local decision/mission breadth is absent for unattested rows and no runtime decision/mission inspector is available. |
| Ideas and advisors | `common/ideas/006_independence_wave_ideas_registry.txt`, `common/characters/006_independence_wave_characters_registry.txt`, and NWE advisor localisation | Shared/route definitions exist for the accepted surface; unattested identities do not have a safe package-specific idea, advisor, or lifecycle contract. |
| Flags and portrait wiring | `interface/006_independence_wave_small_assets.gfx`, `interface/006_independence_wave_portraits_registry.gfx`, `gfx/flags/`, and portrait worker manifests | Static flag families are 102/102; portrait coverage is partial and rights/consumer evidence remains incomplete for most grounded subjects. |
| AI | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` and focus/decision `ai_will_do` blocks | 24 source AI profiles exist, but the mandatory typed probability route is unavailable, so no quantitative survival, selection, or balance claim is made. |
| Technology | Package histories and shared setup effects | No installed Technology Tree Viewer is available; technology coverage is source-only and unresolved as engine evidence. |
| 3D assets | None in the accepted Event 006 country scope | No custom unit, building, audio, or counter package is claimed by this audit. |

## File-surface checklist

The current source-of-truth and package surfaces are:

| Surface | Current path |
|---|---|
| Candidate registry | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` |
| Installed map/binding ledger | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` |
| Registry constants | `common/script_constants/006_independence_wave_constants_registry.txt` |
| Event 006 tag reservations | `common/country_tags/006_independence_wave_countries.txt` |
| Named country definitions | `common/countries/006_independence_wave_*.txt` |
| Inert unresolved definitions | `common/countries/006_independence_wave_unresearched_reservations.txt` |
| Country histories | `history/countries/<TAG> - <name>.txt` |
| Character recruitment | `history/general/006_independence_wave_character_recruitment_registry.txt` |
| Character definitions | `common/characters/006_independence_wave_characters_registry.txt` |
| Package adapter and attestation triggers | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` |
| Setup/final-validation/cleanup dispatcher | `common/scripted_effects/006_independence_wave_effects.txt` |
| Generic focus tree | `common/national_focus/006_independence_wave_focus.txt` |
| Adapter-specific focus trees | `common/national_focus/006_independence_wave_iw043_iw058_focus.txt` and `common/national_focus/006_independence_wave_iw093_iw098_focus.txt` |
| Ideas | `common/ideas/006_independence_wave_ideas_registry.txt` |
| AI profiles | `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` |
| Consolidated decisions | `common/decisions/006_independence_wave_*.txt` with current authority called out in `006_source_of_truth_map.md` |
| Localisation | `localisation/english/006_independence_wave_*_l_english.yml` |
| Portrait and small-asset definitions | `interface/006_independence_wave_portraits_registry.gfx`, `interface/006_independence_wave_small_assets.gfx`, and `interface/006_independence_wave.gfx` |
| Current authority map | `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` |

Historical handoffs may name the removed `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` or older trigger/cosmetic paths. The current consolidated paths above are authoritative; those older names must not be used as current evidence.

## Missing or stale country-package surfaces

### Exact unattested selectable IDs

The following IDs are selectable or route-relevant in the candidate registry but are not in the current 32-ID content-attestation trigger. They therefore fail the central package preflight even where a tag shell, map anchor, or adapter exists.

| Disposition | Current unattested IDs |
|---|---|
| `automatic_pool_ready` (5) | `IW-003, IW-073, IW-086, IW-182, IW-185` |
| `automatic_pool_ready_if_not_living` (23) | `IW-015, IW-039, IW-046, IW-048, IW-050, IW-051, IW-052, IW-053, IW-057, IW-060, IW-081, IW-082, IW-098, IW-108, IW-130, IW-136, IW-140, IW-141, IW-170, IW-175, IW-177, IW-180, IW-192` |
| `automatic_pool_ready_if_unique_state_exists` (66) | `IW-013, IW-016, IW-021, IW-032, IW-036, IW-037, IW-047, IW-049, IW-054, IW-061, IW-062, IW-063, IW-065, IW-066, IW-067, IW-076, IW-078, IW-083, IW-084, IW-087, IW-089, IW-094, IW-095, IW-096, IW-103, IW-107, IW-109, IW-110, IW-111, IW-112, IW-113, IW-114, IW-115, IW-119, IW-121, IW-122, IW-123, IW-124, IW-125, IW-126, IW-131, IW-132, IW-134, IW-137, IW-138, IW-139, IW-142, IW-143, IW-145, IW-147, IW-148, IW-152, IW-154, IW-155, IW-158, IW-159, IW-162, IW-164, IW-165, IW-176, IW-179, IW-181, IW-186, IW-188, IW-189, IW-194` |
| `formable_or_route_only` (7) | `IW-034, IW-074, IW-100, IW-133, IW-144, IW-149, IW-183` |
| `high_chaos_only` (27) | `IW-020, IW-042, IW-043, IW-058, IW-064, IW-068, IW-069, IW-075, IW-090, IW-097, IW-099, IW-104, IW-106, IW-117, IW-135, IW-150, IW-151, IW-161, IW-166, IW-167, IW-169, IW-171, IW-198, IW-200, IW-201, IW-203` |
| `scenario_variant_only` (3) | `IW-011, IW-077, IW-116` |
| `specific_community_variant_only` (30) | `IW-055, IW-056, IW-079, IW-080, IW-088, IW-091, IW-092, IW-118, IW-120, IW-127, IW-128, IW-129, IW-146, IW-153, IW-157, IW-160, IW-163, IW-168, IW-172, IW-174, IW-178, IW-187, IW-190, IW-191, IW-193, IW-195, IW-199, IW-202, IW-205, IW-206` |

The eight current adapter-only IDs are `IW-013 NAV`, `IW-015 GLC`, `IW-043 CHU`, `IW-058 ASY`, `IW-093 DOX`, `IW-098 SOK`, `IW-177 FIJ`, and `IW-179 FSM`. Their adapters must not be mistaken for complete packages.

### Unresolved country identity shells

`common/countries/006_independence_wave_unresearched_reservations.txt` is parser-safe only. The following 17 rows currently resolve to inert reservation definitions and have no researched identity, usable country localisation, approved party/leader roster, or package-specific asset evidence:

`IW-088 DJX` Tuareg/Kel, `IW-091 DMX` Toubou/Teda-Daza, `IW-092 DNX` Atlas/Kabyle-adjacent, `IW-118 ENX` Maasai section/district, `IW-128 EXX` Nama, `IW-129 EYX` Ovambo, `IW-146 FPX` Naga, `IW-160 GDX` Karen, `IW-163 GGX` Chin/Zo, `IW-164 GHX` Arakan/Rakhine route, `IW-168 GLX` Hmong, `IW-190 HHX` Pueblo, `IW-195 HMX` Garifuna coast, `IW-199 HQX` Quechua members, `IW-202 HTX` Gran Chaco, `IW-205 HWX` Amazonian river peoples, and `IW-206 HXX` historical maroon community.

All 102 X tags have matching history filename prefixes, but the 17 unresolved files are not evidence of a playable history setup. Their inert status is correctly protected by the package readiness gate and must remain fail-closed until identity research and consent-sensitive asset work are complete.

## Map and state setup issues

The current binding ledger has no missing current state IDs, but its state safety is not equivalent to executable package readiness. Fifty-five selectable rows are unbound, 27 are disabled because no unique current state exists, and 13 are overlay-only. The current registry constants record 138 bound selectable rows and 55 unbound selectable rows.

The static allocator witness covers 20 admitted packages and protects former-host states for `BEL=6`, `ENG=126`, `FIN=111`, `FRA=16`, `GER=64`, `HOL=7`, `ITA=2`, `ROM=46`, `SOV=219`, `SPR=41`, and `USA=361`. This is a static witness, not a live transaction, save/load, or engine proof.

The current 32 attested state anchors are:

| Package | Tag/name | Anchor state | Reservation group | Map readiness |
|---|---|---:|---|---|
| IW-001 | SCO Scotland | 121 | RG-121-120-133 | ready if tag not living |
| IW-002 | WLS Wales | 122 | RG-122 | ready if tag not living |
| IW-004 | BRI Brittany | 14 | RG-14 | ready if tag not living |
| IW-006 | AFX Wallonia | 34 | RG-34 | automatic |
| IW-007 | AGX Frisia | 36 | RG-36 | unique state confirmed |
| IW-008 | RHI Rhineland | 51 | RG-RHINE-SAAR | ready if tag not living |
| IW-009 | BAY Bavaria | 52 | RG-52-53-54 | ready if tag not living |
| IW-010 | AJX Saar | 42 | RG-RHINE-SAAR | unique state confirmed |
| IW-012 | ICE Icelandic emergency republic | 100 | RG-100 | ready if tag not living |
| IW-017 | COR Corsica | 1 | RG-1 | ready if tag not living |
| IW-018 | ARX Sardinia | 114 | RG-114 | automatic |
| IW-019 | ASX Sicily | 115 | RG-115 | automatic |
| IW-023 | TRA Transylvania | 84 | RG-DANUBE-BORDERLAND | ready if tag not living |
| IW-024 | AXX Banat | 82 | RG-DANUBE-BORDERLAND | unique state confirmed |
| IW-026 | MAC Macedonia | 106 | RG-106 | ready if tag not living |
| IW-027 | BAX Thrace | 184 | RG-184 | unique state confirmed |
| IW-028 | BBX Epirus | 185 | RG-185 | unique state confirmed |
| IW-029 | BOS Bosnia | 104 | RG-104 | ready if tag not living |
| IW-030 | MNT Montenegro | 105 | RG-105 | ready if tag not living |
| IW-031 | KOS Kosovo | 802 | RG-DANUBE-BORDERLAND | unique state confirmed |
| IW-038 | RUT Ruthenia | 73 | RG-73 | unique state confirmed |
| IW-040 | KUB Kuban Cossack Host | 234 | RG-DON-KUBAN | ready if tag not living |
| IW-041 | CRI Crimean Tatar state | 137 | RG-137 | ready if tag not living |
| IW-044 | TAT Tatarstan | 249 | RG-MIDDLE-VOLGA-KAZAN | ready if tag not living |
| IW-045 | BSK Bashkiria | 651 | RG-651 | ready if tag not living |
| IW-070 | ARM Armenia | 230 | RG-230 | ready if tag not living |
| IW-071 | GEO Georgia | 231 | RG-231 | ready if tag not living |
| IW-072 | AZR Azerbaijan | 229 | RG-229 | ready if tag not living |
| IW-014 | CAT Catalonia | 165 | RG-165 | ready if tag not living |
| IW-033 | KAR Karelia | 146 | RG-146 | ready if tag not living |
| IW-173 | HAW Hawaii | 629 | RG-629 | ready if tag not living |
| IW-184 | HBX California | 378 | RG-378 | automatic |

The following first-footprint rows have concrete setup or ownership blockers that should remain visible in the package queue:

| Package | Current map/ownership evidence | Missing package/setup evidence |
|---|---|---|
| IW-095 Dahomey | Current runtime anchor is state 776; research material sometimes names stale baseline state 556 | No DAH shell, attested identity/rights, neutral flag or emblem, approved portrait roster, central adapter/attestation/preflight/Join, typed probability evidence, or repaired MCP artifact manifest. |
| IW-108 Buganda | UGA/Buganda identity, decisions, ideas, and portrait consumer are already owned by Event 012 | Event 006 ownership boundary, Daudi Cwa II source rights/repaint/independent-likeness-style crosswalk, package binding, and attestation are unresolved. |
| IW-136 Sindh | SIN anchor state 443 | No package shell, roster/base flag, identity contract, symbol, portrait, package AI, central adapter/attestation/preflight/Join, FORM-32 consumer, or MCP evidence. |
| IW-130 Madagascar | MAD anchor state 543; Merina origin/consumer is already present in Event 012 | No accepted Event 006 package, base symbol, period identity/portrait, package AI, central gate, FORM-31 consumer, or MCP evidence. |
| IW-086 Tripolitania | DHX anchor 448 with compact 661 and optional 662; Event 012 uses DHX `ancient_hosts` and claims 448/661 only on high chaos | No Event 006 roster, rights-cleared portrait, lifecycle, decision, idea, focus, force, AI, central adapter/attestation/preflight/Join, FORM-22 consumer, or MCP evidence. |
| IW-073 Hejaz | CUX anchors 679 and 856 with optional 855 in RG-ARABIA-HEJAZ-NAJD | No roster, rights-cleared portrait, package lifecycle, decisions/ideas/focus/force/AI, central gate, FORM-20 consumer, or MCP evidence; symbols are route/date-sensitive. |
| IW-048 UDM | Current handoff identifies Boris Berman, `industrial_security` versus `industrial_breakaway`, and state-399 host retention as unresolved design choices | No adapter/attestation/Join/fallback; portrait rights, current MCP, and typed probability compare remain unresolved. |
| IW-050 Komi | Package-local route remains under review | No defensible neutral 1936 flag/emblem, approved asset authorization, central adapter/attestation/preflight/Join, current MCP, or SCN-008 typed evidence. |
| IW-057 FER | Candidate row is selectable-if-not-living | FER is intentionally omitted from `history/general/006_independence_wave_character_recruitment_registry.txt`; identity, roster, and central attestation remain incomplete. |

The 8/29 absent-country release repair in `common/scripted_effects/006_independence_wave_execution_effects.txt` and related liberation effects is a scope-safety correction only. It does not add an adapter, content attestation, identity, asset, or AI package, and therefore does not change the country admission boundary.

## Politics, leaders, portraits, flags, advisors, and parties

The 25 guarded blocks and 54 recruitment calls in `history/general/006_independence_wave_character_recruitment_registry.txt` are current startup-roster evidence for the researched subset. They include the admitted regional roster blocks for SCO, WLS, RHI, BAY, AJX, COR, HAW, FSM, FIJ, CHU, ASY, DOX, SOK, AFX, AGX, MNT, KOS, RUT, MAC, AXX, BAX, BBX, BOS, NAV, and GLC. The registry is not a complete 206-row roster and intentionally does not recruit FER IW-057.

The 17 inert X reservations have no complete party names, country adjective, ruling-party setup, popularity/stability/war-support policy, election/law setup, leader metadata, advisor roster, or character recruitment. They must not be made selectable through a generic fallback identity.

The current portrait audit records 110 supplied PNG/DDS pairs, 70 runtime DDS files, 38 exact supplied matches, 64 unique Event 006 GFX portrait pairs, and 47 resolved character-registry portrait references. Only NAV Aguirre and GLC Castelao are current Event 006 `styled_final` exact runtime matches. GLC Bóveda has a styled output but no safe current consumer. No additional portrait wiring is safe without the portrait-worker identity, provenance, gender/name, and consumer crosswalk.

Grounded subjects remain source-placeholder or rights-pending until an attributed source and a user-supplied HOI4-style replacement are available. Fictional or impossible leaders require an ImageGen evidence trail and portrait-specific wiring through `chaosx_portrait_creator`; no generated identity fallback is authorized for unresolved country rows.

Flags pass the current structural audit at 102 registered Event 006 tags and 102 complete flag families. That result proves family coverage only, not historical provenance, route/date correctness, or consumer approval. The ASX/Sicily S.015 reconstruction uses unsuffixed and all-ideology basenames across five routes and needs owner review against the route-specific source contract. IW-095, IW-086, IW-073, IW-108, IW-130, IW-136, IW-048, and IW-050 do not have accepted package-level flag/symbol provenance in the current boundary.

The NWE advisor localisation surface exists, but no advisor roster, icon, or party contract should be inferred for an unattested package. Institutional councils, committees, juntas, offices, or symbolic bodies must use institutional names rather than personal random-name pools when their package is eventually admitted.

## Focus, decision, idea, and asset issues

The focus MCP inspection is current evidence for tree geometry only: 184 focuses, 195 connectors, and zero layout diagnostics apart from an unrelated vanilla `continuous_restrict_freedom_desc` warning. It is not evidence that all 206 registry rows load distinct focus routes, that every package has the right prerequisites, or that focus rewards, ideas, decisions, AI selection, and map ownership are balanced.

The central final validator in `common/scripted_effects/006_independence_wave_effects.txt` requires the generic focus contract and `independence_wave_generic_ai_profile` after the package-group validators. Rows without adapter plus attestation cannot reach that final validation path. The two adapter-specific focus trees cover CHU/ASY and DOX/SOK only; they do not close the eight adapter-only gap or the remaining 161-row gap.

The current decision source crosswalk covers 80 rows across the consolidated `common/decisions/006_independence_wave_*.txt` surfaces. No installed MCP decision/mission inspector or production GUI render is available for a runtime completion claim. Unattested packages have no accepted package-local decision category, mission/timed objective lifecycle, or focus-unlocked action contract.

The shared idea registry and route-local idea files provide source definitions for accepted paths, but an inert reservation or a state binding does not supply a safe starting idea, icon, lifecycle, or removal condition. No new fallback icon, portrait, flag, or generic party asset was introduced by this audit.

The 48-formable family design remains incomplete. FORM-06 and FORM-10 through FORM-15 plus FORM-17 through FORM-47 fail closed, FORM-07 and FORM-08 remain blocked, FORM-42 remains blocked, and FORM-48 is unreachable while FSM is unadmitted. This is a system-wide country-package breadth blocker rather than a reason to admit individual rows without identity and state safety.

## Starting military, technology, industry, supply, and production

Accepted package setup is runtime-driven through the Event 006 package effects rather than a complete conventional OOB for every candidate history file. The current source contract can map starting force archetypes, manpower, equipment, laws, production, and supply behavior only for the admitted package subset. No serious-fighting, industry, convoy, train, fuel, or supply-survival claim is justified for the 161 unattested rows.

The current map ledger preserves anchor, compact, extended, and lock stages and the allocator witness protects former-host capitals, but there is no live transaction or save/load proof in this audit. The state-399 UDM industrial-force choice, DHX and CUX compact/optional territory choices, and Event 012 ownership overlaps require package-owner decisions before setup can be attested.

No Event 006 custom technology or doctrine tree is accepted in the current country package. The installed package exposes no Technology Tree Viewer, so technology prerequisites, placements, unlocks, bonuses, and missing assets cannot be engine-verified here; this limitation remains unresolved and is not replaced with source-only completion language.

No custom Event 006 3D unit, building, counter, or audio package is in scope. The absence of such a package is not a missing country surface for this event, but no country package may claim one from the current evidence.

## AI and playability issues

`common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` contains 24 source AI profiles, and the generic focus/decision surfaces contain source weights and route factors. The mandatory `chaosx_ai_probability_auditor` typed route currently reports transport/artifact failure (`Transport closed` / `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with no usable adapter), so no same-scenario `hoi4.probability_compare` evidence exists for Event 006.

Consequently, this audit makes no quantitative claim about AI survival, focus selection, research selection, decision scoring, event `ai_chance`, MTTH, strategy factors, or weighted target balance. A future AI or probability patch requires a baseline audit, owner-applied change, and same-named-scenario probability compare through the mandatory auditor.

Rows without current adapter plus attestation cannot execute the package setup, cannot receive a package-local starting roster/ideas/forces/AI profile through the central contract, and cannot be called playable merely because their tag or anchor appears in the registry. The 55 unbound rows and 27 disabled no-unique-state rows also require map-owner decisions before automatic pool behavior can be trusted.

## Current validation evidence

The current worktree static audits reran clean:

| Validation | Current result |
|---|---|
| `python -B .tools/audit_event6_allocator.py` | PASS: 149 publishers, 126 automatic/high-chaos selectable, 138 SCN-008 ranked, 40 adapters, 32 attestations, 29 groups, 20-package static standalone witness, 3/4/5/7/10 package ladder, and pre-event retired/hidden crisis surfaces. |
| `python -B .tools/audit_event6_country_api.py` | PASS: 242 broad unique tags, 191 resolved unique carriers, 34 Soviet carriers, 45 African carriers, zero missing, zero duplicates, and IW-031 crosswalk pass. |
| `python -B .tools/audit_event6_flags.py` | PASS: 102 registered Event 006 tags and 102 complete flag families. |
| `python -B .tools/audit_event6_form16.py` | PASS: ARM/GEO/AZR FORM-16 state 230/231/229, consent/refusal, mutation, rollback, and cleanup. |
| `python -B .tools/audit_event6_gui_matrix.py` | PASS for the semantic Statehood Ledger matrix: five tabs, five recognition frames, three dependency frames, four league frames, four formable frames, cleanup variables/animation, and four static/animated sibling pairs; no runtime render claim. |
| `python -B .tools/audit_event6_scenario_matrix.py` | PASS: all 32 SCN-008 mode/intensity cells and eight edge cases. |

Read-only HOI4 MCP evidence is limited to the current focus geometry inspection described above. Event inspection/rendering is partial with zero helper expansion or artifact-manifest failures in the latest evidence, decision/mission rendering is unavailable, technology-tree inspection is unavailable because no Technology Tree Viewer is installed, and the typed probability route is unavailable. The audit therefore does not claim live event execution, GUI visual completion, technology completion, save/load safety, or quantitative AI balance.

## Remaining blockers and owner actions

1. Keep the Event 006 boundary fail-closed until the 161 unattested rows receive package-local identity, roster, setup, map, asset, decision/idea, focus, and AI attestations.
2. Resolve the eight adapter-only IDs before calling their existing adapters playable: `IW-013`, `IW-015`, `IW-043`, `IW-058`, `IW-093`, `IW-098`, `IW-177`, and `IW-179`.
3. Research and explicitly approve the 17 inert reservation identities before adding country definitions, leaders, parties, portraits, flags, or localisation.
4. Resolve the first-footprint ownership and state setup rows IW-095, IW-108, IW-136, IW-130, IW-086, IW-073, IW-048, IW-050, and IW-057 with current map/identity evidence.
5. Complete portrait-worker provenance, gender/name metadata, consumer wiring, and user-supplied final replacements where grounded portraits remain pending.
6. Review route/date-specific flag provenance, especially the ASX/S.015 reconstruction and all package-local neutral symbols.
7. Re-run the mandatory typed AI probability baseline/compare once the MCP adapter and artifact manifest are available; do not substitute source-only weights for that evidence.
8. Obtain a Technology Tree Viewer or record the limitation in the parent completion report; source review alone cannot close the technology surface.
9. Finish formable consumers and reachability for the blocked FORM-06 through FORM-48 families without bypassing package admission.

## Audit handoff

Changed files: only this dated handoff document. No country tags, definitions, states, history, leaders, characters, portraits, flags, parties, focus trees, decisions, ideas, AI, formables, or map data were changed.

Changed identifiers: none.

Simplifications or unapproved fallbacks: none introduced. This report preserves the current fail-closed boundary and records unresolved MCP, portrait, identity, map, formable, technology, and probability limitations rather than treating source-only evidence as runtime completion.

# Repo Explorer Handoff

## Scope read

- Parent task: build the current Event 006 candidate-registry gap map and identify the safest next package tranche without inventing identity, rights, flags, portraits, map anchors, or central admission.
- Explicit constraints: this was a read-only exploration; no gameplay, localisation, asset, workbook, central adapter, attestation, preflight, Join, or registry source was edited.
- Files or ids requested: IW-046 CHU, IW-049 BWX, IW-051 YAK, IW-052 BYA, IW-057 FER, later candidates with complete identity/map/asset evidence, and current adapter/attestation/Join and asset authorities.
- Skills or docs read: `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-focus-trees`, and `chaos-redux-event-assets`; the offline Country creation, Map modding, State modding, National focus modding, Portrait modding, Graphical asset modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding pages; and the installed vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and script-constants documentation.

## Primary findings

The current source-of-truth boundary is 40 runtime adapters, 32 content-attested selectable packages, 29 compatible reservation groups, and 161 unattested selectable rows out of 193 non-overlay rows, with Event 006 still HOLD/PARTIAL.

No requested candidate currently has a complete identity, rights, map, package-mechanics, portrait/flag, weighted-evidence, and central-admission packet, so there is no safe gameplay or admission tranche to promote now.

IW-049 BWX is the most concrete source-local lead because a country shell, history shell, country-tag registration, and documented flat flag ladder exist, but its current map binding is explicitly unbound and its sourced leader/portrait and complete package surfaces are absent.

IW-051 YAK is the cleanest current-map anchor among the requested candidates at state 574, but the current handoff confirms that it has no package-local decisions, ideas, AI, production/supply setup, or Event 006 focus hook, and its leader/asset evidence is not an admission packet.

The later IW-070 ARM, IW-071 GEO, and IW-072 AZR tranche is the useful complete reference: exact installed anchors 230/231/229, reused vanilla identity/portraits/flags, full package mechanics, central adapter/attestation, and current package audits are all documented. It is a precedent, not an unadmitted next candidate.

## Relevant files

| Path | Why it matters | Evidence |
| --- | --- | --- |
| `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:47,50,52-53,58` | Authoritative candidate rows for CHU, BWX, YAK, BYA, and FER. | CHU uses `CHU`/state `256`; BWX reserves `BWX` but has no anchor; YAK uses `YAK`/`574`; BYA uses `BYA`/`564`; FER uses `FER`/ordered `408|409`. |
| `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:47,50,52-53,58` | Identity, leader, symbol, territory, and source-mode constraints. | Every requested row requires a defensible sourced male leader or authentic institution; BWX requires a researched period civic flag; YAK/BYA/FER may reuse base assets only if they match the released identity and origin. |
| `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:47,50,52-53,58` | Installed-map binding authority. | CHU 256, YAK 574, BYA 564, and FER 408/409 are current bindings; BWX is `disabled_no_unique_current_state` and `unbound_current_map`. |
| `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:35,45-46,95-96` | Reservation and host-protection contracts. | FER is `RG-408-409`; BYA is `RG-564`; YAK is `RG-574`; CHU shares `RG-MIDDLE-VOLGA-KAZAN` with IW-043/IW-044/IW-047; BWX has `RG-MORDOVIA` but no resolved anchor. |
| `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_state_collisions.csv:4` | Current collision witness. | State 256 is shared by IW-043 and IW-046, with a one-automatic-package-per-wave mutex. |
| `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:4-109` | Dormant planner contracts for this regional band. | The source comment keeps IW-049 and IW-056 unbound and IW-055 specifically invoked; helper predicates exist for IW-046, IW-051, IW-052, and IW-057, but these are planning gates, not content admission. |
| `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt:19-117` | Shared CHU package identity and mutex. | IW-046 requires exact `original_tag = CHU`, package id `iw_046`, package flag `independence_wave_package_iw046_chuvashia`, and exclusion of the IW-043 origin/flag. |
| `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:8-59,159-212` | Central runtime adapter, content-attestation, and two-gate preflight authority. | The adapter list contains 40 IDs; the attestation OR-list contains the exact current 32 IDs and excludes every requested candidate; preflight requires both adapter and attestation. |
| `common/scripted_effects/006_independence_wave_join_effects.txt:213-246` | Deterministic Join authority. | The fixed first-success probe ends with the current 32-package order and contains no IW-046, IW-049, IW-051, IW-052, or IW-057. |
| `common/country_tags/006_independence_wave_countries.txt:32` | Existing local tag registration. | Only `BWX = "countries/006_independence_wave_BWX.txt"` exists for the requested rows; YAK, BYA, FER, and CHU remain registered vanilla carriers. |
| `common/countries/006_independence_wave_BWX.txt` and `history/countries/BWX - Erzya-Moksha Federal Republic.txt` | Existing BWX package-local shell. | Both files are neutral shells; comments state that runtime territory, capital, politics, leaders, forces, ideas, focus, and AI are assigned elsewhere at formation, but no such complete Event 006 adapter is present. |
| `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/manifest.md:3-16` and `design_reference_matrix.md:16` | BWX flag provenance and runtime ladder. | BWX has a documented ImageGen flat flag source and normal/medium/small TGA outputs classified as a historically grounded federal synthesis, not proof of a complete identity or portrait package. |
| `docs/plans/006_independence_wave_plans/asset_research/006_package_asset_coverage.md:25,76-104` | Current asset policy and coverage. | IW-046, IW-051, IW-052, and IW-057 are in the installed-base flag coverage group; IW-049 is in the generated civic-flag group; all grounded leader portraits still require item-level source and rights evidence. |
| `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md:5-39,132-157` | Current authority and admission boundary. | Records 40/32/29/161, the exact 32-ID Join order, package-local MEL/UDM/KOM exclusions, and the rule that an existing tag, shell, portrait, flag, focus, or adapter never proves admission. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw051_sakha_package_audit_2026_08_14.md:13,30-52` | Latest direct YAK audit. | Confirms state 574 binding but no IW-051 focus hook, decisions, ideas, AI, production/supply wiring, package caller, admission attestation, or deterministic setup path. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_next_package_gap_scan_2026_08_14.md:1-18` | Latest ranked next-package scan. | It found no unadmitted package clearing all identity, rights, flag, territory, host, formable, cleanup, and central gates and retained the 40/32/29/161 boundary. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw048_udm_current_repair_audit_2026_08_15.md:1-100` | Latest later package-local comparison. | UDM package-local mechanics and state 399 are source-repaired, but central adapter, attestation, preflight, scenario, and Join remain absent and no identity/portrait/flag admission claim is made. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw045_bashkiria_promotion_current_2026_08_14.md:1-55` | Current admitted-package reference. | IW-045 is the latest promoted package under the 32/29 boundary, with exact state 651, source-backed portrait/flags, full mechanics, and central attestation/Join evidence. |
| `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw070_iw072_transcaucasus_country_package_audit_current_2026_08_05.md:1-45` | Later complete package reference. | ARM/GEO/AZR use exact states 230/231/229, reused vanilla histories/leaders/portraits/flags, full package mechanics, dispatch, localisation, cleanup, and content attestation. |

## Existing patterns

The safest reusable pattern is the exact-carrier package contract used by the admitted IW-045 and IW-070–IW-072 packages: preserve the vanilla carrier identity and history, bind one verified current-map anchor, capture a live former host, attach package-scoped leaders/portraits and route symbols, load the shared focus framework, add package-specific forces/ideas/decisions/AI/localisation, and prove generation-safe cleanup before central admission.

The closest shared-carrier pattern is IW-043/IW-046 CHU in `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt`; the package id and package flag are mandatory because `CHU` alone is not an identity selector.

The closest package-local pattern is the current MEL/KOM/UDM tranche, which keeps package effects, triggers, decisions, ideas, AI, localisation, flags, and portraits local while central adapter, attestation, preflight, scenario, and Join lists remain untouched until independent admission evidence exists.

The shared Event 006 focus source currently inspects as 184 focuses and 196 connectors with zero crossings and zero node intersections, but it has six selected layout/reference warnings and fourteen aggregate diagnostics dominated by unrelated missing generic continuous-focus icons; no requested candidate has a package-specific focus hook in the current source.

## Vanilla or reference precedents

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/BSK - Bashkortostan.txt`, `YAK - Yakutia.txt`, `BYA - Buryatia.txt`, and `FER - Far Eastern Republic.txt` are the relevant vanilla carrier/history precedents, but carrier existence does not supply Event 006 package identity, origin, map reservation, leader rights, or cleanup.

The vanilla country-creation and state-modelling rules require a unique tag, country file, country history, localisation, normal/medium/small flags, and state ownership/core assignment; the Event 006 registry deliberately defers these writes for reused carriers until the package contract is complete.

The admitted IW-070–IW-072 handoff is the best approved in-repo precedent for a later complete source tranche, while the current asset coverage ledger is the authority for when vanilla flag reuse is allowed and when a generated civic flag needs a documented source package.

## Candidate comparison

| Candidate | Current map and registry state | Existing package/asset evidence | Blocking gates and disposition |
| --- | --- | --- | --- |
| IW-046 Chuvashia / `CHU` | Exact state 256, `RG-MIDDLE-VOLGA-KAZAN`; shared with IW-043 and the current state-256 collision witness. | CHU route portraits/flags and IW-043 adapter files exist, but they are not IW-046 admission evidence; no independent IW-046 package effects, decisions, ideas, AI, focus hook, or asset manifest were found. | Requires its own sourced Chuvash identity/origin, leader or authentic institution, portrait rights, route symbols, complete mechanics, and a fresh CHU mutex/preflight audit; HOLD. Do not reuse IW-043 content by tag. |
| IW-049 Mordovia / `BWX` | No current unique map anchor; binding is `disabled_no_unique_current_state`, `unbound_current_map`, and `RG-MORDOVIA` requires a Mordovia/Penza split. | Has `common/country_tags/006_independence_wave_countries.txt:32`, a neutral BWX country/history shell, and a documented flat normal/medium/small BWX flag ladder. No sourced leader/portrait, package mechanics, focus/decision/AI, runtime adapter, or central admission surface was found. | Must resolve the exact installed state and host survival first, then resolve a named Erzya-Moksha institution and sourced male leader/portrait rights, and independently audit the generated civic flag against that identity; HOLD. This is the best evidence-research lead, not a safe gameplay tranche. |
| IW-051 Sakha / `YAK` | Exact compact anchor state 574/Yakutsk; optional 644/876/877 extensions; `RG-574`; current binding is valid if YAK is not living. | Vanilla YAK history/flag/portrait exists and Event 005 has YAK focuses, but no Event 006 package-local decisions/ideas/AI/production/supply/force caller or package-specific focus hook exists. The 2026-08-14 audit explicitly records no admission attestation or deterministic setup path. | Requires a sourced Sakha institution or period-valid male leader, identity-matched flag/portrait evidence, full p51 force/economy/lifecycle package, weighted evidence, and central promotion; HOLD. It is the cleanest map lead, not a complete package. |
| IW-052 Buryatia / `BYA` | Exact compact anchor state 564/Ulan Ude; `RG-564`; current binding is valid if BYA is not living. | Vanilla BYA history/flag/portrait exists, but no Event 006 package-local mechanics, decisions, ideas, AI, force caller, focus hook, portrait manifest, or route-asset package was found. | Requires sourced Buryat institution/leader and identity-matched symbols, p52 mounted/frontier mechanics, current host/cleanup proof, weighted evidence, and central promotion; HOLD. |
| IW-057 Far Eastern Republic / `FER` | Ordered alternative anchors 408/Vladivostok or 409/Khabarovsk; `RG-408-409`; current binding is map-valid if FER is not living and the host survives. | Vanilla FER history/flag/portrait exists, but no Event 006 package-local package files or asset manifest were found. Its accepted force profile requires railway/port regular defectors plus conditional naval and air support, increasing lifecycle and source risk. | Requires a sourced Far Eastern institution/leader and flag provenance, ordered-anchor transaction, p57 regular-defector/rail/naval/air package, weighted evidence, and central promotion; HOLD. |
| IW-055 Nenets state / `NEN` (later registry comparison) | Current binding is state 825/Nenets, rebounded from public state 579; `RG-579`; explicitly `specific_community_variant_only`. | The map and carrier binding are unusually concrete, but no complete package-local mechanics, named-community leader/portrait, or symbol manifest was found. | Not an automatic or complete candidate; it still needs a specifically named Nenets/Yamalo-Nenets institution and sourced identity/assets, so it does not beat BWX/YAK for a safe implementation tranche. |
| IW-047 Mari El / `MEL` and IW-048 Udmurtia / `UDM` and IW-050 Komi / `KOM` (later package-local comparison) | Current bindings are state 833, 399, and 397 respectively, with package-local handoffs. | These have more local mechanics than the requested rows, including decisions, ideas, AI, lifecycle and shared-focus hooks, but the latest handoffs retain portrait/rights, neutral-symbol, typed-mission, or central-admission blockers. | They are package-local HOLDs and must not be promoted by copying a central line; the current source-of-truth map expressly keeps them out of adapter, attestation, preflight, and Join. |
| IW-070 ARM, IW-071 GEO, IW-072 AZR (later complete reference) | Exact installed anchors 230/Yerevan, 231/Tbilisi, and 229/Baku. | Current audit records reused vanilla identity/history/leaders/portraits/flags, package ledgers/ideas/forces/focus/decisions/missions/AI/cleanup, central dispatch, and content attestation. | This is the complete source-backed precedent and current admitted tranche, not a new candidate for this gap map. |

## Likely edit order for the parent

1. Keep all current counts and central lists unchanged; no requested candidate currently clears the package contract.
2. If a bounded research tranche is desired, start with IW-049 BWX because its unresolved point is explicit and reproducible: resolve an exact current Mordovia/Penza state split and host-remnant witness before creating any runtime ownership or claiming the existing BWX flag is sufficient.
3. Resolve the exact named institution, period-valid male leader or authentic institutional archive, portrait rights, and symbol provenance for the selected candidate; do not generate a person or relabel a modern/community symbol as a 1936 national identity.
4. Only after identity, map, host, and asset receipts exist should the package owner add the package-local country/history or carrier adapter, forces, ideas, decisions, AI, localisation, focus assignment, and generation-safe cleanup as one bounded contract.
5. For every added anchor or territory surface, rerun `hoi4.map_inspect` and `hoi4.map_render`; for any shared or package-specific focus surface, rerun `hoi4.focus_inspect` and `hoi4.focus_render`; for any setup event, run file-scoped `hoi4.event_inspect` and `hoi4.event_render` before considering admission.
6. For every weighted decision, mission, focus, event option, random list, or AI strategy surface, start with `hoi4.probability_inspect` and route the detailed pass through `chaosx_ai_probability_auditor`, then use the same scenarios for `hoi4.probability_compare`; this audit has no callable `chaosx_ai_probability_auditor` route in the installed tool list, so no quantitative candidate claim is made.
7. Only after an independent package audit passes should the parent decide whether to add a central adapter, content attestation, preflight/scenario branch, and deterministic Join entry in one owner-controlled admission change.

## Validation checks

- Re-read the five authoritative CSV rows and verify that BWX remains unbound, CHU remains mutexed, and YAK/BYA/FER retain states 574/564/408|409 before any implementation.
- Run `rg -n 'iw_046|iw_049|iw_051|iw_052|iw_057' common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt common/scripted_effects/006_independence_wave_join_effects.txt` and require no central admission entry until the full packet exists.
- Run `.tools/audit_event6_allocator.py`, `.tools/audit_event6_country_api.py`, `.tools/audit_event6_flags.py`, and `.tools/audit_event6_scenario_matrix.py` after any owner-applied package change, preserving the 40/32/29/161 authority until a deliberate promotion.
- For BWX, require a fresh map binding and host-survival receipt before creating a gameplay state transfer; do not substitute state 256, 397, 399, 574, or 564 for the unresolved Mordovia/Penza split.
- For YAK, BYA, and FER, verify vanilla carrier ownership/origin, exact anchor ownership/control, protected former-host survival, and route-specific flag/portrait consumers rather than treating installed vanilla assets as package evidence.
- Preserve current flag-family requirements of normal 82x52, medium 41x26, and small 10x7 bottom-origin 32-bit TGA and require a source/rights manifest for every grounded portrait.
- The mandatory read-only MCP evidence from this exploration is `hoi4.map_inspect` for states 256, 564, 574, 408, 409, 249, and 833 and `hoi4.map_render` for the state layer with coastlines, ports, victory points, resources, state buildings, supply nodes, and railways. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c090ba30e2bffb40d7396559ffe83495d2e1a1d4acbe5401a5db5537cec1053c/3ffc855a75b706a9f079985ff23e81e6757b13acac09fe430b2d1229b646c04b/map-inspect.40b912dc578c3d0a.json`; render artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b11da464a58a00f392d20160c03b0af4a5e89f3dc88629a12e57291b26e12dba/34f0884e329d25626d8bb92836451f6d1a47be15581b603e7499f1840fa54d56/map-state.png`, `.../map-state.json`, and `.../map-state.html` under the same workspace artifact.
- Map MCP selected all seven requested state IDs with no unknown or missing geometry IDs and validated state/region membership and networks, but aggregate validation is false because unrelated `mod:map/buildings.txt` diagnostics report 1,323 `MAP_BUILDING_POSITION_INVALID` and 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` errors; no candidate-specific map error was exposed.
- The mandatory shared-focus evidence is `hoi4.focus_inspect` artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3178e5100b67b3f2de6f34c9eda0a74a027b7265ceb845e29d64e5657035e3f/c0f4433374553eed95c15590ac7f18485207cfdedf7f56779a91c8a8d518b421/focus-inspect.4a06542f57301176.json` and `hoi4.focus_render` artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c5494e0a26011621445ed31c1874bd487e070437b9c142fee14ebb5d672ff9a/ab8d9ae55f7baeff6bd34ca88e658ecb81d0ae60ef7a955d9e3cab57817e5dc1/independence_wave_focus_tree.focus.html`; the tree resolves 184 focuses and 196 connectors with zero crossings and zero node intersections, while six selected layout/reference warnings and fourteen aggregate diagnostics remain.
- `hoi4.probability_inspect({})` returned `PROBABILITY_ADAPTERS_LISTED` with 11 adapters but zero available candidates, and an attempted Sakha source inspection returned `PROBABILITY_SOURCE_NOT_FOUND` for `common/ai_strategy/006_independence_wave_sakha.txt`; no probability artifact or quantitative AI claim is made.
- The installed package has no Technology Tree Viewer; no technology surface was invented or treated as complete.

## Risks and blockers

### Confirmed blockers

- No requested candidate is in the current central content-attestation OR-list or deterministic Join order, and no central list may be widened from a registry row, shell, flag, portrait, focus, or adapter alone.
- IW-046 has an intentional CHU carrier collision with IW-043 and requires package-specific origin, flag, leader, and setup mutex evidence.
- IW-049 has no authoritative installed-map anchor and only a neutral shell plus flag ladder, so any generic Mordovia/Penza state or generic leader would violate the accepted source boundary.
- IW-051, IW-052, and IW-057 have valid candidate-map bindings but no complete Event 006 package-local source/asset/leader/AI/decision/focus/cleanup contract; IW-051's direct audit explicitly records these omissions.
- IW-055 is specifically community-restricted despite its current state-825 binding and therefore is not an automatic fallback.
- The current map MCP route exposes unrelated global locator errors, so selected-state evidence is bounded and cannot be presented as a clean whole-map validation.
- No callable `chaosx_ai_probability_auditor` tool was present in `ALL_TOOLS`; the probability route can list adapters but cannot produce the required detailed auditor pass for a future candidate in this session.

### Ordinary risks

- Reused vanilla flags and portraits can be identity-incompatible with the Event 006 opening institution even when the files are installed; every reuse needs package-specific provenance and consumer review.
- Expanded territory rows for YAK and ordered FER alternatives must remain optional/transactionally selected until anchor ownership, host survival, and cleanup are proven.
- The shared focus tree retains unrelated continuous-focus icon diagnostics and authored layout warnings; adding a candidate-specific hook would require a fresh focus inspect/render rather than relying on the aggregate count.

## Recommended next action

Do not implement or admit IW-046, IW-049, IW-051, IW-052, or IW-057 in the current tranche. If the parent needs one bounded source-backed follow-up, select IW-049 for map/identity/flag-source research only, with IW-051 as the next map-clean fallback after its identity and package-local mechanics are researched; preserve the 40-adapter, 32-attested, 29-group, 161-unattested boundary until a complete packet and the mandatory MCP/probability/audit evidence exist.

## Current static recheck — 2026-08-15

The post-reconciliation static recheck still reports 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 40 runtime adapters, 32 attestations, 29 compatible groups, and 161 unattested rows. The allocator audit, SCN-008 scenario matrix, 102-family flag audit, and protected-country-tag audit all pass without changing the central boundary. No candidate admission, Join entry, or asset fallback was added by this recheck.

# Event 006 IW-013 and IW-015 Iberian country-package audit

> Historical snapshot notice (2026-08-05): This audit preserves the pre-adapter map-contract and package-coverage findings. Its missing-adapter and NAV-172 wording are superseded only by the current amendment at the end of this file; the HOLD/fail-closed admission conclusion remains current.

Audit date: 2026-08-03.

Scope: IW-013 Basque Country (`NAV`) and IW-015 Galicia (`GLC`) country-package surfaces used by Event 006 Independence Wave and FORM-07 Iberian Federation.

Disposition: plan-level recommendation only. No safe narrow gameplay patch was identified, so this audit does not add dispatcher branches, runtime adapters, focus content, decisions, ideas, AI, identity assets, or attestation flags.

The existing package rows are allocatable metadata, not complete runtime packages. Adding either package to the admitted runtime set now would create shallow content and would make FORM-07 readiness claims unsupported.

## Accepted identity and map contract

| Package | Accepted registry row | Tag | Baseline anchor and reservation group | Current installed-map binding | Force mapping |
| --- | --- | --- | --- | --- | --- |
| IW-013 Basque Country | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:14` | `NAV` | State `172` Navarre, `RG-172` (`docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:18`) | Compact anchor state `792` País Vasco; optional extensions `172` Navarra and `806` Pyrénées-Atlantiques (`docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:14`) | Mapping `67`, `mountain_frontier`, mountain infantry and industrial militia (`docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:14`) |
| IW-015 Galicia | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:16` | `GLC` | State `171` Galicia, `RG-171` (`docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:17`) | Compact anchor state `171` Galicia (`docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:16`) | Mapping `50`, `territorial_defense`, territorial infantry and coastal guards (`docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:16`) |

The current region-02 loader follows the installed-map audit for IW-013 by using state `792` and preserving `172` and `806` as optional extension states. The research registry and reservation-group prose still describe baseline state `172` as the compact anchor. This is a contract mismatch, not a safe local typo: FORM-07 currently hard-codes state `172` for NAV. Parent coordination is required before any map or formable change.

## Country-package coverage checklist

| Surface | IW-013 `NAV` | IW-015 `GLC` | Evidence and disposition |
| --- | --- | --- | --- |
| Candidate registry and research | Present | Present | Accepted rows are metadata only; both research rows retain leader, flag, map, tag-collision, host-protection, and provenance gates. |
| Reservation group and allocator loader | Present | Present | `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt:9-20,27-38`; `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt:9-20,31-42`. |
| Current-map anchor reservation | Present but crosswalked | Present | IW-013 reserves `792` and tries `172`/`806`; IW-015 reserves `171`. This does not prove release/setup safety. |
| Country tag registration | Vanilla only | Vanilla only | `NAV` and `GLC` are vanilla tags; no Chaos Redux tag file entry is needed. No X tag is reserved for either package. |
| Country history and state setup | Vanilla only | Vanilla only | Vanilla history is authoritative and no Event 006 origin setup exists. Do not duplicate or overwrite country history as a package shortcut. |
| Runtime setup adapter | Missing | Missing | No IW-013/IW-015 branch in package dispatch setup. |
| Runtime final-validation adapter | Missing | Missing | No IW-013/IW-015 branch in package dispatch final validation. |
| Runtime cleanup adapter | Missing | Missing | No IW-013/IW-015 branch in package dispatch cleanup. |
| Content attestation | Missing by design | Missing by design | Neither package is in the exact admitted content-attestation set. Keep them fail-closed. |
| Politics, parties, and route state | Missing | Missing | No package-specific ruling-party, popularity, law, route, diplomacy, or cleanup setup. Vanilla democratic setup remains in country history. |
| Leaders and characters | Unresolved | Unresolved | Vanilla names exist, but no Event 006 source/provenance package or runtime leader choice has been accepted. |
| Portraits | Unresolved | Unresolved | Vanilla GFX use generic Europe textures; no grounded Event 006 source-placeholder package is registered. |
| Flags | Vanilla only | Vanilla only | Vanilla base and ideology flags exist; Event 006 identity/route flag package is not source-approved or wired. |
| Advisors and high command | Missing | Missing | No package-specific advisor, high-command, commander, or institutional leadership package. |
| Focus integration | Missing | Missing | Shared Event 006 framework has no NAV/GLC package-gated overlay. No bespoke tree is authorized by this audit. |
| Decisions and missions | Missing | Missing | No package-specific decisions, missions, costs, tooltips, or lifecycle cleanup. |
| Ideas and national-spirit lifecycle | Missing | Missing | No starting-crisis, stabilization, route replacement, or icon package. |
| Starting forces and equipment | Missing | Missing | Force mapping rows exist, but no dynamic setup consumes mapping `67` or `50`. |
| Technology, industry, supply, and production | Vanilla only | Vanilla only | Vanilla tech and state history are present; no package origin, production, depot, port, or supply adapter exists. |
| AI strategy and playability | Missing | Missing | No IW-013/IW-015 AI profile, focus weights, route selection, survival behavior, or diplomatic behavior. |
| Localisation | Registry prose only | Registry prose only | No package-specific player-facing country, party, leader, idea, focus, decision, mission, tooltip, or debug localisation set. |
| Asset manifests and GFX wiring | Missing | Missing | No Event 006 identity, flag route, portrait, idea, focus, decision, or advisor manifest. |
| Event docs and spreadsheet alignment | Partial planning only | Partial planning only | Registry, research, force mapping, and generic package docs exist; no complete package event document or implementation evidence exists. |

## File-surface checklist and exact findings

### Present allocator and registry surfaces

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:14` defines IW-013 as a Level 2 industrial mountain package with language, industry, fueros, host relations, and five route families.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:16` defines IW-015 as a Level 1 agrarian coastal package with constitutional, agrarian, cultural, traditional, and patron-client routes.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:14` and `:16` bind `NAV` and `GLC` to reuse-registered-tag origins and require a sourced period-valid male leader or authentic institutional material before release.
- `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:17-18` bind `RG-171` and `RG-172` and require rebind against the installed map.
- `common/script_constants/006_independence_wave_package_constants.txt:64,66,498-499` defines package ids `13`, `15` and reservation ids `RG-171`/`RG-172`.
- `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt:9-20,27-38` exposes planning triggers for both packages.
- `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt:9-20,31-42` loads metadata and carrier scopes; `:182-193` publishes reservations; `:124-135,167-169` includes both packages in automatic weight preparation.

### Missing runtime package surfaces

- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` has no IW-013 or IW-015 setup, final-validation, or cleanup branch.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` omits IW-013 and IW-015 from `has_independence_wave_runtime_package_adapter_for_execution_id`, content attestation, and package-specific preflight allowlists.
- `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt` and `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt` implement only IW-017 `COR`, IW-018 `ARX`, and IW-019 `ASX`; they are not NAV/GLC adapters.
- `common/characters/006_independence_wave_mediterranean_characters.txt` contains only `COR`, `ARX`, and `ASX` rosters.
- `common/national_focus/006_independence_wave_focus.txt` and `common/scripted_effects/006_independence_wave_focus_effects.txt` provide the shared framework and CAT content, but no NAV/GLC focus-gated overlay.
- No package-specific files exist for IW-013 or IW-015 ideas, decisions, missions, AI strategy, country setup, advisor/high-command roster, event cleanup, or runtime localisation.

### Vanilla tag, history, map, and asset evidence

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt` maps `NAV = "countries/Navarra.txt"` and `GLC = "countries/Galicia.txt"`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/NAV - Navarra.txt` uses `capital = 792`, has no OOB, starts democratic at `93`, and defines Ramón Ormazábal Tife (`GFX_portrait_Ramon_Ormazabal_Tife`) and Luis Urrengoetxea (`GFX_portrait_Luis_Urrengoetxea`).
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/GLC - Galicia.txt` uses `capital = 171`, has no OOB, starts democratic at `93`, and defines Fuco Gómez, Alfonso Daniel Castelao, Vicente Martínez Risco, and Santiago Casares Quiroga with vanilla GFX keys.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/171-Galicia.txt` is SPR-owned with GLC and SPR cores, victory points `758` and `6734`, infrastructure `3`, two dockyards, one arms factory, an airbase, and naval base `6` at province `758`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/172-Navarre.txt` is SPR-owned with NAV and SPR cores, victory point `3933`, infrastructure `3`, no industry, and manpower `359880`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/792-Basque Country.txt` is SPR-owned with NAV and SPR cores, victory point `740`, steel `8`, infrastructure `3`, one industrial factory, one arms factory, naval base `1`, airbase `1`, and manpower `928094`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/806-French Basque Country.txt` is FRA-owned with NAV and FRA cores and is an optional extension, not a release anchor under the current installed-map binding.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/countries/Navarra.txt` and `Galicia.txt` retain vanilla South American graphics sets and country colors; no Event 006 country identity override exists.
- Vanilla base and ideology flags exist at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/{NAV,GLC}{,_communism,_democratic,_fascism}.tga` and medium/small variants.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/_leader_portraits.gfx` resolves NAV and GLC leaders to generic Europe textures, not independently sourced Event 006 portrait files.

## Map and state setup issues

The primary unresolved issue is the NAV anchor crosswalk. `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:14` and `006_current_installed_map_binding_audit.md:131` identify state `792` País Vasco as the current compact anchor, while `006_candidate_country_registry.csv:14`, `006_package_research_resolution.csv:14`, `006_state_anchor_and_reservation_groups.csv:18`, and FORM-07 use state `172` Navarre as the baseline anchor. The current loader already uses `792`, so changing the loader alone would discard the installed-map audit and could reserve the wrong state.

The parent must choose and document one contract before package or FORM-07 implementation: current-map compact anchor `792` with `172` and `806` as extensions, or a defended baseline `172` contract with an updated installed-map proof. Any map mutation requires dry-run, review, apply, post-validation, and rollback or recovery evidence; this audit performed no map write.

GLC state `171` is internally consistent across registry, current binding, loader, reservation, and vanilla history. It still needs host-remnant, unique-anchor, tag-living, and ownership validation at runtime.

## Politics, leaders, portraits, flags, advisors, and parties

Both tags inherit vanilla democratic politics and generic country files. No package-specific provisional cabinet, party-name mapping, route ideology, popularity, stability, war-support, law, guarantee, subject, faction, or host-relation setup is present.

The research gate permits a sourced real male period leader valid for the release date, or an authentic archival institutional body when a defensible person cannot be established. Existing vanilla names are usable candidates only after independent source/date review; their generic Europe textures do not satisfy an Event 006 sourced portrait package. No generated fictional leader portrait may be substituted for these grounded packages.

No package-specific leader, advisor, high command, commander, institutional roster, female/male metadata, portrait manifest, flag provenance, route-variant flag, or GFX wiring exists. Do not mark identity or flag readiness until the source package and runtime basename manifest are accepted.

## Focus, decisions, ideas, and asset issues

The shared Event 006 focus framework is available, but NAV and GLC have no package-gated route overlay. A complete tranche should adapt the shared framework rather than create a new bespoke tree. NAV requires visible language-institution, industrial-capacity, fueros or municipal-legitimacy, mountain-security, host-relations, network, patron, and league interactions across constitutional, labor, nationalist, traditional, and patron-client routes. GLC requires port/customs/shipping, municipal/merchant/labor/local-defense, host/recognition/network, and Atlantic or league interactions across constitutional, agrarian, cultural, traditional, and patron-client routes.

Neither package has decisions, missions, timed objectives, starting ideas, lifecycle replacements, trigger tooltips, effect descriptions, AI scores, or icons. The force mapping rows are design inputs only and do not create units or equipment. The only related Event 006 asset rows are generic recognition-diplomacy and infrastructure-authority icon families; they are not country identity assets.

## Starting military, technology, industry, supply, and production

Vanilla NAV and GLC histories provide early infantry, support, mountaineer, artillery, anti-air, reconnaissance, engineers, generic 1939 focus completions, Grand Battleplan, an air-radar special project, and twenty convoys, but neither history has an Event 006 OOB or package-origin production setup.

IW-013 mapping `67` calls for mountain infantry and industrial militia with engineers, reconnaissance, mountain logistics, depots, factory or railway guards, and a professional officer path. IW-015 mapping `50` calls for territorial infantry and coastal guards with engineers, reconnaissance, port-access logistics, inland depots, volunteer corridors, and capital or border defense missions. No runtime adapter consumes either mapping, and no package-specific manpower, stockpile, templates, production lines, fuel, trains, convoys, supply-capacity, port, railway, or industry balancing exists.

## AI and playability issues

No IW-013 or IW-015 AI strategy file, route weight, focus weight, decision score, diplomatic behavior, front behavior, reinforcement behavior, or survival profile exists. Without those surfaces, both packages would fall back to vanilla AI and could not pursue their accepted regional identities or protect their compact anchors.

## FORM-07 dependency

`common/scripted_triggers/006_independence_wave_form07_triggers.txt` defines `@FORM07_CAT_ANCHOR = 165`, `@FORM07_NAV_ANCHOR = 172`, and `@FORM07_GLC_ANCHOR = 171`. The same file requires exact CAT/NAV/GLC package candidates, setup completion, identity attestation, X-tag reservation, flag-package readiness, territory adapters, member policy audit, route method, consent, and exact corridor anchors. `common/scripted_effects/006_independence_wave_form07_effects.txt` does not create an X identity or flag and remains fail-closed until those contracts exist.

The current FORM-07 contract therefore has two independent blockers: no NAV/GLC package adapters and no source-approved X identity/flag package. The NAV `172` constant is also stale against the current installed-map binding's compact anchor `792`. Do not add either package to FORM-07 readiness, content attestation, or runtime adapter allowlists as a narrow fix.

## Smallest viable implementation order

1. Reconcile the NAV anchor contract across the current-map binding, research and registry rows, reservation documentation, `common/script_constants/006_independence_wave_formable_constants.txt`, `common/scripted_triggers/006_independence_wave_form07_triggers.txt`, and `common/scripted_effects/006_independence_wave_form07_effects.txt`. Preserve the existing region-02 loader's `792`/`172`/`806` crosswalk unless the parent approves a different map contract.
2. Complete source and provenance review for NAV and GLC leaders or institutional portraits, flags, route variants, and runtime asset basenames. Keep grounded source placeholders separate from any explicitly requested styled replacements.
3. Implement one package adapter per tag with guarded setup, final validation, cleanup, politics, dynamic force setup using mappings `67` and `50`, ideas with lifecycle, decisions and missions, AI strategy, diplomacy and host cleanup, and package-specific localisation. Use the shared Event 006 focus framework with adapted overlays; do not add a generic copied tree.
4. Add package-specific asset manifests, GFX references, and documentation after accepted source packages exist. Update the event spreadsheet only from implementation facts.
5. Add IW-013 and IW-015 branches to package dispatch setup, final validation, cleanup, runtime adapter allowlists, and preflight only after the above surfaces are complete. Keep exact content attestation blocked until an independent country-package audit passes.
6. Re-evaluate FORM-07 corridor and identity readiness only after CAT, NAV, and GLC are all complete and the X identity/flag package is accepted.

## Validation and handoff

Read-only validation covered the accepted registry, research, reservation, force-mapping, current-map binding, region-02 loaders, dispatch allowlists, FORM-07 triggers/effects, vanilla country histories, state histories, country files, flags, and leader GFX references. No gameplay files were changed. No map write, tag allocation, focus rewrite, event mutation, asset generation, or in-game test was performed.

Remaining risks are the unresolved NAV `792` versus `172` anchor contract, absent sourced identity and flag manifests, absent NAV/GLC runtime adapters, absent package gameplay surfaces, and FORM-07's deliberate fail-closed state. This handoff is not a completion or attestation claim.

## Current amendment — 2026-08-05

The installed-map contract is now authoritative for this tranche: IW-013/NAV uses compact anchor state 792 (País Vasco), with states 172 (Navarra) and 806 (French Basque) retained only as optional extension objectives, and IW-015/GLC uses compact anchor state 171 (Galicia).

The NAV and GLC package setup, final-validation, and cleanup adapters are source-wired and dispatchable through the Iberian package effects and central Event 006 package dispatch, but they do not authorize execution by themselves.

Independent source, identity, flag, portrait, and country-package audits remain open, so IW-013 and IW-015 stay outside central content attestation and the runtime/scenario execution gate remains fail-closed.

No advisor icons or advisor portrait assets were created or authorized, no X identity or flag fallback was introduced, and FORM-07 remains fail-closed pending its researched Iberian identity and member/integration contract.

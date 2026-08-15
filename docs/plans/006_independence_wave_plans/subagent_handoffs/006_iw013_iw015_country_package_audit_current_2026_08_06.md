# Event 006 IW-013/NAV and IW-015/GLC current country-package audit

Date: 2026-08-06.

Scope: current source and engine-evidence audit of the vanilla-carrier Iberian packages IW-013 (NAV) and IW-015 (GLC). This handoff is read-only; no gameplay files were changed by this audit.

## Verdict

Both packages are source-wired adapters over the vanilla NAV and GLC carriers, but remain HOLD / FAIL-CLOSED for independent admission. The current implementation preserves vanilla country history, leaders, flags, starting forces, and technologies, then layers the shared Event 006 framework and package-specific ledgers, decisions, ideas, force mappings, and AI profiles.

The central content-attestation gate intentionally excludes `iw_013` and `iw_015` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`. Adapter and preflight branches mention both IDs, but the missing attestation keeps the packages unavailable to the admitting path. Do not remove this exclusion until source, identity, flag, portrait, and independent package attestations are promoted.

## Country-package coverage checklist

| Surface | IW-013 / NAV | IW-015 / GLC | Result |
|---|---|---|---|
| Tag and package crosswalk | `original_tag = NAV`, `package_id = iw_013` | `original_tag = GLC`, `package_id = iw_015` | PASS |
| Installed-map anchor | State 792 (País Vasco compact anchor) | State 171 (Galicia compact anchor) | PASS; MCP map evidence below |
| Former-host protection | Event target and protected-state ownership/controller guards | Event target and protected-state ownership/controller guards | PASS; fail-closed when absent |
| Vanilla carrier history | `history/countries/NAV - Navarra.txt` | `history/countries/GLC - Galicia.txt` | PASS; no duplicate mod country files |
| Leader proof | Vanilla `Ramón Ormazábal Tife` country-leader check | Vanilla `Fuco Gómez` country-leader check | PASS for leader identity; command roster remains partial |
| Full command roster | Country leader only; no army commander/command-staff proof | Country leader only; no army commander/command-staff proof | PARTIAL / blocker for complete-roster claim |
| Politics and parties | Setup writes democratic provisional politics and four party names | Same | PASS source-wired |
| Package ledger | `independence_wave_nav_fueros_legitimacy`, `independence_wave_nav_industrial_capacity` | `independence_wave_glc_council_legitimacy`, `independence_wave_glc_port_capacity` | PASS |
| Lifecycle ideas | NAV crisis/mature pair and five route ideas | GLC crisis/mature pair and five route ideas | PASS; cleanup wired |
| Focus framework | Shared `independence_wave_focus_tree` assignment and readiness checks | Same | PASS source-wired; not independently attested |
| Decisions and mission | Iberian category, 11 paid projects, mission ledger path | Iberian category, 11 paid projects, mission ledger path | PASS; network cancellation patch already present |
| Starting force mapping | Shared package mapping p13 mountain-frontier | Shared package mapping p15 territorial-defense | PASS source-wired |
| Technology | Vanilla carrier starting technology retained; no package-local tech tree | Same | PASS source-wise; Technology Tree Viewer helper analysis partial |
| AI profile | NAV survival/host-restraint/settled-industry/emergency profiles | GLC survival/host-restraint/settled-port/emergency profiles | PASS source-wired; probability compare parent-owned |
| Portraits | Runtime source placeholder exists; no Aguirre consumer | Runtime source placeholder exists; vanilla Castelao rostered | HOLD; portrait worker evidence not promoted |
| Flags | Vanilla NAV flag is Navarrese; no neutral compact Basque flag | Vanilla GLC flag is plain white/blue diagonal; date/rights caveat | HOLD; flag audit says `SAFE_FLAG_ATTESTATION=NO` |
| Advisors and icons | No package advisor/icon surface | No package advisor/icon surface | PASS by design; do not invent |
| Cleanup | Package ideas, mission, decisions, variables, and shared generation state cleared | Same | PASS |

## File surface checklist

### Mod files inspected

- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`.
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
- `common/decisions/006_independence_wave_iberian_decisions.txt`.
- `common/ideas/006_independence_wave_iberian_ideas.txt`.
- `common/ai_strategy/006_independence_wave_iberian.txt`.
- `common/script_constants/006_independence_wave_iberian_constants.txt`.
- `common/national_focus/006_independence_wave_focus.txt`.
- `common/scripted_effects/006_independence_wave_force_package_effects.txt` and the corresponding force-package triggers used by p13/p15.
- `interface/006_independence_wave_iberian_portraits.gfx` and the runtime placeholder DDS files under `gfx/leaders/006_independence_wave/`.

No mod `common/country_tags`, `common/countries`, `history/countries`, or `common/characters` file was found for NAV or GLC. This is intentional vanilla-carrier reuse, not a missing registration.

### Vanilla references inspected

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt` maps `NAV` to `countries/Navarra.txt` and `GLC` to `countries/Galicia.txt`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/NAV - Navarra.txt` retains capital 792, vanilla starting technology/equipment, political setup, and leaders `Ramón Ormazábal Tife` and `Luis Urrengoetxea`.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/GLC - Galicia.txt` retains capital 171, vanilla starting technology/equipment, political setup, and leaders `Fuco Gómez`, `Alfonso Daniel Castelao`, `Vicente Martínez Risco`, and `Santiago Casares Quiroga`.

## Map and state setup evidence

The read-only `hoi4_map_inspect` result for states 792 and 171 is `MAP_INSPECTED`.

- State 792: capital province 740, category `town`, owner/controller SPR, cores NAV+SPR, 928,094 manpower, one air base, one arms factory, one civilian factory, infrastructure 3, naval base 1, steel 8, and victory point 10 at province 740.
- State 171: capital province 758, category `city`, owner/controller SPR, cores GLC+SPR, 2,295,085 manpower, air base 2, arms factory 1, dockyards 2, infrastructure 3, naval base 6, and victory points 5/3 at provinces 758/6734.
- Optional NAV extensions in states 172 and 806 are not compact setup anchors. State 172 is SPR-owned with NAV+SPR cores; state 806 is FRA-owned with NAV+FRA cores. Existing objective/host guards must remain in force before any extension or transfer.
- State membership, region membership, and supply/rail networks are valid for the inspected records. The MCP also reported 1,323 global `MAP_BUILDING_POSITION_INVALID` and 1,331 global `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics in the mod map. They are not localized to 171 or 792 and are outside this country-local scope; no map rewrite is justified.

Map artifact references:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/868f7d5220e9eb37953355c9718ade1575c8f91ad2a0a721e85dd75d54394e55/f0b4ced0f98b2e6cb3a12bdf9e50f9cd401cebc212297d7656661320585e1010/map-inspect.86c2162b7e587fa8.json` for states 792/171.
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5cd4434b8050b970cc315e2a6fb3598d7a70463f5a87afe1a193c305e952deae/b1bc334dfe3e6dee4c176c5113ac2530ae08e14d0009d33edefa9d6b0f179c19/map-inspect.86c2162b7e587fa8.json` for optional states 172/806.

## Politics, leaders, portraits, flags, advisors, and parties

The setup effects correctly initialize the package-specific democratic provisional state, party names, popularity, stability/war-support inputs, and ledgers. The vanilla leader IDs and names are used as the initialization proof and no duplicate character records are introduced.

The command-roster helpers currently prove only `has_country_leader` for the named vanilla leader. They do not prove an army commander or a complete command staff. This is a real limitation for a complete-roster attestation, but adding a commander would invent identity and is outside the allowed small patch.

The portrait handoff remains source-placeholder state. `portrait_NAV_jose_antonio_aguirre.dds` is not a current NAV leader consumer; the GLC Castelao portrait already exists in the vanilla roster, while the mod placeholder is not an admission proof. Keep portrait worker provenance and final identity review unresolved.

The flag audit remains authoritative: vanilla `NAV.tga` depicts Navarrese red/gold chains and arms, not a defensible neutral compact Basque baseline; vanilla `GLC.tga` is a plain white/blue diagonal with historical/date and rights caveats. There are no mod flag overrides or cosmetic tags. `SAFE_FLAG_ATTESTATION=NO`; do not silently substitute either carrier flag for an admitted regional identity.

No package-specific advisors or advisor icons are present or required by the current spec. Do not create symbolic or invented advisors as a workaround.

## Focus, decisions, ideas, and assets

Both carriers receive the shared `independence_wave_focus_tree` only after the generic full-framework checks. The read-only focus inspection returned `FOCUS_INSPECTED` for `common/national_focus/006_independence_wave_focus.txt`, with tree ID `independence_wave_focus_tree`, 184 focuses, and no proposed or changed files. Its artifact is:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cbf01e1df3961186f1d658ffc9d9a2d01c13ac87cb3ebc4e6a65ee4fb7cbdf20/906857f3e93d5683e6b36463382dc6f9b044f98e1a98b6df74cc75f1a6c256ee/focus-inspect.d527cf63a0416797.json`.

The focus report is workspace-wide and contains 14 diagnostics, including missing vanilla continuous-focus sprite references and layout warnings. None is a NAV/GLC package-local focus icon defect. The shared framework remains source-wired but not independently admitted.

The Iberian decision file contains both 11-project categories and the mission/ledger paths. The separate current handoff `006_iw013_iw015_network_cancel_patch_2026_08_06.md` records the already-applied fix that cancellation also checks loss of the League-route flag. This audit did not duplicate or alter that patch.

The Iberian idea file contains package crisis/mature lifecycle pairs plus route ideas, and the package cleanup removes them. Icons are shared existing assets; no new country icon is justified.

## Starting military, technology, industry, supply, and production

NAV and GLC retain the vanilla history starting technology, equipment, production, convoy, industry, supply, and capital setup. The package effects apply force mapping p13 (NAV mountain-frontier) or p15 (GLC territorial-defense) only when the command-roster and force readiness gates pass. No local technology tree or new equipment surface is introduced.

The read-only Technology Tree Viewer scan returned `TECH_INSPECTED_PARTIAL` with 654 technologies, 18 folders, 475 placements, 457 edges, and 820 unlocks. Helper projections were deferred for the large workspace, so this is direct scan evidence rather than a package-specific technology proof. Artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dff513ec593f7402634c5217f793f77e89ffde0a6be97db4d4ac22e6c86fb43b/276535db5f5b20a456c9f02675dfab766981ea2a4d1d23f7e5524198684a8e50/technology-scan-a06f0e6cdd06.json`.

Because neither package adds technology or equipment definitions, no country-local technology patch is warranted. The remaining limitation is lack of a package-specific helper projection in the large scan.

## AI, playability, and weighted logic

`common/ai_strategy/006_independence_wave_iberian.txt` contains distinct NAV survival, host-restraint, settled-industry, and emergency profiles and distinct GLC survival, host-restraint, settled-port, and emergency profiles. The values are centralized in the Iberian constants file and match the file-scoped AI constants.

This audit did not claim quantitative AI balance. The required named-scenario `hoi4.probability_inspect` and `hoi4.probability_compare` pass remains parent-owned and must be run by `chaosx_ai_probability_auditor` before any weighted surface is admitted or tuned.

## Lifecycle, cleanup, and central gates

Setup dispatch, final validation, and cleanup dispatch include both Iberian adapters. Package cleanup removes the mission, all package decisions, package ideas, package-specific variables, setup flags, force-applied state, command-roster state, and shared Event 006 generation state through the existing reset helper. No world-iterating on-action was added.

The central attestation trigger intentionally excludes IW-013 and IW-015 even though adapter/preflight selectors include the IDs. This is the expected fail-closed posture. FORM-07 and any regional formable admission remain separately fail-closed.

Event MCP inspection returned `EVENT_INSPECTED_PARTIAL` and event lint returned no blocking diagnostics, with large-workspace helper/lifecycle passes deferred. Artifacts:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe37e43f21c5df01dc1619688a68d2cf893e0e25f055de745c6784290ec9a61b/628100ee625d47d40fdd0cf97761017af4f14f716ac6c4467c6b3a8ea495ed22/event-scan-be8a459e7129.json`.
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43d598a4d0ce4a08b19260aa9eee065d7f677c2117ade611313cf528a3535e53/3a9475c58ef0f832977fe478aa1198c9797c2cdb541262e380528782ff64c105/event-lint-be8a459e7129.json`.

## Missing, stale, or blocked surfaces

- Independent source/identity/flag attestations for both packages are not promoted.
- NAV flag provenance does not support a neutral Basque admission; GLC flag provenance has historical/date and rights caveats.
- Portrait placeholders are not final source/identity evidence.
- Complete command roster is not proven beyond the country leader.
- Named AI probability scenarios have not been evaluated by the required auditor.
- Focus and technology MCP reports are partial at workspace scale; no package-local blocking focus or technology defect was isolated.
- Global map diagnostics remain outside this country-local scope.

## Patch record

Changed files in this audit: none.

The existing network-cancel fix is recorded separately in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_network_cancel_patch_2026_08_06.md`; it is not part of this audit patch set.

No safe small country-package patch was justified. Adding a commander, changing NAV/GLC flags, wiring Aguirre, adding cosmetic tags, or admitting the IDs would violate the current identity/provenance gates.

## Parent follow-up

Keep `iw_013` and `iw_015` excluded from central content attestation. Route final source/identity/flag/portrait evidence through the designated workers, then rerun the independent country-package audit. Run the named probability baseline/compare scenarios through `chaosx_ai_probability_auditor`. Re-review the optional NAV states 172/806 only when a grounded territorial-expansion design is accepted.


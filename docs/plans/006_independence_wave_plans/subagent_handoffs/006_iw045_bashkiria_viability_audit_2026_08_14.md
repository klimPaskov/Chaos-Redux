# IW-045 Bashkiria (BSK) viability audit

> Superseded package snapshot. IW-045 package-local gameplay, focus, decisions, localisation, route assets, and grounded portrait runtime integration were added after this initial viability audit. The current admission disposition remains fail-closed because central adapter/attestation/Join gates and typed AI evidence are still unresolved. See the current core, portrait runtime, localisation, and package-admission handoffs.

Date: 2026-08-14

Scope: read-only country-package admission audit for the next Event 006 independence-wave tranche. No gameplay, asset, central attestation, dispatcher, or Join files were changed.

## Disposition

**FAIL-CLOSED. IW-045 is not safe for bounded Event 006 implementation or admission.**

BSK has a valid vanilla country, a registry row, a reservation row, and a region-05 candidate wrapper, but it does not have a complete current-generation Event 006 country package. The current package surface is predominantly registry/planning data plus Event 005 Soviet-collapse content. Event 006 dispatch preflight explicitly requires both an exact package adapter and exact content attestation (`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:203-208`); IW-045/BSK is absent from those package-ID branches. The static evidence therefore cannot justify promotion, central admission, or a Join/runtime claim.

## Coverage checklist

| Surface | Evidence | Status |
|---|---|---|
| Tag and identity | Vanilla `BSK = "countries/Bashkortostan.txt"`; `common/script_constants/006_independence_wave_country_registry_constants.txt` includes BSK in registry/availability arrays; IW-045 resolves to BSK in `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` and `research/006_package_research_resolution.csv` | Registered, but not Event 006-admitted |
| Vanilla country history | Vanilla `history/countries/BSK - Bashkortostan.txt`: capital 651, three research slots, democratic 1936 setup, 50/10/20/20 popularity, starting technologies, `recruit_character = BSK_yakov_bykin` | Reusable baseline; must not be duplicated or silently replaced |
| Map anchor | IW-045 and RG-651 bind to state 651/Ufa; installed binding records `651=SOV`, `SOV=219`, compact anchor and host-remnant rule | Static binding only; required MCP map evidence unavailable |
| Event 005 origin/collision | `005_soviet_collapse_triggers.txt` checks BSK with `soviet_collapse_breakaway`; `005_soviet_collapse_effects.txt:4085` cores state 651 for BSK and has BSK league/republic paths; `005_soviet_collapse_republics.txt:3884-3990` contains a BSK-specific focus branch | Blocking origin-separation risk |
| Event 006 adapter/attestation | No `iw_045`/`IW-045`/BSK branch in `006_independence_wave_package_dispatch_triggers.txt`; prior parity audits identify IW-045 among registry/binding-only rows, not current-admission rows | Missing; blocking |
| Event 006 execution/cleanup/Join | Generic execution requires adapter, force probe, and runtime preflight; no BSK-specific execution, materialization, cleanup, or Join proof | Missing; blocking |
| Politics/parties | Vanilla BSK has democratic ruling party and ideology names in installed localisation | Vanilla coverage only; no Event 006 opening/route/party adapter |
| Leader/character | Vanilla `BSK_yakov_bykin` is recruited from country history; mod Event 005 can create institutional `Oilfield and Ural Workshop Council` (`005_soviet_collapse_effects.txt:14884`) with `GFX_portrait_BSK_oilfield_workshop_council` | No Event 006 leader/institution handoff or provenance attestation |
| Portraits | Mod contains `gfx/leaders/005_soviet_collapse/BSK_leader.dds` wired by `interface/005_soviet_collapse.gfx:1961`; no BSK Event 006 portrait package/manifest | Event 005 asset only; not admission-ready |
| Flags | Vanilla BSK political flags exist under installed `gfx/flags/BSK_*`; no mod IW-045 route flag/asset manifest | Reuse needs origin/identity review; no Event 006 evidence |
| Focus tree | Event 005 BSK focuses exist (`internal_soviet_collapse_bashkir_cavalry_oath`, `internal_soviet_collapse_bashkir_oilfield_security`, `internal_soviet_collapse_ural_mobile_defense`, `internal_soviet_collapse_volga_ural_compact`) | Existing Soviet-collapse tree, not an IW-045 tree or validated additive adapter |
| Decisions/missions | BSK appears in IW-043/058 representation/member arrays and FORM-12/13 state puzzle checks, but those are CHU/ASY signature systems, not an IW-045 package | No BSK-owned Event 006 decision/missions |
| Ideas | Event 005 has `iul_tatar_bashkir_committees` and corresponding icon | Existing Event 005 content; no Event 006 lifecycle package |
| Forces/technology/industry/supply | Planning row specifies mounted mobile force, cavalry/frontier infantry/defectors, depots, and rail/remount risks; vanilla history has no OOB and only baseline buildings/tech | Design direction only; no materialization or runtime stockpile/manpower/supply proof |
| AI/probability | Generic Event 006 AI matrix profiles exist; no BSK-specific AI strategy surface found | No package-specific AI evidence; probability MCP unavailable |
| Formables | BSK is an invited member candidate for FORM-12 Volga-Ural and FORM-13 Idel-Ural in `006_independence_wave_formable_state_puzzle_triggers.txt:314,321`; this is membership support, not an IW-045 release package | Conditional/shared only |
| Localisation | Vanilla BSK country/adjective/ideology strings exist; Event 005 Bashkir focus/idea/decision strings exist | No Event 006 country package text/route proof |
| Assets/manifests | Event 005 focus icons, idea icon, decision icon, and BSK portrait are present | No IW-045 asset manifest or portrait-worker handoff |

## File-surface findings

### Registry, binding, and central preflight

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:46` defines IW-045 as Bashkiria, resolved tag BSK, anchor state 651/Ufa, reservation group RG-651, compact territory, and the mounted/cavalry force direction.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:46` requires a defensible sourced period leader or institution and says to reuse the base flag only when identity and origin match. It also requires rebind against the installed map and a full collision check.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:46` is a static accepted baseline (`651=SOV`, `SOV=219`) and says runtime ownership is authoritative.
- `common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:29-30` only checks BSK tag availability and state-651 anchor availability. It does not constitute a country package adapter or attestation.
- `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:38-40` saves BSK and state 651 as generic liberation targets. This is reservation plumbing, not complete implementation.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-52` and `:156-208` contain exact adapter/content-attestation/preflight gates. There is no IW-045/BSK branch. The same file’s existing branches include IW-044 and IW-043/IW-058, demonstrating the missing exact package surface.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:60-68` rejects rows without adapter, force mapping probe, and runtime preflight. No BSK-specific path was found.

Prior Event 006 parity handoffs (`006_event6_country_package_admission_audit_2026_07_29.md`, `006_next_event6_soviet_tag_admission_matrix_2026_07_29.md`, and `006_adapter_attestation_parity_audit_current_2026_08_12.md`) explicitly classify IW-045 among registry/reservation-only rows and state that it must not be promoted from reservation alone. The post-IW044 boundary described in those audits is 39 adapters, 31 content-attested packages, and 162 unattested adapters/rows; IW-045 is not in the admitted set.

### Event 005 collision and origin

- `common/scripted_triggers/005_soviet_collapse_triggers.txt:920` treats `BSK = { exists = yes has_country_flag = soviet_collapse_breakaway }` as a Soviet-collapse breakaway.
- `common/scripted_effects/005_soviet_collapse_effects.txt:4085` adds BSK core to state 651; lines around 6072, 14201, 14222, and 14251 include BSK in Soviet republic news, league, member-count, and league-formation logic.
- `common/scripted_effects/005_soviet_collapse_effects.txt:14884` may create the BSK institutional leader `Oilfield and Ural Workshop Council` using the Event 005 portrait.
- `common/national_focus/005_soviet_collapse_republics.txt:3884-3990` owns a BSK-specific cavalry/oilfield/mobile-defense/Volga-Ural focus branch.
- `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:11-16` distinguishes Event 006 origin from Soviet-collapse origin, and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:207-208` rejects Soviet-collapse flags/origin variables. Any future BSK package must preserve this separation and reject a living/Event 005-origin BSK.

### Vanilla setup and assets

- Vanilla `common/country_tags/00_countries.txt:237` maps BSK to `countries/Bashkortostan.txt`.
- Vanilla `history/countries/BSK - Bashkortostan.txt` uses capital 651, has no OOB, and recruits `BSK_yakov_bykin`.
- Vanilla `common/characters/BSK.txt` defines real male leader `Yakov Borisovich Bykin` with `GFX_portrait_Yakov_Borisovich_Bykin`.
- Vanilla state `history/states/651-Sov state 5.txt` names state 651 Ufa, owner SOV, cores SOV and BSK, infrastructure 3, one civilian factory, victory points 1278/4354, and province list. The mod has no overriding `history/states/651...` file; the binding’s installed-map claim is therefore source-based and still requires engine inspection.
- Installed vanilla political flags are `gfx/flags/BSK_{communism,democratic,fascism,neutrality}` plus medium/small variants. The mod’s only BSK-named leader art is the Event 005 council portrait and must not be treated as an IW-045 final asset.

## Map, focus, event, and probability MCP evidence

The required read-only HOI4 MCP routes were not usable for this audit. Existing Event 006 MCP audits record the exact blocker returned by the server: `ARTIFACT_MANIFEST_INVALID` — “Artifact provenance manifest is invalid” — for workspace `mod_chaos_redux_ea3b2d67c2c0`. A bounded `hoi4_map_inspect` request for state 651 in that workspace also failed to return within the allowed wait. Consequently there is no current engine-backed map ownership/controller/supply/rail/adjacency artifact, no focus inspect/render artifact, no event inspect/render artifact, and no probability baseline for BSK. Static source review is not being substituted for MCP evidence.

The installed package exposes no Technology Tree Viewer. Technology/runtime dependency validation remains unresolved and must be recorded as such by the parent tranche.

## Required gates before reconsideration

1. Design and implement a complete IW-045 package adapter and exact content attestation owned by the parent, without weakening the central preflight.
2. Add origin-gated setup that rejects `soviet_collapse_active_origin`, `liberation_origin.soviet_collapse`, active Event 005 BSK, existing subjects, and duplicate/live-tag conditions.
3. Rebind state 651 against the current map through `hoi4_map_inspect`; prove SOV retains a valid protected remnant and that compact transfer does not take its protected capital.
4. Resolve sourced leader/institution identity and portrait provenance. Keep the vanilla Bykin baseline or provide an explicitly attested Event 006 institutional route; do not silently reuse the Event 005 council portrait as a final.
5. Provide BSK-specific focus/decision/idea lifecycle, localisation, AI strategy, cleanup, force materialization, reinforcement, stockpile/manpower/production, and save/load evidence. Reusing Event 005 focuses alone is not a package.
6. Re-run focus/event/probability MCP inspections and the unavailable Technology Viewer note after the artifact manifest is repaired.
7. Validate FORM-12/FORM-13 invitation/consent/state-puzzle interactions only as shared formable support; do not treat BSK membership as IW-045 admission.

## Final handoff

No gameplay or asset files were changed. The only new file is this audit handoff. The package is **not safe for a bounded implementation tranche** and must remain fail-closed until the missing exact adapter, attestation, origin-safe runtime path, country surfaces, and MCP evidence are supplied.

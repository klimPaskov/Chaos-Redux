# Event 006 IW-014 — Catalonia (`CAT`) country package audit

## Status

`HOLD / NOT CONTENT-ATTESTED`. This is a static readiness audit only. No CAT gameplay, registry, map, focus, decision, idea, AI, or asset file was patched. The current repository contains a selectable IW-014 registry shell, but no CAT package adapter and no CAT additive overlay implementation.

The task wording calls CAT an additive overlay, while the accepted registry and map ledger still describe IW-014 as `automatic_pool_ready_if_not_living` with a registered-tag release. That design contradiction must be resolved by the parent before implementation. I did not convert the row to a fallback or silently change its disposition.

## Country package coverage checklist

| Surface | Result | Evidence and gap |
|---|---|---|
| Tag and country shell | Partial, vanilla only | Vanilla registers `CAT = "countries/Catalonia.txt"` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:200` and supplies `common/countries/Catalonia.txt` with South American graphical culture and color. The Event 006 registry references CAT, but no mod package shell or overlay identity trigger exists. |
| Event 006 registry and loader | Present but stale for runtime | `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt:18-25` admits CAT through the generic content-ready gate and state 165. `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt:20-30` loads IW-014, CAT, RG-165, region, depth, archetype, and anchor 165. Weight/reservation calls remain active at `:128-130`, `:192`, and `:213`. |
| Runtime adapter | Missing | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-24` invokes regional setup dispatch, but `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:1-10,879-898` owns only IW-017 COR, IW-018 ARX, and IW-019 ASX. No CAT setup, final-validation, or cleanup entry is defined. |
| Runtime preflight and attestation | Correctly fail-closed | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-32` has no IW-014 adapter branch; `:66-82` has no IW-014 content attestation; and `:87-176` therefore cannot preflight CAT. Do not add CAT to either OR list until the complete package or approved overlay is audited. |
| Origin and content gate | Closed | `common/scripted_triggers/006_independence_wave_package_triggers.txt:23-49` requires a non-living, origin-safe country and `independence_wave_package_content_ready`. No CAT effect grants that flag. This prevents the existing loader from becoming playable by accident. |
| Scenario ranking | Listed but not executable | IW-014 is ranked in `common/scripted_effects/006_independence_wave_scenario_effects.txt:168`, but the scenario preflight still requires the absent content attestation. |
| State, anchor, and host | Baseline valid; runtime proof missing | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:15` binds CAT to compact anchor state 165 and host SPR. `.../006_current_map_reservation_groups.csv:16` reserves RG-165. Vanilla `history/states/165-Catalonia.txt:4-32` confirms owner SPR, CAT/SPR cores, Barcelona VP 9764, industry, airbase, port, and coal. The binding says SPR retains 41 states, but the runtime package still lacks an explicit host-survival/final-validation witness. Rebind state IDs against any current map override before implementation. |
| Region overlay contract | Not implemented | The Mediterranean/Iberia overlay is `REG-02` in `docs/specs/006_independence_wave_specs/matrices/006_regional_overlay_matrix.csv:3`, with ideological polarization, language/autonomy, land reform, port security, and republican/labor/traditional/military routes. No CAT-specific pressure values, route flags, one-time hook, cleanup, or localisation exists. |

## File surface checklist

Expected CAT/Event 006 surfaces and current state:

- Registry constants and candidate trigger: present in `common/script_constants/006_independence_wave_country_registry_constants.txt:21-41,56-60,118-120` and `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt:155`; these are registry metadata only.
- Region loader, weight, reservation: present in `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt:20-30,128-130,192,213`.
- Package setup/final-validation/cleanup: missing for IW-014; only the COR/ARX/ASX functions exist in `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt`.
- Dispatch trigger adapter, exact CAT origin branch, and content attestation: missing by design in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
- CAT decisions, missions, ideas, scripted effects, scripted triggers, AI strategy, focus route, events, and localisation: no CAT/IW-014-specific package files or gameplay identifiers were found under the mod `common`, `events`, `localisation`, `interface`, or `gfx` surfaces. Registry-only CAT matches and unrelated `CAT` acronyms remain. The existing Mediterranean files (`common/decisions/006_independence_wave_mediterranean_decisions.txt`, `common/ideas/006_independence_wave_mediterranean_ideas.txt`, `events/006_independence_wave_mediterranean.txt`, and `common/ai_strategy/006_independence_wave_mediterranean.txt`) contain only COR, ARX, and ASX IDs.
- Documentation/asset provenance: the research rows exist, but no CAT-specific Event 006 implementation handoff or final asset manifest existed before this audit. Vanilla base assets must not be treated as Event 006 source attestation without the required provenance check.

## Map and state setup issues

Vanilla state 165 is a compact Catalan anchor and is currently coherent for a dormant registered-tag release: owner SPR, cores CAT and SPR, Barcelona VP 9764, two factories, an airbase, a level-four naval base, and two coal. The package binding records `165=SPR`, `SPR=41`, and an unchanged current-ID baseline. The anchor is not a standalone overlay carrier, however, and there is no CAT-specific final validation proving that the host remains viable after any transfer. Any future implementation must preserve the protected host state, avoid taking a host capital when a safe alternative exists, and rerun the installed-map rebind.

## Politics, leaders, portraits, flags, advisors, and parties

Vanilla CAT history (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/CAT - Catalonia.txt:68-101`) starts democratic with 50 democratic, 3 fascist, and 47 communist popularity, recruits `CAT_lluis_companys`, and creates Andreu Nin, Daniel Cardona, and Francesc Cambó with vanilla portrait keys. `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/CAT.txt:4-17` defines Lluís Companys as a liberalism country leader with `GFX_portrait_CAT_lluis_companys`. These are existing vanilla identities, not an Event 006 leadership audit. The research resolution requires a defensible period-valid sourced leader or an authentic provisional institution; no CAT source/portrait attestation is present in the mod handoff surface.

Vanilla `common/ideas/catalonia.txt` supplies CAT-gated advisor/high-command/theorist IDs (`CAT_democratic_guy`, `CAT_communist_guy`, `CAT_fascist_guy`, `CAT_pot`, `CAT_coi`, `CAT_stc`, `CAT_aco2`, `CAT_acd2`, `CAT_acr`, `CAT_acgs`, `CAT_nccr`, `CAT_ncm`, `CAT_ar`, `CAT_ai2`, `CAT_aa2`, `CAT_acas`, `CAT_ncs`, `CAT_mt`, and `CAT_nt`). No Event 006 lifecycle ideas, party-name overrides, institutional council, or cleanup calls preserve and rebind these advisors. The repository `common/countries/cosmetic.txt:331-334` also contains `CAT_aragon`; no Event 006 route uses or validates that cosmetic identity. Do not invent a leader, portrait, flag, or party source to close this gap.

## Focus, decision, idea, and asset issues

Vanilla CAT history completes generic focuses on the 1939 date block, but no CAT national-focus file or Event 006 focus/overlay assignment exists. The shared Event 006 focus framework is not a CAT adapter. An approved additive overlay would need an exact carrier/route-state trigger, a one-time activation flag, route-local decisions/missions, lifecycle ideas, cleanup, localisation, and proof that the carrier's existing focus tree, history, cores, autonomy, and state transfers are untouched. The existing overlay precedent is IW-022 (`common/scripted_triggers/006_independence_wave_iw022_dalmatia_triggers.txt:9-19` and `common/scripted_effects/006_independence_wave_iw022_dalmatia_effects.txt:230-328`), but CAT is a static vanilla tag rather than a CRO-origin dynamic carrier, so the trigger contract cannot be copied without a design decision.

No CAT-specific decision category, mission, idea file, icon registration, flag package, portrait manifest, event incident, or localisation file exists in the mod. The general CAT acronym matches in unrelated files and broad target allowlists are not CAT package coverage.

## Starting military, technology, industry, supply, and production issues

Vanilla CAT history has no OOB (`#oob = ""`), sets 20 convoys, and supplies a small infantry/support/mountaineer/truck/artillery/anti-air technology baseline plus DLC-conditional early aircraft (`CAT - Catalonia.txt:1-43`). State 165 has one arms factory, one civilian factory, infrastructure 4, airbase 2, naval base 4, and coal 2. The Event 006 force mapping prescribes `industrial militia, coastal defense, regular defectors`, `regular_defectors`, force level 72, inherited-force and navy/air oversight, but no executable CAT force profile or `independence_wave_load_force_package_mapping` path exists. No CAT starting production, templates, manpower materialisation, equipment stockpile, supply, or inherited-asset preservation effect is wired.

## AI and playability issues

No CAT AI strategy profile, focus weights, decision AI, diplomatic route, host settlement, recognition, Mediterranean republic league/Iberian federation formable registration, or cleanup behavior exists. The generic allocator can retain a zero weight because the content-ready flag is absent, but it still exposes IW-014 in the ranked registry and can reserve state 165 if that gate is ever granted without adding the missing adapter. CAT must remain non-attested until the full setup and playability contract is implemented and reviewed.

## Validation performed

- Read the required Event 006, focus-tree, subagent, offline wiki, and vanilla documentation guidance before inspection.
- Compared the IW-014 research/registry/map-binding rows with the live CAT registry, region loader, dispatcher, preflight, scenario ranking, and Mediterranean package files.
- Read the installed vanilla CAT country, history, character, state, country-tag, cosmetic, focus, and idea surfaces.
- Performed exact identifier searches across mod `common`, `history`, `events`, `localisation`, `interface`, and `gfx` surfaces. No in-game process or save was launched.

## Changed files and remaining risks

Only this dated audit handoff was added. No gameplay or asset files were changed. CAT remains fail-closed and is not admitted to `content_attestation`.

Blocking work for the parent is to choose one design: (1) complete IW-014 as a registered-tag Level 2 country package and add its exact adapter, or (2) reclassify IW-014 as a true additive overlay with an identified living carrier and one-time route hook, then remove or fail-close the standalone allocator row. Either path requires sourced identity/asset evidence, state/host validation, setup/final-validation/cleanup, decisions/ideas/localisation, AI, force materialisation, and a post-wiring audit before any attestation change.

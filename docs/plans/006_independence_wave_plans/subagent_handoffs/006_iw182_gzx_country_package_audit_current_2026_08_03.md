# IW-182 GZX Newfoundland country-package audit

Date: 2026-08-03

Scope: read-only country-package audit for Event 006 Independence Wave candidate `IW-182`, Newfoundland, registered tag `GZX`, anchor state `331`, compact state `332`, and reservation group `RG-331`.

Authority: current post-v104 Event 006 completion evidence and resume packet, the accepted one-tree generic-focus contract, the current registry/planner/adapters, current source assets, and the installed vanilla state history as inspected on 2026-08-03.

## Overall verdict

`IW-182` / `GZX` is **BLOCKED / shell-only** and must not be promoted into the Event 006 admitted package set.

The tag, registry row, reservation metadata, state binding, flag family, force mapping, generic focus source, and generic decision/mission framework are present as static framework surfaces. The country has no runtime package adapter, no setup/final-validation/cleanup dispatch, no package attestation, no playable identity/politics/leader/idea package, no package AI profile, and no runtime force application path. The neutral history shell is therefore not a playable Newfoundland package.

The correct eventual contract is the accepted **full generic-focus framework** assignment because `GZX` has no meaningful vanilla focus carrier to preserve. Portrait-rights clearance is necessary for promotion, but it is not sufficient. A promotion review also needs a sourced identity roster, runtime adapter and attestation, full package setup and cleanup, politics and ideas, package AI, force application, localisation, asset wiring, and transaction-level validation.

FORM-02 is a separate gate. `GZX` may be admitted as an independent Event 006 package without FORM-02, but the package must not advertise or commit North Atlantic Compact formation until the independent FORM-02 founder and member proof succeeds.

No gameplay files were changed by this audit. No fallback identity, generic portrait, generated historical flag, or admission shortcut is authorized.

## Country-package coverage checklist

| Surface | Status | Evidence and exact boundary |
| --- | --- | --- |
| Tag registration | **PASS static** | `common/country_tags/006_independence_wave_countries.txt:100` registers `GZX = "countries/006_independence_wave_GZX.txt"` for `IW-182`. The protected-tag scan reports zero external country-definition or identity-surface collisions. |
| Candidate registry | **PASS static / not attested** | `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:183` defines `IW-182`, Newfoundland, `GZX`, Americas and Caribbean, automatic-pool-ready, anchor `331`, `RG-331`, compact North Atlantic scope, and sourced historical flags/leaders. A registry row is not package-content attestation. |
| Reservation binding | **PASS static / runtime unproven** | `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:28`, `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:183`, and `.../006_current_map_reservation_groups.csv:28` bind `RG-331` to states `331|332` and host `ENG`. Runtime host-survival, allocator, and save/load evidence is absent. |
| Country definition | **SHELL ONLY** | `common/countries/006_independence_wave_GZX.txt:1-11` supplies only graphical cultures and colour. Its comments explicitly defer territory, capital, politics, leaders, forces, ideas, focus, and AI to runtime package code that does not exist for GZX. |
| Country history | **SHELL ONLY** | `history/countries/GZX - Newfoundland.txt:1-16` uses `ruling_party = neutrality`, `elections = no`, and neutral popularity `100`, with comments describing a runtime replacement. No GZX setup effect replaces this shell. |
| Map/state ownership | **STATIC BINDING / runtime unproven** | Vanilla `history/states/331-Newfoundland.txt` and `332-Labrador.txt` currently use `owner = ENG`; state `331` has the Newfoundland port and state `332` is Labrador. Event 006 runtime ownership is authoritative, but no GZX transaction commits it. |
| Force mapping | **PASS static / unapplied** | `common/script_constants/006_independence_wave_force_package_constants.txt:259,473,687,901,1115` maps `p182` to profile `5` (`coastal_maritime`), tradition `60`, reinforcement mask `535`, navy/air inheritance mask `3`, and research sensitivity `0`. `common/scripted_effects/006_independence_wave_force_package_effects.txt:337-372` can load this mapping, but no GZX adapter invokes it. |
| Focus contract | **SOURCE AVAILABLE / UNASSIGNED** | `common/scripted_effects/006_independence_wave_focus_effects.txt:29-85` provides `independence_wave_assign_focus_framework`; no GZX package setup calls full-framework assignment or sets the generic AI profile. The accepted tree is `independence_wave_focus_tree`, not a bespoke Newfoundland tree. |
| Decisions and missions | **GENERIC SOURCE AVAILABLE / PACKAGE UNWIRED** | `common/decisions/006_independence_wave_decisions.txt` and Event 006 mission sources are generic and can operate after activation. No GZX-specific decision, mission, route, or unlock consumer exists. |
| Leaders and characters | **MISSING** | No GZX character definition or leader consumer was found under `common/characters`, `common/country_leader`, or related Event 006 sources. |
| Portraits and rights | **SOURCE-ONLY / RIGHTS BLOCKED** | `docs/assets/006_independence_wave/gzx_newfoundland_portrait_source_research_2026_08_03/` contains a William R. Howley 1937 source crop and research images, but no rights/provenance manifest, processed runtime portrait, DDS/GFX consumer, character block, or role/date acceptance. |
| Flags | **STATIC FAMILY PASS / GZX ART REVIEW OPEN** | `gfx/flags`, `gfx/flags/medium`, and `gfx/flags/small` contain the GZX base and four ideology variants. The strict Event 006 flag audit reports 102/102 complete families, while `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02_chunk3/manifest.md:12` and `metadata/asset_manifest.csv:5` retain GZX Newfoundland as `needs_user_review`. |
| Ideas and advisors | **MISSING** | No GZX starting idea, lifecycle, advisor, high-command, or advisor localisation consumer is present. Generic ideas cannot be claimed as a Newfoundland package identity. |
| Politics and parties | **MISSING** | No GZX package `set_politics`, `set_party_name`, law baseline, election posture, popularity, or party localisation exists. The neutral shell remains the only starting state. |
| Package AI | **MISSING** | No GZX package AI strategy or package-specific profile exists. The generic AI profile requires the full/additive focus flag and `independence_wave_generic_ai_profile`, neither of which GZX setup assigns. |
| Localisation | **PARTIAL** | `localisation/english/006_independence_wave_countries_l_english.yml:1244-1259` covers GZX country, adjective, and ideology names. No GZX leader, party, advisor, idea, focus, decision, mission, asset, or debug-name keys exist because the gameplay consumers are absent. |
| Package admission and cleanup | **MISSING** | There is no GZX content-attestation writer, runtime setup adapter, final-validation adapter, cleanup adapter, or execution dispatch entry. The package must remain fail-closed. |

## File-surface checklist and exact findings

### Registry, planner, and reservation surfaces

- `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt:24-37` defines `independence_wave_load_package_iw_182` with package id `iw_182`, reservation group `rg_331`, region `Americas and Caribbean`, disposition `automatic_ready`, registered tag mode, and anchor `331`.
- `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt:252-260` defines `independence_wave_prepare_weight_iw_182`, but unlike the attested `IW-184` branch at `:263-275`, it does not set `independence_wave_execution_package_id` or require `has_independence_wave_runtime_package_content_attestation_for_execution_id` before weight planning. This is a stale planner asymmetry that should be repaired as part of package admission, not used to bypass attestation.
- `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt:400-407` reserves the `331` anchor and tries compact state `332`, but this is only a static reservation transaction and does not initialize a country.
- `common/scripted_effects/006_independence_wave_packages_region_14_effects.txt:526` includes `iw_182` in the region-14 selector, so selector presence must not be mistaken for package readiness.
- `common/scripted_triggers/006_independence_wave_packages_region_14_triggers.txt:18-25` checks that GZX and state `331` are available, but it has no content, identity, force, focus, AI, or asset readiness gate.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:183` requires sourced leaders and flags, institutionally grounded names, compact territory, rights/autonomy routes, and asset provenance. Those requirements are not implemented in source.

### Runtime dispatch and admission surfaces

- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-26` has no `iw_182` setup call.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:31-44` has no `iw_182` final-validation call.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:64-76` has no `iw_182` cleanup call.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-35` does not include `iw_182` in the runtime adapter trigger.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:72-89` does not include `iw_182` in the content-attestation trigger.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:94-100` therefore cannot mark GZX preflight-ready.
- `common/scripted_effects/006_independence_wave_execution_effects.txt:321-394` freezes the package, prepares the capital, dispatches setup, and commits only after final validation. Without a GZX adapter, setup remains incomplete and no durable GZX origin is committed.

### Map and state setup

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/331-Newfoundland.txt` is vanilla-owned by `ENG`, has Newfoundland's port `12505`, victory point `12505 = 2`, infrastructure `2`, one civilian industry, and a Canadian core.
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/332-Labrador.txt` is vanilla-owned by `ENG`, wasteland, has Labrador port `12503`, and a Canadian core.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:183` records `331|332`, `331=ENG|332=ENG`, `ENG=126`, and the host-remnant rule that ENG must retain at least one state after the compact set.
- No GZX state override, capital assignment, core/claim writer, port/supply adjustment, resource/building setup, or rollback/cleanup writer exists. Map admission is therefore static-only and cannot be promoted on the reservation CSV alone.

### Politics, leaders, portraits, flags, advisors, and parties

- `common/countries/006_independence_wave_GZX.txt:1-11` defines no ruling-party or leader surface.
- `history/countries/GZX - Newfoundland.txt:1-16` leaves GZX neutral and non-electoral until nonexistent runtime replacement code runs.
- Existing package precedents such as `common/scripted_effects/006_independence_wave_brittany_package_effects.txt:200-303` and `...catalonia...:140-244` show the missing contract: package-specific laws, `set_politics`, all-ideology party names, and promoted characters.
- `docs/assets/006_independence_wave/gzx_newfoundland_portrait_source_research_2026_08_03/GZX_william_r_howley_1937.jpg` and its crop JSON are valuable source evidence, but the 1937 label requires a 1936 role/date check and rights/provenance acceptance before runtime use. The folder has no manifest or runtime consumer.
- No GZX portrait exists under `gfx/leaders`, no GZX character exists under `common/characters`, and no GZX advisor or commander is defined.
- The GZX flag ladder is physically complete, but the asset manifest still marks the Newfoundland red-ensign/seal treatment `needs_user_review`. The generated redraw must not be treated as a cleared historical flag until the requested review closes.
- No GZX party, leader, advisor, or idea localisation exists beyond the country/adjective/ideology keys in `localisation/english/006_independence_wave_countries_l_english.yml:1244-1259`.

### Focus, decisions, ideas, and assets

- The accepted generic tree `independence_wave_focus_tree` is source-complete and independently audited, but `GZX` has no assignment call in `common/scripted_effects/006_independence_wave_focus_effects.txt` or a package adapter. The full framework contract must be used for a future GZX package; an additive carrier is not applicable.
- `common/ai_strategy/006_independence_wave_generic.txt:35-105` requires the generic focus assignment and `independence_wave_generic_ai_profile`; both are absent from GZX runtime setup.
- Generic Event 006 decisions and missions are available after activation, but no GZX-specific category, mission, focus-unlock, idea lifecycle, or route-localisation consumer exists.
- The generic focus tree does not substitute for country identity, package ideas, role localisation, or package AI. Those surfaces must be added to the GZX adapter or companion source files before attestation.
- The GZX flag family is present, but the GZX-specific asset manifest remains user-review gated. The Howley source crop is not a processed DDS or `.gfx` registration.

### Starting military, technology, industry, supply, and production

- Static force mapping is present at `common/script_constants/006_independence_wave_force_package_constants.txt:p182`, as recorded above. The audit corrects the common false finding that GZX lacks force mapping.
- `common/scripted_effects/006_independence_wave_force_package_effects.txt:337-372` loads the profile and pathway masks, and `common/scripted_effects/006_independence_wave_force_effects.txt:718-803,869-888` can inherit technology and slots, define the division template, create divisions, seed stockpiles, transfer approved navy/air, and mark the force applied. No GZX adapter calls the loader or the dynamic starting-force effect.
- No GZX division template, starting army, navy, air force, equipment stockpile, manpower adjustment, research slot, production line, convoy, train, fuel, or supply-capacity setup is present outside the unapplied mapping.
- The force mapping's naval and air inheritance is appropriate to the Newfoundland profile, but the runtime must still prove port, convoy, fuel, and host-ownership safety before transfer.
- No installed Technology Tree Viewer is exposed in the current package, so technology inheritance can only be checked against the static force-effect contract and vanilla documentation; this remains an unresolved validation limitation.

### AI and playability

- No GZX-specific AI strategy, focus preference, diplomacy posture, survival weighting, template behavior, or package cleanup behavior exists.
- The generic AI source can be reused after full framework assignment, but it cannot make a neutral shell playable by itself.
- A compact Newfoundland package is strategically fragile because its manpower and industrial base are small, its maritime access is essential, and its force mapping depends on port, convoy, fuel, and air/sea inheritance. These are design constraints for the package balance review, not permission to inflate the starting force.
- No allocator scenario, runtime transaction, save/load, or live playability proof was run for GZX. The current Event 006 authority admits only 14 non-overlay packages and does not admit `IW-182`.

## Event 005 and FORM-02 interaction

- `common/scripted_triggers/006_independence_wave_triggers.txt:533-578` excludes Event 005 opening Soviet-core states from Event 006 anchors and hosts. Newfoundland `331` is outside that Event 005 opening-core list, and static binding records ENG retaining a remnant after the compact set. This is a capacity witness only, not a runtime transaction proof.
- `docs/events/006_independence_wave/systems/formable_registry.md:105` defines FORM-02 as the North Atlantic Compact requiring GZX plus any two of ICE, scenario AKX, or SCO.
- `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt:29-51,162-177,264-288` requires active-member identity, exact anchors, GZX state `331` with a usable port and convoy equipment, bilateral connections, and a strict founder/member set.
- `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:237-284` contains the GZX state transfer/core integration branch, but it cannot run until the independent FORM-02 gates pass.
- `docs/plans/006_independence_wave_plans/006_iw012_formal_route_ai_closure_addendum_2026_07_28.md:415-432` explicitly keeps FORM-02 separate from IW-012 and forbids advertising formation, weakening the matrix, fallback tags/packages, or seeding post-formation values while GZX is unadmitted.

Verdict: GZX can eventually be admitted as an independent full-framework Event 006 package without FORM-02. Admission must not set FORM-02 readiness or claim formation reachability. FORM-02 requires a later separate founder-plus-two-member audit and strict runtime transaction proof.

## Validation performed

- `python -B .tools/audit_chaosx_country_tags.py --surface-scan` returned 136 protected Event 006/Soviet tags, zero external country-definition collisions, and zero external identity-surface collisions.
- `python -B .tools/audit_event6_flags.py --strict` returned 102 registered Event 006 tags, 102 complete flag families, and zero incomplete families.
- A bounded source scan found zero GZX setup, prepared, complete, cleanup, adapter, final-validation, dispatch, package-AI, character, leader, or Newfoundland-idea consumers in gameplay source.
- Static inspection confirmed `p182` force values, `RG-331` and state `331|332` bindings, generic focus assignment contract, and the Event 005/FORM-02 gates listed above.

## Skipped validation and limitations

- Hearts of Iron IV was not launched, and no live game, save/load, allocator transaction, runtime state transfer, or post-activation GZX playtest was performed.
- No map rewrite was attempted because the accepted map binding is static and runtime ownership is parent-owned; no dry-run/apply/post-validation map evidence exists for GZX.
- No Technology Tree Viewer is installed in the current package, so no read-only technology-tree artifact can be supplied.
- No portrait-rights or historical-flag review was adjudicated. The Howley crop and GZX flag manifest remain source/user-review evidence only.
- No gameplay patch is justified while the package is shell-only and the parent worktree contains broad unrelated changes.

## Promotion gates for a future full-framework package

Promotion may be reconsidered only after all of the following are evidenced for `iw_182` / `GZX`:

1. A rights-cleared, period-compatible leader or institutional identity roster with provenance, role/date acceptance, portrait processing, DDS/GFX wiring, and localisation.
2. A GZX setup adapter that sets capital/territory, cores/claims, politics, laws, parties, ideas, leaders, focus framework, generic AI profile, and package-specific state flags.
3. Invocation of the existing `p182` force mapping and dynamic starting-force effects, with port, convoy, fuel, supply, technology, industry, and host-remnant checks.
4. GZX entries in central setup, final-validation, and cleanup dispatch, plus the runtime adapter and content-attestation triggers.
5. Complete GZX party, leader, advisor, idea, focus/decision/mission, asset, and debug localisation keys.
6. Package AI and balance evidence for a compact maritime country with small manpower and industrial capacity.
7. Static and runtime checks for `RG-331`, state `331`, optional compact state `332`, Event 005 host safety, allocator capacity, rollback, cleanup, and save/load persistence.
8. A separate FORM-02 audit if the North Atlantic Compact is to be advertised or committed; GZX admission alone is not FORM-02 readiness.

No simplification or fallback is approved. Until these gates are met, `IW-182` remains a registered but unattested candidate and must stay outside the Event 006 admitted set.

Handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw182_gzx_country_package_audit_current_2026_08_03.md`.

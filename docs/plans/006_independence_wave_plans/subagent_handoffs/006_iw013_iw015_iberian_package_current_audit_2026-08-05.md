# Event 006 IW-013 / IW-015 Iberian Country Package Current Audit

## Scope/current status

This is a current-files-only country-package audit for IW-013 NAV (Basque carrier) and IW-015 GLC (Galicia carrier).

The inspected scope covers the Iberian package effects and triggers, constants, ideas, decisions, AI strategy, localisation, dispatch hooks, regional loader, force mapping, generic focus admission, current event documentation, and relevant vanilla state/history precedents.

Source wiring is present for both adapters, but central runtime content attestation and final identity/visual admission remain fail-closed.

The package is therefore **PASS source-wired / HOLD admission**.

## Country package coverage checklist

- **Tag and adapter identity — PASS:** `NAV` maps to package `iw_013`; `GLC` maps to package `iw_015` in `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt` and the region-02 loader.
- **Setup contract — PASS:** NAV requires Mediterranean-Iberia regional depth, industrial-breakaway archetype, state 792 anchor, capital 792, a living former host, and leader `Ramón Ormazábal Tife`; GLC requires standard depth, agrarian-regional archetype, state 171 anchor, capital 171, a living former host, and leader `Fuco Gómez`.
- **Lifecycle and cleanup — PASS source wiring:** package setup, founding mission, local crisis, route, host settlement, Network, sovereignty, cleanup, and shared dispatch hooks are present.
- **Politics and parties — PATCHED:** authored start-popularity constants are now applied and provisional institutional party names are initialized before route selection.
- **Leader/roster — PARTIAL:** leader-name predicates are present, but command-roster readiness only attests the country leader and does not create or verify army commanders.
- **Map/state — PASS for package anchors:** NAV uses state 792 with optional 172/806 reservation; GLC uses state 171; vanilla state ownership, cores, ports, factories, and capitals match the package contract.
- **Generic focus admission — PASS source contract:** both carriers call `independence_wave_assign_focus_framework`, receive the shared full tree and AI profile, and satisfy the generic focus contract.
- **Decisions and missions — PASS source wiring:** each carrier has a local category, founding mission, serialized project set, route project, host work, Network work, and cleanup list.
- **Ideas and ledgers — PASS source wiring:** route ideas, contested/mature lifecycle, package ledger variables, clamping, and dynamic category descriptions are present.
- **AI/playability — PASS source references:** carrier-specific survival, host restraint, settled-industry/port, and emergency-command profiles reference existing flags and decision IDs.
- **Identity/visual provenance — HOLD:** final grounded source, portrait, flag, and independent identity review evidence is not complete in the current package scope.

## File surface checklist

- `common/scripted_effects/006_independence_wave_iberian_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt`
- `common/script_constants/006_independence_wave_iberian_constants.txt`
- `common/ideas/006_independence_wave_iberian_ideas.txt`
- `common/decisions/006_independence_wave_iberian_decisions.txt`
- `common/ai_strategy/006_independence_wave_iberian.txt`
- `localisation/english/006_independence_wave_iberian_l_english.yml`
- `common/scripted_effects/006_independence_wave_packages_region_02_effects.txt`
- `common/scripted_triggers/006_independence_wave_packages_region_02_triggers.txt`
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`
- `common/scripted_effects/006_independence_wave_focus_effects.txt`
- `common/scripted_triggers/006_independence_wave_focus_triggers.txt`
- `common/scripted_effects/006_independence_wave_force_package_effects.txt`
- `common/scripted_effects/006_independence_wave_force_effects.txt`
- `docs/events/006_independence_wave/iberian_registered_packages.md`
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw013_iw015_iberian_package_current_audit_2026-08-05.md`
- Vanilla precedents inspected: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/NAV - Navarra.txt`, `GLC - Galicia.txt`, and states 792/171/172/806.

## Missing or stale surfaces

The central attestation trigger `has_independence_wave_runtime_package_content_attestation_for_execution_id` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` lists the IW-013/IW-015 adapter IDs in dispatch but still omits execution IDs 13 and 15 from the attested-content list.

The FORM-07 comment in `common/scripted_triggers/006_independence_wave_form07_triggers.txt` was corrected to describe NAV/GLC as outside central content attestation rather than absent; FORM-07 behavior remains fail-closed.

No missing package-local decision, idea, party, focus-admission, or AI identifier was found in the current source crosswalks.

## Map and state setup issues

Vanilla state 792 (`Basque Country`) is SPR-owned with NAV core, one arms factory, one civilian factory, port, and airbase, matching the NAV anchor contract.

Vanilla state 171 (`Galicia`) is SPR-owned with GLC core, one arms factory, two dockyards, port, and airbase, matching the GLC anchor contract.

The region-02 loader reserves state 792 plus optional states 172 and 806 for NAV and state 171 for GLC, and the package triggers use the same anchors.

Read-only map inspection passed the relevant state membership/network checks but returned global diagnostics for unrelated invalid building positions and floating-harbor sea positions in `map/buildings.txt`; those diagnostics are not attributable to IW-013 or IW-015.

## Politics, leader, portrait, flag, advisor, and party issues

Before this audit, `nav_start_*` and `glc_start_*` constants existed but setup did not consume them, so vanilla NAV/GLC would retain 93/3/4 popularity and no package party names.

The patch now sets a democratic provisional government and applies NAV popularity 44/29/22/5 and GLC popularity 48/25/22/5 for democratic, communist, neutrality, and fascist ideologies respectively.

The patch adds institutional baseline party names and route labels, including NAV civic assembly, workers arsenal, municipal fueros, frontier command, constitutional fueros, protected Pyrenean, and GLC civic council, workers port, municipal Atlantic, coastal security, Atlantic charter, and protected customs labels.

All 24 short/long party localisation keys resolve in `localisation/english/006_independence_wave_iberian_l_english.yml`.

The current country-leader names are grounded vanilla names and match the package predicates, but the command-roster trigger only checks `has_country_leader` for `Ramón Ormazábal Tife` or `Fuco Gómez`.

No package-local army commander creation or commander-character attestation is present, so command-roster readiness remains a design risk even though the current package-specific gate is structurally safe.

No package-specific advisor or portrait runtime reference was added; final grounded portrait/flag provenance and independent visual review remain admission blockers.

## Focus, decision, idea, and asset issues

Both carriers call the shared focus framework loader and receive `independence_wave_focus_tree` with the generic contract flags and generic AI profile.

No NAV- or GLC-specific national-focus IDs are required by the current adapter design; package-specific route and ledger effects are exposed through the local decisions and shared focus framework.

The read-only focus inspection artifact reported one tree-specific long connector and 14 global missing-icon diagnostics inherited from the shared tree, so the generic tree has not received a clean visual validation result.

The package ideas file contains the contested/mature lifecycle and five route ideas per carrier, with matching localisation and generic Event 006 icon reuse.

The local decision maps contain all current route, host, Network, sovereignty, and cleanup identifiers, and the whole-locale decision crosswalk resolved their names, descriptions, custom costs, and custom effect tooltips.

## Starting military, technology, industry, supply, and production issues

The force mapping table defines IW-013 `mountain_frontier` profile `p13=709` and IW-015 `territorial_defense` profile `p15=1047`, including militia/depots/guards/terrain or regional-defense role masks and no inherited navy/air package.

The force-package loader validates both profile rows, and dynamic starting-force effects apply mapped divisions, stockpiles, technologies, and research-slot changes.

No package-specific navy or air inheritance is expected by the current design, and no missing technology or production identifier was found in the current source surfaces.

The force mapping creates starting formations but does not create army commanders, which is the remaining command-roster limitation noted above.

## AI and playability issues

`common/ai_strategy/006_independence_wave_iberian.txt` provides separate NAV mountain-survival and GLC territorial-defense profiles, host-restraint factors, settled-industry/port priorities, and emergency-command priorities.

Decision AI weights reference the active package, setup-complete flag, route availability, host settlement, and Network conditions, with no missing decision IDs found.

The package registers the host route, regional ambition family, League route, and `iberian_federation` formable family, and the host/Network decisions require a living former host and the expected stability/network gates.

AI scenario execution and live game validation were not run because they are user-owned and outside this subagent audit.

## Patch made

Changed `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` to consume the authored start-popularity constants, set democratic provisional politics, initialize institutional party names, and provide route-specific party labels for NAV and GLC.

Changed `localisation/english/006_independence_wave_iberian_l_english.yml` with 24 matching short/long party keys.

Changed `docs/events/006_independence_wave/iberian_registered_packages.md` with the current politics-and-parties setup note.

Changed `common/scripted_triggers/006_independence_wave_form07_triggers.txt` only to remove the stale “adapters remain absent” comment; the file's behavioral anchor change from state 172 to 792 was pre-existing work by another agent and is not claimed here.

Before the patch, NAV/GLC setup did not apply the authored 44/29/22/5 and 48/25/22/5 values or party labels and would inherit vanilla 93/3/4 politics.

After the patch, each carrier starts with its authored popularity profile and institutional provisional parties, and route installers can replace the provisional label with the matching constitutional, workers, municipal, emergency, or protected-customs label.

The command-roster-ready gate was inspected but not changed in this audit because its package-specific condition is already correctly paired with the shared readiness flag and reset.

## Validation/evidence

Static crosswalks found zero missing party localisation keys across 24 references, zero missing idea localisation keys across 14 ideas, zero missing decision localisation keys, and zero missing Iberian constant references.

Static popularity validation confirmed all six authored start/route profiles sum to 100 for each carrier.

The Iberian localisation file retains its required UTF-8 BOM.

Read-only focus inspection used workspace `mod_chaos_redux_ea3b2d67c2c0` and produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a8ad30dccd393d81eadb440c38832ab3e7597439702d48b9ce84a2492baed5ca/1778836abd3090f67c4a661de6b5a65928dfe907716ca14d9188439f9c86296e/focus-inspect.a917208ce1367538.json`.

Read-only map inspection used workspace `mod_chaos_redux_ea3b2d67c2c0` and produced artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56cdd14e21f9ac1bf86f60e1c6fa898ae396f74ac2414b483735e90c08fe1f84/4e6136fbe334a509ec59ed0471d02ad55ad2f653a46fd8096bcca95f3ec18b64/map-inspect.2c1cde840ea0e249.json`.

## Admission boundary, blockers, and simplifications

Central content attestation must remain blocked for execution IDs 13 and 15 until grounded leader/flag provenance, independent country-package review, and final visual package evidence are complete.

FORM-07 identity, flag-package, and attestation gates must remain fail-closed.

No broad identity redesign, new focus route, new country package, new formable suite, or unapproved fallback was introduced.

The shared generic focus tree remains a framework admission surface rather than a NAV/GLC bespoke tree, consistent with the current adapter design.

The leader-only command-roster predicate is an unresolved package risk and should be addressed in a separately scoped roster/source pass before central attestation.

## Remaining risks

The central dispatch adapter list proves package registration but does not prove content attestation because `has_independence_wave_runtime_package_content_attestation_for_execution_id` still omits 13 and 15.

The generic focus inspection's shared icon diagnostics and one long connector remain outside this country-local patch scope.

The global map diagnostic noise in unrelated building data prevents a clean whole-map pass, although the NAV/GLC state anchors themselves are consistent.

No final grounded portrait or flag package evidence was found in the current source surfaces.

## No obsolete pasted logs

This handoff records current files, current read-only artifacts, and current static crosswalk results only.

No obsolete pasted logs or historical runtime dumps are used as evidence.

## Skills used

`chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, and `chaos-redux-comfyui` guided the audit and handoff boundary.

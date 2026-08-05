# Event 006 IW-026 Macedonia country-package audit — 2026-08-06

## Verdict

**HOLD / FAIL-CLOSED.** IW-026 has a valid vanilla registered identity and a safe compact map reservation, but it is not an executable Event 006 country package. The repository contains only the region-03 planner, loader, weight, and reservation metadata for `iw_026`; it has no MAC package setup adapter, content attestation, leader/portrait contract, force setup, package-specific AI, decision/mission layer, or cleanup adapter. No gameplay or registry promotion is warranted in this audit.

## Scope and source authority

The accepted package resolution is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:27`: `IW-026`, Macedonia, existing tag `MAC`, compact anchor `106`, reservation group `RG-106`, sourced institutional bridge, sourced real male period leader or authentic archival institution required, and reused base flag only after identity review. The candidate matrix is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:27`; its proposed `AZX` field is stale/contradictory and must not override the resolved `MAC` tag. The force design row is `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv:27`: mountain infantry and veteran networks, `mountain_frontier`, force level `65`, with engineers/reconnaissance/mountain logistics first and veteran-network command screening.

## Country-package coverage checklist

| Surface | Result | Evidence and required disposition |
| --- | --- | --- |
| Tag registration and identity | Partial/pass | Vanilla `common/country_tags/00_countries.txt:191` maps `MAC` to `countries/Macedonia.txt`; vanilla `common/countries/Macedonia.txt` defines eastern-European graphical culture and color. Chaos Redux has no MAC country-definition or history override. Preserve `MAC`; do not promote `AZX` or remap the tag. |
| Country history and politics | Partial | Vanilla `history/countries/MAC - Macedonia.txt` sets capital `106`, three research slots, Yugoslavia-clone starting technology, democratic ruling party, and 33/33/34 democratic/neutrality/communist popularity. It has no OOB, starting units, MAC leader, package ideas, diplomatic setup, or Event 006 setup. |
| State ownership/cores | Pass for reservation | Vanilla states `106-Macedonia.txt` and `970 - Western Macedonia.txt` are owned by `YUG` and core `YUG`/`MAC`. State 106 is the compact anchor; state 970 is optional Debar/Western Macedonia extension. |
| Host remnant | Pass in map evidence | MCP selected state 107 as `owner = YUG`; after compact state 106 release, YUG retains a protected state. This is map evidence only, not a package execution attestation. |
| Leader and portrait | Blocked | No MAC leader or MAC character appears in the installed vanilla character surface or Chaos Redux package files. Resolution row requires a sourced real male period leader or authentic archival institution; no fallback/generic/generated leader may be invented. Route any grounded portrait work to `chaosx_portrait_creator` after a source decision. |
| Flags | Vanilla base available, route unverified | Vanilla provides `MAC_{communism,democratic,fascism,neutrality}.tga` in full/medium/small sizes. No Chaos Redux MAC flag override exists. Reuse is allowed only after confirming the released identity and origin; no alternate route flag is attested. |
| Advisors/ideas | Vanilla-only | Vanilla `common/ideas/macedonia.txt` contains generic MAC political advisors, army/air/navy chiefs, high command, and theorists gated by `original_tag = MAC`; their portraits are generic vanilla slots. No Chaos Redux MAC ideas or lifecycle exists, and no Event 006 starting idea is applied. Do not treat these generic slots as the required sourced leader or package attestation. |
| Focus assignment | Blocked at package boundary | The shared `independence_wave_focus_tree` exists and MCP inspected/rendered it, but no MAC-specific loader or package adapter assigns/initializes it. Existing MAC vanilla content is tied to YUG release logic in vanilla `common/national_focus/yugoslavia.txt` (the release block creates two Macedonian divisions); Event 006 cannot rely on that vanilla focus path without a bounded package adapter. |
| Decisions/missions | Blocked | No MAC-specific Chaos Redux decision or mission file exists. Shared Event 006 decisions require an active, fully initialized Event 006 country; IW-026 has no setup adapter to satisfy that state. |
| Starting forces | Blocked | Vanilla MAC history has no `set_oob`, army, navy, or air setup. The design force mapping is metadata only; no `independence_wave_setup_iw_026` or MAC force spawn implementation exists. |
| Technology/industry/supply | Vanilla baseline only | Vanilla MAC has three research slots and Yugoslavia-clone technologies; state 106 has 1 industrial complex, 2 air-base levels, 2 infrastructure, 10 aluminium, 50 chromium, 1,030,650 manpower; state 970 has 1 industrial complex, 1 infrastructure, 6 aluminium, 20 chromium, 343,550 manpower. No package-specific industry, supply, production, division template, equipment, or reinforcement path exists. A workspace-wide technology scan was available, but no country-specific Technology Tree Viewer projection for MAC was available; treat any technology-package claim as unresolved. |
| AI/playability | Blocked | No MAC AI strategy file or package-specific focus/decision weights exist. Region-03 candidate allocation includes IW-026, but runtime execution still requires adapter and content-attestation gates. |
| Host relations/cleanup | Blocked | IW-026 saves the primary host during reservation only. No MAC setup/final-validation/cleanup adapter records former-host relations, created ideas, force ownership, or release cleanup. |
| Assets/manifests | Blocked | Vanilla flags exist; no MAC leader/portrait package, manifest, source evidence, or package-specific asset handoff exists. |

## File-surface findings

The only IW-026 gameplay references are:

- `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt:32-38` (`can_plan_independence_wave_package_iw_026`), which checks planner slot, living-tag availability, and state 106 availability only.
- `common/scripted_effects/006_independence_wave_packages_region_03_effects.txt:40-49` (`independence_wave_load_package_iw_026`), `:110` (weight), `:132` (reservation of 106 with optional 970), and `:143` (weighted reservation dispatch).
- `common/scripted_effects/006_independence_wave_scenario_effects.txt:173`, which ranks IW-026 for scenario selection but does not implement country setup.

`common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-47` does not list `iw_026` in the runtime adapter OR-list, and `:88-119` does not list it in the content-attestation OR-list. Consequently `is_independence_wave_runtime_package_preflight_ready` (`:125-129`) rejects IW-026. `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-30`, `:35-52`, and `:72-88` contain no IW-026 setup, final-validation, or cleanup dispatch branch.

No Chaos Redux file path contains a MAC-specific country definition, MAC history override, MAC character, MAC leader, MAC package ideas, MAC focus assignment, MAC decision/mission package, MAC AI strategy, or MAC runtime asset manifest. This absence is a hard package gap, not a reason to add generic filler.

## Map and state evidence

The installed map binding is recorded in `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:27`: anchor 106 Macedonia, optional 970 Debar, `106=YUG|970=YUG`, host remnant 107, and installed MAC cores 106/970. Reservation group `RG-106` is `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv:6`.

Vanilla state files confirm state 106 capital province 3882, provinces 907/974/3833/3865/3882/6886, rural category, 5 VP, aluminium/chromium, and YUG/MAC cores; state 970 has provinces 833/867/11856, pastoral category, 2+1 VP, aluminium/chromium, and YUG/MAC cores. MCP map inspection selected 106/970/107 and confirmed the same owners, cores, capitals, resources, buildings, and host remnant. MCP map validation passed state-region membership and networks/adjacencies but the workspace-wide map report is globally `passed = false` because unrelated `mod:map/buildings.txt` has 1,323 invalid building positions and 1,331 invalid floating-harbor adjacency diagnostics; none of those diagnostics identifies state 106 or 970. No map write was attempted.

## MCP evidence

All evidence was read-only in workspace `mod_chaos_redux_ea3b2d67c2c0`.

- Map inspection: `map-inspect.afc8e0e3a7afeb2e.json`, SHA-256 `820bccd04bb95334b169ee31cc6783f09aacfcdd3a91044eee69ec584d6b7b2d`; selected states 106/970/107.
- Map rendering: `map-state.png`, SHA-256 `9c8a38f2a0c09e2af8e7995c5a27803696c79c642b4d19a9fb7e001d8d2e9ae9` (state layer with ports, VPs, resources, buildings, supply, railways, and adjacencies).
- Event inspection: `event-scan-04e76dcf50ae.json`, SHA-256 `acbf68464c2b076aa306d93ba6dd7e0522672b81fddce95977d0d60caa9ec2c0`; focused trace `event-trace-04e76dcf50ae.json`, SHA-256 `313344dd64e9951f11d3155383d781d5b6849395c9afd7b63539cf2d116359c0`.
- Event rendering: `event-overview-04e76dcf50ae.png`, SHA-256 `f103621cf8e858b6ef33ad11a5a7245ffb411f46fd70d783c3c12945eff9ff57`; the Event Viewer reported partial workspace analysis with no blocking diagnostic in the bounded branch.
- Focus inspection/rendering: `focus-inspect.08877a307b338d93.json`, SHA-256 `962548d16a2cb5a428ad078d1551cae21169d924fb3f01e9d4fcedff10e623fd`; `independence_wave_focus_tree.focus.svg`, SHA-256 `99315e3b89510ee95475cdcaa004b6120834db4ffe96f9ca9e101b1bae25ff3e`. The shared tree has 184 focuses; MCP reported unrelated missing generic focus icons and five layout warnings, not MAC-specific defects.
- Probability inspection: custom pool source `probability-inspect-ff114c943bad.json`, SHA-256 `90dbe7b64723a4d5e294bcb62f277b08b495f228b7a1c16b5e29f3e89045b912`, reported `poolComplete = false`, `candidates = 0`, and one unresolved input for the IW-026 source; national focus AI source `probability-inspect-cea5fad03a09.json`, SHA-256 `b94fc2939fc5952d501d840cd20a0fd401bd88e49444c07d9b332876896ebd08`, reported 184 focus candidates with no source diagnostics. A separate `chaosx_ai_probability_auditor` pass was requested for the region-03 weight surface.
- Technology scan: `technology-scan-6baef9937716.json`, SHA-256 `144b288082c3cfc2d89d645edad800575b568f8a92dd959fa1ab66a89dbb7853`; this is a workspace-wide partial scan, not a MAC-specific tree proof.

## Required next steps before any admission

1. Resolve the accepted MAC leader/institution from period-sourced evidence and route the portrait package through `chaosx_portrait_creator`; do not use a generic or generated fallback.
2. Decide whether the vanilla MAC base flag is the released identity; if not, research and attest a route-specific flag before wiring it.
3. Build a bounded MAC package adapter that initializes the compact state, politics/ideas, force package, focus assignment, AI, visible ledgers, decisions/missions, former-host relations, and cleanup, while preserving YUG host-remnant safety.
4. Add package-specific final validation and content attestation, then add IW-026 to the central runtime adapter/content-attestation dispatch only after independent source, portrait, force, AI, localisation, and cleanup audits pass.
5. Reconcile the candidate matrix's stale `AZX` field with the accepted `MAC` resolution through design authority; do not silently edit the central registry in this audit.
6. Keep FORM-08 MAC admission fail-closed. Existing FORM-08 code can mention MAC 106 as a prospective anchor, but the current accepted family gate and package attestation do not admit it.

## Changes and validation

Changed file: this handoff only, `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw026_macedonia_country_package_audit_2026_08_06.md`.

No gameplay, map, registry, localisation, leader, portrait, flag, idea, decision, focus, AI, or asset file was changed. No map write, registry promotion, tag remap, or game launch was performed. Live save/in-game validation remains intentionally skipped because agents are not authorized to launch HOI4; parent/user validation is required after a future package implementation.

## Simplifications, omissions, and blockers

This audit intentionally leaves IW-026 unimplemented. The missing country package adapter, sourced leader/portrait contract, forces, AI, decisions/missions, package ideas/ledgers, and cleanup are all blocking omissions. The vanilla MAC history, flags, advisors, ideas, technologies, and YUG release precedent are evidence for future design, not an Event 006 attestation.

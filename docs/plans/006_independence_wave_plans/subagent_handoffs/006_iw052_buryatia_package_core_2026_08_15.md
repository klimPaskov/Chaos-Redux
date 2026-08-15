# IW-052 Buryatia Package-Local Audit Handoff

> Historical pre-implementation audit. Superseded for current package-local source coverage by `006_iw052_buryatia_package_core_implementation_2026_08_15.md`; its missing-source findings remain useful only as the before-state baseline.

## Scope and disposition

This is a read-only package-local audit for Event 006 IW-052 Buryatia (`BYA`).

No gameplay source, vanilla file, map file, flag, portrait, workbook, central adapter, attestation, preflight, scenario, or deterministic Join surface was changed.

The package remains unadmitted and fail-closed because the required parent-owned identity/rights receipt, leader or institutional identity evidence, symbol provenance, and weighted package evidence are not present.

The next implementation owner may use this handoff to add package-local files only after the parent publishes an explicit identity/rights gate such as `independence_wave_iw_052_identity_rights_cleared`; that flag must not be set by package-local setup.

## Required coverage checklist

| Surface | Status | Evidence or blocker |
|---|---|---|
| Tag registration | Present in vanilla only | Vanilla `00_countries.txt:222` maps `BYA` to `countries/Buryatia.txt`; no Event 006 local tag registration is needed for carrier reuse. |
| Country definition | Present in vanilla only | `common/countries/Buryatia.txt` supplies Asian graphical cultures and the vanilla blue color. |
| Country history | Present in vanilla only | `history/countries/BYA - Buryatia.txt` uses capital state 564, two research slots, vanilla technologies, mass-assault/new-fleet-in-being doctrines, and a democratic/neutrality 50/50 start. |
| Event 006 identity/origin | Missing | No package-local identity, origin, rights, or setup contract exists. |
| Map anchor and reservation | Planner binding present | State 564/Ulan Ude is the fixed anchor in `RG-564`; region-05 reservation currently reserves only state 564. |
| Host survival | Not package-proven | The current binding says SOV retains 219 other states, but no BYA package setup or cleanup proof validates the live host. |
| Leaders and roster | Vanilla roster only | `BYA_seymon_ignatyev` and `BYA_bidia_dandaron` exist, but no Event 006 identity/rights receipt authorizes their reuse. |
| Portraits | Unresolved | Vanilla portrait references exist; the Event 005 `Baikal Relay Council` portrait is an origin-specific institutional asset and is not Event 006 evidence. |
| Flags | Unresolved | Vanilla ideology flags exist, but there is no package-specific source/rights manifest proving reuse for this Event 006 origin and no route-variant package. |
| Focus framework | Shared tree present, BYA hook missing | The shared tree has no BYA callback in the five package callback sites. |
| Decisions and missions | Missing | No BYA category, decisions, timed objective, or lifecycle cleanup exists. |
| Ideas and lifecycle | Missing | No BYA Event 006 ideas or cleanup helpers exist. |
| Force package | Mapping present, caller missing | IW-052 maps to `mounted_mobile`, tradition 68, no navy/air inheritance, and five mounted/frontier reinforcement paths, but no BYA package caller applies it. |
| AI strategy | Missing | No `common/ai_strategy/006_independence_wave_buryatia.txt` exists and no BYA strategy evidence is available. |
| Localisation | Missing | No BYA Event 006 party, idea, decision, mission, focus callback, or tooltip keys exist. |
| Technology viewer | Unresolved limitation | The installed package exposes no Technology Tree Viewer; no technology-tree completion claim is made. |

## Authoritative registry and package binding

The candidate registry row is `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` for `IW-052`.

That row resolves `Buryatia`, tag `BYA`, anchor state `564`, reservation group `RG-564`, a frontier republic opening, a compact Transbaikal package, and a `cavalry, mountain and frontier units` force direction.

The research resolution row is `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv` for `IW-052`.

It requires named local councils, municipal or district administration, veterans, border forces, transport authorities, and customary institutions only where specifically sourced, and it requires a defensible sourced male period leader or authentic institutional bridge before admission.

The installed binding is `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` for `IW-052`.

It binds `BYA` to state `564` (`Buryatia`), marks the disposition `automatic_pool_ready_if_not_living`, and records `SOV=219` as the host-survival implication.

The force row is `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` for `IW-052`.

It specifies `mounted_mobile`, military-tradition score `68`, no navy or air inheritance, reconnaissance/engineer/mountain-logistics support, and reinforcement paths for militias, regional guards, depots, mounted or mountain/frontier units, and professional officers.

## Current region-05 loader and reservation boundary

`common/scripted_triggers/006_independence_wave_packages_region_05_triggers.txt:72-80` has a planner-only `can_plan_independence_wave_package_iw_052` gate that checks an open plan slot, package and `RG-564` uniqueness, BYA availability, and state-564 availability.

`common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:96-106` loads package ID `iw_052`, region `volga_urals_siberia_far_east`, regional depth, `mountain_or_frontier` archetype, `automatic_if_not_living` disposition, BYA as the candidate country, and state 564 as the anchor.

`common/scripted_effects/006_independence_wave_packages_region_05_effects.txt:195` reserves only state 564 for IW-052.

These central region-05 surfaces do not prove package content readiness, identity rights, leader/portrait rights, or admission and were intentionally not changed.

## Map and state setup findings

Vanilla `history/states/564-TS 6.txt` defines rural state 564 with 370,893 manpower, steel 10, chromium 12, tungsten 10, aluminium 4, infrastructure 2, victory points 7835 (2) and 12644 (1), owner SOV, SOV/BYA/FER cores, and the listed 18 provinces.

The state is a valid fixed compact anchor for the registry and current binding, but no package-local ownership, controller, capital, supply, rail, or host-remnant transaction exists.

The required read-only map inspection used `hoi4.map_inspect` with state selector 564 and returned `MAP_INSPECTED` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

Map inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e58f39ef6f6d6d41b40514cd71084365fcb0abb385557707d05a92875012fcf0/d8305e624f3760853d908a3b8c3910b0eb5507a5f5eba6cfedaa009d0e7dacae/map-inspect.1144978a8f1bafcd.json`.

The selected state and state/region/network checks were available, but aggregate map validation was false because unrelated global `map/buildings.txt` diagnostics reported 1,323 `MAP_BUILDING_POSITION_INVALID` and 1,331 `MAP_PORT_ADJACENT_SEA_INVALID` errors; no candidate-specific state-564 map error was exposed.

The required read-only map render used the owner layer with coastlines, victory points, resources, state buildings, province buildings, supply nodes, and railways.

Map render artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9a9b699614e18b16f89981f73bc332c1890dd0f192ef7d835376c3733745c209/463f53195eb0633042c141e2ad227d27c8c8ba453ca86c47549f93db97f92f97/map-owner.png`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32e9738d2ce0026f8de03457aaf4fe58f3646bdfcac8534877e8542569a4f6d8/7f030db2334dbbcd54593d80f24623b6428234dc93983e63676290ee4cec3872/map-owner.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ec8e5f1b00e01bed20d7aeecf0b6b65e2ba60774cc4af527b3f63cc4b6dafe8/a8784e84f49c5c936b3cb3e3abf43940e4cdc18ae91691c74d21b69f3dbee80d/map-owner.html`.

No map write was attempted, so no dry-run, apply, rollback, or post-write validation exists or is required for this tranche.

## Politics, leader, portrait, flag, advisor, and party findings

Vanilla `common/characters/BYA.txt` defines `BYA_seymon_ignatyev` (`Seymon Ignatyev`) with `GFX_portrait_Seymon_Ignatyev` and `BYA_bidia_dandaron` (`Chakravartin Bidia Dandarovitch Dandaron`) with `GFX_portrait_Chakravartin_Bidia_Dandarovitch_Dandaron`.

Vanilla `history/countries/BYA - Buryatia.txt` recruits both characters and sets democratic and neutrality popularity to 50 each with elections enabled.

There is no package-local roster gate, advisor roster, party naming, route politics, or cleanup implementation.

Event 005 creates an institutional `Baikal Relay Council` leader for BYA at `common/scripted_effects/005_soviet_collapse_effects.txt:14923-14931` and wires `GFX_portrait_BYA_baikal_relay_council` at `interface/005_soviet_collapse.gfx:1963` to `gfx/leaders/005_soviet_collapse/BYA_leader.dds`.

That institutional leader is tied to the Event 005 origin path and cannot be treated as an Event 006 sourced identity without a separate rights and origin decision.

Vanilla has `gfx/flags/BYA_communism.tga`, `BYA_democratic.tga`, `BYA_fascism.tga`, and `BYA_neutrality.tga`, but no plain `BYA.tga` was found.

No package-specific route flags, portrait manifest, or source/rights receipt exists, and no asset worker was dispatched because the task forbids inventing or substituting identity assets.

## Focus, decisions, ideas, and asset findings

The shared focus file is `common/national_focus/006_independence_wave_focus.txt` with tree ID `independence_wave_focus_tree`.

The five package callback sites currently cover the shared founding administration, state inventory, first oath, former-host policy, and network-recognition focuses for existing packages through UDM, but no `BYA` callback or exact BYA helper exists.

The required read-only focus inspection returned `FOCUS_INSPECTED` and resolved 184 focuses and 196 connectors with zero crossings and zero node intersections.

Focus inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/998c33edc3581f77b82252257be8828abcf85bafc60c4da85d9173e59dca2a31/4163b36184d531ee4db26be05e5b6fea9abf16e83f4ec86686be97d3a6d0de6e/focus-inspect.f7bd24e540b52ef2.json`.

The required read-only focus render returned `FOCUS_RENDERED`.

Focus render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b544a2d28f4c36cc2b4c2f8c2f661dd2182eb37c3d62cdc840681c51e6f2791/965745026dd675dc110747c8e0e6083e1c01a0a001c75a25dcffbd2a4cc667fb/independence_wave_focus_tree.focus.html`.

The focus route remains diagnostically partial because the viewer reports unrelated missing vanilla continuous-focus icons and existing layout warnings; no BYA-specific focus asset or layout issue was introduced.

No BYA files exist under `common/decisions/`, `common/decisions/categories/`, `common/ideas/`, `common/scripted_effects/`, or `common/scripted_triggers/`.

No package-local localisation file exists for BYA Event 006 names, parties, ideas, decisions, missions, focus callbacks, tooltips, or cleanup.

## Military, technology, industry, supply, and production findings

The vanilla BYA history supplies only the carrier baseline: infantry, recon, support, engineer, military-police, mountaineer, truck, motorized, paratrooper, and basic artillery technologies, conditional aircraft/tank/naval technologies, two research slots, and no starting order of battle.

The Event 006 force mapping is not applied because no BYA setup caller exists, so there is no package-specific army template, stockpile, manpower reinforcement, support access, production line, fuel, train, convoy, supply, or officer-state proof.

The no-navy/no-air mapping is a registry constraint, not runtime evidence.

## AI and playability findings

No `common/ai_strategy/006_independence_wave_buryatia.txt` exists, so BYA has no gated survival, host-restraint, settled-frontier, or emergency-guard behavior.

The mandatory detailed `chaosx_ai_probability_auditor` route is not callable in the installed tool list; `ALL_TOOLS` exposes the HOI4 probability tools but no callable auditor route.

As a capability baseline, direct `hoi4.probability_inspect` on the analogous BSK strategy returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero candidates, and no unresolved diagnostics.

BSK strategy baseline artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/285c7113d6c74de2c8aaf34e5facb345a0ff7e968c45af005d53653d6fb44b89/aef3cf5a2c1ca4926db95080c9f2bc2979b5e2d5be7dc24e2433e7377e284875/probability-inspect-38b83abe93f1.json`.

Direct `hoi4.probability_inspect` on the analogous BSK decision source returned no decision candidates and suggested the mission adapter with 11 available mission candidates; this is a parser capability receipt only and is not BYA evidence.

BSK decision baseline artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f59da2a2a3b60d638c34b139f52a4d3aa890cb8307194ef34927e69bf45ffb09/d9914218cfa31d8fc8e2c5c620bc4f62e92f1f31c950b81db4b69215ea925ef7/probability-inspect-b7b031d727e0.json`.

No BYA probability compare is valid because there is no owner-applied BYA source patch or pre-patch BYA source, and no typed BYA scenario contract was supplied.

## Event and collision findings

The required file-scoped Event 006 inspection used `events/006_independence_wave.txt` and returned `EVENT_INSPECTED_PARTIAL` with helper projections deferred and no blocking diagnostics in the bounded scan.

Event scan artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93ee6af288c8833ce20cb316bad7035932e7afed44baf5c725ee9eeef6cc5a77/ecaa53080f175e65141e569a36317d5a96653b93cb4fdb3fd05ed73ef4d192a0/event-scan-741883f50501.json`.

The required Event 006 render returned `EVENT_RENDERED_PARTIAL` with bounded overview artifacts and deferred workspace-wide helper analysis.

Event overview manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4d348115846234c0493bd64ab956843372d6012c240426c7bcad0284cca6ae81/9f0218d894c864ae53c62b4a8227e60eb1bb0018b82653ce0463631efc6711ac/event-overview-741883f50501-manifest.json`.

Event 005 and Event 006 share the registered BYA tag, and the collision handoff `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event5_collision_handoff.md` records that Event 005 currently has no Event 006 reservation, tag, anchor, state, origin, or focus guards.

The known geographic collision is BYA state 564 against Far Eastern packages, and the required combined scenarios include Event 005 before Event 006, Event 006 before Event 005, living Event 006 countries before Event 005 release, and host survival after combined loss footprints.

Any future BYA package trigger must reject Event 005-origin state through the package's parent-owned identity/origin contract, including the generic `soviet_collapse_breakaway` and `soviet_collapse_event_created_republic` surfaces where applicable, without mutating Event 005 in this package tranche.

## Central admission boundary

No `iw_052` entry exists in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`, or `common/scripted_effects/006_independence_wave_join_effects.txt`.

The region-05 planner and scenario ranking references are not content attestation and do not admit BYA.

Central adapter, content attestation, preflight, scenario, and deterministic Join must remain untouched and fail-closed until the parent receives a complete identity, rights, asset, setup, cleanup, weighted, and package audit packet.

## Durable implementation blockers

1. No parent-owned identity/rights clearance flag is currently published for IW-052, so roster/setup must not consume a BYA leader, portrait, or flag.
2. No sourced Buryat period leader or authentic provisional institution with rights evidence is resolved for Event 006.
3. Vanilla BYA flag and portrait assets are installed but not proven identity-compatible with the Event 006 origin; the Event 005 Baikal Relay Council portrait is origin-bound.
4. No package-local constants, triggers, effects, ideas, AI, decisions, category, localisation, focus callbacks, force caller, or cleanup source exists.
5. State 564 has a valid current-map binding, but live host survival and combined Event 005/Event 006 collision behavior are not package-proven.
6. No callable `chaosx_ai_probability_auditor` route exists, and the direct strategy adapter reports no weighted surfaces for the analogous package; no quantitative AI claim is allowed.
7. The installed package has no Technology Tree Viewer, so technology dependency coverage remains an explicit unresolved limitation.

## Safe next step for the parent

Publish the identity/rights decision and source receipts first, then add package-local BYA files behind the parent-owned flag, preserving vanilla BYA history, leaders, portraits, and flags until those receipts authorize reuse.

After exact helper definitions exist, add only five guarded shared-focus callbacks for founding administration, community rights, frontier integration, former-host settlement, and network recognition, then rerun the required focus inspect/render and package-specific probability route.

Do not widen central adapter, attestation, preflight, scenario, or Join lists from this handoff alone.

## Validation and skipped work

Completed meaningful validation: vanilla BYA tag/country/history/character/flag inspection, authoritative registry and binding review, region-05 loader/reservation review, force profile review, Event 005 collision review, bounded map inspect/render, bounded shared-focus inspect/render, bounded Event 006 inspect/render, and probability adapter capability probes.

Skipped source implementation, map writes, flag or portrait production, live HOI4 execution, technology-tree inspection, and before/after probability comparison because the parent-owned identity/rights and asset gates are unresolved and the task was narrowed to a read-only audit.

No source simplification was silently substituted for the missing identity, portrait, flag, probability, or central-admission evidence.

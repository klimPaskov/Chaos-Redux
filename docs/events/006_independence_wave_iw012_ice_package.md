# Event 006 — IW-012 Icelandic Emergency Republic

IW-012 reuses the registered vanilla `ICE` tag when Iceland is dormant and the release allocator can reserve state 100 while leaving a living former host with its protected state. The package is an additive Event 006 origin. It does not create a duplicate country, write a dormant history file, replace the vanilla Iceland flag, or call `load_focus_tree = independence_wave_focus_tree`.

## Source-of-truth and preservation

- Accepted registry row: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`, IW-012.
- Research resolution: `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv`, IW-012.
- State reservation: `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv`, RG-100, state 100.
- Runtime binding: `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`, IW-012.
- Vanilla tree and history remain authoritative: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/iceland.txt` (`iceland_tree`) and `history/countries/ICE - Iceland.txt`.
- Vanilla leaders remain authoritative: `common/characters/ICE.txt`, including `ICE_sveinn_bjornsson` and `ICE_bjorn_sveinsson_bjornsson`. The package does not add portraits or advisor icons.

## Runtime contract

The package dispatches through `common/scripted_effects/006_independence_wave_ice_package_effects.txt` and its paired trigger file. Setup proves the Event 006 origin, state 100 anchor ownership, a living former host, the vanilla `iceland_tree`, the sourced vanilla male command roster, an additive focus overlay, the North Atlantic Compact formable family, the coastal-maritime p12 force mapping, and the visible Iceland ledgers. Final validation requires the active and network registries to be aligned. Cleanup removes only generation-local Event 006 decisions, ideas, flags, and variables; vanilla ICE history, tree, characters, flag, and cosmetic identity are not removed.

## Visible mechanics

The package owns five central values: Port Authority, Civic Cohesion, Coastwatch Readiness, Shipping Security, and Compact Support. Their values are initialized centrally in `common/script_constants/006_independence_wave_ice_constants.txt`, clamped to the shared 0–100 range, displayed through the package decisions and ideas, and changed by projects, the host charter, league/network actions, route commitment, and mission failure.

The timed `Hold the Harbour Together` mission is a real survival deadline. It cancels successfully when the island stabilizes and fails when the capital loses control, the former host disappears, or the timer expires. The shared DM-01 capital mission remains available with a fragile-tier two-division guard, while the harbour crisis counts as an active founding mission so generic founding projects cannot overlap it. Six concrete-cost projects then serialize one at a time:

- `Reconcile the Shipping Registers` spends administrative labour and factory time.
- `Charter the Municipal Council` spends a larger administrative package.
- `Expand the Coastwatch` spends manpower, command power, army experience, rifles, and support equipment.
- `Negotiate the North Atlantic Compact` spends diplomatic command attention and convoy or train stock.
- `Settle the Former Host Charter` spends diplomatic materials and records a recognized-separation host outcome.
- `Declare Armed Neutrality` spends the major security package and strengthens the emergency-military route's security case; the formal government route remains a mutually exclusive focus choice.

The host project writes all eight bilateral ledger dimensions through the shared transaction helper. The Compact project changes network standing and all five league values through their shared transaction helpers. Government-route locks use an ICE-specific additive adapter: constitutional, traditional, emergency, and patron routes each set the registered government's politics and visible route idea, while patron influence remains owned by the shared Event 006 patron system; no patron or advisor asset is invented.

## Forces and AI

IW-012 uses the existing p12 `coastal_maritime` dynamic force profile, p12 military tradition, navy inheritance, and its researched reinforcement pathways. Force materialization is performed only after the vanilla roster and reservation anchors pass, so the package never runs a free-unit loop. `common/ai_strategy/006_independence_wave_ice.txt` adds coastwatch, convoy, harbour, host-charter, and compact priorities while leaving vanilla ICE AI plans in place. Host-charter and compact diplomacy are added through `independence_wave_ice_apply_host_ai` with the frozen `independence_wave_setup_former_host` target rather than a Denmark literal; cleanup reverses the same target-specific weights before the Event 006 context is discarded.

## Formable and focus integration

Setup selects FORM-02 North Atlantic Compact through the shared formable registry, including the existing ICE state-100 member adapter and NUX X-ending carrier identity. The package registers the North Atlantic ambition family and league route. The mod carries an exact vanilla `iceland_tree` snapshot at `common/national_focus/iceland.txt` with additive `shared_focus` imports, so the existing 89 vanilla focus blocks and Nordic shared focus remain intact while the complete Event 006 overlay becomes visible. Four ICE-specific route consumers hang from that shared root and lock the route through the package adapter. Vanilla Nordic League precedence is explicit: the FORM-02 member trigger refuses a country with `form_nordic_nation_flag` or the global `form_nordic_league_flag`; cleanup clears only Event 006 FORM-02 state and never vanilla Nordic identity flags.

## Route arbitration

The six visible IW-012 projects establish a founding posture through state-aware AI willingness, but they never write the formal government route. `Declare Armed Neutrality` is an emergency security commitment that raises Coastwatch and Shipping Security and gives the emergency route a material signal. The four mutually exclusive route focuses remain the sole formal route writers and re-evaluate Civic Cohesion, Port Authority, Shipping Security, Compact Support, Network Standing, former-host pressure, League membership, war, and instability before locking the route.

The route weights are centralized in `independence_wave_focus_ai`. Constitutional Republic is preferred by stable civic peace and a settled charter; Traditional Authority by mature port and shipping administration; Emergency Military by war, severe former-host threat, Coastwatch readiness, or the armed-neutrality flag; and Patron-Client by a treaty-backed Compact, League membership, or peaceful severe host pressure. Invalid routes remain hidden through their existing package gates, and no project cost, duration, reward, focus cost, or route outcome changes in this arbitration layer.

## Assets

No new IW-012 portrait, flag, or advisor icon is required. The registered vanilla ICE flag and portraits are the approved historical identity sources. This package follows the repository asset rule that sourced real portraits must be cropped and repainted in HOI4 style before DDS wiring; because ICE already supplies the approved vanilla assets, no duplicate portrait master is placed in `docs/assets/006_independence_wave/portraits_generated_png`. The flat portrait shelf remains reserved for original-size Event 006 masters only, with no nested folders and no normalized 156×210 PNGs.

## Validation and remaining admission evidence

Static validation must confirm the exact IW-012 package ID/tag wrapper, the automatic readiness witness, synchronized dispatch, additive-tree preservation, state-100 host survival, p12 force mapping, localization coverage, and the independent country-package audit. Runtime allocator/save-load, in-game decision timing, AI choice balance, and live FORM-02 congress behavior remain separate completion evidence and are not replaced by this document.

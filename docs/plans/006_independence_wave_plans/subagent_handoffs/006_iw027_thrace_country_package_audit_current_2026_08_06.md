# IW-027 Thrace package audit handoff

Date: 2026-08-06

Status: source-attested and admitted to the current Event 006 closure.

## Locked identity and reservation

- Package: IW-027 Thrace.
- Runtime carrier: `BAX`, a registered Event 006 `X`-ending carrier shell.
- Installed anchor: state `184`, Thrace.
- Former host: `GRE`, with the host retaining its protected remnant.
- Reservation group: `RG-184` / `rg_184`.
- Region: Balkans and Danube.
- Package depth: standard.
- Archetype: river or corridor.
- Force profile: mounted mobile, with package mapping `p27`.
- Formable family: Balkan Federation.

## Package surfaces reviewed

The package-specific effects, triggers, decisions, ideas, constants, AI strategy, character consumer, localisation, portrait GFX, central dispatcher, region-03 loader, synchronous roster checkpoint, and shared-tree hooks were reviewed together.

- `common/scripted_effects/006_independence_wave_thrace_package_effects.txt` owns setup, two visible ledgers, lifecycle ideas, five government routes, host settlement, league/network action, paid projects, force mapping, final validation, and generation-safe cleanup.
- `common/scripted_triggers/006_independence_wave_thrace_package_triggers.txt` proves exact tag, anchor, host, roster, ledgers, focus framework, route, formable, force, AI, and cleanup readiness.
- `common/decisions/006_independence_wave_thrace_decisions.txt` exposes one founding mission and eleven concrete administration, security, diplomatic, strategic, route, host, and network projects with time and resource costs. No political-power store or free-unit loop is used.
- `common/ideas/006_independence_wave_thrace_ideas.txt` defines two lifecycle ideas and five mutually exclusive route ideas.
- `common/script_constants/006_independence_wave_thrace_constants.txt` centralizes politics, ledger thresholds, project duration, and AI tuning. The AI strategy file uses only its file-scoped compatibility constants where the engine rejects shared constant tokens.
- `common/ai_strategy/006_independence_wave_thrace.txt` provides survival, former-host restraint, settled compact, and emergency commission layers.
- `common/characters/006_independence_wave_thrace_characters.txt` uses one sourced male Hristo Silyanov consumer for the civilian, country-leader, and corps-commander roles. No advisor, high-command, dossier, or small-portrait surface is defined.
- `localisation/english/006_independence_wave_thrace_l_english.yml` is UTF-8 with BOM and contains the package's party, idea, mission, decision, tooltip, and sourced leader text.
- `interface/006_independence_wave_iw027_thrace_portraits.gfx` wires the runtime portrait DDS.
- `gfx/leaders/006_independence_wave/portrait_BAX_independence_wave_hristo_silyanov.dds` is the 156x210 source-placeholder runtime consumer. The original, explicit head-and-shoulders crop, resized PNGs, provenance, and handoff remain in `docs/assets/portraits/006_independence_wave/iw027_thrace_hristo_silyanov_source_placeholder_2026_08_06/`.
- The flat ImageGen source, processed ladder, final TGAs, prompt, and manifest for BAX are retained in `docs/assets/006_independence_wave/event006_missing_flags_2026_08_02/` and the runtime flag ladder under `gfx/flags/`.
- `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`, `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, `common/scripted_triggers/006_independence_wave_packages_region_03_triggers.txt`, `events/006_independence_wave.txt`, and `common/national_focus/006_independence_wave_focus.txt` carry the central setup, final-validation, cleanup, exact planner, roster, and generic-focus hooks.

## Source checks

- `python -B .tools/audit_event6_allocator.py`: PASS. The current closure is 25 attested selectable packages across 23 compatible reservation groups, with 126 automatic/high-chaos candidates, a 20-package static witness, and the 6/8/10/14/20 ladder.
- `python -B .tools/audit_event6_flags.py`: PASS. All 102 registered Event 006 tag families have complete flag ladders.
- `python -B .tools/audit_event6_scenario_matrix.py`: PASS. All SCN-008 mode/intensity cells and eight edge-case receipts remain present.
- `python -B .tools/audit_event6_country_api.py`: PASS. Broad and resolved carrier inventories have no missing or duplicate API entries.
- `python -B .tools/audit_chaosx_country_tags.py --surface-scan`: PASS. The protected Event 006/Soviet tag audit reports zero external country-definition or identity-surface collisions.
- A package-local read-only helper and localisation-key scan found no undefined `independence_wave_bax_*` helpers or package-local keys.

## MCP evidence and limitations

- Event lint for `chaosx.nr6.350` completed with status `EVENT_INSPECTED_PARTIAL`, revision `14d8422b3bdd0298de54a049ad4bb2200d723de12efc3f8eb4e802a046e4cb3b`, and linked artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bfb3f4097dd07efa81ec6467a288471e149b049e6335e24c4440f2a08af81bf1/734027b18b5785499542b0bce06fa3be0c7a5754ed4999e33a25ebcc3e976dfb/event-lint-14d8422b3bdd.json`. The large-workspace helper projection was deferred, so this is partial evidence rather than a whole-workspace pass.
- Shared focus inspection completed with status `FOCUS_INSPECTED`, revision `63b96335e304b11ad03fa544611507048f48f27b73e7292db093dbc4fcc87a3e`, 184 focuses, and 193 connectors. It reported the known authored-layout spacing warnings, one intentional long connector, and no Event 006 crossing or node-intersection result. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1de38aebcdabc8742d7a8c03c6d45ec0831969ab94be4d2342280b648a354bbc/22e7219801d66f201741b281aa1507175407c297cee7492e1026306c79d4c2d0/focus-inspect.63b96335e304b11a.json`.
- Map inspection for state 184 completed with status `MAP_INSPECTED` and confirmed the state was addressable. The workspace-wide map validator also surfaced unrelated installed `buildings.txt` locator diagnostics, so no global map-clean claim is made. The latest linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5a49dc04550b56e772f171862e893efb148ba4476c9e37eaa9279307f4be98a/12ba893fe705f4eb6455ab29908bee450e7f5a2be04b63ae326a9e7e9a87414f/map-inspect.fcbea3f4ca2e25c0.json`.
- The installed decision probability adapter now returns `PROBABILITY_SOURCE_INSPECTED` for the BAX decision source, with 11 discovered adapters, one candidate, ten required inputs, `poolComplete=false`, and zero unresolved source diagnostics. The linked artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a0f52deb43df220daed6166a7d68ee35dd56d86fb13a2cdce0a37a1373d02bbc/6997ddf5e1b709e2685e9eba3cbe436dd17326c73a4e2d336ac4648c2b372e08/probability-inspect-e06347f593b9.json`. The AI-strategy adapter returns `PROBABILITY_SURFACE_EMPTY`; no quantitative BAX probability or AI-balance claim is made because the typed pool is incomplete and the strategy surface is unavailable.
- A context-free `chaosx_country_package_auditor` retry could not start because the required `blender_hoi4` and `meshy` MCP servers timed out during bootstrap. Parent-side review and static checks above are the available evidence.
- A context-free `chaosx_localisation_auditor` retry encountered the same `blender_hoi4` and `meshy` bootstrap timeout. The parent-side package-local key scan and UTF-8-with-BOM check above are the available localisation evidence.

## Remaining risks

This admission does not claim live game, save/load, player-owned transaction, or final styled-portrait validation. The Hristo Silyanov image is an accepted historical source placeholder under the current policy and preserves the archival identity without a repaint. Ordinary super-event `23`, the unadmitted formable families, package-specific typed probability comparisons, and the large set of still-unattested registry rows remain whole-event blockers outside IW-027.

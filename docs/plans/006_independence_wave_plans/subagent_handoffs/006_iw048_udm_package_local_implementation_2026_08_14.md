# IW-048 Udmurtia package-local implementation handoff

Date: 2026-08-14

Companion audit: `006_iw048_udm_package_audit_2026_08_14.md`.

## Disposition

IW-048 UDM is package-local and unadmitted. The tranche adds source-complete local constants, ideas, AI strategy, scripted triggers, scripted effects, a decisions category, one founding mission, ten paid projects, player-facing localisation, and five shared-focus helper calls. It does not widen central adapter, attestation, preflight, scenario, Join, map, flag, portrait, country-history, character, or `.gfx` surfaces.

## Files changed

- `common/script_constants/006_independence_wave_udm_constants.txt`
- `common/ideas/006_independence_wave_udm_ideas.txt`
- `common/ai_strategy/006_independence_wave_udm.txt`
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_udm_package_effects.txt`
- `common/decisions/006_independence_wave_udm_decisions.txt`
- `localisation/english/006_independence_wave_udm_l_english.yml`
- `common/national_focus/006_independence_wave_focus.txt`
- `docs/events/006_independence_wave/udmurtia_package.md`

## Vanilla reuse and map contract

The package keeps vanilla `UDM`, vanilla capital/state 399 Izhevsk, vanilla history and politics baseline, vanilla `UDM_boris` / Boris Berman, vanilla leader portrait token, and the installed UDM normal/medium/small ideology ladders. No new portrait or flag files were created, and no 156x210 portrait processing was performed.

The source uses the registry's p48 `industrial_security` force profile. The shared package-archetype constants expose `industrial_breakaway` but not `industrial_security`, so the package-local initialization gate uses `industrial_breakaway` as the source-mapped archetype while retaining `industrial_security` for force mapping. This is an explicit admission-review item, not a central registry rewrite.

## Mechanics and identifiers

The package exposes `is_independence_wave_udm_package`, `is_independence_wave_udm_project_ready`, state-399 runtime checks, UDM former-host and cost gates, generation-safe active-project checks, roster checkpoint `UDM_boris`, compact ledgers `independence_wave_udm_workshop_control` and `independence_wave_udm_forest_rail_readiness`, and setup/final-validation/cleanup wrappers for `iw_048`.

The founding mission is `independence_wave_udm_hold_workshop_congress`. The ten project IDs are `independence_wave_udm_secure_workshop_depots`, `independence_wave_udm_integrate_industrial_guards`, `independence_wave_udm_register_udmurt_communities`, `independence_wave_udm_settle_former_host_ledgers`, `independence_wave_udm_ratify_constitutional_autonomy`, `independence_wave_udm_adopt_forest_land_compact`, `independence_wave_udm_convene_worker_councils`, `independence_wave_udm_establish_industrial_emergency_command`, `independence_wave_udm_codify_durable_sovereignty`, and `independence_wave_udm_open_volga_ural_corridor`.

The shared focus file now contains UDM-only guarded calls for `independence_wave_udm_focus_convene_workshop_council`, `independence_wave_udm_focus_secure_rail_communities`, `independence_wave_udm_focus_integrate_industrial_guards`, `independence_wave_udm_focus_settle_former_host_ledgers`, and `independence_wave_udm_focus_open_volga_ural_corridor`.

## Targeted evidence

The current UDM mission probability inspect returned `PROBABILITY_SOURCE_INSPECTED` for `mission_ai_will_do`, source revision `fe351fc9e258351b956fc3d6d15c806a13735fa9863686cea50aa644dd762024`, source hash `cae802712e775a81971ae7ae90970e7328b31674dcce862bdce65b3bf8da2f98`, eleven candidates, zero available candidates, fifteen required inputs, and an incomplete pool. The corresponding artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82218d803ca3527bf189eafe49da5b27b1f14aa9bda094b0811c4ccb90ac3f2f/dfe53edb2105d5482c38df0a7d3e6b72e44bc6093283c4c328b7045b75ec0cca/probability-inspect-cae802712e77.json`. No quantitative score, ranking, timing, or balance claim is made.

The required UDM AI strategy inspect returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, and zero required inputs. The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/849134039cf1cf8e6a90bb3e760caacefa33718a40bcddf861c1426cb99c6a10/6522e87f1139350d2425912809f779c30607937aa60c486edadaedd3ed8c3dca/probability-inspect-f02db2218ca2.json`. No quantitative AI claim is made.

The explicit map inspect for state 399 returned `MAP_STATE_ID_COLLISION` when an allocation request was supplied, then `MAP_INSPECTED` when the existing installed state was selected directly. The successful artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dea0061bd5218ade4bb192313c92537ca6eefec7f659839ad94280f55df7b0df/00008f648fde2164ce2506b9ea908bea03bba23e2a97fe9cfd492cfc26e3365e/map-inspect.68ac9f655377f72c.json`. State, region, and network checks passed; global validation remains false because of unrelated workspace building/port diagnostics and truncated inventory.

The focused Event 006 inspect for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with no selected blocking diagnostics, revision `741883f50501db1f866db675ee6ad6cb4009a90ad539eb84b08ce5e82602f65b`, and current artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e939b1731bcebf13cfba3fab36d4f1a314a7b6a073516a3b47e9ddc27aed75ed/80e75713f9d4fc5d2731e275b84e712dc5fa413557f275ae841723f54893fa3a/event-scan-741883f50501.json`. The helper/lifecycle projection is workspace-deferred, so this is not a full event-completion claim.

The focused shared focus inspect returned 184 focuses, 196 connectors, zero crossings, zero node intersections, and two long connectors with the existing aggregate diagnostics. The UDM calls did not add nodes or alter the layout hash. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/abbb904dad2be952015abcda2125e1ca7b620afbb10d738003e7f64378c5f1d1/d580596e7982f9614a477108879b5fbc7afef446ce937c9b7485c616de2f8665/focus-inspect.bed2a32d209541d2.json`. Render artifacts were produced for HTML, SVG, and JSON; no new focus node or icon was introduced.

## Static checks and remaining gates

The package-local script files have balanced braces, exact decision-to-trigger project parity, and complete owned localisation for the UDM category, mission, ten project names/descriptions, custom effect tooltips, seven ideas, and four route party names. Factory-bearing administration and strategic projects use UDM-specific cost selectors whose base, blocked, and tooltip triplets disclose the package's one-factory modifier. The baseline-law effect uses `add_ideas` for `civilian_economy`, `export_focus`, and `volunteer_only`, matching the established Event 006 package precedent. The cultural route installs both `udm_cultural_register` and `udm_cultural_land_compact`, and cleanup removes both.

Central authority remains 40 adapters, 32 content attestations, 29 compatible groups, and 161 unattested selectable rows. IW-048 is absent from central attestation, adapter dispatch, normal/scenario preflight, and deterministic Join by design. Admission remains blocked on a complete identity/asset/provenance packet, state-399 host/anchor acceptance, central wiring review, typed probability fixtures, and a fresh package audit.

No generated assets, copied portrait replacements, runtime flag overrides, map edits, central dispatcher edits, attestation edits, Join edits, spreadsheet edits, or live-game claims were made in this tranche.

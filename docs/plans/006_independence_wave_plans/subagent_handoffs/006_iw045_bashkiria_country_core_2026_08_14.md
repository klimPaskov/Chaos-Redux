# IW-045 Bashkiria country-core implementation handoff — 2026-08-14

> Superseded for current package-local status by the IW-045 localisation, flag, portrait-runtime, and package-admission receipts dated 2026-08-14. This handoff remains authoritative for the core scripted identifiers and deliberately fail-closed central admission boundary.

## Disposition

The bounded IW-045 country-core sources are landed, but the package remains fail-closed and is not centrally admitted.

The implementation preserves vanilla BSK history, state 651/Ufa, installed BSK flags, and the exact vanilla `BSK_yakov_bykin` character contract; it does not create a new leader, portrait, flag, focus tree, or Join path.

Central adapter, content attestation, scenario preflight, and deterministic Join surfaces were intentionally not widened because the required current asset provenance, package admission, and complete MCP evidence are not present.

## Package contract

| Surface | Contract |
|---|---|
| Package | `iw_045` |
| Carrier | `BSK` / Bashkiria |
| Anchor | State `651` / Ufa |
| Reservation | `RG-651` |
| Region | `volga_urals_siberia_far_east` |
| Depth | `regional` |
| Archetype | Existing `mountain_or_frontier` package archetype |
| Force profile | Existing `mounted_mobile` profile |
| Force tradition | Existing p45 mapping (`independence_wave_force_package_military_tradition.p45 = 70`) |
| Ledgers | `independence_wave_bsk_congress_cohesion`, `independence_wave_bsk_frontier_readiness` |
| Setup flag | `independence_wave_iw_045_setup_complete` |
| Crisis flags | `independence_wave_bsk_compact_crisis_resolved`, `independence_wave_bsk_compact_crisis_failed` |
| Origin guard | Rejects `soviet_collapse_active_origin` and `liberation_origin.soviet_collapse` |
| Formables | No FORM-12/13 release behavior; shared membership-only systems remain outside this package |

The registry/force distinction is deliberate: the package archetype remains the existing `mountain_or_frontier` value while the dynamic starting force uses `mounted_mobile` and p45.

## Files changed

- `common/script_constants/006_independence_wave_bashkiria_constants.txt` adds package-local politics, ledger, crisis-duration, cost, and AI tuning constants.
- `common/scripted_triggers/006_independence_wave_bashkiria_package_triggers.txt` adds exact BSK/state-651 identity, origin, former-host, roster, ledger, project, setup, force, runtime, and completion proofs.
- `common/scripted_effects/006_independence_wave_bashkiria_package_effects.txt` adds package idea lifecycle, ledger changes, route government effects, focus hooks, setup/final-validation/cleanup dispatch, and decision aliases.
- `common/ideas/006_independence_wave_bashkiria_ideas.txt` adds crisis, mature compact, constitutional, socialist/oilfield, agrarian, and frontier-emergency ideas. Each idea is BSK-only, civil-war compatible, and reuses the installed Independence Wave idea-picture tokens rather than introducing an unproven asset token.
- `common/ai_strategy/006_independence_wave_bashkiria.txt` adds frontier-survival, host-restraint, settled-frontier, and emergency-guard strategy layers.

The parent-owned `events/006_independence_wave.txt` source now contains the narrow BSK roster-checkpoint branch. This subagent does not claim any broader central adapter, attestation, or Join change.

## Helper identifiers

The five shared-focus hooks now resolve to these package effects:

- `independence_wave_bsk_focus_convene_frontier_congress`
- `independence_wave_bsk_focus_secure_oilfield_communities`
- `independence_wave_bsk_focus_integrate_frontier_guards`
- `independence_wave_bsk_focus_settle_former_host_ledgers`
- `independence_wave_bsk_focus_open_volga_ural_corridor`

Decision-facing aliases include `independence_wave_bsk_focus_secure_frontier_depots`, `independence_wave_bsk_focus_integrate_border_guards`, `independence_wave_bsk_focus_register_bashkir_communities`, and `independence_wave_bsk_focus_open_ural_network_corridor` so the decision owner can keep project names separate from shared focus names.

The decision owner has canonicalized project IDs, setup flag, category path, and shared duration constants against this core contract in `common/decisions/006_independence_wave_bashkiria_decisions.txt`. Its availability/activation surfaces consume `is_independence_wave_bsk_project_ready`, which includes the current force-package generation guard.

## Vanilla roster and identity evidence

Installed vanilla `common/characters/BSK.txt` defines `BSK_yakov_bykin` as the male country leader Yakov Borisovich Bykin with `GFX_portrait_Yakov_Borisovich_Bykin`.

Installed vanilla `history/countries/BSK - Bashkortostan.txt` recruits `BSK_yakov_bykin`, uses capital 651, and retains the baseline technology and political setup.

No mod character file or portrait asset was created, and no Event 005 council portrait is reused as an Event 006 final.

## MCP evidence

- `hoi4.map_inspect` for state 651 succeeded with `MAP_INSPECTED` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f4bc77fcb8207340b057276583cfbccce65e57cb9af74e066b24add2d612c19/e9e6beb01cba97cb8cf9b678eb5290ed98232bc0f3104fdca688d7205286dd5e/map-inspect.91c9debcb4c57109.json`.
- The map inspection confirms state, region, adjacency, supply-node, and railway checks, but global map validation remains false because unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics dominate the workspace.
- `hoi4.map_render` state-layer output passed and produced `map-state.png`, `map-state.json`, and `map-state.html` artifacts under the same workspace.
- `hoi4.focus_inspect` on `common/national_focus/006_independence_wave_focus.txt` returned 184 focuses and 206 connectors with current shared diagnostics, including 14 blocking diagnostics; post-core artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3a7c60ef9a95ed37287260b3afb8e9db45adad9d02fa3d3b49c00abf3eddacdf/401409ba1bbf58f5faaa5a169885ad352cfbae5ab8cb01758d00d640c6cbf772/focus-inspect.8ddba04dcb6226a4.json`.
- Focus gameplay references for the five BSK hooks resolve after these files landed; shared layout/icon diagnostics remain unrelated to this bounded package.
- `hoi4.event_inspect` for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics; the post-roster-checkpoint artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a95732500c3efc403a2e157c7f7d8e8a6cccd78f65791b427d669368c39db47/e3b96967a410c1d40756ecaf912bfc22dca19fef3440eb3d186b29ca8cae9225/event-state_flow-10b71c98d51a.json`.
- `hoi4.probability_inspect` source discovery for `common/ai_strategy/006_independence_wave_bashkiria.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`, zero candidates, and zero unresolved inputs; artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/338ab0b10430e632175c4f18abb894b2e73b63ee6ab1bfda1c0a4b2c346b65e0/967cfa1aeeea2a8ab6a517d47cfb134ed3fad0f31be95c5e0738701c22ed04c8/probability-inspect-38b83abe93f1.json`.
- A mandatory `chaosx_ai_probability_auditor` pass completed in `006_iw045_bashkiria_probability_audit_2026_08_14.md`: the strategy-factor adapter returned `no_weighted_surfaces`; the named evaluation returned `PROBABILITY_SURFACE_EMPTY`. No quantitative AI balance claim is made here.
- The installed package exposes no Technology Tree Viewer, so technology/runtime dependency proof remains unresolved as required by the parent tranche.

## Static checks

The five package-local source files have balanced Clausewitz braces, no unsupported `<=` or `>=` operators, all five shared focus hook identifiers resolve to package effect definitions, and all BSK decision effect calls resolve to the package effect file. Idea-picture tokens were cross-checked against existing Independence Wave idea definitions.

The package decision references were cross-checked against the package trigger/effect definitions after the decision owner completed project-name, setup-gate, category, and duration canonicalization.

## Remaining blockers and omissions

- The narrow central BSK roster checkpoint is present in the parent-owned event source; broader central adapter, attestation, preflight, and Join wiring remains intentionally absent.
- Central adapter/content-attestation/normal-preflight/scenario-preflight/Join admission remains deliberately absent and fail-closed.
- BSK-specific localization, decisions, focus source, spreadsheet, flags, portraits, and asset manifests are owned by sibling workers or the parent and are not claimed here.
- Current map global validation is false for unrelated workspace building/port diagnostics even though state 651 selected map checks passed.
- Shared focus inspection still has 14 blocking layout/icon diagnostics; this package does not claim to fix them.
- Probability evidence has no weighted AI strategy surface and therefore cannot support ranking, timing, dominance, or survival claims.
- Existing BSK localization still contains the earlier oilfield/communities/emergency project-name variants alongside the canonical decision IDs; the localization owner must retain or add canonical keys before player-facing completion.
- No live HOI4 session, save/load test, technology-tree viewer proof, or final Join/runtime claim is made.

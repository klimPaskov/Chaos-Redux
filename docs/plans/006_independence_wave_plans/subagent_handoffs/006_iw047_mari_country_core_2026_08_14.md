# IW-047 Mari El country-core handoff (2026-08-14)

## Scope and outcome

This tranche adds the package-local Mari El (MEL) Event 006 core surfaces. It does not modify the central package dispatcher, content attestation, deterministic Join, Event 005 Soviet Collapse, decisions owned by the decisions worker, focus files owned by the focus worker, localization, spreadsheets, map data, or assets.

The package remains bounded to the vanilla MEL country and state 833. It models a Volga-Finnic forest compact with separate congress cohesion and forest readiness ledgers, local community registration, woodland guard integration, former-host ledger settlement, and a Volga-Finnic corridor reward.

## Gameplay files

Changed or added package-local files:

- `common/script_constants/006_independence_wave_mari_constants.txt` — IW-047 pressure, duration, cost, and route-politics constants.
- `common/scripted_triggers/006_independence_wave_mari_package_triggers.txt` — MEL/state-833 identity, Soviet-origin exclusion, generation-safe project gates, former-host proof, exact roster proof, force/archetype checks, and prepared/complete setup gates.
- `common/scripted_effects/006_independence_wave_mari_package_effects.txt` — compact lifecycle, progress/failure, former-host and network rewards, four government routes, five focus hooks, vanilla roster checkpoint, setup/final-validation dispatch, and cleanup.
- `common/ideas/006_independence_wave_mari_ideas.txt` — fragmented mandate, forest compact, congress charter, woodland councils, community register, forest-land compact, and emergency command spirits.
- `common/ai_strategy/006_independence_wave_mari.txt` — survival, host-restraint, settled-compact, and emergency-guard strategy layers.

The expected decision helper contract is present in the effects file:

- `independence_wave_mel_begin_project`
- `independence_wave_mel_apply_project_failure`
- `independence_wave_mel_focus_secure_forest_depots`
- `independence_wave_mel_focus_integrate_woodland_guards`
- `independence_wave_mel_focus_register_mari_communities`
- `independence_wave_mel_focus_settle_former_host_ledgers`
- `independence_wave_install_mel_constitutional_government`
- `independence_wave_install_mel_forest_land_government`
- `independence_wave_install_mel_woodland_council_government`
- `independence_wave_install_mel_forest_emergency_government`
- `independence_wave_mel_apply_administrative_progress`
- `independence_wave_mel_apply_diplomatic_progress`
- `independence_wave_mel_apply_security_progress`
- `independence_wave_mel_apply_major_settlement`
- `independence_wave_mel_focus_open_ural_network_corridor`

The five shared-focus helper IDs are also present:

- `independence_wave_mel_focus_convene_forest_congress`
- `independence_wave_mel_focus_secure_mari_communities`
- `independence_wave_mel_focus_integrate_woodland_guards`
- `independence_wave_mel_focus_settle_former_host_ledgers`
- `independence_wave_mel_focus_open_volga_finnic_corridor`

## Identity and setup contract

- Original tag: `MEL`.
- Package id: `constant:independence_wave_package_id.iw_047`.
- Anchor state: `833` only; capital and ownership checks remain state-specific.
- Registry archetype: `constant:independence_wave_package_archetype.river_or_corridor`.
- Force profile: `constant:independence_wave_force_profile.river_jungle`.
- Military tradition: `constant:independence_wave_force_package_military_tradition.p47`.
- Setup gate: `independence_wave_iw_047_setup_complete`.
- Package flag: `is_independence_wave_mari_package` with alias `is_independence_wave_mel_package`.
- Ledgers: `independence_wave_mel_congress_cohesion` and `independence_wave_mel_forest_readiness`.
- Crisis flags: `independence_wave_mel_compact_crisis_resolved` and `independence_wave_mel_compact_crisis_failed`.

The package rejects Soviet Collapse origin flags and the Soviet Collapse origin variable, requires `liberation_origin.independence_wave`, and does not extend the MEL anchor beyond state 833. Former-host settlement only operates when the protected host remains a separate, valid country and is not at war with MEL. FORM-12/13 membership remains central and membership-only.

## Vanilla roster checkpoint

Vanilla references were checked before implementation. The installed vanilla files provide `MEL_zinovy_zhadinov` (Zinovy Zhadinov) with `GFX_portrait_Zinovy_Zhadinov`, MEL country history capital 833, and the vanilla MEL ideology flag ladder. The setup effect only records `independence_wave_mel_roster_checkpoint` and `independence_wave_command_roster_ready` when `has_character = MEL_zinovy_zhadinov` is true. It does not generate a character, set a portrait, replace vanilla history, or create a new identity.

## Validation evidence

- Static source scan found balanced braces in `common/scripted_effects/006_independence_wave_mari_package_effects.txt` (207 opening and 207 closing braces), tab indentation, and no unsupported `<=`/`>=`, Event 005 origin mutation, character generation, or portrait override in the package effects.
- Expected decision helper IDs and all five focus helper IDs were enumerated from the effects source and found.
- A read-only map inspection covered state 833 and the relevant Volga/forest region bindings. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f6c6cb9a4447b3d700a395df0d3e2180e3ddcc0e8845feeb9392beddd41cc07/9967b09f997086d46cae029a991a3e6c9bf49bff746e1a5e0b7d68030e51b723/map-inspect.cb427d91802129c8.json`. The adapter reported global building-position and port-adjacency diagnostics; no unknown selected-state IDs were reported.
- After the effects landed, the shared focus worker reran the mandatory `hoi4.focus_inspect` and `hoi4.focus_render` passes. The MEL guarded hooks resolved with no MEL-specific unresolved helper reference. The authoritative inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1620929ffe9f2fb6f3c7f86f0ef7db2f61e580c7d832c20b02f4120e10ef0f59/6b07099d4bb2dd44f996c0bfebb904c2e996af7e8b7b2519c709e5314e68665a/focus-inspect.653a3a130d61c0732e89233cc5b3964d7b1fce657e032eaadb754538565d05bb.json`. The full tree still reports pre-existing global missing-icon and layout diagnostics; the unchanged tree is not claimed clean.
- A read-only Event 006 scan was attempted for `events/006_independence_wave.txt` and `chaosx.nr6.350`. The adapter returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics but deferred workspace-wide helper projections/lifecycle passes. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d3782d041b6f4e56c3293f32ddb92f9153ba4cc7d54be00c97c3884ed7b3e607/1392908de39538b218e645dedef4fbfff948efdcec354b157cdc8680b56d05fc/event-scan-d21fdfa2723e.json`.
- The mandatory AI probability pass was run by `chaosx_ai_probability_auditor`. Handoff: `006_iw047_mari_probability_audit_2026_08_14.md`. `ai_strategy_factor` discovery returned `PROBABILITY_SOURCE_DISCOVERED` with `no_weighted_surfaces`; the named MEL evaluation returned `PROBABILITY_SURFACE_EMPTY`. No quantitative AI ranking or balance claim is made. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/754a7015fd11f12a7851f1b1cc7a1e2ba303d572bfe8b7a9a7bd26fb022cbed9/75dde7347fb8406d33922284d1f5f88094d3c535ab60e187bb071da88d844566/probability-inspect-1ebebf8cc5f53ba2f3fa1e8a615f5c6413557179b9baafe4f8b7ec63fb5392bd.json`.

## Supersession note (post-handoff allocator correction)

After this handoff was written, the parent corrected `common/scripted_effects/006_independence_wave_packages_region_05_effects.txt` in `independence_wave_load_package_iw_047` so its allocator archetype is `constant:independence_wave_package_archetype.river_or_corridor` (current source line 57). The earlier blocker below is retained as historical handoff context and is superseded for the current IW-047 archetype state. This correction resolves the allocator/package archetype mismatch only; the research anchor 256 versus implemented state 833, asset and identity holds, central attestation, normal/scenario preflight, and deterministic Join remain open.

## Remaining blockers and parent actions

1. **Superseded for current archetype state:** At handoff time, the region-05 allocator scaffold contained the older IW-047 `mountain_or_frontier` assignment. The parent correction recorded above now aligns the allocator with the package-local `river_or_corridor`/`river_jungle` contract. Anchor, asset, identity, central preflight, attestation, and Join evidence remain required before admission can be considered complete.
2. Focus hooks and decisions are separate ownership surfaces. Rerun the read-only focus inspect/render and decision undefined-reference audit after this effects file is visible; no central attestation or Join change is implied by this handoff.
3. MEL cosmetic-tag and player-facing decision/focus localization remain downstream work. No fallback portrait, flag, or leader was introduced.
4. The installed package exposes no Technology Tree Viewer; no technology claim was made.

No commit or staging was performed by this subagent; a shared `.git/index.lock` was present during the probability worker's commit attempt and was not removed.

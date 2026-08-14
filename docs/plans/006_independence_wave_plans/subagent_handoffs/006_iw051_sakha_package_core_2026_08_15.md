# IW-051 Sakha/YAK Package-Local Core Handoff

## Disposition

The package-local IW-051 core is implemented for the registered `YAK` carrier with state `574`/Yakutsk as the required anchor and optional extension states `644`, `876`, and `877` left to the existing central reservation flow.

The tranche is intentionally fail-closed: central adapter, attestation, preflight, scenario, deterministic Join, Event 006 admission, Event 005 origins, state history, vanilla YAK files, flags, portraits, and other assets were not changed.

Setup and roster use the source-backed vanilla characters `YAK_pavel_pevznyak` and `YAK_anatoly_pepelyayev`, but require the parent-owned `independence_wave_iw_051_identity_rights_cleared` country flag before any setup or roster checkpoint can proceed.

## Changed files

- `common/script_constants/006_independence_wave_sakha_constants.txt` adds Sakha pressure, duration, cost, and politics constants.
- `common/scripted_triggers/006_independence_wave_sakha_package_triggers.txt` adds the exact YAK/IW-051 package, state-574 runtime, identity-rights, vanilla-roster, lifecycle, decision, route, force, and generation guards.
- `common/scripted_effects/006_independence_wave_sakha_package_effects.txt` adds generation-safe setup, local vanilla-roster checkpoint, ledger lifecycle, four government routes, five idempotent focus hooks, decision rewards, final validation, dispatch aliases, and cleanup.
- `common/ideas/006_independence_wave_sakha_ideas.txt` adds seven YAK-only package spirits.
- `common/ai_strategy/006_independence_wave_sakha.txt` adds four dormant YAK strategy profiles for arctic survival, host restraint, settled compact, and emergency river guard.
- `common/decisions/006_independence_wave_sakha_decisions.txt` adds the Sakha Arctic Compact category, one founding mission, and ten serialized projects.
- `localisation/english/006_independence_wave_sakha_l_english.yml` adds UTF-8-BOM party names, cosmetic names, idea text, mission/decision text, tooltips, and focus-hook labels.
- `common/national_focus/006_independence_wave_focus.txt` adds five YAK-specific calls at the existing capital, state-inventory, first-oath, former-host, and network focus rewards.

## Identifiers and behavior

- Package predicate: `is_independence_wave_sakha_package` and alias `is_independence_wave_yak_package` require `original_tag = YAK`, active-country membership, and `constant:independence_wave_package_id.iw_051`.
- Anchor: state `574` is required for candidate availability, initialization, runtime validation, capital scope, decisions, and founding-mission completion.
- Ledger variables: `independence_wave_yak_council_cohesion` and `independence_wave_yak_river_guard_readiness` clamp to `0..100`, start at `36` and `38`, and stabilize at `60`.
- Ideas: `yak_fragmented_arctic_mandate`, `yak_sakha_arctic_compact`, `yak_sakha_council_charter`, `yak_sakha_community_register`, `yak_arctic_land_compact`, `yak_lena_workers_councils`, and `yak_river_guard_command`.
- Decisions: `independence_wave_yak_hold_arctic_council`, `independence_wave_yak_secure_lena_depots`, `independence_wave_yak_integrate_river_guards`, `independence_wave_yak_register_sakha_communities`, `independence_wave_yak_settle_former_host_ledgers`, `independence_wave_yak_ratify_constitutional_autonomy`, `independence_wave_yak_adopt_arctic_land_compact`, `independence_wave_yak_convene_lena_councils`, `independence_wave_yak_establish_river_guard_emergency_command`, `independence_wave_yak_codify_durable_sovereignty`, and `independence_wave_yak_open_lena_network_corridor`.
- Focus hooks: `independence_wave_yak_focus_convene_arctic_council`, `independence_wave_yak_focus_secure_lena_communities`, `independence_wave_yak_focus_integrate_river_guards`, `independence_wave_yak_focus_settle_former_host_ledgers`, and `independence_wave_yak_focus_open_lena_arctic_corridor`.
- Force mapping: setup expects `constant:independence_wave_force_profile.mountain_frontier`, `constant:independence_wave_force_package_military_tradition.p51`, current-generation mapping, and the five p51 reinforcement pathways `convert_defectors`, `regional_guards`, `secure_depots`, `terrain_units`, and `professional_officers`; navy and air inheritance remain disabled.
- Political routes: constitutional, popular-council, traditional/arctic-land, and emergency river-guard routes are supported; radical sovereignty and formable-family routes remain excluded.
- Cleanup: removes only package decisions, mission, ideas, variables, flags, cosmetic tag, and package party names, then restores vanilla YAK politics and party-name keys; it never rewrites vanilla characters or portrait tokens.

## Coverage checklist

- Tag and package registration: local predicate complete; central admission registration intentionally not added.
- State/map: state-574 anchor and capital checks complete; optional `644|876|877` are not written locally.
- Politics/parties: local starting and route politics plus YAK party/cosmetic localisation complete.
- Leaders/roster: vanilla character IDs are source-backed and exact; clearance gate remains unset by default.
- Portraits/flags/assets: no new or overridden asset; generic vanilla YAK portrait provenance and rights remain unresolved.
- Focus tree: five shared callbacks wired after helper definitions; no new tree or icon was created.
- Decisions/missions: founding mission and ten project decisions are package-local and generation-guarded.
- Ideas: starting/lifecycle/route ideas are YAK-only and localised.
- Military/setup: p51 mountain-frontier mapping and five reinforcement paths are wired in strict setup.
- Technology/industry/supply/production: no new technology tree, history OOB, production line, supply network, port, railway, or state-building write was made; AI infrastructure priorities are local only.
- AI/probability: four local AI strategy blocks exist and are dormant until strict setup; probability evidence is blocked by the MCP adapter reporting no weighted surfaces.
- Formables: no formable was added.

## Unresolved gates and risks

- `independence_wave_iw_051_identity_rights_cleared` has no local setter and must come from the parent-owned admission packet after source/rights review.
- The vanilla YAK characters are source-backed in the installed game, but their generic Asia portrait consumers and permission/identity review are not a Chaos Redux portrait approval; no portrait override was added.
- No central setup caller or admission promotion was added, so the package remains inert until the parent integrates the exact package dispatch under its existing fail-closed contract.
- No map rewrite was performed; the optional extension reservation and host-retention logic remain central-owned.
- No technology-tree viewer is exposed by the installed MCP package, so YAK technology dependency rendering remains an unresolved limitation.
- No live Hearts of Iron IV launch or in-game validation was performed, per repository rules.

## MCP receipts

- Required map inspection for states `574,644,876,877`: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a7427b4342a818f448a4448f186dd594813dbef97fd0f4e7e650cfa2eafa57b/ed2ca18cf8ae7f9dfa481dce37d64bbc194eeafdfbe392e42d5925b635783766/map-inspect.40b912dc578c3d0a.json`; selected map data loaded, while the workspace report retained unrelated global building/port locator errors.
- Post-change map render: `MAP_RENDERED`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b11da464a58a00f392d20160c03b0af4a5e89f3dc88629a12e57291b26e12dba/19bc6622aa4e1173f05e7669fcf24083650de070e2c617c779d54e9cf91b1d84/map-state.png`; no map file was proposed or changed.
- Required focus inspection before hooks: `FOCUS_INSPECTED`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3178e5100b67b3f2de6f34c9eda0a74a027b7265ceb845e29d64e5657035e3f/c0f4433374553eed95c15590ac7f18485207cfdedf7f56779a91c8a8d518b421/focus-inspect.4a06542f57301176.json`.
- Post-change focus render: `FOCUS_RENDERED`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9b544a2d28f4c36cc2b4c2f8c2f661dd2182eb37c3d62cdc840681c51e6f2791/9dae8b9b160161f94ccd1c4b83f297f902806b1aeb803f60514c7a8544b34e09/independence_wave_focus_tree.focus.html`; the renderer reports the existing workspace missing-icon blockers and layout warnings, not a YAK-specific parse failure.
- Required Event Chain Viewer roots: `EVENT_INSPECTED_PARTIAL`, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f24e0a97e05f6008ab654d0d8d9a42c1232c964c974b9d3332c5fa1cbe30e847/7244178609eaa9fa961e59fc743fc6950293ca99d3399315f7c97fc3304f009f/event-roots-741883f50501.json`.
- Post-change Event Chain Viewer scan and neighborhood render: `event-scan-741883f50501.json` and `event-neighborhood-741883f50501-manifest.json` were returned with partial workspace analysis and no blocking event diagnostics; the event route is intentionally not modified by this tranche.
- Baseline weighted pass through `hoi4.probability_inspect` on the existing package AI returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`.
- Post-change weighted pass through `hoi4.probability_inspect` on `common/ai_strategy/006_independence_wave_sakha.txt` returned the same `no_weighted_surfaces` result in artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cc496c763dfd282ecfc82fa0dc7606780f3f72c99ae43a8afd36a8c04ebcb08f/daea952ffba48a1bca1b0b9111c73999979b902703a9d0687116264e8d3af8fc/probability-inspect-aecf23c812ca.json`.
- Required probability comparison was attempted with the same setup-clearance scenario and returned `PROBABILITY_SURFACE_EMPTY`; the exposed `chaosx_ai_probability_auditor` collaboration route was unavailable, so no quantitative AI claim is made.

## Static checks

- All changed Clausewitz files had balanced braces in a bounded PowerShell check.
- The localisation file has a UTF-8 BOM and zero duplicate localisation keys.
- Local package files contain no portrait/recruit/create-country writes, no unsupported `<=`/`>=` operators, and no YAK leader/flag asset invention.
- The focus source contains all five YAK callback calls at lines `120`, `169`, `199`, `1433`, and `1704` after helper definitions were added.
- Parent review should re-run the repository's broader parser and admission audits after any central dispatch integration.

## Parent review

Review the identity-clearance flag contract, the exact vanilla YAK character consumers, and the route-key/localisation alignment before any admission promotion.

No commit was created in this shared dirty worktree; the parent should selectively stage these package-local files and the five focus-hook additions after review.

# IW-048 UDM current repair audit

Date: 2026-08-15

Scope: read-only re-audit after commit `2087a1619` (`Repair UDM package-local force and cleanup gates`). This handoff supersedes the three-blocker status in the 2026-08-14 audit. No gameplay or central files were edited during this re-audit.

## Result

All three previously identified package-local blockers are closed in the current source.

- `common/scripted_effects/006_independence_wave_udm_package_effects.txt:278` captures `independence_wave_generation_id` as `independence_wave_udm_package_generation_id` during successful setup.
- `common/scripted_effects/006_independence_wave_udm_package_effects.txt:325-327` requires the package snapshot to exist, equal the live generation, and retain the shared current-generation force package before cleanup can mutate UDM state.
- `common/scripted_effects/006_independence_wave_udm_package_effects.txt:349` clears the package snapshot after valid cleanup.
- `common/scripted_effects/006_independence_wave_udm_package_effects.txt:307` loads `independence_wave_add_reinforce_factory_rail_guards` for the fifth IW-048 pathway.
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:177-181` requires factory/rail guards, rejects terrain units, and retains the other four accepted p48 pathways.
- `common/scripted_effects/006_independence_wave_udm_package_effects.txt:342` restores vanilla UDM popularities as democratic 60, communist 10, neutrality 10, and fascist 20.

The setup predicate still validates p48 `industrial_security`, military tradition `54`, state 399, the former-host protection contract, and the five expected reinforcement pathways. The shared Event 006 reset calls package cleanup before clearing `independence_wave_generation_id`, so the valid-generation cleanup ordering remains compatible with the new guard.

## Static validation

A bounded source contract check returned true for setup factory/rail loading, terrain rejection, mapping text, generation snapshot capture, snapshot presence/equality/clear, and exact vanilla popularity restoration. `git show --check 2087a1619` returned no whitespace errors. No UDM/IW-048 references were found in the central package dispatcher or Join files inspected for this audit.

## MCP evidence

- `hoi4_map_inspect` on state 399 returned `MAP_INSPECTED`, one selected state, no unknown province IDs, no missing geometry IDs, and passed state/region/network checks. Global validation remains false due unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3d9dfb72b611f7b8835c97612dd1765d9cab9fabe4fad24d28044f84434a149b/a9bf480074fcac9f552182f29003d0d371930bf070892129edd416557913f991/map-inspect.2bbb0ec306dc6906.json`.
- `hoi4_map_render` completed a read-only state render with state, coastlines, victory points, resources, buildings, supply, rail, and adjacency overlays. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ae19c9cca4c4adb77a5c6061865d7d798092217815cd270b7be3e4a9bc9ad0a/64c1195952142aa3c06ac0297067d95ec504e4fec70013c1b0267292f809a8a6/map-state.png`.
- `hoi4_event_inspect` for `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero selected blocking diagnostics. Bounded `hoi4_event_render` returned `EVENT_RENDERED_PARTIAL` with JSON, SVG, PNG, and manifest artifacts, while workspace-wide helper/lifecycle analysis remained deferred. Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e493d9886de11022199b6a6022491db957c9e317bb9cf1211515cf165c0c40c1/1d847c857acbfa6c24d7cf3cb0d180a3c160e214edbbf0d55ce3f7d373b288fa/event-state-741883f50501-manifest.json`.
- `hoi4_focus_inspect` and `hoi4_focus_render` completed for `independence_wave_focus_tree`. The tree has 184 focuses, 196 connectors, zero crossings, and zero node intersections. Aggregate diagnostics remain unrelated missing continuous-focus icons and layout warnings. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e3178e5100b67b3f2de6f34c9eda0a74a027b7265ceb845e29d64e5657035e3f/c0f4433374553eed95c15590ac7f18485207cfdedf7f56779a91c8a8d518b421/focus-inspect.4a06542f57301176.json`; render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c5494e0a26011621445ed31c1874bd487e070437b9c142fee14ebb5d672ff9a/ab8d9ae55f7baeff6bd34ca88e658ecb81d0ae60ef7a955d9e3cab57817e5dc1/independence_wave_focus_tree.focus.html`.
- `mission_ai_will_do` inspection found 11 candidates, zero available candidates, 15 required inputs, zero unresolved inputs, and `poolComplete=true`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe300eb3ec1d7547a0731cc2cf82e4adee17af9e7cf4d556e7c036571d111076/12eff0293cb2962fe182087be055142cf57cf2536b47182b1ebee82762b10d14/probability-inspect-79dd363b733c.json`.
- `ai_strategy_factor` inspection returned `no_weighted_surfaces`, zero candidates, and zero required inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02194788708ebec70889890e4b6ed52d84be73681935894d1f440aef4e6a77fd/aeb4578cbe90de00901bab43f09dc3186adcede0cb133c303fe30ccc19223bcb/probability-inspect-f02db2218ca2.json`.
- The installed MCP set exposes no Technology Tree Viewer. UDM adds no technology or doctrine surface, so this remains a tooling limitation rather than a UDM defect.

## Remaining boundaries

The package remains unadmitted. Central adapter dispatch, content attestation, normal/scenario preflight, scenario registration, and deterministic Join entries remain intentionally absent and were not edited. The provisional democratic setup/elections choice remains a design review item. No identity, portrait, flag, map, asset, workbook, or live-game admission claim is made.

Changed source files in the owner repair commit were `common/scripted_effects/006_independence_wave_udm_package_effects.txt`, `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt`, and their companion UDM docs. This re-audit added only this handoff.

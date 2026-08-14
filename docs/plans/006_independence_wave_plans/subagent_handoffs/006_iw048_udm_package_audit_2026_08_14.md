# IW-048 UDM package admission audit

Date: 2026-08-14

Audit mode: read-only current-source admission audit. No gameplay, central registry, dispatcher, attestation, preflight, Join, map, asset, workbook, or staging changes were made.

## Verdict

IW-048 UDM remains fail-closed and is not admitted. The package has local constants, scripted triggers/effects, ideas, decisions, localisation, AI strategy, and guarded calls into the shared focus tree, but the current source has three package-local correctness blockers and is intentionally absent from central admission surfaces.

### Superseding source update

The three source blockers listed below were repaired after this read-only snapshot. The current repair receipt is `006_iw048_udm_package_local_repairs_2026_08_14.md`; the package remains fail-closed because central admission, portrait identity, flag provenance, and usable probability evidence are still unresolved.

No new country tag, country definition, country history, character, portrait, flag, map state, formable, technology, GUI, central adapter, attestation, preflight, deterministic Join, or asset was added by this audit.

## Identity and vanilla reuse

- Registry source: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` row IW-048 records Udmurtia, registered tag `UDM`, industrial-forest identity, state `399`, Izhevsk, constitutional/socialist/cultural/military routes, and industrial guards plus forest infantry.
- Installed binding: `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` row IW-048 records anchor `399`, Izhevsk, `399=SOV`, reservation group `RG-399`, unchanged current IDs, and host protection.
- Vanilla registration: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt` maps `UDM` to `countries/Udmurtia.txt`.
- Vanilla identity: `common/countries/Udmurtia.txt` uses the vanilla eastern-European graphics and colour definition; no mod country definition overrides it.
- Vanilla leader: `common/characters/UDM.txt` defines `UDM_boris`, Boris Berman, with `GFX_portrait_Boris_Berman`; the package checkpoint requires this exact character and reuses the existing portrait token.
- Vanilla setup: `history/countries/UDM - Udmurtia.txt` retains `capital = 399` and recruits `UDM_boris`; no package history replacement exists.
- Vanilla flags: the installed vanilla flag ladder contains `UDM_communism.tga`, `UDM_democratic.tga`, `UDM_fascism.tga`, and `UDM_neutrality.tga`; no package flag override or cosmetic-tag transition exists.

## Map, state, host, origin, and collision contract

- The package-local triggers require original tag `UDM`, package id `iw_048`, Event 006 origin `liberation_origin.independence_wave`, and explicit exclusions for Soviet Collapse origin and republic flags.
- Runtime readiness requires state `399` to be owned and controlled by the package, the capital to remain state `399`, a former-host event target, and `liberation_release_protected_state` to be owned by the former host.
- Candidate availability requires an existing non-UDM owner of state `399`; the regional loader reserves `RG-399` and state `399` before package setup.
- The package does not write map ownership, controller, province geometry, state history, resources, buildings, railways, ports, or supply data.
- Existing formable consumers remain outside the package: `common/scripted_triggers/006_independence_wave_formable_state_puzzle_triggers.txt` references UDM/state `399` for existing FORM-12 and FORM-13 qualification, but IW-048 creates no formable family and explicitly requires `independence_wave_formable_family_registered` to be absent during package preparation.

## Package-local source coverage and helper IDs

### Triggers

The package defines `is_independence_wave_udm_package`, `is_independence_wave_udm_project_ready`, `has_independence_wave_udm_unsettled_host`, `can_pay_independence_wave_udm_administration_light_cost`, `can_pay_independence_wave_udm_administration_standard_cost`, `can_pay_independence_wave_udm_strategic_cost`, `is_independence_wave_exact_package_iw_048_runtime_ready`, `can_initialize_independence_wave_iw_048_package`, `has_independence_wave_udm_command_roster`, `is_independence_wave_exact_package_iw_048_tag_available`, `has_stable_independence_wave_udm_compact`, `has_independence_wave_udm_active_package_project`, `has_independence_wave_udm_route_government`, `has_prepared_independence_wave_iw_048_package_setup`, and `has_complete_independence_wave_iw_048_package_setup` in `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt`.

### Effects and ledgers

The package defines visible ledgers `independence_wave_udm_workshop_control` and `independence_wave_udm_forest_rail_readiness`, lifecycle helpers `independence_wave_refresh_udm_compact_lifecycle` and `independence_wave_change_udm_compact_values`, progress helpers `independence_wave_udm_apply_administrative_progress`, `independence_wave_udm_apply_security_progress`, `independence_wave_udm_apply_diplomatic_progress`, `independence_wave_udm_apply_major_settlement`, project helpers `independence_wave_udm_begin_project`, `independence_wave_udm_apply_project_failure`, `independence_wave_udm_apply_former_host_settlement`, and `independence_wave_udm_reward_network_project` in `common/scripted_effects/006_independence_wave_udm_package_effects.txt`.

Route helpers are `independence_wave_install_udm_constitutional_government`, `independence_wave_install_udm_cultural_government`, `independence_wave_install_udm_worker_government`, and `independence_wave_install_udm_emergency_government`.

Focus workers are `independence_wave_udm_focus_convene_workshop_council`, `independence_wave_udm_focus_secure_rail_communities`, `independence_wave_udm_focus_integrate_guards`, `independence_wave_udm_focus_settle_former_host_ledgers`, and `independence_wave_udm_focus_open_corridor`.

Decision-facing aliases are `independence_wave_udm_focus_secure_workshop_depots`, `independence_wave_udm_focus_integrate_industrial_guards`, `independence_wave_udm_focus_register_udmurt_communities`, `independence_wave_udm_focus_ratify_constitutional_autonomy`, `independence_wave_udm_focus_adopt_forest_land_compact`, `independence_wave_udm_focus_convene_worker_councils`, `independence_wave_udm_focus_establish_industrial_emergency_command`, `independence_wave_udm_focus_codify_durable_sovereignty`, and `independence_wave_udm_focus_open_volga_ural_corridor`.

Lifecycle wrappers are `independence_wave_udm_checkpoint_vanilla_roster`, `independence_wave_setup_iw_048_udm`, `independence_wave_dispatch_udm_package_setup`, `independence_wave_validate_iw_048_udm`, `independence_wave_dispatch_udm_package_final_validation`, `independence_wave_cleanup_iw_048_udm`, and `independence_wave_dispatch_udm_package_cleanup`.

### Ideas, decisions, focus, and localisation

The seven ideas are `udm_fragmented_workshop_mandate`, `udm_industrial_forest_compact`, `udm_workshop_charter`, `udm_worker_forest_councils`, `udm_cultural_register`, `udm_cultural_land_compact`, and `udm_industrial_emergency_command` in `common/ideas/006_independence_wave_udm_ideas.txt`.

The founding mission is `independence_wave_udm_hold_workshop_congress` in category `independence_wave_udm_industrial_forest_category`.

The ten project decisions are `independence_wave_udm_secure_workshop_depots`, `independence_wave_udm_integrate_industrial_guards`, `independence_wave_udm_register_udmurt_communities`, `independence_wave_udm_settle_former_host_ledgers`, `independence_wave_udm_ratify_constitutional_autonomy`, `independence_wave_udm_adopt_forest_land_compact`, `independence_wave_udm_convene_worker_councils`, `independence_wave_udm_establish_industrial_emergency_command`, `independence_wave_udm_codify_durable_sovereignty`, and `independence_wave_udm_open_volga_ural_corridor` in `common/decisions/006_independence_wave_udm_decisions.txt`.

The ten decision IDs are present in the active-project trigger, decision definitions, completion effects, cancellation effects, and cleanup removals.

The shared tree `independence_wave_focus_tree` calls five UDM workers in `common/national_focus/006_independence_wave_focus.txt` for workshop council, rail communities, industrial guards, former-host ledgers, and the Volga-Ural corridor; no UDM-specific nodes or icons are introduced.

`localisation/english/006_independence_wave_udm_l_english.yml` covers the category, mission, ten projects, cost triplets, effect tooltips, seven ideas, and four route party names. No missing package-local key was found in the inspected source.

### AI and probability boundary

`common/ai_strategy/006_independence_wave_udm.txt` defines `independence_wave_udm_industrial_survival`, `independence_wave_udm_host_restraint`, `independence_wave_udm_settled_compact`, and `independence_wave_udm_emergency_guard`.

The strategies cover workshops, infrastructure, depots, industrial guards, forest defence, equipment production, and host-war restraint. The source uses static strategy values and does not expose an additional custom weighted pool.

The current `mission_ai_will_do` probability inspection for `common/decisions/006_independence_wave_udm_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED`, `poolComplete=true`, eleven candidates, zero available candidates, fifteen required inputs, and zero unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/05794e499c9f97759789ba9c25e95a3601772a72960aa671b74192e568f87bfa/a1b53ec3bf1a41ecc313d6cc418ecdd66befd529e7d325e0cbaa5eee75610a62/probability-inspect-cae802712e77.json`.

The current `ai_strategy_factor` inspection for `common/ai_strategy/006_independence_wave_udm.txt` returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason=no_weighted_surfaces`, zero candidates, and zero required inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad21c282dd51efd848024e872f484db563f0f58ce0d626f73b7239aab398c1a0/301aa495b0c412504e79df2c21537341f0aa985e59fb6f7092ee514be409d1aa/probability-inspect-f02db2218ca2.json`.

No numeric AI ranking, timing, dominance, or balance claim is made because the mission candidate pool has no available scenario inputs and the strategy source exposes no weighted surfaces to evaluate.

## Concrete package-local blockers

1. **Resolved by the superseding source update.** The accepted IW-048 force row requires `industrial_security`, military tradition `54`, and `mobilize factory or railway guards`; setup and the prepared trigger now use that exact factory/rail pathway and reject the terrain-unit substitute.
2. **Resolved by the superseding source update.** UDM setup snapshots `independence_wave_generation_id` into `independence_wave_udm_package_generation_id`, and cleanup requires that snapshot to equal the live generation plus `has_independence_wave_force_package_for_current_generation = yes`; the shared reset order performs package cleanup before clearing current-generation and force-mapping variables.
3. **Resolved by the superseding source update.** Cleanup now restores vanilla UDM popularities as democratic `60`, communism `10`, neutrality `10`, and fascism `20`.
4. Setup uses `set_politics = { ruling_party = democratic elections_allowed = yes }` in `independence_wave_initialize_udm_politics`. This differs from the provisional setup used by the accepted KUB/TAT pattern and should be explicitly accepted or changed by the package owner; it is an admission review item in addition to the three blockers above.

## MCP evidence and limitations

- `hoi4_map_inspect` on state `399` returned `MAP_INSPECTED` with one selected state, no unknown province IDs, no missing geometry IDs, and passed state/region/network checks. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dea0061bd5218ade4bb192313c92537ca6eefec7f659839ad94280f55df7b0df/00008f648fde2164ce2506b9ea908bea03bba23e2a97fe9cfd492cfc26e3365e/map-inspect.68ac9f655377f72c.json`.
- `hoi4_map_render` produced a read-only state render with coastlines, victory points, resources, state buildings, supply nodes, railways, and adjacencies. PNG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4ae19c9cca4c4adb77a5c6061865d7d798092217815cd270b7be3e4a9bc9ad0a/fa70e3a9349ed7baee4384d20531626a4a52806a663993aa4113cd50dda5e9b7/map-state.png`.
- Map inspection did not constitute a global map pass because unrelated `MAP_BUILDING_POSITION_INVALID` and `MAP_PORT_ADJACENT_SEA_INVALID` diagnostics remain in the workspace.
- `hoi4_event_inspect` on hidden `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with no selected blocking diagnostic. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f55797e1833e4bdbbbbe7dcf5a550c840f58f1e7236adf00a0a8ce169f0312a/529e677382b95a850da72dcad2a0e5df284803fd601292a8c13c078de6cbbc42/event-scan-741883f50501.json`.
- The bounded `hoi4_event_render` request for `chaosx.nr6.350` timed out after 180 seconds. No event-render evidence is claimed; workspace-wide event helper projection is also deferred.
- Corrected `hoi4_focus_inspect` on `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, returned 184 focuses, 196 connectors, zero crossings, and zero node intersections. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c231ee98caeed15357ab49e5acfcb5185845ab2942348e31043a2419f72232e/a04872d340b96e0c298e3df81c27c2719bc6ee350ef35bbebb474555cbc8e8b7/focus-inspect.0244507754010095.json`.
- `hoi4_focus_render` produced HTML/SVG/JSON artifacts, including `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c5494e0a26011621445ed31c1874bd487e070437b9c142fee14ebb5d672ff9a/6051fb6a02360358751699591c2a443ef1d2c2741b0e9a3c7241477d347977ba/independence_wave_focus_tree.focus.html`. Aggregate focus validation remains false because of unrelated missing-icon and long-connector diagnostics; UDM calls add no nodes.
- The installed MCP set exposes no Technology Tree Viewer. UDM adds no technology or doctrine surface, so technology rendering remains an unresolved tooling limitation rather than a package change.

## Central authority boundary

The following surfaces are intentionally absent and must be supplied by the parent admission owner if IW-048 is later promoted: package-dispatch calls in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, content attestation, normal/scenario preflight, scenario registration, and deterministic Join references in `common/scripted_effects/006_independence_wave_join_effects.txt`, `common/scripted_triggers/006_independence_wave_join_triggers.txt`, `common/on_actions/006_independence_wave_join_on_actions.txt`, and `events/006_independence_wave_join.txt`.

No central source was edited or admitted during this audit. The package must remain fail-closed until the remaining politics design review, identity/map/asset acceptance packet, central adapter/attestation/preflight/Join review, and usable probability scenarios are resolved by the owning agent.

## Files reviewed

- `common/script_constants/006_independence_wave_udm_constants.txt`
- `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_udm_package_effects.txt`
- `common/ideas/006_independence_wave_udm_ideas.txt`
- `common/ai_strategy/006_independence_wave_udm.txt`
- `common/decisions/006_independence_wave_udm_decisions.txt`
- `common/national_focus/006_independence_wave_focus.txt`
- `localisation/english/006_independence_wave_udm_l_english.yml`
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv`
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv`
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv`
- Event 006 source `events/006_independence_wave.txt`
- Vanilla UDM country, history, state, character, flag, wiki, and documentation references required by `AGENTS.md`.

No gameplay source was patched, staged, or committed. This handoff is the only file changed by this audit.

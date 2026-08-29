# Two mapmode owner patch handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and ownership

This patch implements exactly two dedicated scripted state mapmodes: famine_state_map_mode and migration_state_map_mode. No combined famine/migration mode, route-only mode, reception-only mode, third mode, event, event-pool row, pacing pulse, recurring world scan, scripted GUI, province/state/region rewrite, gameplay effect, decision, mission, or dynamic modifier was added.

The owner files are common/map_modes/chaosx_state_map_modes.txt, common/script_constants/state_map_modes_constants.txt, common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt, localisation/english/chaosx_map_modes_l_english.yml, and the two validation documents docs/plans/famine_and_migration_system_plans/mapmode_validation.md and this handoff. interface/mapmodes_interface.gfx was inspected but did not need a change because all four existing final DDS consumers are present and uniquely wired.

## Implemented helper map

The mapmode files use native mapmode blocks rather than adding gameplay helpers. The reusable presentation selectors are the following.

- famine_state_map_mode: bottom type = state is the primary food-security stage selector; top type = state is the complementary blockade, relief-proof, or normalized-pressure border selector. The bottom selector reads famine_migration_food_stage. The top selector reads the bounded blockade proof/exposure fields, exact relief-action route proof, exact credited relief delivery, and food pressure. Its outputs are map colors, alpha, thickness, and highlight only. It has no side effects.
- migration_state_map_mode: bottom type = state is the primary deterministic lifecycle selector; top type = state is the complementary obligation, border-policy, corridor-status, reception-share, flight-share, or exact relief-proof selector. Both layers read state-local flags and ledgers already registered by the famine/migration system. Its outputs are map colors, alpha, thickness, and highlight only. It has no side effects.
- GetFamineStateMapModeStage and GetFamineStateMapModeDetail select public versus owner/controller-authorized stage and detail text. Their inputs are the current state scope and the existing food-security variables. Their outputs are localisation keys and interpolated values only.
- GetFamineStateMapModeBlockadeStatus selects the exact blockade proof/exposure wording. GetFamineStateMapModeReliefStatus distinguishes an action-contract route proof from a measured credited delivery. Neither selector treats an unproven route as safe or uses the orphan famine_migration_relief_access_active flag.
- GetMigrationStateMapModeRole mirrors the map bottom-layer priority exactly: trapped, overcrowded, organized evacuation, active exodus, preparing, return readiness, return, resettlement, transit, reception, then no active role. Its inputs are exact state-local flags, missions, corridor operation variables, border policy, and positive ledgers. Its output is the public lifecycle key.
- GetMigrationStateMapModeOriginRole, GetMigrationStateMapModeHostRole, and GetMigrationStateMapModeDestinationRole expose only whether a current state-local projection records the corresponding endpoint role. They deliberately do not scan aligned global cohort arrays during map refresh, so they return a generic projection label rather than inventing a state or country name.
- GetMigrationStateMapModeRouteStatus reports exact corridor safety proof, exact relief-action route proof, exact credited relief delivery, or unproven. It does not consume famine_migration_route_unsafe, famine_migration_route_damaged, or the orphan active-relief-access flag.
- GetMigrationStateMapModeCorridorStatus reports preparation, offer, acceptance, operation/mission, and retained terminal statuses. GetMigrationStateMapModeCorridorGeneration exposes the exact route-generation variable only when that variable exists.
- GetMigrationStateMapModeCohortStatus reports exact, ambiguous, or none, with ambiguity taking precedence over a single-cohort claim. GetMigrationStateMapModeFlowIdentity reads the exact producer-written projection role for voluntary return, forced return, resettlement, deportation, evacuation, transit, and integration, while retaining exact pressure-source evidence for internal or cross-border movement and returning unresolved when no exact role is retained.
- GetMigrationStateMapModeFlightShare and GetMigrationStateMapModeReceptionShare display the last exact producer-written projection shares in authorized tooltips. GetMigrationStateMapModeReceptionCapacityStatus reports the owner capacity validity beside the supporting capacity value. These selectors do not turn a presentation threshold into a gameplay severity label.
- GetMigrationStateMapModeDetail gates detailed migration values to the state owner or controller. Public viewers receive the concise lifecycle role only.

Inputs, outputs, and side effects are intentionally narrow: all selectors consume the current FROM/state scope, emit localisation text, and perform no set_variable, flag, event-target, country, or ledger mutation.

Call sites are limited to the native scripted_map_modes registry, the two existing mapmode tooltip delayed-localisation keys, and the four existing selected/deselected GFX sprite consumers. No gameplay producer callsite was changed; the map layers and selectors read the producer-owned state facts listed below.

## Primary and complementary layers

Famine uses one mode with independent layers. The bottom fill is the five-stage primary classification: stable supply, supply strain, acute shortage, famine, and catastrophic famine. The top border is a second dimension: continuous proven blockade exposure, exact relief-action route proof, exact credited relief delivery, or normalized food pressure. Catastrophic famine adds an unmistakable highlighted border without turning the top layer into another stage palette.

Migration uses one mode with independent layers. The bottom fill covers the lifecycle in deterministic priority: preparing to leave, active exodus, organized evacuation, trapped population, reception, overcrowding, transit, resettlement, return, and return readiness wherever the current producers support those roles. The top border shows obligations, closed/violent/forced-return owner policy on an active state, corridor offer/operation/terminal status, exact relief proof, reception-load share, or flight-pressure share. Closed-border/trapped and overcrowded states receive highlighted border treatment.

The migration fill and border are therefore complementary rather than duplicate role palettes. The reception and flight bands divide the exact state-local ledgers by the exact state_population_k * people_per_k population base. No absolute population amount is used for thickness. The 10% and 25% bands are scale-independent presentation thickness thresholds so the same raw amount cannot imply the same pressure in every state; the authorized tooltip retains the raw amount, population base, and exact producer-written share, and the bands do not label gameplay severity.

## Constants and tuning table

All map colors, alpha values, border thicknesses, exposure bands, and normalized share bands are in common/script_constants/state_map_modes_constants.txt. No undocumented color magic numbers are used in the mapmode source.

- state_map_modes_famine.stage_* remains the existing five-stage fill palette.
- state_map_modes_famine.blockade_*, blockade_exposure_heavy_days, and blockade_exposure_terminal_days control the proven blockade border and its continuous-duration bands.
- state_map_modes_famine.pressure_* and pressure_heavy_normalized control the complementary food-pressure border.
- state_map_modes_famine.relief_delivery_* and relief_route_* distinguish measured delivery from route proof.
- state_map_modes_famine.top_neutral_*, relief_thickness, and catastrophic_border_thickness control neutral and terminal emphasis.
- state_map_modes_migration.preparing_*, organized_evacuation_*, return_readiness_*, transit_*, and the distinct resettlement_* palette complete the lifecycle colors while existing constants cover the other roles.
- state_map_modes_migration.trapped_*, overcrowded_*, closed_border_*, corridor_active_*, corridor_offer_*, corridor_failed_*, reception_load_*, and flight_intensity_* control complementary border statuses.
- state_map_modes_migration.flight_pressure_high_share = 0.10, flight_pressure_heavy_share = 0.25, reception_load_high_share = 0.10, and reception_load_heavy_share = 0.25 are normalized presentation bands, not absolute population severity claims.
- state_map_modes_migration.relief_delivery_*, relief_route_*, top_active_thickness, top_heavy_thickness, and top_critical_thickness control exact relief proof and obligation emphasis.

Both mapmodes retain daily refresh because they read dynamic registered state data. No scheduler or on-action was added.

## Producer, cleanup, and event-target plan

No new event targets are introduced. The mapmodes read state-local variables, flags, missions, and corridor terminal history already owned by the famine/migration system. No global event target is needed, and no map refresh performs a world scan.

- Food stage, pressure, reserves, components, score, exposure, deaths, blockade proof, and blockade exposure are written by the registered famine evaluator and state initialization/cleanup helpers. Blockade exposure resets when the full proof breaks.
- famine_migration_relief_action_route_proven is written by the exact relief-action contract and cleared by its contract cleanup. It means route proof during an action with delivery still pending.
- famine_migration_relief_delivery_proven and positive famine_migration_relief_last_delivery_credit are written after measured delivery and cleared by delivery cleanup. They mean credited delivery, not an active corridor.
- The broader timed famine_migration_relief_access_active flag has no bounded set producer in the current source census and is intentionally not consumed.
- Trapped context is registered by famine_migration_register_trapped_population and cleared when the trapped ledger reaches zero or state cleanup runs.
- Reception and overcrowding context are refreshed by famine_migration_refresh_reception_context from positive state reception load and owner load/capacity, and cleared when the projection is empty.
- Evacuation preparation/mission, corridor preparation/offer/acceptance/operation/mission, return mission, resettlement projection, and return projection are set by their named decisions/effects and cleared by their matching cleanup paths.
- Corridor terminal status is written before terminal cleanup and retained as famine_migration_corridor_last_terminal_status, so the tooltip can distinguish failed/disqualified/rejected/expired/invalidated history without presenting it as a live route.

The census found no bounded setter/clearer pair for famine_migration_route_unsafe or famine_migration_route_damaged. Those predicates were removed from map colors and scripted localisation instead of being treated as general route truth. The exact bounded route proofs remain available where their contracts write them.

The top-layer predicate audit is bounded to the following producers and cleanup paths: famine_migration_blockade_proof is the registered scripted trigger backed by refresh_blockade_proof and apply_blockade_components, which increments or resets blockade exposure; famine_migration_relief_action_route_proven is written by famine_migration_relief_create_contract and cleared by relief selection/contract cleanup; famine_migration_relief_delivery_proven plus positive famine_migration_relief_last_delivery_credit are written by famine_migration_relief_deliver_contract and cleared by relief corridor-proof cleanup; famine_migration_population_trapped is set by famine_migration_register_trapped_population and cleared by zero-ledger reconciliation and state/corridor cleanup; famine_migration_overcrowded_context_active and famine_migration_reception_context_active are set or cleared together by famine_migration_refresh_reception_context; famine_migration_border_policy is written by famine_migration_set_border_policy from the validated request; corridor preparation, offer, acceptance, operation, mission, route safety, and retained terminal status are written and cleared by the named famine_migration_corridor_* effects; and flight/reception raw ledgers are written by the exact movement/reception effects and reduced only by their paired transfer reconciliation. The migration role selectors use those same producer-owned facts and do not introduce proxy flags.

## Migration from the earlier draft

The earlier draft had broader or orphan-proxy predicates in the visual and tooltip paths. This patch narrows them as follows.

- Replaced orphan famine_migration_relief_access_active with exact action-contract route proof and exact post-delivery credit proof.
- Removed general famine_migration_route_unsafe and famine_migration_route_damaged presentation because no bounded producer/clearer was found.
- Removed absolute flight/reception population thickness bands and replaced them with exact state-population-share calculations. Tooltips retain the exact amount, population base, and last recorded projection share.
- Added deterministic migration role priority and kept the top layer independent of it.
- Added explicit origin/current-host/destination projection wording, exact/ambiguous cohort wording, flow identity wording, corridor generation, owner Displacement Load as the primary owner value, Reception Capacity and Border Policy as supporting values, and exact resettled/returned totals.
- Added voluntary-return and forced-return identity when the exact transfer projection role is retained, with unresolved wording only when that state-local role is absent; no country-level pending flag is used as a proxy.

## Validation evidence

The task-specific source audit confirms exactly two definitions named famine_state_map_mode and migration_state_map_mode; no combined, route-only, reception-only, or third famine/migration definition was added. All scripted-localisation localization_key references have an English localization key, all referenced state_map_modes_* constants resolve, and the touched script/localisation braces remain balanced.

The English localisation file retains its UTF-8 BOM and has no :0 keys. The four existing mapmode button definitions each occur exactly once and point to existing final DDS files: famine_state_map_mode_selected.dds, famine_state_map_mode_deselected.dds, migration_state_map_mode_selected.dds, and migration_state_map_mode_deselected.dds. Each is the existing 20x18 one-level uncompressed BGRA8 DDS with native alpha; no replacement art was generated.

The mandatory pre-edit hoi4.map_inspect broad, bounded, and minimal attempts timed out after 180 seconds at the MCP tools/call route. A post-edit minimal retry with stateIds = [41], includeOverview = false, and queryLimit = 1 returned MAP_INSPECTED, status ok, with artifact URI hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e413249a6ce3d65308f2966ff1eeb0b38b5c4fb045379761ba9fa91ed7876952/86b8478ae4dec421522fd9b74dd69340535d4decbefed1a741caf5b770862cba/map-inspect.e2d792f8160aa9aa3d89a8a243887559192834a7ff95f95e79ca03289fbb445f, SHA-256 e413249a6ce3d65308f2966ff1eeb0b38b5c4fb045379761ba9fa91ed7876952, and no mapmode-specific blocker. Aggregate validation was false only for unrelated existing building-position and port-adjacency diagnostics in map/buildings.txt, with diagnostics truncated after 2,654 omitted errors.

A final minimal map_inspect retry after the last source refinements used the same state and query parameters but timed out after 180 seconds while awaiting the MCP tools/call route. The earlier successful post-edit artifact remains the available map-inspect evidence; this later timeout is recorded as an exact MCP blocker.

The final post-edit hoi4.map_render rerun after the relief-proof, normalized-share, resettlement-palette, exact-return-identity, and capacity-validity adjustments returned MAP_RENDERED, status ok, revision 9d7d710f11e4dd5241055e8852e095d90394b8827f55ce0b9316c570b3da96a1, and no blockers. Its offline geometry artifacts were map-state.png SHA-256 52b108966ee8fa0c47ca7458c9be87112fed5d84a5836a4c5f9bb313cb021685, map-state.json SHA-256 84eb5b7c422ff71112b888848f2c899ee967a9a89aed9b60c81c00279bcb12a3, and map-state.html SHA-256 41fadb1662a2e53190a562b2a95d8f9569fd5239735371be9d0e81ede0bb4e21. The render proves state geometry and transport substrate only; the tool cannot execute dynamic map colors, scripted tooltips, or click regions.
The final render resource URIs are hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52b108966ee8fa0c47ca7458c9be87112fed5d84a5836a4c5f9bb313cb021685/a4ed0f4e4349464582c7319bf91e6d89db2e191788fcb321acb1f747e00e264b/map-state.png, hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/84eb5b7c422ff71112b888848f2c899ee967a9a89aed9b60c81c00279bcb12a3/5ade08eb606ec77870a3307a4883f1453eb49114f00d2535964b11cc963add43/map-state.json, and hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/41fadb1662a2e53190a562b2a95d8f9569fd5239735371be9d0e81ede0bb4e21/3da704960661cfb4072e30b25f69e38521f2869d620ab71f51697e89874a0ab5/map-state.html.

The hardcoded mapmodes GUI inspect/render route accepted post-change requests but resolved zero elements or exposed no linked raster/payload. This is an exact presentation blocker, not evidence of runtime map color or tooltip execution. No map_rewrite, gui_rewrite, or probability workflow was appropriate because this patch changes declarative mapmode presentation only and introduces no weighted logic.

## Remaining truthful presentation gaps

- The exact origin/current-host/destination endpoint names are not available to map refresh from the aligned global cohort arrays without a new producer or scan, so the authorized tooltip reports exact projection role rather than inventing names.
- A return identity is unresolved only when the exact transfer projection role was not retained on the state; the tooltip does not infer it from country-level pending flags.
- The map renderer and hardcoded GUI route do not execute dynamic scripted colors, tooltip authorization, or click regions, so live in-game presentation remains user-owned validation.
- The unrelated aggregate map diagnostics do not belong to these mapmode files and were not changed under the exclusive-file boundary.

No gameplay simplification or fallback was added. The route and endpoint gaps above are explicitly reported blockers, and the mapmodes use neutral/unproven wording where the source cannot prove a stronger claim.

## Files changed

- common/map_modes/chaosx_state_map_modes.txt
- common/script_constants/state_map_modes_constants.txt
- common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt
- localisation/english/chaosx_map_modes_l_english.yml
- docs/plans/famine_and_migration_system_plans/mapmode_validation.md
- docs/plans/famine_and_migration_system_plans/subagent_handoffs/two_mapmode_owner_patch.md

No commit was created; the parent agent should review and commit the plan if the shared worktree policy requires it.

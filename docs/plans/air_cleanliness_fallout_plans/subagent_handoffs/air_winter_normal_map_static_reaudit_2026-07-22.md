# Air Winter Normal Map Static Re-audit

Date: 2026-07-22

Status: static source route passes. Runtime presentation remains unobserved by user instruction.

## Verdict

The promoted Air Winter visual route is an ordinary-map entity system. It is not dependent on the Air Winter mapmode. The synchronized global host calls the existing monthly Air Contamination update. That update begins one Air Winter cycle, visits every state in its existing state pass, updates the authoritative state phase and survival ledgers, and calls `air_winter_refresh_regional_visuals` at the end of each state update.

The static route covers all nine reviewed presentation classes and all six active phases. Phase 0 creates no visual and removes any recorded ground, particle, vegetation, and hydrology slots. No additional world iterator was added for presentation.

This re-audit does not claim that Hearts of Iron IV rendered the package. The user instructed the implementation run not to launch the game.

An independent `chaosx_event_completion_auditor` returned a static PASS. It confirmed the exact nine-class ledger counts, all 54 numeric class and phase aliases, all 27 numeric class prop aliases, the nine particle chains, ordinary-map lifecycle, regional weather selection, phase 0 cleanup, and the same runtime-only limits recorded below.

## Engine evidence

The installed official `effects_documentation.md` documents `create_entity` in any scope, state-relative placement, stable numeric ids, and replacement when the supplied id already exists. It also documents `destroy_entity` by numeric id. The offline Effects reference independently documents state-relative entity creation and numeric destruction.

The visual lifecycle uses five non-overlapping deterministic id bands:

- ground: `1860000 + state id`
- primary weather: `1862000 + state id`
- secondary weather: `1864000 + state id`
- dead vegetation: `1866000 + state id`
- hydrology: `1868000 + state id`

The installed live state domain is 1 through 1081. Every calculated id stays inside its allocated 2,000-id band and below the Clausewitz fixed-point ceiling. Active slots are replaced with the same id. Phase 0 and invalid class or phase rows destroy the recorded slots.

## Ordinary-map call chain

The reviewed call chain is:

1. `on_monthly` selects the existing global host and calls `air_contamination_monthly_update`.
2. The monthly update calls `air_winter_begin_monthly_cycle` when no Fallout rewrite is active.
3. The begin effect calls `air_winter_prepare_regional_visual_cycle`.
4. The existing `every_state` pass calls `air_winter_update_state` once per state.
5. The state update reconciles the typed presentation ledger, resolves the final phase and survival values, and calls `air_winter_refresh_regional_visuals` last.
6. The refresh effect creates or replaces ordinary-map entities relative to the current state.

The mapmode scripted GUI is not present in this chain. Turning the mapmode off does not remove the entity route in source.

## Regional and phase coverage

The typed state collection contains 1,081 rows with 1,081 unique ids, no duplicates, no missing ids, and no out-of-range ids.

| Class | States | Primary weather progression |
| --- | ---: | --- |
| Boreal and continental | 244 | snow and frost from Phase 1 through Phase 6 |
| Temperate maritime | 76 | cold rain and mist in Phases 1 through 4, snow in Phases 5 and 6 |
| Mediterranean | 58 | cold rain and mist in Phases 1 through 5, mild snow and frost in Phase 6 |
| Desert and arid plateau | 202 | dry ground in Phases 1 and 2, ash from Phase 3 through Phase 6 |
| Tropical coast and monsoon | 152 | cold rain and mist from Phase 1 through Phase 6 |
| Equatorial rainforest | 47 | cold rain and mist from Phase 1 through Phase 6 |
| Mountain and highland | 176 | snow and frost from Phase 1 through Phase 6 |
| Island and oceanic | 77 | cold rain and mist in Phases 1 through 4, mild snow in Phases 5 and 6 |
| Polar and subpolar | 49 | snow and frost from Phase 1 through Phase 6 |

This matrix does not apply universal snow. Warm and maritime classes remain rain, mist, wet ground, dim light, and ash led. Desert states remain dry in the first two phases.

The secondary weather channel adds progressive ash in Phases 4 through 6 outside the arid class. Local Fallout can add mild ash in Phases 1 through 3. Recovery can occupy the secondary channel with runoff in Phases 1 through 3, while the class-specific thaw prop carries recovery at later phases.

Dead vegetation is selected by reviewed class thresholds or low food. Frozen-water props use class-specific thresholds and are excluded by default from tropical, equatorial, and oceanic states. Recovery replaces eligible frozen-water presentation with thaw and flood presentation. The ground phase matrix supplies progressive dimming, frost or wetness, soot, and desaturation for all active classes.

## Asset and registry audit

The ordinary-map package is dedicated to Air Winter and Fallout.

- 81 numeric entity aliases exist for nine classes times six ground phases plus three class props.
- 85 unique PDX mesh definitions exist and all 166 descriptive and numeric entity references resolve to them.
- 85 runtime `.mesh` files exist.
- 181 DDS records are present in the build report and every recorded path exists.
- Nine weather entity wrappers resolve to nine dedicated particle types.
- Nine particle assets resolve to four dedicated atlases. Every atlas path exists.
- The particle source package contains four separately authored frames for each of snow and frost, cold rain and mist, ash and dirty snow, and thaw and flood.
- The reviewed Air Winter runtime model package has no SHA-256 match with the repository's Zombie visual files.

The package does not reference Zombie ids, sprites, audio, entity names, model paths, or particle paths.

## Runtime boundary

The following facts remain unobserved because Hearts of Iron IV was not launched:

- state-center placement and z ordering
- visibility at the configured minimum zoom
- visual scale on very small and very large states
- particle playback and particle cleanup after entity replacement
- save and reload reconstruction before the next monthly pulse
- multiplayer synchronization
- ordinary-map frame cost with the maximum simultaneous five-slot load
- conflicts with entity ids introduced by another enabled mod

These are runtime validation limits, not approved fallbacks. The source route, class coverage, phase selection, cleanup path, registry, and file existence pass static review.

## Files reviewed

- `common/on_actions/chaosx_on_actions_chaos_meter.txt`
- `common/scripted_effects/chaos_meter_effects.txt`
- `common/scripted_effects/air_cleanliness_winter_effects.txt`
- `common/scripted_effects/air_cleanliness_winter_visual_effects.txt`
- `common/scripted_triggers/air_cleanliness_winter_triggers.txt`
- `common/script_constants/air_cleanliness_winter_presentation_states.txt`
- `common/script_constants/air_cleanliness_winter_visual_constants.txt`
- `gfx/entities/air_cleanliness_winter_regional_visuals.asset`
- `gfx/entities/air_cleanliness_winter_regional_visuals.gfx`
- `gfx/entities/air_cleanliness_winter_regional_particles.asset`
- `gfx/entities/air_cleanliness_winter_regional_particles.gfx`
- `gfx/particles/air_cleanliness_winter/*.asset`
- `docs/assets/air_cleanliness_fallout/regional_map_visuals/build_report.json`
- `docs/assets/air_cleanliness_fallout/regional_map_visuals/mesh_export_report.json`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_NORMAL_MAP_PROOF.md`
- `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_REGIONAL_VISUAL_WIRING_PROOF.md`

## Simplifications and blockers

No source-level simplification was found in the ordinary-map regional selection or asset registry. Runtime presentation remains unproven under the user's no-launch instruction and must not be described as observed gameplay.

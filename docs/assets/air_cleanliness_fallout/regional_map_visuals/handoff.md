# Air Winter Regional Ordinary-Map Integration Handoff

## Boundary

This document records the installed gameplay integration and the remaining UI and runtime proof boundary. The asset package registers every mesh, particle, grade, and static fallback. The synchronized ordinary-map entity lifecycle is implemented in `common/scripted_effects/air_cleanliness_winter_visual_effects.txt`.

The integration replaces the temporary state-64 proof from the existing `air_winter_update_state` call inside `air_contamination_monthly_update`. It adds no `on_daily`, `on_weekly`, `on_monthly`, `every_state`, or other world iterator. The full-screen grade and static accessibility setting remain unwired because their interface parent and user setting are not proven.

## Authoritative inputs

State scope inputs already exist:

- `air_winter_presentation_class`: stable value 1-9, while value 0 is unclassified
- `air_winter_phase`: stable value 0-6
- `air_winter_previous_phase`: the preceding phase
- `air_winter_peak_phase_memory`: highest phase in the current winter episode
- `air_winter_trend`: `-1` recovering, `0` stable, `1` worsening
- `air_winter_phase_changed_this_tick`: state flag set by the existing lifecycle

Phase and regional classification are not duplicated in visual-only variables. The visual schema version is the only persistent numeric visual value.

Five presence flags record normal cleanup hints. Deterministic IDs remain reconstructible from the state id, so no generated entity handle is persisted.

| Slot | Base | Live range for states 1-1081 |
| --- | ---: | ---: |
| Regional ground | 1,860,000 | 1,860,001 to 1,861,081 |
| Primary particle | 1,862,000 | 1,862,001 to 1,863,081 |
| Secondary particle | 1,864,000 | 1,864,001 to 1,865,081 |
| Dead vegetation | 1,866,000 | 1,866,001 to 1,867,081 |
| Frozen water or thaw | 1,868,000 | 1,868,001 to 1,869,081 |

These ranges do not collide with another repository literal and remain below the Clausewitz fixed-point ceiling. Frozen water and thaw are mutually exclusive and share the hydrology slot.

## Numeric alias contract

Ground entities:

`air_winter_class_<class>_phase_<phase>_entity`

where `<class>` is 1-9 and `<phase>` is 1-6.

Prop entities:

- `air_winter_class_<class>_dead_vegetation_entity`
- `air_winter_class_<class>_frozen_water_entity`
- `air_winter_class_<class>_thaw_flood_entity`

These numeric aliases are registered in `gfx/entities/air_cleanliness_winter_regional_visuals.asset`. Descriptive aliases also exist for manual inspection, but dynamic selection should use the numeric contract.

## Dynamic creation pattern

The installed route calculates each slot id as a centralized base plus `THIS.id`, then uses `meta_effect` to emit literal `id`, `state`, and placement values. The same id replaces the active entity on every monthly pulse.

```txt
set_temp_variable = { air_winter_visual_state_id = THIS.id }
set_temp_variable = { air_winter_visual_ground_id = constant:air_winter_visual_entity_id.ground_base }
add_to_temp_variable = { air_winter_visual_ground_id = air_winter_visual_state_id }

meta_effect = {
	text = {
		create_entity = {
			entity = air_winter_class_[CLASS]_phase_[PHASE]_entity
			id = [ENTITY_ID]
			state = [STATE_ID]
			z = [GROUND_Z]
			scale = [GROUND_SCALE]
			min_zoom = [MIN_ZOOM]
		}
	}
	CLASS = "[?air_winter_presentation_class|.0]"
	PHASE = "[?air_winter_phase|.0]"
	ENTITY_ID = "[?air_winter_visual_ground_id|.0]"
	STATE_ID = "[?air_winter_visual_state_id|.0]"
	GROUND_Z = "[?air_winter_visual_ground_z|.0]"
	GROUND_SCALE = "[?air_winter_visual_ground_scale|.0]"
	MIN_ZOOM = "[?air_winter_visual_minimum_zoom|.0]"
}
```

Cleanup injects the same calculated id into the documented literal destroy form:

```txt
meta_effect = {
	text = { destroy_entity = [ENTITY_ID] }
	ENTITY_ID = "[?air_winter_visual_ground_id|.0]"
}
```

The same lifecycle applies to each prop and particle slot. A class or phase change replaces the stable slot id. Phase 0, an unclassified state, system disable, schema migration, state reset, or deferred global reset destroys stale slots.

## Ground mapping

The ground mapping is intentionally simple and exhaustive:

| Presentation class | Phase 1-6 entity pattern |
| --- | --- |
| Boreal and continental | `air_winter_class_1_phase_<phase>_entity` |
| Temperate maritime | `air_winter_class_2_phase_<phase>_entity` |
| Mediterranean | `air_winter_class_3_phase_<phase>_entity` |
| Desert and arid plateau | `air_winter_class_4_phase_<phase>_entity` |
| Tropical coast and monsoon | `air_winter_class_5_phase_<phase>_entity` |
| Equatorial rainforest | `air_winter_class_6_phase_<phase>_entity` |
| Mountain and highland | `air_winter_class_7_phase_<phase>_entity` |
| Island and oceanic | `air_winter_class_8_phase_<phase>_entity` |
| Polar and subpolar | `air_winter_class_9_phase_<phase>_entity` |

No phase-0 entity exists. Warm-class ground plates use dimming, cold cast, ash, wetness, deadening, and modest frost. They do not become universal snow plates.

## Particle mapping

Abbreviations:

- `SFm`: `air_winter_snow_frost_mild_entity`
- `SFs`: `air_winter_snow_frost_severe_entity`
- `CRm`: `air_winter_cold_rain_mist_mild_entity`
- `CRs`: `air_winter_cold_rain_mist_severe_entity`
- `ADm`: `air_winter_ash_dirty_snow_mild_entity`
- `ADs`: `air_winter_ash_dirty_snow_severe_entity`
- `ADt`: `air_winter_ash_dirty_snow_terminal_entity`
- `TFm`: `air_winter_thaw_flood_mild_entity`
- `TFs`: `air_winter_thaw_flood_severe_entity`

The `+` notation means primary plus secondary particle slot. `-` means no animated precipitation entity. The ground material still shows the phase.

| Class | P1 | P2 | P3 | P4 | P5 | P6 |
| --- | --- | --- | --- | --- | --- | --- |
| Boreal/continental | SFm | SFm | SFs | SFs + ADm | SFs + ADs | SFs + ADt |
| Temperate maritime | CRm | CRm | CRs | CRs + ADm | SFm + ADs | SFs + ADt |
| Mediterranean | CRm | CRm | CRs | CRs + ADm | CRs + ADs | SFm + ADt |
| Desert/arid plateau | - | - | ADm | ADm | ADs | ADt |
| Tropical coast/monsoon | CRm | CRm | CRs | CRs + ADm | CRs + ADs | CRs + ADt |
| Equatorial rainforest | CRm | CRm | CRs | CRs + ADm | CRs + ADs | CRs + ADt |
| Mountain/highland | SFm | SFm | SFs | SFs + ADm | SFs + ADs | SFs + ADt |
| Island/oceanic | CRm | CRm | CRs | CRs + ADm | SFm + ADs | SFm + ADt |
| Polar/subpolar | SFm | SFs | SFs | SFs + ADm | SFs + ADs | SFs + ADt |

This table preserves the spec requirement that tropical and desert states look colder without automatic snow. If the runtime performance gate cannot support two particle entities per state, that is a blocker requiring a design decision. Do not silently remove one family. An explicitly approved reduced-density mode can prioritize ash in phases 4-6 while retaining the regional ground cue.

Eligible recovery at phases 1-3 uses `TFs` in the secondary slot during a downward phase step and `TFm` during continuing recovery. At phases 4-6, required ash retains the secondary slot and the class-specific thaw prop carries the recovery cue. A local fallout state receives `ADm` in an otherwise empty secondary slot at phases 1-3, except when visible thaw runoff takes precedence.

## Prop mapping

Props should represent an active gameplay consequence, not decorate every state indiscriminately. Recommended default activation follows the approved visual state matrix:

| Class | Dead vegetation from | Frozen water from | Recovery thaw/flood eligibility |
| --- | --- | --- | --- |
| Boreal/continental | Phase 4 | Phase 3 | Recovering after phase 3+ |
| Temperate maritime | Phase 2 | Phase 4 | Recovering after phase 3+ |
| Mediterranean | Phase 2 | Phase 4 | Recovering after phase 3+ |
| Desert/arid plateau | Phase 4 | Phase 3 | Recovering after phase 3+, for pipe/well/oasis runoff |
| Tropical coast/monsoon | Phase 2 | No default, require a proven local-freeze condition | Recovering after phase 2+ |
| Equatorial rainforest | Phase 2 | No default, require a proven local-freeze condition | Recovering after phase 2+ |
| Mountain/highland | Phase 4 | Phase 2 | Recovering after phase 2+ |
| Island/oceanic | Phase 4 | No default, require latitude or local-freeze support | Recovering after phase 3+ |
| Polar/subpolar | Phase 5 | Phase 1 | Recovering after phase 2+ |

The table describes default class behavior. A future documented local-freeze or gameplay-consequence flag may override a `No default` cell. Do not infer one from art alone.

During worsening or stable phases, destroy the thaw/flood presentation. During recovery, thaw/flood replaces frozen-water presentation where eligible. It does not stack with frozen water. When recovery ends or phase reaches clear, destroy the thaw/flood presentation. Dead vegetation persists during an active phase when the regional threshold or low-food consequence remains true.

## Static-mode mapping

An approved static-accessibility setting should replace each animated family with its package-owned mesh entity:

- snow/frost -> `air_winter_static_snow_frost_entity`
- cold rain/mist -> `air_winter_static_cold_rain_mist_entity`
- ash/dirty snow -> `air_winter_static_ash_dirty_snow_entity`
- thaw/flood -> `air_winter_static_thaw_flood_entity`

The matching GUI sprites are:

- `GFX_air_winter_regional_static_snow_frost`
- `GFX_air_winter_regional_static_cold_rain_mist`
- `GFX_air_winter_regional_static_ash_dirty_snow`
- `GFX_air_winter_regional_static_thaw_flood`

Choose one runtime route per setting. Do not render both the mesh and sprite fallback. If a reduced-effects setting permits only one static marker in phases 4-6, ash has signal priority, but that reduction requires explicit design approval.

## Atmospheric grade mapping

Registered sprites:

- `GFX_air_winter_regional_grade_phase_1`
- `GFX_air_winter_regional_grade_phase_2`
- `GFX_air_winter_regional_grade_phase_3`
- `GFX_air_winter_regional_grade_phase_4`
- `GFX_air_winter_regional_grade_phase_5`
- `GFX_air_winter_regional_grade_phase_6`
- `GFX_air_winter_regional_grade_recovery_soot_thinning`
- `GFX_air_winter_regional_grade_recovery_uv_clear`

The grade reads global forcing/recovery state, while ground/particle/prop assets read local state class and phase. A later GUI implementation must prove a non-blocking map-layer parent and order. It must keep top bars, tabs, popups, text, borders, units, map icons, and selection readable and clickable. It must hide or recede outside supported ordinary-map views if that is needed for legibility.

Do not promote the proof GUI parent merely because the sprites exist. `mapicons_container`, resolution behavior, UI scale, mapmode coexistence, and multiplayer visibility remain proof obligations.

## Lifecycle sequence

For each state visited by the existing monthly pass:

1. Calculate the five stable slot ids from `THIS.id`.
2. On a schema mismatch, destroy all five ids and stamp the current state visual schema.
3. Validate `air_winter_presentation_class` and `air_winter_phase` using the existing class and phase helpers.
4. If class 0, phase 0, or Air Winter is disabled, destroy only slots whose presence flags are set.
5. Recreate exactly one active ground entity using the numeric alias and the stable ground id.
6. Recreate zero to two particle entities using the regional and recovery matrix.
7. Recreate or destroy dead vegetation and the mutually exclusive frozen-water or thaw hydrology slot.

State reset destroys every deterministic slot id immediately. Global reset marks state cleanup for the next existing monthly pass, which avoids a second world iterator. Save-load reconstruction is idempotent in script because every desired slot is recreated with the same id on the first monthly pulse and replaces any surviving copy.

## Runtime proof checklist

Before gameplay integration can be called complete, observe:

- all nine class families at phases 1, 4, and 6 on ordinary political and terrain maps
- no universal desert/tropical snow
- state-center placement, z order, borders, counters, icons, and click behavior
- one- and two-particle combinations at near, medium, and far zoom
- static setting replacement and cleanup
- phase escalation, recovery thaw, phase 0, disable, and global reset cleanup
- save-load reconstruction and repeated refresh without stacking
- multiplayer consistency
- world-scale entity and particle cost
- grade order, click-through, UI scale, resolution, mapmode, and open-window behavior

Until those observations exist, report ordinary-map runtime presentation as unproven even though the asset package is complete.

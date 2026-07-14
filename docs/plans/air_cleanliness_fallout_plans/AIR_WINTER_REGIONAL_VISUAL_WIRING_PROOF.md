# Air Winter Regional Visual Wiring Proof

## Conclusion

The ordinary-map route is statically supported and wired into the synchronized Air Winter monthly lifecycle. It is not runtime proven. HOI4 was not launched.

The implementation creates class-specific ground, weather, ash, vegetation, ice, and thaw entities during ordinary map play. It uses the existing host-owned `every_state` pass and adds no second world iterator.

## Authoritative files

- `common/script_constants/air_cleanliness_winter_visual_constants.txt`
- `common/scripted_effects/air_cleanliness_winter_visual_effects.txt`
- `common/scripted_effects/air_cleanliness_winter_effects.txt`
- `common/scripted_triggers/air_cleanliness_winter_triggers.txt`
- `common/scripted_effects/chaos_meter_effects.txt`
- `gfx/entities/air_cleanliness_winter_regional_visuals.asset`
- `gfx/entities/air_cleanliness_winter_regional_visuals.gfx`
- `gfx/entities/air_cleanliness_winter_regional_particles.asset`
- `gfx/entities/air_cleanliness_winter_regional_particles.gfx`
- `docs/assets/air_cleanliness_fallout/regional_map_visuals/manifest.md`
- `docs/assets/air_cleanliness_fallout/regional_map_visuals/handoff.md`

## Engine references

The installed official effect documentation records the required surfaces:

- `effects_documentation.md`, `create_entity`, lines 3051-3067, supports any scope, literal entity and state values, optional `id`, replacement of an existing id, z, scale, and minimum zoom.
- `effects_documentation.md`, `destroy_entity`, lines 3528-3536, documents destruction by literal numeric id.
- `effects_documentation.md`, `meta_effect`, lines 4833-4849, documents construction and execution of an effect from substituted text.
- `script_concept_documentation.md`, Math Expressions, records Clausewitz fixed-point arithmetic.
- The offline Data Structures and Scopes pages document variables, temporary variables, `THIS.id`, state scope, and the fixed-point value model.

Kaiserreich's `common/scripted_effects/00_ambient_object_effects.txt` provides the approved large-mod precedent for stable literal entity ids and `min_zoom = 1100`. Vanilla and Kaiserreich provide no generated-id cleanup precedent. The implementation therefore calculates a deterministic id, then uses `meta_effect` to emit the documented literal forms.

## Deterministic five-slot ledger

Each state id from 1 through 1081 receives five non-overlapping calculated ids:

| Slot | Formula | Maximum |
| --- | --- | ---: |
| Ground | 1,860,000 + state id | 1,861,081 |
| Primary particle | 1,862,000 + state id | 1,863,081 |
| Secondary particle | 1,864,000 + state id | 1,865,081 |
| Dead vegetation | 1,866,000 + state id | 1,867,081 |
| Hydrology | 1,868,000 + state id | 1,869,081 |

All calculated values remain below the fixed-point ceiling of 2,147,483.647. A repository scan found no other literal inside these ranges. The engine does not expose a reserved entity-id namespace, so collision with another externally combined mod remains unprovable. The bands are 2,000 ids apart and are valid for the installed 1 through 1081 state domain. A future or combined map with a state id of 2001 or higher would overlap the bands and requires a new reviewed allocation.

The hydrology slot holds frozen water or thaw. It never holds both. This reduces no visible state because the two conditions are mutually exclusive.

## Monthly authority and order

`air_contamination_monthly_update` remains the only host-owned global monthly entry point. Its existing state pass calls `air_winter_update_state` once per state. The regional visual refresh runs at the end of that state update after classification, phase movement, recovery direction, survival ledgers, damage, and event candidacy are known.

The post-pass proof-entity refresh was removed. The retired literal id `8600064` is destroyed during visual schema migration and global reset.

All create and destroy effects run from synchronized gameplay script. No scripted GUI or client-only button creates a map entity.

## Regional weather proof

The ground entity uses the numeric alias `air_winter_class_<class>_phase_<phase>_entity`. The asset package registers every combination for classes 1-9 and phases 1-6.

The two particle channels preserve the reviewed matrix:

- Boreal, mountain, and polar classes use snow and frost as their primary weather.
- Maritime, Mediterranean, tropical, equatorial, and most oceanic phases use cold rain and mist.
- Desert states receive no low-phase snow or rain particle. Their ash channel begins at phase 3.
- Phase 4 adds mild ash as a second channel outside the desert class.
- Phase 5 adds severe ash.
- Phase 6 adds terminal ash.
- Local nuclear fallout adds mild ash at phases 1-3 when thaw does not occupy the second channel.
- Eligible recovery at phases 1-3 uses a mild thaw particle, or the severe runoff frame on the downward phase-change pulse.

Warm classes therefore become darker, colder, wetter, and ashier without universal snow.

## Vegetation and hydrology proof

Dead vegetation follows the reviewed regional thresholds. Low food also keeps the marker present during an active recovery phase, which ties the art to a gameplay consequence.

Frozen water follows class-specific thresholds:

- boreal and arid from phase 3
- maritime and Mediterranean from phase 4
- mountain from phase 2
- polar from phase 1
- no default freeze for tropical, equatorial, or oceanic states

Thaw eligibility reads recovery trend and a persistent peak-phase memory. It replaces frozen water and can appear in warm wet classes as runoff or flood without implying prior blanket ice.

## Save recovery and cleanup proof

Every desired slot is recreated with the same id on each monthly pulse. The documented replacement behavior makes repeated refresh idempotent and provides reconstruction on the first resumed monthly pulse if an entity was not retained by the save.

A state visual schema mismatch destroys all five deterministic ids before rebuilding. State reset destroys all five ids immediately. Global reset sets the existing deferred state-reset flag, and the next existing monthly pass clears every state without adding a new iterator. Finalize clears the reset request only after that pass.

Presence flags reduce unnecessary destruction during ordinary clear phases. They are not used to calculate identity. Administrative and schema cleanup can always reconstruct every id from `THIS.id`.

## Asset ownership and registration

The regional package contains:

- 181 dedicated DDS files
- 85 custom PDX meshes
- 166 regional visual entities
- 81 numeric class aliases
- nine registered particle entities and particle types
- 16 separately authored particle source frames
- 12 registered review, fallback, and grade sprites

All runtime tokens referenced by the gameplay effect resolve to Fallout-owned files and identifiers. No zombie path, sprite, sound, image, or entity is referenced.

## Unproven runtime boundary

Static evidence cannot prove:

- whether the engine loads and renders every new mesh and particle registration
- exact state centering, scale, z order, terrain clipping, border readability, and zoom behavior
- particle atlas playback, density, culling, and two-channel stacking
- entity persistence across save and load before the next monthly reconstruction pulse
- multiplayer replication and late-join presentation
- destruction of an absent entity id
- interaction with another mod that independently chooses the same entity-id range
- world-scale rendering and simulation cost
- the full-screen grade parent, click-through behavior, resolution scaling, and mapmode interaction

The full-screen grade sprites and static accessibility alternatives remain registered but unwired. They are not substituted for the animated route. No completion claim should treat those runtime surfaces as observed.

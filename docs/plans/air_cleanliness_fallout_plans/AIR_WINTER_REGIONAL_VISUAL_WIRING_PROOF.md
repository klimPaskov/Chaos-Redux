# Air Winter Regional Visual Wiring Proof

## Conclusion

The ordinary-map route is statically supported and wired into the synchronized Air Winter monthly lifecycle. HOI4 was not launched, and no live observation claim is made.

The implementation creates class-specific ground, weather, ash, vegetation, ice, and thaw entities during ordinary map play. It uses the existing host-owned `every_state` pass and adds no second world iterator.

## Authoritative files

- `common/script_constants/fallout_consolidated_constants.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_triggers/fallout_consolidated_triggers.txt`
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
- no unowned review, fallback, grade, or accessibility sprite registrations

All runtime tokens referenced by the gameplay effect resolve to Fallout-owned files and identifiers. No zombie path, sprite, sound, image, or entity is referenced.

## Post-wire static audit, 2026-07-15

The final package was audited again from the live runtime files after integration:

- The installed vanilla state database contains 1,081 unique state ids, exactly 1 through 1081. The typed presentation ledger contains 1,081 rows, 1,081 unique ids, no duplicate membership, no missing id, and no out-of-range id. Its class counts are 244 boreal, 76 temperate maritime, 58 Mediterranean, 202 arid plateau, 152 tropical monsoon, 47 equatorial rainforest, 176 mountain highland, 77 island oceanic, and 49 polar or subpolar.
- The gameplay meta-effect can emit 81 mesh entity names and nine particle entity names. All 90 names resolve. The mesh asset has 166 unique entity definitions, including all 54 numeric class-phase aliases and all 27 numeric class-prop aliases. The particle asset has all nine required wrappers with no duplicate entity name.
- The text registrations contain 106 file references and 101 unique paths. Every path exists. All 85 `pdxmesh` references resolve to one of the 85 registered mesh names. All nine particle instance types resolve to one of the nine particle-file definitions, and every wrapper particle resolves to one of the nine registered instances.
- `mesh_export_report.json` contains 85 records. Every runtime mesh exists, every SHA-256 matches the record, and every diffuse, specular, and normal texture named by the record exists. The report records 54 `PdxMeshAdvanced` ground meshes and 31 `PdxMeshAlphaBlend` prop or static meshes.
- `build_report.json` contains 181 DDS records. Every runtime file exists, has a valid DDS header, and matches its recorded width, height, and byte count. All 22 recorded source hashes match. The 16 separately authored particle source frames have 16 distinct hashes.
- The 181 runtime DDS files have 177 distinct hashes. The only four duplicate groups are intentional pairs between each static fallback sprite and the matching static mesh diffuse. No other runtime DDS is duplicated. A content-hash comparison against all 134 repository DDS files under zombie-named paths found no identical file.
- The current entity-id bands have no literal collision elsewhere in gameplay, GUI, or asset script. The installed state maximum remains 1081, below the documented band-overlap boundary.
- The particle wrapper form matches vanilla `gfx/entities/weather_entities.asset`: an idle state with `state_time = 2`, a time-zero particle event, and `keep_particle = yes`. The Air Winter wrappers omit vanilla weather sound events by design.

Decoded contact-sheet review found nine visibly distinct regional ground families, region-specific dead vegetation, ice, and thaw props, and four independently composed frames for each particle family. Warm and arid classes do not become copies of the boreal snow field. Early wet or frost phases may gain local highlight before the soot jump, while every class darkens from black harvest through terminal winter. This is asset and source-wiring evidence without a live observation claim.

## User validation handoff

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

The full-screen grade and static accessibility registrations were removed because no approved GUI or player setting owned them. The ordinary-map entity and particle route remains the sole active regional presentation route. Live presentation checks belong to the user's later validation and are not a completion requirement for this static core-mechanics tranche.

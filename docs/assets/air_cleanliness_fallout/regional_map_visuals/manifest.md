# Air Winter Regional Ordinary-Map Visual Manifest

## Ownership and scope

Owner: Air Cleanliness Fallout / Air Winter.

Purpose: dedicated regional ordinary-map visual assets for the nine stable `air_winter_presentation_class` identities and six active `air_winter_phase` values.

Final art status: complete for the regional package.

Integration status: the synchronized five-slot state lifecycle is wired through the existing monthly state pass. It creates regional ground, two particle channels, dead vegetation, and mutually exclusive frozen-water or thaw entities with deterministic ids. The 2026-07-15 post-wire resolver, hash, DDS, state-ledger, and contact-sheet audit is recorded in `docs/plans/air_cleanliness_fallout_plans/AIR_WINTER_REGIONAL_VISUAL_WIRING_PROOF.md`. No full-screen grade window or static accessibility setting was added. Runtime behavior remains subject to that proof gate.

Asset provenance: all raster source plates were generated as fictional Air Winter imagery. The package does not reuse vanilla, zombie, disaster, or unrelated mod textures. Mesh geometry was authored procedurally in Blender for this package. The particle `.asset` structure follows documented Paradox/vanilla syntax, but its textures and registrations are dedicated Air Winter assets.

## Stable class enum

| Value | Class token | Ground entity pattern |
| ---: | --- | --- |
| 1 | `boreal_continental` | `air_winter_class_1_phase_<phase>_entity` |
| 2 | `temperate_maritime` | `air_winter_class_2_phase_<phase>_entity` |
| 3 | `mediterranean` | `air_winter_class_3_phase_<phase>_entity` |
| 4 | `desert_arid_plateau` | `air_winter_class_4_phase_<phase>_entity` |
| 5 | `tropical_coast_monsoon` | `air_winter_class_5_phase_<phase>_entity` |
| 6 | `equatorial_rainforest` | `air_winter_class_6_phase_<phase>_entity` |
| 7 | `mountain_highland` | `air_winter_class_7_phase_<phase>_entity` |
| 8 | `island_oceanic` | `air_winter_class_8_phase_<phase>_entity` |
| 9 | `polar_subpolar` | `air_winter_class_9_phase_<phase>_entity` |

The values mirror `common/script_constants/air_cleanliness_winter_constants.txt`. Value 0 is unclassified and has no visual entity.

## Stable phase enum

| Value | Phase token | Ground asset intent |
| ---: | --- | --- |
| 0 | `clear` | No Air Winter regional ground entity. |
| 1 | `dimming` | First frost or regional cold equivalent with light desaturation. |
| 2 | `crop_shock` | Failed-season cold, weakened ground, and region-fit precipitation. |
| 3 | `hard_freeze` | Persistent cold state and transport/water freeze cues. |
| 4 | `black_harvest` | Independent soot/dimming jump plus regional cold, without universal snow. |
| 5 | `ash_winter` | Heavy soot, dirty snow or warm-region ash/rain, dead vegetation. |
| 6 | `terminal_winter` | Strongest soot grade and severe class-specific cold presentation. |

## Runtime registration files

| File | Registered surface | Count |
| --- | --- | ---: |
| `gfx/entities/air_cleanliness_winter_regional_visuals.gfx` | `pdxmesh` registrations | 85 |
| `gfx/entities/air_cleanliness_winter_regional_visuals.asset` | Descriptive mesh entities plus numeric class/phase aliases | 166 |
| `gfx/particles/air_cleanliness_winter/*.asset` | Dedicated particle-file definitions | 9 |
| `gfx/entities/air_cleanliness_winter_regional_particles.gfx` | `pdxparticle` registrations | 9 |
| `gfx/entities/air_cleanliness_winter_regional_particles.asset` | Particle wrapper entities | 9 |
| `interface/air_cleanliness_winter_regional_visuals.gfx` | Grade and static-fallback sprites | 12 |

The 85 descriptive mesh entities comprise 54 phase plates, 27 regional props, and 4 static fallbacks. The 81 numeric aliases comprise 54 phase aliases and 27 prop aliases. Numeric aliases exist so a gameplay integration can select an entity with `meta_effect` using the stable integer class and phase values.

## Texture and mesh inventory

### Regional ground

For every class token and phases 1-6:

- mesh: `gfx/models/air_cleanliness_winter/regional/air_winter_<class>_phase_<phase>.mesh`
- diffuse: `gfx/models/air_cleanliness_winter/regional/air_winter_<class>_phase_<phase>_diff.dds`
- shared class normal: `gfx/models/air_cleanliness_winter/regional/air_winter_<class>_n.dds`
- shared class specular: `gfx/models/air_cleanliness_winter/regional/air_winter_<class>_spec.dds`

The phase meshes use `PdxMeshAdvanced`. Each is a low-profile irregular disc with 97 vertices and 96 polygons. The phase progression applies class-specific frost reach and independent phase-specific soot, dimming, and desaturation. Consequently, desert, tropical, and equatorial phases become cold/dim/sooty without automatically becoming snow fields.

### Regional props

For every class and each `dead_vegetation`, `frozen_water`, and `thaw_flood` family:

- mesh: `gfx/models/air_cleanliness_winter/regional/air_winter_<class>_<family>.mesh`
- material channels: matching `_diff.dds`, `_spec.dds`, and `_n.dds`
- descriptive entity: `air_winter_<class>_<family>_entity`
- numeric alias: `air_winter_class_<class_value>_<family>_entity`

These meshes use `PdxMeshAlphaBlend`. Dead vegetation uses three layered ground cards. Frozen water and thaw/flood use low-profile irregular discs. Thaw/flood is deliberately darker, wetter, and muddier than the frozen-water family.

### Particles

| Family | Atlas | Runtime severities | Wrapper entities |
| --- | --- | --- | --- |
| Snow/frost | `gfx/particles/air_cleanliness_winter/air_winter_snow_frost_atlas.dds` | mild, severe | `air_winter_snow_frost_mild_entity`, `air_winter_snow_frost_severe_entity` |
| Cold rain/mist | `gfx/particles/air_cleanliness_winter/air_winter_cold_rain_mist_atlas.dds` | mild, severe | `air_winter_cold_rain_mist_mild_entity`, `air_winter_cold_rain_mist_severe_entity` |
| Ash/dirty snow | `gfx/particles/air_cleanliness_winter/air_winter_ash_dirty_snow_atlas.dds` | mild, severe, terminal | `air_winter_ash_dirty_snow_mild_entity`, `air_winter_ash_dirty_snow_severe_entity`, `air_winter_ash_dirty_snow_terminal_entity` |
| Thaw/flood | `gfx/particles/air_cleanliness_winter/air_winter_thaw_flood_atlas.dds` | mild, severe | `air_winter_thaw_flood_mild_entity`, `air_winter_thaw_flood_severe_entity` |

Every atlas is 4x1 and contains four separately generated/authored visual states extracted from the approved 4x4 source plate. Each particle definition uses its dedicated atlas, alpha blending, finite lifetime, fade animation, velocity, and forces. No vanilla particle texture path appears in the final definitions.

### Static fallbacks

Each animated family has both:

- a normal-mapped mesh entity: `air_winter_static_<family>_entity`
- a registered sprite: `GFX_air_winter_regional_static_<family>`

The fallback uses the first authored frame, not a transform-only imitation of the animation. Final mesh material channels live under `gfx/models/air_cleanliness_winter/regional/`. Final sprite DDS files live under `gfx/interface/air_cleanliness_winter/regional_grades/`.

### Atmospheric grades

| State | Sprite |
| --- | --- |
| Phase 1-6 | `GFX_air_winter_regional_grade_phase_1` through `GFX_air_winter_regional_grade_phase_6` |
| Soot-thinning recovery | `GFX_air_winter_regional_grade_recovery_soot_thinning` |
| Ultraviolet-clear recovery | `GFX_air_winter_regional_grade_recovery_uv_clear` |

The grade textures are 512x512 RGBA DDS plates. The six phase plates increase coldness/darkness in distinct steps. They are registered only. Their non-blocking ordinary-map GUI parent, draw order, resolution behavior, click-through behavior, and mapmode interaction remain unproven.

## Source and processed inventory

Generated source plates:

- `source_png/materials/boreal_continental_detail_source.png`
- `source_png/materials/regional_material_atlas_source.png`
- `source_png/particles/regional_particle_frames_source.png`
- `source_png/props/dead_vegetation_atlas_source.png`
- `source_png/props/frozen_water_atlas_source.png`
- `source_png/grades/phase_grade_atlas_source.png`

The 16 separated particle source frames live under `source_png/particles/source_frames/<family>/`. All derived review PNGs live under `processed_png/`. Final engine DDS and mesh files live only in the runtime paths listed above.

## Conversion and export provenance

Raster conversion used Microsoft DirectXTex `texconv.exe`, version `2026.5.8.1` (DirectXTex May 2026). Executable SHA-256 at build time: `DCFDEC10244E02CF5037FBA089C55FB7E1326B1C8181742D77D15FA5CB5EEF06`. The executable was used from a temporary tool location and is not committed.

The build forced `TEXCONV_PATH` into `.tools/convert_to_dds.py`. The fallback converter path was not used. Final regional material/prop/static-mesh textures are 256x256. Particle atlases are 1024x256. Grade plates are 512x512. `build_report.json` records every final DDS width, height, byte count, and the source-image hashes.

Meshes were exported through Blender 5.1 and the installed PDX mesh exporter. `mesh_export_report.json` records 85 mesh hashes and exact material bindings: 54 `PdxMeshAdvanced` meshes and 31 `PdxMeshAlphaBlend` meshes. Text-form exports under `mesh_exports/` provide inspectable proof of diffuse, specular, normal, vertex, UV, and shader data. `source_blend/air_winter_regional_mesh_templates.blend` is the editable scene source.

## Evidence boundary

Proven offline:

- every required class/phase/family has a source, processed, and final asset
- engine registrations resolve to package-owned files
- mesh exports contain diffuse, specular, and normal material channels
- separately authored particle states exist as individual source-frame files
- static fallbacks exist for every animated family
- contact sheets show class fit and phase/recovery separation
- the five deterministic id ranges do not collide with another repository literal
- every gameplay entity token resolves to a dedicated registered asset
- gameplay refresh, schema migration, state reset, and deferred global cleanup use the existing monthly state pass

Not proven because HOI4 was not launched:

- ordinary-map placement, state centering, draw order, z height, and zoom thresholds
- particle appearance, atlas playback, culling, density, or performance in the engine
- GUI grade click-through, UI layering, mapmode coexistence, UI scale, and resolution behavior
- entity replacement, save-load reconstruction, multiplayer synchronization, and cleanup behavior in the engine
- world-scale cost when many states display multiple entities

These are integration/runtime proof obligations, not missing substitute art. No fallback asset, vanilla reuse, or simplified regional class was used.

# Air Winter Regional Particle Frame Plan

## Frame-by-frame content

| Family | Frame 1 | Frame 2 | Frame 3 | Frame 4 |
| --- | --- | --- | --- | --- |
| Snow/frost | Sparse crisp flakes and frost crystals with the clearest static silhouette. | Broader flakes and split crystal clusters. | Denser wind-torn flake groups and ice needles. | Mixed fine frost grains and larger flakes with a changed cluster pattern. |
| Cold rain/mist | Isolated cold droplets, thin streaks, and a small fog wisp. | Longer sleet-like streaks with changed bead spacing. | Denser rain diagonals and separate mist knots. | Broken droplets, suspended beads, and a wider low-cloud wisp. |
| Ash/dirty snow | Sparse soot flakes and dirty snow clumps form the static signal. | More angular ash fragments and changed clump silhouettes. | Dense mixed ash, dark specks, and granular snow. | Terminal-looking heavy fragments and broad contaminated clumps. |
| Thaw/flood | Clear droplets and a restrained ripple form the static recovery signal. | Changed splash crown and scattered melt beads. | Wider ripples, runoff fragments, and a distinct splash state. | Broken water arcs, droplets, and overlapping muddy ripples. |

Each cell changes internal content and silhouette. No frame is produced by repositioning the preceding frame.

## Processing plan

1. Crop the approved 4x4 source atlas into 16 independent 384x384 source-frame files.
2. Derive alpha from the black background and apply only the family palette needed for strategic-map readability.
3. Resize each processed frame to 256x256.
4. Pack the four family frames horizontally in authored order.
5. Convert the atlas with the approved DirectXTex path.
6. Export frame 1 separately as the static fallback.
7. Derive diffuse, normal, and specular channels for the static mesh fallback.
8. Build the contact sheets and GIF review previews.

Color/alpha processing does not create the animation. It prepares the independently authored source states for engine use.

## Runtime registration plan

| Family | Runtime atlas | Particle files | Wrapper entities |
| --- | --- | --- | --- |
| Snow/frost | `air_winter_snow_frost_atlas.dds` | `air_winter_snow_frost_mild.asset`, `air_winter_snow_frost_severe.asset` | `air_winter_snow_frost_mild_entity`, `air_winter_snow_frost_severe_entity` |
| Cold rain/mist | `air_winter_cold_rain_mist_atlas.dds` | `air_winter_cold_rain_mist_mild.asset`, `air_winter_cold_rain_mist_severe.asset` | `air_winter_cold_rain_mist_mild_entity`, `air_winter_cold_rain_mist_severe_entity` |
| Ash/dirty snow | `air_winter_ash_dirty_snow_atlas.dds` | mild, severe, and terminal `.asset` files | mild, severe, and terminal wrapper entities |
| Thaw/flood | `air_winter_thaw_flood_atlas.dds` | `air_winter_thaw_flood_mild.asset`, `air_winter_thaw_flood_severe.asset` | `air_winter_thaw_flood_mild_entity`, `air_winter_thaw_flood_severe_entity` |

Particle-file definitions live under `gfx/particles/air_cleanliness_winter/`. PDX particle registrations live in `gfx/entities/air_cleanliness_winter_regional_particles.gfx`. Wrapper entities live in `gfx/entities/air_cleanliness_winter_regional_particles.asset`.

## Static registration plan

| Family | Mesh entity | Sprite |
| --- | --- | --- |
| Snow/frost | `air_winter_static_snow_frost_entity` | `GFX_air_winter_regional_static_snow_frost` |
| Cold rain/mist | `air_winter_static_cold_rain_mist_entity` | `GFX_air_winter_regional_static_cold_rain_mist` |
| Ash/dirty snow | `air_winter_static_ash_dirty_snow_entity` | `GFX_air_winter_regional_static_ash_dirty_snow` |
| Thaw/flood | `air_winter_static_thaw_flood_entity` | `GFX_air_winter_regional_static_thaw_flood` |

Mesh registrations live in `gfx/entities/air_cleanliness_winter_regional_visuals.gfx` and `.asset`. Sprite registrations live in `interface/air_cleanliness_winter_regional_visuals.gfx`.

## Runtime proof still required

The package proves source-frame separation and offline asset construction. HOI4 still needs to prove atlas progression, particle size and density, fade, culling, z order, zoom behavior, multiple-family stacking, performance, and static replacement. Do not report those as passing based on GIF or Blender previews.

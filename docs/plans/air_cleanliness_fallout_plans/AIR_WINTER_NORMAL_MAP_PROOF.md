# Air Winter Normal-Map Proof Gate

Status: the documented normal-map entity route is proven for a one-state implementation. Runtime visual observation is outside this proof and is not claimed.

## Proof boundary

The first proof uses:

- state 64 as the single reviewed placement state
- entity id `8600064` as the single reserved proof slot
- `air_winter_normal_map_proof_entity` as a particle-only entity definition
- the vanilla light-snow particle as temporary proof material
- `air_winter_refresh_normal_map_proof_entity` as the idempotent lifecycle helper
- `min_zoom = 1100`, matching the approved Kaiserreich ambient-object precedent
- `air_winter_normal_map_grade_proof_gui` as a non-interactive cold-grade test
- `mapicons_container` as the unproven parent attachment intended to keep the grade on the map layer rather than over ordinary interface windows

This is not final climate art. It establishes the engine-supported route before dedicated snow, frost, rain, ash, vegetation, frozen-water, dim-light, and thaw assets are created.

## Runtime observation boundary

1. The entity appears at the state position on the ordinary political and terrain maps when state 64 has Air Winter phase 1 or higher.
2. It remains legible without hiding state borders, units, supply icons, or province selection.
3. The zoom threshold removes it before world-scale clutter becomes visible.
4. Repeated coordinator refreshes replace the same entity id instead of stacking particles.
5. Returning state 64 to phase 0 destroys the proof entity.
6. A save made while the entity is active reconstructs the same slot on the first resumed Air Winter coordinator pulse.
7. Other mapmodes and open windows remain readable.
8. The particle does not produce unwanted weather audio.
9. The cold grade covers the map at supported resolutions and UI scales.
10. The grade remains behind top bars, tabs, popups, and other ordinary interface windows.
11. Unit counters, state borders, map icons, and selection remain readable and clickable.
12. Hiding the proof condition removes the grade without leaving a stale interface layer.

## Engine limits preserved

- The entity is centered on the state. It does not conform to state borders.
- The effect does not change native weather, snow cover, terrain normals, vegetation, water shaders, or lighting.
- Runtime-created entity serialization is undocumented. Recovery is supplied by idempotent reconstruction on the existing coordinator pulse.
- The entity id range is not documented by the engine. The proof id is reserved by this package and must not be reused.
- `parent_window_window` is documented but explicitly marked as a surface that may not work. The `mapicons_container` attachment therefore remains a proof candidate, not an accepted implementation.
- The proof grade uses a hand-authored solid RGBA texture. It is not final cold, soot, or ultraviolet art.

## Promotion rule

The documented `create_entity` and `destroy_entity` route, the stable replacement id, the state scope, the existing monthly reconstruction call, and the approved Kaiserreich normal-mapped entity precedent are sufficient to begin final regional asset production. The temporary vanilla particle must be replaced by dedicated Air Winter asset families, the entity-id ledger must be expanded, and state presentation classes must be rolled out in reviewed regional batches. The twelve runtime observations above remain unobserved and cannot be reported as passing evidence.

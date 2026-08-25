# Event 020 humanoid rat Meshy handoff

## Outcome

The shared Event 020 rat model was regenerated as an oversized humanoid rat, rigged and animated through Meshy, converted through Blender/io_pdx_mesh, reimported, and installed. Both rat tags and every rat subtype continue to use one entity.

## Runtime files

- `gfx/models/units/020_black_plague_rat/black_plague_rat.mesh`
- `gfx/models/units/020_black_plague_rat/black_plague_rat_{idle,move,attack,defend,support_attack,retreat,training,death}.anim`
- `gfx/models/units/020_black_plague_rat/black_plague_rat_{diff,n,spec}.dds`
- `gfx/models/units/020_black_plague_rat/animation_020_black_plague_rat.asset`
- `gfx/entities/020_black_plague_rat.gfx`
- `gfx/entities/020_black_plague_rat.asset`

## Evidence

The mesh is 29,999 triangles, uses one 24-bone Meshy rig, has no unweighted vertices and no vertex above four influences, is grounded at source Z `0`, and renders at `1.6875×` vanilla infantry height after entity scale. All eight actions are distinct Meshy motions at 24 FPS and were visually reviewed at multiple phases. The actual `.mesh` and every `.anim` were reimported through io_pdx_mesh; proof blends are `blender/checkpoints/reimport_humanoid_<role>.blend`.

The reference, provider tasks, hashes, frame ranges, PDX texture packing, sound/counter status, and runtime hashes are recorded in `docs/assets/020_black_plague/models_3d/rat_ground_unit_shared/manifest.md`.

## Remaining boundary

Live Hearts of Iron IV consumer validation is user-owned and was not performed. There is no model-production or runtime-wiring blocker.

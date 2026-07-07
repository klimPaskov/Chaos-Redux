# Chaos Redux Integration TODO

Use this reference only when the user asks to continue from Blender modeling toward exported PDX assets or Chaos Redux in-game wiring. Treat this section as a TODO workflow until it has been implemented and validated in a real game session.

## Asset Export TODO

Research and verify against current vanilla files before implementing:

- Export `.mesh` with the PDX Blender add-on.
- Export or reuse `.anim` files only when skeleton compatibility is proven.
- Create or bake texture maps as game-ready files, likely `.dds` for diffuse/normal/specular as required by the material/shader path.
- Keep source `.blend`, generated concept art, texture sources, and exported runtime files in separate, documented folders.

Suggested Chaos Redux structure to verify before use:

```text
gfx/models/units/chaos_redux/<model_id>/
gfx/entities/chaos_redux_<model_id>.gfx
gfx/entities/chaos_redux_<model_id>.asset
docs/assets/<model_id>_model_manifest.md
```

Do not invent final paths if the mod already has a model/entity convention. Inspect existing Chaos Redux and vanilla files first.

## Vanilla Wiring References

Consult vanilla examples:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/animation.asset`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/*.gfx`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/entities/*.asset`

Useful in-game/debug documentation found in vanilla docs:

- `debug_unit_entity` prints entity hierarchy.
- `debug_army_entity` shows debug entities for armies.
- `reload_textures` reloads textures by optional filter.
- `create_entity`, `set_entity_animation`, `set_entity_position`, `set_entity_rotation`, and `set_entity_scale` are documented in `effects_documentation.md`.

## Animation TODO

Future animation work should be a separate explicit phase:

- Confirm whether the zombie rig can reuse vanilla infantry animations without distortion.
- Import representative vanilla `.anim` files and test idle/move/death poses on the zombie rig.
- If vanilla animation compatibility fails, create custom idle/move/death animations with the PDX animation exporter.
- Keep `chk_bonespace=False` unless intentionally creating a fully custom animation set.
- Validate root motion, foot grounding, hand/claw placement, and loop seams.

## Chaos Redux Wiring TODO

When turning the model into an in-game unit:

- Create or update entity definitions for the exported mesh.
- Reference animation ids and default states from a known-good vanilla pattern.
- Wire the entity into the intended unit/equipment/country/event surface.
- Add localisation only for player-facing names/tooltips if the model appears in UI.
- Document every runtime asset and source asset in a manifest.
- Include validation notes: game load, entity debug visibility, animation states checked, texture reload checked, and any missing animations or placeholder assets.

Do not claim in-game completion until the exported model is visible in-game with correct scale, orientation, textures, and animations or documented static behavior.

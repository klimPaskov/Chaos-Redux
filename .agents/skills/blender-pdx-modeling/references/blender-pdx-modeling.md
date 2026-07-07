# Blender PDX Modeling

Use this reference when creating a PDX/HOI4-style model through Blender MCP.

## Tool Discovery

If Blender MCP tools are not already loaded, search for Blender tools with `tool_search`. Verify scene access before editing.

Check the PDX add-on before relying on it:

```python
import addon_utils, bpy
addons = []
for mod in addon_utils.modules():
    name = getattr(mod, "__name__", "")
    bl_info = getattr(mod, "bl_info", {}) or {}
    label = bl_info.get("name", "")
    if "pdx" in (name + " " + label).lower() or "paradox" in (name + " " + label).lower():
        addons.append((name, label, name in bpy.context.preferences.addons))
```

Expected installed add-on in this environment: `IO PDX Mesh`, module similar to `bl_ext.user_default.io_pdx_mesh`.

Useful operators:

- `bpy.ops.io_pdx_mesh.import_mesh(filepath=..., chk_mesh=True, chk_skel=True, chk_locs=True, chk_joinmats=True, chk_bonespace=False)`
- `bpy.ops.io_pdx_mesh.import_anim(filepath=..., int_start=1)`
- `bpy.ops.io_pdx_mesh.export_mesh(filepath=..., chk_mesh=True, chk_skel=True, chk_locs=True, chk_selected=True)`
- `bpy.ops.io_pdx_mesh.export_anim(filepath=..., chk_selected=True)` when animation work is later implemented

Do not set `chk_bonespace=True` when preserving vanilla animation compatibility. The add-on warning says bone orientation conversion breaks existing animations unless the model will be fully reanimated.

## Vanilla Reference

Prefer this vanilla infantry reference unless the user requests a different class:

```text
C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/models/units/ENG_infantry.mesh
```

Import with mesh, skeleton, and locators enabled. Keep the result visible as ghost/wire reference.

Measure these from the imported scene:

- World bounds for all imported mesh objects.
- Ground/origin convention: feet should sit on the same ground plane as the reference.
- Armature object name and bone count.
- First/root bone. The exporter traverses from `rig.data.bones[0]`.
- Bone hierarchy and names, especially `Root`, `Hip`, `back_mid`, `head`, limb bones, hands, and foot/toe bones.
- Facing direction. For imported HOI4 infantry, compare `back_mid` and `mid_back_node`; the side containing `mid_back_node` is the back. The front is the opposite direction.

Observed sanity check from `ENG_infantry.mesh` in this environment: imported bounds were about `5.45 x 1.78 x 7.67` Blender units and the front direction inferred as `-Y`. Treat this only as a sanity check; always remeasure.

## Real 3D Modeling Standards

The final model must be inspectable from front, side, back, top, and angled views.

Acceptable geometry:

- Sculpted mesh objects, joined mesh parts, bevelled primitives, curves converted to mesh, metaballs converted to mesh, or manually created mesh topology.
- Separate accessory meshes for straps, pouches, helmets, boots, exposed bones, claws, and cloth tears.
- Material slots and texture maps on real mesh surfaces.

Unacceptable as final model:

- Flat image plane.
- Billboard/card/sprite.
- Alpha cutout.
- Extruded silhouette from a PNG.
- Single front-facing textured shell.
- Primitive stick figure without modeled body volume.

Use imagegen output only as visual reference. It may sit off to the side as a hidden or non-rendered reference plane, but it must not be the model.

## Armature and Export Requirements

The PDX Blender exporter expects skinned mesh data to resolve through armature modifiers and vertex groups:

- A mesh should have one armature modifier referencing the export rig.
- Vertex group names must match bone names.
- Bone hierarchy is collected from the first bone of the armature and recursively traversed.
- Ignored bones may be skipped by add-on metadata; do not invent ignore flags unless intentionally controlling export.
- Export only selected model/rig/locators when using `chk_selected=True`.

For a replacement unit that should reuse vanilla animations, preserve bone names, hierarchy, rest pose compatibility, and scale as closely as possible. If the skeleton changes substantially, treat animation reuse as unsafe and record that the model needs custom animations.

## Validation Checklist

Before reporting completion:

- Vanilla reference remains visible and was used for measured scale/facing/origin.
- Final model object is not flat and has side/back volume.
- Root bone and main hierarchy exist.
- Meshes have armature modifiers and vertex groups.
- Materials are assigned to actual geometry.
- Cameras/lights exist for inspection.
- Front and side renders or viewport checks were inspected.
- Hidden helper image planes are not counted as the final model.

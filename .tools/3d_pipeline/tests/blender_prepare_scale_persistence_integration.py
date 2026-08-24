"""Synthetic FBX proof that humanoid normalization survives save and PDX export."""

from __future__ import annotations

import json
import math
import sys
import tempfile
from pathlib import Path

import bpy


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import blender_worker  # noqa: E402


TARGET_HEIGHT = 7.3518242835
SOURCE_HEIGHT = 1.6488708258


def reset_scene() -> None:
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for action in list(bpy.data.actions):
        bpy.data.actions.remove(action)


def make_provider_fbx(path: Path) -> None:
    reset_scene()
    armature_data = bpy.data.armatures.new("ProviderArmatureData")
    rig = bpy.data.objects.new("ProviderArmature", armature_data)
    bpy.context.scene.collection.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    hips = armature_data.edit_bones.new("Hips")
    hips.head = (0.0, 0.0, 0.0)
    hips.tail = (0.0, 0.0, 100.0)
    accessory_bone = armature_data.edit_bones.new("Accessory")
    accessory_bone.head = (0.0, 0.0, 100.0)
    accessory_bone.tail = (0.0, 0.0, 140.0)
    accessory_bone.parent = hips
    bpy.ops.object.mode_set(mode="OBJECT")
    rig.scale = (0.01, 0.01, 0.01)

    mesh_data = bpy.data.meshes.new("ProviderMeshData")
    local_height = SOURCE_HEIGHT / 0.01
    mesh_data.from_pydata(
        [
            (-20.0, -10.0, 0.0),
            (20.0, -10.0, 0.0),
            (20.0, 10.0, local_height),
            (-20.0, 10.0, local_height),
        ],
        [],
        [(0, 1, 2, 3)],
    )
    mesh = bpy.data.objects.new("ProviderMesh", mesh_data)
    bpy.context.scene.collection.objects.link(mesh)
    mesh.parent = rig
    mesh.matrix_parent_inverse = rig.matrix_world.inverted()
    mesh["preserve_marker"] = "mesh"
    modifier = mesh.modifiers.new("ProviderArmature", "ARMATURE")
    modifier.object = rig
    group = mesh.vertex_groups.new(name="Hips")
    group.add([0, 1, 2, 3], 1.0, "REPLACE")
    material = bpy.data.materials.new("ProviderMaterial")
    material.use_nodes = True
    mesh.data.materials.append(material)

    accessory_data = bpy.data.meshes.new("AccessoryData")
    accessory_data.from_pydata([(0.0, 0.0, 20.0), (5.0, 0.0, 20.0), (0.0, 5.0, 20.0)], [], [(0, 1, 2)])
    accessory = bpy.data.objects.new("AccessoryMesh", accessory_data)
    bpy.context.scene.collection.objects.link(accessory)
    accessory.parent = rig
    accessory.parent_type = "BONE"
    accessory.parent_bone = "Accessory"
    accessory["preserve_marker"] = "accessory"

    action = bpy.data.actions.new("ProviderScaleAction")
    rig.animation_data_create()
    rig.animation_data.action = action
    for frame in (1, 2):
        rig.scale = (0.01, 0.01, 0.01)
        rig.keyframe_insert("scale", frame=frame)
        pose_hips = rig.pose.bones["Hips"]
        pose_hips.scale = (1.0, 1.0, 1.0)
        pose_hips.keyframe_insert("scale", frame=frame, group="Hips")
        pose_hips.rotation_mode = "QUATERNION"
        angle = 0.1 if frame == 2 else 0.0
        pose_hips.rotation_quaternion = (math.cos(angle / 2), math.sin(angle / 2), 0.0, 0.0)
        pose_hips.keyframe_insert("rotation_quaternion", frame=frame, group="Hips")

    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 2
    bpy.ops.object.select_all(action="SELECT")
    bpy.context.view_layer.objects.active = rig
    bpy.ops.export_scene.fbx(
        filepath=str(path),
        use_selection=True,
        object_types={"ARMATURE", "MESH"},
        apply_unit_scale=False,
        apply_scale_options="FBX_SCALE_NONE",
        add_leaf_bones=False,
        bake_anim=True,
        bake_anim_use_all_actions=False,
        bake_anim_use_nla_strips=False,
        bake_anim_force_startend_keying=True,
        bake_anim_simplify_factor=0.0,
    )


def main() -> None:
    config = json.loads((PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json").read_text(encoding="utf-8"))
    io_pdx_root = str(config["io_pdx_mesh_root"])
    with tempfile.TemporaryDirectory(prefix="chaosx_prepare_scale_persistence_") as temporary:
        job = Path(temporary)
        source = job / "provider" / "downloads" / "provider.fbx"
        source.parent.mkdir(parents=True)
        (job / "blender" / "reports").mkdir(parents=True)
        make_provider_fbx(source)
        pdx = blender_worker.load_pdx(io_pdx_root)
        result = blender_worker.prepare(
            {
                "job_root": str(job),
                "io_pdx_root": io_pdx_root,
                "payload": {
                    "source_rel": "provider/downloads/provider.fbx",
                    "asset_kind": "humanoid_unit",
                    "target_height_m": TARGET_HEIGHT,
                    "runtime_entity_scale": 0.8,
                    "runtime_stem": "synthetic_humanoid",
                    "target_triangles": 0,
                    "excluded_provider_objects": [],
                    "vanilla_reference": {},
                    "texture_source_rels": {},
                    "preserve_geometry_topology": True,
                    "render_previews": False,
                },
            },
            pdx,
        )
        assert result["asset_kind"] == "humanoid_unit"
        assert math.isclose(result["imported_geometry"]["dimensions"][2], SOURCE_HEIGHT, abs_tol=2e-4)
        assert math.isclose(result["normalization"]["scale_factor"], TARGET_HEIGHT / SOURCE_HEIGHT, rel_tol=2e-4)
        assert math.isclose(result["geometry"]["dimensions"][2], TARGET_HEIGHT, abs_tol=2e-4)
        persistence = result["normalization_persistence"]
        assert math.isclose(persistence["persisted_height_m"], TARGET_HEIGHT, abs_tol=2e-4)
        assert persistence["policy"] == "save_reopen_and_remeasure_working_world_bounds"
        assert persistence["armatures"]
        scale_cleanup = result["rig_and_actions"]["scale_sanitization"]
        assert scale_cleanup["remaining_scale_fcurves"] == 0
        assert any(
            "scale" in record["removed_paths"]
            for record in scale_cleanup["actions"]
        )
        rig = blender_worker.armatures()[0]
        mesh = next(obj for obj in blender_worker.mesh_objects() if obj.name.startswith("ProviderMesh"))
        accessory = next(obj for obj in blender_worker.mesh_objects() if obj.name.startswith("AccessoryMesh"))
        expected_rig_scale = 0.01 * TARGET_HEIGHT / SOURCE_HEIGHT
        assert all(math.isclose(component, expected_rig_scale, rel_tol=2e-4) for component in rig.matrix_world.to_scale())
        assert mesh.parent is rig
        assert mesh.modifiers[0].object is rig
        assert accessory.parent is rig
        assert accessory.parent_type == "BONE"
        assert accessory.parent_bone == "Accessory"
        assert len(mesh.vertex_groups) == 1
        assert bpy.data.actions
        assert all(
            "scale" not in fcurve.data_path.casefold()
            for action in bpy.data.actions
            for fcurve, _ in blender_worker.action_fcurves(action)
            if action.name.endswith("_WORKING")
        )

        mesh_output = job / "export" / "mesh" / "synthetic.mesh"
        export = blender_worker.export_mesh(
            {
                "job_root": str(job),
                "io_pdx_root": io_pdx_root,
                "payload": {
                    "blend_rel": "blender/checkpoints/05_pre_export.blend",
                    "output_rel": "export/mesh/synthetic.mesh",
                    "split_verts": False,
                },
            },
            pdx,
        )
        assert mesh_output.is_file()
        assert all(math.isclose(component, 1.0, abs_tol=1e-6) for component in export["export_transforms"]["armature_world_scale_after"])
        reset_scene()
        pdx["import_meshfile"](
            str(mesh_output),
            imp_mesh=True,
            imp_skel=True,
            imp_locs=True,
            join_materials=True,
            bonespace=False,
        )
        reimported_minimum, reimported_maximum = blender_worker.world_bounds(blender_worker.mesh_objects(False))
        reimported_height = float((reimported_maximum - reimported_minimum).z)
        assert math.isclose(reimported_height, TARGET_HEIGHT, abs_tol=2e-3), reimported_height
        assert len(blender_worker.armatures(False)) == 1
        print(json.dumps({"status": "pass", "persisted_height": round(persistence["persisted_height_m"], 6), "reimported_height": round(reimported_height, 6)}, sort_keys=True))


if __name__ == "__main__":
    main()

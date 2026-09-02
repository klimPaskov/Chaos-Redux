"""Disposable native-Blender locator regression; never a production asset proof.

Run only after parent review and the approved adapter 1.10.15 lock refresh.
This fixture creates its own tiny mesh/rig/action in a temporary directory and
round-trips actual io_pdx_mesh bytes; no production checkpoint is opened.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
import tempfile
import tomllib
from pathlib import Path

import bpy
from mathutils import Matrix, Quaternion, Vector


PIPELINE_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PIPELINE_ROOT.parents[1]
sys.path.insert(0, str(PIPELINE_ROOT / "adapter"))

import blender_worker  # noqa: E402


RIG_NAME = "FixtureRig"
ROOT_BONE = "fixture_root"
PARENT_BONE = "fixture_weapon_bone"
LOCATOR_NAME = "fixture_muzzle"
ACTION_NAME = "fixture_pose_action"
FRAMES = (1, 6, 12)
RIG_SCALE = 1.75
LOCAL_POSITION = (0.25, -0.4, 0.8)
AUTHOR_TOLERANCE = 1e-5
ROUNDTRIP_TOLERANCE = 2e-4
INSTALLED_EXPORTER_SHA256 = "FCBE2EDFC6C24A72450CB1F398C88EDCAA970556B1448224DCE4074A961A2799"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def verified_environment() -> tuple[dict, dict]:
    """Fail before fixture creation if the parent-owned production lock is stale."""
    config = json.loads((PIPELINE_ROOT / "config/blender_hoi4_adapter.json").read_text(encoding="utf-8"))
    lock = json.loads((PIPELINE_ROOT / "config/dependencies.lock.json").read_text(encoding="utf-8"))
    routes = lock["routes"]
    adapter = routes["blender_hoi4_adapter"]
    assert config["adapter_version"] == adapter["version"] == "1.10.15", "Review/version/lock gate is not complete"
    assert config["operations"] == adapter["operations"]
    assert adapter["operations"].count("author_locator") == 1
    for relative, expected in adapter["source_sha256"].items():
        assert digest(REPO_ROOT / relative) == expected.upper(), f"Locked raw-byte source mismatch: {relative}"
    assert bpy.app.version_string == routes["blender"]["version"]
    assert bpy.app.build_hash.decode() == routes["blender"]["build_commit"]
    addon = Path(config["io_pdx_mesh_root"])
    manifest = tomllib.loads((addon / "blender_manifest.toml").read_text(encoding="utf-8"))
    assert manifest["version"] == routes["io_pdx_mesh"]["version"] == "0.91.0"
    assert digest(addon / "pdx_blender/blender_import_export.py") == INSTALLED_EXPORTER_SHA256
    return config, routes


def reset_fixture_scene() -> None:
    if bpy.context.object and bpy.context.object.mode != "OBJECT":
        bpy.ops.object.mode_set(mode="OBJECT")
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    for blocks in (bpy.data.meshes, bpy.data.armatures, bpy.data.materials, bpy.data.images, bpy.data.actions):
        for block in list(blocks):
            blocks.remove(block)


def matrix_rows(matrix: Matrix) -> list[list[float]]:
    return [[float(value) for value in row] for row in matrix]


def matrix_error(actual: Matrix, expected: Matrix) -> float:
    return max(abs(actual[row][col] - expected[row][col]) for row in range(4) for col in range(4))


def assert_matrix(actual: Matrix, expected: Matrix, tolerance: float, label: str) -> float:
    error = matrix_error(actual, expected)
    assert math.isfinite(error) and error <= tolerance, f"{label}: max matrix error {error} > {tolerance}"
    return error


def actual_bone_local(locator: bpy.types.Object) -> Matrix:
    rig = locator.parent
    bone = rig.data.bones[locator.parent_bone]
    bone_matrix = bone.matrix_local if rig.data.pose_position == "REST" else rig.pose.bones[bone.name].matrix
    return (rig.matrix_world @ bone_matrix).inverted() @ locator.matrix_world


def create_fixture(job: Path) -> Quaternion:
    reset_fixture_scene()
    rig_data = bpy.data.armatures.new("FixtureRigData")
    rig = bpy.data.objects.new(RIG_NAME, rig_data)
    bpy.context.scene.collection.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    root = rig_data.edit_bones.new(ROOT_BONE)
    root.head, root.tail = (0.0, 0.0, 0.0), (0.2, 0.3, 1.0)
    parent = rig_data.edit_bones.new(PARENT_BONE)
    parent.head, parent.tail = root.tail, (1.1, 1.5, 1.6)
    parent.parent, parent.use_connect, parent.roll = root, True, 0.37
    bpy.ops.object.mode_set(mode="OBJECT")
    # The installed 0.91.0 exporter unconditionally includes its first root.
    rig.data.bones[ROOT_BONE]["pdxIgnoreJoint"] = True
    rig["chaosx_working"] = True
    rig.scale = (RIG_SCALE,) * 3

    mesh = bpy.data.meshes.new("FixtureBodyData")
    mesh.from_pydata(
        [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)],
        [], [(0, 2, 1), (0, 1, 3), (1, 2, 3), (2, 0, 3)],
    )
    mesh.update()
    body = bpy.data.objects.new("FixtureBody", mesh)
    bpy.context.scene.collection.objects.link(body)
    body["chaosx_working"] = True
    modifier = body.modifiers.new("FixtureSkin", "ARMATURE")
    modifier.object = rig
    body.vertex_groups.new(name=PARENT_BONE).add(list(range(4)), 1.0, "REPLACE")
    uv = mesh.uv_layers.new(name="FixtureUV")
    for polygon in mesh.polygons:
        for loop_index, value in zip(polygon.loop_indices, ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))):
            uv.data[loop_index].uv = value
    material = bpy.data.materials.new("FixtureMaterial")
    material.use_nodes = True
    material["shader"] = "PdxMeshAdvanced"
    mesh.materials.append(material)
    image = bpy.data.images.new("FixtureDiffuse", width=2, height=2, alpha=True)
    image.generated_color = (0.2, 0.4, 0.6, 1.0)
    image.filepath_raw = str(job / "export/mesh/fixture_diffuse.png")
    image.file_format = "PNG"
    image.save()
    texture = material.node_tree.nodes.new("ShaderNodeTexImage")
    texture.name, texture.image = "FixtureTexture", image
    principled = material.node_tree.nodes.get("Principled BSDF")
    principled.inputs["Metallic"].default_value = 0.37
    principled.inputs["Roughness"].default_value = 0.61
    material.node_tree.links.new(texture.outputs["Color"], principled.inputs["Base Color"])

    action = bpy.data.actions.new(ACTION_NAME)
    action.use_fake_user = True
    rig.animation_data_create()
    rig.animation_data.action = action
    for frame, angle, root_height in ((1, -0.25, 0.0), (6, 0.65, 0.025), (12, -0.1, 0.0)):
        for pose_bone in rig.pose.bones:
            pose_bone.rotation_mode = "QUATERNION"
            pose_bone.rotation_quaternion = Quaternion(Vector((0.3, 0.7, 0.2)).normalized(), angle) if pose_bone.name == PARENT_BONE else Quaternion()
            pose_bone.location = (0.0, 0.0, root_height if pose_bone.name == ROOT_BONE else 0.0)
            pose_bone.scale = (1.0, 1.0, 1.0)
            for channel in ("location", "rotation_quaternion", "scale"):
                pose_bone.keyframe_insert(data_path=channel, frame=frame)
    for curve, _ in blender_worker.action_fcurves(action):
        for key in curve.keyframe_points:
            key.interpolation = "LINEAR"
    decoy = bpy.data.objects.new("unregistered_decoy", None)
    bpy.context.scene.collection.objects.link(decoy)
    decoy.location = (5.0, 6.0, 7.0)
    bpy.context.scene.render.fps = 30
    bpy.context.scene.frame_start, bpy.context.scene.frame_end = FRAMES[0], FRAMES[-1]
    bpy.context.scene.frame_set(6)
    bpy.context.view_layer.update()
    return Quaternion(Vector((0.3, 0.4, 0.5)).normalized(), 0.7)


def invariant_snapshot() -> dict:
    body, rig = bpy.data.objects["FixtureBody"], bpy.data.objects[RIG_NAME]
    material = body.data.materials[0]
    principled = material.node_tree.nodes.get("Principled BSDF")
    return {
        "objects_without_locator": sorted(obj.name for obj in bpy.data.objects if obj.name != LOCATOR_NAME),
        "vertices": [tuple(vertex.co) for vertex in body.data.vertices],
        "edges": [tuple(edge.vertices) for edge in body.data.edges],
        "polygons": [tuple(polygon.vertices) for polygon in body.data.polygons],
        "uvs": [tuple(loop.uv) for layer in body.data.uv_layers for loop in layer.data],
        "weights": [[(group.group, group.weight) for group in vertex.groups] for vertex in body.data.vertices],
        "groups": [group.name for group in body.vertex_groups],
        "modifiers": [(modifier.name, modifier.type, modifier.object.name) for modifier in body.modifiers],
        "body_world": matrix_rows(body.matrix_world),
        "rig_world": matrix_rows(rig.matrix_world),
        "rig_scale": tuple(rig.scale),
        "rig_pose_position": rig.data.pose_position,
        "bones": [(bone.name, bone.parent.name if bone.parent else None, matrix_rows(bone.matrix_local), bone.get("pdxIgnoreJoint")) for bone in rig.data.bones],
        "poses": [(bone.name, matrix_rows(bone.matrix)) for bone in rig.pose.bones],
        "material_slots": [slot.material.name for slot in body.material_slots],
        "shader": material["shader"],
        "nodes": sorted((node.name, node.bl_idname) for node in material.node_tree.nodes),
        "links": sorted((link.from_node.name, link.from_socket.name, link.to_node.name, link.to_socket.name) for link in material.node_tree.links),
        "images": [(image.name, image.filepath, tuple(image.size)) for image in bpy.data.images],
        "material_values": [principled.inputs[name].default_value for name in ("Metallic", "Roughness")],
        "actions": {action.name: {"fake_user": action.use_fake_user, "keys": blender_worker._export_checkpoint_action_snapshot(action)} for action in bpy.data.actions},
        "active_action": rig.animation_data.action.name,
        "frame": bpy.context.scene.frame_current,
        "decoy_world": matrix_rows(bpy.data.objects["unregistered_decoy"].matrix_world),
    }


def sample_follow(local: Matrix, tolerance: float) -> dict[int, list[list[float]]]:
    locator = bpy.data.objects[LOCATOR_NAME]
    assert locator.type == "EMPTY" and locator.data is None
    assert locator.parent.type == "ARMATURE" and locator.parent_type == "BONE" and locator.parent_bone == PARENT_BONE
    samples = {}
    for frame in FRAMES:
        bpy.context.scene.frame_set(frame)
        bpy.context.view_layer.update()
        assert_matrix(actual_bone_local(locator), local, tolerance, f"bone local at frame {frame}")
        expected_world = locator.parent.matrix_world @ locator.parent.pose.bones[PARENT_BONE].matrix @ local
        assert_matrix(locator.matrix_world, expected_world, tolerance, f"pose follow at frame {frame}")
        record = blender_worker.locator_records([locator])[0]
        assert record["parent_bone"] == PARENT_BONE and record["frame"] == frame
        assert_matrix(Matrix(record["bone_local_matrix"]), local, tolerance, f"reported local at frame {frame}")
        assert_matrix(Matrix(record["matrix_world"]), locator.matrix_world, tolerance, f"reported world at frame {frame}")
        samples[frame] = matrix_rows(locator.matrix_world)
    assert matrix_error(Matrix(samples[1]), Matrix(samples[6])) > 0.05, "Fixture did not exercise a moving pose"
    return samples


def main() -> None:
    config, routes = verified_environment()
    with tempfile.TemporaryDirectory(prefix="chaosx_locator_fixture_") as directory:
        job = Path(directory).resolve()
        for relative in ("blender/checkpoints", "blender/reports", "export/mesh", "export/anim"):
            (job / relative).mkdir(parents=True)
        rotation = create_fixture(job)
        local = Matrix.Translation(LOCAL_POSITION) @ rotation.to_matrix().to_4x4()
        source = job / "blender/checkpoints/source.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(source))
        bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
        before, source_hash = invariant_snapshot(), digest(source)
        req = {"job_id": "locator_fixture", "job_root": str(job), "io_pdx_root": config["io_pdx_mesh_root"]}
        author = blender_worker.author_locator({**req, "payload": {
            "blend_rel": "blender/checkpoints/source.blend",
            "checkpoint_rel": "blender/checkpoints/authored.blend",
            "target_armature_name": RIG_NAME, "parent_bone": PARENT_BONE, "locator_name": LOCATOR_NAME,
            "bone_local_position": list(LOCAL_POSITION),
            "bone_local_rotation_xyzw": [rotation.x, rotation.y, rotation.z, rotation.w],
        }})
        assert author["created"] and author["actions_verified_unchanged"] == [ACTION_NAME]
        assert author["locator"]["parent_bone"] == PARENT_BONE
        assert_matrix(Matrix(author["locator"]["bone_local_matrix"]), local, AUTHOR_TOLERANCE, "author report local")
        assert digest(source) == source_hash == author["source_sha256"]
        authored = job / author["checkpoint"]
        assert digest(authored) == author["checkpoint_sha256"]
        bpy.ops.wm.open_mainfile(filepath=str(authored), use_scripts=False)
        assert invariant_snapshot() == before, "Locator author/save/reopen changed mesh/material/weights/rig/action/scale"
        authored_samples = sample_follow(local, AUTHOR_TOLERANCE)

        pdx = blender_worker.load_pdx(req["io_pdx_root"])
        from io_pdx_mesh.pdx_blender.blender_import_export import get_skeleton_hierarchy
        from io_pdx_mesh import pdx_data
        assert [bone.name for bone in get_skeleton_hierarchy(bpy.data.objects[RIG_NAME])] == [ROOT_BONE, PARENT_BONE]
        mesh_report = blender_worker.export_mesh({**req, "payload": {
            "blend_rel": author["checkpoint"], "output_rel": "export/mesh/fixture.mesh",
        }}, pdx)
        assert mesh_report["selected_export_objects"] == ["FixtureBody", LOCATOR_NAME]
        assert bpy.data.objects[RIG_NAME].data.pose_position == "POSE", "REST state was not restored"
        assert len(mesh_report["locators"]) == 1 and mesh_report["locators"][0]["parent_bone"] == PARENT_BONE
        scaled_local = local.copy()
        scaled_local.translation *= RIG_SCALE
        assert_matrix(Matrix(mesh_report["locators"][0]["bone_local_matrix"]), scaled_local, AUTHOR_TOLERANCE, "serialized local")
        exported = job / mesh_report["exported_checkpoint"]
        bpy.ops.wm.open_mainfile(filepath=str(exported), use_scripts=False)
        assert_matrix(bpy.data.objects[RIG_NAME].matrix_world, Matrix.Identity(4), AUTHOR_TOLERANCE, "normalized rig scale")
        normalized_samples = sample_follow(scaled_local, AUTHOR_TOLERANCE)
        anim_report = blender_worker.export_animation({**req, "payload": {
            "blend_rel": mesh_report["exported_checkpoint"], "action_name": ACTION_NAME,
            "output_rel": "export/anim/fixture.anim",
        }}, pdx)
        mesh_path, anim_path = job / mesh_report["mesh"], job / anim_report["anim"]
        assert mesh_path.stat().st_size > 0 and anim_path.stat().st_size > 0
        raw_locators = pdx_data.read_meshfile(str(mesh_path)).find("locator")
        assert raw_locators is not None and [node.tag for node in raw_locators] == [LOCATOR_NAME]
        assert raw_locators[0].attrib["pa"] == [PARENT_BONE]
        hashes = {"source_blend": source_hash, "authored_blend": digest(authored), "mesh": digest(mesh_path), "anim": digest(anim_path)}

        reset_fixture_scene()
        pdx["import_meshfile"](str(mesh_path), imp_mesh=True, imp_skel=True, imp_locs=True, join_materials=True, bonespace=False)
        assert "unregistered_decoy" not in bpy.data.objects
        locators = [obj for obj in bpy.context.scene.objects if obj.type == "EMPTY"]
        assert len(locators) == 1 and locators[0].name == LOCATOR_NAME
        assert not locators[0].get("chaosx_export_locator", False), "PDX reimport unexpectedly retained private registry metadata"
        assert_matrix(actual_bone_local(locators[0]), scaled_local, ROUNDTRIP_TOLERANCE, "actual mesh bytes local")
        imported_meshes = [obj for obj in bpy.context.scene.objects if obj.type == "MESH"]
        assert len(imported_meshes) == 1 and len(imported_meshes[0].data.polygons) == 4
        assert imported_meshes[0].data.materials[0]["shader"] == "PdxMeshAdvanced"
        pdx["import_animfile"](str(anim_path), frame_start=1)
        assert locators[0].parent.animation_data.action is not None
        reimported_samples = sample_follow(scaled_local, ROUNDTRIP_TOLERANCE)
        errors = {frame: assert_matrix(Matrix(reimported_samples[frame]), Matrix(normalized_samples[frame]), ROUNDTRIP_TOLERANCE, f"actual animation bytes world at frame {frame}") for frame in FRAMES}
        print(json.dumps({
            "status": "pass", "fixture_only": True, "production_asset_acceptance": False,
            "blender_version": bpy.app.version_string, "adapter_version": routes["blender_hoi4_adapter"]["version"],
            "io_pdx_mesh_version": routes["io_pdx_mesh"]["version"], "parent_bone": PARENT_BONE,
            "author_invariants_preserved": True, "root_own_ignore_flag_included": True,
            "selected_objects": mesh_report["selected_export_objects"], "source_samples": authored_samples,
            "reimport_world_errors": errors, "hashes": hashes,
        }, sort_keys=True))
        # Leave no test data-blocks or file handles pointing into the disposable directory.
        reset_fixture_scene()


if __name__ == "__main__":
    main()

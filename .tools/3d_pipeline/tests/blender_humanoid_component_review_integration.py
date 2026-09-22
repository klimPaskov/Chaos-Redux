"""Disposable native component-review and action-channel inventory proof; never opens a production model."""

from __future__ import annotations

import json
import math
import sys
import tempfile
from pathlib import Path

import bpy
from mathutils import Quaternion, Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
from blender_locator_adapter_integration import PIPELINE_ROOT, REPO_ROOT, blender_worker, digest


REVIEWED_CANDIDATE_HASHES = {
    ".tools/3d_pipeline/adapter/blender_worker.py": "0C59C4E1D6A241003F59458F5DD130C05670633D304A05AB017E554410216FD6",
    ".tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py": "B72B323CC9B0C9D70597F662F951D1EC0B18F566BB9CFC3854E321D6D03849A4",
    ".tools/3d_pipeline/blender_client.py": "B2FE78FA84E297C6A913F4E2E17E2E3C1620F417306E33F3066B6F9162241A50",
}


def verified_environment() -> dict:
    config = json.loads((PIPELINE_ROOT / "config/blender_hoi4_adapter.json").read_text(encoding="utf-8"))
    lock = json.loads((PIPELINE_ROOT / "config/dependencies.lock.json").read_text(encoding="utf-8"))
    adapter = lock["routes"]["blender_hoi4_adapter"]
    assert config["adapter_version"] == adapter["version"]
    assert config["operations"] == adapter["operations"]
    assert "review_humanoid_components" in adapter["operations"], "Registered component review operation is missing"
    for path, expected in adapter["source_sha256"].items():
        required = REVIEWED_CANDIDATE_HASHES.get(path, expected.upper())
        assert digest(REPO_ROOT / path) == required, f"Reviewed candidate/unchanged lock mismatch: {path}"
    for path, expected in REVIEWED_CANDIDATE_HASHES.items():
        assert digest(REPO_ROOT / path) == expected, f"Native component-review candidate changed: {path}"
    assert bpy.app.version_string == lock["routes"]["blender"]["version"]
    assert bpy.app.build_hash.decode() == lock["routes"]["blender"]["build_commit"]
    return config


def reset_scene() -> None:
    bpy.ops.wm.read_factory_settings(use_empty=True)


def create_fixture(job: Path) -> tuple[object, object, object]:
    reset_scene()
    mesh = bpy.data.meshes.new("ComponentFixtureData")
    mesh.from_pydata(
        [(0, 0, 0), (1, 0, 0), (0, 1, 0),
         (1.5, 0, 0.25), (2.5, 0, 0.25), (2.0, 1, 0.25),
         (-0.5, 0, 0.5), (-0.5, 1, 0.5), (0, 0, 1.8)],
        [(6, 7)],
        [(0, 2, 1), (3, 5, 4)],
    )
    mesh.update()
    body = bpy.data.objects.new("ExactComponentMesh", mesh)
    bpy.context.scene.collection.objects.link(body)
    body.location = (0.4, -0.3, 0.2)
    body.rotation_euler = (0.18, -0.27, 0.31)
    body.scale = (1.3, 0.75, 1.15)
    body["chaosx_source_protected"] = True
    body["fixture_lineage"] = "disposable_native_component_review"
    uv = mesh.uv_layers.new(name="FixtureUV")
    for polygon_index, polygon in enumerate(mesh.polygons):
        coordinates = ((0.0, 0.0), (0.9, 0.1), (0.15, 0.95)) if polygon_index == 0 else ((0.2, 0.2), (0.85, 0.3), (0.7, 0.9))
        for loop_index, coordinate in zip(polygon.loop_indices, coordinates):
            uv.data[loop_index].uv = coordinate
    for index, color in enumerate(((0.18, 0.34, 0.68, 1), (0.48, 0.20, 0.12, 1))):
        material = bpy.data.materials.new(f"FixtureMaterial{index}")
        material.use_nodes = True
        material.diffuse_color = color
        image = bpy.data.images.new(f"FixtureImage{index}", width=2, height=2, alpha=True)
        image.generated_color = color
        texture = material.node_tree.nodes.new("ShaderNodeTexImage")
        texture.name, texture.image = f"FixtureTexture{index}", image
        mesh.materials.append(material)
    mesh.polygons[0].material_index = 0
    mesh.polygons[1].material_index = 1

    rig_data = bpy.data.armatures.new("InventoryRigData")
    rig = bpy.data.objects.new("InventoryRig", rig_data)
    bpy.context.scene.collection.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    rig.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")
    euler_name, quaternion_name = 'Euler "Quoted"', "QuaternionBone"
    euler = rig_data.edit_bones.new(euler_name)
    euler.head, euler.tail = (0, 0, 0), (0, 0, 1)
    quaternion = rig_data.edit_bones.new(quaternion_name)
    quaternion.head, quaternion.tail = (0, 0, 1), (0.4, 0.2, 1.8)
    quaternion.parent = euler
    bpy.ops.object.mode_set(mode="OBJECT")
    rig.rotation_mode = "ZYX"
    rig.animation_data_create()
    action = bpy.data.actions.new("InventoryAttack")
    action.use_fake_user = True
    rig.animation_data.action = action
    euler_pose = rig.pose.bones[euler_name]
    quaternion_pose = rig.pose.bones[quaternion_name]
    euler_pose.rotation_mode = "XYZ"
    quaternion_pose.rotation_mode = "QUATERNION"
    euler_pose["fixture_custom"] = 0.0
    for frame, angle in ((1, -0.2), (5, 0.55)):
        rig.location = (0.1 * frame, 0, 0)
        rig.keyframe_insert(data_path="location", frame=frame)
        euler_pose.rotation_euler = (angle, angle * 0.25, -angle * 0.5)
        euler_pose.keyframe_insert(data_path="rotation_euler", frame=frame)
        euler_pose.scale = (1.0, 1.0 + frame * 0.01, 1.0)
        euler_pose.keyframe_insert(data_path="scale", frame=frame)
        euler_pose["fixture_custom"] = frame * 0.1
        euler_pose.keyframe_insert(data_path='["fixture_custom"]', frame=frame)
        quaternion_pose.rotation_quaternion = Quaternion(Vector((0.2, 0.7, 0.3)).normalized(), angle)
        quaternion_pose.keyframe_insert(data_path="rotation_quaternion", frame=frame)
    unrelated = bpy.data.actions.new("UnrelatedRetainedAction")
    unrelated.use_fake_user = True
    rig.animation_data.action = unrelated
    rig.rotation_euler = (0, 0, 0.1)
    rig.keyframe_insert(data_path="rotation_euler", frame=1)
    rig.rotation_euler = (0, 0, 0.2)
    rig.keyframe_insert(data_path="rotation_euler", frame=5)
    rig.animation_data.action = action
    track = rig.animation_data.nla_tracks.new()
    track.name = "UnrelatedNLA"
    track.mute = True
    track.strips.new("UnrelatedStrip", 1, unrelated)
    bpy.context.scene.frame_set(3)
    bpy.context.view_layer.update()
    return body, rig, action


def png_dimensions(path: Path) -> tuple[int, int]:
    value = path.read_bytes()
    assert value[:8] == b"\x89PNG\r\n\x1a\n"
    return int.from_bytes(value[16:20], "big"), int.from_bytes(value[20:24], "big")


def main() -> None:
    verified_environment()
    with tempfile.TemporaryDirectory(prefix="chaosx_component_review_fixture_") as temporary:
        job = Path(temporary).resolve()
        (job / "blender/checkpoints").mkdir(parents=True)
        body, rig, action = create_fixture(job)
        source = job / "blender/checkpoints/source.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(source))
        source_hash = digest(source)
        before_action = blender_worker._mesh_region_action_integrity()
        before_binding = blender_worker._action_channel_binding_record(rig)

        inventory = blender_worker.inspect({"request_id": "inventory", "job_id": "fixture", "job_root": str(job), "operation": "inspect_scene", "payload": {
            "blend_rel": "blender/checkpoints/source.blend", "render_previews": False, "runtime_stem": "", "action_name": "InventoryAttack",
            "target_armature_name": "InventoryRig", "preview_frame": -1, "preview_view_names": [],
            "include_action_channels": True, "expected_source_sha256": source_hash,
        }})["action_channels"]
        rows = inventory["rows"]
        assert any(row["data_path"] == "location" and row["rotation_mode"] == "ZYX" for row in rows)
        assert any(row["data_path"].endswith(".rotation_euler") and row["rotation_mode"] == "XYZ" for row in rows)
        assert any(row["data_path"].endswith(".scale") and row["rotation_mode"] == "XYZ" for row in rows)
        assert any(row["data_path"].endswith(".rotation_quaternion") and row["rotation_mode"] == "QUATERNION" for row in rows)
        assert any("fixture_custom" in row["data_path"] and row["rotation_mode"] == "XYZ" for row in rows)
        assert inventory["source_immutable"] and inventory["action_data_unchanged"] and digest(source) == source_hash
        rig = bpy.data.objects["InventoryRig"]
        assert blender_worker._mesh_region_action_integrity() == before_action
        assert blender_worker._action_channel_binding_record(rig) == before_binding

        request = {"request_id": "1" * 32, "job_id": "fixture", "job_root": str(job), "operation": "review_humanoid_components", "payload": {
            "blend_rel": "blender/checkpoints/source.blend", "expected_source_sha256": source_hash, "mesh_name": "ExactComponentMesh",
            "render_group": True, "component_ids": [], "component_offset": 0, "component_limit": 16,
            "preview_view_names": ["front", "left", "right", "rear", "top", "three_quarter"],
        }}
        review = blender_worker.review_humanoid_components(request)
        assert review["component_count"] == 4
        assert review["component_page"]["component_ids"] == ["c_v0", "c_v3", "c_v6", "c_v8"]
        assert review["source_immutable"] and review["original_data_unchanged"] and not review["semantic_component_acceptance"]
        assert review["source_record"]["components"][0]["uv_layers"]["FixtureUV"]["uv_island_count"] == 1
        assert review["source_record"]["components"][2]["topology_class"] == "wire"
        assert review["source_record"]["components"][3]["topology_class"] == "point"
        assert len(review["previews"]) == 6
        for preview in review["previews"]:
            path = job / preview["path"]
            assert png_dimensions(path) == (1024, 1024)
            assert digest(path) == preview["sha256"]
            assert preview["component_ids"] == review["component_page"]["component_ids"]
        report = job / review["report"]
        assert digest(report) == review["report_sha256"] and report.stat().st_size == review["report_bytes"]
        assert digest(source) == source_hash

        explicit = json.loads(json.dumps(request))
        explicit["request_id"] = "2" * 32
        explicit["payload"]["component_ids"] = ["c_v6", "c_v8"]
        explicit["payload"]["preview_view_names"] = ["front"]
        selected = blender_worker.review_humanoid_components(explicit)
        assert selected["component_page"]["component_ids"] == ["c_v6", "c_v8"]
        assert selected["component_page"]["offset"] is None and len(selected["previews"]) == 1
        assert digest(source) == source_hash

        rejected = json.loads(json.dumps(request))
        rejected["request_id"] = "3" * 32
        rejected["payload"]["component_ids"] = ["c_v999"]
        try:
            blender_worker.review_humanoid_components(rejected)
        except ValueError as exc:
            assert "Unknown component_ids" in str(exc)
        else:
            raise AssertionError("Unknown component ID did not reject")
        assert digest(source) == source_hash and not (job / f"blender/reports/component_review_{'3' * 32}.json").exists()

        original_render = blender_worker._render_component_group
        failed = json.loads(json.dumps(request))
        failed["request_id"] = "4" * 32
        def injected(*args, **kwargs):
            raise RuntimeError("injected render failure")
        blender_worker._render_component_group = injected
        try:
            try:
                blender_worker.review_humanoid_components(failed)
            except RuntimeError as exc:
                assert "injected render failure" in str(exc)
            else:
                raise AssertionError("Injected render failure did not reject")
        finally:
            blender_worker._render_component_group = original_render
        assert digest(source) == source_hash and not (job / f"blender/reports/component_review_{'4' * 32}.json").exists()
        print(json.dumps({"status": "pass", "fixture_only": True, "production_asset_acceptance": False,
                          "reviewed_registered_candidate": True, "adapter_version": adapter["version"],
                          "source_sha256": source_hash, "native_action_sha256": inventory["native_action_sha256"],
                          "component_catalog_sha256": review["component_catalog_sha256"],
                          "component_ids": review["component_page"]["component_ids"],
                          "preview_sha256": {row["view"]: row["sha256"] for row in review["previews"]}}, sort_keys=True))


if __name__ == "__main__":
    main()

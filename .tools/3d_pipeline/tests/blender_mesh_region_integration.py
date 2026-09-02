"""Native, disposable mesh-region proof; never opens a production checkpoint."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path

import bpy
from mathutils import Matrix, Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))

from blender_locator_adapter_integration import (
    ACTION_NAME, PARENT_BONE, PIPELINE_ROOT, REPO_ROOT, RIG_NAME,
    blender_worker, create_fixture, digest, reset_fixture_scene,
)


def verified_environment() -> dict:
    config = json.loads((PIPELINE_ROOT / "config/blender_hoi4_adapter.json").read_text(encoding="utf-8"))
    lock = json.loads((PIPELINE_ROOT / "config/dependencies.lock.json").read_text(encoding="utf-8"))
    adapter = lock["routes"]["blender_hoi4_adapter"]
    assert config["adapter_version"] == adapter["version"] == "1.10.18"
    assert config["operations"] == adapter["operations"] and "inspect_scene" in adapter["operations"]
    for path, expected in adapter["source_sha256"].items():
        assert digest(REPO_ROOT / path) == expected.upper(), f"Source lock mismatch: {path}"
    assert bpy.app.version_string == lock["routes"]["blender"]["version"]
    assert bpy.app.build_hash.decode() == lock["routes"]["blender"]["build_commit"]
    return config


def near(actual, expected, label: str, tolerance: float = 2e-5) -> float:
    error = (Vector(actual) - Vector(expected)).length
    assert error <= tolerance, f"{label}: {error}"
    return error


def reject(request: dict, expected: str) -> str:
    try:
        blender_worker.inspect(request)
    except (ValueError, RuntimeError, FileNotFoundError) as exc:
        assert expected in str(exc), str(exc)
        return str(exc)
    raise AssertionError(f"Expected rejection: {expected}")


def main() -> None:
    config = verified_environment()
    with tempfile.TemporaryDirectory(prefix="chaosx_mesh_region_fixture_") as temporary:
        job = Path(temporary).resolve()
        (job / "export/mesh").mkdir(parents=True)
        create_fixture(job)
        body, rig = bpy.data.objects["FixtureBody"], bpy.data.objects[RIG_NAME]
        body.scale = (1.2, 0.8, 1.4)
        rig.scale = (1.5, 0.75, 2.0)
        body["chaosx_source_protected"] = True
        rig["chaosx_reference_read_only"] = True
        rig["chaosx_promotion_validation"] = "fixture_lineage.json"
        rig["chaosx_promotion_validation_sha256"] = "A" * 64
        bpy.data.materials.new("HarmlessUnconsumedMaterial")
        bpy.context.scene.frame_set(1)
        bpy.context.view_layer.update()
        source = job / "source.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(source))
        source_hash = digest(source)
        req = {"job_id": "mesh_region_fixture", "job_root": str(job), "operation": "inspect_scene",
               "payload": {"blend_rel": "source.blend", "target_armature_name": RIG_NAME, "action_name": ACTION_NAME, "preview_frame": 6, "render_previews": False}}
        # Public legacy inspection supplies the exact native action identity.
        legacy = blender_worker.inspect(req)
        assert "mesh_region" not in legacy
        action_hash = legacy["inspected_action_sha256"]
        assert digest(source) == source_hash
        body, rig = bpy.data.objects["FixtureBody"], bpy.data.objects[RIG_NAME]
        bone_world = rig.matrix_world @ rig.pose.bones[PARENT_BONE].matrix
        deformation = bone_world @ rig.data.bones[PARENT_BONE].matrix_local.inverted() @ rig.matrix_world.inverted() @ body.matrix_world
        expected_positions = {vertex.index: deformation @ vertex.co for vertex in body.data.vertices}
        normal_transform = deformation.to_3x3().inverted().transposed()
        expected_loop_normals = {loop.index: (normal_transform @ body.data.corner_normals[loop.index].vector).normalized() for loop in body.data.loops}
        source_uvs = {loop.index: list(body.data.uv_layers["FixtureUV"].data[loop.index].uv) for loop in body.data.loops}
        req["payload"]["mesh_region"] = {
            "mesh_name": "FixtureBody", "bone_name": PARENT_BONE,
            "expected_source_sha256": source_hash, "expected_action_sha256": action_hash,
            "aabb": {"space": "WORLD", "min": [-100, -100, -100], "max": [100, 100, 100]},
            "weight": {"bone_name": PARENT_BONE, "min": 1, "max": 1},
            "offset": 1, "limit": 1,
            "measurement": {"origin_vertex_indices": [0], "endpoint_vertex_indices": [2, 3]},
        }
        result = blender_worker.inspect(req)["mesh_region"]
        assert result["total_matches"] == 4 and result["page"]["returned_vertices"] == 1
        assert result["page"]["truncated"] is True and result["page"]["next_offset"] == 2
        assert result["measurement"]["endpoint_vertex_indices"] == [2, 3]
        assert result["measurement"]["endpoint_count"] == 2
        assert result["measurement"]["rotation_quaternion"] is None
        assert bpy.context.scene.frame_current == 1
        assert bpy.data.objects["FixtureBody"]["chaosx_source_protected"] is True
        assert bpy.data.objects[RIG_NAME]["chaosx_reference_read_only"] is True
        assert result["source_immutable"] and result["all_actions_unchanged"] and result["frame_action_binding_restored"]
        assert result["source_receipt_metadata"][RIG_NAME]["chaosx_promotion_validation_sha256"] == "A" * 64
        assert result["checkpoint_saved"] is False and result["new_provider_call"] is False
        errors = {}
        record = result["records"][0]
        assert record["vertex_index"] == 1 and record["source_position"] == [1.0, 0.0, 0.0]
        assert record["weights"] == [{"group_index": 0, "group_name": PARENT_BONE, "weight": 1.0}]
        errors["deformed_vertex"] = near(record["evaluated_world_position"], expected_positions[1], "single-bone deformation")
        errors["bone_roundtrip"] = near(Matrix(result["matrices"]["bone_pose_world"]) @ Vector(record["bone_local_position"]), expected_positions[1], "bone/world roundtrip")
        for corner in record["corners"]:
            assert corner["source_uvs"]["FixtureUV"] == source_uvs[corner["loop_index"]]
            assert corner["evaluated_uvs"] == corner["source_uvs"]
            assert corner["material_index"] == 0 and corner["material_name"] == "FixtureMaterial"
            errors[f"corner_normal_{corner['loop_index']}"] = near(corner["evaluated_world_normal"], expected_loop_normals[corner["loop_index"]], "inverse-transpose normal")
            errors[f"bone_normal_{corner['loop_index']}"] = near(corner["bone_local_normal"], (bone_world.to_3x3().transposed() @ expected_loop_normals[corner["loop_index"]]).normalized(), "bone-local normal")
        endpoint = (expected_positions[2] + expected_positions[3]) / 2
        errors["endpoint_centroid"] = near(result["measurement"]["world_endpoint"], endpoint, "outside-page centroid")
        errors["measured_axis"] = near(result["measurement"]["world_axis"], (endpoint - expected_positions[0]).normalized(), "observed centroid axis")
        assert digest(source) == source_hash

        narrow = copy.deepcopy(req)
        point = record["bone_local_position"]
        narrow["payload"]["mesh_region"]["aabb"] = {"space": "BONE_LOCAL", "min": [value - 1e-4 for value in point], "max": [value + 1e-4 for value in point]}
        narrow["payload"]["mesh_region"].update(offset=0, limit=256)
        del narrow["payload"]["mesh_region"]["measurement"]
        selected = blender_worker.inspect(narrow)["mesh_region"]
        assert selected["total_matches"] == 1 and selected["records"][0]["vertex_index"] == 1
        assert selected["page"]["truncated"] is False
        failures = {}
        bad = copy.deepcopy(req)
        bad["payload"]["blend_rel"] = "../escape.blend"
        failures["path"] = reject(bad, "relative")
        bad = copy.deepcopy(req)
        bad["payload"]["mesh_region"]["aabb"]["min"][0] = float("nan")
        failures["nonfinite_selector"] = reject(bad, "finite")
        bad = copy.deepcopy(req)
        bad["payload"]["mesh_region"]["measurement"]["endpoint_vertex_indices"] = [999]
        failures["unmatched_measurement"] = reject(bad, "match the complete selector")
        assert bpy.context.scene.frame_current == 1, "Failure path did not restore the frame"
        assert bpy.data.objects[RIG_NAME].animation_data.action.name == ACTION_NAME
        try:
            blender_worker._mesh_region_measurement({"origin_vertex_indices": [0], "endpoint_vertex_indices": [1]}, [0, 1], lambda index: Vector((0, 0, 0)), Matrix.Identity(4))
        except ValueError as exc:
            assert "zero length" in str(exc)
            failures["zero_axis"] = str(exc)
        else:
            raise AssertionError("Zero centroid axis was accepted")
        for label, matrix in (("negative", Matrix.Scale(-1, 4)), ("singular", Matrix.Diagonal((0, 1, 1, 1)))):
            try:
                blender_worker._mesh_region_matrix(matrix, label)
            except ValueError as exc:
                failures[label + "_transform"] = str(exc)
            else:
                raise AssertionError("Invalid transform was accepted")
        bad = copy.deepcopy(req)
        bad["payload"]["mesh_region"]["expected_action_sha256"] = "0" * 64
        failures["action_hash"] = reject(bad, "native action SHA-256 mismatch")
        bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
        external_parent = bpy.data.objects.new("ExternalAnimatedParent", None)
        bpy.context.scene.collection.objects.link(external_parent)
        external_parent.location = (1, 2, 3)
        external_parent.keyframe_insert(data_path="location", frame=6)
        bpy.data.objects[RIG_NAME].parent = external_parent
        parent_source = job / "external_parent.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(parent_source))
        bad = copy.deepcopy(req)
        bad["payload"]["blend_rel"] = parent_source.name
        bad["payload"]["mesh_region"]["expected_source_sha256"] = digest(parent_source)
        failures["external_animated_parent"] = reject(bad, "uninspected parent dependency")
        bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
        bpy.data.objects["FixtureBody"].modifiers.new("ForbiddenTopologyChange", "SUBSURF")
        bad_source = job / "topology_change.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(bad_source))
        bad = copy.deepcopy(req)
        bad["payload"]["blend_rel"] = bad_source.name
        bad["payload"]["mesh_region"]["expected_source_sha256"] = digest(bad_source)
        failures["topology_changing_modifier"] = reject(bad, "exactly one active Armature")
        assert digest(source) == source_hash
        print(json.dumps({"status": "pass", "fixture_only": True, "production_asset_acceptance": False,
                          "adapter_version": config["adapter_version"], "blender_version": bpy.app.version_string,
                          "source_sha256": source_hash, "native_action_sha256": action_hash, "errors": errors,
                          "rejections": failures, "page": result["page"], "measurement": result["measurement"]}, sort_keys=True))
        reset_fixture_scene()


if __name__ == "__main__":
    main()

"""Disposable native action-phase patch proof; never a production model or action."""

from __future__ import annotations

import copy
import json
import math
import sys
import tempfile
from pathlib import Path

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parent))
from blender_locator_adapter_integration import (
    ACTION_NAME, PARENT_BONE, ROOT_BONE, PIPELINE_ROOT, REPO_ROOT, RIG_NAME,
    blender_worker, create_fixture, digest, reset_fixture_scene,
)


CHILD_BONE = "fixture_chain_child"
REVIEWED_CANDIDATE_HASHES = {
    ".tools/3d_pipeline/adapter/blender_worker.py": "5C8DF03BF75355BE60CAFE1CE7C300025A07449FB327383A0CC89B1C0F11FE40",
    ".tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py": "2011F13EFF2887A67C52A1662381EC7CBE2146132B13B1122285F5E86D2FF935",
    ".tools/3d_pipeline/blender_client.py": "ADA7C52EB14AE7A48AEB4D7369E4464E1AA3F447878EB989A0EBCDEA7C6A99A8",
}


def verified_environment() -> dict:
    config = json.loads((PIPELINE_ROOT / "config/blender_hoi4_adapter.json").read_text(encoding="utf-8"))
    lock = json.loads((PIPELINE_ROOT / "config/dependencies.lock.json").read_text(encoding="utf-8"))
    adapter = lock["routes"]["blender_hoi4_adapter"]
    # Parent explicitly requested this disposable native proof before registration.
    # Every deliberate candidate is pinned; all other production locks still apply.
    assert config["adapter_version"] == adapter["version"] and adapter["version"] in {"1.10.18", "1.10.19", "1.10.20", "1.10.21"}
    assert config["operations"] == adapter["operations"]
    candidate = adapter["version"] == "1.10.18"
    assert adapter["operations"].count("patch_existing_humanoid_action_phases") == (0 if candidate else 1)
    assert set(REVIEWED_CANDIDATE_HASHES).issubset(adapter["source_sha256"])
    for path, expected in adapter["source_sha256"].items():
        required = REVIEWED_CANDIDATE_HASHES.get(path, expected.upper()) if candidate else expected.upper()
        assert digest(REPO_ROOT / path) == required, f"Reviewed candidate/source lock mismatch: {path}"
    for path, expected in REVIEWED_CANDIDATE_HASHES.items():
        assert digest(REPO_ROOT / path) == expected, f"Native fixture candidate changed: {path}"
    assert bpy.app.version_string == lock["routes"]["blender"]["version"]
    assert bpy.app.build_hash.decode() == lock["routes"]["blender"]["build_commit"]
    return {**config, "reviewed_unregistered_candidate": candidate}


def quaternion(angle: float) -> list[float]:
    return [math.cos(angle / 2), math.sin(angle / 2), 0.0, 0.0]


def phase_request(job: Path, source: Path, role: str) -> dict:
    phases = {"ready": 1, "aim": 3, "discharge": 5, "recoil": 7, "recovery": 10}
    if role == "support_attack":
        phases = {"ready": 1, "aim": 2, "discharge": 4, "recoil": 6, "recovery": 9}
    if role == "defend":
        phases = {"guard_start": 1, "guard_hold": 5, "guard_release": 10}
    if role == "retreat":
        phases = {"disengage": 1, "withdrawal": 5, "recovery": 10}
    frames = sorted({1, 12, *phases.values()})
    angles = {1: -0.25, 2: 0.3, 3: 0.4, 4: 0.35, 5: 0.45, 6: 0.75, 7: 0.85, 9: 0.15, 10: 0.1, 12: -0.25}
    keys = [{"frame": frame, "value": quaternion(angles[frame])} for frame in frames]
    payload = {
        "blend_rel": source.name, "checkpoint_rel": f"patched_{role}.blend",
        "expected_source_sha256": digest(source),
        "expected_action_sha256": blender_worker._mesh_region_action_hash(bpy.data.actions[ACTION_NAME]),
        "target_armature_name": RIG_NAME, "source_action_name": ACTION_NAME, "target_action_name": f"patched_{role}",
        "semantic_role": role, "source_fps": 30, "source_fps_base": 1.0,
        "frame_start": 1, "frame_end": 12, "phase_frames": phases,
        "allowed_bones": [PARENT_BONE], "motion_bone_chain": [],
        "bone_patches": {PARENT_BONE: {"rotation_quaternion": keys}},
    }
    if role == "retreat":
        payload["allowed_bones"].append(CHILD_BONE)
        payload["motion_bone_chain"] = [PARENT_BONE, CHILD_BONE]
        payload["bone_patches"][CHILD_BONE] = {"rotation_quaternion": [{"frame": row["frame"], "value": quaternion(-0.5 * {1: -0.25, 5: 0.45, 10: 0.1, 12: -0.25}[row["frame"]])} for row in keys]}
    return {"job_id": "action_phase_fixture", "job_root": str(job), "operation": "patch_existing_humanoid_action_phases", "payload": payload}


def reject(request: dict, source: Path, expected: str) -> str:
    before = digest(source)
    output = Path(request["job_root"]) / request["payload"]["checkpoint_rel"]
    existed = output.exists()
    try:
        blender_worker.patch_existing_humanoid_action_phases(request)
    except (ValueError, RuntimeError, FileNotFoundError) as exc:
        assert expected in str(exc), str(exc)
        assert digest(source) == before, "Failure changed immutable source bytes"
        assert output.exists() == existed, "Pre-save failure unexpectedly created a checkpoint"
        return str(exc)
    raise AssertionError(f"Expected rejection: {expected}")


def main() -> None:
    config = verified_environment()
    with tempfile.TemporaryDirectory(prefix="chaosx_action_phase_fixture_") as temporary:
        job = Path(temporary).resolve()
        (job / "export/mesh").mkdir(parents=True)
        create_fixture(job)
        rig = bpy.data.objects[RIG_NAME]
        bpy.context.view_layer.objects.active = rig
        bpy.ops.object.mode_set(mode="EDIT")
        child = rig.data.edit_bones.new(CHILD_BONE)
        child.head = rig.data.edit_bones[PARENT_BONE].tail
        child.tail = (1.5, 1.8, 2.1)
        child.parent = rig.data.edit_bones[PARENT_BONE]
        bpy.ops.object.mode_set(mode="OBJECT")
        rig.pose.bones[CHILD_BONE].rotation_mode = "QUATERNION"
        for frame in (1, 6, 12):
            rig.pose.bones[CHILD_BONE].rotation_quaternion = (1, 0, 0, 0)
            rig.pose.bones[CHILD_BONE].keyframe_insert(data_path="rotation_quaternion", frame=frame)
        # The shared locator fixture keys constant scale; this capability forbids
        # source scale tracks, so omit them before creating this fixture's source.
        for curve, collection in list(blender_worker.action_fcurves(bpy.data.actions[ACTION_NAME])):
            if curve.data_path.endswith(".scale"):
                collection.remove(curve)
        collision = bpy.data.actions[ACTION_NAME].copy()
        collision.name, collision.use_fake_user = "ExistingTarget", True
        locator = bpy.data.objects.new("fixture_observed_locator", None)
        bpy.context.scene.collection.objects.link(locator)
        locator.parent, locator.parent_type, locator.parent_bone = rig, "BONE", PARENT_BONE
        locator.location = (0.2, 0.1, 0.3)
        bpy.context.scene.frame_set(6)
        bpy.context.view_layer.update()
        source = job / "source.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(source))
        source_hash = digest(source)
        bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
        before = blender_worker._promotion_fingerprint(job, ())
        source_action_hash = blender_worker._mesh_region_action_hash(bpy.data.actions[ACTION_NAME])
        reports = {}
        for role in ("attack", "support_attack", "defend", "retreat"):
            bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
            request = phase_request(job, source, role)
            result = blender_worker.patch_existing_humanoid_action_phases(request)
            assert result["source_immutable"] and result["original_actions_unchanged"]
            assert result["reopen_comparison"]["accepted"] and result["target_action_reopen_exact"]
            assert result["manual_or_procedural_replacement_authored"] is True
            assert result["procedural_generator_used"] is False and result["semantic_acceptance"] is False
            assert result["source_fps"] == 30 and result["source_fps_base"] == 1.0
            assert result["source_action_sha256"] == source_action_hash
            assert result["target_action_sha256"] != source_action_hash
            assert digest(source) == source_hash
            assert bpy.context.scene.frame_current == 6
            assert bpy.data.objects[RIG_NAME].animation_data.action.name == ACTION_NAME
            target_name = request["payload"]["target_action_name"]
            after = blender_worker._promotion_fingerprint(job, (), exclude_action_name=target_name)
            assert blender_worker._promotion_reopen_comparison(before, after)["accepted"]
            assert {ACTION_NAME, "ExistingTarget", target_name} == {action.name for action in bpy.data.actions}
            for bone, channels in request["payload"]["bone_patches"].items():
                for channel, keys in channels.items():
                    path = bpy.data.objects[RIG_NAME].pose.bones[bone].path_from_id(channel)
                    curves = {curve.array_index: curve for curve, _ in blender_worker.action_fcurves(bpy.data.actions[target_name]) if curve.data_path == path}
                    assert len(curves) == (4 if channel == "rotation_quaternion" else 3)
                    for index, curve in curves.items():
                        assert [point.co.x for point in curve.keyframe_points] == [row["frame"] for row in keys]
                        assert all(abs(point.co.y - row["value"][index]) < 1e-6 for point, row in zip(curve.keyframe_points, keys))
                        assert all(point.interpolation == "LINEAR" for point in curve.keyframe_points)
            assert all(phase["locators"] and phase["meshes"] for phase in result["target_phases"].values())
            reports[role] = {key: result[key] for key in ("target_action_sha256", "changed_bones", "phase_transitions", "target_action_reopen_exact")}

        bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
        request = phase_request(job, source, "attack")
        request["payload"]["checkpoint_rel"] = "rejection.blend"
        failures = {}
        for field, value, expected in (("source_fps", 24, "FPS"), ("expected_source_sha256", "0" * 64, "source SHA"),
                                       ("expected_action_sha256", "0" * 64, "action SHA"), ("target_action_name", "ExistingTarget", "exists"),
                                       ("checkpoint_rel", "../escape.blend", "relative")):
            bad = copy.deepcopy(request)
            bad["payload"][field] = value
            failures[field] = reject(bad, source, expected)
        bad = copy.deepcopy(request)
        bad["payload"]["bone_patches"][PARENT_BONE]["rotation_quaternion"][0]["value"] = [2, 0, 0, 0]
        failures["invalid_quaternion"] = reject(bad, source, "unit quaternion")
        bad = copy.deepcopy(request)
        bad["payload"]["allowed_bones"] = [ROOT_BONE]
        bad["payload"]["bone_patches"] = {ROOT_BONE: bad["payload"]["bone_patches"][PARENT_BONE]}
        failures["root_only"] = reject(bad, source, "non-root")
        bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
        bad = copy.deepcopy(request)
        # Source quaternion interpolation can have non-unit component length;
        # identity via an unchanged location channel avoids normalization ambiguity.
        bad["payload"]["bone_patches"][PARENT_BONE] = {"location": [{"frame": frame, "value": [0, 0, 0]} for frame in (1, 3, 5, 7, 10, 12)]}
        failures["identity_only"] = reject(bad, source, "identity-only")
        bpy.ops.wm.open_mainfile(filepath=str(source), use_scripts=False)
        bpy.data.objects[RIG_NAME].animation_data.nla_tracks.new()
        nla_source = job / "nla_source.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(nla_source))
        bad = copy.deepcopy(request)
        bad["payload"]["blend_rel"] = nla_source.name
        bad["payload"]["expected_source_sha256"] = digest(nla_source)
        failures["nla"] = reject(bad, nla_source, "NLA")
        assert digest(source) == source_hash
        print(json.dumps({"status": "pass", "fixture_only": True, "production_asset_acceptance": False,
                          "adapter_version": config["adapter_version"], "blender_version": bpy.app.version_string,
                          "reviewed_unregistered_candidate": config["reviewed_unregistered_candidate"], "candidate_source_sha256": REVIEWED_CANDIDATE_HASHES,
                          "source_sha256": source_hash, "source_action_sha256": source_action_hash,
                          "roles": reports, "rejections": failures}, sort_keys=True))
        reset_fixture_scene()


if __name__ == "__main__":
    main()

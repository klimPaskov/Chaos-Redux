"""Disposable native partition image-consumer transaction regression."""
import hashlib
import json
import sys
import tempfile
from pathlib import Path

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parent))
from blender_locator_adapter_integration import PIPELINE_ROOT, REPO_ROOT, RIG_NAME, blender_worker, create_fixture
import skeletal_export_partition as partition


def main():
    lock = json.loads((PIPELINE_ROOT / "config/dependencies.lock.json").read_text())
    adapter = lock["routes"]["blender_hoi4_adapter"]
    candidate = "--candidate" in sys.argv
    assert adapter["version"] == ("1.10.45" if candidate else "1.10.46")
    source_hashes = {path: hashlib.sha256((REPO_ROOT / path).read_bytes()).hexdigest().upper() for path in adapter["source_sha256"]}
    for path, expected in adapter["source_sha256"].items():
        if candidate and path in {".tools/3d_pipeline/adapter/skeletal_export_partition.py", ".tools/3d_pipeline/adapter/chaosx_blender_hoi4_mcp.py"}:
            continue
        assert source_hashes[path] == expected, path
    assert bpy.app.version_string == lock["routes"]["blender"]["version"]
    with tempfile.TemporaryDirectory(prefix="chaosx_partition_images_") as directory:
        job = Path(directory)
        (job / "export/mesh").mkdir(parents=True)
        create_fixture(job)
        source = job / "source.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(source), relative_remap=False)
        source_hash = blender_worker.file_sha256(source)
        request = {"job_id": "fixture", "job_root": str(job), "payload": {
            "blend_rel": source.name, "checkpoint_rel": "partition.blend", "expected_source_sha256": source_hash,
            "target_armature_name": RIG_NAME, "target_mesh_names": ["FixtureBody"], "max_export_vertices_per_batch": 3}}
        report = partition.partition_skeletal_mesh_export_batches(request, blender_worker)
        assert report["status"] == "pass" and len(report["material_clones"]) == 3
        assert report["fingerprints_before"] == report["fingerprints_after_partition"] == report["fingerprints_reopened"]
        image_proof = report["partition_consumer_reconciliation"]["image_consumers"]
        assert len(image_proof["images"]) == 1
        assert image_proof["images"][0]["after"]["users"] - image_proof["images"][0]["before"]["users"] == 3
        assert report["partition_consumer_reconciliation"] == report["reopened_consumer_reconciliation"]
        assert blender_worker.file_sha256(source) == source_hash
        baseline = report["fingerprints_before"]["image_retention"]
        def check_reject(label, mutate, undo):
            mutate()
            try:
                partition._fingerprint(blender_worker, job, ["FixtureBody"], report["material_clones"],
                    ownership=report["material_clone_ownership"], baseline_images=baseline)
            except RuntimeError as exc:
                failures[label] = str(exc)
            else:
                raise AssertionError("Native mutation was accepted: " + label)
            finally:
                undo()
        failures = {}
        image = bpy.data.images["FixtureDiffuse"]
        old_alpha = image.alpha_mode
        check_reject("changed_image", lambda: setattr(image, "alpha_mode", "NONE"), lambda: setattr(image, "alpha_mode", old_alpha))
        first_clone = bpy.data.materials[next(iter(report["material_clones"]))]
        check_reject("changed_clone", lambda: first_clone.__setitem__("shader", "OtherShader"), lambda: first_clone.__setitem__("shader", "PdxMeshAdvanced"))
        extra = bpy.data.materials.new("UnplannedMaterial")
        extra.use_nodes = True
        extra.node_tree.nodes.new("ShaderNodeTexImage").image = image
        try:
            partition._fingerprint(blender_worker, job, ["FixtureBody"], report["material_clones"], ownership=report["material_clone_ownership"], baseline_images=baseline)
        except RuntimeError as exc:
            failures["unplanned_image_consumer"] = str(exc)
        else:
            raise AssertionError("Unplanned native consumer was accepted")
        bpy.data.materials.remove(extra)
        other_mesh = bpy.data.meshes.new("UnplannedMesh")
        other_mesh.materials.append(first_clone)
        try:
            partition._fingerprint(blender_worker, job, ["FixtureBody"], report["material_clones"], ownership=report["material_clone_ownership"], baseline_images=baseline)
        except RuntimeError as exc:
            failures["clone_outside_owned_mesh"] = str(exc)
        else:
            raise AssertionError("Unplanned native clone slot was accepted")
        bpy.data.meshes.remove(other_mesh)
        assert len(failures) == 4
        result = {"scope": "Disposable native fixture; no production asset acceptance", "candidate": candidate,
                  "adapter_version": adapter["version"], "source_sha256": source_hashes, "partition": report, "native_negative_cases": failures}
        path = PIPELINE_ROOT / "reports/partition_image_consumers_1_10_46.json"
        path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"status": "pass", "report": str(path), "candidate": candidate}))


if __name__ == "__main__":
    main()

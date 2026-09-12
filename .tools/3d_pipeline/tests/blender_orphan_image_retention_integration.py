"""Disposable native save/reopen orphan-image regression; no production checkpoint."""
import hashlib
import json
import sys
import tempfile
from pathlib import Path

import bpy

sys.path.insert(0, str(Path(__file__).resolve().parent))
from blender_locator_adapter_integration import PIPELINE_ROOT, REPO_ROOT, blender_worker, create_fixture


def main():
    lock = json.loads((PIPELINE_ROOT / "config/dependencies.lock.json").read_text())
    config = json.loads((PIPELINE_ROOT / "config/blender_hoi4_adapter.json").read_text())
    adapter = lock["routes"]["blender_hoi4_adapter"]
    assert adapter["version"] == config["adapter_version"] == "1.10.45"
    assert adapter["operations"] == config["operations"]
    for relative, expected in adapter["source_sha256"].items():
        assert hashlib.sha256((REPO_ROOT / relative).read_bytes()).hexdigest().upper() == expected
    assert bpy.app.version_string == lock["routes"]["blender"]["version"]
    with tempfile.TemporaryDirectory(prefix="chaosx_orphan_image_") as directory:
        job = Path(directory)
        (job / "export/mesh").mkdir(parents=True)
        create_fixture(job)
        stable = job / "stable.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(stable), relative_remap=False)
        bpy.ops.wm.open_mainfile(filepath=str(stable), use_scripts=False)
        image_file = job / "orphan.png"
        image_file.write_bytes((job / "export/mesh/fixture_diffuse.png").read_bytes())
        image = bpy.data.images.load(str(image_file), check_existing=False)
        image.name = "OrphanImage"
        image.pack()
        orphan = bpy.data.materials.new("OrphanMaterial")
        orphan.use_nodes = True
        orphan.node_tree.nodes.new("ShaderNodeTexImage").image = image
        before = blender_worker._promotion_fingerprint(job, ())
        checkpoint = job / "orphan_drop.blend"
        bpy.ops.wm.save_as_mainfile(filepath=str(checkpoint), copy=True, relative_remap=False)
        bpy.ops.wm.open_mainfile(filepath=str(checkpoint), use_scripts=False)
        after = blender_worker._promotion_fingerprint(job, ())
        proof = blender_worker._promotion_reopen_comparison(before, after)
        assert proof["accepted"], proof
        assert [row["name"] for row in proof["removed_orphan_materials"]] == ["OrphanMaterial"]
        assert [row["name"] for row in proof["retained_images_with_released_orphan_consumers"]] == ["OrphanImage"]
        assert before["sha256"]["images"] == after["sha256"]["images"]
        assert before["image_retention"]["inventory"]["OrphanImage"]["packed_hashes"] == after["image_retention"]["inventory"]["OrphanImage"]["packed_hashes"]
        assert before["image_retention"]["inventory"]["FixtureDiffuse"] == after["image_retention"]["inventory"]["FixtureDiffuse"]
        assert before["image_retention"]["content_sha256"] == after["image_retention"]["content_sha256"]
        retained = bpy.data.images["FixtureDiffuse"]
        retained.alpha_mode = "NONE"
        changed = blender_worker._promotion_fingerprint(job, ())
        changed_proof = blender_worker._promotion_reopen_comparison(before, changed)
        assert not changed_proof["accepted"] and "image_retention.inventory['FixtureDiffuse'].changed" in changed_proof["mismatches"]
        bpy.data.images.remove(retained)
        lost = blender_worker._promotion_fingerprint(job, ())
        lost_proof = blender_worker._promotion_reopen_comparison(before, lost)
        assert not lost_proof["accepted"] and "image_retention.inventory['FixtureDiffuse'].required_image_missing" in lost_proof["mismatches"]
        bpy.ops.wm.open_mainfile(filepath=str(checkpoint), use_scripts=False)
        retained_file = job / "export/mesh/fixture_diffuse.png"
        retained_file.write_bytes(retained_file.read_bytes() + b"unexpected trailing bytes")
        file_changed = blender_worker._promotion_fingerprint(job, ())
        file_proof = blender_worker._promotion_reopen_comparison(before, file_changed)
        assert not file_proof["accepted"] and "sha256.images" in file_proof["mismatches"]
        # A later native save discards the now-zero-user packed image. Reject that loss.
        bpy.ops.wm.save_as_mainfile(filepath=str(job / "cascade_drop.blend"), copy=True, relative_remap=False)
        bpy.ops.wm.open_mainfile(filepath=str(job / "cascade_drop.blend"), use_scripts=False)
        cascade = blender_worker._promotion_reopen_comparison(before, blender_worker._promotion_fingerprint(job, ()))
        assert not cascade["accepted"] and "image_retention.inventory['OrphanImage'].required_image_missing" in cascade["mismatches"]
        report = {"adapter_version": adapter["version"], "blender_version": bpy.app.version_string,
                  "source_sha256": adapter["source_sha256"], "native_orphan_material_drop_with_exact_surviving_packed_image": proof,
                  "later_packed_image_disappearance_rejected": cascade,
                  "retained_image_change_rejected": changed_proof, "retained_image_loss_rejected": lost_proof,
                  "retained_external_file_change_rejected": file_proof,
                  "scope": "Disposable Blender fixture; no production asset or live game acceptance"}
        report_path = PIPELINE_ROOT / "reports/orphan_image_retention_1_10_45.json"
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"status": "pass", "report": str(report_path), "adapter_version": adapter["version"]}))


if __name__ == "__main__":
    main()

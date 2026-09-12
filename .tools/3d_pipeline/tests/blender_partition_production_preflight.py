"""Read an explicit production source and stop before any checkpoint save.

Usage after Blender's --: request.json job_root report.json.
Only the requested report under the adapter reports directory may be written.
"""
import hashlib
import json
import sys
import types
from pathlib import Path

import bpy

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
sys.path.insert(0, str(ROOT / "adapter"))
import blender_worker as worker
import skeletal_export_partition as partition


class PreflightComplete(RuntimeError):
    pass


def main():
    args = sys.argv[sys.argv.index("--") + 1:]
    request_path, job, report_path = [Path(value).resolve() for value in args]
    report_path.relative_to(ROOT / "reports")
    assert not report_path.exists(), "Preflight report overwrite is forbidden"
    args = json.loads(request_path.read_text(encoding="utf-8-sig"))["arguments"]
    job_id = args.pop("job_id")
    args["checkpoint_rel"] = str(Path(args["checkpoint_rel"]).with_name("adapter_partition_1_10_46_preflight_never_saved.blend")).replace("\\", "/")
    request = {"job_id": job_id, "job_root": str(job), "payload": args}
    native_inputs = partition._inputs
    exact_inputs = native_inputs(request, worker)
    source, output = exact_inputs[1:3]
    source_hash = worker.file_sha256(source)
    assert not output.exists()
    def redirected_inputs(req, api):
        # Preserve the original path/checksum validation and image containment.
        # Redirect only the report into adapter-owned evidence outside the model job.
        original = native_inputs(req, api)
        return (REPO, original[1], original[2], report_path, original[4], original[5])
    def no_save(**kwargs):
        assert Path(kwargs["filepath"]).resolve() == output
        raise PreflightComplete("Intentional preflight stop after exact partition invariants; no checkpoint save attempted.")
    class API:
        bpy = types.SimpleNamespace(data=bpy.data, context=bpy.context,
            ops=types.SimpleNamespace(wm=types.SimpleNamespace(open_mainfile=bpy.ops.wm.open_mainfile, save_as_mainfile=no_save)))
        def __getattr__(self, name):
            return getattr(worker, name)
        def _promotion_fingerprint(self, ignored_root, names, **kwargs):
            return worker._promotion_fingerprint(job, names, **kwargs)
    partition._inputs = redirected_inputs
    try:
        partition.partition_skeletal_mesh_export_batches(request, API())
    except PreflightComplete:
        pass
    else:
        raise AssertionError("Preflight did not reach its intentional save boundary")
    finally:
        partition._inputs = native_inputs
    assert worker.file_sha256(source) == source_hash and not output.exists()
    report = json.loads(report_path.read_text())
    assert report["fingerprints_before"] == report["fingerprints_after_partition"]
    assert report["partition_consumer_reconciliation"]["image_consumers"]["accepted"]
    report.update(status="preflight_pass_no_save", source_immutable=True, output_created=False,
                  scope="Production source read and partitioned only in disposable Blender memory; no production asset or runtime file written",
                  request_file=str(request_path), source_file=str(source),
                  adapter_source_sha256=hashlib.sha256((ROOT / "adapter/skeletal_export_partition.py").read_bytes()).hexdigest().upper())
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "report": str(report_path), "material_clones": report["material_clones"]}))


if __name__ == "__main__":
    main()

"""Run one or both autonomous 3D model pilots through Meshy and Blender."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from PIL import Image


if not os.environ.get("MESHY_API_KEY", "").strip():
    print(
        "MESHY_API_KEY is missing or blank. Stop. Run this PowerShell command, "
        "then restart the shell or Codex:\n\n"
        '[Environment]::SetEnvironmentVariable(\n'
        '    "MESHY_API_KEY",\n'
        '    "msy_your_actual_key_here",\n'
        '    "User"\n'
        ")\n"
    )
    raise SystemExit(2)

PIPELINE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PIPELINE_ROOT.parents[1]
sys.path.insert(0, str(PIPELINE_ROOT))

from blender_client import BlenderAdapterClient  # noqa: E402
from init_pilot_jobs import initialize_one  # noqa: E402
from lib.paths import (  # noqa: E402
    append_history,
    ensure_job_layout,
    file_record,
    read_job_document,
    read_json,
    resolve_job_root,
    utc_now,
    write_json,
)
from meshy_client import (  # noqa: E402
    MeshyClient,
    MeshyTaskFailed,
    _first_key,
    _payload,
    status_from,
    task_id_from,
)
from pack_pdx_material import (  # noqa: E402
    pack_pdx_normal_map,
    pack_pdx_specular_map,
    prepare_texture_source_rels,
)


STATIC_ASSET_KINDS = {"static", "building", "static_building"}
REFERENCE_CALIBRATED_ASSET_KINDS = {"humanoid", "creature", "building", "static_building"}
MESHY_TEXTURED_IMAGE_TO_3D_ESTIMATE = 30
MESHY_REMESH_ESTIMATE = 5
MESHY_TEXTURED_IMAGE_MODEL_IDS = {"meshy-7"}


def task_file(job: Path, stage: str) -> Path:
    return job / "provider" / "tasks" / f"{stage}.json"


def read_job(job: Path) -> Dict[str, Any]:
    return read_job_document(job / "job.yaml")


def stage_vanilla_reference(job: Path, spec: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Stage the named installed vanilla reference inside the bounded job root."""

    asset_kind = spec.get("asset_kind")
    if asset_kind not in REFERENCE_CALIBRATED_ASSET_KINDS:
        return None
    reference = spec.get("vanilla_scale_reference") or {}
    if asset_kind in {"building", "static_building"} and not reference:
        raise RuntimeError(
            "Static building preparation requires a named installed vanilla scale reference; "
            "height-only calibration is not permitted."
        )
    source = Path(str(reference.get("mesh", ""))).resolve()
    if not source.is_file():
        raise FileNotFoundError(f"Installed vanilla scale reference is missing: {source}")
    destination = job / "blender" / "reference" / source.name
    destination.parent.mkdir(parents=True, exist_ok=True)
    source_record = file_record(source)
    if not destination.exists() or file_record(destination)["sha256"] != source_record["sha256"]:
        shutil.copy2(source, destination)
    staged_record = file_record(destination, relative_to=job)
    write_json(
        job / "blender" / "reports" / "vanilla_reference_stage.json",
        {
            "source_path": str(source),
            "source_sha256": source_record["sha256"],
            "staged_file": staged_record,
            "read_only_source": True,
        },
    )
    return {
        "mesh_rel": staged_record["relative_path"],
        "entity": reference.get("entity"),
        "mesh_object_names": reference.get("mesh_object_names", []),
        "exclude_name_patterns": reference.get("exclude_name_patterns", []),
        "forward_axis": reference.get("forward_axis"),
        "up_axis": reference.get("up_axis"),
        "mesh_height": reference["mesh_height"],
        "entity_scale": reference["entity_scale"],
        "runtime_height": reference["runtime_height"],
    }


def update_job(job: Path, **changes: Any) -> Dict[str, Any]:
    value = read_job(job)
    value.update(changes)
    value["updated_at"] = utc_now()
    (job / "job.yaml").write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return value


def result_value(result: Dict[str, Any], key: str) -> Optional[Any]:
    value = _first_key(result, (key.lower(),))
    return value


def balance_value(result: Dict[str, Any]) -> Optional[int]:
    value = result_value(_payload(result), "balance")
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def record_balance(job: Path, stage: str, result: Dict[str, Any], estimate: int) -> int:
    balance = balance_value(result)
    if balance is None:
        raise RuntimeError("Meshy balance response did not contain a numeric balance.")
    write_json(
        job / "provider" / "credits" / f"{stage}_preflight.json",
        {
            "timestamp": utc_now(),
            "stage": stage,
            "balance_before_paid_call": balance,
            "estimated_credits": estimate,
            "hard_limit": estimate,
            "paid_call_authorized_by": "user_task",
        },
    )
    if balance < estimate:
        raise RuntimeError(f"Meshy balance {balance} is below the {estimate}-credit gate for {stage}.")
    return balance


def save_task(
    job: Path,
    stage: str,
    *,
    task_id: str,
    task_type: str,
    initial: Dict[str, Any],
    final: Dict[str, Any],
    estimate: int,
    input_stage: Optional[str] = None,
) -> None:
    consumed = _first_key(final, ("consumed_credits", "credits_used", "credit_cost"))
    record = {
        "schema_version": "1.0.0",
        "stage": stage,
        "task_id": task_id,
        "task_type": task_type,
        "initial_response": _payload(initial),
        "final_response": _payload(final),
        "status": status_from(final),
        "estimated_credits": estimate,
        "consumed_credits": consumed,
        "input_stage": input_stage,
        "provider": {
            "server_package": "@meshy-ai/meshy-mcp-server",
            "server_version": os.environ.get("MESHY_MCP_VERSION", "0.4.0"),
        },
        "recorded_at": utc_now(),
    }
    write_json(task_file(job, stage), record)
    append_history(
        job,
        state="provider_task_completed",
        event=stage,
        actor="meshy_mcp",
        details={
            "task_id": task_id,
            "task_type": task_type,
            "status": record["status"],
            "estimated_credits": estimate,
            "consumed_credits": consumed,
        },
    )


def record_paid_reconciliation(
    job: Path,
    stage: str,
    *,
    balance_before: Optional[int],
    balance_after: Optional[int],
    final: Dict[str, Any],
    estimate: int,
) -> None:
    """Persist provider-reported cost and the observed account balance delta."""

    consumed = _first_key(final, ("consumed_credits", "credits_used", "credit_cost"))
    try:
        observed_delta = (
            int(balance_before) - int(balance_after)
            if balance_before is not None and balance_after is not None
            else None
        )
    except (TypeError, ValueError):
        observed_delta = None
    try:
        provider_consumed = int(consumed) if consumed is not None else None
    except (TypeError, ValueError):
        provider_consumed = None
    if balance_before is None or balance_after is None:
        status = "missing_balance_boundary"
    elif provider_consumed is None:
        status = "missing_provider_consumption"
    elif observed_delta != provider_consumed:
        status = "balance_delta_mismatch"
    else:
        status = "reconciled"
    write_json(
        job / "provider" / "credits" / f"{stage}_reconciliation.json",
        {
            "timestamp": utc_now(),
            "stage": stage,
            "status": status,
            "estimate_credits": estimate,
            "provider_consumed_credits": provider_consumed,
            "balance_before_paid_call": balance_before,
            "balance_after_task": balance_after,
            "observed_balance_delta": observed_delta,
        },
    )


def existing_task(job: Path, stage: str) -> Optional[Dict[str, Any]]:
    path = task_file(job, stage)
    return read_json(path) if path.exists() else None


def generation_stage_for(spec: Dict[str, Any]) -> str:
    """Return the immutable provider stage selected for this geometry attempt."""

    stage = str(spec.get("generation_stage") or "generation").strip()
    if (stage != "generation" and not stage.startswith("generation_")) or any(
        character not in "abcdefghijklmnopqrstuvwxyz0123456789_" for character in stage
    ):
        raise ValueError(f"Invalid generation stage {stage!r}.")
    return stage


def generation_download_name(spec: Dict[str, Any], extension: str) -> str:
    """Keep every accepted or rejected provider attempt as a separate artifact."""

    return f"{generation_stage_for(spec)}_model.{extension.lstrip('.')}"


def recover_unrecorded_task(
    job: Path,
    *,
    stage: str,
    task_type: str,
    estimate: int,
    response_name_fragment: str,
) -> Optional[Dict[str, Any]]:
    """Recover a paid task created before a process crash wrote its task file."""

    if task_file(job, stage).exists():
        return read_json(task_file(job, stage))
    candidates = sorted(
        path for path in (job / "provider" / "responses").glob("*.json")
        if response_name_fragment in path.name
    )
    if len(candidates) != 1:
        return None
    response = read_json(candidates[0])
    try:
        task_id = task_id_from(response)
    except Exception:
        return None
    recovered = {
        "schema_version": "1.0.0",
        "stage": stage,
        "task_id": task_id,
        "task_type": task_type,
        "status": "PENDING",
        "initial_response": _payload(response),
        "estimated_credits": estimate,
        "recovered_from_response": str(candidates[0].relative_to(job)).replace("\\", "/"),
        "recovered_at": utc_now(),
    }
    write_json(task_file(job, stage), recovered)
    append_history(
        job,
        state="provider_task_recovered",
        event=stage,
        actor="chaosx_3d_model_pipeline",
        details={"task_id": task_id, "response": recovered["recovered_from_response"]},
    )
    return recovered


def provider_task(
    client: MeshyClient,
    job: Path,
    stage: str,
    *,
    task_type: str,
    estimate: int,
    create,
    input_stage: Optional[str] = None,
) -> str:
    existing = existing_task(job, stage)
    if existing:
        if existing.get("status") in {"SUCCEEDED", "SUCCESS", "COMPLETED", "DONE"}:
            return str(existing["task_id"])
        if existing.get("task_id") and existing.get("status") in {"PENDING", "IN_PROGRESS", "UNKNOWN"}:
            try:
                final = client.wait_for_task(
                    str(existing["task_id"]),
                    task_type=task_type,
                )
            except MeshyTaskFailed as exc:
                save_task(
                    job,
                    stage,
                    task_id=str(existing["task_id"]),
                    task_type=task_type,
                    initial=existing.get("initial_response", {}),
                    final=exc.final,
                    estimate=estimate,
                    input_stage=input_stage,
                )
                raise
            save_task(
                job,
                stage,
                task_id=str(existing["task_id"]),
                task_type=task_type,
                initial=existing.get("initial_response", {}),
                final=final,
                estimate=estimate,
                input_stage=input_stage,
            )
            return str(existing["task_id"])
        raise RuntimeError(
            f"Paid stage {stage} already has a non-success record. "
            "No paid retry is permitted: " + str(task_file(job, stage))
        )
    balance_result = client.check_balance()
    balance_before = record_balance(job, stage, balance_result, estimate)
    initial = create()
    task_id = task_id_from(initial)
    write_json(
        task_file(job, stage),
        {
            "schema_version": "1.0.0",
            "stage": stage,
            "task_id": task_id,
            "task_type": task_type,
            "status": "PENDING",
            "initial_response": _payload(initial),
            "estimated_credits": estimate,
            "input_stage": input_stage,
            "provider": {
                "server_package": "@meshy-ai/meshy-mcp-server",
                "server_version": os.environ.get("MESHY_MCP_VERSION", "0.4.0"),
            },
            "created_at": utc_now(),
        },
    )
    append_history(
        job,
        state="provider_task_created",
        event=stage,
        actor="meshy_mcp",
        details={"task_id": task_id, "task_type": task_type, "estimated_credits": estimate},
    )
    try:
        final = client.wait_for_task(task_id, task_type=task_type)
    except MeshyTaskFailed as exc:
        save_task(
            job,
            stage,
            task_id=task_id,
            task_type=task_type,
            initial=initial,
            final=exc.final,
            estimate=estimate,
            input_stage=input_stage,
        )
        try:
            balance_after = balance_value(client.check_balance())
            record_paid_reconciliation(
                job,
                stage,
                balance_before=balance_before,
                balance_after=balance_after,
                final=exc.final,
                estimate=estimate,
            )
        except Exception:
            pass
        raise
    save_task(
        job,
        stage,
        task_id=task_id,
        task_type=task_type,
        initial=initial,
        final=final,
        estimate=estimate,
        input_stage=input_stage,
    )
    balance_after = balance_value(client.check_balance())
    record_paid_reconciliation(
        job,
        stage,
        balance_before=balance_before,
        balance_after=balance_after,
        final=final,
        estimate=estimate,
    )
    return task_id


def download_once(
    client: MeshyClient,
    job: Path,
    *,
    stage: str,
    task_id: str,
    task_type: str,
    format_name: str,
    filename: str,
    include_textures: bool = True,
    allow_url_only: bool = False,
    fetch_provider_url: bool = False,
) -> Dict[str, Any]:
    destination = job / "provider" / "downloads" / filename
    manifest = job / "provider" / "downloads" / f"{destination.name}.manifest.json"
    url_manifest = job / "provider" / "downloads" / f"{destination.name}.url.json"
    if destination.exists() and manifest.exists():
        return read_json(manifest)
    if fetch_provider_url and url_manifest.exists():
        url_record = read_json(url_manifest)
        return client.fetch_provider_artifact(
            task_id=task_id,
            task_type=task_type,
            format_name=format_name,
            url=url_record["url"],
            destination=destination,
            include_textures=include_textures,
        )
    if allow_url_only and url_manifest.exists():
        return read_json(url_manifest)
    if destination.exists():
        record = {
            "timestamp": utc_now(),
            "task_id": task_id,
            "task_type": task_type,
            "format": format_name,
            "include_textures": include_textures,
            "file": file_record(destination, relative_to=job),
            "recovered_manifest": True,
        }
        write_json(manifest, record)
        return record
    result = client.download(
        task_id=task_id,
        task_type=task_type,
        format_name=format_name,
        destination=destination,
        include_textures=include_textures,
        allow_url_only=allow_url_only,
    )
    if result.get("url_only") and fetch_provider_url:
        return client.fetch_provider_artifact(
            task_id=task_id,
            task_type=task_type,
            format_name=format_name,
            url=result["url"],
            destination=destination,
            include_textures=include_textures,
        )
    if result.get("url_only"):
        return result
    append_history(
        job,
        state="provider_artifact_downloaded",
        event=stage,
        actor="meshy_mcp",
        details={"task_id": task_id, "format": format_name, "file": result["file"]},
    )
    return result


def candidate_gate(
    job: Path,
    prep: Dict[str, Any],
    *,
    hard_max: int,
    stage: str,
    max_runtime_footprint_m: Optional[float] = None,
    runtime_entity_scale: float = 1.0,
) -> None:
    geometry = prep.get("geometry", {})
    failures = []
    if geometry.get("triangles", 0) <= 0:
        failures.append("no triangles")
    if geometry.get("triangles", 0) > hard_max:
        failures.append(f"triangles exceed hard maximum {hard_max}")
    if geometry.get("degenerate_faces", 0):
        failures.append("degenerate faces remain")
    if geometry.get("negative_scale_objects"):
        failures.append("negative scale remains")
    if max_runtime_footprint_m is not None:
        dimensions = geometry.get("dimensions", [0.0, 0.0, 0.0])
        runtime_footprint = max(float(dimensions[0]), float(dimensions[1])) * runtime_entity_scale
        if runtime_footprint > float(max_runtime_footprint_m) + 1e-5:
            failures.append(
                f"runtime footprint {runtime_footprint:.4f}m exceeds "
                f"budget {float(max_runtime_footprint_m):.4f}m"
            )
    if failures:
        write_json(
            job / "validation" / f"{stage}_gate.json",
            {
                "status": "blocked",
                "failures": failures,
                "geometry": geometry,
                "runtime_footprint": prep.get("runtime_footprint"),
            },
        )
        raise RuntimeError(f"Geometry gate failed for {stage}: {failures}")
    write_json(
        job / "validation" / f"{stage}_gate.json",
        {
            "status": "passed",
            "failures": [],
            "geometry": geometry,
            "runtime_footprint": prep.get("runtime_footprint"),
            "visual_review_required": True,
            "visual_review": "parent_agent_reviewed_preview_set",
        },
    )


def prepare_pilot_texture_sources(job: Path, spec: Dict[str, Any]) -> Dict[str, str]:
    """Create and select the engine-compatible material source maps."""

    provider_sources = dict(spec.get("texture_source_rels", {}))
    spec["_provider_texture_source_rels"] = provider_sources
    sources = prepare_texture_source_rels(job, provider_sources)
    if sources:
        spec["texture_source_rels"] = sources
    return sources


def _finalize_pdx_runtime_texture(
    job: Path,
    spec: Dict[str, Any],
    textures: Dict[str, Any],
    *,
    source_rel: str,
    image_name: str,
    packer: Any,
    report_key: str,
    layout: Dict[str, str],
) -> Dict[str, Any]:
    """Replace one extracted working map with its final PDX-layout DDS."""

    pack_report = packer(job, source_rel)
    if pack_report.get("status") not in {"packed", "already_packed"}:
        return textures
    output_rel = pack_report["output"]["path"]
    packed_source = job / output_rel
    conversion = next(
        (
            item
            for item in textures.get("conversions", [])
            if item.get("image") == image_name
        ),
        None,
    )
    if conversion is None:
        raise RuntimeError(f"No extracted normal texture conversion for {image_name}.")
    processed_rel = f"textures/processed/{image_name}.png"
    processed = job / processed_rel
    if processed.exists():
        if not processed.is_file():
            raise RuntimeError(f"Processed texture target is not a file: {processed}")
        processed.unlink()
    shutil.copy2(packed_source, processed)
    dds_rel = str(conversion["dds"])
    dds = job / dds_rel
    if dds.exists():
        try:
            dds.unlink()
        except OSError as exc:
            raise RuntimeError(f"Unable to replace existing DDS output: {dds}") from exc
    converter = REPO_ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
    converter_args = [
        sys.executable,
        str(converter),
        "--input",
        str(processed),
        "--output",
        str(dds),
    ]
    width = conversion.get("width")
    height = conversion.get("height")
    if width and height:
        converter_args.extend(["--width", str(width), "--height", str(height)])
    completed = subprocess.run(
        converter_args,
        cwd=str(REPO_ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=600,
        check=False,
    )
    if completed.returncode != 0 or not dds.exists():
        raise RuntimeError(f"PDX runtime DDS conversion failed for {dds}.")
    conversion["png"] = processed_rel
    conversion["layout"] = layout
    textures[report_key] = pack_report
    return textures


def _apply_runtime_diffuse_grade(
    job: Path,
    spec: Dict[str, Any],
    textures: Dict[str, Any],
) -> Dict[str, Any]:
    """Make a deliberately dark provider diffuse map readable in the engine.

    The provider source remains immutable. The runtime-derived diffuse map is
    rebuilt from that source on every continuation, so repeated runs never
    compound the grade. A gamma below one lifts near-black cloth without
    flattening the authored seams and hardware detail.
    """

    gamma = float(spec.get("runtime_diffuse_gamma", 1.0))
    if gamma <= 0.0:
        raise ValueError("runtime_diffuse_gamma must be greater than zero.")
    if abs(gamma - 1.0) < 1e-9 or spec["asset_kind"] not in {"humanoid", "creature"}:
        return textures

    provider_sources = dict(
        spec.get("_provider_texture_source_rels")
        or spec.get("texture_source_rels")
        or {}
    )
    source_rel = provider_sources.get("diffuse")
    if not source_rel:
        raise RuntimeError("Runtime diffuse grading requires a provider diffuse source.")
    source = (job / source_rel).resolve()
    if not source.is_file():
        raise FileNotFoundError(f"Runtime diffuse source is missing: {source}")
    conversion = next(
        (
            item
            for item in textures.get("conversions", [])
            if item.get("image") == "texture_0"
        ),
        None,
    )
    if conversion is None:
        raise RuntimeError("No extracted diffuse texture conversion was recorded.")

    width = int(conversion.get("width") or 1024)
    height = int(conversion.get("height") or 1024)
    processed_rel = f"textures/processed/{conversion['image']}.png"
    processed = job / processed_rel
    with Image.open(source) as source_image:
        rgba = source_image.convert("RGBA")
        if rgba.size != (width, height):
            rgba = rgba.resize((width, height), Image.Resampling.LANCZOS)
        lut = [
            int(round(255.0 * ((value / 255.0) ** gamma)))
            for value in range(256)
        ]
        graded_rgb = Image.merge(
            "RGB",
            tuple(channel.point(lut) for channel in rgba.convert("RGB").split()),
        )
        graded = Image.merge("RGBA", (*graded_rgb.split(), rgba.getchannel("A")))
        graded.save(processed, format="PNG", optimize=True)

    dds = job / str(conversion["dds"])
    if dds.exists():
        if not dds.is_file():
            raise RuntimeError(f"Runtime diffuse DDS target is not a file: {dds}")
        dds.unlink()
    converter = REPO_ROOT / ".agents" / "skills" / "chaos-redux-event-assets" / "tools" / "convert_to_dds.py"
    converter_args = [
        sys.executable,
        str(converter),
        "--input",
        str(processed),
        "--output",
        str(dds),
        "--width",
        str(width),
        "--height",
        str(height),
    ]
    completed = subprocess.run(
        converter_args,
        cwd=str(REPO_ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=600,
        check=False,
    )
    if completed.returncode != 0 or not dds.exists():
        raise RuntimeError(f"Runtime diffuse DDS conversion failed for {dds}.")
    conversion["png"] = processed_rel
    textures["runtime_diffuse_grade"] = {
        "source": source_rel,
        "processed": processed_rel,
        "dds": str(conversion["dds"]),
        "gamma": gamma,
        "policy": "provider_source_rebuilt_each_run_with_single_gamma_lift",
    }
    return textures


def finalize_pdx_runtime_textures(
    job: Path,
    spec: Dict[str, Any],
    textures: Dict[str, Any],
) -> Dict[str, Any]:
    """Keep Blender previews conventional while installing PDX runtime DDS maps."""

    textures = _apply_runtime_diffuse_grade(job, spec, textures)
    provider_sources = dict(
        spec.get("_provider_texture_source_rels")
        or spec.get("texture_source_rels")
        or {}
    )
    if spec["asset_kind"] in {"humanoid", "creature"}:
        # The preview binding deliberately uses roughness.png. The runtime
        # binding must always go back to the provider metallic/roughness source
        # so the PDX packed channels cannot silently be replaced by gray RGB.
        specular_source = provider_sources.get("specular")
        if not specular_source or Path(specular_source).name.casefold() == "roughness.png":
            candidate = job / "provider" / "downloads" / "generation_model_textures" / "metallic_roughness.png"
            if not candidate.is_file():
                raise FileNotFoundError(
                    "Humanoid runtime material finalization requires the provider metallic_roughness.png map."
                )
            provider_sources["specular"] = str(candidate.relative_to(job)).replace("\\", "/")
    image_names = {
        "diffuse": "texture_0" if spec["asset_kind"] in {"humanoid", "creature"} else "Image_0",
        "specular": "texture_specular" if spec["asset_kind"] in {"humanoid", "creature"} else "Image_1",
        "normal": "texture_normal" if spec["asset_kind"] in {"humanoid", "creature"} else "Image_2",
    }
    specular_rel = provider_sources.get("specular")
    if specular_rel:
        textures = _finalize_pdx_runtime_texture(
            job,
            spec,
            textures,
            source_rel=specular_rel,
            image_name=image_names["specular"],
            packer=pack_pdx_specular_map,
            report_key="pdx_specular_pack",
            layout={
                "red": "unused_mask_zero",
                "green": "specular_level_32",
                "blue": "metallic",
                "alpha": "roughness",
            },
        )
    normal_rel = provider_sources.get("normal")
    if normal_rel:
        textures = _finalize_pdx_runtime_texture(
            job,
            spec,
            textures,
            source_rel=normal_rel,
            image_name=image_names["normal"],
            packer=pack_pdx_normal_map,
            report_key="pdx_normal_pack",
            layout={
                "red": "unused_zero",
                "green": "source_normal_red_tangent_x",
                "blue": "unused_zero",
                "alpha": "source_normal_green_tangent_y",
            },
        )
    report = job / "blender" / "reports" / "textures_dds.json"
    textures["runtime_texture_sources"] = provider_sources
    report.write_text(json.dumps(textures, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return textures


def run_candidate(spec: Dict[str, Any]) -> Dict[str, Any]:
    slug = spec["asset_id"].rsplit(".", 1)[-1]
    job = ensure_job_layout(resolve_job_root(slug))
    client = MeshyClient(REPO_ROOT, job)
    blender = BlenderAdapterClient(REPO_ROOT)
    vanilla_reference = stage_vanilla_reference(job, spec)
    generation_stage = generation_stage_for(spec)
    # The legacy unrecorded-task recovery scans response names that do not
    # contain a logical attempt id. Restrict it to the original stage so a
    # rejected response can never be mistaken for an explicitly authorised
    # recovery attempt.
    if generation_stage == "generation":
        recover_unrecorded_task(
            job,
            stage=generation_stage,
            task_type="image-to-3d",
            estimate=spec["image_to_3d_estimate_credits"],
            response_name_fragment="image_to_3d",
        )
    reference = job / spec["reference_path"]
    generation_id = provider_task(
        client,
        job,
        generation_stage,
        task_type="image-to-3d",
        estimate=spec["image_to_3d_estimate_credits"],
        create=lambda: client.image_to_3d(
            image_path=reference,
            ai_model=spec["meshy_ai_model"],
            model_type="standard",
            pose_mode=spec["meshy_pose_mode"],
            target_polycount=spec["target_polycount"],
            estimate_credits=spec["image_to_3d_estimate_credits"],
        ),
    )
    generation_glb = download_once(
        client,
        job,
        stage=f"{generation_stage}_glb",
        task_id=generation_id,
        task_type="image-to-3d",
        format_name="glb",
        filename=generation_download_name(spec, "glb"),
    )
    download_once(
        client,
        job,
        stage=f"{generation_stage}_fbx",
        task_id=generation_id,
        task_type="image-to-3d",
        format_name="fbx",
        filename=generation_download_name(spec, "fbx"),
    )
    profile = read_json(PIPELINE_ROOT / "config" / "asset_profiles.json")["profiles"][spec["profile"]]
    footprint_config = profile.get("footprint", {})
    max_runtime_footprint_m = footprint_config.get("max_runtime_footprint_m")
    runtime_footprint_policy = spec.get("runtime_footprint_policy", "reject")
    texture_sources = (
        prepare_pilot_texture_sources(job, spec)
        if spec["asset_kind"] in STATIC_ASSET_KINDS | {"humanoid", "creature"}
        else {}
    )
    prep = blender.prepare_candidate(
        slug,
        source_rel=generation_glb["file"]["relative_path"],
        asset_kind=spec["asset_kind"],
        target_height_m=spec.get("blender_target_height_m", spec["target_height_m"]),
        runtime_entity_scale=float(spec.get("runtime_entity_scale", 1.0)),
        runtime_stem=f"{spec['runtime_stem']}_candidate",
        target_triangles=profile["triangle_range"]["working_triangle_target"],
        vanilla_reference=vanilla_reference,
        texture_source_rels=texture_sources,
        max_runtime_footprint_m=max_runtime_footprint_m,
        runtime_footprint_policy=runtime_footprint_policy,
    )
    candidate_gate(
        job,
        prep,
        hard_max=profile["triangle_range"]["hard_max"],
        stage="provider_candidate",
        max_runtime_footprint_m=max_runtime_footprint_m,
        runtime_entity_scale=float(spec.get("runtime_entity_scale", 1.0)),
    )
    update_job(job, status="candidate_qa", selected_provider_task=generation_id)
    append_history(
        job,
        state="candidate_qa",
        event="blender_candidate_prepared",
        actor="chaosx_3d_model_pipeline",
        details={
            "generation_task_id": generation_id,
            "checkpoint": prep["checkpoints"]["pre_export"],
            "previews": prep["previews"],
        },
    )
    return {
        "slug": slug,
        "job_root": str(job),
        "generation_task_id": generation_id,
        "generation_glb": generation_glb,
        "prepare": prep,
    }


def continue_static(spec: Dict[str, Any]) -> Dict[str, Any]:
    slug = spec["asset_id"].rsplit(".", 1)[-1]
    job = ensure_job_layout(resolve_job_root(slug))
    blender = BlenderAdapterClient(REPO_ROOT)
    prep_report = read_json(job / "blender" / "reports" / f"{spec['runtime_stem']}_candidate_prepare.json")
    pre_export = prep_report["checkpoints"]["pre_export"]
    textures = finalize_pdx_runtime_textures(
        job,
        spec,
        blender.process_textures(slug, pre_export),
    )
    mesh_rel = f"export/mesh/{spec['runtime_stem']}.mesh"
    exported = blender.export_mesh(slug, pre_export, mesh_rel)
    reimport = blender.reimport_export(slug, mesh_rel)
    mesh_file = job / mesh_rel
    update_job(job, status="pdx_exported", exports={"mesh": mesh_rel})
    append_history(
        job,
        state="pdx_exported",
        event="static_pilot_exported",
        actor="chaosx_3d_model_pipeline",
        details={"mesh": file_record(mesh_file, relative_to=job), "reimport": reimport},
    )
    return {"textures": textures, "export": exported, "reimport": reimport}


def _specialized_zombie_spec(slug: str, job_root: Path, job: Dict[str, Any]) -> Dict[str, Any]:
    """Build a pilot spec from a repository-owned specialized zombie job manifest."""

    asset_profiles = read_json(PIPELINE_ROOT / "config" / "asset_profiles.json")["profiles"]
    job_profile_name = str(job.get("profile") or "humanoid_unit")
    is_creature = job_profile_name.startswith("nonhumanoid")
    profile_name = (
        "nonhumanoid_winged_biped"
        if job_profile_name in {"nonhumanoid_winged_creature", "nonhumanoid_winged_biped"}
        else "nonhumanoid_creature"
        if is_creature
        else "humanoid_unit"
    )
    profile = asset_profiles[profile_name]
    manifest_path = job_root / "refs" / "original" / "input_manifest.json"
    manifest = read_json(manifest_path) if manifest_path.exists() else {}
    brief_path = job_root / "refs" / "briefs" / "meshy_input_prompt.md"
    brief = brief_path.read_text(encoding="utf-8") if brief_path.exists() else str(job.get("brief", ""))
    provider_plan = job.get("provider_plan", {})
    blender_plan = job.get("blender_plan", {})
    vanilla_plan = blender_plan.get("vanilla_scale_reference", {})
    vanilla_root = Path("C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV")
    raw_vanilla_mesh = vanilla_plan.get("mesh") or profile["vanilla_reference"]["mesh"]
    vanilla_mesh = Path(str(raw_vanilla_mesh))
    if not vanilla_mesh.is_absolute():
        vanilla_mesh = vanilla_root / vanilla_mesh
    raw_vanilla_height = (
        job.get("vanilla_height")
        or blender_plan.get("target_height_m")
        or profile["vanilla_reference"]["mesh_height"]
    )
    raw_entity_scale = (
        job.get("entity_scale")
        or blender_plan.get("runtime_entity_scale")
        or profile["vanilla_reference"]["entity_scale"]
    )
    reference_path = str(
        job.get("reference")
        or job.get("meshy_input_gate", {}).get("image")
        or "refs/original/meshy_input.png"
    )
    try:
        vanilla_height = float(raw_vanilla_height)
        entity_scale = float(raw_entity_scale)
    except (TypeError, ValueError):
        if not is_creature:
            raise ValueError(
                f"{slug} has a non-numeric humanoid scale crosswalk: "
                f"vanilla_height={raw_vanilla_height!r}, entity_scale={raw_entity_scale!r}"
            )
        return {
            "asset_id": f"chaosx.model.pilot.{slug}",
            "asset_kind": "creature",
            "profile": profile_name,
            "reference_path": reference_path,
            "reference_generator_output": None,
            "reference_source_mode": manifest.get("source_mode", "native_imagegen_portrait_reference"),
            "asset_brief": brief,
            "runtime_stem": str(
                job.get("runtime_stem")
                or blender_plan.get("runtime_stem")
                or f"chaosx_{slug}"
            ),
            "proposed_runtime_identifiers": {
                "entity": str(
                    job.get("entity")
                    or job.get("runtime", {}).get("proposed_identifiers", {}).get("entity")
                    or f"chaosx_{slug}_entity"
                ),
                "consumer": "land-unit entity",
                "route": "custom creature rig",
            },
            "scale_crosswalk": job.get("scale_crosswalk"),
            "_requires_reference_approval": True,
            "_route_status": "pending_creature_scale_crosswalk",
            "_route_blocker": (
                "The job manifest intentionally has no numeric creature scale crosswalk. "
                "Measure the approved creature against the installed infantry runtime reference "
                "before enabling paid generation or export."
            ),
            "_job_root": str(job_root),
        }
    runtime_stem = str(job.get("runtime_stem") or blender_plan.get("runtime_stem") or f"chaosx_{slug}")
    entity = str(
        job.get("entity")
        or job.get("runtime", {}).get("proposed_identifiers", {}).get("entity")
        or f"{runtime_stem}_entity"
    )
    target_triangles = int(
        job.get("target_triangles")
        or provider_plan.get("target_polycount")
        or profile["triangle_range"]["working_triangle_target"]
    )
    rig_source_target_polycount = int(
        job.get("rig_source_target_polycount")
        or provider_plan.get("rig_source_target_polycount")
        or target_triangles
    )
    vanilla_reference = {
        "mesh": str(vanilla_mesh),
        "entity": profile["vanilla_reference"]["entity"],
        "mesh_object_names": profile["vanilla_reference"]["mesh_object_names"],
        "exclude_name_patterns": profile["vanilla_reference"]["exclude_name_patterns"],
        "forward_axis": profile["vanilla_reference"]["forward_axis"],
        "up_axis": profile["vanilla_reference"]["up_axis"],
        "mesh_height": vanilla_height,
        "entity_scale": entity_scale,
        "runtime_height": vanilla_height * entity_scale,
    }
    creature_rig_family = (
        str(
            job.get("creature_rig_family")
            or ("winged_biped" if job_profile_name in {"nonhumanoid_winged_creature", "nonhumanoid_winged_biped"} else "quadruped")
        )
        if is_creature
        else "humanoid"
    )
    if is_creature and creature_rig_family != "winged_biped":
        route_status = "pending_creature_rig_route"
        route_blocker = (
            f"The selected creature rig family {creature_rig_family!r} has no enabled generic pilot route."
        )
    else:
        route_status = "ready"
        route_blocker = None
    required_components = (
        [
            "complete portrait-matched nonhumanoid body",
            "attached wings and stable digitigrade silhouette",
            "custom creature rig with rigid semantic components",
        ]
        if is_creature
        else [
            "complete portrait-matched humanoid body",
            "distinctive specialized zombie silhouette",
            "grounded riggable infantry proportions",
        ]
    )
    required_actions = (
        [
            {"role": role, "provider_action_id": None, "task_type": "blender_authored_skeletal", "fps": int(job.get("fps", 30)), "loop": role in {"idle", "move"}, "root_policy": "in_place"}
            for role in ("idle", "move", "attack", "death")
        ]
        if is_creature
        else [
            {"role": "idle", "provider_action_id": 0, "fps": 24, "loop": True, "root_policy": "in_place"},
            {"role": "move", "provider_action_id": None, "task_type": "blender_authored_skeletal", "fps": 24, "loop": True, "root_policy": "in_place"},
            {"role": "attack", "provider_action_id": 4, "fps": 24, "loop": False, "root_policy": "in_place"},
            {"role": "death", "provider_action_id": 8, "fps": 24, "loop": False, "root_policy": "in_place"},
        ]
    )
    meshy_ai_model = str(job.get("provider_model") or provider_plan.get("ai_model") or "meshy-7")
    resolved_meshy_ai_model = str(
        job.get("resolved_provider_model")
        or provider_plan.get("resolved_ai_model")
        or meshy_ai_model
    )
    if meshy_ai_model.lower() != "meshy-7" or resolved_meshy_ai_model.lower() != "meshy-7":
        raise RuntimeError(
            "The Chaos Redux 3D workflow requires explicit Meshy 7 generation. "
            f"Received provider_model={meshy_ai_model!r}, "
            f"resolved_provider_model={resolved_meshy_ai_model!r}."
        )
    generation_stage = str(job.get("generation_stage") or "generation")
    image_to_3d_estimate = int(
        job.get("image_to_3d_estimate_credits") or MESHY_TEXTURED_IMAGE_TO_3D_ESTIMATE
    )
    if meshy_ai_model.lower() in MESHY_TEXTURED_IMAGE_MODEL_IDS and bool(provider_plan.get("should_texture", True)):
        # A stale job manifest may still contain a 20-credit no-texture
        # estimate. Never under-preflight the required textured Meshy 7 route.
        image_to_3d_estimate = max(image_to_3d_estimate, MESHY_TEXTURED_IMAGE_TO_3D_ESTIMATE)
    remesh_estimate = int(job.get("remesh_estimate_credits") or MESHY_REMESH_ESTIMATE)
    rig_estimate = int(job.get("rig_estimate_credits") or 5)
    animation_estimate = int(job.get("animation_estimate_credits") or 3)
    planned_total = int(
        job.get("estimated_credits")
        or (
            image_to_3d_estimate
            if is_creature
            else image_to_3d_estimate + remesh_estimate + rig_estimate + (3 * animation_estimate)
        )
    )
    required_minimum = (
        image_to_3d_estimate
        if is_creature
        else image_to_3d_estimate + remesh_estimate + rig_estimate + (3 * animation_estimate)
    )
    return {
        "asset_id": f"chaosx.model.pilot.{slug}",
        "asset_kind": "creature" if is_creature else "humanoid",
        "profile": profile_name,
        "reference_path": reference_path,
        "reference_generator_output": None,
        "reference_source_mode": manifest.get("source_mode", "native_imagegen_portrait_reference"),
        "asset_brief": brief,
        "required_components": required_components,
        "forbidden_additions": [
            "weapons",
            "extra characters",
            "floating disconnected geometry",
            "multi-view board",
            "turnaround collage",
            "text or watermark",
        ],
        "excluded_provider_objects": list(
            job.get("excluded_provider_objects")
            or (["Icosphere"] if not is_creature else [])
        ),
        "target_height_m": vanilla_height,
        "blender_target_height_m": vanilla_height,
        "blender_effective_runtime_height_m": vanilla_height * entity_scale,
        "runtime_entity_scale": entity_scale,
        "runtime_diffuse_gamma": profile.get("runtime_diffuse_gamma"),
        "vanilla_scale_reference": vanilla_reference,
        "target_polycount": target_triangles,
        "rig_source_target_polycount": rig_source_target_polycount,
        "meshy_ai_model": meshy_ai_model,
        "resolved_meshy_ai_model": resolved_meshy_ai_model,
        "meshy_pose_mode": provider_plan.get("pose_mode"),
        # Textured Meshy 7 generation is billed at 30 credits. Keep this
        # fallback aligned with the required textured request.
        "image_to_3d_estimate_credits": image_to_3d_estimate,
        "remesh_estimate_credits": remesh_estimate,
        "rig_estimate_credits": rig_estimate,
        "animation_estimate_credits": animation_estimate,
        "planned_total_credits": max(planned_total, required_minimum),
        "generation_stage": generation_stage,
        "rig_stage": job.get("rig_stage"),
        "rig_input_mode": str(job.get("rig_input_mode") or "input_task_id"),
        "humanoid_rig_route": str(job.get("humanoid_rig_route") or ""),
        "provider_paid_attempts": int(provider_plan.get("paid_attempts") or 1),
        "provider_retry_paid_calls": bool(provider_plan.get("retry_paid_calls", False)),
        "texture_source_rels": {
            "diffuse": f"provider/downloads/{generation_stage}_model_textures/base_color.png",
            "normal": f"provider/downloads/{generation_stage}_model_textures/normal.png",
            "specular": f"provider/downloads/{generation_stage}_model_textures/metallic_roughness.png",
        },
        "required_actions": required_actions,
        "creature_rig_family": creature_rig_family,
        "scale_crosswalk": job.get(
            "scale_crosswalk",
            "overall_creature_height_matches_western_european_infantry_runtime"
            if is_creature
            else None,
        ),
        "runtime_stem": runtime_stem,
        "shared_humanoid_batch": job.get("shared_humanoid_batch"),
        "shared_humanoid_rig_owner": job.get("shared_humanoid_rig_owner"),
        "shared_humanoid_role": job.get("shared_humanoid_role"),
        "proposed_runtime_identifiers": {
            "pdxmesh": f"{runtime_stem}_mesh",
            "entity": entity,
            "consumer": "land-unit entity",
            "entity_scale": entity_scale,
        },
        "_requires_reference_approval": True,
        "_route_status": route_status,
        "_route_blocker": route_blocker,
        "_job_root": str(job_root),
    }


def load_pilot_configs() -> Dict[str, Dict[str, Any]]:
    """Load generic pilots and discover configured specialized zombie jobs."""

    configs = read_json(PIPELINE_ROOT / "config" / "pilot_jobs.json")["pilots"]
    adapter_config = read_json(PIPELINE_ROOT / "config" / "blender_hoi4_adapter.json")
    for slug, raw_root in adapter_config.get("job_overrides", {}).items():
        if slug in {"zombies", "wendigo_zombies"} or not slug.endswith("_zombies"):
            continue
        job_root = Path(str(raw_root)).resolve()
        job_file = job_root / "job.yaml"
        if not job_file.exists():
            continue
        job = read_job_document(job_file)
        configs[slug] = _specialized_zombie_spec(slug, job_root, job)
    return configs


def require_reference_approval(spec: Dict[str, Any]) -> None:
    """Block paid generation until the parent has accepted the exact provider image."""

    if not spec.get("_requires_reference_approval"):
        return
    job_root = resolve_job_root(spec["asset_id"].rsplit(".", 1)[-1])
    manifest_path = job_root / "refs" / "original" / "input_manifest.json"
    manifest = read_json(manifest_path)
    status = str(manifest.get("candidate_status", "needs_user_visual_approval"))
    if status not in {"user_accepted", "accepted", "approved"}:
        raise RuntimeError(
            f"{job_root.name} reference status is {status!r}; paid generation requires explicit user visual approval."
        )


def require_route_ready(spec: Dict[str, Any]) -> None:
    """Refuse a job whose asset class has not completed its calibrated route design."""

    status = str(spec.get("_route_status", "ready"))
    if status == "ready":
        return
    blocker = str(spec.get("_route_blocker") or "The selected asset route is not ready.")
    raise RuntimeError(
        f"{spec['asset_id']} is blocked before provider work: route_status={status}; {blocker}"
    )


def require_live_blender_authored_continuation(spec: Dict[str, Any]) -> None:
    """Refuse a continuation whose rig, weights and actions Python no longer authors."""

    if spec["asset_kind"] in STATIC_ASSET_KINDS:
        return
    raise RuntimeError(
        f"{spec['asset_id']} is a {spec['asset_kind']!r} asset. Rigging, skinning and skeletal "
        "actions are authored live in Blender through the Blender MCP bridge; repository Python "
        "no longer creates or edits bones, skin weights or keyframes from declarative specs. Run "
        "--phase candidate for the provider geometry, then rig and animate that candidate live "
        "in Blender."
    )


def preflight_selected_credits(specs: List[Dict[str, Any]], phase: str) -> None:
    """Check the full selected tranche before any paid provider call."""

    if not specs:
        return
    estimates = []
    for spec in specs:
        if not spec.get("_requires_reference_approval"):
            continue
        estimate = (
            int(spec["image_to_3d_estimate_credits"])
            if phase == "candidate"
            else int(spec.get("planned_total_credits", 44 if spec.get("asset_kind") == "humanoid" else 30))
        )
        estimates.append((spec["asset_id"], estimate))
    total = sum(value for _, value in estimates)
    if total == 0:
        return
    result = MeshyClient(REPO_ROOT).check_balance()
    balance = balance_value(result)
    if balance is None:
        raise RuntimeError("Meshy balance preflight returned no numeric balance.")
    if balance < total:
        breakdown = ", ".join(f"{asset}={estimate}" for asset, estimate in estimates)
        raise RuntimeError(
            f"Meshy batch gate refused paid work: balance={balance}, required={total}; {breakdown}"
        )


def main() -> int:
    configs = load_pilot_configs()
    args = sys.argv[1:]
    if "--specialized-zombie-batch" in args:
        index = args.index("--specialized-zombie-batch")
        if index + 1 >= len(args) or args[index + 1].startswith("-"):
            raise RuntimeError("--specialized-zombie-batch requires a configured batch id.")
        raise RuntimeError(
            "--specialized-zombie-batch is a removed repository-owned batch route. Rigging, "
            "skinning and skeletal actions are authored live in Blender through the Blender MCP "
            "bridge; repository Python no longer creates or edits bones, skin weights or "
            "keyframes from declarative specs. Generate every selected unit with --phase "
            "candidate, then rig and animate each candidate live in Blender."
        )
    all_assets = "--all" in args or not args
    assets = list(configs) if all_assets else [item for item in args if not item.startswith("-")]
    phase = "full"
    phase_value = None
    if "--phase" in args:
        phase_value = args[args.index("--phase") + 1]
        phase = phase_value
    excluded = {"--all", "--phase", phase_value}
    results = []
    assets = [item for item in assets if item not in excluded]
    selected_specs = [configs[item] for item in assets]
    for spec in selected_specs:
        require_route_ready(spec)
        require_reference_approval(spec)
        if phase != "candidate":
            require_live_blender_authored_continuation(spec)
    if phase in {"full", "candidate"}:
        preflight_selected_credits(selected_specs, phase)
    for asset in assets:
        spec = configs[asset]
        initialize_one(spec)
        if phase in {"full", "candidate"}:
            candidate = run_candidate(spec)
            results.append({"asset": asset, "candidate": candidate})
        if phase == "candidate":
            continue
        require_live_blender_authored_continuation(spec)
        results.append({"asset": asset, "continuation": continue_static(spec)})
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

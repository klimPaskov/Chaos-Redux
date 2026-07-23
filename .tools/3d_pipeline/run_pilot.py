"""Run one or both autonomous 3D model pilots through Meshy and Blender."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


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
    read_json,
    resolve_job_root,
    utc_now,
    write_json,
)
from meshy_client import (  # noqa: E402
    MeshyClient,
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


def task_file(job: Path, stage: str) -> Path:
    return job / "provider" / "tasks" / f"{stage}.json"


def read_job(job: Path) -> Dict[str, Any]:
    return json.loads((job / "job.yaml").read_text(encoding="utf-8"))


def stage_vanilla_reference(job: Path, spec: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Stage the named installed vanilla reference inside the bounded job root."""

    if spec.get("asset_kind") != "humanoid":
        return None
    reference = spec.get("vanilla_scale_reference") or {}
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


def existing_task(job: Path, stage: str) -> Optional[Dict[str, Any]]:
    path = task_file(job, stage)
    return read_json(path) if path.exists() else None


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
            final = client.wait_for_task(
                str(existing["task_id"]),
                task_type=task_type,
            )
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
    record_balance(job, stage, balance_result, estimate)
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
    final = client.wait_for_task(task_id, task_type=task_type)
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


def candidate_gate(job: Path, prep: Dict[str, Any], *, hard_max: int, stage: str) -> None:
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
    if failures:
        write_json(
            job / "validation" / f"{stage}_gate.json",
            {"status": "blocked", "failures": failures, "geometry": geometry},
        )
        raise RuntimeError(f"Geometry gate failed for {stage}: {failures}")
    write_json(
        job / "validation" / f"{stage}_gate.json",
        {
            "status": "passed",
            "failures": [],
            "geometry": geometry,
            "visual_review_required": True,
            "visual_review": "parent_agent_reviewed_preview_set",
        },
    )


def action_name_for_role(prep: Dict[str, Any], role: str) -> str:
    """Resolve a provider animation's actual Blender action name."""

    actions = prep.get("rig_and_actions", {}).get("actions", [])
    if not actions:
        raise RuntimeError(f"No Blender actions were imported for required role {role!r}.")
    matches = [
        action for action in actions
        if role.casefold() in str(action.get("name", "")).casefold()
    ]
    working_matches = [
        action for action in matches
        if "working" in str(action.get("name", "")).casefold()
    ]
    if len(working_matches) == 1:
        return str(working_matches[0]["name"])
    if len(matches) == 1:
        return str(matches[0]["name"])
    if len(actions) == 1:
        return str(actions[0]["name"])
    raise RuntimeError(
        f"Could not unambiguously map provider action role {role!r}: "
        + json.dumps(actions, sort_keys=True)
    )


def exported_animation_path(report: Dict[str, Any]) -> str:
    """Return the recorded animation path from either adapter response shape."""

    export = report.get("export", {})
    for key in ("anim", "animation", "output_rel"):
        value = export.get(key)
        if isinstance(value, str) and value:
            return value
    fallback = report.get("output_rel")
    if isinstance(fallback, str) and fallback:
        return fallback
    raise ValueError(f"Animation export response did not contain an output path: {export!r}")


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


def finalize_pdx_runtime_textures(
    job: Path,
    spec: Dict[str, Any],
    textures: Dict[str, Any],
) -> Dict[str, Any]:
    """Keep Blender previews conventional while installing PDX runtime DDS maps."""

    provider_sources = spec.get("_provider_texture_source_rels") or spec.get("texture_source_rels") or {}
    image_names = {
        "diffuse": "texture_0" if spec["asset_kind"] == "humanoid" else "Image_0",
        "specular": "texture_specular" if spec["asset_kind"] == "humanoid" else "Image_1",
        "normal": "texture_normal" if spec["asset_kind"] == "humanoid" else "Image_2",
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
                "red": "source_normal_red",
                "green": "unused_zero",
                "blue": "unused_zero",
                "alpha": "source_normal_green",
            },
        )
    report = job / "blender" / "reports" / "textures_dds.json"
    report.write_text(json.dumps(textures, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return textures


def run_candidate(spec: Dict[str, Any]) -> Dict[str, Any]:
    slug = spec["asset_id"].rsplit(".", 1)[-1]
    job = ensure_job_layout(resolve_job_root(slug))
    client = MeshyClient(REPO_ROOT, job)
    blender = BlenderAdapterClient(REPO_ROOT)
    vanilla_reference = stage_vanilla_reference(job, spec)
    generation_stage = "generation"
    generation = recover_unrecorded_task(
        job,
        stage=generation_stage,
        task_type="image-to-3d",
        estimate=spec["image_to_3d_estimate_credits"],
        response_name_fragment="image_to_3d",
    )
    if generation:
        generation_id = str(generation["task_id"])
    else:
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
        stage="generation_glb",
        task_id=generation_id,
        task_type="image-to-3d",
        format_name="glb",
        filename="generation_model.glb",
    )
    download_once(
        client,
        job,
        stage="generation_fbx",
        task_id=generation_id,
        task_type="image-to-3d",
        format_name="fbx",
        filename="generation_model.fbx",
    )
    profile = read_json(PIPELINE_ROOT / "config" / "asset_profiles.json")["profiles"][spec["profile"]]
    texture_sources = (
        prepare_pilot_texture_sources(job, spec)
        if spec["asset_kind"] == "static"
        else {}
    )
    prep = blender.prepare_candidate(
        slug,
        source_rel=generation_glb["file"]["relative_path"],
        asset_kind=spec["asset_kind"],
        target_height_m=spec.get("blender_target_height_m", spec["target_height_m"]),
        runtime_stem=f"{spec['runtime_stem']}_candidate",
        target_triangles=profile["triangle_range"]["working_triangle_target"],
        vanilla_reference=vanilla_reference,
        texture_source_rels=texture_sources,
    )
    candidate_gate(
        job,
        prep,
        hard_max=profile["triangle_range"]["hard_max"],
        stage="provider_candidate",
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


def continue_humanoid(spec: Dict[str, Any]) -> Dict[str, Any]:
    slug = spec["asset_id"].rsplit(".", 1)[-1]
    job = ensure_job_layout(resolve_job_root(slug))
    client = MeshyClient(REPO_ROOT, job)
    blender = BlenderAdapterClient(REPO_ROOT)
    vanilla_reference = stage_vanilla_reference(job, spec)
    generation = existing_task(job, "generation")
    if not generation:
        raise RuntimeError("Humanoid generation must be completed before continuation.")
    generation_id = str(generation["task_id"])

    candidate_report = read_json(
        job / "blender" / "reports" / f"{spec['runtime_stem']}_candidate_prepare.json"
    )
    rig_input_id = generation_id
    remesh_id: Optional[str] = None
    source_triangles = int(candidate_report.get("imported_geometry", {}).get("triangles", 0))
    if source_triangles > 300000:
        remesh_id = provider_task(
            client,
            job,
            "rig_remesh",
            task_type="remesh",
            estimate=spec["remesh_estimate_credits"],
            input_stage="generation",
            create=lambda: client.remesh(
                input_task_id=generation_id,
                target_polycount=spec["rig_source_target_polycount"],
                estimate_credits=spec["remesh_estimate_credits"],
            ),
        )
        remesh_glb = download_once(
            client,
            job,
            stage="rig_remesh_glb",
            task_id=remesh_id,
            task_type="remesh",
            format_name="glb",
            filename="remesh_model.glb",
        )
        download_once(
            client,
            job,
            stage="rig_remesh_fbx",
            task_id=remesh_id,
            task_type="remesh",
            format_name="fbx",
            filename="remesh_model.fbx",
        )
        prepare_pilot_texture_sources(job, spec)
        rig_input_id = remesh_id

    rig_id = provider_task(
        client,
        job,
        "rig",
        task_type="rigging",
        estimate=spec["rig_estimate_credits"],
        input_stage="rig_remesh" if remesh_id else "generation",
        create=lambda: client.rig(
            input_task_id=rig_input_id,
            height_meters=spec["target_height_m"],
            estimate_credits=spec["rig_estimate_credits"],
        ),
    )
    rig_glb = download_once(
        client,
        job,
        stage="rigged_provider_glb",
        task_id=rig_id,
        task_type="rigging",
        format_name="glb",
        filename="rigged_provider_model.glb",
        include_textures=False,
        allow_url_only=True,
        fetch_provider_url=True,
    )
    download_once(
        client,
        job,
        stage="rigged_provider_fbx",
        task_id=rig_id,
        task_type="rigging",
        format_name="fbx",
        filename="rigged_provider_model.fbx",
        include_textures=False,
        allow_url_only=True,
        fetch_provider_url=True,
    )

    animation_downloads: Dict[str, Dict[str, Any]] = {}
    for action in spec["required_actions"]:
        role = action["role"]
        stage = f"animation_{role}"
        animation_id = provider_task(
            client,
            job,
            stage,
            task_type="animation",
            estimate=spec["animation_estimate_credits"],
            input_stage="rig",
            create=lambda action_id=action["provider_action_id"]: client.animate(
                rig_task_id=rig_id,
                action_id=action_id,
                estimate_credits=spec["animation_estimate_credits"],
            ),
        )
        animation_downloads[role] = download_once(
            client,
            job,
            stage=f"{stage}_provider_glb",
            task_id=animation_id,
            task_type="animation",
            format_name="glb",
            filename=f"animation_{role}_provider.glb",
            include_textures=False,
            allow_url_only=True,
            fetch_provider_url=True,
        )
        download_once(
            client,
            job,
            stage=f"{stage}_provider_fbx",
            task_id=animation_id,
            task_type="animation",
            format_name="fbx",
            filename=f"animation_{role}_provider.fbx",
            include_textures=False,
            allow_url_only=True,
            fetch_provider_url=True,
        )

    profile = read_json(PIPELINE_ROOT / "config" / "asset_profiles.json")["profiles"][spec["profile"]]

    final_source = animation_downloads["attack"]["file"]["relative_path"]
    texture_sources = prepare_pilot_texture_sources(job, spec)
    prep = blender.prepare_candidate(
        slug,
        source_rel=final_source,
        asset_kind="humanoid",
        target_height_m=spec.get("blender_target_height_m", spec["target_height_m"]),
        runtime_stem=f"{spec['runtime_stem']}_attack",
        target_triangles=profile["triangle_range"]["working_triangle_target"],
        excluded_provider_objects=spec.get("excluded_provider_objects"),
        vanilla_reference=vanilla_reference,
        texture_source_rels=texture_sources,
    )
    candidate_gate(
        job,
        prep,
        hard_max=profile["triangle_range"]["hard_max"],
        stage="animated_candidate_attack",
    )
    textures = finalize_pdx_runtime_textures(
        job,
        spec,
        blender.process_textures(slug, prep["checkpoints"]["pre_export"]),
    )
    blender.save_checkpoint(
        slug,
        prep["checkpoints"]["pre_export"],
        "attack_pre_export",
    )
    attack_blend = "blender/checkpoints/attack_pre_export.blend"
    mesh_rel = f"export/mesh/{spec['runtime_stem']}.mesh"
    mesh_export = blender.export_mesh(slug, attack_blend, mesh_rel)
    action_reports: Dict[str, Dict[str, Any]] = {}
    attack_action_name = action_name_for_role(prep, "attack")
    attack_anim_rel = "export/anim/chaosx_anomaly_recon_trooper_attack.anim"
    attack_anim_export = blender.export_animation(
        slug,
        attack_blend,
        attack_action_name,
        attack_anim_rel,
    )
    action_reports["attack"] = {
        "required_role": "attack",
        "action_name": attack_action_name,
        "source_checkpoint": attack_blend,
        "export": attack_anim_export,
        "output_rel": attack_anim_rel,
        "loop": False,
        "frame_policy": next(
            item.get("frame_policy", "provider_native_fps_in_place")
            for item in spec["required_actions"]
            if item["role"] == "attack"
        ),
    }
    attack_reimport = blender.reimport_export(
        slug,
        mesh_rel,
        attack_anim_rel,
        proof_name="chaosx_anomaly_recon_trooper_attack",
    )

    idle_source = animation_downloads["idle"]["file"]["relative_path"]
    idle_prep = blender.prepare_candidate(
        slug,
        source_rel=idle_source,
        asset_kind="humanoid",
        target_height_m=spec.get("blender_target_height_m", spec["target_height_m"]),
        runtime_stem=f"{spec['runtime_stem']}_idle",
        target_triangles=profile["triangle_range"]["working_triangle_target"],
        excluded_provider_objects=spec.get("excluded_provider_objects"),
        vanilla_reference=vanilla_reference,
        texture_source_rels=texture_sources,
    )
    candidate_gate(
        job,
        idle_prep,
        hard_max=profile["triangle_range"]["hard_max"],
        stage="animated_candidate_idle",
    )
    blender.save_checkpoint(
        slug,
        idle_prep["checkpoints"]["pre_export"],
        "idle_pre_export",
    )
    idle_blend = "blender/checkpoints/idle_pre_export.blend"
    idle_action_name = action_name_for_role(idle_prep, "idle")
    idle_anim_rel = "export/anim/chaosx_anomaly_recon_trooper_idle.anim"
    idle_anim_export = blender.export_animation(
        slug,
        idle_blend,
        idle_action_name,
        idle_anim_rel,
    )
    action_reports["idle"] = {
        "required_role": "idle",
        "action_name": idle_action_name,
        "source_checkpoint": idle_blend,
        "export": idle_anim_export,
        "output_rel": idle_anim_rel,
        "loop": True,
        "frame_policy": next(
            item.get("frame_policy", "provider_native_fps_in_place")
        for item in spec["required_actions"]
            if item["role"] == "idle"
        ),
    }
    idle_reimport = blender.reimport_export(
        slug,
        mesh_rel,
        idle_anim_rel,
        proof_name="chaosx_anomaly_recon_trooper_idle",
    )
    move_action_name = "Armature|Move|baselayer_WORKING"
    move_blend = "blender/checkpoints/move_pre_export.blend"
    move_authoring = blender.author_locomotion_action(
        slug,
        idle_blend,
        move_blend,
        move_action_name,
    )
    move_anim_rel = "export/anim/chaosx_anomaly_recon_trooper_move.anim"
    move_anim_export = blender.export_animation(
        slug,
        move_blend,
        move_action_name,
        move_anim_rel,
    )
    move_reimport = blender.reimport_export(
        slug,
        mesh_rel,
        move_anim_rel,
        proof_name="chaosx_anomaly_recon_trooper_move",
    )
    action_reports["move"] = {
        "required_role": "move",
        "action_name": move_action_name,
        "source_checkpoint": move_blend,
        "authoring": move_authoring,
        "export": move_anim_export,
        "output_rel": move_anim_rel,
        "loop": True,
        "frame_policy": "24fps_in_place_blender_authored",
    }
    mesh_file = job / mesh_rel
    update_job(
        job,
        status="pdx_exported",
        exports={
            "mesh": mesh_rel,
            "animations": {
                role: exported_animation_path(report)
                for role, report in action_reports.items()
            },
        },
    )
    append_history(
        job,
        state="pdx_exported",
        event="humanoid_mesh_exported",
        actor="chaosx_3d_model_pipeline",
        details={
            "rig_task_id": rig_id,
            "animation_downloads": animation_downloads,
            "mesh": file_record(mesh_file, relative_to=job),
            "reimport": {
                "attack": attack_reimport,
                "idle": idle_reimport,
                "move": move_reimport,
            },
        },
    )
    return {
        "rig_task_id": rig_id,
        "animation_downloads": animation_downloads,
        "prepare": {"attack": prep, "idle": idle_prep},
        "textures": textures,
        "mesh_export": mesh_export,
        "action_reports": action_reports,
        "reimport": {
            "attack": attack_reimport,
            "idle": idle_reimport,
            "move": move_reimport,
        },
    }


def main() -> int:
    configs = read_json(PIPELINE_ROOT / "config" / "pilot_jobs.json")["pilots"]
    args = sys.argv[1:]
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
    for asset in assets:
        spec = configs[asset]
        initialize_one(spec)
        if phase in {"full", "candidate"}:
            candidate = run_candidate(spec)
            results.append({"asset": asset, "candidate": candidate})
            if phase == "candidate":
                continue
        if spec["asset_kind"] == "static":
            results.append({"asset": asset, "continuation": continue_static(spec)})
        else:
            results.append({"asset": asset, "continuation": continue_humanoid(spec)})
    print(json.dumps(results, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

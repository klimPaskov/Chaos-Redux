"""Hash-bound texture staging, native BC delivery, QA, and CAS installation.

Every conversion writes to a separate staging root. The install manifest stores
input hashes, target preimages, mask/provenance hashes, encoded hashes, and
decoded-image measurements; installation rechecks all of them before an
atomic replacement. No provider call, Blender process, download, or runtime
write occurs during planning or conversion.
"""

from __future__ import annotations

import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple

from PIL import Image

from . import bc_codec
from .atlas import downsample_occupancy_mask, dilate_from_occupancy, load_occupancy_mask, mask_stats
from .conventions import (
    NORMAL_FLAT_RGBA,
    build_pdx_specular_from_provider,
    gate_normal,
    gate_specular,
    packed_normal_cleanup,
    repack_provider_normal,
)
from .dds import DdsError, decode_mip_rgba, parse_dds_header


SCHEMA_VERSION = 1
VALID_ROLES = {"diffuse", "normal", "specular"}
VALID_SCOPES = {
    "compression_only",
    "packed_normal_cleanup",
    "provider_normal_repack",
    "provider_specular_recipe",
}
_SHA256_RE = re.compile(r"^[0-9a-fA-F]{64}$")


class TextureDeliveryError(RuntimeError):
    """A texture batch is invalid, unsafe, or failed a required gate."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _relative_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def _resolve_under_root(root: Path, relative_path: str, *, must_exist: bool) -> Path:
    if not isinstance(relative_path, str) or not relative_path.strip():
        raise TextureDeliveryError("Every path must be a non-empty repository-relative string.")
    candidate = Path(relative_path)
    if candidate.is_absolute() or candidate.drive:
        raise TextureDeliveryError(f"Absolute paths are not accepted: {relative_path}")
    pure = PurePosixPath(relative_path.replace("\\", "/"))
    if any(part in {"", ".", ".."} for part in pure.parts):
        raise TextureDeliveryError(f"Path traversal is not accepted: {relative_path}")
    current = root
    for part in pure.parts:
        current = current / part
        if current.is_symlink():
            raise TextureDeliveryError(f"Symbolic-link path components are not accepted: {relative_path}")
    resolved = current.resolve(strict=must_exist)
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise TextureDeliveryError(f"Path escapes the repository root: {relative_path}") from error
    if must_exist and not resolved.is_file():
        raise TextureDeliveryError(f"Expected a regular file: {relative_path}")
    return resolved


def _relative_path(root: Path, path: Path) -> str:
    try:
        return _relative_posix(path.resolve(strict=False), root)
    except ValueError as error:
        raise TextureDeliveryError(f"Path escapes the repository root: {path}") from error


def _atomic_json(path: Path, value: Dict[str, object], *, replace: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not replace:
        raise TextureDeliveryError(f"Refusing to replace existing manifest: {path}")
    handle, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    temp_path = Path(temp_name)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_path, path)
    except BaseException:
        try:
            temp_path.unlink()
        except OSError:
            pass
        raise


def _read_json(path: Path) -> Dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise TextureDeliveryError(f"Unable to read JSON document: {path}") from error
    if not isinstance(value, dict):
        raise TextureDeliveryError(f"Expected a JSON object: {path}")
    return value


def _valid_hash(value, field: str) -> str:
    if not isinstance(value, str) or not _SHA256_RE.fullmatch(value):
        raise TextureDeliveryError(f"{field} must be a 64-character SHA-256 hex digest.")
    return value.lower()


def _source_image(path: Path) -> Tuple[Image.Image, Dict[str, object]]:
    suffix = path.suffix.lower()
    if suffix == ".dds":
        data = path.read_bytes()
        header = parse_dds_header(
            data,
            require_full_mips=False,
            min_dimension=4,
            max_dimension=4096,
            allow_uncompressed_bgra=True,
        )
        image = decode_mip_rgba(data, header, 0)
        return image, {
            "kind": "dds",
            "format": header.format_name,
            "width": header.width,
            "height": header.height,
            "mip_count": header.mip_count,
            "decoded_with": "repo BC1/BC3 or legacy BGRA reader",
        }
    try:
        with Image.open(path) as source:
            source.load()
            image = source.convert("RGBA")
    except (OSError, ValueError) as error:
        raise TextureDeliveryError(f"Unable to decode texture input: {path}") from error
    return image, {
        "kind": "image",
        "format": Image.registered_extensions().get(suffix, suffix.lstrip(".")),
        "width": image.width,
        "height": image.height,
        "mode": image.mode,
    }


def _validate_size_policy(item: Dict[str, object], source_size: Tuple[int, int]) -> Tuple[int, int]:
    requested = item.get("size", 512)
    if requested not in {128, 256, 512, 1024}:
        raise TextureDeliveryError("Target size must be 128, 256, 512, or 1024 pixels.")
    if requested == 1024:
        justification = item.get("size_justification")
        if not isinstance(justification, str) or len(justification.strip()) < 30:
            raise TextureDeliveryError("A 1024px request requires a concrete 30-character size justification.")
    width, height = source_size
    if width != height or width < 128 or width & (width - 1):
        raise TextureDeliveryError("Input atlas must be square, power-of-two, and at least 128px.")
    actual = min(width, int(requested))
    if actual > width:
        raise TextureDeliveryError("Texture upscaling is forbidden.")
    return actual, actual


def _validate_skip_dilation(item: Dict[str, object]) -> int:
    amount = item.get("dilation_px", 12)
    if not isinstance(amount, int) or amount < 0 or amount > 16:
        raise TextureDeliveryError("dilation_px must be an integer from 0 through 16.")
    if amount == 0:
        reason = item.get("skip_dilation_reason")
        if not isinstance(reason, str) or len(reason.strip()) < 20:
            raise TextureDeliveryError("Skipping dilation requires a concrete skip_dilation_reason.")
    elif amount < 8:
        raise TextureDeliveryError("Atlas dilation must be 8 through 16 pixels unless explicitly skipped.")
    return amount


def _provenance_rows(provenance: Dict[str, object]) -> List[Dict[str, str]]:
    rows = []
    kind = provenance.get("kind")
    if provenance.get("detail_synthesized") is True or provenance.get("generated_detail") is True:
        raise TextureDeliveryError("Texture provenance claims synthesized detail; ungrounded detail is forbidden.")
    if kind == "provider_rgb_normal":
        source = provenance.get("source")
        if not isinstance(source, dict):
            raise TextureDeliveryError("Provider-normal provenance requires a source path and SHA-256.")
        rows.append(source)
        if provenance.get("green_sign", "preserve") == "invert":
            evidence = provenance.get("green_sign_evidence")
            if not isinstance(evidence, dict):
                raise TextureDeliveryError("Normal green inversion requires separate handedness evidence.")
            rows.append(evidence)
    elif kind == "provider_pbr_specular":
        roughness = provenance.get("roughness")
        if not isinstance(roughness, dict):
            raise TextureDeliveryError("Provider-specular provenance requires a roughness source.")
        rows.append(roughness)
        metalness = provenance.get("metalness")
        if metalness is not None:
            if not isinstance(metalness, dict):
                raise TextureDeliveryError("Metalness provenance must be a path/SHA object or null.")
            rows.append(metalness)
        masks = provenance.get("material_masks")
        if not isinstance(masks, dict):
            raise TextureDeliveryError("Provider-specular provenance requires explicit class masks.")
        for row in masks.values():
            if not isinstance(row, dict):
                raise TextureDeliveryError("Every material mask requires a path and SHA-256.")
            rows.append(row)
    elif kind in {"pdx_packed_normal_evidence", "pdx_material_mask_evidence"}:
        source = provenance.get("source")
        if not isinstance(source, dict):
            raise TextureDeliveryError("PDX evidence provenance requires an exact source path and SHA-256.")
        rows.append(source)
        if kind == "pdx_material_mask_evidence":
            masks = provenance.get("material_masks")
            if not isinstance(masks, dict):
                raise TextureDeliveryError("PDX specular evidence requires explicit class masks.")
            for row in masks.values():
                if not isinstance(row, dict):
                    raise TextureDeliveryError("Every PDX material mask requires a path and SHA-256.")
                rows.append(row)
    else:
        raise TextureDeliveryError(f"Unsupported material provenance kind: {kind!r}")
    return rows


def _validate_provenance(root: Path, item: Dict[str, object]) -> Dict[str, object]:
    provenance_rel = item.get("provenance_rel")
    if provenance_rel is None:
        return {"status": "missing", "rows": [], "value": None, "sha256": None}
    path = _resolve_under_root(root, provenance_rel, must_exist=True)
    value = _read_json(path)
    rows = _provenance_rows(value)
    validated_rows = []
    for row in rows:
        path_rel = row.get("path_rel")
        if not isinstance(path_rel, str):
            raise TextureDeliveryError("Provenance path_rel must be repository-relative.")
        source = _resolve_under_root(root, path_rel, must_exist=True)
        expected = _valid_hash(row.get("sha256"), f"provenance {path_rel}.sha256")
        actual = sha256_file(source)
        if actual != expected:
            raise TextureDeliveryError(f"Provenance source hash mismatch: {path_rel}")
        validated_rows.append({"path_rel": path_rel, "sha256": actual})
    if value.get("kind") in {"pdx_packed_normal_evidence", "pdx_material_mask_evidence"}:
        source_row = value["source"]
        if source_row["path_rel"] != item.get("source_rel") or source_row["sha256"].lower() != sha256_file(
            _resolve_under_root(root, item["source_rel"], must_exist=True)
        ):
            raise TextureDeliveryError("PDX material evidence does not identify the exact input texture bytes.")
    return {
        "status": "verified",
        "rows": validated_rows,
        "value": value,
        "path_rel": provenance_rel,
        "sha256": sha256_file(path),
    }


def _input_sha_rows(root: Path, item: Dict[str, object], provenance: Dict[str, object]) -> List[Dict[str, str]]:
    rows = [
        {"role": "texture_source", "path_rel": item["source_rel"], "sha256": item["source_sha256"]},
        {"role": "occupancy_mask", "path_rel": item["occupancy_mask_rel"], "sha256": item["occupancy_mask_sha256"]},
    ]
    if provenance.get("path_rel"):
        rows.append(
            {
                "role": "material_provenance",
                "path_rel": provenance["path_rel"],
                "sha256": provenance["sha256"],
            }
        )
    for source in provenance.get("rows", []):
        rows.append({"role": "provenance_input", **source})
    dedup = {}
    for row in rows:
        dedup[row["path_rel"]] = row
    return list(dedup.values())


def resolve_uv_mask(
    repo_root: Path,
    mask_manifest_path: Path,
    pdxmesh: str,
    texture_name: str,
    *,
    expected_mesh_sha256: Optional[str] = None,
    expected_registration_sha256: Optional[str] = None,
) -> Dict[str, object]:
    """Resolve one texture occupancy mask and verify mesh/registration lineage."""

    root = Path(repo_root).resolve(strict=True)
    manifest_path = Path(mask_manifest_path)
    if not manifest_path.is_absolute():
        manifest_path = _resolve_under_root(root, str(mask_manifest_path), must_exist=True)
    else:
        try:
            manifest_path = manifest_path.resolve(strict=True)
            manifest_path.relative_to(root)
        except (OSError, ValueError) as error:
            raise TextureDeliveryError("UV mask manifest must be inside the repository root.") from error
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise TextureDeliveryError("Unable to read UV mask manifest.") from error
    if not isinstance(manifest, list):
        raise TextureDeliveryError("UV mask manifest must be a list of PDX mesh records.")
    mesh_rows = [row for row in manifest if isinstance(row, dict) and row.get("pdxmesh") == pdxmesh]
    if len(mesh_rows) != 1:
        raise TextureDeliveryError(f"Expected exactly one UV-mask mesh row for {pdxmesh!r}.")
    mesh_row = mesh_rows[0]
    matches = [row for row in mesh_row.get("masks", []) if row.get("texture") == texture_name]
    if len(matches) != 1:
        raise TextureDeliveryError(f"Expected exactly one UV mask for {pdxmesh}/{texture_name}.")
    row = matches[0]
    mesh_sha = _valid_hash(row.get("mesh_sha256"), "UV mask mesh_sha256")
    registration_sha = _valid_hash(row.get("registration_sha256"), "UV mask registration_sha256")
    if expected_mesh_sha256 and mesh_sha != _valid_hash(expected_mesh_sha256, "expected_mesh_sha256"):
        raise TextureDeliveryError("UV occupancy mask does not match the expected installed mesh SHA.")
    if expected_registration_sha256 and registration_sha != _valid_hash(
        expected_registration_sha256, "expected_registration_sha256"
    ):
        raise TextureDeliveryError("UV occupancy mask does not match the expected registration SHA.")
    mask_path = _resolve_under_root(root, row.get("mask"), must_exist=True)
    actual_sha = sha256_file(mask_path)
    expected_mask_sha = _valid_hash(row.get("sha256"), "UV mask sha256")
    if actual_sha != expected_mask_sha:
        raise TextureDeliveryError("UV occupancy-mask file SHA does not match its manifest row.")
    with Image.open(mask_path) as image:
        image.load()
        mask = load_occupancy_mask(image)
    if mask.size != (row.get("size"), row.get("size")):
        raise TextureDeliveryError("UV occupancy-mask dimensions do not match their manifest row.")
    measured = mask_stats(mask)
    if abs(measured["coverage"] - float(row.get("coverage"))) > (1.0 / max(1, row["size"] ** 2)):
        raise TextureDeliveryError("UV occupancy-mask coverage does not match its manifest row.")
    return {
        "pdxmesh": pdxmesh,
        "texture": texture_name,
        "mask_rel": _relative_path(root, mask_path),
        "sha256": actual_sha,
        "mesh_sha256": mesh_sha,
        "registration_sha256": registration_sha,
        "coverage": measured["coverage"],
        "size": row["size"],
        "issues": mesh_row.get("issues", []),
        "policy": "verified PDX UV occupancy; no color/luminance inference",
    }


def prepare_batch(
    repo_root: Path,
    request_json: Path,
    staging_root: Path,
    manifest_path: Path,
) -> Dict[str, object]:
    """Create a dry-run batch plan and checksum-bound compare-and-swap manifest."""

    root = Path(repo_root).resolve(strict=True)
    request_path = Path(request_json)
    if not request_path.is_absolute():
        request_path = _resolve_under_root(root, str(request_json), must_exist=True)
    else:
        try:
            request_path = request_path.resolve(strict=True)
            request_path.relative_to(root)
        except (OSError, ValueError) as error:
            raise TextureDeliveryError("Request JSON must be inside the repository root.") from error
    request = _read_json(request_path)
    batch_id = request.get("batch_id")
    if not isinstance(batch_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}", batch_id):
        raise TextureDeliveryError("batch_id must be a short stable slug.")
    stage_path = Path(staging_root)
    if stage_path.is_absolute():
        try:
            stage_path = stage_path.resolve(strict=False)
            stage_path.relative_to(root)
        except ValueError as error:
            raise TextureDeliveryError("Staging root must be inside the repository root.") from error
    else:
        stage_path = _resolve_under_root(root, str(staging_root), must_exist=False)
    stage_rel = _relative_path(root, stage_path)
    if not isinstance(request.get("items"), list) or not request["items"]:
        raise TextureDeliveryError("Request must contain a non-empty items list.")
    output_manifest_path = Path(manifest_path)
    if output_manifest_path.is_absolute():
        try:
            output_manifest_path = output_manifest_path.resolve(strict=False)
            output_manifest_path.relative_to(root)
        except ValueError as error:
            raise TextureDeliveryError("Install manifest must be inside the repository root.") from error
    else:
        output_manifest_path = _resolve_under_root(root, str(manifest_path), must_exist=False)
    if output_manifest_path.exists():
        raise TextureDeliveryError(f"Refusing to replace an existing install manifest: {output_manifest_path}")

    planned_items = []
    ids = set()
    target_paths = set()
    for raw in request["items"]:
        if not isinstance(raw, dict):
            raise TextureDeliveryError("Every request item must be a JSON object.")
        item_id = raw.get("id")
        if not isinstance(item_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}", item_id):
            raise TextureDeliveryError("Each texture id must be a short stable slug.")
        if item_id in ids:
            raise TextureDeliveryError(f"Duplicate texture item id: {item_id}")
        ids.add(item_id)
        role = raw.get("role")
        if role not in VALID_ROLES:
            raise TextureDeliveryError(f"Unsupported texture role for {item_id}: {role!r}")
        scope = raw.get("conversion_scope", "compression_only")
        if scope not in VALID_SCOPES:
            raise TextureDeliveryError(f"Unsupported conversion_scope for {item_id}: {scope!r}")
        source_rel = raw.get("source_rel")
        source = _resolve_under_root(root, source_rel, must_exist=True)
        source_rel = _relative_path(root, source)
        source_image, source_info = _source_image(source)
        target_rel = raw.get("target_rel")
        target = _resolve_under_root(root, target_rel, must_exist=False)
        target_rel = _relative_path(root, target)
        if source == target and not source.is_file():
            raise TextureDeliveryError("In-place conversion requires an existing source/target file.")
        mask_rel = raw.get("occupancy_mask_rel")
        mask_path = _resolve_under_root(root, mask_rel, must_exist=True)
        mask_rel = _relative_path(root, mask_path)
        with Image.open(mask_path) as mask_source:
            mask_source.load()
            mask_image = load_occupancy_mask(mask_source)
        if mask_image.size != source_image.size:
            raise TextureDeliveryError(f"Occupancy mask dimensions differ from source for {item_id}.")
        actual_size = _validate_size_policy(raw, source_image.size)
        dilation_px = _validate_skip_dilation(raw)
        requested_coverage = raw.get("minimum_coverage")
        if requested_coverage is not None and not 0 <= float(requested_coverage) <= 1:
            raise TextureDeliveryError("minimum_coverage must be between 0 and 1.")
        resized_mask = mask_image.resize(actual_size, Image.Resampling.NEAREST) if mask_image.size != actual_size else mask_image
        measured_mask = mask_stats(resized_mask)
        if requested_coverage is not None and measured_mask["coverage"] < float(requested_coverage):
            raise TextureDeliveryError(
                f"UV coverage {measured_mask['coverage']} is below requested {requested_coverage} for {item_id}."
            )
        alpha_choice = raw.get("alpha_used", "auto")
        if alpha_choice not in {True, False, "auto"}:
            raise TextureDeliveryError("alpha_used must be true, false, or 'auto'.")
        alpha_values = source_image.getchannel("A").getdata()
        detected_alpha = any(value != 255 for value in alpha_values)
        if alpha_choice is False and detected_alpha and role == "diffuse":
            raise TextureDeliveryError(f"Diffuse {item_id} contains non-opaque alpha but declares alpha_used=false.")
        alpha_used = detected_alpha if alpha_choice == "auto" else bool(alpha_choice)
        if role != "diffuse" and alpha_choice is not False:
            alpha_used = False

        normalized_raw = dict(raw)
        normalized_raw.update({
            "source_rel": source_rel,
            "target_rel": target_rel,
            "occupancy_mask_rel": mask_rel,
        })
        if raw.get("provenance_rel") is not None:
            provenance_path = _resolve_under_root(root, raw["provenance_rel"], must_exist=True)
            normalized_raw["provenance_rel"] = _relative_path(root, provenance_path)
        provenance = _validate_provenance(root, normalized_raw)
        if scope == "provider_normal_repack":
            if role != "normal" or provenance.get("value", {}).get("kind") != "provider_rgb_normal":
                raise TextureDeliveryError("provider_normal_repack requires normal role and provider RGB normal provenance.")
        if scope == "provider_specular_recipe":
            if role != "specular" or provenance.get("value", {}).get("kind") != "provider_pbr_specular":
                raise TextureDeliveryError("provider_specular_recipe requires specular role and provider PBR provenance.")
        if scope == "packed_normal_cleanup" and role != "normal":
            raise TextureDeliveryError("packed_normal_cleanup is valid only for the normal role.")

        source_sha = sha256_file(source)
        expected_before = raw.get("expected_target_sha256", "capture")
        target_before = sha256_file(target) if target.is_file() else None
        if expected_before != "capture":
            if expected_before is None:
                if target_before is not None:
                    raise TextureDeliveryError(f"Target was expected absent but already exists: {target_rel}")
            elif _valid_hash(expected_before, f"{item_id}.expected_target_sha256") != target_before:
                raise TextureDeliveryError(f"Target preimage SHA mismatch while planning: {target_rel}")
        if target in target_paths:
            raise TextureDeliveryError(f"Duplicate install target: {target_rel}")
        target_paths.add(target)
        if target == source:
            if not source.is_file() or target_before != source_sha:
                raise TextureDeliveryError("In-place conversion source and target hashes do not match.")
        item_inputs = _input_sha_rows(
            root,
            {
                "source_rel": source_rel,
                "source_sha256": source_sha,
                "occupancy_mask_rel": mask_rel,
                "occupancy_mask_sha256": sha256_file(mask_path),
            },
            provenance,
        )
        relative_stage_item = (PurePosixPath(stage_rel) / batch_id / item_id)
        if any(part in {"", ".", ".."} for part in relative_stage_item.parts):
            raise TextureDeliveryError("Invalid staging path.")
        source_archive_rel = str(relative_stage_item / f"input_original{source.suffix.lower() or '.bin'}")
        stage_dds_rel = str(relative_stage_item / "output.dds")
        prepared_png_rel = str(relative_stage_item / "prepared_base.png")
        report_rel = str(relative_stage_item / "qa_report.json")
        item = {
            "id": item_id,
            "role": role,
            "conversion_scope": scope,
            "source_rel": source_rel,
            "source_sha256": source_sha,
            "source_bytes": source.stat().st_size,
            "source_image": source_info,
            "source_archive_rel": source_archive_rel,
            "target_rel": target_rel,
            "expected_target_sha256": target_before,
            "occupancy_mask_rel": mask_rel,
            "occupancy_mask_sha256": sha256_file(mask_path),
            "occupancy_mask": measured_mask,
            "dilation_px": dilation_px,
            "skip_dilation_reason": raw.get("skip_dilation_reason"),
            "requested_size": raw.get("size", 512),
            "output_size": actual_size[0],
            "size_justification": raw.get("size_justification"),
            "alpha_used": alpha_used,
            "alpha_source_pixels_nonopaque": detected_alpha,
            "provenance_rel": normalized_raw.get("provenance_rel"),
            "provenance_sha256": provenance.get("sha256"),
            "provenance_status": provenance["status"],
            "input_hashes": item_inputs,
            "stage_dds_rel": stage_dds_rel,
            "prepared_png_rel": prepared_png_rel,
            "qa_report_rel": report_rel,
            "minimum_coverage": requested_coverage,
            "planned_format": (
                "BC3_UNORM"
                if role in {"normal", "specular"} or (role == "diffuse" and alpha_used)
                else "BC1_UNORM"
            ),
            "planned_operations": [
                "decode and checksum source",
                "resize down only when above requested maximum",
                f"dilate from explicit occupancy mask by {dilation_px}px" if dilation_px else "skip dilation with recorded reason",
                f"encode {('BC3' if role in {'normal', 'specular'} or alpha_used else 'BC1')} full mip chain",
                "validate DDS header, every decoded mip, pixel error, and alpha bounds",
            ],
        }
        planned_items.append(item)

    if len({item["source_rel"] for item in planned_items if item["source_rel"] in {i["target_rel"] for i in planned_items}}) > 0:
        # Same-item in-place conversions are safe because the original is archived;
        # cross-item source/target aliases are rejected below by id matching.
        rel_to_ids = {}
        for item in planned_items:
            rel_to_ids.setdefault(item["source_rel"], set()).add(item["id"])
            rel_to_ids.setdefault(item["target_rel"], set()).add(item["id"])
        for item in planned_items:
            if item["source_rel"] == item["target_rel"]:
                continue
            if item["target_rel"] in {other["source_rel"] for other in planned_items}:
                raise TextureDeliveryError("A batch target cannot overwrite another item's source.")

    stage_root_abs = stage_path / batch_id
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "batch_id": batch_id,
        "state": "prepared",
        "repository_root": str(root),
        "request_rel": _relative_path(root, request_path),
        "request_sha256": sha256_file(request_path),
        "staging_root_rel": _relative_path(root, stage_root_abs),
        "manifest_rel": _relative_path(root, output_manifest_path),
        "encoder": {
            "backend": "native_numpy_bc_blockfit",
            "version": bc_codec.ENCODER_VERSION,
            "numpy_version": __import__("numpy").__version__,
            "formats": ["BC1_UNORM/DXT1", "BC3_UNORM/DXT5"],
            "texconv_search": "bounded search found no installed texconv; native encoder is the declared route",
        },
        "items": planned_items,
        "install": {"status": "not_started", "mode": "compare_and_swap"},
    }
    _atomic_json(output_manifest_path, manifest, replace=False)
    return manifest


def _load_manifest(repo_root: Path, manifest_path: Path) -> Tuple[Path, Dict[str, object], Path]:
    root = Path(repo_root).resolve(strict=True)
    path = Path(manifest_path)
    if not path.is_absolute():
        path = _resolve_under_root(root, str(manifest_path), must_exist=True)
    else:
        try:
            path = path.resolve(strict=True)
            path.relative_to(root)
        except (OSError, ValueError) as error:
            raise TextureDeliveryError("Install manifest must be inside the repository root.") from error
    manifest = _read_json(path)
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise TextureDeliveryError("Unsupported texture install-manifest schema.")
    if Path(manifest.get("repository_root", "")).resolve(strict=False) != root:
        raise TextureDeliveryError("Manifest repository_root does not match the supplied root.")
    return root, manifest, path


def _verify_item_inputs(
    root: Path,
    item: Dict[str, object],
    *,
    allow_installed_target: bool = False,
    require_archive: bool = False,
) -> None:
    target_rel = item["target_rel"]
    source_rel = item["source_rel"]
    same_target_source = source_rel == target_rel and allow_installed_target
    for record in item["input_hashes"]:
        path = _resolve_under_root(root, record["path_rel"], must_exist=True)
        if same_target_source and record["role"] == "texture_source":
            continue
        if sha256_file(path) != record["sha256"]:
            raise TextureDeliveryError(f"Input changed since the batch was prepared: {record['path_rel']}")
    if require_archive:
        archive = _resolve_under_root(root, item["source_archive_rel"], must_exist=True)
        if sha256_file(archive) != item["source_sha256"]:
            raise TextureDeliveryError(f"Immutable input archive SHA mismatch for {item['id']}.")


def _load_provenance_value(root: Path, item: Dict[str, object]) -> Optional[Dict[str, object]]:
    if not item.get("provenance_rel"):
        return None
    path = _resolve_under_root(root, item["provenance_rel"], must_exist=True)
    if sha256_file(path) != item.get("provenance_sha256"):
        raise TextureDeliveryError(f"Material provenance changed after planning: {item['id']}.")
    return _read_json(path)


def _provenance_image(root: Path, row: Dict[str, str]) -> Image.Image:
    path = _resolve_under_root(root, row["path_rel"], must_exist=True)
    if sha256_file(path) != row["sha256"]:
        raise TextureDeliveryError(f"Material source changed after planning: {row['path_rel']}.")
    with Image.open(path) as source:
        source.load()
        return source.copy()


def _apply_scope(root: Path, item: Dict[str, object], source: Image.Image, mask: Image.Image):
    scope = item["conversion_scope"]
    provenance = _load_provenance_value(root, item)
    report = {"scope": scope, "detail_synthesized": False}
    if scope == "compression_only":
        return source.convert("RGBA"), report
    if scope == "packed_normal_cleanup":
        processed, details = packed_normal_cleanup(source, mask, dilation_px=0)
        report.update(details)
        return processed, report
    if scope == "provider_normal_repack":
        source_row = provenance.get("source")
        if source_row.get("path_rel") != item["source_rel"] or source_row.get("sha256", "").lower() != item["source_sha256"]:
            raise TextureDeliveryError("Provider-normal provenance does not identify the exact input bytes.")
        green_sign = provenance.get("green_sign", "preserve")
        processed, details = repack_provider_normal(source, green_sign=green_sign)
        report.update(details)
        return processed, report
    if scope == "provider_specular_recipe":
        rough = _provenance_image(root, provenance["roughness"])
        metal_row = provenance.get("metalness")
        metal = _provenance_image(root, metal_row) if metal_row is not None else None
        masks = {
            name: _provenance_image(root, row)
            for name, row in provenance["material_masks"].items()
        }
        if provenance["roughness"]["path_rel"] != item["source_rel"]:
            raise TextureDeliveryError("Specular recipe source_rel must identify the provider roughness map.")
        if provenance["roughness"]["sha256"].lower() != item["source_sha256"]:
            raise TextureDeliveryError("Specular recipe roughness SHA does not match source_rel.")
        source_hashes = {
            "roughness": provenance["roughness"],
            "metalness": provenance.get("metalness"),
            "material_masks": provenance["material_masks"],
        }
        processed, details = build_pdx_specular_from_provider(
            rough,
            metal,
            masks,
            mask,
            source_hashes=source_hashes,
            recipe_overrides=provenance.get("material_recipe_overrides"),
        )
        report.update(details)
        return processed, report
    raise TextureDeliveryError(f"Unsupported conversion scope: {scope}")


def _resize_channels(image: Image.Image, size: Tuple[int, int]) -> Image.Image:
    image = image.convert("RGBA")
    if image.size == size:
        return image.copy()
    channels = [channel.resize(size, Image.Resampling.LANCZOS) for channel in image.split()]
    return Image.merge("RGBA", channels)


def _pillow_decode(dds_bytes: bytes) -> Image.Image:
    try:
        with Image.open(io.BytesIO(dds_bytes)) as image:
            image.load()
            return image.convert("RGBA")
    except (OSError, ValueError) as error:
        raise TextureDeliveryError("Pillow could not decode the generated DDS base level.") from error


def _mip_sources(
    base: Image.Image,
    occupancy_mask: Image.Image,
    role: str,
    dilation_px: int,
    conversion_scope: str,
) -> Tuple[List[Image.Image], List[Dict[str, object]]]:
    raw_chain = bc_codec.build_mip_chain(base)
    mask_chain = [occupancy_mask.convert("L")]
    for level in raw_chain[1:]:
        mask_chain.append(downsample_occupancy_mask(mask_chain[-1], level.size))
    prepared = []
    reports = []
    for level, (image, mask) in enumerate(zip(raw_chain, mask_chain)):
        if dilation_px == 0 and conversion_scope == "compression_only":
            prepared.append(image)
            reports.append({
                "level": level,
                "dilation_radius_px": 0,
                "filled_pixels": 0,
                "source_pixel_values_only": True,
                "skipped": True,
            })
            continue
        if dilation_px == 0:
            radius = 0
        else:
            radius = max(1, int(round(dilation_px / float(2 ** level))))
        if role == "diffuse":
            channels = (0, 1, 2)
            fill = None
        elif role == "normal":
            channels = (0, 1, 2, 3)
            fill = NORMAL_FLAT_RGBA
        else:
            channels = (0, 1, 2, 3)
            fill = (0, 0, 0, 0)
        result, report = dilate_from_occupancy(
            image,
            mask,
            radius,
            channels=channels,
            outside_fill=fill,
        )
        prepared.append(result)
        reports.append({"level": level, **report})
    return prepared, reports


def _compression_gate(
    root: Path,
    item: Dict[str, object],
    output_bytes: bytes,
    mip_sources: List[Image.Image],
    selected_format: str,
    padding_reports: List[Dict[str, object]],
    processing_report: Dict[str, object],
) -> Dict[str, object]:
    header = parse_dds_header(
        output_bytes,
        require_full_mips=True,
        min_dimension=128,
        max_dimension=1024,
    )
    expected_format = item["planned_format"]
    if header.format_name != expected_format or header.format_name != selected_format:
        raise TextureDeliveryError(f"Encoded {item['id']} format {header.format_name} != requested {expected_format}.")
    if header.mip_count != len(mip_sources):
        raise TextureDeliveryError(f"Encoded {item['id']} mip count differs from prepared mip sources.")

    mip_evidence = []
    decoded_levels = []
    failures = []
    for level, source_mip in enumerate(mip_sources):
        decoded = decode_mip_rgba(output_bytes, header, level)
        if decoded.size != source_mip.size:
            failures.append(f"Mip {level} dimensions changed during encoding.")
        metrics = bc_codec.encode_metrics(source_mip, decoded)
        minimum_psnr = 25.0 if min(source_mip.size) >= 8 else 15.0
        maximum_channel_mae = 16.0 if min(source_mip.size) >= 8 else 32.0
        if metrics["rgb_psnr_db"] is not None and metrics["rgb_psnr_db"] < minimum_psnr:
            failures.append(
                f"Mip {level} RGB PSNR {metrics['rgb_psnr_db']} dB is below {minimum_psnr} dB."
            )
        for channel in ("R", "G", "B"):
            if metrics["channels"][channel]["mae"] > maximum_channel_mae:
                failures.append(
                    f"Mip {level} {channel} MAE {metrics['channels'][channel]['mae']} exceeds {maximum_channel_mae}."
                )
        if item["role"] == "normal" or item["role"] == "specular" or item["alpha_used"]:
            if metrics["channels"]["A"]["mae"] > 10.0:
                failures.append(f"Mip {level} packed alpha MAE exceeds 10.")
        mip_evidence.append({"level": level, "decoded_size": list(decoded.size), "pixel_error": metrics})
        decoded_levels.append(decoded)

    pillow_pixels = _pillow_decode(output_bytes)
    pillow_metrics = bc_codec.encode_metrics(mip_sources[0], pillow_pixels)
    if pillow_pixels.tobytes() != decoded_levels[0].tobytes():
        pillow_diff = bc_codec.encode_metrics(decoded_levels[0], pillow_pixels)
        if pillow_diff["rgb_mae"] > 1.0 or pillow_diff["channels"]["A"]["mae"] > 1.0:
            failures.append("Pillow and repository DDS pixel decoders disagree by more than 1 channel value.")

    alpha_report = None
    if item["role"] == "diffuse":
        source_alpha = list(mip_sources[0].getchannel("A").getdata())
        decoded_alpha = list(pillow_pixels.getchannel("A").getdata())
        alpha_report = {
            "used": item["alpha_used"],
            "source_min": min(source_alpha),
            "source_max": max(source_alpha),
            "decoded_min": min(decoded_alpha),
            "decoded_max": max(decoded_alpha),
            "mean_abs_error": pillow_metrics["channels"]["A"]["mae"],
            "p95_abs_error": pillow_metrics["channels"]["A"]["p95_abs_error"],
        }
        if not item["alpha_used"] and (alpha_report["decoded_min"] != 255 or alpha_report["decoded_max"] != 255):
            failures.append("Opaque diffuse BC1 decoded with non-opaque alpha.")
        if item["alpha_used"] and abs(alpha_report["source_min"] - alpha_report["decoded_min"]) > 4:
            failures.append("Diffuse alpha minimum changed by more than 4 values.")
        if item["alpha_used"] and abs(alpha_report["source_max"] - alpha_report["decoded_max"]) > 4:
            failures.append("Diffuse alpha maximum changed by more than 4 values.")

    mask_path = _resolve_under_root(root, item["occupancy_mask_rel"], must_exist=True)
    with Image.open(mask_path) as source_mask:
        source_mask.load()
        occupancy = load_occupancy_mask(source_mask, mip_sources[0].size)
    semantics = {"status": "unresolved", "reason": "No material provenance was supplied."}
    provenance = _load_provenance_value(root, item)
    if item["conversion_scope"] in {"packed_normal_cleanup", "provider_normal_repack"}:
        if item["role"] == "normal":
            precompression_gate = gate_normal(mip_sources[0], occupancy)
            decoded_gate = gate_normal(pillow_pixels, occupancy)
            semantics = {
                "status": "passed" if precompression_gate["status"] == decoded_gate["status"] == "passed" else "failed",
                "precompression": precompression_gate,
                "decoded": decoded_gate,
            }
    elif item["conversion_scope"] == "provider_specular_recipe":
        masks = {
            name: _provenance_image(root, row)
            for name, row in provenance["material_masks"].items()
        }
        for name, mask in list(masks.items()):
            if mask.size != pillow_pixels.size:
                masks[name] = mask.resize(pillow_pixels.size, Image.Resampling.NEAREST)
        precompression_gate = gate_specular(mip_sources[0], occupancy, masks,
                                           recipe_overrides=provenance.get("material_recipe_overrides"))
        decoded_gate = gate_specular(
            pillow_pixels,
            occupancy,
            masks,
            steel_blue_tolerance=5,
            recipe_overrides=provenance.get("material_recipe_overrides"),
        )
        semantics = {
            "status": "passed" if precompression_gate["status"] == decoded_gate["status"] == "passed" else "failed",
            "precompression": precompression_gate,
            "decoded": decoded_gate,
        }
    elif item.get("provenance_rel") and provenance.get("kind") == "pdx_material_mask_evidence" and item["role"] == "specular":
        masks = {
            name: _provenance_image(root, row)
            for name, row in provenance["material_masks"].items()
        }
        for name, mask in list(masks.items()):
            if mask.size != pillow_pixels.size:
                masks[name] = mask.resize(pillow_pixels.size, Image.Resampling.NEAREST)
        semantics = gate_specular(
            pillow_pixels,
            occupancy,
            masks,
            steel_blue_tolerance=5,
            recipe_overrides=provenance.get("material_recipe_overrides"),
        )
    elif item.get("provenance_rel") and provenance.get("kind") == "pdx_packed_normal_evidence" and item["role"] == "normal":
        semantics = gate_normal(pillow_pixels, occupancy)

    coverage = mask_stats(occupancy)
    if item.get("minimum_coverage") is not None and coverage["coverage"] < float(item["minimum_coverage"]):
        failures.append("Decoded DDS occupancy falls below the requested coverage floor.")

    transport_status = "passed" if not failures else "failed"
    scope = item["conversion_scope"]
    if scope == "compression_only":
        install_eligible = transport_status == "passed"
    elif scope == "packed_normal_cleanup":
        # This repair preserves occupied G/A and changes only unused padding plus
        # the safe PDX R/G/B structural channels; semantic variance can remain open.
        install_eligible = transport_status == "passed" and processing_report.get("occupied_green_alpha_preserved") is True
    else:
        install_eligible = transport_status == "passed" and semantics.get("status") == "passed"
    return {
        "transport_status": transport_status,
        "transport_failures": failures,
        "install_eligible": install_eligible,
        "dds": {
            "format": header.format_name,
            "width": header.width,
            "height": header.height,
            "mip_count": header.mip_count,
            "payload_bytes": sum(header.mip_sizes),
            "full_chain": True,
            "header_and_payload_valid": True,
        },
        "decoder": {
            "repository": "textures.dds.decode_mip_rgba",
            "pillow": Image.__version__ if hasattr(Image, "__version__") else __import__("PIL").__version__,
            "pillow_base_level_decoded": True,
            "pillow_vs_repository_base_pixels_equal": pillow_pixels.tobytes() == decoded_levels[0].tobytes(),
        },
        "pillow_decoded_base_pixel_error": pillow_metrics,
        "per_mip_decoded_pixel_error": mip_evidence,
        "diffuse_alpha_bounds": alpha_report,
        "occupancy": coverage,
        "padding_per_mip": padding_reports,
        "material_semantic_gate": semantics,
    }


def _process_item(root: Path, manifest: Dict[str, object], item: Dict[str, object]) -> Dict[str, object]:
    source_path = _resolve_under_root(root, item["source_rel"], must_exist=True)
    mask_path = _resolve_under_root(root, item["occupancy_mask_rel"], must_exist=True)
    original, source_info = _source_image(source_path)
    if sha256_file(source_path) != item["source_sha256"]:
        raise TextureDeliveryError(f"Input SHA changed before conversion: {item['source_rel']}.")
    if original.size != (item["source_image"]["width"], item["source_image"]["height"]):
        raise TextureDeliveryError(f"Input dimensions changed after planning: {item['source_rel']}.")
    with Image.open(mask_path) as mask_file:
        mask_file.load()
        occupancy_mask = load_occupancy_mask(mask_file)
    if sha256_file(mask_path) != item["occupancy_mask_sha256"]:
        raise TextureDeliveryError(f"Occupancy mask SHA changed before conversion: {item['occupancy_mask_rel']}.")

    scope_base, processing_report = _apply_scope(root, item, original, occupancy_mask)
    output_size = int(item["output_size"])
    if scope_base.size != (output_size, output_size):
        scope_base = _resize_channels(scope_base, (output_size, output_size))
    output_mask = occupancy_mask.resize((output_size, output_size), Image.Resampling.NEAREST)
    base_before_padding = scope_base.copy()
    mip_sources, padding_reports = _mip_sources(
        scope_base,
        output_mask,
        item["role"],
        int(item["dilation_px"]),
        item["conversion_scope"],
    )
    processed_base = mip_sources[0]
    format_name = item["planned_format"]
    if format_name == "BC1_UNORM" and any(value != 255 for value in processed_base.getchannel("A").getdata()):
        raise TextureDeliveryError("BC1 diffuse output cannot discard non-opaque alpha.")
    dds_bytes, encoded_sources = bc_codec.build_dds_from_mips(mip_sources, format_name)
    stage_path = _resolve_under_root(root, item["stage_dds_rel"], must_exist=False)
    prepared_path = _resolve_under_root(root, item["prepared_png_rel"], must_exist=False)
    report_path = _resolve_under_root(root, item["qa_report_rel"], must_exist=False)
    for path in (stage_path, prepared_path, report_path):
        if path.exists():
            raise TextureDeliveryError(f"Refusing to replace staged artifact from an earlier attempt: {path}")
    stage_path.parent.mkdir(parents=True, exist_ok=True)
    source_archive = _resolve_under_root(root, item["source_archive_rel"], must_exist=False)
    source_archive.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, source_archive)
    if sha256_file(source_archive) != item["source_sha256"]:
        raise TextureDeliveryError("Immutable source archive did not preserve the input SHA.")
    processed_base.save(prepared_path, format="PNG", optimize=False)
    stage_path.write_bytes(dds_bytes)
    if sha256_file(source_path) != item["source_sha256"]:
        raise TextureDeliveryError("Texture conversion altered its source input.")
    qa = _compression_gate(
        root,
        item,
        dds_bytes,
        mip_sources,
        format_name,
        padding_reports,
        processing_report,
    )
    target = _resolve_under_root(root, item["target_rel"], must_exist=False)
    before_after = {
        "source_dimensions": list(original.size),
        "output_dimensions": list(processed_base.size),
        "source_sha256": item["source_sha256"],
        "prepared_base_sha256": sha256_file(prepared_path),
        "dds_sha256": sha256_file(stage_path),
        "source_to_prepared_changed_pixel_fraction": _pixel_changed_fraction(
            _resize_channels(original, processed_base.size), base_before_padding
        ),
        "source_target_relation": "in_place_cas" if source_path == target else "separate_input_and_target",
        "target_preimage_sha256": item["expected_target_sha256"],
    }
    report = {
        "schema_version": SCHEMA_VERSION,
        "batch_id": manifest["batch_id"],
        "item_id": item["id"],
        "role": item["role"],
        "conversion_scope": item["conversion_scope"],
        "source": {"path_rel": item["source_rel"], "sha256": item["source_sha256"], "decoded": source_info},
        "processing": processing_report,
        "before_after": before_after,
        "qa": qa,
    }
    _atomic_json(report_path, report, replace=False)
    return {
        "stage_dds_rel": item["stage_dds_rel"],
        "stage_dds_sha256": sha256_file(stage_path),
        "stage_dds_bytes": stage_path.stat().st_size,
        "prepared_png_rel": item["prepared_png_rel"],
        "prepared_png_sha256": sha256_file(prepared_path),
        "qa_report_rel": item["qa_report_rel"],
        "qa_report_sha256": sha256_file(report_path),
        "source_archive_rel": item["source_archive_rel"],
        "source_archive_sha256": sha256_file(source_archive),
        "processing": processing_report,
        "qa": qa,
        "before_after": before_after,
    }


def _pixel_changed_fraction(before: Image.Image, after: Image.Image) -> float:
    before = before.convert("RGBA")
    after = after.convert("RGBA")
    if before.size != after.size:
        raise ValueError("Before/after pixel comparisons require equal dimensions.")
    before_bytes = before.tobytes()
    after_bytes = after.tobytes()
    changed = sum(
        1
        for offset in range(0, len(before_bytes), 4)
        if before_bytes[offset:offset + 4] != after_bytes[offset:offset + 4]
    )
    return round(changed / max(1, before.width * before.height), 8)


def convert_batch(
    repo_root: Path,
    manifest_path: Path,
    *,
    execute: bool = False,
) -> Dict[str, object]:
    """Dry-run by default; `execute=True` writes only to the staging root."""

    root, manifest, path = _load_manifest(repo_root, manifest_path)
    if manifest.get("state") != "prepared":
        raise TextureDeliveryError("Conversion requires a prepared manifest; refusing to rerun a staged batch.")
    if not execute:
        return {
            "status": "dry_run",
            "batch_id": manifest["batch_id"],
            "items": [
                {
                    "id": item["id"],
                    "role": item["role"],
                    "format": item["planned_format"],
                    "size": item["output_size"],
                    "mips": int(item["output_size"]).bit_length(),
                    "source_sha256": item["source_sha256"],
                    "target_preimage_sha256": item["expected_target_sha256"],
                    "staged_output_rel": item["stage_dds_rel"],
                }
                for item in manifest["items"]
            ],
            "writes_performed": False,
        }
    stage_root = _resolve_under_root(root, manifest["staging_root_rel"], must_exist=False)
    if stage_root.exists():
        raise TextureDeliveryError(f"Staging root already exists; use a new batch id: {stage_root}")
    stage_root.mkdir(parents=True)
    converted = []
    failures = []
    for item in manifest["items"]:
        try:
            _verify_item_inputs(root, item)
            converted_item = _process_item(root, manifest, item)
            item["converted"] = converted_item
            item["status"] = "converted"
            converted.append(converted_item)
            if not converted_item["qa"]["install_eligible"]:
                failures.extend(
                    f"{item['id']}: {failure}"
                    for failure in converted_item["qa"]["transport_failures"]
                )
        except Exception as error:
            item["status"] = "failed"
            item["error"] = str(error)
            failures.append(f"{item['id']}: {error}")
            break
    manifest["state"] = "staged" if not failures and len(converted) == len(manifest["items"]) else "stage_failed"
    manifest["conversion"] = {
        "status": "passed" if manifest["state"] == "staged" else "failed",
        "native_encoder_version": bc_codec.ENCODER_VERSION,
        "failures": failures,
        "completed_items": len(converted),
        "total_items": len(manifest["items"]),
    }
    manifest["install"]["status"] = "ready" if manifest["state"] == "staged" and all(
        item["converted"]["qa"]["install_eligible"] for item in manifest["items"]
    ) else "blocked"
    manifest["install"]["install_eligible"] = manifest["install"]["status"] == "ready"
    _atomic_json(path, manifest)
    return manifest


def _current_target_sha(root: Path, item: Dict[str, object]) -> Optional[str]:
    target = _resolve_under_root(root, item["target_rel"], must_exist=False)
    if not target.exists():
        return None
    if not target.is_file():
        raise TextureDeliveryError(f"Install target is not a regular file: {item['target_rel']}")
    return sha256_file(target)


def _copy_verified(source: Path, destination: Path, expected_sha: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    if sha256_file(destination) != expected_sha:
        raise TextureDeliveryError(f"Copy verification failed for {destination}.")


def _copy_atomic_from_stage(stage_path: Path, target: Path, expected_sha: str, batch_id: str) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_symlink():
        raise TextureDeliveryError(f"Install target is a symbolic link: {target}")
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{target.name}.{batch_id}.", suffix=".install.tmp", dir=str(target.parent))
    temp_path = Path(temp_name)
    try:
        with os.fdopen(descriptor, "wb") as output, stage_path.open("rb") as source:
            shutil.copyfileobj(source, output, 1024 * 1024)
            output.flush()
            os.fsync(output.fileno())
        if sha256_file(temp_path) != expected_sha:
            raise TextureDeliveryError(f"Prepared install copy hash mismatch: {target}")
        return temp_path
    except BaseException:
        try:
            temp_path.unlink()
        except OSError:
            pass
        raise


def install_batch(
    repo_root: Path,
    manifest_path: Path,
    *,
    execute: bool = False,
) -> Dict[str, object]:
    """Dry-run by default; execute a hash-checked batch compare-and-swap."""

    root, manifest, path = _load_manifest(repo_root, manifest_path)
    if manifest.get("state") != "staged" or not manifest.get("install", {}).get("install_eligible"):
        raise TextureDeliveryError("Install requires a staged batch whose required delivery gates passed.")
    for item in manifest["items"]:
        if item.get("status") != "converted" or not item.get("converted", {}).get("qa", {}).get("install_eligible"):
            raise TextureDeliveryError(f"Texture {item.get('id')} is not eligible for installation.")
        _verify_item_inputs(root, item, require_archive=True)
        stage_path = _resolve_under_root(root, item["stage_dds_rel"], must_exist=True)
        if sha256_file(stage_path) != item["converted"]["stage_dds_sha256"]:
            raise TextureDeliveryError(f"Staged output changed after QA: {item['stage_dds_rel']}.")
        if _current_target_sha(root, item) != item["expected_target_sha256"]:
            raise TextureDeliveryError(f"CAS target preimage changed: {item['target_rel']}.")
    if not execute:
        return {
            "status": "dry_run",
            "batch_id": manifest["batch_id"],
            "writes_performed": False,
            "targets": [
                {
                    "target_rel": item["target_rel"],
                    "expected_before_sha256": item["expected_target_sha256"],
                    "staged_after_sha256": item["converted"]["stage_dds_sha256"],
                }
                for item in manifest["items"]
            ],
        }

    backups = []
    prepared = []
    committed = []
    stage_root = _resolve_under_root(root, manifest["staging_root_rel"], must_exist=False)
    if not stage_root.is_dir():
        raise TextureDeliveryError("Staging root is missing or is not a directory.")
    try:
        for item in manifest["items"]:
            target = _resolve_under_root(root, item["target_rel"], must_exist=False)
            staged = _resolve_under_root(root, item["stage_dds_rel"], must_exist=True)
            output_sha = item["converted"]["stage_dds_sha256"]
            backup_rel = str(PurePosixPath(manifest["staging_root_rel"]) / item["id"] / "target_preimage.bin")
            backup_path = _resolve_under_root(root, backup_rel, must_exist=False)
            if target.exists():
                _copy_verified(target, backup_path, item["expected_target_sha256"])
                backups.append({"target": target, "backup": backup_path, "preimage_sha256": item["expected_target_sha256"]})
            prepared_temp = _copy_atomic_from_stage(staged, target, output_sha, manifest["batch_id"])
            prepared.append({
                "item": item,
                "target": target,
                "temp": prepared_temp,
                "output_sha256": output_sha,
                "backup": backup_path if target.exists() else None,
            })

        for entry in prepared:
            item = entry["item"]
            _verify_item_inputs(root, item, allow_installed_target=False)
            if _current_target_sha(root, item) != item["expected_target_sha256"]:
                raise TextureDeliveryError(f"CAS target changed during preflight: {item['target_rel']}.")
        for entry in prepared:
            item = entry["item"]
            if _current_target_sha(root, item) != item["expected_target_sha256"]:
                raise TextureDeliveryError(f"CAS target changed immediately before replace: {item['target_rel']}.")
            os.replace(entry["temp"], entry["target"])
            committed.append(entry)
            if sha256_file(entry["target"]) != entry["output_sha256"]:
                raise TextureDeliveryError(f"Installed output hash mismatch: {item['target_rel']}.")
        for item in manifest["items"]:
            if item["source_rel"] != item["target_rel"]:
                source = _resolve_under_root(root, item["source_rel"], must_exist=True)
                if sha256_file(source) != item["source_sha256"]:
                    raise TextureDeliveryError(f"Source input changed after installation: {item['source_rel']}.")
            archive = _resolve_under_root(root, item["source_archive_rel"], must_exist=True)
            if sha256_file(archive) != item["source_sha256"]:
                raise TextureDeliveryError(f"Source archive no longer preserves its original SHA: {item['id']}.")
        manifest["install"] = {
            "status": "installed",
            "mode": "compare_and_swap",
            "installed_at_utc": datetime.now(timezone.utc).isoformat(),
            "targets": [
                {
                    "target_rel": item["target_rel"],
                    "before_sha256": item["expected_target_sha256"],
                    "after_sha256": item["converted"]["stage_dds_sha256"],
                    "backup_rel": next(
                        (str(entry["backup"].relative_to(root).as_posix()) for entry in prepared
                         if entry["item"]["id"] == item["id"] and entry["backup"] is not None),
                        None,
                    ),
                }
                for item in manifest["items"]
            ],
        }
        manifest["state"] = "installed"
        _atomic_json(path, manifest)
        return manifest
    except BaseException as error:
        rollback_errors = []
        for entry in reversed(committed):
            target = entry["target"]
            item = entry["item"]
            try:
                if not target.is_file() or sha256_file(target) != entry["output_sha256"]:
                    raise TextureDeliveryError(f"Rollback CAS refuses externally changed target: {item['target_rel']}.")
                backup = entry["backup"]
                if backup is None:
                    target.unlink()
                else:
                    temp_restore = _copy_atomic_from_stage(backup, target, item["expected_target_sha256"], manifest["batch_id"])
                    os.replace(temp_restore, target)
                    if sha256_file(target) != item["expected_target_sha256"]:
                        raise TextureDeliveryError(f"Rollback hash mismatch: {item['target_rel']}.")
            except Exception as rollback_error:
                rollback_errors.append(str(rollback_error))
        for entry in prepared:
            try:
                entry["temp"].unlink()
            except OSError:
                pass
        manifest["state"] = "install_failed"
        manifest["install"] = {
            "status": "rolled_back" if not rollback_errors else "needs_recovery",
            "error": str(error),
            "rollback_errors": rollback_errors,
        }
        _atomic_json(path, manifest)
        if rollback_errors:
            raise TextureDeliveryError(
                f"Batch install failed and rollback needs recovery: {rollback_errors}"
            ) from error
        raise TextureDeliveryError(f"Batch install failed; committed targets were rolled back: {error}") from error

"""Deterministic job paths and append-only evidence helpers.

This module deliberately keeps all write operations inside the model job root.
The provider and Blender adapters use the same helpers so a task can be
reproduced without copying workstation-specific paths into the job manifest.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional


REPO_ROOT = Path(__file__).resolve().parents[3]
OWNER_ID = "chaos_redux_3d_model_pilots"
MODEL_ROOT = REPO_ROOT / "docs" / "assets" / OWNER_ID / "models_3d"
PIPELINE_ROOT = REPO_ROOT / ".tools" / "3d_pipeline"
CONFIG_ROOT = PIPELINE_ROOT / "config"
STAGING_ROOT = PIPELINE_ROOT / "staging"
ADAPTER_CONFIG_PATH = CONFIG_ROOT / "blender_hoi4_adapter.json"

JOB_DIRS = (
    "refs/original",
    "refs/derived",
    "refs/briefs",
    "provider/requests",
    "provider/responses",
    "provider/tasks",
    "provider/credits",
    "provider/downloads",
    "provider/rejected",
  "blender/source",
  "blender/reference",
  "blender/working",
    "blender/checkpoints",
    "blender/previews",
    "blender/reports",
    "textures/source",
    "textures/processed",
    "textures/dds",
    "export/mesh",
    "export/anim",
    "logs",
    "runtime",
    "validation",
    "evidence",
)


def utc_now() -> str:
    """Return a stable UTC timestamp suitable for JSON evidence."""

    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def safe_slug(value: str) -> str:
    """Normalize an owner or asset id without accepting path syntax."""

    normalized = re.sub(r"[^a-z0-9_]+", "_", value.lower()).strip("_")
    if not normalized:
        raise ValueError("A non-empty lowercase slug is required.")
    return normalized


def read_job_document(path: Path) -> Dict[str, Any]:
    """Read the repository's JSON-compatible job YAML or a native JSON job file."""

    raw = path.read_text(encoding="utf-8")
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        try:
            import yaml
        except ImportError as exc:
            raise RuntimeError(
                "A non-JSON job.yaml requires the repository's PyYAML dependency."
            ) from exc
        value = yaml.safe_load(raw)
    if not isinstance(value, dict):
        raise ValueError(f"Job document must contain a mapping: {path}")
    return value


def _configured_job_overrides() -> Dict[str, Path]:
    """Resolve allowlisted adapter job overrides without accepting arbitrary paths."""

    if not ADAPTER_CONFIG_PATH.exists():
        return {}
    config = json.loads(ADAPTER_CONFIG_PATH.read_text(encoding="utf-8"))
    overrides = config.get("job_overrides", {})
    if not isinstance(overrides, dict):
        raise ValueError("blender_hoi4_adapter.json job_overrides must be a mapping.")
    resolved: Dict[str, Path] = {}
    for job_id, raw_path in overrides.items():
        if not isinstance(job_id, str) or not isinstance(raw_path, str):
            raise ValueError("Adapter job overrides must use string ids and paths.")
        candidate = Path(raw_path)
        if not candidate.is_absolute():
            candidate = REPO_ROOT / candidate
        candidate = candidate.resolve()
        assert_within(candidate, REPO_ROOT)
        resolved[safe_slug(job_id)] = candidate
    return resolved


def _assert_supported_job_root(path: Path) -> Path:
    """Allow only the generic pilot root or an explicit adapter override root."""

    resolved = path.resolve()
    allowed_roots = [MODEL_ROOT.resolve(), *_configured_job_overrides().values()]
    for allowed_root in allowed_roots:
        try:
            resolved.relative_to(allowed_root)
            return resolved
        except ValueError:
            continue
    raise ValueError(f"Path is outside the configured 3D job roots: {resolved}")


def resolve_job_root(asset_slug: str, owner_id: str = OWNER_ID) -> Path:
    """Resolve the only supported job root for an asset."""

    owner = safe_slug(owner_id)
    slug = safe_slug(asset_slug)
    del owner
    root = _configured_job_overrides().get(slug, MODEL_ROOT / slug)
    return _assert_supported_job_root(root)


def ensure_job_layout(job_root: Path) -> Path:
    """Create the deterministic job directories and return the resolved root."""

    root = _assert_supported_job_root(job_root)
    root.mkdir(parents=True, exist_ok=True)
    for relative in JOB_DIRS:
        (root / relative).mkdir(parents=True, exist_ok=True)
    return root


def assert_within(path: Path, allowed_root: Path) -> Path:
    """Reject paths escaping an approved root, including traversal."""

    resolved_path = path.resolve()
    resolved_root = allowed_root.resolve()
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"Path is outside the approved root: {resolved_path}") from exc
    return resolved_path


def job_path(job_root: Path, relative: str, *, must_exist: bool = False) -> Path:
    """Resolve a job-relative path and enforce the job boundary."""

    candidate = assert_within(job_root / relative, job_root)
    if must_exist and not candidate.exists():
        raise FileNotFoundError(candidate)
    return candidate


def sha256_file(path: Path) -> str:
    """Calculate a streaming SHA-256 digest."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def file_record(path: Path, *, relative_to: Optional[Path] = None) -> Dict[str, Any]:
    """Return an evidence-friendly file record."""

    path = path.resolve()
    record: Dict[str, Any] = {
        "path": str(path),
        "name": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }
    if relative_to is not None:
        record["relative_path"] = path.relative_to(relative_to.resolve()).as_posix()
    return record


def write_json(path: Path, value: Any, *, indent: int = 2) -> Path:
    """Write UTF-8 JSON with a trailing newline."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=indent, sort_keys=True) + "\n", encoding="utf-8")
    return path


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def append_jsonl(path: Path, value: Dict[str, Any]) -> Path:
    """Append one immutable event to a JSONL history file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(value, sort_keys=True) + "\n")
    return path


def append_history(
    job_root: Path,
    *,
    state: str,
    event: str,
    actor: str,
    details: Optional[Dict[str, Any]] = None,
) -> Path:
    """Append a state transition to the job's append-only lineage."""

    return append_jsonl(
        job_root / "history.jsonl",
        {
            "timestamp": utc_now(),
            "state": state,
            "event": event,
            "actor": actor,
            "details": details or {},
        },
    )


def redact(value: Any) -> Any:
    """Recursively redact credential-shaped values before evidence writes."""

    secret_names = {
        "meshy_api_key",
        "api_key",
        "authorization",
        "access_token",
        "refresh_token",
        "token",
    }
    if isinstance(value, dict):
        return {
            key: ("[REDACTED]" if key.lower() in secret_names else redact(item))
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [redact(item) for item in value]
    return value


def relative_file_list(root: Path, suffixes: Iterable[str]) -> list[str]:
    """List evidence files relative to a root, excluding transient caches."""

    wanted = {suffix.lower() for suffix in suffixes}
    result: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        if path.suffix.lower() in wanted:
            result.append(path.relative_to(root).as_posix())
    return sorted(result)

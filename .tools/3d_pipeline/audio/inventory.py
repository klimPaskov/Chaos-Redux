"""Runtime sound inventory, family-pool, and attribution evidence helpers."""

import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

from .metrics import sha256_file


def load_json(path: Path) -> Tuple[Dict[str, Any], str]:
    payload = path.read_bytes()
    return json.loads(payload.decode("utf-8-sig")), hashlib.sha256(payload).hexdigest()


def flatten_runtime_inventory(inventory: Dict[str, Any]) -> Tuple[Dict[str, Dict[str, Any]], List[Dict[str, Any]]]:
    """Return file records and cue rows from the pipeline baseline inventory."""
    files: Dict[str, Dict[str, Any]] = {}
    cues: List[Dict[str, Any]] = []
    for model in inventory.get("models", []):
        model_id = str(model.get("pdxmesh", "unknown_model"))
        if model_id.endswith("_mesh"):
            model_id = model_id[:-5]
        for cue in model.get("sound_cues", []):
            sample_rows = cue.get("samples", [])
            unresolved_sample_count = sum(
                1 for sample in sample_rows if not isinstance(sample.get("file"), dict)
            )
            cues.append(
                {
                    "unit_id": model_id,
                    "soundeffect": cue.get("name"),
                    "loop": _as_bool(cue.get("loop")),
                    "sample_count": len(sample_rows),
                    "unresolved_sample_count": unresolved_sample_count,
                    "sample_names": [sample.get("name") for sample in sample_rows],
                    "paths": [
                        (sample.get("file") or {}).get("path")
                        if isinstance(sample.get("file") or {}, dict)
                        else None
                        for sample in sample_rows
                    ],
                }
            )
            for sample in sample_rows:
                info = sample.get("file") or {}
                if not isinstance(info, dict):
                    continue
                relative_path = info.get("path")
                if not relative_path:
                    continue
                record = files.setdefault(
                    relative_path,
                    {
                        "path": relative_path,
                        "sha256": info.get("sha256"),
                        "bytes": info.get("bytes"),
                        "consumer_units": [],
                        "consumer_cues": [],
                        "sample_names": [],
                    },
                )
                if model_id not in record["consumer_units"]:
                    record["consumer_units"].append(model_id)
                record["consumer_cues"].append(cue.get("name"))
                record["sample_names"].append(sample.get("name"))
                # The per-model inventory is the source of record; report
                # disagreement rather than silently selecting one checksum.
                if record.get("sha256") != info.get("sha256"):
                    record["inventory_sha_conflict"] = True
        for sample in model.get("additional_sound_files", []):
            info = sample if isinstance(sample, dict) else {}
            relative_path = info.get("path")
            if not relative_path:
                continue
            record = files.setdefault(
                relative_path,
                {
                    "path": relative_path,
                    "sha256": info.get("sha256"),
                    "bytes": info.get("bytes"),
                    "consumer_units": [],
                    "consumer_cues": [],
                    "sample_names": [],
                    "additional_sound_file": True,
                },
            )
            if model_id not in record["consumer_units"]:
                record["consumer_units"].append(model_id)
            record["additional_sound_file"] = True
            record["consumer_cues"].append("additional_sound_file")
            record["sample_names"].append(Path(relative_path).stem)
            if record.get("sha256") != info.get("sha256"):
                record["inventory_sha_conflict"] = True
    return files, cues


def _as_bool(value: Any) -> bool:
    return str(value).strip().lower() in ("yes", "true", "1")


def parse_soundeffect_assets(sound_root: Path) -> Dict[str, List[Dict[str, Any]]]:
    """Read named soundeffect blocks without modifying source asset files."""
    definitions: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for path in sorted(sound_root.rglob("*.asset")):
        try:
            text = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError):
            continue
        for line_number, block in _extract_blocks(text, "soundeffect"):
            name = _assignment(block, "name")
            if not name:
                continue
            sounds = re.findall(r"\bsound\s*=\s*[\"']?([^\s\"'}]+)", block, flags=re.IGNORECASE)
            definitions[name].append(
                {
                    "name": name,
                    "asset_path": str(path),
                    "line": line_number,
                    "sample_names": sounds,
                    "sample_count": len(sounds),
                    "loop": _as_bool(_assignment(block, "loop")),
                    "prevent_random_repetition": _as_bool(_assignment(block, "prevent_random_repetition")),
                }
            )
    return dict(definitions)


def _assignment(block: str, key: str) -> Optional[str]:
    match = re.search(
        r"\b{}\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s}}]+))".format(re.escape(key)),
        block,
        flags=re.IGNORECASE,
    )
    if not match:
        return None
    return next((part for part in match.groups() if part is not None), None)


def _extract_blocks(text: str, keyword: str) -> Iterable[Tuple[int, str]]:
    pattern = re.compile(r"\b{}\s*=\s*\{{".format(re.escape(keyword)), flags=re.IGNORECASE)
    for match in pattern.finditer(text):
        open_brace = match.end() - 1
        depth = 0
        quoted = False
        quote = ""
        escaped = False
        in_comment = False
        end = None
        for index in range(open_brace, len(text)):
            char = text[index]
            if in_comment:
                if char in "\r\n":
                    in_comment = False
                continue
            if quoted:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == quote:
                    quoted = False
                continue
            if char in "\"'":
                quoted = True
                quote = char
            elif char == "#":
                in_comment = True
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end = index + 1
                    break
        if end is not None:
            yield text.count("\n", 0, match.start()) + 1, text[open_brace:end]


def build_sound_coverage(
    sound_root: Path,
    cue_rows: Sequence[Dict[str, Any]],
    attribution_map: Optional[Dict[str, Any]] = None,
    repo_root: Optional[Path] = None,
    file_records: Optional[Dict[str, Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    definitions = parse_soundeffect_assets(sound_root)
    cue_report: List[Dict[str, Any]] = []
    for cue in cue_rows:
        name = cue.get("soundeffect")
        candidates = definitions.get(str(name), [])
        definition = candidates[0] if len(candidates) == 1 else None
        sample_count = int(cue.get("sample_count", 0))
        cue_report.append(
            {
                "unit_id": cue.get("unit_id"),
                "soundeffect": name,
                "loop": cue.get("loop"),
                "sample_count": sample_count,
                "sample_names": cue.get("sample_names", []),
                "single_sample_cue": sample_count == 1,
                "minimum_two_takes_met": sample_count >= 2,
                "preferred_three_takes_met": sample_count >= 3,
                "prevent_random_repetition": (
                    definition.get("prevent_random_repetition") if definition else None
                ),
                "definition_count": len(candidates),
                "definition_path": definition.get("asset_path") if definition else None,
                "definition_line": definition.get("line") if definition else None,
                "status": _cue_status(sample_count, definition, candidates),
            }
        )

    attribution = []
    source_paths = {
        path
        for cue in cue_rows
        for path in cue.get("paths", [])
        if path and _is_mod_sound_path(path)
    }
    source_paths.update(path for path in (file_records or {}) if _is_mod_sound_path(path))
    source_paths = sorted(source_paths)
    for relative_path in source_paths:
        spec = (attribution_map or {}).get(relative_path)
        if spec:
            attribution.append(_read_attribution(relative_path, spec, repo_root))
        else:
            attribution.append(
                {
                    "source_path": relative_path,
                    "status": "not_mapped_to_existing_attribution_manifest",
                    "license_claim": "not_assessed",
                    "derivative_license_verified": False,
                }
            )
    attribution_status_counts: Dict[str, int] = defaultdict(int)
    for row in attribution:
        attribution_status_counts[str(row.get("status", "unknown"))] += 1
    return {
        "cue_count": len(cue_report),
        "single_sample_cues": [row for row in cue_report if row["single_sample_cue"]],
        "cues": cue_report,
        "attribution_coverage_count": len(attribution),
        "attribution_status_counts": dict(sorted(attribution_status_counts.items())),
        "attribution_coverage": attribution,
    }


def _is_mod_sound_path(value: str) -> bool:
    normalized = str(value).replace("\\", "/")
    return not Path(value).is_absolute() and normalized.lower().startswith("sound/")


def _cue_status(sample_count: int, definition: Optional[Dict[str, Any]], candidates: Sequence[Dict[str, Any]]) -> str:
    if len(candidates) != 1:
        return "definition_missing_or_ambiguous"
    if sample_count < 2:
        return "single_sample_requires_more_takes"
    if not definition or not definition.get("prevent_random_repetition"):
        return "prevent_random_repetition_missing"
    if sample_count < 3:
        return "minimum_met_preferred_three_takes_missing"
    return "covered"


def _read_attribution(relative_path: str, spec: Any, repo_root: Optional[Path]) -> Dict[str, Any]:
    if isinstance(spec, str):
        spec = {"manifest_path": spec}
    manifest_value = spec.get("manifest_path") if isinstance(spec, dict) else None
    if not manifest_value:
        return {"source_path": relative_path, "status": "manifest_path_missing"}
    manifest_path = Path(manifest_value)
    if not manifest_path.is_absolute() and repo_root:
        manifest_path = repo_root / manifest_path
    if not manifest_path.is_file():
        return {
            "source_path": relative_path,
            "manifest_path": str(manifest_path),
            "status": "manifest_missing",
        }
    raw = manifest_path.read_bytes()
    text = raw.decode("utf-8-sig", errors="replace")
    expected_row = spec.get("source_row") if isinstance(spec, dict) else None
    needle = spec.get("match") if isinstance(spec, dict) else None
    supplied_sha = spec.get("source_sha256") if isinstance(spec, dict) else None
    if expected_row:
        rows = [expected_row] if expected_row in text else []
    else:
        tokens = [Path(relative_path).name]
        source_sha = spec.get("source_sha256") if isinstance(spec, dict) else None
        if source_sha:
            tokens.append(source_sha)
        if needle:
            tokens = [str(needle)]
        rows = [line for line in text.splitlines() if any(token and token in line for token in tokens)]
    return {
        "source_path": relative_path,
        "manifest_path": str(manifest_path),
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "matched_rows": rows,
        "status": "row_matched" if rows else "source_row_unresolved",
        "source_sha256_supplied_by_manifest_entry": supplied_sha,
        "source_sha256_appears_in_attribution_document": (
            str(supplied_sha).lower() in text.lower() if supplied_sha else None
        ),
        "license_claim": "inherited_source_record_not_reverified_for_derivative",
        "derivative_license_verified": False,
    }


def summarize_duplicates(
    file_records: Dict[str, Dict[str, Any]],
    actual_hashes: Dict[str, str],
    family_pools: Optional[Sequence[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    by_hash: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for path, record in file_records.items():
        actual_hash = actual_hashes.get(path)
        if not actual_hash:
            continue
        by_hash[actual_hash].append(
            {
                "path": path,
                "consumer_units": sorted(set(record.get("consumer_units", []))),
                "consumer_cues": sorted(set(filter(None, record.get("consumer_cues", [])))),
            }
        )
    pools = list(family_pools or [])
    duplicate_groups = []
    for digest, files in sorted(by_hash.items()):
        units = sorted({unit for item in files for unit in item["consumer_units"]})
        distinct_paths = sorted({item["path"] for item in files})
        if len(distinct_paths) <= 1 and len(units) <= 1:
            continue
        pool = _matching_pool(pools, digest, units, distinct_paths)
        duplicate_groups.append(
            {
                "sha256": digest,
                "unit_ids": units,
                "paths": distinct_paths,
                "references": files,
                "family_pool": pool,
                "status": "declared_family_pool" if pool else ("undeclared_cross_unit_duplicate" if len(units) > 1 else "same_unit_duplicate"),
            }
        )
    return {
        "duplicate_group_count": len(duplicate_groups),
        "undeclared_cross_unit_duplicates": [row for row in duplicate_groups if row["status"] == "undeclared_cross_unit_duplicate"],
        "duplicate_groups": duplicate_groups,
    }


def _matching_pool(pools: Sequence[Dict[str, Any]], digest: str, units: Sequence[str], paths: Sequence[str]) -> Optional[Dict[str, Any]]:
    for pool in pools:
        declared_hashes = pool.get("sha256", [])
        if isinstance(declared_hashes, str):
            declared_hashes = [declared_hashes]
        declared_units = sorted(set(pool.get("unit_ids", [])))
        declared_paths = sorted(set(pool.get("paths", [])))
        if (
            digest in declared_hashes
            and set(units).issubset(declared_units)
            and set(paths).issubset(declared_paths)
            and pool.get("id")
            and pool.get("rationale")
        ):
            return {
                "id": pool.get("id"),
                "unit_ids": declared_units,
                "paths": declared_paths,
                "rationale": pool.get("rationale"),
            }
    return None


def source_lineage(
    repo_root: Path,
    source_path: Path,
    manifest_entry: Dict[str, Any],
    inventory_record: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    attribution_spec = manifest_entry.get("attribution") or {}
    manifest_value = attribution_spec.get("manifest_path")
    manifest_record: Dict[str, Any] = {"status": "not_supplied", "derivative_license_verified": False}
    if manifest_value:
        manifest_record = _read_attribution(
            str(source_path), attribution_spec, repo_root
        )
    raw_entry = dict(manifest_entry)
    return {
        "source_manifest_entry": raw_entry,
        "inventory_source_sha256": inventory_record.get("sha256") if inventory_record else None,
        "inventory_record": inventory_record,
        "attribution": manifest_record,
        "license_claim": "inherited_source_record_not_reverified_for_derivative",
        "derivative_license_verified": False,
    }


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def resolved_path_under(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    root = root.resolve()
    try:
        path.relative_to(root)
    except ValueError:
        raise ValueError("path escapes approved root: {}".format(relative))
    return path

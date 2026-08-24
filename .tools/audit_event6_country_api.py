#!/usr/bin/env python3
"""Check that the broad Chaos Redux country API exposes every Event 006 carrier.

This is a static namespace audit only. It does not promote a package, grant an
origin, or prove that a carrier is ready for release.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parents[1]
BROAD = ROOT / "common/script_constants/chaosx_country_registry_constants.txt"
EVENT6 = ROOT / "common/script_constants/006_independence_wave_constants_registry.txt"
CANDIDATES = ROOT / "docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv"
INSTALLED_BINDINGS = ROOT / "docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv"


def array_body(path: Path, name: str) -> list[str]:
	text = path.read_text(encoding="utf-8-sig")
	match = re.search(rf"\b{re.escape(name)}\s*=\s*\{{(.*?)\n\t\}}", text, re.S)
	if match is None:
		raise RuntimeError(f"array not found: {path}:{name}")
	body = "\n".join(line.split("#", 1)[0] for line in match.group(1).splitlines())
	return body.split()


def csv_rows(path: Path) -> dict[str, dict[str, str]]:
	with path.open(newline="", encoding="utf-8-sig") as handle:
		return {row["package_id"]: row for row in csv.DictReader(handle)}


def validate_iw031_current_map_crosswalk() -> Optional[str]:
	"""Keep the public-baseline caveat tied to the exact installed KOS binding."""
	candidates = csv_rows(CANDIDATES)
	bindings = csv_rows(INSTALLED_BINDINGS)
	candidate = candidates.get("IW-031")
	binding = bindings.get("IW-031")
	if candidate is None or binding is None:
		return "IW-031 crosswalk row missing from candidate or installed-binding authority"
	checks = {
		"candidate.resolved_tag": (candidate.get("resolved_tag", "").strip(), "KOS"),
		"candidate.baseline_anchor_state_ids": (candidate.get("baseline_anchor_state_ids", "").strip(), ""),
		"candidate.automatic_pool_disposition": (candidate.get("automatic_pool_disposition", "").strip(), "automatic_pool_ready_if_unique_state_exists"),
		"binding.resolved_tag": (binding.get("resolved_tag", "").strip(), "KOS"),
		"binding.anchor_state_ids": (binding.get("anchor_state_ids", "").strip(), "802"),
		"binding.compact_state_ids": (binding.get("compact_state_ids", "").strip(), "802"),
		"binding.anchor_state_names": (binding.get("anchor_state_names", "").strip(), "Kosovo"),
		"binding.rebind_status": (binding.get("rebind_status", "").strip(), "new_current_state_binding"),
		"binding.installed_state_history_files": (binding.get("installed_state_history_files", "").strip(), "802-Kosovo.txt"),
	}
	for field, (actual, expected) in checks.items():
		if actual != expected:
			return f"IW-031 crosswalk mismatch for {field}: expected {expected!r}, got {actual!r}"
	return None


def main() -> int:
	broad = array_body(BROAD, "all_chaosx_country_tags")
	resolved = array_body(EVENT6, "all_resolved_carrier_tags")
	soviet = array_body(BROAD, "soviet_collapse_tags")
	africa = array_body(BROAD, "africa_tags")
	broad_set = set(broad)
	resolved_set = set(resolved)
	missing = sorted(resolved_set - broad_set)
	missing_soviet = sorted(set(soviet) - broad_set)
	missing_africa = sorted(set(africa) - broad_set)
	duplicates = sorted(tag for tag in broad_set if broad.count(tag) > 1)
	crosswalk_error = validate_iw031_current_map_crosswalk()
	if missing or missing_soviet or missing_africa or duplicates or crosswalk_error:
		if missing:
			print("missing resolved carriers:", " ".join(missing))
		if missing_soviet:
			print("missing Soviet carriers:", " ".join(missing_soviet))
		if missing_africa:
			print("missing Africa carriers:", " ".join(missing_africa))
		if duplicates:
			print("duplicate broad carriers:", " ".join(duplicates))
		if crosswalk_error:
			print(crosswalk_error)
		return 1
	print(
		"Event 006 country API audit passed: "
		f"broad={len(broad_set)} unique tags; "
		f"resolved={len(resolved_set)} unique carriers; "
		f"Soviet={len(set(soviet))}; Africa={len(set(africa))}; "
		"missing=0; duplicates=0; IW-031-crosswalk=pass"
	)
	return 0


if __name__ == "__main__":
	sys.exit(main())

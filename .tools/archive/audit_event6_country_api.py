#!/usr/bin/env python3
"""Check that the broad Chaos Redux country API exposes every Event 006 carrier.

This is a static namespace audit only. It does not promote a package, grant an
origin, or prove that a carrier is ready for release.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BROAD = ROOT / "common/script_constants/chaosx_country_registry_constants.txt"
EVENT6 = ROOT / "common/script_constants/006_independence_wave_country_registry_constants.txt"


def array_body(path: Path, name: str) -> list[str]:
	text = path.read_text(encoding="utf-8-sig")
	match = re.search(rf"\b{re.escape(name)}\s*=\s*\{{(.*?)\n\t\}}", text, re.S)
	if match is None:
		raise RuntimeError(f"array not found: {path}:{name}")
	body = "\n".join(line.split("#", 1)[0] for line in match.group(1).splitlines())
	return body.split()


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
	if missing or missing_soviet or missing_africa or duplicates:
		if missing:
			print("missing resolved carriers:", " ".join(missing))
		if missing_soviet:
			print("missing Soviet carriers:", " ".join(missing_soviet))
		if missing_africa:
			print("missing Africa carriers:", " ".join(missing_africa))
		if duplicates:
			print("duplicate broad carriers:", " ".join(duplicates))
		return 1
	print(
		"Event 006 country API audit passed: "
		f"broad={len(broad_set)} unique tags; "
		f"resolved={len(resolved_set)} unique carriers; "
		f"Soviet={len(set(soviet))}; Africa={len(set(africa))}; "
		"missing=0; duplicates=0"
	)
	return 0


if __name__ == "__main__":
	sys.exit(main())

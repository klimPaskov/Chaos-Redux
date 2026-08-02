"""Audit Event 006 country flag triplets against the registered tag list.

HOI4 loads normal, medium, and small flag atlases independently. This audit
checks the engine-facing TGA names for every Event 006 country registration and
reports missing files without treating a dormant package as playable.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAG_FILE = ROOT / "common/country_tags/006_independence_wave_countries.txt"
FLAG_DIRS = (ROOT / "gfx/flags", ROOT / "gfx/flags/medium", ROOT / "gfx/flags/small")
TAG_RE = re.compile(r"^\s*([A-Z][A-Z0-9_]{2})\s*=", re.MULTILINE)


def registered_tags() -> list[str]:

	text = TAG_FILE.read_text(encoding="utf-8-sig")
	return sorted(dict.fromkeys(TAG_RE.findall(text)))


def main() -> int:

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--strict", action="store_true", help="return non-zero when any triplet is incomplete")
	args = parser.parse_args()

	tags = registered_tags()
	missing: dict[str, list[str]] = {}
	for tag in tags:
		for directory in FLAG_DIRS:
			path = directory / f"{tag}.tga"
			if not path.is_file():
				missing.setdefault(tag, []).append(str(path.relative_to(ROOT)).replace("\\", "/"))

	print(f"registered Event 006 tags: {len(tags)}")
	print(f"complete flag triplets: {len(tags) - len(missing)}")
	print(f"incomplete flag triplets: {len(missing)}")
	for tag, paths in missing.items():
		print(f"- {tag}: {', '.join(paths)}")

	return 1 if args.strict and missing else 0


if __name__ == "__main__":
	raise SystemExit(main())

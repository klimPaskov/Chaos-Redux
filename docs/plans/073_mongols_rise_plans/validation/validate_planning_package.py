#!/usr/bin/env python3
"""Check this planning package's manifest and local Markdown links, not game behavior."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote

def find_root() -> Path:
    for root in Path(__file__).resolve().parents:
        if (root / "docs/plans/073_mongols_rise_plans/package_manifest.json").is_file():
            return root
    raise RuntimeError("Cannot find the extracted Event 073 planning package")

def main() -> int:
    root = find_root()
    manifest_path = root / "docs/plans/073_mongols_rise_plans/package_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors = []
    for entry in manifest["files"]:
        path = root / entry["path"]
        if not path.is_file():
            errors.append(f"Missing file: {entry['path']}")
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry["sha256"]:
            errors.append(f"Changed hash: {entry['path']}")
        if len(data) != entry["bytes"]:
            errors.append(f"Changed length: {entry['path']}")
        if path.suffix == ".md":
            text = data.decode("utf-8-sig")
            for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
                target = target.strip().split("#", 1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                dest = (path.parent / unquote(target)).resolve()
                if not dest.exists():
                    errors.append(f"Broken link in {entry['path']}: {target}")
    goal = root / "docs/plans/073_mongols_rise_plans/prompts/073_mongols_rise_goal_prompt.md"
    if not 3500 <= len(goal.read_text(encoding="utf-8").strip()) <= 4000:
        errors.append("Goal prompt must contain 3500 to 4000 characters")
    if errors:
        print("PACKAGE CHECK FAILED")
        print("\n".join(errors))
        return 1
    print(f"PACKAGE CHECK PASSED: {len(manifest['files'])} manifest-listed files")
    print("This does not prove implementation, subagent review, or live-game validation.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"PACKAGE CHECK FAILED: {exc}", file=sys.stderr)
        sys.exit(1)

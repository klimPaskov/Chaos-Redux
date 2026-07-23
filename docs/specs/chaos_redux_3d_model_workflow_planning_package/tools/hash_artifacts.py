#!/usr/bin/env python3
"""Create a deterministic SHA256 inventory for files under one artifact root."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CHUNK_SIZE = 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--exclude", action="append", default=[], help="Relative path prefix to exclude.")
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"artifact root is not a directory: {root}")

    excludes = tuple(item.replace("\\", "/").rstrip("/") for item in args.exclude)
    rows: list[dict[str, object]] = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        relative = path.relative_to(root).as_posix()
        if any(relative == prefix or relative.startswith(prefix + "/") for prefix in excludes):
            continue
        rows.append(
            {
                "path": relative,
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )

    payload = {
        "root": str(root),
        "algorithm": "sha256",
        "file_count": len(rows),
        "files": rows,
    }
    serialized = json.dumps(payload, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(serialized, encoding="utf-8")
    else:
        print(serialized, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

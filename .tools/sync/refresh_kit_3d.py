#!/usr/bin/env python3
"""Replace the pinned kit 3D unit tools in `.tools/kit_3d/` with the files of one Agentic HOI4 Modding Kit commit.

`.tools/kit_3d/mapping.json` lists the kit files to take, as paths under the kit's `.tools/3d_pipeline/`. They are
written to `.tools/kit_3d/` with the same layout, so each tool finds its own `lib/`, `blender/` and `config/`, and
`manifest.json` records the kit commit and the SHA-256 of every file. The files are read from the commit with git,
never from the kit's working tree, so uncommitted kit edits cannot enter the snapshot. `--check` verifies the
snapshot against its manifest and fails on any edit: change the tools upstream in the kit, then refresh.

The Chaos Redux 3D pipeline in `.tools/3d_pipeline/` stays as it is. The snapshot adds the kit's unit checks
(`check_unit_files.py`), the independent visual review (`review_unit.py`) and the free mesh repair
(`repair_unit.py`), which run on any exported unit folder.

    python .tools/sync/refresh_kit_3d.py --kit <kit repository> --commit <revision>
    python .tools/sync/refresh_kit_3d.py --check

Standard library only; runs on Python 3.9 or newer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence

SNAPSHOT = Path(".tools") / "kit_3d"
KIT_PREFIX = ".tools/3d_pipeline/"
TEXT_SUFFIXES = (".py", ".md", ".json", ".txt", ".toml", ".yaml", ".yml")
KEEP = {"mapping.json", "manifest.json", "README.md"}


class KitSnapshotError(RuntimeError):
    pass


def to_lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def digest(rel: str, data: bytes) -> str:
    """SHA-256 of a file; text is hashed with LF endings so a CRLF checkout keeps its digest."""
    return hashlib.sha256(to_lf(data) if rel.lower().endswith(TEXT_SUFFIXES) else data).hexdigest()


def git(kit: Path, *arguments: str) -> bytes:
    try:
        return subprocess.run(["git", "-C", str(kit), *arguments], check=True, capture_output=True).stdout
    except (OSError, subprocess.CalledProcessError) as error:
        detail = error.stderr.decode("utf-8", "replace").strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        raise KitSnapshotError(f"git {' '.join(arguments)} failed in {kit}: {detail}") from error


def mapping(root: Path) -> List[str]:
    path = root / SNAPSHOT / "mapping.json"
    try:
        files = json.loads(path.read_text(encoding="utf-8"))["files"]
    except (OSError, ValueError, KeyError) as error:
        raise KitSnapshotError(f"cannot read {path}: {error}") from error
    if not files or any(not isinstance(rel, str) or rel.startswith(("/", "..")) or ".." in rel.split("/") for rel in files):
        raise KitSnapshotError(f"{path} must list kit-relative file paths under {KIT_PREFIX}")
    return sorted(files)


def refresh(root: Path, kit: Path, revision: str) -> int:
    commit = git(kit, "rev-parse", "--verify", f"{revision}^{{commit}}").decode("ascii").strip()
    files: Dict[str, bytes] = {}
    for rel in mapping(root):
        data = git(kit, "cat-file", "blob", f"{commit}:{KIT_PREFIX}{rel}")
        files[rel] = to_lf(data) if rel.lower().endswith(TEXT_SUFFIXES) else data
    snapshot = root / SNAPSHOT
    for old in sorted(snapshot.rglob("*"), reverse=True):
        rel = old.relative_to(snapshot).as_posix()
        if old.is_file() and rel not in KEEP:
            old.unlink()
        elif old.is_dir() and not any(old.iterdir()):
            old.rmdir()
    for rel, data in files.items():
        (snapshot / rel).parent.mkdir(parents=True, exist_ok=True)
        (snapshot / rel).write_bytes(data)
    manifest = {
        "_about": "Written by .tools/sync/refresh_kit_3d.py. SHA-256 of every snapshot file (text with LF line endings).",
        "kit": "Agentic HOI4 Modding Kit",
        "kit_commit": commit,
        "files": {rel: digest(rel, data) for rel, data in sorted(files.items())},
    }
    (snapshot / "manifest.json").write_bytes((json.dumps(manifest, indent=2) + "\n").encode("utf-8"))
    print(f"Snapshot of {len(files)} kit 3D files at {commit[:7]}")
    return 0


def check(root: Path) -> List[str]:
    """Differences between the snapshot and its manifest; empty when they match."""

    snapshot = root / SNAPSHOT
    try:
        recorded = json.loads((snapshot / "manifest.json").read_text(encoding="utf-8"))["files"]
    except (OSError, ValueError, KeyError) as error:
        return [f"cannot read {SNAPSHOT.as_posix()}/manifest.json: {error}"]
    problems = []
    wanted = mapping(root)
    if sorted(recorded) != wanted:
        problems.append("manifest.json and mapping.json list different files; run the refresh")
    for rel, expected in sorted(recorded.items()):
        path = snapshot / rel
        if not path.is_file():
            problems.append(f"{rel}: missing")
        elif digest(rel, path.read_bytes()) != expected:
            problems.append(f"{rel}: edited; change it in the kit and refresh")
    present = {p.relative_to(snapshot).as_posix() for p in snapshot.rglob("*") if p.is_file() and "__pycache__" not in p.parts}
    for extra in sorted(present - set(recorded) - KEEP):
        problems.append(f"{extra}: not in the snapshot; add it to the kit and mapping.json instead")
    return problems


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--kit", type=Path, help="the Agentic HOI4 Modding Kit repository")
    parser.add_argument("--commit", help="the kit revision to pin (a commit, tag or branch name)")
    parser.add_argument("--check", action="store_true", help="verify the snapshot against its manifest")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2], help="repository root (default: this repository)")
    args = parser.parse_args(argv)
    try:
        if args.check:
            problems = check(args.root.resolve())
            for problem in problems:
                print(f"ERROR: kit_3d: {problem}", file=sys.stderr)
            if not problems:
                print("kit_3d: snapshot matches its manifest")
            return 1 if problems else 0
        if not (args.kit and args.commit):
            parser.error("--kit and --commit are required to refresh")
        return refresh(args.root.resolve(), args.kit.resolve(), args.commit)
    except KitSnapshotError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

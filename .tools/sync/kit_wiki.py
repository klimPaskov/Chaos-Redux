#!/usr/bin/env python3
"""Keep the wiki snapshot identical to one Agentic HOI4 Modding Kit commit.

`paradox_wiki/` is the kit's, copied whole. `.tools/kit_wiki.json` records the kit commit and the SHA-256 of
every file in it (text with LF line endings). The check reports a changed, missing or extra
file as drift, so a hand edit here is caught; wiki fixes belong in the kit. A refresh copies the folder from
the kit commit and records them again, so taking a newer snapshot never fails the check.

    python .tools/sync/kit_wiki.py                                            # check (exit 1 on drift)
    python .tools/sync/kit_wiki.py --refresh --kit <kit repository> --commit <revision>

Standard library only; runs on Python 3.9 or newer.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from sync_engine_skills import EngineSkillError, file_digest, is_text, to_lf

FOLDERS = ("paradox_wiki",)
MANIFEST = ".tools/kit_wiki.json"
SKIPPED = ("__pycache__",)


def git(kit: Path, *arguments: str) -> bytes:
    try:
        return subprocess.run(["git", "-C", str(kit), *arguments], check=True, capture_output=True).stdout
    except (OSError, subprocess.CalledProcessError) as error:
        detail = error.stderr.decode("utf-8", "replace").strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        raise EngineSkillError(f"git {' '.join(arguments)} failed in {kit}: {detail}") from error


def local_files(root: Path) -> Dict[str, Path]:
    """Every file under the pinned folder, by path relative to the repository root."""
    files: Dict[str, Path] = {}
    for folder in FOLDERS:
        for path in sorted((root / folder).rglob("*")):
            if path.is_file() and not any(part in SKIPPED for part in path.parts):
                files[path.relative_to(root).as_posix()] = path
    return files


def load_manifest(root: Path) -> Dict[str, str]:
    path = root / MANIFEST
    try:
        files = json.loads(path.read_text(encoding="utf-8"))["files"]
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise EngineSkillError(f"cannot read {MANIFEST}: {error}") from error
    if not isinstance(files, dict):
        raise EngineSkillError(f"{MANIFEST} has no `files` table")
    return {str(rel): str(digest) for rel, digest in files.items()}


def check(root: Path) -> int:
    recorded = load_manifest(root)
    present = local_files(root)
    problems: List[str] = []
    for rel in sorted(set(recorded) | set(present)):
        if rel not in present:
            problems.append(f"DRIFT {rel}: missing")
        elif rel not in recorded:
            problems.append(f"DRIFT {rel}: not in the kit snapshot")
        elif file_digest(rel, present[rel].read_bytes()) != recorded[rel]:
            problems.append(f"DRIFT {rel}: differs from the kit snapshot")
    for line in problems:
        print(line)
    if problems:
        print(f"{len(problems)} wiki file(s) differ from the kit snapshot. Make the change in the kit, then refresh: "
              "python .tools/sync/kit_wiki.py --refresh --kit <kit repository> --commit <revision>")
        return 1
    print(f"Wiki snapshot matches the kit: {len(recorded)} files.")
    return 0


def kit_files(kit: Path, commit: str) -> Dict[str, bytes]:
    files: Dict[str, bytes] = {}
    for folder in FOLDERS:
        listing = git(kit, "ls-tree", "-r", "--name-only", "-z", commit, "--", f"{folder}/").decode("utf-8")
        for rel in (path for path in listing.split("\0") if path):
            if any(part in SKIPPED for part in rel.split("/")):
                continue
            data = git(kit, "cat-file", "blob", f"{commit}:{rel}")
            files[rel] = to_lf(data) if is_text(rel) else data
    if not any(rel.startswith("paradox_wiki/") for rel in files):
        raise EngineSkillError(f"the kit has no paradox_wiki/ at {commit[:7]}")
    return files


def refresh(root: Path, kit: Path, revision: str) -> int:
    commit = git(kit, "rev-parse", "--verify", f"{revision}^{{commit}}").decode("ascii").strip()
    files = kit_files(kit, commit)
    for folder in FOLDERS:
        shutil.rmtree(root / folder, ignore_errors=True)
    for rel, data in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_bytes(data)
    manifest = {
        "_about": "Written by .tools/sync/kit_wiki.py. SHA-256 of every file in paradox_wiki/ (text with LF line endings).",
        "kit": "Agentic HOI4 Modding Kit",
        "kit_commit": commit,
        "files": {rel: file_digest(rel, data) for rel, data in sorted(files.items())},
    }
    (root / MANIFEST).parent.mkdir(parents=True, exist_ok=True)
    (root / MANIFEST).write_bytes((json.dumps(manifest, indent=2) + "\n").encode("utf-8"))
    print(f"Wiki snapshot of {len(files)} files at kit {commit[:7]}")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2], help="repository root (default: this repository)")
    parser.add_argument("--check", action="store_true", help="check only (the default)")
    parser.add_argument("--refresh", action="store_true", help="copy paradox_wiki/ from the kit commit and record it")
    parser.add_argument("--kit", type=Path, help="the Agentic HOI4 Modding Kit repository (with --refresh)")
    parser.add_argument("--commit", help="the kit revision to pin (with --refresh)")
    args = parser.parse_args(argv)
    if args.refresh and (args.check or not args.kit or not args.commit):
        parser.error("--refresh needs --kit and --commit, and no --check")
    try:
        if args.refresh:
            return refresh(args.root.resolve(), args.kit.resolve(), args.commit)
        return check(args.root.resolve())
    except EngineSkillError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

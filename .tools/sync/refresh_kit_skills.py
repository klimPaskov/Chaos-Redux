#!/usr/bin/env python3
"""Replace the pinned kit snapshot in `.tools/kit_skills/` with the skills of one Agentic HOI4 Modding Kit commit.

The snapshot holds the kit skills listed under `generated` in `.tools/kit_skills/mapping.json`, one folder per
kit skill, and `manifest.json` records the kit commit and the SHA-256 of every file. The files are read from the
commit with git, never from the kit's working tree, so uncommitted kit edits cannot enter the snapshot.
`sync_engine_skills.py` refuses a snapshot that differs from the manifest, so this is the only way to change it.

    python .tools/sync/refresh_kit_skills.py --kit <kit repository> --commit <revision>
    python .tools/sync/sync_engine_skills.py            # then regenerate the skills

Standard library only; runs on Python 3.9 or newer.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, Optional, Sequence

from sync_engine_skills import SNAPSHOT, EngineSkillError, file_digest, is_text, load_mapping, to_lf


def git(kit: Path, *arguments: str) -> bytes:
    try:
        return subprocess.run(["git", "-C", str(kit), *arguments], check=True, capture_output=True).stdout
    except (OSError, subprocess.CalledProcessError) as error:
        detail = error.stderr.decode("utf-8", "replace").strip() if isinstance(error, subprocess.CalledProcessError) else str(error)
        raise EngineSkillError(f"git {' '.join(arguments)} failed in {kit}: {detail}") from error


def kit_skill(kit: Path, commit: str, kit_name: str) -> Dict[str, bytes]:
    """The files of one kit skill at the commit, by path inside the skill folder."""
    prefix = f".claude/skills/{kit_name}/"
    listing = git(kit, "ls-tree", "-r", "--name-only", "-z", commit, "--", prefix).decode("utf-8")
    paths = [path for path in listing.split("\0") if path]
    if f"{prefix}SKILL.md" not in paths:
        raise EngineSkillError(f"{kit_name} has no SKILL.md at {commit[:7]} in the kit")
    files: Dict[str, bytes] = {}
    for path in paths:
        rel = path[len(prefix):]
        data = git(kit, "cat-file", "blob", f"{commit}:{path}")
        files[rel] = to_lf(data) if is_text(rel) else data
    return files


def refresh(root: Path, kit: Path, revision: str) -> int:
    mapping = load_mapping(root)
    commit = git(kit, "rev-parse", "--verify", f"{revision}^{{commit}}").decode("ascii").strip()
    snapshot = root / SNAPSHOT
    skills = {kit_name: kit_skill(kit, commit, kit_name) for kit_name in mapping.generated}
    for kit_name in mapping.generated:
        shutil.rmtree(snapshot / kit_name, ignore_errors=True)
    recorded: Dict[str, str] = {}
    for kit_name, files in skills.items():
        for rel, data in files.items():
            (snapshot / kit_name / rel).parent.mkdir(parents=True, exist_ok=True)
            (snapshot / kit_name / rel).write_bytes(data)
            recorded[f"{kit_name}/{rel}"] = file_digest(rel, data)
    manifest = {
        "_about": "Written by .tools/sync/refresh_kit_skills.py. SHA-256 of every snapshot file (text with LF line endings).",
        "kit": "Agentic HOI4 Modding Kit",
        "kit_commit": commit,
        "files": dict(sorted(recorded.items())),
    }
    (snapshot / "manifest.json").write_bytes((json.dumps(manifest, indent=2) + "\n").encode("utf-8"))
    print(f"Snapshot of {len(skills)} kit skills ({len(recorded)} files) at {commit[:7]}")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--kit", type=Path, required=True, help="the Agentic HOI4 Modding Kit repository")
    parser.add_argument("--commit", required=True, help="the kit revision to pin (a commit, tag or branch name)")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2], help="repository root (default: this repository)")
    args = parser.parse_args(argv)
    try:
        return refresh(args.root.resolve(), args.kit.resolve(), args.commit)
    except EngineSkillError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

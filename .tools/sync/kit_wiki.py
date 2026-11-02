#!/usr/bin/env python3
"""Keep the wiki snapshot identical to one Agentic HOI4 Modding Kit commit.

`hoi4_wiki/` is the kit's, copied whole. `.tools/kit_wiki.json` records the kit commit and the SHA-256 of
every file in it (text with LF line endings). The check reports a changed, missing or extra
file as drift, so a hand edit here is caught; wiki fixes belong in the kit. A refresh copies the folder from
the kit commit and records them again, so taking a newer snapshot never fails the check.

`--freshness` asks the other question: has the kit's wiki changed since the pinned commit? It compares with
the newest `main` of a local kit clone (`--kit`, or the `HOI4_KIT_REPO` environment variable), and otherwise
asks GitHub. A snapshot that is behind is reported with the refresh command and still exits 0, because being
behind is a reminder and never a failure. When neither source can be read the answer is `UNKNOWN`, also exit 0.

    python .tools/sync/kit_wiki.py                                            # check (exit 1 on drift)
    python .tools/sync/kit_wiki.py --freshness [--kit <kit repository>]       # BEHIND / CURRENT / UNKNOWN, exit 0
    python .tools/sync/kit_wiki.py --refresh --kit <kit repository> --commit <revision>

Standard library only; runs on Python 3.9 or newer.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import Callable, Dict, List, Optional, Sequence, Tuple

from sync_engine_skills import EngineSkillError, file_digest, is_text, to_lf

FOLDERS = ("hoi4_wiki",)
MANIFEST = ".tools/kit_wiki.json"
SKIPPED = ("__pycache__",)
KIT_REPOSITORY = "klimPaskov/Agentic-HOI4-Modding"
KIT_ENVIRONMENT = "HOI4_KIT_REPO"
REFRESH_COMMAND = "python .tools/sync/kit_wiki.py --refresh --kit <kit repository> --commit <revision>"
REMOTE_TIMEOUT_SECONDS = 8
COMPARE_FILE_LIMIT = 300  # GitHub's compare endpoint lists at most this many files


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


def pinned_commit(root: Path) -> str:
    path = root / MANIFEST
    try:
        commit = json.loads(path.read_text(encoding="utf-8"))["kit_commit"]
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise EngineSkillError(f"cannot read {MANIFEST}: {error}") from error
    if not isinstance(commit, str) or not commit:
        raise EngineSkillError(f"{MANIFEST} has no `kit_commit`")
    return commit


def changed_in_clone(kit: Path, pinned: str) -> Optional[List[str]]:
    """Wiki files that differ between the pinned commit and the newest main of a local kit clone.

    `None` means the clone cannot answer (not a repository, or the pinned commit is not in it). The clone is
    read as it is: fetch it first to compare with the kit's latest.
    """
    for ref in ("origin/main", "main", "HEAD"):
        try:
            git(kit, "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")
            listing = git(kit, "diff", "--name-only", "-z", pinned, ref, "--", "hoi4_wiki/")
        except EngineSkillError:
            continue
        return [path for path in listing.decode("utf-8").split("\0") if path]
    return None


def changed_on_github(pinned: str) -> Optional[List[str]]:
    """Wiki files changed between the pinned commit and the kit's `main` on GitHub, or `None` when it cannot be read."""
    request = urllib.request.Request(
        f"https://api.github.com/repos/{KIT_REPOSITORY}/compare/{pinned}...main",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "kit-wiki-freshness-check"})
    try:
        with urllib.request.urlopen(request, timeout=REMOTE_TIMEOUT_SECONDS) as response:
            names = [str(row["filename"]) for row in json.loads(response.read().decode("utf-8"))["files"]]
    except (OSError, ValueError, KeyError, TypeError):
        return None
    changed = [name for name in names if name.startswith("hoi4_wiki/")]
    if not changed and len(names) >= COMPARE_FILE_LIMIT:
        return None  # the list was cut off, so an empty answer proves nothing
    return changed


def freshness(root: Path, kit: Optional[Path] = None,
              remote: Optional[Callable[[str], Optional[List[str]]]] = None) -> Tuple[str, str]:
    """Return (`current`, `behind` or `unknown`, message) for the snapshot against the kit's newest wiki.

    `remote` answers when no kit clone does; it defaults to `changed_on_github`.
    """
    pinned = pinned_commit(root)
    remote = remote or changed_on_github
    if kit is None and os.environ.get(KIT_ENVIRONMENT):
        kit = Path(os.environ[KIT_ENVIRONMENT])
    changed = changed_in_clone(kit, pinned) if kit is not None else None
    if changed is None:
        changed = remote(pinned)
    if changed is None:
        return "unknown", (f"could not compare with the kit's newest wiki: no readable kit clone (--kit or "
                           f"{KIT_ENVIRONMENT}) and GitHub was not reachable")
    if not changed:
        return "current", f"hoi4_wiki/ matches the kit's newest wiki (pinned kit {pinned[:7]})"
    names = ", ".join(Path(name).name for name in changed[:3]) + (", ..." if len(changed) > 3 else "")
    return "behind", (f"hoi4_wiki/ is behind the kit: {len(changed)} wiki file(s) changed since pinned kit "
                      f"{pinned[:7]} ({names}). Refresh with: {REFRESH_COMMAND}")


def kit_files(kit: Path, commit: str) -> Dict[str, bytes]:
    files: Dict[str, bytes] = {}
    for folder in FOLDERS:
        listing = git(kit, "ls-tree", "-r", "--name-only", "-z", commit, "--", f"{folder}/").decode("utf-8")
        for rel in (path for path in listing.split("\0") if path):
            if any(part in SKIPPED for part in rel.split("/")):
                continue
            data = git(kit, "cat-file", "blob", f"{commit}:{rel}")
            files[rel] = to_lf(data) if is_text(rel) else data
    if not any(rel.startswith("hoi4_wiki/") for rel in files):
        raise EngineSkillError(f"the kit has no hoi4_wiki/ at {commit[:7]}")
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
        "_about": "Written by .tools/sync/kit_wiki.py. SHA-256 of every file in hoi4_wiki/ (text with LF line endings).",
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
    parser.add_argument("--refresh", action="store_true", help="copy hoi4_wiki/ from the kit commit and record it")
    parser.add_argument("--freshness", action="store_true", help="report BEHIND, CURRENT or UNKNOWN against the kit's newest wiki (always exit 0)")
    parser.add_argument("--kit", type=Path, help="the Agentic HOI4 Modding Kit repository (with --refresh or --freshness)")
    parser.add_argument("--commit", help="the kit revision to pin (with --refresh)")
    args = parser.parse_args(argv)
    if args.refresh and (args.check or args.freshness or not args.kit or not args.commit):
        parser.error("--refresh needs --kit and --commit, and no --check or --freshness")
    try:
        if args.freshness:
            state, message = freshness(args.root.resolve(), args.kit.resolve() if args.kit else None)
            print(f"{state.upper()} {message}")
            return 0
        if args.refresh:
            return refresh(args.root.resolve(), args.kit.resolve(), args.commit)
        return check(args.root.resolve())
    except EngineSkillError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Install only the Event 072 specification and plan documents into a repository."""
from __future__ import annotations
import argparse
from pathlib import Path
import sys

SPEC_NAME = "072_ireland_reclaims_north_specs"
PLAN_NAME = "072_ireland_reclaims_north_plans"
EXCLUDE = {"handoff", "install_spec_package.py", "validate_package.py", "PACKAGE_MANIFEST.json"}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--overwrite", action="store_true", help="Explicitly replace conflicting documentation files")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    if not (source / "handoff" / PLAN_NAME).is_dir():
        parser.error("Run the installer from the original extracted package")
    repo = args.repository.expanduser().resolve()
    if not repo.is_dir():
        parser.error("Repository path must be an existing directory")
    jobs: list[tuple[Path, Path, bytes]] = []
    for file in sorted(source.rglob("*")):
        if not file.is_file():
            continue
        rel = file.relative_to(source)
        if rel.parts[0] == "handoff":
            if len(rel.parts) < 3 or rel.parts[1] != PLAN_NAME:
                raise ValueError(f"Unexpected handoff path: {rel}")
            destination = repo / "docs" / "plans" / PLAN_NAME / Path(*rel.parts[2:])
        elif rel.parts[0] in EXCLUDE or "__pycache__" in rel.parts:
            continue
        else:
            destination = repo / "docs" / "specs" / SPEC_NAME / rel
        # Resolve symlinks and refuse an escape from the repository.
        if not destination.resolve().is_relative_to(repo):
            raise ValueError(f"Unsafe destination: {destination}")
        content = file.read_bytes()
        if file.suffix == ".md":
            text = content.decode("utf-8")
            if rel.parts[0] != "handoff":
                text = text.replace(f"(handoff/{PLAN_NAME}/", f"(../../plans/{PLAN_NAME}/")
                if file.name == "INDEX.md":
                    text = "\n".join(line for line in text.splitlines() if "](install_spec_package.py)" not in line and "](validate_package.py)" not in line and line != "## Package tools") + "\n"
            content = text.encode("utf-8")
        if destination.exists() and destination.read_bytes() != content and not args.overwrite:
            raise FileExistsError(f"Conflicting file: {destination}. Review it or use --overwrite explicitly.")
        jobs.append((file, destination, content))
    # No writes occur until every conflict and path has passed preflight.
    for _, destination, content in jobs:
        print(destination.relative_to(repo))
        if not args.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            temporary = destination.with_name(destination.name + ".072-copying")
            temporary.write_bytes(content)
            temporary.replace(destination)
    verb = "Would install" if args.dry_run else "Installed"
    print(f"{verb} {len(jobs)} documentation files. No game files or network services were touched.")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        print(f"Installation stopped: {exc}", file=sys.stderr)
        raise SystemExit(1)

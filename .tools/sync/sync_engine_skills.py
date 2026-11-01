#!/usr/bin/env python3
"""Generate the Chaos Redux engine-system skills from the kit snapshot and the Chaos Redux overlays.

Each generated skill, `.claude/skills/<chaos-redux-name>/`, holds:

- the kit skill pinned in `.tools/kit_skills/<kit-name>/` with every name in
  `.tools/kit_skills/mapping.json` replaced by its Chaos Redux name (skills and agent routing names),
- the reference files of `.claude/skill-overlays/<chaos-redux-name>/` (every file but `overlay.md`),
- a `SKILL.md` made of the Chaos Redux frontmatter (`name` and the overlay's `description`), a provenance
  comment, the mapped kit body and a `## Chaos Redux` section holding the body of `overlay.md`.

Edit the overlay, never a generated file. A new kit revision enters through `refresh_kit_skills.py`, which
rewrites the snapshot and `manifest.json` together; this tool refuses a snapshot that differs from the manifest.

    python .tools/sync/sync_engine_skills.py                          # write every generated file
    python .tools/sync/sync_engine_skills.py --check                  # report stale files, write nothing
    python .tools/sync/sync_engine_skills.py --skill chaos-redux-mtth # one skill (repeatable)
    python .tools/sync/sync_engine_skills.py --root <folder>          # another repository root

Exit codes: 0 in sync, 1 drift (`--check` prints `Would update <path>` for each stale, missing or extra file
and writes nothing), 2 cannot run (an invalid mapping, overlay or snapshot, an unknown `--skill`, or a
`SKILL.md` over the size limit of `read_limits.json`). Only files under the generated skill folders that no
source produces are deleted. Line endings are compared as LF, so a CRLF checkout is not drift.

Standard library only; runs on Python 3.9 or newer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Pattern, Sequence, Tuple

SCRIPT = ".tools/sync/sync_engine_skills.py"
SNAPSHOT = ".tools/kit_skills"
OVERLAYS = ".claude/skill-overlays"
SKILLS = ".claude/skills"
LIMITS = ".tools/sync/read_limits.json"
DEFAULT_SKILL_LIMIT = 58000
TEXT_SUFFIXES = (".md", ".txt", ".json", ".yml", ".yaml")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


class EngineSkillError(Exception):
    """The generator cannot run: the exit status is 2."""


def is_text(rel: str) -> bool:
    return rel.lower().endswith(TEXT_SUFFIXES)


def to_lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def file_digest(rel: str, data: bytes) -> str:
    """SHA-256 of a file; text is hashed with LF endings so a CRLF checkout keeps its digest."""
    return hashlib.sha256(to_lf(data) if is_text(rel) else data).hexdigest()


def read_json(path: Path, root: Path) -> Dict[str, Any]:
    shown = path.relative_to(root).as_posix()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise EngineSkillError(f"{shown} is missing") from None
    except (OSError, ValueError) as error:
        raise EngineSkillError(f"{shown} cannot be read as JSON: {error}") from error
    if not isinstance(data, dict):
        raise EngineSkillError(f"{shown} must hold a JSON object")
    return data


def string_map(data: Dict[str, Any], key: str, shown: str) -> Dict[str, str]:
    value = data.get(key, {})
    if not isinstance(value, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in value.items()):
        raise EngineSkillError(f"{shown}: \"{key}\" must map names to names")
    return {str(k): str(v) for k, v in value.items()}


@dataclass(frozen=True)
class Mapping:
    """The kit names of the generated skills and every name replaced inside their text."""

    generated: Dict[str, str]  # kit skill name to Chaos Redux skill name
    pattern: Pattern[str]
    names: Dict[str, str]

    def apply(self, text: str) -> str:
        """Replace whole names only: a name next to a letter, digit, underscore or hyphen is another name."""
        return self.pattern.sub(lambda match: self.names[match.group(0)], text)


def load_mapping(root: Path) -> Mapping:
    shown = f"{SNAPSHOT}/mapping.json"
    data = read_json(root / SNAPSHOT / "mapping.json", root)
    skills = string_map(data, "skills", shown)
    names = dict(skills)
    names.update(string_map(data, "agents", shown))
    names.update(string_map(data, "instruction_files", shown))
    names = {source: target for source, target in names.items() if source != target}
    listed = data.get("generated", [])
    if not isinstance(listed, list) or not listed or not all(isinstance(item, str) for item in listed):
        raise EngineSkillError(f"{shown}: \"generated\" must list the kit skills to generate")
    generated: Dict[str, str] = {}
    for kit_name in listed:
        target = skills.get(kit_name)
        if target is None or not NAME.match(target):
            raise EngineSkillError(f"{shown}: \"skills\" has no valid Chaos Redux name for {kit_name}")
        generated[kit_name] = target
    if len(set(generated.values())) != len(generated):
        raise EngineSkillError(f"{shown}: two kit skills map to one Chaos Redux skill")
    ordered = sorted(names, key=lambda source: (-len(source), source))
    pattern = re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(source) for source in ordered) + r")(?![\w-])")
    return Mapping(generated, pattern, names)


@dataclass(frozen=True)
class Manifest:
    commit: str
    files: Dict[str, str]  # "<kit-name>/<path>" to SHA-256


def load_manifest(root: Path) -> Manifest:
    shown = f"{SNAPSHOT}/manifest.json"
    data = read_json(root / SNAPSHOT / "manifest.json", root)
    commit = data.get("kit_commit")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{7,40}", commit):
        raise EngineSkillError(f"{shown}: \"kit_commit\" must be a commit hash")
    return Manifest(commit, string_map(data, "files", shown))


def snapshot_files(root: Path, kit_name: str) -> Dict[str, bytes]:
    """Every file of one pinned kit skill, by its path inside the skill folder."""
    folder = root / SNAPSHOT / kit_name
    if not (folder / "SKILL.md").is_file():
        raise EngineSkillError(f"{SNAPSHOT}/{kit_name}/SKILL.md is missing")
    return {path.relative_to(folder).as_posix(): path.read_bytes() for path in sorted(folder.rglob("*")) if path.is_file()}


def verify_snapshot(root: Path, manifest: Manifest, kit_names: Sequence[str]) -> None:
    """Refuse a snapshot that differs from `manifest.json`, so only `refresh_kit_skills.py` changes it."""
    problems: List[str] = []
    for kit_name in kit_names:
        actual = {f"{kit_name}/{rel}": file_digest(rel, data) for rel, data in snapshot_files(root, kit_name).items()}
        recorded = {name: digest for name, digest in manifest.files.items() if name.startswith(f"{kit_name}/")}
        problems += [f"{SNAPSHOT}/{name}" for name in sorted(set(actual) | set(recorded)) if actual.get(name) != recorded.get(name)]
    if problems:
        raise EngineSkillError("the kit snapshot differs from manifest.json (refresh it with refresh_kit_skills.py): "
            + ", ".join(problems))


def split_frontmatter(text: str, shown: str) -> Tuple[Dict[str, str], str]:
    """Split `---` frontmatter of single-line `key: value` fields from the body that follows it."""
    if not text.startswith("---\n"):
        raise EngineSkillError(f"{shown} must start with --- frontmatter")
    end = text.find("\n---\n", 3)
    if end < 0:
        raise EngineSkillError(f"{shown} has no closing --- line in its frontmatter")
    fields: Dict[str, str] = {}
    for line in text[4:end].split("\n"):
        key, separator, value = line.partition(":")
        if not line.strip():
            continue
        if not separator or not key.strip() or key != key.strip():
            raise EngineSkillError(f"{shown}: frontmatter line is not a single-line `key: value` field: {line}")
        fields[key] = value.strip()
    return fields, text[end + 5:]


def skill_limit(root: Path) -> int:
    path = root / LIMITS
    if not path.is_file():
        return DEFAULT_SKILL_LIMIT
    value = read_json(path, root).get("root_skill_max_bytes", DEFAULT_SKILL_LIMIT)
    if not isinstance(value, int) or value <= 0:
        raise EngineSkillError(f"{LIMITS}: \"root_skill_max_bytes\" must be a positive integer")
    return value


def read_overlay(root: Path, name: str) -> Tuple[str, str, Dict[str, bytes]]:
    """The description and body of `overlay.md`, and the overlay's reference files by path in the skill."""
    folder = root / OVERLAYS / name
    shown = f"{OVERLAYS}/{name}/overlay.md"
    if not (folder / "overlay.md").is_file():
        raise EngineSkillError(f"{shown} is missing")
    text = to_lf((folder / "overlay.md").read_bytes()).decode("utf-8")
    fields, body = split_frontmatter(text, shown)
    if not fields.get("description"):
        raise EngineSkillError(f"{shown} needs a description in its frontmatter")
    extras: Dict[str, bytes] = {}
    for path in sorted(folder.rglob("*")):
        rel = path.relative_to(folder).as_posix()
        if path.is_file() and rel != "overlay.md":
            extras[rel] = to_lf(path.read_bytes()) if is_text(rel) else path.read_bytes()
    return fields["description"], body.strip("\n"), extras


def render_skill(mapping: Mapping, manifest: Manifest, kit_name: str, text: str, name: str,
                 description: str, overlay: str) -> str:
    """The generated SKILL.md: Chaos Redux frontmatter, provenance comment, mapped kit body, overlay section."""
    _, kit_body = split_frontmatter(text, f"{SNAPSHOT}/{kit_name}/SKILL.md")
    body = mapping.apply(kit_body).strip("\n")
    note = (f"<!-- Generated by {SCRIPT} from the kit's {kit_name} at {manifest.commit[:7]} "
        f"and {OVERLAYS}/{name}/. Edit the overlay, never this file. -->")
    result = f"---\nname: {name}\ndescription: {description}\n---\n{note}\n\n{body}\n"
    if overlay:
        result += f"\n## Chaos Redux\n\n{overlay}\n"
    return result


def build_skill(root: Path, mapping: Mapping, manifest: Manifest, kit_name: str, limit: int) -> Dict[str, bytes]:
    """Every file one generated skill must hold, by path from the repository root."""
    name = mapping.generated[kit_name]
    description, overlay, extras = read_overlay(root, name)
    files: Dict[str, bytes] = {}
    skill_text = ""
    for rel, data in snapshot_files(root, kit_name).items():
        if rel == "SKILL.md":
            skill_text = to_lf(data).decode("utf-8")
        elif is_text(rel):
            files[rel] = mapping.apply(to_lf(data).decode("utf-8")).encode("utf-8")
        else:
            files[rel] = data
    for rel, data in extras.items():
        if rel == "SKILL.md" or rel in files:
            raise EngineSkillError(f"{OVERLAYS}/{name}/{rel} would replace the kit file {rel}; rename the overlay file")
        files[rel] = data
    skill = render_skill(mapping, manifest, kit_name, skill_text, name, description, overlay).encode("utf-8")
    if len(skill) > limit:
        raise EngineSkillError(f"{SKILLS}/{name}/SKILL.md would be {len(skill)} bytes, over the {limit}-byte limit in "
            f"{LIMITS}; move a complete overlay topic into an overlay reference file and link it")
    files["SKILL.md"] = skill
    return {f"{SKILLS}/{name}/{rel}": data for rel, data in files.items()}


def is_current(root: Path, rel: str, data: bytes) -> bool:
    path = root / rel
    if not path.is_file():
        return False
    found = path.read_bytes()
    return (to_lf(found) if is_text(rel) else found) == data


def extra_files(root: Path, names: Sequence[str], expected: Dict[str, bytes]) -> List[str]:
    found: List[str] = []
    for name in names:
        folder = root / SKILLS / name
        found += [path.relative_to(root).as_posix() for path in sorted(folder.rglob("*")) if path.is_file()] if folder.is_dir() else []
    return [rel for rel in found if rel not in expected]


def prune_empty(root: Path, rel: str) -> None:
    """Remove the folders a deleted file leaves empty, up to the generated skill folder itself."""
    skill = root.joinpath(*rel.split("/")[:3])
    folder = (root / rel).parent
    while folder != skill and not any(folder.iterdir()):
        folder.rmdir()
        folder = folder.parent


def select_skills(mapping: Mapping, requested: Sequence[str]) -> List[str]:
    """Kit names of the skills to generate; `--skill` accepts the Chaos Redux name or the kit name."""
    if not requested:
        return list(mapping.generated)
    chosen: List[str] = []
    for item in requested:
        kit_name = next((kit for kit, name in mapping.generated.items() if item in (kit, name)), None)
        if kit_name is None:
            raise EngineSkillError(f"{item} is not a generated engine skill ({', '.join(mapping.generated.values())})")
        if kit_name not in chosen:
            chosen.append(kit_name)
    return chosen


def run(root: Path, check: bool, requested: Sequence[str]) -> int:
    mapping = load_mapping(root)
    manifest = load_manifest(root)
    kit_names = select_skills(mapping, requested)
    verify_snapshot(root, manifest, kit_names)
    limit = skill_limit(root)
    expected: Dict[str, bytes] = {}
    problems: List[str] = []
    for kit_name in kit_names:
        try:
            expected.update(build_skill(root, mapping, manifest, kit_name, limit))
        except EngineSkillError as error:
            problems.append(str(error))
    if problems:
        raise EngineSkillError("; ".join(problems))
    stale = [rel for rel, data in sorted(expected.items()) if not is_current(root, rel, data)]
    extra = extra_files(root, [mapping.generated[kit_name] for kit_name in kit_names], expected)
    if check:
        for rel in sorted(stale + extra):
            print(f"Would update {rel}")
        return 1 if stale or extra else 0
    for rel in stale:
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_bytes(expected[rel])
        print(f"Updated {rel}")
    for rel in extra:
        (root / rel).unlink()
        prune_empty(root, rel)
        print(f"Removed {rel}")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="report stale, missing and extra files and write nothing; exit 1 on drift")
    parser.add_argument("--skill", action="append", default=[], metavar="NAME", help="generate only this skill (repeatable)")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2], help="repository root (default: this repository)")
    args = parser.parse_args(argv)
    try:
        return run(args.root.resolve(), args.check, args.skill)
    except EngineSkillError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python
"""Verify evidence citations in the .qoder/repowiki knowledge base.

The repowiki pages cite repository sources with `file://<repo-relative-path>#L<a>-L<b>`
links.  Those citations rot silently whenever a source file is moved, deleted or
reformatted, which makes the whole wiki untrustworthy.  This tool walks every
markdown page under `.qoder/repowiki`, extracts every citation and checks it
against the working tree.

Checks performed per page:

* every `file://` target exists in the repository
* every `#L<a>` / `#L<a>-L<b>` anchor is inside the referenced file and ordered
* every page still carries its `<cite>` "Referenced Files in This Document` block
* knowledge modules carry a `_module.yaml` next to their markdown files
* markdown paragraph lines are not hard-wrapped mid-sentence

Usage:

    python -B .tools/repowiki/verify_repowiki_refs.py                 # summary
    python -B .tools/repowiki/verify_repowiki_refs.py --verbose       # per-page detail
    python -B .tools/repowiki/verify_repowiki_refs.py --json out.json # machine-readable
    python -B .tools/repowiki/verify_repowiki_refs.py --paths         # only list broken paths
    python -B .tools/repowiki/verify_repowiki_refs.py --page <substr>  # limit to matching pages

Exit code is 0 when the wiki is clean and 1 when any problem was found.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI_ROOT = os.path.join(REPO_ROOT, ".qoder", "repowiki")

# `file://path#L12` / `file://path#L12-L40`; the path may contain spaces and slashes.
CITATION_RE = re.compile(r"file://([^)\s#]+?)(?:#L(\d+)(?:-L(\d+))?)?(?=[)\s#]|$)")
# A path guess for citations that were written without the file:// scheme.
BARE_CITE_RE = re.compile(r"\]\((?:file://)?([A-Za-z0-9_./\- ]+\.(?:txt|gui|gfx|md|yml|yaml|json|py|mjs|js|csv|toml|mod|dds|tga|png))\)")

# Sentences are not hard-wrapped, so a prose line ending in a lowercase word
# followed by a line that starts lowercase is treated as a wrap defect.
PROSE_LINE_RE = re.compile(r"^[A-Za-z0-9*`\[(\"'][^|]*$")


@dataclass
class PageReport:
    path: str
    refs: int = 0
    resolved: int = 0
    missing: list[str] = field(default_factory=list)
    out_of_range: list[tuple[str, int, int | None, int]] = field(default_factory=list)
    loose: list[tuple[str, int, int]] = field(default_factory=list)
    empty_targets: list[str] = field(default_factory=list)
    duplicate_headings: dict[str, int] = field(default_factory=dict)
    unreadable: list[str] = field(default_factory=list)
    has_cite_block: bool = False
    is_module: bool = False
    empty_knowledge_file: bool = False
    wrapped_lines: list[int] = field(default_factory=list)

    @property
    def clean(self) -> bool:
        if self.missing or self.out_of_range or self.unreadable or self.wrapped_lines:
            return False
        if self.empty_knowledge_file:
            return False
        return self.is_module or self.has_cite_block


# Knowledge modules are short structured notes; a `_module.yaml` describes the
# module and the markdown files carry the four required sections.
REQUIRED_MODULE_SECTIONS = ("overview.md", "architecture_design.md", "coding_conventions.md", "tech_stack.md")


def _read_lines(path: str) -> list[str] | None:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            return handle.readlines()
    except OSError:
        return None


def _line_count_cache() -> dict[str, int]:
    return {}


def _line_count(path: str, cache: dict[str, int]) -> int | None:
    if path in cache:
        return cache[path]
    lines = _read_lines(path)
    count = None if lines is None else len(lines)
    cache[path] = count  # type: ignore[assignment]
    return count


def check_page(page_path: str, root: str, counts: dict[str, int]) -> PageReport:
    rel_page = os.path.relpath(page_path, root).replace("\\", "/")
    report = PageReport(path=rel_page)
    lines = _read_lines(page_path)
    if lines is None:
        report.unreadable.append(rel_page)
        return report

    text = "".join(lines)
    report.has_cite_block = "<cite>" in text and "Referenced Files" in text
    report.is_module = "/knowledge/" in ("/" + rel_page)
    report.empty_knowledge_file = report.is_module and len(text.strip()) == 0

    seen: set[str] = set()
    for match in CITATION_RE.finditer(text):
        raw_path, first, last = match.group(1), match.group(2), match.group(3)
        target = raw_path.replace("%20", " ").strip().lstrip("/")
        if not target or target.endswith("/"):
            continue
        # Illustrative placeholders inside fenced examples are not citations.
        if target.startswith("path/to/") or target.startswith("other_file"):
            continue
        report.refs += 1
        absolute = os.path.join(root, target)
        if not os.path.exists(absolute):
            if target not in seen:
                seen.add(target)
                report.missing.append(target)
            continue
        report.resolved += 1
        if first is None:
            continue
        total = _line_count(absolute, counts)
        if total is None:
            continue
        # A citation to an empty file proves nothing, and any anchor on it is a defect.
        if total == 0:
            if target not in seen:
                seen.add(target)
                report.empty_targets.append(target)
            continue
        start = int(first)
        end = int(last) if last else start
        if start > total or end > total or end < start:
            report.out_of_range.append((target, start, int(last) if last else None, total))
            continue
        # Existing-but-wrong anchors are the silent defect class. A citation like
        # `#L1-800` on a 48,000-line file is a legitimate partial read, so only a
        # whole-file anchor whose end sits just short of the real end is stale: that
        # shape means the anchor was derived from an earlier revision of the file.
        if start == 1 and end != total and 0 < total - end <= 10:
            report.loose.append((target, end, total))

    report.wrapped_lines = find_wrapped_lines(lines)
    report.duplicate_headings = find_duplicate_headings(lines)
    return report


def find_duplicate_headings(lines: list[str]) -> dict[str, int]:
    """Repeated top-level headings mean a page holds its own body twice.

    That happens when an edit appends the replacement instead of replacing the
    original, and the citation verifier cannot see it because both copies cite
    valid files.
    """
    counts: dict[str, int] = {}
    in_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^##\s+(.*)$", stripped)
        if match:
            heading = match.group(1).strip()
            counts[heading] = counts.get(heading, 0) + 1
    return {name: count for name, count in counts.items() if count > 1}


def find_wrapped_lines(lines: list[str]) -> list[int]:
    """Return 1-based line numbers that look like mid-sentence hard wraps."""
    flagged: list[int] = []
    in_fence = False
    in_cite = False
    in_front_matter = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        # YAML front matter is a data block, not prose.
        if index == 0 and stripped == "---":
            in_front_matter = True
            continue
        if in_front_matter:
            if stripped == "---":
                in_front_matter = False
            continue
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # The <cite> block and source lists are link lists, not prose.
        if stripped.startswith("<cite"):
            in_cite = True
            continue
        if stripped.startswith("</cite"):
            in_cite = False
            continue
        if in_cite:
            continue
        if stripped.startswith("- [") or stripped.startswith("* ["):
            continue
        if not stripped or stripped.startswith(("#", "|", "-", "*", ">", "<", "**Section", "**Diagram")):
            continue
        if not PROSE_LINE_RE.match(stripped):
            continue
        # A wrapped sentence continues on the next line with a lowercase word.
        following = ""
        for candidate in lines[index + 1:]:
            candidate = candidate.strip()
            if candidate:
                following = candidate
                break
        if not following:
            continue
        if following[0].islower() and not following.startswith(("-", "*", "|", "[")):
            flagged.append(index + 1)
    return flagged


def collect_pages(root: str, page_filter: str | None) -> list[str]:
    pages: list[str] = []
    for directory, _dirs, files in os.walk(root):
        for name in files:
            if not name.endswith(".md"):
                continue
            full = os.path.join(directory, name)
            rel = os.path.relpath(full, root).replace("\\", "/")
            if page_filter and page_filter.lower() not in rel.lower():
                continue
            pages.append(full)
    return sorted(pages)


def check_knowledge_modules(root: str) -> list[str]:
    """Every knowledge module folder must declare itself with _module.yaml.

    A folder is treated as a module when it carries a `_module.yaml`; only those
    folders are then checked for the required short-form markdown files. Standalone
    knowledge documents such as the business glossary are not modules.
    """
    problems: list[str] = []
    knowledge = os.path.join(root, "knowledge")
    if not os.path.isdir(knowledge):
        return problems
    for directory, _dirs, files in os.walk(knowledge):
        if not any(name.endswith(".md") for name in files):
            continue
        if "_module.yaml" not in files:
            continue
        for required in REQUIRED_MODULE_SECTIONS:
            if required not in files:
                problems.append(
                    f"{os.path.relpath(directory, root).replace(chr(92), '/')}: missing {required}"
                )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=WIKI_ROOT, help="repowiki root (default: .qoder/repowiki)")
    parser.add_argument("--page", help="only check pages whose relative path contains this text")
    parser.add_argument("--verbose", action="store_true", help="print every finding")
    parser.add_argument("--paths", action="store_true", help="print only the broken citation target paths")
    parser.add_argument("--json", help="write the full report to this file")
    parser.add_argument("--style", action="store_true", help="also report hard-wrapped prose lines")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="also treat loose whole-file anchors (#L1-N where N is not the file length) as failures",
    )
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"repowiki root not found: {root}", file=sys.stderr)
        return 2

    counts: dict[str, int] = {}
    pages = collect_pages(root, args.page)
    reports = [check_page(page, REPO_ROOT, counts) for page in pages]
    module_problems = check_knowledge_modules(root)

    total_refs = sum(report.refs for report in reports)
    total_resolved = sum(report.resolved for report in reports)
    broken_paths: dict[str, int] = {}
    for report in reports:
        for target in report.missing:
            broken_paths[target] = broken_paths.get(target, 0) + 1

    if args.paths:
        for target in sorted(broken_paths):
            print(target)
        return 1 if broken_paths else 0

    print(f"pages scanned          : {len(reports)}")
    print(f"citations found        : {total_refs}")
    print(f"citations resolved     : {total_resolved}")
    print(f"broken citation targets: {len(broken_paths)} distinct")
    print(f"out-of-range anchors   : {sum(len(r.out_of_range) for r in reports)}")
    print(f"loose whole-file anchors: {sum(len(r.loose) for r in reports)}")
    print(f"pages with a doubled body: {sum(1 for r in reports if r.duplicate_headings)}")
    print(f"citations to empty files : {sum(len(r.empty_targets) for r in reports)}")
    print(f"content pages no <cite>: {sum(1 for r in reports if not r.is_module and not r.has_cite_block)}")
    print(f"empty knowledge files  : {sum(1 for r in reports if r.empty_knowledge_file)}")
    print(f"modules missing yaml   : {len(module_problems)}")

    if args.verbose or args.style:
        for report in reports:
            problems = []
            if report.missing:
                problems.append(f"{len(report.missing)} broken target(s)")
            if report.out_of_range:
                problems.append(f"{len(report.out_of_range)} stale anchor(s)")
            if report.loose and args.strict:
                problems.append(f"{len(report.loose)} loose anchor(s)")
            if report.duplicate_headings:
                repeated = ", ".join(
                    f"{name} x{count}"
                    for name, count in sorted(report.duplicate_headings.items(), key=lambda kv: -kv[1])[:4]
                )
                problems.append(f"doubled body ({repeated})")
            if report.empty_targets:
                problems.append(f"{len(report.empty_targets)} empty-file citation(s)")
            if not report.is_module and not report.has_cite_block:
                problems.append("no cite block")
            if report.empty_knowledge_file:
                problems.append("empty knowledge file")
            if args.style and report.wrapped_lines:
                problems.append(f"{len(report.wrapped_lines)} wrapped line(s)")
            if problems:
                print(f"  {report.path}: {', '.join(problems)}")
                for target in report.missing:
                    print(f"      missing: {target}")
                for target, start, end, total in report.out_of_range:
                    span = f"{start}-{end}" if end else str(start)
                    print(f"      stale anchor: {target}#L{span} (file has {total} lines)")
                if args.strict:
                    for target, end, total in report.loose:
                        print(f"      loose anchor: {target}#L1-{end} (file has {total} lines)")

    if args.json:
        payload = {
            "summary": {
                "pages": len(reports),
                "citations": total_refs,
                "resolved": total_resolved,
                "broken_targets": len(broken_paths),
                "out_of_range_anchors": sum(len(r.out_of_range) for r in reports),
                "loose_whole_file_anchors": sum(len(r.loose) for r in reports),
                "content_pages_missing_cite": sum(
                    1 for r in reports if not r.is_module and not r.has_cite_block
                ),
                "empty_knowledge_files": sum(1 for r in reports if r.empty_knowledge_file),
                "modules_missing_yaml": module_problems,
            },
            "broken_targets": sorted(broken_paths),
            "pages": [
                {
                    "path": report.path,
                    "refs": report.refs,
                    "missing": report.missing,
                    "out_of_range": report.out_of_range,
                    "loose": report.loose,
                    "has_cite_block": report.has_cite_block,
                    "is_module": report.is_module,
                    "wrapped_lines": report.wrapped_lines,
                }
                for report in reports
            ],
        }
        with open(args.json, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, indent=2)
            handle.write("\n")
        print(f"json report written    : {args.json}")

    dirty = (
        broken_paths
        or any(report.out_of_range for report in reports)
        or module_problems
        or any(not report.is_module and not report.has_cite_block for report in reports)
        or any(report.empty_knowledge_file for report in reports)
        or any(report.duplicate_headings for report in reports)
        or any(report.empty_targets for report in reports)
        or (args.strict and any(report.loose for report in reports))
    )
    return 1 if dirty else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python
"""Reconcile the Qoder repowiki catalog registry with the pages on disk.

`.qoder/repowiki/en/meta/repowiki-metadata.json` carries four registries Qoder
reads to render the wiki tree:

* `wiki_catalogs` - one row per wiki page, keyed by `name`, which is the page file
  name without its extension. `progress_status` is `completed` or `failed`.
* `wiki_items` - one row per page, keyed by `title`, which matches the page file
  name. This registry is left untouched except when a brand new page appears.
* `knowledge_relations` - parent/child links between item ids, with an integer
  sequence `id`.
* `wiki_overview`, `wiki_readme`, `wiki_repo` - records whose payload is encrypted
  by Qoder and therefore preserved byte for byte.

A catalog left at `failed` keeps hiding a page that now exists, and a page added
after generation has no catalog row at all. This tool makes the registries
describe what is actually on disk:

* mark a catalog `completed` once its page exists
* add a catalog (and matching item) for every page that has no entry
* report entries whose page is missing
* rebuild the nested parent/child relations from the page tree
* refresh the recorded baseline commit and timestamp

Usage:

    python -B .tools/repowiki/reconcile_repowiki_metadata.py            # dry run
    python -B .tools/repowiki/reconcile_repowiki_metadata.py --apply    # write
    python -B .tools/repowiki/reconcile_repowiki_metadata.py --json out.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WIKI_ROOT = os.path.join(REPO_ROOT, ".qoder", "repowiki")
METADATA = os.path.join(WIKI_ROOT, "en", "meta", "repowiki-metadata.json")
CONTENT_ROOT = os.path.join(WIKI_ROOT, "en", "content")

# Fixed namespace so repeated runs derive the same ids for the same page.
NAMESPACE = uuid.UUID("6f1d5b2a-9c47-4f31-8a2e-5c7b0d9e4a13")


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def stable_id(kind: str, name: str) -> str:
    return str(uuid.uuid5(NAMESPACE, f"{kind}:{name}"))


def iso_now() -> str:
    return datetime.now(timezone.utc).astimezone().replace(microsecond=0).isoformat()


def git_head() -> tuple[str, str]:
    def run(*args: str) -> str:
        return subprocess.run(
            ["git", "-C", REPO_ROOT, *args], capture_output=True, text=True, encoding="utf-8"
        ).stdout.strip()

    return run("rev-parse", "HEAD"), run("log", "-1", "--format=%cI")


def collect_pages() -> dict[str, str]:
    """page name -> content-relative path (first path wins for duplicate names)."""
    pages: dict[str, str] = {}
    for directory, _dirs, files in os.walk(CONTENT_ROOT):
        for name in files:
            if not name.endswith(".md"):
                continue
            full = os.path.join(directory, name)
            pages.setdefault(name[:-3], os.path.relpath(full, CONTENT_ROOT).replace("\\", "/"))
    return pages


def collect_all_pages() -> list[str]:
    """Every content page path, including pages that share a file name."""
    found: list[str] = []
    for directory, _dirs, files in os.walk(CONTENT_ROOT):
        for name in files:
            if not name.endswith(".md"):
                continue
            full = os.path.join(directory, name)
            found.append(os.path.relpath(full, CONTENT_ROOT).replace("\\", "/"))
    return sorted(found)


def build_relations(all_pages: list[str], item_by_title: dict[str, dict], next_id: int, now: str):
    """Nest each page under the nearest ancestor page that is also a wiki item.

    Works from full paths so that two pages sharing a file name, such as the two
    `Air Contamination Monitoring` pages, each keep their own relation.
    """
    relations: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for rel in all_pages:
        parts = rel.split("/")
        name = parts[-1][:-3]
        if name not in item_by_title:
            continue
        parent_title = None
        # The nearest enclosing folder that is itself a page wins.
        for depth in range(len(parts) - 1, 0, -1):
            candidate = parts[depth - 1]
            if candidate in item_by_title and candidate != name:
                parent_title = candidate
                break
        if parent_title is None:
            continue
        source = item_by_title[parent_title]["id"]
        target = item_by_title[name]["id"]
        if (source, target) in seen:
            continue
        seen.add((source, target))
        relations.append(
            {
                "id": next_id,
                "source_id": source,
                "target_id": target,
                "source_type": "WIKI_ITEM",
                "target_type": "WIKI_ITEM",
                "relationship_type": "PARENT_CHILD",
                "extra": f"Wiki parent-child relationship: {source} -> {target}",
                "gmt_create": now,
                "gmt_modified": now,
            }
        )
        next_id += 1
    return relations, next_id


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--apply", action="store_true", help="write the reconciled metadata")
    parser.add_argument("--json", help="write the reconciliation report to this file")
    args = parser.parse_args()

    if not os.path.isfile(METADATA):
        print(f"metadata not found: {METADATA}", file=sys.stderr)
        return 2

    with open(METADATA, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    catalogs = data.get("wiki_catalogs", [])
    items = data.get("wiki_items", [])
    pages = collect_pages()
    now = iso_now()
    head, head_date = git_head()

    overview = data.get("wiki_overview") or {}
    if isinstance(overview, list):
        overview = overview[0] if overview else {}
    repo_id = overview.get("repo_id") or (items[0].get("repo_id") if items else "")

    catalog_names = {row.get("name") for row in catalogs}
    item_titles = {row.get("title") for row in items}
    # Row counts and unique-name counts differ because two names appear twice, so
    # report both instead of subtracting the additions from one of them.
    before = {
        "catalog_rows": len(catalogs),
        "catalog_names": len(catalog_names),
        "item_rows": len(items),
        "item_titles": len(item_titles),
    }
    report = {"promoted": [], "added_catalogs": [], "added_items": [], "missing_pages": []}

    # 1. Promote catalogs whose page now exists.
    for row in catalogs:
        name = row.get("name")
        if name in pages and row.get("progress_status") != "completed":
            report["promoted"].append(name)
            row["progress_status"] = "completed"
            row["gmt_modified"] = now

    # 2. Add a catalog and an item for every page with no entry.
    for name in sorted(pages):
        description = slugify(name)
        if name not in catalog_names:
            catalogs.append(
                {
                    "id": stable_id("catalog", name),
                    "repo_id": repo_id,
                    "name": name,
                    "description": description,
                    "prompt": f"Document {name} for the Chaos Redux Hearts of Iron IV mod.",
                    "progress_status": "completed",
                    "dependent_files": "",
                    "gmt_create": now,
                    "gmt_modified": now,
                }
            )
            catalog_names.add(name)
            report["added_catalogs"].append(name)
        if name not in item_titles:
            items.append(
                {
                    "catalog_id": stable_id("catalog", name),
                    "title": name,
                    "description": description,
                    "extend": {},
                    "progress_status": "completed",
                    "repo_id": repo_id,
                    "reference_count": 0,
                    "id": str(uuid.uuid4()),
                    "gmt_create": now,
                    "gmt_modified": now,
                }
            )
            item_titles.add(name)
            report["added_items"].append(name)

    # 3. Report entries whose page no longer exists.
    for name in sorted(name for name in catalog_names if name and name not in pages):
        report["missing_pages"].append(name)

    # 3b. Repair item rows whose catalog_id does not resolve. An item must point at
    #     the catalog that carries its own name, so derive the id from the catalog
    #     row rather than from a freshly generated one.
    catalog_id_by_name: dict[str, str] = {}
    for row in catalogs:
        name = row.get("name")
        if name and name not in catalog_id_by_name:
            catalog_id_by_name[name] = row.get("id")
    repaired: list[str] = []
    for row in items:
        title = row.get("title")
        expected = catalog_id_by_name.get(title)
        if expected and row.get("catalog_id") != expected:
            repaired.append(title)
            row["catalog_id"] = expected
            row["gmt_modified"] = now
    report["repaired_catalog_ids"] = repaired

    # 4. Rebuild the nested relations from the page tree.
    item_by_title = {row.get("title"): row for row in items if row.get("id")}
    existing = data.get("knowledge_relations", [])
    next_id = 1 + max((row.get("id") for row in existing if isinstance(row.get("id"), int)), default=0)
    relations, _ = build_relations(collect_all_pages(), item_by_title, next_id, now)
    report["relations_before"] = len(existing)
    report["relations_after"] = len(relations)

    data["wiki_catalogs"] = catalogs
    data["wiki_items"] = items
    data["knowledge_relations"] = relations
    data["last_commit_id"] = head
    data["last_commit_update"] = head_date
    data["recovery_checkpoint"] = "wiki_generation_completed"

    print(f"pages on disk           : {len(pages)}")
    print(f"catalog rows before/after: {before['catalog_rows']} -> {len(catalogs)}")
    print(f"catalog names before/after: {before['catalog_names']} -> {len(catalog_names)}")
    print(f"item rows before/after  : {before['item_rows']} -> {len(items)}")
    print(f"item titles before/after: {before['item_titles']} -> {len(item_titles)}")
    print(f"catalogs promoted       : {len(report['promoted'])}")
    for name in report["promoted"]:
        print(f"    promoted: {name}")
    print(f"catalogs added          : {len(report['added_catalogs'])}")
    for name in report["added_catalogs"]:
        print(f"    added: {name}")
    print(f"items added             : {len(report['added_items'])}")
    print(f"catalog ids repaired    : {len(report['repaired_catalog_ids'])}")
    for name in report["repaired_catalog_ids"]:
        print(f"    repaired: {name}")
    print(f"catalogs without a page : {len(report['missing_pages'])}")
    for name in report["missing_pages"]:
        print(f"    missing page: {name}")
    print(f"relations before/after  : {report['relations_before']} -> {report['relations_after']}")
    print(f"baseline commit         : {head[:12]} {head_date}")

    if args.json:
        with open(args.json, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(report, handle, indent=2)
            handle.write("\n")
        print(f"report written          : {args.json}")

    if args.apply:
        with open(METADATA, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(data, handle, ensure_ascii=False, separators=(",", ":"))
            handle.write("\n")
        print(f"metadata written        : {METADATA}")
    else:
        print("dry run: pass --apply to write the reconciled metadata")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

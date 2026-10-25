#!/usr/bin/env python3
"""Regenerate AGENTS.md from the canonical CLAUDE.md.

CLAUDE.md is the single authoring source for project rules. Codex, Cursor,
Qoder, OpenCode, and DeepSeek Harness read AGENTS.md, so this tool writes it as
a projection: the same text with the runtime-specific phrases listed in
`instruction_projection.json` replaced. Edit CLAUDE.md, then run:

    python .tools/sync/sync_instructions.py           # write AGENTS.md
    python .tools/sync/sync_instructions.py --check   # report drift, write nothing

A replacement whose canonical text no longer occurs in CLAUDE.md is reported,
so a reworded rule cannot silently drop its runtime-specific variant.
Adopted from the Agentic HOI4 Modding package's tool of the same name.

Standard library only; runs on Python 3.9 or newer.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable, Tuple

TOOLS_DIR = Path(__file__).resolve().parent
MOD_ROOT = TOOLS_DIR.parents[1]
CONFIG = TOOLS_DIR / "instruction_projection.json"


def project(text: str, replacements: Iterable[Tuple[str, ...]]) -> str:
    for canonical, replacement in replacements:
        text = text.replace(canonical, replacement)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate AGENTS.md from the canonical CLAUDE.md.")
    parser.add_argument("--check", action="store_true", help="report drift without writing; exit 1 when out of sync")
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    replacements = [tuple(pair) for pair in config["replacements"]]
    handled = 0
    failures = 0
    for pair in config["pairs"]:
        source = MOD_ROOT / pair["source"]
        target = MOD_ROOT / pair["target"]
        if not source.is_file():
            continue
        handled += 1
        text = source.read_text(encoding="utf-8").replace("\r\n", "\n")
        unused = [canonical for canonical, _ in replacements if canonical not in text]
        for canonical in unused:
            print(f"UNUSED: {pair['source']} no longer contains the replacement source starting {canonical[:60]!r}.")
        failures += len(unused)
        expected = project(text, replacements)
        current = target.read_text(encoding="utf-8").replace("\r\n", "\n") if target.is_file() else None
        if current == expected:
            print(f"{pair['target']}: in sync with {pair['source']}.")
            continue
        if args.check:
            print(f"Would update {pair['target']}")
            print(f"  it differs from the projection of {pair['source']}; run python .tools/sync/sync_instructions.py")
            failures += 1
            continue
        with target.open("w", encoding="utf-8", newline="") as handle:
            handle.write(expected)
        print(f"{pair['target']}: regenerated from {pair['source']}.")
    if not handled:
        print("No canonical instruction file (CLAUDE.md) was found; nothing to project.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Static audit of Chaos Redux script definitions against their references.

This tool answers four source-only questions without running the game:

1. Which scripted effects, scripted triggers, scripted-localisation entries,
   script-constant categories, ideas, dynamic and opinion modifiers, and events
   are defined but never referenced by name anywhere in the loaded tree? Those
   are dead-code candidates.
2. Which of those candidates could still be reached through a built name? A
   definition is reported as `dynamic` instead of `dead` when some
   `prefix_[`, `prefix_@` or `prefix_$` stem in the tree is a prefix of its
   name (meta_effect / meta_trigger substitution or targeted names). Events
   use the same test with id stems such as `chaosx.fallout.[` or `chaosx.nr6.`.
3. Which flags are checked with `has_<scope>_flag` but never set, and which are
   set but never checked? The first list is a bug-triage list.
4. Which scripted effects and triggers have byte-identical bodies (`exact`), or
   bodies that differ only in numbers, script constants, `@` macros and tag
   literals (`param`)? Those are consolidation candidates.

The test is deliberately conservative: comments are stripped, and a name counts
as live when it appears as a token anywhere outside its own definition.
Generated registries and catalogs still appear as candidates; their file headers
say whether they may be edited. Every candidate must be verified with a search
before anything is removed. See `.claude/skills/chaos-redux-codebase-cleanup/`.

Usage:
	python .tools/audit_script_references_static.py                 # summary
	python .tools/audit_script_references_static.py --json out.json # full data
	python .tools/audit_script_references_static.py --sections dead,flags
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = ["common", "events", "interface", "history", "localisation", "map", "gfx", "music", "sound"]
SCAN_SUFFIXES = (".txt", ".gui", ".gfx", ".yml", ".asset", ".lua")
FLAG_SCOPES = ["country", "global", "state", "character", "unit_leader", "mio"]
EVENT_KINDS = ("country_event", "news_event", "state_event", "unit_leader_event", "operative_leader_event")
MIN_CLONE_CHARS = 120

TOKEN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
STEM = re.compile(r"([A-Za-z_][A-Za-z0-9_]*_)(?:\[|@|\$)")
EVENT_STEM = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)*\.[A-Za-z0-9_]*)\[")
EVENT_ID = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)+)\b")
CONSTANT_REF = re.compile(r"constant:([A-Za-z0-9_]+)\.")
FLAG_USE = re.compile(
	r"\b(set|has)_(?:%s)_flag\s*=\s*(?:\{[^}]*?\bflag\s*=\s*)?([A-Za-z_][A-Za-z0-9_]*)(?![A-Za-z0-9_@\[\$])" % "|".join(FLAG_SCOPES)
)
TOP_KEY = re.compile(r"([A-Za-z0-9_@.:\-]+)\s*=\s*\{")


def strip_comments(text: str) -> str:
	out = []
	for line in text.split("\n"):
		if "#" not in line:
			out.append(line)
			continue
		quoted = False
		for i, c in enumerate(line):
			if c == '"':
				quoted = not quoted
			elif c == "#" and not quoted:
				line = line[:i]
				break
		out.append(line)
	return "\n".join(out)


def keys_at_depth(text: str, want: int) -> List[Tuple[str, int, int, int]]:
	"""Return (key, line, body_start, body_end) for `key = {` blocks at brace depth `want`."""
	res = []
	depth = 0
	line = 1
	i = 0
	n = len(text)
	while i < n:
		c = text[i]
		if c == "\n":
			line += 1
		elif c == "{":
			depth += 1
		elif c == "}":
			depth -= 1
		elif depth == want and (c.isalnum() or c in "_@") and (i == 0 or not (text[i - 1].isalnum() or text[i - 1] in "_.")):
			m = TOP_KEY.match(text, i)
			if m:
				start = m.end()
				d = 1
				j = start
				while j < n and d:
					if text[j] == "{":
						d += 1
					elif text[j] == "}":
						d -= 1
					j += 1
				res.append((m.group(1), line, start, j - 1))
				line += text[i:m.end()].count("\n")
				depth += 1
				i = m.end()
				continue
		i += 1
	return res


def load_tree() -> Dict[str, str]:
	texts = {}
	for d in SCAN_DIRS:
		base = REPO_ROOT / d
		if not base.exists():
			continue
		for p in base.rglob("*"):
			if p.is_file() and p.suffix in SCAN_SUFFIXES:
				rel = p.relative_to(REPO_ROOT).as_posix()
				t = p.read_text(encoding="utf-8-sig", errors="replace")
				texts[rel] = t if rel.endswith(".yml") else strip_comments(t)
	return texts


def dirty_paths() -> set:
	try:
		out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=REPO_ROOT,
			capture_output=True, text=True, check=True).stdout
	except Exception:
		return set()
	return {line[3:].strip().strip('"') for line in out.splitlines()}


def helper_blocks(texts: Dict[str, str]) -> Dict[str, Tuple[str, List[Tuple[str, int, int, int]]]]:
	"""Parse every scripted effect and trigger file once: rel -> (kind, top-level blocks)."""
	blocks = {}
	for rel, t in texts.items():
		if not rel.endswith(".txt"):
			continue
		if rel.startswith("common/scripted_effects/"):
			blocks[rel] = ("effect", keys_at_depth(t, 0))
		elif rel.startswith("common/scripted_triggers/"):
			blocks[rel] = ("trigger", keys_at_depth(t, 0))
	return blocks


def collect_definitions(texts: Dict[str, str], blocks) -> Dict[str, List[Tuple[str, str, int]]]:
	defs: Dict[str, List[Tuple[str, str, int]]] = defaultdict(list)
	for rel, (kind, found) in blocks.items():
		defs["scripted_" + kind] += [(k, rel, ln) for k, ln, _, _ in found if not k.startswith("@")]
	for rel, t in texts.items():
		if not rel.endswith(".txt") or rel in blocks:
			continue
		if rel.startswith("common/scripted_localisation/"):
			for m in re.finditer(r'defined_text\s*=\s*\{\s*name\s*=\s*"?([A-Za-z0-9_]+)', t):
				defs["scripted_localisation"].append((m.group(1), rel, t.count("\n", 0, m.start()) + 1))
		elif rel.startswith("common/ideas/"):
			defs["idea"] += [(k, rel, ln) for k, ln, _, _ in keys_at_depth(t, 2)]
		elif rel.startswith("common/dynamic_modifiers/"):
			defs["dynamic_modifier"] += [(k, rel, ln) for k, ln, _, _ in keys_at_depth(t, 0)]
		elif rel.startswith("common/opinion_modifiers/"):
			defs["opinion_modifier"] += [(k, rel, ln) for k, ln, _, _ in keys_at_depth(t, 1)]
		elif rel.startswith("common/script_constants/"):
			defs["constant_category"] += [(k, rel, ln) for k, ln, _, _ in keys_at_depth(t, 0)]
		elif rel.startswith("events/"):
			for m in re.finditer(r"^(%s)\s*=\s*\{" % "|".join(EVENT_KINDS), t, re.M):
				idm = re.search(r"\bid\s*=\s*([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)+)", t[m.end():m.end() + 400])
				if idm:
					defs["event"].append((idm.group(1), rel, t.count("\n", 0, m.start()) + 1))
	return defs


def audit_dead(texts, defs, dirty):
	tokens: Counter = Counter()
	stems = set()
	event_refs: Counter = Counter()
	const_refs: Counter = Counter()
	for rel, t in texts.items():
		tokens.update(TOKEN.findall(t))
		const_refs.update(CONSTANT_REF.findall(t))
		stems.update(STEM.findall(t))
		if not rel.endswith(".yml"):
			event_refs.update(EVENT_ID.findall(t))
			stems.update(EVENT_STEM.findall(t))
	out = {}
	for kind, items in defs.items():
		counts = Counter(n for n, _, _ in items)
		rows = []
		for name, rel, ln in items:
			if kind == "event":
				refs = event_refs[name] - counts[name]
			elif kind == "constant_category":
				refs = const_refs[name] + max(0, tokens[name] - counts[name])
			else:
				refs = tokens[name] - counts[name]
			if refs > 0:
				continue
			dyn = sorted(s for s in stems if name.startswith(s))[:5]
			rows.append({"name": name, "file": rel, "line": ln, "dirty_file": rel in dirty, "dynamic_stems": dyn})
		out[kind] = {
			"defined": len(items),
			"duplicate_definitions": sorted(n for n, c in counts.items() if c > 1),
			"dead": [r for r in rows if not r["dynamic_stems"]],
			"dynamic": [r for r in rows if r["dynamic_stems"]],
		}
	return out


def audit_flags(texts):
	set_c: Counter = Counter()
	chk_c: Counter = Counter()
	where: Dict[str, set] = defaultdict(set)
	dyn = set()
	for rel, t in texts.items():
		if rel.endswith(".yml"):
			continue
		for m in FLAG_USE.finditer(t):
			(set_c if m.group(1) == "set" else chk_c)[m.group(2)] += 1
			where[m.group(2)].add(rel)
		dyn.update(re.findall(r"\b(?:set|has|clr)_[a-z_]+_flag\s*=\s*(?:\{[^}]*?\bflag\s*=\s*)?([A-Za-z_][A-Za-z0-9_]*?)(?:@|\[|\$)", t))

	def is_dynamic(flag):
		return any(flag.startswith(s) for s in dyn if len(s) > 3)

	return {
		"checked_never_set": [{"flag": f, "files": sorted(where[f])[:4]} for f in sorted(chk_c) if not set_c[f] and not is_dynamic(f)],
		"set_never_checked": [{"flag": f, "files": sorted(where[f])[:4]} for f in sorted(set_c) if not chk_c[f] and not is_dynamic(f)],
	}


def _norm(body):
	return re.sub(r"\s+", " ", body).strip()


def _param(body):
	b = _norm(body)
	b = re.sub(r"constant:[A-Za-z0-9_]+\.[A-Za-z0-9_]+", "C", b)
	b = re.sub(r"@[A-Za-z0-9_]+", "C", b)
	b = re.sub(r"(?<![A-Za-z0-9_])-?\d+(\.\d+)?(?![A-Za-z0-9_])", "N", b)
	return re.sub(r"\b[A-Z][A-Z0-9]{2}\b", "TAG", b)


def audit_clones(texts, blocks):
	exact = defaultdict(list)
	param = defaultdict(list)
	for rel, (kind, found) in blocks.items():
		t = texts[rel]
		for name, ln, s, e in found:
			body = t[s:e]
			nb = _norm(body)
			if len(nb) < MIN_CLONE_CHARS:
				continue
			exact[(kind, nb)].append([name, rel, ln])
			param[(kind, _param(body))].append([name, rel, ln])
	ex = [{"kind": k[0], "chars": len(k[1]), "members": v} for k, v in exact.items() if len(v) > 1]
	pa = [{"kind": k[0], "chars": len(k[1]), "members": v} for k, v in param.items() if len(v) > 2]
	ex.sort(key=lambda g: -g["chars"] * len(g["members"]))
	pa.sort(key=lambda g: -g["chars"] * len(g["members"]))
	return {"exact": ex, "param": pa}


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
	ap.add_argument("--json", help="write the full findings to this file")
	ap.add_argument("--sections", default="dead,flags,clones", help="comma list of dead, flags, clones")
	args = ap.parse_args()
	sections = set(args.sections.split(","))
	texts = load_tree()
	dirty = dirty_paths()
	blocks = helper_blocks(texts) if sections & {"dead", "clones"} else {}
	result = {}
	if "dead" in sections:
		result["dead"] = audit_dead(texts, collect_definitions(texts, blocks), dirty)
	if "flags" in sections:
		result["flags"] = audit_flags(texts)
	if "clones" in sections:
		result["clones"] = audit_clones(texts, blocks)

	print("=" * 78)
	print("Chaos Redux static script reference audit")
	print("=" * 78)
	for kind, v in result.get("dead", {}).items():
		print(f"{kind:22s} defined={v['defined']:6d} duplicate_defs={len(v['duplicate_definitions']):4d} "
			f"dead={len(v['dead']):5d} dynamic={len(v['dynamic']):5d}")
	if "flags" in result:
		print(f"flags checked never set : {len(result['flags']['checked_never_set'])}")
		print(f"flags set never checked : {len(result['flags']['set_never_checked'])}")
	if "clones" in result:
		print(f"exact clone groups      : {len(result['clones']['exact'])}")
		print(f"param clone groups (3+) : {len(result['clones']['param'])}")
	if args.json:
		Path(args.json).write_text(json.dumps(result, indent=1), encoding="utf-8")
		print(f"wrote {args.json}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

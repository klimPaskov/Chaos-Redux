#!/usr/bin/env python3
"""
sync_agents.py - one-way Claude Code -> other-runtime synchronization.

Chaos Redux is authored in Claude Code. The Claude Code definitions are the
canonical source, and every other runtime is generated from them:

  * Claude Code subagents : .claude/agents/<kebab-name>.md      (CANONICAL)
  * Claude Code skills    : .claude/skills/<name>/SKILL.md      (CANONICAL)
  * Codex subagents       : .codex/agents/<snake_name>.toml     (generated)
  * Qoder subagents       : .qoder/agents/<kebab-name>.md       (generated)
  * Cursor subagents      : .cursor/agents/<kebab-name>.md      (generated)
  * opencode subagents    : .opencode/agent/<kebab-name>.md     (generated)
  * Shared skill root     : .agents/skills/<name> -> .claude/skills/<name>
                            (junction or copy, read by Codex, DSH, opencode)

Run it after changing a canonical definition or adding a skill:

    python .tools/sync/sync_agents.py              # every target
    python .tools/sync/sync_agents.py codex skills # selected targets
    python .tools/sync/sync_agents.py --verify     # read the outputs back

Canonical agent format
----------------------
Markdown with YAML frontmatter `name` (hyphen-case), `description`,
`model` (`haiku`, `sonnet`, or `opus`), and `effort` (`low`, `medium`, `high`,
`xhigh`, or `max`), then the prompt body. The body is the
scope contract for every runtime, so it stays runtime-neutral. Facts that only
one runtime needs live in `.tools/sync/agent_profiles.json`: the authority
class (used for Qoder tool lists and the maps), the tier-to-model mapping for
Codex, Cursor and opencode, and the Codex nickname candidates.

Conversion rules
----------------
1. Qoder, Cursor and opencode keep the hyphen-case name; Codex uses the
   snake_case identifier (`chaosx-repo-explorer` -> `chaosx_repo_explorer`).
2. `description` and the prompt body are copied verbatim.
3. The model tier maps through `agent_profiles.json`: Codex receives a pinned
   model, Cursor receives `fast` or `inherit`, opencode receives `inherit`, and
   Qoder has no model field. `effort` is a Claude Code frontmatter field that
   overrides the session effort for the subagent; Codex receives it as
   `model_reasoning_effort`, and Cursor, Qoder and opencode have no verified
   equivalent in this setup, so it is dropped there.
4. Qoder tools derive from the authority class; no other runtime has a
   verified tool allowlist, so the prompt body is the scope contract there.
5. Only agent files are written into the agent folders, because Cursor,
   opencode, Qoder and Claude Code load every Markdown file in them.

Skill mirror
------------
`.agents/skills/<name>` is a Windows junction to the canonical
`.claude/skills/<name>`, so a skill's bundled `assets/` and `tools/` stay
readable and the content stays single-sourced. `--mode copy` copies instead,
for machines or archives without junctions. A refused junction degrades to a
copy and is reported. A real directory that blocks a mirror is reported and
left in place.

Output is idempotent: files are rewritten only when their content changes.
Stale outputs without a canonical source are reported, never deleted.
"""

import argparse
import ctypes
import filecmp
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

MOD_ROOT = Path(__file__).resolve().parents[2]
PROFILES_PATH = Path(__file__).with_name("agent_profiles.json")
CLAUDE_DIR = MOD_ROOT / ".claude"
CLAUDE_AGENTS = CLAUDE_DIR / "agents"
CLAUDE_SKILLS = CLAUDE_DIR / "skills"
CLAUDE_AGENT_MAP = CLAUDE_DIR / "agent-map.md"
CODEX_AGENTS = MOD_ROOT / ".codex" / "agents"
QODER_AGENTS = MOD_ROOT / ".qoder" / "agents"
CURSOR_DIR = MOD_ROOT / ".cursor"
CURSOR_AGENTS = CURSOR_DIR / "agents"
OPENCODE_DIR = MOD_ROOT / ".opencode"
OPENCODE_AGENTS = OPENCODE_DIR / "agent"
SHARED_SKILLS = MOD_ROOT / ".agents" / "skills"

TARGETS = ("claude-map", "codex", "qoder", "cursor", "opencode", "skills")
VALID_TIERS = ("haiku", "sonnet", "opus")
VALID_EFFORTS = ("low", "medium", "high", "xhigh", "max")

TOOLS_READONLY = "Read, Grep, Glob, Bash, Write"
TOOLS_PATCH = "Read, Grep, Glob, Bash, Edit, Write"
TOOLS_ASSET_WEB = TOOLS_PATCH + ", WebFetch, WebSearch"
AUTHORITY_CLASSES = {
    "readonly": ("read-only / plan-only", TOOLS_READONLY),
    "patch": ("patch-capable", TOOLS_PATCH),
    "asset_web": ("asset / research (web)", TOOLS_ASSET_WEB),
}


# --------------------------------------------------------------------------
# Canonical definitions
# --------------------------------------------------------------------------

def load_profiles():
    with open(PROFILES_PATH, encoding="utf-8") as handle:
        return json.load(handle)


def parse_scalar(raw):
    raw = raw.strip()
    if raw.startswith('"'):
        return json.loads(raw)
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1].replace("''", "'")
    return raw


def parse_agent(path):
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.match(r"---\n(.*?)\n---\n(.*)\Z", text, re.S)
    if not match:
        sys.exit("ERROR: {} has no YAML frontmatter".format(path))
    fields = {}
    for line in match.group(1).split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep or line.startswith((" ", "\t")):
            sys.exit("ERROR: {}: unsupported frontmatter line: {!r}".format(path, line))
        fields[key.strip()] = parse_scalar(value)
    for key in ("name", "description", "model", "effort"):
        if not fields.get(key):
            sys.exit("ERROR: {} is missing frontmatter `{}`".format(path, key))
    if fields["model"] not in VALID_TIERS:
        sys.exit("ERROR: {}: model `{}` is not one of {}".format(path, fields["model"], VALID_TIERS))
    if fields["effort"] not in VALID_EFFORTS:
        sys.exit("ERROR: {}: effort `{}` is not one of {}".format(path, fields["effort"], VALID_EFFORTS))
    if fields["name"] != path.stem:
        sys.exit("ERROR: {}: name `{}` must equal the file name".format(path, fields["name"]))
    body = match.group(2).strip()
    if not body:
        sys.exit("ERROR: {} has an empty prompt body".format(path))
    snake = fields["name"].replace("-", "_")
    return {
        "kebab": fields["name"],
        "snake": snake,
        "description": fields["description"].strip(),
        "tier": fields["model"],
        "effort": fields["effort"],
        "body": body + "\n",
        "source": path.name,
    }


def load_agents(profiles):
    if not CLAUDE_AGENTS.is_dir():
        sys.exit("ERROR: canonical agent folder not found: {}".format(CLAUDE_AGENTS))
    agents = [parse_agent(p) for p in sorted(CLAUDE_AGENTS.glob("*.md"))]
    for agent in agents:
        meta = profiles["agents"].get(agent["snake"])
        if not meta:
            sys.exit("ERROR: {} has no entry in agent_profiles.json".format(agent["snake"]))
        if meta["authority"] not in AUTHORITY_CLASSES:
            sys.exit("ERROR: {}: unknown authority `{}`".format(agent["snake"], meta["authority"]))
        agent["authority"] = meta["authority"]
        agent["nicknames"] = meta.get("codex_nickname_candidates", [])
    return agents


def policy_effort(profiles, snake):
    policy = profiles["effort_policy"]
    for level in VALID_EFFORTS:
        if snake in policy.get(level, []):
            return level
    return policy["default"]


def policy_tier(profiles, snake):
    policy = profiles["tier_policy"]
    for tier in ("opus", "sonnet"):
        if snake in policy[tier]:
            return tier
    return policy["default"]


# --------------------------------------------------------------------------
# Shared helpers
# --------------------------------------------------------------------------

def yaml_quote(value):
    return '"{}"'.format(value.replace("\\", "\\\\").replace('"', '\\"'))


def toml_quote(value):
    return '"{}"'.format(value.replace("\\", "\\\\").replace('"', '\\"'))


def toml_multiline(value):
    escaped = value.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
    return '"""\n{}"""'.format(escaped)


def write_if_changed(path, content):
    if path.exists() and not path.is_dir() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(content)
    return True


def banner_comment(agent, target_script="python .tools/sync/sync_agents.py"):
    return "Generated from .claude/agents/{} by {}. Do not hand-edit.".format(agent["source"], target_script)


def label(agent):
    return AUTHORITY_CLASSES[agent["authority"]][0]


# --------------------------------------------------------------------------
# Renderers
# --------------------------------------------------------------------------

def render_codex(agent, profiles):
    tier = profiles["tiers"][agent["tier"]]["codex"]
    effort = profiles["codex_effort"][agent["effort"]]
    lines = [
        "# " + banner_comment(agent),
        "name = {}".format(toml_quote(agent["snake"])),
        "description = {}".format(toml_quote(agent["description"])),
        "model = {}".format(toml_quote(tier["model"])),
        "model_reasoning_effort = {}".format(toml_quote(effort)),
        "sandbox_mode = {}".format(toml_quote(profiles["codex_sandbox_mode"])),
        "nickname_candidates = [{}]".format(", ".join(toml_quote(n) for n in agent["nicknames"])),
        "",
        "developer_instructions = " + toml_multiline(agent["body"]),
        "",
    ]
    return "\n".join(lines)


def render_qoder(agent, profiles):
    tools = AUTHORITY_CLASSES[agent["authority"]][1]
    return "\n".join(
        [
            "---",
            "name: {}".format(agent["kebab"]),
            "description: {}".format(yaml_quote(agent["description"])),
            "tools: {}".format(tools),
            "---",
            "",
            "<!-- {} -->".format(banner_comment(agent)),
            "",
            agent["body"].rstrip(),
            "",
        ]
    )


def render_cursor(agent, profiles):
    model = profiles["tiers"][agent["tier"]]["cursor"]
    return "\n".join(
        [
            "---",
            "# " + banner_comment(agent),
            "name: {}".format(agent["kebab"]),
            "description: {}".format(yaml_quote(agent["description"])),
            "model: {}".format(model),
            "---",
            "",
            agent["body"].rstrip(),
            "",
        ]
    )


def render_opencode(agent, profiles):
    model = profiles["tiers"][agent["tier"]]["opencode"]
    return "\n".join(
        [
            "---",
            "# " + banner_comment(agent),
            "description: {}".format(yaml_quote(agent["description"])),
            "mode: subagent",
            "model: {}".format(model),
            "---",
            "",
            agent["body"].rstrip(),
            "",
        ]
    )


MAP_NOTE = (
    "Authority classes follow the `chaos-redux-subagents` skill. {runtime} has no verified tool allowlist "
    "in this setup, so the prompt body is the scope contract."
)


def map_rows(agents, name_key, extra=None):
    rows = []
    for agent in agents:
        cells = ["`{}`".format(agent["snake"]), "`{}`".format(agent[name_key])]
        if extra:
            cells.append("`{}`".format(extra(agent)))
        cells.append(label(agent))
        rows.append("| " + " | ".join(cells) + " |")
    return rows


def render_claude_map(agents, profiles):
    rows = map_rows(agents, "kebab", extra=lambda a: "{} / {}".format(a["tier"], a["effort"]))
    return (
        "<!-- Derived from the .claude/agents frontmatter and .tools/sync/agent_profiles.json by "
        "python .tools/sync/sync_agents.py claude-map. -->\n"
        "# Claude Code Subagent Map\n\n"
        "Every file in `.claude/agents/` is a canonical Claude Code project subagent: Markdown with `name`, "
        "`description`, `model` and `effort` YAML frontmatter plus a prompt body. Edit those files directly. "
        "Do not put README or other non-agent Markdown in that folder, because Claude Code loads every `*.md` there.\n\n"
        "Other runtimes are generated from these definitions with `python .tools/sync/sync_agents.py`. "
        "Claude Code subagents run in an isolated context window, so the parent prompt must be fully explicit. "
        "Each subagent runs on the fixed model tier and reasoning effort in the table; the parent may override the model for one spawn.\n\n"
        "| Identifier | Claude Code | Model / effort | Authority |\n| --- | --- | --- | --- |\n"
        + "\n".join(rows)
        + "\n\n"
        + MAP_NOTE.format(runtime="Claude Code")
        + "\n"
    )


def render_qoder_readme(agents, profiles):
    rows = map_rows(agents, "kebab")
    return (
        "<!-- GENERATED FILE: regenerated by python .tools/sync/sync_agents.py qoder. -->\n"
        "# Qoder Subagents (Generated)\n\n"
        "Every file in this folder is generated from the canonical Claude Code definitions in `.claude/agents/`. "
        "Do not hand-edit them. To change a subagent, edit its `.claude/agents/<name>.md` source and rerun the sync script.\n\n"
        "| Identifier | Qoder | Authority |\n| --- | --- | --- |\n"
        + "\n".join(rows)
        + "\n\nQoder tool access in the frontmatter is coarse and derives from the authority class. "
        "The prompt body of each agent is the authoritative scope contract.\n"
    )


def render_runtime_map(runtime, agents, profiles, folder, name_key="kebab", with_model=None):
    if with_model:
        rows = map_rows(agents, name_key, extra=with_model)
        header = "| Identifier | {} | Model | Authority |\n| --- | --- | --- | --- |".format(runtime)
    else:
        rows = map_rows(agents, name_key)
        header = "| Identifier | {} | Authority |\n| --- | --- | --- |".format(runtime)
    return (
        "<!-- GENERATED FILE: regenerated by python .tools/sync/sync_agents.py {key}. -->\n"
        "# {runtime} Subagent Map\n\n"
        "Every file in `{folder}` is a generated {runtime} project subagent. "
        "Do not hand-edit them and do not put README or other non-agent Markdown in that folder. "
        "Edit the canonical `.claude/agents/<name>.md` definition and rerun the sync script.\n\n"
        "{header}\n{rows}\n\n{note}\n"
    ).format(
        key=runtime.lower(),
        runtime=runtime,
        folder=folder,
        header=header,
        rows="\n".join(rows),
        note=MAP_NOTE.format(runtime=runtime),
    )


# --------------------------------------------------------------------------
# Target runners
# --------------------------------------------------------------------------

def sync_files(label_text, folder, agents, profiles, renderer, extension, extra_outputs=None, keep=()):
    created, updated, unchanged = [], [], []
    expected = set(keep)
    for agent in agents:
        name = agent["snake"] if extension == ".toml" else agent["kebab"]
        out_path = folder / (name + extension)
        expected.add(out_path.name)
        existed = out_path.exists()
        changed = write_if_changed(out_path, renderer(agent, profiles))
        (updated if existed and changed else created if changed else unchanged).append(name)
    for path, content in (extra_outputs or []):
        write_if_changed(path, content)
        if path.parent == folder:
            expected.add(path.name)
    stale = sorted(p.name for p in folder.glob("*" + extension) if p.name not in expected)
    print(
        "{}: {} agent(s), {} created, {} updated, {} unchanged.".format(
            label_text, len(agents), len(created), len(updated), len(unchanged)
        )
    )
    if created:
        print("  created: {}".format(", ".join(created)))
    if updated:
        print("  updated: {}".format(", ".join(updated)))
    if stale:
        print("  WARNING: stale file(s) without a canonical source (not deleted): {}".format(", ".join(stale)))


def run_claude_map(agents, profiles):
    changed = write_if_changed(CLAUDE_AGENT_MAP, render_claude_map(agents, profiles))
    print("claude-map: {}.".format("updated" if changed else "unchanged"))


def run_codex(agents, profiles):
    sync_files("codex", CODEX_AGENTS, agents, profiles, render_codex, ".toml")


def run_qoder(agents, profiles):
    sync_files(
        "qoder", QODER_AGENTS, agents, profiles, render_qoder, ".md",
        extra_outputs=[(QODER_AGENTS / "README.md", render_qoder_readme(agents, profiles))],
        keep=("README.md",),
    )


def run_cursor(agents, profiles):
    text = render_runtime_map(
        "Cursor", agents, profiles, ".cursor/agents/", with_model=lambda a: profiles["tiers"][a["tier"]]["cursor"]
    )
    sync_files(
        "cursor", CURSOR_AGENTS, agents, profiles, render_cursor, ".md",
        extra_outputs=[(CURSOR_DIR / "agent-map.md", text)],
    )


def run_opencode(agents, profiles):
    text = render_runtime_map(
        "opencode", agents, profiles, ".opencode/agent/", with_model=lambda a: profiles["tiers"][a["tier"]]["opencode"]
    )
    sync_files(
        "opencode", OPENCODE_AGENTS, agents, profiles, render_opencode, ".md",
        extra_outputs=[(OPENCODE_DIR / "agent-map.md", text)],
    )


# --------------------------------------------------------------------------
# Skill mirror (.agents/skills -> .claude/skills)
# --------------------------------------------------------------------------

def is_junction(path):
    if not path.is_dir():
        return False
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(str(path))
    except (AttributeError, OSError):
        return path.is_symlink()
    if attrs == -1:
        return False
    return bool(attrs & 0x400)  # FILE_ATTRIBUTE_REPARSE_POINT


def make_junction(link, target):
    if os.name == "nt":
        result = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True, text=True
        )
        return result.returncode == 0
    try:
        os.symlink(target, link, target_is_directory=True)
        return True
    except OSError:
        return False


def copy_tree(src, dst):
    changed = False
    if dst.is_symlink() or dst.is_file():
        dst.unlink()
        changed = True
    dst.mkdir(parents=True, exist_ok=True)
    for root, dirs, files in os.walk(src):
        rel = Path(root).relative_to(src)
        target_root = dst / rel
        target_root.mkdir(parents=True, exist_ok=True)
        for name in dirs:
            (target_root / name).mkdir(exist_ok=True)
        for name in files:
            source_file = Path(root) / name
            target_file = target_root / name
            if target_file.exists() and not target_file.is_dir() and filecmp.cmp(source_file, target_file, shallow=False):
                continue
            shutil.copy2(source_file, target_file)
            changed = True
    return changed


def sync_skill(name, source, mode):
    link = SHARED_SKILLS / name
    if link.is_symlink() or is_junction(link):
        if mode == "junction":
            if os.path.normcase(os.path.realpath(str(link))) == os.path.normcase(os.path.realpath(str(source))):
                return ("unchanged-junction", None)
        try:
            link.rmdir()  # removes a junction or directory symlink without touching its target
        except OSError:
            return ("blocked", "existing link could not be removed")
    elif link.is_dir():
        if mode == "copy":
            return ("copied" if copy_tree(source, link) else "unchanged-copy", None)
        return ("blocked", "a real directory is in the way; move its content into .claude/skills and remove it")
    elif link.exists():
        return ("blocked", "a non-directory entry is in the way")
    SHARED_SKILLS.mkdir(parents=True, exist_ok=True)
    if mode == "junction":
        if make_junction(link, source):
            return ("junctioned", None)
        return ("copied-fallback" if copy_tree(source, link) else "unchanged-copy", "junction refused; copied instead")
    return ("copied" if copy_tree(source, link) else "unchanged-copy", None)


def run_skills(mode):
    if not CLAUDE_SKILLS.is_dir():
        sys.exit("ERROR: canonical skill folder not found: {}".format(CLAUDE_SKILLS))
    SHARED_SKILLS.mkdir(parents=True, exist_ok=True)
    status, notes, expected = {}, {}, set()
    for skill_dir in sorted(p for p in CLAUDE_SKILLS.iterdir() if p.is_dir()):
        if not (skill_dir / "SKILL.md").is_file():
            continue
        expected.add(skill_dir.name)
        result, detail = sync_skill(skill_dir.name, skill_dir, mode)
        status[skill_dir.name] = result
        if detail:
            notes[skill_dir.name] = detail
    tally = {}
    for value in status.values():
        tally[value] = tally.get(value, 0) + 1
    print(
        "skills: {} skill(s) mirrored into .agents/skills: {}.".format(
            len(status), ", ".join("{} {}".format(c, s) for s, c in sorted(tally.items())) or "none"
        )
    )
    for name, detail in sorted(notes.items()):
        print("  note: {} - {}".format(name, detail))
    stale = sorted(p.name for p in SHARED_SKILLS.iterdir() if p.is_dir() and p.name not in expected)
    if stale:
        print("  WARNING: .agents/skills entr(ies) without a canonical skill (not deleted): {}".format(", ".join(stale)))


# --------------------------------------------------------------------------
# Verification
# --------------------------------------------------------------------------

def field_of(path, pattern):
    match = re.search(pattern, path.read_text(encoding="utf-8"), re.M)
    return match.group(1) if match else None


def run_verify(agents, profiles):
    problems, rows = [], []
    for agent in agents:
        expected = policy_tier(profiles, agent["snake"])
        if agent["tier"] != expected:
            problems.append("{}: canonical model {} but routing policy says {}".format(agent["kebab"], agent["tier"], expected))
        tiers = profiles["tiers"][agent["tier"]]
        codex_path = CODEX_AGENTS / (agent["snake"] + ".toml")
        cursor_path = CURSOR_AGENTS / (agent["kebab"] + ".md")
        opencode_path = OPENCODE_AGENTS / (agent["kebab"] + ".md")
        qoder_path = QODER_AGENTS / (agent["kebab"] + ".md")
        seen = {
            "claude": agent["tier"],
            "codex": field_of(codex_path, r'^model = "([^"]+)"') if codex_path.exists() else None,
            "cursor": field_of(cursor_path, r"^model: (\S+)") if cursor_path.exists() else None,
            "opencode": field_of(opencode_path, r"^model: (\S+)") if opencode_path.exists() else None,
        }
        want = {
            "claude": agent["tier"],
            "codex": tiers["codex"]["model"],
            "cursor": tiers["cursor"],
            "opencode": tiers["opencode"],
        }
        for runtime, value in seen.items():
            if value is None:
                problems.append("{}: {} output missing".format(agent["kebab"], runtime))
            elif value != want[runtime]:
                problems.append("{}: {} has model {} but expected {}".format(agent["kebab"], runtime, value, want[runtime]))
        want_effort = policy_effort(profiles, agent["snake"])
        if agent["effort"] != want_effort:
            problems.append("{}: canonical effort {} but effort policy says {}".format(agent["kebab"], agent["effort"], want_effort))
        if codex_path.exists():
            effort = field_of(codex_path, r'^model_reasoning_effort = "([^"]+)"')
            if effort != profiles["codex_effort"][agent["effort"]]:
                problems.append("{}: codex effort {} differs from the effort mapping".format(agent["kebab"], effort))
        if qoder_path.exists() and re.search(r"^model:", qoder_path.read_text(encoding="utf-8"), re.M):
            problems.append("{}: qoder definition unexpectedly carries a model field".format(agent["kebab"]))
        rows.append((agent["kebab"], seen["claude"], agent["effort"], seen["codex"], seen["cursor"], seen["opencode"]))
    for folder in (CLAUDE_AGENTS, CODEX_AGENTS, QODER_AGENTS, CURSOR_AGENTS, OPENCODE_AGENTS):
        for path in folder.glob("*"):
            if path.is_file() and re.search(r"fable", path.read_text(encoding="utf-8", errors="ignore"), re.I):
                problems.append("{}: mentions a forbidden model name".format(path.relative_to(MOD_ROOT)))
    print("{:<40} {:<8} {:<8} {:<14} {:<8} {}".format("agent", "claude", "effort", "codex", "cursor", "opencode"))
    for row in rows:
        print("{:<40} {:<8} {:<8} {:<14} {:<8} {}".format(*[str(c) for c in row]))
    if problems:
        print("VERIFY FAILED:")
        for problem in problems:
            print("  " + problem)
        return 1
    print("VERIFY OK: {} agents match the routing and effort policy in every generated runtime.".format(len(rows)))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("targets", nargs="*", metavar="target", help="Targets to generate (default: all): " + ", ".join(TARGETS) + ".")
    parser.add_argument("--mode", choices=("junction", "copy"), default="junction",
                        help="How to mirror skills into .agents/skills (default: junction, copy fallback).")
    parser.add_argument("--verify", action="store_true",
                        help="Read the generated outputs back and compare them with the routing policy.")
    args = parser.parse_args()
    unknown = [name for name in args.targets if name not in TARGETS]
    if unknown:
        parser.error("unknown target(s): {} (choose from {})".format(", ".join(unknown), ", ".join(TARGETS)))

    profiles = load_profiles()
    agents = load_agents(profiles)
    if args.verify:
        sys.exit(run_verify(agents, profiles))
    selected = args.targets or list(TARGETS)
    if "claude-map" in selected:
        run_claude_map(agents, profiles)
    if "codex" in selected:
        run_codex(agents, profiles)
    if "qoder" in selected:
        run_qoder(agents, profiles)
    if "cursor" in selected:
        run_cursor(agents, profiles)
    if "opencode" in selected:
        run_opencode(agents, profiles)
    if "skills" in selected:
        run_skills(args.mode)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
sync_claude_agents.py — one-way Codex → Claude Code synchronization.

Chaos Redux keeps Codex as the primary authoring workflow:

  * Codex runtime       : .codex/agents/*.toml    (CANONICAL authoring source)
  * Claude Code runtime : .claude/agents/*.md     (GENERATED, do not hand-edit)

Claude Code reads neither `AGENTS.md` nor `.agents/skills/`, so this generator
also produces the four Claude Code entry points that need it:

  1. `.claude/agents/<kebab-name>.md` — the project subagents.
  2. `.claude/skills/<name>`          — one junction (or copy) per repo skill,
                                        because Claude Code only loads skills
                                        from `.claude/skills/<name>/SKILL.md`
                                        and has no "point at this folder"
                                        config option.
  3. `.mcp.json` at the repo root     — the project-scoped MCP servers.
  4. `CLAUDE.md` at the repo root     — a byte-identical copy of `AGENTS.md`,
                                        written only by this generator and
                                        gitignored. `AGENTS.md` stays canonical,
                                        so edit it and rerun this command.

Run it whenever a `.codex/agents/*.toml` definition or a `.agents/skills/` skill
changes:

    python .tools/sync/sync_claude_agents.py

Also rerun `python .tools/sync/sync_qoder_agents.py`,
`python .tools/sync/sync_cursor_agents.py`, and
`python .tools/sync/sync_opencode_agents.py` in the same change so every
runtime stays aligned. Do not treat generated Claude files as a second
authoring source.

Conversion rules
----------------
1. `name` is converted from snake_case to hyphen-case for consistency with the
   Qoder, Cursor, and opencode generated-name convention
   (`chaosx_repo_explorer` -> `chaosx-repo-explorer`). The mapping is written
   to `.claude/agent-map.md`.
2. `description` is copied verbatim into the YAML frontmatter.
3. `developer_instructions` becomes the Markdown system-prompt body, with the
   same runtime-neutral substitutions used by the other generators plus the
   Claude Code wording for the fork-context rule. Claude Code subagents always
   run in a fresh context window, so the Codex-only `collaboration.spawn_agent`
   and `fork_turns="none"` mechanics are replaced with that statement instead
   of being carried into the generated prompt.
4. Codex-only fields (`model`, `model_reasoning_effort`, `sandbox_mode`,
   `nickname_candidates`) are dropped. Claude Code gets `model: inherit` so the
   parent session chooses the model.
5. Claude Code has no Claude-specific tool allowlist that reproduces the Codex
   authority classes safely, so no `tools:` key is emitted. Authority
   (read-only, patch-capable, asset/research) is enforced by the system-prompt
   body and documented per agent in `.claude/agent-map.md`, exactly as the
   Cursor and opencode generators do.
6. Write only one `.md` file per subagent into `.claude/agents/`. Never write
   README or other non-agent markdown there; Claude Code loads every `*.md` in
   that folder as a project subagent.

Skill materialization
---------------------
`.agents/skills/<name>` mirrors to `.claude/skills/<name>` as a Windows
junction by default. The junction is transparent, so a skill's bundled
`assets/` and `tools/` stay readable and runnable, and the skill content stays
single-sourced. `--mode copy` copies instead, for machines or archives where
junctions are unavailable. Re-running the sync in copy mode refreshes changed
skill files.

Output is idempotent: files are rewritten only when their content changes, and
junctions are left alone when they already point at the right target. Stale
entries without a source are reported, never deleted.
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

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    try:
        import tomli as tomllib  # Python 3.9 / 3.10 fallback
    except ModuleNotFoundError:
        sys.exit(
            "ERROR: no TOML parser available. Install tomli "
            "(python -m pip install tomli) or run on Python 3.11+."
        )

MOD_ROOT = Path(__file__).resolve().parents[2]
CODEX_AGENTS = MOD_ROOT / ".codex" / "agents"
SOURCE_SKILLS = MOD_ROOT / ".agents" / "skills"
CLAUDE_DIR = MOD_ROOT / ".claude"
CLAUDE_AGENTS = CLAUDE_DIR / "agents"
CLAUDE_SKILLS = CLAUDE_DIR / "skills"
CLAUDE_AGENT_MAP = CLAUDE_DIR / "agent-map.md"
CLAUDE_MCP = MOD_ROOT / ".mcp.json"
CLAUDE_INSTRUCTIONS = MOD_ROOT / "CLAUDE.md"
CLAUDE_INSTRUCTIONS_SOURCE = MOD_ROOT / "AGENTS.md"

# Runtime-neutral substitutions applied to developer_instructions. The first
# two replace the Codex-only spawn mechanics with the Claude Code statement of
# the same rule, so the Claude subagents do not carry instructions for a tool
# they cannot call. Keep the remaining entries aligned with
# `.tools/sync/sync_cursor_agents.py` and `.tools/sync/sync_opencode_agents.py`.
BODY_SUBSTITUTIONS = [
    (
        r"Spawn every project custom subagent with a fully explicit, self-contained prompt and no "
        r"inherited parent-thread context\. With the current Codex collaboration\.spawn_agent tool, "
        r"set fork_turns=\"none\"\. Qoder and Cursor isolate subagent context through their own "
        r"runtime mechanisms\.",
        "Spawn every project custom subagent with a fully explicit, self-contained prompt and no "
        "inherited parent-thread context. Claude Code subagents always run in an isolated context "
        "window and never see the parent thread.",
    ),
    (
        r"This project requires every custom subagent to be spawned without parent-thread history: "
        r"use `fork_turns=\"none\"` with Codex `collaboration\.spawn_agent`\. Qoder and Cursor "
        r"subagents are isolated by their runtimes\.",
        "This project requires every custom subagent to be spawned without parent-thread history. "
        "Claude Code subagents always run in an isolated context window and never see the parent "
        "thread.",
    ),
    (
        r"restart the shell or Codex",
        "restart the shell",
    ),
    (
        r"fork_context=false",
        "a fully explicit, self-contained prompt (no inherited conversation context)",
    ),
    (
        r"Agent Nudger writes",
        "UI-assisted writes",
    ),
]

# Authority classes from the chaos-redux-subagents skill. Claude Code has no
# Codex-style tool allowlist in this setup, so this map is documentation-only
# and must stay aligned with the other sync scripts.
AUTHORITY = {
    "chaosx_repo_explorer": "read-only / plan-only",
    "chaosx_event_completion_auditor": "read-only / plan-only",
    "chaosx_ai_probability_auditor": "read-only / plan-only",
    "chaosx_improvement_loop_planner": "read-only / plan-only",
    "chaosx_documentation_curator": "patch-capable",
    "chaosx_scripted_system_architect": "patch-capable",
    "chaosx_decision_mission_auditor": "patch-capable",
    "chaosx_focus_tree_auditor": "patch-capable",
    "chaosx_country_package_auditor": "patch-capable",
    "chaosx_localisation_auditor": "patch-capable",
    "chaosx_event_ui_worker": "patch-capable",
    "chaosx_skill_maintainer": "patch-capable",
    "chaosx_spreadsheet_doc_worker": "patch-capable",
    "chaosx_asset_source_researcher": "asset / research (web)",
    "chaosx_generated_event_art": "asset / research (web)",
    "chaosx_icon_artist": "asset / research (web)",
    "chaosx_portrait_creator": "asset / research (web)",
    "chaosx_super_event_text_researcher": "asset / research (web)",
    "chaosx_super_event_audio_researcher": "asset / research (web)",
    "chaosx_3d_model_pipeline": "asset / research (web)",
}

# Project-scoped Claude Code MCP servers. The server names and launch commands
# mirror `.cursor/mcp.json` and `.opencode/opencode.json`. `cwd` is set for every
# server because Claude Code launches a stdio server from an unspecified
# working directory. The mod root is written literally rather than through
# `${CLAUDE_PROJECT_DIR}`: that variable is only populated in the server's own
# environment, so a project-scoped reference to it would need a fallback and
# could silently expand to the wrong root.
MCP_SERVERS = [
    (
        "hoi4_agent_tools",
        {
            "type": "stdio",
            "command": "cmd.exe",
            "args": ["/d", "/c", "hoi4-agent-tools.cmd"],
            "cwd": "{root}",
            "env": {"CHAOS_REDUX_MOD_ROOT": "{root}"},
        },
    ),
    (
        "meshy",
        {
            "type": "stdio",
            "command": "cmd.exe",
            "args": [
                "/d",
                "/c",
                "call",
                "{root}/.tools/3d_pipeline/wrappers/run_meshy_mcp.cmd",
            ],
            "cwd": "{root}",
            "env": {
                "MESHY_API_KEY": "${MESHY_API_KEY:-}",
                "MESHY_MCP_VERSION": "${MESHY_MCP_VERSION:-}",
            },
        },
    ),
    (
        "blender_hoi4",
        {
            "type": "stdio",
            "command": "cmd.exe",
            "args": [
                "/d",
                "/c",
                "call",
                "{root}/.tools/3d_pipeline/wrappers/run_blender_hoi4_adapter.cmd",
            ],
            "cwd": "{root}",
            "env": {
                "MESHY_API_KEY": "${MESHY_API_KEY:-}",
                "CHAOS_REDUX_MOD_ROOT": "{root}",
                "CHAOS_REDUX_3D_JOB_ROOT": "{root}/docs/assets/chaos_redux_3d_model_pilots/models_3d",
            },
        },
    ),
]

AGENT_MAP_TEMPLATE = """<!-- GENERATED FILE: regenerated by python .tools/sync/sync_claude_agents.py. -->
# Claude Code Subagent Map

Every file in `.claude/agents/` is a Claude Code project subagent: Markdown with
`name`, `description`, and `model` YAML frontmatter plus a prompt body. Claude
Code loads each of those files. Do not put README or other non-agent Markdown in
`.claude/agents/`.

Regenerate after Codex TOML or `.agents/skills/` changes:

```text
python .tools/sync/sync_claude_agents.py
```

Codex remains the primary workflow. `.codex/agents/*.toml` files are Codex
definitions, not Claude Code subagent prompts. Invoke a subagent from this table
by its Claude Code name with the `Agent` tool. Claude Code subagents always run
in an isolated context window, so the parent prompt must still be fully
explicit.

| Canonical (Codex) | Claude Code | Authority |
| --- | --- | --- |
{rows}

Authority classes follow the `chaos-redux-subagents` skill. This generator emits
no `tools:` frontmatter, so the prompt body is the scope contract, exactly as in
the generated Cursor and opencode definitions.
"""


def load_toml(path):
    with open(path, "rb") as handle:
        return tomllib.load(handle)


def apply_substitutions(body):
    result = body
    for pattern, replacement in BODY_SUBSTITUTIONS:
        result = re.sub(pattern, replacement, result)
    return result.strip() + "\n"


def yaml_quote(value):
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return '"{}"'.format(escaped)


def render_agent(description, body, src_name):
    lines = [
        "---",
        "# Generated from .codex/agents/{} by python .tools/sync/sync_claude_agents.py. Do not hand-edit.".format(
            src_name
        ),
        "description: {}".format(yaml_quote(description)),
        "model: inherit",
        "---",
        "",
        body.rstrip(),
        "",
    ]
    return "\n".join(lines)


def render_mcp_config():
    servers = {}
    root = MOD_ROOT.as_posix()
    for name, entry in MCP_SERVERS:
        servers[name] = json.loads(json.dumps(entry).replace("{root}", root))
    return json.dumps({"mcpServers": servers}, indent=2, ensure_ascii=False) + "\n"


def write_if_changed(path, content):
    if path.exists() and not path.is_dir() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(content)
    return True


def copy_if_changed(source, target):
    """Write a byte-identical copy of source at target; report whether it changed."""
    if not source.is_file():
        sys.exit("ERROR: canonical source not found: {}".format(source))
    content = source.read_bytes()
    if target.is_file() and target.read_bytes() == content:
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    return True


def is_junction(path):
    """A Windows junction, or any directory symlink, presents as a reparse point."""
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
    """Create a directory junction. Needs no elevation, unlike a true symlink."""
    if os.name == "nt":
        result = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(link), str(target)],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return True
        if not link.exists():
            return False
        return False
    try:
        os.symlink(target, link, target_is_directory=True)
        return True
    except OSError:
        return False


def copy_tree(src, dst):
    """Mirror one skill directory into the Claude Code location."""
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
            if target_file.exists() and not target_file.is_dir():
                if filecmp.cmp(source_file, target_file, shallow=False):
                    continue
            shutil.copy2(source_file, target_file)
            changed = True
    return changed


def sync_skill(name, source, mode):
    """Materialize one skill. Returns (status, detail)."""
    link = CLAUDE_SKILLS / name
    if link.is_symlink() or is_junction(link):
        if mode == "junction":
            current = os.path.realpath(str(link))
            if os.path.normcase(current) == os.path.normcase(os.path.realpath(str(source))):
                return ("unchanged-junction", None)
        # Drop the link before re-creating it. rmdir removes a junction or a
        # directory symlink without touching what it points at.
        try:
            link.rmdir()
        except OSError:
            return ("blocked", "existing link could not be removed")
    elif link.is_dir():
        if mode == "copy":
            return ("copied" if copy_tree(source, link) else "unchanged-copy", None)
        return ("blocked", "a real directory is in the way; remove it to use junctions")
    elif link.exists():
        return ("blocked", "a non-directory entry is in the way")

    return materialize(link, source, mode)


def materialize(link, source, mode):
    if mode == "junction":
        CLAUDE_SKILLS.mkdir(parents=True, exist_ok=True)
        if make_junction(link, source):
            return ("junctioned", None)
        # Junctions can be refused by policy on some machines; copy instead so
        # the skill still loads, and report the degradation.
        return (
            "copied-fallback" if copy_tree(source, link) else "unchanged-copy",
            "junction refused; copied instead",
        )
    return ("copied" if copy_tree(source, link) else "unchanged-copy", None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("junction", "copy"),
        default="junction",
        help="How to materialize skills into .claude/skills (default: junction, "
        "with an automatic copy fallback when a junction is refused).",
    )
    args = parser.parse_args()

    if not CODEX_AGENTS.is_dir():
        sys.exit("ERROR: canonical source folder not found: {}".format(CODEX_AGENTS))
    if not SOURCE_SKILLS.is_dir():
        sys.exit("ERROR: skill source folder not found: {}".format(SOURCE_SKILLS))
    CLAUDE_DIR.mkdir(parents=True, exist_ok=True)
    CLAUDE_AGENTS.mkdir(parents=True, exist_ok=True)
    CLAUDE_SKILLS.mkdir(parents=True, exist_ok=True)

    created, updated, unchanged, unmapped = [], [], [], []
    expected_files = set()
    rows = []

    for toml_path in sorted(CODEX_AGENTS.glob("*.toml")):
        data = load_toml(toml_path)
        name = data.get("name") or toml_path.stem
        description = data.get("description", "").strip()
        instructions = data.get("developer_instructions", "").strip()
        if not description or not instructions:
            sys.exit("ERROR: {} is missing description or developer_instructions".format(toml_path))

        if name not in AUTHORITY:
            unmapped.append(name)

        claude_name = name.replace("_", "-")
        out_path = CLAUDE_AGENTS / "{}.md".format(claude_name)
        expected_files.add(out_path.name)
        content = render_agent(description, apply_substitutions(instructions), toml_path.name)

        if not out_path.exists():
            write_if_changed(out_path, content)
            created.append(claude_name)
        elif write_if_changed(out_path, content):
            updated.append(claude_name)
        else:
            unchanged.append(claude_name)

        rows.append(
            "| `{}` | `{}` | {} |".format(
                name, claude_name, AUTHORITY.get(name, "unmapped")
            )
        )

    write_if_changed(CLAUDE_AGENT_MAP, AGENT_MAP_TEMPLATE.format(rows="\n".join(rows)))

    mcp_changed = write_if_changed(CLAUDE_MCP, render_mcp_config())

    instructions_changed = copy_if_changed(CLAUDE_INSTRUCTIONS_SOURCE, CLAUDE_INSTRUCTIONS)

    stale_agents = sorted(
        p.name for p in CLAUDE_AGENTS.glob("*.md") if p.name not in expected_files
    )

    skill_status = {}
    skill_notes = {}
    expected_skills = set()
    for skill_dir in sorted(p for p in SOURCE_SKILLS.iterdir() if p.is_dir()):
        if not (skill_dir / "SKILL.md").is_file():
            continue
        expected_skills.add(skill_dir.name)
        status, detail = sync_skill(skill_dir.name, skill_dir, args.mode)
        skill_status[skill_dir.name] = status
        if detail:
            skill_notes[skill_dir.name] = detail

    stale_skills = sorted(
        p.name
        for p in CLAUDE_SKILLS.iterdir()
        if p.is_dir() and p.name not in expected_skills
    )

    print(
        "Synced {} agent(s): {} created, {} updated, {} unchanged.".format(
            len(created) + len(updated) + len(unchanged),
            len(created),
            len(updated),
            len(unchanged),
        )
    )
    if created:
        print("  created: {}".format(", ".join(created)))
    if updated:
        print("  updated: {}".format(", ".join(updated)))
    if unmapped:
        print("  WARNING: no authority mapping: {}".format(", ".join(unmapped)))
    print(
        "CLAUDE.md copy of AGENTS.md: {}.".format(
            "updated" if instructions_changed else "unchanged"
        )
    )
    if stale_agents:
        print(
            "  WARNING: stale agent file(s) without a TOML source (not deleted): {}".format(
                ", ".join(stale_agents)
            )
        )

    tally = {}
    for status in skill_status.values():
        tally[status] = tally.get(status, 0) + 1
    summary = ", ".join("{} {}".format(count, status) for status, count in sorted(tally.items()))
    print("Synced {} skill(s): {}.".format(len(skill_status), summary or "none"))
    for name, detail in sorted(skill_notes.items()):
        print("  note: {} — {}".format(name, detail))
    if stale_skills:
        print(
            "  WARNING: stale skill entr(ies) without a source (not deleted): {}".format(
                ", ".join(stale_skills)
            )
        )

    print("{} .mcp.json".format("Wrote" if mcp_changed else "Unchanged"))


if __name__ == "__main__":
    main()

## Multi-Runtime Workflow (Codex + Qoder + Cursor + opencode + Claude Code + DSH)

This repository runs parallel agent runtimes that never author each other's configuration.
Codex is the primary workflow and the sole authoring source for shared instruction and subagent content.
Most other runtimes' agent definitions and skill links are generated from Codex plus the shared skills folder.
DSH is the exception and needs no generator: it already reads `AGENTS.md` and `.agents/skills/` natively.

| Runtime | Loads | Agent definitions | MCP registration |
| --- | --- | --- | --- |
| Codex | `.codex/config.toml` | `.codex/agents/*.toml` (canonical source) | `.codex/config.toml` |
| Qoder | `.qoder/mcp.json` | `.qoder/agents/*.md` (generated) | `.qoder/mcp.json` |
| Cursor | `.cursor/mcp.json` and `.cursor/rules/` | `.cursor/agents/*.md` (generated) | `.cursor/mcp.json` |
| opencode | `.opencode/opencode.json` | `.opencode/agent/*.md` (generated) | `.opencode/opencode.json` |
| Claude Code | `CLAUDE.md` (generated copy of `AGENTS.md`) and `.mcp.json` | `.claude/agents/*.md` (generated) | `.mcp.json` |
| DSH | `AGENTS.md`, plus the generated `CLAUDE.md` copy when it exists | none in the repository; the shared named roles come from the skills | none in the repository; profile-scoped only |

Shared and runtime-agnostic: `.agents/skills/`, `AGENTS.md`, `docs/`, specs, plans, handoffs, and the `.tools/3d_pipeline/wrappers/` MCP wrappers.
`AGENTS.md` remains the canonical project instruction file for every runtime.

DSH is documented in [`docs/runtimes.md`](../docs/runtimes.md), which covers its native instruction and skill roots, its skill root priority, its runtime-composed subagents and model selection, and its profile-scoped MCP registration.

### Canonical source and generated output

The Codex agent TOMLs in `.codex/agents/` are the single authoring source for every custom subagent.
Qoder, Cursor, opencode, and Claude Code definitions are generated files.
Never hand-edit a generated `.qoder/agents/*.md`, `.cursor/agents/*.md`, `.opencode/agent/*.md`, or `.claude/agents/*.md` file.
Never edit the generated repo-root `CLAUDE.md`: it is a copy of `AGENTS.md` and is gitignored.
Edit the TOML source or the canonical `.agents/skills/<name>/SKILL.md`, then regenerate the affected runtimes:

```text
python .tools/sync/sync_qoder_agents.py
python .tools/sync/sync_cursor_agents.py
python .tools/sync/sync_opencode_agents.py
python .tools/sync/sync_claude_agents.py
```

DSH has no generated agent files to refresh. It consumes `AGENTS.md` and `.agents/skills/` directly, so a canonical change reaches DSH as soon as the file is saved.

### Name mapping

Codex identifiers use snake_case (`chaosx_repo_explorer`).
Every other runtime requires lowercase letters and hyphens, so the generated name is the hyphen-case equivalent (`chaosx-repo-explorer`).
Maps live in `.qoder/agents/README.md`, `.cursor/agent-map.md`, `.opencode/agent-map.md`, and `.claude/agent-map.md`.
Routing rules in this file and in the repo skills always use the canonical snake_case identifier.

### Runtime-specific rules

Cursor subagent files stay Cursor-native Markdown in `.cursor/agents/<kebab-name>.md` with YAML frontmatter `name`, `description`, and `model: inherit`, followed by the prompt body.
Cursor loads every `*.md` in that folder into the Task tool, so do not place README or other non-agent Markdown there.
Spawn a Cursor subagent by hyphen-case name (`/chaosx-repo-explorer` or the matching Task `subagent_type`).
Do not treat `.codex/agents/*.toml` as Cursor subagent prompts.

Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so `sync_claude_agents.py` writes the repo-root `CLAUDE.md` as a byte-identical copy of `AGENTS.md`.
Rerun that generator after any `AGENTS.md` change.
`AGENTS.md` stays canonical and `CLAUDE.md` is gitignored, so the copy is never edited or committed.
Claude Code also has no option to point at an external skills folder, so `.tools/sync/sync_claude_agents.py` mirrors each `.agents/skills/<name>` into `.claude/skills/<name>` as a Windows junction.
The junction is transparent, so a skill's bundled `assets/` and `tools/` stay readable and the skill content stays single-sourced.
Run the generator with `--mode copy` on a machine or archive where junctions are unavailable.
`.claude/agents/*.md` uses `description`, `model: inherit`, and the prompt body, and no `tools:` allowlist, so the prompt body is the scope contract just as it is for Cursor and opencode.

opencode has no Codex-style tool allowlist either, and it reads skills through the `skills.paths` entry in `.opencode/opencode.json` instead of a mirrored folder.

DSH needs no generated file at all: `dsh-agent-instructions` loads `AGENTS.md`, and the identical `CLAUDE.md` copy when `sync_claude_agents.py` has written one, from the project root down to the working directory, and `dsh-skill-filesystem` discovers project skills from `.agents/skills/`.
DSH also reserves `.dsh/skills/` at a higher priority than `.agents/skills/`, and this repository deliberately leaves it absent so the shared skills folder stays the single source.
DSH has no project-level MCP configuration and no repository-level subagent definition format, so its MCP servers are profile-scoped and its subagents are composed at runtime. See [`docs/runtimes.md`](../docs/runtimes.md).

MCP registration differs by runtime.
Codex registers servers in `.codex/config.toml`.
Qoder and Cursor register the matching production servers (`hoi4_agent_tools`, `meshy`, `blender_hoi4`) in `.qoder/mcp.json` and `.cursor/mcp.json`.
opencode registers them in `.opencode/opencode.json`, and Claude Code registers them in the repo-root `.mcp.json`.
DSH registers them only in the active profile's `$DSH_HOME/profiles/<profile>/cordis.patch.yml`, so no repository file carries them.
Codex-only keys such as approval modes and tool allowlists have no equivalent in the other runtimes, so the matching discipline is carried by the subagent prompts instead.
`blender_lab_dev` remains a Codex-only diagnostic server.

### Anti-interference and instruction changes

During a Qoder, Cursor, opencode, Claude Code, or DSH session, treat `.codex/**` as read-only reference.
During a Codex session, leave `.qoder/**`, generated `.cursor/agents/**`, `.opencode/agent/**`, and `.claude/**` untouched.
Any subagent instruction change lands in the TOML first, then propagates through the sync scripts.
An `AGENTS.md` change propagates to `CLAUDE.md` the same way, by rerunning `python .tools/sync/sync_claude_agents.py`; the generated copy is never committed.
The same rule applies to skill changes: edit `.agents/skills/<name>/SKILL.md` and let the generators re-link it.

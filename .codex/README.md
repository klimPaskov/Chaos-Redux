## Multi-Runtime Workflow (Claude Code + Codex + Qoder + Cursor + opencode + DSH)

This repository runs parallel agent runtimes that never author each other's configuration.
Claude Code is the primary workflow and the sole authoring source for subagent and skill content.
The other runtimes' agent definitions and the shared skill root are generated from the Claude Code definitions by `python .tools/sync/sync_agents.py`.
DSH is the exception and needs no generator: it already reads `AGENTS.md` and `.agents/skills/` natively.

| Runtime | Loads | Agent definitions | MCP registration |
| --- | --- | --- | --- |
| Claude Code | `CLAUDE.md` and `.mcp.json` | `.claude/agents/*.md` (canonical source) | `.mcp.json` |
| Codex | `AGENTS.md` and `.codex/config.toml` | `.codex/agents/*.toml` (generated) | `.codex/config.toml` |
| Qoder | `.qoder/mcp.json` | `.qoder/agents/*.md` (generated) | `.qoder/mcp.json` |
| Cursor | `.cursor/mcp.json` and `.cursor/rules/` | `.cursor/agents/*.md` (generated) | `.cursor/mcp.json` |
| opencode | `.opencode/opencode.json` | `.opencode/agent/*.md` (generated) | `.opencode/opencode.json` |
| DSH | `AGENTS.md`, plus `CLAUDE.md` when it exists | none in the repository; the shared named roles come from the skills | none in the repository; profile-scoped only |

Skills are canonical in `.claude/skills/<name>/`; `.agents/skills/<name>` is the shared skill root that Codex, DSH, and opencode read, and it is generated as a junction to the canonical folder.
Shared and runtime-agnostic: `docs/`, specs, plans, handoffs, and the `.tools/3d_pipeline/wrappers/` MCP wrappers.
`CLAUDE.md` is the canonical project instruction file for Claude Code, and `AGENTS.md` serves the other runtimes with the same structure.
The two differ only where a runtime needs different wording, such as the image-generation route: Codex has native ImageGen, and Claude Code uses the `gptimage` MCP server.

DSH is documented in [`docs/runtimes.md`](../docs/runtimes.md), which covers its native instruction and skill roots, its skill root priority, its runtime-composed subagents and model selection, and its profile-scoped MCP registration.

### Canonical source and generated output

The Claude Code agent definitions in `.claude/agents/` are the single authoring source for every custom subagent, and `.claude/skills/` is the single authoring source for skills.
Codex, Qoder, Cursor, and opencode definitions and the `.agents/skills/` links are generated files.
Never hand-edit a generated `.codex/agents/*.toml`, `.qoder/agents/*.md`, `.cursor/agents/*.md`, or `.opencode/agent/*.md` file.
Edit the canonical `.claude/agents/<name>.md` or `.claude/skills/<name>/SKILL.md`, then regenerate:

```text
python .tools/sync/sync_agents.py
python .tools/sync/sync_agents.py --verify
python .tools/sync/sync_read_limits.py
```

DSH has no generated agent files to refresh. It consumes `AGENTS.md` and `.agents/skills/` directly, so a canonical change reaches DSH as soon as the file is saved.
Shared read budgets and each runtime’s supported settings are documented in [Read budgets](../docs/runtimes.md#read-budgets); keep files under 20,000 tokens while readers allow 30,000.

### Name mapping

Canonical Claude Code identifiers use hyphen-case (`chaosx-repo-explorer`).
Codex identifiers are the snake_case equivalent (`chaosx_repo_explorer`), and Qoder, Cursor, and opencode keep the hyphen-case name.
Maps live in `.claude/agent-map.md`, `.qoder/agents/README.md`, `.cursor/agent-map.md`, and `.opencode/agent-map.md`.
Routing rules in the instruction files and in the repo skills use the snake_case identifier, which every runtime resolves to its own spelling.

### Model routing

Each canonical definition carries a `model:` of `haiku`, `sonnet`, or `opus`, set by the routing table in `.tools/sync/agent_profiles.json`.
The generator maps that tier to the model field of every other runtime: Codex pins a model and reasoning effort, Cursor uses `fast` or `inherit`, opencode uses `inherit`, and Qoder has no model field.
`python .tools/sync/sync_agents.py --verify` reads every generated file back and fails on drift from the routing table.

### Runtime-specific rules

Cursor subagent files stay Cursor-native Markdown in `.cursor/agents/<kebab-name>.md` with YAML frontmatter `name`, `description`, and `model`, followed by the prompt body.
Cursor loads every `*.md` in that folder into the Task tool, so do not place README or other non-agent Markdown there.
Spawn a Cursor subagent by hyphen-case name (`/chaosx-repo-explorer` or the matching Task `subagent_type`).
Do not treat `.codex/agents/*.toml` as Cursor subagent prompts.

Claude Code reads `CLAUDE.md` and loads project skills only from `.claude/skills/<name>/SKILL.md`, which is why that folder is canonical.
`.claude/agents/*.md` uses `name`, `description`, `model`, and the prompt body, with no `tools:` allowlist, so the prompt body is the scope contract just as it is for the generated runtimes.

opencode has no Codex-style tool allowlist either, and it reads skills through the `skills.paths` entry in `.opencode/opencode.json` that points at `.agents/skills`.

DSH needs no generated file at all: `dsh-agent-instructions` loads `AGENTS.md` and `CLAUDE.md` from the project root down to the working directory, and `dsh-skill-filesystem` discovers project skills from `.agents/skills/`.
DSH also reserves `.dsh/skills/` at a higher priority than `.agents/skills/`, and this repository deliberately leaves it absent so the shared skills folder stays the single source.
DSH has no project-level MCP configuration and no repository-level subagent definition format, so its MCP servers are profile-scoped and its subagents are composed at runtime. See [`docs/runtimes.md`](../docs/runtimes.md).

MCP registration differs by runtime.
Claude Code registers servers in the repo-root `.mcp.json`.
Codex registers servers in `.codex/config.toml`.
Qoder and Cursor register the matching production servers (`hoi4_agent_tools`, `meshy`, `blender_hoi4`) in `.qoder/mcp.json` and `.cursor/mcp.json`.
opencode registers them in `.opencode/opencode.json`.
DSH registers them only in the active profile's `$DSH_HOME/profiles/<profile>/cordis.patch.yml`, so no repository file carries them.
Codex-only keys such as approval modes and tool allowlists have no equivalent in the other runtimes, so the matching discipline is carried by the subagent prompts instead.
`blender_lab_dev` remains a Codex-only diagnostic server.
The `gptimage` MCP server is a Claude Code user-level server that supplies image generation where Codex uses its native ImageGen.

### Anti-interference and instruction changes

During a Codex, Qoder, Cursor, opencode, or DSH session, treat `.claude/agents/**` and `.claude/skills/**` as the canonical definitions: change them only when the user's request covers that content.
During a Claude Code session, leave the generated `.codex/agents/**`, `.qoder/**`, `.cursor/agents/**`, and `.opencode/agent/**` files untouched and regenerate them with the sync script instead.
Any subagent instruction change lands in `.claude/agents/` first, then propagates through the sync script.
A rule change lands in `CLAUDE.md`; `python .tools/sync/sync_instructions.py` regenerates `AGENTS.md` from it, applying the runtime-specific wording in `.tools/sync/instruction_projection.json`. Never edit `AGENTS.md` directly.
The same rule applies to skill changes: edit `.claude/skills/<name>/SKILL.md`, and the `.agents/skills/<name>` link shows the same file.
New settings may require a new runtime session; writing them does not change every already-running reader.

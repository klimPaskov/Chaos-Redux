# Agent synchronizers

This directory contains the maintained one-way generators that project canonical `.codex/agents/*.toml` definitions into the Qoder, Cursor, opencode, and Claude Code runtime formats.

DSH is intentionally absent.
It reads `AGENTS.md` and `.agents/skills/` directly, so it has neither generated agent files nor a skills mirror to refresh. Its layout and its profile-scoped MCP registration are documented in [`docs/runtimes.md`](../../docs/runtimes.md).

The available generator commands are:

```powershell
python .tools/sync/sync_qoder_agents.py
python .tools/sync/sync_cursor_agents.py
python .tools/sync/sync_opencode_agents.py
python .tools/sync/sync_claude_agents.py
```

The Codex TOML files remain authoritative. Never hand-edit generated Qoder, Cursor, opencode, or Claude Code agent definitions.

## What each generator writes

| Generator | Writes | Destinations |
| --- | --- | --- |
| `sync_qoder_agents.py` | Qoder subagent definitions | `.qoder/agents/*.md` |
| `sync_cursor_agents.py` | Cursor subagent definitions | `.cursor/agents/*.md`, `.cursor/agent-map.md` |
| `sync_opencode_agents.py` | opencode subagent definitions | `.opencode/agent/*.md`, `.opencode/agent-map.md` |
| `sync_claude_agents.py` | Claude Code subagents, skill links, MCP registration, and the generated instruction copy | `.claude/agents/*.md`, `.claude/skills/<name>`, `.claude/agent-map.md`, repo-root `.mcp.json`, repo-root `CLAUDE.md` |

`sync_claude_agents.py` writes more than agent definitions because Claude Code has no configuration option that points at an external skills folder or a shared MCP file, and it reads `CLAUDE.md` rather than `AGENTS.md`.
It therefore also writes the repo-root `CLAUDE.md` as a byte-identical copy of `AGENTS.md`, and that copy is gitignored: `AGENTS.md` stays canonical, so rerun this generator after changing it.
It mirrors each `.agents/skills/<name>` into `.claude/skills/<name>` as a Windows junction, so a skill's bundled `assets/` and `tools/` stay readable and the skill content stays single-sourced.
Pass `--mode copy` to copy the skill directories instead, for a machine or archive where junctions are unavailable.
A junction that is refused degrades to a copy and the run reports it.

## Write rules

Before running a generator, check the active runtime's destination-write rules in [`.codex/README.md`](../../.codex/README.md#anti-interference-and-instruction-changes).
A listed command does not authorize writing another runtime's files.
If the synchronization requirement conflicts with a rule to leave the destination untouched, preserve both requirements, record blocked synchronization, and request a specific ownership decision through the handoff.
Keep canonical instruction changes and unresolved generated-file consistency visible in the same handoff.

## Verification

Every generator is idempotent, so a second run must report every artifact unchanged.
Run the applicable generator twice and confirm the second run reports `0 created, 0 updated` and unchanged skills and MCP config.
A stale definition that no longer has a canonical source is reported and left in place, never deleted, so a renamed agent shows up as a stale-file warning until the parent removes it deliberately.

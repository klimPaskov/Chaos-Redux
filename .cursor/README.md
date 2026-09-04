# Cursor project runtime

Codex remains the primary workflow. This folder is the Cursor equivalent of `.qoder/`: MCP registration, a thin always-on rule, and generated Cursor project subagents.

Canonical project instructions stay in `AGENTS.md`. Cursor injects that file automatically. Do not duplicate it here.

| Path | Role |
| --- | --- |
| `AGENTS.md` (repo root) | Canonical project instructions, auto-injected by Cursor |
| `.codex/agents/*.toml` | Canonical subagent source. Edit these. |
| `.codex/config.toml` | Codex-only MCP, approval, and agent registration |
| `.cursor/mcp.json` | Cursor production MCP servers (`hoi4_agent_tools`, `meshy`, `blender_hoi4`) |
| `.cursor/rules/chaos-redux-cursor-runtime.mdc` | Always-on Cursor anti-interference rule |
| `.cursor/agents/*.md` | Generated Cursor Task-tool subagents. Do not hand-edit. |
| `.cursor/agent-map.md` | Generated Codex-to-Cursor name map |

Each file in `.cursor/agents/` must stay a valid Cursor subagent: Markdown with YAML `name`, `description`, and `model` frontmatter, then the prompt body. Cursor loads every `*.md` in that folder, so mapping docs stay outside it.

Invoke a specialist with `/chaosx-repo-explorer` or by asking the parent to use that Task subagent. Use the hyphen-case Cursor name. Cursor's built-in `explore`, `shell`, and `browser` agents are not Chaos Redux specialists.

Regenerate Cursor subagents after any Codex TOML change:

Apply the active runtime's destination-write rules before running either generator, as described in the [synchronization guide](../.tools/sync/README.md).
If those rules conflict with regeneration, record blocked synchronization and retain both requirements pending an ownership decision.

```text
python .tools/sync/sync_cursor_agents.py
```

If Qoder is also in use, regenerate it in the same change with `python .tools/sync/sync_qoder_agents.py`.

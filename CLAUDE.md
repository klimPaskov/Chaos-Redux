@AGENTS.md

# Claude Code Runtime

`AGENTS.md` is the canonical project instruction file and it is imported above.
Do not duplicate its rules here.

`.mcp.json` in this repository root registers the same production MCP servers as
the other runtimes (`hoi4_agent_tools`, `meshy`, `blender_hoi4`). Claude Code
asks for approval the first time it loads a project-scoped server, so approve
them once and they stay available.

Project subagents are generated into `.claude/agents/` and repo skills are
linked into `.claude/skills/`. Both are generated output. Never hand-edit them:
change the canonical `.codex/agents/*.toml` file or the canonical
`.agents/skills/<name>/SKILL.md` file, then run the generator from the
repository root.

```text
python .tools/sync/sync_claude_agents.py
```

The generated name map is `.claude/agent-map.md`. Invoke a specialist by its
hyphen-case name (`chaosx-repo-explorer`) with the `Agent` tool. Claude Code
subagents always run in an isolated context window, so the parent prompt has to
carry every path, constraint, and prior decision the subagent needs.

## Anti-interference

`.codex/**` is the canonical subagent source. While a Claude Code session is
active, edit the TOML definitions and the skills, and leave the generated
runtime trees alone. Run the relevant generator instead of editing generated
output by hand.

- `.codex/agents/*.toml` and `.agents/skills/**` — canonical, edit these.
- `.claude/agents/*.md` and `.claude/skills/**` — generated, do not edit.
- `.qoder/**`, `.cursor/agents/**`, and `.opencode/agent/**` — generated output
  for the other runtimes. Regenerate them with their own sync scripts when a
  canonical change lands.

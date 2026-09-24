# Agent Runtime Layout

This repository is developed from several agent runtimes.
Codex is the primary workflow and the sole authoring source for shared instruction and subagent content, and the cross-runtime workflow rules live in [`.codex/README.md`](../.codex/README.md).
This file records the runtime-specific layouts that are not already covered there.

## DSH (DeepSeek Harness)

DSH needs no generated artifacts, because it reads this repository's canonical files directly.

| Surface | Path |
| --- | --- |
| Project instructions | `AGENTS.md`, plus `CLAUDE.md` as the generated copy of it when `sync_claude_agents.py` has written one, and `AGENTS.local.md` and `CLAUDE.local.md` overlays |
| Project skills | `.agents/skills/<name>/SKILL.md` |

`dsh-agent-instructions` loads the instruction chain from the project root down to the working directory.
It collapses sibling candidates whose trimmed content is byte-identical, so `CLAUDE.md` loads without duplicating `AGENTS.md`, and it does not interpret `@path` imports.

`dsh-skill-filesystem` discovers skills at the top level of each scanned root as either `<name>/SKILL.md` or `<name>.md`.
`name` must be kebab-case and must match the directory, and `description` is required.

### Skill root priority

The earlier rank wins when two roots provide the same skill name.

| Rank | Source | Path |
| --- | --- | --- |
| 100 | `project-dsh` | `<projectRoot>/.dsh/skills` |
| 200 | `project-agents` | `<projectRoot>/.agents/skills` |
| 300 | `custom` | Configured `customSkillDirs` |
| 400 | `user-dsh` | `$DSH_HOME/skills` |
| 500 | `user-agents` | `$DSH_AGENTS_HOME` or `~/.agents/skills` |

This repository leaves `.dsh/` absent so that `.agents/skills/` stays the single source for every runtime.
Create `.dsh/skills/<name>/SKILL.md` only for a skill that must exist for DSH and must not load in the other runtimes, and record why inside that skill.

### Subagents and model selection

DSH composes subagents at runtime through its delegation tool and loads no agent definition files.
There is therefore no DSH agent definition format, no DSH agent map, and no DSH generator.

The Codex model names in `.codex/agents/*.toml` do not apply here.
DSH does not read those files, so a named role does not arrive with the model it names in the TOML.
A DSH child agent runs on the deployment default from `dsh-agent-default-model`, or on the child options configured in the `dsh-tool-subagent` entry's `agentOptions`.
Neither is configured inside this repository, because that profile patch lives outside it.
The active profile does configure the child options, so a DSH subagent runs on DeepSeek regardless of the model its Codex TOML names.
No skill or role prompt chooses a child model: the runtime decides, and the parent therefore specifies none.
Where a runtime fixes its own child route, [`chaos-redux-subagents`](../.agents/skills/chaos-redux-subagents/SKILL.md) records that route.

The named Chaos Redux roles still apply as routing and ownership contracts.
The parent writes the role's boundaries into the delegation prompt, which is why every prompt must stay fully explicit and self-contained.
[`chaos-redux-subagents`](../.agents/skills/chaos-redux-subagents/SKILL.md) is the source of truth for routing, ownership, and this runtime's child model policy.

### MCP registration

DSH registers MCP servers in the active profile, not in this repository:

```text
$DSH_HOME/profiles/<profile>/cordis.patch.yml
```

That file is a top-level YAML array of loader entries applied after every bundle layer.
One server is one `@deepseek-ai/dsh-mcp-client` entry, and its tools appear as `mcp__<serverName>__<tool>`:

```yaml
- id: mcp-hoi4-agent-tools
  name: '@deepseek-ai/dsh-mcp-client'
  config:
    serverName: hoi4_agent_tools
    transport: stdio
    command: cmd.exe
    args: ['/d', '/c', 'hoi4-agent-tools.cmd']
    cwd: C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux
```

The production servers are `hoi4_agent_tools`, `meshy`, and `blender_hoi4`, and their wrappers live under `.tools/3d_pipeline/wrappers/`.
Because the patch layer is outside the repository, a checkout does not carry them and they must be registered per machine.

An MCP tool name that does not appear in a session means the server was never registered, and a configuration file for another runtime is not evidence that DSH has it.
`AGENTS.md` makes MCP use mandatory for focus, event, technology, doctrine, weighted-logic, scripted GUI, and map work, so an unregistered profile blocks that work rather than downgrading it to source-only review.

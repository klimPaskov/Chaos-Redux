# DSH project runtime

DeepSeek Harness (DSH) is the runtime that needs the least setup here, because it already reads this repository's canonical files.
There is no generator for DSH and no generated tree to keep in sync.
The shared instructions and the shared skills are the DSH configuration.

## What DSH reads from this repository

| Surface | Path | Notes |
| --- | --- | --- |
| Project instructions | `AGENTS.md` | Canonical. Loaded from the project root down to the working directory. |
| Claude Code notes | `CLAUDE.md` | Loaded alongside `AGENTS.md` as a sibling candidate. |
| Local overlays | `AGENTS.local.md`, `CLAUDE.local.md` | Additive, gitignored personal overlays. |
| Project skills | `.agents/skills/<name>/SKILL.md` | Shared with the other runtimes. |

`dsh-agent-instructions` loads the instruction chain broad to specific, and collapses sibling candidate files whose trimmed content is byte-identical.
It does not interpret `@path` imports, which is why `CLAUDE.md` is a real file rather than an import shim: DSH loads it directly and deduplicates it against `AGENTS.md` on its own.

`dsh-skill-filesystem` discovers project skills from `.agents/skills` and parses each `SKILL.md` frontmatter.
A skill is a `<name>/SKILL.md` directory bundle or a flat `<name>.md` file at the top level of a scanned root, so nested skill trees and package manifests are ignored.
`name` must be kebab-case and must match the directory, and `description` is required.

## Skill root priority

DSH scans several roots and the earlier rank wins when two roots provide the same skill name.

| Rank | Source | Path |
| --- | --- | --- |
| 100 | `project-dsh` | `<projectRoot>/.dsh/skills` |
| 200 | `project-agents` | `<projectRoot>/.agents/skills` |
| 300 | `custom` | Configured `customSkillDirs` |
| 400 | `user-dsh` | `$DSH_HOME/skills` |
| 500 | `user-agents` | `$DSH_AGENTS_HOME` or `~/.agents/skills` |

This repository deliberately leaves `.dsh/skills/` absent so that `.agents/skills/` stays the single source for every runtime and a skill cannot silently fork into two copies.
Create `.dsh/skills/<name>/SKILL.md` only for a skill that must exist for DSH and must not load in the other runtimes, and record why in the skill.

## Subagents

DSH composes subagents at runtime rather than loading them from definition files.
This repository has no DSH subagent file format to maintain, and the shared named roles are delivered by the [`chaos-redux-subagents`](../.agents/skills/chaos-redux-subagents/SKILL.md) skill instead.
Parent and subagent ownership boundaries, routing gates, and handoff requirements come from that skill.

## MCP registration

DSH registers MCP servers as loader entries in the active profile, not in this repository.

```text
$DSH_HOME/profiles/<profile>/cordis.patch.yml
```

The patch layer is a top-level YAML array of loader entries, applied after every bundle layer.
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

The production servers used by the other runtimes are `hoi4_agent_tools`, `meshy`, and `blender_hoi4`.
Their launch commands and environment match `.codex/config.toml`, `.cursor/mcp.json`, `.opencode/opencode.json`, and `../.mcp.json`, and the wrappers live under `.tools/3d_pipeline/wrappers/`.
Because the patch layer is outside the repository, a DSH session does not pick these servers up from a checkout and they have to be registered per machine.

Verify registration with `/mcp` in a DSH session rather than assuming it: an MCP tool name that does not appear means the server was never registered, and a checked-in configuration file for another runtime is not evidence that DSH has it.

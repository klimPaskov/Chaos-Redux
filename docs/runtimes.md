# Agent Runtime Layout

This repository is developed from several agent runtimes.
Claude Code is the primary workflow and the sole authoring source for subagent and skill content, and the cross-runtime workflow rules live in [`.codex/README.md`](../.codex/README.md).
This file records the runtime-specific layouts that are not already covered there.

## Read budgets

[`.tools/sync/read_limits.json`](../.tools/sync/read_limits.json) owns the 30,000-token reader/output target and the separate 20,000-token guidance-file ceiling.
The larger reader budget is headroom, not permission to enlarge skills.
Apply its supported settings with `python .tools/sync/sync_read_limits.py`; `--check` checks for drift without writing.
Add `--user-defaults` to update this user's Codex, Claude, and OpenCode defaults, or `--dsh-profile <existing cordis.patch.yml>` to update a specific DSH profile without starting it.
These settings are independent of the selected AI model/provider; they do not change model context windows, reply lengths, permissions, or retry limits.

| Runtime | Applied setting | Scope and limits |
| --- | --- | --- |
| Codex | `tool_output_token_limit = 30000` | Project and optional user config; preserves tool results in history. A call that explicitly requests less still needs a larger `max_output_tokens` for a full read. |
| Claude Code | `env.CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` and `env.MAX_MCP_OUTPUT_TOKENS`, both `30000` | Project and optional user `settings.json`. File reads and MCP results are separate limits; MCP character annotations or automatic result-file delivery can still apply. |
| OpenCode | `tool_output.max_bytes = 90000`, `max_lines = 6000` | Project and optional user config. This is a byte/line output allowance; the built-in Read tool's separate 50-KiB and per-line caps remain. Use an authorized shell full-file read for larger guidance. |
| DSH | `tool-fs.config.readMaxBytes = 90000`, `readLimit = 6000`, `readMaxLineLength = 90000` | Explicit existing profile override, preserving plugin enablement and unrelated entries. These are byte/line/character limits. |
| Cursor and Qoder | Shared AGENTS.md read policy | No supported global reader-size setting was found in the inspected configuration docs or installed setting registrations. Request the larger allowance where a tool exposes it; fixed client caps remain a limitation. |

The byte allowance uses the config's explicit three-bytes-per-token estimate; it is not an exact tokenizer conversion.

### Measured single-read capacity

Measured on 10 October 2026 with the Claude Code Read tool at `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS = 30000`, on concatenated repository skill prose.
A 122,715-byte file reported 40,539 tokens, which is 3.03 bytes per token for this prose, and the tool paginated at the 30,000-token cap instead of failing.
The paginated first page held 83,651 bytes, so one call reads about 83,000 to 90,000 bytes of skill text completely.
A 73,202-byte skill with a 2,041-character line was returned in one call without truncation, which is about 24,200 tokens.
The maximum reliable single read is therefore the 30,000-token cap, about 90,000 bytes of this prose.
The 20,000-token guidance ceiling is about 60,000 bytes, and root `SKILL.md` files stay under 58,000 bytes so that dense tables, line numbers, and code-heavy sections still read completely.
Skills that exceed the ceiling move coherent sections into linked `references/` files, and `python .tools/sync/sync_read_limits.py --check` lists any guidance file over its byte ceiling.
Read one large guidance file per result, keep smaller calls narrow, and inspect truncation markers and line/byte coverage before treating a read as complete.
New settings may require a new runtime session; writing them does not change every already-running reader.

Sources: [Codex configuration](https://developers.openai.com/codex/config-reference), [Claude environment variables](https://code.claude.com/docs/en/env-vars), [OpenCode output configuration](https://opencode.ai/v2/docs/config), [OpenCode Read implementation](https://github.com/anomalyco/opencode/blob/dev/packages/opencode/src/tool/read.ts), and [DSH filesystem configuration](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/fs/tool-fs#configuration).
The Claude file-read variable was also verified in the installed `2.1.288` executable; the installed OpenCode SDK `1.18.23` declares the `tool_output` fields.
[Cursor configuration](https://cursor.com/docs/cli/reference/configuration) and [Qoder configuration](https://docs.qoder.com/cli/settings) are the inspected public setting references.

## DSH (DeepSeek Harness)

DSH needs no generated artifacts, because it reads this repository's canonical files directly.

| Surface | Path |
| --- | --- |
| Project instructions | `AGENTS.md` and `CLAUDE.md`, plus `AGENTS.local.md` and `CLAUDE.local.md` overlays |
| Project skills | `.agents/skills/<name>/SKILL.md`, a generated junction to the canonical `.claude/skills/<name>/SKILL.md` |

`dsh-agent-instructions` loads the instruction chain from the project root down to the working directory.
It collapses sibling candidates whose trimmed content is byte-identical. `CLAUDE.md` and `AGENTS.md` now differ in their image-generation wording, so DSH loads both. It does not interpret `@path` imports.

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

The model names in the generated `.codex/agents/*.toml` files do not apply here.
DSH does not read those files, so a named role does not arrive with the model it names in the TOML.
A DSH child agent runs on the deployment default from `dsh-agent-default-model`, or on the child options configured in the `dsh-tool-subagent` entry's `agentOptions`.
Neither is configured inside this repository, because that profile patch lives outside it.
The active profile does configure the child options, so a DSH subagent runs on DeepSeek regardless of the model its Codex TOML names.
No skill or role prompt chooses a child model: the runtime decides, and the parent therefore specifies none.
Where a runtime fixes its own child route, [`chaos-redux-subagents`](../.claude/skills/chaos-redux-subagents/SKILL.md) records that route.

The named Chaos Redux roles still apply as routing and ownership contracts.
The parent writes the role's boundaries into the delegation prompt, which is why every prompt must stay fully explicit and self-contained.
[`chaos-redux-subagents`](../.claude/skills/chaos-redux-subagents/SKILL.md) is the source of truth for routing, ownership, and this runtime's child model policy.

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

An MCP tool absent from the session is unavailable there; another runtime's configuration does not prove DSH has it.
Do not infer the exact registration or startup failure without inspecting it.
Unavailable domain tools are verification limits under `AGENTS.md`; continue source implementation and local checks, carrying existing results and retry history into delegated or resumed work.
Profile repair is a separate task when requested.

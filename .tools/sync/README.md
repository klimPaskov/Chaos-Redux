# Agent synchronizers

This directory holds the maintained one-way generator that projects the canonical Claude Code definitions into the other runtimes, plus the shared read-limit applier.

Claude Code is the primary development environment.
The canonical sources are:

- `.claude/agents/<kebab-name>.md` for subagents, with `name`, `description`, `model` (`haiku`, `sonnet`, or `opus`), and `effort` (`low`, `medium`, `high`, `xhigh`, or `max`) frontmatter and a runtime-neutral prompt body. `effort` is the Claude Code subagent field that overrides the session reasoning effort for that subagent; `CLAUDE_CODE_EFFORT_LEVEL` still takes precedence, and the available levels depend on the model.
- `.claude/skills/<name>/` for skills, including their `references/`, `assets/`, `tools/`, and `templates/`.
- `CLAUDE.md` for the Claude Code project instructions.

Everything else is generated or maintained per runtime, and none of it is a second authoring source.

```powershell
python .tools/sync/sync_agents.py                 # every target
python .tools/sync/sync_agents.py codex skills    # selected targets
python .tools/sync/sync_agents.py --verify        # read the outputs back and compare with the routing policy
python .tools/sync/sync_read_limits.py --check    # reader and output budgets
```

## What each target writes

| Target | Writes | Destination | Tracked |
| --- | --- | --- | --- |
| `claude-map` | Subagent map derived from the canonical frontmatter | `.claude/agent-map.md` | yes |
| `codex` | Codex subagent TOMLs with the tier-mapped model and the definition's effort as `model_reasoning_effort` | `.codex/agents/*.toml` | no |
| `qoder` | Qoder subagents with a tool list derived from the authority class | `.qoder/agents/*.md` | no |
| `cursor` | Cursor subagents and agent map | `.cursor/agents/*.md`, `.cursor/agent-map.md` | no |
| `opencode` | opencode subagents and agent map | `.opencode/agent/*.md`, `.opencode/agent-map.md` | no |
| `skills` | Shared skill root: a junction (or copy) per skill | `.agents/skills/<name>` to `.claude/skills/<name>` | no |

`.agents/skills/` is the shared skill root read by Codex, DSH, and opencode.
It is a mirror, so `.agents/skills/<name>/SKILL.md` and `.claude/skills/<name>/SKILL.md` are the same file.
A new skill is created under `.claude/skills/<name>/` and the `skills` target links it.
After a fresh clone, run `python .tools/sync/sync_agents.py` once to create every ignored runtime artifact.
Pass `--mode copy` to copy skills instead of linking them, for a machine or archive where junctions are unavailable.
A refused junction degrades to a copy and the run reports it.

## Runtime-specific facts

`agent_profiles.json` holds what a single runtime needs and the canonical Markdown cannot carry:

- `tier_policy` is the model routing table: Opus for the improvement loop planner; Sonnet for the 3D model pipeline, event completion auditor, localisation auditor, scripted system architect, and skill maintainer; Haiku for every other specialist.
  `--verify` fails when a canonical definition drifts from it.
- `effort_policy` is the reasoning effort table: `high` for the auditors that judge correctness (AI probability, country package, decision and mission, focus tree, event completion, localisation), the 3D model pipeline, the scripted system architect, and the improvement loop planner; `medium` for every other role, including researchers, art, icon and portrait workers, the explorer, the spreadsheet and documentation workers, the skill maintainer, and the equipment and units, technology tree, and map and states workers.
  `--verify` fails when a canonical definition's `effort` differs from it.
  `codex_effort` maps the field to Codex `model_reasoning_effort`; Cursor, Qoder, and opencode have no verified equivalent in this setup, so the field is dropped there.
- `tiers` maps each Claude tier to the model field of the other runtimes.
  Codex pins a model.
  Cursor receives `fast` for Haiku and `inherit` otherwise.
  opencode receives `inherit`, because no Anthropic model identifier is verified for it in this repository.
  Qoder subagents have no model field.
- `agents` holds each role's authority class (read-only, patch-capable, or asset and research) and the Codex nickname candidates.

A new subagent needs its `.claude/agents/<name>.md` definition and one `agents` entry in the profile.
The generator stops on a definition without an entry or with a model outside `haiku`, `sonnet`, and `opus`.

## Instruction files

`CLAUDE.md` is canonical for Claude Code and is edited directly.
`AGENTS.md` serves Codex, Cursor, Qoder, opencode, and DSH, and keeps the Codex wording for image generation.
The two files share their structure, so apply a rule change to both and keep only the runtime-specific image-generation wording different.

## Write rules

Before running a generator, check the active runtime's destination-write rules in [`.codex/README.md`](../../.codex/README.md#anti-interference-and-instruction-changes).
Generated agent folders accept only agent files, because Cursor, opencode, Qoder, and Claude Code load every Markdown file in them.

## Verification

The generator is idempotent, so a second run must report `0 created, 0 updated` for every agent target and only unchanged skill links.
A stale output without a canonical source is reported and left in place, never deleted, so a renamed agent shows up as a stale-file warning until the parent removes it deliberately.

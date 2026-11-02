# Agent synchronizers

This directory holds the maintained one-way generators that project the canonical Claude Code definitions and instructions into the other runtimes, plus the shared read-limit applier.

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
python .tools/sync/sync_agents.py --check         # render every output in memory and report the stale ones
python .tools/sync/sync_read_limits.py --check    # reader and output budgets
python .tools/sync/generators.py                  # run every registered generator
python .tools/sync/generators.py --check          # report stale outputs, write nothing
```

## Registry and hook

`generators.json` lists every generator and generated-file check in the repository: the AGENTS.md projection, the agent definitions, the read limits and the size check, the event catalog CSV exports, the formable state puzzle runtime and the Event 016 transit catalog. `generators.py` is a byte-identical copy of the Agentic HOI4 Modding Kit's runner. It runs the entries a change affects, and `check.py` uses it for the `generators` check.

The `PostToolUse` hook in `.claude/settings.json` runs it after every Edit or Write. An edit to a canonical file regenerates its outputs and names them, so they are committed with it. An edit to a generated file is reported with the canonical file to edit instead, and any other edit starts nothing. Deny rules in the same file stop the edit tools from writing the tracked generated files. `.tools/py.sh` finds a working Python for the hook. Add a new generator as a `generators.json` entry, not as a hard-coded list.

The `codex` target also keeps the `[agents.*]` rows of `.codex/config.toml` in step with `.claude/agents/`, because Codex finds a custom agent through its row. `--verify` reports a missing or stale row.

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

`CLAUDE.md` is canonical and is the only instruction file edited by hand.
`AGENTS.md` serves Codex, Cursor, Qoder, opencode, and DSH; `sync_instructions.py` generates it from `CLAUDE.md`, replacing each runtime-specific line listed in `instruction_projection.json` (the Codex wording for image generation and portraits, the `.agents/skills` mirror sentence, and the Linux live-testing route).

```powershell
python .tools/sync/sync_instructions.py           # regenerate AGENTS.md after editing CLAUDE.md
python .tools/sync/sync_instructions.py --check   # exit 1 on drift or on a replacement whose source line no longer exists
```

When a replaced line in `CLAUDE.md` is reworded, update its pair in `instruction_projection.json` in the same change; `--check` reports the stale pair. `.tools/check.py` runs the check whenever `CLAUDE.md`, `AGENTS.md` or this folder changes.

## Engine-system skills

`chaos-redux-ai-strategies`, `chaos-redux-characters-leaders`, `chaos-redux-diplomacy-war`, `chaos-redux-equipment`, `chaos-redux-ideas-modifiers`, `hoi4-imagegen` (kept under its kit name, which is also its MCP command), `chaos-redux-investigate`, `chaos-redux-map-states`, `chaos-redux-mtth`, `chaos-redux-technology-doctrines` and `chaos-redux-units-divisions` are generated, so `.claude/skills/<name>/` is not an authoring location for them.
Each is the Agentic HOI4 Modding Kit's skill text, pinned in `.tools/kit_skills/<kit-name>/`, with the names in `.tools/kit_skills/mapping.json` replaced (kit skill names, `hoi4_*` agent routing names), plus the Chaos Redux overlay in `.claude/skill-overlays/<name>/`.
`.tools/kit_skills/manifest.json` records the kit commit and the SHA-256 of every snapshot file, and the generator refuses a snapshot that differs from it.

```powershell
python .tools/sync/sync_engine_skills.py                              # write every generated skill
python .tools/sync/sync_engine_skills.py --check                      # print "Would update <path>" for each stale or extra file, write nothing
python .tools/sync/sync_engine_skills.py --skill chaos-redux-mtth     # one skill (repeatable)
python .tools/sync/refresh_kit_skills.py --kit <kit repository> --commit <revision>   # pin a new kit commit, then run the generator
```

- A generated `SKILL.md` is the Chaos Redux frontmatter (`name`, and the `description` from `overlay.md`), a provenance comment, the mapped kit body and a `## Chaos Redux` section holding the body of `overlay.md`. Every other file of the folder is the mapped kit file or a file of the overlay folder (`references/...`), which is where a Chaos Redux-only reference file lives.
- Edit the overlay, never the generated folder: a hand edit fails `--check` and the generators hook, and the next run overwrites it. Group overlay lines under `### In <original section>` headings, and mark a line that restates a kit line in other words with `(Chaos Redux wording differs from the kit)` until the maintainer settles which wording stays.
- A rule that every mod needs belongs in the kit. Remove its overlay line after the snapshot is refreshed from the kit commit that carries it.
- A generated `SKILL.md` must stay at or below `root_skill_max_bytes` of `read_limits.json`. When it would not, the generator exits 2 without writing: move a complete overlay topic into an overlay reference file and link it from `overlay.md`.
- Exit codes: 0 in sync, 1 drift, 2 the generator cannot run (invalid mapping, overlay or snapshot, unknown `--skill`, oversized `SKILL.md`). Only files under the generated skill folders that no source produces are deleted.

## Wiki snapshot

`hoi4_wiki/` is the kit's snapshot, copied whole from one kit commit. `.tools/kit_wiki.json` records the commit and the SHA-256 of every file (text with LF endings), and the `kit_wiki` check in the registry reports a changed, missing or extra file as `DRIFT`. Wiki corrections are made in the kit; then take its newer snapshot here. `--freshness` is the reminder to do so: `check.py` reports a snapshot that is behind as a `WIKI-BEHIND` warning with the refresh command, and never as an error.

```powershell
python .tools/sync/kit_wiki.py                                                    # check; exit 1 on drift
python .tools/sync/kit_wiki.py --freshness [--kit <kit repository>]               # BEHIND, CURRENT or UNKNOWN against the kit's newest wiki; always exit 0
python .tools/sync/kit_wiki.py --refresh --kit <kit repository> --commit <revision>   # copy hoi4_wiki/ from the kit commit and record it
```

## Write rules

Before running a generator, check the active runtime's destination-write rules in [`.codex/README.md`](../../.codex/README.md#anti-interference-and-instruction-changes).
Generated agent folders accept only agent files, because Cursor, opencode, Qoder, and Claude Code load every Markdown file in them.

## Verification

The generator is idempotent, so a second run must report `0 created, 0 updated` for every agent target and only unchanged skill links.
A stale output without a canonical source is reported and left in place, never deleted, so a renamed agent shows up as a stale-file warning until the parent removes it deliberately.

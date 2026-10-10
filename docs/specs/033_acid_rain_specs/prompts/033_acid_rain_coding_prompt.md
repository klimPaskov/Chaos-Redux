# Event 033 Acid Rain implementation resume prompt

Event 033 is implemented in source.
This prompt is a resume handoff for the remaining work; the requirements it relies on live in their owning parts and are not restated here.

## Before editing

1. Read the package README: implementation status, reading authority, invariants and open questions.
2. Read [the runtime resume](../../../plans/033_acid_rain_plans/runtime_resume_2026_10_08.md), [the agent decision log](../../../plans/033_acid_rain_plans/agent_decisions_2026-10-04.md) and the newest handoffs under `docs/plans/033_acid_rain_plans/subagent_handoffs/`.
3. Read the current source listed in `implementation_readiness/033_acid_rain_file_map_and_migration.md`, including other sessions' uncommitted edits.
4. Use [the events skill](../../../../.claude/skills/chaos-redux-events/SKILL.md), [the decisions skill](../../../../.claude/skills/chaos-redux-decisions-missions/SKILL.md), [the scripted GUI skill](../../../../.claude/skills/chaos-redux-scripted-gui/SKILL.md) and [the subagent skill](../../../../.claude/skills/chaos-redux-subagents/SKILL.md) for their surfaces, and the HOI4 reference workflow in `CLAUDE.md` for syntax.

## Ownership

- The parent owns gameplay, wiring, shared registries, Event Details, the event log, settings and the super-event framework.
- `chaosx_event_ui_worker` owns only the dedicated `acid_rain_world_window` and `acid_rain_category_inlay` layout, under the scripted GUI skill.
- `chaosx_ai_probability_auditor` runs the Part 8 probability workflow read-only; preserve the before source of any weighted change for its comparison.
- Asset production follows [the asset prompt](033_acid_rain_asset_prompt.md).

## Remaining work

The goal prompt lists the remaining items in order.
Changes that come from an accepted open question update the owning spec part, the event overview and, for catalog-visible wording, the workbook before its exports.

## Completion blockers

Completion is blocked by any violated README invariant, any accepted requirement left unimplemented, any Part 12 gate without agent evidence, a free or stale AI action, a missing or unregistered sprite, an unverified audio or quote right, stale catalog data, or an unreviewed specialist finding.
User live checks are listed as pending verification and never reported as passed.

# Skill Maintainer Handoff

Status: complete for the reusable-workflow gate; no gameplay, localisation, asset, spreadsheet, spec, or generated Qoder file was edited.

## Audit performed

- Read `AGENTS.md`, `.agents\skills\chaos-redux-subagents\SKILL.md`, and `docs\specs\famine_and_migration_system_specs\subagent_prompts\13_skill_maintainer.md`.
- Audited `.agents\skills\chaos-redux-events\SKILL.md`, `.agents\skills\chaos-redux-decisions-missions\SKILL.md`, and `.agents\skills\chaos-redux-subagents\SKILL.md` for existing transfer, ledger, cohort, registry, reception, projection, mapmode, scope, and handoff guidance.
- Reviewed the current scripted-system implementation and handoffs in `common\script_constants\`, `common\scripted_triggers\`, `common\scripted_effects\`, `common\map_modes\`, `common\scripted_localisation\`, `common\on_actions\`, `docs\plans\famine_and_migration_system_plans\subagent_handoffs\scripted_system_architect.md`, and `docs\plans\famine_and_migration_system_plans\mapmode_validation.md`.
- Consulted the required offline wiki pages and installed vanilla documentation for state population, manpower scope, arrays, event targets, bounded loops, on-action scopes, script constants, and scripted mapmode layers.

## Skill decision

The closest existing skills cover event/decision ownership and formable state-puzzle presentation, but none captures the cross-system population-ledger contract established by this implementation. A distinct reusable skill was warranted.

## Skill changed

- Created `.agents\skills\chaos-redux-state-ledgers\SKILL.md`.

The skill deliberately contains no famine-specific identifiers, historical profiles, event ids, decision ids, one-off balance values, or private implementation history. It captures generic exact-transfer conservation, scoped destination targets, temporary-variable and scope hazards, sparse aligned cohort arrays, state-plus-country reception accounting, transaction-time map projections, privacy, no-double-counting proof, validation scenarios, and parent handoff requirements.

## Validation

- `python -X utf8 C:\Users\klimp\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\chaos-redux-state-ledgers` returned `Skill is valid!`.
- The initial validator invocation without UTF-8 mode failed only because Windows Python opened the UTF-8 file with the console code page; the UTF-8-mode rerun passed.
- No gameplay or live-game validation was run because this task changes reusable instructions only.

## Routing and follow-up

No `AGENTS.md`, `.codex\agents\`, `.qoder\agents\`, or existing owner-skill routing change was needed. Parent review should decide whether future owner prompts should name `chaos-redux-state-ledgers` explicitly when a task includes exact population transfer or state projection work.

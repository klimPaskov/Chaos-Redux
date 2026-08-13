# Localisation audit prompt for Event 016 Brilliant Scientist

Use the binding origin-conclusion and visible-state contracts from `016_source_of_truth_map.md`.

Spawn `chaosx_localisation_auditor` with `fork_context=false` after a substantial implementation tranche and again before completion.

Read:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_brilliant_scientist_spec_part_9_assets_animation_and_localisation.md`
- Current Event 16 implementation, scripted localisation, Event Details, event log, super-event, achievement, focus, decision, country, and GUI text

## Audit scope

Check:

- Missing and duplicate keys.
- Wrong namespaces and UTF-8 BOM issues.
- Broken scripted localisation and dynamic actor references.
- Consistency of `Doctor Warren Kruger` across advisor, scientist, leader, event, GUI, project, and country surfaces.
- Host, recipient, former-host, laboratory-state, foreign-actor, project-family, route, country-name, and singularity-stage dynamic text.
- Value formatting for visible Mandate, Dependence, Exposure, Project Capacity, and status breakdowns. Do not expose exact Independent Capacity or Grievance arithmetic.
- Custom trigger tooltips for project, facility, security, formation, and disarmament requirements.
- Icon-first costs and readable long-requirement summaries.
- Route-specific tone for human, clone, machine, temporal, paleogenetic, xenobiological, extraterrestrial-provenance, and synthesis content.
- Hidden route and variable spoilers.
- Early alien-origin overstatement.
- Contradictions among extraterrestrial provenance, temporal displacement, manufactured continuity, and unresolved origin; later transformation must not be written as alien proof.
- Event Details and workbook mirror text containing mechanical effects.
- Cross-surface mismatch between events, decisions, focuses, GUI, super-events, achievements, docs, and catalog.
- Unresearched working labels, quotes, remarks, slogans, or audio titles copied into final super-event localisation.

## Writing rules

Patch small local issues directly.

Preserve:

- No em dash.
- No semicolons in sentences.
- No staccato drama.
- No thesis-antithesis-synthesis formulas.
- No staged official-denial contrast formulas.
- No generic apocalypse filler.
- No implementation-history language.
- No achievement advertising in ordinary event, decision, or focus text.
- No effect lists in Event Details.

Kruger should sound precise, dry, impatient with institutions, and increasingly possessive. He should not become a generic cackling villain.

## Required output

- Missing-key list.
- Duplicate-key list.
- Scripted-localisation issue list.
- Dynamic text opportunities.
- Cross-surface mismatch list.
- Changed files and keys if patched.
- Before and after behavior.
- Task-specific validation.
- Unresolved wording or research gates.

Write a handoff under `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/`. If a text problem reveals a missing mechanic, write a plan instead of inventing the mechanic in localisation.

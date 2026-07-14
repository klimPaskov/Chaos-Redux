# Event 016 subagent routing plan

All project custom subagents must be spawned with `fork_context=false`. Each prompt must carry the event ID, slug, package paths, user constraints, accepted design rules, current implementation state, and every prior handoff needed by that role.

The parent remains responsible for integration, source-of-truth decisions, validation, plan disposition, and completion claims.

## Planning closure

The improvement-loop planner and documentation-curator passes are complete. Their result and parent dispositions are recorded in `docs/plans/016_brilliant_scientist_plans/016_source_of_truth_map.md`. Do not rerun either pass before implementation creates new evidence. The exact current continuation state is `docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_resume_packet.md`.

## Architecture and implementation preparation

### 1. Scripted-system architect

Before broad implementation, spawn `chaosx_scripted_system_architect` with:

`prompts/016_brilliant_scientist_scripted_system_architect_prompt.md`

Priority outputs are the unique Kruger ownership lifecycle, transfer and cleanup helpers, Directorate values, project-history state, evolution logging context, project-derived rebellion package, dynamic cost helpers, and shared tuning plan. Small reusable helpers may be patched only when implementation has begun and direct call sites are available.

### 2. Repo explorer only when uncertainty remains

`chaosx_repo_explorer` is not a ritual preflight. Use it only if the implementation parent still lacks exact file locations, a vanilla precedent, special-project field support, animated portrait wiring precedent, country-tag safety, or a reusable event-log pattern. Pass a bounded search question and a report path under `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/`.

## Gameplay implementation tranches

### 5. Host event and Directorate tranche

The parent implements the opening event, unique character, appointment and transfer choices, advisor package, scientist package, host values, facilities, and baseline decisions.

After the tranche, spawn:

- `chaosx_decision_mission_auditor` using `prompts/016_brilliant_scientist_decision_mission_prompt.md`
- `chaosx_localisation_auditor` using `prompts/016_brilliant_scientist_localisation_auditor_prompt.md`

### 6. Project and evolution tranche

The parent implements conventional and impossible projects, project history, evolved openings, four evolution milestones, foreign action hooks, security incidents, and containment routes.

Run the decision and localisation auditors again only for new surfaces. Use the scripted-system architect when repeated project or evolution logic should become a helper.

### 7. Kruger State tranche

The parent implements country creation, viable territory selection, project-derived forces, leaders, ideas, production, technologies, decisions, AI, and the large focus tree.

After the tranche, spawn:

- `chaosx_country_package_auditor` using `prompts/016_brilliant_scientist_country_focus_prompt.md`
- `chaosx_focus_tree_auditor` with the same package paths and a focus-specific audit request
- `chaosx_decision_mission_auditor` for Kruger State decisions, missions, costs, cleanup, and exploits
- `chaosx_localisation_auditor` for country, leader, focus, decision, and dynamic-text coverage

## Asset and presentation production

### 8. Generated non-icon art

Spawn `chaosx_generated_event_art` for fictional portraits, report and news scenes, super-event images, Kruger State flag concepts, faction emblems, and Directorate panel art. Use:

`prompts/016_brilliant_scientist_asset_prompt.md`

Kruger is fictional, so generated later-stage portrait work is appropriate. Stage 0 is already complete from the exact approved `portrait_generic_biowarfare_europe_male_01` base and must not be recreated. Use its preserved source and registered runtime sprites to maintain identity.

### 9. Icon and frame-animation work

Spawn `chaosx_icon_artist` for focus, idea, decision, category, achievement, technology, warning, project-family, and route-state icons. Animated icon work must also follow:

`prompts/016_brilliant_scientist_animation_prompt.md`

Every final animation requires separate source frames, processed frames, a frame sheet, DDS outputs, a static fallback, preview GIF, contact sheet, manifest, and GFX handoff.

### 10. Sourced visual research

Use `chaosx_asset_source_researcher` only where the final asset must depict real historical scientific institutions, real wartime laboratories, real documents, or an archival object. Do not use it for Kruger or invented project imagery.

### 11. Super-event research

Spawn separately:

- `chaosx_super_event_text_researcher` for quotes, attribution, title and remark research
- `chaosx_super_event_audio_researcher` for unique licensed music, source verification, conversion, and documentation

Use `prompts/016_brilliant_scientist_super_event_prompt.md`. Six-package title, button, quotation, and audio research is complete. Six final Event 016-owned OGGs are ready at IDs `90` through `95`. Images, final descriptions, localisation, shared music and sound definitions, settings-aware playback, and live presentation wiring remain blocked until their dedicated handoffs and implementation exist.

## Documentation, catalog, and final audit

### 10. Achievement implementation and audit

Use `prompts/016_brilliant_scientist_achievement_prompt.md`. Implement exactly seventeen working achievements. `public_method` and `clean_break` remain separate.

### 13. Documentation curation

After implementation handoffs accumulate, rerun `chaosx_documentation_curator` to record plan dispositions, current implementation state, asset status, and remaining blockers.

### 14. Spreadsheet catalog

Only after final in-game wording exists, spawn `chaosx_spreadsheet_doc_worker` with:

`prompts/016_brilliant_scientist_spreadsheet_prompt.md`

It owns only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`. Event details and evolution details must mirror final in-game wording. It should also record that Event 16 has no cluster and that the duplicate `Crazy Scientist` concept is retired or absorbed.

### 15. Completion audit

Spawn `chaosx_event_completion_auditor` with:

`prompts/016_brilliant_scientist_completion_auditor_prompt.md`

The audit must compare every spec, accepted addendum, plan disposition, gameplay surface, AI path, asset package, super-event, achievement, document, and spreadsheet field. It must separate complete, partial, blocked, simplified, and unvalidated work.

## Conditional skill maintenance

Use `chaosx_skill_maintainer` only if implementation reveals a reusable project workflow or repeated error that the existing skills do not cover. Event-specific Kruger rules belong in the specs and implementation docs, not in a reusable skill.

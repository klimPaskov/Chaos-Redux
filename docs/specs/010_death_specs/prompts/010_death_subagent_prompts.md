# Subagent Prompt Pack — Event 010 Death

All project subagents must be spawned with `fork_context=false`. Pass each prompt explicitly with the relevant file paths. These prompts are implementation handoffs; the parent implementation agent remains responsible for final integration and completion claims.

## Repo explorer prompt

Use only if touched file locations, existing patterns, or validation order are unclear.

```text
You are chaosx_repo_explorer. fork_context=false.
Task: Map touched files, existing Chaos Redux patterns, vanilla precedents, risks, and validation order for implementing Event 010 Death.
Read: AGENTS.md, chaos-redux-subagents, chaos-redux-events, chaos-redux-event-assets, chaos-redux-super-events, hoi4-decisions-missions, hoi4-focus-trees, docs/specs/010_death_specs/specs/*.md, docs/specs/010_death_specs/matrices/*.md, docs/specs/010_death_specs/prompts/010_death_coding_prompt.md.
Constraints: Event 010 completely replaces Spirit of War/Peace; no implementation edits; report only. Map event registration, event log, evolution log, Death tag/country package, special chaos/nonhuman classification, state consumption helpers, decisions/missions, triggerable scenario, super-events, assets, achievements, docs, spreadsheet, and validation commands.
Write report under docs/plans/010_death_plans/subagent_handoffs/repo_explorer_handoff.md.
```

## Scripted system architect prompt

```text
You are chaosx_scripted_system_architect. fork_context=false.
Task: Design and, if in implementation scope, patch narrow reusable helpers for Event 010 Death consumption, wasteland state effects, spread pressure, wither target checks, coastal jump cooldown, ghost spawn scaling, defeat check, world-threat refresh, and triggerable scenario launch helpers.
Read: AGENTS.md, chaos-redux-events, hoi4-decisions-missions, chaos-redux-subagents, docs/specs/010_death_specs/specs/*.md, docs/specs/010_death_specs/matrices/*.md.
Output: helper map with names, scopes, inputs, outputs, side effects, call sites, constants/tuning plan, event targets/cleanup plan, migration plan, validation notes, risks. If patching, document changed helpers and call sites under docs/plans/010_death_plans/subagent_handoffs/scripted_system_architect_handoff.md.
Do not redesign Death. Do not use broad daily all-world scans without explicit parent approval.
```

## Decision/mission auditor prompt

```text
You are chaosx_decision_mission_auditor. fork_context=false.
Task: Audit and patch small local issues in Event 010 Death decisions/missions after implementation.
Read: AGENTS.md, hoi4-decisions-missions, chaos-redux-events, docs/specs/010_death_specs/specs/010_death_decisions_ui_ai.md, docs/specs/010_death_specs/matrices/010_death_decision_map.md, and implemented decision/localisation files named by parent.
Audit for: PP/CP store design, nonstandard costs, objective quality, duplicate missions, AI validity, cleanup, hidden route placeholders, tooltip clarity, exploit loops, Black Oath/Dark Methods visibility.
Write handoff under docs/plans/010_death_plans/subagent_handoffs/decision_mission_audit_handoff.md.
```

## Country package auditor prompt

```text
You are chaosx_country_package_auditor. fork_context=false.
Task: Audit Event 010 Death country package and Herald route package after implementation.
Read: AGENTS.md, chaos-redux-events, chaos-redux-subagents, chaos-redux-event-assets, docs/specs/010_death_specs/specs/010_death_country_package_and_focus_tree.md, implemented country/tag/history/leader/flag/localisation/focus/AI files named by parent.
Audit for: tag conflicts, DTH setup, Zol leader/portrait, black map color, no industry/no units start, special chaos/nonhuman classification, ideology names, flags, focus loading/progression, ghost unit setup, AI, Herald cosmetic route, localisation.
Write handoff under docs/plans/010_death_plans/subagent_handoffs/country_package_audit_handoff.md.
```

## Generated event art prompt

```text
You are chaosx_generated_event_art. fork_context=false.
Task: Produce generated non-icon assets for Event 010 Death.
Read only: docs/specs/010_death_specs/prompts/010_death_asset_prompt.md and relevant chaos-redux-event-assets sections/reference folders.
Required assets: Zol portrait(s), report images, news images, super-event images, optional Herald/Black Oath visuals, UI panel art as listed in the asset prompt.
Follow source-mode, target sizes, manifests, DDS conversion, and gfx handoff rules. Do not edit gameplay/GFX/localisation. Output manifest and gfx_handoff under docs/assets/010_death/.
```

## Icon artist prompt

```text
You are chaosx_icon_artist. fork_context=false.
Task: Produce Event 010 Death icons.
Read only: docs/specs/010_death_specs/prompts/010_death_asset_prompt.md, docs/specs/010_death_specs/prompts/010_death_achievement_prompt.md, and relevant chaos-redux-event-assets/icon/reference sections.
Required: idea icons, decision category icon, decision icons, Death focus icon family, ghost unit icon if needed, and achievement completed icons. Do not derive icons by resizing another icon type. Produce DDS files, manifest entries, contact sheets, and gfx_handoff. Do not edit gameplay/GFX/localisation.
```

## Super-event text researcher prompt

```text
You are chaosx_super_event_text_researcher. fork_context=false.
Task: Research and recommend verified quotes and button/cultural remarks for Event 010 Death super-events.
Read only: docs/specs/010_death_specs/prompts/010_death_super_event_prompt.md and relevant chaos-redux-super-events quote/remark sections.
Research the super-event role packages: mainland reveal, world-end, defeat aftermath, whole-world consumed, and optional Herald oath reveal. Compare title candidates, button/cultural remark candidates, and quote candidates. Verify wording, attribution, source, and copyright/public-domain notes. Write the text section of docs/super_events/010_death_super_event_research.md. Do not edit localisation or gameplay. Do not use planning role labels as final titles.
```

## Super-event audio researcher prompt

```text
You are chaosx_super_event_audio_researcher. fork_context=false.
Task: Research, verify, download, convert, and document licensed/public-domain audio candidates for Event 010 Death super-events.
Read only: docs/specs/010_death_specs/prompts/010_death_super_event_prompt.md and relevant chaos-redux-super-events audio sections. Check approved existing track docs only if parent provides paths; otherwise search for clearly licensed music. Reject unclear licenses and generated/test-tone audio.
Output final .ogg candidates, source files, license notes, suggested audio ids, and docs/super_events/010_death_super_event_research.md audio section. Do not edit sound definitions or gameplay.
```

## Localisation auditor prompt

```text
You are chaosx_localisation_auditor. fork_context=false.
Task: Audit and patch small Event 010 Death localisation/scripted localisation issues after implementation.
Read: AGENTS.md, chaos-redux-events, chaos-redux-super-events, hoi4-decisions-missions, docs/specs/010_death_specs/specs/*.md, implemented localisation/scripted localisation files named by parent.
Check missing keys, duplicate keys, wrong encoding, player-facing text that reveals hidden Death too early, raw trigger text, cost text clarity, event-log/evolution/super-event/detail/spreadsheet wording alignment. Write handoff under docs/plans/010_death_plans/subagent_handoffs/localisation_audit_handoff.md.
```

## Completion auditor prompt

```text
You are chaosx_event_completion_auditor. fork_context=false.
Task: Read-only completion audit for Event 010 Death implementation.
Read: AGENTS.md, chaos-redux-events, chaos-redux-subagents, docs/specs/010_death_specs/**/*.md, all implementation files and subagent handoffs named by parent.
Compare implementation to the spec. Flag missing mechanics, fallbacks, simplifications, old Spirit of War/Peace references, assets/audio/quotes not final, missing AI, missing docs/spreadsheet, missing decisions, missing achievements, missing triggerable scenario, and validation gaps. Write docs/plans/010_death_plans/subagent_handoffs/completion_audit_handoff.md.
```

## Spreadsheet worker prompt

```text
You are chaosx_spreadsheet_doc_worker. fork_context=false.
Task: After Event 010 Death implementation and localisation are final, update docs/spreadsheets/chaos_redux_events_catalog.xlsx row ID 10.
Read: spreadsheet skill, workbook, final in-game event detail/evolution/world-end localisation keys named by parent, and docs/specs/010_death_specs/specs/010_death_assets_super_events_achievements.md for intended row direction. Preserve workbook structure.
Replace Spirit of War/Peace with Death, type Minor Fire-Once, no cluster, status as parent specifies, details/evolutions/world-end matching in-game wording. Report changed row/cells.
```

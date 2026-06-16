# Subagent Routing Prompt Pack — Event 013 Natural Disasters

Every project subagent must be spawned with `fork_context=false`. Pass the full relevant paths and the task constraints explicitly. This file is a routing handoff for the implementation agent; it is not a claim that subagents have already patched files.

## Scripted system architect

Spawn `chaosx_scripted_system_architect` with:

- Event ID 13, slug `natural_disasters`.
- Read `AGENTS.md`, `chaos-redux-events`, `hoi4-decisions-missions`, and the spec pack.
- Design or implement reusable helpers for target scoring, family selection, impact application, burst queues, evolution logging, recovery context, manual scenario context, Event 46 cleanup, constants, event targets, and cleanup.
- Output helper map, constants plan, event target cleanup plan, changed files if patched, and validation.

## Decision/mission auditor

Spawn `chaosx_decision_mission_auditor` after the Disaster Response Office category exists.

Audit costs, missions, visible target names, dynamic resource requirements, AI weights, clutter control, duplicate mission risk, cleanup, and exploit loops. Patch only small local decision/localisation/helper call issues inside scope.

## Localisation auditor

Spawn `chaosx_localisation_auditor` after broad visible text exists.

Audit event names, event details, evolution detail, history rows, cluster text, scenario text, decision and mission text, dynamic state/region names, missing keys, duplicate keys, encoding, and hidden-spoiler risks. Patch small local text issues.

## Asset agents

Spawn `chaosx_icon_artist` for decision/category/idea/achievement icons and small animated UI markers.  
Spawn `chaosx_generated_event_art` for generated report/news/super-event images and Disaster Ledger UI panel art.  
Spawn `chaosx_asset_source_researcher` only if implementation chooses archival real disaster images rather than generated documentary scenes.

All asset prompts must point to `prompts/013_natural_disasters_asset_prompt.md` and require manifests plus `gfx_handoff.md`.

## Super-event researchers

Spawn `chaosx_super_event_text_researcher` for final Evolution IV title/quote/button/cultural remark research gates.  
Spawn `chaosx_super_event_audio_researcher` for unique final audio if the Evolution IV super-event is implemented.

Both must write research notes and not edit gameplay/localisation directly.

## Spreadsheet worker

Spawn `chaosx_spreadsheet_doc_worker` only after final in-game localisation/scripted localisation exists. Update only `docs/spreadsheets/chaos_redux_events_catalog.xlsx`, preserving workbook structure and matching in-game wording.

## Completion auditor

Spawn `chaosx_event_completion_auditor` before the implementation is called complete. Compare spec, accepted plans, implementation, assets, docs, scenario, Event 46 placeholder disposition, localisation, decisions, AI, and spreadsheet handoff.

## Negative-scope subagents

Do not spawn focus-tree or country-package auditors unless implementation unexpectedly creates focus trees, countries, formables, or country identity changes. This spec deliberately does not create countries or focus trees.

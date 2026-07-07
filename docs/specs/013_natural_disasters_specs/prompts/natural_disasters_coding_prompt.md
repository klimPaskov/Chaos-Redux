# Coding-agent prompt for Event 013 Natural Disasters

Implement Event 013 Natural Disasters from scratch using the spec package in `docs/specs/013_natural_disasters_specs/`. Do not reuse deleted Event 013 logic. Do not reuse old Earth Earthquake logic. Event 046 must remain an inactive unknown placeholder. Event 099 Sandstorm must not keep separate sandstorm logic and should either remain a placeholder or bridge narrowly into Event 013 dust and sandstorm calls.

Read AGENTS.md, chaos-redux-events, hoi4-decisions-missions, chaos-redux-event-assets, chaos-redux-frame-animation, chaos-redux-super-events, chaos-redux-subagents, chaos-redux-improvement-loop, and any touched-system skill before editing. Inspect the live repo, offline Paradox wiki pages, vanilla docs, and existing Chaos Redux patterns before implementation.

Core requirements:

- Event 013 is Minor Repeatable.
- One Event 013 firing creates one history log row even if many delayed subevents happen.
- Ordinary warning, impact, report, and aftermath subevents must not create extra Event 013 log rows.
- A reusable dynamic disaster call system must support family, target mode, severity, sequence count, news policy, report policy, aftermath policy, chain policy, and scaling multipliers.
- Other events must be able to call specific disaster families without copying logic.
- Disaster impacts must damage buildings and reduce real state population through the Deaths system.
- Baseline disasters must matter. Do not use tiny flavor-only effects.
- Evolution II must scale deaths and destruction much harder and allow chained aftermaths.
- Evolution III must include abnormal meteor, rupture, volcanic, tsunami, and moving storm or tornado corridor behavior, with super-event treatment where the spec requires it.
- Serious impacts must reliably deliver a delayed affected-country report after 1 to 2 days and open or refresh a visible aftermath decision category notification.
- News must be disaster-specific and place-specific early, then throttled later to avoid spam.
- Heat family must not stack with active Event 051 Heat Wave logic.
- Disaster Barrage scenario must use the same controller with type and intensity controls and no terminal world-end branch.

Use dynamic values and script constants for tuning. Do not hardcode magic numbers across files. Keep text direction-only notes out of final localisation. Write final player-facing text from scratch and follow Chaos Redux writing rules.

Required follow-up subagents before completion claims:

- chaosx_scripted_system_architect for reusable effects, triggers, constants, event targets, and cleanup.
- chaosx_decision_mission_auditor for aftermath decisions, missions, costs, AI, cleanup, and exploit risk.
- chaosx_localisation_auditor for visible text, dynamic values, duplicate keys, and encoding.
- chaosx_icon_artist, chaosx_generated_event_art, and possibly chaosx_asset_source_researcher for assets.
- chaosx_super_event_text_researcher and chaosx_super_event_audio_researcher for super-event packages.
- chaosx_event_completion_auditor before final completion.
- chaosx_spreadsheet_doc_worker after implementation facts and in-game wording are final.

Report every simplification, missing asset, missing AI behavior, missing super-event package, placeholder, skipped validation, and unresolved plan. Do not claim completion until the spec acceptance criteria are met.

## Second-pass implementation priorities

Read the expanded continuation files before implementation:

1. Deep family mini-specs define per-family warning decisions, aftermath card fields, AI priorities, report direction, news direction, state modifier direction, and follow-up routes.
2. The abnormal scripted GUI map file defines the map panel, lane cards, coming-next cards, animation states, static fallbacks, target sprite names, and player interaction flow.
3. The recovery decision and mission map defines early rescue, middle stabilization, late reconstruction, foreign relief, active caps, partial success, failure, cleanup, and AI variants.
4. The super-event research matrix is a research handoff only. Do not write final titles, quotes, remarks, slogans, lyric fragments, or audio choices until the super-event workflow documents sources and licensing.
5. The catalog and docs alignment file gives direction for Event Details, scenario details, cluster details, spreadsheet fields, and prompt alignment without final localisation.

Implementation must not preserve old Event 013 logic. Event 046 Earth Earthquake stays an inactive unknown placeholder, while whole-earth rupture behavior belongs to Event 013 Evolution III. Event 099 Sandstorm becomes a placeholder or bridge into the Event 013 dust and sandstorm family. Event 051 Heat Wave remains separate, so Event 013 heat calls must not stack with active Event 051 effects.

Every direct call from another event should be able to pass family, target country, target state or region, severity, report setting, news setting, aftermath setting, follow-up setting, and scaling overrides. The caller should not copy family damage logic.

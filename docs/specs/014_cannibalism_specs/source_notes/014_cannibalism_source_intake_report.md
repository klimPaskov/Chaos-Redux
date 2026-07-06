# Event 014 Cannibalism source intake report

This report records the project files inspected before creating the planning package.

## Uploaded Markdown source files

- AGENTS.md
- CHAOS_REDUX_MECHANICS.md
- chaos-redux-subagents.md
- chaos-redux-improvement-loop.md
- chaos-redux-event-planning.md
- hoi4-focus-trees.md
- hoi4-decisions-missions.md
- chaos-redux-frame-animation.md
- chaos-redux-event-assets.md
- chaos-redux-super-events.md
- chaos-redux-events.md

## Uploaded subagent files

- chaosx_scripted_system_architect.toml
- chaosx_spreadsheet_doc_worker.toml
- chaosx_super_event_audio_researcher.toml
- chaosx_improvement_loop_planner.toml
- chaosx_decision_mission_auditor.toml
- chaosx_icon_artist.toml
- chaosx_generated_event_art.toml
- chaosx_localisation_auditor.toml
- chaosx_country_package_auditor.toml
- chaosx_super_event_text_researcher.toml
- chaosx_skill_maintainer.toml
- chaosx_event_completion_auditor.toml
- chaosx_repo_explorer.toml
- chaosx_documentation_curator.toml
- chaosx_focus_tree_auditor.toml
- chaosx_asset_source_researcher.toml

## Spreadsheet intake

Workbook: chaos_redux_events_catalog.xlsx

Event 014 row in the workbook currently records:

- ID: 14
- Event Name: Cannibalism
- Details: Random country at war gets cannibalism in units.
- Type: Minor Repeatable
- Status: To Be Reworked

The user prompt records the event as Minor Fire-Once. This spec follows the user prompt and records the workbook mismatch as an implementation alignment task after localisation exists.

## Web research intake

External research was used only for historical inspiration and source notes. It does not provide final localisation or final super-event quotes.

- National WWII Museum, History Through the Viewfinder
- Australian War Memorial, The Japanese experience at Buna-Gona
- Smithsonian Institution, Survival Cannibalism in Historic Jamestown
- National Archives, Researching Japanese War Crimes PDF

## Project constraints carried into the spec

- Event source specs belong under docs/specs/014_cannibalism_specs.
- Prompt files stay separate from the spec.
- Final package is delivered as one zip.
- Goal prompt stays below 4000 characters.
- Event Details and spreadsheet details must describe the situation, not raw mechanical effects.
- Evolutions are mutation tracks, not ordinary baseline stages.
- Decisions and missions use concrete costs, not political power or command power only.
- Animated assets need real source frames, frame sheets, and static fallbacks.
- Super-event titles, quotes, button remarks, and audio choices require research before final implementation.
- Asset subagents handle source or generated files, while implementation owns final wiring.

## Implementation-only reveal identity

The true-name data for the final reveal is stored in `implementation_notes/014_cannibalism_reveal_identity.md`. Keep that data out of pre-reveal player-facing text and visible asset names.

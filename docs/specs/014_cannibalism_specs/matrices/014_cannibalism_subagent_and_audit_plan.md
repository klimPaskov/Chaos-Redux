# Event 014 Cannibalism subagent and audit plan

This file maps project subagent ownership for implementation. It does not claim that subagents have already implemented anything.

## Planning and architecture

| Subagent | Use |
| --- | --- |
| chaosx_scripted_system_architect | design and patch reusable effects, triggers, constants, event targets, dynamic values, cleanup helpers, spread helpers, and cannibal country setup helpers |
| chaosx_improvement_loop_planner | use only after a major implementation tranche if the system still feels shallow or disconnected |
| chaosx_repo_explorer | use before implementation only if actual repo file locations or existing patterns are unclear |
| chaosx_documentation_curator | use after several handoffs or before resume if docs and plans become stale |

## Gameplay audits

| Subagent | Required after |
| --- | --- |
| chaosx_decision_mission_auditor | after decision category, missions, scripted GUI buttons, costs, and cleanup exist |
| chaosx_focus_tree_auditor | after cannibal country focus tree or additive focus hooks exist |
| chaosx_country_package_auditor | after CBL or any cannibal country package exists |
| chaosx_localisation_auditor | after broad visible text and scripted localisation are written |
| chaosx_event_completion_auditor | before final completion claim |
| chaosx_spreadsheet_doc_worker | after in-game Event Details and evolution wording are final |

## Asset and super-event work

| Subagent | Use |
| --- | --- |
| chaosx_generated_event_art | generated report, news, super-event, portraits, flags, faction emblems, UI panels |
| chaosx_icon_artist | idea, decision, category, focus, achievement, and small animated icon assets |
| chaosx_asset_source_researcher | only non-gore archival source material or real historical symbols if later needed |
| chaosx_super_event_text_researcher | quotes, button remarks, slogans, and cultural references |
| chaosx_super_event_audio_researcher | licensed or public domain music research and OGG handoff |

## Handoff locations

Patch handoffs should use:

- docs/plans/014_cannibalism_plans/subagent_handoffs/

Design addenda should use:

- docs/plans/014_cannibalism_plans/

Accepted source design should be merged into:

- docs/specs/014_cannibalism_specs/

## Audit focus points

- source classification mismatch, user prompt says Minor Fire-Once and workbook currently says Minor Repeatable
- no baseline stage should be logged as an evolution
- no country should receive the cannibal tree unless event-created or transformed through the event
- no real gore assets should be sourced from identifiable victims
- no super-event title, quote, remark, or audio should remain unresearched
- no exploit path should become safe or optimal without severe future risk
- no active country cleanup should erase other countries' active outbreaks

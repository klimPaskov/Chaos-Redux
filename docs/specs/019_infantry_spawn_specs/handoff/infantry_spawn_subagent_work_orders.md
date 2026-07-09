# Infantry Spawn subagent work orders

This file converts the provided subagent instruction files into implementation work orders. In this chat environment, project subagents could not be spawned directly. The implementation environment should spawn them with `fork_context=false` and pass the relevant spec paths explicitly.

## Recommended order

1. `chaosx_repo_explorer` if the implementation agent needs a file map for existing event, decision, unit, focus, chaos unit, and scenario patterns.
2. `chaosx_scripted_system_architect` for density helpers, random template helpers, chaos unit registry, cleanup helpers, and dynamic cost constants.
3. `chaosx_icon_artist` for decision, idea, achievement, focus, and animated icon packages.
4. `chaosx_generated_event_art` for possessed general portraits, fictional report images, fictional news images, super-event images, flags, and country identity art.
5. `chaosx_super_event_text_researcher` if any candidate super-event is accepted.
6. `chaosx_super_event_audio_researcher` if any candidate super-event is accepted.
7. `chaosx_decision_mission_auditor` after decision category and missions exist.
8. `chaosx_country_package_auditor` after breakaway country packages exist.
9. `chaosx_focus_tree_auditor` if the shared crisis focus tree is implemented.
10. `chaosx_localisation_auditor` after broad localisation exists.
11. `chaosx_improvement_loop_planner` near completion for depth and anti-bloat pass.
12. `chaosx_spreadsheet_doc_worker` after in-game Event Details and evolution text exist.
13. `chaosx_documentation_curator` if long implementation creates many specs, plans, handoffs, or reports.
14. `chaosx_event_completion_auditor` before any final completion claim.

## Parent prompt requirements

Every subagent prompt should include event id 019, event slug infantry_spawn, exact source spec paths, current implementation status, accepted or queued plan status, and the user's core constraints. Do not rely on inherited conversation context.

## Known blocker in this planning chat

The uploaded TOML files were read and their requirements were folded into this package, but no custom Codex subagent execution tool was available here. This package therefore provides work orders instead of subagent handoff outputs.

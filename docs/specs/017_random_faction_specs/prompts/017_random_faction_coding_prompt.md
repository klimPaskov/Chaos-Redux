# Coding prompt for Event 17: Random faction

Implement Event 17 from the full spec package under `docs/specs/017_random_faction_specs/`.

Read and follow:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-event-planning`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation` for animated assets
- relevant offline Paradox wiki pages and vanilla HOI4 documentation before editing game files

Implement:

- Event ID `17`, name `Random faction`, type `Minor Repeatable`
- dynamic eligible minor selection, including the player if their country is selected and eligible
- dynamic valid faction discovery, with one to four player options and no decline option
- shared helper logic for player options, AI resolution, event logs, pressure memory, and cleanup
- baseline faction join, alignment shock, faction leader memory, and regional pressure
- Evolution I Regional Bloc Race
- Evolution II Pressured Neutrality
- Evolution III Collapse of Neutrality
- Bloc Pressure decision category, decisions, timed missions, dynamic costs, AI behavior, and cleanup
- event log, event details, evolution log entries, cluster assignment, docs, achievements, assets, and spreadsheet alignment

Do not hardcode Axis or Comintern. Do not leave placeholder assets or unwired localisation. Do not reduce the system to a single random join effect. Do not claim completion until every visible surface, AI path, cleanup path, and documentation surface is aligned.

Unresearched final prose is not provided by the spec. Write final localisation from the direction files, and treat any final source-dependent quote, song, slogan, or cultural reference as blocked until researched.

Use relevant subagents through explicit prompts with `fork_context=false` when working in Codex. At minimum use scripted-system, decision, localisation, asset/icon, spreadsheet, documentation, and completion audit handoffs.

# Coding Prompt — Event 010 Death

Implement Event ID 10 as `Death`, fully replacing the obsolete `Spirit of War/Peace` event. Read and follow:

- `AGENTS.md`
- `CHAOS_REDUX_MECHANICS.md`
- `chaos-redux-events`
- `chaos-redux-event-planning`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `hoi4-decisions-missions`
- `hoi4-focus-trees` if implementing the Death focus/progression tree
- all spec files under `docs/specs/010_death_specs/specs/`
- all matrices and prompt handoffs under `docs/specs/010_death_specs/`

## Core implementation requirements

- Delete, disable, or supersede all active `Spirit of War/Peace` content. ID 10 must resolve to Death everywhere.
- Event type: Minor Fire-Once. No cluster.
- Entry event root: `chaosx.nr10.1`.
- Create Death (`DTH` or conflict-free final tag), leader Zol, complete black map color, no starting units, remote island origin.
- Origin selection must choose valid remote low-pop island states only; show N/A if no valid island exists.
- No initial world notification. Use delayed missing-island reports months later without revealing Death.
- Implement one shared state-consumption effect used by origin, island spread, withering, coastal jumps, world-end footholds, and scenarios.
- Every consumed state: population to zero; add consumed population and civilian deaths when enabled; delete/neutralize industry, infrastructure, ports, airbases, rail/supply, resources; transfer/core to Death; apply wasteland effects; no resistance.
- Death states severely slow divisions, cause heavy attrition, and apply ticking strength loss through a narrow tracked-state pulse.
- Reveal super-event fires when Death consumes a mainland state with more than 100,000 population.
- After reveal, Death becomes a world threat, auto-declares war on neighbors, can wither undefended neighboring states, and can coastal-jump with cooldown if pushed back.
- Withering cannot consume target states containing non-Death enemy divisions.
- Death defeat requires full occupation/no Death-controlled states, not ordinary surrender shortcuts.
- Ghost divisions: none at start; weak passive ghosts around 600 tier; more/stronger but still inferior ghosts around 800; infantry-parity aggressive hosts only at world-end.
- World-end starts only when Death has consumed an entire continent and Chaos is above 1000. Then create a random coastal foothold on every remaining continent, spawn world-end hosts, and intensify withering/aggression.
- Whole-world consumed final super-event and achievement hooks must exist.

## Required systems

- Event registration, event-name/debug-name mappings, event details, history/evolution logs, actor mapping, manual firing availability, docs, and spreadsheet update.
- Death country package: tag, history/setup, localisation, ideology-specific names, party, leader, trait, flags, special chaos/nonhuman classification, AI, ideas.
- Death mechanics/focus/progression tree or equivalent staged branch system preserving Shroud, Hunger, Census, Wasteland, Coastal, Host, Last Shores lanes.
- Decisions/missions: Missing Island, Death Country, Living Containment Compact, Wasteland Outposts, World-End Emergency. Dark Methods and Black Oath must be fully implemented or explicitly queued/hidden, not half-visible.
- Script constants and helper effects/triggers for tuning, target selection, consumption, state cleanup, wither progress, ghost spawn, coastal jump, defeat check, compact values, and UI values.
- Triggerable scenario `SCN-006` with Quiet Origin, Island Pattern, Mainland Reveal, Last Shores types and four intensity stops.
- Assets and super-events per asset/super-event prompts. Register placeholder sprite definitions only if final asset production is queued, and report placeholders clearly.
- Achievements per achievement prompt.
- AI strategy for Death, neighbors, majors, compact, dark methods, and Heralds.

## Subagents to use during implementation

Use project subagents with `fork_context=false` and explicit prompts:

- `chaosx_repo_explorer` if touched files/patterns are uncertain.
- `chaosx_scripted_system_architect` before duplicating consumption, spread, wither, ghost, scenario, or compact logic.
- `chaosx_generated_event_art`, `chaosx_icon_artist`, and possibly `chaosx_asset_source_researcher` for assets.
- `chaosx_super_event_text_researcher` and `chaosx_super_event_audio_researcher` for quotes/remarks/audio.
- `chaosx_decision_mission_auditor`, `chaosx_country_package_auditor`, `chaosx_localisation_auditor`, and `chaosx_event_completion_auditor` before completion.
- `chaosx_spreadsheet_doc_worker` after in-game wording exists.

## Completion standard

Do not claim completion if any requested mechanic, decision family, country package surface, asset, super-event, achievement, AI behavior, docs update, spreadsheet update, or validation/audit is missing. Report all simplifications, blockers, queued branches, placeholders, unsupported visual/building fields, and unimplemented optional systems explicitly.

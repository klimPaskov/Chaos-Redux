# Repository exploration prompt for Event 58 Random Buildings

Use this prompt with `chaosx_repo_explorer` before implementation. Spawn with `fork_context=false`.

The accepted source specs are under `docs/specs/058_random_buildings_specs/`.

## Exploration goal

Map every current repository and installed-reference surface needed to replace Event ID `58` with Random Buildings without editing files.

The explorer must read `AGENTS.md`, `chaos-redux-subagents`, `chaos-redux-events`, the Event 58 specs, the relevant decision and asset skills, the offline wiki pages required by AGENTS, installed vanilla documentation, and only the repository files discovered through targeted Event 58 and building searches.

## Required searches

Find and report:

- every existing `chaosx.nr58.*` event and Event 58 name mapping
- Event 58 registration, default enable state, classification, manual trigger, and repeatable handling
- Event Logs History, Events, Event Details, evolution, actor, debug-name, and scripted-localisation paths
- current Event 58 docs, specs, plans, prompts, assets, localisation, and catalog references
- all occurrences of `The Industrial Complex`, `Random Buildings`, and likely old ID 58 variables or flags
- the closest implemented global all-state event transaction
- the closest provider or owner-registration system in Chaos Redux
- current ordinary and custom state building definitions
- current province building, railway, naval-base, supply-hub, facility, dam, landmark, stronghold, electrical-grid, camp, extermination-camp, gulag, reactor, heavy-water, and rocket-site definitions
- public owner adapters and lifecycle hooks for those structures
- shared country classifier call sites relevant to building validity
- current achievement registry and Event 58-compatible tracking patterns
- current report-event image and Event Details image precedents
- Positive Economy cluster registration, member rules, severity, and probability surfaces
- authoritative workbook row locations and current exporter

## Vanilla and local reference mapping

Identify exact installed vanilla files and documentation proving:

- state-level building identifiers and maximum-level or shared-slot behavior
- province-level fort, coastal-fort, naval-base, railway, and supply-hub behavior
- special facility placement and DLC gates
- event-scope and state-scope construction effects
- safe iteration and random-list patterns
- report-event image and event structure
- achievement registration

Use approved large mods only when vanilla and Chaos Redux do not answer a concrete question.

## MCP evidence

Use the exact read-only MCP tools available for:

- Event 58 chain inspection and rendering
- cluster and weighted-selection structure
- map, province, railway, supply, coastline, facility, and landmark inspection
- current GUI surfaces only where Event 58 uses shared report or Event Details presentation

Route detailed weighted analysis to `chaosx_ai_probability_auditor`. Do not substitute hand arithmetic.

## Output

Write the handoff to:

`docs/plans/058_random_buildings_plans/subagent_handoffs/repo_explorer_handoff.md`

Include:

- primary files and exact identifiers
- existing patterns and reusable helpers
- owner API map
- vanilla precedents
- map and DLC blockers
- catalog discrepancy confirmation
- implementation order
- task-specific validation plan
- unresolved questions

Do not patch any source file. Do not invent a provider API that the repository already supplies under another name.

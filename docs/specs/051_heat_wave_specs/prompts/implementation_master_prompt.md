# Master Implementation Prompt

Implement Chaos Redux Event 051, Heat Wave, from the accepted specification package at:

`docs/specs/051_heat_wave_specs/`

Work against the live repository. Do not treat this prompt as a substitute for the full specs.

## Required reading

Read in full before editing:

- `AGENTS.md`
- every file under `docs/specs/051_heat_wave_specs/`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-super-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- current mechanics guide
- current dynamic scripted trigger and effect registries
- Famine and Migration owner documentation
- Event 013 Natural Disasters documentation
- Deaths, Air Cleanliness, event-log, cluster, map-mode, achievement, audio, and terrain documentation

Read the required offline Paradox wiki pages and installed vanilla documentation for events, decisions, missions, triggers, effects, scopes, variables, event targets, modifiers, localisation, AI, map and terrain, graphical assets, interface behavior, and on-actions. Inspect current Chaos Redux and vanilla precedents for each touched surface.

## Accepted identity

- Event ID: `051`
- Name: Heat Wave
- Type: Minor Repeatable
- Chaos level: 1
- Cluster: Natural Disasters
- Member severity: High
- Entry event: `chaosx.nr51.1`

The older CSV export says Fire-Once. The accepted specs supersede that snapshot. Update only the authoritative XLSX after implementation and regenerate CSV exports.

## Core behavior

Create one global episode with a generation ID, dynamic Global Heat Wave Intensity, changing phases, regional amplification, surges, lulls, decline, recovery, cleanup, and later repeat eligibility.

Expose only two event-specific player values:

1. Global Heat Wave Intensity from 0 to 100 with band and trend.
2. Local Heat Stress as a state band with trend.

Keep water, agriculture, industry, military exposure, environmental exposure, and mitigation components internal. Present their actionable causes through short tooltips, hotspot roles, reports, and decisions.

Use bounded registered processing. Do not add a whole-world daily, weekly, or monthly country scan without explicit user approval.

## Required gameplay

Implement:

- uneven state Heat Stress from environment, load, weakness, mitigation, and exposure memory
- state modifiers with hysteresis
- military heat exposure, acclimatization, unit rotation, supply interaction, and Evolution I casualties
- water pressure, rationing, cooling centers, hospital and sanitation pressure
- crop, livestock, irrigation, food-transport, and harvest pressure
- factory, construction, power, rail, port, resource, and infrastructure consequences
- one phased decision category with national protection priorities
- all specified decision and mission families, with real costs and no more than four spendable cost types per action
- condition-linked report families and rate limits
- exact cleanup and later repeat behavior
- twelve achievements or an explicitly documented accepted disposition for any changed count

## Evolution behavior

Implement one ordered track:

- Evolution I, The Killing Heat, at 200+
- Evolution II, The Drying Earth, at 600+
- Evolution III, The Scorched World, at 1000+

Use shared MTTH evolution pacing. Evolution activation adds zero Chaos. Respect evolution enable and disable state. Do not set recorded flags when disabled.

Evolution I adds confirmed recurring civilian and military mortality through shared transactions.

Evolution II activates permanent environmental degradation evaluation from recorded exposure.

Evolution III permits near-uninhabitable states, the one-time escalation super-event, and rare wasteland eligibility.

The event remains recoverable and repeatable after Evolution III.

## Integration boundaries

Reuse:

- `call_natural_disaster` for actual wildfire requests
- `apply_exact_state_civilian_population_loss` for heat deaths
- supported military casualty and Deaths path
- Famine adapter for food-security incidents
- Migration adapter for cohorts, routes, reception, and return
- stockpile debit helpers where suitable
- shared country classifiers

Do not duplicate Deaths, Famine, Migration, Event 013 impact, or Air Cleanliness source accounting. Heat alone adds zero direct Air Contamination.

Inspect exact owner API contracts and fail closed when proof is incomplete.

## Environmental degradation

Implement the permanent ledger and warnings. Actual terrain or province conversion requires mandatory map inspect, supported rewrite, comparison, and rollback evidence. Do not silently replace an accepted map change with only a modifier. Report any blocked map route.

Wasteland must require Evolution III, prior degradation, long Scorched exposure, severe collapse, failed mitigation, and strict caps.

## Logs, cluster, and repeatability

Wire:

- normal event history once
- Event Details premise, type, Chaos level, status, and three evolution previews
- evolution history rows across all required surfaces
- Natural Disasters cluster membership and skip reasons
- repeatable fired count, cap reduction, recovery, and active exclusion
- concrete event-owned Chaos milestones with no duplicate Deaths or Air Cleanliness Chaos

## Presentation and assets

Follow the complete authorized inventory in the asset specification and use the correct narrow asset subagents.

Use one category picture with static fallback. Implement the optional intensity-linked frame animation only through real source frames and a frame sheet.

Research and implement the Evolution III super-event with a verified quote and unique licensed musical recording. Use settings-aware playback and update the canonical music catalogue.

## Required subagents and evidence

Use context-complete prompts with no inherited parent context.

Use or route as needed:

- scripted-system architect for helper architecture
- decision and mission auditor after decisions exist
- localisation auditor after visible text exists
- asset researcher, generated event art, and icon artist for actual assets
- super-event text and audio researchers
- probability auditor before and after weighted changes
- completion auditor before claiming completion
- spreadsheet worker after final implementation wording exists

Do not spawn the event UI worker unless implementation proves a dedicated event-owned GUI is necessary and a new accepted UI brief is written.

Use mandatory MCP paths for event chains, probabilities, and map changes. Source-only review is not equivalent when the route exists.

## Completion

Do not claim completion while mechanics, AI, localisation, assets, audio, achievements, terrain proof, logs, cluster wiring, docs, workbook alignment, or accepted validation remain missing.

Write a concrete completion report under `docs/plans/051_heat_wave_plans/`. List files, identifiers, gameplay systems, task-specific validation, assets, audio, docs, workbook update, and every simplification or blocker.

No unapproved fallback is allowed.

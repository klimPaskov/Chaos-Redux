# Event 005 Soviet Collapse Clean Overview

This is the compact entry point for the Soviet Collapse implementation state. It merges the scattered Event 005 notes into a small readable set and replaces older audits, package notes, asset sidecars, and subagent handoffs as the current documentation source.

## Current Gameplay Surface

Event 005 is a major Soviet crisis started through `chaosx.nr5.1` and visible event `chaosx.nr5.2`. The implementation spans:

- event chain: `events/005_soviet_collapse.txt`
- crisis constants: `common/script_constants/005_soviet_collapse_constants.txt`
- MTTH values: `common/mtth/005_soviet_collapse_mtth.txt`
- shared logic: `common/scripted_effects/005_soviet_collapse_effects.txt`
- shared gates: `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- decisions and missions: `common/decisions/005_soviet_collapse_decisions.txt`
- focus trees: `common/national_focus/005_soviet_collapse_*.txt`
- localisation: `localisation/english/005_soviet_collapse*.yml`
- country setup: `history/countries/*`
- assets: `gfx/`, `interface/`, `music/`, `sound/`, and `docs/assets/005_soviet_union_collapse/`

The main active systems are:

- a dynamic Union Collapse Threat model
- Moscow Authority, Armed Breakaway Momentum, Command Obedience, Foreign Penetration, League Cohesion, Depot Vulnerability, and Old Movement pressure
- opening breakaway selection
- progressive MTTH republic releases
- Soviet crisis missions and response decisions
- breakaway emergency decisions
- foreign patron decisions and dependency pressure
- local league and Free Republics' League logic
- Union Unmade terminal collapse
- triggerable scenario launch: the Scenarios window can force Union Unmade immediately, release ordinary republics or ordinary plus high-chaos splinters by type, form local factions, start the anti-Soviet wars, and grant extra opening forces scaled by intensity, controlled states, and factories
- reconquest resolution: Moscow marks the crisis resolved after regaining control of every state held when the crisis began, which clears the crisis/terminal flags, removes active Soviet missions, hides breakaway and foreign intervention boards, and resets the crisis meters
- runtime focus trees for ordinary republics and fixed focus trees for custom/high-chaos actors
- super-event and report/news presentation surfaces

Focus rewards avoid direct idea stacking as a normal payoff. New focus rewards should prefer variable progression, state work, units, decisions, recognition, depot control, League coordination, or one of the consolidated staged idea helpers rather than adding a fresh visible spirit from each focus. Tiny repeated train, truck, or isolated state-building rewards should be routed through shared rail authority, field-defense, and mobile-column helpers, so the visible result is supply nodes, defended capitals, deployed field columns, depot readiness, command capacity, or route progress rather than clutter. The External Support consolidated idea is reserved for republics that have actually received foreign aid or accepted dependency patronage; self-directed liaison or diplomacy focuses can raise liaison, recognition, resilience, or patronage risk, but they must not mark the republic as externally supported by themselves.

High-chaos/custom splinter military routes are deliberately more dangerous than ordinary republic routes. Their war-plan and hidden-doctrine payoffs create assault and raider templates, spawn equipped formations, core controlled ground, and issue dynamic war goals against the Soviet remnant and non-allied neighbors. This keeps chaos actors expansion-driven instead of defensive focus trees that only collect small stockpile or building rewards.

## Event Log Evolutions

Event 005 registers two event-log evolution families:

- Republic Secession Progression, type `constant:soviet_collapse_event_log.secession_evolution_type`: records first republic declarations, regional cascade, Union Unmade, and terminal republic/splinter rupture milestones.
- High-Chaos Successor Mutation, type `constant:soviet_collapse_high_chaos_event_log.evolution_type`: records the first qualifying high-chaos or extreme successor authority while keeping later high-chaos reports out of the evolution log.

The event-details preview list for event ID `5` is registered in `events_log_rebuild_open_event_details_view`. Player-facing evolution body text mirrors the Event 005 row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

## Legacy Doc Routing

Older Event 005 markdown now redirects into the clean set:

- top-level `docs/events/*005*soviet*.md` and `docs/events/*005*Soviet*.md`
- `docs/plans/005_soviet_union_collapse_plans/**/*.md`
- old `docs/plans/005_soviet_collapse_plans/**/*.md`
- markdown sidecars under `docs/assets/005_soviet_union_collapse/`, `docs/assets/005_soviet_collapse/`, and `docs/assets/005_soviet_collapse_generated_handoff/`
- `docs/super_events/005_soviet_union_collapse_super_event_research.md`

Generated/source/final binary assets and text prompt files remain in place. The removed Markdown bodies should not be used for implementation decisions; update this clean doc set instead.

## Current Priority

Implementation should continue in this order:

1. Balance: prove and fix calm strong-USSR threat, Republic Momentum, Foreign Penetration, and Union Unmade pacing.
2. MTTH releases: make later republics appear through dynamic pressure without a fixed trio or permanent stalling.
3. Focus quality: remove duplicate reward clusters and clean layouts without overlapping focuses or crossing lines.
4. Countries and leaders: ensure generated portraits, leader names, gender flags, history setup, focus loading, and country localisation match.
5. Assets: finish unique flags, ideology flags, route flags, portraits, and super-event assets after gameplay is stable.

# Event 40 Full Implementation Prompt

Implement Chaos Redux Event 40, Lawrence of Arabia, from the complete accepted specification pack under:

`docs/specs/040_lawrence_of_arabia_specs/`

Treat every mapped mechanic, outcome, evolution, character state, decision family, AI route, federation package, asset, achievement, super-event, log surface, and cleanup rule as acceptance criteria.

## Required reading

Before editing, fully read:

- `AGENTS.md`
- all relevant offline Paradox wiki pages required by the touched systems
- all relevant installed vanilla documentation and vanilla precedents
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-focus-trees/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- every Event 40 spec, prompt, research note, diagram, and quality scenario

Use installed HOI4 MCP tools for every supported event, focus, weighted-logic, GUI, technology, and map surface. Missing MCP capability is a blocker for the affected evidence. Do not treat source inspection as equivalent.

## Core identity

- entry event: `chaosx.nr40.1`
- type: Minor Fire-Once
- Chaos level: `1`
- cluster: none
- one initial History entry
- later regional interventions are internal follow-up stages
- three true evolution milestones
- no world-end branch
- no triggerable scenario
- no dedicated scripted GUI
- no custom 3D unit

Correct the current catalog type from Minor Repeatable to Minor Fire-Once only through the authoritative workbook after implementation wording is stable.

## Historical premise

Lawrence died publicly in 1935. The entry chain reveals concealed survival and British recall.

Create one canonical Lawrence character. Search installed vanilla and the repository for existing ownership. Reuse or transfer through a guard when needed. Never clone him.

If Lawrence dies during Event 40, close every dependent route permanently.

## Suggested event-owned files

Use clear event-scoped ownership unless an existing repository pattern requires another location.

- `events/040_lawrence_of_arabia.txt`
- `common/script_constants/040_lawrence_of_arabia_constants.txt`
- `common/scripted_triggers/040_lawrence_of_arabia_triggers.txt`
- `common/scripted_effects/040_lawrence_of_arabia_effects.txt`
- `common/on_actions/040_lawrence_of_arabia_on_actions.txt`
- `common/decisions/040_lawrence_of_arabia_decisions.txt`
- `common/decisions/categories/040_lawrence_of_arabia_categories.txt`
- `common/ideas/040_lawrence_of_arabia_ideas.txt`
- `common/opinion_modifiers/040_lawrence_of_arabia_opinion_modifiers.txt`
- `common/dynamic_modifiers/040_lawrence_of_arabia_dynamic_modifiers.txt` when a dynamic modifier is the clearest implementation
- `common/characters/040_lawrence_of_arabia_characters.txt`
- event-owned AI strategy files
- event-owned federation focus and country files after collision audit
- Event 40 localisation and scripted localisation files
- Event 40 GFX and runtime asset paths
- permanent Event 40 documentation

Do not put Event 40 lifecycle or validation inside the shared dynamic-effect or dynamic-trigger registry. Use shared helpers only for neutral cross-system behavior.

## Architecture

Implement one active target at a time with:

- active target proof
- campaign generation ID
- phase
- Lawrence's Influence
- British capability and route state
- character state
- target settlement memory
- delayed next-target job
- sparse registered target and regional-node arrays

Do not use a whole-world daily or monthly scan. Use event-driven updates, active registries, country-local coordination, and bounded delayed work.

Every public request or transaction fails closed when target, generation, or contract proof is incomplete.

## Target registry

Create an explicit Event 40 Arabian country and state registry for the current map.

- Peninsula, Levant, and Mesopotamia are the ordinary core.
- Egypt is conditional as specified.
- Maghreb is outside ordinary targeting.
- special Chaos and actual nonhuman countries are excluded.
- released stable regional countries can enter.
- existing subjects and clients can serve as nodes without being retargeted.

Use `is_desert_state` only for terrain and logistics behavior.

## Public mechanic

Expose only `Lawrence's Influence` during the active intervention.

Implement six readable bands, trend, next threshold, and confirmation windows. Keep reach, cells, trust, credibility, and federation readiness internal or qualitative.

After federation formation, close Lawrence's Influence and begin `Federal Authority` for the new country.

## Baseline stages

Implement:

1. Recall and Arrival
2. Terms of Access
3. Network Contest
4. Institutional Decision
5. Settlement and Regional Transfer

Implement every accepted baseline outcome:

- British protectorate or client
- independent British ally
- sovereign armed partner
- restricted or unresolved mission
- expulsion
- arrest
- network dismantlement
- double-game victory
- rare Lawrence defection

Use confirmation periods. A threshold spike cannot immediately decide a country.

## Decisions and missions

Implement the decision and mission prompt. Keep phase action counts inside the stated budget. Use real costs, real routes, named states, partial success, AI equivalents, and full cleanup.

Support La Résistance intelligence and the accepted no-DLC fallback.

## Evolution I

At Chaos 200, through normal evolution pacing and enable checks, unlock:

- arms and smuggling cells
- railway and communications cells
- officer cells
- local-leader cells
- political and press cells
- sabotage, defections, mutiny, uprising, and government-replacement routes

Civil war requires a validated country split with territory, capital, forces, equipment, supply, AI, and rollback.

## Evolution II

At Chaos 400, through normal evolution pacing and enable checks, build the British Arabian System from real settled partners.

Implement:

- Arabian Liaison Conference
- Arms Standardization Office
- Regional Intelligence Office
- Desert Air Route
- Oil and Transport Agreements
- Joint Defense Charter
- favored-partner and autonomy politics
- independent counter-bloc

Reuse valid existing factions. Do not conjure clients or empty institutions.

## Evolution III

At Chaos 600, through normal evolution pacing and enable checks, unlock federation formation.

Implement:

- congress and ratification
- legitimate core selection
- British Arabia
- Independent Arab Federation
- rare Lawrence's Kingdom
- one validated formation transaction
- rollback
- player switching
- Federal Authority
- outcome-specific country and focus package
- three unique regional-order super-events

Do not grant instant cores over the region.

## Chaos

Evolution activation gives zero Chaos.

Implement only the event-owned one-shot consequence values from the specification. Do not duplicate shared war, puppet, annexation, ideology, death, or contamination sources.

## Event log

Wire:

- Fire-Once registration
- event name and debug name
- default actor behavior
- one History entry
- Event Details
- three evolution preview rows
- three logged evolution milestones
- actor, tier, stage, date, and enabled state

Keep later intervention stages out of the random History and pacing transactions.

## Cross-event bridges

Implement explicit bridges for:

- Malta Crusaders
- Independence Wave
- existing faction and alliance systems
- Great Embargo
- Intel Leaked
- Murder Mystery only where evidence exists
- Famine and Migration through proven owner contracts
- later oil, colonial-collapse, and regional-war readers

Do not create broad dependencies through shared registries when a narrow adapter is enough.

## Federation package

Follow the federation country and focus specification in full.

Before tag work, audit vanilla, Chaos Redux, Workshop mods, and sibling local mods. Lock the carrier approach.

Implement:

- capital and territory
- member consent and refusal
- unit, stockpile, manpower, leader, war, subject, and technology transfer
- starting economy and supply
- three starting idea lifecycles
- Federal Authority
- route-aware focus tree
- decisions, AI, flags, names, leaders, advisers, claims, staged cores, diplomacy, defeat, release, and cleanup

## Assets

Run the asset prompt through the named asset workers.

Grounded Lawrence portrait rules are strict. Source-placeholder mode is accepted. Do not generate or reconstruct his identity.

No required asset may remain an unreported placeholder.

## Achievements and super-events

Implement every accepted achievement and all three federation super-events through their dedicated prompts.

Quotes and audio require verified sources. Every super-event needs unique final audio and settings-aware playback.

## AI and probability

Use the named scenarios in:

`quality/040_lawrence_of_arabia_probability_scenarios.md`

Run baseline audits before changing weighted logic. Let the owning agent apply the source change. Run probability compare afterward with the same scenarios.

Do not claim exact probabilities from an incomplete pool.

## Documentation and catalog

Update:

- permanent event documentation
- implementation and completion reports
- Event Details and evolution wording
- super-event research
- audio catalog
- asset provenance crosswalks
- achievement documentation
- focus route coverage
- authoritative event workbook
- regenerated CSV exports

Do not edit export CSVs directly.

## Required subagents and audits

Use context-complete prompts with no inherited conversation context.

Required specialist passes include:

- scripted-system architect
- decision and mission auditor
- AI probability auditor
- focus-tree auditor
- country-package auditor
- localisation auditor
- portrait and asset workers
- super-event text and audio researchers
- spreadsheet worker
- event completion auditor

The parent retains final integration and completion responsibility.

## Implementation order

1. Inspect current repo and vanilla precedents.
2. Lock target registry, character ownership, and federation carrier strategy.
3. Build constants, triggers, effects, and generation-safe lifecycle.
4. Implement entry and baseline stages.
5. Implement decisions, missions, AI, and no-DLC intelligence fallback.
6. Implement evolutions and logs.
7. Implement federation transaction and country package.
8. Implement focus tree and Federal Authority.
9. Produce and wire assets, achievements, super-events, and audio.
10. Align localisation, docs, Event Details, and workbook.
11. Run probability, focus, decision, country, localisation, and completion audits.
12. Validate every named acceptance scenario.

## Completion standard

Do not call the event complete when any accepted outcome, evolution entry path, AI profile, asset, portrait, achievement, super-event, federation route, log row, cleanup path, documentation surface, or catalog field is missing.

Report every simplification, fallback, blocker, and unresolved audit. If none remain, state that explicitly and support it with task-specific evidence.

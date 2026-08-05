# Independence Wave coding prompt

Implement the full Chaos Redux Event 6 rework from the source specification package under `docs/specs/006_independence_wave_specs/`.

Event ID: `6`

Event name: Independence Wave

Event type: Minor Repeatable

Cluster: Liberations

Do not implement a reduced release popup or an empty-tag system. The event is a synchronized global country-creation system with survival mechanics, regional content, focus trees or overlays, dynamic forces, foreign patrons, former-host relations, a league, formables, evolutions, achievements, super-events, and a triggerable scenario.

## Required reading and process

Read and follow:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-frame-animation/SKILL.md`
- `.agents/skills/chaos-redux-super-events/SKILL.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- all Event 6 spec parts, matrices, diagrams, research notes, and prompt files
- relevant offline Paradox wiki pages
- vanilla documentation and at least one vanilla precedent for every touched system
- existing Chaos Redux event, country, focus, decision, event-log, cluster, scenario, super-event, and dynamic helper patterns

Use `chaosx_repo_explorer` only if the touched-file map or precedent is unclear. Spawn every project subagent with `fork_context=false` and pass all needed paths and constraints explicitly.

## Core release system

Implement the doubled automatic wave ladder:

- Calm World: 6 countries
- Gathering Storm: 8 countries
- Rising Chaos: 10 countries
- Chaos Tier: 14 countries
- Totalen Chaos: 20 countries
- World Collapse: 20 countries, with stronger forces, instability, rarity, and ambition

Build the complete wave plan before releasing anything. Reserve a protected state for every host, prefer its capital, guarantee at least one surviving host state, select unique candidate anchors, trim optional territory before dropping a candidate, and reroll invalid or living tags. Execute the locked plan as one synchronized incident.

## Pre-wave crisis surface

Implement the host-facing crisis as a scoped, costed mission rather than a second release path. Expose it below 35% stability, when an enemy controls an owned state above 50 resistance, or when a country controls a foreign-owned state above 50 resistance; use the centralized 120-day mission and standard security commitment. On successful resolution, queue `chaosx.nr6.3` for the ordinary current-band wave; the endpoint waits through a bounded retry window when the shared Liberations coordinator is busy and fails closed when the plan remains invalid. Busy, invalid, cancelled, or failed resolution must apply visible pressure/cooldown outcomes without changing ownership. The crisis may not add a world-wide periodic loop, create a country directly, bypass host survival, or bypass reservation and synchronized execution. Record live mission, AI, queue-cleanup, save/load, and allocator evidence separately from static source validation.

Use the candidate registry as a data source. A candidate is runtime-eligible only when its tag, country definition, anchor, capital, flags, leader mode, starting setup, focus content, decisions, AI, and localisation are ready.

## Origin separation

Event 6 and Event 5 are separate origin systems.

- Set Event 6 origin only when Event 6 creates the country.
- Never overwrite a living country's origin or meaningful focus tree.
- Soviet Collapse origin countries keep Soviet Collapse content.
- In a joint Liberations cluster firing, reserve tags and anchors before either event executes. One tag receives one origin. The other event rerolls.
- End active origin content on annexation or voluntary reunion while preserving historical log and achievement memory.
- A later release receives the origin of the action that recreates it.

Every new Event 6 country tag, formable tag, cosmetic tag, and route split tag must end in `X`. Existing registered tags may be reused.

## Country package

Every released country must receive:

- valid tag and country setup
- capital and ownership
- complete name, adjective, party, leader, and flag coverage
- dynamic starting ideas
- visible mechanic values
- dynamic starting forces, templates, equipment, manpower, commanders, and supply assumptions
- reinforcement pathways
- full Independence Wave focus tree or safe additive overlay
- decisions and missions
- AI strategy
- former-host relationship
- patron and recognition access
- network and league eligibility
- regional ambitions and formables
- event log, docs, and achievement tracking

Use the regional overlay matrix and package depth levels. Do not bulk-generate identical content and call it complete. Existing meaningful trees remain in place and receive additive content.

## Mechanics

Implement visible, dynamic state for:

- Founding Legitimacy
- International Recognition
- Government Capacity
- Security Readiness
- Post-Release Instability
- former-host relationship
- per-patron influence and dependency
- network standing
- league cohesion, common cause, patron capture, reserve, and member confidence

Focuses, decisions, missions, events, wars, state control, patrons, host actions, and league actions must move these values. Centralize thresholds, caps, duration bands, costs, AI weights, wave tuning, force budgets, and recognition logic.

## Focus content

Implement the shared framework as a real tree with regional and package adaptation.

Required lanes:

- survival and state construction
- government and internal power
- economy, infrastructure, and administration
- army, security, and military identity
- diplomacy, recognition, and patrons
- former host, borders, and expansion
- network, league, formables, and high-chaos ambitions

Required government route families:

- constitutional republic
- popular councils
- traditional restoration
- emergency military rule
- patron client
- hidden radical sovereignty where eligible

Routes need early, middle, and late pacing, tradeoffs, failure states, distinct AI, visible identity changes, varied rewards, decisions, missions, leaders, advisers, flags, units, buildings, claims, and formable links. Implement signature ambition modules for the priority packages in the spec. Do not replace a full branch with one or two decorative focuses.

## Decisions and missions

Implement the accepted rows in `matrices/006_decision_mission_map.csv`.

Use action-based objectives and dynamic costs. Do not make a political-power store. Use equipment, manpower, XP, factories, trains, convoys, fuel, local support, unit placement, supply, legitimacy, recognition, cohesion, patron influence, and time. Provide custom tooltips, target selection, AI equivalents, success, failure, partial success, cooldowns, cleanup, phase gating, mission caps, and exploit controls.

## League and faction

Implement the informal network before the faction. Form the league only after membership, congress, charter, leadership, and common-cause requirements are met.

Implement:

- membership, refusal, associate status, exit, and expulsion
- five charter pillars
- charter route families
- votes and leadership contests
- league goals
- reserve contributions and withdrawals
- rescue calls
- border arbitration
- patron capture
- member confidence
- faction war behavior that matches the charter
- collapse, reform, split, and dissolution

A non-Event 6 country does not normally become a full member. Former hosts need settled claims before observer or treaty status.

## Formables

Implement the data-driven family registry.

- focuses and events reveal or prepare formables
- decisions verify territory, consent, government route, recognition, legitimacy, and member state
- support negotiated, dynastic, revolutionary, military, league, and hidden high-chaos methods
- grant broad immediate cores only for valid consenting regions
- use staged integration for conquered, disputed, large, or mixed territories
- update tag or cosmetic tag, name, adjective, flag, leader, parties, ideas, decisions, focus access, AI, faction, and capital
- clean obsolete pre-formation content

## Evolutions

Implement five true evolution stages with active-event and pre-fire opening effects:

1. Replicable Independence
2. Dormant Nations
3. Armed Birth
4. Sovereign Congress
5. Open Sovereignty

These are working labels. Write final localisation from the spec direction. Do not log ordinary wave counts as evolutions. Respect the evolution enable and disable system.

## Triggerable scenario

Register proposed `SCN-008` with Low, Medium, High, and Maximum intensity.

Every intensity attempts all viable candidates. Intensity changes territory and forces, not candidate count.

Implement scenario types:

- Sovereign Scatter
- Common Congress
- Wars of Separation
- Universal Belligerence with clearly defined selectable rule
- Patron Worlds
- Great Partition

Use the data-driven scenario UI, confirmation flow, type control, four-stop slider, bypass cleanup, and blocked-candidate summary. Manual launch bypasses ordinary chaos, date, evolution, and route prerequisites but preserves impossible-state and terminal-state safety.

## Super-events and achievements

Implement the league formation and dangerous coordinated bloc super-events from the approved text and corrected audio research. Produce both images. Produce and wire the cleared `24` audio package, preserve attribution, and keep `23` absent unless permission or a waiver clears the exact accepted recording. Reopening recording selection requires explicit user approval. Normal waves do not receive super-events.

Implement every achievement in `matrices/006_achievement_matrix.csv`, including tracking, disqualifiers, localisation, icons, docs, origin checks, and scenario restrictions.

## Assets, localisation, docs, and catalog

Produce and wire the complete asset package from the asset prompt. Source real leaders, historical flags, and attested symbols. Generate fictional and alternate-history art. Use real frame-by-frame animation with static fallbacks.

Write final player-facing localisation from the direction in the specs. Do not paste working labels or research gates. Keep Event Details free of effect lists and spoilers.

Update event registration, event log, actor mapping, evolutions, cluster data, Event Details, scenario UI, super-event wiring, docs, manifests, achievements, and the event catalog workbook after final in-game wording exists.

## Required audits and completion

After meaningful tranches, use the appropriate active auditors and write handoffs. Before completion, run:

- focus tree audit
- decision and mission audit
- country package audit
- localisation audit
- documentation cleanup
- spreadsheet update
- event completion audit
- mandatory improvement-loop pass, then resolve its addendum or closure handoff

Provide route coverage, candidate coverage by region and depth, mechanics action map, formable coverage, AI scenario evidence, host-survival tests, Event 5 collision tests, scenario tests at every intensity, asset status, super-event research status, achievement status, docs and catalog alignment, and every simplification or blocker.

Do not claim full completion while any accepted route, package, mechanic, AI path, asset, localisation surface, formable, super-event, achievement, scenario type, audit, or catalog update is missing.

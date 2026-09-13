# Event 062 full implementation prompt

Implement Chaos Redux Event 62, Allies Backstab, from the complete source pack under:

`docs/specs/062_allies_backstab_specs/`

Treat every file under `specs/` as source design and every file under `quality/` as acceptance and evidence requirements.

## Required reading before editing

Read in full:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-event-assets`
- `chaos-redux-super-events`
- `chaos-redux-improvement-loop`
- `chaos-redux-subagents`
- relevant offline Paradox wiki pages
- relevant installed vanilla documentation
- at least one current vanilla and one Chaos Redux precedent for faction removal, war creation, event chains, decisions, missions, ideas, AI, localisation, event pictures, and super-events

Inspect the current repository before trusting provisional paths. Preserve unrelated changes.

Use the HOI4 MCP event workflow. Begin with narrow `hoi4.event_inspect` queries and render the existing chain if one exists. Use compare after implementation.

## Event identity

- Event ID `62`
- entry `chaosx.nr62.1`
- Minor Repeatable
- Chaos level `1`
- Wars cluster, High member
- three Evolutions at `200+`, `400+`, and `600+`

One normal firing must affect at least two valid factions. If fewer than two exist, the event is unavailable and cluster firing skips it.

## Core implementation

Create a global generation and separate transaction receipt for each selected faction.

At event fire:

1. collect valid faction leaders through one bounded scan
2. select multiple factions without replacement
3. snapshot membership, political units, subjects, wars, guarantees, access, capitals, and player roles
4. calculate faction pressure and member vulnerability
5. select weak victims without replacing core protections or strategic utility
6. assign loyalist and expelled roles
7. reconcile subjects and military relationships
8. expel victims with receipts
9. run a one-day delayed legal recheck
10. create or attach the smallest legal war graph
11. open role events, decisions, and missions
12. resolve settlements, outcomes, handoff, and cleanup

Every phase must be idempotent and safe across save and reload.

## Selection

Use the accepted normalized component model for divisions, manpower, equipment, industry, territory, losses, current war situation, contribution, political isolation, and strategic utility.

The faction leader is excluded from baseline victim selection. Strong core members receive major protection without absolute immunity.

Treat an overlord and subjects in the same faction as one political unit. Never place a subject against its overlord without a proven owner-controlled independence receipt.

Respect fresh-faction grace, victim protection, faction cooldown, active-generation exclusion, special-country boundaries, and two-member faction behavior.

## War legality

Do not place a country on both sides of one war. Handle:

- existing loyalist-victim wars
- shared wars against third countries
- expeditionary forces
- withdrawal access
- guarantees and non-aggression
- target or leader death during delay
- faction dissolution
- wider-war handoff

Use immediate legal war, delayed separation war, armed expulsion pending war, or existing-hostility attachment according to proof.

Map the accepted conflict intents to legal current-engine war goals. Territorial settlements may use only registered cores, claims, occupied frontier groups, or accepted transfers.

## Player-facing crisis

Use one ordinary decision category and one public `Crisis Cohesion` value with four stages.

Implement all role actions, missions, dynamic costs, selected-target behavior, idea lifecycle, outcome terms, and cleanup from the decision prompt and source spec.

Do not add a dedicated scripted GUI, focus tree, country, unit, technology, 3D model, portrait, flag, or animation.

## Evolutions

Evolution I expands faction and victim budgets and creates structured co-victim coordination.

Evolution II allows retained members to join victims or withdraw, creating legal internal bloc wars only after tension and side proof.

Evolution III prioritizes large valid factions, applies global mutation budgets, and can trigger the strict one-time global fracture super-event.

Evolution activation adds zero Chaos. Log each Evolution only when its changed behavior becomes real. Respect individual enable states.

## Chaos

Audit the shared faction-leave source. Event 62 forced hostile exits must not receive ordinary negative Chaos for leaving a faction.

Do not duplicate shared war, peace, annexation, puppeting, death, contamination, or faction-join sources.

Implement the one-time world-order fracture source and settlement-violation source only after overlap review. Use stable receipts and Chaos History.

## Connections

Implement bounded integration with:

- Wars cluster
- Random Civil War request ownership
- The Offensive AI posture
- Secret Alliance and faction-formation grace
- A Faction Comes Calling memories
- Subjects Break Free request ownership
- White Peace and settlement reading
- Third Balkan War overlap protection
- Return to Peacetime capacity context
- Famine, Migration, Deaths, Condemnation, and Air Cleanliness ownership boundaries

Do not duplicate another event's transaction.

## AI and probability

Before changing any weighted surface, spawn `chaosx_ai_probability_auditor` with no inherited context and run the baseline scenarios in `quality/062_allies_backstab_probability_scenarios.md`.

After owner implementation and tuning, run `hoi4.probability_compare` with the same scenarios.

AI must understand faction selection, victim choice, side choice, conflict intent, decisions, sponsors, settlement, supply, access, and The Offensive. Invalid actions always have zero probability.

## Assets and super-event

Follow the separate asset and super-event prompts. Produce real final DDS and WAV files, manifests, and handoffs. Do not use placeholders or unapproved reuse.

The Evolution III super-event is not a world-end scenario. It fires once only under the strict proof.

## Achievements

Implement the four achievements from the separate prompt with persistent proof, disqualifiers, localisation, and completed asset triplets.

## Shared systems and documentation

Wire:

- event registration
- default enable state after completion
- event names and debug mapping
- Event Logs history
- Event Details
- Evolution catalog and history
- Wars cluster membership and skip reason
- Chaos History
- super-event slot and sound
- achievements
- event docs
- authoritative catalog workbook and CSV exporter

Do not edit catalog CSV files directly.

## Subagents and audits

Use the sequence in `quality/062_allies_backstab_subagent_handoff_matrix.md`. Every subagent receives a self-contained prompt and no inherited context.

Before completion, run:

- decision and mission audit
- localisation audit
- probability comparison
- improvement-loop planner pass
- event completion audit

Review every handoff. Dispose of every plan as implemented, folded into specs, queued with reason, or rejected with reason.

## Completion report

Report:

- files changed
- event chain and helpers
- selection and transaction evidence
- decision and mission IDs
- AI and probability results
- Chaos deltas
- Evolution tests
- assets and audio
- achievements
- Event Logs and cluster wiring
- workbook export
- acceptance scenario results
- missing validation
- simplifications, fallbacks, and blockers

Do not claim completion while any accepted surface, final asset, AI behavior, localisation, documentation, workbook field, audit, or meaningful validation remains missing.

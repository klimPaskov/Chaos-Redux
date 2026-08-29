# Murder Mystery Specification Part 12: Scripted-System Architecture and Performance

## Architecture goal

Event 39 should be implemented as one owner system with reusable bounded helpers. Baseline investigation, foreign cells, country creation, custom units, subjects, manual scenario setup, and World of Anarchy should call shared Event 39 APIs. Event options must not duplicate that logic.

This file defines ownership and behavioral boundaries. Exact script syntax and file names must be confirmed against the live repository, offline wiki, vanilla documentation, and MCP inspection.

## Event family

The canonical entry remains `chaosx.nr39.1`. Related events should stay in the Event 39 namespace and be grouped by role:

- hidden setup and transaction events
- opening host event
- international news and country reports
- investigation phase events
- incident and attempted-murder events
- successful and failed capture events
- Evolution I through V events
- Assassin State split and reveal events
- foreign cell and revolt events
- country defeat and inheritance events
- World of Anarchy activation, sector, conquest, victory, and defeat events
- manual scenario setup and failure reports

IDs should be reserved in a documented range before implementation. Do not interleave unrelated events or reuse old IDs without a repository-wide search.

## Identifier prefix

New Event 39 identifiers should use one stable prefix such as `chaosx_mm_` or the repository's preferred event-owned naming pattern. The prefix should cover flags, variables, arrays, effects, triggers, constants, ideas, decisions, categories, technologies, units, equipment, characters, cosmetic tags, sprites, and sound IDs.

Once identifiers are wired into saves, manifests, assets, and provider tokens, they should remain stable.

## Owner state groups

### Global lifecycle state

The global owner tracks:

- natural event fired and resolved state
- original host and current central movement actor
- active evolution stage and separate evolution records
- Network Reach
- active cell registry
- movement inheritance count
- Assassin State and derivative registry
- Veiled Compact state
- World of Anarchy readiness, activation, sector, and terminal registry
- one-shot Chaos milestones
- scenario launch identity and cleanup state
- schema or save migration version

### Original-host state

The host tracks:

- Case Progress
- investigation phase
- response philosophy
- evidence integrity stage
- witness safety stage
- intelligence capacity cache
- current protection priority
- current method and adaptation
- active missions and targets
- succession crisis and replacement leader
- incident and role cooldowns
- capture preparation and outcome

### Cell-country state

Each active cell country tracks:

- cell stage and maturity
- Local Case Progress
- current office threat
- local protection priority
- inherited evidence stage
- active mission and route
- revolt readiness stage
- immunity and reseeding state
- movement parent and derivative link

### Assassin-country state

The central state and derivatives track:

- Brotherhood Cohesion
- political route
- command settlement
- custom unit availability and caps
- operations-kit production and sustainment
- selected foreign cell or subject
- faction obligations
- territory and capital package identity
- defeat, inheritance, and cleanup state

## Saved actors and references

Use saved country scopes or the repository's stable dynamic-country reference pattern for original host, central movement, foreign derivatives, and selected target. Character references must use the character registry and owner callbacks.

Every saved actor must have:

- creation point
- validity trigger
- replacement or inheritance rule
- cleanup owner
- save and reload behavior
- no-actor fallback for logs

Do not assume a normal event target can be manually cleared. Follow the shared evolution logger's actor-present contract.

## Registries

### Character disposition registry

Curated rows define target safety, ownership, successor requirements, role pools, and cleanup. Missing rows fail closed.

### Active cell registry

Aligned arrays or the current supported registry structure hold only active or recently immune countries. Every row has a stable country reference and lifecycle fields.

### Assassin derivative registry

Tracks dynamic carrier, origin country, parent movement, territory package, capital, route, subject status, and cleanup. Tag reuse is blocked until full retirement.

### Terminal government registry

Built at World of Anarchy activation and maintained by country-state hooks. It records eligibility, sector, war state, administration outcome, protected exceptions, and victory status.

### Unit provider registry

Event 39 registers one owner provider with the shared Chaos unit-family system and publishes its custom equipment token.

All aligned registries need count validation, duplicate rejection, invalid-row cleanup, and debug repair that does not rebuild the entire world during normal play.

## Core helper responsibilities

### Host and succession helpers

- build valid host pool
- score and select host
- validate current leader and successor
- prepare replacement
- apply opening murder transaction
- record character and event history

### Investigation helpers

- derive national security capacity
- initialize and change Case Progress
- summarize evidence and witness stages
- choose current office threat
- apply protection
- launch and resolve missions
- apply method adaptation
- prepare and resolve final capture

### Character helpers

- build safe role pool
- resolve named or generic casualty
- apply owner-approved removal
- preserve minimum rosters
- record death and cooldown
- process terminal government offices

### Cell helpers

- register and retire cell country
- seed through a concrete route
- change stage and maturity
- initialize Local Case Progress
- select foreign target and route
- apply immunity and reseeding rules
- prepare and cancel revolt

### Country helpers

- preflight original split
- select anchor and grow cluster
- validate original remnant
- reserve carrier and cosmetic identity
- transfer states and set capitals
- initialize economy, technology, stockpile, units, focus, decisions, AI, and agency
- start war after transaction
- create reduced foreign derivative
- resolve defeat and inheritance

### Terminal helpers

- classify ordinary government
- build terminal registry
- select campaign sector
- start bounded war and uprising wave
- process safe leadership pressure
- preflight and apply government dismantling
- create successor administration
- update victory state
- resolve victory or defeat

## Script constants and tuning

Centralize tuning for:

- public value thresholds
- evolution base pacing
- incident cooldown bands
- role cooldowns
- investigation gains and losses
- intelligence capacity factors
- cell caps and stage thresholds
- state-split share bands and viability floors
- unit caps, costs, and sustainment
- scenario intensity ranges
- AI weight factors
- Chaos consequences and one-shot guards
- terminal sector and registry limits

The spec provides behavior and bands. Implementation chooses exact constants after MCP probability and balance inspection. Do not scatter copies across events, decisions, focuses, and effects.

## On-action policy

Use event-owned on-actions only for state changes that genuinely require them, such as country capitulation, annexation, leader transition, unit or equipment registration, peace, and terminal government updates.

Do not introduce a new whole-world daily, weekly, or monthly loop. Investigation pacing should use scheduled events, mission timers, and active-registry pulses. Cell processing iterates only active rows. Terminal updates react to country events and active sectors.

A bounded monthly reconciliation may validate active registries if the live engine requires it. It must not search every country for new cells.

## Idempotence and transactions

Every setup and cleanup helper must tolerate repeated calls without duplicating countries, units, ideas, decisions, flags, registry rows, subjects, faction membership, or history.

High-risk transactions are:

- opening leader murder and succession
- Assassin State split
- foreign derivative creation
- movement inheritance
- World of Anarchy activation
- government dismantling
- scenario launch

Each transaction has preflight, commit, rollback or fail-closed behavior, and postcondition checks. History and evolution records happen only after commit.

## Performance budgets

### Normal investigation

- one original host
- zero to three active missions
- scheduled incidents with cooldowns
- no all-character scan outside pool rebuild moments

### International network

- active-cell registry within phase cap
- one incident or mission resolution per affected country at a time
- spread selection only at explicit network actions or evolution moments

### Assassin movement

- bounded derivative tag pool
- one central actor and limited subjects
- foreign support processes one selected target per action

### World of Anarchy

- terminal registry built once and updated by hooks
- one to three active sectors
- phased war fanout and uprising waves
- no daily whole-world eligibility scan

Performance pressure should reduce future spread or sector fanout before it removes existing content.

## Multiplayer

Event 39 uses one global movement lifecycle and country-scoped investigation views. Every player sees only the decisions and values owned by their country. The original-host player can choose whether to switch to the Assassin State after the split through the existing multiplayer-safe country-switch pattern.

The event must avoid duplicate popups, double setup, and conflicting player control. Scenario host selection and country switch options should identify the initiating player without forcing all players.

Global values, evolution history, cell registry, and terminal state remain synchronized. Local GUI or decision selection values stay country scoped where possible.

## DLC matrix

### La Résistance

Use real agencies, operatives, upgrades, intelligence, and operations where supported. The DLC path must still call the same Event 39 results.

### No La Résistance

Use derived national security capacity, institutional case teams, and decisions. The player receives equivalent core counterplay without fake operatives.

### Other DLC

Country, military, market, designer, special-project, and diplomatic content should use available systems only when the live repo already supports clean DLC branches. Missing DLC cannot remove the complete baseline investigation, country war, unit family, or terminal route.

## Save migration

The owner system needs a schema version. Migration should:

- initialize missing public values safely
- rebuild only Event 39 active rows
- preserve evolution and history records
- repair missing selected targets or invalid country references
- retire duplicate or dead registry rows
- preserve country tags and unit provider identities
- avoid refiring the opening murder

A save from before Event 39 implementation should begin with the event dormant and normal catalog state.

## Event log and debug evidence

The system should record:

- opening host and date
- named or generic incident role and country
- capture operations and results
- local cell creation, stage changes, and dismantling
- Evolution I through V
- Assassin State and derivative creation
- movement inheritance
- World of Anarchy activation and government outcomes
- victory or defeat
- event-owned Chaos changes with reason

Debug logs can expose identifiers and values. Player-facing logs must not show hidden target registries, exact weights, or future route spoilers.

## Required MCP evidence

Implementation and audit should use:

- event inspection, rendering, and comparison for long event chains
- probability inspection and evaluation for every complex weighted surface
- focus inspection, render, rewrite, and comparison for the tree
- technology inspection, render, and comparison for the custom unit branch
- GUI inspection only for the normal category and shared Event Details surfaces that Event 39 touches

If a required route is unavailable, record the exact blocker. Source-only reasoning is not equivalent evidence.

## Documentation ownership

Permanent documentation should include Event 39 event docs, country package, investigation system, character safety registry, cell network, units, Event 19 provider, CXT coverage, 3D package, super-events, triggerable scenario, Intelligence cluster, achievements, and terminal branch.

Temporary `docs/assets/039_murder_mystery/` evidence is deleted only after durable provenance and runtime facts are promoted and no runtime path points into it.

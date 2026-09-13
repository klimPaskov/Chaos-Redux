# Event 067 Generalissimo Scripted-System Prompt

Implement the reusable scripted logic, state ownership, tuning, and lifecycle infrastructure required by Event `067` Generalissimo.

## Required sources

Read in full:

- every file under `docs/specs/067_generalissimo_specs/specs/`
- `docs/specs/067_generalissimo_specs/diagrams/067_generalissimo_state_machine.md`
- every Event 067 handoff and specialist prompt
- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-focus-trees`
- `chaos-redux-subagents`
- `chaos-redux-improvement-loop`
- the shared dynamic-effects and dynamic-triggers registries
- Event 019 claimant-commander implementation
- Event 065 Random Trait implementation
- current Event Logs, Event Details, evolution, scenario, cluster, civil-war, world-end, character, and country-classifier systems
- relevant offline Paradox wiki pages
- current vanilla documentation and examples for characters, civil wars, variables, event targets, script constants, on actions, meta effects, army leaders, country leaders, decisions, and scopes

Use `chaosx_scripted_system_architect` for this bounded surface. The parent agent owns event direction, final cross-file integration, and completion claims.

## Ownership model

Keep Event 067 lifecycle and validation in event-owned files. Likely owners include:

- `common/script_constants/067_generalissimo_constants.txt`
- `common/scripted_triggers/067_generalissimo_triggers.txt`
- `common/scripted_effects/067_generalissimo_effects.txt`
- `common/on_actions/067_generalissimo_on_actions.txt`

Exact paths must follow current repository precedent.

Do not put event stage, influence, demand, removal, coup, focus, or cleanup logic into `chaosx_dynamic_triggers` or `chaosx_dynamic_effects`. Add a shared helper only when its contract is neutral and useful to multiple event families. Document any new shared helper in the matching registry during the same change.

## Tuning and identifiers

Centralize every threshold, cap, duration, chance anchor, influence movement, army-share band, intensity scalar, AI factor, and cooldown in Event 067 script constants or another documented tuning source.

Required stable identities include:

- Event `067`
- entry event `chaosx.nr067.1`
- one canonical Generalissimo character token
- one original-host reference
- one current Generalissimo country reference
- Generalissimo Influence
- Command Cohesion
- four command-authority states
- three evolution milestones
- removal resolution states
- junta civil-war identity markers
- manual scenario `SCN-015`, subject to authoritative collision confirmation
- public world-end branch identity
- bounded world-end actor registry

Do not use numeric variables as boolean substitutes. Use flags for true or false lifecycle state. Use event targets only where a stable scope pointer is required. Clean every global target explicitly.

## Canonical character contract

Create and maintain one fictional male character.

The same token must serve as:

- army commander
- field marshal-rank commander or equivalent maximum supported direct-command role
- country leader after takeover

The system must never fabricate a separate commander clone for peaceful submission, civil war, world-end launch, scenario launch, tag switching, annexation, reload repair, or country transfer.

Provide idempotent helpers for:

- creation
- commander package application
- role transfer
- ruler promotion
- current owner resolution
- portrait and trait consumer synchronization
- removal and death
- invalid-owner recovery
- duplicate detection and fail-closed cleanup

If the engine cannot place one character in two roster ranks simultaneously, preserve one field marshal-rank army leader with all safe positive applicable commander traits and direct military use. Do not create a second character to imitate a second roster entry.

## Trait package

Inspect every current applicable general and field marshal trait.

Create an audit-backed allowlist for positive compatible traits. Record exclusions and their reasons. Do not include traits that:

- corrupt scope or ownership
- represent injury, sickness, demotion, or another negative condition
- require a role the character cannot hold
- create duplicate or invalid behavior
- are event-owned by another package in a way that cannot safely coexist

Set the maximum supported level, Attack, Defense, Planning, and Logistics values through the safest current engine route. Give maximum useful command capacity through a dedicated Event 067 trait or supported field.

Create four dedicated country-leader traits representing strategic command, operational direction, military administration, and supreme authority. Register them in Event 065's normal dynamic trait pool through the current owner-provider contract. Do not hardcode Event 067 traits into a central switch when Event 065 supports provider registration.

## Target validation and selection

Create one reusable valid-host trigger.

A valid host must:

- exist
- be a major or player-controlled country
- use normal civilian systems
- not be an actual nonhuman country
- not be an invalid special Chaos actor
- have a valid government and capital
- be able to own the canonical character
- not already have Event 067 active or resolved
- not already be the current Generalissimo country through scenario or recovery state

For normal targeting, require enough valid territory for the event's possible civil-war path. One-state countries should be excluded unless a proven engine-safe non-war route is explicitly supported by the event stage. Manual immediate-war setup must fail closed for a host that cannot produce two viable sides.

Player-controlled countries and valid majors must enter one complete weighted pool. The selection must not give accidental duplicate weight to a country that satisfies both categories. Use the named selection scenarios in the probability matrix.

## Hidden service record

Before Evolution I, track a bounded hidden service record through sparse owner hooks and concrete military outcomes.

Inputs may include:

- army share under command
- command duration
- major victories
- captured important states
- defense of capitals and strategic regions
- heavy defeats
- relief from command
- public promotion
- loyal subordinate appointments

The hidden record prepares the opening Influence state. It does not display a second public value.

Do not scan every division or country every day. Use bounded owner state, registered objectives, war-state changes, selected strategic states, and scheduled pulses.

## Influence system

Generalissimo Influence is the only public pre-takeover Event 067 value. Clamp it from 0 to 100.

Maintain hidden components only where they improve calculation and AI:

- officer loyalty
- public prestige
- command reach
- coercive reach
- military-industry penetration
- regional-command support
- loyal force share
- civilian counterweight

Each hidden component must affect the public total, a visible chance, a qualitative status, an action requirement, or AI behavior. Do not expose them as persistent public counters.

Create helpers for:

- initial Influence from the hidden service record
- bounded gains and losses
- authority-state changes
- demand results
- victory and defeat transactions
- counterweight effects
- removal chance calculations
- revolt-strength calculations
- clean closure after removal or takeover

Every gain and loss must have one source ledger or event-owned history path sufficient for tooltips and debugging. Avoid duplicate application when the same battle or state capture reaches several hooks.

## Evolution pacing

Implement three actual evolution milestones:

- Evolution I at 200 or higher Chaos
- Evolution II at 400 or higher Chaos
- Evolution III at 600 or higher Chaos

Each must:

- require Event 067 to be active and unresolved
- respect the evolution enable state
- use paced MTTH through the project evolution system
- record the shared evolution context once
- use the canonical host as actor
- unlock its correct stage behavior
- add zero Chaos for evolution activation itself
- remain idempotent across save and reload

A disabled evolution must not set its recorded flag, enable demands, open decisions, schedule an ultimatum, or unlock later stages.

## Demand system

Build candidate pools from current stage, authority, Influence, war state, current concessions, and institutional conditions.

Demand families include:

- supreme command
- operational planning authority
- military appointments
- rival commander removal
- military budget
- loyal officer protection
- military production control
- internal security authority
- emergency powers
- government appointments
- foreign-policy influence
- strategic-industry control
- political opponent removal

Candidate construction must exclude already granted, impossible, obsolete, contradictory, and currently meaningless demands. No empty random list may execute.

Demand timing and AI weights must follow named scenarios. Use the probability auditor before and after any weight change.

## Removal calculations

Create distinct calculation and execution helpers for:

- negotiated retirement
- ordinary dismissal
- arrest at headquarters
- capture during inspection or transit
- assassination
- final removal during the ultimatum

The displayed chance and executed chance must use the same final calculation contract.

Relevant factors include:

- Influence
- command authority
- current army share
- loyal officer network
- internal-security penetration
- capital security
- civilian counterweight
- loyal government reserve
- intelligence preparation
- public prestige
- current location
- wartime emergency
- prior concessions
- prior failed dismissal

Required failure rules:

- failed arrest starts the revolt immediately
- failed capture starts the revolt immediately
- failed assassination starts the revolt immediately
- failed final removal starts the revolt immediately
- failed ordinary dismissal before Evolution III does not automatically revolt
- successful permanent removal ends the crisis and blocks later coup and world-end readiness

Only one coercive removal attempt is allowed in a natural crisis. Save and reload must not restore the attempt.

## Revolt-strength model

Build a deterministic score from Influence and hidden power components, then map it to bounded shares and packages.

The score must resolve:

- army share
- equipment and stockpile share
- defecting commanders
- state and regional-command support
- military factories and bases
- naval assets where relevant
- air assets where relevant
- capital selection
- initial Command Cohesion
- starting officer and administration package

Use bounded army-share targets that can range from a weak revolt near 15 percent to a dominant revolt near 80 percent under extreme conditions. The exact function must be centralized, inspectable, and protected from empty or total-transfer failures.

The legal government must retain a viable capital, command structure, forces, stockpiles, and route to continue the war. The junta must receive a usable force package. Do not solve partition failure with arbitrary fixed states.

## Dynamic civil-war country

Prefer the current engine's dynamic civil-war side.

Identify the junta through stable Event 067 markers and preserve:

- host cores and claims
- appropriate technology
- compatible laws
- equipment identities
- valid templates
- territory and capital
- commander ownership
- wars
- subject and faction settlement state
- dynamic names, colors, flags, and focus loading

Do not reserve a fixed tag unless engine and MCP inspection prove that a required surface cannot work dynamically. A fixed-tag route is blocked until a current collision scan covers vanilla, Chaos Redux, installed Workshop mods, and sibling local mods.

The junta remains human and uses normal civilian systems. Do not add it to `is_actual_nonhuman_country`. Add it to the shared special-country classifier only if an ordinary civilian system truly needs to exclude it, and document the reason.

## Peaceful submission

Provide an idempotent takeover route with no second country.

Required effects:

- Generalissimo becomes ruler
- commander role remains usable
- Influence closes
- Command Cohesion opens
- three starting junta ideas apply
- dedicated focus tree loads
- current forces, technology, stockpiles, cores, claims, subjects, and wars remain
- incompatible political content closes safely
- ruler super-event triggers once
- world-end readiness can later use the canonical ruler state

## Command Cohesion

Clamp from 0 to 100. It is the only public post-takeover Event 067 value.

Provide helpers for:

- initialization after peaceful submission and civil-war victory
- victory, defeat, supply, officer settlement, regional command, purge, council conflict, and reconstruction changes
- route gates
- decision costs and mission difficulty
- low-state penalties and recoveries
- high-state international actions
- closure if the Generalissimo state ends

Do not turn low Cohesion into repeated generic civil wars. Use officer obstruction, command penalties, decision locks, regional disobedience, mission failures, and bounded crisis events.

## Manual scenario

Implement the source logic needed by Generalissimo's Coup.

Proposed ID:

- `SCN-015`

Confirm the ID against the authoritative workbook and runtime registry before use.

Scenario types:

- Favored Commander
- State Within the State
- The Ultimatum
- Generalissimo's War

Intensity stops:

- Low
- Medium
- High
- Maximum

The scenario targets the current player when valid, bypasses normal event timing and evolution prerequisites, consumes the unique Event 067 character opportunity, and never counts as a natural event firing or pacing transaction. Generalissimo's War starts a valid civil war during setup. Bypass state must be tightly scoped and cleared.

## World-end system

Implement the event-owned public branch The Generalissimos' World.

Readiness requires:

- 1000 or higher Chaos
- no active `world_end`
- branch enabled through its independent Event Details toggle
- a living canonical Generalissimo who rules an active or victorious host state
- no successful permanent-removal resolution
- valid world state for bounded transformation

On launch:

- set the shared and Event 067 terminal flags
- freeze ordinary event firing through the existing world-end contract
- trigger the world-end super-event once
- build a bounded actor registry
- classify current military governments, legal civilian governments, vulnerable countries, aligned juntas, rival officer regimes, and resistance-capable states
- initialize International Command, rival military blocs, and Civil Authority Compact only when their membership gates are met

Do not use recurring all-country scans. Register actors once and update them through bounded membership, government-change, war, annexation, and scenario callbacks.

Support these country outcomes:

- existing military government
- peaceful officer takeover
- split-command civil war
- controlled emergency government
- civilian defiance

One-state countries and countries that cannot support a civil war must use a valid non-war outcome or remain resistant. They must not receive a broken partition.

## Event Logs, Event Details, cluster, and Chaos

Provide the event-owned context needed for shared systems:

- normal history actor
- three evolution entries
- event details and availability
- public world-end row and independent toggle
- Military Preparation High-member identity
- valid-target skip reason
- one cluster pacing transaction
- concrete Event 067 Chaos outcomes

Do not add Chaos for evolution activation, Influence thresholds, demand scheduling, or hidden value movement. Add or remove Chaos only for accepted concrete outcomes such as a military revolt, durable peaceful military takeover, restored civilian command, international coup spread, or terminal world transformation. Do not duplicate generic war, annexation, death, or ideology sources.

## Runtime cadence and cleanup

Whole-world daily, weekly, and monthly iteration is prohibited unless the user explicitly authorizes it.

Use:

- event-owned delayed events
- MTTH evolution jobs
- host-local pulses
- registered state and country arrays
- war start and end hooks
- government-change hooks
- annexation and country invalidation callbacks
- bounded world-end actor processing

Cleanup must cover:

- successful removal
- failed removal and revolt
- peaceful submission
- government victory
- junta victory
- annexation by a third party
- Generalissimo death
- original host disappearance
- scenario launch
- world-end launch
- world-end actor invalidation
- save and reload repair
- invalid event targets
- duplicate character recovery

## Probability evidence

Use every relevant named scenario from `067_generalissimo_probability_scenario_matrix.md`.

The probability auditor must:

- begin with `hoi4.probability_inspect`
- state candidate-pool completeness
- distinguish exact, bounded, sampled, score-only, and unresolved results
- evaluate targeting, demands, AI decisions, removal, civil-war allocation, focus routes, scenario intensity, world-end outcomes, and bloc behavior
- use `hoi4.probability_compare` after any weight patch against the same scenarios

Do not ask the probability tool to prove exact chances when the candidate pool or external game state is incomplete.

## Validation and handoff

Return a handoff under:

`docs/plans/067_generalissimo_plans/subagent_handoffs/`

Include:

- files changed
- constants, flags, variables, event targets, helpers, and call sites
- before and after behavior
- character idempotence proof
- target-selection evidence
- evolution and demand state transitions
- displayed and executed removal chance consistency
- revolt-strength test cases
- dynamic civil-war country proof or exact blocker
- scenario and world-end registries
- classifier disposition
- cadence and cleanup ownership
- MCP event and probability evidence
- meaningful validation gaps
- all remaining integration work for the parent

Do not claim Event 067 complete. This subagent owns the bounded scripted-system surface only.

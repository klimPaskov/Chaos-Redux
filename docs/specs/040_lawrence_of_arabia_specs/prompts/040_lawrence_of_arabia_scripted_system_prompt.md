# Event 40 Scripted-System Architecture Prompt

Use `chaosx_scripted_system_architect` to design and, where parent-authorized, implement the bounded Event 40 runtime architecture.

## Context

Event 40 is a Minor Fire-Once event with one initial random entry and a longer internal regional chain. Only one country is the active intervention target at a time. The public target value is Lawrence's Influence. Regional outcomes persist and affect later targets. Three evolutions add revolt networks, a regional client system, and federation formation.

## Required reading

Read:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-subagents`
- shared dynamic trigger and effect documentation
- all Event 40 specs and acceptance scenarios
- relevant offline wiki and vanilla documentation for variables, event targets, arrays, effects, triggers, delayed events, characters, subjects, and state transfer

## Required architecture

Design event-owned contracts for:

- target eligibility and target scoring inputs
- Britain sponsor eligibility and capability
- one active target
- campaign generation ID
- active phase
- Lawrence's Influence and band evaluation
- trend and confirmation windows
- active routes and map targets
- British commitment receipts
- evidence and turned-contact state
- Evolution I cell families
- settled-country regional nodes
- settlement identity
- character state
- delayed next-target selection
- campaign completion and cleanup
- federation readiness
- federation transaction, proof, and rollback
- Federal Authority after formation

## Scope and persistence

Use regular event targets for one effect chain. Use global event targets only when the reference must survive beyond the chain and provide explicit cleanup.

Use country flags for true or false persistent state. Use variables for scaled values. Use script constants for shared tuning values when supported.

Temporary variables are unscoped. Do not write scoped temporary-variable access.

Use generation IDs and one-shot proof flags so delayed events, decisions, missions, and aid receipts cannot apply to a replaced target or later campaign generation.

## Processing model

Do not add whole-world `on_daily`, `on_weekly`, or `on_monthly` iteration.

Use:

- event-driven recalculation
- active target callbacks
- registered settled-node arrays
- country-local periodic processing where an existing permitted hook supports it
- delayed events with generation proof
- explicit refresh after relevant decisions, missions, wars, annexation, character changes, and evolution activation

## Influence transaction

Create one event-owned helper that:

- requires active-target and generation proof
- receives a signed change through an accepted variable contract
- clamps the result to `0-100`
- records recent direction
- updates the qualitative band
- starts or clears confirmation windows
- refreshes decision presentation
- never registers Chaos by itself

Do not put this event-owned helper in `chaosx_dynamic_effects` unless a later review proves that other event families need the same neutral contract.

## Settlement transaction

Create one bounded settlement gateway that:

- validates active target and generation
- validates outcome requirements
- consumes one outcome ID
- applies the relationship, idea, access, and character consequences once
- writes durable target settlement identity
- removes active decisions and missions
- updates regional-node data
- queues the next-target delay only when continuation remains valid
- clears active target state
- preserves History and evolution data

## Character state

Use one canonical Lawrence character and one explicit state machine.

States include:

- concealed
- British liaison
- field adviser
- political adviser
- wounded
- detained
- expelled
- defected
- federation architect
- federation leader
- retired
- dead

Every transition validates current state and removes incompatible roles before adding the new role.

## Evolution activation

Each evolution helper must:

- check the evolution enable state
- set the shared evolution log context
- record the milestone once
- unlock only its own behavior
- support active-event and pre-fire entry
- give zero direct Chaos

## Federation transaction

Design a request, validation, apply, and rollback structure.

Validation covers:

- outcome ID
- core candidate
- participating countries
- member consent
- territory and capital
- player countries
- wars and subjects
- forces and equipment
- leaders and Lawrence role
- country carrier availability
- supply and viability

Apply covers:

- freeze participants
- snapshot proofs required for rollback
- create or transform the core
- transfer accepted territory and state rights
- transfer or reconcile forces, stockpiles, manpower, technology, wars, subjects, and player control
- assign government, ideas, focus tree, flags, and AI origin
- begin Federal Authority
- close the intervention campaign
- fire the correct super-event only after success

Rollback restores every modified participant and removes the incomplete federation.

## Shared-system boundaries

Use existing shared helpers for:

- exact population loss when a proven Event 40 consequence needs it
- stockpile debits
- special Chaos and nonhuman classification
- Deaths, Famine, Migration, and Chaos owner contracts

Do not add Event 40 lifecycle logic to shared classifiers or shared registries.

## Handoff

Return:

- proposed files
- helper and trigger IDs
- public inputs and outputs
- persistent variables, flags, arrays, and targets
- call-site map
- generation and rollback model
- lifecycle diagram
- performance analysis
- engine uncertainties
- tests tied to acceptance scenario IDs
- any narrow implementation patch made
- remaining parent work

# Gods of Africa implementation map

## Implementation goal

Add Gods of Africa as a persistent Event 012 subsystem that creates a capacity-based tribute relationship between the African unifier and every valid major or player-controlled country.

The implementation must preserve the accepted design without assigning Event 070, adding a third public value, or granting punishment above the current Strength ceiling.

## Pre-edit requirements

Before editing the repository:

1. Read `AGENTS.md` and every relevant project skill.
2. Read the complete Event 012 specs, plans, docs, events, decisions, focuses, localisation, assets, AI, and scenario files.
3. Inspect the authoritative Event 012 African unifier target, establishment proof, continent-control ledger, evolution state, victory trigger, and SCN-011 path.
4. Inspect Event 070's current live files and authoritative XLSX row so its old Gods entry can be removed without deleting unrelated work.
5. Read the required offline Paradox wiki pages.
6. Read current vanilla documentation and direct vanilla precedents for events, decisions, missions, scripted localisation, event targets, AI, and any GUI surface accepted.
7. Use `hoi4.event_inspect` and `hoi4.event_render` to map Event 012 before editing.
8. Use `hoi4.focus_inspect` and `hoi4.focus_render` if the focus overlay branch is implemented.
9. Use `hoi4.probability_inspect` before analyzing any weighted selector or AI choice.

## Stage 1: source reconciliation

### Event 012 audit

Identify:

- exact entry event and subevent ranges
- African unifier carrier or event target
- Event 012 activation, establishment, and cleanup flags
- Evolution I, II, and III proofs
- participant, claimant, congress, aid, guarantee, base, sanction, and victory systems
- existing Event 012 decision categories
- existing African unifier focus tree
- existing super-event slots and audio
- Event 012 docs and spreadsheet wording

### Event 070 migration audit

Identify:

- event registration
- event script
- event name mappings
- default enabled state
- event details
- catalog row
- any old Gods code, assets, or localisation

Disposition:

- remove or archive only the old Gods of Africa assignment
- preserve Event 070 as a free ID
- do not invent its replacement idea during this task
- remove stale `nr70` Gods references from player-facing surfaces

## Stage 2: owner data and constants

Create or extend Event 012 owner files for:

- Strength range and bands
- Wrath range and bands
- Wrath transaction values
- demand cooldown bands
- deadline bands
- burden shares
- protected floors
- active-demand global budget
- recent-family cooldowns
- punishment tier gates
- Tier V gates
- protection cooldowns
- participant onboarding cadence
- final outcome weights and disqualifiers

Use script constants for shared tuning where supported.

## Stage 3: scripted trigger architecture

Owner triggers should include:

- system can activate
- valid African unifier
- valid participant
- participant belongs to current generation
- participant can receive ordinary demand
- participant can be registered
- participant has active demand
- participant can offer substitute
- participant can request extension
- participant can defy
- participant can seek reconciliation
- Africa can grant leniency
- Africa can mark offender
- Africa can protect participant
- demand family valid for participant
- Africa needs demand family
- participant has capacity for demand family
- punishment tier valid
- punishment family valid
- Tier V full gate
- final Favored eligibility
- final Respected eligibility
- final Enemy eligibility

Do not add owner lifecycle or Event 012 stage logic to the shared `chaosx_dynamic_triggers` registry.

## Stage 4: scripted effect architecture

Owner effects should include:

- initialize Gods system
- start consolidation delay
- activate system
- register participant
- archive invalid participant
- recalculate Strength
- apply Wrath transaction
- enforce Wrath floor
- build African need profile
- build target capacity profile
- select demand participant
- select demand family
- calculate demand amount
- calculate demand deadline
- build substitute set
- create demand contract
- resolve full compliance
- resolve partial compliance
- submit substitute
- resolve substitute
- request extension
- resolve extension
- refuse demand
- fail demand
- declare defiance
- start reconciliation
- complete reconciliation
- evaluate punishment
- apply punishment family
- call Event 013 disaster gateway
- apply exact population-loss wave
- issue protection
- set African priority
- mark priority offender
- grant leniency
- commit final settlement
- resolve participant final outcome
- terminate system after African defeat
- clean participant state
- clean system state

Shared helpers should be reused when their contracts match. A new helper belongs in `chaosx_dynamic_effects` only when its contract is neutral and several unrelated systems will call it.

## Stage 5: activation and participant registry

Implement:

- Evolution I gate
- 180-day consolidation delay
- activation fail-closed checks
- one-time participant initialization
- deterministic demand staggering
- later major and player onboarding
- participant generation proof
- introduction event
- Africa-side category visibility
- Event 012 log milestone

Test:

- Africa disappears before activation
- evolution disabled
- delayed recovery after temporary crisis
- player-controlled minor registration
- later major registration
- no duplicate participant

## Stage 6: Strength

Implement the composite Strength calculation from:

- military readiness
- industry and logistics
- continental control
- strategic reach
- internal condition
- Chaos and evolution amplifier

Requirements:

- `0 to 100` clamp
- five cached bands
- smoothing for ordinary changes
- immediate response to major defeat
- owner-local refresh
- no per-participant recalculation
- clear player tooltip

Test:

- weak unifier remains in limited band
- continent-wide industrial major reaches global or extreme band
- capital loss lowers Strength
- high Chaos cannot carry a powerless Africa to extreme band

## Stage 7: Wrath and hidden history

Implement:

- central Wrath transaction helper
- reason constants
- band cache
- war, occupation, broken-treaty, and defiance floors
- compliance and aid reductions
- refusal and failure gains
- hidden history counters and flags
- qualitative public feedback

Test:

- one participant's action does not affect another's Wrath
- floor prevents payment exploit
- one last payment cannot erase permanent grievance
- save and reload preserves history

## Stage 8: demand families

Implement demand families in tranches.

### Tranche A

- infantry equipment
- support equipment
- motorized
- artillery where helper support exists
- fuel
- convoys
- trains
- industrial support
- recognition
- territory return

### Tranche B

- tanks
- aircraft
- strategic resources
- continuing support contracts
- military assistance
- access and basing
- end support for African enemy

### Tranche C

- alliance and faction concessions
- foreign-base removal
- sanctions and later Evolution III routes

Each family requires:

- Africa need proof
- participant capacity proof
- protected floor
- amount rounding
- valid debit and Africa credit
- deadline
- substitutions
- AI behavior
- localisation
- DLC parity
- cleanup

Do not mark the system complete after Tranche A if the accepted Event 012 evolution content requires the later families.

## Stage 9: decision and mission layer

Implement the participant category with:

- two meters
- one active demand mission
- five-action maximum
- phased substitution UI
- extension
- refusal
- permanent defiance confirmation
- voluntary aid
- defiant preparation decisions
- reconciliation route

Implement the Africa-side category with:

- current Strength
- current doctrine and priority
- selected-target flow
- leniency
- offender marking
- protection
- pardon
- escalation
- grouped reports

Run the decision and mission auditor after the full category exists.

## Stage 10: punishment and protection

Implement tier selection from separate desired and capability values.

Required invariants:

- first ordinary refusal capped
- low Strength caps at Tier I
- extreme route requires every gate
- recent-family and extreme cooldowns
- Event 013 gateway for natural disasters
- exact Deaths transaction for population loss
- no duplicate Chaos
- attribution and Condemnation integration
- target-condition scaling
- real African cost for protection

Test each tier with a named scenario and inspect exact effects.

## Stage 11: focus integration

Add the Event 012 overlay branch only after inspecting the live tree.

Required route groups:

- preparation and proclamation
- reciprocal doctrine
- extractive doctrine
- Provision
- Oaths
- Protection
- Judgment
- Evolution II expansion
- Evolution III expansion
- continental settlement

Use focus MCP inspect, render, rewrite if needed, compare, and audit.

## Stage 12: AI and probability

Weighted surfaces:

- participant response
- defiance
- substitute acceptance
- extension acceptance
- African priority
- target selection
- demand-family selection
- punishment-family selection
- protection target
- focus route

Process:

1. baseline probability audit with named scenarios
2. parent or owner patch
3. comparison with the same scenarios
4. record exact, bounded, sampled, score-only, or unresolved status

Do not claim exact probabilities from incomplete candidate pools.

## Stage 13: events and writing

Write final player-facing text for:

- activation
- participant introduction
- demand families
- negotiation
- refusal and failure
- punishments
- protection
- defiance
- reconciliation
- Africa defeat
- final outcomes
- Event Details and logs

Use the localisation direction in the source spec.

Run the localisation auditor after all visible text exists.

## Stage 14: assets

Register stable sprite names before asset production.

Route:

- generated event and category art to generated event art worker
- icons and achievements to icon artist
- super-event quote to text researcher
- super-event audio to audio researcher

Inspect the canonical reference family for each asset.

Process and wire:

- source PNG
- final PNG preview
- DDS
- GFX
- gameplay consumer
- manifest and permanent provenance

Do not use placeholders or resized cross-type icons.

## Stage 15: super-event

Implement one credibility super-event only if the accepted threshold remains justified after Event 012 inspection.

Requirements:

- one-time Strength threshold
- unique slot or intentional existing Event 012 slot
- sourced quote
- sourced cultural remark if used
- unique licensed musical track
- final WAV
- sound definitions and volume wrappers
- settings-aware playback
- image and scripted localisation
- docs and catalog

Weak-Strength activation uses normal news until the threshold is reached.

## Stage 16: endings

Implement:

- African unifier destroyed before activation
- African unifier destroyed after activation
- participant capitulates Africa
- Event 012 restoration generation
- secured-continent settlement
- four final relationship outcomes
- World Is One relationship input
- demand and punishment cleanup

## Stage 17: documentation and catalog

Update:

- Event 012 source specs if implementation decisions change accepted design
- Event 012 public documentation
- Event 012 system documentation
- Event 012 focus and decision docs
- super-event research doc
- audio catalog
- asset provenance and coverage
- authoritative XLSX Events row for Event 012
- authoritative XLSX Scenarios row for SCN-011 if needed
- Event 070 row to remove the old assignment

Run the CSV exporter after the workbook save.

Never edit the three CSV exports directly.

## Stage 18: audits and completion

Required final passes:

- decision and mission auditor
- focus auditor
- localisation auditor
- AI probability auditor
- country package auditor for African unifier integration
- event completion auditor
- spreadsheet worker
- improvement-loop planner after implementation tranches and again near closure only when the previous addendum is resolved

A full GUI adds the event UI worker and mandatory MCP GUI evidence.

## Completion proof

The final report should list:

- files changed
- identifiers added or changed
- Event 012 integration points
- demand families
- punishment tiers
- protection routes
- focus route coverage
- AI probability scenario results
- multiplayer scenarios
- assets and super-event status
- documentation and workbook updates
- meaningful validation
- remaining blockers
- every deviation or simplification

Do not claim completion while Event 070 still owns Gods of Africa, any accepted demand family is missing, protection is absent, AI is incomplete, or punishment can exceed Strength.

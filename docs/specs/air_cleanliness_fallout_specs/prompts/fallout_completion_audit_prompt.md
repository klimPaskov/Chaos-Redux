# Fallout Living World Completion Audit Prompt

Run a read-only completion audit of the implemented Air Cleanliness and Fallout system against the complete accepted source design, corrected ownership rules, repository implementation plan, and living-world expansion.

Do not edit gameplay files. Write the audit under `docs/plans/air_cleanliness_fallout_plans/subagent_handoffs/`.

## Required inputs

Read:

- `AGENTS.md`
- all files under `docs/specs/air_cleanliness_fallout_specs/`
- all accepted and unresolved files under `docs/plans/air_cleanliness_fallout_plans/`
- current gameplay, localisation, GUI, GFX, asset, audio, and documentation files, plus workbook and catalog exclusion evidence
- relevant local engine documentation and vanilla precedents
- prior implementation handoffs and audit reports

Build a disposition table for every accepted plan and addendum.

## Ownership audit

Confirm:

- every Fallout event definition is in `events/fallout_world_end_events.txt`
- every Fallout event uses `chaosx.fallout.*`
- no Fallout event remains in chemical warfare, zombie, generic scenario, or another feature event file
- no caller uses a non-Fallout event id
- no Fallout asset points into another feature folder
- no zombie event id, file, namespace, image, icon, portrait, flag, GUI texture, sound, music, or sprite path is reused
- Fallout does not use the normal super-event system
- the manual scenario id equals the previous live maximum plus one and did not renumber existing entries

Treat any failure as blocking.

## Air Winter audit

Confirm the complete state phase 0 through 6 model.

Audit:

- phase calculation
- exposure, recovery, adaptation, food, shelter, and reclamation values
- state population effects through the shared Deaths system
- building, infrastructure, railway, supply, port, power, factory, and repair effects
- state category degradation and recovery
- military supply, movement, attrition, organization, and reinforcement effects
- disease and medical interaction
- winter flavour events with actual effects
- AI adaptation
- save and load migration
- performance and monthly iteration ownership

Confirm both presentation layers:

1. dedicated winter mapmode
2. visible colder normal-map presentation

The normal-map audit must compare phase and visual class. Universal snow, mapmode-only completion, unreadable overlays, or visual states that disagree with mechanics are blocking defects.

## Fallout transition audit

Confirm:

- all request sources use one idempotent coordinator
- eligibility can begin at 100 percent Air Contamination
- scripted terminal callers and manual scenario can request Fallout without 1000 Chaos
- blackout is a dedicated full-screen scripted GUI
- text sequencing, input blocking, pause behavior, save-load behavior, and multiplayer behavior work
- the rewrite is deterministic and bounded
- player continuation is preserved before general successor assignment
- state grading, wasteland conversion, government change, country assignment, population, building, supply, and category changes match the accepted design
- no normal super-event appears

## Manual scenario audit

Verify with engine evidence that every valid province receives a real thermonuclear strike.

Confirm:

- valid province definition
- no sea, lake, invalid, or placeholder targeting
- thermonuclear classification
- actual strike visuals and effects
- synthetic batch aggregation
- exact seven-day delay after the final strike batch
- standard blackout and rewrite on day seven
- save-load persistence
- multiplayer determinism
- intensity changes aftermath severity without reducing strike coverage

One strike per state, province modifiers, or variable-only fallout do not satisfy the requirement.

## Event library audit

Count real `chaosx.fallout.*` event blocks by primary family.

The release floor is 660 manually reviewed blocks. Report actual counts and compare them with:

- transition and orientation
- global survival and society
- regional and biome
- government archetype
- successor country memory
- character and leader
- diplomacy, trade, war, and settlement
- cause memory, fictional altered content, and ecology
- recovery and late world order

Raw count is insufficient. Sample every family for:

- distinct eligibility
- real conflict
- meaningful choice
- actual effects
- AI choice
- memory
- delayed result
- partial success or failure
- callback
- cleanup
- event-log behavior
- asset and localisation coverage

Flag template events that differ only by replaced nouns.

## Coverage audit

Verify:

- nine regional visual and event classes
- twelve government archetypes
- four linked country-memory arc obligations for every selected successor
- an explicit disposition for all 99 candidate successors
- recurring character arcs that alter gameplay roles
- contact, recognition, trade, refugee, border, war, armistice, settlement, annexation, migration, and integration support
- all supported Fallout causes
- fictional mutant boundaries
- Years 5 through 10
- Year 10 onward repeatability without event exhaustion

Every surviving playable country must have non-generic Fallout focus content and connected decisions, ideas, AI, events, and assets.

## Event pacing audit

Test the scheduler for:

- ash-week orientation lock
- active arc caps
- family fatigue
- ordinary cooldown
- crisis interruption
- bilateral reservations
- country-size scaling
- war and compact replacement of routine events
- player-facing volume near the planned 90 to 180 events over ten years
- hidden AI resolution
- save and load recovery
- multiplayer host authority

Flag popup floods, event starvation, same-family repetition, dead arcs, and deterministic loops.

## Choice and balance audit

Check that important options use varied costs and tradeoffs.

Flag:

- repeated political-power purchases
- obvious best options
- harmless failure
- tiny standalone modifiers
- free unit or resource loops
- repeated state damage with no recovery path
- unchecked snowballing
- AI suicide
- invalid bilateral targets
- dead characters still acting
- annexed countries retaining arcs
- stale decisions or missions
- route changes that do not update events

## Text and localisation audit

Confirm final text exists and working labels were not pasted as final localisation.

Audit:

- missing and duplicate keys
- encoding
- dynamic actor, country, state, value, route, and character text
- regional specificity
- choice clarity
- effect tooltip clarity
- quote and cultural-reference sourcing
- no em dashes or semicolons
- no staccato filler
- no generic apocalypse language
- no staged contrast formulas
- no process or rework language
- no claim that fantasy mutants are ordinary radiation science

## Asset audit

Confirm:

- dedicated Fallout paths and manifests
- report and news image coverage
- successor flags and portraits
- recurring character portraits
- focus, idea, decision, category, achievement, and GUI icons
- climate presentation assets
- static fallbacks for animation
- historical sourcing rules
- generated fictional asset rules
- no placeholders on completed visible content
- no normal Fallout super-event image or audio slot

## Documentation and catalog-exclusion audit

Confirm:

- source specs, plans, event docs, system docs, asset manifests, and handoffs agree
- the event workbook and exported catalogs contain no Fallout rows or Fallout-specific fields
- every accepted plan has a disposition
- no stale event-numbered Fallout folder, fixed scenario id, zombie ownership, 1000-percent-only trigger, or super-event claim remains as current guidance

## Output

Provide:

- completion status by surface
- event counts by primary family
- coverage table for regions, archetypes, successors, characters, diplomacy, causes, and late game
- missing or simplified requirements with file evidence
- accepted-plan disposition table
- engine proof results
- task-specific validation performed
- asset, localisation, AI, and documentation gaps
- blockers
- recommended next actions
- closure recommendation only when no accepted requirement, fallback, placeholder, or blocker remains

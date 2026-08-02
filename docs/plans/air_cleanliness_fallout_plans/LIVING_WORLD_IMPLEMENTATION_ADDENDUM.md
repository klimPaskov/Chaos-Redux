# Living World Implementation Addendum

## Purpose

This addendum extends the corrected repository implementation plan with the Fallout event ecosystem and normal-map climate presentation defined in the living-world source specs.

It does not change the order of the existing proof gates. Air Winter phase logic, mapmode proof, normal-map visual proof, blackout proof, province-wide strike proof, scenario id allocation, and tag conflict work remain prerequisites.

## New implementation surfaces

Primary gameplay files:

- `events/fallout_world_end_events.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt` when event helpers need separation from rewrite helpers
- `common/scripted_triggers/fallout_consolidated_triggers.txt` when event eligibility helpers need separation
- `common/script_constants/fallout_consolidated_constants.txt`
- `common/on_actions/fallout_world_end_on_actions.txt` only for narrow lifecycle hooks
- `common/scripted_localisation/fallout_consolidated_scripted_localisation.txt`
- dedicated Fallout decision, idea, focus, AI, country, GUI, GFX, and localisation files already mapped by the corrected plan

The event definitions remain in one dedicated Fallout event file unless verified local engine or repository rules require a stronger physical split that retains the Fallout namespace and ownership.

## Event ledger

Create a maintained ledger under the plan folder before adding the first event block.

The ledger records:

- event suffix
- primary family
- working design anchor
- final localisation keys
- country or region ownership
- event class
- visible or hidden status
- caller
- follow-up
- cooldown family
- asset
- implementation batch
- audit status

Do not reserve guessed suffix ranges. Scan the dedicated event file and allocate stable free suffixes.

## Scheduler implementation order

1. Fallout timeline phase
2. country event eligibility
3. family fatigue
4. ordinary cooldown
5. active major-arc reservations
6. bilateral reservation
7. weighted candidate construction
8. host-authoritative selection
9. visible player event or hidden AI resolution
10. memory, delayed result, callback, and cleanup
11. save and load recovery
12. debug inspection and event-log support

The scheduler must not build a full global candidate pool every day. Use bounded periodic checks and current-scope candidates.

## Pilot batch

The pilot begins only after Air Winter passes its tranche gate.

Required pilot countries:

- one small successor
- one large successor
- one maritime or island successor
- one fictional altered successor

They must use different regions and government archetypes.

Required pilot event coverage:

- orientation
- food
- water
- medicine
- shelter
- power
- salvage
- first winter
- one climate visual-class incident per class
- one complete government-archetype chain
- one opening, domestic, external, and late identity chain for each pilot successor
- five recurring characters
- first contact
- recognition
- trade
- refugee pressure
- border dispute
- war cause
- armistice
- settlement
- first reliable harvest
- Year 2 government settlement

The pilot should be large enough to expose repetition and scheduler problems, but small enough for manual line-by-line review.

## Pilot exit gate

The pilot passes when:

- no event is defined outside Fallout ownership
- event suffixes are unique
- orientation blocks ordinary events until complete
- family fatigue prevents immediate repetition
- active arcs do not overlap incoherently
- bilateral events reserve both countries
- annexed or invalid actors clean up
- AI resolves equivalent content
- visible event volume matches the pilot budget
- every event changes real state
- final text is regional and government-aware
- assets exist or have accepted handoffs
- save and load resume active arcs
- multiplayer clients do not choose global outcomes
- event log and debug inspection expose the active family and arc
- the completion auditor finds no copied template chain

## Scale-up batches

### Shared layer batch

Complete global, regional, archetype, character, diplomacy, cause-memory, altered-fiction, recovery, and late-world-order foundations.

### Successor batches

Process successors by region. Before each batch:

- confirm selected tags and state groups
- confirm leader and flag plan
- confirm government archetype
- confirm survival profile
- confirm focus overlay
- identify unique founder conflict
- identify external behavior
- identify late ambition
- identify regional event overrides

After each batch, run country, focus, decision, localisation, and completion audits.

### Late campaign batch

Complete Years 5 through 10, generation change, thaw, ultraviolet hazards, constitutional settlements, interregional blocs, late wars, and repeatable Year 10 onward content.

## Event count reporting

Report counts by primary family after every batch.

A block counts only when it has:

- final implementation
- final keys
- AI behavior
- effects
- memory or closure where needed
- cleanup
- asset disposition
- audit status

Do not count comments, debug events, empty wrappers, compatibility shims, or copied variants that differ only by a substituted noun.

## Normal-map climate integration

The living-world specs add a hard normal-map presentation requirement.

The implementation handoff must record:

- verified engine surface
- exact asset type
- visual-class selector
- phase selector
- update cadence
- multiplayer behavior
- interaction with terrain, political, supply, and unit readability
- static fallback
- performance
- unsupported visual channels

The winter mapmode remains required even when the normal-map layer works.

## Documentation and catalog

After each implementation batch, update:

- Air Cleanliness system doc
- Fallout system doc
- event ownership doc
- event ledger
- successor package status
- asset manifests
- event catalog
- scenario catalog
- workbook after final localisation exists
- plan disposition table
- continuation or resume handoff

## Improvement-loop checkpoint

Run a new improvement-loop pass after the pilot, not before.

The pass should evaluate:

- popup density
- family repetition
- copied structure
- regional distinction
- government distinction
- choice strength
- character memory
- bilateral coherence
- AI behavior
- normal-map climate readability
- event art repetition
- Year 2 pacing

Resolve the result before scaling to the release floor.

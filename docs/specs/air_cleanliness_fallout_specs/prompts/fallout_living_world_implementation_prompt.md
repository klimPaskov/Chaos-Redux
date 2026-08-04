# Fallout Living World Implementation Prompt

Implement the accepted Air Cleanliness and Fallout source design together with this living-world expansion. Work in the writable Chaos Redux repository and treat `docs/specs/air_cleanliness_fallout_specs/` as the canonical source-spec area.

## Required reading before edits

Read:

- `AGENTS.md`
- the complete Air Cleanliness and Fallout source-spec package
- the corrected Fallout event and asset ownership rules
- the corrected manual scenario plan
- the existing implementation-tranche plan
- all required local offline Paradox wiki pages
- official Hearts of Iron IV documentation in the local game installation
- relevant vanilla files
- existing Chaos Redux mapmode, scripted GUI, event-log, Deaths, Air Contamination, scenario, country, focus, decision, and asset patterns

Do not begin a gameplay edit until the local engine proof gates have been recorded.

## Independent Fallout ownership

All Fallout events belong in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.

Do not define a Fallout event in chemical warfare, zombie, generic scenario, or another feature event file. Do not reuse another feature's event namespace, event suffix, report image, portrait, icon, GUI texture, audio wrapper, music, sprite path, or asset folder.

The generic manual-scenario framework may dispatch to a Fallout-owned entry event. The request, countdown, blackout, rewrite, continuation, orientation, survival, regional, government, character, diplomatic, war, recovery, and late-game chains remain Fallout-owned.

Fallout is not a normal super-event. Remove stale super-event image, quote, reaction, slot, and audio wiring.

## Local proof gates

Before content implementation:

1. prove the exact normal-map climate presentation route
2. inspect the live mapmode strips, frames, and available slot
3. prove the exact thermonuclear effect for every valid province
4. allocate the manual Fallout scenario as highest live scenario id plus one
5. prove full-screen blackout drawing order and input blocking
6. build the live tag and country-package conflict ledger
7. scan all Fallout event definitions, callers, suffixes, flags, variables, assets, and old ownership
8. record local source paths and unsupported engine behavior

Do not replace a failed proof with a quiet approximation.

## Air Winter and visible climate

Implement the accepted state phase 0 through 6 model before the Fallout rewrite.

The winter system must affect:

- state population through the shared Deaths pipeline
- shelter and displacement
- food output and reserve pressure
- infrastructure, rail, supply hubs, ports, power, factories, and repair burden
- state category degradation and recovery
- unit supply, movement, attrition, organization, and reinforcement
- disease and medical pressure
- adaptation and reclamation capacity
- event eligibility and event weights

Implement a dedicated winter mapmode with ordered phase colors and useful tooltips.

Also make the world visibly colder in normal map presentation. The visual state must follow region and phase. Do not cover every biome in the same snow texture. Use the accepted visual classes for snow, frost, cold rain, ash, dead vegetation, frozen water, dim light, dust, and delayed thaw. If the engine cannot support one planned visual channel, report the exact blocker and preserve the other verified channels. Do not call a mapmode-only result complete.

## Fallout event engine

Build a Fallout-owned event scheduler that supports:

- timeline phases
- country size and player status
- regional and biome pools
- government archetype pools
- country-memory overlays
- cause memory
- winter phase
- survival-resource crises
- active character and institution arcs
- bilateral reservations
- family fatigue and cooldown
- active arc caps
- event memory
- delayed results
- hidden AI resolution
- multiplayer determinism
- save and load recovery
- cleanup after annexation, tag change, government change, death, migration, and route closure

The normal random-event picker must not own this pacing.

## Event library

The release floor is 660 manually reviewed Fallout event blocks. The planned ceiling is 910.

Use the matrices as design obligations. Do not bulk-generate a large event file and call it complete. Every block must be manually reviewed and customized.

A major chain needs an opening, conflict, choice, delayed result, success or partial success or failure, memory, callback, and cleanup.

A routine incident must still change a resource, state, relationship, character, mission, route weight, population movement, repair state, market, corruption, or adaptation value.

The player-facing campaign target is 90 to 180 meaningful events over ten years. Enforce cadence, family fatigue, and arc caps so the large library produces variation without spam.

## Implementation batches

Implement in reviewable batches.

### Batch A: engine and pilot

- orientation flow
- scheduler, memory, fatigue, and arc helpers
- twenty global survival anchors
- one regional pilot from each visual class
- one complete government archetype
- four pilot successors with different regions and governments
- five recurring character arcs
- first contact, trade, refugee, border, war, and peace pilot chains
- first-winter and Year 2 recovery milestones

Run scripted-system, decision, localisation, and completion audits.

### Batch B: full shared layers

- remaining global anchors
- all regional pools
- all twelve archetypes
- character-role library
- diplomacy, trade, war, and settlement library
- cause-memory and fictional altered-content foundations
- Years 2 through 10 recovery and world-order foundations

Run the relevant audits and resolve every accepted handoff.

### Batch C: successor packages

Implement selected successors in regional batches. Each receives:

- opening chain
- domestic conflict chain
- external relationship chain
- late identity chain
- recurring local incident hooks
- route-aware AI
- focus overlay integration
- decision and mission integration
- idea lifecycle
- leader or council memory
- unique assets and localisation direction

Do not use a copied generic country chain with renamed nouns.

### Batch D: full campaign closure

- late-generation politics
- thaw and ultraviolet hazards
- constitutional settlements
- interregional blocs and wars
- Year 10 ambitions
- defeat, annexation, migration, and integration cleanup
- all documentation, event log, catalog, assets, and audit closure

## Choices and AI

Every important option needs:

- visible meaning
- real cost or sacrifice
- beneficiaries and losers
- short-term effect
- delayed risk
- route and character memory
- AI weighting
- invalid-state handling
- multiplayer-safe resolution

Use equipment, manpower, fuel, trains, convoys, shelter, food, medicine, power, legitimacy, cohesion, local support, state control, time, and infrastructure where they fit. Political power alone is not an adequate default cost.

## Text and presentation

Working labels in the source specs are not final localisation.

Write final text during implementation. Keep it concrete, in-world, region-aware, and mechanically honest. Avoid em dashes, semicolons, staccato prose, generic apocalypse wording, staged contrast formulas, and process language.

Do not invent quotes, lyrics, slogans, or cultural references. Route them through the text research workflow when needed.

## Assets

Use dedicated Fallout asset folders and manifests. Historical people, flags, and attested symbols require sourced material. Fictional successors, altered societies, councils, event scenes, and icons may use generated art through the correct asset workflow.

Do not create climate art before the local engine route and texture requirements are proven.

## Validation and completion

After each batch, run the owning audits. Before completion, run:

- scripted-system audit
- focus-tree audit
- decision-mission audit
- country-package audit
- localisation audit
- documentation cleanup
- catalog-exclusion verification
- event completion audit
- manual improvement-loop closure pass

Completion requires real event counts by primary family, all selected successor obligations, AI, cleanup, assets, final text, ten-year play coverage, and meaningful scenario validation. Report every omission, blocker, fallback request, and unresolved accepted plan.

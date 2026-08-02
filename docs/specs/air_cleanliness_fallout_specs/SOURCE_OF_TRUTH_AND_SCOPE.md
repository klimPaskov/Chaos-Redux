
# Air Cleanliness and Fallout Living World Planning Pass

## Status

This package is a consolidated source-spec suite for the Air Cleanliness and Fallout design. It includes normalized copies of the accepted baseline specs and matrices, the corrected repository implementation architecture, and a new living-world expansion for event depth, social life, regional variation, campaign pacing, and visible climate presentation.

The accepted core architecture remains in force. The normalized baseline files preserve the state winter system, blackout transition, deterministic world rewrite, successor matrix, focus overlay matrix, survival mechanics, manual scenario sequence, and dedicated Fallout ownership rules. The living-world files make those systems inhabited and reactive across a ten-year post-collapse campaign.

## Canonical folders

Accepted source specifications belong under:

`docs/specs/air_cleanliness_fallout_specs/`

Implementation plans and subagent handoffs belong under:

`docs/plans/air_cleanliness_fallout_plans/`

Earlier event-numbered Fallout filenames are legacy planning filenames. They do not assign Fallout to an ordinary event number. New Fallout work must use the system-level canonical folders and must not use a zombie namespace, zombie event id, or zombie asset path.

## Independent Fallout ownership

Fallout owns:

- `events/fallout_world_end_events.txt`
- `add_namespace = chaosx.fallout`
- Fallout-specific scripted effects, scripted triggers, constants, on-actions, scripted GUI, scripted localisation, interface definitions, assets, audio, documentation, and event memory
- every transition, orientation, survival, society, regional, diplomatic, war, recovery, and late-game Fallout event

The generic manual-scenario framework may dispatch a Fallout-owned bootstrap callback. That callback starts the manual strike transaction and is not the Fallout consequence itself. The generic framework does not own the Fallout chain.

Air Contamination may request Fallout through the shared request helper. It does not define Fallout events.

No Fallout event, image, icon, sound, music file, sprite, quote slot, or GUI element may reuse zombie-owned content. Fallout is not a normal super-event.

Fallout itself is a consequence transition, not an ordinary Event Log row or evolution. It replaces the retired Final Silence row in the world-end selector registry, where its title and details describe the consequence without registering a normal event. Its stable settings-ledger value is owned by `fallout_consequence_id` in `common/script_constants/fallout_consolidated_constants.txt`. The manual trigger is a Fallout-owned sandbox launch surface at the allocated next-live id. It remains absent from ordinary Event Log, evolution, ordinary Event Details, and ordinary super-event registries. The exact native thermonuclear sweep and seven-day handoff are activation gates, not reasons to register a normal event. Post-consequence survivor chains are ordinary Fallout-owned events and may have their own histories.

## Manual scenario numbering

The manual Fallout trigger reserves the next free live scenario id after the writable repository is scanned. The plan does not assume any fixed number. Existing scenarios keep their ids. The reservation is Fallout-owned and may appear only in the manual sandbox scenario list. It never authorizes insertion into ordinary Event Log, ordinary Event Details, evolution, or ordinary super-event registries. The engine-native sweep and seven-day handoff remain activation gates.

## What this pass adds

This pass adds:

- a complete event ecology and pacing model
- a large catalogue target with global, regional, archetype, country-memory, character, diplomatic, war, mutant-fiction, recovery, and generational event layers
- concrete event chains with real effects and follow-up state
- a 99-candidate successor event overlay matrix
- a normal-map climate presentation requirement in addition to the winter mapmode
- biome-specific visible cold states
- climate recovery, thaw, ultraviolet, and second-generation event arcs
- anti-spam rules so a large event library creates variety instead of constant popups
- implementation, asset, and audit prompts
- a manual improvement-loop pass
- a precise continuation prompt

## Text boundary

All event names and chain names in this package are working labels for planning. They are not final localisation. Implementation must write final player-facing text from the direction, actor, facts, choices, and tone recorded here.

No source-dependent quote, lyric, slogan, or cultural line is final until researched and documented through the appropriate text research workflow.

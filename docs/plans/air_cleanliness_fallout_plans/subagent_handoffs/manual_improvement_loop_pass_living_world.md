# Manual Improvement-Loop Pass: Fallout Living World

## Pass status

The custom improvement-loop subagent could not be spawned in this environment. This is a manual application of the same planning standard.

The pass reviewed the accepted Air Cleanliness and Fallout design, the expanded successor and focus matrices, the corrected implementation architecture, the dedicated Fallout ownership rules, and the new living-world files in this package.

## Feature promise

The Fallout scenario promises a transformed world that remains playable for another decade.

That promise requires:

- a world that keeps changing after the rewrite
- countries with memories and institutions
- recurring people
- regional material differences
- hard survival choices
- diplomacy and new international orders
- wars with causes and settlements
- climate that is visible and persistent
- recovery that creates new conflicts
- enough content that successive campaigns diverge

## Main shallow-system finding

The accepted architecture already described:

- state winter phases
- population and building damage
- a winter mapmode
- blackout
- state grading
- wasteland
- successor governments
- focus overlays
- survival resources
- manual scenario
- long-term recovery

The event layer did not match that scale. It contained useful categories and a few broad chain expectations, but lacked enough concrete event families, recurring actors, regional chains, bilateral memory, war causes, social life, and late-game incidents to make the transformed world feel inhabited.

A large mechanical rewrite without this event layer would become a map and modifier system with occasional briefings.

## Secondary shallow-system finding

The winter mapmode made the climate readable when selected, but the normal map did not have a firm requirement to look colder during ordinary play.

A player could therefore suffer severe winter mechanics while looking at a visually ordinary world.

## Accepted expansions

This pass accepts and records:

- a release floor of 660 manually reviewed Fallout event blocks
- an optional expansion ceiling of 910 blocks after the floor passes review
- 90 to 180 meaningful visible events per human campaign over ten years
- a dedicated Fallout scheduler with family fatigue, active arc caps, bilateral reservations, and memory
- 58 global survival and society anchors
- 108 regional anchors across nine broad regional pools
- 120 government-archetype anchors across twelve archetypes
- four linked arc obligations for every one of 99 candidate successors
- 30 recurring character-role blueprints
- 57 diplomacy, trade, war, and settlement anchors
- 36 cause-memory anchors
- 31 fictional altered-content anchors
- 49 recovery and late-world-order anchors
- nine normal-map climate visual classes across phases 0 through 6
- visible cold in normal map presentation
- phase-aware thaw, flood, ultraviolet, and recovery presentation
- asset, implementation, writing, and completion-audit handoffs

## Why the event target is large

The target is justified by the number of orthogonal contexts:

- timeline phase
- region
- biome
- government
- country memory
- cause memory
- active survival crisis
- winter phase
- neighboring countries
- character arc
- diplomacy
- war
- generation
- recovery state

The library is not meant to appear in one campaign. Context selection and cooldown rules make a fraction of it visible.

## Anti-bloat findings

Several possible expansions were rejected or bounded.

### Universal unique event art

Rejected. The event library needs a deep image family, but not one image for every event. Tightly related routine events can share a family image when the physical subject and region match.

### One country tag for every candidate at once

Rejected. The 99-country matrix remains a candidate pool. Spawn selection depends on the rewrite, geography, tag ledger, and campaign state.

### One full independent event engine per successor

Rejected. Successors use shared scheduler and helper infrastructure with unique event conflicts, memory, options, effects, and callbacks.

### Universal snow

Rejected. Cold presentation varies by climate class. Tropical, arid, maritime, and seasonal regions require different visual evidence.

### Constant popups

Rejected. The large library is controlled by per-campaign budgets, cooldowns, family fatigue, active arc caps, and hidden AI resolution.

### Custom GUI for every subsystem

Rejected. Normal events, decisions, mapmode tooltips, and existing country surfaces remain the default. Custom GUI is reserved for blackout and mechanics that cannot be read cleanly elsewhere.

### Final localisation inside planning files

Rejected. Working labels provide structure. Implementation writes final text after mechanics, actors, and research are stable.

### Scientific treatment of fantasy mutants

Rejected. Fictional altered countries remain explicit high-chaos or scripted fiction.

### Recovery as a return to the pre-collapse world

Rejected. Recovery creates new institutions, trade systems, generational politics, wars, and environmental hazards.

## Quality risks that remain

### Mechanical template risk

The four successor arc obligations could still become copied chains if implementation changes only names and resource nouns.

Mitigation:

- manual country-package review
- country-memory effects
- region and government interaction
- distinct founder conflict
- different external behavior
- country-specific late ambition
- completion audit sampling

### Event count risk

A large count can encourage shallow blocks.

Mitigation:

- release floor by family
- manual review
- multi-event chain standard
- real effect requirement
- AI and cleanup requirement
- no raw count completion claim

### Presentation risk

Normal-map climate support may be limited by engine surfaces.

Mitigation:

- local proof gate
- multiple coordinated visual channels
- no quiet mapmode-only substitution
- explicit blocker report if a channel cannot be supported

### Regional stereotype risk

A large regional matrix can reduce countries to simple climate or cultural cues.

Mitigation:

- local institutional research
- several political positions inside each region
- competence and ordinary life
- sourced history
- country memory overriding generic region when appropriate

### Multiplayer and performance risk

State updates, event selection, and bilateral reservations can become expensive.

Mitigation:

- extend the existing Air state scan
- host-authoritative scheduler
- bounded candidate pools
- dirty updates
- active arc caps
- hidden AI batching
- performance checks after every implementation batch

## Accepted stopping point for planning

The system now has enough event architecture to begin implementation. Another broad planning pass before a pilot implementation would create plan stacking.

The next useful design review should occur after Batch A implements:

- scheduler
- orientation
- twenty global anchors
- regional pilots
- one archetype
- four successors
- five character arcs
- first contact through peace pilots
- winter normal-map proof

At that point, a new improvement-loop pass can judge actual pacing, text repetition, helper overreach, regional distinction, and choice quality.

## Work that remains implementation-owned

The following are not missing planning sections:

- final event suffixes
- final manual scenario id
- exact state ids
- exact tags
- final country selections
- final event titles and prose
- final costs and tuning
- final asset filenames after registration
- verified map and weather texture surfaces
- verified province-wide thermonuclear syntax
- final AI weights
- parser and live-game validation

These require the writable repository and local game references.

## Recommendation

Promote this living-world package into the canonical source-spec area. Do not create another broad Fallout design addendum until the pilot batch has been implemented and audited.

The implementation goal remains open. The design pass is ready for local proof and staged implementation, but no gameplay completion claim is justified.

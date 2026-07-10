# Achievement Implementation Prompt for Event 19 Infantry Spawn

## Task

Implement the complete Event 19 achievement set from `matrices/019_achievement_matrix.md`. Treat every title in the matrix as a working label. Write final player-facing titles and descriptions during implementation.

Read:

- `AGENTS.md`
- `chaos-redux-events`
- `chaos-redux-event-assets`
- the Event 19 specification
- the final event, decision, lot, claimant, derivative, scenario, and combat-tracking implementation
- existing Chaos Redux achievement registration, localisation, GFX, and tracking patterns

## Achievement set

Implement all final approved IDs based on these working IDs:

- `019_infantry_spawn_every_rifle_accounted_for`
- `019_infantry_spawn_one_battalion_wonder`
- `019_infantry_spawn_the_army_has_voted`
- `019_infantry_spawn_order_from_noise`
- `019_infantry_spawn_combined_arms_accident`
- `019_infantry_spawn_no_room_on_the_train`
- `019_infantry_spawn_borrowed_future`
- `019_infantry_spawn_three_false_apocalypses`
- `019_infantry_spawn_barracks_of_babel`
- `019_infantry_spawn_quiet_demobilisation`
- `019_infantry_spawn_every_barracks_a_front`

Preserve stable final IDs once registered.

## Tracking requirements

### Generated formation identity

Achievements involving a random division must track the original Event 19 generation and lot. Manual template construction or unrelated divisions cannot satisfy them.

Track:

- generation
- lot
- original composition signature or verified required family flags
- whether the division was materially expanded or replaced
- battle participation and survival

Do not create expensive per-division permanent tracking when a safe lot or unit-leader flag pattern can provide the same proof.

### Significant combat

Define a meaningful battle standard. It should require a real enemy force and material combat result. A token skirmish, empty enemy, or one-hour combat cannot unlock the challenge.

Centralize the threshold and document it.

### High-control completion

Achievements about integration and demobilization must verify:

- generation size threshold
- final Muster Control band
- final Army Congestion band
- no unresolved debt or lots when required
- no claimant or derivative revolt when required
- no exploit path through instant disband or forced cleanup

### Claimant takeover

Track whether a claimant actually became national leader or controlling regime through Event 19. Later survival or war success must happen after takeover.

### Technology-locked formation

Verify that the formation used its event-created advanced equipment before the country unlocked the core technology. Do not unlock from a formation cloned after technology acquisition.

### Derivative isolation

The three-derivative challenge must identify zombie, ghost, and golem Event 19 derivative origin flags. Parent Zombie, Death, or golem actors cannot substitute.

### Triggerable scenario

Store scenario type and intensity in a durable history record. Clear temporary launch bypass flags after setup. The achievement reads the history record and starting-country continuity.

## Disqualifiers

Implement the disqualifiers listed in the matrix, including:

- manual template substitution where prohibited
- forced or debug completion
- tag switching where prohibited
- changing scenario intensity after launch
- using a parent-event actor instead of a derivative
- cloning technology-locked equipment through an exploit

Disqualifiers must be visible in achievement UI where project style allows, but should not appear in ordinary event or decision text.

## AI and player scope

These are player achievements. AI can create the relevant world state but cannot unlock them for itself.

## Assets

Coordinate with the Event 19 asset package.

Every achievement needs:

- one completed 64 by 64 icon
- one grey variant
- one not-eligible variant using the project overlay
- filenames exactly matching the final registered achievement ID
- GFX registration
- manifest coverage

Do not reuse one icon for several achievements without a strong visual reason.

## Documentation

Update:

- the root Chaos Redux achievement registry
- achievement localisation
- achievement GFX
- Event 19 documentation
- asset manifest
- any project achievement list or catalog

## Validation

Run task-specific checks for:

- each achievement’s positive path
- each disqualifier
- generated-identity preservation
- parent versus derivative distinction
- scenario type and intensity history
- battle significance
- icon triplet and filename alignment

Report any simplification, missing icon, unverified tracking path, or false-positive risk. Do not mark the achievement set complete if any listed achievement is omitted or converted into a trivial unlock.

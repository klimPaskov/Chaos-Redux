# Achievement implementation prompt: Event 011 Secret Alliance

Status: fulfilled historical implementation prompt. All six achievements and icon triplets are implemented. Do not rerun this prompt as open work; use the holistic completion audit and `docs/achievements/011_secret_alliance_achievements.md` for current status.

Implement the complete achievement set from `matrices/011_secret_alliance_achievement_matrix.md`. Read the event specs, the asset register, the project event skill, and the event-asset skill before work.

## Required achievements

Implement these working IDs unless an existing registry conflict requires a documented stable rename:

1. `011_secret_alliance_the_empty_chair`
2. `011_secret_alliance_every_thread`
3. `011_secret_alliance_their_man_in_the_room`
4. `011_secret_alliance_divide_the_table`
5. `011_secret_alliance_surrounded_not_buried`
6. `011_secret_alliance_two_giants_one_grave`

Use the matrix as the exact source for eligibility, unlock conditions, disqualifiers, difficulty, visibility, and tracking meaning.

## Tracking requirements

- Distinguish normal automatic event origin from manual scenario origin.
- Snapshot active membership before reveal when an achievement compares confirmed and actual members.
- Snapshot major status at reveal for the two-major achievement.
- Record whether an accused country was innocent at the moment of public accusation.
- Record whether a turned channel survived and produced a concrete reveal or war effect.
- Count coalition exits only when produced by the event's fracture, defection, refusal, or separate-terms systems. Capitulation does not count.
- Record the selected scenario intensity at launch and do not let later variable changes alter eligibility.
- Clean tracking when the event terminates, the target ceases to exist, or the run becomes disqualified.

Do not create achievements that unlock from the event firing, from clicking one decision, or from ordinary conquest without using the event mechanics.

## Registry and assets

Use the shared Chaos Redux achievement registry. Keep one shared `unique_id` structure and group Event 011 achievements in an Event 011 section.

Wire:

- registry entries
- English localisation
- completed, grey, and not-eligible icons
- GFX definitions
- tracking flags or variables
- event and scenario hooks
- docs

Achievement icon filenames must exactly match the final achievement IDs and live directly under `gfx/achievements/`. Use the asset package output and the required overlay workflow for not-eligible variants.

## Localisation direction

Write final player-facing text during implementation. Use the working labels only as direction. Text should clearly state visible requirements and avoid implementation flags, event IDs, and hidden formulas. Hidden achievements may conceal one requirement, but the broad challenge should remain inferable from the icon and description.

## Validation

For each achievement, document one positive path and at least one disqualifying path. Verify:

- no automatic unlock at event fire
- normal and scenario origin rules
- active member snapshots
- innocent accusation disqualifier
- turned-channel consequence
- coalition exit counting
- two-major snapshot
- exact icon triplets
- no duplicate achievement ID

Report any renamed, merged, simplified, or omitted achievement. Do not use placeholders.

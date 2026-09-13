# Achievement implementation handoff for Event 045

Implement the complete Event 045 achievement set from `specs/045_third_balkan_war_spec_part_6_ai_achievements_assets.md`.

## Required achievements

1. `chaosx_achievement_045_keep_it_regional`
2. `chaosx_achievement_045_the_conference_holds`
3. `chaosx_achievement_045_every_map_is_temporary`
4. `chaosx_achievement_045_no_friends_left`
5. `chaosx_achievement_045_a_very_small_incident`
6. `chaosx_achievement_045_the_entente_reversed`

## Implementation contract

For every achievement, implement the complete runtime surface:

- a stable achievement definition in the single Chaos Redux achievement registry
- event-owned tracking flags or variables
- precise unlock triggers
- explicit disqualifiers
- save and reload persistence
- cleanup after an invalid event generation
- player-country continuity rules
- final localisation written from the working direction in the spec
- three independent achievement-state assets when required by the current consumer
- documentation and catalog-facing alignment where achievement summaries are shown

Do not convert the working labels into final text without a localisation pass. Do not weaken a difficult achievement into an automatic unlock. Do not count Force Trigger Mode, invalid opening generations, or unrelated pre-existing world wars unless the achievement contract explicitly allows them.

## Shared proof rules

Use the same Event 045 ledgers that control gameplay. Do not maintain a second contradictory achievement-only claim registry, participant list, stage proof, or settlement record.

The following facts must be available to achievement triggers:

- original participant status
- opening participant count
- opening cause family
- maximum escalation reached
- direct outside-major entry
- conference leadership and cooperating powers
- successful armistice-line mission
- active registered claims settled by the player
- Evolution I and Evolution III activation
- former-ally war participation
- verified Third Balkan War origin of Another World War
- settlement signatories and their opening camps
- final independence, subject status, annexation, capital survival, and player-country continuity

When the event hands off to a wider war, preserve only the achievement facts needed for post-handoff checks and clear them after success, permanent failure, or campaign invalidation.

## Asset handoff

Route six complete achievement triplets to `chaosx_icon_artist` through the event asset workflow. Each completed icon must be independently composed for the achievement surface. Grey and not-eligible variants must follow the exact current achievement precedent. Do not resize decision art, reuse another achievement, or make local primitive substitutes.

## Validation

Test every unlock and every main disqualifier in separate scenarios. Include a negative test where the numerical escalation threshold is reached without the required world-state proof. Include a negative test where a pre-existing world war prevents Event 045 origin credit. Include a save and reload checkpoint before each delayed or post-handoff unlock.

The completion handoff must list definitions, tracking identifiers, localisation keys, asset paths, scenario evidence, and any unresolved blocker. No simplification or fallback is authorized.

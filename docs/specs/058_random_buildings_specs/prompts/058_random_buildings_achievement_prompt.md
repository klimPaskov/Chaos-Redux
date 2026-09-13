# Achievement implementation prompt for Event 58 Random Buildings

Implement the Event 58 achievements from `docs/specs/058_random_buildings_specs/specs/058_random_buildings_spec_part_5_achievements.md`.

Read `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, the Event 58 core and integration specs, and the current Chaos Redux achievement registry, localisation, tracking, and asset precedents.

## Required achievements

### `058_random_buildings_every_plot_accounted_for`

During one natural or cluster-driven firing, the player country must own and control at least ten land states at transaction start and receive a successful baseline result in every one. All player states count in the denominator, including saturated states. No force, debug, hidden-resolver, observer, or tag-switch credit.

### `058_random_buildings_mixed_use_empire`

The same player country must accumulate and still possess surviving Event 58 results from at least eight stable display families. Mandatory roles are industry, infrastructure or transport, air or detection or state defense, fuel or energy or synthetic industry, one province-package family, and one advanced, rare, restricted, or exceptional family. Validate live surviving structures. Stale markers do not qualify.

### `058_random_buildings_the_exceptional_case`

At `600+` Chaos, a natural or cluster-driven Evolution III result must place a persistent exceptional structure in a player-owned and controlled core state. The player must retain the state and valid structure continuously for 365 days. Loss of ownership, control, structure validity, or player-country identity resets progress.

## Implementation contract

- Inspect the single root Chaos Redux achievement registry and follow its exact ID, unique ID, localisation, tracking, and DLC rules.
- Keep working labels out of final localisation. Write final player-facing titles and descriptions from the design direction.
- Use Event 58 transaction proofs and provider callbacks. Do not infer credit from total building levels.
- Bind player identity at transaction start and follow the project multiplayer standard.
- Prevent direct hidden resolver, force-trigger, debug, observer, and unsupported tag-switch credit.
- Preserve save and reload progress.
- Use bounded country or state checks. Do not add a whole-world daily scan for retention.
- Keep temporary transaction variables temporary and clear them after evaluation.
- Document every persistent achievement flag, variable, event target, display-family marker, and structure-exists proof.
- Register all three achievements in the current root registry.
- Add title, description, requirement, and debug localisation.
- Wire the completed, grey, and not-eligible icon triplets produced through the Event 58 asset prompt.
- Audit IDs, keys, paths, and icon collisions.
- Add task-specific acceptance cases and report any weaker substitute as a blocker.

Use `chaosx_icon_artist` for final icon production, `chaosx_localisation_auditor` for final wording and key coverage, and `chaosx_event_completion_auditor` for the final achievement surface. Every subagent is spawned with `fork_context=false` and receives the exact Event 58 paths and IDs.

Do not weaken the conditions to make random testing easier. Do not grant achievements merely for seeing the event.

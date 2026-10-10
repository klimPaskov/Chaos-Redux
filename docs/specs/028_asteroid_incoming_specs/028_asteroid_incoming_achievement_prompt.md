# Achievement audit prompt for Event 028: Asteroid Incoming

The five achievements are implemented with final localisation and complete icon triplets.
Their conditions and tracking rules are owned by [Part 10](028_asteroid_incoming_spec_part_10_achievements_and_acceptance.md); the artwork record is `docs/events/028_asteroid_incoming/assets/achievements.md`.

## When to run

Run only when an achievement condition, a tracked flag, a hold constant, or a system it reads (missions, crater control, dust protection) changes.
For example, accepting README Open question 2 or the fragment-marker cleanup in Part 5 requires rechecking Government Beyond the Crater and Collector of Fallen Stars.

## Checks

- Each condition in Part 10 matches the `possible` and `happened` blocks and the tracking effects.
- `_NAME`, `_DESC` and `_tooltip` text matches the conditions and reads the same constants.
- Holds reset on lost control and annexation; an annexer never inherits original-target identity.
- Tracking still runs with the Chaos Meter disabled and only after a recorded strike.
- Disqualifiers for manual opening and disabled evolutions still apply.

Native confirmation of reload persistence and hold resets belongs to the user (Part 10 scenario 14).

# Zombie Prevention and Disease Containment Integration

## Overview

The zombie outbreak prevention category is now tied into the broader biowarfare disease containment system.

This means the zombie-focused country measures do not only reduce the chance of a new zombie outbreak. They also strengthen the same contamination-defense layer already used by:

- field hospitals
- state quarantine measures
- anthrax antibiotics
- plague antibiotics
- tularemia antibiotics
- smallpox vaccination

The integration is dynamic. If a country takes or revokes one of the zombie prevention measures, all currently contaminated controlled states are rebuilt from their base disease values and then reduced again using the new full protection stack.

## Integrated measures

The following zombie prevention measures now contribute country-level disease protection:

- `Strict Hygiene Protocols`
- `Migration Restrictions`
- `Quarantine Protocols`
- `Completely Closed Borders`
- `Extreme Martial Law`

These are additive with the state-level disease containment decisions and antibiotic or vaccination protections, but the zombie-prevention contribution itself is capped so it does not dominate the whole contamination system by itself.

## How it works

### Shared contamination reduction

The main disease-reduction effect in:

- `common/scripted_effects/biowarfare_effects.txt`

now calls a shared state-scope helper:

- `calculate_zombie_prevention_contamination_reduction`

That helper reads the controller country's zombie-prevention flags and converts them into a country-level contamination reduction value using:

- `common/script_constants/biowarfare_constants.txt`

### State refresh after decision changes

Because contaminated-state disease modifiers are stored as variables, simply adding a new prevention decision is not enough. Existing contaminated states must be rebuilt from their base disease values first, then the current active protections must be reapplied.

This is handled by:

- `refresh_contaminated_state_effects_from_active_measures`
- `refresh_country_contamination_effects_from_active_measures`

The prevention decisions in:

- `common/decisions/chaosx_zzz_cure_decisions.txt`

now call the country refresh effect when they are enacted or revoked.

The Anti-Zombie League member-preparation effect in:

- `common/scripted_effects/002_zombie_outbreak_effects.txt`

also calls the same refresh effect after seeding hygiene and quarantine, so a country that joins the league immediately benefits in already contaminated states as well.

## Tuning

The new shared values are stored in:

- `common/script_constants/biowarfare_constants.txt`

Category:

- `bio_zombie_prevention_containment`

Current values:

- `hygiene = 0.04`
- `migration = 0.02`
- `quarantine_protocols = 0.08`
- `borders_closed = 0.12`
- `extreme_martial_law = 0.16`
- `country_measure_cap = 0.25`

## UI and localisation

The player-facing text for the zombie prevention decisions and the related ideas was updated to explain that these measures now also improve broader disease containment, not only zombie-outbreak prevention.

Files:

- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/chaosx_ideas_l_english.yml`

## Icons

No new icons or sprites are required for this integration.

## Future Work

- Different disease families could react differently to each zombie-prevention measure instead of all reading the same country-level reduction bucket.
- Border closure could later reduce contamination spread chance between neighboring states directly, not only reduce active contamination severity.
- The disease-containment side could later surface the shared country-level bonus as read-only information without duplicating the zombie-law decisions themselves.

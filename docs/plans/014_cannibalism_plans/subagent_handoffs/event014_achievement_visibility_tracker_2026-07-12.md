# Event 014 Staged Achievement Visibility Tracker

## Outcome

Event 014 keeps all eighteen real achievements in the root Chaos Redux achievement registry. The five baseline achievements remain visible in the ordinary Career Profile. Achievements 06 through 18 remain statically hidden there because the HOI4 achievement schema only provides a static `hidden = yes` field.

A dedicated read-only decision category mirrors all eighteen entries at the public stage specified in Part 11. This gives the campaign a stage-aware achievement surface without placing achievement routes inside Event Details and without exposing Hannibal Lecter or the Wendigo route early.

## Files

- `common/achievements/chaos_redux_achievements.txt`
- `common/decisions/categories/014_cannibalism_achievement_tracker_categories.txt`
- `common/decisions/014_cannibalism_achievement_tracker_decisions.txt`
- `common/scripted_localisation/014_cannibalism_achievement_tracker_scripted_localisation.txt`
- `interface/014_cannibalism_achievement_tracker.gfx`
- `interface/014_cannibalism_achievements.gfx`
- `localisation/english/014_cannibalism_l_english.yml`

## Visibility contract

| Achievements | Tracker visibility |
|---|---|
| 01 through 05 | Event 014 system start |
| 06 | First terror exploitation selection |
| 07 | First successful Island Host formation |
| 18 | Evolution II becomes public |
| 12 | First convergence window |
| 08 through 11, 13, 15 | Public reveal complete |
| 14 and 16 | Wendigo merge occurs |
| 17 | Global defeat aftermath becomes eligible |

The four stage flags used before the established reveal, merge, and aftermath flags are:

- `achievement_cannibalism_exploitation_visibility_open`
- `achievement_cannibalism_island_host_visibility_open`
- `achievement_cannibalism_evolution_ii_visibility_open`
- `achievement_cannibalism_convergence_visibility_open`

They are persistent campaign discovery flags. Ordinary phase transitions do not clear them.

## Read-only behavior

Each tracker entry uses the corresponding completed achievement icon and the same name and requirement localisation as the real achievement. Its completion status calls the real achievement trigger through a dedicated scripted-localisation selector. The decision itself is permanently unavailable and has no cost, effect, AI action, or completion hook. It cannot grant or disqualify an achievement.

## Asset contract

The eighteen entry icons intentionally use the matching real achievement icons because they represent the same objective. The category requires its own generated assets:

- `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_achievement_tracker.dds`
- `gfx/interface/decisions/014_cannibalism/cannibalism_achievement_tracker_category_panel.dds`

Neither category texture may reuse an existing Event 014 icon or panel.

## Validation evidence

- 18 tracker decision entries exist.
- 18 completion-status selectors resolve to 18 existing achievement completion triggers.
- Exactly 13 late Career Profile achievements use static hiding.
- Early tracker files contain no Hannibal Lecter or Wendigo identity token.
- The English localisation file retains its UTF-8 BOM.

## Engine boundary

The dedicated tracker is the verified stage-aware presentation surface. It does not change the engine achievement schema and does not claim that static Career Profile entries can become dynamically visible.

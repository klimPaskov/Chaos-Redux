# Soviet Collapse Local Leagues

## Overview

Event 005 uses local leagues as the regional layer between isolated breakaway republics and the larger Free Republics' League. The Baltic League, Caucasus League, and Central Asian League are founded through the `soviet_collapse_regional_faction_category` decision category once a valid ordinary breakaway exists and the crisis has enough pressure to justify regional coordination.

## Flow

1. A breakaway republic or eligible local successor becomes a regional faction candidate.
2. The relevant founding decision creates the faction, marks the founder and members, recruits aligned partners, strengthens each member's staged League coordination, and raises Soviet-facing League pressure.
3. Faction leaders can invite partners, coordinate goals, adopt defense, recognition, or logistics priorities, and settle internal tension.
4. Active goals can resolve as successes or failures. Defense succeeds through an active anti-Soviet defensive war, recognition succeeds through sufficient recognition progress, and logistics succeeds through depot control. High tension, collapsed cohesion, invalid calm defense policy, patron-dominated recognition failure, or failed depot logistics can break the current program.
5. Under high threat or direct war pressure, regional members can call a defensive war against Moscow. The call arms members, brings faction partners into the war, clears the progressive-release cooldown, and immediately checks the MTTH release scheduler.
6. Kazakhstan is restricted from Central Asian League membership and release pressure until at least three smaller Central Asian republics are already free.

## Interactions

Local leagues protect republics from foreign client-state pressure by giving them faction membership and regional-faction flags. They also feed the wider `soviet_collapse_league_cohesion` variable, which increases release pressure and blocks calm reintegration routes when the bloc is strong.

Foundation is gated by pressure through `is_soviet_collapse_regional_league_foundation_pressure_ready`. That trigger accepts an existing war with Moscow, credible recognition progress, high Union Crisis Threat or republican confidence, multiple breakaways, high foreign appetite, or a fresh failed Soviet objective. A single calm breakaway no longer opens a league on its own.

The Baltic League, Caucasus League, and Central Asian League keep their existing scripted keys and wired sprites for asset compatibility, but player-facing text uses league names throughout.

League formation is reported through normal news events, not super-events. The Baltic, Caucasus, and Central Asian founding helpers fire `chaosx.nr5.30`, `chaosx.nr5.31`, and `chaosx.nr5.32`; the Steppe Federation endgame report uses `chaosx.nr5.36`. The retired league super-event helpers and sprite/localisation mappings are not active.

Goal resolution is reported through normal report events. Successful common programs fire `chaosx.nr5.41`; failed or patron-disputed programs fire `chaosx.nr5.42`. The supporting source audit is `docs/events/005_soviet_collapse_faction_goal_audit.md`.

## Icons

No new art is required for this pass.

- `soviet_collapse_regional_faction_category` uses `GFX_decision_category_soviet_collapse_regional_faction` in `interface/005_soviet_collapse_icons.gfx`.
- `soviet_collapse_found_baltic_restoration_pact` uses `GFX_decision_soviet_collapse_baltic_restoration_pact`.
- `soviet_collapse_found_caucasus_defense_compact` uses `GFX_decision_soviet_collapse_caucasus_defense_compact`.
- `soviet_collapse_found_steppe_federation` uses `GFX_decision_soviet_collapse_steppe_federation`; the icon now represents the Central Asian League.
- Shared coordination, goal, tension, war, and withdrawal decisions reuse the existing regional faction decision sprites.

## Future Plans

The next expansion can add region-specific event option effects for Baltic legal restoration, Caucasus border mediation, and Central Asian oasis-steppe bargaining. A later asset pass can replace the legacy Steppe Federation emblem with a dedicated Central Asian League emblem while keeping the scripted name stable.

# Event 010 Death - Achievement Prompt

## Achievement Goals

Achievements should reward hard play and clear alternate outcomes. Do not grant achievements for merely seeing Event 010 fire.

Each achievement needs:

- trigger flags
- prevention/disqualifier flags
- localisation
- icon assets in all required sizes
- `.gfx` sprite aliases
- docs entry in the custom achievements system

## Proposed Achievements

| Achievement | Player role | Conditions |
| --- | --- | --- |
| `death_lighthouse_was_enough` | ordinary country | Discover Death before public reveal and prevent mainland reveal for a configured duration. |
| `death_not_one_step_into_the_sea` | ordinary country or compact leader | Defeat Death before it consumes any mainland state and without forbidden decisions. |
| `death_conference_of_the_living` | compact leader | Form the Living Compact with members from at least three continents and keep cohesion above threshold until Death is defeated. |
| `death_map_with_islands_still_on_it` | small island country | Survive the island phase, avoid consumption, and contribute to Death's defeat. |
| `death_black_candle_victory` | ordinary country | Use forbidden study/containment and still defeat Death. Disqualifies clean achievements. |
| `death_no_names_for_the_dead` | Death player | Consume a configured population threshold before public reveal. |
| `death_every_shore_a_door` | Death player | Establish footholds on every continent without triggering world-end yet. |
| `death_zols_hand` | marked client | Petition Zol, survive as a marked client until world-end, and avoid being consumed before a configured deadline. |
| `death_world_under_zol` | Death player | Consume every valid state. |
| `death_every_shore_guarded` | compact or ordinary country | Clear all world-end footholds and defeat Death after world-end fires. |

## Trigger And Flag Notes

Suggested flags:

- `achievement_death_discovered_before_reveal`
- `achievement_death_no_mainland_reveal_until_date`
- `achievement_death_clean_containment`
- `achievement_death_forbidden_used`
- `achievement_death_compact_three_continents`
- `achievement_death_small_island_survivor`
- `achievement_death_world_end_footholds_cleared`
- `achievement_death_player_consumed_world`

Disqualifiers:

- using forbidden/necromancy decisions
- joining Death as a marked client
- letting Death consume a mainland state for early-containment achievements
- compact leadership collapse for compact achievements
- switching tags in a way that invalidates actor ownership

## Icon Brief

| Achievement | Icon concept |
| --- | --- |
| `death_lighthouse_was_enough` | lit lighthouse over black sea |
| `death_not_one_step_into_the_sea` | boot at shore stopping black waterline |
| `death_conference_of_the_living` | compact seal over coastline map |
| `death_map_with_islands_still_on_it` | small island map still marked in white |
| `death_black_candle_victory` | black candle with pale victory mark |
| `death_no_names_for_the_dead` | ledger page with names erased |
| `death_every_shore_a_door` | multiple coastlines opening into black |
| `death_zols_hand` | gloved hand over black register |
| `death_world_under_zol` | globe reduced to black ledger mark |
| `death_every_shore_guarded` | ring of lights around a dark coast |

## Implementation Prompt

Implement Event 010 Death achievements after core mechanics are wired. Add precise flags to reveal, containment, compact, forbidden, world-end, defeat, and world-consumed effects. Achievements must not rely on vague state at check time if a durable flag should be set earlier. Register icon sprites, localisation, and docs. Run a custom achievement audit to ensure no achievement can be awarded by passive event firing, unrelated tag switching, repeated decision clicks, or incomplete Death cleanup.

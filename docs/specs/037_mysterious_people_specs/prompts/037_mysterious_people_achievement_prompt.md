# Prompt: Event 037 achievements

Implement the three achievements defined in [Part 7](../specs/037_mysterious_people_spec_part_7_assets_achievements_and_catalog.md#achievements) after the ledger, pressure, mission, and Famine stage reads are stable.
Part 7 owns the IDs and conditions, and `docs/systems/custom_achievements.md` with the existing entries in `common/achievements/chaos_redux_achievements.txt` owns the shared rules for game mode, country continuation, and persistence.

## Implementation focus

- Room for Everyone uses a continuous `365`-day timer that resets on any failed condition, reads the newcomer count from the latest count, and reads famine stages from the Famine owner.
- A Billion More checks at the end of a firing, using that firing's world and country counts.
- Three Censuses counts mission successes keyed to the manifestation that started each mission, so reports, reloads, and multiplayer cannot add a count, and it clears when the country reaches Emergency between the first counted manifestation and the third success.
- Titles and descriptions state the real conditions in player language.
- Each achievement uses its own triplet from the asset package.

## Checks

Success, timer reset, reload during a timer, a second success for the same manifestation, the Emergency reset for Three Censuses, and the world threshold at a firing.

# Achievement prompt for Event 17: Random faction

Implement the achievement set only after the event mechanics, decisions, evolutions, and assets are wired. Titles below are working labels, not final localisation.

| Working key | Working label | Visibility | Eligible play | Unlock conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `017_random_faction_four_doors` | Four Doors, One Cabinet | visible | any eligible minor | be selected by Event 17 while at least four valid factions exist, choose a faction, survive one year without capitulating, and remain in that faction | leaving faction within one year, becoming subject | medium | four faction banners around a small council table |
| `017_random_faction_hold_the_line` | Hold the Neutral Line | visible | neutral minor pressured as neighbor | under Evolution I or higher, complete neutrality council and border post mission, remain outside factions for one year | joining a faction, becoming subject, failing border mission | hard | guarded border post with sealed neutrality emblem |
| `017_random_faction_crowded_border` | Crowded Border | hidden | any country in pressured region | cause or witness a region where at least three different factions have members bordering or neighboring the same small neutral country | target country joins a faction before condition is met | hard | three colored banners pressing toward one border marker |
| `017_random_faction_liaison_web` | The Liaison Web | visible | faction leader | successfully support three different Event 17 pressured or newly aligned minors through staff mission or radio networks without any target capitulating within 180 days | target capitulates, support target becomes direct enemy | hard | radio mast and officer cords linking three flags |
| `017_random_faction_frontier_commitment` | Frontier Commitment | hidden | selected wartime or war-adjacent minor | under Evolution II, join a faction while at war or bordering an enemy faction member, then hold capital and all core border states for 180 days | losing capital, becoming subject | very hard | small shield between two faction fronts |
| `017_random_faction_not_everyone` | Not Everyone Signed | hidden | any country | reach Evolution III and resolve a regional cascade while at least one eligible neutral country in that region remains outside all factions for 180 days | every eligible regional neutral joins factions | very hard | one unmarked flag standing apart from bloc banners |

## Tracking notes

- Use tracking flags that are set by actual Event 17 mechanics, not generic faction joining.
- Do not unlock achievements only because the event fires.
- Track disqualifiers through country flags or variables as needed.
- Icon assets belong to the asset prompt and must be wired before completion.
- Final localisation should be written from achievement direction and should not expose hidden variable names.

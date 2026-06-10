# 007 Fury achievement specification

Fury achievements should reward containment, difficult scenario survival, defeating a grown Fury state, and handling pact or hostile variants. Since the player is excluded from becoming Fury, achievements should not require the player to use the Fury package.

## Achievement list

| Working id | Title | Visibility | Difficulty | Eligible player role |
| --- | --- | --- | --- | --- |
| `achievement_fury_fuse_cut` | Fuse Cut Short | visible | medium | any country near Fury |
| `achievement_fury_no_minor_major` | No Minor Shall Be Major | visible | hard | any country |
| `achievement_fury_firebreak` | The Firebreak Holds | visible | hard | Fury neighbor or regional power |
| `achievement_fury_pact_breaker` | Break the March Pact | visible | hard | any country |
| `achievement_fury_ten_fires` | Ten Fires, No Dawn | hidden | very hard | triggerable scenario challenge |
| `achievement_fury_last_neighbor` | The Last Neighbor Stands | hidden | hard | country bordering Fury |
| `achievement_fury_world_without_fury` | A World Without Fury | hidden | extreme | world-end challenge |
| `achievement_fury_rivals_burn` | Let the Fires Fight | hidden | hard | hostile scenario manipulation |
| `achievement_fury_major_without_faction` | Alone Against the Major | hidden | very hard | independent country |
| `achievement_fury_no_cores` | Paper Borders Hold | visible | medium | any country |

## Detailed achievement designs

### Fuse Cut Short

Description direction: Defeat an active Fury country before it wins its first war.

Unlock conditions:

- a Fury actor exists.
- that Fury actor has no first-conquest flag.
- player or player faction defeats or capitulates the Fury actor.
- Fury has existed for less than a tuned early duration.

Disqualifiers:

- Fury completes first conquest.
- player uses the triggerable Maximum scenario.
- player is the Fury country through console or tag switch.

Icon direction: cut fuse over a small border map.

### No Minor Shall Be Major

Description direction: Prevent any Fury country from becoming a major for a full Fury cycle, then defeat all active Fury actors.

Unlock conditions:

- Fury fires normally or through scenario.
- at least one Fury actor wins a first war.
- no Fury actor reaches major threshold.
- all active Fury actors are defeated or cleaned up.

Disqualifiers:

- any Fury major super-event fires.
- player becomes Fury through nonstandard control.

Icon direction: small flag blocked by a large staff marker.

### The Firebreak Holds

Description direction: As a country bordering Fury, complete border watch and survive the next Fury war without losing your capital.

Unlock conditions:

- player borders Fury.
- player completes Border Watch mission.
- Fury declares on player only through terminal warning route or player is drawn in through an allowed defensive war.
- player holds capital and wins or survives until Fury is defeated.

Disqualifiers:

- capital falls.
- player joins Fury faction.
- player becomes Fury.

Icon direction: line of soldiers along a marked border.

### Break the March Pact

Description direction: Defeat the Fury Pact after at least two Fury countries have joined it.

Unlock conditions:

- Fury Pact type or cooperation branch active.
- at least two Fury countries join same Fury faction.
- player or player faction defeats the faction leader.
- no active Fury faction remains.

Disqualifiers:

- Fury Pact never forms.
- world-end branch defeats itself without player contribution.

Icon direction: broken faction seal with marching arrows split.

### Ten Fires, No Dawn

Description direction: Survive and defeat a Maximum intensity World in Fury scenario.

Unlock conditions:

- player launches `The World in Fury` at Maximum intensity.
- at least ten Fury actors are created, or every safe eligible actor is created if the world has fewer than ten.
- player is never Fury.
- all Fury actors are defeated.
- no Fury actor remains a faction leader.

Disqualifiers:

- scenario is not Maximum intensity.
- player uses pact join exploit.
- player transfers to a Fury tag.

Icon direction: ten small flames crossed by a world map grid.

### The Last Neighbor Stands

Description direction: Border a Fury country that has no other valid neighbors and defeat it before the world-end branch begins.

Unlock conditions:

- player borders a Fury actor.
- Fury has no other valid AI land neighbor.
- world-end branch has not begun.
- player defeats or helps defeat that Fury actor.
- player capital remains held.

Disqualifiers:

- world-end super-event fires.
- player joins Fury faction.

Icon direction: last border marker standing in front of a map table.

### A World Without Fury

Description direction: End the Fury world-end branch by defeating every Fury country.

Unlock conditions:

- Fury world-end branch begins.
- world-end super-event fires.
- at least three continents receive Fury actors.
- all Fury actors are defeated.
- world threat source from Fury is cleared.

Disqualifiers:

- player becomes Fury.
- another terminal branch ends the campaign first if the achievement system cannot track Fury defeat cleanly.

Icon direction: burned maps being archived under a sealed stamp.

### Let the Fires Fight

Description direction: In Hostile Fury type, cause two Fury countries to fight and make sure both are defeated.

Unlock conditions:

- Hostile Fury type active.
- at least two Fury actors exist.
- one Fury actor declares on another Fury actor.
- both involved Fury actors are later defeated.
- player is not Fury.

Disqualifiers:

- pact type active.
- both Fury actors join same faction before fighting.

Icon direction: two arrows crashing into each other over a small map.

### Alone Against the Major

Description direction: Defeat a Fury major while not in a faction.

Unlock conditions:

- a Fury country becomes major.
- player is not in a faction when the war starts and when Fury capitulates.
- player or player-led war contribution is meaningful.
- Fury major is defeated.

Disqualifiers:

- player joins a faction before Fury capitulates.
- Fury is defeated by unrelated AI with no player contribution.

Icon direction: lone shield in front of a large red map marker.

### Paper Borders Hold

Description direction: Stop Fury before it cores any conquered state.

Unlock conditions:

- Fury wins at least one war.
- Fury does not complete any coring decision.
- Fury is defeated or contained.
- player contributed to containment through war, aid, or border missions.

Disqualifiers:

- any Fury-cored-state flag is set.
- player becomes Fury.

Icon direction: official border papers stamped and intact.

## Achievement tracking notes

The implementation should track:

- first Fury actor.
- first conquest fired.
- Fury major super-event fired.
- Fury actor count by scenario setup.
- scenario intensity and type.
- player was never Fury.
- player faction and factionless status for specific achievements.
- Fury coring completion.
- Fury world-end active and defeated.
- two Fury actors fought each other.
- player contribution or aid contribution where needed.

Achievement icons are handled through the asset prompt.

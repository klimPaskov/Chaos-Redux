# Event 19 Achievement Matrix

Titles below are working labels, not final player-facing localisation. Final titles and descriptions must be written during implementation from the direction supplied here.

## Achievement set

| Working ID | Eligibility | Unlock condition direction | Disqualifiers | Visibility | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| `019_infantry_spawn_every_rifle_accounted_for` | any country | close a very large generation with high control, low congestion, no revolt, and no unresolved debt | claimant takeover, derivative revolt, debug or forced completion | visible | hard | complete roster, stacked rifles, sealed ledger |
| `019_infantry_spawn_one_battalion_wonder` | any country | a one-combat-battalion event division earns a significant combat or war result and survives | template expanded before feat | hidden | hard | lone battalion marker against a large front |
| `019_infantry_spawn_the_army_has_voted` | any country under Evolution III | accept or suffer a claimant takeover, then win a major war or survive a long specified period | claimant removed before proof | visible | hard | ballot box crossed with command baton, no readable text |
| `019_infantry_spawn_order_from_noise` | any country | at Evolution III, integrate many distinct random lots while ending at very high control and low congestion | use of forced scenario setup | visible | very hard | chaotic unit symbols arranged into a precise formation |
| `019_infantry_spawn_combined_arms_accident` | any country | win a major battle with one event division containing a large number of distinct valid battalion families | deliberate template edit removes generated identity | hidden | very hard | mismatched cavalry, armor, bicycle, and artillery silhouette |
| `019_infantry_spawn_no_room_on_the_train` | any country with a large generation | keep the main supply network functional while integrating a specified high division count | rail mission failure or emergency exploit | visible | hard | train surrounded by unit markers without derailment |
| `019_infantry_spawn_borrowed_future` | any country | win a major battle with a technology-locked advanced event formation before unlocking its core technology | obtaining technology first, cloning template equipment | hidden | hard | advanced vehicle emerging from an old depot |
| `019_infantry_spawn_three_false_apocalypses` | any ordinary country | defeat zombie, ghost, and golem derivative countries in one campaign while parent event identities remain distinct | playing a derivative, forced parent-event merge | visible | extreme | three contained silhouettes behind separate seals |
| `019_infantry_spawn_barracks_of_babel` | any country | a generated division containing camel, bicycle, amphibious tank, flamethrower element, and other required valid types wins a major battle | manual template construction | hidden | extreme | impossible mixed column, readable at 64 by 64 |
| `019_infantry_spawn_quiet_demobilisation` | any country | supervised demobilization of a very large generation with no revolt, no equipment exploit, and stable control | emergency instant removal, claimant seizure | visible | hard | orderly stacks, departing columns, intact seal |
| `019_infantry_spawn_every_barracks_a_front` | triggerable scenario | survive or win under Maximum General Mutiny or Anomalous Rising with the starting country and no terminal world-end state | lowering intensity after launch, tag switching | visible | extreme | country outline filled with many hostile formation markers |

## Tracking notes

### Generated-identity preservation

Achievements involving a random division need a persistent division or lot identity. Manual template editing, deleting, or converting the division must not satisfy a generated-composition achievement unless the achievement explicitly allows standardized follow-up.

### Battle significance

A significant battle should use a robust criterion such as:

- minimum enemy strength
- minimum combat duration
- minimum casualties or damage
- victory in a named war objective

It should not unlock from a token skirmish against an empty unit.

### Parent-isolation achievement

`three_false_apocalypses` must verify derivative origin flags rather than infer from unit appearance alone. It should also verify that the player did not simply defeat the parent Zombie or Death actor and count it as a derivative.

### Scenario achievement

The scenario achievement reads stored launch type and intensity. The temporary bypass flag is not the achievement source.

## Achievement text direction

- Titles can use military, bureaucratic, and darkly absurd language.
- Descriptions should state the visible challenge without revealing hidden random thresholds.
- No achievement text should be advertised in ordinary event, focus, or decision descriptions.
- Historical coercive mobilization should not be treated as slapstick.

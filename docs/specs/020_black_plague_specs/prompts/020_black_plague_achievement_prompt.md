# 020 Black Plague achievement prompt

Use this prompt after the implementation agent has read the full Event 020 Black Plague spec package. Achievements should be difficult and should not unlock just because the event fired, because the player clicked one obvious decision, or because a rat country appeared.

All titles and descriptions are direction only. Do not use the working labels as final localisation unless a later localisation pass deliberately rewrites and approves them.

## Achievement suite

| Working id | Eligible country | Difficulty | Hidden | Unlock direction | Disqualifier direction | Icon direction |
| --- | --- | --- | --- | --- | --- | --- |
| `020_black_plague_clean_room` | any country with first infected state or outbreak owner | hard | visible | contain and cure the first outbreak state before infection spreads to another state | disease spreads beyond the first state, first state reaches collapse, or player weaponizes Black Death | clean cordon around one dark state |
| `020_black_plague_no_graves_left_open` | any country | hard | visible | suffer severe Black Death deaths, reach mature cure progress, clean every owned infected state, and never weaponize | use or progress weaponization, lose a state to rats, or fail cleanup before route timeout if implemented | hospital and black fog fading |
| `020_black_plague_firebreak_continent` | any country on a threatened continent | very hard | visible | after Evolution II, prevent any overseas infection from establishing on the player's home continent for a long exposure period | own or control an infected port on the protected continent | port cordon and continent mark |
| `020_black_plague_black_doctor` | bio-capable country | hard | hidden | study Black Death defensively and reach high cure contribution without causing a home accident | weaponized deployment, major domestic accident, or plague collapse in capital | mask and sealed sample in abstract style |
| `020_black_plague_bad_idea_survived` | bio-capable country | very hard | hidden | weaponize Black Death, deploy it, survive diplomatic backlash, and avoid domestic outbreak collapse | domestic capital outbreak, rat emergence in owned states, or world-end caused by rats | cracked payload and shield motif |
| `020_black_plague_last_quarantine` | country bordering rats | hard | visible | hold a rat-border cordon long enough to stop a rat country from entering core states | lose a core state to rats during the cordon period | wire line and rat shadow |
| `020_black_plague_first_warren_burned` | any human country | medium hard | visible | destroy the first rat nation before any second rat nation appears | a second rat nation appears first or King forms before destruction | burning warren mark |
| `020_black_plague_no_crown` | any human country | very hard | hidden | prevent the King of Rats from appearing after Evolution III becomes possible | King appears | broken crown before completion |
| `020_black_plague_crown_hunter` | any human country | very hard | visible | defeat the King after it controls a large region but before the world-end path completes | rat world-end fires or King is defeated before it became a major threat if the implementation tracks this | spear, cordon, or cleanup mark through rat crown |
| `020_black_plague_clean_continent` | any human country | very hard | visible | clear all Black Death, rat-held, and warren-remnant states from a continent after the King existed | leave active relapse pressure, infected states, or warren remnants on the target continent | continent and cleanup flame |
| `020_black_plague_play_the_warren` | base rat nation | hard | hidden | as a base rat nation, absorb another rat nation and become the dominant warren before King formation | become King before absorption if the achievement requires base form | two nests merging |
| `020_black_plague_crowned_below` | King of Rats | hard | visible | form the King and complete the coronation trunk while holding all inherited warrens | lose the capital nest or inherited warren group before the trunk is complete | rat crown below tunnel |
| `020_black_plague_three_minds` | King of Rats | hard | hidden | complete one accepted King government route capstone, with optional variants for Royal Command, Brood Council, and Hunger Mind | route switching exploit, missing route lock, or failing route-specific control requirements | crown, council, and hunger triptych |
| `020_black_plague_continent_under_earth` | King of Rats | very hard | visible | control the required continent group as King without triggering world-end yet | terminal scenario fires before the non-terminal control condition is recorded | continent tunnel motif |
| `020_black_plague_rat_world` | King of Rats | extreme | hidden | trigger the rat world-end scenario | none beyond normal world-end conditions | world under rat crown |
| `020_black_plague_humanity_returns` | human coalition leader or major human country | extreme | hidden | defeat a near-terminal King and clean enough states to stop relapse and warren remnants | world-end succeeds or major warren remnants remain | broken crown and survivor cleanup motif |

## Tracking requirements

The implementation should add durable tracking for:

- first outbreak state id
- whether the first outbreak spread before containment
- first outbreak maximum severity
- cure progress by country or contribution tier
- whether the player ever studied Black Death defensively
- whether the player ever started weaponization
- whether the player ever deployed a Black Death payload
- whether a Black Death accident occurred at home
- domestic capital outbreak or collapse flags
- severe death threshold reached by the player's country
- every owned infected state cleanup completion where needed
- first rat nation id
- number of rat nations appeared
- first rat nation destroyed state
- King of Rats formation
- King source country
- King maximum controlled states
- King maximum continent progress
- King world-end path started and completed
- rat-held state maximum count
- continent cleanup completion
- warren-remnant cleanup completion
- route identity when playing base rats or King
- player tag transition from base rat to King where applicable

## Visibility and spoiler rules

Achievements that reveal rat nations, King formation, or the rat world-end path should be hidden until the implementation accepts public visibility. Public achievement text should not spoil the King before the player has discovered rat content unless the achievement is deliberately hidden.

Achievement UI can be more direct than ordinary event text, but it should still avoid giving away hidden implementation details. Keep early disease achievement wording focused on containment, cure, ports, and safe study.

## Icon requirements

Each achievement needs a completed 64x64 icon. Create grey and not-eligible variants when the achievement registry requires them.

Achievement icons must be designed as achievement icons, not resized focus or idea icons. Use `chaosx_icon_artist` and inspect achievement references before generation. Record every source, processed preview, final DDS, and status in the asset manifest.

## Implementation requirements

- Register achievements in the existing Chaos Redux achievement structure.
- Add localisation after final route and achievement visibility decisions are stable.
- Add icons and sprite references.
- Add tracking flags or variables where a final state cannot be checked from one trigger.
- Add disqualifiers that fail clean containment, no-weapon, or no-King achievements at the time the disqualifying action happens.
- Handle player tag switching, rat tag play, King transformation, annexation, defeat, and world-end state.
- Update event docs and catalog material after final implementation and localisation are known.
- Do not add automatic unlocks for simply seeing the event, forming the King, or ending the world unless the listed conditions also apply.

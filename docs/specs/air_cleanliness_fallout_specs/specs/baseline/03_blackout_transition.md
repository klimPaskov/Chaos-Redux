# Air Cleanliness and Fallout World-End Source Spec, Part 3 Fallout Transition and Black Screen

Canonical status: accepted baseline design, corrected for independent Fallout ownership and extended by the living-world specs in this package.

Working label, not final localisation: `fallout_blackout_sequence`.

## Transition purpose

Fallout should feel like the campaign has been broken and rebuilt. The player should not receive an ordinary report event. The screen should go black, ordinary UI should become unavailable, and short centered text beats should appear one after another. The text must be final-written during implementation, not copied from this spec.

The blackout hides heavy state processing and creates a clean emotional boundary between the old world and the post-Fallout campaign.

## Black screen sequence

The black-screen sequence should use a scripted GUI overlay or equivalent UI surface. It should cover the full screen, block ordinary interaction, and show one centered text beat at a time.

| Beat number | Direction for final text | Gameplay processing window |
| ---: | --- | --- |
| 1 | The old world has ended. | Freeze ordinary event firing and diplomacy processing. |
| 2 | Mass death has already happened. | Apply immediate death accounting and state population reductions. |
| 3 | Survivors are scattered and sealed away. | Assign shelter, bunker, refugee, and isolated survivor states. |
| 4 | Governments no longer control what they once controlled. | Break old factions, clear invalid wars, set government collapse flags. |
| 5 | The sky itself has become the new border. | Assign winter and Fallout categories. |
| 6 | Some people have changed in ways no ministry can classify. | Seed mutant and altered-country candidates. |
| 7 | The player will continue in the new world. | Select player successor if the old tag is dead or transformed. |
| 8 | The map returns. | Remove blackout, open Fallout introduction interface. |

These are not final localisation lines. They are directions. The implementation agent must write final text that follows Chaos Redux writing rules, avoids staccato filler, avoids em dashes, avoids semicolons, and avoids generic apocalypse titles.

## Processing order during blackout

| Step | What changes |
| ---: | --- |
| 1 | Store the cause memory and pre-Fallout global snapshot. |
| 2 | Stop automatic random event firing, ordinary world-end selection, and incompatible crises. |
| 3 | Apply immediate death and population effects from the triggering cause. |
| 4 | Assign state Fallout grades. |
| 5 | Rewrite state categories and damage buildings. |
| 6 | Break old diplomatic blocs, guarantees, and normal trade assumptions. |
| 7 | Decide which governments survive, which fragment, and which become cosmetic successors. |
| 8 | Spawn warlords, refuges, bunker authorities, mutant polities, and continuity governments. |
| 9 | Load or assign Fallout focus-tree packages. |
| 10 | Activate survival resources, survival decisions, and mapmode layers. |
| 11 | Choose player continuation target if required. |
| 12 | Open the first Fallout interface and release the blackout. |

## Manual scenario timing

The manual Fallout scenario must do the following.

1. Apply thermonuclear strike effects to every valid province.
2. Mark every state as manually nuked for Fallout grade calculation.
3. Set a seven-day visible countdown with a severe warning that the world rewrite is coming.
4. Let the engine display destruction for that week.
5. Fire the blackout sequence.
6. Rewrite the world into Fallout.

If province-level thermonuclear application is technically impossible in HOI4, implementation must stop and report a blocker. It must not quietly downgrade the scenario to a state-only visual effect.

## Fallout state grade model

Every state receives one grade. This grade controls category rewrite, population, building damage, local resources, country spawning, and later salvage.

| Grade | Working label | Source conditions | Result |
| ---: | --- | --- | --- |
| 0 | Remote refuge | Low target density, low exposure, remote or sheltered | State remains livable, may host refugee or continuity government. |
| 1 | Scarred province | Indirect fallout and severe winter | Damaged but recoverable. Buildings remain valuable. |
| 2 | Ash zone | Nuclear fallout, Phase 4 or higher, infrastructure failure | Population drops, buildings damaged, survival decisions needed. |
| 3 | Dead city | Dense city, industrial strike, high deaths | State becomes salvage hub, high attrition, low ordinary population. |
| 4 | Wasteland | Direct thermonuclear or terminal exposure | State category becomes wasteland or equivalent. Severe attrition. |
| 5 | Vitrified zone | Direct thermonuclear in high-value target or repeated strikes | Almost no ordinary life. Rare mutants, robots, sealed bunkers, or forbidden zones. |
| 6 | Altered biosphere | High radiation plus biological, chemical, or strange cause memory | Mutant countries, fungal states, strange units, unique research and dangers. |

## Cause memory impact on state grades

| Cause memory | Grade bias |
| --- | --- |
| Manual full thermonuclear exchange | High direct bias to grades 3, 4, and 5 across the entire map. |
| Gradual air collapse | More grades 1, 2, and 6, fewer vitrified zones unless nuclear use was high. |
| Final Silence | More impossible altered terrain, cult successors, dead pilgrimage routes, and black-sky zones. |
| Chemical saturation | More toxic fog states and gas-mask polities. |
| Biological collapse | More quarantine states, sterile cities, and altered biosphere zones. |

## Government collapse model

Every pre-Fallout country is evaluated.

| Result | Conditions | Outcome |
| --- | --- | --- |
| Continuity state | Capital bunker, high legitimacy, remote or protected capital | Same tag survives with a Fallout cosmetic identity and continuity focus tree. |
| Fragmented state | Several survivable state clusters but no unified command | Existing releasables or civil-war tags appear with warlord, regional, or bunker cosmetic identities. |
| Occupied wasteland | Core areas mostly grades 4 to 5 | Tag may disappear or become a remnant with one bunker state. |
| Mutated successor | Altered biosphere, high fallout, biological or strange cause | Existing tag or releasable receives mutant cosmetic identity and mutant focus tree. |
| Refuge government | Old government loses core land but has overseas or island holdout | Exile or port authority identity with diplomacy and reclamation branches. |
| Dead tag memory | No survivable governance | Tag is marked dead for achievements and event memory. Its ruins become salvage states. |

## Old world cleanup

Fallout must feel like a new game. Ordinary factions, world tension logic, trade routes, standard treaties, guarantees, and event chains that assume normal governments should stop or become dormant. Some event-created threats can remain only if they make sense after Fallout.

| Old system | New rule |
| --- | --- |
| Normal factions | Dissolved or converted into compact memories. |
| Guarantees | Cleared unless a surviving compact focus restores them. |
| Trade | Replaced by survival convoys, barter, and port compacts. |
| Diplomacy | Limited by radio range, passable routes, and recognition. |
| Normal random events | Paused or filtered to Fallout-compatible events. |
| Air Cleanliness | Becomes the permanent atmosphere system and mapmode. |
| Deaths | Continues with Fallout death sources. |
| Condemnation | Freezes old blame as history, new blame uses survival atrocity and contamination abuse. |
| World threats | Reset into Fallout threat sources. |

## Player continuation

The player should not lose the ability to play because their old country was destroyed. The transition should offer a player-continuation choice when needed.

| Situation | Continuation rule |
| --- | --- |
| Old tag survives | Continue as old tag with new cosmetic identity. |
| Old tag fragments | Offer a choice among strongest successors, with details on politics and starting problems. |
| Old tag dies but has exile or port refuge | Continue as refuge government by default, with option to choose a local warlord. |
| Old tag becomes mutant polity | Player may accept mutation route or choose a human continuity remnant if one exists. |
| No obvious successor | Assign nearest survivable state or largest refugee cluster as an emergency council. |

## First Fallout interface

After the blackout, the player sees a Fallout introduction interface. This is not a super-event. It should show:

- Cause memory.
- Player successor identity.
- Map status summary.
- Survival resources.
- Nearest threats.
- First 180-day objectives.
- Mapmode button.
- Focus tree route hint.

The interface should use strong art and sound, but it should not use super-event quote, button, or music structure.

# Achievement prompt for Event 16 Brilliant Scientist

Implement achievements only when their gameplay route exists, is trackable, has localisation, has asset coverage, and has disqualifiers where needed. Title labels in the specs are working labels, not final localisation.

## Core achievement families

Cover these route families: recruiting Kruger and surviving his benefits, sending him away and later defeating or exploiting the result, public science without losing control, military science without immediate collapse, ethical restraint, sealed-project escalation, Kruger secession, defeating the Kruger State, surviving the final-device race, stopping the final device at the last practical moment, and recovering useful science after containment.

## Project route achievements

Use the second-pass achievement matrix for route-specific achievements. Include achievements for public medicine restraint, military lab control, audit mastery, no sealed city, clone conquest, machine low-manpower victory, specimen war, xenotech material route, temporal fast victory, final-device sabotage, foreign attention web, clean containment without panic, postwar science oversight, all facility memories, and last-moment final-device stoppage.

## Tracking expectations

Achievements should require several conditions at once. Use route flags, project memory variables, facility memory, confrontation outcome, evolution state, Kruger country status, foreign attention state, final-device progress, world-end state, and player country identity where needed. Add failure flags for shortcuts, hidden disqualifiers, puppet abuse, automatic event participation, and route choices that invalidate the achievement.

## Asset expectations

Every implemented achievement needs a unique completed 64x64 icon and standard variants. Icon direction should match the route rather than using a generic scientist portrait.

## Validation expectations

Audit that no achievement unlocks merely because the event fired, Kruger was recruited, or the player clicked an obvious option. Secret achievements can hide description detail, but implementation notes must still define exact requirements.

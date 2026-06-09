# Event 007 Fury AI Matrix

## AI actor groups

| Actor | Role |
| --- | --- |
| Fury country | expands into weaker AI land neighbors |
| First target | emergency defense and survival |
| Later targets | prepare if Fury is nearby |
| Other Fury countries | cooperate from Evolution II onward |
| Nearby majors | contain, guarantee, or ignore based on risk |
| Player countries | never selected as Fury or scripted targets |

## Fury AI route behavior

| State | Preferred behavior |
| --- | --- |
| low momentum | finish current war, avoid stronger targets |
| high momentum | shorten declaration delay and seek next target |
| high occupation strain | take administration focuses and integration decisions |
| low supply | prioritize logistics focuses and supply missions |
| low manpower | use weaker militia packages and avoid all-front if not Evolution III |
| many weak neighbors | choose General Staff route |
| captured many states | choose March Administration route |
| another Fury exists | choose cooperation branch if Evolution II active |
| no valid neighbors | enter no-neighbor branch |
| high chaos and no-neighbor | evaluate world-end preparation |

## Target AI behavior

Targets should not receive large unfair buffs, but they should react.

Possible reactions:

- emergency militia if weak
- defensive AI strategy for capital and border
- seek guarantees if nearby major and diplomacy allows
- pull units from unrelated fronts if not already collapsing
- avoid suicidal attacks into Fury if outmatched

## Nearby major AI behavior

Majors should not always intervene. They evaluate:

- distance
- faction membership
- ideology
- Fury expansion speed
- whether Fury is near their borders or subjects
- chaos value
- number of active Fury countries
- whether Fury has become major
- whether world-end branch is near

Possible actions:

- guarantee a likely next target
- send volunteers or aid if a general support system exists
- join containment war through ordinary game rules if interests align
- ignore a distant low-chaos Fury war

## Evolution AI behavior

| Evolution | AI change |
| --- | --- |
| I | Fury accepts slightly harder first targets and uses better units |
| II | Fury seeks partner coordination and avoids partner conflict |
| III | Fury declares on all valid weaker neighbors at once and accepts overextension |

## Anti-suicide rules

Fury should not:

- declare on a stronger major under ordinary branch logic
- declare on a player through scripted target logic
- declare when its capital is about to fall unless Evolution III or world-end branch demands it
- repeat target a country that no longer exists
- continue expansion decisions after capitulation
- choose a focus branch that requires another Fury country when none exists
- try to form or lead Fury Pact if it is a subject and the faction would break normal diplomacy

## Validation scenarios

1. One-state AI minor with one weak AI neighbor becomes Fury and declares once.
2. Fury defeats first neighbor, fires news, then selects another weaker AI neighbor.
3. Fury has only player neighbors, it should not fire or should enter no valid target state.
4. Fury capitulates during first war, cleanup removes active loops.
5. Evolution II selects two Fury countries and enables cooperation only if both remain alive.
6. Evolution III selects three Fury countries and each declares on all valid weaker AI neighbors.
7. Fury becomes major, super-event fires once.
8. Fury has no valid neighbors and high chaos, world-end branch becomes possible only if threshold rules are met.
9. Existing country with meaningful focus tree is not replaced unless the event set the Fury origin flag.
10. Player never receives Fury flag, Fury tree, Fury decisions, or scripted Fury target declaration.

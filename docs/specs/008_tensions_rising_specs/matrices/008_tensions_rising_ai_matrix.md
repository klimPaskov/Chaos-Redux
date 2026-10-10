# Event 008: AI and System Behavior Matrix

Disposition: the implemented posture layer is described as current; the wider action-family directions remain unresolved design, and numerical validation is blocked with the probability owner.

Event 008 influences AI through timed posture ideas, timed relation damage, and incident consequences.
It never forces a normal war declaration; Stage III+ incidents can rarely start safe non-transfer border clashes.

## AI principle

AI behavior should feel like governments reacting to an atmosphere.
The event may raise willingness for already-valid systems, but it must not bypass target validity, route validity, alliance rules, or existing war logic.

## Implemented posture layer

Each evolved root gives one hidden timed idea to AI countries that are majors, faction leaders, or already at war and were not recently selected.

| Stage | Idea | Countries | Days | Direction |
| --- | --- | ---: | ---: | --- |
| I | `tensions_rising_cautious_alignment` | 4 | 45 | cheaper guarantees, stronger alliance desire, small defensive-war stability |
| II | `tensions_rising_alarmist_rearmament` | 6 | 75 | adds war support and arms production, small stability loss |
| III | `tensions_rising_general_staff_fever` | 8 | 100 | stronger rearmament, planning speed, faster enemy justification against the country |
| IV | `tensions_rising_permanent_alert` | 12 | 140 | the strongest version of the same pressure |

Embassy Side Doors, Staff Cars After Midnight, Fleets Keep Radio Silence, and The Last Normal Briefing add extra posture applications.
No player country receives a posture idea, and no idea grants war goals, units, cores, or claims.

## Actor groups

| Actor group | Baseline | Stage I | Stage II | Stage III | Stage IV |
| --- | --- | --- | --- | --- | --- |
| Major powers | normal WT reaction | cautious posture | rearmament posture | staff-fever posture, possible clash actor | permanent-alert posture, still target-checked |
| Faction leaders | normal | cautious posture | rearmament posture | staff-fever posture | permanent-alert posture |
| Border rivals | normal | possible relation shock | relation shock likely | safe clash candidates | clash candidates with cooldowns |
| Naval powers | normal | none | insurance incident possible | radio-silence incident possible | radio-silence incident more likely |
| Minor and neutral countries | normal | mostly flavour | relation shocks only | relation shocks and clash candidates | relation shocks and clash candidates |
| Special chaos and nonhuman tags | excluded | excluded | excluded | excluded | excluded |

## Design directions not yet expressed in source

These remain unresolved design and are not current requirements:

| Action family | Direction | Hard limits |
| --- | --- | --- |
| Faction invitations | rise with stage | ideology, geography, and faction rules respected |
| Existing hostile decisions | rise with stage | valid targets only |
| Secret-diplomacy systems | rise from Stage II where an approved hook exists | owning event requirements respected |

Guarantees, rearmament, and planning are already covered by the posture ideas' modifiers.

## AI weights by world condition

- A country already in a major war gains defensive and production posture rather than new fronts; clash actors must be at peace.
- A peaceful country bordered by safe rivals is the natural clash and relation-shock candidate.
- A subject is excluded from relation shocks and clashes.
- After `world_end`, automatic Event 8 stops and queued incidents close.

## AI exploit prevention

- Hidden Stage IV pressure never produces impossible or suicidal wars; clashes stay non-transfer, cooldown-gated, and target-checked.
- Temporary relation damage expires and never locks allies into permanent hostility.
- No permanent AI strategy flag is created.

## Human-player visibility

The player never sees a raw AI modifier list.
They infer the shift from incidents, relation changes, guarantees, alliances, border clashes, and the event log.

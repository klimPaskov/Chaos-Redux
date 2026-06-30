# Event 011 Secret Alliance Event Chain, Evolution Log, and Details Plan

This file maps the event chain and the player-facing log surfaces.

## Event chain roles

| Working event id | Role | Player-facing state |
| --- | --- | --- |
| chaosx.nr11.1 | Root firing and founder selection | First quiet report |
| chaosx.nr11.2 | First closed meeting follow-up | Baseline pattern grows |
| chaosx.nr11.3 | Press whisper incident | Low-intensity diplomatic pressure |
| chaosx.nr11.4 | Courier trace incident | Chance for early clue |
| chaosx.nr11.5 | Procurement irregularity | War readiness seed |
| chaosx.nr11.6 | Evolution I unlock | More minor recruitment |
| chaosx.nr11.7 | Minor invitation report | Possible clue from refusal or leak |
| chaosx.nr11.8 | Low sabotage report | First tangible domestic impact |
| chaosx.nr11.9 | Evolution II unlock | Dossier opens and active sabotage begins |
| chaosx.nr11.10 | Major patron joins or founds evolved opening | Major involvement becomes possible |
| chaosx.nr11.11 | Factory sabotage | Industry pressure |
| chaosx.nr11.12 | Targeted intimidation | Political or officer pressure |
| chaosx.nr11.13 | Border provocation | Neighbor target mission or border war path |
| chaosx.nr11.14 | Exposure attempt result | Public scandal, partial success, or failure |
| chaosx.nr11.15 | Defector event | Member exit or false defector risk |
| chaosx.nr11.16 | Evolution III public compact | Public faction appears |
| chaosx.nr11.17 | Public ultimatum | War timer and demands |
| chaosx.nr11.18 | Forced reveal from war | Immediate faction creation and war join |
| chaosx.nr11.19 | Pact war opening | War state setup |
| chaosx.nr11.20 | Pact collapse by exposure | Peaceful dismantling outcome |
| chaosx.nr11.21 | Pact defeat | Postwar cleanup outcome |
| chaosx.nr11.22 | Pact victory | Target capitulation or severe concession outcome |
| chaosx.nr11.23 | Aftermath cleanup | Removes temporary systems and preserves durable flags |

The exact numbering can change if the repository has existing Event 011 ids. Keep the root id stable.

## Evolution log entries

Only three evolution entries should be recorded.

| Evolution | Stage | Trigger direction | Log direction |
| --- | ---: | --- | --- |
| Wider minor compact | I | Pact cohesion, time, member count, and chaos support minor recruitment | Several minor governments now move in a recognizable pattern without public admission |
| Patron and sabotage phase | II | Compact aggression, evidence pressure, and possible major patron entry | The pattern becomes active enough for a dossier and direct counterplay |
| Public compact | III | Public reveal, major entry, high war readiness, exposure, or war conversion | The hidden network becomes a public Anti-[target] Pact |

Do not record normal dossier progress, individual sabotage, member invitation, or war timer movement as evolutions.

## Event Details direction

The Event Details window should use dynamic text direction based on reveal state.

| State | Detail direction |
| --- | --- |
| Before event fired | The catalog describes the premise as a secret anti-player diplomatic pattern that can grow into sabotage and public faction pressure |
| Hidden baseline | Describe odd diplomacy, repeated contacts, and foreign public habits without naming members |
| Dossier open | Describe an unresolved compact investigation, the dossier values, and the player's response tools |
| Public compact | Describe the public faction, members, war horizon, and remaining diplomatic routes |
| War state | Describe the open anti-target war and how preparedness affects defense |
| Defeated or dissolved | Describe the outcome and cleanup state |

Event Details should not list raw effects or reward values. It should describe the situation and the visible pressure.

## History log actor handling

The root history row should show the target country as actor or affected country. Hidden member actors should not appear in the public history row before identification unless the row represents a clue that names a member. Evolution rows with an actor should use the compact convenor, major patron, or target only when that actor is visible to the player.

## Evolution catalog wording direction

The evolution preview in the event catalog should explain what each evolution adds without spoiling every hidden branch. It can state that minor recruitment increases, that major patronage and sabotage can begin, and that the public compact can appear. It should not reveal member selection formulas.

## Dossier entry log

The dossier should maintain a compact recent-actions list. It can show entries such as courier leads, protected factories, border screens, member identifications, exposure attempts, and defector outcomes. This list should be dynamic and not pollute the global event history.

## Spreadsheet handoff direction

After implementation, the catalog row should be updated from the final in-game Event Details and evolution wording. The row should not expose hidden formulas. The current row is a placeholder and should be replaced only after localisation and event detail selectors exist.

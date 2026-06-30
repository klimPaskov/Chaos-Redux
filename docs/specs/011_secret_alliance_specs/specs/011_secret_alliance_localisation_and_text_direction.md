# Event 011 Secret Alliance Localisation and Text Direction Handoff

This file gives direction for final player-facing text. It is not final localisation and should not be pasted into game files.

## Global style direction

The event should sound like a state noticing a repeated foreign pattern before it can prove the pattern. Early text should use concrete details such as repeated delegations, shared newspaper phrases, couriers, railway curiosity, contracts, border patrol habits, and odd embassy behavior. It should not announce that the player has found a hidden alliance.

Avoid:

- labels that tell the player a clue is a warning
- dramatic prophecy language
- contrast structures between public denial and private truth
- modern intelligence jargon where period diplomatic language works better
- joke buttons during sabotage, intimidation, or deaths
- final titles based on unresearched quotes or songs

## Event popup text direction

| Popup family | Viewpoint | Information visible | Tone |
| --- | --- | --- | --- |
| Root report | Target government | Several countries show an odd diplomatic rhythm | Curious, restrained, uneasy |
| Baseline meeting | Foreign-service staff | Attachés, trade delegates, and junior envoys move through neutral venues | Observational, not accusatory |
| Press whisper | Public and press staff | Similar accusations or editorials appear in different countries | Annoyed, cautious, political |
| Courier trace | Intelligence clerks | Couriers and pouches cross between legations | Procedural, tense |
| Procurement irregularity | Industrial staff | Repeated contract patterns point toward military planning | Practical, suspicious |
| Evolution I | Intelligence and foreign office | Minor governments behave as if they have a shared rhythm | Uneasy, still incomplete |
| Evolution II | Cabinet and intelligence staff | Evidence is strong enough to open a dossier | Serious, actionable |
| Sabotage | Civil defense and investigators | Actual damage or disruption occurs | Concrete, restrained, no cheap humor |
| Border provocation | Border command | Patrols, checkpoints, or local units create an incident | Controlled tension |
| Defector | Intelligence service | A member or agent offers testimony | Suspicious, conditional, risky |
| Public compact | Public diplomacy | The compact becomes open and organized | Political, severe, specific |
| Ultimatum | Cabinet and military | Public demands and war pressure arrive | Cold, formal, hostile |
| War opening | Military command | The pact acts openly | Direct and operational |
| Collapse or defeat | Foreign office and intelligence | Networks are dismantled or public faction broken | Measured relief, lingering caution |

## Option tone direction

| Option role | Tone | Notes |
| --- | --- | --- |
| Ignore early pattern | Irritated dismissal | Should feel plausible, not foolish |
| Quietly file evidence | Professional caution | Good early option for players who notice patterns |
| Ask for clarification | Diplomatic politeness with suspicion underneath | Can create relation risk |
| Harden factories | Practical civil defense | No boastful tone |
| Push exposure | Assertive, legalistic, public | Should warn through tooltips when evidence is weak |
| Bribe or reassure member | Political compromise | Should feel like a cost to pride or legitimacy |
| Prepare war | Military readiness | Serious, not bloodthirsty by default |
| Strike first | Hardline and risky | Tooltip should explain public consequences |

## Decision text direction

Decision titles should be clear actions. Decision descriptions should explain what the government is doing and what the visible result can be. Requirements should use icon-first costs and short custom trigger text. Target-specific decisions should mention the selected country through dynamic localisation.

Examples of direction, not final text:

| Decision family | Name direction | Description direction |
| --- | --- | --- |
| Trace couriers | Action verb plus courier or pouch motif | Intelligence staff follow diplomatic movements and look for repeated routes |
| Guard arsenals | Action verb plus arsenal or rail motif | Military police and local troops secure vulnerable industry and transport |
| Expose member | Public evidence motif | Government presents evidence against selected member or convenor |
| Split member | Diplomatic wedge motif | Envoys offer a way out or apply pressure to a wavering member |
| Border patrol | Border screen motif | Units secure named border states and watch crossings |
| War cabinet | Preparedness motif | Cabinet and general staff prepare for public confrontation |

## Event detail direction

Event Details should describe the current situation rather than effects. Use dynamic state:

| Condition | Detail content direction |
| --- | --- |
| Hidden compact active | Odd diplomatic behavior and repeated incidents surround the target country |
| Dossier open | The target country has enough evidence to begin active countermeasures |
| Major patron involved | A major power has become tied to the pattern, making the network more capable and more exposed |
| Public compact | The pact is now visible, named against the target, and preparing public pressure or war |
| Open war | Public members fight the target through the pact's military framework |
| Compact dismantled | The compact's network has been broken or absorbed into post-crisis diplomacy |

## Scripted localisation needs

| Key family | Dynamic inputs |
| --- | --- |
| Current pact target name | Target country name |
| Public faction name | Target country name |
| Selected dossier target | Selected country name or unknown card |
| Suspicion value | Target variable integer |
| Evidence value | Target variable integer |
| Preparedness value | Target variable integer |
| Member count | Valid member count |
| Major member count | Valid major count |
| Reveal reason | Evolution, exposure, failed operation, member war, player attack |
| War readiness status | Low, rising, imminent, delayed |
| Cohesion status | Fractured, wavering, steady, hardened |

## Super-event text gate

The public compact reveal super-event needs researched title, button remark, quote, and audio. Do not convert working labels into final text. The super-event research prompt defines the source workflow.

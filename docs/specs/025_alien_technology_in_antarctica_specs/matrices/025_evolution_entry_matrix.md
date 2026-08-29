# Evolution entry matrix

| Evolution | Minimum tier | Active-race entry condition | Pre-fire entry effect | Ordinary phase preserved | Disabled behavior |
| --- | --- | --- | --- | --- | --- |
| I Active Signal | Gathering Storm, 200+ | Active race, signal not recorded, MTTH influenced by survey and radio activity | Opening detects repeated active transmissions and initializes signal sectors | Yes | No signal flags, actions, incidents, or record |
| II Something Survived | Rising Chaos, 400+ | Outpost or survey phase, survivor evidence not recorded, MTTH influenced by opened compartments and missing personnel | Opening includes immediate trace or damaged-camp evidence | Yes | No survivor profile, contact action, or record |
| III Militarised Antarctica | Chaos Tier, 600+ | Several active participants and public hostility or strategic pressure, MTTH | Opening begins with armed escorts or exclusion zones already forming | Yes | No blockade, seizure, clash escalation, or record |
| IV Wreck Breaking Apart | Totalen Chaos, 800+ | Main sector probable or confirmed, wreck integrity pressure, MTTH | Opening detects multiple debris fields and unstable material | Yes | No fragment field, wreck integrity, or record |
| V Technology Changes Its Users | World Collapse, 1000+ | Usable alien technology held, dependence milestone not recorded, MTTH influenced by unsafe use | Opening seeds latent dependence property, visible only after technology use | Yes, then aftermath | No dependence, policy family, accident track, or record |

## MTTH direction

Base evolution pacing is around 90 days after eligibility.

Dynamic modifiers:

| Factor | I | II | III | IV | V |
| --- | ---: | ---: | ---: | ---: | ---: |
| Higher Chaos above threshold | Faster | Faster | Faster | Faster | Faster |
| More active participants | Slightly faster | Neutral | Faster | Slightly faster | Neutral |
| Aggressive signal action | Much faster | Slightly faster | Neutral | Neutral | Slightly faster |
| Missing personnel or opened compartment | Neutral | Much faster | Slightly faster | Neutral | Neutral |
| Public sabotage and armed escort | Neutral | Slightly faster | Much faster | Slightly faster | Neutral |
| Reckless wreck recovery | Neutral | Neutral | Slightly faster | Much faster | Faster |
| High Exposure Risk | Faster | Faster | Faster | Faster | Faster |
| Strong containment | Slower | Slower | Slower | Slower | Slower |

Exact factors require probability audit.

## Entry stage behavior

| Current baseline phase | I | II | III | IV | V |
| --- | --- | --- | --- | --- | --- |
| Entry window | Can alter first participant brief | Trace can appear in first reports | Armed preparations can be visible | Debris field can be known | Latent only |
| Mobilization | Signal affects equipment preparation | Rare early trace at gateway or radio intercept | Escort commitments appear | Debris reports alter search plan | Latent only |
| Crossing | Signal can guide or disrupt route | Ship or aircraft contact possible | Route patrols and blockade begin | Falling fragments can alter route | Latent only |
| Outpost | Full signal action set | Full survivor action set | Fortification and seizure begin | Fragment sites emerge | Latent only |
| Survey | Strongest search interaction | Tracks and compartments central | Hostile survey competition | Core-versus-fragment choices begin | Latent only |
| Final recovery | Signal affects success and risk | Survivor may interfere or assist | Corridor and seizure actions | Full wreck instability | Latent until reward applied |
| Aftermath | Signal may persist in material | Survivor custody or escape follow-up | Captive and incident settlement | Fragment settlement | Full policy and Dependence track |

## Evolution logging

Each evolution records one shared milestone with:

- Event ID 25
- stable evolution type
- stage 1 unless the live system requires another public stage
- displayed tier
- date
- actor only for a deliberately country-owned milestone

Country-specific Dependence bands are ordinary aftermath state, not separate evolution rows.

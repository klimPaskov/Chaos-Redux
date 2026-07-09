# Event 019 Infantry Spawn spec part 5, Evolution IV chaos units and splinter countries

This file defines the high-chaos layer. It uses working labels only.

## Evolution IV identity

Evolution IV lets the event touch Chaos Redux special unit families. The rule is strict: this event uses a registry of units that are allowed to appear through Infantry Spawn. It must not copy parent event logic, hijack parent event countries, or grant every unit family full access.

Chaos units should feel like the army has started receiving formations from systems that were never meant to obey a normal staff. The player can use them, but each use raises chaos_leakage and can create a splinter country if mismanaged.

## Chaos unit registry

Implementation should create or reuse a single dynamic registry for event-spawnable chaos units. Future chaos units should be added to the registry once, then Infantry Spawn can use them without needing a separate reminder.

Registry fields should include:

| Field | Purpose |
| --- | --- |
| unit_profile_id | Stable internal profile id |
| display direction | Localisation direction, not final text |
| unit type or template hook | What division or battalion family is spawned or trained |
| availability | spawn-only, trainable, or both |
| minimum evolution | Evolution IV by default |
| minimum chaos context | calm, high chaos, total chaos, world collapse as tuning bands |
| spawn weight | Base chance among chaos units |
| abuse weight factor | How strongly reckless use raises future chance |
| country profile | Which lesser splinter profile can form from abuse |
| parent event isolation | Parent event mechanics that must not be called |
| cleanup rules | What flags, training unlocks, and template access are removed if contained |
| AI permission | When AI can use or avoid the unit |

The registry should live in a reusable helper or documented scripted system. The event spec recommends a helper family with names chosen by the implementation agent after inspecting existing Chaos Redux dynamic effects.

## Initial chaos unit profiles

| Unit family | Availability | Player access | Breakaway risk | Parent isolation rule |
| --- | --- | --- | --- | --- |
| Base zombie unit | Trainable after authorization, also low-weight spawn | Only the base zombie unit, no stronger variants | Ragged horde profile | Does not trigger Zombie Outbreak evolutions or parent horde logic |
| Ghost divisions | Spawn-only | Can be kept, exorcised, or quarantined | Grey host profile | Does not create Death, Black Ledger, or instant state erasure |
| Golem divisions | Spawn-only | Can be bound, stationed, or dismantled | Stone host profile | Does not call any future parent golem event chain |
| Future chaos units | Registry-defined | Follow registry availability | Registry-defined lesser profile | Must document what parent mechanics are blocked |

Zombies are the only initial chaos unit family that should become trainable. The trainable unit must be the base zombie unit only. Stronger zombie variants stay locked to the Zombie Outbreak event.

Ghosts and golems are spawn-only. The player can receive, move, and fight with them if the template supports it, but cannot train them from the normal recruit screen unless a later design explicitly changes the registry and docs.

## Chaos unit management decisions

| Decision family | Unit family | Action direction | Costs | Risks |
| --- | --- | --- | --- | --- |
| Authorize base zombie training | zombie | open limited recruitment | manpower policy, stability, medical or security burden, chaos leakage | zombie splinter risk, foreign alarm |
| Cap zombie recruitment | zombie | close training and stop new queues | stability, command power, possible unit anger | lower leakage, lower short-term army size |
| Quarantine zombie cadres | zombie | isolate or destroy unsafe units | support equipment, manpower, local control | casualties, stability hit, lower splinter risk |
| Exorcise ghost companies | ghost | remove or weaken ghost units | army XP, support equipment, stability, local state objective | lose units, lower wasteland risk |
| Assign ghost perimeter duty | ghost | keep ghosts away from cities | supply and command costs | slower harm, lower combat use |
| Bind golem cadres | golem | formalize control over golems | construction capacity, support equipment, trains | less revolt risk, high supply burden |
| Dismantle golem bodies | golem | convert golems into inert material | stability, time, risk of local clashes | no equipment farm, lowers leakage |
| Close the chaos ledger | all | ban further chaos musters | political and army costs, cooldown | lowers future weights, blocks dangerous power |
| Demand another impossible unit | all | high-risk on-demand spawn | escalating cost, chaos leakage, officer appetite | strong unit, splinter seed, absurd template |

## Lesser splinter countries

Chaos splinters are not the parent event countries. They use separate identities, flags, ideas, AI, and weaker mechanics.

| Splinter profile | Public identity direction | Starting forces | Special mechanic direction | Aggression |
| --- | --- | --- | --- | --- |
| Ragged horde | A zombie-linked lesser horde with a local name | base zombie units only and human fragments if relevant | fragmented hunger, weak cohesion, manpower hunger | attacks nearby population centers but can fracture |
| Grey host | A ghost-linked lesser host | weak ghost divisions and hollow militia | slow population drain, slow wasteland pressure, no instant erasure | aggressive when leakage high, otherwise creeping |
| Stone host | A golem-linked lesser host | slow strong golem divisions, few human handlers | heavy defense, bad speed, quarry or stone pressure | defensive first, expansion if depots secured |
| Mixed impossible army | Future or mixed chaos registry | profile-defined units | profile-defined lesser mechanic | registry-defined |
| Human-chaos mutiny | possessed general plus chaos units | human mutineers plus one chaos family | officer appetite and leakage combined | attacks parent first |

Every splinter country should be weaker than its parent event equivalent. The danger comes from surprise, local collapse, and stacking with other wars, not from copying a world-end actor.

## Ragged horde profile

The ragged horde can form when a country trains or receives too many base zombie units and fails containment. It should not use advanced zombie types. It should not count as the main Zombie Outbreak horde. It can add a lesser world-threat source if it grows large enough, but it must use a separate source flag and docs.

Starting package:

- units come from local zombie-trained units, failed quarantine sites, and a small scaled horde package
- territory is selected from states with zombie training, chaos leakage, or failed containment
- starting idea direction: fragmented hunger and broken nerves
- reinforcement route uses captured population, local failures, and focus decisions
- no cure research, no Anti-Zombie League takeover, no parent outbreak collapse logic
- AI attacks weak nearby states, but fragmentation can reduce its ability to hold far territory

## Grey host profile

The grey host can form from ghost divisions that remain near populated areas, repeated ghost perimeter failures, or accepting a general's ghost authorization demand.

Starting package:

- weak ghost divisions with low organization at first
- slow state harm that kills population gradually and damages buildings over time
- controlled states can become pale dead zones through long pressure, not instant removal
- no Black Ledger, no Death island route, no continent consumption logic
- recaptured harmed states need recovery decisions but remain salvageable
- AI tries to connect ghost-held states and attack isolated coasts or depots

The state harm must be much weaker than Death. It should scare the player without replacing Death's identity.

## Stone host profile

The stone host can form from golem units that are repeatedly bound, stationed, or used without control.

Starting package:

- small number of tough, slow golem divisions
- very low manpower needs, high supply or construction burden
- starting ideas around heavy bodies, cracked command, and inert economy
- reinforcement through quarries, captured factories, or strange construction decisions
- no parent golem event country if one exists later
- AI prefers defensive wars until it captures enough industry

The stone host should be hard to push in bad terrain but poor at fast conquest.

## Dynamic future-proofing rule

Whenever Chaos Redux adds a new unit family that is meant to interact with this event, the implementation should update only the chaos unit registry and its documentation. The event should read registry fields to know whether the unit can spawn, train, create a splinter, or remain excluded.

The registry must allow a unit to be marked:

- excluded from Infantry Spawn
- ordinary random only
- chaos spawn-only
- chaos trainable
- chaos spawn and trainable
- chaos breakaway eligible
- parent-event protected

If a unit is parent-event protected, Infantry Spawn may use only the lesser profile defined in the registry. It must not set parent event progress flags.

## Chaos splinter focus route overlay

The shared crisis focus tree from Evolution III should have route overlays for chaos profiles.

| Route overlay | Focus group direction | Decision unlocks | Late payoff |
| --- | --- | --- | --- |
| Ragged horde | gather fragments, follow scent, fracture or cohere | horde surge, consume depots, fragment management | either unstable spread or contained bargaining if human handlers exist |
| Grey host | listen to the silent ranks, mark thresholds, pace the living | slow wasteland pressure, recovery denial, ghost concentration | small dead-zone network that can be defeated state by state |
| Stone host | awaken quarries, bind bodies, march slowly | quarry labor, stone reinforcement, fortified advance | defensive stone state with limited expansion goals |
| Mixed impossible army | classify the impossible, pick a dominant logic | profile-specific decisions | registry-defined end state |

These routes should not use generic political depth. They need internal choices about method, cohesion, expansion, and containment.

## Parent country aftermath

When a chaos splinter forms, the parent should receive aftermath content.

- temporary shame or command scandal
- decisions to contain, negotiate, quarantine, or abandon infected states
- option to permanently ban chaos unit access
- option to create a special containment command with heavy costs
- possible foreign opinion damage if splinter causes deaths
- recovery decisions for slow ghost wastelands or golem-ruined infrastructure
- achievement tracking for containment without using parent event mechanics

## AI for chaos units

AI countries should be conservative with chaos units. At peace they should quarantine, dismantle, or close the chaos ledger. At war they may use chaos units if losing badly, low on manpower, or already high chaos. AI should almost never authorize base zombie training unless desperate, high chaos, and facing major threat.

Chaos splinter AI should be aggressive locally. It should not try remote naval campaigns unless it has ports and a profile that supports naval behavior. It should prioritize parent states, nearby weak states, depots, capitals, and states tied to its profile.

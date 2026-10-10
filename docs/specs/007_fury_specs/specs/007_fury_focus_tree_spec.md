# 007 Fury shared focus tree specification

## Tree role

Fury uses a shared focus tree loaded onto the selected AI Fury country.
The tree is a behavioral tree for a dynamic actor, not a national history tree.
It must feel useful for Luxembourg, Uruguay, or any other eligible small AI country without relying on their exact history.

Tree id: `fury_focus_tree` in `common/national_focus/007_fury_focus_tree.txt`.
Player text lives in `localisation/english/007_random_expansion_l_english.yml`.

The tree is compact enough for a repeatable minor event, but deep enough that a Fury actor that survives for years has meaningful branches.

## Tree loading rules

- Load the shared Fury tree on every Fury actor, including countries with a bespoke tree, because Fury is a takeover behavior; this replacement is intentional.
- Never load the Fury tree for a player country.
- If a player later takes control of a Fury country through tag switching, the tree can remain, but ordinary random play must not grant it to the player.

## Implemented route map

The tree has 52 focuses with stable IDs.
The [route map](../focus_graphs/007_fury_focus_tree_route_map.mmd) mirrors the source prerequisites.
Player-facing names below are the current localisation; where the stable ID reads differently, the ID is kept for save compatibility and the accepted release corrections govern the promise.

| Branch | Unlock | Focuses in order |
| --- | --- | --- |
| Opening trunk | always | `Open the War Office`, `The War Office in Motion`, then `Count the Rifles` and `Capital Guard`, `Choose the First Target`, `First War Office Orders` |
| Army of the March | trunk | `Field Columns`, `Depot Cadres` and `Storm Columns`, `Forward Depots`, `Logistics Under Movement` and `Officer Tables` |
| Expansion | trunk | `One Border at a Time`, `Weak Neighbor Doctrine`, `Frontier War Plans` and `Motorised Supply Columns`, `The Next Neighbor` |
| Occupation and integration | trunk | `Occupation Administration`, `Survey Occupied States` and `Occupation Offices`, `Rail and Occupation Supply`, `Garrison Occupied Towns` and `Conquest Coring`, then the mutually exclusive `Core by Administration` or `Core by March` |
| Cooperation | Evolution II or Pact challenge; excludes rivalry | `Second War Table`, `The Other Fire Answers`, `Shared War Tables` and `Joint Campaign Plans`, `Joint Cadre Transfers`, `Fury Pact Command` |
| Rivalry | Evolution II or Hostile challenge; excludes cooperation | `Rival Column`, `No Second Fury`, `Claim the Same Victim` and `Absorb the Rival Fire`, `Last Fury Standing` |
| Evolution I | Hardened Fury unlocked | `Hardened Doctrine`, `Harden the Columns`, `Depot Officers Without Leave` and `Forced March Tables`, `Occupation as Recruitment` |
| Evolution III | All Borders at Once unlocked | `All Borders`, `Three War Offices`, `Storms on All Fronts` and `No Target Is First`, `All Roads Are Front Roads` |
| World-end | no valid neighbours, after the expansion route plus coring, or after `Last Fury Standing` | `Beyond the Old Frontier`, `Carry the Orders Overseas` and `Continental Ignitions`, `Main Fury Pact`, `World in Fury`, `No Neutral Ground` |

## Branch roles

### Opening trunk

The trunk establishes the Fury identity and the first war.
It adds `National Fury`, opens the War Office category, grants a stockpile and a one-time reinforcement wave, and runs the first target selection.
It avoids generic stability and political power rewards and grants concrete systems, units, stockpiles, target handling, and decisions.

### Army of the March

This branch improves Fury's army without making the weekly reinforcement loop infinite.
Rewards use army experience, stockpiles, trucks, trains, command power, and one-time waves.
`Depot Cadres` unlocks the paid wartime depot deployment and adds finite reserves through the lifetime cap.
No focus may create an uncapped weekly division loop, and every scripted reserve grant respects the 100-division per-actor cap.
Each unit focus names the institution that creates the wave; avoid repeating `add two infantry divisions` across focuses.

### Expansion

The sequential path focuses on one target at a time.
It improves target preparation, adds momentum, and `The Next Neighbor` immediately selects and declares on the next legal target.
`Frontier War Plans` and `Motorised Supply Columns` provide command power, momentum, trucks, and preparation; they do not promise capital selection, rail sabotage, or partition.

### Occupation and integration

This branch controls compliance and coring.
It adds the Compliance Drive idea, registers occupied states, relieves overextension, and unlocks the register, rail registry, garrison mission, and the two coring decisions.
Fury never gets instant cores on conquest; coring requires decisions, compliance, control, and concrete costs.
`Core by Administration` is slower, compliance-heavy, and relieves more strain.
`Core by March` is faster and harsher, adds momentum and overextension, and accepts lower compliance.

### Cooperation and rivalry

The two Evolution II branches are mutually exclusive, and the paid route decisions lock the opposite branch.
Cooperation uses project-pact membership, the `Fury Pact Command` idea, and physical reserve sharing.
Rivalry allows Fury-on-Fury targeting after ordinary legal neighbours are exhausted, adds the shared-rival target score, and gives the last surviving rival a path to terminal preparation.
Neither branch uses a cohesion counter or partitions conquered land.

### Evolution I and III

`Hardened Doctrine` applies Hardened Fury, and its branch adds artillery, command power, finite reserves, manpower, and momentum with matching overextension costs.
`All Borders` and `No Target Is First` declare on every valid neighbour, while the branch adds supply equipment and a capped wave and raises overextension sharply.

### World-end

The world-end branch is not reachable from a short first war.
`Beyond the Old Frontier` requires that no valid neighbour remains and either the expansion route plus a coring route or the last-rival path.
`World in Fury` names the actor as world-end candidate and calls `fury_try_start_world_end`, which still checks the terminal eligibility rules in Part 2.

## Unresolved Internal Fury branch

The original design specified an Internal Fury branch with three political paths: a War Directorate that replaces the leader with a fictional institutional council, Civil Mobilization that trades stability for recruitment, and Compliance Administration that trades early pace for consolidation.
The 52-focus implementation omits it, and no user or parent decision accepts its removal.
Its disposition is `unresolved` and is tracked in the README's open questions, together with the audit's proposed resolution.
The institutional portrait for the War Directorate is needed only if that route is accepted.

## Focus filters

| Filter | Focus families |
| --- | --- |
| Fury Command | opening trunk |
| Fury Army | Army of the March, finite reserve support |
| Fury Expansion | target selection, war declarations, world-end entry |
| Fury Occupation | compliance, integration, coring, garrisons |
| Fury Pact | cooperation branch |
| Fury Rivalry | rivalry branch |
| Fury Evolution | Evolution I and III content |
| Fury World-End | terminal branch |

The current source maps these families onto vanilla `FOCUS_FILTER_*` tags.

## Idea lifecycle

| Idea | Source | Role | Ends |
| --- | --- | --- | --- |
| `fury_national_fury` | package and opening focus | makes a tiny country dangerous | replaced by Hardened Fury or removed at cleanup |
| `fury_hardened_fury` | Evolution I | stronger force and a five-point recruitable population bonus | cleanup |
| `fury_overextension` | high occupation pressure | shows strain | removed when pressure falls |
| `fury_compliance_drive` | occupation branch or settlement decision | absorbs captured states | cleanup |
| `fury_pact_command` | cooperation route or Main Fury Pact | shared coordination | cleanup |
| `fury_rival_doctrine` | rivalry route | anti-Fury competition | replaced at Main Fury Pact or cleanup |
| `fury_world_in_fury` | world-end start or seed | terminal identity | cleanup after defeat |

The earlier `Improvised Command` starting idea was not adopted.

## AI focus behavior

Baseline Fury AI prioritizes:

1. opening trunk.
2. first war support.
3. Army of the March if it lacks divisions and still has reserve potential or capped refill focuses available.
4. Expansion branch if it is winning.
5. Occupation branch if overextension is high.
6. Cooperation branch if another Fury exists and the type is pact.
7. Rivalry branch if the type is hostile.
8. world-end branch only when eligible.

AI avoids:

- world-end branch before eligibility.
- all-neighbor focuses before Evolution III.
- pact focuses in hostile type and rivalry focuses after a cooperation commitment.
- coring focuses when it controls no occupied territory.
- unit-spawn focuses when manpower and equipment are exhausted.

Numeric focus weights remain unverified by a completed probability inspection; see the probability audit in `docs/plans/007_fury_plans/`.

## Localisation tone

Focus text is bureaucratic, cold, and direct, not ordinary nationalist expansion.
Good subjects are offices, registers, depots, maps, border counts, marching orders, census work, corridors, staff tables, and administrative seizure.
Avoid generic lines about destiny, glory, ancient borders, or ideology; Fury is a dynamic behavior, so the shared tree stays broadly applicable.

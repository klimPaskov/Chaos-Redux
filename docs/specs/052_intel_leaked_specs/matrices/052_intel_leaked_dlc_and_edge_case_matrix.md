# DLC Compatibility and Edge Case Matrix

## DLC compatibility

| Surface | Full intelligence and agency mechanics available | Base-game-compatible path | Required equivalence |
| --- | --- | --- | --- |
| Broad leak | Civilian, army, navy, air intelligence plus agency-related depth | Reversible civilian, army, navy, air intelligence and target modifiers | Every foreign ordinary government receives meaningful temporary knowledge |
| Personnel exposure | Operatives, networks, operations, cryptology, liaison | Generic security personnel, military attaché, diplomatic and command procedures | Personnel at Risk remains a real mission with a severe bounded failure |
| Recall action | Recall exposed operatives, close networks, cancel operations | Withdraw security contacts, change procedures, accept generic intelligence penalty | The action protects personnel and costs useful access |
| Network reconstruction | Rebuild target-owned networks | Restore generic foreign security reach or omit the network-specific action | The incident remains complete without an empty substitute button |
| Foreign exploitation | Agency quality shapes extraction and operations | Military, industrial, diplomatic, and political use | Hostility, capability, and domains still drive named exploiters |
| Poison the Leak | False contact chains, operation traps, service feedback | False plans, codes, deployments, diplomacy, and industrial assumptions | Deception remains available and recipient Reliance still matters |
| Trace the Source | Cryptology, networks, operative evidence | Staff records, diplomatic traffic, courier routes, archives | Practical route classes remain available |
| Achievements | Operative proof when present | Equivalent generic personnel proof | Achievements never require unavailable DLC surfaces |

## Target edge cases

| Edge case | Required behavior |
| --- | --- |
| Source player country is invalid | Use the valid major route when available, otherwise Event 52 is unavailable |
| No valid major exists | Use the valid source player route when available |
| Neither route has a valid target | Show `N/A` through normal event availability and do not queue the event |
| Selected target becomes invalid before opening report | Abort incomplete target initialization and rerun only if the same event chain safely retains selection authority |
| Selected target is annexed during incident | Close that target state, remove its temporary exposure, preserve committed real consequences, and continue other Total Compromise targets |
| Target changes ideology or faction | Incident continues, recipient behavior updates from current relations |
| Target becomes a special Chaos actor or actual nonhuman | Remove ordinary Event 52 state through bounded owner cleanup |
| Target has no agency | Use complete base-game path |
| Target has no navy | Naval domain can remain low-level only when archive logic supports it, named naval actions require a real foreign use |
| Target has no air force | Air-domain named exploitation should normally drop out or remain limited to basing plans that still exist |
| Target at civil war | Treat valid countries separately, do not duplicate the same archive across parent and rebel without an explicit Total Compromise selection |
| Target switches player control | Incident ownership follows the country state, UI becomes available to the current human controller through established multiplayer rules |

## Recipient edge cases

| Edge case | Required behavior |
| --- | --- |
| Recipient becomes target's ally | Aggressive future exploitation falls, cooperative behavior can replace it |
| Recipient enters war against target | It can enter a free named-exploiter slot when relevant Exposure remains |
| Recipient is annexed | Remove pair Reliance and pending outcomes safely |
| Recipient has no relevant capability | It retains broad knowledge but should not receive an unsupported named action |
| Recipient already has maximum ordinary intelligence | Event 52 still creates event-owned exploitation behavior, but temporary intel must not overflow or become permanent |
| Recipient is a subject | Behavior reflects overlord, autonomy, relations, and current war, without assuming automatic hostility or obedience |
| Several recipients share a faction | Curated sharing can occur through one bounded outcome, not duplicate the same report for every member |
| Same recipient exploits several Total Compromise targets | Keep separate pair Reliance, cooldowns, and deception outcomes |

## Incident overlap and timing edge cases

| Edge case | Required behavior |
| --- | --- |
| Event 52 selected while a sequence is active | Event is unavailable through normal selection |
| Deep Files activates after Exposure reaches zero | No second tranche, future incidents use Deep Files |
| Deep Files activates at Fading Exposure | Normally no tranche, unless a rare profile proves current sensitive material |
| Total Compromise activates after current sequence closes | Future incidents use Total Compromise |
| Total Compromise activates during active sequence with no additional targets | Existing target can remain on current profile, or receive a bounded severe upgrade only when the accepted branch explicitly selects it |
| Total Compromise multi-target branch cannot fill unique target count | Select a valid smaller branch or severe single before initialization, never partially create an invalid branch |
| Evolution disabled during active deep state | Existing committed consequences resolve, no new evolution-gated tranche or target is added |
| Event disabled during active incident | Existing incident resolves and cleans up, no new repeat firing begins |
| World-end state begins during incident | Follow shared world-end freeze and owner cleanup rules, preserving committed real losses and preventing stale UI |
| Save and reload at any phase | Exposure, domains, deadlines, missions, targets, and pair records restore exactly once |

## Decision edge cases

| Edge case | Required behavior |
| --- | --- |
| Player lacks one cost | Action remains visible only when useful and shows exact blocked cost through texticon and tooltip |
| Action's domain disappears | Decision hides and any reserved cost or target state clears |
| Recall would cancel several operations | Tooltip names or summarizes affected operations before action |
| False deployment loses required units or state | Mission enters failure or cancellation path, not silent success |
| Deception target becomes friendly | That target leaves aggressive outcome pool, remaining valid recipients continue |
| Poison route has no high-Reliance recipient | Action is unavailable and states why in concise terms |
| Trace Source finishes after incident reaches zero | Practical route result can still complete when its administrative work remains meaningful, then closes its own temporary state |
| Compartmentation already at cap | Action hides or gives no false promise of further future resilience |

## Cluster edge cases

| Edge case | Required behavior |
| --- | --- |
| Event 039 target is invalid for Event 052 | Event 052 selects independently under cluster rules or skips with a recorded reason |
| Same target qualifies for both | Use one bounded evidence or personnel interaction through public adapters |
| Event 052 sequence already active | Event 052 cluster member skips, Event 039 can still resolve |
| One member disabled | Enabled member can still fire according to cluster rules |
| Cluster actor disappears during setup | Fail closed for affected member without corrupting the cluster transaction |

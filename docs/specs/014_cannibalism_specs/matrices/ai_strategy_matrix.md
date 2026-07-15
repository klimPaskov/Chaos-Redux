# AI Strategy Matrix

## Actor profiles

| Actor | Preferred response | Avoid | Escalation trigger | Terminal priority |
| --- | --- | --- | --- | --- |
| Democratic host | Supply, witnesses, public evidence | Exploitation | Multiple countries or warlord state | Coalition and anchors |
| Authoritarian host | Quiet discipline, targeted purge | Public panic and weak-evidence purge | Officer conspiracy | Military suppression |
| Fascist host | Hard discipline, concealment | Humane cost when desperate | Imminent defeat can allow exploitation | Aggressive counterwar or dark route |
| Communist host | Ration campaign, political purge | Uncontrolled local captains | Prison and deportation node | Centralized suppression |
| Poor minor | Aid, evacuation, amnesty | Resource-heavy simultaneous missions | Island or prison threat | Defensive coalition |
| Major ally | Equipment, convoys, intelligence | Unnecessary direct occupation | Cross-border spread | Break network hubs |
| Rival power | Border screen, propaganda, opportunism | Routine cult support | Enemy collapse | Attack world threat if endangered |
| Island Host | Ports, raids, landings | Deep mainland war without transport | Blockade or high Larder | Submit or expand islands |
| Siege Commune | Fortify, attack relief | Open-field pursuit | Relief assault | Break siege and align |
| March Host | Depots, weak fronts, movement | Long static siege | High Frenzy | Seek host status |
| Hannibal | Absorb, centralize, infiltrate | Wastelands and unusable territory | Coalition formation | Ordinary world end |
| Wendigo Hannibal pre-lock | Protect anchors, preserve Larder reserve, recruit, consume, hunt scored enemies | Sacrificing anchors or countdown reserve | Countdown active | Reach terminal lock |
| Wendigo Hannibal post-lock | Separate scored terminal priority and complete conquest | Peace, normalization, unusable targets | Pulse-owned terminal state | Consume remaining population centers |

## Shared target-scoring contract

- Country scorers: `cannibalism_unified_target_scorer` and `cannibalism_wendigo_target_scorer`.
- Targeted-decision MTTH entries: `cannibalism_unified_target_decision_weight` and `cannibalism_wendigo_target_decision_weight`.
- Six unified consumers: seed a major enemy army, prepare a global campaign, issue a terror ultimatum, provoke a border incident, destroy a coalition hub, and collapse an enemy front.
- Hard-invalid targets are excluded. This includes self, allies and subjects, dead or capitulated countries, Event 014 cannibal countries, actual nonhumans, unusable population, locked targets, and targets without a proved war, adjacency, cell, rail, naval, or post-lock route.
- Independent positive factors include usable population, cells, prisons, ports, weak supply, low stability, adjacency, physical corridors, coalition command, current war, and cold-front evidence for the pre-lock Wendigo profile.
- The overextension penalty applies before mature distant logistics and is not a permanent target ban.

## Resolved first-band behavior

The pre-lock scored AI package intentionally uses fixed first assignment. Each valid target receives one score-banded strategy package, and later calls can add newly valid targets. The engine exposes `add_ai_strategy` but no matching scripted removal effect, so an already recorded pre-lock target is not dynamically removed or re-banded when its score changes. Post-lock targeting is a separate one-time terminal escalation package applied after the transformation pulse locks the route. This is the implemented design contract, not an open audit finding, and it is not represented as live dynamic re-scoring.

Pack training, receipt muster, inherited-cell activation, terminal-hunt launch, and terminal-hunt pressure AI also require the action cost plus the existing countdown Larder reserve. Duplicate Pack-contract and pre-lock target-priority writes are guarded.

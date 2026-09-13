# Event 045: Third Balkan War

## Catalog identity

- Event ID: `45`
- Event name: Third Balkan War
- Event type: Minor Fire-Once
- Chaos level: `1`, Calm World
- Cluster: Wars
- Member severity: High
- Entry event: `chaosx.nr45.1`
- Accepted status after planning: Ready for implementation

## Event promise

The event turns the Balkans into the origin of a war that begins as a genuine regional struggle and can expand through decisions made by regional governments, outside patrons, guarantors, and factions. The opening conflict must already involve several countries. The player should never wait through a diplomatic prelude to discover whether the event will produce a war.

The central play question is whether governments treat the conflict as a bounded Balkan settlement or as an opportunity to settle every nearby rivalry. A regional belligerent chooses which claim is worth extending the war for. A neutral Balkan state decides whether its own frontier is now at stake. An outside power decides whether containment is worth more than weakening a rival. Each of those choices changes the same public measure, **Balkan War Escalation**.

The event can end with a contained regional victory, a negotiated settlement, an imposed armistice, a wider European war, or a global war that ordinary systems continue. It must never force the world-war outcome merely because the event has remained active for a long time.

## Player experience

A regional player receives an immediate wartime situation with clear objectives, a visible escalation stage, and a small set of actions that fit its current role. The player can press a registered claim, secure a military corridor, request foreign support, seek an armistice, or contest an ally's occupation. The player is not asked to manage a separate claim score, foreign influence score, camp cohesion score, and settlement score. Those calculations remain internal.

An outside player receives a role-aware intervention category only when it has a real route into the crisis. It can coordinate containment, arm one side, recognize a claim, issue a guarantee, invite a country into a faction, or prepare direct intervention. These are consequential commitments. They consume equipment, fuel, convoys, political capacity, diplomatic access, or military readiness according to the action.

The event should become easier to read as it grows. More countries and more hidden relationships may exist, but the decision category still presents only the current stage, the latest material cause of escalation, the next threshold, and the actions relevant to the current country.

## Public mechanic

The event has one persistent public value:

### Balkan War Escalation

- Range: `0` to `100`
- Public presentation: a labelled meter with five named stages
- Main cause: concrete expansion of the linked conflict
- Main response: containment actions, withdrawal of commitments, armistice compliance, or settlement
- No passive upward drift
- Hidden inputs are summarized in a concise tooltip instead of exposed as separate values

The five public stages are:

| Range | Stage | Campaign meaning |
| --- | --- | --- |
| `0-24` | Balkan Conflict | The opening regional camps are fighting and outside powers remain observers or limited suppliers. |
| `25-44` | The Balkans Are on Fire | More regional countries have joined, active claims have multiplied, or the original conflict has opened additional Balkan fronts. |
| `45-64` | European Crisis | Opposing camps have meaningful outside backing through arms, volunteers, guarantees, sanctions, deployments, or faction pressure. |
| `65-84` | The Powder Keg Explodes | Major powers or major-led factions are directly fighting on opposing sides. |
| `85-100` | Another World War | The linked conflict now qualifies as a wider global war and Event 045 hands control to normal war, faction, and peace systems. |

A numerical threshold is necessary but never sufficient for the final two stages. Each stage also requires the matching world-state proof. The meter caps below the next threshold until that proof exists. This prevents a large pile of aid shipments from being displayed as direct major-power war.

## Hidden simulation

The event may track many internal facts without making them player counters:

- event generation and active lifecycle
- opening cause and dispute family
- initiator and opening camp leaders
- opening participants and later entrants
- linked war identifiers
- country role and camp membership
- registered regional interests
- activated claims
- sponsor, recipient, support type, and support tier
- guarantees and faction commitments
- maximum escalation reached
- stage proof flags
- armistice offers and compliance
- settlement participation
- allied occupation disputes
- fragmentation candidates
- former allies with incompatible claims
- postwar memories

These facts should use bounded registered arrays, event targets, flags, and owner-scoped ledgers. The event must not add a broad daily whole-world scan.

## Lifecycle overview

1. Validate that the event can honestly create a multi-country Balkan war.
2. Build the current regional country pool from geography, country type, survival, and diplomatic state.
3. Select a valid dispute and an initiator.
4. Build two hostile camps, or a justified three-sided conflict graph.
5. Start the linked wars immediately.
6. Record opening participants, claims, sponsors, and escalation.
7. Show the outbreak super-event and role-aware decisions.
8. React to new entrants, support, guarantees, faction calls, direct intervention, armistices, occupation, and settlement.
9. Activate Evolutions through their own requirements and pacing.
10. Resolve through regional settlement, imposed ceasefire, wider-war continuation, or world-war handoff.
11. Clear temporary state and retain only defined postwar memories.

## Global-war honesty gate

The event should normally be unavailable for automatic selection when the world is already in a multi-faction global war whose active participants cover most valid Balkan candidates. In that state the event cannot honestly claim to have started another world war.

A large existing war does not automatically block Event 045 when the Balkan countries remain outside it and the event can create a distinct regional conflict. The `third_balkan_war_origin_crisis` memory is set only when Event 045 creates the first qualifying wider-war linkage. Force Trigger Mode may bypass normal selection for testing, but the causal origin flag still requires proof.

## Presentation direction

The opening uses restrained dark humour about the recurrence of Balkan crises and Europe's repeated belief that this time the fire will remain local. The fighting, civilian harm, and military losses are treated seriously. Each later stage removes more humour. The world-war handoff should be direct and grave.

The emotional focus should remain on mobilizing troops, crowded railways, frontier posts, contested ports, broken armistice lines, and foreign columns arriving in the region. Maps can appear as secondary objects but should not be the main visual subject.

Final player-facing wording belongs to implementation and super-event research. The spec supplies tone and factual direction, not pasteable localisation.

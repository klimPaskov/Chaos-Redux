# Event 062 core design

## Catalog entry

- Event ID: `62`
- Event name: Allies Backstab
- Type: Minor Repeatable
- Status before implementation: To Be Reworked
- Chaos level: `1`
- Cluster: Wars
- Cluster role: High member

## Premise

Alliances across the world identify members that appear expendable, remove them from the bloc, and attack them. Several factions are affected by one event firing. A faction can lose one member, several weak members, or at higher Evolutions split into opposing camps.

The event is forced once a faction is selected. The faction leader does not receive a harmless refusal option that cancels the incident. Player agency begins with the way the purge is prosecuted, resisted, widened, negotiated, or settled.

## Player experience

An uninvolved player receives one aggregated international report built around the largest fracture in the generation. The report states how many factions were affected and names only the most important examples that can fit cleanly. It does not produce one world popup for every faction.

A player inside an affected faction receives one role-specific event:

- the faction leader learns which governments have been removed and chooses the public war intent
- an expelled government sees the expulsion, the immediate military danger, and any co-victims
- a member retained by the faction decides how strongly to support the purge
- at Evolution II or III, a dissatisfied member can join the expelled bloc or withdraw from the crisis when legal
- a selected outside sponsor receives a bounded intervention or mediation opportunity

The expulsion is already real when the role event appears. The war declaration follows after a short hidden transaction step that rechecks all legal and war-side conditions. This gap exists to prevent broken diplomacy, not to turn the purge into an avoidable ultimatum.

## Global firing rule

One Event 62 firing must affect at least two distinct valid factions. When fewer than two valid factions exist, the event has no valid target and is unavailable to normal selection. A manual force route may expose the same failure reason, but it must not invent invalid factions or apply a partial transaction.

Each selected faction receives a separate transaction receipt under the same global generation. A failure in one faction does not roll back completed safe transactions in another faction. A faction that becomes invalid before mutation is skipped and replaced from the unused valid-faction pool when possible.

## Affected faction count

The ordinary baseline uses a bounded faction budget.

| Valid factions at draw time | Baseline factions affected | Evolution I factions affected | Evolution III maximum |
| --- | --- | --- | --- |
| `0-1` | Event unavailable | Event unavailable | Event unavailable |
| `2` | `2` | `2` | `2` |
| `3-5` | `2` | `3` when possible | `3-4` |
| `6-9` | `2-3` | `3-4` | `4-5` |
| `10+` | `3` | `4` | `4-6` |

The exact roll inside a range is weighted by faction pressure and the global mutation budget. Evolution III may select six factions, but no more than three may undergo a full internal bloc war in one generation. Other selected factions use a baseline or Evolution I purge.

## Faction identity

The event treats the current faction leader as the stable transaction anchor. It takes a membership snapshot before any country leaves. The snapshot remains the source for generation history even when the faction later dissolves or changes leader.

A political unit is the selection unit used for faction size and side assignment:

- an independent faction member forms one political unit
- subjects inside the same faction travel with their overlord as one bundle unless a safe independence route is explicitly invoked
- a subject whose overlord is outside the faction is excluded until implementation proves a legal owner-specific route
- a country cannot appear in two political units

This prevents an overlord and its subjects from being selected separately and placed on contradictory sides.

## Faction eligibility

A faction is valid when all of these are true:

- it has a living faction leader
- it contains at least two valid political units
- at least one nonleader unit can be expelled and opposed legally
- it has no unresolved Event 62 transaction
- its Event 62 faction cooldown has ended
- it is outside the fresh-faction protection period
- its members can be snapshotted without duplicate or invalid country entries
- the event can identify a legal immediate war, a legal delayed war, or a proven shared-war separation path

A two-member faction is valid. Its sole nonleader member becomes the only baseline target. The event records the bilateral betrayal even if the original faction later becomes a one-country shell or dissolves through normal engine behavior.

A faction created recently by Secret Alliance, A Faction Comes Calling, an Event 62 victim compact, or another faction-forming system receives a default protection period before it can be selected. The baseline planning value is `180` days. An Event 62 successor faction receives `365` days because immediate repeated betrayal would create a deterministic loop.

## Ordinary-country boundary

The event is designed for ordinary faction politics. An actual nonhuman country and a system actor that cannot use normal diplomacy are excluded. A special but human country may participate only when its owner marks normal faction behavior as safe.

The event should use the shared country classifiers as inputs, then keep its detailed participant trigger in the Event 62 owner files. It must not expand the shared classifier with Event 62 lifecycle rules.

## Generation lifecycle

Every firing creates one global generation number and one faction transaction number per selected faction.

A generation moves through these states:

1. valid factions collected
2. factions selected without replacement
3. membership and war state snapshotted
4. victims selected
5. initial side roles assigned
6. expulsion applied
7. military and diplomatic relationships reconciled
8. delayed war launch revalidated
9. crisis decisions and missions opened
10. settlement, victory, collapse, or ordinary-war handoff recorded
11. temporary state cleaned
12. durable memory and achievement facts preserved

Every state transition is idempotent. Reloading or receiving the same delayed event twice cannot expel a country twice, create duplicate wars, repeat equipment grants, or add a second crisis category.

## Public mechanic value

The event exposes one custom value, working label `Crisis Cohesion`.

Each active side has its own value, but a country sees only the value for the side it currently serves. The concept and thresholds remain identical for loyalists, expelled governments, and a successor bloc.

| Value | Stage | Meaning |
| --- | --- | --- |
| `0-24` | Disintegrating | members seek exits, separate peace becomes likely, and joint actions weaken |
| `25-49` | Shaken | the side can act, but failures can trigger defections or isolation |
| `50-74` | Coordinated | joint missions, settlement leverage, and reliable support become available |
| `75-100` | Unified | the side can sustain major joint action and claim a durable political outcome |

The category header shows the exact value, the stage name, the next threshold, and the most important recent cause. It does not expose the hidden target, defection, or settlement formulas.

Initial cohesion is dynamic. Suggested central tuning anchors are:

- loyalist side base: `55`
- expelled side base: `40`
- at least two mutually friendly victims: `+10`
- credible common external threat: loyalist `+10`
- severe leader-member hostility: loyalist `-10`
- outside guarantee or active mediator: expelled side `+10`, once per source class
- no viable route between co-victims: expelled side `-10`

Important events move cohesion in visible steps. A capital loss, member defection, separate peace, failed mission, successful war council, outside guarantee, or accepted settlement should matter. Routine combat does not create constant small ticks.

## Hidden simulation values

The event may track as many internal values as needed, including:

- faction selection pressure
- member vulnerability
- core-member protection
- strategic utility
- war contribution
- defection interest
- neutral-withdrawal interest
- side viability
- war launch legality
- military balance
- settlement willingness
- outside sponsor interest
- escalation proof

These values remain hidden unless one becomes a direct player choice. They feed the single public cohesion value, event availability, role events, AI behavior, and settlement outcomes.

## Baseline invariants

The baseline must preserve these rules:

- at least two factions are affected per normal firing
- every selected faction has a pre-mutation snapshot
- the faction leader is never the initial baseline victim
- one or more weak members are expelled
- former allies attack when a legal conflict edge can be created
- several victims from one faction cooperate by default and do not automatically fight each other
- the event never places one country on both sides of the same war
- no subject fights its overlord unless an owner-approved independence transaction resolved the relationship first
- no event effect directly creates civilian deaths, migration, famine, or contamination
- the event does not grant Chaos for the draw or for Evolution activation
- active decisions disappear after the linked crisis ends
- durable betrayal and settlement memories remain available to later events

# Event 062 faction and victim selection

## Selection goals

The event should usually strike members that the faction can describe as weak, exhausted, isolated, or expendable. The outcome must remain uncertain enough that repeated firings do not always select the smallest tag.

Raw size is one input. Strategic value, war contribution, geography, supply, and political trust can protect a small country. Severe losses can make a previously important member vulnerable. A large member can become a target when it is militarily broken and politically isolated, but this should be uncommon.

## Faction selection pressure

Eligible factions receive a hidden pressure score. The score determines which factions enter the generation, not which members become victims.

Suggested factor families are:

| Factor family | Pressure direction |
| --- | --- |
| size and number of political units | larger factions receive more pressure, especially at high Evolution |
| capability disparity | a large gap between strongest and weakest members raises pressure |
| political divergence | ideology distance, poor relations, and hostile memories raise pressure |
| war strain | multiple fronts, high losses, capitulations, and broken supply raise pressure |
| faction instability | recent exits, leadership disputes, and failed calls raise pressure |
| shared external threat | a credible common enemy lowers pressure unless internal hostility is already severe |
| institutional depth | long membership, strong relations, and high mutual contribution lower pressure |
| recent Event 62 exposure | active and cooling factions are invalid, not merely reduced in weight |

Faction size must not dominate every draw. A medium faction under severe strain can outrank a larger stable alliance. Evolution III adds a strong large-faction preference only after the faction passes the full-fracture validity gate.

## Member vulnerability model

Every nonleader political unit receives a normalized score relative to the other members of its faction. Higher values mean greater vulnerability.

The implementation should centralize the weights. The planning allocation below is the intended starting model.

| Component | Share of baseline score | Interpretation |
| --- | --- | --- |
| military weakness | `25` | division count, average strength, organization readiness, and deployed military capacity |
| equipment and manpower weakness | `15` | usable stockpile, reinforcement condition, available manpower, and mobilization depth |
| industrial weakness | `15` | military factories, civilian support capacity, dockyards where relevant, and current usable output |
| territorial and supply weakness | `10` | controlled states, capital security, rail and port access, and supply continuity |
| current war strain | `15` | number of fronts, enemy proximity, surrender progress, and threatened capital or supply hubs |
| military losses | `8` | recent casualties and equipment losses relative to national capacity |
| low faction contribution | `7` | low war contribution, weak expeditionary support, and failure to cover useful fronts |
| political isolation | `5` | poor relations with the leader and core members, ideology distance, and betrayal memories |

The values are ranks or normalized ratios inside the current faction. A twenty-division country in a faction of small states can be strong. The same country inside a major-power alliance can be weak.

## Core-member protection

A member receives core status when one or more of these facts are proven:

- it belongs to the strongest capability tier of the faction
- it supplies a large share of faction divisions, industry, air power, naval access, or war contribution
- it controls a capital, port, strait, rail corridor, or front that the faction currently depends on
- it has long membership, strong relations, and repeated support history
- the faction would lose a critical theater connection if it were expelled

Core status applies a major protection deduction to vulnerability. It does not create absolute immunity. A core member can still become a victim when military collapse, surrender progress, leader hostility, or strategic rivalry overwhelms the protection.

The faction leader is a separate case. It is excluded from baseline victim selection. Evolution II can leave the leader isolated in a rump faction when most members defect, which creates a leader-betrayed outcome without attempting to expel the legal faction leader through an unsafe effect.

## Strategic utility

A small country may be useful enough to avoid selection. Strategic utility includes:

- control of a front against the faction's current enemy
- a port or naval base needed for supply
- a rail or land bridge between other members
- an airfield network serving an active theater
- access to resources that the faction lacks
- a credible army positioned where no other member can replace it

Strategic utility is recalculated at the selection snapshot. Historical importance without current gameplay value does not provide permanent immunity.

## Protection and grace rules

A political unit is invalid as a victim when any of these apply:

- it contains the faction leader
- it was created, released, or transferred too recently to produce a safe package
- it has active Event 62 victim protection
- its removal would produce an unresolved subject-overlord conflict
- it is already in an Event 62 crisis
- it lacks any controlled state and has no viable government-in-exile route approved for this event
- it is an actual nonhuman or excluded system actor
- it cannot be separated from a shared war without placing countries on both sides

Planning defaults:

- ordinary faction-join grace: `180` days
- newly created Event 62 successor-faction grace: `365` days
- country victim protection after resolution: `1,095` days
- faction reuse cooldown after resolution: `720` days
- active-generation protection: permanent until cleanup

A human-controlled country receives the same hard protection after a prior Event 62 victimization. It has no permanent immunity. The event can target a weak player country after the protection expires.

## Candidate pool construction

Victim selection follows this order:

1. build the nonleader political-unit list
2. remove hard-invalid units
3. calculate normalized vulnerability and protection
4. sort by adjusted vulnerability
5. begin with units above the faction median vulnerability
6. expand downward only when the required victim count cannot be filled
7. draw without replacement from the eligible high-vulnerability group
8. revalidate each selected unit against the final bundle and loyalist-side viability rules

The draw remains weighted. The weakest unit should dominate when the gap is clear, but two similarly weak units should both be plausible.

## Victim count by faction size

The baseline uses the number of political units before expulsion.

| Political units | Baseline victims | Evolution I victims |
| --- | --- | --- |
| `2-5` | `1` | `1` |
| `6-9` | `1` | `1-2` |
| `10-14` | `1-2` | `2-3` |
| `15+` | `2-3` | `3-4` |

The count cannot exceed the valid candidate pool. A faction with three or more political units must retain the leader and at least one additional viable loyalist unit after a baseline or Evolution I purge. A two-member faction is the explicit exception.

At Evolution II, a full split follows side-viability rules instead of the victim-count table. At Evolution III, the world mutation budget can reduce a faction's planned victim count so one generation does not create an uncontrolled number of country mutations.

## Multi-victim grouping

Victims selected from the same faction belong to one expelled group for the generation. The group receives:

- mutual non-aggression for the active crisis
- temporary military access where legal
- permission to coordinate supply and war planning through event decisions
- a shared settlement position unless a member deliberately seeks separate peace
- a candidate group leader selected from capability, legitimacy, relations, and player status

The group is not forced into a permanent faction at once. It can operate as a temporary coalition. A durable successor faction becomes available only after survival, sufficient cohesion, and legal membership checks.

## Group leader selection

The expelled group leader is selected from independent victim political units. The score reads:

- military and industrial capacity
- capital security
- relations with other victims
- ideology compatibility
- diplomatic recognition and outside support
- player control
- absence of subject status
- ability to create or lead a faction under current engine rules

The strongest country does not win automatically. A somewhat weaker country with much better relations and legitimacy can lead. When a human player is a credible candidate, the player may accept or decline leadership. Declining does not remove the player from the group.

## High-contribution casualty protection

A country that suffered severe losses while making a high faction contribution should not be treated as weak solely because it was used heavily by the alliance. Losses increase vulnerability, while high contribution and strategic utility provide counterweight.

The probability audit must include a damaged high-contribution ally and a low-contribution isolated ally. The isolated ally should remain the preferred target unless the damaged ally is also collapsing politically and strategically.

## Player faction leader behavior

A human faction leader cannot choose no purge. The player receives a choice over conflict intent and the treatment of retained members. The target list is already selected by the global resolver.

The player can choose among valid directions such as:

- compel readmission or political compliance
- seize only registered cores and claims
- remove the victim government when severe ideological hostility supports it
- pursue complete destruction only under a narrow high-chaos and tiny-target gate

The final event options must show the visible war aim and likely diplomatic cost. Hidden follow-up branches remain hidden.

## Selection failure

A selected faction is skipped when its final snapshot no longer supports the transaction. Common reasons include:

- the only target was annexed or changed faction
- a subject relationship changed and cannot be reconciled
- a shared war makes legal hostility impossible
- the faction fell below two political units
- another event already dissolved the faction
- the selected countries entered a terminal or special state

The resolver attempts one replacement faction from the unused snapshot pool. It does not rescan the world repeatedly. When the final generation contains fewer than two completed faction transactions, the event records a failed firing only if the shared event system already committed the draw. Normal selection should prevent that state through the valid-target gate.

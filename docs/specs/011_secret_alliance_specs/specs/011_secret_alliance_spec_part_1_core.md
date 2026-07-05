# Event 011 Secret Alliance Spec, Part 1 Core Concept and Hidden Pact Model

Event ID: `011`
Working label, not final localisation: Secret Alliance
Type: Minor Fire-Once
Primary target: the current player country that receives the firing
Core fantasy: the player becomes the object of a private anti-player compact before the threat is clearly visible.

## Playable promise

Secret Alliance should feel like a diplomatic trap that has been built around the player before the player can name it. The early game feel is not a loud crisis. It is missing shipments, unfriendly newspapers, embassy habits changing, odd military visits, unexplained arrests of friendly agents, and small countries making choices that look unrelated until the pattern becomes too clean.

The player should eventually learn that several countries have privately agreed to act together against them. The player can ignore the pattern, overreact to the wrong country, quietly build a counter-network, expose the pact, split weak members away, or prepare for a war that will become larger than the first border incident.

The hidden threat is not a new country. It is a hostile coordination layer over existing countries. The event must therefore work through event targets, arrays, country flags, targeted decisions, temporary ideas, AI strategies, event log state, and a reveal super-event rather than through a custom tag.

## Design pillars

1. The pact begins hidden, but not invisible forever.
2. Three eligible countries found the compact at baseline.
3. Members are not at war with the target when chosen.
4. Countries outside factions are preferred, but faction membership can be allowed with heavy penalties when later evolutions need a major patron.
5. The pact can invite more members.
6. A member entering war with the target reveals the compact immediately.
7. War reveal forms the Anti-[target country] Pact and pulls every live member into the war.
8. Investigation can reveal parts of the pact before war and can weaken later war pressure.
9. Evolution II gives the player a decision category and active tools.
10. Evolution III makes the pact publicly legible and gives the player a direct war option.

## Target and founder selection

The event is a player-targeted event. The target should be saved as the permanent event target and as a stable variable-backed identity for scripted localisation. This avoids confusion if the player later changes tags.

### Hard founder exclusions

A country cannot be selected as a founder if any of these are true:

- it is the target country
- it is currently at war with the target
- it is in the same faction as the target
- it is a subject of the target
- it is a subject that cannot conduct diplomacy
- it is capitulated or cannot act
- it is an event-created nonhuman or special chaos country that should not participate in normal diplomacy
- it is marked as a world threat actor
- it is already a secret pact member through this event
- it is currently locked by another event that forbids normal diplomatic behavior

If fewer than three valid founders exist, Event 011 is unavailable and the event list should show `N/A` rather than selecting dummy founders.

### Founder preference factors

The founding pool should be weighted, not pure uniform randomness. The final implementation may tune exact values, but the ranking should follow this order:

1. Independent minors outside factions.
2. Minors with negative opinion of the target.
3. Minors that border the target or border a target subject.
4. Minors with claims, cores, or recent conflict memory involving the target.
5. Minors that fear target expansion, high world tension, target faction pressure, or target ideology spread.
6. Minors on the same continent or in the same strategic region as the target.
7. Countries that recently lost trade, access, territory, guarantees, or influence because of the target.
8. Countries with incompatible ideology, but ideology should never override stronger strategic reasons.

A country in another faction should receive a strong selection penalty at baseline. It may still become a later hidden supporter if the evolution logic needs it and no cleaner candidate exists.

### Founder roles

Each founding country receives one role. Roles are working labels, not final localisation.

| Role | What the role does | Gameplay identity |
| --- | --- | --- |
| Convener | Hosts meetings, maintains hidden protocols, proposes new members | raises pact cohesion and secrecy |
| Financier | Funds exiles, sabotage networks, press organs, covert shipments | increases operation tempo and reduces member costs |
| Provocateur | Pushes border incidents, hostile speeches, false-flag action, and pressure missions | increases war readiness and confrontation chance |

The roles should be distinct enough that a pact founded by three landlocked minors feels different from one founded by a maritime minor, a rich neutral, and a border rival.

## Core values

The hidden pact should use a small set of readable values. Exact storage belongs to implementation, but the spec requires these concepts.

| Value | Scope | Starts visible | Meaning | What raises it | What lowers it |
| --- | --- | --- | --- | --- | --- |
| Pact secrecy | global to event | hidden | how hard the pact is to expose | low chaos, no failed operations, strong Convener, target lacks agency | investigations, failed sabotage, leaks, high pact size |
| Pact cohesion | global to event | hidden until suspect stage | willingness of members to stay coordinated | successful operations, shared ideology, fear of target, major patron | exposure, bribes, conflicting promises, member defeats |
| Pact readiness | global to event | hidden at first, shown later | how close the pact is to open confrontation | border incidents, major patron, target weakness, high chaos | counter-preparation, disrupted shipments, exposed plans |
| Player suspicion | target country | vague early, visible at Evolution II | how clear the pattern is to the target | repeated operations, intelligence spending, neighboring incidents | pact quieting down, failed investigations, public distraction |
| Evidence | target country | visible at Evolution II | how much proof the player can use | investigations, captured couriers, exposed financing, border mission success | rushed public claims, forged evidence exposure, member coverups |
| Counter-readiness | target country | visible at Evolution II | how prepared the target is for a reveal war | border missions, security sweeps, industry protection, ally briefings | repeated sabotage, political panic, bad decisions |
| Member confidence | per pact member | hidden or suspected | how willing a member is to escalate | target weakness, pact success, major backing | isolation, investigation, economic pressure, military defeats |

Values should use dynamic factors. A strong target, high stability, good intelligence capability, and allied diplomatic access should make counter-work stronger. A large pact, a nearby major patron, high chaos, low target stability, and existing target wars should make the pact bolder.

## Baseline founding stage

Baseline founding is the normal opening when Event 011 fires in a calm or low-chaos world.

The event selects three founders and creates the hidden compact. The target player receives at most a vague diplomatic report that does not name the pact or members. If the implementation supports a fully hidden start cleanly, the opening can be logged in the system without a disruptive popup. The Event Details entry should describe public unease and odd diplomatic movement, not hidden member identities.

Baseline operations should be slow and subtle:

- small relation damage with countries already inclined against the target
- minor trade disruptions with no clear culprit
- small intelligence leaks
- foreign newspapers and radio organs echoing the same themes
- officials from separate countries meeting in neutral capitals
- low chance of a minor industrial disruption
- low chance of foreign support for anti-target parties or exiles
- quiet invitation attempts against more minors

Baseline should be noticeable after time, but not obvious in the first weeks. The player should see a pattern only if they pay attention to repeated small incidents.

## Hidden invitation rules

The pact can invite new members during every stage. Invitations are not free.

A candidate should be more likely to join when it has one or more of these motives:

- it borders the target
- it has a claim dispute with the target or a target subject
- it is ideologically hostile to the target
- it has low opinion of the target
- it fears target expansion
- it receives a promise from a founder or major patron
- it is outside a faction and wants protection
- it has weak industry and values secret military backing
- it was recently harmed by a Chaos Redux event and blames the target through propaganda

A candidate should be less likely to join when:

- it depends on target trade or target guarantees
- it is a target subject or ally
- it is in the target faction
- it is already fighting a large war
- it has high opinion of the target
- it is democratic and the target has high diplomatic credibility
- the pact has already suffered exposure or member defections

The pact should not invite every possible country at once. It should use a member cap that rises with evolutions, pact cohesion, major patron status, and target threat.

## Public visibility ladder

The event should not jump from hidden to full faction without intermediate states unless war causes the reveal.

| Visibility state | Player experience | Unlock behavior |
| --- | --- | --- |
| Background noise | subtle incidents, no named suspect list | baseline only |
| Suspected coordination | repeated patterns and a vague decision category notice | late Evolution I or early Evolution II |
| Dossier stage | suspected countries can be inspected and targeted | Evolution II |
| Public exposure | members known or partly known, faction label can appear | investigation success or Evolution III |
| War reveal | formal faction exists and all live members join the war | any member war with target |

The player should never be forced to wait for war to react once Evolution II is active. They should still need work to prove the pact and choose how far to escalate.

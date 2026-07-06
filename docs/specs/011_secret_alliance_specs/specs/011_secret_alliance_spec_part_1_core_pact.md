# Event 011 Secret Alliance Spec Part 1: Core Pact

## Design Pillar

Secret Alliance is a hidden anti-player compact, not an ordinary random faction event. Its tension comes from the player noticing a pattern before knowing the roster. The event should create a living roster of conspiring countries, make their actions gradually visible through reports and pressure, then reveal the compact as a public faction only when war, brinkmanship, or deliberate exposure forces the members into the open.

The player should feel three things:

- the world is beginning to coordinate against them
- scattered incidents are connected
- preparation and investigation matter before the war starts

## Opening Contract

The entry event remains `chaosx.nr11.1`.

When the event fires in the player target scope:

- save the player country as the event target
- select exactly three valid hidden founders
- choose one organizer from the founders unless an evolved opening permits a major organizer
- create hidden pact state without creating a visible faction
- start low-grade suspicious reports
- record Event 011 as active for logs, details, and evolution tracking

If three valid founders cannot be selected, the event should fail availability or delay cleanly before any visible player effect. Do not create dummy members, invalid substitutes, or a generic static fallback.

## Target Player

The player country is always the pact target. The pact is named and framed as anti-player, not as a neutral regional alliance that happens to fight the player later.

The target must be:

- alive and normal enough for diplomacy, war, decisions, and event logs
- not already in an Event 011 cleanup or reveal state
- not a special Chaos Redux country or terminal system state that would make normal diplomacy invalid

The implementation should support observer or AI-player tests, but normal play is built around the human player receiving reports and countermeasures.

## Founder Eligibility

Founder countries must be valid independent countries that can plausibly conspire against the player.

Hard rejects:

- the player target
- countries at war with the player
- countries in the player's faction
- subjects of the player
- non-existing countries
- capitulated countries
- governments in exile
- countries already marked as Event 011 members or invalidated
- special Chaos Redux countries or locked systems that should not take normal diplomacy

Initial founders should be factionless. If a later implementation wants countries already in factions, they should be represented as associates, contacts, or sympathizers until they become safe pact members. The first implementation should not force hidden members out of unrelated factions during reveal.

## Founder Weighting

Selection should be weighted, not uniform random.

Strong increases:

- not in any faction
- borders the player
- has claims, cores, lost land, or recent grievance against the player
- is in the same region or nearby sea region
- has hostile ideology or low opinion toward the player
- is threatened by the player's generated threat, expansion, or recent wars
- can plausibly coordinate with other candidates

Moderate increases:

- medium stability and enough agency to act
- rival or guarantee tension with the player
- location near a strategic route, canal, port, or frontier

Decreases:

- very remote with no plausible route
- weak and near collapse
- already in another major war
- diplomatically tied to the player
- in a major faction that would make reveal unsafe

The selection effect should build a candidate array, weight entries through repeated adds or equivalent helper logic, select founders, then immediately mark them to prevent duplicate selection.

## Pact Roles

Each member receives a role. Roles should influence AI, report flavour, sabotage target types, and counterplay.

| Role | Holder | Mechanical meaning |
| --- | --- | --- |
| Organizer | strongest founder or major sponsor | maintains cohesion, recruits members, leads revealed faction |
| Financier | industry-heavy minor or major | funds sabotage, front companies, and press work |
| Border arm | neighbor of the player | enables frontier pressure and border-war candidates |
| Intelligence node | stable or agency-flavoured country | increases courier, safehouse, and exposure race activity |
| Agitator | ideological rival | drives propaganda, party pressure, and diplomatic smears |
| Reluctant member | low-commitment minor | best target for negotiation, delay, and double-cross play |
| Major sponsor | Evolution II or III major | raises cohesion, sabotage intensity, and diplomatic shield |

Roles are not final localisation. They are script and design categories.

## Hidden Values

The pact should be governed by dynamic values rather than one hidden boolean.

| Value | Owner | Meaning | Player visibility |
| --- | --- | --- | --- |
| `secret_alliance_phase` | global or target | inactive, hidden, exposed, revealed, cleanup | summarized through events and category state |
| `secret_alliance_pact_cohesion` | global or organizer | how tightly members act together | hidden before reveal, visible after public bloc |
| `secret_alliance_exposure` | player | gathered proof and intelligence | visible after countermeasures unlock |
| `secret_alliance_threat_pressure` | player | intensity of pact action | visible as incident band |
| `secret_alliance_member_commitment` | member | willingness to stay, recruit, sabotage, and join war | hidden or hinted |
| `secret_alliance_provocation_heat` | player or member | closeness to public crisis or war | visible after Evolution II |
| `secret_alliance_player_readiness` | player | preparation against reveal war | visible after Evolution II |
| `secret_alliance_industrial_security` | player | resistance to sabotage | visible after Evolution II |
| `secret_alliance_negotiation_leverage` | player | ability to split or delay members | visible through decisions |

Binary state should use flags. Numeric state should use variables and constants.

## Baseline Hidden Behavior

Baseline is quiet and subtle.

Required behavior:

- no visible faction exists
- three hidden founders exist
- one founder is organizer
- members receive roles and commitment values
- the player receives suspicion state, not a full response menu
- reports appear sparingly and only when they move state, hint at a likely region, seed later targets, or explain pressure
- no automatic war starts

Subtle incident families:

- trade obstruction
- suspicious press campaigns
- embassy leaks
- border rumours
- foreign attaches appearing near the frontier
- courier routes through neutral ports or rail junctions
- minor industrial accidents with uncertain attribution
- unexplained arms movement near likely conflict regions

Reports must not reveal the full roster before exposure mechanics justify it. Early text should describe patterns, not answers.

## Reveal Rule

If any live pact member enters war with the player, the pact reveals.

Reveal must:

- confirm or reassign a valid organizer
- create a visible anti-player faction from a faction template
- add all valid live members to the revealed faction
- join all valid live members to the intended war against the player
- trigger the reveal super-event
- update Event Logs and Event Details
- convert hidden decisions, missions, flags, and reports into public or wartime state
- run cleanup for invalid members, selected targets, stale border states, and global event targets

If the player attacks a pact member, reveal still fires. If the player attacks a suspected non-member, the pact should gain propaganda or cohesion instead of revealing hidden members.

## Public Faction Name

The intended public faction direction is Anti-[player country] Pact.

Implementation must verify whether dynamic localisation in faction template names can display the target country cleanly in the faction UI. If it cannot, do not silently use a generic static fallback. Record the blocker and request design approval.

## Event Log And Details Direction

Event log and details entries should preserve the mystery until the reveal state.

Baseline details:

- describe patterns of isolated incidents and foreign meetings
- avoid naming all hidden members
- show a clear player target viewpoint

Evolution details:

- record widening cells, major sponsorship, public bloc movement, and reveal war
- mention the player's countermeasure choices where they materially change the pact
- record if a founding member split, delayed, or exposed the pact

After reveal:

- name the public pact and its leader
- describe war entry and the super-event
- preserve whether the player was prepared, surprised, or responsible for the forced reveal

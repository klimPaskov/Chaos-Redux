# Event 011 Secret Alliance AI strategy matrix

This matrix defines behavior by role, motive, stage, and world state. Values are qualitative design weights rather than final script numbers.

## Founder and member route logic

| Actor role | Ordinary preference | Strong positive factors | Strong blockers | High-chaos exception | Failure behavior |
| --- | --- | --- | --- | --- | --- |
| Fear founder | Defensive containment, guarantees, intelligence, access denial | Target expansion, nearby border, target army advantage, weak own faction protection | Strong target guarantee, excellent relations, secure existing faction | Can accept offensive preparation when target appears unstoppable | Seeks reassurance, neutrality, or withdrawal |
| Grievance founder | Sabotage, border pressure, punitive settlement | Claims, lost cores, humiliation, recent target annexation | Grievance already settled, no reachable theater, target weakness with no spoils | Accepts wider war if sponsor promises settlement | Demands terms, may defect after specific concession |
| Ideological founder | Propaganda, infiltration, regime pressure, uncompromising reveal | Opposed ideology, target support for domestic rivals, ideological major sponsor | Shared ideology, domestic instability, stronger ideological threat elsewhere | Can tolerate incompatible partners against a common target | Blames moderates and pushes radicalization |
| Patronage founder | Recruitment, logistics, access, sponsor-aligned planning | Sponsor aid, guarantee, military mission, economic dependence | Sponsor withdrawal, sponsor war collapse, better rival patron | May remain despite poor odds if dependence is extreme | Switches patron, leaks plans, or exits quickly |
| Opportunist founder | Late joining, spoils bargaining, low-risk pressure | Expected territorial gain, target weakness, sponsor victory prospects | High expected casualties, no spoils, target deterrence | Can join extreme coalition when victory looks easy | First to delay, seek separate terms, or defect |
| Major sponsor | Strategic direction, recruitment, military access, coalition leadership | Rivalry, target expansion, geographic reach, useful minor partners, available fronts | Losing existential war, no access, incompatible faction duty, severe domestic crisis | Can enter from desperation or global ideological conflict | Withdraws support, delegates leadership, or demands tighter control |
| Second major | Burden sharing or leadership contest | First sponsor weakness, independent rivalry with target, different theater access | Strong conflict with first sponsor, existing allied duty, no strategic reach | More likely in Totalen Chaos | Creates command dispute or parallel war aims |
| Minor recruit | Limited commitment tied to motive | Nearby threat, target aggression, sponsor guarantee, compatible grievance | Good target relations, target protection, no plausible reach, internal collapse | Higher willingness when coalition looks inevitable | Refuses, leaks, or accepts conditionally |

## Target AI response logic

AI-controlled targets can receive the event in non-player testing or scenario contexts. Their response must follow the same rules without needing a human-only GUI.

| Target condition | Investigation priority | Protection priority | Diplomacy priority | Escalation tolerance | Preferred reveal strategy |
| --- | --- | --- | --- | --- | --- |
| Strong intelligence agency, stable peace | High | Medium | High | Low | Build case and force weakened reveal |
| Weak intelligence, exposed industry | Medium | High | Medium | Low | Protect sites and seek ally consultation |
| At war on several fronts | Low to medium | High on critical routes | High | Very low unless confirmed border threat | Delay reveal while raising Preparedness |
| Strong army, weak diplomacy | Medium | Medium | Low | High | Preempt after confirming members |
| Democratic government | High when public evidence is credible | Medium | High | Low to medium | Public dossier and neutral inquiry |
| Fascist government | Medium | High | Low to medium | High | Coercive probes and preemptive pressure |
| Communist government | High through counter-subversion | Medium | Medium | Medium to high | Turn networks and expose sponsor |
| Non-aligned government | Balanced | Balanced | High when guarantees are useful | Medium | Private settlements and selective exposure |
| Low stability | Medium | High for leadership and industry | Medium | Low | Avoid public accusation until proof is strong |
| High Evidence, high Preparedness | High | Maintain | High | Medium | Force reveal on favorable terms |
| Low Evidence, high Preparedness | Medium | Maintain | Medium | Low | Continue defense and avoid reckless accusation |
| High Evidence, low Preparedness | High | Emergency | High | Low until preparations improve | Delay public reveal if possible |
| Evolution III countdown | Focus only on confirmed leads | Emergency maximum | Final split attempts | High | Preempt, deter, or force fracture |

## Operation selection

| Observed target weakness | Preferred operation | Secondary option | Avoid | Reason |
| --- | --- | --- | --- | --- |
| Poor counterintelligence | Penetration | Political network building | Noisy sabotage | Plans and access provide compounding value |
| Concentrated industry | Industrial sabotage | Technical-delegation penetration | Repeated minor propaganda | Tangible disruption with clear vulnerability |
| Fragile rail and supply | Transport sabotage | Forward-depot preparation | Political killing | Weak logistics shape the later war |
| Diplomatic isolation | Recruitment | Coordinated complaints | High-risk border action | Coalition can widen cheaply |
| Strong alliance network | Infiltration of partners | Propaganda against target reliability | Direct public pressure | Pact needs to weaken support before reveal |
| Long land border | Military surveys | Border agents and depots | Distant naval plans | Geographic access gives credible war preparation |
| Island or maritime target | Naval access talks | Port sabotage and convoy intelligence | Land-border events | Reach must be established first |
| High player Evidence | False traffic | Network cleanup and indirect recruitment | Repeating known methods | Pact should adapt to exposure |
| High player Preparedness | Diplomacy and recruitment | Political pressure | Another failed attack on hardened site | Indirect pressure has better expected value |
| Low pact cohesion | Low-risk intelligence | Mediation conference | Lethal operation | A failure could collapse the network |
| High pact readiness | Military preparation | Public pressure and recruitment | Basic nuisance incidents | The coalition is moving toward reveal |
| Sponsor under battlefield pressure | Minor-led operations | Local grievance action | Sponsor-dependent high-cost plan | Preserve network while sponsor is distracted |

## Recruitment AI

| Candidate state | Accept tendency | Conditional demands | Leak tendency | Refuse tendency |
| --- | --- | --- | --- | --- |
| Neighbor threatened by target | High | Guarantee, border defense, military aid | Low | Low |
| Country with unresolved claim | High | Recognition of claim or promised settlement | Low | Medium if sponsor opposes claim |
| Ideological rival | Medium to high | Propaganda support, regime-security aid | Low | Medium if members are ideologically incompatible |
| Target friend | Low | Strong guarantee or proof of target betrayal | High | High |
| Target subject or ally | Blocked for normal recruitment | None | Can create counterintelligence clue only | Required |
| Factionless minor with weak security | Medium | Protection, aid, sponsor access | Medium | Medium |
| Country in incompatible faction | Very low or blocked | Faction exit guarantee | Medium | High |
| Distant country with no reach | Low | Basing access, spoils, sponsor logistics | Medium | High |
| Country losing a war | Medium if sponsor can save it | Immediate aid and guarantee | Medium | Medium |
| Human-controlled country | Choice-based only | Player-defined | Player-defined | Player-defined |

## Major sponsor entry

A major sponsor is not a random reward for reaching Evolution II. It must pass strategic validity.

| Factor | Weight direction | Design interpretation |
| --- | --- | --- |
| Existing rivalry with target | Strong positive | Sponsor has a reason to invest |
| Target threatens sponsor sphere | Strong positive | Coalition protects regional position |
| Geographic reach through members | Strong positive | Minors provide ports, borders, or air access |
| Target world-tension contribution | Positive | Sponsor can justify containment |
| Sponsor already at war with target | Blocked as secret join, reveal contract may apply if already a member through valid prior state | Avoid retrospective hidden membership |
| Sponsor losing existential war | Strong negative | It cannot credibly direct a new coalition |
| Sponsor faction obligations | Negative or blocker | Existing alliance may be incompatible |
| Strong ideological alignment with founders | Positive | Easier command and public justification |
| Severe ideological incompatibility | Negative | Mixed pact needs stronger common threat |
| High chaos | Positive | Risk tolerance and unusual alignments rise |
| Target very weak and isolated | Mixed | Opportunist sponsor may join, defensive sponsor may see no need |
| Target very strong | Positive until suicidal threshold | Fear and balance-of-power motives rise |
| No plausible theater | Strong negative | Distant paper membership adds no gameplay |

## Pact doctrine behavior

| Doctrine | Operational focus | Recruitment profile | Reveal preference | War goal behavior | Main fracture risk |
| --- | --- | --- | --- | --- | --- |
| Containment Front | Intelligence, guarantees, access denial, defensive preparation | Fearful neighbors and cautious states | Public reveal with deterrent countdown | Limit target expansion or impose security settlement | Aggressive members demand war |
| Punitive Coalition | Sabotage, border action, military preparation | Grievance states and military opportunists | Rapid reveal and attack | Territorial or military punishment | Spoils disputes and casualty shock |
| Regime Pressure | Propaganda, infiltration, political disruption | Ideological rivals and exiles' patrons | Reveal after internal destabilization | Government change or ideological isolation | Members disagree on successor regime |
| Spoils Compact | Recruitment, secret bargains, access deals | Opportunists and states with claims | Reveal when target appears vulnerable | Partition, concessions, and status gains | Competing claims and sponsor dominance |

## Cohesion behavior

| Cohesion band | Pact behavior | Recruitment | Operation risk | Reveal behavior | War behavior |
| --- | --- | --- | --- | --- | --- |
| Fragile | Avoid lethal actions, hold mediation meetings | Limited and targeted | Low | Delay unless secrecy is impossible | Delayed calls and separate terms likely |
| Uneasy | Normal low-risk operations | Moderate | Medium | Reveal only with high readiness or exposure | Weak coordination |
| Functional | Diverse operations and planned recruitment | Active | Medium to high | Doctrine-driven | Normal coalition play |
| Committed | Coordinated incidents and sponsor-led plans | Strong | High | Can reveal early | Rapid calls and shared offensives |
| Fanatic | Rare, high-chaos state | Aggressive | Very high | Prefers public confrontation | Refuses settlement until major defeat |

## Readiness behavior

| Readiness band | Hidden preparation | Visible incidents | AI objective |
| --- | --- | --- | --- |
| Improvised | Basic contacts and vague plans | Isolated incidents | Gain intelligence and access |
| Networked | Stable liaison, preliminary depots | Repeated methods | Protect routes and recruit |
| Operational | Theater assumptions and target vulnerabilities | Serious sabotage and surveys | Raise cohesion or resolve exposure |
| Mobilized | Calls, depots, access, offensive timing | Exercises and visible pressure | Reveal on favorable schedule |
| Overextended | High plan ambition with poor cohesion or resources | Noisy incidents and mistakes | Consolidate or risk fracture |

## Evidence response by pact AI

| Target Evidence | Pact adaptation |
| --- | --- |
| Minimal | Continue preferred operations and broad recruitment |
| Suspicious pattern | Reduce repetition and use intermediaries |
| Credible network | Clean routes, feed false clues, pressure sources |
| Confirmed member | Protect or sacrifice exposed member based on cohesion |
| Sponsor proof | Accelerate reveal, discredit evidence, or withdraw sponsor |
| Near-complete case | Fracture, public justification, preemptive reveal, or desperate sabotage |

## Preparedness response by pact AI

| Target Preparedness | Pact adaptation |
| --- | --- |
| Unready | Build readiness and preserve surprise |
| Alert | Test a different surface and recruit around defenses |
| Guarded | Shift toward diplomacy, deception, and indirect pressure |
| Mobilized | Seek another theater, fracture target alliances, or reveal before defenses improve further |
| Fully prepared | Delay offensive if doctrine is defensive, or escalate political pressure and sponsor recruitment |

## Reveal decision tree

1. If any active member enters a normal hostile war against the target, reveal immediately and call every valid member.
2. Otherwise, if Evolution III is active and the offensive countdown completes, reveal and begin war according to doctrine.
3. Otherwise, if the target completes a valid forced-reveal action, reveal with weakness from Evidence and compromised networks.
4. Otherwise, if Evidence is near complete and cohesion is low, consider fractured reveal or collapse.
5. Otherwise, if sponsor withdrawal leaves too few committed members, collapse or return to minor-led secrecy.
6. Otherwise, continue operations with adaptation to target defenses.

## Coalition war AI

| Role | Front behavior | Support behavior | Withdrawal behavior |
| --- | --- | --- | --- |
| Faction leader | Prioritize target defeat, allocate theaters by access, maintain Resolve | Coordinate calls, aid weak members, manage war aims | Rare unless sponsor collapse or doctrine goal met |
| Neighboring minor | Defend border, exploit prepared routes, avoid suicidal deep offensives | Local supply and intelligence | Seeks terms after heavy losses and low Resolve |
| Maritime member | Raid convoys, secure access, support coastal fronts | Naval and air aid | Withdraws if access is lost and motive is weak |
| Distant member | Avoid useless land deployment | Equipment, expeditionary, air, naval, intelligence support | Can reduce commitment without immediate exit |
| Fear member | Defensive lines and containment | Guarantees and support | Accepts security settlement readily |
| Grievance member | Focus disputed region or punitive objective | Local offensive support | Accepts specific territorial settlement |
| Ideological member | Sustained political and military commitment | Propaganda and internal subversion | Harder to settle with unless regime conditions change |
| Opportunist member | Join successful fronts, avoid attrition | Limited aid until victory seems likely | First to seek separate terms |
| Turned member | Delay call, misroute support, expose depots | Feed target intelligence | Defects when exposure and survival conditions align |

## Scenario AI

| Scenario type | Coalition composition | AI emphasis |
| --- | --- | --- |
| Regional Ring | Neighboring and nearby minors | Multi-border pressure, local access, rapid defense |
| Ideological Front | Ideological rivals with compatible governments | Regime pressure and sustained cohesion |
| Great-Power Sponsor | One major with regional partners | Sponsor-led theater plan and aid distribution |
| Unlikely Coalition | Mixed ideologies united by fear or grievance | High initial power, faster cohesion decay, strong dispute events |
| Random Coalition | Valid weighted pool | Adapt doctrine from composition and geography |

Intensity affects AI boldness, starting Resolve, readiness conversion, and risk tolerance. It must not make AI ignore impossible geography or active existential wars.

## Multiplayer AI and human safeguards

- Human candidates receive explicit choices.
- AI may not use hidden knowledge to target innocent human countries as confirmed members.
- A human pact member who accepted must receive reveal and war obligations clearly before commitment.
- A human target receives the same visible Evidence and Preparedness logic as single-player.
- Scenario launch should require consent before assigning a human-controlled country to an enemy coalition.
- AI should not exploit tag switching to retarget or clear the pact.

## AI cleanup

AI strategy flags and priorities close when:

- the pact collapses
- the target ceases to exist
- a member is removed from active validity
- reveal converts hidden strategy into faction-war strategy
- the target war ends
- the faction dissolves or changes into a postwar regional bloc
- a manual scenario is reset or ends

No country should retain anti-target hidden priorities after it is no longer an active member.

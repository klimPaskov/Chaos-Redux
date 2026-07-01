# Event 011 Secret Alliance Spec, Part 4 Systems, AI, Assets, Super-Event, Achievements, and Acceptance

## Event log and catalog presentation

The event log should support two kinds of detail.

Early detail should be vague and public. It should describe unexplained coordination, foreign meetings, and rising diplomatic coldness without naming hidden signatories.

After public exposure, event detail should update to describe the Anti-[target country] Pact and the visible state of the crisis. The implementation should avoid mechanical reward lists in event details. The spreadsheet details should mirror the final in-game Event Details wording after implementation.

Evolution entries should be actual evolutions:

| Evolution | Log direction | Actor |
| --- | --- | --- |
| Evolution I | coordinated minor expansion becomes visible through repeated diplomatic habits | target as actor, with pact hidden |
| Evolution II | the conspiracy gains active operational reach and the target opens countermeasures | target as actor, patron if revealed later |
| Evolution III | public pact crisis and open faction pressure emerge | target and visible pact leader if known |

## Chaos Redux system connections

The event should interact with existing systems where it is natural.

| System | Connection direction |
| --- | --- |
| Chaos Meter | sabotage, reveal, and pact war can raise chaos modestly. Quiet baseline should not flood chaos. |
| Event timer | Event 011 remains Minor Fire-Once and should contribute ordinary minor pacing when fired. |
| Diplomatic Panic | Secret Alliance can increase diplomatic pressure themes, but it is not a cluster member by default. |
| War systems | reveal war should use normal war participation where possible and should not create a separate one-off war framework. |
| Condemnation | only interact if pact operations use already-condemned unconventional actions, which is not core to this event. |
| Deaths | sabotage or war may use ordinary deaths systems only if implementation already routes those damage events. |
| World threat | the pact is a hostile diplomatic crisis, not a world-threat source unless later implementation radically changes it. |

## Temporary ideas and national spirits

The event should use a small number of meaningful ideas rather than many one-off modifiers.

| Idea working label | Owner | Role | Lifecycle |
| --- | --- | --- | --- |
| Unnamed Diplomatic Pressure | target | early subtle relation and trade pressure | replaced by Dossier Pressure when Evolution II opens |
| Dossier Pressure | target | visible pressure with suspicion and readiness tooltip | upgraded, removed, or transformed on exposure |
| Counter-Conspiracy Network | target | earned through decisions, improves investigation and war opening | strengthens with successful missions, removed after aftermath |
| Secret Protocol Discipline | pact members | hidden coordination and operation support | becomes public war idea or is removed when member exits |
| Patron Liaison Offices | major patron | improves pact cohesion and operations | removed if patron exposed, split, or defeated |
| Publicly Exposed Signatory | revealed member | diplomatic penalty, lower secrecy, possible readiness boost | removed after settlement or converted in war |
| Pact War Coordination | formal pact members | temporary opening war coordination | decays or upgrades based on war progress |
| Diplomatic Credibility Restored | target after peaceful exposure | reward for clean exposure and fracture route | timed or medium-term legacy |

Effects should be strong enough to matter. They should change operations, investigation, readiness, diplomacy, or war opening behavior rather than giving tiny decorative modifiers.

## AI behavior matrix

The AI should understand both sides of the system.

### Pact members

- Convener AI prioritizes secrecy, invitation attempts, and cohesion.
- Financier AI prioritizes covert funding, sabotage support, and weakening target counter-readiness.
- Provocateur AI prioritizes border incidents, threats, and readiness gain.
- Major patron AI prioritizes member protection, arms support, faction timing, and avoiding early exposure if not ready.
- Weak recruits prioritize survival and may leave if exposed or pressured.

### Target AI if Event 011 can target AI countries in tests

If an AI country becomes the target through manual testing or non-player event routing, it should use simplified but real behavior:

- investigate when suspicion is high
- protect industry after sabotage
- guard borders with neighboring suspects
- expose pact only when evidence is strong
- prepare war if pact readiness is high
- avoid reckless border wars if already fighting a major war

### Foreign observers

Countries outside the pact can react after public exposure:

- target allies become more willing to support the target if evidence is high
- neutral democracies become less willing to join exposed pact members
- rivals of the target may quietly sympathize with the pact but should not join unless invited and eligible
- countries threatened by a major patron may back the target diplomatically

## Super-event direction

The reveal super-event fires when war reveal creates the formal Anti-[target country] Pact, or when a public self-reveal reaches the same diplomatic threshold. It should not fire for a small partial exposure that reveals only one suspect.

Role: reveal and faction formation.

Title direction: short, cold, and specific to hidden diplomacy becoming public. Research required. Do not use a generic world-crisis title.

Description direction:

- explain that several states have moved from private coordination into open anti-target alignment
- mention the target dynamically
- name the formal pact only after reveal
- state that the first war contact has activated the hidden protocol if reveal came from war
- avoid a generic apocalypse tone
- keep the focus on the sudden public shape of a prepared diplomatic machine

Quote direction:

- research lines about secret diplomacy, open covenants, hidden agreements, betrayal, alliance obligations, or public consequences of private promises
- Wilson's Fourteen Points is a candidate direction, but final use requires the super-event text researcher
- public domain diplomatic writing, parliamentary speeches, memoirs, or treaty commentary may fit

Button remark direction:

- bitter diplomatic irony or a short cultural allusion about private promises coming due
- research required before final wording
- avoid cheap comedy if the reveal immediately starts a large war

Image direction:

- generated period-documentary or symbolic super-event image
- hidden diplomatic chamber, shadowed delegates, sealed protocol, radio cables, guards at a corridor, and a central sense of coordinated threat
- avoid readable text
- avoid making a map the main subject
- no real leader likenesses

Audio direction:

- tense, formal, restrained music with a sense of a chamber opening into war
- public domain or clearly licensed audio only
- no placeholder, generated tone, or ambient drone as final audio

## Asset coverage

Required visual asset families:

| Asset family | Source mode | Target use |
| --- | --- | --- |
| super-event image | generated event art | reveal super-event |
| report image family | generated or sourced depending on incident | suspicious meetings, sabotage aftermath, exposed protocol |
| decision category icon | generated icon | Counter-Conspiracy Dossier category |
| decision icons | generated icon | investigation, protection, diplomacy, border watch, exposure, war preparation |
| national spirit icons | generated icon | pressure, counter-network, pact coordination, public exposure |
| faction emblem | generated emblem | Anti-[target country] Pact display if UI supports it |
| Dossier Board UI pieces | generated UI art plus normal UI slicing | scripted GUI panel, meters, cards, warning frames |
| animated UI state assets | generated per-frame source art | evidence pulse, readiness warning, exposed card, war countdown |
| achievement icons | generated icons | achievement set |

Historical flags and real leader portraits are not needed because the event uses existing countries and does not create real leaders. Do not replace country flags just because a country becomes a pact member.

## Achievement set

Achievement titles are working labels, not final localisation.

| Working key | Player route | Conditions | Disqualifiers | Difficulty | Icon direction |
| --- | --- | --- | --- | --- | --- |
| `secret_alliance_empty_chair` | peaceful exposure | expose the pact before any target-member war and make at least two members leave | target starts war first, pact war begins | hard | empty conference chair, sealed folder |
| `secret_alliance_all_names` | investigation mastery | identify every live member before public reveal | public reveal before all members confirmed | hard | list of signatory seals, no readable text |
| `secret_alliance_three_knocks` | founder neutralization | reveal or split all three founding members within a tight time window after Evolution II opens | any founder dies from unrelated annexation before being handled | hard | three broken wax seals |
| `secret_alliance_lone_target` | survival against odds | as a minor target, survive and win a reveal war against a pact with at least five members and one major patron | target joins a larger faction after reveal if achievement requires isolation | very hard | small shield surrounded by dark banners |
| `secret_alliance_counter_protocol` | preemptive war | launch the war option at Evolution III with high counter-readiness and defeat the pact quickly | low counter-readiness, pact has fewer than four members | hard | crossed protocol pages and bayonet |
| `secret_alliance_wrong_room` | misdirection | plant a false leak that causes the pact to expose or expel a member, then win without declaring first | false leak fails twice | medium hard | open door with wrong delegation shadow |
| `secret_alliance_no_patrons` | anti-major counterplay | prevent any major patron from joining before reveal, then dissolve or defeat the pact | major patron joins at any point | hard | severed radio mast and major-star silhouette |
| `secret_alliance_paid_in_promises` | promise exploitation | expose conflicting promises between two members and force both to leave or refuse war | neither member had conflicting promise flags | hard | torn treaty ribbon |

Achievements should be rare and route-spanning. Do not grant any achievement only because Event 011 fired.

## Implementation acceptance criteria

The event is complete only when all of these are true:

1. Event 011 selects valid founders and is unavailable when three valid founders cannot be found.
2. The target, founders, members, roles, patron, and public leader are tracked safely.
3. Baseline, Evolution I, Evolution II, and Evolution III behavior exist and are distinct.
4. Active-event evolutions and pre-fire evolved openings are both handled where the spec requires them.
5. Member invitations are dynamic and capped.
6. War reveal creates the formal pact and pulls all valid members into war.
7. Player investigation and counterplay can weaken, expose, or split the pact.
8. Decisions use concrete costs, objectives, and risks instead of default political power purchases.
9. Border missions require real borders, units, states, or routes.
10. The Dossier category or GUI shows readable values and does not reveal hidden members too early.
11. AI uses the pact actions and target counterplay safely.
12. The reveal super-event has researched final text, verified audio, image, and complete wiring.
13. Required static and animated assets have source files, processed previews, DDS outputs, manifests, and sprite handoffs.
14. Event log, event detail, evolution entries, docs, and catalog update handoff all align.
15. Achievements are implemented with tracking, icons, disqualifiers, localisation, and docs.
16. Localisation is written as final in-world text and does not paste planning directions.
17. Subagent audits are run before completion, especially decision, localisation, scripted-system, and completion audits.
18. Any simplification, fallback, blocked source, missing asset, or skipped validation is reported directly.

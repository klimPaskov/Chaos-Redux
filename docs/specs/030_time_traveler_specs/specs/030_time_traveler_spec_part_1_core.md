# Event 030 Time Traveler Specification Part 1: Core Design

Acceptance status: proposed design, disposition `unresolved` unless a line cites a user-brief or user-allocation basis.
The [README](../README.md) records the acceptance basis, the implemented runtime baseline, and open questions.

## Playable promise

Event 030 gives one country access to knowledge that should not exist and asks whether that knowledge can be used without losing control of the person who carries it or the history that made it accurate.

The baseline must already support a complete campaign story.
The traveler proves their origin, enters an access arrangement, gives specific advice, becomes the target of an international intelligence race, and reaches a durable outcome.
Evolutions widen the consequences.
They do not replace the baseline or postpone its resolution.

The event should feel useful from its first day.
The host gains a modest national spirit because the traveler has already briefed selected officials.
The strongest rewards come from completed consultation objectives.
The player should care about what the traveler recommends, whether the advice still applies, and what the government must risk to act on it.

## Host selection

The host pool is every existing major country plus every player-controlled country, including a player non-major.
Each candidate's owner score is multiplied by the shared individual-crisis ticket weight from [individual crisis targeting](../../../systems/event_system/individual_crisis_targeting.md), so a country already carrying three crisis packages is ineligible and a country carrying one or two is less likely.
Actual nonhuman countries, special Chaos actors without civilian institutions, and countries under a terminal world-end state are excluded through the shared classifiers.
The original traveler appears only once per campaign.

The owner score should prefer a player country enough that a single-player campaign usually sees the mechanic, while preserving the chance that an AI major hosts and the player participates as a foreign rival.
The exact weighting belongs in the `TT_AI` probability scenarios in Part 10.

The arrival state is the capital when it is controlled and not encircled.
Otherwise it is the safest controlled core state with strong infrastructure, a research facility, or an intelligence agency.
The selected state is saved before the opening event so later decisions do not re-roll it.

The implemented runtime already performs load-aware weighted selection, reserves the slot with a short prefire flag, and refuses to consume the event when the pool is empty.
It currently draws from every existing country with an equal base weight, so the major-or-player owner score and the classifier exclusions remain pending.

## The traveler

The traveler is a fictional Chaos Redux character.
This avoids assigning impossible future knowledge to a real person and permits a coherent original portrait, advisor role, leader route, and possible temporal duplicate.

The character has one knowledge profile selected at arrival and shown as a character trait:

| Profile | Strongest consultation families | Weakness |
| --- | --- | --- |
| Strategic analyst | Military, diplomacy, and counterintelligence | Scientific advice depends on existing institutions |
| Systems engineer | Industry, science, and logistics | Political forecasts are less exact |
| Institutional historian | Domestic threats, diplomacy, and state reform | Battlefield advice is less detailed |

The profile decides which consultation families are cheaper and stronger.
It is not a fourth value.

The traveler remembers one possible future, not a perfect script of the current campaign.
They can know private conversations, secret projects, later technologies, institutional failures, and major political outcomes from that future.
They do not possess complete technical drawings, perfect battlefield vision, or knowledge of events the player has already changed.

## Core state model

Event 030 has four connected layers.

### Custody

Custody identifies the country that physically controls the original traveler.
Only the custodian receives consultations, the traveler character, and the main decision category.
Custody can change through defection, asylum, abduction, occupation, negotiated transfer, or disappearance.
Custody, not legacy knowledge, occupies the custodian's individual-crisis slot.

Every previous custodian keeps the knowledge its institutions copied.
That legacy is weaker than direct access and cannot recreate the traveler.

### Access arrangement

The host chooses one of four access arrangements after verification.
Part 2 defines them.

| Arrangement | Main tradeoff |
| --- | --- |
| Cabinet Advisor | every consultation family, faster Exposure growth |
| Secret Program | slowest Exposure growth, only two profile families plus counterintelligence, severe breach risk |
| Confinement | low Exposure and strong records, slower Credibility and a restless traveler |
| Public Recognition | permanent public Exposure, diplomatic prestige, and open foreign competition |

The arrangement can later be revised through one costly policy decision or a crisis event.

### Institutional knowledge

The national spirit represents knowledge already copied into ministries, staffs, archives, factories, and laboratories.
It begins as a restrained mixed bonus and upgrades through completed consultations.
The system never stacks separate advice spirits.

If the traveler is lost, direct access and the advisor role end.
The former custodian keeps a reduced legacy stage whose strength depends on completed consultations and protected records.

### Temporal disturbance

Timeline Divergence is global and survives the traveler.
Once future knowledge has changed decisions, the event can evolve even if the original traveler dies.
Evolution I requires a living or missing traveler.
Evolutions II through V continue from the temporal disturbance itself.

## Baseline phases

### Phase 1: Arrival

The traveler appears under controlled circumstances and asks for contact with the state.
The character gives one piece of evidence that can be checked within days.
The host chooses whether to hear, detain, isolate, or discreetly test the visitor.
Refusing all contact ends direct access, but officials may still copy the first proof, rumors may escape, and Timeline Divergence may begin at a low level.

### Phase 2: Verification

The host receives a short verification chain drawn from three proof families:

- a secret project or hidden facility
- a private conversation, sealed order, or undisclosed political arrangement
- a near-term forecast with a bounded validation window

Two proof families must succeed before the traveler is treated as authentic.
A high-chaos opening can validate the first proof immediately and begins the second with higher Exposure.

### Phase 3: Access decision

The government chooses the access arrangement.
This sets the first spirit stage, the available consultation families, and the Exposure growth rate.

### Phase 4: Consultation cycle

The host may run one consultation mission at a time.
The first consultation is offered soon after access is set.
Later consultations use a shared cooldown and choose targets from current wars, industry, research, diplomacy, and internal threats.

### Phase 5: International race

A bounded group of foreign countries becomes interested.
They infiltrate the program, plant forgeries, offer asylum, or try to seize the traveler.
The host answers with a small set of countermeasures and can share selected forecasts with allies.

### Phase 6: Durable outcome

The baseline reaches a durable state after a completed consultation set, one major custody crisis, or loss of the traveler.
Later evolutions remain eligible where their prerequisites still exist.

## Baseline completion states

| State | Direct consultations | Institutional legacy | Later effect |
| --- | --- | --- | --- |
| Trusted advisor | Full | Strong and upgradeable | Fastest route into Evolution I |
| Confined asset | Restricted | Strong technical record | Higher defection and internal control risk |
| Public figure | Full but exposed | Strong and widely copied | Foreign action intensifies and secrecy cannot return |
| Defected or abducted | Moves to the new custodian | Origin keeps reduced legacy | Rivalry and counter-operation chain continues |
| Assassinated | Ends | Reduced legacy | Evolution I closes, later evolutions remain possible |
| Disappeared | Suspended | Reduced legacy | A later reappearance is possible, never guaranteed |
| Fragments dispersed | Current custodian only | Several countries hold a Future Fragment | Divergence grows and foreign alignment broadens |

## Evolution ladder

| Evolution | Chaos gate | Base pacing after prerequisites | Main new play |
| --- | ---: | ---: | --- |
| I, The Traveler's Ambition | `200+` | about 105 days | political struggle around the original traveler |
| II, The Door to the Past | `400+` | about 135 days | limited historical arrivals and claimant movements |
| III, Visitors from the Future | `600+` | about 150 days | later-era visitors and incompatible futures |
| IV, Epoch Breakdown | `800+` | about 120 days | material temporal incidents and machine scouts |
| V, War of the Possible Futures | `1000+` | about 90 days | temporal stances, portal nodes, and machine world-end readiness |

These are tuning anchors for the shared evolution MTTH framework.
Timeline Divergence is an MTTH factor for Evolutions II through V, not a hard gate: a Recognizable timeline slows them and a Broken timeline speeds them up, so restraint delays temporal collapse without locking content forever.
Evolution activation gives zero Chaos.
Chaos changes only from concrete consequences listed in Part 10.

## High-chaos first firing

When Event 030 first fires after one or more evolution thresholds are already met, the opening is compressed.
The traveler still proves their origin and the player still chooses access.
The event then seeds the eligible higher layer without an empty baseline wait.

A compressed opening uses one opening super-event, one host event, and a bounded sequence of delayed reports, never five same-day popups.
Each active evolution is still recorded through the shared evolution log with its stage and actor context.

## Cluster decision

Event 030 has no cluster.
Its connections to other events are conditional integrations, not a request to fire several events as one incident.

## Content that stays absent

The design does not create a full scripted GUI, a global country roster, a technology tree, a portal currency, or a full focus tree for every returned person.
Part 2 and the [anti-bloat audit](../quality/anti_bloat_and_clarity_audit.md) list the rejected meters and surfaces.

## Legacy runtime migration

The current `events/030_time_traveler.txt` is a short legacy chain that this design replaces.
Its retained parts and superseded parts are recorded in the [README](../README.md#implementation-status).
The implementation must keep the Event 016 contact bridge working when the legacy `time_traveler` idea is retired, as Part 10 describes.

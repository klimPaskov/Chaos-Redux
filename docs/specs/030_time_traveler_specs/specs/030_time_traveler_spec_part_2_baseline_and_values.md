# Event 030 Time Traveler Specification Part 2: Baseline Progression and Public Values

Acceptance status: the three value names and the Evolution V Temporal Stability presentation come from the user's Event 030 brief.
Bands, thresholds, arrangements, and spirit stages are proposed design, disposition `unresolved`.

## Public value budget

The player tracks three persistent values.
No other Event 030 number is shown as a long-term counter.
This section owns the value rules; other parts and matrices point here.

| Value | Scope | Question it answers | Decision it drives |
| --- | --- | --- | --- |
| Credibility | Current custodian | How much does the government trust the traveler | which consultation tier is offered and whether ambition can start |
| Exposure | Traveler and custody network | How widely is the traveler known | which foreign operations rivals can attempt and how many rivals join |
| Timeline Divergence | Global | How far has the campaign moved from the remembered future | how precise advice is and how fast later evolutions arrive |

Each value runs from `0` to `100` and has three bands.
The category header shows the value, its band name, and one icon.
The tooltip states only what the current band allows or threatens and the last three causes of change.
Hidden scores for bloc support, operation networks, visitor reliability, portal severity, machine footprint, and AI weights stay internal and never appear as numbers.

## Credibility

Credibility belongs to the current custodian.
A new custodian does not inherit the previous government's trust and starts from the transferred evidence, the transfer method, and the public record.

| Range | Band | What it changes |
| ---: | --- | --- |
| `0-34` | Doubted | only verification, containment, expulsion, and the basic consultation tier |
| `35-69` | Trusted | every family allowed by the arrangement, staff copying, and selective sharing |
| `70-100` | Indispensable | country-specific advanced variants, strongest spirit upgrade, and faster Evolution I |

Credibility moves only through evidence and outcomes, never through waiting.
It rises when a proof is verified, a consultation succeeds, a forged record is exposed before the government acts on it, or a rival operation proves foreign governments believe the traveler.
It falls when a consultation fails for an unchanged reason, the government acts on forged advice, the traveler conceals a personal interest, or two verified visitors expose a contradiction.
A failure caused by a recorded timeline change costs little or nothing, and the tooltip says that exact dates are becoming unreliable.

## Exposure

Exposure follows the traveler and the network of verified copies.

| Range | Band | Foreign behavior |
| ---: | --- | --- |
| `0-29` | Secret | at most two interested countries, only infiltration is possible |
| `30-64` | Suspected | up to four interested countries, forgery and asylum offers become possible |
| `65-100` | Public | up to six interested countries, seizure attempts and open diplomatic pressure become possible |

Public Recognition or a confirmed public revelation sets a permanent floor at the Public band.
Exposure rises from wide staff circles, leaked consultations, failed foreign operations that become public, propaganda use, and returned figures who confirm the temporal disturbance.
It falls from relocating the traveler, a successful counterintelligence sting, or exposing a forged story.
Every reduction costs capacity and slows consultations.

## Timeline Divergence

Timeline Divergence is global.
It measures how much the remembered future has lost predictive value and how much temporal activity the campaign can sustain.

| Range | Band | Advice precision | Temporal pressure |
| ---: | --- | --- | --- |
| `0-29` | Recognizable | dates and named actors | later evolutions arrive slowly |
| `30-64` | Altered | date ranges and trigger conditions | normal evolution pacing, small incidents |
| `65-100` | Broken | structural warnings only | later evolutions arrive quickly, machine activity becomes possible |

Divergence rises from acting on advice that changes a major diplomatic or military outcome, deploying adapted future technology, placing the traveler in government, letting a returned figure or visitor take power, restoring a historical state, keeping a portal open, and letting machines seize industry.
It falls from closing a portal, destroying a machine node, resolving a claimant crisis without a new state, returning displaced people or formations safely, destroying dangerous future material after study, and completing coordinated closure projects.
Reductions are harder than increases.
The player can stabilize the world but cannot restore the original future after major changes.

Divergence changes only through visible sources and never drifts automatically.

## Temporal Stability in Evolution V

Evolution V shows Temporal Stability in the third slot instead of Timeline Divergence, because the player is now managing collapse.

`Temporal Stability = 100 - Timeline Divergence`

The underlying variable stays the same and only one of the two numbers is shown at any time.
Its bands are Coherent (`71-100`), Strained (`36-70`), and Collapsing (`0-35`), which mirror the Divergence bands.
The [README open questions](../README.md#open-questions) record a proposal to keep the Divergence label throughout.

## Verification chain

The opening chain selects two or three proofs that fit the host.

### Secret project proof

The traveler names a real hidden facility, project, procurement route, diplomatic channel, or research obstacle.
The proof uses country-specific content where a researched package exists and otherwise reacts to the host's current technology, agency, production, and active focus.
It never reveals a route the player has not unlocked through normal play.

### Private conversation proof

The traveler recounts a recent private exchange involving the head of government, a minister, a commander, or a diplomat.
The event names the in-world character when one exists and otherwise describes a sealed meeting without inventing a real historical quotation.

### Near-term forecast proof

The traveler predicts a bounded development within roughly 20 to 60 days, drawn only from current campaign state:

- a foreign diplomatic move already supported by relations and alliances
- a measurable production or supply bottleneck
- an enemy buildup along a real border
- a coup, strike, or faction split supported by current instability
- a disaster pattern only when the Event 013 gateway can prove it

The forecast is written as a range or condition and never forces unrelated AI behavior to make itself true.

## Access arrangements

The knowledge profile already decides which consultation families are strongest, so arrangements decide reach, secrecy, and the traveler's treatment rather than duplicating specialty.

### Cabinet Advisor

The traveler consults ministries, staffs, intelligence, and laboratories.
Every consultation family allowed by Credibility is available.
Exposure grows fastest of the private arrangements, rival staff recruitment is easier, and Evolution I gains broad support.

### Secret Program

Only the profile's two strongest families and counterintelligence are available.
Exposure growth is slowest and the security services gain influence.
A breach produces a larger Exposure jump than any other arrangement, because rivals learn the government hid a strategic asset.

### Confinement

Every family is available, but Credibility gains are halved because the traveler's evidence is filtered through guards.
Exposure stays low and records are well protected.
Asylum offers succeed more often and the traveler may build support among the few officials allowed to visit.

### Public Recognition

Exposure moves to the permanent Public floor.
The host gains diplomatic prestige and rapid staff coordination, later arrivals start verified, and rivals can act openly.

Revising the arrangement is one decision with a political-power cost and a cooldown, and it is the only way to restrict access.

## Institutional knowledge spirit

| Working label | Condition | Design role |
| --- | --- | --- |
| Unverified Forecasts | arrival before verification | small mixed benefit and administrative friction |
| Directed Foreknowledge | verified traveler with direct access | modest base bonus shaped by the profile |
| Distributed Future Knowledge | three successful consultations | stronger but bounded institutional bonus |
| Scattered Forecasts | traveler lost | reduced legacy based on completed consultations and protected records |

Each stage carries two or three coherent modifiers whose values live in script constants.
The baseline stage must be far weaker than the legacy `time_traveler` idea, which grants `+20%` research speed, `+100%` planning speed, `+50%` offence, and `+20%` army experience gain at once.
As a tuning anchor, Directed Foreknowledge should stay near the strength of an ordinary national-spirit advisor, and Distributed Future Knowledge near a mid-tree national focus reward.
Consultations carry the strong specialty rewards.

A Future Fragment is the single minor spirit that a foreign country gains from stolen or shared knowledge.
It never stacks and is the only Event 030 spirit a non-custodian can hold apart from Scattered Forecasts.

## Rumor progression

Rumors are consequence events, not flavor text.
Each rumor names one group and one concrete effect: scientists demand wider access, officers alter plans around private forecasts, journalists notice unusual security, diplomats ask whether policy rests on impossible information, industrialists compete for predicted contracts, or the opposition accuses the government of hiding a prophet or a fraud.
Rumors change Exposure, stability, foreign opinion, or support blocs.
They read the current arrangement and Exposure band so the same rumor never repeats unchanged.

## Prediction precision

The Divergence band sets the precision of every forecast.
A Recognizable timeline yields dates and named actors.
An Altered timeline yields date ranges and trigger conditions.
A Broken timeline yields structural warnings, such as an exposed supply network or an unstable coalition, without the exact outcome.
Every consultation tooltip states the current precision in one line.

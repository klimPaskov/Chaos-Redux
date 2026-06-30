# Event 011 Secret Alliance Balance and Validation Plan

This file defines implementation acceptance criteria and meaningful validation scenarios.

## Balance anchors

| Area | Intended balance |
| --- | --- |
| Baseline damage | Low. The player notices patterns but should not lose a campaign to baseline incidents. |
| Evolution I pressure | Moderate. More countries join and the pattern becomes visible, but direct war remains avoidable. |
| Evolution II pressure | High. Sabotage, intimidation, and border provocations become strategically relevant. The dossier gives tools at the same time. |
| Evolution III pressure | Very high. Public faction pressure and war readiness can become the main campaign problem. |
| Major patron | Strong impact. A major makes the pact more dangerous and easier to expose. |
| Player preparedness | Must matter. Prepared players should reduce sabotage and war shock in visible ways. |
| Evidence route | Must be viable. Strong evidence can force early reveal, member exits, or collapse. |
| War route | Must be viable but risky. Striking first should help only if evidence and preparedness justify it. |

## Dynamic scaling expectations

| Mechanic | Scales with |
| --- | --- |
| Candidate hostility | Opinion, ideology, claims, target world tension, shared borders, recent wars |
| Incident chance | Stage, secrecy, aggression, member roles, target stability, target countermeasures |
| Sabotage damage | Stage, aggression, target preparedness, guarded state missions, industry size |
| Invitation success | Cohesion, secrecy, major patronage, target exposure, invitee fear of target |
| Evidence gain | Suspicion, intelligence actions, target stability, failed pact actions, defector presence |
| Exposure success | Evidence, identified convenor, secrecy, observer relations, major patron role |
| Splitter diplomacy success | Member commitment, cohesion, evidence, relations, cost paid, patron pressure |
| War timer | War readiness, cohesion, major count, target preparedness, public ultimatum outcomes |
| Pact war bonuses | Cohesion, member count, major count, player exposure damage, target first strike |

## Exploit checks

| Exploit risk | Prevention |
| --- | --- |
| Repeated defector farming | Defection one-time per member, evidence rewards capped |
| Border war farming | Border war cooldowns, limited valid neighbor targets, isolation reward one-time |
| Free preparedness stacking | Preparedness cap, decay or conversion after war, mission caps |
| Infinite member invitations | Member count cap by stage, invitation cooldowns, candidate validity refresh |
| Easy public collapse | Exposure requires evidence and can fail |
| Free war bonuses | Preparedness rewards tied to completed missions and clear caps |
| Major patron suicide | AI avoids joining if it is collapsing or target alliance is overwhelming |
| Stale hidden members | Refresh helper sanitizes dead, annexed, capitulated, invalid, and exempt members |
| Player attacks isolated member repeatedly | Isolation flag is rare, explicit, and consumed or reviewed after border outcome |

## Meaningful validation scenarios

| Scenario | Setup | Expected result |
| --- | --- | --- |
| Calm baseline opening | Event fires early with many factionless minors available | Three valid minors join hidden compact, slow incidents begin, no instant war |
| Low candidate pool | Few valid minors exist | Event shows unavailable or waits rather than selecting invalid war enemies |
| Evolution I active compact | Hidden compact survives into Evolution I | New minor invitation logic works and refusals can leak evidence |
| Evolution II active compact | Compact reaches sabotage phase | Dossier opens, decisions show values, sabotage can be mitigated |
| Evolution II first firing | Event first fires after relevant stage | Major founder or patron path works with minors added around it |
| Major invalidation | Candidate major is in target faction or at war with target | Major is excluded from patron selection |
| Border member | Neighbor is identified | Border missions and controlled border war actions appear with named states |
| No border member | No member borders target | Border war actions stay hidden without clutter |
| Early exposure success | Player builds strong evidence before public stage | Pact reveals weakly or collapses, member exits possible |
| Exposure failure | Player exposes with weak evidence | Target loses credibility and pact aggression rises |
| Member war conversion | A hidden member enters war with target from another source | Public faction forms and valid members join war immediately |
| Isolated member exception | Player completed isolation chain | Isolated member does not trigger full war call unless conditions changed |
| Public compact countdown | Evolution III reveal occurs without war | War timer appears and responds to preparedness, cohesion, and ultimatums |
| Pact defeat | Target wins public war | Pact ideas, decisions, AI strategies, and timers clean up |
| Peaceful collapse | Player collapses compact through evidence and diplomacy | War never starts, aftermath and achievements evaluate correctly |
| Target capitulates | Pact wins | Severe concession or humiliation package applies without random state theft |

## Completion acceptance criteria

Implementation is not complete unless:

- Event 011 is registered as Minor Fire-Once and has stable root event wiring.
- Founder selection respects hard eligibility and minor preference.
- Hidden compact values are dynamic and visible only through the correct surfaces.
- Evolution logs record only the three evolution stages.
- Dossier category has selected-target flow, AI equivalents, nonstandard costs, timed missions, custom tooltips, and cleanup.
- Public reveal creates the dynamic Anti-[target] Pact and handles the instant war rule.
- Defection, isolation, exposure, public compact, war, defeat, collapse, and target defeat outcomes exist.
- Assets and animation handoffs are implemented or explicitly blocked before public reveal super-event completion.
- Achievements are wired with nontrivial conditions and disqualifiers.
- Localisation is final, clear, and does not reveal hidden members too early.
- AI weights prevent invalid targets and suicidal public patron behavior.
- Docs and catalog wording align with final in-game text.

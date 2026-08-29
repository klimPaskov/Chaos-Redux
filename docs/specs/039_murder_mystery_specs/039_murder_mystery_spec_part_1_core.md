# Murder Mystery Specification Part 1: Core Event Contract

## Catalog contract

Event 039 is a Minor Fire-Once event available from Chaos level 1. It belongs to the Intelligence cluster as a Medium member. Automatic selection may choose one valid random major or one valid player-controlled ordinary country. A player country can qualify without major status and must pass every safety and viability gate.

The current exported event catalog still identifies Event 39 as Minor Repeatable. Implementation must update the authoritative XLSX workbook through the spreadsheet worker and regenerate the exported CSV files. The CSV snapshots in the supplied planning package are read-only evidence and must not be edited directly.

## Player-facing premise

A sitting national leader is murdered by an unidentified attacker. The country must secure the succession, preserve evidence, protect vulnerable officials, and identify the murderer before imitation, institutional infiltration, and foreign cells make a complete resolution impossible.

The event should feel uncertain because evidence is incomplete and some crimes are committed by copycats. Uncertainty must come from case state, contradictory clues, missing witnesses, and the difference between the original murderer and imitators. It must not come from hidden random failure that makes good preparation meaningless.

## Host eligibility

A country is eligible only when all of the following are true:

- it exists and is either a major or player controlled
- it passes `uses_normal_civilian_systems`
- it is not classified by `is_special_chaos_country`
- it is not classified as an actual nonhuman country
- Event 39 is not already active or permanently resolved
- it has a current leader whose Event 39 disposition is explicitly safe for the opening murder
- it has at least one verified succession route that produces a functioning replacement government
- it can own the investigation category and receive case actors
- it has enough institutional depth for later target roles, or safe generic office casualties can represent missing roles
- it has at least one valid state for baseline state incidents
- it is not already in a terminal world-end state that conflicts with Event 39

Normal host selection must also pass a predictive Assassin State split preflight whenever Evolution III is enabled. The preflight proves that the opening map can support a connected movement territory and a viable original government, while recognizing that later wars may invalidate that result. If later map changes remove every safe split, Evolution III waits under the fail-closed rule in Part 4 and the government receives the final underground-crackdown phase. A country that could never support the territorial stage contributes zero host weight unless Evolution III is disabled before Event 39 fires.

## Host weighting

The selection model should use named scenarios and dynamic weights. A universal equal roll is rejected. A valid player country receives a strong inclusion weight so a human can encounter the event. Major countries receive weight based on safe succession, number of eligible character roles, agency capacity, state count, connected core territory, and likelihood of a viable Evolution III split. Countries with active internal collapse, recent forced leader replacement, or unresolved character ownership transitions receive reduced weight.

The weighting must never overcome a failed hard gate. A country with no safe successor, protected leader, invalid civilian classification, or unsafe character package contributes zero.

## Event-owned public values

### Case Progress

Case Progress is a country value from 0 to 100. Higher values mean the investigation has converted clues into an actionable case.

| Range | Public stage | Meaning |
| --- | --- | --- |
| 0 to 24 | Rumors | The country has fragments, witnesses, and theories with no reliable link |
| 25 to 49 | Trace | Investigators can connect incidents, movements, or logistics |
| 50 to 69 | Identified Cell | One operational group or support route is understood |
| 70 to 84 | Suspect Network | The core network and likely protection system are mapped |
| 85 to 99 | Trap Ready | The country can launch a final capture operation |
| 100 | Capture Resolution | The active target is resolved through capture, death, escape, or a wider network result |

Case Progress rises through evidence preservation, intelligence work, witness protection, cell raids, captured records, allied intelligence, and completed missions. It falls through murdered investigators, destroyed evidence, compromised offices, abandoned operations, and successful cell counteraction. It is capped by the current phase when the country lacks a required capability, but the player must be told which public requirement blocks further progress.

### Network Reach

Network Reach is the event-wide movement value from 0 to 100. Higher values represent recruitment, safe houses, institutional access, foreign cells, military cadres, and public mythology around the murderer.

| Range | Public stage | Meaning |
| --- | --- | --- |
| 0 to 24 | Isolated | One attacker or a very small support circle |
| 25 to 49 | Cult Support | Protection, imitation, recruitment, and witness intimidation exist |
| 50 to 69 | Organized Network | Multiple cells coordinate resources and targets |
| 70 to 84 | International Access | Foreign cells, routes, and shared methods are active |
| 85 to 100 | Insurrection | Cells can support territorial revolt and open warfare |

Network Reach rises through concrete successful murders, escaped raids, institutional infiltration, foreign cell formation, territorial revolt, Assassin State victories, and subject creation. It falls through captured cell leadership, secured records, protected targets, exposed supply routes, defeated revolts, and durable international cooperation.

The original host sees Case Progress and Network Reach. Secondary affected countries see their Local Case Progress and the shared Network Reach stage. The Assassin State sees Network Reach and Brotherhood Cohesion instead of Case Progress.

### Brotherhood Cohesion

Brotherhood Cohesion belongs to the Assassin State and mature foreign Assassin derivatives. It measures whether cells, military formations, administrators, subjects, and the central leader accept enough common direction to function.

Cohesion is hidden before Evolution III. It becomes a public value from 0 to 100 once the Assassin State exists. Low Cohesion weakens supply, subject obedience, military planning, and revolt coordination. High Cohesion enables advanced units, synchronized uprisings, faction action, and the terminal route. Extremely centralized and extremely decentralized routes raise different risks, so no route can keep maximum Cohesion without maintenance and tradeoffs.

## Hidden support state

The system may track hidden values for target vulnerability, witness safety, investigator exposure, killer adaptation, cell maturity, route security, counterfeit evidence, succession strain, and local government weakness. These values support simulation and AI. They must not become extra persistent numbers in the player interface.

Repeated use of one investigation action may raise hidden killer adaptation and reduce the next use. The category tooltip must show that the method has become less effective. Adaptation must decay or be bypassed by changing methods. It cannot turn a valid action into an unexplained failure.

## Lifecycle state machine

| State | Entry | Main play | Exit |
| --- | --- | --- | --- |
| Dormant | Event not fired | None | Valid host selected |
| Opening Shock | Leader murdered | Succession, emergency protection, crime scene | Investigation established |
| Baseline Investigation | Category active | Evidence, protection, intelligence, first capture opportunity | Full capture, Evolution I, host collapse, invalidation |
| Murder Cult | Evolution I | Infiltration, imitation, stronger protection and raids | Full capture, Evolution II, host collapse |
| International Network | Evolution II | Local cases, intelligence sharing, foreign cells | Global dismantling, Evolution III, inheritance path |
| Territorial Movement | Evolution III | Assassin State war, country routes, continued cell struggle | Movement defeat, Evolution IV, host conquest |
| Brotherhood System | Evolution IV | Foreign revolts, subjects, faction coordination | Movement defeat, Evolution V |
| World Collapse Readiness | Evolution V | Terminal preparation, elite units, global objectives | World of Anarchy activation or movement defeat |
| Terminal War | World of Anarchy active | Government dismantling and world resistance | Assassin victory, Assassin defeat, incompatible terminal resolution |
| Resolved | Capture, defeat, victory, invalidated setup | Aftermath only | No normal repeat firing |

## Opening sequence

1. The event selector saves the original host and performs a final transactional eligibility check.
2. The current leader is rechecked against the protected-character and safe-succession registry.
3. The successor or emergency institutional replacement is prepared before the murder is applied.
4. The current leader is removed through the character-safe Event 39 effect.
5. The verified successor takes office in the same transaction.
6. The opening event records the murdered office, successor, host, date, and Event 39 status.
7. The country receives a temporary succession crisis idea and the investigation category.
8. Initial Case Progress, Network Reach, witness safety, evidence integrity, and target protection are set from host conditions.
9. A restrained international news report announces the assassination.
10. The event log records Event 39 with the host actor and does not reveal future evolutions.

The opening must not leave a country without a leader, duplicate the successor, or remove a character that remains active in another roster.

## Baseline pacing

The first follow-up incident should not occur immediately. The country receives a preparation window. Baseline incidents use dynamic pacing influenced by Network Reach, protection coverage, current Case Progress, host intelligence capability, war state, institutional disruption, and recent incident history.

At baseline, the expected interval should normally allow the player to complete at least one serious investigative action before another murder can occur. Repeated murders become more likely only after concrete failures or Evolution I. A hard incident cooldown prevents multiple character losses in a few days.

## Baseline conclusions

### Complete capture

A final operation at sufficient Case Progress can capture or kill the original murderer and dismantle the core support circle. When no independent foreign cell, Assassin State, or surviving movement heir exists, Event 39 ends permanently. The country receives an institutional memory outcome, temporary recovery, and a bounded long-term counterintelligence benefit. The world receives a normal news event, not a super-event.

The public account remains incomplete. It confirms the operation and the end of the immediate crisis while leaving the murderer's full origin and motive unresolved.

### Partial capture

A final operation may capture a local leader or decoy while evidence proves that the movement is wider. Partial capture grants Case Progress, weakens the local cell, delays incidents, and may expose a foreign route. It does not falsely end the event.

### Failed operation

A failed operation must follow visible preparation gaps, compromised intelligence, missing protection, or a player-selected high-risk approach. It can kill or expose investigators, reduce Case Progress, raise Network Reach, trigger an escape incident, or accelerate an eligible evolution. Failure cannot silently delete a character outside the target pool.

### Host collapse before capture

If the original host ceases to exist before Evolution III, the event tries to rebind the original investigation and core network to the controller of the host capital or the most suitable successor state only when that country passes normal civilian and character gates. If no safe successor exists, the network enters a bounded fugitive state. It may seed foreign cells under Evolution II, but it cannot remove unprotected characters or create a country without a valid host.

## Event log and Event Details

Event Details must show the premise, Chaos level, type, Intelligence cluster membership, public evolution previews, and the World of Anarchy public terminal row. It must not show hidden target lists, exact murder chances, protected-character registries, preselected country tags, or secret inheritance logic.

The History row records the opening host and date. Evolution rows record real Evolution I through V milestones with actor where applicable. Baseline investigation phases do not masquerade as evolutions. The World of Anarchy row has its own persistent default-enabled toggle that does not disable Event 39 or sibling content.

## Permanent fire-once behavior

Natural Event 39 can fire only once. A successful capture, movement defeat, terminal victory, terminal defeat, or invalidated host transaction permanently closes the normal event. The Assassin Network manual scenario may create its own scoped run when no incompatible normal setup is active. It must not reset or falsify normal event history.

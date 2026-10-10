# 102 Serial Killer: core specification

## Design authority and reading order

The uploaded planning package attributes its core requirements to `102 - Serial Killer(2).md`: selected countries, four archetypes, three evolutions, investigation interface, civilian losses and separate national conclusions. That brief and the separate review companion were not included in this eight-file import. Preserve the substantive design while the parent records its acceptance basis. The import and documentation review authorize preservation and reconciliation, and do not authorize gameplay implementation or independently establish approval for the expanded design. The older catalog description records the previous idea and does not narrow this proposal.

All newly introduced route, action, outcome and asset labels in this package are **working labels, not final localisation**. The supplied event and archetype names retain their established identities. Evidence examples specify fictional case facts and the meaning of a choice. They are not draft event descriptions, option text or finished in-game wording.

Read this part for the crisis and its limits, [Part 2](102_serial_killer_spec_part_2_casebook.md) for twelve playable case families, [Part 3](102_serial_killer_spec_part_3_evolutions_and_connections.md) for regional spread, global organizations and crossovers, and [Part 4](102_serial_killer_spec_part_4_investigation_ai_and_aftermath.md) for presentation, cooperation, AI, Chaos and endings. The [coding](102_serial_killer_coding_prompt.md), [asset](102_serial_killer_asset_prompt.md), [achievement](102_serial_killer_achievement_prompt.md) and [goal](102_serial_killer_goal_prompt.md) prompts are future production inputs. Their imperative commands and references to a supplied source protocol do not initiate implementation during import. Current import evidence and per-document dispositions belong to the [review handoff](../../plans/102_serial_killer_plans/subagent_handoffs/102_import_review_2026-10-10.md) and [evidence record](../../plans/102_serial_killer_plans/102_import_evidence_2026-10-10.json).

## Catalog identity

| Field | Required design |
|---|---|
| Event ID | 102 |
| Event name | Serial Killer |
| Classification | Minor Fire-Once |
| Entry Chaos level | 1 |
| Catalog cluster | None |
| Initial host pool | Each currently valid major country and each currently valid player-controlled country |
| Initial culprit | One persistent person with one hidden archetype |
| Principal interaction | A sequence of evidence-based country events |

The metadata preserves the design attributed to the brief's Catalog entry and Core idea. At the 10 October 2026 import review, the authoritative workbook names row 102 `Serial killer`, marks it `Unavailable`, and leaves Type, Chaos and cluster blank. No `chaosx.nr102.*` implementation definition was found in the parent's targeted current-source check. These current facts do not erase the proposed classification, Chaos or cluster. Catalog status follows the [current events owner](../../../.agents/skills/chaos-redux-events/SKILL.md#event-catalog-status-contract), with `Playable` requiring explicit approval.

The proposed event is fire-once at campaign level. A failed investigation starts another case attempt within the same episode. It does not fire another Event 102 or replace the original person.

## The experience

The opening should feel like a small, intelligible emergency inside a much larger war game. A government receives a civilian murder report. A few facts disagree with the obvious explanation. The player follows those facts through successive choices, commits to a theory and eventually acts on a prediction. The reward for paying attention is an identifiable person stopped and an identifiable population spared further crimes.

Failure should change what the player understands. A plausible suspect can survive the first inquiry, then a witnessed movement, an authenticated document or a later scene disproves the theory. The next inquiry uses new facts. Its underlying offender is still the same person, with the same appetite, method of communicating or behavioral compulsion. The player learns how to reason about that person without learning an invariant sequence of buttons.

Escalation changes the problem in three specific ways. At 200 Chaos the original person's activity becomes more frequent, more severe and capable of crossing neighboring borders. At 400 Chaos real additional murderers and organized cells take the crisis beyond its original continent. At 600 Chaos an existing killer or cell can acquire a consequential connection to another active event. These are the three evolutions requested by the user, not ordinary investigation stages.

The emotional center remains the civilian case. Reports establish that victims had ordinary lives and that errors have consequences. Their purpose is to explain evidence, disrupted communities and the government's response. Graphic descriptions, celebrity criminals and spectacular casualty totals do not carry the design.

## Selecting the first country

Build a current candidate pool when the event is eligible to manifest. A country qualifies if it is currently a major or is controlled by a human player, uses an appropriate functioning civilian society, and has at least one usable crime-scene state under its actual administration. A country that is both a major and player-controlled receives one entry. Select uniformly by eligible country, so the two routes into eligibility do not give a human major two tickets.

An AI major, human major and human minor can each be the initial host. An ordinary AI minor cannot enter that first pool. It becomes eligible as a later victim when the original trail or an independently created threat actually reaches it. Human eligibility follows current control, including a multiplayer participant who controls a minor. The game must not silently substitute the player's country for an AI target.

The country needs a meaningful place for a civilian crime. A government without accessible civilian territory is not a suitable opening host. A purely nonhuman actor cannot qualify merely because it occupies a tag in the country list. An unusual human country is not automatically excluded. Use the project's current country classifiers, then the event's specific civilian and scene requirements.

Select a plausible populated state inside the chosen administration. State population, transport access and the archetype's opportunities influence scene selection, but no clue may depend on the player knowing an unshown map attribute. A railway case supplies its relevant timetable and candidate connections. A harbor case establishes that the locations really have usable maritime access. A small country with one usable state can support a complete domestic route by using separate fictional civilian places within that state.

The actor's identity is committed with the first real incident. Selection alone does not spend the campaign's fire-once opportunity or create a successful event record. If the selected country or state becomes invalid before the first incident commits, choose another still-valid target through the same entry contract. If the pool is empty, the entry returns the normal failure or retry disposition without inventing a victim or consuming the event.

Once the first incident is committed, later annexation, capitulation, controller changes and player hot-joining use the existing episode. They never create a replacement original killer merely to recover a lost country pointer.

### Civilian ownership and investigation authority

The physical state is the location of a crime. Its lawful owner and current controller can differ. The controller that can actually investigate the scene receives the local inquiry, while the shared casualty contract determines the recorded civilian country attribution. Both facts remain in the incident history. A report must not imply that the lawful owner administered a scene it could not reach.

Crime-scene validation occurs again when an incident commits. If the front moves, the case is transferred, delayed or given a newly supported scene according to the real actor's location. Administrative disruption is evidence context. It does not let the same scheduled crime kill civilians in both the old and new country.

## One original person

The original has a persistent identity, a selected archetype, a current location or travel state, a case history and a final disposition. Its visible name or suspect label can change when an alias is exposed. Its underlying identity cannot. An unknown person in two reports is one actor only when the evidence and travel history support that relationship.

The initial archetype draw gives all four archetypes an ordinary chance to appear. Country conditions select compatible case families and locations after the draw. They must not make the Gourmet exclusive to Cannibalism countries, the Ritualist exclusive to supernatural campaigns or the Cipher Killer exclusive to powerful countries. Every archetype supports a grounded domestic case at every Chaos level.

The actor occupies one scene, one refuge or one travel leg at a time. It can leave evidence in several countries over time. Reports about earlier crimes can arrive together, but the underlying incident dates and locations must describe a possible sequence. A global news summary does not authorize simultaneous original-killer attacks worldwide.

Archetypes supply behavioral continuity rather than supernatural powers:

| Archetype | Persistent organizing behavior | Evidence the player learns to examine | Ordinary variation |
|---|---|---|---|
| The Gourmet | Manipulation, educated access and deliberate arrangement around food, anatomy, medicine or art | Access records, provenance, professional routines and differences between display and actual handling | Kitchens, collections, medical stores and private gatherings |
| The Cipher Killer | Attempts to control the inquiry through correspondence and manufactured patterns | Document authenticity, ordering rules, dates, source editions and consistency between message and scene | Newspapers, mailed material, administrative records and diagrams |
| The Hunter | Repeated choices shaped by movement and ordinary civilian routines | Arrival and departure windows, route direction, work changes and evidence of waiting | Roads, railways, workplaces and transport interchanges |
| The Ritualist | An intentional sequence of objects, placements or recurring acts | Which object moved, which sequence is physical, which symbol is borrowed and who can prepare a scene | Civil ceremonies, stored props, workshops and repeated arrangements |

Archetype recognition helps the player ask the right questions. It is never sufficient evidence to arrest someone. A correct guess that the killer is a Gourmet cannot substitute for establishing the responsible person and a valid stopping operation.

## A complete inquiry

Every individual-killer family in Part 2 contains four decisive deductions and a permanent stopping resolution. The four deductions need not all concern a suspect. They can establish authenticity, order, movement, access or the meaning of a repeated act. Together they identify a coherent culprit and the place or action that will stop that person.

The presentation alternates between fact and decision. A scene report presents a bounded set of observations. A later comparison can add an authenticated fact. The player then selects the conclusion supported by the available material. The case recap includes all facts needed for the current choice, so solving the puzzle does not require memorizing a popup that disappeared several real-world hours earlier.

Correct deductions create a continuous proof for the current case. The fourth correct deduction establishes the stopping plan. The final confrontation implements that plan when its real targets remain valid. It does not apply an undisclosed arrest roll after the player has already completed the required reasoning.

A wrong deduction can provisionally direct investigators toward a plausible explanation. Subsequent evidence then exposes the error. The game explains which observation no longer fits the accepted theory. The current chain collapses and a fresh, solvable route begins. The outcome does not silently mark a choice wrong and jump back to an unchanged first question.

Basic facts already established about the original remain known. A failed attempt cannot make authorities forget a fingerprint comparison, a verified absence, a proven forgery or the identity of someone already exonerated. What resets is the unproved chain connecting the latest incidents to a valid confrontation. New route facts can change the correct inference while preserving the original's behavioral identity.

### Fairness rules

Each decisive step has one supported inference under the exact facts presented at that step. The alternatives can be attractive, but the decisive distinction must already be available. A later contradiction explains a failure. It cannot retroactively supply the only information that would have made the earlier question answerable.

Whenever the case needs a special rule, it supplies the rule. A code explains its indexing convention. A timetable states the relevant day and departure. A comparison states whether specimens are genuinely comparable. A testimony states its reliability limits. The player does not need external cryptography, forensic or geographical knowledge.

Uncertainty can be the correct subject of a deduction. A clue may prove that the familiar suspect is unsupported without proving another person's identity. In that situation the correct action follows the verified lead. The case must not force an arrest from insufficient facts.

Fabricated evidence has a visible, checkable flaw. The case distinguishes a forged message, an honest witness error and a real clue interpreted incorrectly. These are different kinds of reasoning. Rare fabrications do not create a universal rule that every suspicious document is false.

Difficulty comes from comparing facts, following chronology and separating correlated events. It does not come from tiny text, inaccessible colors, ambiguous translation, pixel inspection or a hidden fact available only to the AI.

## Time, murder opportunities and pressure

The offender has an opportunity schedule. Investigations have their own sequence of reports and decisions. Closing one popup cannot make several days pass or create another crime by itself. Deferred or replayed interfaces also cannot accelerate the offender's opportunity schedule.

The following are design tuning anchors. They establish the intended scale and require adjustment through the later probability and campaign review. They are not claims about existing repository behavior.

| Threat and context | Ordinary incident size | Typical interval between real opportunities | Exceptional shape |
|---|---|---|---|
| Original or independent killer in baseline conditions | 1 to 5 civilians | Roughly 21 to 40 days | A prepared group incident of 6 to 10 can occur with an evidenced venue and opportunity |
| Original after Escalating Murders | 3 to 12 civilians | Roughly 6 to 14 days | A prepared group incident of 13 to 24 requires a suitable location and a concrete failure or opening |
| Independent killer after global spread | Its own archetype and current pressure determine the band | Usually 10 to 24 days | It does not automatically inherit every failure accumulated by the original |
| Organized cult operation | 6 to 24 civilians for a small participating cohort | Usually 18 to 36 days per available cell operation | Up to 40 requires several actual participating offenders and a single evidenced operation |

The large difference between baseline and Evolution I is deliberate. A slow domestic series becomes an urgent recurring threat. Higher brutality is expressed through scene consequences, intimidated witnesses, groups of missing civilians and disrupted places. Descriptions remain non-graphic.

Archetype shapes the schedule within these bands. The Gourmet needs access and preparation, so interruptions to those opportunities matter. The Cipher Killer's authenticated communications can establish a more regular sequence. The Hunter follows actual transport or work opportunities. The Ritualist's sequence provides forecastable occasions, but its calendar is a supplied case fact rather than a universal occult clock.

Time free increases confidence and access gradually. A failed inquiry can create an additional opening or move the next opportunity earlier within the allowed interval. Both effects saturate. Years at large and many failures cannot multiply one person's victims without bound. At the same time, a stable, cooperative administration that protects the predicted venue can reduce losses or deny that specific opportunity.

Population sets a physical ceiling and influences suitable scene selection. It is not a flat percentage casualty formula. A large state offers more plausible places and movement cover. It does not turn an ordinary serial killer into a mass-disaster mechanism. An empty or protected state cannot provide an invented minimum victim count.

War, occupation, damaged administration, displacement and broken transport alter both opportunity and investigation. War can conceal movement while also blocking a route. A destroyed rail connection can invalidate the Hunter's expected journey. These conditions create visible case changes instead of a single universal war multiplier.

### Consequences beyond the casualty count

Exact civilian losses matter even when they are small relative to wartime population. The broader cost is temporary disruption tied to the affected places and authorities. A substantiated domestic series can create a small national stability pressure while the local case is unresolved. Escalation can intensify that pressure and interrupt civilian work or transport in the selected state.

Use standard stability, temporary modifiers and the specific action costs described in Part 4. Do not invent a new permanent public investigation score. The player should see why a place is disrupted and what result will remove or reduce the disruption.

The intended ordinary national stability pressure is modest, around one or two percentage points at baseline. Sustained escalated activity can reach roughly three or four. Several threats share a national ceiling of about six rather than stacking one full penalty per killer, case attempt and cult. These are temporary active-case pressures, with strength recalculated from real local threats. They are not repeatable permanent stability deductions for every murder popup.

Local work disruption normally stays near a small temporary output or repair penalty. A prepared cult operation can be worse at its actual location for a short time. The specific footprint must reflect the venue and participating offenders. A staged railway clue does not justify destroying the country's rail network. Fear cannot quietly create military losses, divisions or political assassinations.

An innocent suspect detained after an unsupported theory is released or cleared when the contradiction arrives. A modest, bounded administrative or trust cost may follow the failure. The false lead never grants an achievement, removes the real killer or kills an unrelated named character.

## Every victim corresponds to one physical loss

An Event 102 incident names its real offender or participating group, occurrence time, physical state, local authority and source of attribution. The requested loss is limited to that operation's size and the civilians actually available in that state. The population transaction occurs once. Reports, local history and the normal enabled Deaths accounting use the measured loss from that transaction.

When no civilian population actually falls, the incident cannot report a positive completed murder count. It may become a prevented attack, a discovered intention or an invalidated operation according to the facts. If fewer civilians are physically lost than requested, every downstream total uses the smaller actual amount.

The project's shared Deaths setting continues to govern its accounting display and ledger. Physical losses still follow the population contract when that optional accounting is disabled. Event 102 must not bypass that owner setting or backfill the same physical loss when the setting changes later. The implementation dependency and historical discrepancy found in the pinned repository are documented in the [coding prompt](102_serial_killer_coding_prompt.md#exact-civilian-loss-is-an-owner-dependency).

The same ownership rule applies at every scale. A copycat incident and a cult operation are not two entries for the same victims. A Cannibalism victim encountered as evidence remains a Cannibalism victim. A political assassination remains owned by Murder Mystery. Ordinary outbreak and disaster deaths remain with their source. An independently caused Event 102 killing during those crises is a distinct incident with its own physical loss.

## Permanent stopping and meaningful local endings

An individual inquiry ends by stopping its identified person. The archetype-specific resolution can involve an arrest, an intercepted journey, an exposed refuge, a prevented planned act or a confrontation in which the culprit dies. The result is permanent for that actor. Capturing one suspect label and then reviving the same original under another alias is not a valid retry.

Ordinary arrest is the default. A lethal confrontation needs evidence and a credible immediate situation. It is an outcome direction, not an additional random penalty imposed on a correct investigation. Named politicians, generals and ministers do not become routine suspects or collateral victims.

The country that completes the operation receives its own conclusion. Countries that supplied authenticated evidence receive an appropriate contribution record. The killer's personally attributed future opportunities are cancelled everywhere. Other countries do not keep receiving murders from a culprit already stopped abroad.

Before independent global threats exist, stopping the original can close the active episode. Rising Chaos after that closure does not unlock new killers, revive the original or produce a delayed global cult from nothing.

After independent threats exist, their ownership matters. Stopping the original leaves an already active independent killer intact. Dismantling a cell removes the support and violence that the cell actually controlled. A murderer who survives independently requires its own conclusion. Arresting a coordinator does not establish that every armed member has been contained.

Local safety and global closure are separate outcomes. A country can conclude that the known original has left, finish the local evidence transfer and remove pressure caused solely by that person's local presence. It records the risk of return. If the actor genuinely returns, new local incidents can reopen the local inquiry. A foreign failure does not itself generate another domestic crime.

The wider episode closes when every real active killer and every dangerous surviving cell component has been permanently stopped or genuinely contained. A disabled interface, an empty current popup queue, a lost country pointer or a quiet month is not evidence of closure. Historical incidents, established facts, credited cooperation and past victims remain after active work ends.

## What carries into the next parts

Part 2 makes the reasoning playable through twelve case families and changed-fact retries. Part 3 specifies how one original becomes a regional pursuit, how a bounded set of real independent threats becomes global, and how source-owned crossovers alter a case. Part 4 ensures that these cases remain readable, fair to AI, cooperative in multiplayer and capable of ending cleanly.

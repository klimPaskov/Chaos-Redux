# Mistresses: screening, uncertain evidence, and individual consequences

## The person at the centre of the decision

Screening begins with an adult individual whose place in ordinary life is intelligible.
A candidate might live with a soldier, work near a railway depot, introduce acquaintances to a minister, or maintain a household that neighbours value.
The portrait and short personal description should create a person the player can recognise, while the evidence describes conduct, relationships, and observations that the government can actually investigate.
Beauty, composure, a remarkably convenient history, or an apparently perfect relationship cannot establish alien identity.

The difficult choice is whether further investigation is worth its time and opportunity cost, whether to spare someone despite unresolved suspicion, and whether the available evidence justifies an irreversible purge.
Each choice must remain useful in some circumstances.
A strong containment campaign combines patient investigation, selective interventions, protected witnesses, and institutional repair.
It can contain infiltration without indiscriminate killing, while an infiltrator who is repeatedly spared can continue to help an existing network.

All new terms used for methods, states, missions, and interface components in this chapter are working design labels, not final localisation.
The numerical tables are launch tuning proposals whose balance must be checked against the implemented system.
They are not measurements of a real population, historical claims, or claims of completed engine validation.

## A stable identity inside a changing campaign

Every case has a permanent case identity and a separate permanent person identity.
The person owns the saved truth, underlying evidence, age eligibility, household relationships, local network membership, and any actual role within that network.
The case records what the investigating country has learned, the methods it has used, its costs, and its decisions.
Several countries can encounter the same person through a legitimate cross-border connection, but they cannot remove that person repeatedly or each claim the same disruption.

Truth is established when the underlying person is admitted to the finite event population and cannot change because a player opens a card, changes a filter, reloads, or chooses another investigation method.
The underlying evidence packets are also established then.
Later events may add new observations of new conduct, with their own dates and provenance, but they cannot rewrite an earlier packet.

Saved randomness prevents rerolling a case. It cannot make a player forget a completed outcome after returning to a pre-action save. Truthful post-purge population and Deaths accounting can therefore reveal information to a player who deliberately reloads an earlier state. The design retains correct accounting and does not claim complete prevention of that external replay strategy. Ordinary active play still receives no pre-action truth oracle.
An innocent person who later disappears during Replacement Wave remains an innocent person in the original case.
A replacement is a genuinely different entity with a new identity and an explicit relationship to the older record, handled through `119_mistresses_spec_part_5_evolutions.md`.

Human-visible case publication freezes the portrait, fictional alias, description, and relevant role together.
The UI never draws a new truth value or substitutes another face after publication.
AI-only investigative records can exist without a portrait allocation, since their reasoning uses the same evidence fields and does not inspect images.
When such a record first becomes visible to a human, its already established truth and evidence are retained and its visual identity is published once.
This separation saves portrait capacity without giving AI countries a different truth system.

### Portrait pool and the long campaign

The production target is 1,250 distinct adult identity portraits, with a release floor of 1,000.
At least 80 percent of the shipped pool must consist of actual internet-sourced photographs cleared for the intended fictional and sensitive use.
At the launch target, this means at least 1,000 photographs and at most 250 fictional generated identities.
These are acquisition and acceptance requirements, not a claim that the images have already been sourced.
The complete production and rights workflow belongs to `119_mistresses_spec_part_11_assets_audio.md`.

The image sampler cannot read alien truth, case outcome, investigation reliability, protected characteristics, or whether an image was sourced or generated.
Photographic style, scan quality, file order, crop dimensions, source collection, and generated status must not become predictive shortcuts.
An image that accompanies an infiltrator in one campaign can accompany an innocent person in another.
Fictional aliases and descriptions vary independently within compatible adult life histories.
The real subject's identity is not copied into an allegation or fictional criminal biography.

Use a deterministic no-repeat deck for newly presented identities in each human observer's campaign view.
An identity already published to another observer retains its existing global portrait assignment when shared.
Sharing therefore does not change the person or consume a second portrait allocation.
The observing country's deck marks that portrait as encountered and resolves future allocation conflicts against the authoritative person assignment.
All globally published active identities reserve their photographs until closure, so sharing a case cannot create two simultaneously actionable local people with the same photograph.

After the observer exhausts a full deck, a new deterministic deck cycle may reuse images belonging to older, closed identities.
Exclude every globally published active identity and the latest 250 archived identities encountered by that observer from fresh allocation.
An old archive record retains its original image and immutable identity even when a later, different fictional person uses that photograph.
The archive identifies both people through their separate case identities and dates.
The interface help explains the possibility of image reuse in a long campaign without presenting recognition as evidence.
No old evidence, verdict, network membership, or truth follows a photograph into the next cycle.

The allocation process must reserve an eligible image before publishing a new visible card.
It must never silently replace an active image to solve a collision.
The simultaneous human-visible active-case ceiling across the session is the installed pool size minus the 250-image recent-archive reserve.
This gives 1,000 active visible records at the production target and 750 at the release floor, far above the normal national caseload.
An exceptional session reaching that ceiling retains new leads in the finite admission queue until an active case closes.
It continues all existing cases, AI work, and operational counterplay, and never publishes a portraitless substitute.
Fair admission rotates between waiting countries and cannot prioritise hidden guilt.
The implementation must demonstrate deck cycling, shared-observer collisions, and release of the oldest archive exclusion at this exact capacity boundary.

Reopening an older case must pass the same portrait reservation gate as first publication.
If its immutable image has since been assigned to a different active person, retain the old identity, portrait, evidence, and truth in the readable archive, and queue its actionable dossier until that reservation releases.
Do not swap either face, close the newer case automatically, or publish two simultaneously actionable identities with the same portrait.
New dated observations can still attach to the older record, and urgent source protection, institutional audit, and macro-containment work can act on the actual source or location while it waits.
Those operations retain their ordinary evidence limits and cannot become a concealed replacement for a blocked individual purge.
The old case's investigate, spare, and purge controls become available only after its portrait is reserved again.
Waiting creates no fee, new method draw, or artificial case deadline, and reopened urgent cases receive admission priority based on observed danger rather than hidden truth.

## Who enters screening

Screening examines a selected caseload.
It does not present a census of women or a random percentage of the country's population.
Referrals arise from finite local incidents, independent requests for help, exposed network links, and specific access to sensitive institutions.
An innocent candidate can have several suspicious circumstances, and an infiltrator can have a mundane description and no striking visual trait.

The admission system uses the following selected-case priors in ordinary launch scenarios.
These priors are conditional on the sampling channel and are never displayed as national infiltration prevalence.

| Admission channel, working label | Alien share in the admitted case cohort | Why the case is present | Control against abuse |
| --- | ---: | --- | --- |
| Broad voluntary referral | 10% | An adult asks for help, a household requests mediation, or an ordinary check finds an ambiguity | One person record, no reward for flooding the queue with weak referrals |
| Ordinary incident referral | 20% | A dated local incident connects the person to a consequential anomaly or disputed activity | The incident must exist before admission and cannot be generated by reopening the UI |
| Linked-cell referral | 35% | A discovered, existing network connection creates a reason to examine this individual | A finite unconsumed edge must support the referral, and an association is not guilt |

The hidden network simulation can change the mix of channels and the supply of eligible candidates.
It should normally change which cases arrive rather than make a finished portrait card secretly more or less guilty.
The table defines launch targets for standard test cohorts with eligible candidates of both truth states.
Actual admission must select from the finite people who exist, and cannot create an infiltrator to satisfy a target percentage.
A clean country can receive ordinary human referrals with no alien case at all.
An exhausted or disrupted cell likewise cannot replenish its candidate population through the screening interface.
Replacement Wave can create a different cohort with separately documented sampling, but existing cases retain their original truth.
Any additional cohort prior belongs in the same central tuning family and in the blind evaluation matrix.

Admission consumes a finite lead, not the lead's person or any population.
The same lead cannot generate another independent chance of finding an alien after the player spares its subject.
Two contradictory accusations about one person become evidence on that person's existing record.
The national active caseload is normally five cases, expanding to ten at Investigative Reach 50.
An additional bounded queue retains credible unadmitted leads in dated order.
The queue cannot manufacture population, new people, or fresh evidence when the player clears a card.

A short queue should remain strategically legible.
Prioritise a threatened witness or a presently used sensitive access point, then a newly exposed link, then older ordinary referrals.
Do not order cards by hidden guilt, hidden coordinator rank, or a probability available only to the simulation.
The country can still run protective and institutional missions when it has no eligible case.

## Evidence that supports judgement without solving the person

Each evidence item contains an observation, its date, its source group, how it was obtained, and what uncertainty remains.
Evidence can be adverse, reassuring, or inconclusive.
The public presentation uses those meanings without displaying a single computed guilt meter.
The player's work is to compare observations and assess whether several apparently supporting statements actually come from one source.

The following clean-source likelihoods give the implementation a quantitative starting point.
Each row totals 100 percent within each truth group.
An adverse result means the method found something relevant to the case, not a definitive test of species.

| Method family, working label | Adverse if alien | Reassuring if alien | Inconclusive if alien | Adverse if human | Reassuring if human | Inconclusive if human |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Independent history check | 60% | 20% | 20% | 25% | 45% | 30% |
| Material or clinical verification | 70% | 15% | 15% | 20% | 55% | 25% |
| Observed contact trace | 65% | 15% | 20% | 25% | 45% | 30% |

History checks examine continuity between independently obtained observations, not whether a name sounds foreign or a family follows a particular religion.
Material verification concerns a specific anomalous observation and the reliability of the sample.
It must not frame pregnancy, infertility, disability, illness, sexual history, or refusal of an invasive procedure as proof of alien identity.
Contact tracing investigates consequential activity and access, not ordinary affection or association alone.
All methods have innocent explanations and failed collection states.

Portrait-only appearance has a likelihood ratio of 1 in the launch model.
An unusually perfect account in the biography may occur in 25 percent of alien records and 20 percent of human records.
Its positive likelihood ratio is therefore 1.25.
This is the maximum combined contribution of beauty and perfection cues.
Several flattering adjectives, a highly polished photograph, and an implausibly convenient biography cannot multiply into independent evidence.
No protected identity trait is permitted as a truth-bearing clue.

### Dependence between reports

A witness statement repeated by a neighbour, an introduction list, and a clerk's account can all describe the same underlying source.
The evidence record must show their common provenance once that relationship is known.
Before it is known, the record can describe uncertain independence, but it must never promise independent confirmation without support.

For the launch model, a history check and a contact trace using the same source group share the first family packet in 80 percent of cases.
In the remaining 20 percent, the contact method reads its separately saved contact packet.
For example, after an adverse history result, another adverse report from that same group is expected with probability 93 percent for an alien and 85 percent for a human under the clean-source table.
That second report adds much less information than multiplying 60/25 by 65/25.
These are computed results from the dependency rule, not additional authored tuning values.

Material verification is a separate family only when collection and assessment have distinct provenance.
Two analyses of the same sample share a packet.
A foreign laboratory repeating a compromised domestic report without obtaining independent material shares the same defect.
The audit receipt can establish genuine independence, but a new icon or another country name cannot do so.

### Worked uncertainty examples

For a 20 percent ordinary-referral prior, one adverse clean history result changes the mathematical posterior to 37.5 percent.
An adverse independent material result as well changes it to approximately 67.74 percent.
A perfect biography alone changes the same starting prior to approximately 23.81 percent.
The two independent adverse results give approximately 81.89 percent for the 35 percent linked-cell prior and approximately 48.28 percent for the 10 percent broad-referral prior.

Those examples show why referral context and provenance matter.
They are internal balance calculations, not numbers that the interface promises to the player.
Compromised sources lower their practical reliability, and the final implementation must calculate its complete mixture rather than copying these clean-source examples as actual player certainty.
There is no universal two-click test that reveals every innocent and every infiltrator.

## Investigating a case

The player chooses a specific available method through the principal investigation action.
A preview explains which question it can examine, its source family, its full price, its expected completion interval, and the limits of the method.
The selected method occupies a national investigation slot and reads its saved packet at completion.
Changing the selection, closing the window, or reopening the method list does not draw another packet.

Each person normally permits two completed method families.
Only one method can be active for that person at a time, and legitimate foreign assistance shares the same authoritative person record and family budget.
A country can learn only findings it obtained or that were actually shared, even though the underlying packet and method-use record are global.
An attempt lost through genuine authority loss can return an unconsumed method when no evidence was delivered, while spent supplies remain governed by the transaction's cancellation terms.
A source-remedy investigation can replace one contested packet once for that person after a recorded independent audit finding supports a collection concern.
Eligibility uses that observable finding and a genuinely separate collection path, not the source's hidden integrity bit.
A false concern about a clean source permits the same bounded replacement workflow, so an enabled button cannot reveal whether the accusation was correct.
The original report remains in the archive alongside the later finding, and the replacement reads its own saved packet.
It cannot act as a third ordinary investigation or a way to erase an inconvenient honest result.
New conduct can justify one later reopening, but reopening preserves all previous evidence and method use.
Spare or purge during an active investigation atomically cancels that pending completion, releases its staff slot, retains already delivered evidence, and follows the paid contract's stated rule for spent supplies.
The cancelled method cannot later deliver a reward, debit again, or restore a removed person.

| Investigation path, working label | Launch completion interval | Main tradeoff | Availability |
| --- | --- | --- | --- |
| Local interviews and history visit | 30 to 45 days | Uses scarce staff time, with limited independence if local sources are shared | Available to the weakest affected host without an equipment payment |
| Supplied verification team | 15 to 25 days | Consumes support equipment and, for travel, fuel | Requires an accessible named location and a coherent quote |
| Protected contact trace | 20 to 35 days | Consumes support equipment and command attention while following a specific connection | Requires a recorded contact and safe access to the observation area |

These short case actions are asynchronous investigations, not a wall of native timed missions.
The country's larger operational missions usually last 90 days or longer and appear in `119_mistresses_spec_part_4_decisions_missions.md`.
Case completion intervals lengthen with lost access, dispersed locations, and inadequate staff.
High Reach reduces delay and supports more parallel work, but it does not remove honest uncertainty from the evidence table.

Launch slot capacity is one at Reach below 25, two from 25, and three from 50.
Reach 75 improves national coordination and recovery from obstruction rather than adding more simultaneous case buttons.
The strongest host therefore gains throughput without turning screening into an unbounded list.
No reserve is drained when a method is unavailable, the target is stale, a slot has already been taken, or the selected quote has changed.

## When the investigators are being manipulated

Compromised investigations are a playable problem with observable ways to respond.
They must not be an arbitrary rule that invalidates evidence whenever the player begins to succeed.
At case creation, mark the relevant source groups with a saved integrity condition.
The ordinary compromised-source launch chance is 15 percent.
It rises to 25 percent where a recorded infiltrator holds protective institutional access or where Public Confidence is below 25 and witnesses have reason to avoid investigators.
An effective independent audit can reduce the chance for newly established sources to 5 percent for its protected service interval.
It cannot cleanse evidence retrospectively without a replacement investigation.

For a compromised source in the launch test model, the report distribution becomes 25 percent adverse, 55 percent reassuring, and 20 percent inconclusive when its subject is an infiltrator.
For a human subject, it becomes 55 percent adverse, 25 percent reassuring, and 20 percent inconclusive.
The same source-group packet is reused by reports that depend on it.
This provides concrete false reassurance and false accusation risks without making either result certain.

Counterplay has three distinct purposes.
Protecting witnesses keeps a source reachable.
Auditing the collection chain can reveal that two reports share a source or that the collection was altered.
An independent replacement investigation obtains a different saved packet through a different validated source group.
The player sees the recorded concern and its relevance, while any stronger claim about manipulation or its responsible actor requires evidence that actually establishes it.

The audit mission selects a bounded, disclosed set of existing source groups.
It reveals a real defect with a launch sensitivity of 80 percent and raises an erroneous concern about a clean source with a launch rate of 10 percent.
An erroneous concern remains a reason to seek independent verification, not an automatic exoneration.
Audit failure or inconclusiveness cannot be rerolled on the same group until new conduct creates a new source record.
The audit's result is saved and shared between cases that use that group.

## Investigate, spare, and purge

### Investigation outcomes

Investigation spends time and any quoted resources to add evidence.
It can expose a source problem or an existing link without removing the person.
A case closes only when the player resolves it, the person becomes unavailable through an independent world event, or the case reaches a documented administrative expiry.
There is no automatic guilty verdict when a timer ends.
An expiring unresolved case becomes inactive without coercion, retains its evidence, and can reopen only through the bounded new-conduct rule.

### Sparing the person

Sparing ends the current coercive response and releases any temporary restriction attached to the case.
It has no new Political Power, Command Power, or equipment charge.
An innocent person can return to ordinary life and participate in witness or restitution outcomes without granting an instant truth-revealing confidence reward.
An alien remains alive and can continue its actual role if the surrounding network still functions.
Its return to activity uses the existing network schedule and resources.
Sparing does not create new infiltration, free equipment, a new person, or an immediate alien success grant.

A government can openly choose protective handling of uncertain cases.
Public Confidence improvements come from visible, completed protection and restitution work, not a hidden test that rewards the player only when the spared person was human.
The player learns whether an earlier decision was mistaken through later evidence or consequences, and some uncertainty can remain permanently.

### Purging the person

Purge is a deliberate lethal removal of the identified adult, with an explicit consequence preview and a separate confirmation.
Cancellation is the first, harmless confirmation option and is also the timeout outcome.
The final click must still refer to the same person, case, country authority, and quote.
A pending confirmation cannot silently retarget another portrait after selection changes.

Each country has one coercive-handling slot, shared by the human and AI policies.
A successful purge commitment reserves it for five elapsed days, covering the actual removal and its immediate administrative handling.
The lethal effect occurs once at commitment, while another purge cannot commit until the slot returns.
This finite per-action reservation is shown with the quote and does not become a third persistent public meter.
It survives a responsible host's authority transition through the same receipt, and a rejected or cancelled confirmation starts no reservation.
Investigation and nonlethal operational work remain available through their separate ordinary capacity.

Every purge has an immediate nominal Public Confidence loss of 5 as the visible consequence of exceptional coercion, regardless of hidden truth.
The actual loss is the smaller of 5 and current Confidence, and is previewed exactly.
Confidence is never driven below zero and its depletion does not prevent an otherwise valid removal.
The act consumes its quoted operational resources and permanently retires the person.
An accurate removal changes only that person's real network role and incident links.
An innocent removal produces one actual civilian death and no alien-disruption credit.
An alien removal consumes one adult from the actual alien cohort and removes no human population.
Shared human Deaths accounting receives only the measured human loss, while the private alien ledger receives only the measured alien loss.
It never converts one portrait into thousands of fictional casualties.

Every purge schedules one bounded post-action review of the actual person's available household and institutional evidence over 30 to 90 days.
This review is automatic and reads a saved packet, so refusing to start an optional audit cannot suppress accountability.
The launch review establishes a wrongful removal in 80 percent of human cases and remains inconclusive in the rest.
An alien case can produce disputed claims, but this factual review cannot publish a proven human identity without a valid supporting record.
Any lack of access preserves a pending review for the responsible successor instead of deleting it.
If independently established later evidence demonstrates a wrongful purge, apply a further Confidence loss of 15 and a serious local disruption lasting 60 days.
The launch consequence begins as a 5 percentage-point national stability penalty.
Each additional established wrongful case adds five points to the same crisis, to a ceiling of 25 points, and renews its 60-day minimum consequence interval.
Represent this through one existing host crisis modifier rather than an unlimited pile of national spirits.
The owning core may use a mechanically equivalent local consequence where the inspected state system supports it, but cannot silently discard the cumulative burden.
The affected person's actual surviving household source group also withdraws from new voluntary collection until redress or an independently documented recovery.
It retains its old evidence and does not draw another corruption result.
This loss of real cooperation can make later source protection and investigations harder even after the national modifier reaches its ceiling.
After five independently established wrongful deaths within 90 days, the response enters a national accountability crisis with a 10-point additional Confidence loss and an available restitution mission.
This threshold is an observable history outcome and cannot be triggered twice for the same five deaths.
The unrest and lost cooperation still apply when Confidence is already zero.
The policy comparison must reject a tuning set in which exhausting Confidence turns further indiscriminate killing into the efficient response.

The certainty of guilt is not revealed automatically by a purge animation, portrait colour, generic result icon, or immediate changes in the two public values.
The actual post-action population and shared Deaths totals remain truthful, even if a very attentive player can infer something from their change after an irreversible act.
That legitimate consequence is never exposed in the pre-action quote, preview, enabled state, or target selection, and it cannot be disguised by adding a false human death for an alien.
Later vindication requires actual evidence and can restore 5 Confidence once for the incident through a public finding.
Vindication does not refund equipment or reverse the coercion's other consequences.
Unproved cases remain unproved in the archive.

## From one removal to a damaged network

A useful screening result changes the finite network that created the referral.
An ordinary infiltrator's successful removal lowers the owning state's hidden cell-presence score by 5.
A verified pivotal coordinator lowers it by 10.
The person is deleted from active network membership and its incident edges are removed once.
Only a person who actually held institutional access can reduce that state's hidden access score, by 5 for an ordinary access holder or 10 for an elite coordinator.
The scores stop at zero and represent network reach, not a percentage of residents.

Role verification comes from existing evidence and links.
A convenient portrait cannot be promoted to coordinator status to increase the reward.
If two case records refer to the same person, the second resolution reports the person's current unavailability and grants no additional disruption.
If two removals sever the same connection, only its first actual deletion counts.

The next bounded network update recomputes operations from surviving people, links, access, and resources.
A cell may lose a route, fail to protect an introduction, or fall below its capture-readiness conditions.
This can weaken the opening force and territory produced by The Unveiling through `119_mistresses_spec_part_2_networks_population.md` and `119_mistresses_spec_part_5_evolutions.md`.
The case itself never transfers a whole state or subtracts a cohort's population.

Exposing a coordinator can publish up to five existing, previously unknown leads.
It cannot create five guaranteed aliens or duplicate an already consumed lead.
The player chooses which leads merit scarce follow-up work.
If the cell has no surviving dependent links, the removal can finish its local disruption objective.
The objective's reward is attached to the real cell outcome and its receipt, which prevents farming that reward by reopening old cases.

## AI judgement and equal information

AI countries use the same saved evidence packets, source-group relationships, method limits, payment gates, delays, and finite disruption receipts as a human host.
Their policy can evaluate an internal evidence estimate, but that estimate must use only information available to the acting country.
The AI cannot read true person identity, hidden network rank, an unobserved compromised-source flag, or the unrevealed transformation state.

Ordinary AI prioritises an endangered source, a corroborated sensitive-access case, and a case whose unused independent method could change the resolution.
It spares weak cases when further work is unlikely to justify the cost.
Its launch purge threshold is an evidence estimate of 70 percent under ordinary conditions and 65 percent during a visible immediate access crisis.
An uncertain civilian case also needs two adverse method families with independently supported provenance.
A perfect biography cannot substitute for that corroboration.
A threshold crossing is necessary, not sufficient.
The AI also needs lawful acting authority, a valid individual target, affordable costs, and room in its crisis budget.
Visible violent activity handled as ordinary combat is not a shortcut for reclassifying an uncertain civilian.

These thresholds are reachable under the complete uncertain-source model without strengthening the evidence to fit an arbitrary policy number.
With independent source-group integrity draws and a 15 percent compromise chance, adverse material and contact results in a linked referral produce an approximate 72.956 percent posterior before any biography cue.
The corresponding posterior is approximately 79.950 percent for newly protected sources with a five percent compromise chance, and 65.061 percent at a 25 percent compromise chance.
An ordinary 20 percent referral with the same pair at 15 percent compromise reaches only approximately 55.604 percent.
Many such cases should therefore be spared or addressed through institutional containment rather than forced into a lethal conclusion.
These are computed model examples, not public guilt scores.

For that fixed independent method pair, human joint-adverse rates are approximately 5.764, 7.449, and 9.344 percent at source-compromise chances of five, 15, and 25 percent respectively.
Those expectations do not prove the full policy's wrongful-purge rate.
Adaptive method selection, audit replacement, new-conduct reopening, and the real candidate mix still require the complete blind policy comparison.
The AI chooses its source-reliability mixture from actor-known Confidence, service history, and publicly supported concerns.
It cannot substitute the actual hidden integrity flag or hidden institutional holder for that estimate.

At most one new discretionary case action is scheduled per participating AI country in each five-day service window.
Existing investigations complete on their own dates.
AI countries use the national staff slots and monthly resource envelope defined in the decisions chapter.
Major powers cannot inspect every person each day, and weak states retain the slower no-equipment investigation path.
Policy differences may change risk tolerance and institutional spending, but cannot give an ideological group secret knowledge of truth.

## Difficulty evaluation and the mistakes audit

Evaluate difficulty with a blinded set of at least 1,000 saved cases that contains the admission-channel mix, clean and compromised sources, dependent and independent evidence, and both truth states.
Keep the truth manifest separate from the records given to human testers and from the AI policy input.
Use different campaign seeds and hold back portrait identities from any tuning sample used to refine descriptions.
The evaluator must not choose only cases whose evidence cleanly supports the intended answer.

Compare four policies: portrait-only judgement, random resolution at the same purge rate, an evidence-aware novice policy, and the full constrained AI or experienced-human policy.
Portrait-only prediction must not outperform a prior-only baseline beyond sampling uncertainty.
Report balanced accuracy as well as ordinary accuracy so that always choosing the more common truth class is not mistaken for visual insight.
The launch acceptance target is balanced accuracy no greater than 55 percent on held-out portraits, with uncertainty compatible with the 50 percent chance baseline.
Generated versus sourced images, demographic appearance, source archive, crop style, and file sequence must not predict guilt beyond sampling noise.
Any material shortcut found in that audit requires changes to sampling or art acceptance.

Among policies that perform irreversible removals, informed investigation should improve the share of those removals that actually interrupt hostile membership by at least 15 percentage points over the matched random policy.
Report missed infiltrators and harmed innocents alongside that precision measure, rather than rewarding an arbitrary increase in purges.
If a policy makes no removals, report the precision comparison as not estimable and judge its nonlethal containment through actual network operations and protected people.
A meaningful group of cases should remain unresolved after two methods.
The informed policy should reduce actual network operations by 25 to 50 percent against a matched no-response campaign over 180 days without purging more than 15 percent of innocent admitted people.
These are tuning targets, not promised results.
Compare them at equal staff time and equal resource expenditure, including the slower paths available to small countries.

The mistakes audit records false accusations, wrongful purges, missed infiltrators, dependent evidence counted twice, misread source concerns, and failures caused by an unaffordable response.
Separate an unavoidable ambiguous case from a UI misunderstanding or a model defect.
An error caused by a hidden cost, a stale portrait, misleading independence, or an unlabelled unavailable method is a design failure.
An error made from genuinely overlapping evidence can be part of the intended uncertainty if the recovery path remains meaningful.

`119_mistresses_spec_part_12_chaos_balance.md` owns cross-campaign policy comparisons and global tuning.
`119_mistresses_spec_part_13_achievements_validation.md` owns the combined validation scenarios.
`119_mistresses_spec_part_9_interfaces_information.md` owns the presentation contract that keeps case truth out of the interface.

## Source notes

The persistent two-value budget and frozen-case rules follow [Part 1](119_mistresses_spec_part_1_core.md) and the accepted case design in this chapter.
The consequence, uncertainty, AI, and cost design applies `.claude/skills/chaos-redux-event-planning/SKILL.md`, sections 3.4, 3.9, 3.10, and 3.11, with its complete `references/player-facing-text-direction.md` and `references/advanced-focus-tree-design.md`.
Payment, mission pacing, AI validity, and lifecycle guidance comes from `.claude/skills/chaos-redux-decisions-missions/SKILL.md`, sections 5, 8 through 10, 16, and 17, and its `references/cost-payment-and-localisation.md`.
The harmless-first irreversible confirmation contract comes from `.claude/skills/chaos-redux-events/SKILL.md`, Event anatomy and Proposal popup lifecycle.
The quantitative likelihoods, policy thresholds, and outcome amounts in this chapter are proposed game tuning under the parent's accepted design direction.

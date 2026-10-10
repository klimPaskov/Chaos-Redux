# Treaty of Tordesillas Restoration: AI behavior and scenario matrix


## Principles

The AI should pursue a plausible route for its current country, not guarantee the event's most dramatic ending.
Spain can defend Galicia.
Portugal can avoid a losing war.
A Spanish winner can honor a useful bargain without becoming permanently obedient.
A successful treaty can remain limited.

Separate eligibility, strategic preference, and stochastic choice.
An action that is illegal, unaffordable, or directed at a dead country is excluded before weights are evaluated.
A willingness weight is not a probability.
Focus selection, event-option choice, diplomatic acceptance, and MTTH opportunity timing require their own proper evaluation.

The matrix below specifies expected direction and disallowed outcomes.
It intentionally does not invent validated percentages.
Exact implementation weights and their behavior are checked by `chaosx_ai_probability_auditor` with the available probability tools or source-derived calculations.

## Portugal before a settlement

Portugal favors negotiation when Spain is stable and stronger.
It favors a compensated bargain when it can afford the price and Galicia offers real strategic value.
It gives greater attention to an intervention bargain when Spain is divided and a compatible, viable recipient exists.

Political compatibility is important but not absolute.
The Nationalists are the natural partner where the current government and war support that relationship.
Another national claimant can be preferred under a different Portuguese government.
An ideological enemy should not accept an imperial bargain simply because it is labelled 'Spanish.'

The AI protects its home defense, essential stockpile reserve, existing war commitments, and usable delivery route.
It must not pledge a material package that it cannot plausibly deliver.
It also must not send every rifle abroad while its own army has a critical deficit.

After refusal, escalation rises with real military readiness, a credible route to Galicia, Spanish weakness, and favorable diplomatic conditions.
It falls sharply when guarantees or faction commitments make a wider war likely.
A claim or a high Chaos level does not override an unwinnable strategic situation.

## Spain before and after civil war

A unified, secure Spain normally prefers to keep Galicia unless the price and geopolitical value justify cession.
A threatened Spain may prefer a quiet western frontier.
Refusal is not automatically reckless, and acceptance is not automatically surrender to Portugal's later ambitions.

A civil-war side weighs the aid package against its need, prospects, ideology, and ability to honor the promise.
A side unable to obtain Galicia should recognize that uncertainty rather than offer it with certainty.
The package's actual usefulness matters more than Portugal's nominal opinion modifier.

After victory, earned and fully delivered support strongly favors honoring the bargain.
A government with a territorial-nationalist policy or severe domestic pressure may still repudiate it.
Such a choice must carry the recorded grievance and risk, not be a cost-free 50/50 coin flip inherited from the legacy script.

A side that did not receive the promised standard is more willing to renegotiate.
The AI should distinguish an incomplete but still timely contract from deliberate Portuguese default.
A victor opposed by Portugal is skeptical of immediate treaty restoration and asks for a real reconciliation.

## Treaty diplomacy

Restoration is favored by a recognized border, completed obligations, sufficient Confidence, shared external threats, and feasible faction arrangements.
It is disfavored by anti-imperial policy, unresolved betrayal, incompatible alliances, or dependence on an outside overlord.

Global partition is more attractive when the treaty is functioning and both governments have a plausible expansion path.
It is less attractive to a government whose entire security rests on allied countries that the partition would threaten.
The AI can stop at Evolution I.

Universal conquest requires demonstrated power and administrative capacity.
A weakened partner should ask for support or consolidate.
The AI must not treat every newly visible claim as an immediate declaration target.

## Choosing campaigns

Choose from bounded, current theaters inside the correct sphere.
Rank access, active war relevance, supply feasibility, opponent strength, strategic value, and the amount of useful contiguous territory.
Strongly penalize targets that create a second major war while the current one is unresolved.

A reachable neighboring region is normally more attractive than a remote isolated state.
A crucial port or access route can justify a smaller target.
The AI should not chase empty land solely because it raises a geographic component of readiness while ignoring the population and integration components.

When its own Consolidation is high and its partner's is low, a crown increases the priority of real assistance.
It does not annex the partner or exploit wrong-sphere conquests to grow its own score.
Transfer decisions should prefer legally safe, non-core, undisputed states covered by a standing agreement.

## Choosing integration projects

The AI selects coherent regions it owns and can keep supplied.
It prefers an affordable, secure project that fills the current limiting component of Consolidation.
It leaves an equipment reserve and does not begin projects in states likely to be lost immediately.

The capacity focus is attractive to a broad empire with several affordable secure regions.
The acceleration focus is attractive where fewer high-value projects are the bottleneck.
Neither is always the best choice.
The more expensive concentrated project approach is selected only when the time saved has strategic value.

The AI prefers a negotiated settlement and chooses a coercive one only for a valuable recent conquest whose compliance would otherwise delay integration by more than the coercive preparation period, or when negotiation is impossible.
It feeds a starving enrolled region through the famine actions rather than requisitioning from it, unless its own home states are in famine.

A project nearing completion is not an excuse to escalate into a war that cuts its only supply route.
The AI should be able to cancel a doomed project, accept the documented loss, and free its slot.

## External-country behavior

A threatened country weighs subordination against actual enforcement capability and credible outside assistance.
A small isolated government can accept a protectorate.
A viable major normally prefers resistance or a strong negotiated compromise.
The target's autonomy expectations and the treaty's record of keeping promises matter.

Targets read the crown's record: each coercive settlement in the previous 365 days lowers willingness to accept subordination, a repudiated Galicia bargain lowers trust in autonomy promises, and a crown at Condemnation Tier 4 or higher receives refusals regardless of power.
A crown recognized by a Spanish civil-war side before the contract, or sharing intelligence with it, is a more acceptable aid partner.

Opposition cooperation is favored when the target is directly threatened and prospective partners can materially help.
It is not blocked merely by ideological differences, but it is also not an automatic worldwide alliance.
Existing wars and national interests continue to matter.

## Required probability scenarios

| Scenario | Expected direction | Unacceptable result |
| --- | --- | --- |
| Stable strong Spain, weak peaceful Portugal | Negotiation or restraint | Forced Portuguese war after refusal |
| Exhausted Spain, affordable Portuguese compensation | Serious settlement consideration | Acceptance independent of price or ownership |
| Compatible Nationalist recipient in a live war | Higher Portuguese interest | Historical winner assumed without live evidence |
| Compatible alternative national claimant | Valid alternative contract | Hard-coded rejection by tag alone |
| Anti-imperial Spanish policy | Lower treaty willingness | Automatic imperial conversion at 200 Chaos |
| Portuguese equipment deficit | Delay or smaller explicit bargain | Critical home stockpile emptied |
| Earned, fully delivered aid and Spanish victory | Strong honor preference | Legacy fixed 50/50 behavior retained |
| Partial timely aid and early victory | Extension or renegotiation | Automatic Portuguese default |
| Portugal backed the loser | Difficult reconciliation | Dead recipient hands over Galicia |
| Unresolved repudiation, high diplomatic opinion | Restoration blocked | Opinion bypasses restitution |
| Same faction, foreign major leader | Valid reorganization or delay | Foreign members silently expelled |
| Separate hostile factions | Delay until valid diplomacy | Instant merge of unrelated wars |
| High Chaos at initial firing | Baseline still runs | Immediate world cores or faction |
| Broad empire, little integrated land | Integration priority | More empty-land wars indefinitely |
| Core-rich compact empire | Reach and access priority | World-end qualified by cores alone |
| Correct partner ready, other partner weak | Assistance priority | Annexation of junior crown |
| Wrong-sphere non-core conquest with standing consent | Restitution favored | Permanent AI hoarding without reason |
| Wrong-sphere native core | Explicit negotiation | Automatic core-state transfer |
| Small isolated threatened country | Plausible submission | Automatic annexation on refusal |
| Well-supported major target | Resistance or negotiation | Submission unrelated to real power |
| One crown capitulated | No world-end entry | Signature substitutes for sovereignty |
| World-end already owned by another event | No takeover | Event 093 clears another scenario |
| Two human treaty powers | Both approvals required | AI auto-vote overwrites human refusal |
| Save/reload during pending offer | Same legal options | Fresh roll duplicates rewards or ownership |
| Recent low-compliance conquest of high value | Coercive settlement considered | Coercion chosen for a calm region that qualifies for negotiation |
| Enrolled region in famine | Relief actions taken, project waits | Requisition from the starving region while the home is fed |
| Crown at Condemnation Tier 4 issues an ultimatum | Target refuses | Submission to a pariah crown |

## Validation workflow

The AI probability auditor should inspect actual scripted candidate sets and branches, evaluate these scenarios, sweep strength, reserves, Confidence, and Chaos around boundaries, compare alternatives, and render the results.
Sequence tests must cover demand, refusal, aid, victory, restoration, and later treaty behavior together.

Where the relevant tool supports simulation, record seeds and scenario inputs.
Where it supports exact evaluation, preserve the exact result.
Do not call a hand-normalized focus weight a proven event probability.
Do not claim balance from one successful observer game.


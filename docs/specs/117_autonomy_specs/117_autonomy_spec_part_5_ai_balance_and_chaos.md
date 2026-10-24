# 117 Autonomy: AI, balance, and Chaos

The AI should understand autonomy as a political opportunity whose value depends on security, the current relationship, and the ability to govern afterward.
A subject may rationally want a higher status while still valuing its master's protection.
A master under heavy military pressure may gain more from a workable concession than from preserving a formally tighter relationship it cannot support.

## AI policy by situation

Eligibility is evaluated before preference.
An AI weight cannot make an illegal native promotion, stale agreement, unsupported confrontation, or unavailable payment route valid.
The baseline award is unconditional and has no AI acceptance gate.

| Actor and situation | Preferred ordering | Why and expected timing |
| --- | --- | --- |
| Stable subject with valuable protection | Useful lawful improvement or compact, continued cooperation, then pressure | Take a material gain without discarding necessary security |
| Secure subject already close to a legal higher status | Use the native route, consider a compact, retain current status if the remaining price is poor | Act during the opportunity while respecting all actual gates |
| Fragile subject under defensive military pressure | Accessible consolidation or assistance, workable compact, civilian stand-down, confrontation last | Preserve government and avoid a second front |
| Subject with no viable army or territory for conflict | Negotiation, consolidation, retention or stand-down | Military escalation is unavailable unless the exact owner supports a viable alternative |
| Subject harmed after a successful agreement | Repair the administration and seek delivery of agreed support | A signed agreement is not proof that its aftermath is stable |
| Subject facing repeated actual suppression | Seek better terms or a legal exit, while comparing confrontation with survival | Past conduct changes trust without erasing current military reality |
| Master with one cooperative subject | Tailored lawful concession or compact before costly retention | The singleton receives substantive diplomacy |
| Master with many unresolved subjects | Common feasible terms, targeted help to the most consequential fragile members, selective retention | Limited attention should be allocated where it changes actual outcomes |
| Master losing an important war | Accept feasible concessions, avoid new wars, preserve cooperation where possible | A second front and prolonged unrest carry greater costs |
| Master with a vital base or defensive partner | Seek a cooperative status settlement and preserve military terms through their owner | Strategic value supports negotiation as well as retention |
| Master already delivering commitments | Honor current service before promising new assistance | Avoid breached compacts and a fourth unsupported assistance promise |
| Country in both subject and master roles | Evaluate the two relationships independently and account for combined burdens | Neither role supplies consent for the other |

Read military pressure from real wars, capitulation exposure, controlled territory, commitments, and credible support.
Read the value of cooperation from the actual military and diplomatic relationship.
Do not hardcode a country tag, ideology, or region to always accept or always revolt.
Ideological preferences may refine an otherwise legal strategic choice, but they cannot replace its factual evaluation.

## Relative preferences and probability semantics

Decision willingness is a priority, not a direct probability of clicking.
Event response weights are relative to the complete legal option pool at that moment.
The numerical harmful-outcome chances in Parts 2 and 3 are separate deliberate random assessments.
Do not describe all three systems as the same kind of probability.
[PS-S050–S052, PS-S102]

The following preference anchors are planning comparisons for complete legal response pools.
They establish intended ordering and strength, rather than final script weights.

| Representative response pool | Cooperation or concession | Continued bargaining | Refusal or pressure |
| --- | --- | --- | --- |
| Ordinary stable master considering a feasible compact | 60 | 30 | 10 |
| Master under heavy military pressure with a feasible settlement | 80 | 15 | 5 |
| Secure master with a highly valuable relationship and credible retention capacity | 35 | 40 | 25 |
| Fragile subject receiving workable support and no hidden status loss | 70 | 20 | 10 |
| Secure subject offered terms materially worse than a legal higher status | 20 | 50 | 30 |

An unavailable option has zero weight.
A safe cancellation remains available in confirmations and receives the fallback weight when every substantive route is invalid.
Once real script options are known, the probability auditor must inspect the whole pool, its modifiers, and its no-valid-substantive-option case.
These tables must not be pasted into a decision `ai_will_do` block and then reported as exact percentages.

The AI should respond within a useful share of a political window.
Target first consideration within 10 days of a valid offer and a reconsideration after a material change in war pressure, terms, or domestic harm.
Use the existing supported AI cadence or bounded owner callbacks.
No new whole-world daily polling is justified by this timing goal.

## Checked arithmetic examples

These examples apply the planning formulas directly.
They are source-level arithmetic, not observed engine outcomes.

| Evolution I scenario at day 30 | Raw probability | Final probability |
| --- | --- | --- |
| Stability 60, no defensive war, no recent relationship conflict, no program | 10 percent | 10 percent |
| Stability 75, no current relationship conflict | 10 − 5 | 5 percent |
| Stability 45, active defensive war, no prior conflict | 10 + 10 + 10 | 30 percent |
| Same case with consolidation | 30 − 10 | 20 percent |
| Stability 25, defensive war, previous real conflict | 10 + 10 + 10 + 10 + 10 | 40 percent after the ceiling |
| Same severe case with one safeguard | 50 − 10 | 40 percent |
| Same severe case with both safeguards | 50 − 10 − 10 | 30 percent |

| Evolution II scenario at assessment | Raw probability | Final probability |
| --- | --- | --- |
| Orderly agreement, stability 60, no other factor | 10 percent | 10 percent |
| Honored agreement, stability 75 | 10 − 5 | 5 percent |
| Unanswered negotiation, stability 60, two unresolved members | 20 percent | 20 percent |
| Explicit rejection, stability 35, no separate history | 30 + 10 | 40 percent |
| Rejection with low stability, separate prior conflict, three unresolved members, and current crisis | 30 + 10 + 10 + 5 + 10 | 50 percent after the ceiling |
| Same severe case with one safeguard | 65 − 10 | 50 percent |
| Same severe case with both safeguards | 65 − 10 − 10 | 45 percent |

A safeguard does not always change the clamped chance.
At a floor it may provide no further risk reduction, and one safeguard at a high raw value may leave the ceiling unchanged.
The AI must calculate the actual marginal reduction, then consider immediate recovery relief and compact value separately.
The UI must not promise a ten-point reduction in the displayed final chance when the clamp absorbs it.

The two harmful assessments are conditionally linked when both evolutions operate.
For illustration, suppose the first shock has a 30 percent chance, and the second assessment has a 20 percent chance without that shock or a 30 percent chance with it, holding all other factors fixed.
Then the chance of at least one harmful result is 0.30 + 0.70 × 0.20 = **44 percent**.
The chance that both assessments return a harmful result is 0.30 × 0.30 = **9 percent**.
The second assessment's overall harmful frequency in that illustration is 0.30 × 0.30 + 0.70 × 0.20 = **23 percent**.
Actual campaign conditions may also change stability, support, timing, or legal participation, so these figures are not a universal combined-event prediction.
The merged-harm rule still prevents the two outcomes from stacking duplicate national penalties.

## Pacing and meaningful strength

The baseline's quarter-tier award is substantial without normally traversing a whole interval by itself.
The momentum window adds one-fifth of the same entry interval over four months.
A completed compact adds one-tenth after real service.
The combination gives a prepared subject a credible route toward a status change while keeping its starting position and ordinary requirements meaningful.

Compare baseline 20, 25, and 30 percent against representative early-, middle-, and late-interval subjects.
Compare momentum at 90, 120, and 150 days while keeping its total extra fraction fixed before changing both speed and total at once.
Compare compact delivery at 90 days with the real costs of normal progression and the ability to retain cooperation.
Evaluate one factor at a time where possible.

Important undesirable outcomes include a baseline that is mostly swallowed by caps, native AI that never uses earned readiness, support that is irrational because it has no marginal benefit, and negotiation that always produces a dominant choice.
Other risks are repeated firings that reset commitments, an empire punished once per subject on its own stability, and a late newcomer harmed before it had a useful chance to answer.
The specified repeat, aggregate burden, and short-notice rules address these risks directly.

## Chaos ownership

The event's Low cluster role describes its baseline severity.
Evolutions can produce concrete disorder, while the shared liberation and conflict systems keep ownership of the larger outcomes they actually create.
Use the current tier bands from the supplied mechanics rather than treating the tier number as a direct Chaos award.
[PS-S121]

| Outcome | Owner | Proposed Event 117 contribution | Limit and recovery |
| --- | --- | --- | --- |
| Initial point grant, clipping, readiness, or ordinary cooperation | Event 117 | 0 | No Chaos for merely becoming eligible to act |
| Evolution eligibility, enablement, activation, or preview | Shared evolution presentation and Event 117 | 0 | No direct Chaos from the mutation itself |
| Actual first Autonomy Shock | Event 117 domestic incident | +1 | Once per incident, within the originating firing's budget |
| Actual organized petition unrest | Event 117 domestic incident | Up to +2 total for the incident | If it is the same disturbance already counted at +1, add only the missing +1 |
| Failed talks without a harmful outcome | Event 117 | 0 | Disagreement alone is not a separate catastrophe |
| Real completed civil containment or honored stand-down | Event 117 | Remove only that incident's outstanding Event 117 contribution | No refund for an uncommitted assessment, failed work, or already refunded contribution |
| Native independence, war relations, peace, annexation, faction changes, casualties | Existing shared outcome owners | 0 additional Event 117 award | Consume actual owner outcomes without duplicating their configured values |

The initial aggregate Event 117 disorder budget is **+6 per originating firing** across all its subjects and both evolutions.
The first harmful result assigns the domestic incident's originating firing.
Later coalesced descriptions or firings do not reset that incident's budget identity.
The budget limits only the event-owned increment, not the actual local consequences or a separate shared war contribution.
The +6 limit counts gross positive contribution consumed by that firing.
Later containment refunds do not replenish its allowance for another assessment.

Record the actual increment applied after caps, not merely the requested increment.
A country whose requested contribution was zeroed by the firing budget has no contribution to refund later.
Containment can never reduce Chaos by more than its outstanding recorded amount.
A new grant, natural timer expiry, or a canceled invalid target is not proof that active political containment occurred.
A voluntary stand-down qualifies only after its full 90 days are honored, even if its shortened harm tail ended earlier.
There is no repeatable positive-then-negative farm with a net reward.

The current shared war handler counts qualifying war relations and contains its own faction and daily-cap logic.
Event 117 must use that current owner rather than copying a remembered war formula.
[R-WAR]

## Temporary AI steering

If the native AI needs help respecting a compact or avoiding an unviable confrontation, use an event-owned, phase-gated strategy with explicit end conditions.
Remove its authority on settlement, withdrawal, loss of relationship, or handoff.
Do not accumulate permanent strategic additions on every repeated firing.
Do not let a native zero desire to change a special autonomy level be silently overridden by a generic AI weight.
That case belongs to the relationship owner and the compatibility review.

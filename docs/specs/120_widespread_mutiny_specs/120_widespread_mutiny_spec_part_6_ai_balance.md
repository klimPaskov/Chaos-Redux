# 120 Widespread Mutiny, Part 6: AI, pacing and balance

## Balance goals

A Low opening should create an immediate military decision without routinely deleting a country's army. Reliable relief should cost real time and capacity. Coercion should be competitive when loyal superiority and supply make it credible, while a divided, poorly supplied government should find it dangerous. Demobilization should be attractive when ending the disputed obligation is worth more than preserving the present army. Waiting should be useful when a real external resolution is near.

The dangerous outcomes need warning, a campaign cause and a failed response. The 600+ evolution adds reciprocal front politics and a possible joint armed actor. It does not turn every country in every war into a rebel state at the threshold.

All values in this part are authored tuning proposals. Arithmetic examples are design calculations. No engine simulation, MCP probability run or campaign test is implied.

## Distinct weighted surfaces

| Surface | Candidate pool | Interpretation | Required exclusions |
| --- | --- | --- | --- |
| Primary outbreak country | Every currently eligible country in the event snapshot | H from Part 1 is a relative selection weight | Active incident, recovery protection, no valid actual formation, impossible response authority |
| Additional-country outbreak | Each remaining eligible country separately | H is a percentage for this one draw | Same exclusions, no second check for the primary country |
| Cohort selection | Actual eligible formations in the selected operational locality | Relative contextual preference within a bounded manpower budget | Already consumed, conflicting commitment, unresolved ownership or incompatible unit type |
| Baseline spread | Each incident with a valid linked new cohort | One percentage check per 20 days | Active on-time settlement, cap reached, no real connection |
| Suppression outcome | Contained, Partial, Fracture | Three exhaustive percentages from Part 2 | Impossible loyal-force preparation prevents the attempt |
| Government action | Every currently legal action and target | AI willingness and priority scores | Human UI selection is irrelevant to legality |
| Evolution opportunity | Exact opposing eligible front pairs | Native verified timing model using a contextual MTTH anchor | Disabled evolution, Chaos below 600, absent opposing cohort, stale war/front identity |
| Counterparty response | Accept, observe with conditions, reject | Event-option weights after feasibility gates | No acceptance of impossible terms or expired proposals |
| Council route and focus | Complete available route or focus pool | Route priorities and the current engine's focus score race | Incompatible route, unreachable promise, invalid geography or missing recipient |
| White Peace context | Event 009's complete eligible pair pool | An owner-provided bounded multiplier | Mutiny cannot legalize an otherwise excluded pair |

The implementation must keep these meanings separate. Decision scores are not percentages of daily clicks. Focus weights are not normalized shares of a simple weighted lottery. A 90-day MTTH anchor does not establish a cumulative probability without the current timing model and its changing conditions.

## Government priorities

First apply the same hard availability, authority, payment and target gates as for a human. Then calculate a nonnegative willingness score. The following complete ordinary action family is the initial policy. Equivalent contextual methods can replace an action only when they perform its promised outcome and disclose their own costs.

| Action | Base score | Positive context | Negative context |
| --- | --- | --- | --- |
| Negotiate compact | 50 | +40 at confidence at least 40, +30 for a feasible unmet representation or command concession | -40 if the available concession poorly addresses the grievance |
| Leave and rotation | 40 | +30 for a secure transport/replacement plan, +20 for an experienced affected cohort | -40 if withdrawal exposes the only defended approach to the capital |
| Supply relief | 40 | +40 when supply is the primary cause, +20 when a suitable project is already near completion | No route or no actual delivery capacity makes the action unavailable |
| Agreed discharge | 30 | +60 after the relevant war ends, +30 when defense remains adequate | -60 if it would remove the last effective field force during an active invasion |
| Immediate local discharge | 20 | +80 when no funded remedy is feasible, +40 after the relevant war ends | -40 when it removes the last effective formation during invasion, while remaining a valid deliberate fallback |
| Loyal-force containment | 25 | +50 at effective ratio at least 2, +20 when ordinary negotiations have already been repudiated | -40 when both sides of a paired front are mutinous, -30 for serious loyal-force supply exposure |
| Wait for a known development | 10 | +50 for an actual scheduled peace or withdrawal within 10 days, +30 for a funded remedy due within 10 days | -60 if an unresolved deadline expires within 10 days and no actual remedy is scheduled |

After a compact is signed, its required delivery action receives priority over an unrelated new promise. The AI does not spend on a second agreement while the first is overdue unless the first can no longer be delivered and the replacement is disclosed. It preserves enough resources to complete active paid commitments before seeking optional institutional rewards.

A direct remedy receives an additional 50 willingness points when it fully resolves the primary grievance before the deadline and no further negotiated concession is required. Discharge and military surrender receive this bonus only when effective defense remains adequate. During an active invasion, keeping the last effective defending formation has priority over elective release unless its continued existence cannot preserve the country and a verified settlement protects the surviving people. The human discharge option remains available. A confirmed external settlement due within 10 days and before the crisis deadline gives waiting a higher priority than opening a new paid commitment, unless immediate survival requires action. A rumored peace or a repeatedly postponed promise does not qualify. These rules prevent routine paid negotiation from displacing a complete practical solution or an already imminent settlement.

This table is the full action family across phases. The live opening exposes compact negotiation, the relevant practical remedy, immediate discharge, eligible containment and waiting. Paid discharge or leave variants replace the practical-remedy row when selected. Commitment and recovery phases replace their start actions. The seven families never imply seven simultaneous primary rows.

The AI attempts suppression only when the computed Contained probability is at least 60%, the loyal deployment is valid, and the expected military gap is tolerable. A human can choose a riskier valid operation after seeing the consequences. If the suppression threshold is not met, the AI considers a smaller compact, a protected withdrawal or discharge. It does not repeatedly select a zero-resource promise it cannot fulfill.

A country facing annihilation can prioritize defense and accept a temporary incomplete settlement, but it cannot reclaim already demobilized soldiers by changing a flag. The military threat changes its choice, not the accounting rules.

## Cohort and target priorities

Prioritize the formation that experienced the grievance. The preference order is a verified direct grievance, an affected supply or deployment corridor, a shared command or delegate link, then a lower-impact eligible nearby formation. A named elite unit is not preferred solely because its loss would be dramatic.

A target that is already being demobilized by Event 114 can supply pressure or an outcome handoff only through that owner's live receipt. It cannot enter a new destruction pool. A military formation transferred to an Event 116 warlord exits the donor's available pool as soon as the committed transfer is proved.

For a country with multiple cohorts, the AI first protects a deadline that can be met, then a cohort whose loss threatens a supply hub or capital, then the greatest recoverable strength per feasible commitment. It may abandon an infeasible demand, but must explicitly choose its consequence rather than stalling on an unavailable action.

## Evolution timing and opposing responses

The Brothers Across the Trenches opportunity uses a 90-day MTTH anchor after the exact front becomes eligible. Shared hardship on both sides, sustained adjacent contact and a recently broken promise accelerate it. A successful rotation, high agreement confidence and a moving front delay or remove the opportunity. The design range is 30 to 180 days. The effective delay cannot be continually reset by a view refresh or an unrelated event draw.

An already established, valid fraternization state can enter the evolved opening immediately when the root fires. Raising Chaos to 600 during an active incident changes the eligible behavior immediately and starts its opportunity checks. It does not wait for Event 120 to fire again. The concrete pact still requires contact and reciprocal acceptance.

For an offered local pact, the initial event-option weights are:

| Response | Base | Additions | Reductions and validity |
| --- | --- | --- | --- |
| Accept a verified bounded compact | 40 | +40 when both cohorts have Disaffection at least 60, +30 when both governments can deliver the stated relief | -40 at confidence below 40, unavailable for terms requiring nonexistent authority |
| Observe and seek one guarantee | 30 | +40 at confidence below 40, +20 when one side has an incomplete relief route | Unavailable when the proposal's remaining time cannot accommodate the stated guarantee |
| Reject the compact | 20 | +40 when the accepting cohort already has a delivered settlement, +30 when the territorial terms exceed the front footprint | -20 when both exhausted cohorts have an immediately feasible local solution |

An unqualified confidence condition in this response table reads the responding constituency's own Agreement confidence. Both sides' Disaffection is used only where the row explicitly requires both. Weights are clamped to nonnegative values after modifiers. The valid choices are normalized only within this exact response pool. A zero total uses a lawful noncommittal expiry result, never an acceptance. Neither side can accept on behalf of an absent human player or a third-party ally.

## Council AI

Council AI first protects survival of the founding population and supply, then chooses a political route. It retains the same manpower, equipment, territorial and promise constraints as a human council player.

It favors a negotiated service charter when the former authorities can deliver specific guarantees and continued independence would leave an unsupplied enclave. It favors a civilian territorial republic when the founding region can sustain itself and civilian institutions accept a transfer of authority. It favors temporary emergency defensive command while an immediate attack prevents safe demobilization or a civilian settlement. The emergency route must pursue its stated handover deadline.

The route is a strategic commitment. Temporary adversity does not make the AI switch routes every review. If a route becomes impossible, it follows the defined revision, settlement or clean-closure branch. It never waits forever for one foreign AI to accept a single invitation.

Military AI protects the founding footprint, avoids sending its only force on an unrelated offensive, maintains a realistic conventional template mix and buys only the equipment its actual units use. It seeks a supply passage before annexing an adjacent region. A foreign sponsor cannot draw the council automatically into the sponsor's other wars.

Focus AI uses the complete live available-focus pool and current score-race semantics. Opening priorities are food-equivalent supply access through actual supported resources, administration, command responsibility and a political direction. Industry and military support branches remain useful across routes. Exact focus weights follow the implemented branch architecture and receive their own audit.

## Quantitative examples

The examples use the exact formulas in Parts 1 and 2. Each declares its complete local inputs. They do not model the whole campaign or the unknown external candidate pool.

| Case | Inputs | Outbreak H | Initial D | Initial confidence |
| --- | --- | --- | --- | --- |
| Recently mobilized minor | W 30, all context flags zero | 20 | 40 | 40 |
| Exhausted frontline army | W 20, L S K equal one, other flags zero | 60 | 75 clamped to 70 | 40 |
| Severe linked desertion | W 10, L S K B X equal one, R zero | 90 clamped to 70 | 100 clamped to 70 | 20 |
| Reliable prior settlement | W 30, R one, other flags zero | 10 | 30 | 60 |

The stressed cases begin with a response window even at the Disaffection cap. The first opening cannot silently consume the army because its starting value is high. If four eligible countries have H values 20, 60, 70 and 10, the complete primary-selection pool totals 160. Their primary chances are 12.5%, 37.5%, 43.75% and 6.25%. These are exact design arithmetic for this declared pool. Additional-country checks remain independent direct percentages after the primary is removed.

| Suppression case | Inputs | Contained | Partial | Fracture |
| --- | --- | --- | --- | --- |
| Supplied loyal superiority | R 2, U 1, D 55, confidence 40 | 80% | 15% | 5% |
| Adequate but tense containment | R 1.5, U 0, D 70, confidence 40 | 50% | 35% | 15% |
| Divided emergency | R 1.5, U 0, D 85, confidence 10 | 20% | 30% | 50% |
| Overwhelming prepared force | R 4, U 1, D 55, confidence 80 | 85% | 10% | 5% |

The first row has a raw fracture score of zero, which reaches the 5% minimum before the remaining probability is assigned to the partial result. At high Disaffection and very low confidence, the fracture share is also capped by the probability remaining after success. This keeps all three outcomes nonnegative and exhaustive.

## Required threshold and strategic reviews

Check war support at 35 and immediately above it, Disaffection at 25, 60 and 80, confidence at 20, 40 and 70, effective loyal ratio at 1.5 and 2, and Chaos immediately below and at 600. The same displayed rule and actual gate must agree at equality. Review the one-division exception separately from ordinary manpower-budget selection.

Run the spread calculation at every authored threshold and after each promise outcome. Verify that the combination of shared human pressure, local spread modifiers and timing does not charge the same difficulty adjustment twice. Compare a quiet low-support country, a long but inactive war, a heavily supplied offensive army and a starved defensive army.

Test strategic dominance with actual opportunity costs. Negotiation should not be an instant paid cure. Suppression should not be an inevitable revolt. Discharge should not create a larger reserve than the actual released people. Waiting should not grant repeated grace periods. Council independence should require sustainable institutions and material supply, while reintegration should offer a worthwhile and credible campaign outcome.

The full validation and exploit matrix is in [Part 8](120_widespread_mutiny_spec_part_8_achievements_acceptance.md). The implementation handoff separates design calculations, source review, native capability proof and user-authorized live testing.

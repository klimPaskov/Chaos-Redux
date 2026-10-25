# Part 5: AI behavior and balance verification

## Balance objectives

The event should reward functioning services, maintenance and realistic allocation.
Preparedness and supplied transport improve survival.
Small countries need useful local work and credible assistance.
Large territories carry larger obligations.

[Part 1](124_sun_moves_away_spec_part_1_core.md) owns environmental and deprivation targets.
[Part 2](124_sun_moves_away_spec_part_2_evolutions_and_return.md) owns evolution and Return pacing.
[Part 4](124_sun_moves_away_spec_part_4_decisions_missions.md) owns action costs and limits.
This part defines the tests and AI preferences used to evaluate those proposals.
No numerical result below claims a game run, native probability audit or observed campaign frequency.

The principal balance questions are whether paid services materially improve survival, whether existing commitments stay affordable, whether geography changes decisions, and whether recovery preserves the real cost of the episode.
Relief must remain useful during a long random tail.
Exhausting a response budget cannot secretly trigger Return.

## AI validity and order of work

AI first proves the same actor, target, stock, access, ownership, reception and generation conditions required from a player.
Invalid candidates leave the available pool.
A missing shared-owner receipt remains a blocked action.
AI receives no invented route, food reserve, surviving creature or free equipment.

The planning order is:

1. Protect the next authorized installment of an essential existing service.
2. Evaluate feasible rescue and immediate exposure emergencies.
3. Repair the bottleneck that prevents several services from functioning.
4. Improve security, industrial continuity or broader coverage.
5. Expand long-term refuge capacity when continuing upkeep is affordable.
6. Use observation when uncertainty blocks better work.

Mission availability matters throughout.
Three occupied slots require settlement or suspension of an eligible commitment before a new mission starts.
AI should preempt a low-value survey or expansion project when a feasible urgent rescue warrants it, preserving consumed costs and completed work.

Use current registered countries, states, routes and obligations through the existing bounded owner coordination.
Material access, capture, affordability and threat changes prompt reevaluation.
A routine review every seven days is an initial tuning target.
Upkeep and emergency callbacks keep their actual deadlines.
Reopening the panel and pausing the game do not generate extra AI actions or income.

## Proposed willingness model

Action willingness combines a family priority with current urgency, useful reach, resource margin and allocation fit.
These are internal relative scores.
Native decision activation frequency requires separate observation and probability evidence.

| Factor | Proposed range | Interpretation |
| --- | ---: | --- |
| Family priority | 40 to 100 | Survival and rescue start near 100, maintenance near 80, security and recovery near 70, continuity near 60, observation and expansion near 40 |
| Urgency | 0.5 to 3.0 | Low optional need through a confirmed immediate threat |
| Useful reach | 0.5 to 1.5 | Actual residents or essential deliveries helped relative to the accepted package |
| Resource margin | 0.5 to 1.0 | Caution near an uncommitted stock limit |
| Allocation fit | 1.0 to 1.15 | A modest preference for the selected national priority |

A high score cannot override validity.
The resource factor considers the whole authorized commitment, including scheduled upkeep.
Equipment already consigned to another operation is unavailable for a second promise.

As a starting prudence target, AI retains twenty percent of its pre-decision fuel stock where possible, together with verified near-term demand from essential existing commitments.
That percentage influences willingness.
The actual retained contractual requirements remain equally binding for players and AI.
An emergency may justify a lower discretionary margin while preserving already committed resources.

A country with five support equipment, no spare factory and no fuel should evaluate A02's reduced local adaptation where functioning heat already exists.
It should avoid quoting a standard installation it cannot afford.
A country without usable heat capacity needs assistance or a valid evacuation destination.
Observation cannot substitute for either.

## National priority choice

The first national choice uses a complete pool of the three valid priorities.
Proposed controlled examples give the following initial weights.
They are test cases for a future choice implementation.

| Controlled circumstances | Distributed relief | Strategic continuity | Concentrated support |
| --- | ---: | ---: | ---: |
| Accessible rural population with modest industry | 60 | 25 | 15 |
| Major industrial war with several vital corridors | 25 | 60 | 15 |
| Ruined rural network with a supplied receiving city | 25 | 20 | 55 |
| Balanced capacity and mixed exposure | 40 | 35 | 25 |

Each row totals 100, so its entries also express the proposed percentages for that complete choice pool.
These percentages do not describe later decision clicks.
With a different surviving candidate set, normalization must use every remaining valid choice.

A priority switch requires a sustained change in practical circumstances.
AI should ordinarily retain its choice for at least thirty days, then compare the prospective benefit with the 25 political power cost and fourteen-day reorganization.
An active emergency can justify a change after the same legal cooldown.
Switching preserves every service debt, receipt and exposure interval.

## Geography and campaign scenarios

| Scenario | Expected response | Evidence to inspect |
| --- | --- | --- |
| Prepared cold country | Maintain functioning services, repair critical gaps and preserve its preparedness advantage | Equal anomaly applied, lower avoidable disruption, continued real upkeep |
| Tropical or desert country | Expand basic warmth and rest, use feasible local adaptation and prioritize unfamiliar cold failures | Exposure reflects actual preparedness and access, without identical outcomes for every climate |
| Industrial country at war | Keep high-demand corridors and worker services functioning while weighing military fuel diversion | Genuine fuel competition, visible rural gaps and ordinary night-fighting advantages |
| Small island | Protect its working port and actual deliveries, seek assistance when affordable shipments exist | Complete sea quote, convoy availability and measured arrival |
| Small inland country without a free factory | Use a smaller labor-supported service and repair package | Useful protected residents, no fictitious factory reservation |
| Occupied and divided territory | Validate both owner and controller and place costs on a lawful payer | Rejected ineligible humanitarian requests, no double coverage after movement or capture |
| Mixed human army with a surviving nocturnal family | Preserve ordinary civilian duties and apply only the proven family delta | Exact survivor selection and unchanged unrelated human units |
| Endless Night with damaged refuges | Maintain affordable sites, restore a shared route, then consolidate or evacuate an unsustainable site | Authorized upkeep, real reception and surviving residents throughout closure |

Run each relevant case through a baseline opening, an evolved opening, a long episode and an early Return.
Include existing famine and current displacement.
Their owners continue their own problems from the first day.

## Coverage and cost arithmetic

Protection measures operating capacity.
Consider 100,000 residents with warmth for 100,000, food access for 80,000, safety for 90,000 and sufficient rest capacity.
The protected contribution is at most 80,000 residents.
If 30,000 of them were already protected, the new net contribution is 50,000.
In a country with one million eligible residents, that is five percentage points.
Installing another lamp does not bypass the food bottleneck.

For Lifeline Reliability, a route delivering 60 of 100 required service units and another delivering 180 of 200 produce a demand-weighted value of 80.
The units represent internal comparable delivery evidence.
They introduce no player stockpile.
A disconnected second route delivering zero would reduce the same network to 20.
Repaired capacity must produce actual delivery before the value rises.

The cost check should reproduce A02's difficult-access Deep Freeze example of 5,300 fuel and 35 support equipment before a priority adjustment.
It must also reduce an overlarge package to the stated 225,000-resident example of 11,900 fuel and 79 equipment.
Evaluate rounding at the exact affordability boundary and after each factor changes.

A15's reference ninety-day authorization for 100,000 residents includes 18,000 fuel, 90 support equipment and thirty civilian factory-days of maintenance.
Verify its disclosed reservation schedule, 150 factory-day ceiling and maximum of two simultaneous factories per package.
A14's initial construction cannot pay this recurring obligation.
Competing programs must reserve distinct available capacity, and a smaller accepted scope must fit the supported whole-reservation mapping.

A bilateral example can debit 3,500 sender fuel, including 500 transit fuel, and consign 30 support and 100 infantry equipment.
If the transport owner proves delivery of 2,700 fuel, 27 support and 90 infantry equipment, those are the receiving credits.
The difference needs the owner's real consumption or loss account.
A partial arrival cannot credit the original cargo and then receive a refund for that same lost cargo.

## Evolution opening probabilities

The complete enabled opening pools follow part 2.

| Current Chaos | Baseline | Deep Freeze | Things in the Darkness | The Endless Night |
| --- | ---: | ---: | ---: | ---: |
| Below 400 | 100% | 0% | 0% | 0% |
| 400 to 599 | 60% | 40% | 0% | 0% |
| 600 to 799 | 20% | 40% | 40% | 0% |
| 800 or above | 5% | 15% | 30% | 50% |

Disabled or ineligible candidates leave the pool before normalization.
At Chaos 800 with Things disabled, the remaining weights 5, 15 and 50 total 70.
Their probabilities become approximately 7.14 percent baseline, 21.43 percent Deep Freeze and 71.43 percent Endless.
Endless installs only enabled stages.
With every evolution disabled, baseline receives 100 percent.

Later stage activation has constant-condition median anchors of ninety, 120 and 150 eligible days, subject to part 2's modifiers and thirty-day floor.
Under a fixed exponential-hazard interpretation, the corresponding thirty-day activation chances are 20.63, 15.91 and 12.94 percent.
The thirty-day median floor gives 50 percent over thirty eligible days.
Verify the intended distribution through the actual runtime mechanism.
A field named MTTH does not establish these probabilities by itself.

## Return distribution

For an unchanged median, the probability of Return during a future interval of delta days is:

\[
P(\text{Return in }\Delta)=1-2^{-\Delta/m}.
\]

The table gives conditional probabilities while the highest active stage and other relevant conditions remain unchanged.

| Highest active stage | Median days | Next 30 days | Next 90 days | Next 180 days |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 240 | 8.30% | 22.89% | 40.54% |
| Deep Freeze | 360 | 5.61% | 15.91% | 29.29% |
| Things in the Darkness | 540 | 3.78% | 10.91% | 20.63% |
| The Endless Night | 810 | 2.53% | 7.41% | 14.28% |

Stage changes alter future hazard.
They preserve the actual elapsed history and cannot reroll the opening or create a daylight gap.
For changing conditions, combine survival across the actual intervals.
Do not apply a single final-stage median retrospectively to the whole episode.

The model has an unbounded duration tail.
An 810-day median means half of constant-condition Endless episodes survive beyond 810 days.
Budgets, renewal options and ordinary recovery therefore need sustained-campaign tests.
Observation, country size, relief purchases and achievement progress leave the Return distribution unchanged.
A short episode can legitimately end before an expensive project or achievement completes.

## Creature, accounting and lifecycle checks

The cumulative Chaos comparison uses part 6's separate receipts.
Independent fully proven manifestation, service-failure and predatory-reach awards have a combined gross ceiling of 65.
Equivalent generic manifestation awards count within that total.
Full permitted service restoration and Return relief can reduce it by at most 25, leaving 40 in that complete example.
Shared deaths, migration and physical-damage accounting remain separate.
Test simultaneous threshold crossings, one physical cause presented under several labels, and repeat callbacks.
Only independent qualifying facts can earn both service-failure and predatory premiums.

Existing weaponized zombie packages already contain family-specific night bonuses, including the Wendigo package.
Record the baseline before applying any Sun delta.
Eligibility needs actual survivors, current family ownership and the correct holder.
Definitions, old flags, available templates and catalog rows cannot supply that proof.
[Creature sources](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/docs/systems/cbrn_warfare/chaos_unit_family_registry.md), lines 67 to 86 and 114 to 150, establish the owner distinction.

Test a pure nocturnal country, a human country hosting a derivative lot, a country with an extinct family and a saved episode after capture.
Human units keep their own modifiers.
Return removes precisely the Sun delta while retaining original family bonuses.
A missing vampire owner leaves that conditional interaction inactive.
The current source inspection found no verified vampire runtime.

Famine pressure, direct cold mortality and migration are separate receipts.
The current famine gateway validates positive owner facts and consumes its request inputs.
It does not provide an Event 124 episode replay guard.
The Sun caller must prevent repeated pressure for one cause before delegation.
See the [current gateway](https://github.com/klimPaskov/Chaos-Redux/blob/41bc4e5045a7b5c131be69dda2f08079d478634c/common/scripted_effects/famine_core_effects.txt), lines 695 to 721 and 783.

Test simultaneous callbacks, expiry during pause, capture during transit, Return during payment and stale reports answered after a new holder exists.
Verify conserved stocks, exact population transfers, once-only deaths and complete removal of temporary effects.
Keep native map darkness and all-hour night acceptance in the [acceptance matrix](124_sun_moves_away_acceptance_matrix.md).

## Evidence required before balance acceptance

Use identical saved scenarios and random conditions for baseline and candidate comparisons.
Report the full candidate pools, modifier factors, paid scope, failed gates and actual observations.
Keep sampled results distinct from the analytical probabilities above.

The minimum evidence covers exact-cost equality, unaffordable reduced scope, three occupied mission slots, no free factory, unsafe reception, mixed creature holders, Heat Wave conflict, disabled evolution bypass, evolved first entry, a long-tail episode and immediate Return.
Track useful served population-days, delivered essential demand, resource consumption, losses by their actual owner, interruption rates and unresolved obligations.

Source checks can verify arithmetic, references and transaction intent.
Native claims about scheduler behavior, control rendering, modifier scope or observed AI frequencies require native evidence.
Useful source and local checks can close otherwise completed work without waiting for a user-owned game run.
Unavailable observations remain stated evidence limits.
The required map-darkness and all-hour-night mechanisms remain feature-completion gates.
This planning session performed no game launch or native probability comparison.


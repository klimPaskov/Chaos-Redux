# Sandstorm: civilians, industry and recovery

## Exposure begins with residents

Civilian danger follows current residents in the affected land.
For each state, the calculation begins with its current native population immediately before a committed exposure interval.
Population that already departed through migration, died earlier or moved through another owner is not available to be counted again.
Sea cells contribute no civilian state population.

The moving footprint supplies the share of the state's populated geography affected over time.
Where the installed map provides no reliable population distribution below state level, the baseline approximation apportions current state population by covered land area.
That is explicitly a geographic model, not a claim that residents are uniformly distributed in reality.
Verified settlement weighting may replace that approximation only with a documented complete map input and a consistent method.
It cannot selectively invent city precision for favorable cases.

The public estimate sums unique current residents in the union footprint.
The casualty calculation separately integrates the time that each covered portion spends in each intensity band.
The estimate and the damage therefore come from the same geography while answering different questions.
A dense state produces more exposed residents than an empty desert state with equal covered area.
Partial coverage of a giant state does not automatically expose its entire population.

## Direct civilian consequences

The design includes suffocation and severe particulate exposure, exposure while trapped outside, accidents, transport disasters and structural collapse.
These causes form one direct Sandstorm casualty calculation.
They do not each roll an additional unbounded death event.
Contextual reports may emphasize the channels supported by actual conditions, such as a busy rail corridor or damaged buildings.

The first balance model separates three hidden risk shares.

| Risk channel | Share of baseline direct risk | What changes it |
| --- | --- | --- |
| Breathing and outdoor exposure | 70% | Valid mask quality and effective coverage, household retreat, prolonged severe conditions and proven heat overlap |
| Movement and transport accidents | 20% | Traffic restriction, an operated essential corridor, actual migration-route exposure and visibility |
| Structures, entrapment and related accidents | 10% | Local physical exposure, damaged facilities and protective activity reduction |

These shares are tunable game abstractions.
They are not medical or epidemiological estimates.
Civilian risk within migration cohorts already removed from the origin population belongs to the migration owner, using the supplied route hazard.
The state calculation does not add those travelers back into its residents.

## Mortality balance proposal

| Local band | Unprotected direct loss per 100,000 fully exposed residents per day |
| --- | --- |
| Weakening | 5 |
| Normal | 20 |
| Severe | 80 |
| Extreme | 250 |

These are deliberately fictional balance anchors for an extraordinary Chaos Redux disaster.
They establish a strong relationship between population, intensity and time without asserting real-world fatality rates.
For a short interval, scale the rate by the actual fraction of a day and the geographic exposure fraction.
Compute protection separately for the three risk channels and combine them once.
Intensity changes and overlapping fronts update the interval's aggregate dose before a population transaction occurs.

A six-hour severe exposure of 200,000 otherwise unprotected residents has a nominal expected loss of 40 people before actual-population clamping and fractional carry.
Five full severe days over two million exposed residents produce roughly eight thousand nominal losses before population decline and protection are accounted for.
The declining current population is reread for subsequent intervals, so a hand calculation using a fixed initial population is only an approximation.
The balance scenarios file includes exact labeled arithmetic examples.

Fractions of a person accumulate inside a state exposure receipt until a whole-person request is available.
The implementation must not round every tiny update upward.
Retiring an unfinished fractional remainder does not create one last death.
Loss is capped by actual available population above a protected minimum of 1,000 residents, or the state's smaller current population when it already lies below that minimum.
The minimum never creates residents.
The exact native conversion floors available people and rounds a required protected floor upward as specified by the corrected shared contract.

The population owner applies one physical debit and returns the measured actual difference between population before and after.
Only that actual result enters Deaths and historical attribution.
Current pinned code does not yet satisfy this measured-loss contract, which is a mandatory prerequisite identified in the evidence register.
Calling a function whose name contains exact is not sufficient proof.

## Protection and response

Household shelter means staying inside suitable existing buildings, sealing openings, reducing outdoor work and interrupting nonessential travel.
The model does not claim a counted stock of shelter beds or exactly known protected headcount.
Its proposed risk multipliers are 0.45 for breathing and outdoor exposure, 0.40 for movement accidents and 0.80 for structural and related risk after the response becomes effective.
That reduces the combined baseline risk to 47.5 percent while imposing the economic sacrifices in Part 05.
It remains available to countries unable to afford specialist equipment.

Shared civilian masks are actual protective-equipment crates.
Current owner documentation uses about 1,000 civilians per crate before fitting, filter and logistical effects.
Effective coverage is a percentage from zero to one hundred, while respiratory quality is a separate ceiling.
Full basic issue has a 55-point respiratory ceiling in the inspected owner.
Coverage must not be mistaken for an equal percentage reduction in deaths.

The proposed dust adapter reads verified effective coverage and weighted respiratory quality, takes their lesser value and converts it to a fraction R.
It multiplies only the breathing and outdoor component by 1 minus 0.65 times R.
At full basic issue, this component therefore has a multiplier of 0.6425.
This is a new dust-specific balance interpretation requiring the protection owner's acceptance and proof.
The current chemical protection calculator does not establish a dust result and must not receive a fabricated chemical class to obtain one.
Automatic distribution, actual stock debit, fitting, filter wear and controller transfer remain the shared mask owner's responsibility.

Household retreat and valid masks can combine because they address different circumstances within the same component model.
All protection together retains at least 25 percent of the comparable unprotected direct Sandstorm risk before cross-hazard amplification.
This floor prevents a fully protected district from becoming completely immune to extreme dust, transport accidents and structural danger.
It is an event balance floor, not a claim about protective equipment in reality.

Evacuation can reduce exposure more decisively by moving residents out of the threatened geography.
It requires actual safe routes, destination capacity and population conservation through the migration system.
Leaving a state does not count as a death.
Returning after the storm must follow that owner's settlement and return rules.

## Heat Wave and Acid Rain overlap

Severe or extreme Heat Wave in the same exposed land and time interval raises direct Sandstorm risk by a proposed 25 percent.
Acid Rain overlap raises it by a proposed 15 percent where the companion owner confirms an acute affected footprint.
Both together are capped at a 35 percent combined Sandstorm amplification.
The interaction expresses compounded exposure and harder rescue or movement.
It does not assert a newly invented chemical reaction or transfer ownership of the companion hazard's ordinary effects.

Each owner keeps its own actual losses and cause accounting.
The Sandstorm calculation includes its bounded interaction once and records the overlap receipt.
The companion owners must not add the same interaction premium a second time.
Missing or stale geographic proof produces no guessed overlap bonus.
A country-level disaster flag is insufficient when the storm is crossing only one part of the country.

## Temporary industrial disruption

| Local output or activity | Weakening | Normal | Severe | Extreme |
| --- | --- | --- | --- | --- |
| Productive factory capacity or equivalent verified local output | −15% | −35% | −60% | −80% |
| Construction progress | −20% | −45% | −70% | −85% |
| Resource extraction | −10% | −25% | −50% | −70% |
| Local supply throughput | −15% | −35% | −60% | −80% |

Sand infiltrates factories, engines, workshops, warehouses, rail facilities and machinery.
The implemented native representations may be factory availability, local output, construction, extraction, supply and actual building damage.
The writing must describe the representation that actually exists rather than inventing a new warehouse building.
An output modifier must not be described as deleting ore deposits or permanently removing factories.

Partial geographic coverage scales these local consequences consistently.
Important facilities at a verified covered province may receive a more precise result when the map supports it.
The mechanism cannot use a national production penalty simply because the state belongs to that country.
Local disruption can still propagate through the game's ordinary supply and production dependencies.

## Physical damage from intensity and duration

Damage accumulates after meaningful exposure and uses existing intact facilities.
The following starting anchors describe the proportion of exposed working capacity becoming repairably damaged per further full day after its grace period.
They must be translated into verified native building and railway behavior during implementation.

| Band | Exposure before damage accumulation | Industry and airfields | Infrastructure | Rail segments |
| --- | --- | --- | --- | --- |
| Weakening | No ordinary physical damage pulse | 0% | 0% | 0% |
| Normal | 48 hours | 1% per day | 2% per day | 2% per day |
| Severe | 24 hours | 3% per day | 4% per day | 5% per day |
| Extreme | 12 hours | 7% per day | 8% per day | 10% per day |

Only exposure beyond the qualifying grace contributes to that damage rate.
Mixed intensity uses a forty-eight-equivalent-hour grace, with each normal hour contributing one, severe hour two, extreme hour four and weakening hour zero.
Only the portion of an interval beyond that threshold receives the current band's damage rate.
This makes forty-eight normal hours, twenty-four severe hours and twelve extreme hours equivalent for first physical damage, while alternating bands cannot repeatedly claim fresh first-contact damage.
The first implementation should preserve one continuous-passage receipt until the state has been fully clear for at least forty-eight hours.

One passage caps newly damaged capacity at 40 percent of exposed working industry and airfields, 45 percent of infrastructure and 60 percent of rail capacity available at that passage's entry.
Already damaged capacity is not available to damage again until actual repair restores it.
A later returning passage can cause new damage to the remaining or repaired facilities under a new valid receipt.
Building levels never become negative, and a state with no relevant facility receives no substitute damage elsewhere.

Machinery protection reduces the physical damage rate and cap contribution for facilities actually covered by the completed preparation.
It does not undo earlier damage.
Railway damage must identify actual exposed segments and preserve a segment already damaged by another disaster.
Storm expiration cannot repair it by clearing a modifier.

## Recovery

Temporary storm effects end when the union footprint clears the relevant scope.
Weather penalties cannot linger merely because an aftermath mission remains open.
Normal industrial operation returns only to the capacity still working.
Repairs, reconstruction priorities and supply recovery continue through their proper owners.
Organization, equipment losses, population losses and issued shared protection are not rolled back.

Aftermath choices prioritize real repair queues and route restoration.
They can commit existing civilian factories or equipment to speed work where a verified native mechanism supports it.
They cannot award free building levels, recreate killed residents or refund equipment already consumed during a successful response.
If the front returns before recovery finishes, the same damaged facilities and remaining population face the new passage.
Recovery tracking preserves separate actual damage receipts for each passage and other known causes within the same native capacity pool.
An accepted shared measurement adapter allocates each verified actual repair proportionally across the known remaining damaged amounts, capped by each receipt's remaining amount.
The allocation includes other owners and later storm passages, so one repair cannot be credited in full to several achievements or missions.
Unresolved competing damage, demolition, new construction or an unexplained capacity change receives no claimed Sandstorm repair credit until its meaning is established.
The native repair continues normally while an unproven achievement or mission observation remains an explicit tracking gate.

## Longer consequences and shared systems

Food disruption can become famine only when the famine owner receives a valid measured pressure and duration path that satisfies its own stages.
A few dusty days do not directly create a full famine stage by label.
Migration receives actual route danger, state safety and reception constraints without a parallel Sandstorm displacement meter.
Shared Air Cleanliness may receive a bounded particulate contribution through an accepted owner adapter.
When the wall clears, future local emissions stop.
Previously accepted shared atmospheric contribution follows that owner's recovery rather than being subtracted by a guessed Sandstorm withdrawal.

An already active [Inflation episode](../100_inflation_specs/100_inflation_spec_part_2_economic_balance.md#supply-disruption-during-and-after-a-storm) can read the same verified present shortage, damage and repair facts for the country controlling the affected facilities.
Event 100 owns their national ratio, pressure family, cap and review, and a forecast or dust label supplies no guessed price pressure or new episode.
The controller chooses how much useful capacity to protect and repair while managing its existing monetary or fiscal restraint.

M3 and Inflation's productive restoration can observe one qualifying native repair, retaining its proportional attribution and physical result once.
Starting Inflation's optional repair support still requires its own disclosed allocation and minimum paid term.
Clearance leaves remaining damage intact, and a control change moves the current facility assessment without transferring the old government's paid policy or resetting either owner's history.

These longer consequences can outlast the weather because their physical or shared-system causes remain.
The local report links remaining damage to the actual repair location and the owning system, while Inflation explains its own current economic cause.
AI reevaluates useful repair and protective commitments from remaining facilities and current authority rather than prolonging a weather response to cure a price index.

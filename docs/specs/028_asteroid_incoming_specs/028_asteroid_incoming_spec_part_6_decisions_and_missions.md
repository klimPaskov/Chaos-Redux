# Asteroid Incoming, Part 6: Decisions and Missions

Status: implemented, with the mission-failure simplification (README Open question 2) and the global-mitigation revision (Part 4) proposed.
Decision and mission identifiers are in `common/decisions/028_asteroid_incoming_decisions.txt`; the [overview](../../events/028_asteroid_incoming/overview.md) documents their helpers.

## Presentation

Event 028 uses one ordinary decision category, `asteroid_incoming_recovery_category` ("Asteroid Recovery"), with a static category picture and no dedicated scripted GUI.
The category shows only what drives the next choice.

The header carries at most four values:

- **Dust**: the current global stage.
- **Protection**: the country's protection tier.
- **Recovery**: the national recovery phase (active recovery, recovery burden, burden extended after a failed mission, recovery legacy, lasting recovery legacy, recovery complete, or none required).
- **Craters**: under Extraordinary Minerals only, whether the country controls the main crater and how many fragment sites it controls.

Raw formulas, per-state ledgers, price multipliers and mitigation points stay internal or in concise tooltips.
The category is hidden for countries with no local damage, no active dust and no crater interest.

## Phases

| Phase | Who sees it | Actions |
| --- | --- | --- |
| Emergency | Countries with a live local emergency (Part 3) | Deploy Mobile Hospitals, Open an Emergency Rail Corridor, Clear Unstable Debris, Distribute Emergency Filters |
| Reconstruction | States whose local emergency is resolved | Rebuild the Supply Spine, Restore Outer-Ring Industry, Rehouse Displaced Workers |
| Dust protection | Every ordinary country while dust is active | Harden Factories Against Dust, Protect Transport Reserves, Join the Observation Network |
| Crater competition | Under Extraordinary Minerals, once the country's own emergency and reconstruction work is closed | One owned-site step and one rival-site step |

Accepted decision (basis: user-granted design authority, 2026-10-04 Crater actions): crater competition does not wait for dust to clear, because dust can outlast most wars.

Each state-targeted action lists only its highest-ranked affordable state, so a phase shows at most one card per action and the late surface stays within five primary actions.
Emergency ranking is live rescue burden, then profile, then population; reconstruction ranking is profile, then the infrastructure and railway gap against the pre-impact snapshot; ties fall to the lower state id.
An unaffordable high-priority state cannot hide a cheaper valid one.

A country runs one pending paid state project at a time; other countries keep independent targets.
Finish callbacks recheck the reserved state and current control, apply the work and always release the slot.

## Emergency actions

The first three actions each resolve the target state's local emergency: its impact-zone damage ends, its rescue-period deaths stop and reconstruction opens there.
They differ in what they rebuild and which mission they can start.

| Action | Effect |
| --- | --- |
| Deploy Mobile Hospitals | Restores part of the state's infrastructure and supply capacity; can start Keep the Rescue Route Open |
| Open an Emergency Rail Corridor | Restores emergency transport through the state and protects national transport reserves; can start Keep the Rescue Route Open |
| Clear Unstable Debris | Restores part of the state's infrastructure and industry; can start Stabilize the Damaged Zone in the two worst-hit states |
| Distribute Emergency Filters | Basic dust protection; hidden while no dust is active |

No action restores the dead.
The medical stance makes the first mobile-hospital deployment cheaper; the transport stance makes the first rail corridor cheaper.

## Reconstruction actions

| Action | Effect |
| --- | --- |
| Rebuild the Supply Spine | Restores network capacity in the state; can start Reconnect the National Network |
| Restore Outer-Ring Industry | Restores factories and dockyards in the state; can start Restore the Outer Ring |
| Rehouse Displaced Workers | Restores housing capacity; for the original target, can start Rebuild the Regional Economy |

Each action restores only a share of what the impact destroyed, never above the pre-impact level, and never in the main crater.

## Dust protection actions

Protection tiers and their effects are defined in Part 4.
Each action is one-time per country, is priced by the current dust stage, and lapses without refund if it finishes after the sky has cleared.

## Crater actions

Owned sites advance through three steps, rival sites through three, and the category offers the highest-profile ready owned site and one ready rival site.

| Step | Effect |
| --- | --- |
| Secure the Crater Perimeter | Defence and attrition benefits at the site while the securing country controls it; unlocks the survey |
| Survey Extraordinary Material | Reveals the site's material profile and grants one research bonus in the matching field |
| Fortify Crater Access | One infrastructure level and one fort level in up to two controlled access states; each access state once across all sites |
| Reconnoitre a Crater Site | Army intelligence on the site's controller; names the material once someone has surveyed it |
| Disrupt Extraction Routes | A timed local-supply penalty for the enemy controller in up to two hostile-held access states |
| Prepare a Crater Offensive | A timed attack bonus for the actor's attacks into the crater state |

Rival actions target only the persistent crater-site array, never the whole map.
The two timed rival operations can be bought again after their effects expire.
None of these actions adds armour.

Accepted decisions (basis: user-granted design authority):

- A "supplied garrison" is at least one of the actor's divisions in the crater state, or in a neighbouring ordinary state it controls that has a rail connection to its capital, because no trigger reads a division's supply status.
  This proxy differs from a real supply reading; the difference is disclosed, not hidden.
- A secured perimeter belongs to the securing country and lapses when control changes; the survey and its research use stay on the state, so control switching cannot farm them.

## Missions

Missions give a player government concrete, named construction goals after a project.
Accepted decision: AI countries receive every project effect but no mission contract, because the AI cannot plan construction toward a mission target.

| Mission | Started by | Duration | Objective |
| --- | --- | ---: | --- |
| Keep the Rescue Route Open | Mobile hospitals or rail corridor | 150 days | The named state meets its infrastructure, railway and supply-hub targets and, if it was rail-linked before the impact, is linked to the current capital |
| Stabilize the Damaged Zone | Debris clearing | 120 days | The two worst-hit damaged states captured at activation both meet their targets; success resolves their local emergencies |
| Reconnect the National Network | Supply spine | 180 days | Every damaged state that was rail-linked before the impact is linked again, every damaged state meets its infrastructure target, and the saved industrial hub is linked; success closes emergency work everywhere |
| Restore the Outer Ring | Outer-ring industry | 270 days | No held state keeps Outer Shock Zone or Light Fragment Damage, and every held major-ring state meets its infrastructure and factory targets |
| Rebuild the Regional Economy | Rehousing, original target only | 365 days | Factory, infrastructure and railway totals across surviving damaged states reach 75 percent of their pre-impact totals |

Repair targets are 60 percent of each state's pre-impact levels, so a state is never asked for a building it never had, and rail objectives ask only for links that existed before the impact.
These scopes are accepted G6 dispositions: they restore the network the impact broke and keep recovery possible during territorial change, instead of demanding a railway in every damaged state.

Rules:

- At most two missions run at once, and running missions do not block projects.
- Each objective can be met from 45 days before the timeout, and the mission completes as soon as its conditions hold after that day.
- A mission whose named state leaves the country's control ends without penalty.
- Network, outer-ring and regional-economy contracts are one-time per country; later repair work cannot reopen them.

### Success

Every success grants the recovery legacy in place of the national burden.
The legacy of Rebuild the Regional Economy is lasting and survives closeout; the others end with the burden they replaced.
Network and outer-ring successes feed Government Beyond the Crater.

### Failure

An expired mission currently applies, once per named state:

1. a rescue-failure Deaths entry of 1 percent of the state's population (2 percent in the catastrophic ring or at a fragment centre), capped at 25,000;
2. the return of the state's ended impact damage for 90 days, reopening its local emergency when the damage is emergency-class;
3. a state failure-pressure modifier;
4. the full national recovery burden for 90 days, setting aside any legacy;
5. a 25 percent repair-price surcharge for 180 days.

README Open question 2 proposes dropping the surcharge, keeping the first four consequences.

## Prices and costs

- Every affected non-crater state carries one stored price quote that the cost text, cost check, reserve check and payment all read, so the displayed price always equals the debit.
  The multiplier rises with the state's profile and its population loss, stays between 1.00 and 2.50, and refreshes at impact, monthly, on control change and when a surcharge starts or ends.
- Dust projects read one global quote scaled by the dust stage; crater operations have flat prices.
- No action has more than four spendable cost types, and native custom costs show at most three inline values with the full cost in the tooltip.
- Costs favour equipment, trains, trucks, fuel, manpower, convoys and civilian-factory time; command power stays small.
- A control, route, division or threshold condition is a requirement, never a hidden fifth cost.
- Every action keeps reserve floors (manpower, support equipment, trucks, trains, fuel, convoys, command power) for players and AI alike; strict equality with the floor is ineligible.
- Blocked actions show a reason-specific tooltip and the exact target state.

## AI

Every action has an `ai_will_do` path with reserve floors.
The normal priority order is:

1. prevent continuing deaths;
2. restore supply to the capital and fronts;
3. reconnect populated damaged states;
4. protect national production from dust;
5. restore surviving industry;
6. secure and defend crater sites;
7. contribute to global observation once national needs are covered.

The AI never spends its last trains, support equipment, fuel or construction capacity during a war it is losing.
Probability scenarios are in Part 7.

## Cleanup and exploit controls

- Obsolete phases and actions hide when their conditions end; dust actions hide at zero dust.
- A state target clears when the state changes controller or becomes invalid, and cancellation, lost control and annexation release only that country's receipts.
- A one-time action cannot repeat on the same state, and no repair exceeds the pre-impact or allowed level.
- Main-crater buildings can never be rebuilt.
- Annexing a damaged state keeps its recovery burden and does not reopen completed rewards; annexation clears the lasting legacy flag so a released country does not regain it.
- Crater security and survey cannot be farmed through control switching.
- Global mitigation is capped (Part 4).

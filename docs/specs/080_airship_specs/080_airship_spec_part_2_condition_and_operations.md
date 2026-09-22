# Event 080: Airship
## Part 2: Condition and operations

## Condition

Condition ranges from 0 to 100. It represents the ship's ability to complete another leg safely, including its engines, structure, controls, and accumulated damage. Small incidental faults should not each create a new permanent subsystem value.

| Condition | Meaning | Practical response |
|---|---|---|
| 76 to 100 | Sound | Normal operation and optional experimentation |
| 51 to 75 | Worn | Plan service before a difficult stretch |
| 26 to 50 | Damaged | Major repair is strongly preferable |
| 1 to 25 | Critical | Seek a landing or knowingly accept a high chance of loss |
| 0 | Flight cannot be sustained | Resolve the crash or a previously secured grounded evacuation |

A grounded ship at Condition 0 is not automatically thrown into the air to create a crash. If it is already safely moored and evacuated, the result is a grounded write-off and an aborted voyage. Reaching 0 while airborne causes a crash. A fatal attack or structural accident can destroy a ship above 0.

The proposal applies 5 Condition of normal wear after each block of ten completed flight steps. Ground time does not generate this flight wear. It can still have a specific incident, such as a failed repair or fire at a mooring site. Routine competent service at an original planned stop restores 10 Condition, once for that visit, up to 100. It cannot be repeated by opening and closing the visit or by circling the stop.

## One flight exposure per movement window

A ship should not make a separate full crash roll for every country, aircraft wing, state, and passenger story on the same leg. Each two-day flight window has one combined operational exposure assessment. A single incident is selected if that assessment succeeds.

Proposed incident probabilities are 5% while sound, 10% while worn, 20% while damaged, and 35% while critical. Severe weather adds 5 percentage points. A nearby active combat area adds 5 points, or direct hostile interception adds 10 points instead. An active experimental trial adds 5 points. A known unsafe approach adds 5 points. A previously ignored safety warning can add another 5 points for the next relevant exposure. The combined chance is capped at 60%.

Modifiers require evidence at the current location. A host being at war on another continent does not by itself qualify as a local combat zone. A historical enemy who is currently friendly does not acquire an invisible attack bonus. Anti-aircraft concentrations and hostile aircraft affect the local combat category, without producing an unlimited additive probability.

When an operational incident occurs, Condition determines its severity mix. Proposed conditional weights are shown below. These are design targets, not results of a completed probability-tool audit.

| Condition | Minor incident weight | Serious incident weight | Fatal incident weight |
|---|---:|---:|---:|
| Sound | 800 | 195 | 5 |
| Worn | 650 | 325 | 25 |
| Damaged | 450 | 450 | 100 |
| Critical | 200 | 500 | 300 |

Each row totals 1,000. The fatal weight is conditional on an incident, not the unconditional crash chance. A minor technical incident usually removes 10 Condition. A serious incident usually removes 25 and opens a response. Circumstances can substitute a specific injury, delay, or diplomatic consequence. The same incident must not also be selected independently through the flavour pool.

Repeated exposure matters. Even a small per-leg fatal chance accumulates across 121 legs. The separate probability review therefore includes complete voyages, repairs, delays, evolution exposure, and deterioration. It does not approve a balance model by looking only at one healthy leg.

## Incident families

| Family | Eligibility | Minor result | Serious result | Fatal result |
|---|---|---|---|---|
| Mechanical | Any flight | A named system loses efficiency, Condition loss | Engine or control fault requires landing or a repair extension | Airborne loss of control |
| Weather | Actual adverse-weather context or a documented event hazard | Delay and light damage | Forced approach or structural strain | Destructive storm encounter |
| Landing | A real scheduled or emergency approach | Damaged fittings and delayed departure | Ground collision, injuries, repair work | Crash at the approach state |
| Security | A prior security concern or an eligible hostile action | Investigation and disrupted service | Damage, detention, or an emergency | Confirmed destructive act against the ship |
| Combat | Active local combat or a deliberate hostile interception | Warning fire or forced course change | Damage, capture attempt, forced landing | Shootdown or destroyed emergency approach |
| Experimental | A current live trial | Invalid measurements or a temporary fault | Failed test and serious damage | A destructive trial failure |

The default eligible-family weights are mechanical 40, weather 25, landing 15, security 10, combat 25, and experimental 20. Ineligible families contribute nothing and the remaining weights are normalised. A weight is not a percent. These weights choose the type of an already selected incident. They do not create an additional crash roll.

## Standing orders

The United States selects one of three standing orders. Changing orders is free at a stop and takes effect for the next unstarted exposure. It cannot retroactively alter a result that has already been drawn.

| Policy | Behaviour | Tradeoff |
|---|---|---|
| Safety first | Automatically accept a suitable basic emergency landing and stop trials below 51 Condition | More delays and fewer eligible demonstrations |
| Keep the timetable | Continue with routine faults and request a decision for serious danger | Fewer automatic delays, more manual risk decisions |
| Prioritise the programme | Complete qualified scientific or ceremonial commitments while Condition permits | Greater exposure during optional activities and clearer warnings before unsafe continuation |

No policy forces a player to crash. An urgent response can override standing orders. Safety first cannot create an unavailable landing site, neutralise an actual attacker, or refill missing equipment.

## Service choices

The basic scheduled service is included in the visit. Extra work uses real resources and time. The following figures define the proposed relative price of each intervention. The decision and mission prompt requires exact native affordability and delivery validation.

| Service | Provider and proposed cost | Additional time | Result |
|---|---|---:|---|
| Patch repair | US or willing host, 25 support equipment and 250 fuel | 2 days | Restore 25 Condition |
| Major repair | US or willing host, 75 support equipment, 25 motorized equipment, and 500 fuel | 4 days | Restore 50 Condition and clear a repairable persistent fault |
| Specialist inspection | US, 25 Political Power and 25 support equipment | 2 days | Find or clear one eligible safety concern and remove the next unsafe-approach surcharge where causally relevant |
| Replacement supplies | US or willing host, 25 support equipment and 250 fuel | 2 days | Resolve a documented provision shortage, without granting Condition above ordinary service |
| Emergency evacuation | Host, 25 motorized equipment and 25 support equipment | 2 days | Remove selected survivors from an already grounded dangerous ship |
| Extended public programme | Host, 25 Political Power and 25 support equipment | 2 days | Improve the visit's cultural or commercial outcome if the site remains safe |

Prices scale with the physical ship form. Grand Tour uses twice the equipment and fuel of baseline service. Flying City uses five times the baseline equipment and fuel. Political Power costs do not scale automatically with headcount. A host sees the exact payable cost before accepting help.

Ordinary servicing requires an actual usable stop. A technical stop with a suitable workshop can perform major repairs. At a poor emergency landing ground, major repair takes an additional two days and needs 25 more support equipment before form scaling. No repair option is offered as payable when the selected payer lacks the required stockpile.

The United States can pay for work at a consenting host's site. Consent does not transfer free ownership of the host's industry. A denied request can produce a modest negotiated service, a diversion, or continued flight. It cannot erase the need for a real repair location.

Repairs are capped by the remaining damage. Paying for a patch at Condition 90 gives 10 restored Condition, with that cap clearly shown before payment. The AI does not buy such inefficient work without a separate reason, such as resolving a dangerous fault.

## Emergency responses

A serious airborne incident presents at most three immediate responses: a suitable emergency landing, a displayed damaged continuation, or a justified local diversion. Unavailable choices stay absent or explain their failure. An approach may still be dangerous, but the tooltip distinguishes approach risk from the risk of remaining airborne.

A warning does not freeze a multiplayer campaign. The default response is determined by standing orders and the actual available destinations. An urgent response window is one day, after which the displayed default resolves. A radio-loss or rescue mission can last longer because it represents work already underway.

A damaged continuation accepts the current incident's resolved damage and proceeds into the next exposure. It does not make a second immediate fatal roll merely because the player clicked continue. A landing choice creates its next approach exposure when the approach actually occurs. This preserves a readable connection between time, actions, and risk.

## Missions and delayed work

| Mission | Normal duration | Owner | Success | Failure or expiry |
|---|---:|---|---|---|
| Extra repair | 2 or 4 days | Payer, with host consent | Apply the purchased repair once | Refund undelivered work only under the defined interrupted-service rule |
| Find missing visitors | 4 days | Current or recent host | Return the actual people or establish that they left safely | Resolve a bounded missing-person outcome, not automatic death |
| Restore contact | 4 days | United States | Recover communication and reveal actual position | Expand to the single eight-day search window |
| Search for the missing ship | 8 days | United States with eligible assistance | Locate survivors, a grounded ship, or wreckage | End as unresolved loss with no fabricated confirmed casualties |
| Ground rescue | 4 days | Impact controller | Recover the recorded living casualty pool | Apply only newly proven deaths among that pool |
| Passenger release | 10 days | Captor and United States | Return or settle detained people through actual population movement | End the voyage with surviving people still in a tracked custody settlement |
| Experimental trial | Five completed flight steps | United States | Resolve a valid trial in its family | Interrupted trials yield no successful-trial reward |

Short missions are intentional because the basic voyage step is two days. The longer shared disaster recovery remains the responsibility of the disaster system. Airship does not replace it with a second competing fire-recovery panel.

A partly delivered service consumes only its documented delivered share. The simplest safe implementation is payment on a committed work order with a single declared interruption policy. It must not support repeated cancellation refunds after benefits have already been granted. A country losing control of the work site cannot charge for new work there.

## Action budget and AI

Underway, show standing orders, the next-stop assistance request, and a currently eligible experiment. At a stop, show repair, the local programme, passenger handling, eligible experimentation or refit, and departure. During an emergency, replace routine actions with the relevant response. This keeps the main action set at three to five rather than showing every possible decision throughout the voyage.

The United States AI plans ahead using the next known route exposure and actual service opportunities. It repairs before a long hazardous stretch, stops trials when seriously damaged, and safely aborts when no credible recovery exists. A wealthy AI can fund host work. A poor AI can shorten ceremonies and abandon optional trials without being forced into an avoidable loss.

A host AI compares the scale of the request with its real resources and current local pressures. Friendly and commercially interested hosts prefer ordinary reception. Occupied, fighting, or badly supplied hosts prefer a brief visit and strict ground control. A country already fighting the United States can choose interception or impoundment where the ship is actually reachable. Mere low opinion does not make deliberate destruction the default.

AI priorities are contextual action preferences. They must be checked through full-sequence probability and decision evaluation. They are not literal percentages attached to an `ai_will_do` score.

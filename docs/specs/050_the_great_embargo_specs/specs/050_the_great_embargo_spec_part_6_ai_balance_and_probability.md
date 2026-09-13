# Event 050: The Great Embargo

## Part 6: AI strategy, balance, probability, and multiplayer behavior

This file defines intended behavior and named audit scenarios. It does not claim measured engine probabilities. Exact weights require repository inspection and the mandatory HOI4 probability workflow during implementation.

## AI design goal

AI countries should understand what the embargo threatens, which response matches their economy and politics, and when a profitable action has become reckless.

The AI must avoid two common failures:

- every target choosing the same response regardless of resources, strength, or ideology
- outside countries joining or leaving according to relations alone while ignoring trade capacity, rivalry, faction position, and enforcement risk

## Target selection AI and probability

Target selection is a weighted pool, not AI choice. Its weights should create a useful mix of player experiences and world events.

### Player-country pool

Player countries should have a meaningful chance of selection whenever eligible. The player pool should be treated as one class so multiplayer does not multiply the global player chance with each added participant.

### Major-country pool

Valid majors should normally receive comparable base weight. Modifiers can raise weight for countries that are economically important, diplomatically isolated, publicly condemned, or involved in a current dispute.

Target dependence should not dominate target selection. The event can strike a self-sufficient power and create a political contest even when economic damage is moderate.

### Exclusion priority

An active Event 50 target, invalid government, special Chaos actor, actual nonhuman actor, or country outside normal civilian systems must receive zero effective weight.

## Target response evaluation

The AI should estimate five broad needs:

- immediate shortage danger
- time available before severe economic damage
- diplomatic room to split the coalition
- military ability to seize or defend resources
- political ability to sustain defiance

### Self-Sufficiency preference

Raise preference when:

- domestic resource deposits can be expanded
- the target has civilian construction capacity
- the embargo is expected to last
- the country is at peace or can protect project states
- current shortages are important but not immediately fatal
- prior self-sufficiency investment reduces completion cost

Lower preference when:

- the target is already collapsing militarily
- no useful domestic project exists
- construction is fully committed to survival
- the crisis is likely to end through a near-term settlement

### Smuggling preference

Raise preference when:

- valid land or sea routes exist
- the target has convoys, fuel, equipment, or intelligence capacity
- relations with likely hosts are good
- Pressure is high enough that relief is valuable
- the target can tolerate exposure

Lower preference when:

- Evolution I enforcement is strong
- previous routes were exposed
- the only hosts are coalition hardliners
- the target lacks shipping or border access
- the target is close to an accepted settlement

### Neutral Intermediary preference

Raise preference when:

- a strong neutral has relevant resources or route capacity
- the target can afford a commercial concession
- the neutral is weakly aligned with the coalition
- the target is too weak for defiance or military expansion

Lower preference when:

- the proposed price exceeds expected relief
- the route is already under secondary pressure
- the neutral has no practical delivery path
- the target expects the coalition to collapse soon

### Diplomatic Concessions preference

Raise preference when:

- dependence is critical
- military strength is low
- the requested concession is limited
- the target is losing another major war
- the convenor and core enforcers are open to settlement
- stability cannot sustain prolonged isolation

Lower preference when:

- the concession threatens national survival
- the target has strong replacement routes
- hardliners will reject the offer regardless
- the government has committed to defiance

### Defy the World preference

Raise preference when:

- the regime has high stability or strong legitimacy
- the country is ideologically hostile to the coalition
- domestic resources are adequate
- the target is militarily strong
- the public justification is weak or can be portrayed as persecution
- concessions would threaten the regime

Lower preference when:

- shortages are critical
- the government is unstable
- the army depends on imported fuel
- a favorable settlement is available
- the country is democratic and public support is collapsing

### Resource Seizure preference

Raise preference when:

- Pressure is severe
- a nearby vulnerable state controls an essential resource
- the target has sufficient forces, fuel, supply, and equipment
- the target is aggressive or already pursuing expansion
- diplomatic replacement routes have failed
- coalition intervention risk is limited

Lower preference when:

- the resource owner belongs to a stronger faction
- the target is already losing a war
- supply to the region is poor
- the target cannot sustain the preparation costs
- the desired resource would still be inaccessible after conquest
- the ultimatum would create an obviously suicidal conflict

## AI strategy archetypes

### Import-dependent maritime power

Priorities:

1. protect fuel and convoy access
2. secure a neutral port or shipping intermediary
3. build synthetic substitutes
4. seek concessions when route closure becomes critical
5. consider resource seizure only with strong naval or regional capacity

### Self-sufficient continental power

Priorities:

1. accept moderate isolation
2. use defiance or selective self-sufficiency
3. split the coalition through diplomacy
4. avoid expensive concessions unless Pressure remains severe

### Weak isolated major

Priorities:

1. seek intermediary access
2. offer bounded concessions
3. complete fast emergency projects
4. avoid defiance and resource war unless regime survival requires them

### Strong aggressive major

Priorities:

1. use defiance and emergency production
2. develop domestic substitutes
3. threaten nearby resource regions when the military case is favorable
4. exploit rival embargoed countries under Evolution II

### Democratic trading state

Priorities:

1. maintain public support and commercial access
2. use lawful intermediaries and negotiated settlement
3. invest in visible self-sufficiency
4. use defiance only during a clear external threat
5. avoid secret trade when exposure would cause a major political crisis

### Ideological siege state

Priorities:

1. convert the embargo into mobilization
2. build autarky
3. use smuggling through sympathetic partners
4. reject symbolic concessions
5. accept practical concessions when military survival is at risk

## Participant AI

Outside-country AI should evaluate:

- ideology and relations with the target
- relations with the convenor
- faction alignment
- rivalry and strategic threat
- economic exposure to the target
- own dependence on coalition markets
- resource and shipping role
- war state and military distraction
- expected profit as an intermediary
- secondary-sanction risk
- public justification and Condemnation
- target ability to retaliate

### Join and remain committed

High priority for threatened neighbors, ideological rivals, faction partners of the convenor, and countries with low trade cost.

### Conditional commitment

High priority for states that support the goal while depending on target trade or fearing escalation.

### Secret trade

High priority for commercially capable countries with strong target links, weak coalition loyalty, and a route that can remain hidden.

### Open defection

High priority when coalition fatigue is high, the target has accepted concessions, the participant's trade losses are severe, or the convenor has become weak.

### Intermediary role

High priority when profit is large, route capacity exists, the country can resist coalition pressure, and the target can pay.

### Secondary enforcement

High priority for hardliners with market power, intelligence capacity, or control over shipping and finance. Low priority for participants that depend on neutral trade.

## AI action cadence

AI should not evaluate every possible country and action every day.

Use event-owned registered ledgers and bounded pulses:

- target response review when the target gains a new stage, decision availability, or urgent shortage
- participant review at scheduled coalition reviews
- intermediary review when an offer arrives or exposure changes
- settlement review when a valid package exists
- Evolution II doctrine review when one country holds several roles

This keeps the system reactive without broad daily scans.

## AI resource budgeting

An AI target must preserve minimum survival reserves before paying decision costs.

It should not spend:

- the last fuel needed for an active front
- all convoys needed for supply
- equipment needed to reinforce a collapsing army
- civilian capacity required to repair critical infrastructure
- political power reserved for a more urgent law or crisis action

A powerful response should still be available when the cost is strategically justified. The AI budget should prevent self-destruction, not block all risk.

## Balance targets

### Crisis impact

At medium Pressure, a low-dependence target should notice reduced flexibility and foreign access. A high-dependence target should make immediate production choices.

At severe Pressure, the event should alter war and economic planning for every target. It should not make a prepared self-sufficient major unable to function.

At near-total isolation, a critically dependent target can face a major emergency. The target must still have at least one plausible response path unless its own prior decisions and world state have closed them.

### Decision strength

Each major response should be strong enough to justify its cost and timing.

- Self-Sufficiency gives durable mitigation with slow payoff.
- Smuggling gives fast relief with exposure risk.
- Intermediaries give reliable relief at a lasting price.
- Concessions can end the crisis while sacrificing policy or strategic value.
- Defiance gives temporary political and economic resilience followed by exhaustion.
- Resource Seizure creates a genuine military route with escalation risk.

No response should dominate every target profile.

### Pressure pacing

Pressure should usually move in visible steps and avoid constant one-point noise. Important actions can move it immediately. Scheduled reviews can produce larger reconciled changes.

A normal campaign should allow:

- early coalition collapse when the opening group is weak
- a stable middle crisis lasting several review cycles
- severe escalation after failed adaptation or exposed evasion
- late fatigue even when no settlement is reached

### Repeatability balance

Permanent self-sufficiency gains and long-lived concessions need caps. A country repeatedly targeted over many years should become more resilient through real investment. It should not receive unlimited free resources or permanently accumulate harsh crisis penalties.

## Probability audit contract

Every weighted surface requires the project audit sequence:

1. inspect the full candidate pool with `hoi4.probability_inspect`
2. define named scenarios and all external state
3. evaluate or sweep the baseline
4. let the owning implementation agent apply the intended weights
5. use `hoi4.probability_compare` against the same scenarios
6. render the result when a matrix or sensitivity view improves review

The probability auditor remains read-only. It does not select the desired balance target and does not patch source.

### Surfaces requiring audit

- player versus major target-class roll
- country selection inside each target pool
- coalition convenor selection
- core-enforcer selection
- neutral-intermediary selection
- participant opening choice
- participant review choice
- target AI response selection
- smuggling outcome bands
- intermediary acceptance
- secondary-sanction target selection
- Evolution I pacing
- Evolution II target count
- additional target selection
- sanction-breaker cooperation choice
- settlement acceptance

## Required named probability scenarios

The full scenario matrix is stored separately. The minimum set covers:

- one eligible player and several majors
- several eligible players and several majors
- no valid player
- no valid major
- import-dependent major against a self-sufficient major
- active target excluded from repeat selection
- coalition built around a high-rivalry convenor
- friendly participant with high economic exposure
- neutral shipping power with strong intermediary capacity
- weak target at eighty Pressure
- strong aggressive target at eighty Pressure
- smuggling under baseline rules
- smuggling under Evolution I
- Evolution II with two open crisis slots
- Evolution II with one open crisis slot
- overlapping coalition roles
- coalition fatigue after twelve months

Exact, bounded, sampled, score-only, and unresolved results must be labelled separately.

## Multiplayer behavior

### Shared world state

Event 50 uses the shared global event system and global Chaos tier. Each crisis stores its own target and coalition state.

### Player targeting

The player pool receives one class weight. Adding players should not multiply the chance without a deliberate setting.

### Human outside roles

A human-controlled core enforcer or intermediary receives a timed choice. Ignoring the choice uses a visible default that preserves the current policy.

### Contradictory roles

Under Evolution II, a player can participate in several crises. Grouped reports and selected-target decisions should prevent popup and category spam.

### Ghost copy and presentation

Authoritative effects must apply once. Local presentation should show the relevant target, coalition, and Pressure to each player without duplicating global outcomes.

## Failure safeguards

- AI cannot choose invalid target countries.
- AI cannot pay hidden costs it does not possess.
- AI cannot start a smuggling route with no usable route.
- AI cannot offer concessions involving invalid states or dead actors.
- AI cannot prepare resource seizure against itself, an ally that should be excluded, or an unreachable target.
- AI cannot remain stuck in a decision category after crisis cleanup.
- AI cannot apply one crisis choice to every overlapping ledger unless the choice explicitly says so.

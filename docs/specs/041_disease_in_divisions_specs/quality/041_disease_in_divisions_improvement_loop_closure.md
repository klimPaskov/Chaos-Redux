# Event 41 improvement-loop closure review

## Review status

This closure review applies the Chaos Redux improvement-loop standard to the completed planning pack.

The dedicated project subagent runtime was not available in this environment, so `chaosx_improvement_loop_planner` was not actually spawned. This file records a parent-authored review using the supplied planner definition and skill contract. The implementation goal still requires the real planner to be spawned near completion in the repository runtime.

## Playable promise review

The event promise is clear and supported by the design:

- a real frontline military epidemic begins in a coherent sector
- the disease removes soldiers from duty and degrades combat readiness
- equipment remains separate from sickness
- the player chooses between operational momentum and containment
- logistics, field hospitals, sanitation, transport, supply, climate, and combat shape the outcome
- poor management can reduce one front toward half effective strength
- evolutions expand the same incident through military and civilian networks

The design does not depend on flat modifiers alone. Decisions change formation use, transport, production, supply routes, posture, and international access.

## Depth review

The event has enough depth for its Low cluster role:

- three hidden profiles create environmental variation
- one public pressure value keeps the player-facing system clear
- a bounded sector simulation supports real causes and consequences
- phased decisions create early, severe, and evolved responses
- resolution preserves recovery and aftermath
- Evolution I changes military transmission rules
- Evolution II adds a strict civilian-system handoff
- AI behavior has named strategic states and audit scenarios
- achievements cover clean containment, recovery from severity, coalition control, and War Plague prevention

The current scope matches a Minor Repeatable event and supports the complete playable promise without unrelated expansion.

## Connection review

The event connects to the existing systems that materially change its behavior:

- Deaths
- field hospitals and medical technology
- supply, infrastructure, railways, ports, trains, trucks, fuel, and convoys
- biological warfare and civilian outbreaks
- chemical contamination
- Air Cleanliness through the civilian outbreak owner
- famine and relief access
- migration and controlled medical reception
- natural disasters and bombardment
- event clusters
- Chaos History

Ownership boundaries are explicit. The design avoids a second civilian disease, famine, migration, contamination, or mortality framework.

## Player choice review

The strongest choices change the military situation:

- rotating formations weakens the front
- quarantine restricts movement and organization
- evacuation consumes transport and logistics capacity
- hospitals consume equipment, manpower, and civilian capacity
- sanitation depends on real route access
- offensive restriction sacrifices tempo
- fighting through preserves freedom of action and worsens disease
- district isolation, port closure, and sector abandonment create strategic costs

The action list is phased. The category should not become a permanent wall of buttons.

## AI review

The AI design distinguishes:

- early containment
- balanced action
- emergency control
- desperate operations
- rich and poor medical systems
- capital defense
- overseas theaters
- coalition fronts
- civilian spillover risk
- demobilization

The probability scenarios define expected ordering and threshold reversals. The implementation must still produce MCP evidence.

## Presentation review

The chosen presentation is proportional to the event:

- one static category picture
- one visible meter
- map highlights
- formation status
- concise tooltips
- milestone reports

A larger mechanic window would add layout and maintenance burden without improving the key decision. The event should keep the ordinary category presentation unless implementation proves that a required action cannot be communicated clearly.

## Anti-bloat decision

Broad expansion is not recommended after this specification. The current design has one strong loop, two clear evolutions, complete integrations, AI, assets, achievements, and acceptance criteria.

Further expansion should be limited to implementation findings, such as a safer manpower transaction, a required adapter, or a clearer decision presentation. New currencies, extra evolution stages, a separate civilian system, or unrelated country content would dilute the event.

## Design verification gates

The following questions belong to implementation verification, not further design expansion:

- which engine-supported mechanism can remove or block division manpower without equipment loss
- which existing military casualty helper should register fatal cases
- which current biological outbreak adapter should receive War Plague spillover
- which safe formation or node registry pattern best survives transfers and civil wars
- which exact HOI4 category picture and decision icon sizes are used by the current consumers

The coding prompt requires source, wiki, vanilla, and repository inspection before selecting these mechanisms.

## Closure recommendation

The planning loop can stop. Broad expansion would add maintenance and clutter. Implementation should proceed from this pack, then run the required specialist audits and one real improvement-loop closure pass before completion.

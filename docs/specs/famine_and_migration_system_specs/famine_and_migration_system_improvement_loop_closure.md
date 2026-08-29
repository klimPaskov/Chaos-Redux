# Famine and Migration Mechanics Improvement-Loop Closure Review

## Review status

This is a parent-authored design review using the `chaos-redux-improvement-loop` standard.

A callable `chaosx_improvement_loop_planner` runtime was not available in this environment. The implementation agent must still run that subagent near completion against the actual repository.

## Playable promise review

The system promise is clear:

- famine grows from actual food, route, policy, environmental, and governance pressure
- severe famine kills a significant dynamic share of the affected state when ignored
- civilians move because remaining is unsafe
- movement has an origin, route, destination, host burden, and durable outcome
- borders, occupation, camps, bombing, nuclear attacks, outbreaks, disasters, ideology, and existing events alter the same shared model

The current specification supports this promise with meaningful player choices, AI paths, failure states, and exact population accounting.

## Depth findings resolved in the final spec

### Famine is more than a modifier ladder

The design includes source composition, mortality, relief logistics, island blockade proof, siege, occupation, Air Cleanliness, political consequences, recovery, and historical profiles.

### Migration is more than a population drain

The design includes internal displacement, refugee flight, evacuation, deportation, trapped populations, route deaths, reception, transit, integration, resettlement, and return.

### Border choices have real consequences

Closure, controlled entry, transit, quarantine reception, violent enforcement, and forced return all preserve the population cohort and create distinct outcomes.

### Historical cases remain dynamic

The profiles alter causes, AI, routes, memory, and politics without imposing fixed death totals.

### Existing systems are connected

The integration matrix covers Deaths, Air Cleanliness, Condemnation, camps, occupation, CBRN warfare, bombing, nuclear aftermath, natural disasters, events, clusters, scenarios, and special-country exclusions.

### AI and probability are testable

The probability matrix names scenarios and expected ordering. It does not ask for a vague AI pass.

## Anti-bloat decisions

Broad expansion is no longer recommended at the planning stage.

Do not add these surfaces unless implementation evidence proves a need:

- a full shared scripted GUI
- a super-event
- a new country
- a focus tree
- a balance of power
- 3D models
- custom units
- portraits
- a second global food stockpile system
- one decision category per cause
- one decision per affected state
- fixed historical casualty quotas

The separate decision categories, state modifiers, report context, map highlights, and compact dynamic text are sufficient for the accepted mechanic; no incident-event layer or combined category is required.

## Required implementation decisions that remain open

These are engine and repository questions, not missing design.

### Positive destination population transaction

The implementation agent must inspect the current engine and repository behavior for adding state population and the resulting recruitable-manpower side effects. The exact transfer helper remains blocked until that evidence is known.

### Food reserve representation

The design requires a bounded relief and reserve input. The implementation should reuse an existing suitable stock, modifier, or country value if one exists. It should not invent a second detailed economic simulator without approval.

### Island and route proof

The implementation must identify reliable installed-game and repository predicates for islands, enclaves, safe land corridors, port access, naval pressure, and convoy sufficiency. The design fails closed when proof is incomplete.

### Occupation-law mapping

The shared policy profiles must be mapped to real current law identifiers after local inspection.

### Deaths UI capacity

The implementation must verify how many reason rows, filters, icons, or grouped categories the current Deaths tab can present cleanly. The separate border-closure reason remains optional because proximate causes are usually clearer.

## Closure condition

The design loop can stop after the implementation agent resolves the engine questions above and completes the accepted system.

Another broad design pass is justified only when:

- the ordinary presentation fails the clarity test in actual implementation
- the exact population transfer cannot be represented safely
- the current Deaths or occupation architecture cannot express the accepted ownership model
- a completion audit finds a new broad playable gap not covered here

Otherwise, further expansion would add maintenance burden without improving play.

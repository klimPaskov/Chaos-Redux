# Mandatory Near-Completion Improvement Loop Review

## Process status

This is a manual role-equivalent review because the `chaosx_improvement_loop_planner` runtime was unavailable. It is not an actual subagent pass. The implementation agent must run the real planner near completion and resolve its result.

## Feature promise

The event promises that armies can appear anywhere, become increasingly useful and strange, create military and political burdens, and eventually introduce Chaos unit families whose mishandling can produce hostile offshoot states.

The design succeeds only if more units can be either salvation or disaster and if the player can deliberately gamble without controlling the result.

## Depth gaps found during review

### Gap 1: A random spawn without persistent generation memory would repeat mechanically

Resolution added:

- generation records
- stacked muster
- prior management affects future quality
- closeout classes

### Gap 2: Fully random templates could become a reroll minigame

Resolution added:

- cost paid before reveal
- escalating request cost and cooldown
- no free cancel-and-reroll
- recombination consumes the same personnel and equipment with loss and failure risk
- weak results retain uses as cadres, garrisons, political liabilities, or achievements

### Gap 3: Claimant generals could remain flavor-only

Resolution added:

- influence values
- archetypes
- demand families
- command districts
- actual loyal formation links
- takeover, negotiation, arrest, and revolt
- one-state handling
- 20 portrait and name-pool plan

### Gap 4: Chaos units could accidentally duplicate parent events

Resolution added:

- opt-in family registry
- explicit train-versus-spawn mode
- parent isolation fields
- derivative origin flags
- shared classifiers
- family-specific weaker country profiles
- default exclusion of future and advanced units

### Gap 5: Derivative countries could be empty tags

Resolution added:

- starting forces from actual revolt units
- idea lifecycles
- sustainment and reinforcement
- hierarchy choices
- focus-scale route architecture
- expansion and integration
- AI and defeat cleanup

### Gap 6: A global system could create unbounded UI and script load

Resolution added:

- lot-level rather than division-level management
- selected-lot UI
- bounded active claimant presentation
- country-scoped active pulses only
- no permanent daily all-country loop
- explicit closeout and cleanup

## Anti-bloat decisions

### No fifth evolution

Four evolutions already move the event from local infantry musters to anomalous military secession. A fifth evolution would likely duplicate parent world-end systems or turn the event into a universal content aggregator.

### No direct world-end path

The user explicitly rejected a direct world-end scenario. Derivative states remain regional threats.

### No ordinary-country focus tree layer

The decision and GUI system is shared across ordinary countries. Country-specific ordinary focus branches would multiply scope without improving the core global event.

### No super-event

No normal threshold in this event changes the whole campaign’s meaning enough to justify image, quote, and audio production. A globally dominant derivative state can be reconsidered in a later separate plan.

### No one-member cluster

Event 19 stays unclustered until other military manifestation events are reworked and can form a real incident group.

### No animation for every claimant

Twenty animated portraits would create asset volume and visual noise. Static claimant portraits plus a critical-state frame animation communicate the mechanic better.

### No automatic future-family inclusion

Dynamic support means one registry entry is enough. It does not mean every new unit is automatically safe.

## Closure assessment

The planning design is deep enough to hand to implementation. Another broad planning expansion is not recommended now. The remaining work is implementation, local identifier verification, asset production, balance testing, specialist audits, final localisation, documentation, and catalog alignment.

This is a manual closure recommendation only. The real improvement-loop planner must still run after a meaningful implementation tranche. If it finds a new gap created by implementation, that addendum must be implemented, promoted, queued with reason, or rejected with reason before completion.

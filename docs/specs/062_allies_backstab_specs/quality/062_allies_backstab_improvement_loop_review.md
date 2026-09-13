# Event 062 improvement-loop review

## Review status

This is a parent-authored design review using the supplied improvement-loop skill. It is not a result from `chaosx_improvement_loop_planner` because the current environment had no working subagent invocation route.

The mandatory future planner pass remains required after implementation. The context-complete task is defined below.

## Playable promise

The event promises sudden alliance betrayal, fear among weak members, armed expulsion, faction fracture, side choice, and a political aftermath that affects later alliances.

The original rough concept delivered the incident but left several gameplay risks:

- random targets could be nonsensical
- faction leaders, subjects, and existing wars could create invalid states
- victims had little to do after expulsion
- several targets could attack one another accidentally
- high Evolutions could create uncontrolled war spam
- repeatability could select the same weak country repeatedly
- generic faction-leave Chaos could reward the violent expulsion with negative Chaos
- the event could end as a one-popup spectacle without settlement memory

## Accepted depth improvements

The specification adds only mechanics that support the promise:

1. a normalized weakness and strategic-utility target model
2. political-unit bundles for overlords and subjects
3. staged faction mutation with delayed legal revalidation
4. automatic co-victim non-aggression and optional coordination
5. one public Crisis Cohesion value
6. phase-based decisions and missions for leaders, victims, members, and limited sponsors
7. settlement outcomes and durable betrayal memory
8. full internal bloc wars at Evolution II
9. bounded simultaneous large-faction collapse at Evolution III
10. a strict one-time super-event threshold
11. repeat and victim protection
12. forced-faction-exit Chaos correction

These changes alter play and reduce invalid outcomes. They do not exist only to increase file count.

## Rejected expansion ideas

### Permanent global alliance-trust system

Rejected because the event needs temporary crisis management and durable memories, not a second global diplomatic simulation attached to every faction forever.

### Dedicated scripted GUI

Rejected because one cohesion value, role text, and phase-based actions fit the ordinary decisions interface. A full window would add layout and maintenance cost without a clear management need.

### Generic emergency focus branches

Rejected because Event 62 can affect almost any country. Injecting temporary branches into every focus tree would be inconsistent, intrusive, and difficult to clean. Decisions and missions give immediate agency.

### New countries for every victim coalition

Rejected because the victims are existing governments. The event can create a successor faction without creating tags.

### Custom military units

Rejected because emergency defense can use ordinary formations paid from real manpower and equipment. New subunits, equipment, models, counters, and audio would not strengthen the event's political identity.

### Five or more Evolutions

Rejected because the three accepted Evolutions already cover wider purges, internal wars, and simultaneous alliance collapse. More tiers would repeat scale changes.

### World-end scenario

Rejected because alliance collapse is a severe world-order event but does not define a terminal campaign state. The conditional super-event provides the correct presentation ceiling.

### Manual triggerable scenario

Rejected from the source spec because the user did not request one and the event can already be tested through normal event controls. A future sandbox scenario would need a separate accepted design for faction selection controls and intensity.

### Automatic direct major-power intervention at baseline

Rejected because it would make a Minor Repeatable event generate global wars too easily. Baseline support remains material and diplomatic. Direct intervention is treaty-bound or high-Evolution.

## Current depth judgment

The event is deep enough for implementation. Broad expansion before implementation would add bloat.

The remaining work is implementation proof:

- repository and engine precedent review
- actual transaction and war-graph feasibility
- probability evidence
- decision and mission balance
- final localisation
- asset production
- super-event research
- workbook alignment
- completion audit

## Mandatory future planner task

After implementation and the first round of specialist audits, spawn `chaosx_improvement_loop_planner` with no inherited context.

The prompt must provide:

- the complete Event 62 spec folder
- implementation files and current diff
- all subagent handoffs
- probability before and after evidence
- decision and mission audit
- asset manifest and super-event research
- open blockers and accepted simplifications

Ask the planner to compare the implemented feature with the playable promise, identify any missing connection or shallow surface, and recommend one of two outputs:

1. a closure handoff listing only final small tasks because additional expansion would bloat the event
2. one bounded addendum under `docs/plans/062_allies_backstab_plans/` when a real design gap remains

The planner must not patch gameplay files. A new broad plan is not allowed if a prior Event 62 addendum remains unresolved.

## Stop condition

Broad design expansion should stop when:

- every transaction case is safe
- player roles have meaningful actions
- AI weights pass the named scenarios
- settlements and cleanup work
- the three Evolutions match their proof conditions
- the super-event fires only at the strict threshold
- assets and localisation are complete
- Event Logs, Event Details, Chaos History, cluster, docs, and workbook agree
- no accepted plan remains unresolved

At that point, any further mechanics would increase maintenance more than gameplay value.

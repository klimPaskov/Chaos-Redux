# Event 061 manual improvement-loop closure

## Context

The planning rules require one near-completion review through `chaosx_improvement_loop_planner` after a meaningful work tranche.

The active ChatGPT environment exposed the subagent definition but not the project subagent spawn command.

The definition and improvement-loop skill were read in full. This document records a manual equivalent design review.

It does not claim a runtime subagent invocation.

The implementation prompt still requires the actual subagent pass after the gameplay implementation exists.

## Review input

The manual review examined:

- the user brief
- all seven Event 61 source-spec parts
- Return to Rearmament decisions and missions
- all three evolutions
- state ledger and law models
- AI and cross-event integration
- balance and exploit plan
- presentation and achievements
- implementation architecture
- catalogs and cluster state
- all supplied subagent role definitions

## Findings and closure

## Finding 1: The original factory conversion had no reversible physical state

### Risk

A generic later factory reward would create free building levels, lose state identity, and break under annexation.

### Closure

Added a state-level physical conversion ledger.

Every baseline and Evolution III conversion adds one ledger unit.

Every restoration consumes one civilian factory and one ledger unit.

The ledger follows the state and is authoritative after ownership changes.

### Acceptance reference

Part 1 factory conversion, Part 2 state reopening, Part 5 exploit table, factory-ledger diagram.

## Finding 2: A simple rearmament score could become a click currency

### Risk

The player could buy arbitrary readiness without restoring military structure.

### Closure

Made Rearmament Readiness a derived total from five structural pillars.

Added separate structural proof for major exemptions.

Evolution III counts distinct action families and requires at least one physical or legal action.

### Acceptance reference

Part 2 Readiness and structural proof, Part 5 Readiness anti-farming.

## Finding 3: Too many values and a bespoke interface would add UI burden

### Risk

Industry, law, manpower, stockpile, and public support could become five public meters and a large scripted GUI.

### Closure

Kept one public numeric value.

Showed pillar state qualitatively.

Used an ordinary phased decision category, one static picture, five primary actions, one mission, and three state targets.

### Acceptance reference

Part 2 presentation layer and category phases.

## Finding 4: High-Chaos opening could destroy industry, stockpiles, and armies on one tick

### Risk

The player would have no response and the event would feel arbitrary.

### Closure

Added staggered evolution warnings and a scheduler.

Each destructive layer has a response period.

Disabled earlier evolutions do not block later stages.

### Acceptance reference

Part 3 staggered application and lifecycle diagram.

## Finding 5: Repeat firing could create duplicate missions and parallel timers

### Risk

A repeatable event could flood the decision category and execute the same evolution several times.

### Closure

Added a global cycle ID, per-country stage guards, singleton visible missions, bounded pending-cycle pressure, and deadline merge rules.

### Acceptance reference

Parts 1, 3, 5, and 7.

## Finding 6: No Army could soft-lock its own recovery

### Risk

A country with no army law could lack army experience, command power, and recruitable manpower required to escape.

### Closure

Created a civilian-resource recovery sequence through Defence Ministry, National Arsenal, and Service Registry.

The first steps use political power, civilian factory commitment, and time.

Added a ledger-free minimum-arsenal fallback.

### Acceptance reference

Part 2 extreme-law recovery.

## Finding 7: Forced army abolition during active war would be mechanically destructive

### Risk

Permanent Peace could remove a country's army while it fights for survival.

### Closure

Added direct-danger deferral, defensive and offensive distinctions, postwar settlement, and an anti-exploit test for irrelevant wars.

### Acceptance reference

Part 3 active-war deferral and Part 5 war edge cases.

## Finding 8: Stockpile removal needed reserve logic and exact transaction proof

### Risk

A percentage of total stockpile could remove essential equipment, unsupported special gear, or produce negative-debit errors.

### Closure

Added positive-surplus calculation, reserve floors, owner-safe exclusions, protection families, actual-debit rewards, and a blocked-family outcome.

### Acceptance reference

Part 3 Evolution I and Part 7 stockpile architecture.

## Finding 9: Division removal needed a safe engine contract

### Risk

Generic scripted deletion may destroy manpower and equipment or remove special units.

### Closure

Made safe native disband a hard local-validation gate.

Added hard exclusions, selection priorities, tiny-army protection, unit-age anti-spam, and actual-result benefits.

### Acceptance reference

Part 3 Evolution II, Part 5 division exploit table, Part 7 division architecture.

## Finding 10: The civilian route lacked a real payoff

### Risk

The event would present rearmament as the only rational route.

### Closure

Added capped Reconstruction Materials, Veteran Reintegration, and Peace Dividend benefits with costs and lifecycle limits.

Added voluntary Permanent Peace for secure countries.

### Acceptance reference

Part 3 all three evolutions.

## Finding 11: AI could follow ideology into obvious defeat

### Risk

Pacifist or low-war-support AI could choose No Army during direct danger.

### Closure

Added three strategic stances, hard threat gates, major and faction-leader floors, subject and overlord logic, naval exposure, and twelve probability scenarios.

### Acceptance reference

Part 4 and the AI probability research file.

## Finding 12: Event 82 could duplicate law restoration

### Risk

An external upward step followed by an Event 61 project could grant two steps for one loss.

### Closure

Added explicit law ranks, stored maximum restore targets, periodic reconciliation, and completion rechecks.

### Acceptance reference

Parts 1, 2, 4, 5, and 7.

## Finding 13: Event 124 overlaps the new design

### Risk

Two global demilitarization systems could apply incompatible state, law, and army restrictions.

### Closure

Assigned Event 61 ownership of global peacetime conversion.

Recommended a later geographic treaty or demilitarized-zone role for Event 124.

No Event 124 source was rewritten in this planning task.

### Acceptance reference

Part 4 cross-event matrix.

## Finding 14: The Peace cluster export is internally wrong

### Risk

The duplicate `9, 9` member list omits Event 61 and can break catalog or execution alignment.

### Closure

Mapped authoritative workbook and cluster changes to `9, 61`, with White Peace first and Event 61 second.

### Acceptance reference

Catalog alignment handoff.

## Finding 15: Achievement concepts could be trivialized by event shortcuts

### Risk

Event 82, emergency actions, annexation, subjects, or one-battalion spam could unlock the achievements without the intended challenge.

### Closure

Added three full achievement contracts with persistent cycle tracking, time windows, disqualifiers, state ownership handling, war-result proof, special-unit classification, and dedicated icons.

### Acceptance reference

Part 6 and achievement prompt.

## Finding 16: Global periodic checks would be expensive

### Risk

A permanent daily or weekly world loop would add needless campaign cost.

### Closure

Restricted broad work to event firing and evolution resolution.

Added a recursively scheduled 30-day pulse only for affected countries with active Event 61 state.

### Acceptance reference

Parts 1, 5, and 7.

## Rejected expansions

The review rejected these additions because they would not improve the accepted event enough to justify their scope:

- a new focus tree
- a custom country or civil-war tag
- a separate global peace faction
- a bespoke scripted mechanic window
- five public readiness meters
- naval task-force scrapping
- a character or portrait package
- a custom 3D model
- animation-only presentation
- a quote and music package
- permanent free civilian factories from stockpile value
- a direct repeatable Chaos reduction for pacifist choices

These rejections preserve focus and reduce duplicate systems.

## Manual review result

The source specification is deep enough to guide implementation without requiring the coding agent to invent the main mechanic.

The implementation still requires an actual near-completion subagent pass because gameplay source, final assets, final localisation, probability evidence, workbook changes, and in-game behavior do not exist in this planning environment.

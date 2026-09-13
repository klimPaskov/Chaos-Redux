# Event 32 improvement-loop closure review

## Review status

This is a planning-time closure review performed against the complete Event 32 specification package.

The accepted closure below remains the design source of truth. A `chaosx_improvement_loop_planner` worker was dispatched with `fork_context=false` on 2026-09-05 for a final implementation-time addendum review, but it produced no handoff after bounded waits and was shut down. No new design addendum is therefore promoted from that worker; the missing independent handoff is recorded in `docs/plans/032_missiles_plans/subagent_handoffs/032_improvement_loop_planner_handoff_2026-09-05.md`.

## Playable promise

Event 32 promises a worldwide missile age that begins as a useful strategic grant and becomes dangerous through repetition, poor maintenance, unconventional payloads, weak command, and retaliation logic.

The completed specification supports that promise through:

- one global repeatable firing that reaches every valid country
- national technology progression and mature-program rewards
- physical launch states with geography, capacity, hardening, damage, capture, and succession
- exact operational reserve accounting
- readable readiness and command values
- preparation, target selection, conventional operations, and bounded failures
- five parallel evolution tracks
- human counterplay and AI equivalents
- shared deaths, contamination, condemnation, evidence, and Fallout consequence bridges
- a bounded causal incident queue for automatic retaliation
- a manual scenario with five profiles and four intensities
- eight mastery achievements
- asset, text, probability, acceptance, and test contracts

## Improvements already folded into the source spec

### A program instead of a gift

The legacy event grants technology and sites with no lasting management. The new design creates a persistent program with reserve, readiness, command, site custody, and maintenance choices.

### Geography with consequences

Launch states are selected, upgraded, damaged, captured, inherited, and repaired through one physical record. Frontline exposure, strategic depth, infrastructure, supply, hardening, and regional dispersion matter.

### Escalation with counterplay

Every evolution creates a new pressure and a response family. Saturation increases scale, poor guidance adds risk, special payloads add consequence, rogue commands threaten custody, and retaliation networks create time-sensitive warning choices.

### Shared-system integration

Special payloads use existing CBRN systems. Population loss uses the shared Deaths system. Public responsibility uses evidence and Condemnation. Terminal environmental collapse remains owned by Fallout. Event 32 therefore adds strategic delivery without duplicating mature shared systems.

### Bounded AI and chain logic

The design includes doctrine profiles, reserve floors, target scoring, payload restraint, maintenance behavior, and named probability scenarios. Automatic retaliation has hard causal and participant bounds, which prevents an uncontrolled recursive exchange.

### Restraint as mastery

The achievement set rewards precision, survivability, command recovery, counterforce, controlled saturation, and refusal to escalate. This gives the event goals beyond accumulating the largest arsenal.

## Broad expansions rejected as bloat

### Dedicated scripted GUI

Three main values, one selected target, and a compact phase state fit an ordinary decision category. A custom control-room window would add asset and maintenance cost without improving the player's decision model.

### Event-owned focus trees or countries

Event 32 affects existing countries and does not create a stable political actor. A shared missile focus tree or missile-state tag would duplicate national content and weaken the global-event identity.

### Event-owned world ending

The event can cause exchanges that feed contamination, deaths, condemnation, and Fallout eligibility. A separate missile apocalypse branch would duplicate the existing consequence owner and the current world-end architecture.

### Super-event package

The baseline is a repeatable minor event. Its evolutions are global mechanic changes, but none creates one unique campaign threshold that requires a dedicated super-event. Reports, news, Event Logs, and the existing Fallout presentation are sufficient.

### Custom 3D models and animation

Installed rocket-site, missile, raid, and explosion assets should support the accepted surfaces. Custom geometry or warning-light animation would add production cost without creating new gameplay.

### Orbital, space, and anti-missile expansion

Space launchers, orbital weapons, satellites, and broad strategic defense belong to Event 73, Space Race, or a separate future event. They should connect through adapters after those systems are designed.

### New missile equipment economy

The normalized reserve ledger is enough for Event 32. A complete missile equipment production tree would change the scope into a technology and industrial overhaul and would require a separate accepted design.

## Closure verdict

Broad design expansion is no longer recommended.

The event is deep enough to proceed to implementation because its player choices, failure states, AI behavior, physical geography, cross-system consequences, visual identity, scenario setup, and mastery goals are mapped.

The remaining work is implementation, engine proof, tuning, asset production, documentation alignment, probability auditing, and later user-owned live validation. Those are completion tasks, not missing design families.

A new improvement-loop pass is justified only after the current package is implemented and a completion audit finds a distinct design gap that this closure did not cover.

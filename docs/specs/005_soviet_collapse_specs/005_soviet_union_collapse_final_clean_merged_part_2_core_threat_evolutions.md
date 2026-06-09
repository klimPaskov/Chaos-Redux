# Soviet Union Collapse Final Clean Merged Specification, Part 2
# Core Crisis, Threat, Event Logs, Evolutions, and Presentation

## Core event identity

Soviet Union Collapse event 005 is a major political fracture crisis. It is not a one-click country release effect.

The Soviet Union begins to lose obedience before it loses territory. The first signs are missing rail shipments, unanswered ministry cables, local garrisons waiting for republican instructions, party offices arguing over legal seals, border guards ignoring Moscow, and foreign diplomats asking whether anyone can still speak for the union.

The first wave creates a serious crisis even for a strong Soviet Union, but a stable calm Soviet Union must not instantly reach terminal collapse. The danger comes from a living system: authority, command obedience, foreign intervention, breakaway confidence, rail control, depots, old movements, and chaos.

The event belongs to the Liberations cluster as its severe political fracture event. It should interact with Independence Wave as a related but distinct cluster member. Soviet Collapse does not reuse Soviet Collapse outcomes from other events unless the source spec explicitly connects them.

## Baseline stages are not evolutions

The ordinary crisis flow is baseline progression:

- first declarations
- local obedience crisis
- Moscow response
- negotiations, isolation, or force
- more republics rising through MTTH pressure
- local league preparation
- Free Republics' League formation under serious crisis
- deeper authority collapse
- Union Unmade terminal release, reconquest, settlement, or rump survival

Do not log these as evolutions.

Evolutions are mutation tracks that make the crisis behave differently or create new actors. Evolution logs should represent patterns such as:

- The Pattern of Secession
- Depots Choose Flags
- The Old Underground Wakes
- Red Resistance without Moscow
- Foreign Liaison Offices
- The War of Committees
- The Flags Return Incorrectly
- The Factory States
- Ancient Claims Return
- The Dead Are Citizens
- The Former Union Becomes Many Worlds

Do not create more than one Soviet Collapse evolution log per chaos tier unless this package explicitly allows it. If several mutation incidents occur in one tier, log the highest priority one as the evolution and handle the rest through news, reports, decisions, or event details. Stage numbers are player-facing progression numbers, not branch identifiers. Non-republic successor branch IDs can still choose actor-specific text, but their visible stage must come from the logged tier: Stage 4 for Totalen Chaos and Stage 5 for World Collapse.

Evolution logs must extend beyond early chaos. They should not stop at Gathering Storm.

## Event log details

Soviet Collapse must have proper event-log window details.

The event detail window should explain:

- current broad crisis state
- first-wave state
- whether major republics are active
- whether local leagues exist
- whether the Free Republics' League exists
- which true evolution tracks have appeared
- whether Moscow Authority is intact, shaken, failing, or broken
- whether Union Crisis Threat is contained, rising, severe, or terminal
- whether foreign intervention is limited, organized, dominant, or contested
- whether old movements, high-chaos splinters, factory states, ancient restorations, or dead-state actors have appeared

Use in-world language, not debug language.

Example tone:

`Moscow has lost obedience in parts of the Union. Republican authorities, rail offices, garrisons, and foreign observers now test whether Soviet orders still carry force outside the center.`

## Threat and pressure model

Union Collapse Threat must be dynamic, readable, dampened, and resistant to runaway in calm conditions.

The crisis should track or represent these main values:

| Value | Role | Typical colour direction |
| --- | --- | --- |
| Moscow Authority | central orders still believed | blue or steel |
| Armed Breakaway Momentum | republics believe independence can be defended | red or crimson |
| Command Obedience | army, security, navy, and rail obedience | grey or white |
| Foreign Penetration | sponsors, recognition, aid, advisers, intelligence | purple |
| Old Movement Resurgence | older and strange movements returning | orange |
| League Cohesion | republic coordination and bloc trust | yellow |
| Local Support | civilians and local institutions support a side | green |

Use project-appropriate colours, but keep them consistent. If a total threat value is built from several components, tooltips must show a readable coloured breakdown.

The player should understand why a visible value rose or fell. Future surprises can stay hidden, but visible cause and effect should not be hidden.

## Initial threat target

In Calm World, with a strong Soviet Union, high stability, reasonable war support, no major war losses, intact rail control, low foreign penetration, and an ordinary structured first wave, initial Union Collapse Threat should normally calculate around 5 to 10.

This is a dynamic target, not a fixed hardcoded number.

Threat can start higher when:

- chaos is high
- Soviet stability is low
- war support is low
- the Soviet Union is losing a major war
- major cities are threatened
- the first wave is larger
- command obedience is weak
- depots are vulnerable
- foreign penetration exists
- old movements are active
- earlier Chaos Redux events damaged Soviet authority

Threat must not start around 80 in Calm World strong-USSR conditions.

## Threat growth

Threat should rise from visible failures:

- failed missions
- expired objectives
- republic capitals held past deadlines
- failed reclamation attempts
- major depot seizures
- garrison defections
- lost rail hubs
- foreign recognition
- major sponsor aid
- local league coordination
- Free Republics' League victories
- old movements holding territory
- high-chaos splinters appearing
- regional cascades
- major Soviet cities or ports lost

Threat should fall or stabilize from visible success:

- successful Soviet missions
- rail hubs restored
- depots secured
- loyal officers re-establish command
- foreign routes closed
- republics accept settlements
- local support restored
- league coordination fails
- old movements are contained
- negotiated reintegration succeeds
- military victories that do not produce major backlash

Mission success must not raise overall threat by accident. Heavy-handed success may lower one pressure while raising another, but the tooltip must show the tradeoff.

## Monthly runaway guard

Threat must not climb dozens of points in one month under calm or moderate conditions unless major visible failures occur.

Expected behavior:

- successful month: threat falls or stabilizes
- mixed month: threat changes modestly
- failed month: threat rises, but not to terminal values
- catastrophic month: sharp rise is allowed only with clear events and real failures

Union Unmade must not fire from early runaway variables.

## Union Unmade pacing

Union Unmade fires only when the crisis has become terminal.

Valid ingredients include several of:

- sustained high Union Collapse Threat
- very low Moscow Authority
- repeated failed Soviet missions
- multiple major republics independent
- local leagues or Free Republics' League coordination
- failed or stalled reclamation
- major rail, depot, or command failures
- foreign recognition spread
- major republics holding capitals
- high-chaos actors holding territory

In ordinary calm or Gathering Storm games, Union Unmade should usually require a long chain of inaction, failed missions, and accumulating release pressure. A strong center should not reach 100 threat in the first year unless the player allows repeated visible failures and additional severe pressure to stack. High chaos or a collapsing wartime USSR can make it faster, but only through visible severe factors.

## Super-event scope

Use super-events only for campaign-defining moments.

Do not use super-events for:

- Baltic League formation
- Caucasus League formation
- Central Asian League formation
- one republic release
- normal internal republic release
- ordinary regional cascade
- recognition conference
- local league war vote
- ordinary faction join

Use news events, report events, event-log entries, or decision notifications for these.

Required or allowed super-events:

- Union Unmade
- Black Banner Returns when the Black Banner becomes a major state actor
- The Dead Are Citizens when death-state mechanics become major
- The World as One Factory when factory-state mechanics become major
- Every Port a Council when sailor or naval council mechanics become major
- other rare major high-chaos transformations implemented as campaign-defining branches

Every retained super-event must have quote, remark, image, audio, wiring, and documentation.

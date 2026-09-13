# Multiplayer, DLC, performance, persistence, and cleanup

## Multiplayer ownership

Event 38 can affect several human countries. The release and scenario transactions must preserve player control and make every forced political change explicit.

### Human Malta

When a human already controls Malta:

- transform the same country actor
- keep the human player on that actor
- present opening choices directly
- do not create an AI Malta duplicate

### Human displaced owner

A human country losing opening states receives its response event and remains in control. The event cannot annex the entire human country merely because one selected state is transferred.

### Human principality candidate

When a human controls a government that could become a principality or local restoration:

- offer transformation or negotiated subject status
- allow rejection and resistance
- preserve the same player actor when transformation is accepted where possible
- never replace the human actor silently

### Human Holy World side choice

Every human ordinary country chooses believer or nonbeliever during terminal setup. AI alignment does not override the choice.

### Human Germany and Holy Realm

Hidden-route negotiations use direct player choices. Human Germany chooses Atlantis normally.

## Determinism

Random selections must use the same frozen arrays and seeds across clients. Important rules:

- freeze opening states before commit
- freeze displaced owners
- freeze order demand candidates
- freeze relic outcome branch before delayed presentation
- freeze principality generation
- freeze terminal side candidate pools
- freeze regional war queues

Do not rebuild a random candidate pool independently on each client after a delay.

## Player switching and ghost actors

The implementation follows the shared multiplayer and tag-switch contract. Required behavior:

- no duplicate player assignment
- no uncontrolled automatic tag switch
- clean actor ownership after release
- settings follow current project rules
- human confirmation before a scenario-created Holy World actor takes control

Any ghost-copy mechanism must be audited against country creation, subject control, and Event Details actor mapping.

## Save and reload

Persistent facts include:

- event fired state
- evolution state
- current actor
- selected opening package
- three public values
- order headquarters and demands
- relic custody and controversy
- principality generation and obligations
- focus routes
- Eleventh Crusade phase
- Teutonic faction formation date
- Atlantis eligibility and route
- Holy World preparation, continent, and readiness
- manual scenario state
- regional war queues
- active world-threat sources

Temporary selection and request variables must clear after each transaction. Save files should not preserve half-completed setup state without a recovery path.

## Existing saves

New Event 38 systems need idempotent initialization for existing saves:

- event registry
- constants and arrays
- country origin detection
- CXT provider registration
- missing hidden-idea carriers
- UI state
- world-end branch registry
- scenario registry

Do not add a whole-world daily repair scan. Use bounded existing-country or owner-local hooks allowed by project rules.

## DLC behavior

The event must define behavior with and without relevant DLC.

### By Blood Alone

Native embargo and some air or peace features can vary. Condemnation enforcement already has a DLC fallback. Event 38 uses the shared result rather than duplicating embargo logic.

### La Résistance

Intelligence, operations, collaboration, and agency features can enrich relic, resistance, sponsor, and atrocity discovery. Without the DLC, use decisions, events, and shared evidence systems.

### No Step Back

Supply hubs, railways, officer corps, spirits, and tank design can affect logistics and Atlantis. Without the DLC, use supported static equipment and building effects.

### Arms Against Tyranny

MIO or market features can support order workshops and procurement. Without the DLC, use production bonuses and decisions.

### Man the Guns

Naval design and government-in-exile features can affect Malta and principalities. Without it, use standard ships and country mechanics.

### Other DLC

Country-specific systems, special projects, and doctrines require an explicit compatibility audit. The event cannot require a DLC without a functional fallback unless the user approves that dependency.

## Focus and decision fallbacks

A DLC fallback must preserve the gameplay choice, cost, and consequence. It should not replace a real mechanic with a tiny modifier.

Examples:

- intelligence operation becomes a timed decision with exposure risk
- equipment designer becomes fixed equipment marks with research
- native embargo becomes bilateral penalties and blocked support through Condemnation
- advanced subject type becomes a standard subject plus Event 38 charter logic

Every fallback is documented and reviewed. Unapproved weak substitutes are forbidden.

## Performance architecture

### Sparse ledgers

Use registered active arrays for:

- Event 38 actors
- active principalities
- active order headquarters
- active relic expeditions
- active regional campaigns
- active terminal projects
- Atlantis atrocity sites through the camp system

### Local processing

- country decisions process their own actor
- state harm processes registered active states
- principalities process their own obligations
- terminal war uses queued regional batches
- migration and famine use their owner ledgers

### No broad periodic scans

No new `on_daily`, `on_weekly`, or `on_monthly` whole-country iteration is approved. If implementation proves one is necessary, stop and request explicit user permission.

### Queue limits

- one major order demand
- one relic expedition
- one selected human campaign target
- one or two regional Final Crusade campaigns
- bounded Holy World regional war batches
- bounded principality creation per transaction

## Idempotency

Every major effect needs a result and generation proof:

- opening release
- provider registration
- principality creation
- unit spawn package
- Holy See transformation
- Kingdom of God transformation
- Teutonic faction formation
- Atlantis 20-formation grant
- Holy World activation
- manual scenario setup

Repeated calls return an existing success or clean rejection. They do not duplicate countries, units, equipment, wars, or flags.

## Cleanup ownership

### Event 38 actor annexed

- identify accepted successor
- transfer or close council facts
- close invalid decisions
- preserve history
- handle principalities
- clear provider public packages when no successor
- clear Event 38 world-threat sources

### Principality annexed

- clear obligation and loyalty records
- resolve charter territory
- remove or transfer units safely
- preserve country history
- allow reformation only through a new generation proof

### Order headquarters lost

- remove local benefits
- trigger relocation or dissolution
- clear selected-state marker
- preserve order grievance and history

### Relic actor invalid

- transfer custody, mark lost, or close the record
- do not leave invalid event targets

### Teutonic faction dissolves

- clear formation timer and regional campaign queues
- settle shared units and technology
- clear threat source
- preserve public history after reveal

### Atlantis defeated

- remove territorial program
- close extermination policy through shared systems
- preserve evidence and Deaths
- clear elite unit provider access as appropriate
- clear threat source

### Holy World victory or defeat

- preserve terminal history
- close or transform active campaigns
- handle believer and nonbeliever factions
- clear preparation-only state
- retain `world_end` according to shared aftermath contract

## Rollback

Transactions that transfer states, create countries, or grant large force packages need a rollback plan.

Rollback records:

- prior owner and controller
- prior capital
- created tags
- created units and stockpiles
- created wars
- created faction membership
- created event targets

Rollback is used only before a transaction commits. After public commit, failures use gameplay consequences and cleanup rather than silent rewinding.

## Error and debug policy

If a live problem cannot be explained, temporary debug logs can expose transaction IDs, actor proofs, state counts, generation numbers, and result codes. Remove every temporary debug line after resolution.

Do not ask the user for logs unless they paste relevant lines. Normal agents do not launch the game. Live testing belongs to the user unless the explicit autonomous debug skill is invoked.

## Persistence acceptance tests

- save before release and load
- save during release transaction recovery
- save with active order demand
- save with active relic expedition
- save during principality creation
- save during Eleventh Crusade
- save on day 729 of Teutonic timer
- save during Atlantis betrayal
- save during full-continent proof
- save during Holy World regional pulses
- multiplayer host and client reload
- DLC-present and DLC-absent campaigns

# Event 19 Infantry Spawn
## Part 7: Decision architecture, decision-only surface, AI, tuning, and balance

## Decision-system purpose

The decision layer is the playable center of Infantry Spawn. It must help the player understand and manage a large, changing military burden without becoming a store or a wall of one-division actions.

The category evolves with the event.

- Baseline shows compact audit and disposition actions.
- Evolution I adds district organization and standardization.
- Evolution II adds supply missions, prototype handling, and on-demand formation requests.
- Evolution III exposes the full Formation Ledger decision category and claimant crisis.
- Evolution IV adds family selection and Anomalous Registry management decisions.

Obsolete actions disappear or are replaced. The category should show what matters in the current phase.

## Category lifecycle

### Dormant state

Before Event 19 affects the country, no category is visible.

### Active generation state

The category appears when the country has an unresolved generation, live or unaccounted Event 19 formations, an active claimant, a pending Evolution III opening, a deferred transaction, a running management operation, or a relevant request cooldown.

### Closeout state

After all lots are resolved and no active claimant, opening, deferred transaction, running operation, or relevant cooldown remains, the decision category closes.

The parent-side derivative revolt marker and Board close are written only after the exact transfer or one-state takeover reaches its final ownership, ledger, control, core, and diplomacy proof; pre-commit recovery and post-commit quarantine do not record a successful revolt.

### Persistent evolved state

At Evolution III and IV, the Formation Ledger decision category remains available while the crisis is live, including the first bounded opening draw and any active claimant or formation.
Persistent Evolution III or IV entitlement flags alone do not keep the ordinary category open after the country intentionally suppresses new draws and resolves the crisis.

### Invalid-country cleanup

The category and all active missions close when:

- the country is annexed
- the tag is safely transformed
- a terminal transition forbids the system
- the country becomes an invalid scope
- the event-created derivative package replaces its ordinary country package
- a claimant completes a takeover or an Event 19 derivative revolt completes
- a direct-scenario actor or isolated breakaway owns the scenario package

Relevant generation, target, and lot data must be migrated or cleared deliberately.

## Decision groups

## Group A: Audit and records

### Audit the New Formations

Phase:

- baseline onward

Purpose:

- begins or accelerates the audit process
- reveals lot summaries
- prevents informal command ownership

Dynamic costs:

- army experience based on lot count and complexity
- command power within conservative limits
- support equipment for large or advanced generations
- temporary staff burden

AI use:

- high priority when control is low or claimant risk is rising

### Conduct a Formation Census

Phase:

- Evolution II onward

Purpose:

- refreshes the list of event divisions, lots, templates, districts, and loyalty links
- repairs stale records after war, transfer, or template changes

This is a maintenance action, not a free control boost.

### Trace the Equipment Ledgers

Phase:

- Evolution I onward

Purpose:

- identifies equipment debt, unsupported types, and salvage opportunities
- improves the next standardization or cannibalization action

Costs:

- time
- factory or logistics burden
- possible temporary reinforcement slowdown

## Group B: Integration and standardization

### Assign Territorial Roles

Phase:

- baseline onward

Purpose:

- converts suitable lots into regional defense roles
- lowers congestion
- limits offensive deployment or grants territory-specific bonuses

### Open a Standardization Cycle

Phase:

- baseline onward

Purpose:

- starts a timed mission that converts compatible lots toward a national template family

Requirements:

- compatible lot set
- equipment or production capacity
- training capacity

Success:

- raises control
- reduces template count
- lowers future reinforcement burden

Failure:

- equipment loss
- organization loss
- higher congestion

### Recombine Random Battalions

Phase:

- Evolution III onward

Purpose:

- uses the same generated personnel and equipment to attempt a more coherent lot

Rules:

- not a free reroll
- meaningful loss and delay
- claimant-attached lots require claimant consent or prior reassignment
- outcome cannot be cancelled and rerolled

### Preserve Specialist Cadres

Phase:

- Evolution I onward

Purpose:

- saves useful support elements from weak formations
- destroys or reduces the combat core
- produces training or support value rather than full equipment duplication

### Emergency Field Integration

Phase:

- baseline onward during war or immediate threat

Purpose:

- removes some readiness locks quickly
- applies strong temporary supply, training, and command penalties

The decision should be powerful enough to matter in a losing war and costly enough that a safe country does not use it routinely.

## Group C: Supply and movement

### Reserve Rail Corridors

Phase:

- Evolution II onward

Purpose:

- dedicates trains and rail capacity to move event formations
- lowers local congestion
- can reduce other supply or civilian movement

The action should target named or dynamically displayed corridors when possible.

### Establish Muster Depots

Phase:

- Evolution I onward

Purpose:

- creates or designates logistics sites for event formations
- improves integration and reinforcement
- becomes a strategic claimant target later

Costs:

- construction capacity
- support equipment
- trains
- state control and time

### Relocate an Impossible Lot

Phase:

- all phases when a lot is locally unsustainable

Purpose:

- moves or abstracts movement of a lot from an island, low-supply state, or encircled position
- costs trains, convoys, fuel, or time

Failure can strand or partially dissolve the lot.

### Clear the Training Grounds

Phase:

- all phases

Purpose:

- reduces training saturation through demobilization, districting, or temporary capacity investment

## Group D: Controlled demobilization

### Supervised Demobilization

Phase:

- baseline onward

Purpose:

- removes selected weak or unwanted lots after a delay
- returns partial salvage and manpower or labor according to safe accounting
- lowers congestion

Restrictions:

- cannot operate instantly
- cannot return full equipment
- claimant or anomalous lots need special handling
- wartime use can lower war support or local trust

### Break Up the Formation

Phase:

- Evolution II onward

Purpose:

- converts a large or advanced lot into smaller cadres, a limited salvage package, and training value

### Disarm a Claimant District

Phase:

- Evolution III onward

Purpose:

- removes heavy equipment from claimant-loyal formations before arrest or negotiation

Risk:

- failure can start revolt

### Disperse an Anomalous Lot

Phase:

- Evolution IV onward

Purpose:

- family-specific removal or containment
- spawn-only families cannot be converted into trainable stock

## Group E: Formation requests

### Request a Field Reinforcement

Phase:

- Evolution II onward

Bias:

- ordinary combat value
- balanced size and equipment

### Request a Mobile Reserve

Phase:

- Evolution II onward

Bias:

- cavalry, bicycle, camel, motorized, mechanized, armored car, and valid air-mobile families

Costs emphasize:

- fuel
- trucks or transport
- army experience

### Request Territorial Defenders

Phase:

- Evolution II onward

Bias:

- supply-light infantry, garrison, local support, terrain fit

### Request Specialist Firepower

Phase:

- Evolution II onward

Bias:

- artillery, armor, anti-air, anti-tank, support companies, specialist battalions

Costs emphasize:

- equipment
- industry
- supply

### Request Anything

Phase:

- Evolution III onward

Bias:

- full eligible pool and broadest tails

Risk:

- highest absurdity, claimant, and saturation multipliers

### Request an Anomalous Formation

Phase:

- Evolution IV onward

Bias:

- registered eligible families

Requirements:

- registry family available
- sufficient containment or deliberate recklessness

### Request scaling

Every request calculates:

- base cost by country scale
- current lot and division burden
- prior requests this generation
- current congestion
- current control
- war urgency
- request family
- claimant influence
- anomalous saturation

Repeated requests have escalating costs, longer cooldowns, and stronger tail risk.

## Group F: Claimant management

### Grant Formal Command

Effect direction:

- improves assigned lots
- raises claimant influence
- sets a recognized role

### Limit the Command

Effect direction:

- grants a bounded district or unit count
- creates a measurable boundary whose violation can trigger incidents

### Reassign Loyal Formations

Effect direction:

- moves one or more lots out of claimant control
- requires replacement officers and supply
- can fail based on influence and local control

### Build a Counter-Command

Effect direction:

- creates loyal officer and depot networks
- lowers revolt risk over time
- expensive in army experience, equipment, and political stability
- starts the same dedicated response lock whether invoked from the decision,
  Muster Board, or AI path

### Meet the Demand

This is a family of timed claimant responses, not one generic button.

The visible requirement and cost match the actual demand.

### Refuse the Demand

The tooltip must explain broad visible risk without revealing the exact hidden revolt roll.

### Negotiate Retirement

Available when:

- the claimant has a path to honorable removal
- the state can offer status, protection, or a limited legacy

Success:

- reduces influence and can absorb formations

Failure:

- raises takeover or revolt risk

### Arrest the Claimant

High-risk action requiring loyal force, control of the headquarters state, and command preparation.

### Accept a Military Takeover

Avoids civil war at the cost of country political transformation. It is not available to every ideology or under every claimant archetype.

## Group G: Anomalous family management

### Open a Sealed Cantonment

- creates containment capacity in a selected state
- ties down guards and supply
- lowers saturation growth

### Appoint a Family Liaison

- improves command and readiness
- increases institutional permanence

### Issue Restricted Deployment Orders

- limits where or how anomalous units can operate
- lowers family incident risk

### Sustain the Family

- uses registry-specific resources
- prevents decay or loss
- can raise saturation

### Authorize Base Zombie Training

- only for the base zombie registry entry
- stronger variants remain blocked

### Manifest Ghost Reinforcements

- only through spawn effects and family conditions
- not a training decision

### Bind Golem Reinforcements

- only through spawn effects and material projects
- not a training decision

### Seal a Breach

- emergency action at high saturation
- large military, stability, or resource cost
- can fail and trigger derivative revolt

## Mission families

## Formation Roll Call

Owner:

- ordinary country

Objective:

- complete audit and officer assignment before deadline

Duration:

- dynamic, usually 90 to 180 days depending on country size and war

Success:

- control gain and lower informal loyalty

Failure:

- congestion and claimant susceptibility

## Standardization Cycle

Objective:

- maintain equipment, training, and control while compatible lots reorganize

The mission can auto-complete when all requirements remain met for the required period.

## Clear the Rail Network

Objective:

- maintain trains and named corridor access
- move or reduce heavy lots

Failure should have a real supply consequence.

## Establish the Command Districts

Objective:

- assign lots, officers, and states into a manageable structure

Success creates future efficiency and future claimant stakes.

## Meet the Claimant’s Deadline

Objective:

- provide the requested command, equipment, district, or political act before time expires

Failure triggers a claimant response based on influence rather than one universal revolt.

## Break the Claimant Network

Objective:

- remove loyal lots, secure depots, and build counter-command before a deadline

Possible partial success:

- depots secured but troops remain loyal
- troops reassigned but claimant keeps political influence

## Contain Anomalous Saturation

Objective:

- lower saturation or family pressure below a band while maintaining specific containment actions

Failure can open derivative revolt eligibility.

## Decision-only Formation Ledger surface

The accepted 2026-08-05 surface uses ordinary decisions rather than a custom
scripted GUI. `infantry_spawn_review_formation_ledger` rebuilds the shared lot,
generation, claimant, family, and request-cost caches without changing the
country. Existing lot, request, integration, demobilization, claimant, and
family decisions remain the substantive controls; every one carries its own
requirements, cost text, effect tooltip, and AI weight.

Evolution IV countries with more than one eligible registry family expose
`infantry_spawn_cycle_anomalous_family_decision`. Countries with more than one
live claimant file expose `infantry_spawn_cycle_claimant_file`. These are cursor
decisions only. They call the same revalidated selection helpers used by the
country AI, while AI selects the highest-pressure family and immutable pending
demand owner directly.

The category lifecycle, scenario isolation, civil-war safety, lot accounting,
and cleanup contracts are unchanged. The historical `muster_gui` variable names
are retained only for save compatibility and shared selection-cache code.

## Archived scripted-GUI design (superseded)

The following design notes document the former GUI proposal for provenance. They
are not runtime requirements after the accepted decision-only conversion.

## Entry point

A button in the Event 19 decision category opens a movable scripted GUI window after Evolution III. Before Evolution III, normal decisions and category text are sufficient.

The interface should not open automatically every time a lot changes.

## Tab 1: Overview

Displays:

- current generation
- unresolved lot count
- event division count
- Muster Control
- Army Congestion
- request cooldown
- current dominant burden
- active mission summaries

Controls:

- open audit
- begin standardization
- close generation when eligible

## Tab 2: Formation Lots

Displays a compact list of active lots.

Each lot card shows:

- working lot identifier
- origin state or region
- division count
- composition summary
- material quality
- coherence band
- supply burden
- equipment debt
- command owner
- integration state

The player selects one lot at a time. Only decisions relevant to that lot are shown.

This selected-lot design prevents a wall of per-lot decisions.

## Tab 3: Command

Visible only when a claimant exists.

Displays:

- primary claimant army/muster identity scene in the fixed portrait-slot widget
- personal name
- archetype summary
- influence
- assigned lots
- controlled district
- current demand
- revolt risk band
- rival claimant indicators

Controls call the same scripted effects and cost logic as decisions.

## Tab 4: Anomalous Registry

Visible only at Evolution IV.

Displays each locally available family:

- family icon
- source identity direction without parent-event spoilers
- trainable or spawn-only mode
- allowed base variant
- local unit count
- sustainment status
- family pressure
- derivative risk state

Controls:

- family-specific training or spawning action
- cantonment
- restricted deployment
- sustainment
- purge or containment

## Tab 5: Generation History

Optional compact local history showing recent generation outcomes. It should not duplicate the global Event Log window.

Useful fields:

- generation number
- date
- lots created
- lots integrated
- lots demobilized
- revolt or takeover result
- anomalous families involved

This tab can be omitted if it creates excessive implementation or performance burden. The global Event Log and a category summary are sufficient. The decision should be made during implementation after inspecting UI space.

## Archived GUI cost and tooltip rules

Every button must show:

- icon-first cost summary
- availability state
- blocked requirement summary
- detailed tooltip with named shortages or targets
- visible consequence direction
- cooldown or mission duration

When more than four costs apply, the button shows a short requirements status and the full list in a tooltip.

No button bypasses decision balance. The GUI and decisions call shared effects and triggers.

## Archived GUI animation plan

Animation should communicate state, not decorate every element.

### Muster Seal Pulse

Use:

- unprocessed lots exist

Target:

- decision category seal or Overview tab emblem

Plan:

- 8 real source frames
- subtle light and paper or metal response
- 6 to 8 frames per second
- looping
- static fallback

### Critical Command Border

Use:

- claimant revolt risk reaches critical band

Target:

- Command tab army/muster identity-scene panel border

Plan:

- 8 real source frames
- restrained pulse and wrong-direction shadow behavior
- 5 to 7 frames per second
- looping while critical
- static fallback

### Anomalous Registry Emblem

Use:

- anomalous family is active or saturation is rising

Target:

- Registry tab emblem

Plan:

- 10 real source frames
- family-neutral impossible movement or light
- slow loop
- static fallback

### Static-only decisions

The 20 claimant army/muster identity scenes remain static in their fixed portrait slots. Individual lot icons remain static. Animating all of them would add visual noise and a disproportionate asset burden.

Every final animation must follow the frame-sheet skill with separate source frames, processed frames, horizontal sheet, DDS, static fallback, contact sheet, and GIF review preview. A transformed still is not acceptable final animation.

## AI architecture

AI behavior exists at three levels.

### National policy profile

The country receives or recalculates one weighted profile:

- Professionalizer
- Territorialist
- Wartime Opportunist
- Gambler
- Panic Demobilizer
- Claimant Appeaser
- Counter-Command State
- Anomalous Exploiter
- Anomalous Containment State

The profile is not permanent. War, stability, supply, claimant state, and evolution can change it.

### Lot evaluation

For each lot, AI calculates:

- projected combat value
- supply cost
- equipment compatibility
- strategic role fit
- training cost
- claimant risk
- anomalous risk
- urgency

It chooses integrate, territorialize, standardize, isolate, cannibalize, demobilize, or claimant assignment.

### Strategic request decision

Before requesting a new formation, AI compares:

- force deficit
- enemy strength
- capital danger
- current congestion
- supply capacity
- equipment position
- request escalation cost
- claimant risk
- saturation

AI does not request because the decision is simply available.

## AI route validity

AI must never:

- train spawn-only units
- request a family not registered or locally eligible
- take a claimant decision after the claimant is invalid
- assign units to a dead or annexed target
- start a standardization mission with no compatible lots
- cannibalize a strategically essential prototype without considering war need
- trigger an impossible one-state civil war
- create a derivative country with no valid territory
- take a naval or distant expansion path it cannot reach
- spam requests during maximum congestion unless facing extreme defeat

## Tuning model

Important values must be centralized in script constants or a documented tuning table.

Required categories:

- state coverage curve
- selected-state minimum and smoothing
- units-per-state factors
- lot count limits
- training distribution
- equipment-fill distribution
- support-company distribution
- random battalion count distribution
- coherence band thresholds
- equipment compatibility burden
- control gains and losses
- congestion gains and decay
- request costs and escalation
- request cooldowns
- mission duration bands
- claimant influence gains and losses
- revolt risk factors
- saturation components
- derivative release thresholds
- derivative starting strength
- AI policy weights
- AI safety blockers

Do not scatter these values across event, decision, GUI, and country files.

## Balance principles

## More divisions can be a loss

The event is balanced by operational burden, not tiny combat modifiers.

A country can receive more nominal divisions and still become weaker because:

- supply collapses
- equipment is diluted
- officers are insufficient
- training stalls
- rail movement is blocked
- claimants control important formations
- technology-locked units cannot replenish

The player should feel this tradeoff immediately.

## Strong results deserve strong costs

An advanced armored or coherent high-quality lot can change a war. Its cost can include:

- large equipment debt
- high fuel use
- limited replacement
- claimant attachment
- long standardization
- large congestion

It should not be reduced to a tiny bonus merely to preserve ordinary balance.

## Weak results need a use

A weak one-battalion or understrength lot can still be:

- a garrison cadre
- a training base
- a territorial guard
- a source of limited specialist salvage
- a political liability
- an achievement opportunity

Bad results should create choices beyond deletion clicks.

## No equipment farming

Exploit controls include:

- audit lock
- partial delayed salvage
- equipment debt
- template conversion limits
- no free rerolls
- escalating request cost
- technology-locked reinforcement rules
- family-specific disband restrictions

## No free civil-war army

A claimant or derivative revolt receives actual loyal units and local resources. It does not gain a second unrelated army.

## No parent-event duplication

Derivative units and countries remain isolated from parent event progression unless a future explicit compatibility design says otherwise.

## Performance principles

The event is global and can affect many countries, so it must avoid unnecessary permanent loops.

Design direction:

- process each country during the event firing through one bounded pass
- store compact lot data rather than per-division arrays where possible
- use country-level pulse logic only while a country has an active generation, claimant, or saturation state
- avoid daily all-country on-actions
- use targeted timed events, decisions, or weekly country-specific pulses only when verified and permitted
- cap visible active claimants and lot cards without capping total useful divisions
- clean stale targets, templates, and variables after closeout
- rebuild GUI lists only when opened or when relevant data changes

Any whole-world recurring iteration requires explicit user permission under project rules. The event firing itself is the requested global operation. Persistent management should be country-scoped.

## Balance validation scenarios

Implementation should document at least these scenarios.

### Microstate at peace

- one to three states
- low industry
- no war

Expected:

- near-total state coverage
- small absolute force
- manageable baseline burden
- safe one-state claimant handling

### Continental major at war

- many states
- several fronts
- high industry

Expected:

- low proportional coverage but large absolute force
- multiple lots
- high supply and command burden
- stronger wartime readiness

### Large colonial empire

Expected:

- remote and occupied-state variation
- more irregular and mounted lots
- transport and loyalty problems
- no unit flood on every state

### Losing minor

Expected:

- emergency-useful formations
- severe debt and congestion
- AI willing to gamble

### High-control Evolution III country

Expected:

- random compositions remain surprising
- coherent results more common
- catastrophic tail still possible

### Low-control Evolution III country

Expected:

- absurd and catastrophic results more common
- claimant pressure rises
- recovery remains possible

### Evolution IV zombie user

Expected:

- base zombie training only
- saturation visible
- no parent zombie progression

### Evolution IV ghost derivative

Expected:

- spawn-only reinforcement
- slow population and wasteland effects
- genuine population loss enters the shared Deaths ledger exactly once under
  the Event 19 ghost-decline cause
- no Event 10 actor counts, souls, consumed-state progression, or super-events

### Triggerable maximum mutiny

Expected:

- immediate revolts and wars
- no invalid one-state partitions
- no terminal world-end flag

## Part 7 acceptance criteria

The decisions, UI, AI, and balance design are satisfied when:

- category content changes by phase
- obsolete decisions hide or replace themselves
- costs use military, equipment, supply, industrial, and political burdens that fit the action
- missions require real action and have success, failure, and partial success where useful
- selected-lot UI prevents decision clutter
- claimant and registry tabs appear only when relevant
- GUI buttons use the same effects and triggers as decisions
- only state-communicating assets are animated
- AI has national, lot, and request logic
- all important values are centralized
- performance avoids permanent daily all-country loops
- exploit and balance scenarios are part of implementation validation

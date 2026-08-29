# Event 32 specification, part 3: Operations and consequences

## Operation model

A missile attack is a prepared state-targeted operation.

Every operation must freeze:

- actor country
- victim country
- exact target state
- target profile
- participating launch states
- reserved missile count
- payload type
- payload stockpile receipt when relevant
- preparation start date
- planned launch date
- technology stage
- readiness snapshot
- command-control snapshot
- guidance inputs
- range or reach band
- attribution state
- causal incident ID
- parent incident ID when the launch is retaliatory
- automatic-retaliation generation when relevant

The operation record remains authoritative until it is completed, canceled, invalidated, or cleaned up.

## Operation sequence

1. select a valid target country
2. select an exact target state or target profile
3. select a strike profile
4. select payload when special delivery is available
5. calculate missile and resource cost
6. prove participating site capacity
7. reserve missiles and payload
8. begin preparation
9. allow bounded counterplay or cancellation where the route supports it
10. revalidate actor, target, sites, reserve receipt, and war state
11. resolve launch or abort
12. calculate interception, guidance, malfunction, and impact
13. apply exact damage and shared consequences once
14. write the incident record
15. schedule bounded readiness recovery and aftermath
16. clear the prepared-operation receipt

A prepared operation cannot silently retarget after the player has paid. If the target becomes invalid, the operation aborts or asks for a new target through an explicit route.

## Valid ordinary targets

Baseline conventional missile operations normally require:

- actor and target exist
- actor and target are at war
- target state is owned or controlled by the target or an active enemy partner
- target state is within the operational reach of at least one active launch state
- target is not allied to the actor
- target is not a neutral country
- target state is not a wasteland or invalid state
- the chosen target profile has at least one valid object or strategic value in the state
- actor has enough reserve, readiness, capacity, and command control
- actor has no active strike cooldown that blocks the chosen profile

Neutral and self-target outcomes are restricted to malfunction, rogue command, false signal, explicit scenario setup, or a future separate event route.

## Target profiles

A target profile determines what the operation is trying to destroy. It is not a separate payload.

### Logistics interdiction

Priorities:

- supply hubs
- railways
- infrastructure
- trucks and trains when a supported exact effect exists
- ports that carry supply
- fuel storage when present

Use when the actor is trying to weaken a front or isolate a region.

### Industrial strike

Priorities:

- military factories
- civilian factories
- dockyards
- refineries
- synthetic facilities
- strategic resource-processing buildings

Use against high-value production states. Civilian casualty risk is higher when the state is densely populated.

### Air and coastal suppression

Priorities:

- airfields
- radar
- anti-air
- naval bases
- coastal forts
- port infrastructure

Use to support air, naval, amphibious, or coastal operations.

### Command strike

Priorities:

- capital
- high-level command buildings or state modifiers
- launch sites
- radar and warning infrastructure
- military command nodes supported by the final implementation

Command strikes carry higher escalation and civilian risk. They should be more difficult to justify for restrained AI profiles.

### Counterforce strike

Priorities:

- Event 32 launch states
- nuclear or special-payload facilities
- rocket sites
- relevant warning or interception systems

This profile becomes more important after other countries have mature programs. Destroying a site should use the site damage contract, not only generic building damage.

### Broad strategic barrage

Distributes hits across several valid strategic objects in one exact state. It is less precise and more destructive than a profile-focused strike.

### Saturation barrage

Available only through Saturation Arsenals. It uses several launch states or a high-capacity site to overwhelm defenses and hit many objects. It creates the greatest readiness loss and malfunction exposure.

## Strike profiles

### Precision strike

Purpose:

- destroy one high-value target family
- minimize reserve use and collateral damage
- preserve readiness

Suggested payment:

- `1` to `2` missiles
- fuel
- command-power allocation or equivalent command commitment

Suggested effects:

- highest guidance
- lower building damage spread
- lower civilian death risk
- longer preparation when intelligence is weak
- unavailable at low readiness

### Strategic barrage

Purpose:

- damage several strategic objects in one state
- impose sustained industrial or logistics pressure

Suggested payment:

- `3` to `6` missiles
- fuel
- command commitment
- optional support equipment for preparation

Suggested effects:

- moderate guidance
- broad building damage
- meaningful readiness loss
- higher civilian risk

### Saturation barrage

Purpose:

- overwhelm defenses and inflict major strategic damage
- support a decisive offensive or retaliatory wave

Suggested payment:

- `8` to `16` missiles
- large fuel cost
- command commitment
- optional stability, war-support, or special program pressure as a consequence

Suggested effects:

- defense saturation
- lower per-missile guidance
- high chance that at least one missile malfunctions under Unreliable Guidance
- severe readiness loss
- long cooldown
- high escalation
- possible multi-state spread only when the selected operation explicitly includes several exact targets

A saturation operation must not use a hidden random-world target pool.

## Reach

Reach should derive from:

- normalized technology stage
- selected launch state
- target state
- terrain and geography only when the engine provides a reliable exact route
- special payload mass or complexity
- temporary range investment
- Saturation Arsenals evolution

The player sees a simple reach result:

- in range
- extended range with penalty
- out of range

The implementation must not claim exact geographic reach if it uses only country adjacency or capital distance. Use the most accurate engine-supported method and document its limitations.

## Preparation time

Suggested preparation bands:

| Operation | Preparation target |
| --- | --- |
| Precision strike | `10` to `20` days |
| Strategic barrage | `14` to `30` days |
| Saturation barrage | `21` to `45` days |
| Emergency retaliation | `2` to `7` days based on posture |
| Special payload integration | additional preparation before the strike can begin |

Preparation time changes with:

- readiness
- technology
- recent launch activity
- site damage
- command control
- payload complexity
- intelligence
- war emergency
- automatic-retaliation posture

A shorter preparation time should usually create higher failure or command risk.

## Launch commitment point

Each operation has one commitment point.

Before commitment:

- the player can cancel
- most reserved missiles return
- some readiness may be lost
- payload stockpile normally returns

After commitment:

- cancellation may consume missiles, payload, or fuel
- crew or site disruption may occur
- a visible abort event may fire
- an attempted special-payload launch may still create evidence or condemnation if the attempt became public
- confirmed use is not recorded unless the payload was released

## Guidance resolution

Guidance resolution selects one of these ordinary outcomes:

| Outcome | Meaning |
| --- | --- |
| On target | Intended state and target profile |
| Degraded hit | Intended state, reduced target accuracy, more collateral damage |
| Wrong object | Intended state, different strategic object |
| Near miss | Limited infrastructure or population damage |
| Breakup or dud | Missile fails before meaningful target effect |
| Wrong state | Adjacent or bounded alternative state |
| Neutral drift | Neutral state inside the verified drift pool |
| Self-strike | Actor state inside the verified return or launch-accident pool |
| Launch-site accident | Damage at the participating site |

Baseline guidance should make serious accidents rare. Unreliable Guidance changes the probability model and unlocks the broader outcomes.

## Bounded drift pools

A wrong-state result must use a physically and politically defensible pool.

Preferred order:

1. state adjacent to the intended target
2. state in the same strategic region
3. state along a verified route or range corridor
4. nearby neutral state when the evolution and geometry allow it
5. actor launch state for a launch or return failure

Do not select a completely unrelated random state elsewhere in the world.

The implementation must freeze the candidate pool before the random roll and pass the full pool to probability inspection.

## Conventional damage model

Conventional missile damage should scale with:

- missiles that reached the target
- strike profile
- warhead strength
- target building levels
- guidance result
- target anti-air or interception
- state infrastructure
- hardening of the specific target
- target population density for collateral deaths
- target defense saturation
- recent prior attacks and remaining valid building levels

Suggested per-operation damage bands:

### Precision strike

- one selected target family
- `1` to `3` building levels damaged or destroyed
- small infrastructure spillover
- low proportional civilian loss

### Strategic barrage

- several target families
- `3` to `8` total building-level damage points
- infrastructure and railway damage
- moderate proportional civilian loss

### Saturation barrage

- several strategic targets
- `8` to `20` total building-level damage points, bounded by real levels
- severe infrastructure and supply disruption
- high proportional civilian loss
- possible temporary state disruption modifier

These are balance targets. Damage must clamp against actual buildings. A strike cannot destroy levels that do not exist.

## Civilian deaths

A populated state can suffer civilian deaths from:

- direct impact
- blast
- structural collapse
- infrastructure failure
- port or industrial fires
- special payloads
- a launch-site accident
- a wrong-state or neutral strike

Every civilian loss must use the shared exact state population-loss and Deaths contract.

Inputs should include:

- actual state population
- missiles that hit
- target profile
- guidance outcome
- population density
- shelters or protection
- payload
- hardening of the target
- whether a capital or urban industrial state was selected
- whether the hit was accidental

Suggested conventional loss bands should remain lower than nuclear or thermonuclear effects. The exact tuning belongs in shared constants and must be audited against ordinary strategic bombing.

Deaths are recorded once. Event 32 must not reduce state population directly and then call the Deaths API for the same loss.

## Military losses

Conventional strikes can create military deaths when:

- a launch site is hit
- divisions are present at an exact target province or state and the engine-supported adapter can prove it
- a command, airfield, port, or supply target contains military personnel
- a launch-site accident kills crews

Military losses use the shared military Deaths route where available. Do not invent precise unit casualties from a state-level strike unless the engine can prove and apply them safely.

## Interception and defense

Missile defense should use existing engine values where they can be proven.

Possible inputs:

- anti-air
- radar
- interception or raid defense
- air superiority
- missile-defense technology if present
- warning readiness
- target intelligence
- saturation level

Defense can:

- destroy missiles
- divert missiles
- reduce guidance
- force higher barrage cost
- protect one target family
- create debris damage

Defense must not guarantee complete safety from a large saturation barrage.

## Readiness cost

Every completed or attempted launch reduces Launch Readiness.

Suggested conceptual loss:

- fixed operation cost
- plus missiles launched multiplied by a small factor
- divided by the number and quality of participating sites
- increased by special payload complexity
- increased by site damage
- capped to prevent one ordinary precision strike from setting readiness to zero

Suggested anchors:

| Operation | Typical readiness loss |
| --- | --- |
| Precision | `5` to `10` |
| Strategic barrage | `10` to `20` |
| Saturation barrage | `20` to `35` |
| Emergency retaliation | normal cost plus posture penalty |
| Failed launch | partial or full cost based on outcome |

Readiness recovery occurs through:

- Restore Launch Readiness decision
- maintenance investment
- repair completion
- one-shot delayed recovery after a launch
- a later Event 32 firing
- valid test-data bridges

Do not run a global periodic recovery scan.

## Command-control effects of launching

Ordinary authorized launches should create a small temporary command burden.

Command Control falls more when:

- the country uses delegated or automatic posture
- the government is unstable
- several sites launch at once
- a special payload is used
- the launch is retaliatory under uncertain attribution
- a launch fails
- orders are disputed
- an unauthorized launch occurs

A successful verified launch under secure control can provide a small recovery receipt after the incident is closed.

## Special payload integration

Special Warheads allows missile delivery for payloads the country already owns.

Supported payload adapters:

- conventional high explosive
- chemical
- biological
- nuclear
- thermonuclear

The country must prove:

- relevant technology or project
- relevant policy or weapon-system access
- sufficient physical stockpile
- a compatible missile technology stage
- a compatible launch site
- enough reserve
- payload-integration preparation
- any shared CBRN command and protection gate

Event 32 grants delivery integration. It does not grant the payload technology or stockpile.

## Chemical payload

A chemical missile strike must:

- select one exact target state
- consume matching chemical payload equipment
- consume missiles
- call the shared chemical exposure pipeline
- create contamination and disruption according to the selected agent
- register evidence and attribution
- add chemical condemnation
- register civilian and military deaths
- add Air Cleanliness pressure once
- create confirmed-use history only after release

If the shared chemical system cannot prove an exact release, the option remains unavailable.

## Biological payload

A biological missile strike must:

- select one exact target state
- consume matching biological stockpile
- consume missiles
- call the shared biological strike or outbreak pipeline
- seed only the selected supported agent or profile
- register evidence, attribution, outbreaks, deaths, and condemnation
- avoid duplicating outbreak progression owned by the biological system

Event 32 must not invent a generic plague substitute when the chosen biological payload cannot be resolved.

## Nuclear payload

A nuclear missile strike must:

- consume one supported nuclear weapon or stockpile unit
- consume missiles
- call the shared nuclear consequence route
- apply the correct visual effect through the owning system
- apply immediate population and building effects
- apply fallout
- add Air Cleanliness pressure
- add nuclear condemnation
- register deaths
- add chaos through the shared ladder

Event 23 can supply Soviet weapons. Event 32 supplies the missile delivery route after Special Warheads.

## Thermonuclear payload

A thermonuclear missile strike follows the same ownership boundary as a nuclear strike with the stronger shared thermonuclear effects.

Event 32 must not reimplement the `+1.5%` Air Cleanliness source or any later Fallout transition. It calls the shared route once.

## Evidence and attribution

Every launch incident stores an attribution state.

Suggested states:

- confirmed actor
- highly likely actor
- disputed actor
- unknown actor
- forged attribution
- false warning with no launch
- accidental actor disclosure

Attribution should derive from:

- visible launch state
- intelligence
- radar or warning coverage
- captured debris
- public claim
- command records
- false-signal interference
- rogue command
- foreign intelligence operation
- guidance failure

Ordinary conventional launches by a known belligerent are usually confirmed. Rogue, false-warning, and third-party incidents create uncertainty.

## Diplomatic consequences

### Authorized conventional strike in war

Possible consequences:

- opinion loss
- world tension or chaos change
- target war-support response
- retaliation pressure
- no CBRN condemnation

### Capital or civilian-centered conventional strike

Possible consequences:

- stronger opinion loss
- greater chaos
- neutral monitoring
- heavier retaliation pressure
- more civilian deaths

### Neutral accidental strike

Possible consequences:

- diplomatic incident
- demand for compensation or inspection
- guarantee or war-entry pressure
- possible mistaken retaliation
- reduced Command Control and readiness
- public evidence record

### Special payload

Use the shared Condemnation system. Do not add a separate Event 32 sanctions ladder.

## Incident record

Every meaningful launch, failure, capture, false warning, or unauthorized order receives one incident ID.

Required fields:

- incident ID
- incident type
- date
- actor ID
- victim ID
- target state ID
- intended target state ID when different
- payload
- missile count
- missiles that launched
- missiles that hit
- attribution state
- civilian deaths
- military deaths
- building damage summary
- contamination or outbreak result
- causal parent ID
- retaliation generation
- closed or active state

The implementation can store only the fields needed by game logic and visible logs. A debug or documentation receipt should prove the full transaction.

## Causal chain controls

Retaliation and mistaken-response chains must have strict limits.

Suggested limits:

- maximum retaliation generation `3`
- maximum participating countries per root incident `6`
- maximum active linked incidents per root `12`
- maximum missiles launched by automatic branches per root set by constants
- one retaliation receipt per country per root incident
- one processed warning receipt per country per root incident
- one final closure event when the root chain ends

A country cannot retaliate twice for the same root incident unless a distinct later strike creates a new root.

## Automatic-retaliation trigger bridge

Every qualifying missile or special-payload strike calls a shared Event 32 warning helper after its effects are committed.

The helper checks:

- victim has Event 32 program
- Automatic Retaliation evolution is active
- victim posture permits warning processing
- victim has surviving sites, reserve, and readiness
- root incident has not reached the chain cap
- victim has not processed this root
- attacker or attribution candidate exists

The helper creates a bounded warning event or mission. It does not launch immediately inside the original damage block.

## False warning

A false warning can arise from:

- Unreliable Guidance debris or route confusion
- damaged radar or command network
- obsolete warning equipment
- forged foreign signal
- rogue launch crew
- high command-control fragmentation
- simultaneous real and false incidents

A false warning has no confirmed launch record. It can still trigger emergency decisions, readiness loss, diplomatic accusations, or automatic retaliation if the system fails.

## Player counterplay

The player should have concrete ways to reduce harm:

- maintain readiness
- improve guidance
- harden sites
- increase site security
- centralize or distribute command
- verify warning data
- disable one command path
- rotate codes
- recall delegated authority
- repair communications
- scuttle a captured or mutinous site
- compensate a neutral victim
- accept inspections or deny responsibility where supported
- keep automatic posture disabled

No investment eliminates all risk. High control and high readiness should make ordinary authorized operations reliable.

## AI parity

Every player operation and emergency response needs an AI equivalent.

AI does not need to use the human selected-target UI. It can call the same prepared-operation API after choosing an exact country, state, profile, payload, and participating sites through audited weighted logic.

## Cleanup

An operation closes when:

- launch resolves
- target becomes invalid before commitment
- actor loses every participating site
- reserve or payload receipt becomes invalid
- actor ceases to exist
- victim ceases to exist and no valid successor target remains
- war ends before commitment and the route does not permit a peacetime strike
- player cancels
- scenario reset clears the program
- a terminal shared system freezes incompatible future launches

Cleanup must:

- return or consume reserved resources according to commitment state
- clear site operation receipts
- clear delayed events or make them fail closed
- update readiness and control once
- close the incident
- refresh decisions and program display

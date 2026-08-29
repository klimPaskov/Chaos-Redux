# Event 32 specification, part 6: AI and probability

## AI design goal

AI countries must treat missiles as finite strategic assets.

The AI should:

- maintain a usable reserve
- keep sites operational
- choose targets that support its current war
- avoid wasteful launches
- understand readiness and command risk
- use saturation only when the target and reserve justify it
- treat special payloads as high-consequence weapons
- respond to rogue incidents
- verify uncertain warnings when time allows
- stop automatic chains at the same hard caps as the player

The AI must not launch merely because a decision is available.

## AI doctrine profiles

Each missile country receives one current AI profile derived from government, strategy, war state, industry, threat, event history, and program condition.

Profiles can change as the campaign changes.

### Restrained deterrent

Priorities:

- secure reserve
- high Command Control
- supervised retaliation
- precision strikes
- counterforce only after enemy launch
- special payloads prohibited or retaliatory only
- strong reluctance to hit capitals and neutral-adjacent states

Likely contexts:

- stable democracies
- neutral countries
- countries under high condemnation pressure
- small countries with limited reserve
- faction members protected by stronger allies

### Conventional interdiction

Priorities:

- logistics
- ports
- airfields
- industrial targets
- moderate reserve floor
- precision and strategic barrages
- limited capital targeting
- special payloads rare

Likely contexts:

- ordinary wartime AI
- regional powers
- countries supporting an active offensive

### Saturation offender

Priorities:

- large reserves
- rapid replenishment
- broad strategic barrages
- defense saturation
- lower reserve floor during decisive war
- shorter cooldowns
- willingness to hit major industry and command targets

Likely contexts:

- Saturation Arsenals adopters
- total war
- large industrial powers
- high-aggression strategies

### Counterforce guardian

Priorities:

- enemy launch states
- nuclear and special-payload facilities
- radar and warning nodes
- reserve preservation
- high site hardening
- supervised or delegated retaliation
- low civilian-target willingness

Likely contexts:

- countries facing several missile powers
- countries with strong intelligence
- countries that have suffered a missile attack

### Special-warhead escalator

Priorities:

- payload integration
- high-value military targets
- retaliatory special use
- stronger command security
- high consequence tolerance
- careful stockpile accounting

Likely contexts:

- countries with supported payloads
- extreme war state
- ideological or event-specific escalation
- enemy first use

This profile still respects condemnation, stockpile, target, and survival conditions.

### Brittle command

Priorities:

- emergency security
- code rotation
- site isolation
- low launch willingness
- high risk of poor decisions under capital threat
- preference for scuttling indefensible sites

Likely contexts:

- low stability
- low Command Control
- civil war
- recent coup
- captured or damaged sites

### Rogue command

This is an incident actor, not a normal national strategy.

Priorities depend on the incident:

- threaten government
- launch at local enemy
- defect
- sell codes
- fire a special payload
- hold site for negotiation
- scuttle instead of surrender

The national AI should oppose or negotiate with it through crisis actions.

### Retaliation network

Priorities:

- maintain warning and response capability
- verify uncertain alerts
- respond to confirmed high-severity attacks
- avoid duplicate responses
- preserve chain caps
- choose posture based on control and survivability

## Profile assignment

The profile helper should use ordered conditions.

Example ordering:

1. active rogue incident
2. active retaliation emergency
3. brittle command
4. special-warhead escalation
5. saturation offense
6. counterforce guardian
7. conventional interdiction
8. restrained deterrent

A country should have one main profile plus limited secondary modifiers.

Do not assign ten overlapping strategy flags that make AI intent unreadable.

## Reserve doctrine

Every profile has a reserve floor.

Suggested conceptual floors:

| Profile | Reserve floor |
| --- | --- |
| Restrained deterrent | high |
| Conventional interdiction | moderate |
| Saturation offender | low during decisive war, moderate otherwise |
| Counterforce guardian | high |
| Special-warhead escalator | separate conventional and payload floors |
| Brittle command | high because launches are risky |
| Retaliation network | enough for one planned response |

The reserve floor should scale with:

- enemy missile count
- number of active fronts
- site capacity
- retaliation posture
- country size
- recent launch rate
- expected Event 32 repeat timing

AI cannot spend reserved payloads twice.

## Maintenance AI

AI should replenish when:

- reserve is below doctrine floor
- industry can absorb the burden
- no urgent command crisis blocks production
- fuel and support equipment remain above protected floors
- a launch is expected soon
- Event 32 repeat package is not due through a deterministic timer known to the system

AI should restore readiness when:

- readiness blocks the profile's preferred strike
- an active warning requires response
- a damaged site has been repaired
- a large reserve would otherwise remain unusable

AI should secure command when:

- Command Control falls below profile minimum
- special payload integration is active
- a new site is captured
- Rogue Launch Commands is active
- automatic posture is selected

AI should harden or expand a site when:

- site is exposed to enemy reach
- reserve exceeds capacity
- current site is the only command node
- territory supports redundancy
- industry can afford the project
- no more urgent repair exists

## Target-country scoring

The target-country pool contains only valid enemies or incident-authorized candidates.

Positive weights:

- at war with actor
- high war contribution against actor
- active front against actor
- controls actor cores
- has large industry
- has supply hubs supporting the front
- has ports or airfields supporting attacks
- has missile launch states
- has used missiles against actor
- has used a special payload against actor
- threatens actor capital
- is the verified attacker in a retaliation incident

Negative or zero weights:

- ally or faction partner
- subject of actor unless an explicit civil conflict permits targeting
- neutral without an incident route
- dead or landless country
- no reachable state
- truce or peace when ordinary strike requires war
- only low-value isolated states
- current selected target invalidated
- already processed for the same retaliation root
- severe diplomatic cost with little military value
- no reserve after operation

The full candidate pool must be passed to probability inspection.

## Target-state scoring

The state pool is built from the selected target country and strike profile.

### Logistics profile

Positive factors:

- supply hub
- high railway level
- key infrastructure
- port carrying supply
- front support
- central position in supply network

### Industrial profile

Positive factors:

- military factories
- civilian factories
- dockyards
- refineries
- high building concentration
- strategic resource production

### Air and coastal profile

Positive factors:

- airfield
- radar
- anti-air
- naval base
- coastal fort
- active air or naval operations

### Command profile

Positive factors:

- capital
- command state modifier
- radar and warning network
- high-value government or military node

### Counterforce profile

Positive factors:

- active Event 32 launch state
- high site capacity
- special payload custody
- nuclear or rocket facility
- retaliation network role

Common negative factors:

- no valid target object
- wasteland
- very low population and infrastructure
- isolated empty island
- already destroyed target
- allied occupation that would create friendly fire
- high neutral adjacency under Unreliable Guidance
- special protected state when the route forbids it

## Strike-profile selection

AI evaluates:

- current war objective
- target profile value
- reserve
- readiness
- site capacity
- command control
- evolution state
- expected damage
- collateral risk
- retaliation risk
- condemnation
- cooldown
- urgency

Expected ordering:

- precision dominates when reserve is low, target value is concentrated, or collateral risk is high
- strategic barrage dominates when several targets exist and readiness is operational
- saturation dominates only when reserve, capacity, target density, and war urgency are high
- counterforce dominates after enemy missile use or when a launch state is exposed
- special payload selection remains a separate gate

## Payload selection

The AI must first prove eligibility.

Then it scores:

- enemy first use
- target military value
- target population
- own policy
- condemnation tier
- sanction vulnerability
- payload scarcity
- command control
- guidance risk
- retaliation risk
- war survival
- faction promises
- target special-payload capability
- expected shared-system effect

Hard blockers:

- no stockpile
- no technology
- no integration
- invalid target
- policy prohibited
- guidance below special-payload minimum
- command control below minimum outside rogue route
- target ally
- duplicate payload reservation

Nuclear and thermonuclear use should remain rarer than chemical or biological use when all are available, unless the country is responding to matching first use or faces imminent defeat.

## Site selection AI

The site-scoring system is shared between player automatic selection and AI.

The audit should prove:

- protected interior state outranks exposed capital when both are valid
- existing site upgrade outranks unnecessary new site
- different strategic region gains weight for redundancy
- one-state minor selects its only valid state
- empty isolated island does not beat a connected core state
- active frontline state receives zero or near-zero weight when safer states exist
- a captured compromised site is not treated as ordinary secure capacity

## Rogue incident AI

The incident selector should weight countries by real vulnerability.

Positive factors:

- low Command Control
- low stability
- civil war
- captured site
- recent coup
- several sites
- large reserve
- special payload custody
- damaged communications
- foreign intelligence access
- site isolation

Protective factors:

- recent code rotation
- high security
- high stability
- loyal garrison
- one secure site
- low reserve
- no eligible foreign actor

Incident choice should match the state.

Examples:

- foreign bribery requires a valid foreign actor
- crew defection requires a valid destination
- regional seizure requires weak central control
- rogue special-payload custody requires physical payload at the site
- unauthorized launch requires reserve and a usable site

## Unreliable outcome probability

The model should separate:

1. launch success
2. target accuracy
3. severe accident
4. attribution outcome

This prevents one roll from simultaneously deciding every consequence.

Expected constraints:

- high technology, high readiness, secure site, short range, and small barrage should produce a high on-target rate
- low readiness, damaged site, long range, and saturation should produce a meaningful but bounded failure rate
- severe neutral or self-strike outcomes remain a minority of failures
- special payload complexity raises severe-failure risk
- maintenance investment materially shifts outcomes
- no scenario produces negative probability or an unnormalized hidden pool

## Automatic-retaliation AI

### Posture choice

AI considers:

- command control
- warning quality
- site survivability
- enemy threat
- current war
- recent attacks
- reserve
- government strategy
- special-payload policy
- alliance support

Expected behavior:

- low control blocks ordinary automatic posture
- high threat plus high control favors delegated or automatic
- restrained profile favors supervised
- recent verified attack increases stronger-posture willingness
- false-warning history reduces automation willingness
- one-site minor with poor survivability may choose delegated despite risk
- rogue command can force a posture outside government preference through an incident

### Warning response

AI should:

- verify uncertain warnings when response time permits
- sever the network when control is lost
- isolate compromised sites
- retaliate against confirmed attacker
- avoid attacking a low-confidence candidate when verification is available
- preserve chain caps
- use payload policy
- avoid duplicate response

## MTTH and evolution probability

Each evolution uses a complete eligibility gate and an MTTH model.

The auditor should inspect:

- base MTTH
- chaos-tier factor
- number of program countries
- number of launches
- global reserve
- vulnerable-country count
- payload-owner count
- hostile missile-pair count
- disabled evolution state
- already recorded state

Expected ordering after all tracks are eligible:

- Saturation Arsenals should usually unlock fastest at Chaos Tier due its `90` day target
- Unreliable Guidance should become likely when launch and backlog pressure are high
- Rogue Launch Commands should accelerate in widespread instability
- Special Warheads should remain slow when only one payload owner exists
- Automatic Retaliation should remain the slowest ordinary track and require at least `900` chaos

## Required probability workflow

Every weighted surface requires:

1. `hoi4.probability_inspect`
2. named scenario definitions
3. complete candidate pool where normalization applies
4. `hoi4.probability_evaluate` for exact scenarios
5. `hoi4.probability_sweep` for sensitive thresholds
6. `hoi4.probability_simulate` for bounded random chains where exact evaluation is insufficient
7. `hoi4.probability_compare` after the final source patch
8. `hoi4.probability_render` when a matrix or sensitivity chart improves review

Use `hoi4.probability_sequence` only for the declared evolution, replenishment, or retaliation sequence after cadence, recovery, caps, removals, cooldowns, resets, and terminal states have been fully declared.

The probability auditor is read-only. The implementation owner chooses the balance target and applies the patch.

## Required audit surfaces

- recipient profile selection when weighted
- first-site selection
- secondary-site selection
- target-country selection
- target-state selection
- strike-profile selection
- payload selection
- AI maintenance decisions
- AI posture selection
- Unreliable Guidance outcome pool
- Rogue Launch Commands country selection
- rogue incident type selection
- false-warning actor attribution
- automatic-retaliation response
- evolution MTTH
- SCN-015 profile-specific random setup

## AI exploit and failure checks

The AI audit must check for:

- reserve spending below zero
- repeated free replenishment
- launch without site capacity
- launch after target invalidation
- repeated response to the same incident
- unlimited automatic chain
- special payload without stockpile
- target selection against allies
- one target monopolizing every weighted pool
- low-value state starvation of valid high-value targets
- permanent maintenance loop that prevents launch
- permanent launch loop that prevents maintenance
- saturation use against empty states
- automatic posture under zero control
- scuttle loop on the same site
- duplicate capture transfer
- AI scenario setup that partially mutates after preflight failure

## Balance interpretation

Exact probabilities are implementation evidence, not design prose.

The final report should state:

- scenario ID
- source revision
- candidate-pool completeness
- exact, bounded, sampled, score-only, or unresolved result
- expected ranking
- observed ranking
- final patch comparison
- remaining uncertainty

A statement such as "AI looks reasonable" is not sufficient.

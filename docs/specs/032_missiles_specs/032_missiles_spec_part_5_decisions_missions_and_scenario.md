# Event 32 specification, part 5: Decisions, missions, and scenario

All decision, mission, phase, scenario, and action names in this file are working design labels. Implementation must write final player-facing localisation from the stated direction and project writing rules.

## Presentation choice

Event 32 uses an ordinary decision category with:

- one event-owned category icon
- one static category picture
- a compact dynamic header
- phased decision visibility
- a separate selected-target flow for human strike preparation
- state and target tooltips
- ordinary timed missions for preparation, repairs, verification, and crisis response

Use the ordinary decision system. The mechanic has three main national values, one selected target at a time, and actions that fit the category. A custom window would add layout, asset, and maintenance work without improving target control or value clarity.

The category picture is presentation only. It should show a launch-control or missile-site scene. It must not contain painted buttons, fake meters, numbers, labels, or controls.

## Category header

The main header should expose:

1. Operational Reserve
2. Launch Readiness
3. Command Control

Additional compact status lines:

- normalized missile stage
- active launch-site count
- current guidance grade
- selected target when one exists
- retaliation posture when Evolution V is active
- active program crisis when one exists

The header should not show every internal pressure component.

Each value needs:

- a texticon or clear icon
- current value or band
- next relevant threshold
- one concise tooltip explaining what changes it
- one concise tooltip explaining the current consequence

## Decision visibility budget

The main program phase should normally show three to five primary decisions.

The hard maximum is six visible primary actions in one phase.

Active missions should normally remain between one and three.

Targeted strike actions appear only after one target country has been selected. Emergency actions replace ordinary actions where possible instead of appearing beneath them.

## Decision category phases

### Phase 1: Program establishment

Visible when:

- program has just initialized
- no usable launch state exists
- technology normalization is incomplete
- a captured site has not been resolved

Main actions:

- survey a launch state
- resolve a captured site
- establish command authority
- inspect the new arsenal
- restore a deferred program

This phase should disappear after the program is operational.

### Phase 2: Maintenance and expansion

Visible during ordinary peacetime and war when no launch is being prepared.

Main actions:

- replenish operational reserve
- restore launch readiness
- improve guidance and maintenance
- secure launch authority
- harden a launch state
- expand site capacity
- establish a secondary site when justified

The category should show only the actions currently useful. A fully hardened site should not keep a dead hardening decision visible.

### Phase 3: War operations

Visible when:

- actor has a valid enemy
- actor has reserve
- actor has a usable site
- readiness and command meet the selected operation minimum
- no incompatible prepared operation is active

Main actions:

- select missile target
- prepare precision strike
- prepare strategic barrage
- prepare saturation barrage when available
- prepare counterforce strike
- integrate or select special payload when available

### Phase 4: Prepared operation

Visible while one operation is active.

Main actions:

- inspect operation
- cancel before commitment
- change participating site before commitment
- increase preparation effort where allowed
- launch when the mission completes
- abort after target invalidation

Ordinary maintenance and expansion actions should hide when they would invalidate the prepared operation.

### Phase 5: Incident response

Visible during:

- guidance failure
- neutral accidental strike
- launch-site accident
- captured site
- mutiny
- unauthorized launch preparation
- code compromise
- disputed attribution

Main actions depend on the incident. The phase should not show unrelated routine program buttons.

### Phase 6: Retaliation emergency

Visible during an active warning after Evolution V.

Main actions:

- verify warning
- delay retaliation
- sever network
- isolate one site
- change target after new evidence
- accept current response
- restore control after stand-down

## Cost design

Each action may consume at most four spendable cost types.

Custom Event 32 values need proper texticons.

Potential cost types:

- operational missiles
- fuel
- support equipment
- manpower
- civilian factory commitment
- military factory output burden
- command power
- air XP
- army XP
- trains
- convoys for overseas sites
- stability
- war support
- intelligence exposure
- readiness
- command control

Readiness and Command Control can be consequences or custom-value costs. The final presentation must distinguish payment from outcome.

Political power should appear only where an action is genuinely political, diplomatic, or administrative. It is not the default missile-program currency.

## Program establishment actions

### Survey for a launch state

#### Visibility

- program exists
- no active controlled launch state
- at least one eligible state exists
- no survey mission active

#### Action

Freezes a candidate pool and starts a short survey mission.

#### Requirements

- controlled state
- valid site geometry and building surface
- no terminal program cleanup
- no active program transfer

#### Suggested costs

- support equipment
- civilian factory commitment
- manpower

#### Success

- selects the highest valid scored state
- creates the primary site
- grants initial capacity
- refreshes program status

#### Failure

Failure should occur only when the frozen state becomes invalid. Resources return according to progress, and the player gets a precise blocked reason.

### Establish command authority

#### Visibility

- first program initialization
- Command Control has not been initialized or is below secure baseline
- no active rogue incident

#### Action

Creates the first code, crew, and command structure.

#### Suggested costs

- command power
- support equipment
- manpower

#### Result

- raises Command Control to the initial secure band
- enables ordinary launch preparation
- sets the first command receipt
- calls Event 16's missile-crisis reaction helper when the recipient is the active Kruger host and the helper has not been recorded

### Resolve a captured site

This is a category of mutually exclusive resolution decisions:

- secure and inspect
- integrate
- scuttle
- transfer through an explicit diplomatic route
- hold inactive

The category appears only for the selected captured state. It hides after resolution.

## Maintenance actions

### Replenish operational reserve

#### Meaning

Commit industry, fuel, and components to produce or assemble a new missile batch.

#### Suggested formula

- base batch from technology stage
- economy-scaled contribution
- site-capacity contribution
- saturation multiplier when active
- lower output under fuel shortage, damage, or low readiness
- bounded cap

#### Suggested costs

Choose up to four:

- military factory output burden
- fuel
- support equipment
- manpower

#### Cooldown

- ordinary: about `60` to `90` days
- saturation: shorter after investment, but never instant

#### AI

Prioritize when reserve is below doctrine floor and the country can afford the burden.

### Restore launch readiness

#### Meaning

Run maintenance, fueling, communications checks, and crew drills.

#### Suggested costs

- fuel
- support equipment
- command power

#### Result

- raises readiness by a dynamic amount
- clears a minor backlog
- improves next-operation guidance
- cannot exceed the cap
- weaker while a site is damaged

#### Cooldown

Shorter than replenishment, about `30` to `60` days.

### Improve guidance and maintenance

#### Meaning

Replace components, recalibrate guidance, and retrain crews.

#### Suggested costs

- air XP or army XP based on final precedent
- support equipment
- civilian factory commitment

#### Result

- reduces derived guidance pressure
- creates a timed maintenance receipt
- raises readiness
- reduces Unreliable Guidance risk
- may unlock precision strike at a threshold

This action must not grant an unrelated technology.

### Secure launch authority

#### Meaning

Rotate codes, inspect crews, verify command links, and reduce delegated access.

#### Suggested costs

- command power
- support equipment
- temporary readiness loss

#### Result

- raises Command Control
- lowers rogue pressure
- invalidates stolen or compromised codes
- may isolate one site while work is underway

### Harden a launch state

#### Selection

Use a selected-site decision. Only active controlled sites below hardening cap appear.

#### Suggested costs

- civilian factory commitment
- support equipment
- manpower
- trains when the state needs heavy inland transport

#### Result

- raises hardening one stage
- adds temporary construction burden
- improves strike and capture resistance

### Expand site capacity

#### Requirements

- site active
- below capacity cap
- country reserve or technology justifies expansion
- no active serious damage

#### Suggested costs

- military factory output burden
- support equipment
- fuel for testing
- manpower

#### Result

- raises operation capacity
- may increase maintenance burden
- refreshes site modifier

### Establish a secondary launch state

#### Requirements

- country below site cap
- primary site fully established
- redundancy or capacity condition true
- valid state in a different strategic region where possible
- enough industry and command control

#### Suggested costs

- civilian factory commitment
- support equipment
- manpower
- trains or convoys depending geography

#### Result

Starts a long construction mission and creates the second site on success.

## Strike target selection

Human target management uses a separate target category.

### Select target country

One selector decision appears for each valid enemy only when the target-management category is open. Selecting one country:

- stores the selected target ID
- sets a temporary selected-target flag
- rebuilds target-state actions for that country
- hides other target-specific decisions from the human player

### Clear target

Clears:

- selected target ID
- target flag
- selected target state
- pending target profile
- visible target decisions

It does not cancel an already committed operation.

### AI

AI bypasses the human selector and evaluates the full candidate pool through the shared target-scoring helper.

## Strike preparation actions

### Prepare precision strike

#### Requirements

- selected enemy
- exact valid target state
- readiness in operational band
- command control above contested minimum
- reserve and site capacity
- no strike cooldown
- target profile has a valid target

#### Suggested costs

- operational missiles
- fuel
- command power

#### Mission

Creates a preparation mission of about `10` to `20` days.

#### Result

On mission completion, launch becomes available.

### Prepare strategic barrage

#### Requirements

Higher reserve and capacity than precision.

#### Suggested costs

- operational missiles
- fuel
- command power
- optional support equipment

#### Mission

About `14` to `30` days.

### Prepare saturation barrage

#### Requirements

- Saturation Arsenals active
- country adopted saturation doctrine
- reserve and capacity above threshold
- at least one high-value target
- readiness above limited band

#### Suggested costs

- large missile payment
- fuel
- command power
- support equipment or a national burden

#### Mission

About `21` to `45` days.

### Prepare counterforce strike

#### Requirements

- selected target has a proven launch state or relevant CBRN facility
- sufficient intelligence
- ordinary war target
- exact target state

#### Result

Uses the same strike pipeline with a launch-site target profile.

### Select special payload

Only operational integrations appear.

The action freezes:

- payload family
- physical stockpile proof
- target compatibility
- extra preparation
- additional command and readiness cost

The payload is reserved when operation preparation begins, not when the player first opens the target category.

## Preparation missions

Preparation missions are goal-style where possible.

The player should not pay a second ceremonial click after completing a requirement that the game can prove automatically.

Useful mission conditions:

- reserve remains available
- participating sites remain controlled
- target remains valid
- readiness remains above minimum
- command control remains above minimum
- payload custody remains valid
- war remains active for ordinary strike routes

Failure results:

- target invalidation
- site capture
- reserve loss
- command collapse
- payload loss
- war end

A mission failure should return or consume resources according to commitment stage and explain the exact reason.

## Launch action

The launch action appears after preparation completes.

The tooltip should show:

- target country
- exact target state
- target profile
- missile count
- payload
- participating sites
- broad guidance grade
- broad collateral risk
- readiness cost
- retaliation risk
- public special-payload consequences

The tooltip should not show the exact hidden random outcome table.

## Post-launch actions

### Inspect the incident

Opens or displays the current result summary.

### Accelerate recovery

Uses a bounded extra cost to improve one-shot readiness recovery.

### Compensate an accidental neutral victim

#### Requirements

- neutral accidental strike occurred
- actor is known or admits responsibility
- compensation not already resolved

#### Suggested costs

- civilian factory burden
- political power or stability
- convoys when overseas aid is required

#### Result

- reduces diplomatic damage
- does not erase deaths, evidence, or confirmed responsibility
- may reduce mistaken-retaliation pressure

### Deny responsibility

Available only when attribution is not confirmed.

Possible consequences:

- temporary diplomatic benefit
- higher cover-up or later evidence penalty
- worse result if exposed

This action should connect to the existing evidence or condemnation system where appropriate.

## Unreliable Guidance actions

### Suspend a damaged site

- removes the site from operation pools
- reduces failure pressure
- lowers total capacity
- can be reversed after repair

### Emergency guidance recalibration

- available after a near miss, wrong-state hit, or breakup
- uses XP, support equipment, and readiness
- reduces the next launch's failure pressure
- does not permanently erase the evolution

### Investigate debris

- available after a failure in controlled or allied territory
- may recover technical data
- may improve attribution
- may expose sabotage

## Rogue Launch Commands crisis actions

### Rotate emergency codes

- invalidates compromised authority
- costs command power and readiness
- can prevent an unauthorized launch
- weaker after the commitment point

### Isolate the site

- cuts one site's communications
- removes its capacity
- can prevent network spread
- increases local mutiny pressure

### Send loyal forces

- requires nearby supplied divisions or a concrete garrison condition
- starts a timed site-recovery mission
- risks site damage and launch

### Negotiate with the command

- uses political or military authority
- buys time
- may preserve the site
- may concede local autonomy or amnesty
- AI chooses based on site payload and assault risk

### Scuttle the site

- destroys local capacity and reserve share
- prevents capture or launch
- creates building and state damage
- may cause casualties
- special payload scuttling must call the owning shared system

### Retake the site

Goal mission requirements can include:

- control the state
- station a required number of supplied divisions
- maintain supply
- keep the site from launching during the mission

## Automatic Retaliation decisions

### Set retaliation posture

The action cycles or selects:

- Off
- Supervised
- Delegated
- Automatic

Each posture has clear public tradeoffs.

Changing posture:

- uses command power
- may use readiness
- has a cooldown
- cannot be changed during a committed response without an emergency action

### Verify warning

Possible requirements:

- radar or intelligence
- functioning command network
- enough time remaining

Possible costs:

- command power
- intelligence exposure
- readiness

Results:

- confidence rises
- confidence falls
- actor changes
- false signal exposed
- conflicting evidence remains

### Delay retaliation

- extends countdown once
- lowers readiness
- may lower AI deterrence evaluation
- cannot be repeated indefinitely

### Sever the network

- stops automatic launch
- disables selected or all sites
- creates a restoration mission
- sharply lowers readiness
- protects against uncertain attribution

### Isolate one site

- targeted state action
- preserves other sites
- useful during local compromise

### Accept response

- confirms current target and payload policy
- commits operation
- hides further stand-down actions after commitment

### Restore retaliation network

Timed mission after severance.

Requirements can include:

- Command Control above threshold
- no active rogue site
- at least one repaired active site
- secure codes
- readiness restored

## Decision cleanup

The decision system must clear:

- selected target when target dies, allies, or war ends
- selected site when control changes
- obsolete captured-site actions after resolution
- launch options during cooldown
- crisis actions after incident closure
- preparation actions during a prepared operation
- retaliation actions after stand-down or launch
- payload actions after stockpile loss
- special evolution actions when the evolution is disabled
- scenario-only actions after setup

## AI decision cadence

Use native decision AI and bounded event triggers.

Do not add a recurring all-country on-action for maintenance.

AI should:

- maintain reserve floor
- restore readiness after launches
- secure low Command Control
- repair active sites
- harden exposed sites
- build a second site only when justified
- select targets through audited scoring
- reserve enough missiles for defense
- respond to incidents within their deadlines
- avoid impossible or obsolete actions

---

# SCN-015: Missile Age

## Identity

- Stable planned ID: `SCN-015`
- Working public name: Missile Age
- Source event: Event 32
- Type control: five profiles
- Intensity control: Low, Medium, High, Maximum
- Launch mode: manual sandbox and challenge setup
- Status target: implemented with Event 32

Implementation must repeat the scenario registry audit. Raw ID 14 is currently reserved by the Fallout manual sandbox.

## Scenario purpose

The scenario creates an immediate missile-strategy campaign without waiting for Event 32 repeat firings or natural evolution MTTH.

It should be useful for:

- sandbox play
- AI stress testing
- evolution testing
- strategic-war challenge starts
- multiplayer setup

The scenario bypasses ordinary Event 32 timing and natural evolution prerequisites. It retains recipient validity, target validity, site validity, program integrity, reserve accounting, incident caps, and active terminal conflict guards.

## Scenario profiles

### Global Proliferation

Creates or advances ordinary missile programs worldwide.

Intensity changes:

- normalized technology steps
- reserve package
- site capacity
- initial readiness
- initial command control

It does not force an evolution unless intensity explicitly maps to one.

### Saturation War

Requires or creates at least one meaningful active war among valid program countries.

Setup:

- unlock Saturation Arsenals
- give belligerent program countries larger reserves
- increase site capacity
- enable saturation AI
- leave neutral countries on ordinary programs

Intensity changes:

- number of advanced belligerents
- reserve size
- site count
- readiness
- AI aggression

The scenario must not declare a random war when no safe conflict can be built. It should fail with a clear reason or use an existing war.

### Command Breakdown

Unlocks Rogue Launch Commands and Unreliable Guidance.

Setup:

- select valid vulnerable countries
- lower Command Control or readiness within bounded ranges
- seed damaged, compromised, or isolated sites
- create no immediate launch by default

Intensity changes:

- affected-country share
- severity
- active incident count
- chance that a crisis begins soon after launch

### Special Payload Crisis

Unlocks Special Warheads.

Setup:

- initialize delivery integration only for countries that already own supported payload technology and stockpile
- give ordinary missiles to other valid countries
- create at least one hostile relationship among payload-capable countries when the world state already supports it
- do not grant chemical, biological, nuclear, or thermonuclear payloads

Intensity changes:

- number of integrations
- readiness
- reserve
- AI policy severity
- warning pressure

If no country owns a supported payload, the scenario is unavailable.

### Retaliation Network

Unlocks Automatic Retaliation and required supporting tracks.

Setup:

- initialize supervised, delegated, or automatic postures according to country profiles
- create warning readiness
- preserve chain caps
- avoid an immediate launch at Low and Medium
- allow one bounded uncertain or false warning at High
- allow one bounded linked warning crisis at Maximum

Intensity changes:

- posture severity
- number of participating countries
- reserve
- readiness
- attribution uncertainty
- initial warning profile

The scenario does not set a terminal flag.

## Intensity model

### Low

- limited set of advanced countries
- one technology step
- modest reserve
- one site each
- high command control
- no immediate destructive incident

### Medium

- broader country coverage
- two technology steps where supported
- stronger reserve
- some secondary sites
- ordinary evolution pressure

### High

- most valid countries
- mature regional programs
- larger reserves
- several advanced sites
- active crisis candidates
- stronger AI willingness

### Maximum

- every valid recipient
- highest supported normalized stage without incompatible grants
- large but bounded reserves
- saturation-capable networks
- selected active incidents
- all profile-specific risks
- no automatic campaign-ending flag

## Scenario setup transaction

The scenario must:

1. freeze profile and intensity
2. freeze valid recipient pool
3. preflight all required profile conditions
4. allocate scenario ID and setup receipt
5. initialize Event 32 runtime if absent
6. apply country packages
7. unlock only selected evolutions
8. set scenario-specific bypass flags
9. clear bypass flags after setup
10. record one scenario launch
11. avoid an ordinary Event 32 random-event history row unless the scenario contract deliberately records one compatible row
12. prevent duplicate launch through an idempotent scenario flag

## Scenario failure

A failed preflight should not partially mutate:

- programs
- technology
- sites
- reserves
- evolutions
- incidents
- scenario history
- AI posture

The player receives one setup-failure report with a stable reason.

## Scenario catalog fields

The final workbook row should include:

- ID
- final public name
- source event
- five profile names
- profile descriptions
- four intensity descriptions
- implementation status
- player-facing detail text

The wording must mirror the final in-game scenario localisation.

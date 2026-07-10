# Air Winter Architecture

## Implementation objective

Replace the current random-state winter pulse with a persistent state system that the player can read, anticipate, mitigate, and fail. The system must remain compatible with the existing global Air Contamination value, nuclear fallout intensity, chemical contamination, Deaths tracking, Chaos synchronization, mapmodes, treaty content, and later Fallout world rewrite.

## Runtime ownership

The host-owned `air_contamination_monthly_update` remains the only global monthly entry point for Air Cleanliness.

The monthly call should be divided into ordered helpers:

1. initialize missing global and state values
2. count live contamination sources
3. calculate the global contamination delta
4. apply global contamination and Chaos synchronization
5. calculate global winter forcing and recovery force
6. update every valid state once
7. aggregate phase counts and exposed population
8. apply global status flags and threshold transitions
9. select a bounded set of flavour incidents
10. update treaty and relief systems
11. evaluate gradual Fallout eligibility and request pressure
12. refresh cached UI values

No second full-state monthly loop should be introduced for winter. Building damage, deaths, phase changes, category damage, and flavour candidate scoring must occur inside the single state pass or through arrays built during that pass.

## Valid state set

A state is valid for Air Winter processing when:

- it exists in the playable map
- it is not a special non-land or engine-only state
- it has an owner or controller that can receive normal state effects, unless the Fallout transition explicitly processes unowned wasteland
- it is not already terminally excluded by a completed Fallout rewrite

Small islands and enclaves remain valid. Their phase and recovery factors differ, but they are not skipped.

## Global forcing model

The global forcing value should combine:

- global Air Contamination percentage above the winter onset band
- number and intensity of nuclear fallout states
- number of chemical contamination states
- active nuclear winter memory
- recent thermonuclear use
- terminal scripted-event forcing
- existing atmospheric cleanup projects
- season and latitude only where the engine data can support it reliably

A stable conceptual form:

`global forcing = contamination forcing + soot forcing + chemical forcing + terminal event forcing - global mitigation`

The implementation uses script constants for coefficients and caps.

The forcing model must have hysteresis:

- entering a winter phase requires a higher threshold than remaining in it
- recovery requires several consecutive favorable months
- severe phases cannot disappear from a single temporary cleanup effect

## State pressure model

Each state receives a pressure score from global forcing and local multipliers.

Local escalation factors:

- current nuclear fallout intensity
- chemical contamination
- existing winter exposure
- urban density and industrial concentration
- damaged infrastructure and supply isolation
- low shelter capacity
- low food reserve
- low adaptation
- active combat and strategic bombing
- adjacency to severe winter states
- scripted terminal-cause markers

Local resistance factors:

- shelter capacity
- food reserve
- adaptation
- active relief route
- functioning infrastructure and supply access
- rural food production where the phase is still survivable
- treaty-backed cleanup
- suitable climate and geography where supported
- route-specific country mechanics

The state pressure score determines the target phase. The current phase moves by at most one step per monthly update unless a direct terminal caller sets an emergency jump.

## Phase transition rules

### Escalation

A state escalates when:

- target phase is above current phase
- escalation pressure exceeds the entry threshold
- minimum phase duration is satisfied, unless an emergency override applies

A direct thermonuclear or scripted terminal event may add exposure and set a minimum target phase. It should not blindly set every state to the same phase.

### Recovery

A state recovers when:

- target phase is below current phase
- recovery force exceeds escalation force by the configured margin
- the state has accumulated enough consecutive recovery months
- no active direct-strike floor blocks the reduction

Recovery lowers the phase by one step at a time. Exposure and category damage decline more slowly.

### Persistence

When target phase equals current phase:

- `air_winter_phase_months` increases
- exposure changes from net pressure
- damage thresholds may trigger
- flavour and mitigation opportunities can appear

## Phase effects

Effects should be implemented through one dynamic modifier per phase or a verified equivalent. The modifiers use strong, readable consequences and avoid stacking every previous phase modifier at once.

### Phase 1

Primary effects:

- reduced air mission efficiency and detection
- mild supply and construction friction
- small stability or local confidence pressure through country aggregation
- forecast uncertainty at low monitoring levels

Map behavior:

- light desaturated fill
- phase-change outline for a short period

Flavour families:

- first persistent haze
- aviation and navigation disruption
- local fuel and heating demand

### Phase 2

Primary effects:

- agricultural and food-reserve loss
- rural population health pressure
- reduced local resources or food abstractions where supported
- increased relief demand

Flavour families:

- crop failure reports
- livestock and seed reserve losses
- rural migration
- rationing disputes

### Phase 3

Primary effects:

- meaningful supply throughput and infrastructure repair penalties
- construction and factory repair slowdown
- monthly civilian death risk through the shared Deaths system
- first bounded building-damage pressure

Flavour families:

- frozen rail and road corridors
- heating-system collapse
- hospital overload
- failed maintenance shifts

### Phase 4

Primary effects:

- severe population loss
- stronger building damage
- local factory and infrastructure shutdowns
- resistance, migration, or authority pressure
- initial state-category damage progress

Flavour families:

- black harvest and food riots
- abandoned districts
- emergency evacuation
- local military seizure of stores

### Phase 5

Primary effects:

- extreme supply and construction collapse
- sustained category degradation
- industrial and resource failure
- increased successor and warlord pressure
- possible local government breakdown events

Flavour families:

- city systems failing together
- depots turning into political centers
- armed food corridors
- isolated technical enclaves

### Phase 6

Primary effects:

- terminal population loss pressure
- wasteland conversion eligibility
- survivor-value collapse unless exceptional shelter or adaptation exists
- direct contribution to gradual Fallout request pressure
- special terminal incidents

Flavour families:

- sealed zones
- failed evacuation corridors
- underground survivor administrations
- fictional high-chaos mutation incidents where allowed

## Population effects

Population loss must use the shared Deaths registration path.

Each monthly state tick sets:

- a phase-based base death percentage
- exposure multiplier
- food reserve multiplier
- shelter and adaptation reductions
- war and supply multipliers
- random band within documented limits
- a winter-specific death reason

The helper must update:

- real state population
- global and state death totals
- death mapmode data
- Chaos synchronization
- any Fallout survival-value memory

Do not also apply a second direct population reduction from the phase modifier.

## Building effects

Building damage begins at Phase 3 and becomes severe at Phases 4 through 6.

Monthly logic:

1. Add phase-weighted pressure to `air_winter_building_damage_pressure`.
2. Subtract active repair, adaptation, and relief reductions.
3. When the threshold is reached, select at most one eligible building family for damage.
4. Reduce pressure by the threshold amount.
5. Set a recent-damage flag for flavour cooldown and UI explanation.

Eligible families depend on the state:

- infrastructure
- railways where a verified effect is available
- supply hubs only under severe and sustained conditions
- civilian factories
- military factories
- dockyards in coastal states
- air bases
- anti-air
- radar
- fuel silos
- synthetic refineries
- ports under extreme coastal failure

Protected rules:

- never reduce below zero
- do not delete a unique facility without a dedicated rule
- do not damage several building families in one state during one monthly pass
- do not damage the same building family repeatedly without a cooldown or rising threshold
- record the selected family for the event and tooltip

## State-category degradation

The existing category ladder is reusable, but the trigger must become sustained and auditable.

Required gates:

- Phase 4 or above
- minimum consecutive phase months
- category damage progress above threshold
- no recent category downgrade cooldown
- current category is not already wasteland

Before the first downgrade, set an original-category flag or stable original-category enum.

Normal degradation:

- one category step per eligible interval
- damage progress partly resets after each downgrade
- adaptation and recovery can stop future damage
- ordinary recovery does not automatically restore categories

Restoration is a late-game decision and focus system. It requires population, supply, construction capacity, and long-term stability. Wasteland restoration is rare and route-specific.

## Mapmode design

### Required initial mapmode

Add one dedicated scripted state mapmode:

`air_winter_state_map_mode`

It displays current phase as the primary fill.

Phase color design:

- Phase 0 remains transparent or uses the country background
- early phases use cold grey and pale blue
- middle phases use darker blue-grey and ash tones
- severe phases use near-black, bruised violet, and cold white contrast
- terminal states use an unmistakable dark fill and strong border

The exact palette belongs in script constants.

### Mapmode layers

The accepted design discusses phase, exposure, and survival information. Engine support for cycling several data layers through one mapmode button must be verified before implementation.

Required delivery:

- phase mapmode
- phase tooltip that includes exposure and forecast

Optional after proof:

- separate exposure mapmode
- separate Fallout survival-value mapmode after the world rewrite
- a scripted GUI selector tied to mapmode state if a stable precedent exists

Do not promise an unsupported sublayer switch.

### Tooltip order

The tooltip should show:

1. current phase
2. direction of travel
3. months in phase
4. exposure
5. next-month forecast range based on monitoring level
6. population effect summary
7. building and supply effect summary
8. category damage state
9. active relief or mitigation
10. available response category direction

At low monitoring, the forecast is a broad band. At high monitoring, it shows the calculated target phase and main factors.

### Frame registration gate

Before adding a winter icon:

1. inspect both mapmode DDS strips
2. divide texture width by frame width
3. confirm actual current frame count
4. compare the selected and deselected strips
5. correct `noOfFrames`
6. record exact existing slot ownership
7. append the winter frame at the next verified slot
8. update the documentation with the verified slot number

## Flavour incident system

Flavour incidents must have real effects and controlled cadence.

During the monthly state pass, build candidate arrays for:

- phase change
- population crisis
- building failure
- food collapse
- supply isolation
- evacuation
- relief success
- recovery milestone
- treaty intervention
- local government breakdown
- fictional mutant emergence

After the pass, select a small global number based on severity and player relevance. Do not fire one event per affected state.

Player priority:

- player-owned state
- player-controlled state
- capital or high-population state
- state with a new phase record
- state with a meaningful choice

AI countries receive hidden or lightweight effects when a popup is not needed.

Every incident family defines:

- eligibility
- cooldown
- visible information
- player choice direction
- direct mechanical effects
- AI choice weights
- follow-up state
- event log or death log integration where relevant

## Mitigation and response

The response system should be a staged decision category, not a permanent store.

Early actions:

- establish monitoring stations
- ration fuel and food
- open emergency shelters
- protect rail and supply corridors

Middle actions:

- relocate vulnerable population
- harden hospitals and utilities
- build regional food reserves
- assign repair brigades
- request treaty relief

Severe actions:

- abandon selected districts
- consolidate industry
- establish guarded food corridors
- evacuate government functions
- seal a terminal zone

Costs should use equipment, trains, convoys, fuel, manpower, civilian factory burden, stability, war support, and local control where relevant. Political power may support administrative actions but cannot be the only cost palette.

## AI behavior

AI state response score should consider:

- phase
- exposure
- state population
- capital or core status
- industry and supply value
- current war fronts
- available trains, convoys, fuel, and equipment
- national food and shelter strategy
- treaty membership
- expected survival value
- whether the country is likely to fragment during Fallout

AI priorities:

1. protect the capital and major supply centers
2. prevent Phase 4 in high-population states
3. preserve food-producing regions
4. keep a continuous supply corridor
5. accept foreign relief when dependency risk is tolerable
6. abandon states only under severe terminal pressure

High-chaos AI may choose extreme or fictional responses only when its route permits them.

## Treaty integration

The treaty should become a practical mitigation framework.

Member benefits:

- shared monitoring
- treaty relief missions
- pooled decontamination projects
- evacuation corridors
- reduced relief decision cost
- better forecast precision

Member obligations:

- ban specified unconventional use
- contribute equipment, trains, convoys, or factories
- accept inspection or verification events
- support member relief votes

Violation consequences:

- expulsion
- embargo and opinion penalties
- loss of relief access
- Fallout memory that shapes successor legitimacy

Performance rule:

- cache members in an array or stable flag set
- refresh relations only on membership change, violation, or a low-frequency treaty pulse
- do not apply every member-to-member opinion modifier every month

## Gradual Fallout evaluation

After state aggregation, evaluate Fallout eligibility.

Inputs:

- contamination at or above 100 percent
- share of states at Phases 5 and 6
- exposed population
- direct-strike memory
- number of wasteland states
- irreversibility
- active terminal scripted-event pressure
- mitigation and surviving global institutions

Behavior:

- at 100 percent, set eligibility and begin pressure growth
- pressure rises from severe state conditions
- pressure can stabilize or fall only if the accepted irreversibility rules permit it
- a guaranteed high threshold may force the request
- direct scripted callers bypass the roll

The monthly evaluator calls `fallout_request_aftermath` with source and intensity. It never starts the world rewrite inside the state loop.

## Acceptance checks for Tranches 1 and 2

- winter phase persists per state across monthly ticks
- mapmode displays every phase correctly
- tooltip explains direction and main causes
- early and severe phases have distinct gameplay effects
- population losses appear in the shared Deaths totals
- building damage is bounded and visible
- categories only degrade after sustained severe exposure
- recovery uses hysteresis
- flavour events change state or country values
- AI uses response decisions
- treaty members gain practical mitigation and violations matter
- no additional world-wide periodic loop was added
- save-load preserves phase, exposure, recovery, and damage progress

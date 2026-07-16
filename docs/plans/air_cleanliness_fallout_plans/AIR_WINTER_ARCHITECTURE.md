# Air Winter Architecture

## Implementation objective

Replace the current random-state winter pulse with a persistent state system that the player can read, anticipate, mitigate, and fail. The system must remain compatible with the existing global Air Contamination value, nuclear fallout intensity, chemical contamination, Deaths tracking, Chaos synchronization, mapmodes, treaty content, and later Fallout world rewrite.

## Runtime ownership

The host-owned `air_contamination_monthly_update` remains the only global monthly entry point for Air Cleanliness.

The implemented monthly order is:

1. prepare capped natural contamination sources
2. open one monotonic Air Winter cycle and snapshot completed contamination inputs
3. update every state once inside the existing world pass, ending each state update with its bounded ordinary-map visual refresh
4. aggregate phase counts and exposed population during that pass
5. register event and evacuation owners during that pass
6. rebuild evacuation quotes from the bounded priority-owner array
7. dispatch one deterministic event candidate per eligible owner from the bounded event-owner array
8. finalize global Air Winter flags and aggregates once

No second full-state monthly loop should be introduced for winter. Building damage, deaths, phase changes, category damage, and flavour candidate scoring must occur inside the single state pass or through arrays built during that pass.

The cycle snapshots, one-update guards, neighbor opening-state reads, score and state-id tie rules, and finalization guard are recorded in `AIR_WINTER_MONTHLY_DETERMINISM_PROOF.md`.

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

The installed engine exposes recent strategic bombing as a state fact, but it does not expose the state of an active ordinary land battle through a documented state predicate or callback. Direct active-combat pressure has no exact state input. A strategic-bombing winter multiplier requires a balance decision that accounts for the existing strategic-bombing Deaths tick.

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

General air fields have documented country scope and no supported runtime state or strategic-region dynamic scope. The country modifier uses the equal-state mean Air Winter phase across controlled states with a working airbase. It also changes the accident rate and weather penalty. A cycle receipt, controller registry, and no-contribution cleanup keep the result deterministic without a new world pass. This is a national operational burden and does not claim local strategic-region confinement.

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
- protected civic shelter with temporary factory diversion in mountain capitals

Flavour families:

- crop failure reports
- livestock and seed reserve losses
- rural migration
- rationing disputes
- tunnel classrooms and shared workshop schedules

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
- dam gates and frozen hydroelectric intakes
- refinery shutdown, guarded output, and district heat
- reactor cooling, emergency power, and plant authority

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

The live tooltip contract derives access for the viewing country instead of storing one universal monitoring value on the state.

| Monitoring level | Live access rule | Live report |
| --- | --- | --- |
| None | Foreign state without shared reports | Current phase only |
| Basic sampling | Owned or controlled state, or treaty membership | Current phase and one-month trend |
| Atmospheric office | Country completed one roof-sampler project | Exact cause readings and likely phase next season |
| Terminal modelling | World at 90 percent contamination, or monitored major power | Possible Fallout classification from atmospheric evidence |

Every winter mapmode layer uses the same gate. The terminal range is not a committed Fallout grade. Direct-strike and blast evidence remain owned by the later grading transaction. Static scope and cleanup proof is recorded in `AIR_WINTER_MAPMODE_MONITORING_PROOF.md`.

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

After the pass, dispatch at most one candidate per eligible owner. Each owner has a 46-day cooldown. Ordinary phase candidates use severity score with the lowest state id resolving equal scores. Seasonal candidates add typed family priority and earliest origin cycle before frozen severity score and state id. This prevents one event per affected state while preserving independent human and AI country pacing. The human campaign target remains 90 to 180 meaningful events across the full Fallout scheduler over ten years, not 90 to 180 Air Winter phase popups alone.

The live recurring seasonal layer uses the same monthly state pass and bounded owner array. The cycle opener snapshots the documented current engine year once. State processing captures complete durable marker rows before the cooldown gate, so an observed condition does not disappear while its country is cooling down. A marker retains its origin year, origin cycle, origin owner, presentation class, score, and typed event id until a validated dispatch consumes it.

The implemented seasonal families are:

- first frost when a state enters Phase 2
- dark harvest when a Phase 4 or worse state matches the food-state classifier
- ash thaw when a state falls from Phase 3 or 4 to a lower phase
- second winter when the same presentation class reaches a severe winter in a later engine year
- terminal season when a Phase 6 state is observed above the terminal contamination threshold

Country receipts make each family at most once for its recorded year. Nine regional severe-year memories seed the first severe year and advance only after a validated later-year second-winter dispatch. Prior-year markers remain valid when their receipt is still earlier than the marker year. No seasonal family adds a world iterator. Full ordering, cleanup, and engine-boundary proof is recorded in `AIR_WINTER_SEASONAL_RECURRENCE_PROOF.md`.

The implemented Phase 3 infrastructure layer adds dam, oil or refinery, and reactor routes inside the ordinary family. Route precedence applies within the selected state. The country still chooses one candidate by family priority, origin cycle, phase and pressure score, then state id, and the Phase 3 seen flag permits one ordinary Phase 3 route per country. Full engine-sensitive proof is recorded in `AIR_WINTER_PHASE_3_INFRASTRUCTURE_EVENT_PROOF.md`.

The implemented Phase 2 mountain-capital route checks the selected state for highland presentation and current capital identity before the generic city route. The typed event id preserves that selection if a first-frost marker dispatches after the capital moves. Its delayed result trades temporary local factory availability for shelter, adaptation, and a durable 10 percent reduction in the established monthly Air Winter civilian death percentage. Full engine-sensitive proof is recorded in `AIR_WINTER_PHASE_2_TUNNEL_SCHOOL_EVENT_PROOF.md`.

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

The response system is a staged decision category, not a permanent store. It has one priority selector, one reception selector, two read-only summaries, and sixteen timed projects. One state project can be active per country.

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

Costs use equipment, trains, convoys, fuel, manpower, civilian factory burden, stability, war support, and local control where relevant. Political power is not used as the response store.

Controlled and final evacuation quotes derive from the selected source population and the lowest-id valid reception state. Population formula work stays in `state_population_k`. A single conversion creates the exact people count used by the delayed state-population transaction. The quote locks transport, support, staff, stability, receiver pressure, and source pressure values when the project begins. The detailed scope and engine proof is in `AIR_WINTER_RESPONSE_DECISION_PROOF.md`.

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

Implemented lifecycle:

- the monthly Air host calls one idempotent treaty coordinator
- bounded arrays own members, violators, active convoy donors, active inspectors, pending removals, pending violation changes, and active relief states
- the lowest eligible country id founds the treaty when severe contamination begins
- invitations carry a generation receipt and expire without leaving stale eligibility
- entry, exit, violation, annexation, founder succession, and dissolution own explicit cleanup paths
- Global Cleaning Day consumes equipment and convoys from its sponsor and reserves that sponsor's civilian factories before cleanup begins
- Joint Filter Convoy targets a treaty member, reserves one eligible controlled state, consumes real equipment and convoys, and writes one temporary relief-route ledger
- Verification Mission lets the current secretariat inspect one member at a time through a fourteen-day targeted project, three paid or disputed responses, and an exact seven-day result
- paired inspection receipts write government-aware cooperation or dispute memory without changing Winter or Fallout tuning formulas
- inspection refusal enforces the accepted expulsion, embargo, opinion, and relief-loss consequences through the existing treaty violation path
- route completion, cancellation, ownership drift, annexation, expiry, and treaty dissolution reconcile through idempotent receipts
- invalid routes reconcile before monthly state pressure
- Fallout silently clears active projects, invitations, and routes while preserving membership and betrayal memory
- Fallout also clears active inspection receipts while preserving completed inspection memory

Remaining treaty work:

- evacuation corridors and refugee allocation
- treaty-owned Fallout memory and successor legitimacy
- broader regional and government-aware treaty event families
- relief vote transactions and major-burner policy
- runtime observation of decision target scope, delayed completion, delayed inspection results, route pressure, and sanctions

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

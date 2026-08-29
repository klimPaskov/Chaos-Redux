# Baseline phase map

## Phase 0: Detection and entry

### Purpose

The opening phase establishes uncertainty, invites human participation, selects AI rivals, and creates the shared event state.

### Duration

The entry window should last about 30 days. It is an event response window, not a normal timed mission.

### Human choices

A human country can:

- authorize an expedition
- decline and observe
- request a route estimate before committing

The route estimate shows the likely route band, broad entry burden, and the main material types required. It does not reveal exact hidden rival scores.

### Entry requirements

Entry should require:

- a valid government, command structure, or institutional controller capable of sponsoring an expedition
- enough available convoys for the route band or a charter route
- a minimum fuel reserve or access to a fuel commitment
- support equipment for the first camp
- enough civilian industrial capacity to sustain the expedition office
- enough available workforce, operators, or manpower to staff the expedition, recorded as a staff requirement outside displayed spendable costs
- at least one research slot or an event-recognized scientific, technical, or analytical capability

The player may enter while below an ideal threshold, but the tooltip must explain the resulting weak readiness.

### Entry commitment

The entry action may use up to four spendable cost types:

- convoys
- fuel
- support equipment
- civilian industrial commitment

Personnel, operators, and scientific staff are represented by actor-appropriate eligibility, roster state, and later casualty risk.

### AI initialization

AI major candidates are scored and selected. The selection is frozen after the entry window except for a bounded early replacement route.

### Visible output

The participant receives the Expedition Board with:

- route estimate
- current progress at setup level
- starting readiness
- starting exposure
- known rivals
- first mobilization actions

## Phase 1: Mobilization and staging

### Purpose

The participant turns an authorization into an actual southbound expedition.

### Core objective

Complete the Organize the Southern Expedition mission.

### Expected duration

90 to 150 days depending on route band and investment.

### Primary actions

1. Charter or assign transport
2. Stock the expedition depots
3. Secure a gateway agreement
4. Prepare aerial survey support
5. Establish a meteorological and radio office

Only actions valid for the country and route appear.

### Main tradeoff

The player chooses between a quick, expensive departure and a slower, resilient buildup.

A rush can reduce travel delay but starts Phase 2 with lower readiness and higher exposure. A careful buildup consumes more civilian capacity and gives rivals time to move.

### Failure states

The mission may be delayed by:

- convoy shortage
- loss of gateway access
- active naval blockade
- severe home-front war pressure
- failure to meet the minimum supply commitment

Failure does not remove the participant immediately. It opens one emergency recovery action and a withdrawal choice.

### Reports

Possible reports include:

- rival ships leaving port
- a gateway government demanding terms
- missing cargo
- weather observations changing the likely route
- a survey aircraft or ship reporting the first fragment

## Phase 2: Crossing and outpost establishment

### Purpose

The expedition reaches Antarctica and creates a base capable of supporting the search.

### Core objective

Complete Establish the Antarctic Outpost.

### Expected duration

90 to 180 days.

### Outpost roles

The player selects one public outpost emphasis:

| Emphasis | Benefit | Cost or risk |
| --- | --- | --- |
| Logistics depot | Higher readiness and safer resupply | Slower survey start |
| Survey station | Faster certainty and progress | Weaker defense and stores |
| Signals station | Better radio and signal tracking | Higher exposure under Evolution I |
| Fortified camp | Better protection from rivals and survivor incidents | Higher fuel and equipment burden |
| Mobile traverse camp | Faster movement between candidate sites | Lower integrity and weather resilience |

The emphasis can be changed later at a meaningful cost. It is not a permanent route lock.

### Outpost state

The outpost has an integrity state shown through a visual frame and status label.

- secure
- strained
- damaged
- compromised
- abandoned

Integrity affects readiness, survey work, and resistance to hostile actions.

### Primary actions

1. Land the construction party
2. Reinforce shelters and stores
3. Expand the radio mast
4. Survey an alternate landing zone
5. Deploy an escort detachment when available

### Hazards

Baseline hazards are severe but ordinary:

- pack ice
- whiteout
- crevasse field
- radio loss
- damaged engines
- missing sledges or vehicles
- medical emergency

A prepared expedition can mitigate each one.

### Completion

The phase completes when the outpost exists, has minimum integrity, and can sustain a search team.

## Phase 3: Search grid and triangulation

### Purpose

Participants narrow several possible crash sectors into one primary recovery route.

### Candidate sites

The board shows six working site roles, not exact map provinces:

1. ice shelf debris field
2. mountain shadow
3. buried signal basin
4. coastal fracture zone
5. magnetic silence area
6. false or unresolved sector

The final asset names and final localisation should avoid implying that the working labels are confirmed facts.

### Core objective

Reach the required Survey Certainty and Expedition Progress for final recovery.

### Expected duration

120 to 240 days.

### Search actions

1. Run aerial reconnaissance
2. Conduct a ground traverse
3. Rebuild the signal model
4. Compare rival movement
5. Recover a verified fragment

The phase shows no more than five primary actions at one time.

### Site model

Each action changes the probability that a candidate site contains the recovery core.

The player should see confidence states:

- unlikely
- possible
- probable
- primary
- ruled out

The actual core location is determined at event initialization or through a stable seeded selection. It must not change because the player clicked the wrong site.

### False information

Rival sabotage may create a false confidence state. Counterintelligence, independent confirmation, and fragment analysis can expose it.

The player must never lose all progress from one false-coordinate incident. A successful deception creates a setback and a temporary wrong-site mission.

### Baseline rivalry

Before militarisation, rivalry remains covert or deniable.

- steal survey notes
- bribe a gateway contractor
- copy radio bearings
- tamper with stores
- spread false coordinates
- expose a rival operation

Every hostile action has a target, cooldown, cost, success state, attribution state, and countermeasure.

### Fragment recovery

Baseline fragments provide:

- small progress
- site certainty
- exposure risk
- a fragment score for losing rewards

Fragments do not grant the full Event 016 technology before the winner is determined.

## Phase 4: Final recovery operation

### Purpose

A qualified participant commits to the primary recovery route and attempts to secure the recovery core.

### Unlock conditions

The final operation requires:

- required Expedition Progress
- required Survey Certainty
- minimum Logistics Readiness
- functioning outpost
- no active emergency retreat
- available transport and recovery equipment
- no current final-operation cooldown

The thresholds must be centralized and visible in a concise tooltip.

### Final mission

The mission should last about 90 to 150 days.

Starting the mission commits material and makes the participant a visible leader. Rivals may counter it through legal baseline actions such as data theft or route interference. Evolution III unlocks stronger direct counterplay.

### Final approaches

The player selects one approach:

| Approach | Strength | Risk |
| --- | --- | --- |
| Controlled recovery | Best protection and wreck integrity | Slowest |
| Rapid extraction | Faster completion | Higher exposure and equipment loss |
| Remote disassembly | Lower personnel risk | Lower fragment yield and slower analysis |
| Armed seizure | Strong against rivals | Diplomatic cost and exposure, mainly relevant under Evolution III |
| Distributed recovery | Safer under Evolution IV | Gives rivals more fragment opportunities |

### Success calculation

The final operation should mostly resolve from visible preparation.

Strong readiness, survey certainty, outpost integrity, route security, and appropriate preparation should make success likely. Random failure should never erase a fully prepared expedition without a visible severe incident.

### Winner

The first participant to complete a valid final recovery secures the primary recovery core.

The winner is stored globally and receives the winner report, technology grant, and post-recovery state.

### Non-winner conversion

Other active final missions convert into:

- high fragment recovery when close to completion
- medium fragment recovery when the team reached the site
- emergency evacuation when readiness collapsed
- a hostile seizure incident when Evolution III conditions apply

The event does not delete their investment without an outcome.

## Phase 5: Recovery analysis and settlement

### Purpose

The race ends, rewards are issued, expeditions return or remain, and persistent alien-material choices begin.

### Immediate winner effects

The winner receives:

- one random valid Event 016 custom operational technology through the neutral external-grant path
- a winner report and global news event
- a temporary Alien Recovery Office idea or event-owned integration state
- the highest fragment tier
- a recorded shared alien-recovery source for Event 036 arbitration

### Losing participant effects

Each losing participant receives a reward based on verified progress, fragment score, and final mission state.

### Withdrawal and repatriation

Participants choose or automatically resolve:

- orderly return
- leave a small scientific station
- transfer records to an ally
- conceal recovered fragments
- destroy dangerous debris

Leaving a scientific station is an abstract persistent expedition record, not state ownership or a new building model.

### Event closure

Without Evolution V, the active race system closes after reward and repatriation events. Temporary industrial commitments and mission state are removed.

With Evolution V, countries retaining material enter the post-recovery technology-use track. The race itself is still closed.

## Baseline rare incidents

The baseline may include rare incidents that do not require an evolution:

- an abandoned camp from an earlier expedition
- a rival rescue request
- a misidentified meteorite
- a clear weather corridor
- a neutral ship offering transport
- a damaged aircraft carrying useful photographs
- a scientist dispute over the search model
- a fragment that reacts to ordinary current

These incidents should create choices and consequences. They should not reveal the later survivor or user-change evolutions early.

## One-participant behavior

When only one participant enters, the event remains a race against weather, route decay, and the closing recovery window.

Rival actions are hidden. Progress and exposure tuning become slightly stricter so the event does not become a free technology purchase. The participant can still lose fragments through poor preparation, but a competent expedition should complete the baseline.

## No-participant behavior

When no human enters and no valid AI major can participate, the opening event records no viable expedition and closes through an observer report.

The major event still counts as fired. It must not remain permanently active with an empty roster.

# Decisions, missions, and costs

## Presentation ownership

The event uses one event-owned scripted GUI called the Expedition Board.

Gameplay actions may be implemented as event-owned decisions, scripted-GUI buttons backed by the same helpers, or a hybrid where missions remain in a compact decision category and the board handles targeting and state presentation.

The same helper must control player and AI effects. The GUI must never become a separate human-only ruleset.

## Action budget

Each phase normally exposes three to five primary actions.

Six visible primary actions is the hard maximum. Additional actions must be hidden by phase, route, current emergency, selected rival, evolution state, or completion state.

The event should not create a long permanent list of every possible expedition action.

## Cost budget

One action may use no more than four spendable cost types.

Requirements such as owning a port, fielding aircraft, having a research slot, or maintaining a minimum readiness do not count as spendable costs.

Every displayed cost needs the correct text icon. A custom cost without a valid text icon is not allowed.

## Main cost families

| Cost or commitment | Appropriate uses |
| --- | --- |
| Convoys | Entry, resupply, evacuation, heavy recovery, alternate route |
| Fuel | Crossing, aviation, escort, rapid extraction, blockade |
| Support equipment | Camp, shielding, repairs, medical protection, recovery rig |
| Civilian industrial commitment | Expedition office, outpost, shielded analysis, long project |
| Manpower loss | Incident consequence only, not the normal displayed entry payment |
| Navy XP | Complex escort or blockade planning where justified |
| Air XP | Specialized aerial survey or interception where justified |
| Command power | Limited expedition escort or emergency command, capped conservatively |
| Stability | Public scandal, concealed casualties, severe diplomatic response |
| War support | Escalation or retreat consequence |
| Intelligence exposure | Covert action consequence, shown through tooltip or event state |
| Equipment loss | Failed or hostile incident outcome |

Political power should be limited to diplomacy, access negotiations, public inquiries, or administrative settlements. It should not be the default expedition currency.

## Entry action

### Authorize the expedition

Spendable cost types:

- convoys
- fuel
- support equipment
- civilian industrial commitment

Requirements:

- valid sponsoring government, command structure, or institutional controller
- minimum expedition workforce, operators, or free manpower
- scientific, technical, or analytical capacity
- route estimate

Consequences:

- joins the participant roster
- creates the expedition office state
- opens Phase 1 actions
- starts readiness and exposure values

The entry cost scales by route band, economy, and current war burden.

## Phase 1 actions

### Assign transport

Purpose: move the team and first stores to the gateway.

Possible costs:

- convoys
- fuel
- civilian commitment

Effects:

- advances mobilization mission
- raises readiness
- locks the selected route for the next phase

### Stock the depots

Possible costs:

- support equipment
- convoys
- civilian commitment

Effects:

- raises readiness
- creates a reserve against one supply setback

### Secure gateway access

Possible costs:

- political power
- convoys or equipment transfer
- civilian commitment

Requirements:

- valid foreign gateway owner
- diplomatic route

Effects:

- improves route band
- creates a time-limited access record
- may create dependence or opinion effects

### Prepare aerial survey support

Possible costs:

- fuel
- air XP
- civilian commitment

Requirements:

- suitable aircraft presence or technology

Effects:

- improves Phase 3 survey gain
- raises vulnerability to weather and interception

### Build the radio and weather office

Possible costs:

- support equipment
- civilian commitment

Effects:

- reduces weather uncertainty
- improves signal and survey actions

## Phase 2 actions

### Land the construction party

Possible costs:

- convoys
- fuel
- support equipment

Effects:

- starts the outpost mission
- converts route readiness into outpost progress

### Reinforce shelters and stores

Possible costs:

- support equipment
- civilian commitment

Effects:

- raises outpost integrity
- lowers weather loss

### Expand the radio mast

Possible costs:

- support equipment
- fuel

Effects:

- raises survey certainty
- interacts with Evolution I

### Survey an alternate landing zone

Possible costs:

- fuel
- convoys

Effects:

- creates a backup route
- lowers outpost-loss risk

### Deploy an escort detachment

Possible costs:

- command power
- support equipment
- fuel

Requirements:

- suitable military assets

Effects:

- improves survivor and rival defense
- raises militarisation pressure when Evolution III is active

## Phase 3 actions

### Run aerial reconnaissance

Possible costs:

- fuel
- air XP

Effects:

- high survey gain
- weather and interception risk

### Conduct a ground traverse

Possible costs:

- fuel
- support equipment

Effects:

- progress and fragment chance
- exposure and personnel risk

### Rebuild the signal model

Possible costs:

- civilian commitment
- support equipment

Effects:

- removes false-coordinate pressure
- raises certainty
- interacts with Evolution I

### Study rival movement

Possible costs:

- intelligence exposure
- political power or civilian commitment, depending on route

Effects:

- reveals rival progress band or target site
- may expose the investigator

### Recover a verified fragment

Possible costs:

- support equipment
- fuel
- civilian commitment

Effects:

- fragment score
- progress
- exposure

## Covert rival actions

Every covert action requires a selected valid rival.

### Steal survey data

Possible costs:

- intelligence exposure
- civilian commitment

Effects on success:

- attacker gains certainty or progress
- target loses no more than a bounded amount
- attribution may remain hidden

Counterplay:

- counterintelligence action
- redundant survey records
- public exposure of the theft

### Feed false coordinates

Possible costs:

- intelligence exposure
- support equipment

Effects on success:

- target receives a temporary false-site state
- attacker gains no direct progress

Counterplay:

- independent confirmation
- signal comparison
- captured courier report

### Compromise stores

Possible costs:

- intelligence exposure
- support equipment

Effects on success:

- target readiness loss
- possible outpost damage

Counterplay:

- guarded depots
- reserve cache
- inspection mission

### Intercept a convoy

Possible costs:

- fuel
- command power or navy XP
- intelligence exposure

Requirements:

- valid route access
- target convoy route

Effects on success:

- target readiness loss
- attacker may recover a small supply share
- higher attribution than ordinary sabotage

## Evolution I actions

### Listen through the pulse

Costs:

- support equipment
- civilian commitment

Effects:

- strong survey gain
- exposure increase

### Build shielded receivers

Costs:

- support equipment
- civilian commitment

Effects:

- lower signal exposure
- modest readiness burden

### Jam the signal

Costs:

- fuel
- civilian commitment
- intelligence exposure

Effects:

- lowers rival signal gain
- can disrupt the user's own data
- raises hostility

## Evolution II actions

### Add field escorts

Costs:

- command power
- support equipment
- fuel

Effects:

- reduces survivor incidents
- raises militarisation pressure if Evolution III is active

### Attempt capture

Costs:

- support equipment
- fuel
- civilian commitment

Requirements:

- verified survivor evidence
- minimum readiness

Effects:

- possible unique fragment
- high exposure and casualty risk

### Avoid contact zone

Costs:

- progress delay

Effects:

- lower exposure
- reroutes survey mission

### Manipulate the survivor

Costs:

- support equipment
- intelligence exposure
- civilian commitment

Effects:

- may move danger toward a rival
- severe backlash and attribution risk

## Evolution III overt actions

### Escort the supply route

Costs:

- fuel
- convoys
- command power or navy XP

Effects:

- protects readiness
- raises militarisation slightly

### Blockade a rival route

Costs:

- fuel
- convoys
- navy XP or command power

Requirements:

- valid maritime reach
- target route

Effects:

- target readiness loss
- high attribution and diplomatic incident risk

### Seize a compromised outpost

Costs:

- fuel
- support equipment
- command power

Requirements:

- target compromised
- military access to the sector

Effects:

- target setback
- attacker gains data or fragments
- potential casualties and exchange of fire

### Establish a demilitarised corridor

Costs:

- political power
- civilian commitment

Requirements:

- willing target or neutral sponsor

Effects:

- lowers hostility and militarisation
- protects both supply routes

## Evolution IV actions

### Stabilize the wreck

Costs:

- support equipment
- civilian commitment
- fuel

Effects:

- preserves Wreck Integrity
- slows personal progress

### Rush the command core

Costs:

- fuel
- support equipment
- civilian commitment

Effects:

- faster final progress
- high exposure and integrity damage

### Search a fragment field

Costs:

- fuel
- support equipment

Effects:

- fragment score and specific fragment category
- reduces time for the main race

### Deny a fragment field

Costs:

- fuel
- support equipment
- intelligence exposure or command power

Effects:

- can bury or contaminate the site
- diplomatic and exposure consequences

## Evolution V actions

### Establish containment

Costs:

- support equipment
- civilian commitment

Effects:

- lowers dependence
- blocks strongest integration route

### Destroy active material

Costs:

- support equipment
- stability or civilian commitment

Effects:

- removes future active-material incidents
- preserves learned base technology
- loses fragment upgrade potential

### Transfer the recovery package

Costs:

- convoys
- civilian commitment

Requirements:

- valid recipient
- route access

Effects:

- moves artifact control
- creates diplomatic consequences
- preserves source ledger

### Conceal continued study

Costs:

- intelligence exposure
- civilian commitment

Effects:

- reduces public information
- raises accident and capture risk

### Integrate alien systems

Costs:

- civilian commitment
- support equipment
- stability risk as consequence

Effects:

- stronger custom-equipment and research benefits
- higher dependence

## Mission families

| Mission | Normal duration | Success | Failure |
| --- | ---: | --- | --- |
| Organize the Southern Expedition | 90 to 150 days | Opens departure | Readiness loss and emergency resupply |
| Reach the Gateway | 90 to 150 days | Locks route and reduces burden | Delay or access renegotiation |
| Establish the Antarctic Outpost | 120 to 180 days | Creates functioning outpost | Damaged camp or alternate landing route |
| Triangulate the Crash Zone | 120 to 240 days | Unlocks final certainty threshold | False sector, lost season, or new survey objective |
| Protect the Supply Route | 90 to 180 days | Prevents one route setback | Readiness loss and convoy incident |
| Confirm the Primary Site | 90 to 150 days | Unlocks final recovery | Bounded progress loss and exposure |
| Secure the Recovery Core | 90 to 150 days | Wins the race | Recovery setback, not automatic elimination |
| Evacuate the Expedition | 90 to 120 days | Preserves personnel and fragments | Higher losses and abandoned data |
| Stabilize the Wreck | 120 to 180 days | Preserves fragment sites | Wreck integrity loss |
| Contain Alien Systems | 180 to 365 days | Safe post-recovery state | Dependence and accident event |

Exact durations should vary by route, preparation, and evolution state. The values above are design bands.

## Mission success and partial success

Missions should resolve with full success, partial success, or failure when the objective supports mixed outcomes.

Examples:

- outpost established but stores damaged
- survey sector confirmed but rival copied the data
- convoy arrived but escort losses raised militarisation
- survivor avoided but a fragment was lost
- wreck stabilized but another country recovered debris

Partial success must have its own effect logic and report direction.

## Selected-target behavior

Rival actions use one selected target at a time for human players.

The selected-target pattern must:

- store the selected rival safely
- show only target-relevant actions
- clear the target when it withdraws, is annexed, or becomes invalid
- keep AI evaluation independent from the human selector
- prevent stale buttons after a roster rebuild

## Cooldowns and escalating cost

Repeated hostile actions should become harder or more expensive.

Use:

- target-specific cooldowns
- action-family cooldowns
- higher attribution after repeated use
- rising hostility
- diminishing returns
- stronger counterintelligence

Do not allow one country to click the same sabotage action every pulse.

## Cleanup

Every mission and action family needs cleanup for:

- withdrawal
- winner declaration
- target invalidation
- war or peace change when relevant
- gateway loss
- outpost abandonment
- evolution disable state
- event closure
- artifact transfer
- incompatible global end-state from another event

The cleanup must remove active decisions, cancel missions, clear selected targets, release temporary industrial commitments, and preserve historical records.

## AI equivalence

AI countries use the same cost, availability, result, cooldown, and cleanup helpers.

The AI may call actions through scheduled effects. It cannot receive hidden free readiness, progress, or fragments outside the documented strategy model.

# Event 32 specification, part 2: Program and launch sites

## Missile program model

Every recipient owns one persistent national missile-program record. The record survives normal government changes, ideology changes, faction changes, and temporary loss of a launch state. It is removed only when the country ceases to exist permanently or an owning cleanup path explicitly transfers or destroys it.

The program uses three main player-facing values.

| Value | Player meaning | Main sources of gain | Main sources of loss |
| --- | --- | --- | --- |
| Operational Reserve | Missiles ready to assign to an operation | Event 32 packages, replenishment, captured stock, special projects | Launches, accidents, capture, sabotage, scuttling |
| Launch Readiness | Ability to prepare and execute launches without delay or failure | Maintenance, training, repairs, repeat firings, test data | Barrages, damaged sites, fuel shortage, neglected maintenance, command disruption |
| Command Control | Government control over crews, codes, warning channels, and launch authority | Security reforms, inspections, stable government, central command | Civil war, captured sites, mutiny, foreign penetration, emergency delegation, false signals |

Recommended ranges:

- Operational Reserve is a nonnegative integer.
- Launch Readiness is clamped from `0` to `100`.
- Command Control is clamped from `0` to `100`.

Guidance quality is an internal derived score. It appears in launch tooltips as a compact grade and risk statement. It does not need a fourth permanent meter.

Retaliation posture is a named state. It appears as one status line when the Automatic Retaliation evolution is active.

## Value bands

### Launch Readiness

| Range | Working status | Gameplay result |
| --- | --- | --- |
| `0` to `24` | Grounded | New launches blocked outside a forced emergency route |
| `25` to `49` | Limited | Precision actions unavailable, preparation is slower, failure risk is higher |
| `50` to `74` | Operational | Baseline operation set available |
| `75` to `89` | High | Faster preparation and improved guidance |
| `90` to `100` | Immediate | Best preparation speed and lowest ordinary failure risk |

### Command Control

| Range | Working status | Gameplay result |
| --- | --- | --- |
| `0` to `19` | Lost | Rogue-site and unauthorized-launch crisis is active |
| `20` to `39` | Fragmented | Emergency actions, high incident risk, automatic posture blocked |
| `40` to `64` | Contested | Normal launches remain possible with additional risk |
| `65` to `84` | Secure | Baseline command state |
| `85` to `100` | Hardened | Lowest rogue risk and best signal verification |

The working labels are directions for final localisation. They are not pasteable final text.

## Derived guidance score

The guidance score is calculated when an operation is prepared and again when it launches.

Inputs should include:

- normalized technology stage
- Launch Readiness
- recent maintenance action
- recent successful test or relevant Event 76 bridge
- barrage size
- range from active launch state to target
- site damage
- Unreliable Guidance evolution
- special payload complexity
- crew training state
- command disruption
- exact target intelligence when available

Suggested conceptual formula:

`guidance = technology base + readiness contribution + maintenance + intelligence - range strain - barrage strain - damage - evolution pressure`

The final implementation must use script constants and reusable helpers. The player sees a grade such as poor, uncertain, serviceable, accurate, or precise plus a short risk breakdown.

## Program status idea

Each program country should have one visible missile-program idea or dynamic modifier. It summarizes:

- technology stage
- reserve band
- readiness band
- command-control band
- active-site count
- retaliation posture when relevant
- active crisis such as compromised command or guidance backlog

The idea should update in place. Do not create a stack of separate permanent ideas for every stage, site, and evolution.

Possible lifecycle:

| Program state | Visible form |
| --- | --- |
| Initial | Experimental missile program |
| Operational | Operational missile command |
| Mature | Strategic missile command |
| Saturated | Saturation missile force |
| Compromised | Compromised missile command |
| Recovered | Reconstituted strategic command |

These are working identity directions. The final implementation may use one dynamic modifier or a small replacement chain.

## Technology adapter

Event 32 needs one event-owned technology adapter.

The adapter must:

1. inspect the country's researched technologies
2. infer the highest supported normalized stage
3. identify the next valid technology in the installed graph
4. grant one step with popups handled consistently
5. preserve prerequisites and mutual exclusions
6. return the new normalized stage
7. return an exhausted-line result when no step remains
8. support any relevant DLC and no-DLC graph variants
9. never remove an existing technology
10. never grant unrelated aircraft, nuclear, chemical, biological, or Kruger technology

The adapter should fail closed when the installed graph cannot be mapped. A country with an unresolved graph mapping receives the reserve and site package only if that result has been explicitly approved during implementation. Otherwise, its transaction is blocked and logged for repair.

## Operational reserve model

The operational reserve is the event's authoritative count for launch planning.

Suggested baseline package formula:

- start with `4`
- add `1` for each complete block of `8` total civilian and military factories, capped at `8`
- add `1` for each complete block of `10` controlled states, capped at `4`
- add `2` when the country is in a live war with a valid enemy
- clamp the ordinary first package near `18`

Suggested mature package:

- start with `8`
- use the same economy and territory contributions
- add a readiness-dependent bonus
- clamp the ordinary mature package near `24`
- apply the Saturation Arsenals multiplier only after that evolution is active

The final formula must remain understandable and must not turn large countries into unlimited stockpile generators. Repeated Event 32 firings remain the strongest free source. Ordinary replenishment should require real economic commitment.

## Reserve integrity

Reserve changes must use a single helper family.

Required operations:

- add reserve
- remove reserve
- test whether reserve can pay a launch
- reserve missiles for a prepared operation
- return reserved missiles after cancellation
- destroy reserved missiles after a failed launch when appropriate
- transfer a bounded captured share
- scuttle reserve
- clear reserve when a country is removed
- display current and reserved counts

A prepared operation reserves its missiles immediately. They cannot be assigned to another operation. Canceling before a defined commitment point returns the missiles after a readiness and command penalty. Canceling after crews have fueled and armed the launch may destroy or consume part of the reserved package.

## Launch-state records

A launch state is a physical site record attached to a real state.

Each record should store or derive:

- owning program country
- current controller
- site level
- launch capacity
- hardening
- site security
- local readiness contribution
- damage state
- compromised state
- mutiny or rogue state
- captured state
- scuttled state
- last operation date
- current prepared-operation receipt when one exists

Use state variables, flags, dynamic modifiers, or a documented combination. Keep the public state tooltip concise.

## Eligible launch-state contract

The ordinary first-site pool should prefer states that meet all of these conditions:

- owned by the recipient
- controlled by the recipient
- a core of the recipient
- not a wasteland
- not impassable or otherwise invalid for the selected building surface
- not occupied enemy territory
- not under an active hostile state takeover
- has useful infrastructure or supply access
- has enough strategic depth to avoid an active frontline when alternatives exist
- has a valid rocket-site or launch-site building surface
- is not an isolated empty region when a better connected state exists

The selector may use a fallback ladder.

### Site selection ladder

1. existing active Event 32 launch state that can be upgraded
2. owned, controlled core state with infrastructure, supply, air defense, and strategic depth
3. owned, controlled core state with weaker protection
4. owned and controlled noncore state with high compliance or long-term control
5. sole owned and controlled state of a one-state country
6. capital state when no safer valid state exists
7. deferred site transaction when no valid state exists

The selector must not choose a random occupied enemy state, wasteland, invalid island, or state already at the event site cap.

## Site scoring factors

Use a complete candidate pool and a documented score model.

Positive factors:

- existing launch infrastructure
- infrastructure
- supply connection
- radar
- anti-air
- distance from an active enemy front
- distance from a hostile border
- interior position
- state control stability
- moderate industrial access
- existing Event 32 security investment
- different strategic region from the primary site when selecting redundancy

Negative factors:

- active combat or contested control
- enemy occupation
- current frontline exposure
- low infrastructure
- isolated island with no meaningful military access
- severe contamination or wasteland state
- high resistance
- recent missile strike damage
- launch-site congestion
- dense capital or industrial center when a safer state exists

The selector should avoid making the capital the automatic first choice. A capital may still win when the country has little territory or when its defenses make it the only practical site.

## Site capacity

Capacity limits how many missiles can be assigned to one prepared operation from that state.

Suggested ordinary capacity:

| Site level | Suggested operation capacity |
| --- | --- |
| Initial | `4` |
| Reinforced | `6` |
| Expanded | `8` |
| Strategic | `10` |

The exact relationship between a native `rocket_site` building level and Event 32 capacity must be verified. Event 32 may maintain its own normalized capacity even when the native building has a different level scale.

A country can combine capacity from several active sites for a strategic or saturation operation. Every participating site receives readiness loss and an operation receipt.

## Site count cap

Suggested ordinary site cap:

| Controlled land states | Ordinary site cap |
| --- | --- |
| `1` to `4` | `1` |
| `5` to `15` | `2` |
| `16` to `35` | `3` |
| `36` or more | `4` |

Saturation Arsenals may add one temporary or permanent cap slot when the country can support it.

The cap also considers:

- total reserve
- current site capacity
- strategic-region diversity
- country industry
- whether an existing site is damaged or compromised
- whether the country is at war
- whether all current sites are exposed to one front

A new site is justified when at least one of these is true:

- reserve substantially exceeds total operation capacity
- the country has no surviving secure site
- the current site is exposed to an enemy front
- the country has reached a later technology stage that requires redundancy
- Saturation Arsenals has made the current network insufficient
- a repeat Event 32 firing grants a mature package and every current site is fully upgraded

## Site reinforcement priority

Repeated Event 32 firings use this order:

1. restore a damaged primary site
2. secure a compromised primary site when ordinary repair can do so
3. increase capacity at an existing site
4. improve hardening
5. improve security
6. establish a secondary site
7. establish later sites up to the cap

A site in active enemy control cannot be repaired by its former owner through a repeat firing. That firing improves the country's remaining controlled network or creates a replacement if the cap rules allow it.

## Hardening

Hardening reduces:

- building damage from enemy missile strikes
- chance of complete site destruction
- chance that stored reserve is lost in one hit
- chance that a captured state yields an intact site
- readiness loss from nearby strategic damage
- command interruption from infrastructure damage

Hardening does not make the state immune. Saturation attacks, thermonuclear effects, occupation, or deliberate scuttling can still destroy a hardened site.

## Site security

Site security reduces:

- sabotage
- foreign bribery
- code theft
- crew defection
- local commander seizure
- mutiny
- captured-reserve transfer
- false order acceptance

Security should interact with Command Control. A secure site under a fragmented national command remains dangerous. A strong national command with one neglected site can still suffer a local incident.

## Damage and repair

Site damage should have at least three meaningful states:

| Damage state | Effect |
| --- | --- |
| Damaged | Reduced capacity and readiness contribution |
| Disabled | Cannot launch until repaired |
| Destroyed | Site record removed or converted to ruins, reserve share lost |

Repairs require time and concrete resources. A repair decision may use:

- support equipment
- civilian factory commitment
- manpower
- fuel for testing
- trains when the site is landlocked and the network is damaged

One action must stay within the four-cost limit.

A repeat Event 32 firing may provide partial repairs, but it must not fully restore every destroyed site for free.

## Capture

When a launch state changes controller:

1. freeze the former owner, new controller, site condition, and stored-share estimate
2. mark the site captured and compromised
3. disable ordinary launches from that site
4. reduce the former owner's available capacity
5. create a bounded captured-reserve estimate
6. give the new controller a site-resolution choice or AI path
7. update Command Control for both sides
8. clear stale prepared operations tied to the site
9. record the incident once

Available resolution paths:

- secure and study the site
- integrate it into an existing program
- scuttle the site
- transfer the site to an ally or overlord when a safe scripted route exists
- leave it guarded but inactive during immediate crisis

Integration is slower and riskier when the new controller lacks the relevant technology. A country cannot instantly gain the full former owner's technology line from one captured state.

## Captured reserve

A site should expose a bounded share of the former owner's reserve based on:

- site capacity
- current operation assignment
- damage
- hardening
- scuttling
- former-owner command control
- capture speed
- new-controller intelligence and security

The transfer cannot exceed the former owner's available reserve. It must debit the former owner and credit the new controller exactly once.

## Civil wars

A civil war resolves missile infrastructure by state control.

Required behavior:

- each side receives the launch states it physically controls
- the parent reserve is split by active-site capacity and a bounded central-command share
- no missile is duplicated
- both sides begin with reduced Command Control
- prepared operations are canceled or transferred through explicit receipts
- sites near the civil-war front become compromised
- Rogue Launch Commands risk rises sharply
- a side with no site cannot use its reserve until it captures or establishes one
- the civil war event can call the Event 32 split helper without activating an Event 32 evolution by itself

This bridge is important for Event 21 and any other event-created civil war.

## Country release and independence

A newly released country that receives an existing launch state resolves the same capture and inheritance contract.

Possible outcomes:

- the releasing country removes or scuttles the site before transfer
- the new country receives an inactive compromised site
- a negotiated transfer gives the new country codes and a small reserve share
- the former owner keeps remote control only when an explicit event route supports it
- a third party attempts to seize or buy the site under Rogue Launch Commands

Event 6 and Event 5 should call the shared inheritance helper when state packages contain Event 32 launch states.

## Annexation and country removal

When a country ceases to exist:

- every surviving launch state is processed by current controller
- remaining reserve is distributed only through exact site receipts or destroyed
- prepared operations are canceled
- retaliation posture is disabled
- incident queue entries are retargeted or canceled
- country variables and flags are cleared after transfer
- Event Logs keep historical records
- no global event target remains pointed at the removed country

## State ownership changes without control changes

Peace conferences, scripted transfers, and negotiated handovers can change ownership while the old controller remains briefly present.

The physical site follows current control for immediate security. Long-term program ownership follows the resolved handover transaction. The implementation must not assume that owner and controller are always identical.

## Site map and UI presentation

Event 32 should reuse the native building and state view where possible.

The player needs to see:

- which states are active launch states
- capacity band
- hardening band
- security band
- damage or compromise status
- prepared operation status

Use state modifiers, building tooltips, decision target markers, or map icons supported by the final engine route. A separate global launch-site GUI is unnecessary.

## DLC and operation-adapter parity

Two operation adapters may be required:

### Native raid adapter

Use when the installed game and relevant DLC expose a stable rocket-site raid route with exact target state, starting site, equipment or reserve receipt, outcome, and AI support.

### Scripted strike adapter

Use when the native raid route is unavailable or cannot satisfy the Event 32 contract.

The scripted adapter must preserve:

- exact country and state target
- reserve payment
- participating launch-state capacity
- preparation time
- launch cooldown
- guidance and failure outcome
- damage
- deaths
- special payload consumption
- condemnation
- AI target logic
- Event Logs and incident records

The adapter choice must be explicit, documented, and validated. A no-DLC player must not receive a launch site and reserve that can never be used.

## Performance requirements

- no daily or weekly global site scan
- site capture checks use bounded ownership-change hooks or event-owned adapters
- readiness recovery uses decision actions, repeat firings, or one-shot delayed recovery jobs after launches
- prepared operations use one receipt per operation
- site records are indexed by country or maintained in event-owned arrays where practical
- cleanup runs on exact country removal, site transfer, operation completion, or scenario reset
- no repeated random-state search after a valid state is frozen

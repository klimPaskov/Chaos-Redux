# Event 32 specification, part 2: Program and launch sites

## Missile program model

Every recipient owns one persistent national missile-program record.
The record survives government, ideology, and faction changes and temporary loss of a launch state.
It is removed only when the country ceases to exist permanently or an owning cleanup path explicitly transfers or destroys it.

The program has three player-facing values.

| Value | Player meaning | Main sources of gain | Main sources of loss |
| --- | --- | --- | --- |
| Operational Reserve | Missiles ready to assign to an operation | Event 32 packages, replenishment, integrated captured stock | Launches, accidents, capture, sabotage, scuttling |
| Launch Readiness | Ability to prepare and execute launches without delay or failure | Maintenance, repairs, repeat firings | Launches, damaged sites, disasters, command disruption |
| Command Control | Government control over crews, codes, warning channels, and launch authority | Code rotation, command authority work, loyal-force recovery | Civil war, captured sites, mutiny, emergency delegation, false signals |

Operational Reserve is a nonnegative integer.
Launch Readiness and Command Control are clamped from `0` to `100`.

## Player-facing value budget

The player sees exactly these program surfaces:

- the three values above in the category header, each with its texticon
- one guidance grade label (Poor, Uncertain, Serviceable, Accurate, Precise) in the category context line and launch tooltips
- one site status per launch state, shown as a single state modifier (active, hardened, damaged, compromised, or rogue)
- the retaliation posture label (Off, Supervised, Delegated, Automatic) once Automatic Retaliation is available
- the current crisis or prepared target in one context line

Everything else stays internal: site hardening and security scores, capacity numbers, guidance pressure inputs, rogue pressure, evolution pressure, queue and receipt fields.
An internal value may appear in the tooltip of the one decision that changes it (for example, the hardening decision may name the site's protection band), but never as a standing list.
A new player-facing number needs a decision it drives; otherwise it stays internal.

## Thresholds

The constants in `missiles_program_value` are authoritative.
The design meaning of the implemented gates:

| Gate | Value | Meaning |
| --- | ---: | --- |
| Launch readiness floor | `25` | Below this, ordinary launches are blocked |
| Baseline launch gate | `50` | Ordinary preparation is available |
| Precision gate | `60` | Precision strikes need readiness at or above this |
| Rogue command gate | `40` | Below this, rogue pressure becomes serious |
| Secure command gate | `65` | Baseline secure command, required for Supervised posture work |
| Automatic posture gate | `75` | Automatic posture can be adopted through ordinary policy |
| Hardened command gate | `85` | Lowest rogue risk and best verification |

Localisation describes these as plain conditions in requirement tooltips, not as numbered bands.

## Derived guidance grade

Guidance is calculated when an operation is prepared and again at launch.
Inputs: normalized technology stage, Launch Readiness, recent maintenance and training, barrage size, range, site damage, Unreliable Guidance, payload complexity, Command Control, and hardening.
The player sees only the grade and a one-line risk statement; the formula and inputs stay internal.

## Program status idea

Each program country has one status idea that names what kind of force it is, not its numbers.
Three implemented variants replace one another in place: `missiles_program_experimental`, `missiles_program_operational`, and `missiles_program_compromised`.
The idea does not list stage, reserve, readiness, control, site count, or posture; those live in the category header.

## Technology adapter

The event-owned adapter:

1. inspects the country's researched technologies
2. infers the highest supported normalized stage
3. identifies the next valid technology in the installed graph
4. grants one step with its notification suppressed
5. preserves prerequisites and mutual exclusions
6. returns the new stage, or an exhausted-line result that triggers the mature package
7. supports the no-DLC graph through the `improved_rocket_engines` successor
8. never removes a technology
9. never grants unrelated aircraft, nuclear, chemical, biological, or Kruger technology

An unmappable graph records an unresolved mapping instead of granting an unrelated technology.

## Operational reserve model

The operational reserve is the authoritative count for launch planning.

Baseline package: `4`, plus `1` per complete block of `8` factories (capped at `8`), plus `1` per complete block of `10` controlled states (capped at `4`), plus `2` at war, clamped at `18`.
Mature package: base `8` with the same contributions, clamped at `24`.
Saturation doctrine raises the ceiling to `40` while the track is enabled and adopted.
Creation packages evaluate all factors first and round to whole missiles before changing the reserve.

Repeat firings remain the strongest free source.
Replenishment requires real economic commitment and a cooldown.

## Reserve integrity

Reserve changes use one helper family: add, remove, test payment, reserve for an operation, return after cancellation, destroy after a failed launch or site loss, transfer captured stock, scuttle, clear on removal, and display available and reserved counts.

A prepared operation reserves its missiles immediately, allocated in whole missiles across participating sites by spare capacity.
Reserved missiles cannot be assigned twice.
Cancelling before commitment returns them once; losing a reserving site before launch loses exactly that site's allocation once.
Free site stock fills capacity left after that site's operation allocation, and any remainder is recorded as unallocated national reserve.
The detailed custody rules are in `docs/plans/032_missiles_plans/032_reserve_custody_repair_2026-10-07.md` and test cases `CUSTODY-01` to `CUSTODY-06`.

## Launch-state records

A launch state is a physical site record attached to a real state.
Each record stores or derives the owning program, current controller, site level, capacity, site-held reserve, hardening, security, damage, capture, isolation, suspension, compromise, rogue state, strategic-region identity, last operation, and the current prepared-operation allocation.

## Eligible launch-state contract

The first-site pool prefers states that are:

- owned, controlled, and core to the recipient
- not wasteland, impassable, occupied, or under a hostile takeover
- supplied, with usable infrastructure
- away from an active front when alternatives exist
- not an isolated empty region when a connected state exists

### Site selection ladder

1. existing active Event 32 site that can be upgraded
2. owned, controlled core state with infrastructure, supply, air defense, and strategic depth
3. owned, controlled core state with weaker protection
4. owned and controlled noncore state with high compliance
5. sole owned and controlled state of a one-state country
6. capital, when no safer valid state exists
7. deferred site transaction when no valid state exists

The selector never chooses an occupied enemy state, wasteland, invalid island, or a state already at the site cap.

## Site scoring factors

Use a complete candidate pool and the scoring weights in `missiles_site_score`.

Positive: existing launch infrastructure, infrastructure, supply, radar and anti-air, distance from the front and hostile borders, interior position, stable control, existing security investment, and a different strategic region from the primary site when selecting redundancy.

Negative: active combat, occupation, frontline exposure, low infrastructure, isolated islands, contamination or wasteland, high resistance, recent strike damage, and a dense capital or industrial center when a safer state exists.

The capital is a fallback, not an automatic first choice.

## Site capacity

Capacity limits how many missiles one site can commit to a prepared operation.

| Site level | Capacity |
| --- | ---: |
| Initial | `4` |
| Reinforced | `6` |
| Expanded | `8` |
| Strategic | `10` |

Event 32 keeps its own normalized capacity derived from site level rather than from the native `rocket_site` building level.
Strategic and saturation operations combine capacity from several sites, and every participating site pays readiness and carries an allocation receipt.

## Site count cap

The design cap scales with controlled land and stops at four sites, so a small country cannot spread a network across its few states.
Implemented today: only the flat maximum of four (`missiles_tuning.site_count_maximum`) is enforced.
Pending: the territory scale defined by the unused constants `site_count_base = 1`, `site_count_state_threshold = 8` and `site_count_state_step = 12` (one site, a second at 8 controlled states, one more per 12 further states, at most four) must gate secondary-site construction and the mature package.

A secondary site is justified by a single working site, by stored missiles exceeding total site capacity, or by the mature-program signal, and needs Command Control at the operation minimum.

## Site reinforcement priority

Repeat firings use this order:

1. restore a damaged primary site
2. secure a compromised primary site when ordinary repair can do so
3. increase capacity at an existing site
4. improve hardening
5. improve security
6. establish a secondary site
7. establish later sites up to the cap

A site in enemy control cannot be repaired by its former owner through a repeat firing.

## Hardening and security

Hardening reduces strike damage, complete destruction, single-hit reserve loss, intact capture, and readiness loss from nearby damage.
Security reduces sabotage, bribery, code theft, defection, local seizure, mutiny, and false-order acceptance.
Neither grants immunity.
Both are internal scores; the player sees the resulting site status and the requirement text of the actions that change them.
A secure site needs both scores at `70` (`missiles_reserve.site_secure_*_threshold`).
README open question 4 proposes merging the two scores.

## Damage and repair

| Damage state | Effect |
| --- | --- |
| Damaged | Reduced capacity and readiness contribution |
| Disabled | Cannot launch until repaired (damage at or above `50`) |
| Destroyed | Site record retired and its stock lost (damage at or above `90`) |

Repair is a 45-day suspension project: the site leaves launch planning, then returns with its damage cleared and one capacity-recovery step.
A cancelled or expired repair returns the site in its current condition.
A repeat firing may provide partial repairs but never restores a destroyed site for free.

## Capture

When a launch state changes controller:

1. bind the former controller as an event target before the handler runs
2. mark the site captured and compromised and disable launches from it
3. reduce the former owner's capacity and settle any operation allocation at that site
4. seal a bounded share of the former owner's stock as captured stock for the new controller
5. lower Command Control for both sides
6. record the incident once
7. offer the new controller the resolution decisions

Implemented resolutions are four final, mutually exclusive decisions shown for one captured state at a time:

- guard: the site stays inactive and its captured stock stays sealed
- study: the same, plus a guidance-training gain
- integrate: a guided program only; the site joins the network and its surviving stock joins Operational Reserve once
- scuttle: the site and its stock are destroyed once

Diplomatic transfer of a captured site was `rejected` for this round (agent decisions, item 3).
Integration cannot grant the former owner's technology line.

## Captured reserve

The sealed share depends on site capacity, current assignment, damage, hardening, and scuttling.
It cannot exceed the former owner's available reserve and is debited and credited exactly once.
Recapture moves existing sealed stock between holders' captured-reserve ledgers without charging the former holder's ordinary reserve.

## Civil wars

Infrastructure follows state control:

- each side receives the launch states it physically controls
- the parent reserve splits by active-site capacity and a central-command share (`50` percent)
- no missile is duplicated
- both sides lose Command Control
- prepared operations are cancelled through receipts
- frontier sites become compromised
- Rogue Launch Commands pressure rises
- a side without a site cannot use its reserve until it captures or establishes one
- the split helper never activates an evolution

## Country release, annexation, and removal

A released country that receives a launch state uses the same capture and inheritance contract.
A site that changes hands while suspended arrives unsuspended, compromised, and isolated so its new controller can repair it.

When a country ceases to exist, every surviving site is processed by current controller, reserve moves only through exact site receipts or is destroyed, prepared operations are cancelled, posture is disabled, queue entries are cancelled, program variables are cleared after transfer, and no global event target points at the removed country.

## Ownership without control

Peace conferences and scripted transfers can change ownership before control.
The physical site follows current control; long-term program ownership follows the resolved handover.

## Site presentation

The player sees which states are launch states through the single site-status modifier and the site-targeted decisions.
A separate launch-site GUI is unnecessary (explicit user presentation rule).

## Operation adapter

The scripted strike adapter is the accepted route (part 8, Operation adapter).
It preserves exact target state, reserve payment, site capacity, preparation, cooldown, guidance, damage, deaths, payload consumption, condemnation, AI, logs, and incident records.

## Performance requirements

- no daily or weekly global site scan
- capture uses the bounded state-control hook
- readiness recovers through decisions, repeat firings, or one-shot recovery after launches
- one receipt per prepared operation
- site records are indexed by country registry arrays
- cleanup runs on exact country removal, site transfer, operation completion, or scenario reset

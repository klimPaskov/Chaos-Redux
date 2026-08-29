# Event 023 specification, Part 2: Arsenal command, production, and posture

## Mechanic overview

The persistent Soviet nuclear system uses two visible values and one discrete posture.

The values are:

- Arsenal Readiness.
- Command Integrity.

The posture describes the current public and military policy of the arsenal. It is displayed through the event-owned national spirit and decision-category status text.

This structure keeps the system readable. Bomb count, reactor count, delivery capability, public knowledge, active target, storage security, and shared global consequences remain visible through existing game surfaces or concise category text. They do not become separate event meters.

## Arsenal Readiness

Arsenal Readiness measures whether the Soviet Union can turn a physical bomb stockpile into an executable test, demonstration, retaliation, or combat release.

Readiness includes:

- Technical certification.
- Warhead maintenance.
- Tested design confidence.
- Delivery crew training.
- Available fuel and suitable aircraft.
- Communication drills.
- Target-package preparation.
- Surviving command and storage infrastructure.

Readiness uses a zero to 100 scale.

### Readiness bands

| Band | Working state label | Gameplay meaning |
| --- | --- | --- |
| 0 to 24 | Experimental stockpile | Weapons exist, but combat release is blocked. Laboratory proof, storage, and delivery preparation are the priority. |
| 25 to 49 | Limited readiness | Covert testing, public demonstration, and a tightly bounded wartime military target become possible. |
| 50 to 74 | Operational arsenal | Normal wartime targeting, credible ultimata, and prepared retaliation become available. |
| 75 to 89 | High alert | Authorization and retaliation are faster. Repeated alert cycles strain Integrity and increase false-warning risk. |
| 90 to 100 | Immediate release posture | The widest legal release options are available. Safety, diplomacy, and command cohesion face severe pressure. |

Readiness should not grant damage multipliers. Shared nuclear strike effects remain based on the shared system. Readiness controls access, timing, reliability, abort chance, target breadth, and the number of concurrent preparations.

### Readiness gains

Readiness rises through:

- Laboratory proof work.
- Successful tests.
- Delivery crew training.
- Command exercises.
- Warhead maintenance.
- Building or securing reactors and assembly capacity.
- Preserving communication links during war.
- Completing target reconnaissance.
- Recovering missing or unsecured devices.
- Choosing a custody doctrine that favors rapid use.

### Readiness losses

Readiness falls through:

- Moving the test ground or central command.
- Changing custody doctrine.
- Losing storage or production states.
- Strategic bombing of registered facilities.
- Low fuel or loss of suitable delivery aircraft.
- Failed tests or aborted launches.
- Extended high-alert periods.
- Purges, commander refusal, scientist refusal, or disputed orders.
- Soviet Collapse pressure.
- Dismantlement or moratorium actions.
- Repeated use without maintenance.

Readiness changes should be large enough to alter available actions. Routine maintenance can move the value modestly. Tests, command collapse, major site loss, doctrine reform, and confirmed use should move it significantly.

## Command Integrity

Command Integrity measures whether political authority, technical personnel, delivery forces, storage guards, and communications agree on who can order, authenticate, prepare, stop, and account for nuclear use.

Integrity includes:

- Central authority.
- Authentication and code control.
- Two-person or multi-office confirmation where the doctrine requires it.
- Physical custody accounting.
- Loyalty of commanders and guards.
- Scientific certification.
- Secure communications.
- Confidence that stored devices remain where the ledger says they are.

Integrity uses a zero to 100 scale.

### Integrity bands

| Band | Working state label | Gameplay meaning |
| --- | --- | --- |
| 80 to 100 | Sealed chain | Unauthorized use and loss are rare. Release may take longer under strict doctrines. |
| 60 to 79 | Controlled chain | Normal operation is reliable. Bounded command incidents remain possible under war or collapse. |
| 40 to 59 | Contested chain | Some commands dispute access, timing, or orders. Target preparation and transfers face delay. |
| 20 to 39 | Fragmented chain | Missing devices, refusal, seizure, false orders, and local custody crises become likely. |
| 0 to 19 | Broken chain | Normal release is blocked unless a validated local retaliation or high-chaos emergency route exists. The priority becomes accounting, recovery, or dismantlement. |

Low Integrity does not make launches easier by default. It creates danger, confusion, and possible local access, but a weapon still needs technical certification, delivery, and a valid shared strike route.

### Integrity gains

Integrity rises through:

- Secure accounting and inspection.
- Hardening and guarding storage sites.
- Restoring rail and communication links.
- Returning seized devices to verified custody.
- Establishing joint custody under a negotiated settlement.
- Adding safety interlocks and authentication procedures.
- Standing down after a false warning.
- Choosing not to overrule a valid safety objection.
- Dismantling devices that cannot be securely maintained.
- Ending Event 5 through an agreement that accounts for the arsenal.

### Integrity losses

Integrity falls through:

- Dispersal without adequate guards or communications.
- Emergency delegation.
- Overruling safety certification.
- Purging technical staff or delivery commanders.
- Losing the capital, central command, storage, or production sites.
- Moving weapons through contested railways.
- Empty threats and repeated backdowns.
- Conflicting release orders.
- Unauthorized loading or refusal incidents.
- Soviet Collapse authority loss.
- Breakaway seizure.
- Foreign raids or occupation.
- Repeated strikes that outpace accounting and maintenance.

## The readiness-integrity tradeoff

The design is built around a command-control tradeoff.

A system optimized for rapid and survivable release tends to distribute authority, pre-position weapons, and shorten confirmation. That raises Readiness and can preserve retaliation, but it weakens Integrity.

A system optimized against unauthorized use tends to centralize authority, add certification, and delay release. That protects Integrity, but can reduce Readiness and make the arsenal vulnerable to command decapitation.

The player should feel this tradeoff without reading a technical essay. Decisions and tooltips should state which value they improve, which value they risk, and which public consequence follows.

## Nuclear posture

Nuclear posture is a discrete state derived from player commitment, public reveal, current evolution access, and active war conditions.

The following labels are working mechanic labels.

### Hidden arsenal

- Default opening posture.
- Foreign public knowledge is Unknown or Suspected.
- Development, safety, covert testing, and delivery preparation dominate.
- Direct peacetime ultimata are unavailable.
- Wartime release requires a valid enemy, sufficient Readiness, and a bounded target profile.

### Demonstrative deterrence

- Opened by a public test, explicit public reveal, or deliberate strategic declaration.
- Public knowledge becomes Demonstrated.
- Foreign reactions and future arms-race hooks activate.
- Wartime warnings and demonstration options become stronger.
- Secrecy decisions shift from hiding the arsenal to hiding deployments and targets.

### Coercive doctrine

- Opened by Evolution II.
- Direct ultimata against valid minors and Soviet breakaways become possible.
- Target response missions, credibility memory, and foreign guarantee reactions activate.
- The Soviet Union can back down, compromise, declare war, or authorize a limited release after refusal.

### Retaliatory release

- Opened by Evolution III or by suffering a confirmed nuclear strike.
- The arsenal is prepared to survive and answer enemy nuclear use.
- Major-to-major first use remains blocked for Soviet AI below 1000 Chaos.
- Emergency stand-down, hotline, reserve preservation, and counterforce planning become available.

### Unrestrained release

- Opened by Evolution IV at 1000 or more Chaos.
- Soviet AI first use against a nuclear major becomes possible under strict strategic-loss gates.
- Player access to the widest exchange plans becomes available.
- Countervalue targeting remains the highest-consequence route and is strongly restricted for AI.

### Atomic moratorium

- Optional controlled end-state.
- Normal targeting and testing are disabled.
- The Soviet Union maintains a sealed reserve, dismantles the arsenal gradually, or transfers devices through a settlement.
- Reactivation requires a severe crisis, a long preparation, and a major Integrity cost.
- A moratorium does not erase public knowledge, prior condemnation, deaths, contamination, or foreign arms-race progress.

## National spirit lifecycle

Event 23 should use one primary visible national spirit family and avoid stacking several permanent ideas.

| Working form | Unlock | Role | Changes into |
| --- | --- | --- | --- |
| Secret Soviet Arsenal | Event opening | Represents secrecy, reactor and storage burden, current posture, Readiness, and Integrity summary | Demonstrated Arsenal, Coercive Arsenal, Retaliatory Command, Atomic Moratorium, Broken Chain |
| Demonstrated Arsenal | Public test or reveal | Represents a known Soviet deterrent and foreign alert | Coercive Arsenal, Retaliatory Command, Atomic Moratorium |
| Coercive Arsenal | Evolution II commitment | Represents direct nuclear pressure and credibility strain | Retaliatory Command, Unrestrained Release, Atomic Moratorium, Broken Chain |
| Retaliatory Command | Evolution III or confirmed enemy nuclear strike | Represents survivable response preparation and exchange risk | Unrestrained Release, Atomic Moratorium, Broken Chain |
| Unrestrained Release | Evolution IV commitment | Represents high-chaos first-use planning and severe diplomatic isolation | Atomic Moratorium, Broken Chain, terminal shared world state |
| Broken Chain | Integrity below the critical floor or severe collapse failure | Represents disputed custody, blocked normal release, loss risk, and emergency recovery | Restored Command, Joint Custody, Atomic Moratorium, arsenal loss |
| Atomic Moratorium | Controlled stand-down | Represents sealed weapons, dismantlement, inspection, or negotiated restraint | Reactivated Command only through a severe crisis route |

The spirit should show current posture and the two visible values through dynamic localisation. It should not list every internal variable or calculation.

## Arsenal accounting

The physical bomb stockpile remains the authoritative count for operational Soviet nuclear bombs.

Event 23 adds an accounting layer for state-linked custody during tests, transfers, collapse, and occupation.

The accounting layer distinguishes:

- Operational Soviet bombs.
- Devices assigned to secure Soviet storage.
- Devices in transit.
- Devices under breakaway custody.
- Devices under foreign or joint custody.
- Devices being dismantled.
- Missing or unaccounted devices.

The sum of assigned, transferred, dismantled, and missing devices must reconcile with every Event 23 stockpile movement. No decision may create or lose bombs without a corresponding ledger transaction.

Normal peacetime operation does not need to assign every individual bomb to a separate state row. Storage sites can hold dynamic shares. The exact state ledger becomes important when control changes, a convoy moves devices, or the Soviet Union fragments.

## Storage network

The opening creates a bounded number of storage states based on stockpile size, current evolution stage, Soviet territory, and available secure interior states.

A good baseline network has enough sites to prevent one strike or occupation from removing the entire arsenal, but few enough sites that the player can understand and defend them.

Storage-site qualities include:

- Secure rail connection.
- Distance from an active front.
- Air defense and garrison presence.
- Infrastructure and supply access.
- Political loyalty.
- Low foreign intelligence exposure.
- Low local unrest.
- Valid central command communication.

The player should see storage security as a summary and receive reports when a site becomes exposed. The decision category should not list every safe depot at all times.

### Storage hardening

The player can harden selected high-risk sites through a timed decision.

The action should:

- Commit civilian construction capacity.
- Consume support equipment and trains or other verified logistics resources.
- Require control of the state and a secure route.
- Improve survival against strategic bombing and occupation.
- Improve Command Integrity.
- Reduce the number of devices lost or seized when the state changes hands.
- Create a long cooldown for the same state.

### Storage dispersal

The player can move part of the stockpile to a new valid site.

The action should:

- Require trains, fuel, guards, and a secure route.
- Temporarily reduce Readiness.
- Create a convoy or transfer mission.
- Increase survival against one-site loss.
- Increase short-term discovery and interception risk.
- Increase collapse risk when the destination has weak loyalty or rising Event 5 pressure.

### Centralization

The player can consolidate devices at fewer sites.

The action should:

- Improve Integrity and accounting.
- Reduce maintenance burden.
- Make the arsenal more vulnerable to strategic bombing, occupation, and command decapitation.
- Require enough secure capacity at the destination.
- Never allow the entire stockpile to move into one state during an active major war.

## Reactor and fissile production program

The event uses current-vanilla nuclear reactors and capability. It must not invent a separate uranium economy or custom reactor building.

The reactor program supports:

- Replacement of expended or dismantled bombs.
- Larger assembly batches.
- Faster technical certification.
- Stronger pre-fire evolved openings.
- Foreign detection through visible industrial expansion.
- Event 5 inheritance pressure when reactor states fall under breakaway control.

### Expand fissile production

This is a timed construction program, not an instant reactor grant during ordinary play.

The program should:

- Select one valid Soviet-controlled industrial state.
- Commit civilian factories for a substantial duration.
- Require secure infrastructure and supply.
- Add reactor construction progress or a reactor level according to the current installed engine pattern.
- Increase foreign detection risk if the program is already suspected.
- Increase assembly capacity after completion.
- Become more expensive when repeated rapidly.
- Use a state cap and national cap so repeated clicks cannot create an unlimited reactor burst.

Evolution I and later pre-fire openings may grant completed reactors immediately because the stronger opening represents a program that matured before the random event became public to the player.

### Reactor state loss

A lost reactor state should:

- Reduce Soviet production capacity.
- Lower Readiness.
- Create foreign or breakaway interest.
- Accelerate independent operationalization only when the new controller also has devices, technical personnel, and a delivery route.
- Never give a full usable arsenal through reactor ownership alone.

## Warhead assembly

The player can assemble additional bombs through a timed batch decision.

The batch size should scale with:

- Controlled reactor count.
- Current Soviet industry.
- Technical readiness.
- Current bomb stockpile.
- Active war and strategic bombing pressure.
- Evolution stage.

The action should commit production and technical capacity for several months. It should not convert political power directly into bombs.

A batch can fail or underperform when:

- A production state is bombed or occupied.
- Command Integrity is severely degraded.
- The Soviet Union loses the technical site.
- Event 5 interrupts transport or staff authority.
- A safety crisis suspends certification.

A failed batch should return unused resources where the engine and existing cost helpers allow it. It should not silently consume a full cost and give nothing without a visible incident.

## Warhead maintenance

A large stockpile creates maintenance and accounting pressure.

Maintenance should be represented through periodic event-owned checks or bounded scheduled jobs tied to the active arsenal. It should not use an unauthorized whole-world daily scan.

Maintenance consequences include:

- Readiness decay when the stockpile greatly exceeds reactor and technical capacity.
- Integrity strain when too many storage sites are active.
- Higher failure risk for old untested devices.
- A reason to dismantle surplus bombs.
- A reason to invest in safety and inspection.

The player can run a maintenance cycle that temporarily reduces available readiness while restoring reliability and accounting.

The player should not need to click maintenance constantly. One medium-duration action should stabilize the arsenal for a meaningful period.

## Dismantlement and stockpile reduction

Dismantlement is a real strategic route, not a cosmetic button.

The action should:

- Remove a chosen bounded number of bombs.
- Commit technical and civilian capacity.
- Improve Command Integrity.
- Reduce maintenance burden and accident risk.
- Reduce some public foreign pressure only when the process is verified or observed.
- Never reverse deaths, contamination, condemnation history, or prior nuclear use.
- Support achievement and moratorium routes.

During Event 5, dismantlement can occur under Soviet, breakaway, joint, or foreign-supervised custody according to Part 6.

## Delivery preparation

The event does not grant free bombers.

A valid air-delivery route requires the current installed game conditions for nuclear delivery, including a suitable aircraft capability, range, fuel, airbase access, and any air superiority or mission requirement used by the shared strike system.

Event 23 adds preparation actions that make the existing delivery force usable:

- Train delivery crews.
- Reserve suitable aircraft.
- Conduct route reconnaissance.
- Prepare an emergency forward base.
- Harden communication and release procedures.

These actions can improve Readiness, shorten authorization, and increase the chance that a planned release reaches the shared strike adapter.

They do not create a new aircraft type, custom air wing, or missile substitute.

Future Event 32 may provide a missile delivery capability. Event 23 should read a generic verified capability hook when that event is implemented. It must remain fully playable through air delivery when Event 32 is absent.

## Delivery force losses

If suitable delivery aircraft, fuel, airbases, or range are lost:

- Operational strike options hide or become blocked with a clear tooltip.
- Readiness declines over time.
- Testing may remain possible at a domestic test ground through a verified domestic delivery route.
- Retaliation can remain planned but unavailable until a carrier is restored.
- The player receives a production or recovery route. A free replacement is not granted.

## Command exercises

Command exercises improve Readiness and expose weaknesses in Integrity.

A normal exercise should:

- Consume fuel and air experience or another current verified training resource.
- Require suitable delivery forces.
- Improve Readiness.
- Reveal a possible command incident when Integrity is low.
- Increase foreign suspicion when repeated.
- Have a substantial cooldown.

An emergency exercise during an active crisis should improve immediate release speed but create a larger Integrity cost and foreign alert.

## Safety and authentication program

The player can invest in procedures, locks, technical certification, and redundant communication.

The program should:

- Improve Command Integrity.
- Reduce false-warning and unauthorized-use incidents.
- Reduce the severity of test accidents.
- Increase the time required for first release under Party custody or Scientific veto.
- Improve the chance that a disputed order is safely aborted.
- Support a controlled moratorium.

The program does not need a custom technology tree. It can use decisions, staged idea changes, and current-vanilla research bonuses where appropriate.

## Doctrine reform paths

Each custody doctrine should have one or two later route-specific developments.

### Party custody developments

- Harden the central code chain.
- Create a mobile reserve command if the capital is threatened.
- Risk a decapitation crisis if every release authority remains in one place.

### Military custody developments

- Pre-authorize retaliation under validated enemy nuclear use.
- Establish a second confirmation channel to recover Integrity.
- Risk commander autonomy during Soviet Collapse.

### Scientific safety developments

- Improve test containment and weapon certification.
- Create a formal technical veto against populated targets.
- Risk a political purge or forced override under high Chaos.

### Dispersed command developments

- Improve depot communication and local accounting.
- Create regional reserve commands for survivable retaliation.
- Risk local seizure, missing devices, and conflicting orders.

These developments should upgrade the primary national spirit or change decision behavior. They should not add a new permanent idea for every step.

## Development-phase decision visibility

The main category should expose only the actions that matter now.

A normal secret-arms phase should show no more than five primary actions, such as:

- Expand production.
- Assemble a batch.
- Harden or inspect storage.
- Train delivery crews.
- Prepare or conduct the next test.

When one action starts, its mission replaces the clickable decision until completion or failure.

Targeting, collapse custody, and full exchange actions belong to their own phased surfaces and should not crowd the development list.

## Tuning direction

The following are design anchors, not final constants:

- Readiness and Integrity both use a zero to 100 range.
- A major test, site loss, doctrine reform, or confirmed nuclear strike should move a value enough to cross or approach a threshold.
- Routine maintenance, training, and inspection should move values by smaller but visible amounts.
- A warhead assembly cycle should take several months and scale from controlled reactors and industry.
- A reactor expansion should take long enough to expose the program to war and foreign observation.
- Storage hardening and dispersal should be meaningful logistical commitments.
- The initial 100 bombs should create maintenance pressure, which prevents the baseline grant from functioning as 100 immediately ready strikes.
- No normal decision may spend more than four distinct resource types.
- Command power costs must remain conservative and below the project maximum.
- Political power may support a political decision, but it cannot be the main currency of the arsenal.

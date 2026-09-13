# Decisions, missions, costs, and visibility

## Presentation choice

Event 036 uses one ordinary decision category with a strong static category picture and a compact status header.

The system does not require a separate scripted GUI at specification stage.

The normal category can present the three public states, phased actions, one to three active missions, and a project progress bar when Evolution III activates the program.

A custom window should be considered only if implementation proves that the normal category cannot present the accepted state clearly.

## Status header

The category header shows:

- National Posture
- Convention Standing
- Current Agenda

When a Chaos weapon project is active, Current Agenda shows the selected project, broad phase, progress percentage, and whether the country has contributed.

Tooltips explain:

- what changes each state
- the next relevant deadline
- the main consequence of the current posture
- the country’s current treaty or project eligibility

Do not show raw variables, component ledgers, vote weights, internal progress units, or project candidate lists.

## Visibility budget

A normal phase shows three to five primary actions.

Six visible primary actions is the hard maximum.

One to three missions may be active.

Obsolete actions disappear when their posture, agenda, target, treaty, project, or membership generation becomes invalid.

The category must not become a permanent list of every treaty action.

## Phase A: National posture

This phase is visible when no conference vote or project contribution deadline requires immediate attention.

Possible actions are filtered by current posture.

### Seek Accession

Who sees it: Public Rejection countries that completed the cooling period.

Purpose: begin the 90-day accession mission.

Default costs:

- political power scaled by government stability and convention standing
- temporary public-trust or diplomatic-capacity burden

Success: choose one valid member posture and join the current generation.

Failure: preserve Public Rejection and apply a shorter retry cooldown.

### Revise National Reservation

Who sees it: members whose 365-day posture lock has expired.

Purpose: strengthen, weaken, or repeal a reservation.

Default costs:

- political power
- temporary stability or war-support pressure according to the direction of change

The action opens a bounded follow-up choice.

It must not allow instant stance cycling before an attack.

### Begin Withdrawal

Who sees it: active members outside a locked emergency obligation.

Purpose: begin the 90-day withdrawal mission.

Default costs and consequences:

- political power
- loss of member trust
- temporary diplomatic penalty

Completion removes future rights while preserving history and obligations already incurred.

### Begin Covert Preparation

Who sees it: Public Rejection countries with valid chemical or biological research routes and no active covert program.

Purpose: open hidden preparation decisions.

Default costs:

- political power
- civilian-factory or research burden
- intelligence-exposure risk as a consequence

The decision grants no technology or stockpile.

### End Covert Preparation

Who sees it: covert opponents that have not been publicly exposed.

Purpose: close the hidden program and reduce future discovery risk.

Completed research remains.

Existing evidence remains.

## Phase B: Conference influence

This phase appears during an active negotiation period.

Only actions relevant to the selected agenda are visible.

### Sponsor the Current Agenda

Who sees it: eligible members when no sponsor is locked or when co-sponsorship is allowed.

Default costs:

- political power
- one civilian factory for 60 to 90 days or another agenda-appropriate commitment

Effect: improves sponsor credibility, AI support, and implementation capacity.

It does not add a direct vote to countries that rejected the treaty.

### Build a Ratification Bloc

Who sees it: members compatible with the proposal.

Default costs:

- political power
- diplomatic or stability risk if the campaign fails

Effect: raises support among valid aligned countries through bounded AI modifiers.

The action requires named or array-selected targets and cannot target every country through a repeated visible decision list.

### Demand a Reservation Clause

Who sees it: countries that support the agenda but reject one major provision.

Default costs:

- political power
- reduced treaty benefit if the reservation is accepted

Effect: opens a supported reservation variant.

Do not offer this action when the treaty has no coherent partial form.

### Organize Opposition

Who sees it: public opponents and members rejecting the current proposal.

Default costs:

- political power
- diplomatic relations with the sponsor

Effect: lowers AI support, recruits abstentions or rejections, and can empower the Opposition Leader.

### Offer Protective Assistance

Who sees it: members during protection, retaliation, inspection, or emergency agendas.

Default costs:

- support equipment
- convoys or trains when route access requires them

Effect: improves implementation support and can satisfy a guarantee or assistance obligation.

### Publish Verified Evidence

Who sees it: countries with a valid public evidence package relevant to the agenda.

Default costs:

- political power or intelligence resource supported by the repository
- diplomatic exposure as a consequence

Effect: uses the shared evidence publication route.

It cannot invent or duplicate evidence.

## Phase C: Treaty implementation

This phase appears after a treaty enters force for the country.

Actions are treaty-specific and replace negotiation actions.

### Submit Required Declaration

Purpose: satisfy production, stockpile, laboratory, facility, or delivery declarations.

Requirements: valid treaty and owner-supported facts.

Failure: treaty breach, inspection pressure, or reduced benefits.

The declaration must not reveal hidden data to the player that the game cannot verify.

### Prepare for Inspection

Purpose: complete a 90-day inspection-readiness mission.

Costs can include political power, support equipment, civilian factories, or temporary research disruption.

Success uses only valid evidence and site facts.

### Fulfill Assistance Guarantee

Purpose: send equipment, convoys, intelligence, or other supported aid after a member suffers a CBRN attack.

The mission lasts 60 to 120 days according to distance and route access.

Failure weakens trust and future guarantee support.

### Implement Doctrine Charter

Purpose: move from Isolated Capability to Theater or Strategic Integration.

Requirements include relevant technology, physical capability, protection, and a completed planning mission.

The action should not be a political-power purchase for a free national spirit.

### Invoke Retaliation Guarantee

Purpose: request aid after a valid public CBRN attack.

The action requires an action record naming the country as victim and an active guarantee treaty.

It opens bounded requests to ratifiers.

## Phase D: Chaos weapon project

This phase replaces ordinary conference actions while a project is active.

It exposes at most four contribution decisions:

- Dedicate Industrial Capacity
- Assign Research Teams
- Provide Specialist Equipment
- Host a Research or Testing Facility

The selected provider profile controls costs, requirements, and availability.

Each country has one active contribution mission at a time.

Contribution decisions disappear during pause, completion, cancellation, invalid membership, or cooldown.

## Mission catalog

| Mission | Normal duration | Success | Failure |
| --- | ---: | --- | --- |
| Accession Review | 90 days | Adopt selected member posture | Remain opponent and receive retry cooldown |
| Withdrawal Notice | 90 days | Leave convention and update registries | Withdrawal cancelled if country becomes invalid or chooses to remain |
| Ratification Deadline | 60 to 120 days | Record national treaty response | Default to abstention or posture-safe response |
| Declaration Deadline | 120 days | Preserve full treaty benefit | Breach memory and inspection pressure |
| Inspection Readiness | 90 days | Complete valid inspection path | Refusal or failure consequence according to evidence |
| Assistance Guarantee | 60 to 120 days | Deliver supported aid | Trust loss and possible treaty breach |
| Doctrine Integration | 120 to 180 days | Raise integration state | Preserve prior state and apply planning setback |
| Counter-Convention Campaign | 180 days | Recruit withdrawals or defeat an agenda | Opposition influence loss and cooldown |
| Project Contribution | 90 to 120 days | Pay costs and apply receipt once | No progress and no duplicate refund exploit |
| Restore Program Quorum | 180 days | Resume paused project | Charter repeal or continued pause |

Mission durations are dynamic inside the listed bands.

## Cost design

Each action has no more than four spendable cost types.

Use costs that match the action:

- political power for diplomacy and public policy
- civilian factory commitment for industry and facilities
- support equipment for protection and inspections
- convoys and trains for international movement
- fuel for transport-intensive or testing work
- manpower for staff and facility security
- army, air, or navy experience for doctrine and delivery planning
- temporary research burden for scientific commitment
- stability, war support, public trust, or diplomatic trust as a consequence

Command power costs remain conservative and below the repository limit.

Do not give every action the same political-power cost.

## Dynamic scaling

Costs scale from documented bands. One flat amount is not used.

Relevant factors include:

- economy size
- current war
- member standing
- distance and route access
- stockpile safety reserve
- research capacity
- prior failed attempts
- current project progress
- posture reversal history

The player-facing cost string shows no more than four icon-first entries.

Blocked text identifies the exact missing resource or requirement through concise tooltips.

## Target management

Diplomatic actions that target another country use a selected-target pattern or bounded target pool.

The human player inspects one selected target at a time.

AI evaluates all valid targets through its own visibility route.

Cleanup removes stale targets after annexation, withdrawal, government invalidation, treaty completion, or membership-generation change.

## Exploit controls

Implementation must prevent:

- repeated posture switching before and after use
- duplicate contribution receipts
- contribution progress after cancellation
- withdrawal immediately before a guarantee deadline without consequence
- repeated one-time Condemnation normalization
- free research bonus renewal
- inspection evidence duplication
- project unlocks for non-contributors
- repeated project completion
- agenda sponsorship stacking without cooldown
- target arrays retaining dead countries

## AI equivalence

Every player action that AI countries can use needs a valid AI path.

AI can use decisions, hidden timed effects, weighted event responses, or owner helpers.

A human-facing selected-target interface must not prevent AI from lobbying, contributing, inspecting, withdrawing, or fulfilling guarantees.

# Decision and mission implementation prompt: Event 061

Implement and audit the complete Return to Rearmament decision and mission system from the Event 61 source specification.

Work only inside the Event 61 scope and required shared helper surfaces.

Read Part 2, Part 3, Part 5, Part 7, the lifecycle diagrams, the AI probability scenarios, the localisation handoff, and the decision and mission skill before editing.

## Core presentation contract

Use one ordinary decision category.

Use one public numeric value, Rearmament Readiness from 0 to 100.

Show five qualitative pillars without exposing five additional raw meters.

Keep the visible surface to:

- no more than five primary actions
- no more than one active mission
- no more than three state reopening targets

Do not build a separate scripted GUI.

Use a static category picture and normal decision mechanics.

## Readiness contract

Recalculate from actual state:

- Event 61 converted capacity restored
- current economy law
- current conscription law
- contracts and defence institutions
- War Support and material preparation

Clamp the result.

Meaningful rearmament requires Readiness 50 and at least one factory or law structural proof.

The Evolution III last-chance test requires Readiness 60, two distinct action families, and one factory or law family.

Actions do not add arbitrary raw points. They change structures that the calculation reads.

## Category phases

Implement these phases and keep obsolete actions hidden:

1. immediate transition
2. industrial revival
3. mobilisation restoration
4. evolution response
5. extreme-law recovery

The current mission can temporarily replace weak ordinary actions.

The category closes only when no ledger, law target, reconversion spirit, mission, extreme law, or deferred settlement remains.

## Normal decisions

Implement:

- Restart Arms Contracts
- Reopen State Arms Plants
- Reconstitute the General Staff
- Make the Case for Defence
- Restore Mobilisation Law
- Restore Conscription
- Emergency Rearmament
- Make the Conversion Permanent
- Begin a National Rearmament Program

Use the exact availability, cost direction, duration range, completion recheck, cancellation, AI, and anti-exploit rules from Part 2.

Every state reopening level must consume one current civilian factory and one current positive state ledger unit.

Every law project must recheck current law rank and stored target at completion.

The public defence action needs an inefficient Stability to War Support transaction and a cooldown.

Emergency Rearmament needs a real threat gate, a one-per-cycle guard, and Improvised Rearmament aftermath.

Permanent conversion needs a confirmation with exact ledger and state totals.

## Evolution I mission and decisions

Implement one Inventory Liquidation mission.

During the mission show at most three relevant protection decisions chosen from:

- Army Stores
- Mobile and Armoured Reserves
- Air Reserves
- Logistics Reserves

Do not show a protection action whose family has no eligible positive surplus.

Implement one civilian disposition choice with a complete base result:

- Central Reconstruction
- Civilian Auctions

The mission resolves from current stockpile state at the deadline.

Repeated Event 61 cycles merge into the one mission and raise bounded pressure.

## Evolution II mission and decisions

Implement one Mustering Out mission.

Response decisions:

- Retain Essential Cadres
- Mark Border Formations Essential
- Accelerate Mustering Out

Border protection requires a named threatened area or verified direct threat.

Accelerated demobilization must show the approximate additional risk and reduce Readiness.

A defensive war normally reduces involuntary disband to zero.

The mission must never select unsafe unit families.

## Evolution III settlement and recovery

Implement one National Defence Settlement mission.

At start, grant immediate exemption only to countries already at Readiness 50 with meaningful structural proof.

Other countries can qualify by reaching Readiness 60 and completing the required two action families.

Direct war danger creates a bounded deferral and later postwar settlement.

Implement voluntary Permanent Peace with a clear irreversible confirmation.

Implement extreme-law recovery:

- Re-establish a Defence Ministry
- Reopen the National Arsenal
- Restore the Service Registry
- Emergency National Defence

The first three projects must be possible without army experience or recruitable manpower.

Provide a difficult ledger-free minimum-arsenal fallback.

## Costs

Use the universal cost framework.

Use varied, relevant costs:

- political power
- civilian factory commitment
- army experience
- Stability
- time
- valid thresholds such as War Support

At most four spendable cost types per action.

Most actions should use two or three.

Every cost needs visible text, a texticon where required, AI affordability, cancellation policy, and cleanup.

Do not use political power as the only recurring cost.

## Dynamic targeting

State target list:

- current owner and controller
- positive ledger
- positive civilian factory level
- valid building conversion
- priority by ledger size, core status, damage, supply connection, and safety

Human list cap: three.

AI can score the full valid pool but remains subject to project caps.

Rebuild stale targets after ownership or control change.

## Mission integrity

Every mission needs:

- start event or decision
- visible deadline
- success or automatic resolution
- cancellation and invalidation rules
- cleanup
- AI plan
- save and reload persistence
- repeat-cycle merge behavior
- Event Logs or history connection where relevant

Do not use decorative missions that merely wait while all effects are predetermined.

## AI

Apply the stance logic from Part 4.

Use probability-tool evidence for every `ai_will_do` and weighted choice.

Hard block:

- emergency actions without threat
- voluntary Permanent Peace during danger
- stale state targets
- duplicate law restoration
- unaffordable project commitments
- protection of a family with no eligible loss

## Required audit

After implementation, spawn `chaosx_decision_mission_auditor` with `fork_context=false`.

The audit must review:

- category clutter
- phase progression
- exact costs
- cancellation and refunds
- dynamic targets
- mission deadlines
- repeat merge
- AI usability
- cleanup after annexation, occupation, law change, war change, and event resolution
- save and reload
- exploit resistance

Resolve every finding before completion or record a real blocker.

## Completion report

Provide a table with:

| Decision or mission | Implemented | Cost validated | AI validated | Cleanup validated | Save reload | Notes |
| --- | --- | --- | --- | --- | --- | --- |

Include exact files, identifiers, probability evidence paths, and unresolved engine limits.

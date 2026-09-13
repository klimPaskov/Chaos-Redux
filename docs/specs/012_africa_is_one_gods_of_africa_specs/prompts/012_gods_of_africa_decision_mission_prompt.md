# Decision and mission implementation prompt

Audit and implement the Gods of Africa decision layer under Event `012` using the accepted full specification.

## Participant surface

Create one participant category with:

- Gods of Africa Strength meter
- per-country Wrath of the Gods meter
- one active demand mission
- phased actions for fulfill, substitute, extension, refusal, and permanent defiance
- voluntary aid only during a real African need
- defiant defensive preparation
- rare reconciliation

Respect these limits:

- exactly two public values
- one ordinary active demand
- three to five primary actions per phase
- six absolute maximum
- one to three active missions
- no more than four spendable cost types per action
- compact icon-first cost text
- exact blocked reasons and valid texticons

Every demand contract must freeze family, amount, deadline, substitute set, extension state, payment progress, sequence ID, and system generation. Save and reload must not reroll any of them.

## Africa-side surface

Create one African-unifier category with:

- Strength
- doctrine
- current need priority
- grouped reports
- selected-target participant flow
- leniency
- priority offender
- protection at real African cost
- pardon
- bounded escalation

Use the selected-target pattern. Human selection must not control AI evaluation.

## Mission quality

Use auto-completing objectives for state transfer, war ending, access, or another condition the engine can prove automatically.

Material transfer decisions must debit once at click time and credit Africa once.

Use varied deadlines from the accepted bands. Do not give every mission the same duration.

## Defiance

Permanent defiance must:

- stop ordinary demands
- set a high Wrath floor
- close normal Favored eligibility
- preserve punishment and hostility
- replace demand actions with relevant threat-response decisions
- require a confirmation window

Reconciliation must be costly, rare, and unable to erase prior-defiance history.

## Audit

After implementation, run `chaosx_decision_mission_auditor` with exact category and decision IDs.

Audit:

- cost validity
- tooltip clarity
- target validity
- AI action path
- active mission cap
- stale contract prevention
- no repeated extension
- no substitute reroll
- no voluntary-aid farming
- no stale selected target
- war, annexation, settlement, and system-end cleanup

Every weighted decision requires the separate probability-audit cycle.

Return a handoff listing files, categories, decisions, missions, helper calls, localisation keys, before and after behavior, meaningful validation, and remaining blockers.

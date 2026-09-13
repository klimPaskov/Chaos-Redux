# Event 050 runtime ledger contract

This is a design contract for the scripted-system architect. It names required information and ownership without prescribing final source identifiers.

## One ledger per active target

Every active crisis needs a stable sequence identity so concurrent crises cannot overwrite one another.

| Data group | Required contents | Cleanup rule |
| --- | --- | --- |
| Identity | Sequence ID, target, firing ID, start date | Remove after final history and aftermath handoff |
| Pressure | Current value, stage, previous value, trend, threshold receipts | Clear for this target only |
| Duration | Planned end, extension count, review date, low-pressure confirmations | Clear scheduled state |
| Justification | Reason family and relevant actors or states | Retain only summary memory when useful |
| Coalition | Convenor, core members, partners, neutrals, role states | Remove only this crisis membership |
| Dependence | Internal profile and major exposure family | Recompute or clear, never expose as a second meter |
| Responses | Active projects, routes, concessions, defiance, seizure preparation | Close, refund, convert, or persist according to action contract |
| Evolutions | Whether evolved rules apply to this crisis | Clear crisis receipt while preserving global evolution state |
| Reports | One-shot threshold and outcome markers | Clear after history summary is safe |
| Achievements | Crisis-scoped counters and disqualifiers | Commit final result, then clear transient counters |
| Resolution | Outcome family, winner or settlement actor, aftermath state | Persist only the intended aftermath |

## Coalition member state

One country may hold a different role in each crisis. Membership cannot rely on one unscoped country flag when Evolution II is active.

Minimum member facts:

- crisis sequence
- country
- current role
- practical contribution band
- commitment state
- public or covert trade state
- fatigue state
- concession demand state
- secondary-sanction state
- last meaningful choice date

## Active-crisis registry

The runtime needs a bounded registry of active crisis sequence IDs and target scopes.

Requirements:

- hard cap of three active crises at Evolution II
- immediate removal after cleanup
- no whole-world daily scan
- review pulses iterate the registered set
- invalid target recovery runs before ordinary review outcomes
- one crisis failure cannot stall the rest

## Transaction order

1. validate target and available registry slot
2. reserve sequence identity
3. select justification
4. build coalition roles
5. calculate opening Pressure
6. classify hidden dependence
7. set duration and first review
8. apply opening effects once
9. show relevant reports and decisions
10. register history and evolution context where required

If a required stage fails before opening effects, the transaction must roll back the reserved ledger and queue no delayed work.

## Review order

1. confirm target and convenor validity
2. resolve pending human or AI choices
3. update routes and concessions
4. update coalition roles and fatigue
5. recalculate Pressure movement
6. update economic stage effects
7. test resolution
8. schedule the next review

## Cleanup order

1. lock the ledger against new actions
2. cancel or resolve active missions
3. remove target and participant crisis effects
4. clear selected targets and route scopes
5. remove this crisis from temporary cooperation networks
6. record resolution summary
7. preserve valid durable obligations and investments
8. remove sequence state from the active registry
9. restore future target eligibility

## Shared-system boundaries

| System | Event 50 can request or read | Event 50 must not own |
| --- | --- | --- |
| Event system | Classification, history, repeatable handling, evolution logging | Global pacing implementation |
| Dynamic classifiers | Civilian and special-country eligibility | Shared actor registry lifecycle |
| Condemnation | Public tier or source-supported status | Hidden evidence or condemnation decay |
| Famine | Valid route and food-security interaction | Food values, deaths, relief ledger |
| Migration | Valid later displacement adapters | Cohorts and movement transactions |
| Deaths | Generic consequences from owner systems | Direct embargo death ticks |
| War | Resource ultimatum or war-goal handoff | Casualties, annexation, peace logic |
| Native embargo | Additive enforcement when available | Baseline event functionality |

# Ordinary missile preparation

This subsystem implements the four ordinary preparation routes inside the one static-picture Missile Command category.
Event 32 remains incomplete as a whole; source behavior and outstanding engine/probability evidence are separate.

## Selection and commitment

The human flow is country → objective family → profile → exact state → preparation → launch or abort.
Country and state pages contain at most three native targeted rows, plus previous, next, and exit/back controls.
The two objective families contain the six accepted target profiles: logistics, industrial, air/coastal, command, counterforce, and broad strategic.
A profile without an eligible controlled state is unavailable.
Explicit selection actions build the session cache; there is no periodic whole-world scanner or dedicated GUI.
Reopening country selection refreshes the current-enemy pool.

The human's pending state is revalidated and copied into the receipt without automatic retargeting.
AI ordinary preflight evaluates the shared country pool and preserves the best-scored state.
Random fallback runs only when scoring returns no state; explicit human states and locked profiles do not enter the fallback ladder.
Retaliation and rogue receivers retain their frozen target exceptions.
Friendly-controlled states are excluded; an enemy-controlled state owned by the actor may be targeted.
The optional `missiles_requested_launch_site` normal scope pointer is validated as a state; a country or undefined FROM is never passed into state predicates.
An invalid explicit launch-site request is rejected instead of silently replaced.

Counterforce locks its target profile before the strategic default.
Its state must contain a real Event 32 launch/custody site, rocket site, reactor, nuclear facility, chemical facility, or biological facility, with more than 50% civilian intelligence over its controller.
Radar alone is not proof of a launch or CBRN facility.
Logistics scores supply hubs above capped railway-level contributions, industry reads actual building levels, and counterforce adds capacity and subtracts damage.
These are source ranking rules, not validated campaign probabilities.

## One paid transaction

| Route | Command power | Fuel | Support equipment | Missile escrow |
| --- | ---: | ---: | ---: | ---: |
| Precision | 8 | 250 | 40 | 1 |
| Strategic | 15 | 450 | 80 | 2 |
| Saturation | 25 | 700 | 140 | 4 |
| Counterforce | 15 | 450 | 40 | 2 |

A selected enabled special payload adds one missile through shared tuning.
Physical special-payload reservation still requires its separate completed custody audit; this table does not assert that surface is complete.
The inline row has three ordinary cost types; its full tooltip adds the fourth Operational Reserve amount with the registered texticon.
Each amount has independent affordability coloring.

`032_missiles_preparation_cost_triggers.txt` owns inclusive read-only affordability.
Availability, the custom cost trigger, and the final effect call the same route predicate.
Readers are `command_power`, `fuel_k`, and `num_equipment@support_equipment`.
The missile check reads live constants and the selected enabled payload, never a display cache.
The regression verifies special total constants equal base cost plus surcharge.
Disabled Special Warheads retains adoption/selection history but new ordinary orders select conventional payload and its base cost; an already-frozen special receipt invalidates rather than silently downgrading.

The final effect checks affordability, runs preflight, and debits command/fuel/support only after an accepted receipt.
Only that branch activates the mission and sets a timed route cooldown.
The original 70/120/120/120-day lengths use success-only flags, avoiding native cooldown consumption on a rejected click.
An unaccepted preflight spends no fees and activates no mission or preparation cooldown.
Accepted preparation spends its fees; a later uncommitted abort returns missile escrow, not those already-spent fees.

## Native mission lifecycle

Each of the four nonselectable native missions is explicitly activated after accepted preflight.
Its available gate uses the current receipt's due date and validity, and its completion effect calls `missiles_complete_preparation`.
Completion exposes the launch action but never commits an ordinary launch automatically.
Cancellation validates the existing receipt, not the gate for starting another operation.

The native duration definition uses a one-day file-local anchor.
`missiles_activate_preparation_mission` adds calculated preparation duration minus that anchor plus one grace day through literal meta expansion of documented `add_days_mission_timeout`.
The timer therefore expires one day after the receipt's due date, avoiding same-day completion/timeout ordering dependence.
No undocumented activate_mission duration object or extra queued receiver is used.
Native timer behavior still needs engine evidence; arithmetic is not runtime proof.

Readiness and commitment share live receipt validation.
Every participating site must exist, remain controlled/launchable, retain this operation ID and its positive unchanged allocation, and retain enough physical capacity for that allocation.
Projected shares are checked before missile escrow is debited; rejection aborts any uncommitted escrow before cleanup.
After reservation, free site custody uses only capacity left by the matching operation allocation.
Available missiles outside that physical projection remain in the national unallocated reserve; they are not credited twice.
Losing a participating site refunds the order and settles that site's assigned missiles before the outer loss transaction reads its unchanged free-stock receipt.
Custody is redistributed only after capture, scuttling, damage or isolation has finished.
The participating-site array cannot be empty.
Ordinary readiness/control minima are 50/40, precision readiness is at least 60, and saturation preflight requires at least two sites and capacity six.
Target, objective, evolution gates, payload custody, and missile escrow must remain valid.

Failure records save the failed operation ID and reason before abort/cleanup remove live scopes.
An unread failure appears as the category's context line until another preparation is accepted, preserving the last-failure history.
Cleanup removes all four native timers without executing their effects, preventing stale timers from aborting successor receipts.
It clears pending state/profile and returns the retained enemy to objective selection.
Survey, construction, repair, recovery, verification, and network-restoration cancellation clear only their own pending work, never an unrelated launch receipt.
Launch uses `missiles_operation_can_be_committed`, not any unrelated launchable site.

## APIs and assets

`missiles_can_afford_preparation`: COUNTRY-scoped read-only trigger; reads five fresh unscoped temporary quotes initialized by the four route wrappers, and returns a boolean.
The wrapper constants populate command, fuel-k, support, base missile, and special missile quotes before the shared check.
`missiles_choose_target_profile`: COUNTRY effect; reads the normal accepted-enum request set by one of six literal profile wrappers, then builds the state cache without payment.
Six `missiles_selected_enemy_has_*_target` COUNTRY triggers validate their literal state predicates.
`missiles_activate_preparation_mission`: COUNTRY effect; reads the active receipt type and selects one of four literal mission IDs, activating/synchronizing only an accepted receipt.
`missiles_cancel_preparation`: COUNTRY effect; records reason, aborts, and cleans only an uncommitted active receipt.

The category has three main values and one phase-dependent context, not nine simultaneous status fields.
Selection/navigation reuse `GFX_decision_032_missiles_select_missile_target`; tactical/strategic families use their precision/strategic decision sprites; counterforce uses its counterforce sprite.
Missions use `GFX_mission_032_missiles_strike_preparation`, and reserve uses `GFX_032_missiles_operational_reserve_texticon`.
These are existing same-family assets in `interface/032_missiles.gfx`; this repair adds no pixels, asset families, or sprite identifiers.

## Validation and remaining work

The source suite checks nested accepted payment, exact affordability boundaries, success-only cooldowns, due-date readiness, timer arithmetic for 10–45 days, live receipt gates, failure-before-cleanup order, counterforce locking, explicit state retention, typed site input, disabled-track fallback, and scored-best protection.
It rejects undocumented named-argument helper calls and checks projected/retained site shares and non-operation cleanup isolation.
Its page-coverage model is not native decision-refresh execution.
Independent mission, localization, and matching probability handoffs require parent review.
Full Event 32 acceptance, all probability scenarios, physical multi-site allocation, special payload reservation, dynamic evolution pacing, retaliation chain bounds, and user-owned live gameplay evidence remain required.

## Future plans

Finish the accepted custody, payload, pacing, and retaliation contracts before adding operation families.
Later campaign telemetry can tune scores without weakening exact-state, receipt, resource, or bounded-selector guarantees.

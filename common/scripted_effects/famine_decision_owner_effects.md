# Famine decision-owner effects

These effects support existing famine decisions and their narrowly bounded migration seam. The Famine decision file remains responsible for start conditions, payment, paid-receipt consumption, and the original decision outcomes.

`famine_decision_prove_evacuation_route` is a COUNTRY-scope bridge to `migration_decision_prove_route_contract`. It reuses the existing positive route proof without creating a destination, movement request, cohort, population change, fee, or fallback.

`famine_select_safe_food_reserve_donor` is a STATE-scope deterministic selector. It scans only physical neighboring states, retains the same-owner/controller, route infrastructure, hazard, and crisis exclusions, and selects the eligible state with the greatest existing reserve. It writes its result and selected donor scope for the original reserve-transfer caller; it does not manufacture stock.

`famine_clear_stale_paid_decision_receipts` is a STATE-scope cleanup called from the existing bounded Famine registration and state-control-change owners. It enumerates only the ten Famine action receipt families. It clears a paid flag, payer, and (for the four relief-contract actions) that same receipt's saved contract-generation and donor fields only when the payer is absent, invalid, or no longer controls the selected state. It preserves a valid payer's funded continuation after the famine phase or route problem recovers, does not refund, and does not call generic cohort or relief-contract cleanup.

Delayed removal and cancellation paths in `common/decisions/famine_decisions.txt` consume only their own flag and payer. The three relief-delivery decisions and invitation first snapshot the separate exact-contract work guard, then consume only their own saved receipt metadata. A stale or replaced contract therefore cannot create free delivery, cannot clear another action's live contract, and cannot permanently block a new activation. The existing Famine evacuation measured-zero-origin refund is still reached under the payer-and-selected-state guard even when its later route/cohort proof fails.

## Explicit action context

Scope-sensitive bodies have one `_in_context` implementation reading the mandatory unscoped temporary COUNTRY pointer `humanitarian_action_actor` and STATE pointer `humanitarian_action_target`.
The original helper name is a compatibility wrapper initializing those inputs from ROOT and FROM before a bare `= yes` call when no explicit context is proven.
A caller that supplies an explicit envelope also initializes temporary `humanitarian_action_context_proven = 1`, so nested legacy wrappers retain that exact actor and target.
Panel gates initialize the actor from their country context and the target from the exact selected state, and an immediate country event establishes the actor as ROOT for deep owner helpers.
These helpers accept no named arguments, have no implicit scope defaults, and publish no additional gameplay output beyond their documented owner body.
These adapters do not change tuning or create independent transaction owners.
See [the shared action lifecycle](../scripted_effects/humanitarian_gui_action_effects.md) for caller, pending, and cleanup contracts.

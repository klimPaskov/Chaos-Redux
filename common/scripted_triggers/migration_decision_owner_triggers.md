# Migration decision-owner triggers

These guards consume migration-owned issue, cohort, policy, and reception-capacity contracts.

`migration_pending_reception_issue_is_valid` is country-scoped and requires an exact valid evacuation offer, not a relief-only offer.
An offer can expose migration response controls only when the receiver already has a migration problem phase or repeated incidents, or the exact live amount offered meets the existing material trapped-population threshold.
A large but unrelated origin pressure total is not the amount that this receiver is asked to admit.
A tiny positive pending row, a quiet food observation, and an initialized registry do not reveal a dormant category.
`migration_decision_reveal_threshold_is_met` and the category visibility consume that same bounded predicate without recursive phase or problem-trigger calls.
The predicate changes presentation and response eligibility only; it does not create a cohort, grant services or capacity, accept a route, move people, or record deaths.

`migration_decision_exact_hosted_cohort_is_valid` is state-scoped and requires one aligned positive live row whose persisted host is the acting state as reflected by the core reconciler's state counters. It fails closed on stale, ambiguous, or missing selectors.

`migration_decision_reception_host_is_valid` is country-scoped and requires a valid current capacity revision, a positive load, and remaining effective people capacity; actions that admit more people use it. `migration_decision_reception_load_is_valid` keeps the same revision proof while allowing an overloaded host, so every action that relieves the burden (Close the Border, Enforce the Closure, Distribute Arrivals, Permit Transit, Local Integration, Help Families Return, Force Repatriation) stays available when the host is over capacity. `migration_decision_reception_state_load_is_valid` is its state-scoped companion over the exact hosted cohort. Those host actions also refuse a state whose own people are being evacuated (`migration_evacuation_prepared`), so one state's people are never moved by two actions at once.

`migration_reception_has_room_for_evacuation` (COUNTRY) holds while the country hosts nobody or its measured load is at or below capacity; it rejects only an overloaded positive-load host, and fails closed when a positive load has no capacity value. Vulnerable, worker, administration, and famine evacuation use it. `migration_state_needs_organized_evacuation` (STATE) holds for active displacement whose flight pressure or trapped population has reached the sustained-issue threshold.

`migration_decision_reception_capacity_exhausted_is_valid` derives the AI warning from the current valid effective-capacity comparison and does not consume the orphan exhausted flag.

`migration_decision_reception_exposure_receipt_is_valid` binds Hungry, Not Contagious to one durable cohort, origin state, host state, generation, transaction, and arrival-time outbreak exposure receipt. Current infection, a policy choice, or an unrelated cohort cannot satisfy it.

`migration_decision_famine_evacuation_country_is_available` and `migration_decision_famine_evacuation_state_is_available` are the narrow migration-owned availability seams used by the famine category's evacuation action. They expose only whether the country's reception network still has room (`migration_reception_has_room_for_evacuation`) and whether the state is valid and not already being evacuated; famine separately proves its own active food-security cause. The famine decision never reads migration reception, preparation, displacement, cohort, or mission ledgers directly.

`migration_reception_policy_is_humanitarian_open` exposes one positive migration-owned policy fact to neutral corridor and famine-relief consumers without allowing them to read the underlying migration policy variable. `migration_state_has_active_persecution` and `migration_destination_native_hazards_are_safe` similarly expose the positive persecution override and the bounded persecution/bombing destination-safety fact.

The departure and reception policy guards validate the two internal policy dimensions and expose role-correct outbound/admission predicates. The displayed Border Policy remains a derived compatibility value.

`migration_decision_forced_return_destination_is_valid` and `migration_decision_voluntary_return_destination_is_valid` resolve the exact persisted historical origin without requiring ROOT to own or control it. They require a valid current capacity revision and destination policy; voluntary return additionally requires admission willingness.

## Legacy decision start and receipt guards

The following COUNTRY-scope hidden Boolean helpers are decision-owner preflights. Each rechecks its original visible/available/target conditions, selected-state control by ROOT, and the exact current inclusive fee profile before the matching `complete_effect` body can write policy, services, receipts, transfers, reports, or phase state. Open departure routes, restrict departure and controlled medical reception are country-wide decisions without a selected state, so their preflights and `available` blocks never read `FROM`; they recheck only the country conditions and the fee.

| Start trigger | Decision |
|---|---|
| `migration_open_departure_routes_can_start` | `migration_open_departure_routes` |
| `migration_restrict_departure_can_start` | `migration_restrict_departure` |
| `migration_close_border_can_start` | `migration_close_border` |
| `migration_prepare_evacuation_can_start` | `migration_prepare_evacuation` |
| `migration_evacuate_vulnerable_can_start` | `migration_evacuate_vulnerable` |
| `migration_evacuate_workers_can_start` | `migration_evacuate_workers` |
| `migration_negotiate_corridor_can_start` | `migration_negotiate_corridor` |
| `migration_controlled_medical_reception_can_start` | `migration_controlled_medical_reception` |
| `migration_distribute_arrivals_can_start` | `migration_distribute_arrivals` |
| `migration_transit_only_can_start` | `migration_transit_only` |
| `migration_enforce_closure_can_start` | `migration_enforce_closure` |
| `migration_local_integration_can_start` | `migration_local_integration` |
| `migration_third_country_resettlement_can_start` | `migration_third_country_resettlement` |
| `migration_voluntary_return_can_start` | `migration_voluntary_return` |
| `migration_forced_repatriation_can_start` | `migration_forced_repatriation` |

The four decisions whose full gameplay remains in `complete_effect`—open departure routes, restrict departure, controlled medical reception, and local integration—use the start preflight and one complete fee debit but do not create a delayed paid-action receipt. Local integration then runs the whole-cohort settlement documented in `common/scripted_effects/migration_integration_effects.md`.

`migration_local_integration_host_can_settle` is STATE-scoped on the integration host with ROOT as the integrating country. It requires ROOT to own and control the host, and both the state reception load and the owner's national reception load to cover the hosted group (`migration_state_live_cohort_amount`). Local integration uses it in `visible`, `available`, `target_trigger` and its start preflight, so the fee is never charged for a settlement that the owner-ledger debit would reject, such as a hosted group in an occupied state that ROOT controls but does not own.

The state-targeted upfront paid continuations use `<decision>_cost_paid` as a state flag and `<decision>_cost_payer` as a state-scoped country pointer. Their receipt guards are `migration_<decision>_cost_receipt_is_valid`, except corridor negotiation, which uses `migration_negotiate_corridor_cost_pending_is_valid` for its unpaid deferred request boundary. A valid receipt requires the exact selected state, the recorded payer to exist and equal callback ROOT, and that payer to remain the current controller. Each `remove_effect` consumes its matching flag before the entire existing continuation; it never rechecks already-spent stock.

`migration_negotiate_corridor` remains deferred-payment: `complete_effect` records only its own state-local pending flag/payer when the entire start and cost preflight passes. Its removal rechecks that pending receipt and the fresh full cost before preparation/submission, then rechecks immediately before the existing successful-offer debit. It does not use a paid flag and does not charge a rejected setup.

`migration_clear_stale_paid_decision_receipts` is STATE-scoped and enumerates only migration-owned paid/pending fields. It clears a receipt only when its payer is missing, invalid, or no longer controls this exact state. It does not clear another action/state/payer receipt, erase still-controlled funded work when the issue phase recovers, or invoke generic cohort/route cleanup.

Every delayed `remove_effect` consumes the exact state/payer receipt before entering its existing continuation. Receipt ownership does not add new route, cohort, phase, or movement-success gates around the measured-zero-origin refund paths (famine evacuation, vulnerable/worker evacuation, voluntary return, and forced repatriation). Their original route execution and zero-debit test still decide whether the original refund occurs; a valid paid actor can therefore resolve that outcome when the later movement preflight fails. Cancellation clears only that action's receipt for the matching recorded payer, then runs the action's existing cancellation cleanup without refunding or cancelling another action's work.

Corridor negotiation is the exception to upfront paid receipts. Its pending contract is private to the selected state and recorded requester; the pending remove requires a current owner callback, unchanged original action requirements, and a fresh full inclusive fee before preparation/submission. Only a newly submitted valid offer reaches the single final pre-debit check. If that final check fails, the exact just-created offer is cleared through the existing corridor owner cleanup; a failed setup is never charged. Cancellation clears only the matching pending requester receipt.

When a delayed receipt guard fails at removal because the selected state is no longer valid or controlled, a fallback branch still consumes that action's own paid flag and payer (or the negotiation's pending flag and payer) when the recorded payer is callback ROOT; it runs no continuation and grants no refund.

The decision `available` blocks keep private receipt flags inside `hidden_trigger`. Player-facing requirements that rely on hidden scripted triggers are wrapped in `custom_trigger_tooltip` blocks with plain keys in `localisation/english/migration_l_english.yml`, shared where the requirement is the same: `migration_reception_load_tt`, `migration_reception_state_host_tt` and `migration_free_mission_slot_tt`, plus one target, policy or mission key per action.

Prepare Evacuation publishes `migration_evacuation_prepared` after its matching paid state work expires.
Vulnerable and worker evacuation require that state-local preparation and spare national reception room.
The existing transfer and cancellation owners retain their preparation-flag cleanup; receipt, route and cohort checks remain with the exact movement owner.

## Published reads for other systems

`migration_state_has_recent_local_integration` is STATE-scoped and true for `constant:migration_decision_timing.local_integration_labor_days` days after a successful Local Integration settlement in that state, through the timed state flag `migration_recent_local_integration` set in the settlement branch of `migration_local_integration`.
It is the only migration fact that Event 34 Industrial Boom reads: an integrated cohort in an Industrial Region lowers that boom's output pressure because the works gain settled labour.
Migration keeps cohorts, reception load and Deaths, and readers move no population.

## Physical transport and local issue guards

Every start revalidates the selected state’s live pressure or measured migration obligations through `migration_state_has_real_migration_issue`, and uses its action-owned cost bundle from `migration_decision_cost_triggers.txt`.
The bundle combines original equipment requirements with the inclusive fuel and conditional-convoy quote; payment must return `migration_transport_payment_result = one` before any equipment debit, work marker or action effect.
Prepare Evacuation uses a state-local unprepared check and publishes preparation for that state at expiry.
The restored evacuation lanes require that preparation and retain the current not-overloaded-host seam.
Worker support stock is a non-consumed prerequisite tuned in `migration_decision_threshold.worker_support_stock`.
Saved transport quantities remain on the original payer until the action’s matching refund or completion consumes them.

## Explicit action context

Scope-sensitive bodies have one `_in_context` implementation reading the mandatory unscoped temporary COUNTRY pointer `humanitarian_action_actor` and STATE pointer `humanitarian_action_target`.
The original helper name is a compatibility wrapper initializing those inputs from ROOT and FROM before a bare `= yes` call when no explicit context is proven.
A caller that supplies an explicit envelope also initializes temporary `humanitarian_action_context_proven = 1`, so nested legacy wrappers retain that exact actor and target.
Panel gates initialize the actor from their country context and the target from the exact selected state, and an immediate country event establishes the actor as ROOT for deep owner helpers.
These helpers accept no named arguments, have no implicit scope defaults, and publish no additional gameplay output beyond their documented owner body.
These adapters do not change tuning or create independent transaction owners.
See [the shared action lifecycle](../scripted_effects/humanitarian_gui_action_effects.md) for caller, pending, and cleanup contracts.

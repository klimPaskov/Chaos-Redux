# Migration owner adapters

This file documents `migration_adapter_effects.txt`. These helpers accept only exact cohort and route facts from migration owners and keep food pressure entirely outside the migration surface.

Migration adapters never initialize or change famine pressure, food stage, reserves, or famine mortality. The exact population transfer owner remains the only owner that debits an origin, accounts route deaths, and credits measured survivors.

## Helper map

| Helper | Scope and required inputs | Output and side effects | Owner call sites and status |
| --- | --- | --- | --- |
| `migration_consume_famine_food_safety` | State scope; bounded destination or registered migration/reception state. | Requests the famine-owned projection and accepts it only through `famine_to_migration_food_safety_is_valid`; it writes no famine state. | Migration registered-state maintenance, reception-capacity candidates, and adjacent destination prepasses. |
| `migration_record_current_state_cohort_custody_exact` | State scope; explicit `migration_cohort_custody_id_request` equal to the unambiguous current cohort, valid aligned migration ledgers, internment/forced-labor action, whole-row living amount, route proof, actor proof and target, site proof, transaction proof, generation, revision, and request identity. | Resolves the explicit row and forwards its current whole-row amount to the strict receipt; returns temporary `migration_current_state_custody_result`. It never changes a cohort, population, route, reception, or food ledger. | The Camp owner stages and re-resolves the exact live row, current host, actor, site/action, generation, revision, and dated request in `camp_rework_commit_exact_cohort_custody`, then consumes the migration-owned result. |
| `migration_apply_related_state_deaths_exact` | State scope; positive not-yet-applied forced-displacement request, explicit cohort ID, route proof, actor proof/target, generation, revision, request identity, and valid state. | Calls the exact state population-loss primitive once and returns temporary `migration_related_deaths_applied`; it never accepts route deaths already measured by an exact transfer. | API-only until a migration owner supplies a separate physical-death transaction. |
| `migration_apply_forced_displacement_deaths_exact` | Migration-owned exact death request with forced-displacement reason. | Delegates to the migration direct-death receipt; it never creates a route or food pressure. | API-only. |
| `migration_record_cohort_custody_action_exact` | State scope; explicit cohort ID, action, positive whole-row amount, transaction/route/actor/site proofs, actor target, aligned arrays, current host, live status, generation, revision, and request identity. | Resolves exactly one row, saves the persisted row owner as `migration_cohort_custody_owner`, and forwards one idempotent evidence receipt to the migration achievement owner. It clears one-shot request/proof fields and performs no population or Deaths mutation. | Called only after a concrete exact internment or labor-assignment owner action. No current owner supplies every required fact. |
| `migration_validate_condemnation_receipt_exact` | Country scope with explicit migration state and actor targets; positive cohort ID and people amount; route, actor, cause, generation, revision, and request identity proof. | Sets only temporary `migration_condemnation_valid`. | Shared by migration-owned condemnation wrappers; forced movement now supplies the exact transaction, cohort, origin-state, actor-target, and dated receipt bundle. |
| `migration_condemn_deportation` | Exact cohort/people/route/actor condemnation receipt. | Adds the existing Condemnation source with `migration_condemnation_gain.deportation`; no food pressure or transfer. | `migration_forced_movement_effects.txt`, `migration_execute_forced_transfer_exact`; caller supplies proof only inside the valid positive transaction branch. |
| `migration_condemn_forced_return` | Exact cohort/people/route/actor forced-return receipt. | Adds the existing Condemnation source with `migration_condemnation_gain.forced_return`; no food pressure or transfer. | Called through `migration_record_exact_decision_condemnation` only after the forced-repatriation transfer finalizes with a positive origin debit and surviving cohort. |
| `migration_condemn_violent_pushback` | Exact cohort/people/route/actor route-death or hostile pushback receipt. | Adds the existing Condemnation source with `migration_condemnation_gain.violent_pushback`; no second Deaths or population mutation. | Called through `migration_record_exact_decision_condemnation` only after violent border enforcement finalizes an exact positive transfer. |
| `migration_record_exact_decision_condemnation` | Origin-state scope after a finalized hosted transfer; explicit forced-return or violent-pushback context, exact origin debit, cohort ID, destination target, country actor, transfer generation, and dated request. | Builds the strict condemnation receipt and dispatches the matching migration wrapper. It never repeats population loss or Deaths logging. | `migration_decisions.txt`, exact successful branches of `migration_enforce_closure` and `migration_forced_repatriation`. |

## Custody proof and idempotence

The current live registry must be aligned across every touched migration array. The requested ID is scanned globally and must occur exactly once; a state, country, site type, quota, pressure amount, or death amount cannot resolve it.

The row host must equal the current state, the persisted row owner must be a valid country, the status must be `active`, `destination_bound`, or `destination_bound_unsafe`, and the owner-provided living amount must equal the current whole-row amount.

`migration_cohort_custody_route_proven` is mandatory even when the row is already destination-bound. It represents the owner’s exact route/current-host receipt and cannot be synthesized from a destination flag.

The helper rejects partial cohorts because the current aligned registry has no split operation. A future partial-custody design must split a child row first and receipt that child as a whole row.

The exact achievement recorders are migration-owned interfaces and must receive the renamed migration request fields. Until the achievement owner exposes those names, the adapter is intentionally blocked rather than calling a neutral compatibility alias.

## Movement boundary

No generic migration flight adapter is created in this narrow split because the current caller census contains no safe new movement producer. A future external hazard owner must call a migration-only movement API with source state, destination or border route, positive live cohort amount, route/transport/safety proof, actor proof, generation, revision, and request identity.

If one hazard has both food and movement consequences, it must call the famine adapter and migration movement adapter as two independent receipts with separate amounts, causes, generations, revisions, and proof fields. This file must never gain an apply-food/apply-flight contract.

## Flight request contract

`migration_apply_flight_request` in `migration_core_effects.txt` remains the sole migration owner for flight pressure, state flight population, incident creation, active registration, decision refresh, and the optional accepted-request ledger.

Famine submits a stage-bound desired amount through `migration_accept_famine_survivor_request`. That migration-owned helper validates the cohort registry, reconciles the state selector, calculates the protected floor and conservative maximum reservation from migration ledgers, caps the desired amount to remaining live population, and then calls `migration_apply_flight_request` only for a material accepted request.

When the optional generation is positive, the migration owner alone writes `migration_flight_request_accepted_total` and `migration_flight_request_generation`, then clears the temporary request fields. It returns `migration_famine_survivor_accepted_amount` and a result receipt; famine retains only its own stage and accepted-request bookkeeping and never reads or writes migration reservation ledgers directly.

## Cleanup and ownership

The custody receipt uses only a short-lived `migration_cohort_custody_owner` event target. It does not create a global target, recurring scan, transfer, population mutation, or food state.

The migration owner clears temporary request/proof fields on both accepted and rejected custody attempts. Durable achievement evidence is not cleared when live rows are cleaned, transferred, released, or annexed.

The migration direct-death receipt is not a route-death substitute. Route deaths remain movement-owned. Movement is not death.

## Unsupported owner seams

Camp, Gulag, genocide, Event 5, Event 6, Event 14, Event 15, Event 21, Event 28, Event 33, Event 50, Event 95, generic war/peace, and generic scenario dispatch lack one or more exact cohort, people, route, destination, transport, safety, actor, or replay facts at their currently inspected callbacks. The forced-transfer condemnation path is the bounded exception because its valid transaction branch already owns those facts.

No movement call is fabricated at a country release, state-control change, event root, cluster queue, modifier application, or country-level reassessment.

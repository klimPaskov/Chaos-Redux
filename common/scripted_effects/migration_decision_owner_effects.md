# Migration decision-owner effects

The new-origin evacuation caller declares `migration_cohort_record_result` as invalid and `migration_cohort_id_result` as zero before recording the displaced group.
Those caller-owned temporary outputs remain available for the subsequent presentation and destination setup.

Decision callbacks themselves declare every scalar output they consume before the owner helper call, including forwarded cohort identity/result, atomic transfer result, physical debit/credit/deaths/finalization/projection results, resolved cohort fields, route safety, history preflight, medical reception, and evacuation finalization.
An initialization inside the returning owner helper does not establish storage in the outer decision callback.
These defaults are invalid results, zero amounts, unknown source, and no status, with existing request inputs preserved.
The measured origin debit remains visible to the callback's existing refund guard, and a successful movement retains its mission/arrival proof after return.

`migration_decision_prove_route_contract` is the positive route adapter for ordinary decision transfers. It requires the saved destination, source/destination state validity, adjacency, infrastructure and transport/border proofs, current control, war separation, safe destination hazards, valid reception capacity, and reception admission policy. It never treats the absent `civilian_transfer_route_unsafe` flag as proof.

`migration_decision_prove_exact_return_route_contract` is the separate return adapter. It proves only exact historical-origin identity, adjacent physical route, control, infrastructure, current destination capacity, and a valid destination policy. It intentionally does not infer a safe origin for forced return; route-death predicates remain explicit inputs to the exact transfer.

`migration_decision_preflight_destination_history` is a read-only ordinary distribution/transit guard. It rejects a destination already visited by the exact cohort, requires the initialized positive history registry plus aligned history/live arrays and at least one matching history receipt, and fails closed on missing, invalid, or misaligned history. Multiple valid receipts for one cohort are expected because the ledger is append-only; the guard checks every matching receipt for the exact destination. It does not initialize or repair migrated saves, so a rejected A->B->A attempt has no global-history mutation. Terminal voluntary/forced return, local integration, and third-country resettlement remain explicit exceptions.

`migration_decision_set_policy` adapts validated external subsystem policy requests to the authoritative native national laws, then reconciles the compatibility variables.
It retains the result and request-reset contract for Event 003.
Paid migration operations and reception-service preparation consume current law and never call this setter.
The native-law mapping and publication contract is documented in [national_policy_effects.md](national_policy_effects.md).

`migration_decision_record_medical_reception_receipt` records the durable exact arrival exposure receipt only after the transfer projection, destination bind, reception delta, and history result are valid and the persisted origin is outbreak-exposed at arrival. It does not create a route, cohort, ledger, or service by itself.

`migration_set_mission_evacuation_deadline`, `migration_set_mission_reception_observation_deadline` and `migration_set_mission_return_deadline` are STATE-scoped and take no inputs. Each sets its mission deadline the matching `migration_mission_timing` day count after today, converting the days to date units through the shared `chaosx_convert_days_to_date_offset` helper because a stored date counts one game hour as 0.00001.

None of these adapters selects destinations, mutates flight/trapped ledgers, unregisters a positive row, or replaces the exact transfer core. The core remains responsible for measured origin debit, survivor credit, route deaths, cohort host/history, generation, and paired-obligation reconciliation.

`migration_clear_stale_paid_decision_receipts` is STATE-scoped and is called by the existing bounded registration and state-control-change owners. It enumerates the twelve upfront delayed action receipts plus `migration_negotiate_corridor_cost_pending`; it clears only missing/invalid payers or payers that no longer control this state. It never refunds, removes a still-controlled funded continuation because the issue phase recovered, or invokes generic route/cohort cleanup.

The delayed migration decisions clear their own paid flag and payer before the full existing removal body, but the receipt guard adds no new route, cohort, phase, or movement-success condition. In particular, the original five measured-zero-origin refund branches remain reachable on a route/cohort failure when the paid actor still controls the selected state. Matching `cancel_effect` paths clear only their own receipt, then preserve the original action-specific cleanup; cancellation does not refund the upfront fee or clear another action's receipt.

Corridor negotiation is deferred-payment. Its pending request is stored on the selected origin state with the exact requester country scope and is consumed before preparation. The existing `humanitarian_corridor_prepare_contract` and `humanitarian_corridor_submit_offer` owners remain authoritative. A fee is debited exactly once only after a valid new offer submission and a fresh full affordability check; an unpaid just-created offer is removed only on that same successful-submission/final-fee-failure branch. Rejected or invalid setup is not charged.

## Explicit action context

Scope-sensitive bodies have one `_in_context` implementation reading the mandatory unscoped temporary COUNTRY pointer `humanitarian_action_actor` and STATE pointer `humanitarian_action_target`.
The original helper name is a compatibility wrapper initializing those inputs from ROOT and FROM before a bare `= yes` call when no explicit context is proven.
A caller that supplies an explicit envelope also initializes temporary `humanitarian_action_context_proven = 1`, so nested legacy wrappers retain that exact actor and target.
Panel gates initialize the actor from their country context and the target from the exact selected state, and an immediate country event establishes the actor as ROOT for deep owner helpers.
These helpers accept no named arguments, have no implicit scope defaults, and publish no additional gameplay output beyond their documented owner body.
These adapters do not change tuning or create independent transaction owners.
See [the shared action lifecycle](../scripted_effects/humanitarian_gui_action_effects.md) for caller, pending, and cleanup contracts.

`migration_decision_finalize_organized_evacuation_in_context` publishes the destination state after its preparation, mission, and corridor-success tails settle from a valid transfer receipt.

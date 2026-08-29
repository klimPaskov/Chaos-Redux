# Migration decision-owner effects

`migration_decision_prove_route_contract` is the positive route adapter for ordinary decision transfers. It requires the saved destination, source/destination state validity, adjacency, infrastructure and transport/border proofs, current control, war separation, safe destination hazards, valid reception capacity, and reception admission policy. It never treats the absent `civilian_transfer_route_unsafe` flag as proof.

`migration_decision_prove_exact_return_route_contract` is the separate return adapter. It proves only exact historical-origin identity, adjacent physical route, control, infrastructure, current destination capacity, and a valid destination policy. It intentionally does not infer a safe origin for forced return; route-death predicates remain explicit inputs to the exact transfer.

`migration_decision_preflight_destination_history` is a read-only ordinary distribution/transit guard. It rejects a destination already visited by the exact cohort, requires the initialized positive history registry plus aligned history/live arrays and at least one matching history receipt, and fails closed on missing, invalid, or misaligned history. Multiple valid receipts for one cohort are expected because the ledger is append-only; the guard checks every matching receipt for the exact destination. It does not initialize or repair migrated saves, so a rejected A->B->A attempt has no global-history mutation. Terminal voluntary/forced return, local integration, and third-country resettlement remain explicit exceptions.

`migration_decision_set_policy` persists separate departure and reception policies, derives the one displayed Border Policy compatibility value, and routes the public core policy setter through one result guard.

`migration_decision_record_medical_reception_receipt` records the durable exact arrival exposure receipt only after the transfer projection, destination bind, reception delta, and history result are valid and the persisted origin is outbreak-exposed at arrival. It does not create a route, cohort, ledger, or service by itself.

None of these adapters selects destinations, mutates flight/trapped ledgers, unregisters a positive row, or replaces the exact transfer core. The core remains responsible for measured origin debit, survivor credit, route deaths, cohort host/history, generation, and paired-obligation reconciliation.

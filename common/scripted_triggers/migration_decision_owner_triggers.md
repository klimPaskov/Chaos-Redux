# Migration decision-owner triggers

These guards consume migration-owned issue, cohort, policy, and reception-capacity contracts.

`migration_pending_reception_issue_is_valid` is country-scoped and requires an exact valid evacuation offer, not a relief-only offer.
An offer can expose migration response controls only when the receiver already has a migration problem phase or repeated incidents, or the exact live amount offered meets the existing material trapped-population threshold.
A large but unrelated origin pressure total is not the amount that this receiver is asked to admit.
A tiny positive pending row, a quiet food observation, and an initialized registry do not reveal a dormant category.
`migration_decision_reveal_threshold_is_met` and the category visibility consume that same bounded predicate without recursive phase or problem-trigger calls.
The predicate changes presentation and response eligibility only; it does not create a cohort, grant services or capacity, accept a route, move people, or record deaths.

`migration_decision_exact_hosted_cohort_is_valid` is state-scoped and requires one aligned positive live row whose persisted host is the acting state as reflected by the core reconciler's state counters. It fails closed on stale, ambiguous, or missing selectors.

`migration_decision_reception_host_is_valid` is country-scoped and requires a valid current capacity revision, a positive load, and remaining effective people capacity. `migration_decision_reception_load_is_valid` keeps the same revision proof while allowing an overloaded host so an outbound relief lane can reduce the measured load.

`migration_decision_reception_state_host_is_valid` composes the country service and exact state cohort/load contracts. `migration_decision_reception_capacity_exhausted_is_valid` derives the AI warning from the current valid effective-capacity comparison and does not consume the orphan exhausted flag.

`migration_decision_reception_exposure_receipt_is_valid` binds Hungry, Not Contagious to one durable cohort, origin state, host state, generation, transaction, and arrival-time outbreak exposure receipt. Current infection, a policy choice, or an unrelated cohort cannot satisfy it.

`migration_decision_famine_evacuation_country_is_available` and `migration_decision_famine_evacuation_state_is_available` are the narrow migration-owned availability seams used by the famine category's evacuation action. They expose only whether the country has no positive reception load and whether the state is valid and not already prepared; famine separately proves its own active food-security cause. The famine decision never reads migration reception, preparation, displacement, cohort, or mission ledgers directly.

`migration_reception_policy_is_humanitarian_open` exposes one positive migration-owned policy fact to neutral corridor and famine-relief consumers without allowing them to read the underlying migration policy variable. `migration_state_has_active_persecution` and `migration_destination_native_hazards_are_safe` similarly expose the positive persecution override and the bounded persecution/bombing destination-safety fact.

The departure and reception policy guards validate the two internal policy dimensions and expose role-correct outbound/admission predicates. The displayed Border Policy remains a derived compatibility value.

`migration_decision_forced_return_destination_is_valid` and `migration_decision_voluntary_return_destination_is_valid` resolve the exact persisted historical origin without requiring ROOT to own or control it. They require a valid current capacity revision and destination policy; voluntary return additionally requires admission willingness.

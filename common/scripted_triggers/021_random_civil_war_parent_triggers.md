# Event 021 parent trigger contracts

This file documents the parent trigger layer in `021_random_civil_war_parent_triggers.txt`.

The triggers are pure eligibility and state checks used by the parent transaction, the bounded scheduler, the Event 006 adapter, the scenario adapter, and cleanup.

`event021_parent_country_is_opening_candidate` requires a normal human country, no terminal state, no active or reserved Event 021 transaction, a valid route, a valid remnant, and an available generation and capacity slot. The route predicate is pre-commit safe: proven route evidence is sufficient before an ordinary opposition actor exists, while the opening-plan validator remains responsible for final leader, force, capital, and package proof.

`event021_parent_same_tag_candidate` and `event021_parent_same_tag_active` gate the unsafe one-state and proven all-island same-tag contest lifecycle. The route planner publishes the all-island receipt only when every owned state is an island and live same-tag evidence exists.

`event021_parent_event6_dormant_candidate`, `event021_parent_event6_package_complete`, and `event021_parent_event6_existing_actor` distinguish a dormant complete Event 006 package from an already recognized human actor.

`event021_parent_viable_anchor_state` requires a controlled, supplied, populated, non-occupied, connected, and nonterminal state that can support the opening anchor.

`event021_parent_sponsor_candidate` limits Evolution II exposure to eligible neighboring normal human countries.

`event021_parent_scheduler_country_due` checks the persistent review date without writing state.

`event021_parent_internal_war_ended`, `event021_parent_territorial_war_ended`, and `event021_parent_reconstruction_due` prevent premature settlement or cleanup. An active package-owned additional Event 006 front remains unresolved until its actor no longer has a war with the host.
Each opponent-pointer branch requires a distinct existing country with the same nonmissing crisis ID.
A host pointer rebound to the successor itself is not a resolved enemy, and a cached global actor from another crisis cannot terminate this one.
These pointer guards do not replace the separate requirement to adopt and resolve every surviving front after succession.

`event021_parent_multifront_setup_available` normally requires active Evolution I and its explicit disabled-evolution gate. A manual High or Maximum scenario may use the same bounded multi-front setup during its immediate launch transaction without mutating the evolution record.

`event021_parent_secondary_front_candidate` requires the multi-front setup gate, an active opposition side, a viable connected state, enough live route receipts for another belligerent, and one unreserved ordinary route.

`event021_parent_event6_secondary_front_candidate` admits one additional complete Event 006 package only for an ordinary government host with a preserved remnant and open crisis, front, and theater capacity.

`event021_parent_has_unreserved_secondary_route` admits only a live ideological, legal, regional, or command receipt that has not already produced a belligerent. Event 006 and same-tag routes remain owned by their dedicated adapters.

`event021_parent_scenario_country_eligible`, `event021_parent_scenario_type_route_valid`, and `event021_parent_scenario_requires_same_tag` validate the selected SCN-018 profile without creating temporary actors. Unsafe one-state and all-island topology forces the same-tag route for every scenario type.

`event021_parent_scenario_anchor_state_candidate` and `event021_parent_scenario_capital_state_candidate` exclude ordinary Event 021 reservations, live front states, and confirmation-time scenario reservations. They are consumed by the per-country frozen-plan receipt before any ownership mutation.

`event021_parent_opening_force_valid`, `event021_parent_global_capacity_ready`, and `event021_parent_opening_external_war_valid` protect the force, cap, and achievement-related opening checks. `event021_parent_reserved_critical_launch_valid` is the owner-aware exception that permits only the claimed Critical target to pass capacity validation while the launch lock is held; it requires the same target to remain in the queue, Critical, generation-eligible, and route-valid.

`event021_parent_settlement_terms_valid`, `event021_parent_negotiated_settlement`, and `event021_parent_reconstruction_complete` gate finite postwar transitions.

All actual nonhuman immunity is inherited from the normal-human predicate and its `is_actual_nonhuman_country` exclusion.

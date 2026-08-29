# Migration reception capacity effects

This file owns the sparse, people-unit reception service used by migration and later decision consumers. It does not write civilian factories, population, route geometry, mapmodes, or presentation files.

The `migration_*` identifiers in this file are migration-owned state, registry, service, capacity, and presentation inputs. Shared runtime/state-validity helpers retain their neutral `humanitarian_*` names, while famine food-stage fields and native safety projections are external inputs that must be replaced by versioned owner adapters.

## Public effects

`migration_register_reception_candidate_state` and `migration_unregister_reception_candidate_state` add or remove an explicit state from `global.migration_reception_candidate_states`. Registration is idempotent, sets the state candidate flag, registers the owner country in the existing sparse displacement-country registry, and marks that country dirty.

`migration_set_reception_shelter_service` and `migration_set_reception_medical_service` are narrow state adapters. The caller supplies a positive people-unit request and a positive proof token in the action-local request variables. The accepted amount is stored as a state service capacity, the corresponding proof is persisted, and the state is registered as a candidate. Both request variables are reset with `set_temp_variable`, so a failed or completed call cannot contaminate a later chain.

`migration_clear_reception_shelter_service` and `migration_clear_reception_medical_service` remove one service adapter and dirty only the owning country. Missing or non-positive service proof leaves the candidate unusable and does not invent capacity.

`migration_mark_reception_capacity_dirty` is the public country callback for food, hazard, control, war, peace, policy, and reception changes. `migration_recalculate_reception_capacity` consumes the dirty marker during the existing sparse host pulse and increments `migration_reception_capacity_revision` on every completed recomputation.

## Candidate validity and sparse scheduling

The capacity loop iterates only `global.migration_reception_candidate_states`. It filters each registered state to the dirty country by persisted owner scope. Each candidate first calls `migration_consume_famine_food_safety`, which accepts only a proven current schema with positive generation/revision and bounded projected stage, pressure, transport, governance, and production fields. A candidate must then have projected food stage at or below `constant:migration_capacity.food_safe_stage`, positive population, and both explicit service adapters with positive people-unit capacities. Missing or untracked food facts fail closed. No whole-world scan, random destination, `migration_route_unsafe` proxy, or distant route claim is used.

Native state safety projections are maintained separately by `migration_refresh_native_state_safety_projections` for already registered states. Route weighting consumes the canonical neutral `civilian_transfer_route_damaged` flag, while the external `migration_bombing_active` state-local hazard input remains separate. These are local availability/safety projections only; strategic-bombing attacker identity is unavailable and is never inferred.

## Capacity formula

All quantities are people units after converting `state_population_k` with `constant:migration_capacity.people_per_k`. For every safe candidate, shelter quality is `clamp(shelter_service / state_population, shelter_quality_floor, 1)` and medical quality is `clamp(medical_service / state_population, medical_quality_floor, 1)`. Infrastructure quality is `clamp(building_level@infrastructure / infrastructure_max_level, infrastructure_quality_floor, 1)`. Transport availability is `clamp((max_component - famine_to_migration_transport_component) / max_component, transport_quality_floor, 1)`; this is availability evidence, not proof of an operating route. Governance quality is the analogous normalized inverse of `famine_to_migration_governance_component`.

The current source consumes the versioned `famine_to_migration_food_stage` projection to select food quality using the centralized stable, supply-strain, acute-shortage, famine, and catastrophic values. The famine publisher does not initialize an untracked state: missing famine facts invalidate the projection and the migration consumer fails closed. Administration quality is `clamp((governance_quality + bounded_civilian_factory_throughput) / safe_factor_divisor, governance_quality_floor, 1)`, where throughput is civilian factories divided by `administration_full_civilian_factories` and clamped to one. Civilian factories therefore contribute bounded administration quality only; they are not a flat capacity writer.

The six published quality inputs are food, shelter, infrastructure, transport availability, medical, and administration. Their population-weighted average is divided by `quality_weight_sum`. Supporting outputs expose each normalized component, plus governance, for consumers that need a diagnostic breakdown.

The bounded safe factor is `min(safe_candidate_states / target_safe_state_count, 1) * safe_population / candidate_population`. Gross service is `candidate_population * capacity_population_share * quality_average * safe_factor`, clamped to `candidate_population * capacity_population_share_max`, then multiplied once by country war, aggregate outbreak, aggregate contamination, and bounded reception-load factors. War is applied once per country after the candidate loop. Outbreak and contamination are population-weighted candidate evidence and their penalties are applied once after aggregation; they are never compounded per state. An unsafe registered candidate contributes zero to the safe aggregate; only a registry length/alignment mismatch poisons the recomputation.

`migration_reception_capacity_gross` stores the quality/safe service before war, outbreak, contamination, and load factors. `migration_reception_capacity` stores the effective threshold after those factors; current reception load is not subtracted a second time. Consumers compare exact load against this effective threshold. The service is invalid when there are no safe candidates, the sparse registry is misaligned, or either adapter total is absent. Validity also requires the current capacity schema and a cleared dirty marker, while freshness is exposed by the monotonically incremented `migration_reception_capacity_revision`.

## Consumers and lifecycle

The later decision owner should call the two service adapters with explicit shelter and medical proofs, call `migration_mark_reception_capacity_dirty` after each adjustment or relevant policy/hazard change, and consume `migration_reception_capacity_is_valid` before using capacity as a destination proof. The core reception-delta effect remains the sole mutator for state and country reception load; capacity calculation never edits that ledger.

The primary UI value remains Displacement Load. Reception Capacity, Border Policy, normalized supporting inputs, validity, and revision are supporting projections for the frozen presentation surfaces. This file does not add a GUI or mapmode.

## Known limits

The engine/source surface does not provide a safe generic route-geometry or route-throughput fact for arbitrary distant states. The transport component is therefore deliberately named availability and cannot authorize a movement by itself. Ordinary-bombing actor attribution, persecution attribution, and a generic `route_unsafe` fact remain fail-closed and are parent-owner follow-up work where consumers still reference them.

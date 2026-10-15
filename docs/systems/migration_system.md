# Migration System

Status: implemented; current status, balance arithmetic and evidence limits are in [the 10 October improvement plan](../plans/famine_and_migration_system_plans/improvement_plan_2026-10-10.md).

Reception/departure laws and the migration management window are documented in [National policies](national_policies.md). The laws are country policy; cohorts, obligations, routes and reception capacity remain migration-owned ledgers.

## Ownership

Migration is an independent cohort, route, reception, and settlement mechanic. Its gameplay identifiers, variables, flags, effects, triggers, decisions, missions, localisation, sprites, and CXT fixture use the `migration_*` namespace.

Famine can be one proven cause of movement, and migration can create trapped-population pressure that worsens famine. Neither mechanic owns the other's primary ledger or decision category.

Famine survivor displacement enters through `migration_accept_famine_survivor_request`; migration alone reconciles cohorts, reserves existing obligations, applies the protected population floor, caps the accepted amount, writes flight ledgers, and refreshes its category. Trapped-population food demand travels in the opposite direction through the versioned `migration_to_famine_reception_demand_*` receipt.

When the Famine panel offers organized evacuation, migration-owned availability helpers expose only whether reception and preparation permit the request. Migration then stages the trapped obligation and cohort, runs the exact transfer, and owns mission subject, cohort, deadline, slot, report, and trapped-state cleanup. The famine surface receives only the neutral transaction receipt and never owns migration lifecycle data.

Migration exposes narrow positive triggers for humanitarian-open reception policy, active persecution, and native destination safety. Famine relief and evacuation consumers use those seams rather than reading migration policy or hazard ledgers. Railway damage is a neutral physical projection refreshed independently by both sparse mechanics.

The Migration management panel is available to eligible human players during quiet conditions as well as crises. It provides state inspection and operational actions; individual actions remain gated by local displacement, reception, corridor, cost, cooldown, and pending-work requirements. Opening or refreshing the panel does not initialize migration or register work. Native AI missions retain their existing decision path.

Durable resettled and returned population totals remain available to mapmode, history, documentation, and achievement consumers. They do not keep operational actions eligible after the live migration problem has resolved, and they do not control access to the quiet-accessible panel.

The dedicated `migration_state_map_mode` remains available from campaign start.

`migration_register_initial_incident` is a migration accounting and presentation seam called after a proven new displacement-pressure episode. It records bounded state presentation and selects migration report context only; it does not create an event object, event ID, event-pool entry, event-log row, pacing pulse, random event, or population transaction.

The deleted `events/migration_incidents.txt` file and its incident constants are deliberate. Earlier incident-event and incident-option probability wording is superseded and is not a current implementation requirement.

## Player-facing values

The Migration panel presents four canonical status values:

- Displacement: active people requiring movement, protection, reception, or resolution.
- Reception Capacity: the validated ability to receive and support arrivals.
- Reception Law: the current native reception law.
- Departure Law: the current native departure law.

Cohort IDs, generations, exact transfer proofs, and registry rows remain internal evidence, not player homework.

## Canonical player-facing value count

Migration exposes exactly four canonical panel values: Displacement, Reception Capacity, Reception Law, and Departure Law. Displacement and capacity describe movement pressure and receiving capacity; the two law fields show current national policy. Those law status fields add no separate pressure mechanic.

Destination and reception safety consume the proven, versioned `famine_to_migration_*` food-safety projection. Migration does not initialize famine or read raw famine stage, pressure, transport, governance, production, exposure, or incident fields. Missing or invalid projection facts fail closed.

Internal conceptual components and ledgers, including cohorts, routes, reception load and capacity components, custody and return receipts, generations, revisions, and scheduler state, are implementation evidence rather than additional player-facing mechanics.

Raw variables, flags, temporary values, transaction receipts, and diagnostic tooltip details do not increase the canonical count; mapmode and report context remains contextual presentation.

## Movement lifecycle

Migration supports internal displacement, cross-border flight, organized evacuation, deportation, reception, controlled medical reception, transit, local integration, third-country resettlement, voluntary return, and forced return.

Movement is never a death. Every physical route delegates to the neutral exact transfer primitive, which debits the origin once, records route deaths as a slice of that debit, and credits only surviving people to the destination.

Migration owns cohort identity, current host, historical origin, route role, generation, status, reception load, integration, resettlement, and return state. Exact aligned registries and generation checks prevent stale-host resolution, duplicated cohorts, and transfer cycling.

The live cohort alignment check includes the visit-history ledger, so `migration_initialize_cohort_history` creates the zero history count at runtime start, outside the one-shot guards of `humanitarian_initialize_runtime` and `migration_initialize_runtime`, and again immediately before `migration_record_displaced_cohort` checks alignment.
In a new campaign the first proven flight therefore records cohort 1, and a state or country whose selection is rebuilt from an aligned registry clears both its ambiguity flag and its misalignment flag.
See `common/scripted_effects/migration_cohort_history_effects.md`.

A successful Hunger Lines launch (Event 014, scenario SCN-010) commits a famine stage in each live Event 014 node state; the famine stage transition submits the ordinary famine survivor flight through `migration_accept_famine_survivor_request`, so the scenario adds no separate migration request.

Local integration settles one whole hosted cohort without moving anyone.
`migration_settle_integrated_cohort` proves the cohort, its current host, the integrating owner-controller and both reception ledgers, debits the state and national reception load once, writes the row as completed with zero people, and only then credits national integration and the achievement history.
A rejected settlement changes nothing, and a settled row can never be settled or credited again.
See `common/scripted_effects/migration_integration_effects.md`.

## Prospective reception contract

The accepted first-reception repair is defined in [Part 3](../specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_3_displacement_migration_return.md), [Part 6](../specs/famine_and_migration_system_specs/famine_and_migration_system_spec_part_6_decisions_ai_presentation.md), and the [bounded implementation plan](../plans/famine_and_migration_system_plans/prospective_reception_lifecycle_plan_20261003.md).
The bounded source path is implemented and independently source-audited in [the completion handoff](../plans/famine_and_migration_system_plans/subagent_handoffs/prospective_reception_completion_audit_20261003.md).
Native execution and the required same-scenario probability comparison remain unresolved, so this is not a full-system completion claim.

A real spontaneous request first uses the existing operational internal-first destination search.
Only when that search cannot resolve the request may the sparse origin-state owner rank adjacent preparable foreign hosts, retaining actual food, native transport, ownership, control, relation, actor, and hazard checks.
No missing reception service is represented as capacity or given a capacity weight bonus.
The exact selected front, live origin cohort, and fresh contract generation are persisted in the existing humanitarian corridor and country mirrors.
The source row remains at the origin without a bound destination; a request creates no arrival, population debit, reception load, or death.

The host's existing Open Emergency Reception action prepares only the exact requested state while an offer is pending.
It uses the existing shelter and medical service setters and population-scaled shares, a single centralized three-resource payment, an inclusive affordability predicate, and exact rollback/refund on rejected paid setup.
An unchanged service receipt cannot be charged again as successful preparation.
Once fresh live-cohort and full headroom checks pass, the host may accept the request; the existing sparse spontaneous owner then delegates movement to the exact civilian-transfer transaction.
Acceptance and transfer each revalidate the actual amount, route, capacity, policy, actor, cohort, and generation.
Rejection or expiry preserves the origin obligations and can clear only matching mirrors.

One tiny incoming request does not create a sustained national migration issue. Large or sustained issue facts, or distinct valid incoming evacuation generations counted once in the existing incident count, still drive issue classification and action gates; they do not control quiet access to the management panel.
Preparation and rejection precede acceptance; these are phased uses of existing controls, not an additional category, mission, GUI, or headline value.
The pending-request priority text explains the current choice without calling the people arrivals.

Reception medical-supply costs live in `common/script_constants/migration_reception_preparation_constants.txt`; fuel and convoy fees live in `migration_transport_cost_constants.txt`.
The existing active-country registration and country phase provider share a display-only cost projector for `common/scripted_localisation/migration_reception_preparation_cost_scripted_localisation.txt`; fresh constants, not cached text values, govern affordability and payment.
`localisation/english/migration_l_english.yml` owns the six ready/blocked cost labels and request wording, reusing the existing `£support_equipment_text_icon`, `£GFX_fuel_texticon`, and `£convoy_text_icon` consumers.
The action retains `GFX_migration_decision_open_border`; no new art or sprite consumer is required.

## Paid decision work

The migration actions use the physical transport fee contract in `common/scripted_effects/migration_transport_cost_effects.md`, with their original train, support and security-equipment costs where those actions consume them.
Political power is not charged.
Fuel fees are 5k, 10k or 20k for connected states, doubled for states without a land connection to the payer’s capital, with 5, 10 or 20 convoys for those sea routes.
Airlift relief uses aircraft and fuel rather than sea convoys.
Availability, the native custom-cost branch, resource colors and final payment use the same exact country-payer bundle; display-only quotes are not payment authority.
Immediate actions validate their whole activation before writes, while delayed paid work uses independent action/state/payer receipts before its existing continuation.
Corridor negotiation preserves deferred payment after a successful offer and rechecks its full fee before preparation, submission and debit.
Receipt cleanup touches only its matching or invalid state-local work and does not erase another state, action or valid payer's receipt.
The existing movement refunds require a matching paid action and zero measured origin debit; real physical transfer does not receive a blanket late-failure refund.
Workers' support-equipment prerequisite remains non-spendable, and no fee, cooldown, numeric AI factor, headline value, category, asset or global scheduler is added by this ownership boundary.
Native callback exclusivity, same-payer replay behavior and the mandatory probability comparison remain unresolved evidence gates, not assumed proofs.

## Borders and trapped populations

Closed borders do not erase a cohort. A valid closure creates or maintains trapped population and produces real humanitarian, diplomatic, security, political, reception, and mortality consequences through their respective owners.

Violent pushback and unsafe forced return can create route deaths under `constant:chaos_meter_deaths_reason.forced_displacement`, localized as `From forced displacement`. The exact transfer transaction logs those deaths without applying a second population debit.

## Panel actions and missions

Every action target must have a current local threat, measured displaced or sheltered civilians, or an exact incoming corridor request.
Reception preparation is limited to that state, an adjacent displacement origin, or the requested receiving front; an unrelated national crisis does not expose preparations on arbitrary owned islands.
Famine, proven blockade, active persecution/bombing/disaster/contamination, neighboring established outbreaks, and enemy-controlled front states can create that local need.
War and state-control callbacks and accepted outbreak receipts request bounded neighboring flight through the existing migration owner, with population shares and cooldowns in `migration_pressure_constants.txt`.

The Migration panel provides seventeen operational actions: Prepare Evacuation, Evacuate Vulnerable People, Evacuate Civilians, Evacuate Civil Administrators, Evacuate Workers, Negotiate a Corridor, Accept a Corridor Offer, Reject a Corridor Offer, Open Emergency Reception, Controlled Medical Reception, Distribute Arrivals, Transit Only, Enforce the Closure, Local Integration, Third-Country Resettlement, Voluntary Return, and Forced Repatriation. Departure and reception posture is selected through the native laws in [National policies](national_policies.md).

Preparation reserves the selected state's departure points before general, vulnerable-person, administrative, or worker evacuation can start.
Worker evacuation retains its distinct support-stock prerequisite and heavier train requirement.
All four evacuation actions use the existing exact movement, corridor, population-floor, and reception contracts. They remain available at exactly national capacity and are blocked only when reception is over capacity.
General and administrative evacuation use the standard prepared batch. Prepared vulnerable evacuation moves half the standard organized-evacuation batch. Administrative evacuation moves civil officials in a standard batch and uses the same route and capacity rules. Worker evacuation retains its distinct support-equipment prerequisite and heavier train requirement.
Each action records the player-selected class (`general`, `vulnerable`, `administrative`, or `industrial`) on the exact cohort ID; the system does not infer an age, health, occupation, or household census for the other residents.
A settled industrial workforce remains a sparse state obligation until its signed balance returns to zero; registration does not mark the state as actively displaced. This lets the existing state refresh update production after integration while ordinary cleanup retires the state when the balance clears.
Industrial cohorts carry a signed state workforce balance. The physical origin loses the measured debit and the destination receives only survivors, so route deaths reduce the combined balance once. Transit and return move that balance with the same cohort ID and transfer generation; the previous host loses its contribution, and one movement generation cannot add credit twice. Integration leaves the contribution at the host because the workers remain there as ordinary residents.
The signed workforce share changes local building construction and industrial-complex repair by up to 50%. Factory output uses that share multiplied by the state's industrial-complex and arms-factory levels divided by the current valid controller's `num_of_factories`; dockyard output uses its dockyard levels over the same denominator. The contributions feed `industrial_capacity_factory` and `industrial_capacity_dockyard` on the current producer. Exact transfers, controller changes, and the existing sparse registered-state modifier refresh reweight each state; occupied industry follows the controller and a stored producer receipt removes the previous controller's share on capture or release.
Civil Administrators is an explicit priority class with the standard movement contract; no separate administration or reception bonus is claimed because the source specification defines no distinct effect for it.
No factory or machinery object changes owner or location.
The emerging, active and resolution phases remain presentation for the panel and native missions; they do not lock operational actions. Every action that relieves a host, such as distribution, transit, integration, return, and resettlement, stays available when the host is overloaded, while actions that admit more people need spare capacity.

Migration missions own corridor, evacuation-transport, reception-observation, and safe-return deadlines. Famine missions are never counted in migration mission slots or presented as migration actions.

The AI uses the same availability, route, capacity, safety, policy, and owner-proof gates as the player. Ideology is a bounded weight after validity; persecution, camps, genocide, bombing, occupation conduct, famine, contamination, route danger, and lack of capacity can override ideological affinity.

## Sparse runtime

The runtime processes only registered active migration states and countries through the existing host-only coordinator. Exact on-actions and owner callbacks add or invalidate affected rows. No whole-world daily, weekly, or monthly scan is added.

## Adapters

Migration accepts exact owner-proven pressure and transaction requests from persecution, occupation, camps, gulags, forced labor, genocide, deportation, bombing, nuclear damage, fallout, outbreaks, natural disasters, war, peace, relevant events, clusters, and scenarios.

An adapter must prove state, people, actor, cause, route or custody context, generation, revision, and request ownership as required by the receiving contract. An event flag, generic severity, or ideology is not a substitute for those facts.

Ordinary wars create refugees through the hostile-capture adapter in `common/scripted_effects/humanitarian_capture_effects.txt`.
When an enemy that is not the owner, a faction partner or in a subject relationship with it captures a state, `on_state_control_changed` requests war flight pressure equal to the live population times a bounded share, scaled by the occupier's conduct and ruling ideology within a fixed range and capped above the protected origin floor.
A minimum state size, a minimum request and a per-state cooldown keep the registry bounded, and liberation by the owner adds no flight.
This covers wars created by event owners, such as civil wars and collapse wars, without editing their files.
When a special Chaos Redux power that runs no civilian system (the walking dead, a rat swarm, ZIN, Death, a revolutionary or terror command) takes a state, that state leaves both mechanics, so `humanitarian_handle_special_front_capture` sends 2% (4% for a nonhuman captor) of each neighbouring state the former owner still holds into flight instead: people run from the advancing front.

## Management panel and state list

Refreshing the Migration panel rebuilds `migration_panel_states` directly from relevant owned and controlled states, then deduplicates and validates current ownership/control. Relevance includes published movement data and qualifying prepared, mission, corridor, workforce, or pending work, not mere ownership or zero-filled fields. States with trapped civilians appear first; other qualifying states retain native collection order. It does not use `migration_header_states` or `global.migration_active_states` as the panel's list source. A selected row changes the panel's selected state; the separate Show on Map button centres the map on that selection.

The overview shows Displacement, Reception Capacity, Reception Law, and Departure Law. The selected-state view shows trapped, sheltered, and fleeing populations, prepared or active work, and eligible operational actions. Action status comes from the action owner's saved start date, due date, cooldown, and remaining-day values. The active-work meter uses the saved start and due timestamps and displays the exact operation's progress over eleven frames; it does not estimate duration from current tuning or advance the operation.

Final panel renderer evidence is tracked in the [national policy panels implementation report](../plans/famine_and_migration_system_plans/national_policy_panels_implementation.md).

## Assets and mapmode

Migration assets use `migration_*` filenames and sprite identifiers.
Evacuate the Vulnerable, Evacuate Civil Administrators, and Evacuate Workers reuse `GFX_migration_decision_evacuate`; the state and country workforce modifiers reuse `GFX_migration_state_exodus`. The added English keys live in `localisation/english/migration_priority_l_english.yml`; no new sprite or gfx consumer is required. `interface/migration_system.gfx` owns the category, decision, state-modifier, and achievement sprites; `interface/chaosx_texticons.gfx` owns the migration Deaths texticon; `interface/migration_report_pictures.gfx` and `interface/migration_report_header.gui` own the compact migration report art consumer; `interface/mapmodes_interface.gfx` owns the two migration mapmode button states.

The migration mapmode colors lifecycle state and independently marks trapped populations, overcrowding, border status, corridor safety, reception pressure, and flight pressure. It does not read famine relief state.

Its authorized reception-capacity status uses the migration owner's complete read-only validity contract, including the current schema, clean revision, positive real capacity and candidates, and no invalid candidates.
A cached positive capacity token alone cannot label a dirty or invalid reception ledger as valid; the tooltip never recalculates or grants capacity.

Receiving fronts of evacuation corridors carry a private reception intent for their owner or controller: requested after a valid offer, prepared after paid reception preparation, and agreed after consent.
The front keeps one identity-only row per live corridor, so an older agreed passage and a newer pending request at the same front survive each other.
Measured passage and every corridor terminal retire exactly their own row, and a front that changes hands drops the rows of a receiver that lost it.
Intent never carries people, reception load, capacity or route permission, and any real trapped, arrival, hosting or overcrowded role keeps display priority.
Latest-movement labels separate actual transfers, including deportation and civilian flight transfers, from pressure-only causes, which read as pressure.
The API is documented in `common/scripted_effects/migration_reception_front_intent_effects.md` and `common/scripted_triggers/migration_reception_front_intent_triggers.md`.

The current documentation inventory contains 61 declared final DDS outputs across the package: 50 root-manifest assets, seven report images, and four mapmode buttons. Category-asset closure reconciles the famine and migration category consumers, and the parent contact-sheet review accepted every visual family. Live in-game consumer validation remains user-owned.

## CXT fixture

`migration_register_cxt_test_content` registers `chaosx_cxt_extension_migration`.
Its idempotent apply effect requests a capacity refresh; the current owner recalculates from real registered food, shelter, and medical receipts rather than granting the legacy requested aggregate amount.
This registration does not supply missing services, create a cohort or route, move population, start a famine problem, or apply mortality.
Starting and exercising a real reception case still needs its exact owner inputs; registration alone is not a capacity or execution proof.

## Event 149 retirement

Event 149 `Immigrations` is retired and absorbed into this system. No replacement event ID, event object, event-pool registration, flat population drain, event-log row, or event-pacing pulse is permitted, and state/accounting pulses are not event pacing.

## Validation limits

Source review and bounded script checks cover the current behaviour; live campaign timing, native rendering and AI frequencies are user-run checks. The current record is section 6 of [the 10 October improvement plan](../plans/famine_and_migration_system_plans/improvement_plan_2026-10-10.md).

## Future extensions

Future depth should prefer richer exact route ownership, bilateral reception agreements, and cohort-specific political consequences over new headline meters. Any extension must preserve sparse scheduling, exact transfer conservation, shared validity for human and AI choices, and the separate migration namespace.

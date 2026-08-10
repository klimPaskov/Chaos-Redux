# Event 016 Kruger State decision layer

## Purpose

This system turns the Kruger State focus tree into paid, target-aware gameplay. The focus tree grants permission and route identity; decisions, missions, native raids, intelligence operations, and exact completion receipts perform the work. The layer is deliberately event-driven. It adds no daily, weekly, or monthly country iteration.

The implementation is split across eight `common/decisions/016_brilliant_scientist_kruger_state_*.txt` files, ten categories, one subsystem constants file, one trigger file, one effect file, one event file, one localisation file, and a narrow set of canonical biological-warfare hooks.

## Activation and shared costs

`brilliant_scientist_krg_initialize_decision_layer` establishes the decision variables, the live project-force package, and the Laboratory Guard template cap. The cap is always restored to 12; decisions never bypass it by spawning free divisions.

Shared script constants centralize political power, command power, equipment, fuel, manpower, factory occupation, duration, capacity, output, temporal, and AI values. Material checks use a gate one unit below the exact debit so the visible availability test and the paid effect agree.

Factory workloads use four matching capacity bands: 1, 2, 4, or 6 available civilian factories for light, standard, heavy, or strategic commitments. Every factory-occupying decision reaches its matching gate either through the material-cost helper or through a direct capacity requirement when it uses the separate foreign-operation cost. Timed country flags receive shared script-constant durations through temporary variables when their `days` field does not parse `constant:` tokens directly.

Repeated production is separated into two steps:

1. The decision pays equipment, fuel, manpower, factories, and any temporal charge when it begins.
2. The completion helper grants only the physical output and writes the exact cycle or batch receipt.

Cancelled or invalidated work does not refund a sunk material or temporal commitment.

When Kruger is actively directing the state, the seven project-force batch decisions use the operational project stage as their direct access point. Clone, robot, paleogenetic, xenobiological, exotic, portal, and temporal production still pays the same concrete batch cost, occupies factories, respects family suspension, damage, dismantling, and capacity history, and keeps its normal output receipt, but it does not require a second facility, staffing, terminal, safety-board, or temporal-debt preparation step. The six bespoke equipment families keep their project-stage and failure-state locks in the production interface while active Kruger bypasses separate facility and terminal gates.

Each batch timer rechecks the decision layer and its matching operational project family before completion. If the project is suspended, damaged, dismantled, or the Kruger decision layer closes during the timer, the batch cancels without granting its physical output.

The first four foundation reports, the existing clone, machine, xenobiological, temporal, and singularity route dossiers, and the five foreign-integration reports keep the country's history readable through two presentation clauses. `GetBrilliantScientistKrgOriginClause` identifies the charter, rebellion, enclave, or takeover that created the state, while `GetBrilliantScientistKrgPortfolioClause` selects the highest-priority active project-force family reconstructed from the carried ledger. Both clauses now appear on the foundation, route, and foreign-integration reports, so later political choices retain the state's formation memory as well as its surviving institution. These clauses add no stage, equipment, unit, technology, meter, or route effect.

## Stale-target contract

All 29 timed state-target decisions have a `cancel_trigger` that rechecks the exact target family while the timer is active. A state that changes owner, controller, facility role, construction eligibility, crisis status, or diplomatic eligibility cannot complete through a stale `FROM` scope. The former-host settlement also cancels when its saved country target disappears.

This contract is intentionally fail-closed: cancellation grants no completion receipt and does not redirect work to another state or country.

## Clone identity pressure

The fourth completed clone growth cycle can open `brilliant_scientist_krg_clone_identity_pressure_mission`, but only on the cohort route unlocked by `brilliant_scientist_focus_unlock_clone_identity_pressure_crises`.

The revolt is prevented when all three institutional proofs exist:

- the clone identity register is active;
- the personhood petition has been heard;
- the registry has been repaired.

If pressure has already begun, `brilliant_scientist_krg_reconcile_clone_identity_pressure` provides a paid 30-day mitigation window. An unresolved 90-day mission sets the permanent achievement disqualifier `brilliant_scientist_clone_revolt_ever`, applies stability and war-support losses, and fires `chaosx.brilliant_scientist_krg.11`. Negotiation or suppression can end the immediate confrontation, but neither erases the historical disqualifier.

## Hazardous mission objectives

The Clone and Machine, Foundation, and Portal categories each contain a hazardous mission that now requires one paid in-mission objective before its timer can grant the existing full completion receipt.

| Mission | Owner and evidence | Paid objective | Full timeout outcome |
| --- | --- | --- | --- |
| `brilliant_scientist_krg_clone_drift_review_mission` | Clone and Machine category; an operational, controlled clone-growth site | `brilliant_scientist_krg_quarantine_and_sequence_clone_lineages` consumes the standard material and factory commitment for 60 days | `brilliant_scientist_krg_clone_registry_repaired` and the existing stability gain |
| `brilliant_scientist_krg_rogue_node_containment_mission` | Clone and Machine category; an operational, controlled machine power node | `brilliant_scientist_krg_isolate_rogue_machine_node` consumes the standard material and factory commitment for 60 days | `brilliant_scientist_krg_rogue_nodes_contained` and the existing stability gain |
| `brilliant_scientist_krg_maintenance_audit_mission` | Foundation category; an intact controlled primary laboratory saved as the canonical facility target | `brilliant_scientist_krg_service_primary_facility` consumes the light material and factory commitment for 30 days | `brilliant_scientist_krg_maintenance_audit_completed` and the existing project-force rebuild |
| `brilliant_scientist_krg_transit_breach_closure_mission` | Portal and Temporal category; an operational, controlled transit terminal in the live terminal network | `brilliant_scientist_krg_seal_transit_breach` consumes the standard material and factory commitment for 60 days | `brilliant_scientist_krg_transit_breach_closed` and the existing stability gain |

An objective is visible only while its exact mission is active, and it records one transient completion receipt only if the named operational proof survives its own timer.

At mission timeout, the full outcome requires both that receipt and the same operational proof to remain valid.

Missing the objective or losing the site, node, facility, or terminal is a contained failure: paid costs remain sunk, no full reward is granted, a permanent `*_failed_ever` history receipt is written, and the mission is unavailable for the centrally tuned 90-day retry cooldown.

The four permanent full-completion receipts also hide their respective starting decisions, preventing stability, force-rebuild, or completion farming.

World-end and category shutdown cancellation clears the active mission and every transient objective flag without granting a success or failure result.

Ministry consolidation and replacement remain deliberately passive in this tranche.

## Machine succession

`brilliant_scientist_krg_install_continuity_network_government` is a real 120-day head-of-state transfer, not a focus-completion marker.

The timer continually requires:

- an active, independent Kruger State;
- the machine-ascendancy route and machine population majority;
- the machine command protocol;
- a recognized network partnership or service settlement;
- completed ministry replacement and population transition;
- Warren Kruger to remain present, personally active, personally sovereign, and not already removed from rule;
- no prior machine-network government.

On completion, event `chaosx.brilliant_scientist_krg.22` calls `brilliant_scientist_krg_install_machine_continuity_network`. The effect recruits `KRG_continuity_network`, writes `brilliant_scientist_continuity_machine` on both the country and the biological Kruger, removes Kruger's active and sovereign character flags, retires him, promotes the network as the despotism leader, and sets:

- `brilliant_scientist_machine_network_rule_active`;
- `brilliant_scientist_biological_kruger_removed_from_rule`.

Existing major enemies are marked once during succession. `on_war_relation_added` marks later major enemies only when the network government is one of the belligerents. `on_capitulation` sets `brilliant_scientist_machine_major_war_victory` only when an independent, active machine-network Kruger State is the actual victor and the capitulated major owns the durable opponent marker. Peace clears an unused marker. No periodic scan is involved.

## Route command staff

Each command-lifecycle effect now writes one route-active flag and invokes the hidden roster handoff `chaosx.brilliant_scientist_krg.90`. The event recruits and activates one fixed institutional character for the selected route, guarded by a permanent recruited flag so repeat focus or decision calls cannot create duplicates:

- `KRG_general_staff_office` supports `KRG_a_general_staff_for_the_state` with a high-command advisor and corps commander.
- `KRG_machine_command_node` supports `KRG_write_the_machine_command_protocol` and the machine command choice with a high-command advisor and corps commander.
- `KRG_clone_officer_corps` supports the clone officer command branch with a high-command advisor and corps commander.
- `KRG_project_command_council` supports `KRG_a_council_of_project_commanders` and its project-force coordination branch with a high-command advisor and corps commander.

The four candidates also carry unpromoted despotism country-leader roles for later route presentation, but none can displace Doctor Warren Kruger or `KRG_continuity_network` during recruitment. Re-selecting a command lifecycle deactivates the prior route advisor, clears its active route flag, and reactivates the matching fixed character if it was already recruited. All four roles reuse existing generic scientist GFX; no new portrait or model asset is required.

## Temporal rescue state machine

`brilliant_scientist_krg_issue_bounded_future_warning` targets either the threatened capital or an intact singularity facility in an owned and controlled state adjacent to enemy-held ground. The target is revalidated for the full 30-day preparation.

On a valid commitment:

1. The one-use warning target ID is bound through the canonical temporal API.
2. Synchronization and temporal debt are charged through `brilliant_scientist_commit_bounded_temporal_action`.
3. The exact state is saved as `brilliant_scientist_krg_temporal_rescue_target`, classified as capital or singularity site, fortified, and placed under a 60-day survival mission.
4. The country records `brilliant_scientist_temporal_capital_or_singularity_danger_recorded` and `brilliant_scientist_temporal_debt_incurred_by_intervention` only after the canonical action commits.

Loss of the exact state, loss of its required facility role, invalid temporal evidence, loss of authority, or civil war fails the chain. Failure clears the bound state/global target and all unfinished rescue receipts. Civil war additionally sets `brilliant_scientist_temporal_civil_war`.

If the same target survives the full window, the system sets `brilliant_scientist_temporal_bounded_intervention_completed` and immediately starts a fresh canonical stabilization through `brilliant_scientist_begin_temporal_stabilization`. A separate supervision mission owns the final `brilliant_scientist_temporal_stabilization_completed` receipt. The target and global event target are explicitly cleared on every terminal path.

Continuity Guard production also uses the canonical temporal commitment contract. Each of its three possible attempts binds a unique target ID, spends synchronization, incurs debt, and consumes an attempt even if the physical batch is later cancelled.

## Focus 088 and offensive biological use

Focus 088 does not invent an agent, payload, reserve, target, or release model. It records the strict governance route that ends with `brilliant_scientist_krg_open_canonical_last_resort_raid_authority`; a living Kruger already supplies release authority for the native raids, so this extra board is not a second mandatory preparation step.

That 90-day authorization requires:

- the Focus 088 unlock and consequence ledger;
- dual-key authority;
- authenticated delivery, audited custody, and compartmentalized network proofs;
- segregated containment logistics;
- a hardened command node and quarantine-ready facility;
- biological weaponization, an exact delivery package, and operational containment;
- a completed ordinary-agent project, a valid staging complex, strategic-use policy, an active war, material cost, and command power.

The canonical authority still governs the strict non-Kruger route and remains visible as a governance receipt. For an active host or Kruger State, a living Kruger makes the four native ordinary-pathogen strategic raids directly usable once their ordinary payload, policy, staging, aircraft, target, and war checks pass. Those canonical systems continue to own exact agent stockpile debits, state selection, preparation duration, exposure and accident risk, lifecycle contamination, deaths, evidence, attribution, Condemnation, retaliation, and treaty consequences. The separate hostile weaponized-zombie operation follows the same Kruger authority shortcut; friendly anti-zombie use remains outside this offensive receipt.

The permanent country flag `brilliant_scientist_offensive_biological_weapon_used` is never set by Focus 088, research, custody, stockpile possession, staging, authorization, preparation, a failed delivery, or an attacker accident. `brilliant_scientist_krg_record_confirmed_offensive_biological_use` is called only at:

- the ordinary biological lifecycle's confirmed attacker scope, alongside `used_bioweapon` and `bio_confirmed_use_history`;
- a hostile successful weaponized-zombie operative release;
- a hostile successful weaponized-zombie strategic strike.

The first valid call writes the Event 016 receipt and refreshes the shared Kruger threat source. Ordinary-agent use therefore follows the canonical attribution threshold; concealed releases are not converted into a fabricated immediate confirmation.

The native payload ledger described above is not yet an Event 016-owned KRG quantity system. The Event 016 country package currently restores biological history, delivery technologies, containment, and authority, while a bounded KRG production, reservation, consumption, transfer, and defeat ledger remains queued under `docs/plans/016_brilliant_scientist_plans/016_krg_biological_stockpile_delivery_addendum.md`. That later tranche must debit or return one Event 016 charge through an idempotent native callback and must preserve the native CBRN outcome owner.

The native raid surface itself is active independently of that queued ledger. Countries may manually launch every ordinary biological, battlefield, captured-facility recovery, hostile weaponized-zombie, friendly weaponized-zombie, and anti-zombie-cure raid whenever the native policy, staging, target, aircraft or formation, and payload checks pass. A living Kruger also bypasses the separate Event 016 authority board and makes the AI prefer those operations; he never auto-launches them or changes their native strength. Portal Warfare from the weaponization stage exposes two raids in the native `brilliant_scientist_raids` category. `brilliant_scientist_portal_facility_raid` targets state factories, reactors, and rocket sites, while `brilliant_scientist_portal_special_project_facility_raid` targets one exact special-project facility. Any country holding the reusable technology and template can prepare either raid with a formation containing at least six Portal Raider battalions and sixty `teleportation_equipment` units. Native reservation, cancellation, expiry, outcome selection, and raid history remain authoritative. Success consumes the assigned formation at origin, reconstructs the standard six-battalion formation in the seized province ready to attack, and transfers one valid target; a critical outcome can transfer a second compatible installation.

Kruger AI no longer waits for a second authority board. The human scientific republic still cannot authorize first use through the native Kruger shortcut. The canonical raid and operation AI continues to perform its own retaliation, safety, target-value, policy, stockpile, staging, aircraft, network, and risk checks afterward.

## Assets and interface wiring

No new art is required for this tranche.

- Decisions reuse registered generic decision sprites.
- The machine government reuses `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_4_machine.dds` through `GFX_portrait_KRG_doctor_warren_kruger_stage_4_machine` in `interface/016_brilliant_scientist.gfx`.
- Route command offices reuse the existing vanilla generic scientist DDS shelf through the stable `GFX_portrait_generic_*` names.
- Canonical biological raids and intelligence operations keep their existing agent, equipment, map, and operation artwork.

If dedicated art is later commissioned, keep decision icons under the Event 016 asset package, register stable sprite names in `interface/016_brilliant_scientist.gfx`, and replace only the generic decision icon references. Do not rename gameplay IDs to match art filenames.

## Future extensions

- Add a player-facing summary of which safety proof still blocks the last-resort authority without weakening the hidden exact gates.
- Give the clone revolt distinct post-crisis reconciliation decisions while preserving `brilliant_scientist_clone_revolt_ever` as immutable history.
- Add a machine-government cabinet presentation that reads the existing succession receipts rather than creating a second government state.
- Add temporal rescue targets for other named crises only after assigning each a unique immutable target ID and exact-state survival contract.

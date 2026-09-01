# Event 016 Wonder-Technology Actions

## Overview

Mature conventional Directorate projects provide paid operational actions in `brilliant_scientist_directorate_category` instead of functioning only as passive national modifiers.

The actions are available only while Doctor Warren Kruger remains the current host scientist, the relevant project stage is complete, the family ledger is healthy, containment and terminal transactions are inactive, and the country can meet the complete material cost.

The actions do not grant project stages, duplicate project history, create a second technology ledger, or bypass the project incident lifecycle.

## Operational sequence

1. A project reaches Weaponization through the existing Theory, Prototype, Deployment, and Weaponization lifecycle.
2. The matching scripted trigger verifies the canonical current host, family stage, family health, terminal state, and concrete resource gates.
3. Selection immediately commits Command Power, support equipment, trucks, fuel, and manpower while the decision timer applies its civilian-factory burden.
4. The removal effect applies the operational outcome only after the preparation or construction timer expires and the project and target remain valid.
5. Cancellation runs one exact refund for the committed Command Power, equipment, fuel, and manpower; factory time already consumed by the cancelled preparation is not restored.
6. Successful removal writes the durable history receipt without repeating the project-stage reward.

## Actions

| Project family | Action | Required stage | Result |
| --- | --- | --- | --- |
| Computation | Launch a Predictive Campaign | Weaponization | Sustains overwhelming planning, intelligence-network growth, decryption, and reinforcement support for ninety days. Computation Deployment also grants one research slot, and the cumulative family ladder reaches the promised research advantage. |
| Electronics | Saturate a Sensor Region | Weaponization | Selects a controlled radar, air-base, or anti-air state as the network anchor and applies overwhelming national detection, interception, mission-efficiency, and anti-air targeting for ninety days. |
| Advanced Materials | Construct State Synthesis Works | Weaponization | Converts one owned industrial core into a permanent synthesis site that produces eight units of aluminium, tungsten, chromium, or rubber. A state can host only one works receipt. |
| Rocketry | Activate the High-Speed Strike Network | Weaponization | Triples air range and greatly improves strategic bombing, air efficiency, and land attack for ninety days. |
| Rocketry | Launch a Long-Range Delivery Strike | Weaponization | Selects an enemy-controlled wartime industrial state, then severely damages its factories, infrastructure, air base, radar, and anti-air installations. Repairs proceed at one quarter of normal speed, and the state cannot be struck again for 180 days. |
| High Energy | Raise the Field Projectors | Weaponization | Sustains extreme national defense, air-superiority support, anti-air targeting, and nuclear output for ninety days. |
| Biomedical | Order Emergency Regeneration | Weaponization | Doubles reinforcement and recovery, nearly eliminates combat-experience loss, and sharply reduces supply demand for ninety days. The operational and weaponized stages also add fifty points each to the shared outbreak surveillance, containment, medical, and biosecurity calculation while the family remains healthy. |
| Biomedical | Order Epidemic Control | Weaponization | Applies major biomedical research, stability, logistics, and reinforcement support for ninety days and immediately restores national stability. |

The existing Advanced Materials plus Rocketry high-speed materials corridor and Electronics plus Teleportation calibration network remain the authoritative paid cross-project actions for those combinations.

## Cross-project consumer map

The portfolio table in the source specification describes gameplay directions rather than fourteen mandatory new decision rows. Each direction has one authoritative concrete consumer so the Directorate does not expose duplicate actions:

| Combination | Authoritative consumer |
| --- | --- |
| Computation plus Robotics | Machine-command protocol, human supervisory keys, power-node assembly, air-gap security, and rogue-node containment in the KRG machine route. |
| Computation plus Temporal Mechanics | Anchor authentication, observer records, bounded rescue, stabilization, continuity, and succession actions in the temporal route. |
| Electronics plus Teleportation | `brilliant_scientist_establish_portal_calibration_network`, its persistent receipt, accident-pressure reduction, and foreign-operation detection score. |
| Advanced Materials plus Rocketry | `brilliant_scientist_prepare_high_speed_materials_trial` and `chaosx.nr16.195`, separating the national qualification archive from Kruger's portable flight envelope. |
| Advanced Materials plus Robotics | Machine power, frame repair, bounded assembly, and machine-force production decisions. |
| Biomedical plus Cloning | Growth sites, bounded maturation cycles, lineage sequencing, medical fabrication, personhood, and population-transition decisions. |
| Cloning plus Paleogenetics | Bounded hatchery cycles, veterinary support, reconstructed-species control, and the corresponding KRG project-force route. |
| Cloning plus Xenobiology | Designed-caste production, medical fabrication, control-mode choice, escape response, and the corresponding KRG project-force route. |
| Robotics plus Xenobiology | The mutually exclusive machine-control doctrine, control centers, synthetic coordination, and escape-response countermeasures. |
| Alien Arms plus High Energy | Strategic-delivery architecture, alien-cohort armament, the exact Singularity component ledger, arming, fail-deadly, disarmament, and terminal paths. |
| Teleportation plus Biological Weapons | Portal-assisted biological deployment is owned by the separate biological-warfare transaction tranche; it must debit its own pathogen payload and never reuse a native-raid reservation. |
| Temporal Mechanics plus Cloning | Clone continuity is one exclusive canonical-Kruger survival route; temporal target-use receipts and debt prevent repeated body recovery. |
| Temporal Mechanics plus Robotics | Machine continuity is one exclusive canonical-Kruger survival route; anchor authentication and temporal debt prevent repeated command restoration. |
| Public Computation plus Independent Teams | Independent-research reconstruction, archive recovery, assistant amnesty, international inspection, and exact-family foreign counter-program decisions. |

The Teleportation plus Biological Weapons row remains owned by the biological-warfare tranche of the final completion contract. It is not represented by a temporary percentage modifier in this tranche.

## Tuning and ownership

Shared costs, duration, output, and AI values live in `common/script_constants/016_brilliant_scientist_technology_action_constants.txt`.

Eligibility lives in `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt`, payment and outcomes live in `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt`, decisions live in `common/decisions/016_brilliant_scientist_technology_actions.txt`, and timed national effects live in `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`.

The strict `has_equipment` and `has_fuel` operators use exclusive gate constants exactly one unit below the displayed payment. Manpower and Command Power use inclusive comparisons so a country with exactly the documented amount can commit the action.

## Icon contract

No new icon identifier is introduced by this surface.

Each decision reuses the original, already registered Event 016 project-stage icon for its owning family:

| Consumer | Sprite identifier | Existing DDS family |
| --- | --- | --- |
| Predictive Campaign | `GFX_decision_brilliant_scientist_project_computational_mathematics_weaponization` | `gfx/interface/decisions/016_brilliant_scientist/projects/` |
| Sensor Saturation | `GFX_decision_brilliant_scientist_project_electronics_guidance_weaponization` | `gfx/interface/decisions/016_brilliant_scientist/projects/` |
| Synthesis Works | `GFX_decision_brilliant_scientist_project_advanced_materials_weaponization` | `gfx/interface/decisions/016_brilliant_scientist/projects/` |
| High-Speed Network and Long-Range Strike | `GFX_decision_brilliant_scientist_project_rocketry_propulsion_weaponization` | `gfx/interface/decisions/016_brilliant_scientist/projects/` |
| Field Projectors | `GFX_decision_brilliant_scientist_project_high_energy_physics_weaponization` | `gfx/interface/decisions/016_brilliant_scientist/projects/` |
| Emergency Regeneration | `GFX_decision_brilliant_scientist_project_biomedical_acceleration_weaponization` | `gfx/interface/decisions/016_brilliant_scientist/projects/` |
| Epidemic Control | `GFX_decision_brilliant_scientist_project_biomedical_acceleration_deployment` | `gfx/interface/decisions/016_brilliant_scientist/projects/` |

Sprite registration remains in the existing Event 016 project GFX files; no unwired filename is reserved.

## Interactions

The action availability triggers consume the same suspended, damaged, dismantled, and stolen family arrays as the project board, so an incident or containment response removes the action without erasing completed history.

The materials synthesis state flag is the permanent state receipt used to prevent duplicate construction.

The long-range strike uses a timed target-state flag rather than a world ledger, so target exclusion is bounded to the selected state and requires no recurring world scan.

The project-stage modifier dispatcher owns the computation research slot. The matching disable and re-enable effects remove or restore it idempotently when the portable project ledger changes country.

The shared biological lifecycle reads `brilliant_scientist_biomedical_response_is_operational` and `brilliant_scientist_biomedical_weaponization_is_operational` inside the exact target controller scope. This raises existing outbreak-response values without creating another contamination, pathogen, or protection ledger; disabled, damaged, dismantled, stolen, or transferred project state stops contributing immediately.

## Future extensions

Future work may add target-specific report events or defender reactions only when they use the existing action receipts and do not create a parallel project or payment ledger.

Any additional cross-project synergy must provide a concrete decision, event variant, production route, countermeasure, or strategic action and must use the canonical family-stage and family-health ledgers.

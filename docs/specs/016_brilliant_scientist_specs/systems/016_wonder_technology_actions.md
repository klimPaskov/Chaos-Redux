# Event 016 Wonder-Technology Actions

> **Biological synergy amendment, 2026-09-20.** The user's approved native-raid migration supersedes the former Teleportation–Biological Weapons battlefield decision receipt described in older plans. The active synergy is a Portal battlefield raid variant within the existing `biological_raids` category; see `docs/events/016_brilliant_scientist/systems/biological_operations.md` for source and engine limits. The conventional weaponization actions elsewhere in this document retain their separate decision contract.

## Overview

Learned conventional Weaponization packages provide eight paid operational actions in the ordinary `conventional_technology_operations` category, alongside their passive national effects.

The same full-strength actions are available to a native project recipient or an authorized external API recipient once the matching durable weaponized package is learned.
They require an existing country, no active terminal commitment or shared world end, the complete material cost, and any action-specific industrial or target requirements.
Kruger's departure and changes to the originating project do not revoke learned capabilities.

The actions do not grant project stages, duplicate project history, or create a second project or payment ledger.
Native project incidents remain separate from the country's permanent knowledge and the action's own payment and target transaction.

## Operational sequence

1. A project reaches Weaponization through its existing lifecycle, or an authorized event grants the same cumulative package through `chaosx_grant_conventional_technology_package`.
2. The matching scripted trigger verifies learned weaponization, terminal state, concrete resource gates, and any specific industry or target requirements.
3. Selection immediately commits Command Power, support equipment, and fuel while the native decision timer occupies civilian factories.
4. The removal effect applies the operational outcome only after preparation or construction expires and the country and target remain valid.
5. Cancellation refunds the committed Command Power, support equipment, and fuel once; occupied factories are released, but elapsed factory time is not restored.
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
| Biomedical | Order Emergency Regeneration | Weaponization | Doubles reinforcement and recovery, nearly eliminates combat-experience loss, and sharply reduces supply demand for ninety days. The operational and weaponized packages also add fifty points each to shared outbreak surveillance, containment, medical, and biosecurity calculations. |
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
| Teleportation plus Biological Weapons | The native Portal battlefield biological raid reaches an authorized hostile rear state and reserves ten Teleportation Equipment alongside the fixed agent lot through `essential_equipment`. Its seven-day preparation and 25 Command Power allocation are native; cancellation and disconnected rear-area path behavior remain engine-validation gaps. |
| Temporal Mechanics plus Cloning | Clone continuity is one exclusive canonical-Kruger survival route; temporal target-use receipts and debt prevent repeated body recovery. |
| Temporal Mechanics plus Robotics | Machine continuity is one exclusive canonical-Kruger survival route; anchor authentication and temporal debt prevent repeated command restoration. |
| Public Computation plus Independent Teams | Independent-research reconstruction, archive recovery, assistant amnesty, international inspection, and exact-family foreign counter-program decisions. |

The Teleportation plus Biological Weapons raid uses the shared `biological_raids` category and its own exact agent/method ID, without an additional Directorate action, separate target receipt, or temporary percentage modifier.

## Tuning and ownership

Shared costs, duration, output, and AI values live in `common/script_constants/016_brilliant_scientist_technology_action_constants.txt`.

Eligibility lives in `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt`, payment and outcomes live in `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt`, decisions live in `common/decisions/016_brilliant_scientist_technology_actions.txt`, and timed national effects live in `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`.

Support-equipment checks use the strict `has_equipment` operator against exclusive gates one whole unit below the displayed payment.
Command Power, fuel, and available civilian factories use inclusive lower bounds, including exact fractional fuel boundaries.
Military factories are a separate non-consumed industrial requirement for the four heavy directives.

| Payment profile | Command Power | Support equipment | Fuel | Occupied civilian factories |
| --- | ---: | ---: | ---: | ---: |
| Sensor saturation | 20 | 75 | 250 | 2 |
| Predictive campaign and epidemic control | 25 | 100 | 500 | 2 |
| Synthesis works | 25 | 100 | 500 | 3 |
| High-speed strike, long-range delivery, field projectors, emergency regeneration | 40 | 200 | 1,500 | 3 |

The four custom-cost rows display each resource with an independently coloured affordability fragment, and concise trigger tooltips keep raw nested checks out of the requirements display.
These eight distinct operations remain directly available in one category when all six packages are weaponized; they are not replaced with an extra selection step or another scripted GUI.

## Icon contract

The ordinary category uses `GFX_decision_category_conventional_technology`, registered in `interface/016_conventional_technology.gfx` against the existing generated scientific-instrument emblem at `gfx/interface/016_brilliant_scientist/directorate/decision_category_directorate.dds`.

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

The action availability triggers consume durable neutral knowledge flags rather than the project's suspended, damaged, dismantled, or stolen arrays.
Those arrays still govern the native project board, incidents, and pre-operational outputs.

The materials synthesis state flag is the permanent state receipt used to prevent duplicate construction.

The long-range strike uses a timed target-state flag rather than a world ledger, so target exclusion is bounded to the selected state and requires no recurring world scan.

The neutral package reconciler owns one computation research slot per country.
It adopts an existing native slot without adding another and the native dispatcher checks both ownership markers before adding a slot.
Project disable and transfer retain learned knowledge in the former country, while a valid recipient learns its own package from the transferred project history; neither country can gain a second slot from repeated grants or reconciliation.
Kruger State formation preserves its ordinary base-slot floor plus any active learned Computation slot, rather than absorbing the learned slot into the base floor.

The shared biological lifecycle reads `brilliant_scientist_biomedical_response_is_operational` and `brilliant_scientist_biomedical_weaponization_is_operational` inside the exact target controller scope.
These queries read the matching learned-package flags, raising existing outbreak-response values without creating another contamination, pathogen, or protection ledger and without revoking the benefit when Kruger or a project leaves.

## Future extensions

Future work may add target-specific report events or defender reactions only when they use the existing action receipts and do not create a parallel project or payment ledger.

Any additional cross-project synergy must provide a concrete decision, event variant, production route, countermeasure, or strategic action.
Native research and governance consumers use the canonical project ledgers; provider-neutral learned-technology consumers use the public package queries and preserve their own payment and target ownership.

# Event 016 project reuse and identifier map

## Purpose and status

This handoff fixes the implementation identifiers and reuse boundaries for all fifteen Event 016 project families. It is a binding map for later gameplay implementation, not an assertion that the projects, technologies, units, equipment, rewards, decisions, AI, or assets listed as new already exist.

The map reconciles the Event 016 source-of-truth packet, project portfolio, project-family matrix, AI matrix, balance review, current scripted architecture, the installed vanilla game and documentation, and the live Chaos Redux biological-warfare systems. Existing identifiers are reused whenever they already express the required result. New identifiers are reserved only where no suitable live object exists.

Two corrections are binding:

- Event 015 owns visible super-event slots 85 through 89. Event 016 uses 90 recognition, 91 formation, 92 threat, 93 Laboratory World, 94 Strategic Singularity, and 95 defeat. Earlier Event 016 planning references to 88 through 93 are superseded.
- Event 016 world-end selector IDs remain 11 for Laboratory World and 12 for Strategic Singularity. These are triggerable-scenario selector values, not visible super-event IDs.

No shared Fallout gameplay file should be edited merely to create a second terminal system. The section named `Strategic Singularity and the dedicated Fallout system` defines the required request bridge.

## Reference evidence

The identifier decisions were made after consulting the required offline wiki snapshot pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Technology, Equipment, Division modding, and Unit modding. The snapshot contains no separate Special Projects page.

Vanilla documentation consulted includes <code>documentation/script_concept_documentation.md</code>, <code>documentation/effects_documentation.md</code>, <code>documentation/triggers_documentation.md</code>, the Special Projects documentation set, the project/specialization/prototype documentation, character documentation, and <code>common/script_constants/documentation.md</code>. Live precedents were checked in vanilla radar, rocket, air, and nuclear project files and in Chaos Redux’s biowarfare projects, technologies, equipment, buildings, lifecycle work, and consequences. The offline wiki and installed files, not memory or the web Paradox wiki, govern this map.

## Identifier legend

- **Reuse**: live vanilla or Chaos Redux object; do not duplicate or rename it.
- **New**: exact reserved identifier for Event 016 implementation.
- **Wrapper**: exact reserved Event 016 scripted identifier for behavior the native special-project surface cannot represent by itself.
- **Conditional hook**: new flag or effect required only if the referenced event is integrated; absence of a current stable marker is not permission to infer completion.

## Shared fifteen-family contract

The current scripted architecture already establishes the common family and stage vocabulary:

| Contract | Exact identifiers |
| --- | --- |
| Family enum | <code>constant:brilliant_scientist_project_family.{computation,electronics,materials,rocketry,high_energy,biomedical,teleportation,cloning,robotics,paleogenetics,xenobiological_synthesis,biological_weapons,alien_arms,temporal,singularity}</code> = 1 through 15 |
| Stage enum | <code>constant:brilliant_scientist_project_stage.{none,theory,prototype,deployment,weaponization}</code> = 0 through 4 |
| Host stage ledger | <code>brilliant_scientist_project_stage_entries</code> |
| Independently replicated stage ledger | <code>brilliant_scientist_independent_project_stage_entries</code> |
| State arrays | <code>brilliant_scientist_project_{suspended,damaged,dismantled,published,stolen}_families</code> |
| Family/stage caller inputs | temporary <code>brilliant_scientist_project_family</code> and <code>brilliant_scientist_requested_project_stage</code> |
| Stage mutation | <code>brilliant_scientist_advance_project_to_requested_stage</code>, <code>brilliant_scientist_replicate_project_to_requested_stage</code>, <code>brilliant_scientist_publish_project</code>, <code>brilliant_scientist_mark_project_stolen</code>, <code>brilliant_scientist_dismantle_project</code> |
| Cost loader | <code>brilliant_scientist_load_project_cost_and_duration</code> |
| Cost outputs | temporary <code>brilliant_scientist_cost_{civilian_factories,military_factories,support_equipment,trucks,trains,fuel,manpower,army_xp,air_xp,navy_xp,political_power,resource_units,duration_days,capacity}</code> plus <code>brilliant_scientist_project_cost_ready</code> |
| Primary and secondary sites | global event targets <code>brilliant_scientist_primary_facility</code> and <code>brilliant_scientist_secondary_facility</code>; state flags of the same names |
| Facility type enum | <code>constant:brilliant_scientist_facility.{primary_type,secondary_type,temporal_anchor_type,singularity_core_type}</code> = 1 through 4 |
| Personal carried stages | character flags <code>brilliant_scientist_personal_&lt;family&gt;_&lt;stage&gt;</code> |
| KRG reconstruction | <code>brilliant_scientist_inherit_kruger_carried_portfolio</code> |

The following wrapper identifiers are still required by the project implementation layer and are reserved here:

| New wrapper | Purpose |
| --- | --- |
| <code>brilliant_scientist_dispatch_project_accident</code> | Family-indexed accident dispatcher using the common pressure calculation and family-specific consequences |
| <code>brilliant_scientist_foreign_project_stage_entries</code> | Stage-by-family knowledge ledger owned by an explicit foreign actor |
| <code>brilliant_scientist_grant_foreign_project_knowledge</code> | Bounded publication, joint-lab, or theft grant; never grants a branch the actor did not obtain |
| <code>brilliant_scientist_project_countermeasure_entries</code> | Family-indexed foreign countermeasure progress |
| <code>brilliant_scientist_apply_project_countermeasure</code> | Family-indexed countermeasure outcome dispatcher |
| <code>brilliant_scientist_apply_project_inheritance_outputs</code> | Converts carried personal stages into the exact KRG technology, equipment, unit, facility, and decision package |

These wrappers should extend, not replace, the live foreign-context gates:
<code>brilliant_scientist_foreign_can_invite</code>,
<code>brilliant_scientist_foreign_can_open_joint_laboratory</code>,
<code>brilliant_scientist_foreign_can_offer_protection</code>,
<code>brilliant_scientist_foreign_can_attempt_theft</code>,
<code>brilliant_scientist_foreign_can_attempt_sabotage</code>,
<code>brilliant_scientist_foreign_can_attempt_extraction</code>, and
<code>brilliant_scientist_foreign_can_attempt_assassination</code>.

## Native engine boundary

Native special projects should own the research clock whenever an actual project object is active. The engine supports a static project specialization, its associated facility, project availability and parent gates, breakthrough cost, resource cost, complexity, prototype time, project output, generic rewards, unique rewards, and project AI. Event 016 should use those surfaces directly.

The Event 016 family ledger is broader than the native project object. Theory, Deployment, Weaponization, maintenance, force production, foreign actions, publication, independent replication, facility occupation, and terminal commitments therefore remain decisions, missions, events, technologies, flags, variables, and scripted wrappers.

Important boundaries:

- The loader’s Prototype duration is informational and tuning parity when a native special project is running. Do not run a second Event 016 duration over the native prototype clock.
- Native <code>resource_cost</code> supports strategic resources, not Event 016’s full dynamic burden bundle. Political power, factories reserved over time, manpower, equipment, trains, trucks, fuel, XP, exposure, and capacity remain wrapper costs.
- A native project has one specialization. Cross-specialization prerequisites and the Singularity’s multi-site component condition require wrapper triggers.
- No new specialization or special-project facility is needed. Reuse vanilla <code>specialization_land</code>/<code>land_facility</code>, <code>specialization_air</code>/<code>air_facility</code>, <code>specialization_nuclear</code>/<code>nuclear_facility</code>, and Chaos Redux <code>specialization_biowarfare</code>/<code>biowarfare_facility</code>.
- Dynamic family selection, dynamic technology identifiers, or dynamic project identifiers must be dispatched through explicit family branches or a documented meta effect. They are not native variable-valued fields.
- Reserve all numerical values below through script constants or file-scoped project constants at implementation time; do not paste tuning numbers repeatedly into gameplay blocks.

## Cost, duration, capacity, and risk contract

### Common stage burden

The loader applies these baseline burdens before the family multiplier. Factory values are timed reservations, not instant factory grants.

| Stage | Civ | Mil | Support eq. | Trucks | Trains | Fuel | Manpower | Army XP | Air XP | Navy XP | PP | Resource units | Capacity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Theory | 1 | 0 | 100 | 0 | 0 | 0 | 250 | 0 | 0 | 0 | 50 | 2 | 10 |
| Prototype | 2 | 1 | 250 | 20 | 0 | 500 | 500 | 5 | 5 | 5 | 75 | 4 | 20 |
| Deployment | 4 | 3 | 750 | 100 | 10 | 2,500 | 2,000 | 15 | 15 | 15 | 100 | 6 | 35 |
| Weaponization | 6 | 5 | 1,500 | 250 | 25 | 7,500 | 5,000 | 30 | 30 | 30 | 150 | 10 | 50 |

Suspension retains half of capacity; dismantling releases capacity while preserving history.

### Family burden multipliers

Column order is factories, equipment, fuel, manpower, PP, Army XP, Air XP, Navy XP, and strategic-resource units.

| Family | Factory | Equip. | Fuel | Manpower | PP | Army XP | Air XP | Navy XP | Resource |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Computation | 0.80 | 0.80 | 0.20 | 0.70 | 0.90 | 0 | 0 | 0 | 0.80 |
| Electronics | 1.00 | 1.00 | 0.50 | 0.80 | 0.90 | 0.50 | 0.75 | 0.50 | 1.20 |
| Materials | 1.20 | 0.80 | 0.40 | 1.00 | 0.90 | 0 | 0 | 0 | 1.50 |
| Rocketry | 1.30 | 1.10 | 1.50 | 0.90 | 1.00 | 0.25 | 1.00 | 0 | 1.30 |
| High energy | 1.50 | 1.00 | 0.80 | 0.80 | 1.20 | 0 | 0 | 0 | 1.80 |
| Biomedical | 0.90 | 1.20 | 0.20 | 1.30 | 1.20 | 0.25 | 0 | 0 | 0.70 |
| Teleportation | 1.50 | 1.20 | 1.20 | 0.80 | 1.20 | 0.50 | 0.50 | 0 | 1.60 |
| Cloning | 1.10 | 1.30 | 0.30 | 1.50 | 1.30 | 0.75 | 0 | 0 | 0.80 |
| Robotics | 1.40 | 1.50 | 0.80 | 0.70 | 1.10 | 1.00 | 0.25 | 0 | 1.50 |
| Paleogenetics | 1.00 | 1.30 | 0.60 | 1.60 | 1.30 | 1.00 | 0 | 0 | 0.70 |
| Xenobiological synthesis | 1.20 | 1.40 | 0.50 | 1.40 | 1.40 | 1.00 | 0 | 0 | 1.10 |
| Biological weapons | 1.10 | 1.40 | 0.30 | 1.20 | 1.60 | 0.75 | 0 | 0 | 0.90 |
| Alien arms | 1.50 | 1.50 | 1.00 | 0.80 | 1.40 | 0.75 | 0.75 | 0.50 | 2.00 |
| Temporal | 1.60 | 1.20 | 1.00 | 0.80 | 1.50 | 0.50 | 0.50 | 0 | 1.70 |
| Singularity | 2.00 | 1.80 | 2.00 | 1.20 | 2.00 | 1.00 | 1.00 | 1.00 | 2.50 |

### Wrapper duration by family

Values are Theory / Prototype / Deployment / Weaponization days. Prototype is not charged twice when a native project supplies its clock.

| Family | Days |
| --- | --- |
| Computation | 120 / 180 / 270 / 360 |
| Electronics | 120 / 210 / 300 / 390 |
| Materials | 150 / 240 / 330 / 420 |
| Rocketry | 180 / 270 / 390 / 540 |
| High energy | 240 / 360 / 540 / 720 |
| Biomedical | 150 / 240 / 330 / 450 |
| Teleportation | 240 / 360 / 540 / 720 |
| Cloning | 210 / 330 / 480 / 660 |
| Robotics | 180 / 300 / 450 / 600 |
| Paleogenetics | 210 / 330 / 480 / 660 |
| Xenobiological synthesis | 240 / 390 / 570 / 750 |
| Biological weapons | 180 / 300 / 450 / 600 |
| Alien arms | 270 / 420 / 600 / 780 |
| Temporal | 360 / 540 / 720 / 900 |
| Singularity | 720 / 900 / 1,080 / 900; component research is 720, core construction 1,080, delivery construction 720, and arming 365 |

### Common accident calculation

<code>brilliant_scientist_refresh_project_accident_pressure</code> combines Exposure and the family/stage capacity burden. Risk bands are 25 minor, 50 major, 75 severe, and 90 catastrophic. Theory, Prototype, Deployment, and Weaponization apply stage factors 0.50, 1.00, 1.25, and 1.60. A suspended project halves its project contribution; a damaged project multiplies it by 1.50. The family-specific incidents in the map below must be selected by <code>brilliant_scientist_dispatch_project_accident</code>.

## All-family implementation map

### 1. Computational mathematics and cryptanalysis

- **Reuse:** vanilla <code>mechanical_computing</code>, <code>computing_machine</code>, <code>improved_computing_machine</code>, <code>advanced_computing_machine</code>, <code>electronic_mechanical_engineering</code>.
- **New project:** <code>sp_brilliant_scientist_computational_engine</code>; <code>specialization_land</code>, <code>land_facility</code>; breakthrough 1; short/small; resource envelope steel 2, tungsten 2, rubber 2.
- **Stages:** Theory grants/requires the early computing line; Prototype completes the computational engine; Deployment requires <code>improved_computing_machine</code> and establishes the national computation network; Weaponization requires <code>advanced_computing_machine</code> and creates a self-directing command network.
- **Synergies:** electronics improves reliability; robotics and temporal consume the command/prediction output. Published computation is the strongest host-side counter-Kruger prerequisite.
- **Accident/countermeasure:** lost calculations → network corruption → false orders or hidden procurement. Counter with auditable architecture and independent operators.
- **KRG inheritance:** stage-derived planning, intelligence, and machine-coordination package only; no technology beyond the carried stage.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_computational_engine</code>, <code>GFX_brilliant_scientist_project_computation</code>.
- **Unique reward:** <code>sp_brilliant_scientist_computational_engine_reward_unreadable_notation</code>; generic land scientist-XP/progress/failure rewards may also be used.
- **AI:** high when research coordination or intelligence is weak; avoid if staff and industrial capacity cannot sustain the equipment burden.

### 2. Electronics, radar, and guidance

- **Reuse project:** <code>sp_air_radar</code>, icon <code>GFX_sp_nuclear_radar</code>, <code>specialization_air</code>, <code>air_facility</code>. No Event 016 radar clone.
- **Reuse technologies/modules:** <code>electronic_mechanical_engineering</code>, <code>radio</code>, <code>improved_radio</code>, <code>advanced_radio</code>, <code>radio_detection</code>, <code>cavity_magnatron</code>, <code>centimetric_radar</code>, <code>phased_array</code>, <code>monopulse_radar</code>, <code>lc_radar</code>, <code>ship_radar_1</code>.
- **Stages:** Theory covers electronics/radio; Prototype is <code>sp_air_radar</code>; Deployment grants the radar/detection outputs already owned by that project and line; Weaponization requires late radar plus computation for autonomous precision delivery.
- **Native cost:** preserve <code>sp_air_radar</code>’s breakthrough 1, medium prototype time/complexity, steel 6 and aluminium 6 cost, and <code>electronic_mechanical_engineering</code> gate.
- **Accident/countermeasure:** equipment fire → radar/control blackout → compromised strategic systems. Counter with electronic disruption and network isolation.
- **KRG inheritance:** interception, ranged support, and guidance support at the carried stage; no free missile branch.
- **Asset IDs:** native project icon plus <code>GFX_brilliant_scientist_project_electronics</code>; no replacement project art.
- **AI:** high against air/missile threats and with an air facility; low without production or a defendable site.

### 3. Advanced materials and industrial synthesis

- **Reuse:** <code>basic_machine_tools</code>, <code>improved_machine_tools</code>, <code>advanced_machine_tools</code>, <code>assembly_line_production</code>, <code>synth_oil_experiments</code>, <code>construction4</code>, <code>excavation5</code>.
- **New project:** <code>sp_brilliant_scientist_advanced_materials</code>; <code>specialization_land</code>, <code>land_facility</code>; breakthrough 2; medium/medium; steel 6, tungsten 4, chromium 4, rubber 2.
- **Stages:** Theory requires an industrial base; Prototype completes one advanced-material batch; Deployment requires advanced tools/assembly-line application; Weaponization allows hardened or self-propagating production.
- **Synergies:** rocketry, robotics, high energy, teleportation, and Singularity components consume materials outputs.
- **Accident/countermeasure:** toxic spill → factory destruction → self-propagating industrial failure. Counter with resource denial and independently verified production standards.
- **KRG inheritance:** industry, armor, and repair package scaled to stage; never grants resources ex nihilo.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_advanced_materials</code>, <code>GFX_brilliant_scientist_project_materials</code>.
- **Unique reward:** <code>sp_brilliant_scientist_advanced_materials_reward_self_propagating_batch</code>.
- **AI:** high for industrial weakness with usable civilian capacity; avoid when the country cannot exploit the output.

### 4. Rocketry, propulsion, and high-speed flight

- **Reuse projects:** <code>sp_rockets_flying_bomb</code>, <code>sp_rockets_ballistic_missile</code>, <code>sp_rockets_medium_range_ballistic_missile</code>, <code>sp_rockets_long_range_ballistic_missile</code>, <code>sp_rockets_ground_to_air_missile</code>, <code>sp_rocket_interceptor</code>, <code>sp_air_jet_engine</code>, <code>sp_air_axial_jet_engine</code>, <code>sp_air_supersonic_jet</code>.
- **Specialization/facility:** preserve the reused projects’ <code>specialization_air</code>/<code>air_facility</code> ownership.
- **Reuse technologies/outputs:** <code>experimental_rockets</code>, <code>rocket_engines</code>, <code>improved_rocket_engines</code>, <code>advanced_rocket_engines</code>, <code>jet_engines</code>, <code>sp_rockets_improved_guidance</code>, <code>guided_missile_equipment_1</code>, <code>guided_missile_equipment_2</code>, <code>guided_missile_equipment_3</code>, <code>ballistic_missile_equipment_1</code>, <code>ballistic_missile_equipment_2</code>, <code>nuclear_missile_equipment_2</code>.
- **Stages:** Theory uses experimental rocket/jet research; Prototype accepts the flying-bomb or jet-engine branch; Deployment accepts ballistic/axial progression; Weaponization accepts long-range/supersonic progression and the relevant delivery prerequisites.
- **Native cost:** preserve each reused project’s own breakthrough, parent, resource, complexity, and prototype-time contract. Notably flying bomb is breakthrough 2, steel 8/aluminium 8/tungsten 2; ballistic missile is breakthrough 3, steel/aluminium/chromium 9; medium range is steel 12/aluminium 9/chromium 9; long range is steel/aluminium/chromium 12 and requires <code>sp_nuclear_warheads</code>.
- **Accident/countermeasure:** test failure → range destruction → distant impact/foreign incident. Reuse rocket onsite-explosion/test-failure rewards. Counter with air defense and destruction of test or launch sites.
- **KRG inheritance:** missile forces and distant-strike decisions only for completed carried stages.
- **Asset IDs:** existing project icons, including <code>GFX_sp_rockets_flying_bomb</code>, <code>GFX_sp_rockets_ballistic_missile</code>, <code>GFX_sp_rockets_medium_range_ballistic_missiles</code>, <code>GFX_sp_rockets_icbm</code>, <code>GFX_sp_air_jet_engine</code>, <code>GFX_sp_air_axial_jet_engine</code>, <code>GFX_sp_air_supersonic_jet</code>; new family card <code>GFX_brilliant_scientist_project_rocketry</code>.
- **AI:** high with electronics, materials, a test range, fuel, and a strategic air threat; low without production or range security.

### 5. Atomic and high-energy physics

- **Reuse projects:** <code>sp_nuclear_reactor</code>, <code>sp_commercial_nuclear_reactor</code>, <code>sp_nuclear_engines</code>, <code>sp_nuclear_bomb</code>, <code>sp_thermo_nuclear_bomb</code>, <code>sp_nuclear_warheads</code>.
- **Specialization/facility:** preserve <code>specialization_nuclear</code>/<code>nuclear_facility</code>.
- **Reuse technologies:** <code>atomic_research</code>, <code>nuclear_reactor</code>, <code>nuclear_reactor_heavy_water</code>, <code>nukes</code>, <code>commercial_nuclear_reactor_tech</code>, <code>isotope_separation_centrifugal</code>, <code>thermonuclear_bombs</code>.
- **Stages:** Theory is <code>atomic_research</code>; Prototype is the reactor; Deployment is commercial power or bomb support; Weaponization requires the bomb branch and may accept thermonuclear/warhead progression.
- **Native cost:** preserve vanilla project contracts: reactor steel 6/tungsten 3/chromium 6, long/large; commercial reactor steel 6/tungsten 4/chromium 7, long/large and <code>construction4</code>; bomb steel 2/tungsten 8/chromium 2, long/large; thermonuclear bomb steel 2/tungsten 10/chromium 3, long/insane; warheads aluminium 4/tungsten 4/chromium 2, long/large.
- **Accident/countermeasure:** radiation release → reactor crisis → mass contamination/strategic blast. Reuse nuclear leak, explosion, and bomb-accident rewards. Counter with material denial, reactor capture, and containment.
- **KRG inheritance:** independent power and strategic-energy package at the carried stage; no free nuclear stockpile unless the inherited output explicitly records it.
- **Asset IDs:** native nuclear project icons plus <code>GFX_brilliant_scientist_project_high_energy</code>.
- **AI:** requires atomic research, rare resources, secure nuclear facilities, and a strategic need; ordinary AI must not use this family as a shortcut to the Singularity.

### 6. Biomedical acceleration and protective medicine

- **Reuse:** <code>pathogen_handling_protocols</code>, <code>sealed_containment_laboratories</code>, <code>fail_safe_containment_facilities</code>, <code>bio_surveillance_networks</code>, <code>rapid_outbreak_response</code>, <code>integrated_epidemic_control</code>, <code>field_epidemiology_teams</code>, <code>mobile_cbrn_hospitals</code>, <code>biological_security_assault_formation</code>.
- **New project:** <code>sp_brilliant_scientist_biomedical_acceleration</code>; <code>specialization_biowarfare</code>, <code>biowarfare_facility</code>; breakthrough 1; medium/medium; steel 2, tungsten 1, chromium 1, rubber 4.
- **Stages:** Theory requires pathogen handling or surveillance; Prototype proves accelerated treatment/artificial tissue; Deployment requires epidemiology/hospital capacity; Weaponization is a self-maintaining protective-medical network, not a pathogen grant.
- **Synergies:** prerequisite for cloning, paleogenetics, xenobiology, and biological defense.
- **Accident/countermeasure:** trial injury → medical contamination → public-health scandal. Counter with ethical oversight and control of medical archives.
- **KRG inheritance:** resilient-force and medical-support package; does not imply bioweapon ownership.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_biomedical_acceleration</code>, <code>GFX_brilliant_scientist_project_biomedical</code>.
- **Unique reward:** <code>sp_brilliant_scientist_biomedical_acceleration_reward_unlicensed_trial</code>; may share biowarfare generic XP/progress/failure rewards.
- **AI:** high under heavy casualties or contamination; avoid if the medical system is disabled or the route forbids human trials.

### 7. Teleportation and quantum transit

- **Reuse prerequisites only:** computation, advanced materials, electronics calibration, and high-energy stages. No live Teleportation Experiment event or reusable teleportation project identifier was found; do not claim an event link until one exists.
- **New project:** <code>sp_brilliant_scientist_quantum_transit</code>; <code>specialization_nuclear</code>, <code>nuclear_facility</code>; breakthrough 3; very-long/insane; steel 6, tungsten 8, chromium 6, rubber 4.
- **Operational outputs:** technology <code>brilliant_scientist_portal_warfare_tech</code>; generic unit <code>portal_raider</code>; archetype/type <code>teleportation_equipment</code>/<code>teleportation_equipment_1</code>.
- **Stages:** Theory requires Computation, Materials, and High Energy at Deployment; Prototype transfers bounded inert matter; Deployment unlocks linked terminals and the operational outputs; Weaponization unlocks capped portal raids and strategic delivery.
- **Accident/countermeasure:** object loss → chamber breach → uncontrolled portal/distant intrusion. Counter with terminal security, power denial, dual control, and electronics-based portal detection.
- **KRG inheritance:** portal force cap uses <code>constant:brilliant_scientist_force.portal_cap</code> = 4 and requires terminals, equipment, supply, and stage; no free teleport spawn.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_quantum_transit</code>, <code>GFX_brilliant_scientist_project_teleportation</code>, <code>GFX_brilliant_scientist_portal_warfare_tech_medium</code>, equipment/unit icons for the exact new outputs.
- **Unique reward:** <code>sp_brilliant_scientist_quantum_transit_reward_duplicate_transfer</code>.
- **AI:** pursue for strategic mobility only when terminals can be defended and power/material burdens can be met.

### 8. Cloning and replicated bodies

- **Structural precedent only:** <code>sp_mengele_cloning</code> demonstrates a medium, biowarfare-specialized cloning project, but it is Germany/Mengele-specific. Event 016 must not reuse that project’s availability, flags, outputs, or identifier.
- **New project:** <code>sp_brilliant_scientist_cloning</code>; <code>specialization_biowarfare</code>, <code>biowarfare_facility</code>; breakthrough 2; medium/medium; steel 5, chromium 3, rubber 4.
- **Operational outputs:** <code>brilliant_scientist_clone_formations_tech</code>, shared unit <code>clone_infantry</code>, and transferable <code>clone_equipment</code>. Clone formations also consume ordinary infantry equipment.
- **Stages:** Theory requires Biomedical; Prototype yields a viable body; Deployment unlocks cadres/replacement systems and growth sites; Weaponization unlocks capped clone armies and Kruger-continuity choices.
- **Synergies:** Biomedical, Paleogenetics, Xenobiological Synthesis, and Temporal.
- **Accident/countermeasure:** nonviable body → growth contamination → identity/escape crisis. Counter with growth-site control, identity records, and amnesty/splinter routes.
- **KRG inheritance:** clone cap 8, stage-derived formations and continuity only; carried stage cannot import Mengele’s country flags.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_cloning</code>, <code>GFX_brilliant_scientist_project_cloning</code>, <code>GFX_brilliant_scientist_clone_formations_tech_medium</code>.
- **Unique reward:** <code>sp_brilliant_scientist_cloning_reward_identity_conflict</code>.
- **AI:** high under manpower shortage with biomedical/growth capacity; avoid without food, medicine, equipment, or identity-control capacity.

### 9. Robotics and autonomous cognition

- **Reuse prerequisites:** late computation, electronics, advanced materials, and relevant ordinary industrial technologies.
- **New project:** <code>sp_brilliant_scientist_autonomous_cognition</code>; <code>specialization_land</code>, <code>land_facility</code>; breakthrough 2; long/large; steel 8, tungsten 4, chromium 5, rubber 3.
- **New operational outputs:** <code>brilliant_scientist_robot_formations_tech</code>; unit <code>kruger_robot_frame</code>; <code>kruger_robot_equipment</code>/<code>kruger_robot_equipment_1</code>.
- **Stages:** Theory requires Computation, Electronics, and Materials; Prototype yields an autonomous device/frame; Deployment unlocks robot support and automation; Weaponization unlocks a distributed robot army/command network.
- **Accident/countermeasure:** frame failure → network takeover → autonomous military activation. Counter with power denial, network isolation, and electronic warfare.
- **KRG inheritance:** robot cap 8; production requires equipment, military factories, power/fuel, and maintenance.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_autonomous_cognition</code>, <code>GFX_brilliant_scientist_project_robotics</code>, <code>GFX_brilliant_scientist_robot_formations_tech_medium</code>, equipment/unit icons.
- **Unique reward:** <code>sp_brilliant_scientist_autonomous_cognition_reward_hidden_instruction</code>.
- **AI:** high with computation/electronics/materials and factory/power capacity; avoid low-power or undersupplied routes.

### 10. Paleogenetics and restored terrestrial creatures

- **New project:** <code>sp_brilliant_scientist_paleogenetics</code>; <code>specialization_biowarfare</code>, <code>biowarfare_facility</code>; breakthrough 2; medium/large; steel 4, tungsten 1, chromium 2, rubber 5.
- **New operational outputs:** <code>brilliant_scientist_paleogenetic_formations_tech</code>; unit <code>kruger_paleogenetic_beast</code>; <code>kruger_paleogenetic_equipment</code>/<code>kruger_paleogenetic_equipment_1</code>.
- **New site markers:** state flags <code>brilliant_scientist_paleogenetic_reserve</code> and <code>brilliant_scientist_paleogenetic_hatchery</code>.
- **Stages:** Theory requires Biomedical and Cloning; Prototype restores one extinct terrestrial organism; Deployment requires reserve, hatchery, handlers, feed, veterinary capacity, and transport; Weaponization unlocks capped restored-creature formations.
- **Burden and separation:** feed, handlers, reserve land, veterinary care, and transport are Paleogenetics-only requirements. Do not use xenobiological reagents, control-channel state, vats, or a shared “monster” project counter.
- **Accident/countermeasure:** specimen injury → large escape → ecological/military crisis. Counter with feed/handler denial, reserve capture, transport interdiction, air power, and anti-armor.
- **KRG inheritance:** cap 6; only the carried stage plus its separate reserve/hatchery capacity enables formations.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_paleogenetics</code>, <code>GFX_brilliant_scientist_project_paleogenetics</code>, <code>GFX_brilliant_scientist_paleogenetic_formations_tech_medium</code>, equipment/unit/site icons.
- **Unique reward:** <code>sp_brilliant_scientist_paleogenetics_reward_specimen_escape</code>.
- **AI:** pursue for terrain, transport, reconnaissance, or intimidation only with feed, land, handlers, veterinary capacity, and transport.

### 11. Xenobiological synthesis and engineered organisms

- **New project:** <code>sp_brilliant_scientist_xenobiological_synthesis</code>; <code>specialization_biowarfare</code>, <code>biowarfare_facility</code>; breakthrough 3; long/large; steel 5, tungsten 4, chromium 4, rubber 6.
- **New operational outputs:** <code>brilliant_scientist_xenobiological_formations_tech</code>; unit <code>kruger_xenobiological_assault</code>; <code>kruger_xenobiological_equipment</code>/<code>kruger_xenobiological_equipment_1</code>.
- **New site markers:** <code>brilliant_scientist_xenobiological_vat_complex</code>, <code>brilliant_scientist_xenobiological_control_center</code>.
- **Control choice:** exactly one of <code>brilliant_scientist_xeno_control_chemical</code>, <code>brilliant_scientist_xeno_control_neural</code>, <code>brilliant_scientist_xeno_control_machine</code>, or <code>brilliant_scientist_xeno_control_researched</code>.
- **Stages:** Theory requires Biomedical plus Cloning or authenticated alien material; Prototype produces one engineered organism and locks the control method; Deployment requires vats, medical fabrication, reagents, power, containment, and a control center; Weaponization unlocks capped specialist-assault organisms or the autonomous-nest risk.
- **Burden and separation:** reagents, power, containment, and control-channel integrity are Xenobiological-only requirements. Do not use Paleogenetic reserves, feed/handler ledgers, restored species, units, equipment, or counters.
- **Accident/countermeasure:** handler death → containment break → engineered-organism attack. Counter by identifying and breaking the selected control method, destroying growth labs, and isolating command.
- **KRG inheritance:** cap 6; carries the selected control method and exact stage, not Paleogenetic infrastructure.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_xenobiological_synthesis</code>, <code>GFX_brilliant_scientist_project_xenobiological_synthesis</code>, <code>GFX_brilliant_scientist_xenobiological_formations_tech_medium</code>, equipment/unit/site/control icons.
- **Unique reward:** <code>sp_brilliant_scientist_xenobiological_synthesis_reward_control_failure</code>.
- **AI:** pursue for fortification breaking or laboratory defense only with fabrication, reagents, power, containment, and a viable control choice.

Paleogenetics and Xenobiological Synthesis converge only through explicit Synthesis. Reserve the wrapper trigger/effect <code>brilliant_scientist_can_unlock_synthesis</code> and <code>brilliant_scientist_unlock_synthesis</code>; both families must be at Deployment or higher. Before that call, they share no project, stage counter, unit, equipment, site marker, maintenance ledger, failure dispatcher, or countermeasure progress.

### 12. Biological weapons

- **Reuse projects:** <code>anthrax_bomb</code>, <code>plague_bomb</code>, <code>tularemia_bomb</code>, <code>smallpox_bomb</code>, <code>weaponize_the_zombies</code>. <code>zombie_cure_bomb</code> is a defensive/cure precedent and may satisfy a protective branch, not an offensive agent grant.
- **Specialization/facility:** preserve <code>specialization_biowarfare</code>/<code>biowarfare_facility</code>.
- **Reuse project icons:** <code>GFX_sp_anthrax_bomb</code>, <code>GFX_sp_plague_bomb</code>, <code>GFX_sp_tularemia_bomb</code>, <code>GFX_sp_smallpox_bomb</code>, <code>GFX_sp_weaponize_the_zombies</code>, <code>GFX_sp_zombie_cure_bomb</code>.
- **Reuse technologies:** <code>anthrax_bomb_delivery_systems</code>, <code>plague_bomb_delivery_systems</code>, <code>tularemia_bomb_delivery_systems</code>, <code>smallpox_bomb_delivery_systems</code>, <code>zombie_disease_bomb_delivery_systems</code>, and the protective biomedical technologies already listed.
- **Reuse equipment:** <code>anthrax_bomb_equipment</code>/<code>anthrax_bomb_1</code>, <code>plague_bomb_equipment</code>/<code>plague_bomb_1</code>, <code>tularemia_bomb_equipment</code>/<code>tularemia_bomb_1</code>, <code>smallpox_bomb_equipment</code>/<code>smallpox_bomb_1</code>, and <code>zombie_disease_bomb_equipment</code>/<code>zombie_disease_bomb_1</code>. Do not create Event 016 copies.
- **Stages:** Theory requires handling/containment/surveillance; Prototype requires at least one completed live agent project, normally anthrax or tularemia; Deployment requires a second independently completed agent/delivery technology and real stockpile; Weaponization requires smallpox, adaptive quality, or the separately gated zombie project and unlocks capped delivery/fail-deadly behavior.
- **Exact agent carry flags:** <code>brilliant_scientist_personal_biological_agent_{anthrax,plague,tularemia,smallpox,weaponized_zombies}</code>. The family stage alone is insufficient to identify inherited agents or stockpiles.
- **Canonical lifecycle:** Event 016 seeds anthrax, plague, tularemia, or smallpox through <code>bio_lifecycle_reset_seed_record</code> and <code>bio_lifecycle_dispatch_seed</code> using <code>constant:bio_lifecycle_agent.{anthrax,plague,tularemia,smallpox}</code>. Weekly deaths flow through <code>bio_lifecycle_register_current_agent_weekly_deaths</code>; attribution Condemnation flows through the lifecycle's staged probable/confirmed attribution effects. The retired <code>apply_*_contamination</code> compatibility effects are not valid callers.
- **Canonical consequences:** the ordinary lifecycle owns Deaths accumulation, state contamination, outbreak state, treatment, quarantine, medical saturation, evidence, attribution, and Condemnation. Event 016 must supply exact actor, victim, state, route, source, result, and payload authority to that lifecycle instead of calling removed immediate-contamination helpers. Zombies remain a separate agent system.
- **Accident/countermeasure:** laboratory exposure → quarantine mission → outbreak/deaths/condemnation. Counter with quarantine, vaccines, surveillance, treatment, and safe stockpile seizure.
- **KRG inheritance:** copy only exact personal agent flags, matching delivery technologies, and bounded existing stockpiles; family cap 4. Never synthesize missing agents from the family stage.
- **Asset IDs:** reuse all agent project/equipment/technology art; add only <code>GFX_brilliant_scientist_project_biological_weapons</code> and Event 016 decision/category art where needed.
- **AI:** forbidden/desperation family. Requires ideology/threat gates, secure containment, and condemnation/self-contamination evaluation.

The lifecycle files are concurrent implementation work. Event 016 integration depends on their accepted canonical API; if that API changes during review, update this map and the Event 016 caller together rather than forking it.

### 13. Alien arms and exotic-energy weapons

- **Reuse cross-event gate:** Event 025 Antarctic UFO success idea <code>antarctica_success</code> remains the actual recovered-artifact prerequisite. Its qualifying success now also presents the bounded Event 016 report <code>chaosx.nr16.17</code> and writes the persistent receipt <code>brilliant_scientist_alien_artifact_contact</code>; the report does not replace the idea gate or assert an origin conclusion.
- **Conditional Event 036 hook:** `chaosx.nr36.2` is the authenticated spacecraft outcome. It now sets exact flag <code>brilliant_scientist_alien_spacecraft_recovered</code> on the recovering country, and an active Event 016 host presents the one-time report <code>chaosx.nr16.18</code>. The report preserves the physical evidence gate without advancing Alien Arms, and the flag remains country-owned rather than following Kruger.
- **New project:** <code>sp_brilliant_scientist_alien_arms</code>; <code>specialization_nuclear</code>, <code>nuclear_facility</code>; breakthrough 3; long/large; steel 4, tungsten 7, chromium 6, rubber 3.
- **New outputs:** <code>brilliant_scientist_exotic_guard_tech</code>; unit <code>kruger_exotic_guard</code>; <code>kruger_exotic_arms_equipment</code>/<code>kruger_exotic_arms_equipment_1</code>.
- **Stages:** Theory requires <code>antarctica_success</code> or the conditional Event 036 flag plus High Energy; Prototype interfaces with one weapon/shield; Deployment unlocks elite equipment; Weaponization unlocks strategic field projectors.
- **Accident/countermeasure:** interface injury → energy breach → unknown strategic effect. Counter with material denial, interface specialists, and protection.
- **KRG inheritance:** exotic cap 4; exact stage and equipment production, not free recovered artifacts.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_alien_arms</code>, <code>GFX_brilliant_scientist_project_alien_arms</code>, <code>GFX_brilliant_scientist_exotic_guard_tech_medium</code>, equipment/unit icons.
- **Unique reward:** <code>sp_brilliant_scientist_alien_arms_reward_interface_breach</code>.
- **AI:** rare/desperation family; requires authenticated artifact, High Energy, materials, secure interface staff, and a strategic threat.

### 14. Temporal mechanics

- **Reuse cross-event signal:** Event 030 supplies the timed idea <code>time_traveler</code> and, when its report reaches an active Event 016 host, the one-time temporal-contact report <code>chaosx.nr16.16</code>.
- **Implemented persistent hook:** the qualifying Event 030 outcome writes exact flag <code>brilliant_scientist_time_traveler_contact</code>, queues <code>brilliant_scientist_time_traveler_contact_pending</code>, and resolves it once into <code>brilliant_scientist_time_traveler_contact_report_seen</code>. The receipt survives expiry of the timed idea and follows ordinary transfer and sovereignty inheritance. It is not a substitute for the Event 016 evidence/authentication gates.
- **New project:** <code>sp_brilliant_scientist_temporal_mechanics</code>; <code>specialization_nuclear</code>, <code>nuclear_facility</code>; breakthrough 4; very-long/insane; steel 6, tungsten 8, chromium 8, rubber 4.
- **New outputs:** <code>brilliant_scientist_temporal_guard_tech</code>; unit <code>kruger_temporal_guard</code>; <code>kruger_temporal_equipment</code>/<code>kruger_temporal_equipment_1</code>.
- **Stages:** Theory requires Computation, High Energy, and authenticated temporal evidence; Prototype allows one bounded information/object result; Deployment unlocks forecast, one-use recovery, and displacement; Weaponization unlocks tightly capped continuity/guard actions.
- **Bounded-target contract:** caller sets <code>brilliant_scientist_temporal_target_id</code>; <code>brilliant_scientist_bind_temporal_target</code> persists it as <code>brilliant_scientist_temporal_bound_target_id</code>; <code>brilliant_scientist_commit_bounded_temporal_action</code> appends the exact ID to immutable <code>brilliant_scientist_temporal_used_target_ids</code> and clears the binding. Every named crisis, component, leader, or bounded unit target receives one stable integer that is never reused for a different meaning.
- **Synchronization/debt:** information/object/bounded-unit actions cost 15/25/40 synchronization and add 15/25/40 temporal debt. Each target has one use. Debt warning/severe/critical bands are 40/70/90; no passive decay.
- **Anchor:** <code>brilliant_scientist_register_temporal_anchor</code> saves global event target <code>brilliant_scientist_temporal_anchor</code>; authentication is the separate country flag <code>brilliant_scientist_temporal_anchor_authenticated</code>. Capture of the state does not authenticate it.
- **Stabilization:** <code>brilliant_scientist_begin_temporal_stabilization</code> disables temporal actions, empties synchronization, occupies the primary facility, and creates a 180-day weakness window. <code>brilliant_scientist_complete_temporal_stabilization</code> reduces debt by 30 and restores synchronization. Anchor loss never erases debt, used-target records, or persistent scars.
- **Accident/countermeasure:** missing time → duplicate personnel → contradiction/command crisis. Counter through authenticated records, anchors, ledgers, and exploitation of the stabilization window.
- **KRG inheritance:** temporal cap 3; carry stages, evidence, exact used-target ledger, debt, scars, and valid anchor state. Never reset target uses on state formation.
- **Asset IDs:** <code>GFX_sp_brilliant_scientist_temporal_mechanics</code>, <code>GFX_brilliant_scientist_project_temporal</code>, <code>GFX_brilliant_scientist_temporal_guard_tech_medium</code>, equipment/unit/anchor/stabilization icons.
- **Unique reward:** <code>sp_brilliant_scientist_temporal_mechanics_reward_contradictory_record</code>.
- **AI:** uses temporal actions only for bounded strategic crises, never routine battles; begins stabilization when debt and security conditions justify the exposed window.

### 15. Strategic Singularity

- **Visibility and prerequisites:** KRG sovereignty, Evolution IV, High Energy at Weaponization, at least two of Teleportation/Temporal/Alien Arms/Robotics/Biological Weapons/Materials at Deployment or higher, at least three valid facilities, and an enabled selector ID 12. No host-state early-project shortcut.
- **New native component projects:** <code>sp_brilliant_scientist_singularity_command_core</code>, <code>sp_brilliant_scientist_singularity_power_link</code>, <code>sp_brilliant_scientist_singularity_containment_lattice</code>, <code>sp_brilliant_scientist_singularity_temporal_authenticator</code>, <code>sp_brilliant_scientist_singularity_delivery_architecture</code>, <code>sp_brilliant_scientist_singularity_fail_deadly_governor</code>.
- **Component enum:** <code>constant:brilliant_scientist_singularity_component.{command_core,power_link,containment_lattice,temporal_authenticator,delivery_architecture,fail_deadly_governor}</code> = 1 through 6.
- **Arming enum:** <code>constant:brilliant_scientist_singularity_arming_state.{dormant,theory,components,construction,arming,armed,disarming,verified_nonterminal,terminal}</code> = 0 through 8.
- **Specialization/facility assignments:** command core and delivery architecture use <code>specialization_air</code>/<code>air_facility</code>; containment lattice uses <code>specialization_land</code>/<code>land_facility</code>; power link, temporal authenticator, and fail-deadly governor use <code>specialization_nuclear</code>/<code>nuclear_facility</code>. Wrapper gates enforce the three-site/mixed-facility condition.
- **Native cost envelopes:** command core steel 6/tungsten 8/chromium 6/rubber 6, breakthrough 3, long/large; power link steel 8/tungsten 8/chromium 8/rubber 4, breakthrough 3, long/large; containment lattice steel 10/tungsten 6/chromium 10/rubber 3, breakthrough 3, long/insane; temporal authenticator steel 8/tungsten 10/chromium 10/rubber 4, breakthrough 4, very-long/insane; delivery architecture steel 10/tungsten 8/chromium 8/rubber 6, breakthrough 3, very-long/insane; fail-deadly governor steel 8/tungsten 10/chromium 10/rubber 6, breakthrough 4, very-long/insane.
- **Stages:** Theory selects the terminal mechanism; Prototype requires the first completed component and local catastrophic proof; Deployment requires all six components, core/delivery construction, at least two live command nodes and two power links; Weaponization is the separate 365-day arming process.
- **Component ledger:** reserve <code>brilliant_scientist_singularity_component_entries</code>, <code>brilliant_scientist_register_singularity_component</code>, and <code>brilliant_scientist_destroy_singularity_component</code>. The live architecture’s <code>brilliant_scientist_singularity_component_count</code> must equal six before terminal readiness.
- **Accident/countermeasure:** component anomaly → prototype catastrophe → premature terminal threat. Counter through component raids, disarmament, command-node conversion, delivery breakage, facility seizure, or survivable surrender.
- **KRG inheritance:** Singularity is KRG-only and not reconstructed from an ordinary host’s family stage. KRG retains exact surviving component/site state; lost components stay lost.
- **Asset IDs:** <code>GFX_&lt;component-project-id&gt;</code> for each of the six exact project IDs, <code>GFX_brilliant_scientist_project_singularity</code>, and <code>GFX_brilliant_scientist_singularity_armed_indicator</code>.
- **Unique rewards:** exact project ID plus one suffix: <code>_reward_false_arming_order</code>, <code>_reward_power_cascade</code>, <code>_reward_lattice_failure</code>, <code>_reward_contradictory_authentication</code>, <code>_reward_targeting_breach</code>, and <code>_reward_unauthorized_activation</code>, respectively.
- **AI:** never expose before prerequisites; weak KRG delays and stabilizes; construction AI defends all components; armed strong KRG uses deterrence unless its route permits deliberate use; near-capitulation failsafe remains blocked by survivable surrender or temporal escape.

## Strategic Singularity and the dedicated Fallout system

The Singularity must request the independent Fallout world-end system without creating a parallel terminal state or duplicating world-end cleanup. Event 016 owns super-event `94` as the Strategic Singularity presentation. Fallout separately owns its full-screen blackout, `chaosx.fallout` transition events, request ledger, world rewrite, audio wrappers, and final files.

Required bridge:

1. <code>brilliant_scientist_prepare_singularity_terminal_commit</code> verifies the six components, armed and fail-deadly state, live command network, KRG ownership, selector 12, and absence of another world end. It records regular event target <code>brilliant_scientist_terminal_source_actor</code>.
2. It calculates the deficit to <code>constant:chaos_meter_tier_range.tier_final.plus</code> and calls <code>add_chaos_meter_value</code> with history reason <code>constant:brilliant_scientist_singularity.chaos_history_reason</code> = 216.
3. Event 016 shows and records super-event `94` through its own settings-aware super-event package.
4. Event 016 supplies a parent-approved Fallout request source, a Fallout request intensity, and the verified actor context, then calls <code>fallout_request_aftermath</code>.
5. The Fallout coordinator validates the request and owns <code>world_end</code>, <code>world_end_fallout</code>, the blackout GUI, the <code>chaosx.fallout.*</code> sequence, and common rewrite cleanup.
6. Event 016 records <code>world_end_strategic_singularity</code> and its terminal-fired marker only after the Fallout request is accepted.
7. Event 016 clears its request context on success, cancellation, disarmament, invalid ownership, and every aborted attempt.

The exact Event 016 request-source mapping is parent-owned because the current Fallout source enum has no Event 016-specific entry. This map intentionally does not edit the dedicated Fallout files.

## New technology, unit, and equipment registry

| Family | Technology | Unit | Equipment archetype/type |
| --- | --- | --- | --- |
| Teleportation | <code>brilliant_scientist_portal_warfare_tech</code> | <code>portal_raider</code> | <code>teleportation_equipment</code>/<code>teleportation_equipment_1</code> |
| Cloning | <code>brilliant_scientist_clone_formations_tech</code> | <code>clone_infantry</code> | Shared <code>clone_equipment</code> plus ordinary infantry equipment |
| Robotics | <code>brilliant_scientist_robot_formations_tech</code> | <code>kruger_robot_frame</code> | <code>kruger_robot_equipment</code>/<code>kruger_robot_equipment_1</code> |
| Paleogenetics | <code>brilliant_scientist_paleogenetic_formations_tech</code> | <code>kruger_paleogenetic_beast</code> | <code>kruger_paleogenetic_equipment</code>/<code>kruger_paleogenetic_equipment_1</code> |
| Xenobiological synthesis | <code>brilliant_scientist_xenobiological_formations_tech</code> | <code>kruger_xenobiological_assault</code> | <code>kruger_xenobiological_equipment</code>/<code>kruger_xenobiological_equipment_1</code> |
| Temporal | <code>brilliant_scientist_temporal_guard_tech</code> | <code>kruger_temporal_guard</code> | <code>kruger_temporal_equipment</code>/<code>kruger_temporal_equipment_1</code> |
| Alien arms | <code>brilliant_scientist_exotic_guard_tech</code> | <code>kruger_exotic_guard</code> | <code>kruger_exotic_arms_equipment</code>/<code>kruger_exotic_arms_equipment_1</code> |

Every new equipment archetype must be added to <code>common/script_enums.txt</code> under <code>script_enum_equipment_bonus_type</code> in the same implementation change. The corresponding technology/equipment/unit icons and localisation are required; these are not placeholder-free merely because their identifiers are reserved.

## Foreign acquisition and countermeasure behavior

The family-indexed wrapper ledgers prevent publication, theft, or joint laboratories from becoming generic “all technology” grants:

- Publication may replicate only the published family and at most the published stage.
- Theft marks <code>brilliant_scientist_project_stolen_families</code> and grants bounded foreign knowledge through <code>brilliant_scientist_grant_foreign_project_knowledge</code>; repeat theft of the same completed family has diminished reward and escalating risk.
- Sabotage marks/damages/dismantles the exact family or component; it does not erase the host’s historical stage or the temporal used-target ledger.
- A countermeasure requires evidence or direct exposure and advances only the matching entry in <code>brilliant_scientist_project_countermeasure_entries</code>.
- Biological countermeasures call the canonical outbreak/quarantine/vaccine systems; Temporal countermeasures require authenticated records/anchor evidence; Singularity countermeasures target exact components; Paleogenetic and Xenobiological counters remain separate.
- No periodic world scan is required. Refresh explicit foreign actors during event/decision chains and preserve the current architecture’s explicit target validation and cleanup.

## KRG inheritance rule

<code>brilliant_scientist_inherit_kruger_carried_portfolio</code> reconstructs the character’s personal four-stage history, not the host’s institutional ledger. <code>brilliant_scientist_apply_project_inheritance_outputs</code> must then grant only outputs supported by the carried stage and exact sub-ledgers:

- no unpublished host-only technology;
- no independently replicated host branch unless Kruger personally carried it;
- no clone, robot, paleogenetic, xenobiological, portal, temporal, exotic, or biological force without its stage, technology, equipment/facility, cap, and production burden;
- no biological agent or stockpile without the exact personal agent flag;
- no Paleogenetic/Xenobiological merger before explicit Synthesis;
- no Temporal reset of debt, scars, anchors, or used target IDs;
- no Singularity reconstruction from a generic family stage.

The force caps already reserved are conventional 12, clones 8, robots 8, paleogenetic 6, xenobiological 6, portal 4, temporal 3, exotic 4, and biological 4. Force scale is zero at Theory, 0.25 at Prototype, 0.60 at Deployment, and 1.00 at Weaponization. These are ceilings, not free-spawn quantities.

## Asset registration boundary

All new native projects use exact icon key <code>GFX_&lt;project-id&gt;</code>. All fifteen Event 016 family cards use:

<code>GFX_brilliant_scientist_project_computation</code>,
<code>GFX_brilliant_scientist_project_electronics</code>,
<code>GFX_brilliant_scientist_project_materials</code>,
<code>GFX_brilliant_scientist_project_rocketry</code>,
<code>GFX_brilliant_scientist_project_high_energy</code>,
<code>GFX_brilliant_scientist_project_biomedical</code>,
<code>GFX_brilliant_scientist_project_teleportation</code>,
<code>GFX_brilliant_scientist_project_cloning</code>,
<code>GFX_brilliant_scientist_project_robotics</code>,
<code>GFX_brilliant_scientist_project_paleogenetics</code>,
<code>GFX_brilliant_scientist_project_xenobiological_synthesis</code>,
<code>GFX_brilliant_scientist_project_biological_weapons</code>,
<code>GFX_brilliant_scientist_project_alien_arms</code>,
<code>GFX_brilliant_scientist_project_temporal</code>, and
<code>GFX_brilliant_scientist_project_singularity</code>.

Reused native/Chaos Redux projects keep their registered icons. New technology medium icons use <code>GFX_&lt;technology-id&gt;_medium</code>. New equipment/unit/site/control icons require stable registrations before art production. No asset in this map is considered produced merely because a GFX key is reserved.

## Collision and reuse audit

Read-only scans covered:

- the full Chaos Redux repository;
- installed vanilla Hearts of Iron IV scripts and interface definitions;
- approved reference mods 1521695605, 2265420196, and 1458561226;
- Event 016 source/spec/plan documents and the current concurrent architecture.

Findings:

- No live Chaos Redux or vanilla definition exists for any reserved <code>sp_brilliant_scientist_*</code> project, <code>brilliant_scientist_*_tech</code> operational technology, <code>kruger_*</code> unit/equipment identifier, new wrapper, Paleogenetic/Xenobiological site/control marker, or Singularity pending/source adapter identifier in this handoff. The Temporal and alien-spacecraft cross-event flags are now implemented in the Event 030/Event 016 and Event 036/Event 016 bounded receipts described above.
- No <code>KRG</code> country definition exists in Chaos Redux or vanilla. The tag is clear in the inspected approved reference mods as well.
- Existing radar, rocket, nuclear, biological-agent, delivery-technology, bioweapon equipment, containment, contamination, Deaths, and Condemnation identifiers are live and must be reused.
- <code>sp_mengele_cloning</code> is live but is deliberately excluded from reuse because its country-specific availability and output contract do not represent Event 016.
- <code>antarctica_success</code> is a stable Event 025 gate. Event 036 now writes its narrow authenticated recovery marker and presents the bounded Event 016 spacecraft receipt described above. No live Teleportation Experiment implementation was found. Event 030 now has the bounded Event 016 temporal-contact receipt described above; no broader Event 030 variant or diplomacy chain is implied.
- Visible super-event slots 85 through 89 have Event 015 ownership evidence. Event 016 90 through 95 have no competing live selector/localisation/GFX owner; Event 016’s corrected audio files use those numbers.
- Event 016 world-end IDs 11 and 12 have no competing live world-end registry owner. The triggerable-scenario value 12 belongs to a different identifier namespace and is not a collision.

The scan cannot guarantee compatibility with arbitrary user-enabled mods outside vanilla and the three approved reference mods. Within the mandated and approved source set, the reserved identifiers are collision-free.

## Implementation order and unresolved integration ownership

1. Accept the current common family/stage/cost/facility/foreign/Temporal/Singularity architecture.
2. Define the ten single-family new projects and six Singularity component projects, with their constants, availability, native rewards, localisation, icons, and AI.
3. Bind reused vanilla/Chaos Redux projects into the family stage ledger without replacing their native clocks.
4. Implement the family accident, foreign knowledge, countermeasure, and inheritance-output wrappers.
5. Add the seven operational technologies, seven units, six new equipment archetype/type pairs, script-enum entries, production burdens, caps, AI, icons, and localisation.
6. Integrate Event 016 biological calls with the accepted canonical lifecycle API.
7. Add only the narrow Event 030/Event 036 cross-event flags if those exact outcomes are implemented.
8. Route Singularity through the parent-owned request bridge into `fallout_request_aftermath` while keeping visible super-event 94 as Event 016 presentation.
9. Run project, country-package, decision/mission, localisation, event-completion, and asset audits before claiming Event 016 completion.

This handoff contains no gameplay implementation and creates no fallback. The remaining work is explicit implementation work, not an omitted substitute.

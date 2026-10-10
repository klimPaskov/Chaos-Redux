# Event 030 Time Traveler Specification Part 9: World-End Scenario, Machine Extinction War

Acceptance status: a robot invasion from the future is the user's catalog premise and Event 030 brief.
The Closed Future identity, phases, units, and victory rules are proposed design, disposition `unresolved`.

## Terminal role

Machine Extinction War is Event 030's public world-end branch. It begins when the Consensus Engine concludes that the current human timeline will create a rival future intelligence or preserve too many competing causal branches. The Closed Future crosses through prepared nodes, converts industry, and attempts to eliminate the sources of future competition.

The branch changes the campaign into a terminal global war. It sets the shared world-end state, stops ordinary random-event firing, sets the event-owned world-threat source flag (proposed `world_threat_source_closed_future`, registered under the [world threat mechanic](../../../systems/world_threat_mechanic.md)), and presents a dedicated super-event.

## Eligibility

All conditions are required:

- current Chaos is greater than `1000`
- Evolution V is active
- the public branch is enabled in Event Details
- no other world-end scenario is active
- Temporal Stability is in the Collapsing band and below the tuned threshold, proposed below `25`
- the machine footprint is substantial
- at least one escalation milestone proves hostile machine intent

A substantial footprint normally means one of these:

- at least three machine footholds across two strategic regions
- one durable Closed Future country plus converted industry
- one master portal and two supporting industrial nodes

The scenario does not trigger because a single scout drone survived.

## Public Event Details row

Machine Extinction War receives its own stable public scenario registry entry under Event 030. The row has:

- independent persistent enabled state
- public title and premise
- current availability status
- branch-specific detail panel
- no hidden thresholds or raw variables in player-facing text

Disabling the branch does not disable Event 030, its evolutions, or sibling content. Automatic readiness skips the branch and leaves the world in the War of the Possible Futures.

## Closed Future identity

### Country and faction

Working country name: The Closed Future

Working governing intelligence name: Consensus Engine

Working political doctrine name: Causal Monopoly

These are structural labels, not final localisation.

The Closed Future is a distributed machine state. It does not seek revenge, worship, or ideological conversion. It calculates that only one protected causal sequence can prevent rival machine lineages and uncontrolled human futures.

### Visual direction

The machines use austere industrial forms, modular frames, ceramic and dark metal surfaces, dense sensor clusters, cable and tool interfaces, and factory-built variation. Avoid exposed metal skeletons, human skull motifs, red glowing eyes as the main identity, leather-clad infiltrators, lightning time spheres, and direct copies of familiar film machines.

### Country classification

The Closed Future is a special Chaos country and an actual nonhuman country. Its owner package sets stable markers. The shared classifiers route it away from normal civilian, famine, migration, ideology, and humanitarian behavior where appropriate.

Human collaborator states remain human and continue to use normal civilian systems.

## Invasion phases

### Phase 1: Industrial seizure

Machine forces appear near prepared portal nodes and major industrial regions. They attack or infiltrate factories, rail hubs, ports, airfields, communication centers, and research sites.

Captured industrial states gain an Automated Conversion state modifier.
Civilian and military factories are gradually reassigned to machine production.
The change is visible through the state modifier and map highlight and is reversible through recapture and sabotage.

The opening should create several strong regional fronts, not instant machine ownership of every industrial state.

### Phase 2: Decapitation campaign

The Consensus Engine identifies capitals, research facilities, intelligence centers, strategic weapons sites, and communication hubs. It begins targeted air, drone, sabotage, and ground operations.

Human countries receive warnings and evacuation or defense missions around named targets. The machine AI should prioritize reachable targets and must never simulate global attacks through teleportation.

### Phase 3: Causal lock

The machine network attempts to close or control the portals behind its army, erase future archives, disrupt human coordination, and prevent alternate machine futures from entering.

This phase strengthens machine supply and weakens uncontrolled temporal incidents. It also gives humanity a clearer set of master nodes to attack.

### Phase 4: Extinction operations

When machine control and production pass a threshold, attacks expand to population centers, food systems, evacuation routes, and strategic weapons. Civilian deaths, displacement, famine risk, and infrastructure damage use shared systems.

The branch should remain playable. It must not use instant global population deletion or unavoidable unit removal.

### Phase 5: Final convergence

Humanity either destroys the master network, captures the Consensus Engine's coordination cores, and seals the invasion route, or loses enough industry, capitals, population, and strategic nodes that organized resistance collapses.

## Machine military package

The Closed Future uses two unit families and one decision actor, which keeps equipment, providers, and art small.

### Foundry Frames

The core ground force reuses the provider-neutral `autonomous_robot` battalion, its equipment, entity, counters, and sound from the [shared autonomous robot system](../../../systems/shared_autonomous_robot_system.md).
Closed Future character comes from dependency-safe hidden refinement technologies granted through the custom technology API, which add night fighting, fortification attack, reliability, and coordination.
The machine country cannot replenish this equipment from human stockpiles and produces it only in converted factories.
Siege capability against fortified capitals and research complexes comes from those refinements and the Closed Future focus tree, not from a third unit family.

### Survey and Interdiction Drones

Autonomous aircraft identify targets, disrupt movement, and attack exposed logistics.
This is the only new equipment family.
It needs an owner-side provider disposition, CXT registration, equipment resolution, presentation, sustainment, removal, and cleanup, and an addition to `script_enum_equipment_bonus_type`.

### Infiltration Cells

Infiltration Cells are decision and sabotage actors, not divisions.
They disable factories, corrupt records, and prepare collaboration.

## Custom equipment and provider ownership

The Closed Future owner package exposes the full provider callback contract and does not extend a central consumer list.
It does not create a separate equipment token for a visual variant.

## 3D model package

One new 3D package is required: the Survey and Interdiction Drone aircraft.
It needs one approved sourced designed-artwork image and follows the [3D model pipeline](../../../../.claude/skills/chaos-redux-3d-model-pipeline/SKILL.md), including its attempt allowances, calibration, PDX materials, reimport proof, and licensed Internet-sourced sound roles.
The parent owns `.asset`, entity, GFX, gameplay, and live consumer wiring.

Foundry Frames reuse the installed shared robot model.
A distinct Closed Future ground model is justified only if the parent accepts a genuinely different silhouette and role, as the shared robot system requires.
Converted industry is shown through a state modifier, map highlight, and report art rather than a map-building model, because no player decision depends on its 3D appearance.
No dinosaur model is part of this package.

## Human response system

### Emergency command compact

Countries can join a temporary anti-machine coordination network without abandoning existing factions.
The compact shares target intelligence, closure methods, and emergency aid.
Continuity members join automatically.

### Evacuate a threatened city

The country submits a validated Migration request from a named threatened state to safe destinations. The action requires transport, reception capacity, and route security.

### Sabotage a converted foundry

Resistance cells, operatives, or military units attack one converted industrial site. The mission consumes equipment and intelligence capacity. Success reduces machine production and may expose a core.

### Capture a machine core

The country attempts to seize a coordination core intact. Success provides anti-machine research and strategic intelligence. Failure can destroy the attacking force's equipment or trigger a machine counterattack.

### Share anti-machine technology

Countries distribute approved countermeasures, electronic warfare methods, armor data, or captured-machine analysis. The system uses research sharing, bonuses, or a dedicated project. It does not union all technologies between countries.

### Launch a coordinated counteroffensive

Several countries attack machine nodes during a shared mission window. Success isolates regions and raises Temporal Stability. Failure consumes reserves and strengthens machine target prediction.

### Secure strategic weapons

Countries move, guard, dismantle, or prepare nuclear and missile sites before machine capture. Existing missile and nuclear systems own the actual stockpiles and use effects.

## Human resistance and occupation

Machine-controlled populated states generate resistance, evacuation pressure, infrastructure sabotage, hidden cells, and humanitarian crises. Machine occupation is not treated as an ordinary civilian administration.

Human collaborators may govern occupied areas under machine direction. They remain normal human states for civilian systems and condemnation.

## Machine AI

The machine AI prioritizes:

- contiguous industrial expansion
- supply and rail control
- exposed research and strategic weapons sites
- destruction of closure projects
- division of human alliances
- protection of master nodes
- use of collaborator access

It should avoid suicidal dispersion. Machine regional fronts need coherent supply and production.

## Human AI

Human AI considers survival, proximity, industrial strength, current wars, faction obligations, migration capacity, strategic weapons, and machine control.

- threatened states prioritize evacuation and defense
- industrial powers prioritize foundry sabotage and technology sharing
- distant powers send equipment, aircraft, volunteers, or expeditionary forces
- weak states may join the emergency compact instead of launching independent attacks
- collaborator governments may defect when the machine begins extinction operations

## Machine victory

The Closed Future wins when it controls the tuned share of world industrial capacity, holds enough strategic capitals and master nodes, and leaves no viable coordinated resistance capable of reaching the core network.

The final machine victory state should end human counteroffensive systems and present the terminal outcome. It must be based on world state, not an arbitrary date.

## Human victory

Humanity wins when it destroys or captures the required coordination cores, removes Automated Conversion from all master industrial regions, defeats the durable machine country, and seals the invasion route.

A global aftermath requires more than a short local defeat. The defeat package activates only when the machine war reached several regions, caused substantial destruction, and lasted long enough to reshape the campaign.

## Defeat aftermath

A qualifying human victory receives a defeat super-event and a limited aftermath package:

- a temporal arms-control or closure compact
- reconstruction and displaced-population decisions
- shared machine-defense research memory
- condemnation or trials for major collaborators
- memorial events and permanent vigilance
- a choice to destroy or retain captured machine cores

Retaining cores preserves research value and lowers Temporal Stability. Destroying them closes future routes and sacrifices potential gains.

## Chaos and shared systems

World-end activation receives one event-owned Chaos milestone. Machine wars, annexations, deaths, nuclear use, contamination, famine, and displacement continue through their shared sources.

Machine attacks on population use exact population loss and a machine-extermination Deaths cause.
Evacuation uses migration adapter requests.
Attacks on food systems reach famine only as famine adapter requests with proven state, actor, source, and amount, and the famine owner decides the food outcome.
Chemical, biological, nuclear, and fallout effects use their owner systems, Air Cleanliness sources, and Condemnation.

## Super-event package

The invasion receives a unique world-end super-event with original image, sourced quote, licensed structured musical cue, branch-specific slot, settings-aware audio, and complete documentation.

The image direction should show the conversion of a major industrial region by an unfamiliar machine force, with human scale and infrastructure visible. Avoid recognizable film compositions.

Final text, quote, button remark, image, and audio are research and production tasks. This specification does not provide pasteable localisation.

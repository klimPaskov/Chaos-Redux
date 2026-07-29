# Event 016 project portfolio implementation handoff

## Scope and status

This handoff covers the isolated Event 016 project-portfolio tranche. It does not claim completion of the full Event 016 package.

All fifteen requested families have persistent Theory, Prototype, Deployment, and Weaponization progression: Computation, Electronics, Materials, Rocketry, High Energy, Biomedical, Teleportation, Cloning, Robotics, Paleogenetics, Xenobiological Synthesis, Biological Weapons, Alien Arms, Temporal, and Strategic Singularity.

The implementation includes exact prerequisites, tuned stage burdens and durations, native Prototype clocks, capacity occupation, family-specific cumulative outputs, project-specific prototype hazards, fifteen incident missions and repair actions, suspension and dismantling behavior, AI weights, exact project history, and nonterminal Strategic Singularity preparation.

## Files

Modified:

- `common/decisions/016_brilliant_scientist_directorate_project_board.txt`

Added:

- `common/script_constants/016_brilliant_scientist_project_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt`
- `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`
- `common/technologies/016_brilliant_scientist_project_technologies.txt`
- `common/special_projects/projects/016_brilliant_scientist_projects.txt`
- `common/on_actions/016_brilliant_scientist_project_on_actions.txt`
- `localisation/english/016_brilliant_scientist_projects_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/projects.md`
- this handoff

The tranche does not edit the parent-owned Event 016 effect or trigger files, incident event namespace, opening events, evolutions, containment, KRG focus work, super events, achievements, specs, or asset manifest.

## Identifier coverage

- 45 direct stage decisions: Theory, Deployment, and Weaponization for each family.
- 15 Prototype integration decisions, one for each family, so a completed native project can be recorded later if Project Capacity was unavailable at project completion.
- 16 new native projects: ten family prototypes and six exact Strategic Singularity components.
- 15 incident missions and 15 matching response decisions.
- 60 cumulative family-stage dynamic modifiers and 15 family incident penalties.
- 11 project-granted hidden operational technologies: seven stable family bridges plus four mutually exclusive Xenobiological control packages.
- Four mutually exclusive Xenobiological control decisions.
- One repeatable facility audit, two command-node constructions, and two power-link constructions for Strategic Singularity preparation.
- No `chaosx.nr16.*` event IDs were allocated.

New Prototype projects:

- `sp_brilliant_scientist_computational_engine`
- `sp_brilliant_scientist_advanced_materials`
- `sp_brilliant_scientist_biomedical_acceleration`
- `sp_brilliant_scientist_quantum_transit`
- `sp_brilliant_scientist_cloning`
- `sp_brilliant_scientist_autonomous_cognition`
- `sp_brilliant_scientist_paleogenetics`
- `sp_brilliant_scientist_xenobiological_synthesis`
- `sp_brilliant_scientist_alien_arms`
- `sp_brilliant_scientist_temporal_mechanics`
- `sp_brilliant_scientist_singularity_command_core`
- `sp_brilliant_scientist_singularity_power_link`
- `sp_brilliant_scientist_singularity_containment_lattice`
- `sp_brilliant_scientist_singularity_temporal_authenticator`
- `sp_brilliant_scientist_singularity_delivery_architecture`
- `sp_brilliant_scientist_singularity_fail_deadly_governor`

## Exact live reuse

Electronics records `sp_air_radar`. Rocketry records the live flying-bomb or jet-engine Prototype path and later requires the exact axial-jet, supersonic, ballistic-missile, or long-range-ballistic-missile projects. High Energy records `sp_nuclear_reactor` and later consumes the live commercial-reactor, nuclear-bomb, thermonuclear-bomb, or nuclear-warhead progression. Biological Weapons records the exact Anthrax, Plague, Tularemia, Smallpox, and Weaponized Zombies projects and preserves the individual agent results on Kruger's character.

The technology gates resolve to live vanilla or Chaos Redux identifiers, including the computing-machine chain, radar chain, machine tools and assembly lines, construction and excavation, rocketry, atomic research, epidemiology, mobile CBRN hospitals, containment, surveillance, and epidemic-control technologies.

No native Prototype is charged a second Event 016 Prototype cost. The native facility clock, breakthrough cost, resources, and iteration rewards are the Prototype cost. Event 016 occupies its ten Prototype-capacity points only when the completion can be recorded; otherwise the matching integration decision waits for available capacity.

## Capacity, costs, and incidents

A family occupies 10, 20, 35, or 50 Project Capacity at Theory, Prototype, Deployment, or Weaponization. Suspending releases half the retained burden, resuming requires and reoccupies the same amount, and dismantling releases the remainder. Completed operational modifiers and site readiness are disabled or removed as appropriate, while learned hidden technologies and history flags remain learned history.

Stage costs are explicit script constants derived from the shared family profiles. Decisions occupy civilian factories and consume Support Equipment, trucks, trains, fuel, manpower, relevant military experience, and Political Power. Military factories and relevant strategic resources are exact availability gates. The engine exposes `civilian_factory_use` for timed decisions but no equivalent `military_factory_use`; therefore military production burden is represented by the military-factory gate plus consumed materiel and logistics, not by an invented or unsupported modifier.

Incident pressure is a live variable weight. Each family activates its own mission, penalty, and response. Technical, industrial, biological, and exotic repairs take 60, 90, 120, or 150 days; their deadlines are separately 120, 150, 180, or 240 days. A timeout damages only the exact family and applies stability and war-support harm, while late recovery remains possible. Repeated incidents clear the matching old resolved marker before activating the new mission.

## Military distinctions

No free units, equipment, or placeholder archetypes are created. Existing formations receive stable project-granted technologies only at Weaponization:

- Teleportation strengthens paratroopers and reduces their supply burden.
- Cloning strengthens ordinary infantry formations.
- Robotics strengthens motorized and mechanized formations.
- Paleogenetics strengthens cavalry while retaining an added supply burden.
- Xenobiological Synthesis strengthens marines and mountaineers and then applies exactly one control method: defensive but supply-heavy chemical signaling, cohesive neural control, hard-target machine control, or balanced supply-efficient researched control.
- Temporal strengthens specialist guard formations without resetting debt or target history.
- Alien Arms strengthens infantry and motorized formations without creating alien equipment.

Paleogenetic reserves and hatcheries remain separate from Xenobiological vats and control centers. Biological agent history remains exact rather than inferred from a generic family flag.

## Strategic Singularity guard

The six-component array, exact component flags, certification of three distinct facility states, two live command nodes, two power links, architecture flag, preparation flag, and guarded-contract flag are exposed for parent consumers. Facility sufficiency is rechecked at component research and every later stage; the audit flag cannot substitute for facilities that were subsequently lost.

Theory locks the existing terminal commitment contract. Prototype records components. Deployment records construction. Weaponization remains at the `construction` arming state, sets `brilliant_scientist_singularity_prepared_nonterminal` and `brilliant_scientist_singularity_terminal_contract_guarded`, and explicitly clears the armed and fail-deadly flags.

Theory and Prototype can be dismantled safely and release the terminal commitment. Deployment and Weaponization are blocked from generic dismantling until the parent-owned disarmament hold is wired. This tranche never arms, detonates, calls Fallout, fires a super event, sets `world_end`, or marks a terminal as fired.

## Validation evidence

- All 45 stage decisions, 15 Prototype integrations, 15 missions, 15 responses, 16 projects, and 11 operational technologies are present exactly once.
- Every new decision, modifier, project, technology, reward, tooltip, and explicit cost-text reference resolves to English localisation.
- All 27 referenced live special-project identifiers and all 21 technology prerequisite identifiers resolve in Chaos Redux or the installed vanilla game.
- Every reused icon key resolves to a registered Chaos Redux or vanilla sprite. No missing sprite key or new `.gfx` file is wired.
- The on-action surface contains only `on_project_completion`; no daily, weekly, monthly, or whole-world recurring iteration was added.
- The owned files contain no Event 016 incident event IDs and no terminal world-end effect.

## Integration work and boundaries

- Parent KRG/focus, containment, evolution, event-detail, spreadsheet, and terminal consumers may read the stable flags above without changing these owned files.
- A parent-owned disarmament action must satisfy the existing disarmament hold before deployed Singularity dismantling can be enabled.
- Dedicated family and project art is not present. Existing registered project and decision icons are intentionally reused; no missing asset is claimed or wired.
- Bespoke new unit and equipment definitions were outside this tranche. Military distinctions are implemented with existing formation categories and no free materiel. A later authorized unit/equipment package must preserve the stable `*_military_package_ready` flags and must not merge Paleogenetics, Xenobiological Synthesis, Cloning, Robotics, Alien Arms, or Biological Weapons into one generic formation.

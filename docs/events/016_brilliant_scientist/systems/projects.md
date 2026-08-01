# Event 016 Brilliant Scientist project portfolio

## Purpose

This system turns the Kruger Directorate's fifteen project families into a persistent four-stage portfolio. Theory, Prototype, Deployment, and Weaponization are separate ledger states. A family can advance only through its exact predecessor, its scientific prerequisites, a valid Directorate facility, available Project Capacity, and a concrete industrial and logistical burden.

The system does not create free units, free equipment, generic technology grants, or a Political Power storefront. Native Hearts of Iron IV and Chaos Redux projects keep their own clocks, resources, prototype rewards, and outputs. Event 016 records those exact completions instead of cloning them.

## Player flow

1. Establish the Directorate and a valid primary facility.
2. Authorize a family's Theory decision. The decision consumes equipment, personnel, fuel, relevant experience, Political Power, strategic-resource access, and factory time according to the common stage baseline multiplied by that family's profile.
3. Complete the family's native Prototype:
   - Ten families use new Event 016 native projects.
   - Electronics, Rocketry, High Energy, and Biological Weapons reuse existing live projects.
   - Strategic Singularity uses six exact component projects.
4. Advance Deployment only after the native prototype and the mapped technology, project, site, or stockpile prerequisites are present.
5. Advance Weaponization only after the mapped late prerequisites. The stage adds a family-specific military or institutional output and a persistent history record.
6. Every completed stage recalculates accident pressure from Exposure, stage burden, project condition, and suspension state. A failed pressure roll activates the exact family's incident mission and recovery action.
7. Suspending a project releases half its occupied capacity. Resuming reoccupies that half. Dismantling releases the remaining burden while historical flags and Kruger's personal character history remain available to the wider Event 016 architecture.
8. The first completed Prototype in each family reserves one ordinary `chaosx.nr16.6` report. Public publication and classified retention adjust the existing Directorate values, but the report never grants a second project-stage reward. If several families reach Prototype in one synchronization pass, later families enter `brilliant_scientist_breakthrough_pending_families` and are dispatched in order after the current report closes.

The first valid primary facility after a resolved Prototype can then receive `chaosx.nr16.7`, and the second resolved Prototype can receive `chaosx.nr16.8`. These reports settle facility terms and method custody as persistent governance receipts rather than advancing a project. A detected foreign operation resolved after any Prototype can schedule `chaosx.nr16.9`, which retains the named actor and operation and offers a bounded diplomatic response. None of these three reports creates another project reward, evolution, or event-log entry.

Prototype projects are not charged a second wrapper clock. Their native facility time, breakthrough points, resources, and prototype iterations are the prototype cost.

## Stage and capacity contract

| Stage | Persistent ledger value | Additional occupied capacity | Baseline wrapper duration source |
| --- | ---: | ---: | --- |
| Theory | 1 | 10 | `constant:brilliant_scientist_project_duration.<family>_theory` |
| Prototype | 2 | 10 | Native project clock |
| Deployment | 3 | 15 | `constant:brilliant_scientist_project_duration.<family>_deployment` |
| Weaponization | 4 | 15 | `constant:brilliant_scientist_project_duration.<family>_weaponization` |

A completed family therefore occupies 10, 20, 35, or 50 capacity at its current stage. The shared arrays remain the source of truth:

- `brilliant_scientist_project_stage_entries`
- `brilliant_scientist_independent_project_stage_entries`
- `brilliant_scientist_project_suspended_families`
- `brilliant_scientist_project_damaged_families`
- `brilliant_scientist_project_dismantled_families`
- `brilliant_scientist_project_published_families`
- `brilliant_scientist_project_stolen_families`
- `brilliant_scientist_breakthrough_reported_families`
- `brilliant_scientist_breakthrough_pending_families`
- `brilliant_scientist_breakthrough_public_families`
- `brilliant_scientist_breakthrough_classified_families`
- `brilliant_scientist_breakthrough_resolved_count`
- `brilliant_scientist_breakthrough_public_count`
- `brilliant_scientist_breakthrough_classified_count`

The country arrays reserve and queue reports while a host owns the Directorate. Dispatch also writes a pending receipt on the single `KRG_warren_kruger` character before the delayed event appears; resolution clears that pending flag and writes reported plus public or classified governance receipts. Transfer and Kruger State formation carry the reserved arrays, governance arrays, counts, and any active report across the handoff. The host-context policy flags and pending `.4` or `.5` obligation are carried without replaying their value deltas. The first resolved report uses full strength, the next two use half strength, and later reports use quarter strength. These character-level receipts survive transfer and Kruger State formation, so a recipient can inherit project history without replaying the first-Prototype governance choice.

## Family implementation map

| Family | Prototype source | Deployment and Weaponization direction | Persistent distinguishing output |
| --- | --- | --- | --- |
| Computation | `sp_brilliant_scientist_computational_engine` | Improved and Advanced Computing Machine | Cryptanalysis, auditable planning, and command-network modifiers |
| Electronics | Existing `sp_air_radar` | Radio Detection, Centimetric Radar, or Phased Array | Detection, guidance, air-mission, and anti-air coordination |
| Materials | `sp_brilliant_scientist_advanced_materials` | Advanced tools, assembly lines, Construction IV, Excavation V | Industrial throughput, resource efficiency, repair, and hardened production |
| Rocketry | Existing flying-bomb or jet-engine project | Ballistic or axial propulsion, then long-range missile or supersonic flight | Propulsion, guidance, air-mission, and strategic-delivery effects |
| High Energy | Existing `sp_nuclear_reactor` | Commercial reactor or bomb, then thermonuclear bomb or warheads | Reactor industry, fuel, nuclear production, and strategic energy |
| Biomedical | `sp_brilliant_scientist_biomedical_acceleration` | Epidemiology or mobile hospitals, then integrated epidemic control and fail-safe containment | Medical reinforcement, reduced experience loss, and protective logistics |
| Teleportation | `sp_brilliant_scientist_quantum_transit` | Two calibrated terminals plus advanced Computation and High Energy | Terminal state flags and `brilliant_scientist_portal_warfare_tech` |
| Cloning | `sp_brilliant_scientist_cloning` | Biomedical Deployment, containment, and a recorded growth site | Growth-site history and `brilliant_scientist_clone_formations_tech` |
| Robotics | `sp_brilliant_scientist_autonomous_cognition` | Computation, Electronics, Materials, and assembly-line integration | Assembly-complex history and `brilliant_scientist_robot_formations_tech` |
| Paleogenetics | `sp_brilliant_scientist_paleogenetics` | Biomedical and Cloning plus separate reserve and hatchery sites | Terrestrial reserve and hatchery flags plus `brilliant_scientist_paleogenetic_formations_tech` |
| Xenobiological Synthesis | `sp_brilliant_scientist_xenobiological_synthesis` | One exclusive control method plus separate vat and control sites | Exact control flag, separate xeno site flags, base assault procedures, and one of four control-specific operational technologies |
| Biological Weapons | Existing Anthrax, Plague, Tularemia, Smallpox, or Weaponized Zombies projects | Two exact agents and real stockpile, then Smallpox or Weaponized Zombies | Exact personal agent flags and existing agent technologies and equipment |
| Alien Arms | `sp_brilliant_scientist_alien_arms` | Antarctic or spacecraft evidence plus Materials and High Energy | Interface-chamber history and `brilliant_scientist_exotic_guard_tech` |
| Temporal | `sp_brilliant_scientist_temporal_mechanics` | Authenticated anchor, immutable target uses, synchronization, and debt | Existing temporal ledger plus `brilliant_scientist_temporal_guard_tech` |
| Strategic Singularity | Six `sp_brilliant_scientist_singularity_*` components | Six components, two command nodes, two power links, then guarded certification | Component array, exact component flags, site counts, and nonterminal preparation flags |

Paleogenetics and Xenobiological Synthesis do not share sites, control flags, maintenance assumptions, or incident state. Biological Weapons do not infer an agent from the family stage. The exact character flags are:

Xenobiological control remains mechanically exclusive. Chemical signaling improves specialist defense at an added supply burden. Neural bonding improves organization and soft attack. Machine mediation emphasizes hard attack and breakthrough. The researched protocol takes longer and costs more to select, then produces the most supply-efficient balanced package. The base `brilliant_scientist_xenobiological_formations_tech` remains the stable family output, while exactly one `brilliant_scientist_xeno_<method>_control_tech` records and applies the selected control architecture.

- `brilliant_scientist_personal_biological_agent_anthrax`
- `brilliant_scientist_personal_biological_agent_plague`
- `brilliant_scientist_personal_biological_agent_tularemia`
- `brilliant_scientist_personal_biological_agent_smallpox`
- `brilliant_scientist_personal_biological_agent_weaponized_zombies`

## Costs and duration

The exact wrapper costs in `constant:brilliant_scientist_project_stage_cost.*` are rounded products of:

- the shared Theory, Deployment, and Weaponization baselines in `constant:brilliant_scientist_project_cost.*`
- the family profiles in `constant:brilliant_scientist_project_profile.*`

Each stage checks and then consumes the exact Support Equipment, trucks, trains, fuel, manpower, and relevant experience. Political Power is paid through the decision cost. Civilian factories remain occupied for the full decision clock. Military factories and relevant strategic resources are explicit start gates. Prototype projects drain their own steel, tungsten, chromium, and rubber through the native special-project system.

## Accidents and recovery

`brilliant_scientist_refresh_project_accident_pressure` computes the live pressure. `brilliant_scientist_dispatch_project_accident` uses that variable as the random weight. An incident records:

- the exact family;
- a persistent incident count;
- a family-specific dynamic penalty;
- the common dangerous-project history flag;
- damage to the exact family when pressure is severe or the recovery deadline expires.

Every family has its own mission and response action. Technical, industrial, biological, and exotic response classes use different durations and burdens. A timeout damages the family and imposes national stability and war-support losses, but the late recovery action remains available. Recovery removes only the matching family penalty and repairs only the matching ledger entry.

Repair operations last 60, 90, 120, or 150 days by response class. Their incident deadlines are separately tuned to 120, 150, 180, or 240 days, so an operation begun before the deadline has a real completion window. A repeated incident clears only the matching family's prior resolved marker before activating its new mission.

New native projects also have one project-specific prototype reward with a cautious verification option and a live-test option. Caution loses prototype progress. The live test immediately checks the matching family's current accident pressure.

## Artificial intelligence

Every stage decision has a nonzero family priority only after its exact visibility and availability gates pass. War raises the value of military families. Low Project Capacity lowers all project weights. Taboo and exotic families use lower base weights. Strategic Singularity cannot appear to ordinary hosts because its gate requires:

- KRG sovereignty;
- recorded Evolution IV chronology;
- High Energy at Weaponization;
- two advanced supporting families at Deployment;
- three certified facility states;
- an enabled Strategic Singularity selector.

Native project AI uses the same host and capacity conditions and retains the engine's facility and breakthrough requirements. Incident recovery is urgent.

## Strategic Singularity guard contract

This tranche researches and prepares the Strategic Singularity. It does not arm, detonate, fire a super-event, request Fallout, set `world_end`, or perform terminal cleanup.

The guarded consumer contract is:

- `brilliant_scientist_singularity_component_entries`
- `brilliant_scientist_singularity_component_count`
- six exact `brilliant_scientist_singularity_<component>_complete` flags
- `brilliant_scientist_singularity_live_command_node_count`
- `brilliant_scientist_singularity_power_link_count`
- `brilliant_scientist_singularity_architecture_integrated`
- `brilliant_scientist_singularity_prepared_nonterminal`
- `brilliant_scientist_singularity_terminal_contract_guarded`

Weaponization certification leaves `brilliant_scientist_singularity_arming_state` at `construction` and explicitly clears `brilliant_scientist_singularity_armed` and `brilliant_scientist_singularity_fail_deadly_active`. A parent-owned terminal implementation must perform a separate authorized arming process and revalidate every terminal prerequisite. Theory or Prototype can be dismantled safely and release the terminal commitment. Deployment and Weaponization cannot use the generic dismantle action until a parent-owned disarmament hold has completed.

## Files

- `common/decisions/016_brilliant_scientist_directorate_project_board.txt`
- `common/script_constants/016_brilliant_scientist_project_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt`
- `common/scripted_triggers/016_brilliant_scientist_breakthrough_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt`
- `common/scripted_effects/016_brilliant_scientist_breakthrough_effects.txt`
- `common/dynamic_modifiers/016_brilliant_scientist_project_modifiers.txt`
- `common/special_projects/projects/016_brilliant_scientist_projects.txt`
- `common/technologies/016_brilliant_scientist_project_technologies.txt`
- `common/on_actions/016_brilliant_scientist_project_on_actions.txt`
- `localisation/english/016_brilliant_scientist_projects_l_english.yml`

## Icons and visual assets

No missing sprite is registered or referenced. New projects intentionally reuse registered Chaos Redux or vanilla special-project icons that match their facility class. The decision layer uses existing generic research and operation icons.

Dedicated project art remains a separate asset task. Stable future keys are the exact `GFX_<project_id>` keys listed in the Event 016 reuse identifier map, plus one family-card key `GFX_brilliant_scientist_project_<family>`. Their eventual DDS files should live under `gfx/interface/special_project/016_brilliant_scientist/` and be registered in an Event 016 project-specific `.gfx` file. Nothing in this tranche claims those assets already exist.

## Future plans

- Produce and register dedicated project and family-card art, then replace only the intentional registered-icon reuse.
- Add exact bespoke unit and equipment production packages if a later parent-owned tranche expands the authorized surface. The current operational technologies strengthen existing formations and create no free materiel.
- Add KRG focus and AI consumers for the family-specific `*_military_package_ready` flags.
- Connect a separately authorized Singularity arming process to the guarded preparation contract.
- Add foreign knowledge and countermeasure consumers without periodic world scans.

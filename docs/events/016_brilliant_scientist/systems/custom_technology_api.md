# Reusable Kruger custom technology API

Event 016 exposes its eighteen custom technologies through country-scoped scripted effects so other events can award the same knowledge without pretending that Warren Kruger, his Directorate, or an Event 016 laboratory performed the discovery.

This custom API never grants vanilla computing, radar, industry, rocketry, nuclear, medical, or CBRN technologies. It also never creates Event 016 project history, project stages, facilities, Kruger ownership, free formations, equipment stockpiles, or event-log entries.

## Public grant effects

`chaosx_grant_custom_operational_technology` accepts the temporary selector `chaosx_custom_technology_family`. The seven valid values are `constant:chaosx_custom_technology_family.portal`, `.clone`, `.robot`, `.paleogenetic`, `.xenobiological`, `.alien_infantry`, and `.temporal`. A valid call grants the matching base custom technology, records an external knowledge flag, and rebuilds the existing runtime consumers. `chaosx_custom_technology_grant_applied` reports `1` for a valid selector and `0` for an invalid selector.

`chaosx_grant_custom_technology_upgrade` accepts the temporary selector `chaosx_custom_technology_upgrade`. The valid values are the seven `*_weaponization` entries and the four `xeno_*_control` entries defined in `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt`. The effect grants the matching operational base first, then the selected upgrade, so no weaponization or control technology can be awarded without its static dependency. `chaosx_custom_technology_upgrade_applied` reports whether the selector was valid.

`chaosx_grant_random_custom_operational_technology` has no input selector. It chooses with the equal `constant:chaosx_custom_technology_tuning.random_candidate_weight` from operational families the country does not yet know and does nothing after all seven have been learned. `chaosx_custom_technology_random_grant_applied` reports whether a family was selected.

Example:

```text
set_temp_variable = { chaosx_custom_technology_family = constant:chaosx_custom_technology_family.robot }
chaosx_grant_custom_operational_technology = yes
```

## Separate conventional technology package API

The separate `chaosx_grant_conventional_technology_package` API covers six existing conventional Event 016 project families: Computation, Electronics, Materials, Rocketry, High Energy, and Biomedical.
Its selectors use the existing `brilliant_scientist_project_family` IDs and the existing `Deployment` or `Weaponization` stage IDs, so it adds no technology, project-family, stage, or random-family ID.
Deployment sets `conventional_technology_<family>_operational`; Weaponization sets both that operational flag and `conventional_technology_<family>_weaponized`, then `chaosx_reconcile_conventional_technology_runtime` reapplies the existing full-strength Theory, Prototype, Deployment, and Weaponization dynamic modifiers.
Computation uses one shared `conventional_technology_computation_research_slot_active` owner marker, adopts an existing native computation marker without adding a second slot, and is also reached by `chaosx_reconcile_custom_technology_runtime` after the Event 016 force rebuild.
The eight paid strategic actions are visible from the neutral weaponized flags through the ordinary `conventional_technology_operations` category rather than Kruger project-history flags; their target, payment, timer, cancellation/refund, cooldown, and AI consumers remain action-owned.
The six-package API is separate from the seven-family custom random helper, which remains unchanged and never selects a conventional package.

## Technology map

| Family | Operational technology | Upgrade technology |
| --- | --- | --- |
| Portal warfare | `brilliant_scientist_portal_warfare_tech` | `brilliant_scientist_portal_warfare_weaponization_tech` |
| Clone formations | `brilliant_scientist_clone_formations_tech` | `brilliant_scientist_clone_formations_weaponization_tech` |
| Robot formations | `brilliant_scientist_robot_formations_tech` | `brilliant_scientist_robot_formations_weaponization_tech` |
| Paleogenetic formations | `brilliant_scientist_paleogenetic_formations_tech` | `brilliant_scientist_paleogenetic_formations_weaponization_tech` |
| Xenobiological formations | `brilliant_scientist_xenobiological_formations_tech` | `brilliant_scientist_xenobiological_formations_weaponization_tech` |
| Alien infantry | `brilliant_scientist_alien_infantry_tech` | `brilliant_scientist_alien_predictive_warfare_tech` |
| Temporal guard | `brilliant_scientist_temporal_guard_tech` | `brilliant_scientist_temporal_guard_weaponization_tech` |

The four xenobiological refinements are `brilliant_scientist_xeno_chemical_control_tech`, `brilliant_scientist_xeno_neural_control_tech`, `brilliant_scientist_xeno_machine_control_tech`, and `brilliant_scientist_xeno_researched_control_tech`.

## Power profile

The operational and weaponization technologies are intentionally late-game prize technologies rather than ordinary research increments. The operational technology makes the associated force immediately exceptional, while the dependency-safe weaponization upgrade creates a second cumulative leap.
The values below are the modifiers in the static technology definitions, while unit base chassis values come from `common/script_constants/016_brilliant_scientist_project_force_constants.txt`; the current autonomous-robot chassis is 88% hardness, 70 armor, 60 breakthrough, 50 defense, 36 soft attack, 30 hard attack, 75 piercing, and speed 7.
Each weaponization column lists the additional static technology block, and the operational and weaponization blocks are cumulative when both are learned.

| Family | Operational technology effect | Additional weaponization effect |
| --- | --- | --- |
| Portal warfare | Enables `portal_raider` and `teleportation_equipment_1`; `portal_raider` receives +20 maximum organization, +50% breakthrough, and -25% supply consumption | `portal_raider` receives another +20 maximum organization, +50% breakthrough, and -25% supply consumption |
| Clone formations | Enables `clone_infantry` and `clone_equipment_1`; `clone_infantry` receives +8 maximum organization, +15% defense, and +15% soft attack | `clone_infantry` receives +20 maximum organization, +85% soft attack, +85% defense, +85% breakthrough, +50% default morale, -50% experience loss, and +30% casualty trickleback |
| Robot formations | Enables `autonomous_robot` and `autonomous_robot_equipment_1`; `autonomous_robot` receives +50% hard attack, +50% breakthrough, +50% defense, and +20 maximum organization | `autonomous_robot` receives another +50% hard attack, +50% breakthrough, and +50% reliability |
| Paleogenetic formations | Enables `paleogenetic_creature` and `paleogenetic_creature_equipment_1`; the creature receives +50% soft attack, +50% breakthrough, and +25% supply consumption burden | `paleogenetic_creature` receives another +50% soft attack, +50% breakthrough, and +25% maximum speed |
| Xenobiological formations | Enables `xenobiological_assault_organism` and `xenobiological_assault_organism_equipment_1`; the organism receives +50% soft attack, +25% hard attack, +8 maximum organization, and +50% breakthrough | `xenobiological_assault_organism` receives another +50% soft attack, +75% hard attack, and +50% breakthrough |
| Alien infantry | Enables `alien_laser_weapon_equipment_1`; the landing cohort is supplied by the shared API and remains outside ordinary recruitment | Enables `tactic_alien_predictive_vector_assault` and `tactic_alien_probability_screen`, with no additional numeric unit modifier |
| Temporal guard | Enables `temporal_guard` and `temporal_guard_equipment_1`; `temporal_guard` receives +20 maximum organization and +50% defense | `temporal_guard` receives another +20 maximum organization, +50% defense, and -75% experience loss |

The four xenobiological control technologies remain mutually exclusive refinements with distinct direct outputs. Chemical adds +50% defense, -50% supply consumption, and +50% casualty trickleback; Neural adds +30 maximum organization, +50% default morale, and +50% soft attack; Machine adds +75% hard attack, +50% breakthrough, and +50% reliability; Researched adds +35% soft attack, +35% hard attack, +8 maximum organization, -25% supply consumption, and -50% experience loss.

## Runtime consumers

An external operational grant enables the matching generic battalion, rebuilds its locked example template, reopens production of the matching custom equipment where that family uses equipment, and registers the existing Event 019 neutral provider row. The API grants no free equipment or stockpiles and adds no artificial API-wide division cap; ordinary training and recruitment remain constrained by each unit package's equipment, manpower, fuel, production, and trainability rules, while free or event-spawned formations may retain their owner-defined hard caps. Rebuilding Event 016 clears and reconstructs ordinary project-derived runtime state while preserving the independent external knowledge ledger. Alien Infantry remains the explicit exception: an alien grant enables laser production and contact consumers but never exposes the battalion to ordinary recruitment.

Portal weaponization authorizes the two native Portal Warfare raid surfaces when the country has the rebuilt `Quantum Transit Raiders` template. Every `portal_raider` battalion has ordinary infantry base stats, requires 100 Infantry Equipment and 10 Teleportation Equipment, and receives its exceptional performance from the two grant-only portal technologies. Both raids prepare for seven days, cost ten Command Power, reserve sixty Teleportation Equipment, and require at least six `portal_raider` battalions. On a successful outcome, `brilliant_scientist_portal_raid_establish_beachhead` commits one `Quantum Transit Raiders` formation in the captured target province with full equipment and manpower factors and 0.50 starting experience, then raises one scope-less reconstruction receipt. The native outcome consumes the assigned formation only against that receipt, preserving one formation and the locked six-battalion baseline budget without a free duplicate or race-condition loss. Damage and experience normalize to the breach-cadre profile because the documented `teleport_armies` effect is STATE-scoped and would relocate every qualifying army in the source state rather than the selected raid formation. `brilliant_scientist_portal_facility_raid` targets a hostile state containing factories, reactors, or rocket sites and calls `brilliant_scientist_portal_raid_extract_state_installation`; critical success may extract two state installations. `brilliant_scientist_portal_special_project_facility_raid` targets an exact `building = { tags = facility }` and calls `brilliant_scientist_portal_raid_extract_installation`; critical success may additionally extract one state installation. The raids remain normal native-raid player actions, with native preparation, reservation, cancellation, expiry, outcome, and history ownership. Warren Kruger's presence increases their AI weight but is not required to expose, prepare, or launch them. Portal Raider counter art is complete and wired, while the runtime model/entity, actions, and sounds remain unaccepted and unwired; the approved recovery boundary preserves existing geometry without regeneration and authorizes finishing the existing rig, actions, firearm, and effects through manual recovery. Seven model runtime packages remain unaccepted, so counter completion does not imply model/runtime acceptance.

## Assets and localisation

The API introduces no new player-facing technology object and therefore needs no new technology icon or localisation key. It reuses the existing technology icons, equipment icons, templates, raid art, Event 019 provider presentation, and their registered sprite names. Portal Raider counters are registered separately in `interface/portal_raider_system.gfx` at `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds`; their completion does not imply that the unaccepted model/entity package is wired. Future technology families must document their runtime icon path under `gfx/interface/technologies/016_brilliant_scientist/`, their sprite in the relevant Event 016 `.gfx` file, and every new player-facing localisation key before joining this API.

## Future plans and suggestions

External knowledge flags and source-provenance arrays are permanent by design and survive runtime rebuilds, project closure, and provider loss; no revocation contract or caller-clearing guidance is authorized. Xenobiological reconciliation may canonicalize stale alternate control outputs, but it does not revoke the chosen learned path or any non-control technology. A future random-discovery event can use a separate weighted pool over these selectors, but it must keep the seven operational technologies distinct from dependency-safe upgrades and from the separate six-package conventional API.

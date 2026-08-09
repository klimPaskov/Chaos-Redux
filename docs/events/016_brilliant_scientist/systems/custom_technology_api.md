# Reusable Kruger custom technology API

Event 016 exposes its eighteen custom technologies through country-scoped scripted effects so other events can award the same knowledge without pretending that Warren Kruger, his Directorate, or an Event 016 laboratory performed the discovery.

The API never grants vanilla computing, radar, industry, rocketry, nuclear, medical, or CBRN technologies. It also never creates Event 016 project history, project stages, facilities, Kruger ownership, free formations, equipment stockpiles, or event-log entries.

## Public grant effects

`chaosx_grant_custom_operational_technology` accepts the temporary selector `chaosx_custom_technology_family`. The seven valid values are `constant:chaosx_custom_technology_family.portal`, `.clone`, `.robot`, `.paleogenetic`, `.xenobiological`, `.exotic`, and `.temporal`. A valid call grants the matching base custom technology, records an external knowledge flag, and rebuilds the existing runtime consumers. `chaosx_custom_technology_grant_applied` reports `1` for a valid selector and `0` for an invalid selector.

`chaosx_grant_custom_technology_upgrade` accepts the temporary selector `chaosx_custom_technology_upgrade`. The valid values are the seven `*_weaponization` entries and the four `xeno_*_control` entries defined in `common/script_constants/016_brilliant_scientist_custom_technology_constants.txt`. The effect grants the matching operational base first, then the selected upgrade, so no weaponization or control technology can be awarded without its static dependency. `chaosx_custom_technology_upgrade_applied` reports whether the selector was valid.

`chaosx_grant_random_custom_operational_technology` has no input selector. It chooses uniformly from operational families the country does not yet know and does nothing after all seven have been learned. `chaosx_custom_technology_random_grant_applied` reports whether a family was selected.

Example:

```text
set_temp_variable = { chaosx_custom_technology_family = constant:chaosx_custom_technology_family.robot }
chaosx_grant_custom_operational_technology = yes
```

## Technology map

| Family | Operational technology | Upgrade technology |
| --- | --- | --- |
| Portal warfare | `brilliant_scientist_portal_warfare_tech` | `brilliant_scientist_portal_warfare_weaponization_tech` |
| Clone formations | `brilliant_scientist_clone_formations_tech` | `brilliant_scientist_clone_formations_weaponization_tech` |
| Robot formations | `brilliant_scientist_robot_formations_tech` | `brilliant_scientist_robot_formations_weaponization_tech` |
| Paleogenetic formations | `brilliant_scientist_paleogenetic_formations_tech` | `brilliant_scientist_paleogenetic_formations_weaponization_tech` |
| Xenobiological formations | `brilliant_scientist_xenobiological_formations_tech` | `brilliant_scientist_xenobiological_formations_weaponization_tech` |
| Exotic guard | `brilliant_scientist_exotic_guard_tech` | `brilliant_scientist_exotic_guard_weaponization_tech` |
| Temporal guard | `brilliant_scientist_temporal_guard_tech` | `brilliant_scientist_temporal_guard_weaponization_tech` |

The four xenobiological refinements are `brilliant_scientist_xeno_chemical_control_tech`, `brilliant_scientist_xeno_neural_control_tech`, `brilliant_scientist_xeno_machine_control_tech`, and `brilliant_scientist_xeno_researched_control_tech`.

## Power profile

The operational and weaponization technologies are intentionally late-game prize technologies rather than ordinary research increments. The operational technology makes the associated force immediately exceptional, while the dependency-safe weaponization upgrade creates a second cumulative leap.

| Family | Operational technology effect | Additional weaponization effect |
| --- | --- | --- |
| Portal warfare | +12 organization, +30% breakthrough, and -25% supply consumption | +12 organization, +40% breakthrough, and -25% supply consumption |
| Clone formations | +8 organization, +30% defense, and +30% soft attack | +12 organization, +35% recovery rate, -40% experience loss, and +25% casualty trickleback |
| Robot formations | +30% hard attack, breakthrough, and defense | +50% hard attack, +50% breakthrough, and +30% reliability |
| Paleogenetic formations | +30% soft attack, +30% breakthrough, and a 15% supply burden | +50% soft attack, +50% breakthrough, and +15% speed |
| Xenobiological formations | +30% soft attack, +15% hard attack, +8 organization, and +30% breakthrough | +50% soft attack, +30% hard attack, and +50% breakthrough |
| Exotic guard | +30% soft attack, hard attack, defense, and breakthrough | +60% hard attack, +50% piercing, and +40% breakthrough |
| Temporal guard | +12 organization and +30% defense | +12 organization, +50% defense, and -50% experience loss |

The xenobiological control technologies remain mutually exclusive refinements. Their shared combat scale is +15% for a minor bonus, +30% for a standard bonus, +8 or +12 organization, and -25% supply consumption for the chemical control logistics effect.

## Runtime consumers

An external operational grant recreates the matching locked and capped division template, authorizes recruiting through the existing cap, reopens production of the matching custom equipment where that family uses equipment, and registers the existing Event 019 neutral provider row. Rebuilding Event 016 clears and reconstructs ordinary project-derived runtime state while preserving the independent external knowledge ledger.

Portal weaponization also authorizes the existing portal facility raid when the country has the rebuilt `Quantum Transit Raiders` template. The raid remains a normal player action. Warren Kruger's presence increases its AI weight but is not required to expose, prepare, or launch it.

## Assets and localisation

The API introduces no player-facing object and therefore needs no new icon, sprite, DDS file, or localisation key. It reuses the existing technology icons, equipment icons, templates, raid art, Event 019 provider presentation, and their registered sprite names. Future technology families must document their runtime icon path under `gfx/interface/technologies/016_brilliant_scientist/`, their sprite in the relevant Event 016 `.gfx` file, and every new player-facing localisation key before joining this API.

## Future plans and suggestions

A future revocation contract should clear only the external ledger entries owned by its caller and then invoke the normal runtime rebuild. It must not clear Event 016 project history or remove knowledge granted by another event without an explicit ownership ledger. A future random-discovery event can build separate weighted pools over these selectors, but it should keep the seven operational technologies distinct from dependency-safe upgrades so every reward remains immediately usable.

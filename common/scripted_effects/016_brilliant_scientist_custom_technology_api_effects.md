# Event 016 custom technology API

This API gives other events, decisions, focuses, and scripted systems a neutral way to award the eighteen existing Event 016 custom technologies. The API never grants vanilla computing, radar, industry, rocketry, nuclear, medical, or chemical/biological technologies and never creates Event 016 project history.

## Public effects

`chaosx_grant_custom_operational_technology` runs in country scope. Set `chaosx_custom_technology_family` to one of `constant:chaosx_custom_technology_family.portal`, `clone`, `robot`, `paleogenetic`, `xenobiological`, `exotic`, or `temporal` before calling it. It grants the matching operational technology, sets a durable external operational/grant flag, and rebuilds the existing runtime package. The temporary output `chaosx_custom_technology_grant_applied` is `1` for a valid selector and `0` for an invalid selector.

`chaosx_grant_custom_technology_upgrade` runs in country scope. Set `chaosx_custom_technology_upgrade` to one of the seven `*_weaponization` selectors or the four `xeno_*_control` selectors. It first grants the matching operational base through the private core, then grants the dependency-safe upgrade, sets the external grant ledger flag, and rebuilds the runtime package. Weaponization upgrades never grant an orphan technology. The four control selectors also set neutral `chaosx_custom_technology_xeno_control_*` flags; they do not create Event 016 control ideas. The temporary output `chaosx_custom_technology_upgrade_applied` is `1` for a valid selector and `0` for an invalid selector.

`chaosx_grant_random_custom_operational_technology` runs in country scope with no selector. It weights only unresearched operational families and chooses one of the seven base technologies. When all seven are already held, it is a no-op. The temporary output `chaosx_custom_technology_random_grant_applied` records whether a branch was selected.

## Runtime behavior and lifecycle

The external ledger flags are independent of `brilliant_scientist_project_force_*` history flags. The existing Event 016 rebuild calls `chaosx_reapply_custom_technology_grants` after its normal clear and history reconstruction. This restores externally granted custom technologies without restoring project stages, facilities, Kruger ownership, project ideas, opening units, stockpiles, or vanilla technologies.

Each external operational family creates or reuses the existing locked division template, sets the existing family cap from `brilliant_scientist_project_force_cap`, and allows recruiting immediately. The matching custom equipment gate accepts the external operational flag while retaining suspended, damaged, and dismantled-family locks. Event 019 provider registration and provider-unlocked triggers accept the same external operational flags, so the existing neutral provider rows remain usable without revealing Event 016 provenance.

Portal weaponization authorizes the existing portal facility raid for any country that also has the rebuilt `Quantum Transit Raiders` template. Kruger's presence still increases the raid's AI weight, but it is not an access requirement.

The clear helper conditionally removes each of the eighteen custom technologies only when its matching external grant ledger flag is absent. External flags intentionally survive rebuilds and ledger changes. There is no automatic revocation API; callers that need revocation must define a separate design and explicitly clear the corresponding external flags before invoking the normal runtime rebuild.

## Selector map

| Selector | Existing custom technology |
| --- | --- |
| `family.portal` | `brilliant_scientist_portal_warfare_tech` |
| `family.clone` | `brilliant_scientist_clone_formations_tech` |
| `family.robot` | `brilliant_scientist_robot_formations_tech` |
| `family.paleogenetic` | `brilliant_scientist_paleogenetic_formations_tech` |
| `family.xenobiological` | `brilliant_scientist_xenobiological_formations_tech` |
| `family.exotic` | `brilliant_scientist_exotic_guard_tech` |
| `family.temporal` | `brilliant_scientist_temporal_guard_tech` |
| `upgrade.portal_weaponization` | `brilliant_scientist_portal_warfare_weaponization_tech` |
| `upgrade.clone_weaponization` | `brilliant_scientist_clone_formations_weaponization_tech` |
| `upgrade.robot_weaponization` | `brilliant_scientist_robot_formations_weaponization_tech` |
| `upgrade.paleogenetic_weaponization` | `brilliant_scientist_paleogenetic_formations_weaponization_tech` |
| `upgrade.xenobiological_weaponization` | `brilliant_scientist_xenobiological_formations_weaponization_tech` |
| `upgrade.exotic_weaponization` | `brilliant_scientist_exotic_guard_weaponization_tech` |
| `upgrade.temporal_weaponization` | `brilliant_scientist_temporal_guard_weaponization_tech` |
| `upgrade.xeno_chemical_control` | `brilliant_scientist_xeno_chemical_control_tech` |
| `upgrade.xeno_neural_control` | `brilliant_scientist_xeno_neural_control_tech` |
| `upgrade.xeno_machine_control` | `brilliant_scientist_xeno_machine_control_tech` |
| `upgrade.xeno_researched_control` | `brilliant_scientist_xeno_researched_control_tech` |

## Usage examples

```text
set_temp_variable = { chaosx_custom_technology_family = constant:chaosx_custom_technology_family.robot }
chaosx_grant_custom_operational_technology = yes
```

```text
set_temp_variable = { chaosx_custom_technology_upgrade = constant:chaosx_custom_technology_upgrade.temporal_weaponization }
chaosx_grant_custom_technology_upgrade = yes
```

Callers should not call `chaosx_grant_custom_operational_technology_core` or `chaosx_reapply_custom_technology_grants`; those are runtime/private helpers. The API intentionally uses static `set_technology` branches because the HOI4 effect accepts technology IDs as static tokens; selector constants only choose the branch.

## Future plans

If a future event needs to revoke externally granted knowledge, add a narrow, documented revocation effect that clears only its own grant ledger flags and then calls the existing rebuild. Do not couple external knowledge to project-history flags or add a second technology family without updating this map, the dependency audit, the runtime package, and the Event 019 provider surface.

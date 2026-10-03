# Event025 external reward scenario contract

This file preserves the domain-state meaning of the ten parent-supplied scenario IDs for a later same-scenario comparison. It is not a probability-tool fixture and does not claim that these fields were accepted by the unavailable MCP route.

The analyzed surface is the Event016 owner API `chaosx_grant_external_alien_recovery_reward`, its `chaosx_grant_random_custom_operational_technology` base pool, its eligible-upgrade pool, and the Event025/Event036 ledger calls that supply the API inputs.

## Shared candidate pool

The complete source-declared base-family set is `portal`, `clone`, `robot`, `paleogenetic`, `xenobiological`, `alien_infantry`, and `temporal`. The owner trigger treats a family as owned when its technology or operational/grant receipt is present.

The complete source-declared upgrade set is `portal_weaponization`, `clone_weaponization`, `robot_weaponization`, `paleogenetic_weaponization`, `xenobiological_weaponization`, `alien_predictive_warfare_weaponization`, `temporal_weaponization`, `xeno_chemical_control`, `xeno_neural_control`, `xeno_machine_control`, and `xeno_researched_control`. `chaosx_custom_technology_upgrade_is_eligible` gates each entry on its operational base and unowned, compatible upgrade state.

Every eligible base and upgrade entry uses the source constant `chaosx_custom_technology_tuning.random_candidate_weight = 1`. These are raw `random_list` weights, not normalized selection probabilities. No MCP result established a complete normalized pool or any selection share.

The owner API maps its `portal` result to the broad field label `aircraft` and its `temporal` result to `propulsion`. This is a result-label mapping, not proof that Event036 and Event016 share an exact technology or equipment ID. `brilliant_scientist_portal_warfare_tech` at line 37 of `common/technologies/016_brilliant_scientist_project_technologies.txt` enables `teleportation_equipment_1` and the `portal_raider` land sub-unit. `brilliant_scientist_temporal_guard_tech` at line 172 enables `temporal_guard_equipment_1` and the `temporal_guard` land sub-unit. Their force upgrade technologies at lines 36 and 121 of `common/technologies/016_brilliant_scientist_project_force_technologies.txt` modify `portal_raider` and `temporal_guard`. The corresponding unit definitions are land consumers in `common/units/016_brilliant_scientist_project_forces.txt`.

The current Event036 legacy option instead grants vanilla `jet_fighter1`, `jet_fighter2`, and 200 units of `jet_fighter_equipment_2` in `events/036_alien_spacecraft.txt`. Broad-field label equality does not establish exact overlap between those IDs and the Event016 portal or temporal technology packages. Exact duplicate identity remains unresolved pending an accepted mapping or matching IDs.

For each fixture, encode ownership through the exact technology and receipt checks in the Event016 trigger source. A missing family means its technology and all checked operational/grant receipts are absent. An owned family means at least one checked ownership signal is present. Keep alternate xenobiological controls explicit because the upgrade preflight makes them mutually exclusive.

The event source, source-specific consumed flags, exact overlap value, country-level Event025/Event036 receipt flags, candidate ownership, and Integration idea state are the external inputs. The random-list blocks contain no extra modifier blocks, dates, strategy factors, war factors, or target factors. The overlap-exclusion flag is derived by the Event025 ledger preparer in the current source.

## Named scenarios

| Scenario ID | Declared state for the later compare | Expected source-level tier ordering | Baseline MCP status |
| --- | --- | --- | --- |
| `no_owned_bases` | Event025 source, no previous alien overlap, no Event025 or Event036 consumed receipt, all seven base families missing, no base-qualified upgrade eligible, and Integration idea absent. | Random missing base first, then upgrades if the base pool is empty, then Integration. | Unresolved. |
| `one_owned_base` | Event025 source, no overlap, `portal` owned and the other six base families missing. Leave only `portal_weaponization` eligible and mark the other ten upgrades owned. Integration idea is absent. | The six missing base candidates remain ahead of the eligible Portal upgrade. | Unresolved. |
| `overlap_aircraft_other_bases_missing` | Same country has a prior Event036 aircraft-field receipt. Event025 is the new source receipt. All seven Event016 bases are missing, all upgrades are ineligible because their bases are absent, and Integration is absent. The current source derives broad overlap value `1`. | The base tier must resolve other valid missing families before upgrades or Integration. The exact candidate to exclude is unresolved because the broad aircraft label does not prove an ID match. | Unresolved. |
| `overlap_propulsion_other_bases_missing` | Same as the aircraft overlap case, with a prior Event036 propulsion-field receipt and derived broad overlap value `2`. | The base tier must resolve other valid missing families before upgrades or Integration. The exact candidate to exclude is unresolved because the broad propulsion label does not prove an ID match. | Unresolved. |
| `overlap_both_other_bases_missing` | The requested fixture represents simultaneous aircraft and propulsion broad-field overlap, with all Event016 bases missing. | The intended base-first tier remains the parent instruction, while the exact excluded candidates require an accepted ID mapping. | Unresolved and not representable by the current scalar overlap input. The current field is `0`, `1`, or `2`, and Event036 stores one field per country. Do not encode a synthetic mask without an owner-approved source contract. |
| `all_bases_owned_upgrade_available` | Event025 source, all seven bases owned, only `portal_weaponization` eligible, other ten upgrades owned, and Integration absent. | The eligible Portal upgrade is selected before Integration. | Unresolved. |
| `all_bases_and_upgrades_owned` | Event025 source, all seven bases and all eleven upgrades owned, Integration idea absent. | Apply `brilliant_scientist_alien_systems_integration`. The already-owned-idea reinforcement branch is a separate unrequested variant. | Unresolved. |
| `repeated_event025_receipt` | A prior Event025 base result is already stored, `chaosx_alien_recovery_event025_recorded` and the Event025 consumed receipt are set, and the resolver is called again for the same country. Preserve the prior result, field, tier, and source values. | Re-expose the stored Event025 result without another owner API call or reward. | Unresolved. |
| `event036_first` | Event036 fires and resolves first for the same country. Use its current aircraft field and completed vanilla jet reward state, then apply the Event025 winner settlement. Keep all seven Event016 bases missing and upgrades ineligible so the later Event025 request tests the broad-field overlap branch. | The Event025 request must resolve the base tier before upgrades or Integration. Exact duplicate identity is unproven because the Event036 jet IDs do not match the Event016 portal or temporal package IDs. | Unresolved. |
| `event025_first` | Event025 first grants the `portal` base result and records the `aircraft` field. Event036 then grants its vanilla jet package for the same country. The ledger treats the equal broad labels as overlap. Leave `portal_weaponization` eligible and other upgrades owned. | Preserve the later Event036 conversion request as upgrade-first because its current caller requests `allow_base = 0`. Whether the broad-label match represents an exact duplicate remains unresolved. | Unresolved. The first random draw is fixed to `portal` here as a conditional ordering case, not as a probability claim about the initial draw. |

## Scenario limits

The parent supplied the scenario IDs but not a live adapter schema, scenario hashes, country bindings, or engine fixtures. The states above use current source identifiers and are proposed domain fixtures for a later adapter call. They have not been submitted to MCP.

`event036_first` conditions on the same country being selected by the Event036 random-country bootstrap. It does not estimate that separate recipient-selection chance. `event025_first` conditions on the first API draw being `portal`; it does not estimate the chance of drawing `portal` from the base pool.

An unconditional event-order distribution would require a complete custom-pool sequence manifest with the two event transitions, same-country scope, source-specific receipt changes, pool eligibility changes, and a supported cadence model. No MCP sequence analysis was run.

# Event 016 custom technology API

This API gives other events, decisions, focuses, and scripted systems a neutral way to award the eighteen existing Event 016 custom technologies. Every public effect is country scoped, and selectors are temporary or country variables supplied by the caller. The API never grants vanilla computing, radar, industry, rocketry, nuclear, medical, or chemical/biological technologies and never creates Event 016 project history.

Every public grant accepts the optional numeric `chaosx_custom_technology_source` input.
A source from `provenance_minimum_source` inclusive to `provenance_stride` exclusive records permanent provenance without changing the grant result; the current range is 1 through values below 1,000,000.
An omitted or out-of-range source records nothing and does not block a valid technology grant.
The Event 025/Event 036 recovery bridge automatically supplies its positive source event when the generic input is absent.

## Public effects

`chaosx_grant_custom_operational_technology` runs in country scope. Set `chaosx_custom_technology_family` to one of `constant:chaosx_custom_technology_family.portal`, `clone`, `robot`, `paleogenetic`, `xenobiological`, `alien_infantry`, or `temporal` before calling it. It grants the matching operational technology, sets a durable external operational/grant flag, records one source receipt when requested, and rebuilds the existing runtime package. Repeating a valid grant is idempotent. The temporary output `chaosx_custom_technology_grant_applied` is `1` for a valid selector and `0` for an invalid selector.

`chaosx_grant_custom_technology_upgrade` runs in country scope. Set `chaosx_custom_technology_upgrade` to one of the seven `*_weaponization` selectors or the four `xeno_*_control` selectors. It first grants the matching operational base through the private core, then grants the dependency-safe upgrade, sets the external grant ledger flag, records both the prerequisite family and selected upgrade source receipts when requested, and rebuilds the runtime package. Weaponization upgrades never grant an orphan technology. The four control selectors are mutually exclusive: a selected control is accepted only when no alternate control is occupied, and repeating that same selected control remains idempotent. The temporary output `chaosx_custom_technology_upgrade_applied` is `1` for a valid selector and `0` for an invalid or incompatible selector.

`chaosx_grant_random_custom_operational_technology` runs in country scope with no selector. It weights only unresearched operational families and chooses one of the seven base technologies with the equal `constant:chaosx_custom_technology_tuning.random_candidate_weight`. When all seven are already held, it is a no-op. The temporary output `chaosx_custom_technology_random_grant_applied` records whether a branch was selected, and the selected grant records `chaosx_custom_technology_source` when present.

`chaosx_grant_external_alien_recovery_reward` is the owner API for alien-derived rewards from Event 025 and compatible recovery systems. It grants the first missing operational family, then one eligible upgrade, then `brilliant_scientist_alien_systems_integration`; it never grants vanilla technology or Event 016 project history. Set the temporary `chaosx_alien_recovery_overlap` value above zero when a caller has proved an aircraft or propulsion overlap. Upgrade weights are built through `chaosx_custom_technology_upgrade_is_eligible`, so already-owned upgrades and all three alternate xenobiological controls have zero weight. The durable result is stored in `chaosx_external_alien_recovery_result`, and repeated calls are guarded by `chaosx_external_alien_recovery_reward_consumed`. The stable result, tier, field, and source values live in `chaosx_custom_technology_recovery`, so the API does not depend on any caller package's constant namespace or file load order.

## Query and reconciliation effects

`chaosx_custom_technology_source_is_valid` is a read-only country-scope query for the optional temporary or country variable `chaosx_custom_technology_source`.
It requires the input to exist and satisfy the inclusive minimum and exclusive stride bounds above.
It has no side effects, makes no default assignment, and returns false for missing or out-of-range input.
Callers requiring recorded provenance can use this query before invoking a public grant; ordinary grants intentionally remain usable without provenance.

`chaosx_custom_technology_family_is_valid` and `chaosx_custom_technology_upgrade_is_valid` are selector-shape queries. They return true only for the seven operational or eleven upgrade constants, respectively.

`chaosx_can_grant_custom_operational_technology` is the idempotent operational preflight query. It requires a valid family selector but deliberately does not reject an already-known family, because the public operational effect is safe to repeat.

`chaosx_can_grant_custom_technology_upgrade` is the public upgrade safety query. It accepts a valid weaponization or control selector, permits the effect to install its own prerequisite base, and rejects a control when any alternate control is currently represented by a project flag, neutral receipt, external receipt, or learned control technology.

`chaosx_custom_technology_has_xeno_control` is the aggregate control-presence query, while the four `chaosx_custom_technology_xeno_*_control_is_current` queries identify the individual occupied channels. They are read-only and never create Directorate or project state.

`chaosx_custom_operational_technology_is_unowned` is used by the random operational pool. It treats a learned base technology or any matching neutral or external operational receipt as owned, including Mengele's neutral clone-program receipt.

`chaosx_custom_technology_upgrade_is_eligible` is the strict pool query. It requires the selected upgrade to be unowned, its operational base to be present or externally received, and its control channel to pass the mutual-exclusion query. Callers that build weighted upgrade pools should use this effect for every candidate and assign the same weight to each true candidate.

`chaosx_reconcile_custom_xeno_control_grants` is the country-scoped control repair effect. It chooses exactly one control in deterministic priority order `chemical`, `neural`, `machine`, then `researched`, preferring existing Event 016 project mode flags and then neutral or external API receipts and learned control technologies. It preserves the chosen path, sets its neutral and external receipt markers, clears stale alternate control flags, removes alternate hidden control technologies, and removes alternate control ideas. It does not clear the chosen learned technology and never creates project history, Directorate variables, facilities, or achievements. If no control is present, it leaves the four channels clear.

`chaosx_reconcile_custom_technology_runtime` is the public runtime boundary. It runs control reconciliation and then calls the existing Event 016 rebuild so templates, production gates, provider rows, caps, ideas, and learned technologies are synchronized. Its temporary output `chaosx_custom_technology_runtime_reconciled` is `1` after the boundary runs.

## Source provenance receipts

Operational receipts are stored in the country array `chaosx_custom_technology_operational_provenance`, and upgrade receipts are stored in `chaosx_custom_technology_upgrade_provenance`.
The API encodes each receipt as `selector * constant:chaosx_custom_technology_tuning.provenance_stride + source`.
Both writers require `chaosx_custom_technology_source_is_valid`, so a source cannot spill into the next selector's numeric range.
The current stride is `1000000`, and valid source IDs are at least 1 and strictly below that stride.
The receipt therefore preserves both the selected API vocabulary and the external source without requiring a second parallel array.

The operational public effect appends one family receipt after a valid grant.
The upgrade public effect appends the prerequisite family receipt and one upgrade receipt after a valid grant.
`chaosx_grant_external_alien_recovery_reward` inherits Event 025 or Event 036's positive source event when no direct source input is supplied.
`is_in_array` guards make each encoded receipt idempotent, and neither reconciliation nor runtime rebuild clears either array.
A missing or out-of-range source is intentionally provenance-free and does not block the technology grant.
No existing receipt is reinterpreted, deleted, or attributed to a guessed source.

```text
set_temp_variable = { chaosx_custom_technology_source = 25 }
if = {
	limit = { chaosx_custom_technology_source_is_valid = yes }
	set_temp_variable = { chaosx_custom_technology_family = constant:chaosx_custom_technology_family.robot }
	chaosx_grant_custom_operational_technology = yes
}
```

## Runtime behavior and lifecycle

The external ledger flags are independent of `brilliant_scientist_project_force_*` history flags. The existing Event 016 rebuild calls `chaosx_reapply_custom_technology_grants` after its normal clear and history reconstruction. This restores externally granted custom technologies without restoring project stages, facilities, Kruger ownership, project ideas, opening units, stockpiles, or vanilla technologies.

Each external operational family rebuilds only its existing runtime consumers. Normally trainable generic families reopen their existing equipment and template paths, while alien infantry remains landing-only and untrainable. Free or event-spawned formation caps remain separate from normal equipment-constrained recruitment and are reconciled by the owning unit package. The matching custom equipment gate accepts the external operational flag while retaining suspended, damaged, and dismantled-family locks. Event 019 provider registration and provider-unlocked triggers accept the same external operational flags, so the existing neutral provider rows remain usable without revealing Event 016 provenance.

Portal weaponization authorizes the existing portal facility raid for any country that also has the rebuilt `Quantum Transit Raiders` template. Kruger's presence still increases the raid's AI weight, but it is not an access requirement.

The clear helper conditionally removes each of the eighteen custom technologies only when its matching external grant ledger flag is absent. External flags and provenance arrays intentionally survive rebuilds and ledger changes. There is no automatic revocation API; callers that need revocation must define a separate design and explicitly clear the corresponding external flags before invoking the normal runtime rebuild. Reconciliation can remove only stale alternate xenobiological control outputs; it never revokes the chosen learned path or any non-control technology.

## Selector map

| Selector | Existing custom technology |
| --- | --- |
| `family.portal` | `brilliant_scientist_portal_warfare_tech` |
| `family.clone` | `brilliant_scientist_clone_formations_tech` |
| `family.robot` | `brilliant_scientist_robot_formations_tech` |
| `family.paleogenetic` | `brilliant_scientist_paleogenetic_formations_tech` |
| `family.xenobiological` | `brilliant_scientist_xenobiological_formations_tech` |
| `family.alien_infantry` | `brilliant_scientist_alien_infantry_tech` |
| `family.temporal` | `brilliant_scientist_temporal_guard_tech` |
| `upgrade.portal_weaponization` | `brilliant_scientist_portal_warfare_weaponization_tech` |
| `upgrade.clone_weaponization` | `brilliant_scientist_clone_formations_weaponization_tech` |
| `upgrade.robot_weaponization` | `brilliant_scientist_robot_formations_weaponization_tech` |
| `upgrade.paleogenetic_weaponization` | `brilliant_scientist_paleogenetic_formations_weaponization_tech` |
| `upgrade.xenobiological_weaponization` | `brilliant_scientist_xenobiological_formations_weaponization_tech` |
| `upgrade.alien_predictive_warfare_weaponization` | `brilliant_scientist_alien_predictive_warfare_tech` |
| `upgrade.temporal_weaponization` | `brilliant_scientist_temporal_guard_weaponization_tech` |
| `upgrade.xeno_chemical_control` | `brilliant_scientist_xeno_chemical_control_tech` |
| `upgrade.xeno_neural_control` | `brilliant_scientist_xeno_neural_control_tech` |
| `upgrade.xeno_machine_control` | `brilliant_scientist_xeno_machine_control_tech` |
| `upgrade.xeno_researched_control` | `brilliant_scientist_xeno_researched_control_tech` |

## Usage examples

```text
set_temp_variable = { chaosx_custom_technology_family = constant:chaosx_custom_technology_family.robot }
set_temp_variable = { chaosx_custom_technology_source = 25 }
chaosx_grant_custom_operational_technology = yes
```

```text
set_temp_variable = { chaosx_custom_technology_upgrade = constant:chaosx_custom_technology_upgrade.temporal_weaponization }
set_temp_variable = { chaosx_custom_technology_source = 36 }
chaosx_grant_custom_technology_upgrade = yes
```

Callers that grant an upgrade and want an existing control path repaired should call `chaosx_reconcile_custom_technology_runtime = yes` after changing source flags or learned technology state. The public upgrade effect already performs this boundary after a successful grant.

Callers should not call `chaosx_grant_custom_operational_technology_core` or `chaosx_reapply_custom_technology_grants`; those are runtime/private helpers. The API intentionally uses static `set_technology` branches because the HOI4 effect accepts technology IDs as static tokens; selector constants only choose the branch.

## Future plans

If a future event needs to revoke externally granted knowledge, add a narrow, documented revocation effect that clears only its own grant ledger flags and then calls the existing rebuild. Do not couple external knowledge to project-history flags or add a second technology family without updating this map, the dependency audit, the runtime package, and the Event 019 provider surface.

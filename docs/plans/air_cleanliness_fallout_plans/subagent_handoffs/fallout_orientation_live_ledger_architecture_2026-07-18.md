# Fallout orientation live-ledger architecture review

## Record status

This file is the parent agent's transcription and review of the bounded `chaosx_scripted_system_architect` conclusions delivered on 2026-07-18. The architect was read-only and made no gameplay edit. The parent interrupted the agent after its conclusions were delivered because its final file-write turn did not complete.

The review did not run Hearts of Iron IV. It did not activate Fallout orientation, the ordinary scheduler, or the manual scenario.

## Verdict

The live-ledger gate remains blocked pending numerical approval and exact infrastructure repair proof.

The current implementation has no accepted durable opening producer for Cohesion. It has no accepted 0 through 100 state Supply Access ledger. `fallout_orientation_state_supply` is an isolated orientation variable with no Air Winter or native supply consumer. The documented engine surfaces do not prove instant repair of exactly one damaged infrastructure level.

## Proven current surfaces

### Country resources and Cohesion

`docs/plans/air_cleanliness_fallout_plans/FALLOUT_SURVIVAL_NUMERICAL_CONTRACT_PROPOSAL.md` defines nine accepted resources. Recognition is index 9. Cohesion is not an accepted resource index and has no accepted formula.

`common/scripted_effects/fallout_consolidated_effects.txt` writes only the accepted initial and current resource arrays in the country-row producer and commit path. The dormant orientation transaction currently requires `fallout_orientation_requested_cohesion`, freezes it, and copies it into the private `fallout_orientation_cohesion` variable in `common/scripted_effects/fallout_consolidated_effects.txt` near lines 3473 and 3506.

The 35 Food, 35 Shelter capacity, and 30 Recognition formula in `FALLOUT_ORIENTATION_LIVE_LEDGER_NUMERICAL_CONTRACT_PROPOSAL.md` is a design proposal. It is not an implementation fact and may not be coded before user approval.

### State supply

The accepted survival numerical contract defines opening Logistics as:

```text
clamp(20 * fallout_building_damage_after_non_damaged_infrastructure, 0, 100)
```

`common/scripted_effects/fallout_consolidated_effects.txt` calculates that value as a temporary signal near lines 377 through 379. The producer uses it inside several resource formulas but does not persist it as a state Supply Access value.

No `air_winter_supply` ledger exists. `air_winter_local_supply_factor` is a phase-derived negative modifier input in `common/scripted_effects/fallout_consolidated_effects.txt` near lines 1158 through 1192. It is not a 0 through 100 supply ledger. `air_winter_survival_value` is a derived viability value and is not a supply resource.

`fallout_orientation_state_supply` appears only in `common/scripted_effects/fallout_consolidated_effects.txt` near lines 4199, 4228 through 4233, 4365, 4399, 4413, and 4427. No native supply modifier or Air Winter calculation consumes it. It is therefore a shadow value and cannot satisfy the accepted live state-result requirement.

Promoting the accepted Logistics formula into immutable opening and mutable current Supply Access is feasible architecture, but the promotion, field names, schema change, and native modifier translation require user approval.

### Air Winter values

The canonical state values are:

- `air_winter_exposure`
- `air_winter_recovery`
- `air_winter_adaptation`
- `air_winter_food_reserve`
- `air_winter_shelter_capacity`
- `air_winter_reclamation`
- `air_winter_water_security`

Their initialization, normalization, and mutation are implemented in `common/scripted_effects/fallout_consolidated_effects.txt` near lines 568 through 617 and 1005 through 1146.

The optional `air_winter_recovery_bonus` feeds state recovery pressure near lines 715 through 734. This proves a potential durable integration input. It does not by itself authorize orientation to own or mutate that input. The proposal's rule that an orientation Recovery gain writes both the bonus and current Recovery requires user approval.

### Deaths

Orientation state loss calls `apply_exact_state_civilian_population_loss` and records `fallout_aftermath` as the reason in `common/scripted_effects/fallout_consolidated_effects.txt` near lines 4115 through 4133. Country loss traverses the stable Fallout state ledger near lines 4059 through 4112.

The shared helper and Deaths gate live in `common/scripted_effects/chaosx_dynamic_effects.txt` near lines 659 through 727. Air Winter monthly loss uses the same shared system with the Air Winter exposure reason. The Deaths surface is proven statically and is not a blocker for this ledger proposal.

## Exact infrastructure repair blocker

Installed official documentation proves:

- `add_building_construction` starts construction in `documentation/effects_documentation.md` near lines 839 through 846
- `damage_building` damages a building near lines 3374 through 3413
- `set_building_level` sets total building level near lines 6621 through 6628
- `damaged_building_level@type` reads damaged levels in `documentation/dynamic_variables_documentation.md`
- `non_damaged_building_level@type` reads operational levels in the same file

No documented effect removes exactly one damaged infrastructure level while preserving total level. Vanilla source contains no reviewed negative `damage_building` precedent and no dedicated repair effect.

The orientation trigger file correctly keeps the capital repair and state-result gates unset near `common/scripted_triggers/fallout_consolidated_triggers.txt` lines 1636 through 1644 and 1937 through 1952. Construction, an increased total level, repair speed, or a variable receipt is not an exact substitute.

## Read-only event inspection

The architect attempted a fresh read-only event manifest scan and a trace for event `chaosx.fallout.62`. The tool returned partial inspection artifacts but did not produce a validation pass. Full graph projection reached the fixed ceiling of 200000 derived edges. No event lint success is claimed.

## Dependency order

1. Obtain user approval or rejection of `FALLOUT_ORIENTATION_LIVE_LEDGER_NUMERICAL_CONTRACT_PROPOSAL.md`.
2. If approved, implement and replay-validate Cohesion and State Supply Access inside the sole survival numerical coordinator.
3. Replace caller-supplied Cohesion and Supply Access with authenticated durable row reads.
4. Replace the private orientation state mirrors with direct live Air Winter and Supply Access mutations.
5. Keep the state-result and capital-repair gates unset until every new row validator passes and exact repair is proven or the user explicitly revises that result.
6. Only then continue the capital events and later Ash-week components.
7. Keep caller wiring, successor materialization, manual scenario activation, and ordinary scheduler activation outside this tranche.

## Remaining uncertainty

Runtime save persistence, dynamic-modifier refresh timing, multiplayer observation, and delayed event behavior remain unobserved because Hearts of Iron IV was not run.

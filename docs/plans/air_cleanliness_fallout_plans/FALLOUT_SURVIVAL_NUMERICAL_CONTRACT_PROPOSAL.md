# Fallout survival numerical contract proposal

## Status

This document is proposed design. It is not accepted design and it does not authorize gameplay implementation.

The current repository has an accepted formula-neutral identity transaction for the nine Fallout survival resources. It deliberately has no numerical producer, numerical commit effect, or setter for `fallout_survival_ledger_ready`. This proposal defines the missing numerical contract for review.

Until this proposal is accepted:

- no survival numerical arrays may be populated
- no survival row commit flag may be set
- no effect may set `fallout_survival_ledger_ready`
- the Fallout transition barrier remains closed
- living-world event ids `100` through `106` and `123` through `126` remain blocked

## Design decisions proposed for acceptance

The proposal makes seven explicit decisions.

1. Every resource uses an integer 0 to 100 scale.
2. State scores describe usable local capacity after Air Winter and the destructive Fallout rewrite. They do not reuse the general `fallout_survival_value` as a substitute.
3. Country scores blend broad territorial coverage with the strongest surviving hub. A tiny specialist state can matter, but it cannot supply a continental successor by itself.
4. Physical starting resources come from state evidence. Government archetypes alter Recognition only. They do not create food, fuel, medicine, or machinery from nothing.
5. The immutable `initial` array is the committed opening profile. The mutable `current` array begins equal to `initial` and is the sole array changed by later gameplay.
6. Every calculation uses frozen or durable transition receipts. Later ownership, repairs, annexations, and resource changes cannot rewrite the opening profile.
7. The global ready flag is written once, last, only after exact replay validators pass every state row and country row.

## Resource identity order

The existing accepted order remains unchanged.

| Index | Resource |
| --- | --- |
| 0 | none |
| 1 | food |
| 2 | clean_water |
| 3 | medicine |
| 4 | scrap |
| 5 | fuel |
| 6 | power |
| 7 | filters |
| 8 | shelter_capacity |
| 9 | recognition |

Index 0 is always zero in every numerical array. The array length remains `constant:fallout_survival_resource.upper_bound`.

## Numerical semantics

### State rows

For resource index `i`:

```text
state_raw_numerator[i] = sum of weighted component signals
state_raw_denominator[i] = 100
state_equal_share[i] = clamp(round(state_raw_numerator[i] / state_raw_denominator[i]), 0, 100)
```

Each component signal is clamped to 0 through 100 before it enters a resource formula. Resource weights total exactly 100. No intermediate division is rounded. The engine-native `round_temp_variable` operation is used once after the final division.

The numerator therefore remains between 0 and 10,000. The denominator is exactly 100 for indexes 1 through 9.

### Country rows

Country aggregation uses the unrounded state numerator, a bounded continuous survivor-population weight, and the strongest unrounded state hub.

For every state in the country row's frozen ownership set:

```text
state_score = state_raw_numerator[i] / 100
weighted_sum = weighted_sum + state_score * population_weight
weight_sum = weight_sum + population_weight
hub = maximum state_raw_numerator[i] / 100
```

The population weight uses the durable `fallout_population_after_loss_k` receipt.

```text
population_weight = clamp(fallout_population_after_loss_k / 1000, 0.001, 8)
```

One weight point represents one million survivors. The 0.001 floor represents one thousand survivors for aggregation purposes. The cap prevents one old metropolis from erasing the rest of a country. A collection of almost empty states therefore contributes very little to broad coverage.

The resource families use these broad-coverage and hub weights.

| Resource | Broad coverage | Strongest hub |
| --- | ---: | ---: |
| Food | 90 | 10 |
| Clean water | 90 | 10 |
| Medicine | 90 | 10 |
| Scrap | 75 | 25 |
| Fuel | 75 | 25 |
| Power | 75 | 25 |
| Filters | 90 | 10 |
| Shelter capacity | 90 | 10 |
| Recognition | 70 | 30 |

For broad weight `B` and hub weight `H`:

```text
coverage = weighted_sum / weight_sum
country_raw_numerator[i] = B * coverage + H * hub
country_raw_denominator[i] = 100
country_base[i] = clamp(round(country_raw_numerator[i] / country_raw_denominator[i]), 0, 100)
```

`B + H` must equal 100. `weight_sum` must be positive. A country row with no frozen states is an error and cannot commit.

The state score division and population scaling remain fixed-point operations. They are not rounded. The sole country rounding operation occurs after the complete blend. This prevents state partition and false hub-tie bias.

The country raw arrays preserve the physical aggregation before any Recognition adjustment.

## Frozen input authority

### Inputs already present

The following existing receipts are authoritative numerical inputs.

Air Winter snapshot:

- `fallout_pretransition_air_winter_phase`
- `fallout_pretransition_air_winter_exposure`
- `fallout_pretransition_air_winter_recovery`
- `fallout_pretransition_air_winter_adaptation`
- `fallout_pretransition_air_winter_food_reserve`
- `fallout_pretransition_air_winter_shelter_capacity`
- `fallout_pretransition_air_winter_reclamation`
- `fallout_pretransition_air_winter_water_security`
- `fallout_pretransition_air_winter_original_category`

Population, grading, and rewrite receipts:

- `fallout_population_after_loss_k`
- `fallout_state_grade`
- `fallout_building_damage_before_infrastructure`
- `fallout_building_damage_before_industrial_complex`
- `fallout_building_damage_before_arms_factory`
- `fallout_building_damage_before_air_base`
- `fallout_building_damage_before_dockyard`
- `fallout_building_damage_after_infrastructure`
- `fallout_building_damage_after_industrial_complex`
- `fallout_building_damage_after_arms_factory`
- `fallout_building_damage_after_air_base`
- `fallout_building_damage_after_dockyard`
- `fallout_supply_network_after_supply_node`
- `fallout_supply_network_after_rail_way`

Frozen geography and deposits:

- `fallout_pretransition_capital`
- `fallout_pretransition_coastal`
- `fallout_pretransition_resource_oil`
- `fallout_pretransition_resource_aluminium`
- `fallout_pretransition_resource_rubber`
- `fallout_pretransition_resource_tungsten`
- `fallout_pretransition_resource_chromium`
- `fallout_pretransition_resource_steel`
- `fallout_pretransition_damaged_infrastructure`
- `fallout_pretransition_damaged_industrial_complex`
- `fallout_pretransition_damaged_arms_factory`
- `fallout_pretransition_damaged_air_base`
- `fallout_pretransition_damaged_dockyard`

Country identity:

- `fallout_survival_country_source_region`
- `fallout_survival_country_source_archetype`
- `fallout_survival_country_source_memory`

Region and country memory remain provenance in this numerical contract. They do not apply generic physical-resource bonuses. Their later focus, decision, event, and consumption rules must be manually customized.

### Required frozen and post-rewrite additions

The accepted resource descriptions name dams, reactors, coal, synthetic plants, fuel storage, ports, and radio infrastructure. The live snapshot does not yet freeze enough evidence for those sources. The numerical implementation must first extend the pretransition state snapshot with these exact operational inputs:

- `fallout_pretransition_non_damaged_naval_base`
- `fallout_pretransition_non_damaged_radar_station`
- `fallout_pretransition_non_damaged_synthetic_refinery`
- `fallout_pretransition_non_damaged_fuel_silo`
- `fallout_pretransition_non_damaged_dam`
- `fallout_pretransition_non_damaged_dam_mountain`
- `fallout_pretransition_non_damaged_cataract_dam_mountain`
- `fallout_pretransition_non_damaged_nuclear_reactor`
- `fallout_pretransition_non_damaged_nuclear_reactor_heavy_water`
- `fallout_pretransition_non_damaged_commercial_nuclear_reactor`
- `fallout_pretransition_resource_coal`

The values must be captured in the same snapshot generation as the current state row. Each field must be required by the structural snapshot validator. A schema migration may not fill an absent field from later live map state.

The existing `fallout_building_damage_after_*` fields use `building_level@type`. They prove retained levels, not operational levels. The permanent-building-loss reconciliation must also freeze these post-rewrite operational receipts with `non_damaged_building_level@type`:

- `fallout_building_damage_after_non_damaged_infrastructure`
- `fallout_building_damage_after_non_damaged_industrial_complex`
- `fallout_building_damage_after_non_damaged_arms_factory`
- `fallout_building_damage_after_non_damaged_air_base`
- `fallout_building_damage_after_non_damaged_dockyard`

The building-loss durable validator must require and replay these fields. Industry, Logistics, Port capacity, and Communication capacity use the post-rewrite non-damaged receipts, never retained total levels.

The proposed specialty-source snapshot remains authoritative only because the current destructive rewrite does not mutate dams, reactors, refineries, fuel silos, naval bases, radar, or coal deposits after the snapshot. If that rewrite gains any such mutation, the same tranche must add and consume durable post-rewrite operational receipts for the affected source. A pretransition value cannot be retained as a silent proxy.

Adding these fields requires a world-transition schema promotion before any Fallout path is activated. An in-progress row from the earlier schema cannot be promoted through a numerical fallback and cannot replay destructive phases. It fails closed. A completed Fallout row receives no fabricated opening profile.

No hospital, laboratory, greenhouse, aquifer, desalination, wind, or generator building has a durable accepted Fallout snapshot surface. This proposal does not invent one. Medicine uses surviving urban and industrial institutional capacity. Food and water use their reviewed Air Winter ledgers, which already encode regional food and water conditions.

### Air Winter not-applicable rows

A state with `fallout_pretransition_air_winter_source_kind = not_applicable` is impassable, unowned, or explicitly excluded under the current Air Winter validity trigger. Its typed zero payload is an applicability receipt, not evidence that an inhabited state has zero food, water, and shelter.

The numerical state row for that source kind uses numerator 0, denominator 100, and equal share 0 for indexes 1 through 9. It remains in the global identity ledger for all-state coverage, but it is excluded from country `weight_sum`, broad coverage, and hub selection.

Every committed country must have at least one frozen state with a produced Air Winter source row. A country with only not-applicable states is a numerical error. The producer may not reinterpret the typed zero payload or read later live state values.

## Common normalized signals

All formula coefficients in this section become typed script constants if the proposal is accepted.

### Access

`access` represents whether survivors can safely use what remains.

| Fallout state grade | Grade access |
| --- | ---: |
| remote refuge | 100 |
| scarred province | 80 |
| ash zone | 60 |
| dead city | 40 |
| wasteland | 20 |
| vitrified zone | 0 |

```text
hazard_access = clamp(
    grade_access
  - 0.30 * fallout_pretransition_air_winter_exposure,
    0,
    100
)

access_numerator =
    50 * hazard_access
  + 20 * fallout_pretransition_air_winter_reclamation
  + 15 * fallout_pretransition_air_winter_adaptation
  + 10 * fallout_pretransition_air_winter_recovery
  + 5 * fallout_pretransition_air_winter_shelter_capacity

access = clamp(access_numerator / 100, 0, 100)
```

### Operational industry

```text
operational_factories =
    fallout_building_damage_after_non_damaged_industrial_complex
  + fallout_building_damage_after_non_damaged_arms_factory

industry = clamp(10 * operational_factories, 0, 100)
```

Ten surviving factories saturate this signal. Larger industrial concentrations still matter through population coverage and other state hubs, but cannot exceed the common 0 to 100 scale.

### Logistics

The province supply network is deliberately collapsed before the resource ledger is built. Its zero receipt is part of the opening condition. Initial local logistics therefore comes from surviving state infrastructure only.

```text
logistics = clamp(20 * fallout_building_damage_after_non_damaged_infrastructure, 0, 100)
```

No hidden supply-node or railway bonus is restored by the resource formula.

### Port capacity

```text
port_capacity = 0 when fallout_pretransition_coastal is absent

port_capacity = clamp(
    15 * fallout_pretransition_non_damaged_naval_base
  + 10 * fallout_building_damage_after_non_damaged_dockyard,
    0,
    100
) when fallout_pretransition_coastal is present
```

Coastline without a surviving port produces no port score.

### Fuel source

```text
fuel_source = clamp(
    4 * fallout_pretransition_resource_oil
  + 30 * fallout_pretransition_non_damaged_synthetic_refinery
  + 10 * fallout_pretransition_non_damaged_fuel_silo,
    0,
    100
)
```

Fuel silos are a bounded reserve source. They cannot replace oil or synthetic production by themselves.

### Power source

```text
hydro_levels =
    fallout_pretransition_non_damaged_dam
  + fallout_pretransition_non_damaged_dam_mountain
  + fallout_pretransition_non_damaged_cataract_dam_mountain

reactor_levels =
    fallout_pretransition_non_damaged_nuclear_reactor
  + fallout_pretransition_non_damaged_nuclear_reactor_heavy_water
  + fallout_pretransition_non_damaged_commercial_nuclear_reactor

power_source = clamp(
    45 * hydro_levels
  + 50 * reactor_levels
  + 4 * fallout_pretransition_resource_coal
  + 3 * operational_factories,
    0,
    100
)
```

A single operational reactor or major dam is important but still depends on access, logistics, and surviving industry in the final Power formula.

### Material stock

```text
material_stock = clamp(
    2 * fallout_pretransition_resource_steel
  + 2 * fallout_pretransition_resource_aluminium
  + fallout_pretransition_resource_tungsten
  + fallout_pretransition_resource_chromium
  + fallout_pretransition_resource_rubber,
    0,
    100
)
```

These deposits represent accessible reusable material, not finished equipment.

### Salvage stock

```text
removed_levels =
    fallout_building_damage_before_infrastructure
  - fallout_building_damage_after_infrastructure
  + fallout_building_damage_before_industrial_complex
  - fallout_building_damage_after_industrial_complex
  + fallout_building_damage_before_arms_factory
  - fallout_building_damage_after_arms_factory
  + fallout_building_damage_before_air_base
  - fallout_building_damage_after_air_base
  + fallout_building_damage_before_dockyard
  - fallout_building_damage_after_dockyard

preexisting_damaged_levels =
    fallout_pretransition_damaged_infrastructure
  + fallout_pretransition_damaged_industrial_complex
  + fallout_pretransition_damaged_arms_factory
  + fallout_pretransition_damaged_air_base
  + fallout_pretransition_damaged_dockyard

salvage_stock = clamp(
    10 * removed_levels
  + 6 * preexisting_damaged_levels
  + 0.30 * urban_identity,
    0,
    100
)
```

Ruins can contain valuable scrap. The separate Access component prevents a vitrified or inaccessible ruin from becoming an automatic industrial advantage.

### Communication capacity

```text
communication_capacity = clamp(
    35 when fallout_pretransition_capital is present
  + 20 * fallout_pretransition_non_damaged_radar_station
  + 5 * fallout_building_damage_after_non_damaged_air_base
  + 8 * fallout_building_damage_after_non_damaged_infrastructure,
    0,
    100
)
```

The capital contribution is zero when the state was not a pretransition capital.

## Category signals

The formula uses the frozen Air Winter original category. It does not read the later live state category.

| Frozen category | Rural identity | Urban identity |
| --- | ---: | ---: |
| wasteland | 0 | 0 |
| enclave | 45 | 20 |
| tiny island | 35 | 10 |
| small island | 55 | 15 |
| pastoral | 100 | 10 |
| rural | 90 | 20 |
| town | 65 | 40 |
| large town | 50 | 55 |
| city | 30 | 70 |
| large city | 20 | 85 |
| metropolis | 10 | 95 |
| megalopolis | 5 | 100 |
| large island | 65 | 45 |

### Administrative identity

`administrative_identity` is 100 for a pretransition capital. Otherwise it is half of `urban_identity`.

## State resource formulas

Every row below totals 100 weight points.

| Resource | Weighted component signals |
| --- | --- |
| Food | 45 Food Reserve, 20 Rural identity, 10 Port capacity, 10 Reclamation, 15 Access |
| Clean water | 50 Water Security, 15 Shelter Capacity, 15 Logistics, 10 Adaptation, 10 Access |
| Medicine | 25 Urban identity, 25 Industry, 20 Recovery, 15 Adaptation, 15 Access |
| Scrap | 35 Salvage stock, 20 Industry, 20 Material stock, 25 Access |
| Fuel | 50 Fuel source, 20 Logistics, 15 Industry, 15 Access |
| Power | 50 Power source, 20 Industry, 15 Logistics, 15 Access |
| Filters | 40 Industry, 20 Shelter Capacity, 15 Adaptation, 10 Reclamation, 15 Access |
| Shelter capacity | 55 Shelter Capacity, 15 Logistics, 10 Urban identity, 10 Adaptation, 10 Access |
| Recognition | 35 Communication capacity, 25 Administrative identity, 15 Urban identity, 15 Recovery, 10 Access |

Food Reserve, Water Security, Shelter Capacity, Reclamation, Adaptation, and Recovery refer to the frozen `fallout_pretransition_air_winter_*` values.

The general `fallout_survival_value` is not a numerical resource input. It remains the separate accepted viability value used by continuation and successor selection. This prevents its correlated Air Winter, infrastructure, population, damage, and geography terms from being counted again across all nine resources.

## Recognition archetype adjustment

Government can organize envoys, legal claims, religious networks, radio discipline, and external trust. It cannot create the eight physical resources. The archetype adjustment therefore applies only to the country Recognition value after physical aggregation.

| Archetype | Recognition adjustment |
| --- | ---: |
| continuity government | 15 |
| bunker authority | -5 |
| warlord command | -15 |
| food compact | 5 |
| maritime remnant | 10 |
| quarantine state | 0 |
| scavenger syndicate | -10 |
| nomad convoy | -10 |
| machine protocol | -15 |
| technate | 5 |
| mutant polity | -20 |
| religious refuge | 5 |

The final Recognition initialization is:

```text
initial_recognition = clamp(country_base_recognition + archetype_adjustment, 0, 100)
```

No generic region or country-memory adjustment is applied. A selected successor's memory must change resources through its manually reviewed opening content, not through a hidden 99-row bonus table.

## Immutable and mutable relationship

At numerical commit:

- `fallout_survival_initial_entries^0` is zero
- `fallout_survival_current_entries^0` is zero
- indexes 1 through 8 set `initial` equal to the physical country base
- index 9 sets `initial` equal to the adjusted Recognition value
- every `current` entry is copied from its matching `initial` entry

After global commit:

- raw arrays never change
- state numerical arrays never change
- `initial` never changes
- only `current` can change
- every current mutation clamps its result to 0 through 100
- later gameplay never sets `current` by recopying live map state

This preserves a stable opening profile for event memory, AI comparison, recovery reporting, and Year 10 history.

## Transaction order

The accepted formula-neutral identity transaction remains the first phase. The proposed numerical transaction is a second phase with one coordinator.

Proposed effect ownership:

- `fallout_reset_provisional_survival_numerical_payload` clears every numerical field while global ready is absent and never touches identity
- `fallout_recover_uncommitted_survival_numerical_transaction` owns the one exact retry signature
- `fallout_commit_survival_numerical_transaction` is the sole producer and sole ready-flag setter

1. Require survivor-allocation phase, current allocation, current player-planning ledger, current survival identity payload, no transition error, no player-continuation commit, and no survival ready flag.
2. Set the existing `fallout_survival_ledger_building` flag. Identity staging and numerical staging never own separate build flags.
3. Clear every numerical array, every state and country numerical row flag, and every numerical commit timestamp while the global ready flag is absent. A row-level commit flag is provisional until the global ready flag exists. Preserve identity arrays and provenance.
4. Iterate the frozen global state ledger in stable index order.
5. Replay and validate every required snapshot, Air Winter, grading, population, building, rewrite, and supply generation.
6. Produce all ten entries of the state numerator, denominator, and equal-share arrays.
7. Set the state row commit flag only after the complete state row validator passes.
8. Iterate the frozen country ledger in stable index order.
9. Select states through `fallout_survival_state_owner`, not current live ownership.
10. Aggregate all nine resources, record physical country raw arrays, apply the Recognition adjustment, and copy initial values to current values.
11. Set the country row commit flag only after the complete country row validator passes.
12. Record global numerical commit date and arithmetic day.
13. Run a precommit exact replay validator across every frozen state and country row.
14. Clear `fallout_survival_ledger_building`.
15. Set `fallout_survival_ledger_ready` as the final write. No effect follows it in the transaction.

If any validation fails, the coordinator clears every provisional numerical array and row flag, clears the build flag and numerical timestamps, records exactly one `survival_ledger_incomplete` error, and leaves the accepted identity transaction intact. It never writes a partial ready flag.

A dedicated numerical recovery effect owns only this exact error signature. During survivor allocation, with current allocation, player planning, survival identity, no player continuation commit, no global ready flag, and exactly one `survival_ledger_incomplete` error, recovery clears that error and immediately invokes the ordinary numerical coordinator. Any different error, later phase, ready ledger, or player-continuation receipt remains closed.

Once the ready flag exists, both identity and numerical initialization effects are no-ops.

## Required validators

### State row

The durable state-row trigger must prove:

- exact array lengths and exact resource ids
- zero sentinels
- denominator 100 for indexes 1 through 9
- numerator range 0 through 10,000
- equal-share range 0 through 100
- exact produced or not-applicable branch from the frozen Air Winter source kind
- exact replay of every common signal
- exact replay of every weighted resource numerator
- exact replay of every final rounded share
- current transition generation for all source receipts
- a state row commit flag written after the row was complete

### Country row

The durable country-row trigger must prove:

- exact array lengths and exact resource ids
- zero sentinels
- raw denominator exactly 100 for indexes 1 through 9
- raw numerator range 0 through 10,000
- exact all-and-only membership through frozen state-owner rows
- exact exclusion of not-applicable rows from coverage, hub, and `weight_sum`
- exact continuous population weight for every produced state
- exact broad and hub weights for every resource
- exact maximum unrounded state numerator for the hub result
- aggregation from unrounded state numerators without an intermediate integer share
- exact physical base result
- exact Recognition archetype adjustment
- `initial` range 0 through 100
- `current` range 0 through 100
- `current` equals `initial` before the global ready flag is written
- a country row commit flag written after the row was complete

After the global ready flag is written, the durable proof does not require `current` to remain equal to `initial`.

### Global row

The global validator must prove:

- every identity row is still durable
- every frozen state has exactly one committed numerical row
- every frozen country has exactly one committed numerical row
- every country owns at least one frozen state with a produced Air Winter source row
- no state contributes to more than one country
- country and state counts match the accepted allocation ledger
- numerical commit time is not earlier than identity staging time
- every country accumulator and multiplication remains inside the documented static arithmetic bound derived from frozen state count and maximum population weight
- ready is absent while numerical building is active
- ready exists only when the exact replay proof passes

## Determinism and exploit controls

- State and country iteration use the existing stable physical indexes.
- Numerical call sites traverse `global.fallout_survival_ledger_states` and `global.fallout_survival_ledger_countries` only. They do not reopen a world iterator.
- No new event target is required. The frozen scope arrays and stored `fallout_survival_state_owner` pointer are sufficient.
- Tied hub scores resolve to the lowest stable state index if a hub identity is recorded for debugging.
- State contribution uses frozen allocation ownership. Annexation before a later scheduler tick cannot rewrite initialization.
- Population weight is continuous, has a 0.001 floor, and has an 8-point cap.
- An almost empty state contributes only the 0.001 floor to broad coverage.
- A specialist state can still contribute through the hub term. Its maximum hub share is 10 percent for local consumables, 25 percent for industrial resources, and 30 percent for Recognition. Acceptance of that hub rule is an explicit design choice.
- Populations above eight million do not grow the coverage weight without limit.
- Deposits and specialized buildings are capped inside their normalized signals.
- A coastal flag without a port gives no Food bonus.
- Every fuel-silo level contributes 10 points to the Fuel source signal. The complete Fuel source signal remains capped at 100 before the remaining Fuel weights apply.
- Ruin damage creates salvage stock, but Access remains a separate 25 percent requirement.
- Collapsed supply nodes and railways do not secretly reappear as Logistics.
- No archetype adjusts a physical resource.
- No player reservation, player-control flag, or human status grants resources or Recognition.

### Arithmetic bound

The installed map contains 1,081 vanilla state definition files and this mod adds no `history/states` files. With state score at 100, population weight at 8, and every state assigned to one country:

```text
maximum weight_sum = 1,081 * 8 = 8,648
maximum weighted_sum = 1,081 * 8 * 100 = 864,800
maximum coverage = 100
maximum country_raw_numerator = 100 * 100 = 10,000
country_raw_denominator = 100
```

Dividing the coverage accumulator before the broad and hub blend keeps the stored country numerator within the same 10,000-point bound as a state row. The coverage division is not rounded. The implementation proof must re-count the installed map and confirm the 864,800 accumulator bound before coefficients are committed. Any later state-map expansion requires the bound and its typed maximum-state constant to be reviewed again.

The installed script-concept documentation confirms fixed-point arithmetic but does not publish its absolute numeric ceiling. This ordering deliberately keeps the largest proposed value below 865,000. Runtime overflow behavior remains unobserved because HOI4 was not run.

## Balance expectations for static review

The following are review targets, not runtime proof.

| State pattern | Expected strongest resources | Expected weak resources |
| --- | --- | --- |
| rural refuge with strong Air Winter ledgers | Food, Clean water | Scrap, Fuel |
| surviving port remnant | Food, Recognition | Power without a source |
| dead industrial city with partial access | Scrap | Food, Shelter capacity |
| oil state with damaged roads | Fuel as a hub, limited country coverage | Medicine |
| dam or reactor enclave | Power as a hub | Food without reserves |
| bunker capital | Shelter capacity, Recognition | Food unless surrounding states produce it |
| vitrified metropolis | Salvage potential, very low usable access | Food, Clean water, Medicine, Shelter capacity |

Static scenario tables must be added with the implementation and must include at least:

- one small one-state successor
- one large successor with more than ten states
- one maritime or island successor
- one altered successor
- one country with an isolated fuel hub
- one country with no specialty assets
- one country with two tied resource hubs

The tables must show every component, state result, population weight, hub, country numerator, country denominator, base value, Recognition adjustment, initial value, and current value.

## Schema version policy

Acceptance would promote `fallout_survival_ledger_schema.version` from 1 to 2 and record version 1 as the identity-only predecessor. A version-1 row can never be treated as numerically committed because no version-1 effect can set the global ready flag.

The added frozen and post-rewrite source fields also require promotion of `fallout_world_end_schema.version` from the current live value 11 to 12. If another accepted transition-schema tranche lands first, implementation must allocate the then-highest live version plus one and update this plan before code review.

There is no value migration. A version-1 survival identity may be cleared and restaged only when its world snapshot already satisfies the promoted source contract and no destructive phase is replayed. An older world snapshot fails closed. No effect reads later live buildings, deposits, Air Winter values, or ownership to fill a missing source.

## Known preflight blocker outside this proposal

The current dirty strategic-singularity work adds Fallout request source 8. The live `fallout_world_snapshot_rows_are_current` proof still caps the frozen request source at `legacy_fallout`, which is source 7. A strategic-singularity request therefore cannot pass the snapshot proof required by this numerical producer.

This proposal does not own or patch that work. Its owner must align the request-source upper-bound validation before the numerical tranche can pass preflight for every accepted terminal source. The ordinary Air Contamination and existing terminal-source routes remain separate from that unresolved dirty hunk.

## Implementation surface after acceptance

The numerical tranche would touch only reviewed Fallout-owned files and aligned documentation.

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/script_constants/fallout_world_end_constants.txt` for the required world-transition schema promotion only
- `common/scripted_effects/fallout_survival_ledger_effects.txt`
- `common/scripted_triggers/fallout_survival_ledger_triggers.txt`
- `common/scripted_effects/fallout_world_end_effects.txt`
- `common/scripted_triggers/fallout_world_end_triggers.txt`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_SURVIVAL_LEDGER_IDENTITY_TRANSACTION_PROOF.md`
- a new numerical transaction proof under the same plan folder

`common/script_constants/fallout_world_end_constants.txt` currently contains overlapping user-owned work. It must not be edited or staged until those hunks are reconciled. The future numerical tranche still requires a narrow world-transition schema promotion there because old snapshot rows do not contain the proposed specialty-source fields. Numerical coefficients belong in the dedicated Fallout event constants file.

Any new reusable dynamic helper must be documented in `common/scripted_effects/chaosx_dynamic_effects.md` in the same change. No helper is proposed merely to bypass a static effect field.

## Engine references and precedents

Primary syntax authority:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md` for variable arithmetic, clamping, rounding, arrays, `for_each_scope_loop`, and stable loop values
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` for exact variable comparison, array validation, and `all_of_scopes`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md` for `resource@type`, `building_level@type`, `damaged_building_level@type`, and `non_damaged_building_level@type` in state scope
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md` for variable scope and typed script constants
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md` for shared tuning schemas
- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` for arrays, indexes, and scope-valued variables
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` for arithmetic and loop effects
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` for variable and scope validation
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` for state and country ownership context

Vanilla precedents inspected:

- `events/AAT_Finland.txt` for `for_each_scope_loop` over stored scopes
- `events/BBA_ItaloEthiopianWar.txt` for engine-native variable rounding
- `events/GOE_Raj.txt` for ordered rounding and clamping of calculated values

The read-only HOI4 event inspection tool returned internal errors for both namespace and file selectors during the independent architecture audit. No event-inspection result is claimed. The proposal's engine evidence is the installed official documentation, offline wiki snapshot, direct vanilla source, and direct repository source listed here.

Repository precedents:

- `fallout_calculate_expected_state_survival_value` for a deterministic frozen-input calculation with final clamp and round
- the Fallout grade, population-loss, permanent building-loss, and supply-collapse receipts for replayable destructive outcomes
- the Air Winter 0 to 100 ledgers for food, water, shelter, adaptation, reclamation, recovery, and exposure
- `fallout_stage_survival_ledger_identity_transaction` for stable state and country indexes and all-and-only allocation coverage
- `006_independence_wave_effects.txt` and `006_independence_wave_triggers.txt` for aligned scope arrays and index validation

## Explicit coefficient and proxy approvals required

Approval must cover each of these choices. They are design tuning, not conclusions supplied by engine documentation.

- the grade-access table and every common-signal coefficient
- the category identity table
- the Medicine proxy based on urban institutions, surviving industry, recovery, adaptation, and access
- the Filters proxy based on surviving industry, shelter, adaptation, reclamation, and access
- the Food port contribution
- the Fuel source coefficients for oil, refineries, and fuel silos
- the Power source coefficients for dams, reactors, coal, and factories
- the Recognition capital, communications, and archetype coefficients
- the continuous population floor, scale, and cap
- the 90 and 10, 75 and 25, and 70 and 30 coverage-to-hub blends
- exclusion of Air Winter not-applicable rows from country aggregation
- use of pretransition non-damaged specialty assets only while the destructive rewrite leaves them unchanged
- no generic region or country-memory adjustment at initialization

## Acceptance choice

Approval of this proposal would authorize the numerical implementation exactly as written, including the required snapshot additions, formula weights, aggregation bands, Recognition adjustment, replay validators, idempotent commit order, and sole ready-flag setter.

If any coefficient, input, aggregation rule, or archetype adjustment should change, revise this document before implementation. Silence does not count as acceptance.

## Out of scope

This proposal does not authorize:

- manual scenario activation
- scheduler activation setters
- living-world event implementation
- successor package creation
- focus, decision, leader, unit, diplomacy, or AI package creation
- GUI changes
- a numerical region bonus
- a hidden country-memory bonus table
- any fallback value for absent snapshot inputs

HOI4 was not run. Runtime persistence, multiplayer observation, and save interruption behavior remain unobserved.

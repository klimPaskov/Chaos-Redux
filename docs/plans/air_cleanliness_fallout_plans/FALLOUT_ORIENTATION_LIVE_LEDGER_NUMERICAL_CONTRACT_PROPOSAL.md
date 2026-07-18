# Fallout orientation live-ledger numerical contract

## Status

Proposed for user approval. This document does not authorize gameplay edits until the user approves its numerical choices and repair disposition.

The accepted Ash-week orientation contract remains dormant. Events `chaosx.fallout.62` through `chaosx.fallout.65` remain uncounted pilot blocks. Events `66` through `84` remain incomplete. This proposal does not authorize a caller, successor materialization, scheduler activation, manual scenario activation, or any recurring country iterator.

## Decision request

Approval is requested for three exact live-ledger decisions:

1. initialize Survival Cohesion from the already committed Food, Shelter capacity, and Recognition values
2. promote the already accepted state Logistics signal into an immutable opening and mutable current Supply Access ledger
3. translate current Supply Access into a live native state supply modifier

Exact instant repair of one damaged infrastructure level remains a separate engine blocker. Approval of the three numerical decisions does not authorize a repair substitute.

## Evidence boundary

The current repository proves the following facts.

| Surface | Current evidence | Disposition |
| --- | --- | --- |
| Food, Shelter capacity, and Recognition | committed country values from 0 through 100 with immutable initial and mutable current arrays | accepted inputs |
| Survival Cohesion | described in the accepted baseline, but no opening numerical producer exists | formula requires approval |
| state Logistics | accepted as `clamp(20 * fallout_building_damage_after_non_damaged_infrastructure, 0, 100)` during opening resource calculation | accepted formula, not yet persisted |
| `fallout_orientation_state_supply` | written only inside the dormant orientation helper file and read by no native supply consumer | shadow value, must be removed |
| Air Winter ledgers | live state variables exist for Exposure, Recovery, Adaptation, Food Reserve, Shelter Capacity, Reclamation, and Water Security | accepted live state surfaces |
| damaged infrastructure | `damaged_building_level@infrastructure` and `non_damaged_building_level@infrastructure` expose observed state | proven read surfaces |
| infrastructure damage | `damage_building` is documented and used by vanilla | proven failure effect |
| exact infrastructure repair | no documented effect restores exactly one damaged level | blocked |

The accepted survival numerical contract already states that initial local Logistics comes only from surviving state infrastructure because Fallout collapses supply nodes and railways before the numerical ledger is built. This proposal preserves that rule.

## Country Survival Cohesion

### Meaning

Survival Cohesion measures internal acceptance of the surviving government. It is distinct from Recognition, which represents external contact, administrative identity, and diplomatic standing.

The accepted baseline says opening Cohesion comes from food security, shelter fairness, and old legitimacy. No successful post-Fallout mission exists before orientation. The opening formula therefore uses exactly the three committed values that represent those sources.

### Durable fields

Each committed Fallout country row receives:

- `fallout_survival_cohesion_initial`
- `fallout_survival_cohesion_current`
- `fallout_survival_cohesion_generation`
- `fallout_survival_cohesion_schema_version`
- `fallout_survival_cohesion_row_committed`

The orientation-only variable `fallout_orientation_cohesion` is retired. Orientation roots freeze `fallout_survival_cohesion_current` into `fallout_orientation_frozen_cohesion`. All orientation costs and results mutate `fallout_survival_cohesion_current` through one clamp-owning helper.

### Opening formula

The exact proposed formula is:

```text
cohesion_numerator =
    35 * fallout_survival_initial_entries^food
  + 35 * fallout_survival_initial_entries^shelter_capacity
  + 30 * fallout_survival_initial_entries^recognition

fallout_survival_cohesion_initial =
    clamp(round(cohesion_numerator / 100), 0, 100)

fallout_survival_cohesion_current = fallout_survival_cohesion_initial
```

The weights total 100. Rounding occurs once after the final division. Recognition already contains its accepted archetype adjustment. No second archetype adjustment is applied to Cohesion. Region and country memory apply no hidden opening bonus.

### Static examples

The values below use the accepted country scenarios in `FALLOUT_SURVIVAL_NUMERICAL_TRANSACTION_PROOF.md`.

| Reviewed scenario | Food | Shelter | Recognition | Proposed opening Cohesion |
| --- | ---: | ---: | ---: | ---: |
| small one-state successor | 74 | 62 | 31 | 57 |
| large twelve-state successor | 43 | 45 | 56 | 48 |
| maritime successor | 64 | 54 | 58 | 59 |
| altered successor | 27 | 45 | 11 | 29 |
| isolated fuel-hub successor | 72 | 61 | 14 | 51 |
| successor with no specialty assets | 45 | 44 | 28 | 40 |
| successor with tied power hubs | 63 | 60 | 42 | 56 |

These examples preserve a useful distinction between physical survival and external Recognition. The altered successor begins with usable shelter and weak Recognition, producing low internal Cohesion without a special mutant penalty.

### Transaction ownership

The survival numerical coordinator remains the sole opening producer. It writes the Cohesion initial value after all nine country resource initial entries exist and before the country row commit flag. The global precommit validator proves the formula exactly and requires current to equal initial. After `fallout_survival_ledger_ready`, the durable validator requires initial to remain exact and current to remain within 0 through 100.

The orientation caller no longer supplies a Cohesion value. A caller-supplied value could diverge from the committed country row and is rejected by this contract.

## State Supply Access

### Meaning

Supply Access measures how much local distribution capacity remains usable inside a Fallout state after the province supply network has collapsed. It does not recreate a supply hub or railway. It is a bounded state ledger that drives a native local-supply modifier and later Fallout content.

### Durable fields

Each produced Fallout state row receives:

- `fallout_state_supply_access_initial`
- `fallout_state_supply_access_current`
- `fallout_state_supply_access_generation`
- `fallout_state_supply_access_schema_version`
- `fallout_state_supply_access_row_committed`
- `fallout_state_supply_impact_factor`

Air Winter not-applicable rows receive typed zero initial and current values. They do not become valid orientation targets.

### Opening formula

The proposal promotes the already accepted Logistics calculation without changing its coefficient:

```text
fallout_state_supply_access_initial = clamp(
    20 * fallout_building_damage_after_non_damaged_infrastructure,
    0,
    100
)

fallout_state_supply_access_current = fallout_state_supply_access_initial
```

The formula reads the durable post-rewrite non-damaged infrastructure receipt. It does not read later live infrastructure during opening initialization. It grants no supply-node, railway, port, or hidden country bonus.

### Native supply translation

A dedicated Fallout state dynamic modifier consumes `fallout_state_supply_impact_factor` through the documented `local_supply_impact_factor` state modifier.

The exact proposed translation is:

```text
fallout_state_supply_impact_factor = clamp(
    -0.50 + 0.005 * fallout_state_supply_access_current,
    -0.50,
    0
)
```

This produces the following stable mapping.

| Current Supply Access | Native local supply impact |
| ---: | ---: |
| 0 | -50 percent |
| 20 | -40 percent |
| 40 | -30 percent |
| 60 | -20 percent |
| 80 | -10 percent |
| 100 | 0 percent |

Supply Access represents restoration toward ordinary capacity. It never creates an above-normal supply bonus. An orientation result of plus 6 improves the native local supply impact by 3 percentage points.

This modifier stacks with the existing Air Winter phase `local_supplies` effect. It does not replace the phase ladder. The phase modifier represents environmental loss at the state's current winter phase. Supply Access represents how much surviving infrastructure can distribute after that phase loss. Approval of this proposal accepts that two-part native supply result.

One state-scoped helper owns every current mutation, the 0 through 100 clamp, factor recomputation, and dynamic-modifier refresh. The opening numerical coordinator calls it directly for each committed produced state. Orientation calls it only on the authenticated state target. Later Fallout events, focuses, and decisions must use the same helper. No daily or monthly world iterator is authorized.

### Schema policy

These derived ledgers require promotion of `fallout_survival_ledger_schema.version` from 2 to 3. They do not require a world-transition schema promotion because every input already exists in world-transition schema 12.

There is no fabricated migration. An uncommitted schema-2 survival row may be cleared and rebuilt only through the ordinary numerical coordinator while the accepted transition phase still permits that transaction. A committed or later-phase row without schema 3 fails closed.

## Live Air Winter result mapping

The accepted orientation results must stop writing the isolated `fallout_orientation_state_*` family. The authenticated bound state receives mutations through these canonical surfaces:

| Accepted result term | Canonical live surface |
| --- | --- |
| target exposure | `air_winter_exposure` |
| target shelter | `air_winter_shelter_capacity` |
| target adaptation | `air_winter_adaptation` |
| target reclamation | `air_winter_reclamation` |
| target supply value | `fallout_state_supply_access_current` |
| target phase | `air_winter_phase`, display and validation only |
| target grade | `fallout_state_grade`, display and validation only |

Recovery needs one additional ownership rule because `air_winter_recovery` is recalculated from recovery pressure during the Air Winter cycle. A durable orientation recovery gain writes the same delta to `air_winter_recovery_bonus` and to the current displayed `air_winter_recovery` value. Both values clamp to 0 through 100. The first write preserves the gain through later Air Winter recalculation. The second makes the result visible immediately without forcing a full state-pressure recalculation inside an event result.

Country Food, Clean water, Medicine, Filters, Scrap, Fuel, Power, Shelter capacity, and Recognition continue to use `fallout_survival_current_entries`. State Food Reserve remains an Air Winter state value and is not silently substituted for the country Food resource.

Every state mutation requires the same current transition generation, the committed state identity row, the schema-3 Supply Access row, an owned and controlled assigned capital or reviewed main state, and a produced Air Winter row. A missing or stale surface records a typed diagnostic and applies no partial state result.

## Exact infrastructure repair blocker

Official effect documentation proves the following surfaces:

- `damage_building` damages a selected building in state scope
- `add_building_construction` starts construction
- `set_building_level` sets total building level
- `damaged_building_level@infrastructure` reads damaged infrastructure
- `non_damaged_building_level@infrastructure` reads operational infrastructure

None of these documents an operation that removes exactly one damaged infrastructure level while preserving total building level. Vanilla search found no negative `damage_building` precedent and no dedicated building-repair effect.

The accepted capital success result that says `repair one eligible infrastructure level` therefore remains blocked. `add_building_construction`, instant construction, a total-level setter, a broad repair-speed modifier, and a variable-only receipt are not exact substitutes.

If the user keeps the exact result, events `66` through `69` remain outside the release floor until an engine-native repair surface can be proven. If the user wants to revise the result, that revision needs a separate explicit approval naming the replacement effect and acknowledging that it changes the accepted branch outcome.

## Implementation surface after approval

Approval authorizes a bounded dormant implementation across:

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/scripted_effects/fallout_survival_ledger_effects.txt`
- `common/scripted_triggers/fallout_survival_ledger_triggers.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
- `common/dynamic_modifiers/fallout_world_end_orientation_dynamic_modifiers.txt`
- aligned Fallout modifier localisation, proof documents, and source specs

Implementation must remove caller-supplied Cohesion and Supply Access inputs, retire the isolated orientation state mirrors, and preserve all current approval gates until exact row validators pass. It must not define events `66` through `84` merely to fill reserved ids while the exact repair, coverage rows, government rows, and candidate registries remain blocked.

## Validation scenarios

Static review must prove at least:

1. all seven accepted country scenarios reproduce the Cohesion values in this document
2. one produced state at each infrastructure level from 0 through 5 produces Supply Access 0, 20, 40, 60, 80, and 100
3. every Supply Access result produces the exact native local supply impact in the mapping table
4. a plus 6 Supply Access result changes 40 to 46 and changes native impact from minus 30 percent to minus 27 percent
5. a minus 5 result at Supply Access 3 clamps to 0 and native impact clamps to minus 50 percent
6. orientation exposure, shelter, adaptation, reclamation, and recovery changes mutate only the authenticated bound state
7. a recovery gain survives a later Air Winter recovery recalculation through `air_winter_recovery_bonus`
8. a stale Supply Access row blocks the whole state result with no partial mutation
9. the exact repair path remains unreachable while its approval gate is unset
10. no caller, scheduler activation setter, manual scenario activation setter, or recurring country iterator is added

HOI4 will not be run. Runtime persistence, save interruption, dynamic-modifier refresh timing, and multiplayer observation remain unobserved.

## Approval record

Not approved yet.

User approval must explicitly cover:

- the 35 Food, 35 Shelter capacity, and 30 Recognition opening Cohesion weights
- use of Recognition after its accepted archetype adjustment with no second archetype bonus
- promotion of the accepted Logistics formula into State Supply Access
- the minus 50 percent through 0 percent native local-supply translation
- stacking Supply Access with the existing phase `local_supplies` effect
- durable Recovery gains through `air_winter_recovery_bonus`
- survival ledger schema 3 with no fabricated migration

The exact one-level infrastructure repair clause remains blocked unless the user separately revises it or a documented engine-native repair surface is proven.

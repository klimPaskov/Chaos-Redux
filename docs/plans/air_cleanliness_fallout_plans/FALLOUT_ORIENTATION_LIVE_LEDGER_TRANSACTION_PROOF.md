# Fallout orientation live-ledger transaction proof

## Status

Implemented as a dormant schema-3 survival transaction on 2026-07-18. This proof covers the accepted Cohesion, State Supply Access, native supply translation, and live Air Winter result mapping. It does not approve the exact capital repair path, define events `66` through `84`, add an orientation caller, activate the living-world scheduler, or activate the public manual scenario.

HOI4 was not run at the user's direction. Runtime persistence, save interruption, dynamic-modifier refresh timing, multiplayer observation, and literal lobby-host behavior remain unobserved.

The read-only event inspector was pointed at `events/fallout_world_end_events.txt` with helper expansion and lint enabled. It stopped at its fixed `EVENT_HELPER_PROJECTION_LIMIT` of 200000 projected helper operations and returned no artifacts. This is a tooling ceiling, not a successful engine validation and not evidence against the dormant pilot.

## Accepted numerical contract

Country Cohesion opens as:

```text
clamp(round((35 * Food + 35 * Shelter capacity + 30 * Recognition) / 100), 0, 100)
```

Recognition is the already archetype-adjusted opening value. The formula applies no second archetype, region, or country-memory adjustment.

State Supply Access opens as:

```text
clamp(20 * post-rewrite non-damaged infrastructure, 0, 100)
```

Its native state supply translation is:

```text
clamp(-0.50 + 0.005 * current Supply Access, -0.50, 0)
```

## Transaction ownership

`common/script_constants/fallout_world_end_event_constants.txt` promotes `fallout_survival_ledger_schema.version` from 2 to 3. It records schema 2 as `previous_without_orientation_live_ledgers`. No migration effect fabricates schema-3 values. An uncommitted older row can only be cleared and rebuilt through the existing ordinary numerical coordinator. A committed older row fails the current-schema triggers.

`common/scripted_effects/fallout_survival_ledger_effects.txt` remains the sole opening producer. It writes Cohesion only after all nine country resource entries exist. It writes Supply Access from the durable post-rewrite infrastructure receipt inside the existing frozen-state array pass. Independent replay values bind both opening calculations before the row commit flags. The global ready flag remains the final successful transaction write.

The only mutable Cohesion writer is `fallout_survival_apply_cohesion_delta`. The only mutable Supply Access writer is `fallout_state_apply_supply_access_delta`. Both helpers own their inclusive 0 through 100 clamps. The state helper also recalculates the native impact and immediately refreshes the modifier.

Schema-3 reset clears the retired `fallout_orientation_cohesion` and `fallout_orientation_state_*` shadows. The begin request no longer accepts caller-supplied Cohesion or state Supply Access.

## Engine-sensitive supply surface

The official installed documentation proves these surfaces:

- `documentation/modifiers_documentation.md` identifies `local_supply_impact_factor` as a state modifier at lines 3245 through 3247.
- `documentation/effects_documentation.md` identifies `add_dynamic_modifier` as valid in state scope at lines 1153 through 1166.
- `documentation/effects_documentation.md` identifies `force_update_dynamic_modifier` as valid in state scope and says it avoids waiting for the daily update at lines 4372 through 4379.
- The same effects documentation lists `remove_dynamic_modifier` for state scope.

Repository precedent uses `local_supply_impact_factor = var:...` in `common/dynamic_modifiers/013_natural_disasters_state_modifiers.txt`. Existing Chaos Redux effects add state dynamic modifiers once and call `force_update_dynamic_modifier = yes` after variable changes.

`common/dynamic_modifiers/fallout_world_end_orientation_dynamic_modifiers.txt` defines the dedicated `fallout_state_supply_access` state modifier. Produced rows receive it only after the Supply Access replay commits. Not-applicable Air Winter rows retain typed zero access, never receive the modifier, and cannot pass the orientation target trigger.

The Supply Access modifier stacks with the existing Air Winter phase `local_supplies` modifier. Supply Access never exceeds zero native impact, so it cannot create an above-normal local supply bonus.

## Live state result ownership

`fallout_orientation_state_target_is_current` requires the exact assigned capital, current ownership and control, committed state identity, current successor inventory and capital rows, a produced canonical Air Winter row, and a current schema-3 Supply Access row.

Every state result prepares signed temporary deltas and calls `fallout_orientation_apply_authenticated_state_deltas` once. The helper authenticates the target again before any Air Winter or Supply Access write. The mapping is:

| Result term | Live value |
| --- | --- |
| Exposure | `air_winter_exposure` |
| Shelter | `air_winter_shelter_capacity` |
| Recovery | `air_winter_recovery_bonus` and `air_winter_recovery` |
| Adaptation | `air_winter_adaptation` |
| Reclamation | `air_winter_reclamation` |
| Supply | `fallout_state_supply_access_current` |

Grade and phase remain frozen display and score facts. They are not state result stores. A stale state row prevents result authentication. The failed resolution records `fallout_orientation_diagnostic.state_ledger_not_current` and applies no state result.

The Air Winter recalculation in `common/scripted_effects/air_cleanliness_winter_effects.txt` adds `air_winter_recovery_bonus` to recovery pressure. Writing the same accepted delta to the bonus and current recovery value preserves it through later recalculation while making it visible immediately.

## Static arithmetic review

The seven accepted country examples produced the exact expected Cohesion values:

| Scenario | Food | Shelter | Recognition | Cohesion |
| --- | ---: | ---: | ---: | ---: |
| small one-state successor | 74 | 62 | 31 | 57 |
| large twelve-state successor | 43 | 45 | 56 | 48 |
| maritime successor | 64 | 54 | 58 | 59 |
| altered successor | 27 | 45 | 11 | 29 |
| isolated fuel-hub successor | 72 | 61 | 14 | 51 |
| no-specialty successor | 45 | 44 | 28 | 40 |
| tied-power-hub successor | 63 | 60 | 42 | 56 |

The complete infrastructure ladder produced:

| Infrastructure | Opening Supply Access | Native impact |
| ---: | ---: | ---: |
| 0 | 0 | -0.50 |
| 1 | 20 | -0.40 |
| 2 | 40 | -0.30 |
| 3 | 60 | -0.20 |
| 4 | 80 | -0.10 |
| 5 | 100 | 0.00 |

A plus 6 result from Supply Access 40 produced 46 and a native impact of -0.27. A minus 5 result from Supply Access 3 clamped to 0 and a native impact of -0.50.

Static writer review found only the opening producer and the clamp-owning helper writing `fallout_survival_cohesion_current`. It found only the opening producer and the clamp-owning helper writing `fallout_state_supply_access_current`. No daily, weekly, or monthly iterator was added.

## Gates and remaining blockers

The schema-3 country replay sets `fallout_orientation_state_result_surface_status` to approved only after exact numerical replay. Any uncommitted reset clears it. This opens the reviewed live state surface without activating a caller.

`fallout_orientation_capital_repair_surface_status` has no setter. The exact one-damaged-level infrastructure repair route therefore remains unreachable. Construction, total-level setting, repair-speed modifiers, and variable receipts were not used as substitutes.

Regional rows, country-memory coverage, government rows, character and institution registries, successor materialization, player continuation, the other nineteen reserved event blocks, logs, details, and final audits remain incomplete. Both living-world scheduler activation flags remain without a setter. The orientation package remains outside the 660-block release floor.

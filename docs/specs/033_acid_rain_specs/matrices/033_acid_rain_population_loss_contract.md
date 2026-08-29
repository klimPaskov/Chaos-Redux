# Event 033 Acid Rain state population loss contract

## Hard result

Every positive Event 33 mortality pulse must remove real civilian population from the affected state. The population transaction and the death record are one operation. A mortality implementation fails when it changes only a modifier, a manpower pool, an attrition value, a counter, or localisation.

The only authoritative death value is `state_civilian_population_loss_applied`, returned by `apply_exact_state_civilian_population_loss`.

## Transaction sequence

| Step | Required operation | Failure condition |
| --- | --- | --- |
| 1 | Read current state civilian population and the protected population floor | Uses country manpower or an estimated population instead |
| 2 | Calculate requested deaths from exposure type, current population, intensity, vulnerability, war exposure, and protection | Uses a fixed decorative death number unrelated to state population |
| 3 | Apply per-pulse, episode, and protected-floor caps | Requested loss can cross an accepted safety boundary |
| 4 | Check the generation, state, exposure type, episode, and pulse-date receipt | A repeated scheduler call can apply the pulse again |
| 5 | Call `apply_exact_state_civilian_population_loss` in state scope with the accepted cause and responsible country | Uses `local_manpower`, recruitable population, generic manpower, or a custom direct counter instead |
| 6 | Read `state_civilian_population_loss_applied` and `state_civilian_population_loss_result` | Uses requested deaths as though they were applied deaths |
| 7 | Verify post-pulse population equals pre-pulse population minus the applied loss, subject to the floor | Population did not fall by the recorded amount |
| 8 | Commit the pulse receipt and add the applied loss to state, country, and global Event 33 totals | Counters differ from the actual population transaction |
| 9 | Register the same applied loss once in Deaths | Duplicate or missing Deaths entry |
| 10 | Run casualty thresholds, reports, achievements, and prevented-death comparison after commit | Text or achievements advance from requested or estimated deaths |

## Explicit non-substitutes

None of these satisfy civilian mortality:

- `local_manpower` or `local_manpower_factor`
- recruitable-population modifiers
- a negative country manpower effect
- division strength damage or attrition
- military casualty variables
- an Event 33 death counter without population mutation
- report text that claims people died
- building destruction or supply penalties by themselves

These effects may exist as separate operational consequences. They never create Event 33 civilian deaths.

## Disabled Deaths logging

The rain remains lethal when the Deaths history or UI is disabled unless the repository's global settings contract explicitly disables civilian population loss itself. The shared exact-loss helper must use its unlogged population-removal path when necessary. A disabled log cannot convert lethal rain into a harmless modifier.

## Acceptance examples

| Scenario | Pre-pulse population | Requested | Protected floor | Applied | Post-pulse population | Deaths and Event 33 totals |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Standard opening | 1,000,000 | 400 | 10,000 | 400 | 999,600 | +400 once |
| Floor clamp | 10,050 | 400 | 10,000 | 50 | 10,000 | +50 once |
| Fully capped pulse | 5,000,000 | 50,000 | 10,000 | Accepted cap result | Pre-population minus applied | Applied value once |
| Duplicate pulse key | Any | Any positive value | Any valid floor | 0 on replay | Unchanged on replay | No second entry |
| Modifier-only prototype | Any | Counter claims deaths | Any | Invalid implementation | Population unchanged | Gate fails |
| Helper returns zero | Any | Positive request | Floor prevents loss | 0 | Unchanged | No death progress |

## Completion blocker

Event 33 cannot be marked implemented while any opening, sustained, severe, global, or superstorm pulse records deaths without an equal real state-population reduction. This remains a blocker even when reports, modifiers, GUI, achievements, and Deaths history appear correct.

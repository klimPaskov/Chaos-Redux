# Air Winter Seasonal Recurrence Proof

## Scope

This proof covers the five recurring Air Winter families carried by the existing monthly event scheduler:

| Family | Observation | Event route |
| --- | --- | --- |
| First frost | A state crosses into Phase 2 or worse from below Phase 2 | Existing regional Phase 2 routes, ids 10 through 14, exact mountain-capital id 16, and exact engine-island id 38. Event 13 stores `desert_city` or `none` to separate its exact and generic routes. Seed route 10 can schedule result 18. |
| Dark harvest | A classified food state is severe | Existing food-collapse opening 33 and result 32 |
| Ash thaw | A state drops from Phase 3 or Phase 4 to a lower phase | Existing recovery opening 50 and result 51 |
| Second winter | A presentation class is severe in a later engine year | Dedicated choice event 60 and result 61 |
| Terminal season | A Phase 6 state is observed while the cycle contamination snapshot is above 9000 basis points | Existing terminal opening 43 and result 46 |

These are Air Winter incidents. They do not activate the Fallout living-world scheduler and do not count toward the 660-block Fallout release floor.

## Engine calendar source

`air_winter_event_prepare_candidate_cycle` copies `global.year` to `global.air_winter_event_cycle_year` once after the existing Air Winter cycle opens and before the existing state pass begins.

The installed official file `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md` defines `global.year` as the current year. Script reads the stored snapshot after that assignment. It does not recalculate a year from day counts and does not compare against an unstored date during state selection.

`air_winter_event_cycle_year_is_valid` requires:

- an open Air Winter cycle
- a stored positive year
- a stored positive cycle id

Missing calendar evidence fails closed. Capture, reconciliation, candidate selection, and receipt mutation do nothing until the calendar contract returns. Global reset clears the snapshot.

## Existing pass only

The seasonal layer adds no `on_daily`, `on_weekly`, `on_monthly`, country-wide loop, or second state-wide loop. It uses:

1. the existing cycle opener
2. the existing one-state Air Winter update
3. the existing bounded candidate-country array
4. the existing post-pass country dispatch

Marker capture occurs inside `air_winter_schedule_phase_event` before its owner cooldown test. A condition observed while an owner is cooling down therefore becomes a durable row instead of disappearing at the end of the state tick.

## Marker contract

Each family has a separate state flag and six base payload fields:

- origin year
- origin cycle id
- origin owner
- origin presentation class
- frozen score
- typed event id

First frost adds a seventh field, `air_winter_first_frost_origin_route_subtype`. Its validator accepts `desert_city` only with event 13 and requires `none` for every other first-frost route.

A validator proves every required field, current ownership by the stored owner, a presentation class from 1 through 9, a positive score, a typed family route, a valid subtype where required, an origin year no later than the current snapshot, an origin cycle no later than the current cycle, and an owner receipt earlier than the origin year.

Reconciliation clears partial rows, transferred rows, impossible calendar rows, invalid routes, and rows already covered by a receipt. Valid prior-year rows remain queued. Each state holds at most one unresolved row for each family. That row preserves the earliest unconsumed observation while later observations of the same family wait for it to resolve.

## Capture rules

### First frost

The state must have changed phase during the current tick. Its previous phase is below Phase 2 and its new phase is Phase 2 or higher. Regional routing is resolved at capture time and stored in the row. The state-local order is mountain capital, engine island, exact arid urban state, generic city, coast, non-city arid or Mediterranean state, highland or polar state, then food state. The typed id preserves the mountain and island selection. Event 13 also preserves `desert_city` or `none`, so category movement cannot exchange its exact and generic interfaces before dispatch. The stored state and owner must remain valid.

When the frozen route is seed event 10, each opening choice schedules event 18 after 45 days. The child result uses the same regular state and country targets and the shared pending-owner transaction. This continuation does not write a second seasonal receipt.

### Dark harvest

The state must be severe and pass the existing food-state classifier. The row stores event 33. The level condition is frozen into a durable marker, so later food or phase recovery does not silently erase the observation.

### Ash thaw

The state must have changed phase during the current tick. Its previous phase is Phase 3 or Phase 4 and its new phase is lower. The row stores recovery event 50. The generic recovery arc remains a separate lower-priority family.

### Second winter

The state must be severe and classified into one of the nine presentation classes. The first severe observation for that owner and class seeds the corresponding country year without opening an event. A severe observation in a later engine year creates event 60's marker. The marker keeps its origin class and year even when dispatch is delayed.

### Terminal season

The state must be Phase 6 and the cycle contamination snapshot must be strictly above 9000 basis points. The row stores terminal event 43. This is an atmospheric winter incident. It does not commit a Fallout grade or bypass the Fallout request coordinator.

## Priority and tie resolution

The typed family priorities are:

1. terminal season
2. ordinary unseen phase
3. second winter
4. dark harvest
5. first frost
6. ash thaw
7. generic recovery

Within equal priority, candidate comparison uses:

1. earlier origin cycle
2. higher frozen score
3. lower state id

The country candidate stores family, priority, origin year, presentation class, origin cycle, and route subtype alongside the existing state, event id, score, and cycle id. Final dispatch rechecks every stored field against the winning state row. State iterator order cannot change the result.

## Annual receipts and carryover

The five country receipts are:

- `air_winter_first_frost_event_year`
- `air_winter_dark_harvest_event_year`
- `air_winter_ash_thaw_event_year`
- `air_winter_second_winter_event_year`
- `air_winter_terminal_season_event_year`

Each receipt stores the winning marker's origin year. A family cannot create another marker for that owner in the same year after the receipt is committed. A marker from a prior year remains valid only while its receipt is absent or earlier than the marker year.

The dispatch effect writes the receipt only after the complete candidate contract passes. It then clears only the winning marker. First frost and dark harvest reuse ordinary phase routes. Dark harvest coalesces when a validated ordinary winner is the same state and exact event id stored by the marker. First frost additionally requires the route subtype to match. Dispatch then writes that marker's origin year and clears it as one coalesced incident. It does not consume a different state, exact event 13 interface, or family. A cooldown failure or stale transient candidate does not consume the durable row.

Second winter also has nine fixed regional severe-year variables. They avoid a generated variable name and make each presentation class independently auditable. The first severe year is a seed. A later severe year is due. The regional year advances only when event 60 passes final dispatch validation.

## Second-winter event chain

`chaosx.fallout.60` provides nine regional descriptions and three government-aware choices:

- reopen ration corridors and move heat with food
- withdraw exposed households to stronger settlements
- place depots and junctions under military heating orders

The choices alter food, shelter, adaptation, exposure, refugees, disease, building pressure, category damage, Stability, War Support, or Command Power according to the selected route. Civilian losses use `air_winter_event_apply_deaths`, which routes the exact population mutation through the shared Deaths system. The military route has an exact Command Power affordability trigger and repeats it at click time. Each opening tooltip discloses the exact ledger conditions used by its delayed result.

After 45 days, `chaosx.fallout.61` resolves the stored route. Ration results test shelter and food. Withdrawal results test reclamation and shelter. Military results test building pressure and shelter. Six mutually exclusive options repeat their outcome thresholds at click time, apply distinct recovery or failure effects, record route memory, and clear the pending branch. Failure outcomes can cause further Deaths, category damage, disease, refugee pressure, or building damage.

The opening choices have explicit AI weights. Their state modifiers favor routes whose current ledgers can remain above the disclosed result thresholds after the opening cost. The result has only one valid deterministic option for the stored route and threshold result. Both events use the dedicated Air Winter report art registry and Fallout-owned paths.

## Cleanup proof

State cleanup clears all five marker flags and all thirty marker payload fields. It also clears the three second-winter pending-route flags and their outcome memories through the existing event-memory cleanup.

Country cleanup clears the five annual receipts, nine regional severe-year variables, and every seasonal candidate field. Global reset clears `global.air_winter_event_cycle_year`. The existing reset flow reaches country cleanup through its bounded owner and controller registry and reaches state cleanup during the next existing Air Winter state pass.

## Static proof results

Source inspection establishes:

- five distinct typed families and seven distinct typed priorities
- five complete marker capture, validation, clear, selection, receipt, and reset paths
- one stored engine-year snapshot per opened monthly cycle
- caller-owned initialization for every temporary helper output before marker capture
- marker capture before the cooldown gate
- prior-year marker acceptance with receipt ordering
- replacement of incomplete transient owner candidates before comparison
- nine explicit second-winter regional seed and commit branches
- final row equality checks before every seasonal receipt
- exact state, event-id, and first-frost route-subtype coalescing for seasonal routes shared with ordinary phase events
- one-marker consumption after successful validation
- no new world iterator or periodic on action
- unique ids and matching localisation for events 60 and 61
- three weighted opening choices and six deterministic delayed outcomes
- exact pre-choice AI boundaries derived from each route's immediate ledger change
- exact click-time target checks on all nine new effect-bearing options
- Deaths integration for every new population-loss path
- Phase 5 report sprite registration, DDS presence, and manifest consumers for events 60 and 61

## Independent audit

A read-only scheduler audit returned PASS for marker completeness, deterministic ordering, receipt mutation, cleanup, event guards, Deaths integration, localisation, and asset ownership.

A separate scope audit found two defects. Temporary helper outputs were not initialized by their caller, and two AI shelter tests used the delayed threshold without subtracting the route's immediate shelter gain. The implementation now initializes all three outputs before seasonal capture and uses exact pre-choice shelter boundaries of 21 and 19. A narrow re-audit of both corrections returned PASS.

## Runtime boundary

HOI4 was not launched. Static sources do not prove runtime assignment of `global.year`, regular event-target retention across the 45-day delay, exact Desert City subtype retention, popup order when several countries dispatch, AI event resolution, marker persistence through save and reload, or annual behavior across an observed year boundary. Those remain runtime observation gates and are not claimed as passing evidence.

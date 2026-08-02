# Air Winter Phase 2 Desert-City Water Convoy Addendum

Status: implemented and statically proven on 2026-07-16 after independent engine and content review. Runtime observation remains excluded. See `AIR_WINTER_PHASE_2_DESERT_CITY_EVENT_PROOF.md`.

## Scope

This tranche deepens the accepted Desert City row from the Air Winter pilot. It expands `chaosx.fallout.13` with one exact urban route and adds `chaosx.fallout.49` as its thirty-day result.

The baseline requirement is concrete. Trains and trucks decide whether an arid city keeps water moving during Phase 2. The chain therefore compares a municipal works programme, railway tanker service, and motor transport columns.

This tranche does not alter the Air Winter survival formula, monthly mortality, Fallout request rules, the blackout GUI, treaty projects, strategic bombing, active combat pressure, or the manual scenario.

## Shared event ID correction

Event ID `13` already serves two different scheduler rows:

- an exact arid urban state that should outrank the generic city route
- a non-city arid or Mediterranean regional fallback

The event ID and presentation class cannot prove which row was selected. Air Winter can also degrade state categories after a first-frost marker is recorded. The exact route must therefore carry a typed receipt instead of reconstructing identity from current state conditions.

Add `air_winter_event_route_subtype` with these values:

| Key | Value | Meaning |
| --- | ---: | --- |
| `none` | 0 | Ordinary route with no specialised subtype |
| `desert_city` | 1 | Arid urban state selected before the generic city row |
| `maximum` | 1 | Validation ceiling |

The scheduler carries the subtype through these surfaces:

1. `air_winter_selected_route_subtype` while a state route is evaluated
2. `air_winter_first_frost_origin_route_subtype` when the seasonal marker is frozen
3. `air_winter_event_candidate_route_subtype` in the country candidate ledger
4. an owner-bound opening receipt on the dispatched state

The first-frost validator and country candidate validator require a valid subtype. `desert_city` is valid only with event ID `13`. Every other route uses `none`.

`air_winter_event_coalesce_matching_seasonal_marker` requires both the event ID and route subtype to match before it consumes a first-frost marker. An exact desert-city marker and a generic ID `13` candidate never coalesce across subtype boundaries.

Every selected temporary route, first-frost marker, country candidate, final dispatcher receipt, reset path, and reconciliation path initializes, copies, validates, or clears the subtype explicitly. No path may inherit a subtype from an older candidate.

The final dispatcher clears an older opening receipt whenever it dispatches event `13`. It writes a new exact receipt only when the frozen country candidate subtype is `desert_city`. The receipt stores the original country and remains valid while that country owns the event state.

## Phase 2 route order

The accepted order is:

1. Mountain capital
2. Engine island state
3. Arid urban state with subtype `desert_city`, routed to event `13`
4. Generic city
5. Maritime, oceanic, or tropical coast
6. Non-city arid or Mediterranean state, routed to event `13` with subtype `none`
7. Highland or polar state
8. Boreal or equatorial food state

The exact urban predicate uses `air_winter_presentation_is_arid` and `air_winter_response_is_city`. The existing city trigger includes town and large-town state categories. That is intentional because the scheduler already treats those strategic state categories as urban response states.

The exact subtype receives the established same-phase bonus of `131`. Generic ID `13` rows do not. The bonus is one point above the complete state-pressure interval and cannot overtake a later phase because the phase weight remains `1000`.

No new country scan, state scan, daily callback, or world iterator is allowed.

## Event 13 opening contract

Event `chaosx.fallout.13` uses conditional descriptions:

- the exact receipt describes frozen municipal mains, ward cisterns, railhead tanks, and a government-aware water authority
- the arid fallback describes district pumps, covered wells, cold dust, and isolated settlements
- the Mediterranean fallback describes cold rain, hill reservoirs, masonry cisterns, and station tanks

The two existing regional choices remain available only when the exact receipt is absent. They keep their immediate, non-delayed effects so every generic ID `13` dispatch retains an executable option.

The following three choices appear only with a valid exact receipt.

### Municipal water board

This is the always-executable exact-route choice.

Opening cost and effect:

- Stability: minus 1 percent
- Local factory availability: minus 10 percent for 31 days
- Water Security: plus 8
- Shelter Capacity: plus 2
- Adaptation: plus 2
- Building Damage Pressure: plus 15

The factory modifier represents workshops, pipe crews, pumps, and protected storage assigned to the water board.

### Railway tanker service

Display and click-time requirements:

- at least one operational railway level in the event state
- 500 Manpower
- 3 Trains
- 1,000 Fuel

Opening effect:

- Water Security: plus 5
- Adaptation: plus 2
- Exposure: plus 1
- Building Damage Pressure: plus 8

### Motor transport columns

Display and click-time requirements:

- at least one operational infrastructure level in the event state
- 200 Manpower
- 20 Motorized Equipment
- 1,000 Fuel
- 7 Command Power

Opening effect:

- Water Security: plus 5
- Adaptation: plus 4
- Exposure: plus 2
- Building Damage Pressure: minus 8

Every exact choice follows the same transaction order:

1. Revalidate the regular country and state targets, exact receipt, branch emptiness, and affordability
2. Clear the older desert-city policy, outcome, receipt, and temporary result modifiers
3. Pay exact country resources through the existing Air Winter payment helpers
4. Apply the opening ledger changes
5. Write one state branch and matching state and country policy memory
6. Refresh the state so the pending owner is bound
7. Refresh the 46-day country cooldown
8. Schedule `chaosx.fallout.49` after exactly 30 days

An invalid click performs no payment and no ledger change. It clears only a stale opening receipt owned by the same event chain, then uses the existing stale-choice recovery event.

## Event 49 deterministic result

Event `chaosx.fallout.49` requires the regular targets, the bound original owner, and exactly one desert-city branch. Each branch has success, partial, and failure predicates. Failure is the exact complement of success and partial.

### Municipal result partition

Success requires all three conditions:

- Water Security at least 30
- Adaptation at least 25
- Building Damage Pressure at most 65

Partial requires success to be false and at least two of those three conditions. Failure is the remaining space.

Results:

| Outcome | Result title and physical consequence | Effects |
| --- | --- | --- |
| Success | **The Cistern Wards Hold.** Pipe crews isolate the split mains before dirty runoff reaches the ward tanks. Bell schedules keep covered cisterns open through the coldest hours. | Water plus 5, Reclamation plus 4, Exposure minus 2, Building Damage Pressure minus 15, and local supplies plus 10 percent for 60 days |
| Partial | **Water by the Bell.** Central cisterns keep their ration hours, but broken feeder pipes leave the outer wards dependent on hand carts and long queues. | Water plus 2, Exposure plus 1, Building Damage Pressure plus 8, and Deaths at 0.00005 of remaining state population |
| Failure | **The Main Gives Way.** A second rupture drains the service reservoirs into frozen streets. Crowds press against contaminated cisterns while repair workshops lose power and access. | Water minus 5, Exposure plus 4, Disease plus 4, Building Damage Pressure plus 15, Stability minus 1 percent, Deaths at 0.00015, repairable infrastructure or supply-node damage, and local supplies minus 10 percent for 60 days |

### Railway result partition

Success requires an operational railway and all three conditions:

- Water Security at least 30
- Adaptation at least 25
- Exposure at most 60

Partial requires success to be false, an operational railway, and at least two of those three conditions. Failure is the remaining space.

Results:

| Outcome | Result title and physical consequence | Effects |
| --- | --- | --- |
| Success | **Tankers at the Railhead.** Heated point crews keep a narrow timetable open from the upland wells. Tank wagons feed station reservoirs before each ward queue forms. | Water plus 8, Reclamation plus 4, Exposure minus 3, Building Damage Pressure minus 8, and local supplies plus 10 percent for 60 days |
| Partial | **A Timetable of Thirst.** Tank wagons reach the central railhead, but frozen points and cracked hoses strand alternate departures. District queues lengthen whenever a train misses its slot. | Water plus 2, Exposure plus 2, Building Damage Pressure plus 8, and Deaths at 0.00005 of remaining state population |
| Failure | **The Sidings Run Dry.** A damaged approach traps the tanker rake beyond the city. Families leave the station queues for uncertain wells as empty reservoirs expose the rail district. | Water minus 5, Exposure plus 4, Refugee Pressure plus 6, Building Damage Pressure plus 15, War Support minus 1 percent, Deaths at 0.00020, repairable railway or infrastructure damage, and local supplies minus 10 percent for 60 days |

### Motor result partition

Success requires operational infrastructure and all three conditions:

- Water Security at least 30
- Reclamation at least 25
- Exposure at most 60

Partial requires success to be false, operational infrastructure, and at least two of those three conditions. Failure is the remaining space.

Results:

| Outcome | Result title and physical consequence | Effects |
| --- | --- | --- |
| Success | **Columns Through the Cold Dust.** Road crews mark sheltered lanes between the well fields and ward tanks. Tanker relays arrive before exposed pipes can freeze between runs. | Water plus 8, Adaptation plus 2, Reclamation plus 4, Exposure minus 3, and local supplies plus 10 percent for 60 days |
| Partial | **Engines at Half Strength.** Stalled tankers divide the convoy into short relays. Inner districts receive irregular deliveries while families from the outer wards move closer to working depots. | Water plus 2, Refugee Pressure plus 4, Exposure plus 2, and Deaths at 0.00010 of remaining state population |
| Failure | **The Road Convoy Breaks.** Cold rain cuts the marked road and disabled tankers block the remaining lane. Uncovered loads foul in roadside runoff while displaced families crowd the last municipal taps. | Water minus 5, Refugee Pressure plus 8, Exposure plus 4, Disease plus 4, Building Damage Pressure plus 15, Stability minus 1 percent, Deaths at 0.00020, repairable infrastructure or supply-node damage, and local supplies minus 10 percent for 60 days |

All civilian losses use `air_winter_event_apply_deaths`. Manpower paid for crews is a country resource cost and never enters the Deaths ledger.

The building damage ladder checks an operational target before `damage_building`. Municipal and motor failures prefer infrastructure and then a supply node. Railway failure prefers railway and then infrastructure. No building is deleted and no level is permanently removed.

## AI contract

Base weights are:

- municipal water board: 60
- railway tanker service: 30
- motor transport columns: 10

Each branch has a pre-choice plausibility trigger translated through its exact opening ledger changes:

| Branch | Pre-choice success projection |
| --- | --- |
| Municipal | Water at least 22, Adaptation at least 23, Building Damage Pressure at most 50 |
| Railway | Operational railway, Water at least 25, Adaptation at least 23, Exposure at most 59 |
| Motor | Operational infrastructure, Water at least 25, Reclamation at least 25, Exposure at most 58 |

The plausible predicate receives factor 2. Its literal inverse receives factor 0.5. Live changes during the 30-day delay may still alter the result.

Government and crisis modifiers remain independent:

- democratic governments favour the municipal board and weaken motor command
- communist governments favour the railway directorate
- fascist governments favour motor command
- high Stability favours the municipal board
- low Stability weakens the municipal board
- peace favours railway commitment
- war weakens railway commitment
- high War Support favours motor command
- low War Support weakens motor command

Unavailable paid choices remain hidden through their option triggers. Every paid choice repeats affordability inside its hidden effect before payment.

## Memory and cleanup

State and country memory records one policy:

- municipal water board
- railway tanker service
- motor transport columns

State and country memory records one result:

- success
- partial
- failure
- casualties where Deaths were requested

The state owns three exclusive pending branch flags. Add them to the shared pending-chain trigger and cancellation effect. Add pairwise invalid-branch checks to the reconciliation effect.

The opening receipt is cleaned independently because it exists before any pending branch. Ownership loss, pending-chain cancellation, full state reset, stale dispatch replacement, exact option consumption, and an invalid click from the original event country all clear both its state flag and owner variable. Reconciliation also clears partial receipts and receipts whose recorded owner no longer owns the state.

The municipal factory modifier is removed by result delivery, ownership invalidation, Fallout cancellation, state reset, and stale-chain cleanup. The positive and negative 60-day supply modifiers replace each other and are removed by full Air Winter state reset. They remain after result delivery for their intended duration.

Fallout keeps the established order. It snapshots the Air Winter state row before pending-chain cleanup. No new Fallout transition hook is required.

## Localisation contract

Player-facing text uses:

- `[air_winter_event_state.GetName]`
- `[air_winter_event_state.GetCapitalVictoryPointName]` where a named settlement is useful
- `[ROOT.GetAirWinterGovernmentOfficial]`
- `[ROOT.GetAirWinterGovernmentAuthority]`

Text must remain concrete and region-aware. It must not mention implementation history, caps, tuning, or scheduler mechanics. New prose may not contain em dashes or semicolons.

## Asset contract

Register one dedicated Fallout-owned sprite:

`GFX_report_event_air_winter_desert_water_convoy`

Event `13` selects its picture through scripted localisation, following the vanilla dynamic event-picture contract. A valid exact receipt uses the dedicated desert-water sprite. Generic arid and Mediterranean fallbacks keep `GFX_report_event_air_winter_phase_2`. Event `49` always uses the dedicated desert-water sprite. Replacing the shared event picture unconditionally is not allowed.

Paths:

- source: `docs/assets/air_cleanliness_fallout/source_png/report_events/report_event_air_winter_desert_water_convoy_source.png`
- processed: `docs/assets/air_cleanliness_fallout/processed_png/report_events/report_event_air_winter_desert_water_convoy.png`
- runtime: `gfx/event_pictures/fallout/report_event_air_winter_desert_water_convoy.dds`
- registration: `interface/air_cleanliness_winter.gfx`

The fictional period-documentary scene shows a frost-split water main, a stone cistern, a railway water tanker, a period tanker truck, engineers with a route sheet, and civilians carrying period containers. Cold dust or sleet and sparse frost replace universal snow. The composition avoids text, flags, logos, modern containers, zombies, and culturally narrow architecture.

The asset must pass the existing 210 by 176 report-card processor, uncompressed 32-bit BGRA DDS contract, decoded contact-sheet review, manifest update, and `.gfx` path check.

## Proof and review requirements

The tranche is not complete until review confirms:

- exact arid urban routing occurs before generic city routing
- the subtype survives ordinary and first-frost candidate paths
- first-frost coalescing requires both the event ID and route subtype to match
- generic ID `13` rows retain executable immediate choices
- event `13` selects the dedicated picture only for its exact receipt and event `49` uses it unconditionally
- only the exact opening receipt can create a delayed branch
- every paid option rechecks and pays the exact displayed cost
- every result partition is exhaustive and mutually exclusive
- every casualty path uses Deaths
- every damage path is repairable and checks a live building target
- all branch, owner, modifier, and opening receipts clean up
- AI plausibility predicates have literal inverse modifiers
- localisation, sprite registration, source asset, processed asset, DDS, manifest, and contact sheet agree
- the event count, option count, delayed schedule count, ID ledger, scheduler proof, pilot review, and implementation status are current

Runtime behavior remains unobserved because the user directed that Hearts of Iron IV not be launched. The engine proof must identify that boundary without presenting it as live validation.

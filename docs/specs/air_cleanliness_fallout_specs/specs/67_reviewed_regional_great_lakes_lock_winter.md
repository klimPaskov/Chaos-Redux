# Spec 67: Great Lakes Lock Winter

Status: accepted source design for a dormant Fallout implementation tranche. Live scheduler delivery is not claimed by this specification.

Great Lakes Lock Winter is a North American regional incident about lake ports and lock stations trying to keep food, fuel, and people moving while ice, ash, and divided control close the ordinary navigation season. The chain targets one native coastal state with a working naval base and current Air Winter records. It records a policy, delayed result, first thaw inspection, durable lake ledgers, Event Log history, and authenticated cleanup.

The chain is Fallout-owned under `add_namespace = chaosx.fallout`. It uses ordinary Fallout receipts and the shared delayed scheduler. It does not create a tag, formable, focus tree, decision category, bilateral partner, recurring on-action, scripted GUI, or government replacement.

## Identity ledger

| Surface | Assigned value |
| --- | --- |
| Candidate and human opening | `663` |
| Hidden-AI opening | `664` |
| Human delayed result | `665` |
| Hidden-AI delayed result | `666` |
| Human callback | `667` |
| Hidden-AI callback | `668` |
| Authenticated cleanup | `669` |
| Transaction key | `710066` |
| Scheduler route | `7166` |
| New route upper bound | `7167` |
| Event Log history | `9172` |
| Catalogue identity | `FALLOUT-663` |
| Report asset identity | `fallout_great_lakes_lock_winter` |

These values are one ownership set. Static implementation recheck is recorded in `docs/plans/air_cleanliness_fallout_plans/FALLOUT_GREAT_LAKES_LOCK_WINTER_PROOF.md`. The row remains dormant while the Fallout scheduler activation flags remain unset.

## Scheduling identity

- Runtime region: `fallout_region.north_america`
- Primary family: `fallout_event_primary_family.regional_and_biome`
- Preferred phase: `fallout_event_phase.first_winter_year`
- Secondary phase: `fallout_event_phase.consolidation`
- Class: `fallout_event_class.routine_incident`
- Cooldown family: `fallout_event_cooldown_family.transport_recovery`
- Required resource: `fallout_survival_resource.fuel`
- Visible budget cost: `3`
- Result delay: `35` days
- Thaw inspection delay: `270` days after result settlement

The candidate pressure is the current gap in native naval-base capacity and shoreline adaptation. The severity is current Air Winter exposure. The state value is current Supply Access. The selector stores one state id and never pretends that a lake-wide multi-state transaction exists.

## Country and state admission

The country must have a current Fallout identity row, current generation, durable country resources, exact North American region, ordinary-event eligibility, campaign days from `365` through `1799`, no committed or closed Great Lakes memory, and at least one affordable branch. Country floors are Food `15`, Clean Water `8`, Fuel `10`, Scrap `8`, Power `6`, Recognition `8`, and Cohesion `20`.

The deterministic selector chooses the lowest native state id owned and controlled by the country that has a current Fallout state row, a produced Air Winter snapshot, coastal geography, a non-damaged naval base above zero, infrastructure above zero, surviving population of at least `5000`, Supply Access from `15` through `100`, Food from `8` through `40`, Adaptation from `10` through `60`, Reclamation below `70`, Exposure from `15` through `70`, and Disease Pressure below `70`. A state with an unresolved exclusive transaction or Great Lakes memory is rejected.

The result and callback reauthenticate the state owner, controller, state id, native naval-base and infrastructure surfaces, state category, current generation, current Air Winter values, selected branch, issued token, and matching delayed ticket before applying effects. Target drift cancels only this row. The chain never writes global Air Contamination and never changes native state category.

## Four authored policies

### Joint ice authority

Spend Food `3`, Fuel `3`, Scrap `2`, and Recognition `2`. Port crews, lock tenders, and local councils publish one shared ice schedule. Success improves convoy throughput, lock trust, and shoreline adaptation. Failure creates queue disorder and a bounded naval-base damage risk.

### Open the locks unilaterally

Spend Food `2`, Fuel `5`, and Command Power `8`. The country pushes a single opening order through the lock chain. Success preserves throughput and War Support. Failure damages the port surface, raises exposure, and leaves a security memory that rival crews can exploit.

### Seasonal closure

Spend Food `2`, Fuel `1`, Shelter Capacity `3`, and Medicine `1`. The country closes the exposed locks, shelters crews, and protects the shoreline until the thaw. Success reduces exposure and disease pressure while sacrificing short-term Supply Access. Failure still loses throughput and worsens Food pressure.

### Sabotage rival locks

Spend Fuel `4`, Scrap `3`, and Support Equipment `2`. The country blocks a rival-controlled lock station without creating a diplomatic partner or a province target. Success raises lake security and local control while increasing customs pressure. Failure damages the authenticated home port and raises cross-border tension.

Every human tooltip discloses the concrete cost, the state name, the 35-day result, the 270-day inspection, and the principal risk. Unaffordable branches are hidden for humans and receive invalid AI priority.

## Frozen grading and durable ledgers

Before payment, freeze Food, Clean Water, Fuel, Scrap, Power, Shelter Capacity, Recognition, Cohesion, Stability, War Support, naval-base level, infrastructure, Supply Access, Food reserve, Adaptation, Reclamation, Exposure, Disease Pressure, state population, and seven country ledgers. The result grade is clamped from `0` through `100` and consumes those frozen values. Branch thresholds are Joint Authority `60` and `40`, Unilateral Opening `62` and `42`, Seasonal Closure `58` and `38`, and Rival Lock Sabotage `64` and `44`.

The seven clamped ledgers are Lock Trust `30`, Convoy Throughput `25`, Ice Protocol `15`, Lake Security `20`, Customs Pressure `15`, Shoreline Adaptation `25`, and Cross-Border Trust `30`. Branch preparation affects the selected primary ledger before grading. Settled result deltas are applied after the grade is locked and remain durable after cleanup.

Result success improves the native state supply surface, shoreline adaptation, the selected ledger, and a timed country modifier. Partial success preserves the port while leaving a contested schedule memory. Failure damages the observed naval base or infrastructure, reduces Supply Access, raises Exposure or Disease Pressure, and may request bounded Deaths through `apply_exact_state_civilian_population_loss` with the Fallout aftermath cause. No branch transfers population, writes the natural-disaster reservoir, or uses variable-only population loss.

The thaw inspection uses current Supply Access, naval-base level, infrastructure, shoreline adaptation, lock trust, the selected primary ledger, convoy throughput, inverse customs pressure, Cohesion, Recognition, and inverse Exposure and Disease Pressure. Success is `64` or higher, partial is `42` through `63`, and failure is below `42`. Callback success preserves a lake service memory. Callback failure damages the observed naval base or infrastructure and records a named closure memory.

## Hidden AI behavior

Continuity Government, Food Compact, and Technate prefer Joint Ice Authority when Recognition and Cohesion are sound. Warlord Command prefers Unilateral Opening at war or when Lake Security is strong. Nomad Convoy and Maritime Remnant prefer Seasonal Closure when exposure is high and Joint Authority when Fuel is scarce. Scavenger Syndicate prefers Rival Lock Sabotage when Scrap and Support Equipment are available. Quarantine State and Religious Refuge prefer Seasonal Closure under disease pressure. Mutant Polity prefers Rival Lock Sabotage only when the state has strong Supply Access.

The deterministic tie order is Joint Ice Authority, Seasonal Closure, Rival Lock Sabotage, then Unilateral Opening. Hidden AI uses the same affordability, payment, result, callback, Event Log, and cleanup effects as human play. Invalid or unaffordable options receive the reviewed invalid priority and are never selected.

## Event Log and presentation

History `9172` records all four opening choices, twelve branch result outcomes, three callback outcomes, and the authenticated cancellation path. The country is the primary actor and the authenticated host state is the secondary actor. Dedicated scripted localisation provides the event name, opening detail, branch result detail, callback detail, cancellation detail, and unknown-payload text.

The report card shows a fictional winter lake lock with ice-sheathed gates, a covered fuel convoy, port crews, ash-darkened snow, and a distant lighthouse. It contains no real people, flags, readable brands, historical institution claims, zombie imagery, animation, or audio. Runtime dimensions follow the 210 by 176 Fallout report-card convention. Asset source, processing notes, DDS hash, and sprite registration belong under `docs/assets/663_great_lakes_lock_winter/`.

## Cleanup and proof boundaries

The opening, result, callback, and cleanup receipts reauthenticate candidate `663`, route `7166`, transaction `710066`, state target, owner, controller, generation, branch, mode, event token, payment flag, result commitment, callback schedule, and matching cleanup ticket. Cleanup preserves the seven durable ledgers and releases only this chain's delayed rows, state reservation, payment receipt, and transient variables.

Static proof must cover native naval-base reads, native damage effects, live Air Winter rechecks, branch affordability parity, deterministic target selection, Deaths wiring, Event Log actor mapping, localisation coverage, DDS geometry, and exact id uniqueness. Runtime scheduler dispatch, save recovery, host authority, multiplayer input blocking, delayed delivery, Event Log rendering, normal-map presentation, and full-screen Fallout blackout remain user validation boundaries. The exact all-valid-province thermonuclear sweep and the 90 to 95 percent manual survival contract remain separate transition obligations.

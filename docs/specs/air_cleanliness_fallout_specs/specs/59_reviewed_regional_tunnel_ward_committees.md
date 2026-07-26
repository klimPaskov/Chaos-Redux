# Reviewed regional chain: Tunnel Ward Committees

The Tunnel Ward Committees chain is a dormant Fallout routine incident for East Asia. It treats a surviving industrial shelter as a contested civic institution. The chain records a branch, a deterministic institutional result, a delayed review, and durable memory. It does not create a country, a formable, a focus route, a decision category, or a recurring council system.

## Identity and ownership

- Namespace: `chaosx.fallout`
- Human opening: `607`
- Hidden AI opening: `608`
- Human result: `609`
- Hidden AI result: `610`
- Human callback: `611`
- Hidden AI callback: `612`
- Cleanup: `613`
- Candidate id: `607`
- Transaction key: `710058`
- Scheduler route: `7158`
- Route upper bound: `7159`
- Event Log history: `9164`
- Region: `fallout_region.east_asia`
- Preferred phase: `fallout_event_phase.ash_week`
- Secondary phase: `fallout_event_phase.consolidation`
- Primary family: `fallout_event_primary_family.regional_and_biome`
- Cooldown family: `fallout_event_cooldown_family.shelter`
- Class: `fallout_event_class.routine_incident`
- Visible budget cost: `2`

The scheduler remains the sole caller. No activation flag is written by this chain. The chain owns its candidate row, state reservation, ledgers, branch costs, delayed receipts, Event Log payloads, dynamic modifiers, and durable memories.

## Admission and target authority

Country admission requires a current Fallout identity and generation, current Survival resources, East Asia membership, an affordable branch, no active or completed Tunnel Ward transaction, and the ordinary-event eligibility gate. The chain does not use a capital fallback or historical city enumeration.

The state selector chooses the lowest native state id among owned and controlled states with a current Fallout state row, a produced Air Winter snapshot, a large town, city, or large city category, surviving population above `6,000`, shelter capacity at least `24`, Supply Access at least `12`, Reclamation at least `6`, Exposure below `78`, Disease Pressure below `72`, and one non-damaged infrastructure level. The selected state is reserved before payment. Every delayed event reauthenticates owner, controller, state id, branch, ticket, and Fallout generation.

The chain requires the Air Winter `air_winter_shelter_capacity` ledger. If the current state snapshot does not provide it, admission fails closed. The chain does not substitute a land-fort or bunker building for shelter evidence.

## Branches and costs

1. Recognize the ward councils. Spend Food `5`, Medicine `3`, and Recognition `3`. This raises committee trust, representation, ward autonomy, and refugee integration. Success records a recognized ward federation. Failure records committee fragmentation.
2. Centralize appointments. Spend Food `4`, Power `5`, Scrap `3`, and Recognition `2`. This raises central capacity and register integrity while reducing ward autonomy. Failure records an appointment crisis.
3. Establish a military ward system. Spend Food `4`, Equipment `3`, and Command Power `12`. This raises security control. Success adds War Support `0.02` and slightly reduces Cohesion. Failure records coercive tunnel control and routes civilian loss through Deaths.
4. Rotate ward leadership. Spend Food `5`, Medicine `2`, Power `3`, and Recognition `3`. This raises representation, committee trust, and refugee integration while accepting slower administration. Failure records committee deadlock.

Country ledgers initialize once and clamp from `0` through `100`: committee trust `35`, central capacity `35`, ward autonomy `30`, security control `20`, representation `25`, refugee integration `25`, and faction pressure `20`.

## Deterministic result and callback

The result is issued after `28` days. Opening values are frozen before payment and are not regraded later. The score has ten equal-weight components: shelter capacity, Supply Access, Reclamation, infrastructure score, Food, Medicine, Power, Recognition, Cohesion, and combined inverse Exposure and Disease Pressure. It clamps from `0` through `100`.

Branch success and partial thresholds are respectively Recognize `58` and `38`, Centralize `61` and `41`, Military `62` and `42`, and Rotate `56` and `36`.

Recognize gains `5` when Cohesion is at least `50`. Centralize gains `5` when Power is at least `40` and Recognition at least `35`, and loses `4` when Cohesion is below `35`. Military gains `6` while at war and `4` when War Support is at least `0.55`, and loses `6` when Cohesion is below `35`. Rotation gains `5` when Cohesion and Shelter Capacity are both at least `45`, and loses `4` while at war.

Common success adds Supply Access `4`, shelter capacity `4`, Reclamation `3`, Recognition `2`, and Cohesion `3`, while reducing Exposure by `2`. Common partial adds Supply Access, shelter capacity, and Reclamation by `1`. Common failure subtracts Supply Access `4` and shelter capacity `3`, adds Exposure `5` and Disease Pressure `3`, subtracts Cohesion `5`, and requests Deaths equal to `0.04%` of frozen population with a minimum-population guard.

The institutional review is issued `210` days after settlement. Its ten-component score uses committee trust, the branch primary ledger, representation, refugee integration, inverse faction pressure, Supply Access, shelter capacity, Recognition, Cohesion, and combined inverse Exposure and Disease Pressure. Success is `65` or higher, partial is `42` through `64`, and failure is below `42`.

Callback failure subtracts Supply Access and shelter capacity by `2`, adds Exposure `3`, subtracts Cohesion `4`, and requests Deaths equal to `0.015%` of frozen population. Target loss records cancellation payload `99` and applies no frozen state effects.

## AI, Event Log, and presentation

AI base scores are Recognize `46`, Rotate `42`, Centralize `38`, and Military `34`. Bunker authority and mutant polity governments prefer recognition. Continuity governments prefer recognition or centralization according to Cohesion and Recognition. Technates and Machine Protocol prefer centralization when Power is secure. Warlord governments prefer military wards, especially during war. Food Compacts, Quarantine States, Religious Refuges, Scavenger Syndicates, and Nomad Convoys prefer rotation or recognition. Military loses priority when Cohesion is below `30`. Unaffordable and unauthenticated branches receive `-1000`. Tie order is Recognize, Rotate, Centralize, Military.

History `9164` uses choice payloads `1` through `4`, result payloads `11` through `13`, `21` through `23`, `31` through `33`, and `41` through `43`, callback payloads `51` through `53`, and cancellation payload `99`. The country is the primary actor and the authenticated host state is the secondary actor.

The report card shows a crowded East Asian industrial shelter with ward delegates around a ration and ventilation board, utility workers, families, and guards. It contains no readable generated text, country-specific claims, stereotypes, modern equipment, or identifiable real people. Target dimensions are `210x176`.

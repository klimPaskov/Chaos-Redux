# Reviewed regional chain: The Metro Republic Below

The Metro Republic Below is a dormant Fallout routine incident for Europe. It treats a surviving capital shelter as a contested civic settlement rather than as an automatic successor country. The chain records a deterministic policy, a delayed result, a later district review, and durable memory. It does not create a tag, a formable, a focus tree, or a permanent decision category.

## Ownership

The reserved ownership set is candidate `614`, transaction `710059`, scheduler route `7159`, route upper bound `7160`, events `chaosx.fallout.614` through `chaosx.fallout.620`, and Event Log history `9165`. These values are reserved together. A collision requires remapping the whole set before any source is edited.

The row remains dormant. It must not set `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`.

## Admission

Country admission requires a current Fallout country identity, a current generation, a current Survival row, Europe region membership, ordinary-event eligibility, campaign day between `730` and `6000`, and at least one affordable branch. A pending or completed Metro Republic memory, an unresolved capital-condition transaction, or a stale orientation receipt blocks the candidate.

The deterministic state selector chooses the lowest native state id owned and controlled by the country that has a current Fallout state row, a produced Air Winter snapshot for the current generation, a city or large-city category, population above `8000`, shelter capacity from `30` through `100`, Supply Access at least `15`, Reclamation at least `5`, infrastructure at least `1`, Exposure below `80`, Disease Pressure below `70`, and no evacuation, dead-city, thaw, bridge, or other exclusive state transaction.

The selector does not use a historical capital list or a capital fallback. The host state id is frozen before branch payment. The phrase underground districts describes the surviving shelter institutions inside the authenticated host state. It does not claim that the engine can select individual metro provinces.

## Branches

The opening offers four authored directions.

1. Surface council

   Spend Food `5`, Scrap `3`, and Recognition `3`. The council opens controlled surface access, publishes a district register, and gives the host a civic legitimacy memory. Success favors Cohesion and Recognition. Failure produces a trust and exposure setback.

2. Tunnel autonomy

   Spend Food `4`, Power `4`, Scrap `2`, and Recognition `2`. Ward delegates keep local ration and ventilation authority while the republic remains loosely federated. Success favors Shelter Capacity, ward autonomy, and refugee integration. Failure increases faction pressure and reduces Supply Access.

3. Military integration

   Spend Food `4`, Fuel `2`, Support Equipment `3`, and Command Power `12`. The surviving army assumes corridor security and accepts a civilian inspection board. Success adds a small War Support benefit while reducing Cohesion by one. Failure uses the Deaths system and records a tunnel crackdown memory.

4. Evacuate the lower districts

   Spend Food `6`, Medicine `3`, Fuel `3`, and Recognition `1`. The republic protects the most exposed lower wards and moves people toward the surface host. Success improves Shelter Capacity and bounded population protection. Failure records an interrupted evacuation and applies bounded civilian loss through Deaths.

All four routes have distinct costs and risks. An unavailable route has a truthful tooltip and receives no AI weight. The candidate is not produced when every branch is unaffordable.

## Durable ledgers

The country owns seven clamped ledgers initialized only once.

| Ledger | Initial value | Meaning |
| --- | ---: | --- |
| surface legitimacy | 30 | confidence in public representation |
| tunnel autonomy | 40 | local authority retained by wards |
| military integration | 25 | civilian acceptance of security command |
| evacuation readiness | 20 | ability to move people safely |
| district trust | 35 | trust between shelter districts |
| salvage access | 25 | safe access to surface repair and salvage |
| faction pressure | 20 | pressure from competing corridor authorities |

Values remain between `0` and `100`. Boolean memories use flags. Numeric ledgers do not replace country or state identity receipts.

## Deterministic result

The result is issued after `35` days. The result reauthenticates generation, country, owner, controller, host state, branch, and transaction ticket before reading the frozen values.

The grade is the equal-weight mean of ten components.

- Shelter Capacity
- Supply Access
- Reclamation
- non-damaged infrastructure score
- Food
- Medicine
- Power
- Recognition
- Cohesion
- inverse Exposure and Disease Pressure

The score is clamped from `0` through `100` before branch thresholds apply.

| Branch | Success | Partial |
| --- | ---: | ---: |
| Surface council | 60 | 40 |
| Tunnel autonomy | 57 | 37 |
| Military integration | 63 | 43 |
| Evacuate lower districts | 59 | 39 |

Surface council gains `5` when Cohesion is at least `50`. Tunnel autonomy gains `5` when Shelter Capacity is at least `45` and Power is at least `35`. Military integration gains `5` while at war and loses `5` when Cohesion is below `35`. Evacuation gains `5` when Shelter Capacity is at least `50` and Exposure is below `55`, and loses `4` when Disease Pressure is at least `50`.

Success improves the host state's Supply Access, Shelter Capacity, and Reclamation and adds a branch memory. Partial success makes smaller repairs and records a contested district memory. Failure reduces Supply Access and Shelter Capacity, raises Exposure and Disease Pressure, and requests a bounded Deaths loss using the accepted minimum-population guard. No branch writes global Air Contamination.

The military success route uses native War Support on the `0` through `1` scale. It does not create a new army or replace a character. The evacuation route uses bounded population protection and a state memory. Native province-level metro movement remains an engine boundary.

## District review callback

The callback is issued `270` days after the result. It reauthenticates the same country, state, owner, controller, generation, branch, result, and callback ticket.

The callback grade uses district trust, the branch's primary ledger, surface legitimacy, tunnel autonomy, evacuation readiness, inverse faction pressure, current Supply Access, Shelter Capacity, Recognition, and inverse Exposure and Disease Pressure.

- Success is `65` or higher.
- Partial is `42` through `64`.
- Failure is below `42`.

Success establishes a durable metro republic memory with a branch-specific identity. Partial success keeps the shelter open with a contested council or inspection board. Failure records a corridor breakdown and applies a small bounded state loss. Callback failure never clears a newer transaction.

## AI and determinism

The hidden AI chooses from the same affordability and snapshot helpers as the human lane. The tie order is surface council, tunnel autonomy, military integration, then evacuation.

- Continuity governments prefer a surface council when Cohesion and Recognition are secure.
- Bunker authorities prefer tunnel autonomy when Shelter Capacity and Power are strong.
- Warlord commands prefer military integration during war, but low Cohesion sharply reduces that weight.
- Quarantine states and religious refuges prefer evacuation when Medicine and Disease control are strong.
- Scavenger syndicates prefer surface council when Salvage Access is high.

The selector uses deterministic scores and a fixed tie order. It does not use `random_list`, MTTH, or proportional `ai_chance`.

## Event Log and presentation

History `9165` contains opening choices `1` through `4`, result payloads `11` through `43`, callback payloads `51` through `53`, and cancellation `99`. The country is the primary actor and the authenticated host state is the secondary actor.

The chain uses one dedicated fictional report image showing a cold European metro shelter with a ration office, ventilation crews, district delegates, a guarded surface hatch, and families moving between levels. The image contains no readable generated text, real-person likeness, national flag, zombie imagery, or super-event composition. It uses the standard `210x176` report-card size and a dedicated sprite name.

## Explicit exclusions and proof gates

The chain does not create a new tag, change the country's government archetype through an unproven native effect, create province-level metro districts, run a world iterator, add an on-action, create a focus or decision surface, or activate the scheduler.

Static proof must cover collision ownership, candidate row construction, exact host selection, branch affordability, frozen inputs, delayed result and callback reauthentication, human and hidden-AI parity, Deaths wiring, Event Log routes, localisation coverage, report DDS integrity, and cleanup on generation or ownership change.

The installed event inspector may close its transport or hit the existing issue limit on the large Fallout source. That is recorded as an engine-sensitive blocker rather than treated as proof. User-owned runtime validation remains required for popup order, host authority, save recovery, multiplayer input blocking, Event Log rendering, and the dormant status.

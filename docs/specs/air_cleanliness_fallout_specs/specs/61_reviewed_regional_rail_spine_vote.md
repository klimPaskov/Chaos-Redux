# Reviewed regional chain: The Rail Spine Vote

The Rail Spine Vote is a dormant Fallout routine incident for the Eurasian interior. It treats one surviving railway state as a political corridor whose stations, depots, and local councils must agree on a service order. The chain records a branch, a deterministic result, a delayed inspection, durable memories, and authenticated cleanup. It does not create a tag, a formable, a focus tree, a recurring decision, or a new government effect.

## Identity and ownership

- Namespace: `chaosx.fallout`
- Human opening: `621`
- Hidden AI opening: `622`
- Human result: `623`
- Hidden AI result: `624`
- Human callback: `625`
- Hidden AI callback: `626`
- Cleanup: `627`
- Candidate id: `621`
- Transaction key: `710060`
- Scheduler route: `7160`
- Route upper bound: `7161`
- Event Log history: `9166`
- Region: `fallout_region.eurasian_interior`
- Preferred phase: `fallout_event_phase.first_season`
- Secondary phase: `fallout_event_phase.consolidation`
- Primary family: `fallout_event_primary_family.regional_and_biome`
- Cooldown family: `fallout_event_cooldown_family.transport_recovery`
- Class: `fallout_event_class.routine_incident`
- Visible budget cost: `2`

The Fallout scheduler remains the sole caller. No activation flag is written by this chain. The chain owns its candidate row, state reservation, country ledgers, branch costs, delayed receipts, Event Log payloads, dynamic modifiers, memories, and generation-safe cleanup.

## Admission and target authority

Country admission requires a current Fallout country and generation, current Survival resources, Eurasian interior membership, ordinary-event eligibility, an affordable branch, and no pending or completed Rail Spine Vote memory. The target state must be owned and controlled by the country and must carry a current Fallout state row and a produced Air Winter snapshot.

The selector chooses the lowest native state id with a non-damaged railway surface above zero, at least one non-damaged infrastructure level, surviving population above `5000`, Supply Access at least `15`, Reclamation at least `7`, shelter capacity at least `20`, Exposure below `78`, and Disease Pressure below `72`. It stores the native railway level and the Air Winter shelter and exposure snapshots before payment. No capital fallback or province enumeration is used.

Every delayed event reauthenticates the owner, controller, state id, branch, transaction ticket, generation, target row, and current Air Winter identity. A lost state, stale generation, changed owner, stale target, or unaffordable retry cancels the exact receipt and records cancellation provenance without applying frozen effects.

## Branches and ledgers

1. Open the central rail board. Spend Food `5`, Scrap `3`, and Recognition `3`. This raises route trust, representation, and Supply Access while making depot delegates answer to one public timetable.
2. Grant the depots regional shares. Spend Food `4`, Fuel `3`, Scrap `2`, and Recognition `2`. This raises depot autonomy and fuel coordination while accepting a slower common schedule.
3. Put the line under military guard. Spend Food `4`, Fuel `2`, Support Equipment `3`, and Command Power `12`. This raises route security and War Support while increasing command pressure.
4. Lease the line to merchant convoys. Spend Food `5`, Fuel `3`, Scrap `3`, and Recognition `1`. This raises trade access and salvage returns while increasing faction pressure and exposure to theft.

Country ledgers initialize once and clamp from `0` through `100`: route trust `35`, depot autonomy `30`, timetable compliance `35`, security control `20`, merchant access `25`, representation `30`, and faction pressure `20`. State memories record the selected policy, result, callback, and cancellation separately.

## Deterministic result and callback

The result is issued after `35` days. Opening values are frozen before payment and are not regraded later. The score uses equal-weight components for railway level, infrastructure, Supply Access, Reclamation, shelter capacity, Food, Fuel, Scrap, Recognition, Cohesion, and inverse Exposure and Disease Pressure. The score clamps from `0` through `100`.

Branch success and partial thresholds are Central Board `60` and `40`, Depot Shares `62` and `42`, Military Guard `64` and `44`, and Merchant Lease `58` and `38`. Government, War Support, low Cohesion, and an intact native railway provide branch-specific additions or penalties. A tie never changes the stored branch or target.

Common success adds Supply Access `4`, Reclamation `3`, railway repair `1`, Recognition `2`, and Cohesion `2`. Common partial adds Supply Access `2` and Reclamation `1`. Common failure subtracts Supply Access `4`, damages the railway or infrastructure according to the observed native surface, adds Exposure `4`, adds Disease Pressure `2`, and requests Deaths equal to `0.03%` of the frozen state population through the shared Deaths contract.

The depot inspection callback is issued `300` days after the result. Its score uses route trust, the selected primary ledger, timetable compliance, representation, merchant access, inverse faction pressure, current Supply Access, current railway level, shelter capacity, Recognition, Cohesion, and inverse Exposure and Disease Pressure. Success is `66` or higher, partial is `44` through `65`, and failure is below `44`.

Callback success improves route trust, Supply Access, railway condition, Reclamation, and Recognition. Partial review preserves the route while leaving a contested timetable memory. Callback failure damages the observed railway surface or infrastructure, adds Exposure, subtracts Cohesion and Supply Access, and requests Deaths equal to `0.012%` of the frozen population. Failure never clears a newer transaction.

## AI and presentation

Hidden AI uses the same branch affordability, frozen ledgers, result score, callback score, and cleanup path as a human country. Continuity governments prefer the Central Board when Recognition and Cohesion are sound. Warlord commands prefer Military Guard while at war or when faction pressure is high. Scavenger Syndicates prefer Merchant Lease when Scrap and railway access are strong. Food Compacts and Nomad Convoys prefer Depot Shares when Fuel is scarce. Quarantine States and Religious Refuges prefer the Central Board or Depot Shares. Unaffordable and unauthenticated branches receive the invalid score and cannot be selected.

The dedicated report card shows a winter railway junction in the Eurasian interior with depot delegates, a timetable board, fuel drums, a guarded locomotive, and merchant wagons waiting under ash snow. It contains no readable generated text, real people, real flags, or modern logos. The runtime report sprite is `210x176` and belongs only to this chain.

## Boundaries and proof

The chain does not invoke thermonuclear strikes, rewrite the normal map, convert a state to wasteland, assign successor tags, change government through an unproven native effect, create a second world iterator, or enable the Fallout scheduler. The exact all-valid-province thermonuclear sweep, blackout host authority, save recovery, multiplayer input blocking, runtime Event Log rendering, and live delayed delivery remain separate engine-sensitive obligations.

The implementation proof must record the constants, target trigger, branch costs, native railway reads and damage effects, Deaths request, delayed result and callback receipts, Event Log history `9166`, dedicated asset hashes, workbook row `FALLOUT-621`, and the final dormant release-floor count. No release-floor credit is granted while scheduler activation remains unset.

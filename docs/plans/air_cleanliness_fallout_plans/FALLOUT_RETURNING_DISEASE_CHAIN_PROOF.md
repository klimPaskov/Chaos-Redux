# Fallout 712 chain proof: The Returning Disease

## Scope

This proof covers the dormant Quarantine State chain added for candidate 712. It does not register Fallout as a normal event and it does not claim a Hearts of Iron IV runtime launch. Live campaign validation remains user-owned.

## Identity and transaction ownership

| Surface | Evidence |
| --- | --- |
| Candidate | `fallout_event_candidate_pilot.returning_disease_candidate_id = 712` |
| Transaction | `fallout_event_candidate_pilot.returning_disease_transaction_key = 710073` |
| Route | `fallout_event_candidate_pilot.returning_disease_route = 7178` with upper bound 7179 |
| Event ids | `chaosx.fallout.712` through `chaosx.fallout.718` |
| Event Log | `fallout_event_712_log.history_id = 9179` |
| Namespace | The chain uses `fallout_event_712_*` and `fallout_returning_disease_*` only |
| Asset | `GFX_report_event_fallout_returning_disease` and its dedicated DDS path |

The candidate registry clears `fallout_event_712_candidate_state_id` during each rebuild. The producer selects the lowest eligible native state, initializes one candidate row, records the human and hidden-AI tokens, and appends the row before setting the generation reviewed flag. A candidate cannot be admitted when the state is reserved, committed, pending, or closed.

## Admission evidence

The trigger file requires a current native state, durable identity, resource, and Supply Access rows, a closed Doctor's Coup state memory, Air Winter phase, Shelter Capacity at least 18, Supply Access at least 12, Adaptation at least 10, Disease Pressure from 22 through 89, Exposure from 8 through 89, and population above the minimum contract. The owner must be a current Quarantine State with public health at least 35, grievance at least 1, Medicine at least 8, Cohesion at least 25, and Recognition at least 10. Campaign days are bounded to 900 through 5199. The candidate requires at least one affordable branch.

The trigger reopens the target by id and checks that the owner tag still equals the receipt owner. Every result and callback trigger revalidates the generation, candidate id, target state, frozen owner, frozen controller, and durable registry rows.

## Branch and timing evidence

| Branch | Constant cost | Result delay | Callback delay |
| --- | --- | --- | --- |
| Seal the infected district | Food 2, Medicine 3, Recognition 2 | 24 days | 210 days |
| Send targeted care teams | Medicine 4, Fuel 2, Recognition 2 | 24 days | 210 days |
| Request the aid convoy | Food 2, Scrap 1, Recognition 3 | 24 days | 210 days |
| Keep the outbreak off the books | Medicine 2, Fuel 1, Power 2 | 24 days | 210 days |

The visible opening charges one branch once. A failed delayed transaction refunds that branch and releases the reserved state. The hidden AI lane uses the same branch affordability and receipt checks and sets its visible budget cost to zero.

The ordinary row carries visible budget cost 3. The result, callback, and cleanup receipts do not create a second public cost.

## Mechanics and Deaths evidence

`fallout_event_712_apply_result_effects` and `fallout_event_712_apply_callback_effects` change Air Winter Disease Pressure, Shelter Capacity, Exposure, Adaptation, Reclamation, and Supply Access through the existing Air Winter helper. They also change Medicine, Recognition, Cohesion, public health, grievance, Treatment Capacity, Border Trust, Aid Dependence, Concealment Pressure, and Cause Memory. Result failure damages infrastructure and calls `apply_exact_state_civilian_population_loss` with `chaos_meter_deaths_reason.fallout_aftermath`. Callback failure uses the same Deaths contract with a lower percentage. Both routes set a minimum remaining population and clear their request variables after resolution.

The chain never changes a country tag, deletes a country, changes the government archetype, or writes a Fallout scenario flag. The durable outcome is carried by country memory flags and state result flags.

## Event Log and cleanup evidence

Opening, result, callback, and cancelled payloads use `fallout_event_712_log`. Shared scripted localisation routes history 9179 to `fallout.event_log.returning_disease.detail` and its name key. The chain records choice history once, result history once, and callback history once. Event 718 releases the delayed cleanup receipt, handles a callback ticket that completes after the result ticket, clears temporary variables and flags, and preserves only the durable branch memory and cause memory.

## Asset evidence

The generated source, processed 210x176 PNG, runtime DDS, prompt record, and handoff are under `docs/assets/712_returning_disease/`. The runtime DDS is copied to `gfx/event_pictures/fallout_returning_disease/report_event_fallout_returning_disease.dds`, and the sprite registration is in `interface/fallout_world_end.gfx`. The asset is dedicated to candidate 712 and is not shared with zombie, world-end, or other Fallout paths.

## Review boundary

The chain is a reviewed content tranche, not the release floor. It contributes seven ordinary event blocks and one candidate row to the ordinary survivor-event library. It remains dormant until a later scheduler activation review. Runtime errors, save behavior, and live presentation still require the user's in-game validation pass.

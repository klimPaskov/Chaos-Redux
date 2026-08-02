# Fallout Work for Rations Chain Proof

## Scope and consequence boundary

Work for Rations is candidate `670` in the dormant Fallout-owned survivor scheduler. It is an ordinary post-consequence country event that can describe how a surviving Food Compact government allocates labor. It is not the Fallout consequence, it does not request the transition, and it does not create a Fallout Event Log or evolution entry for the transition itself. Its result and callback may write ordinary survivor memory history after the consequence has already completed.

The chain uses the dedicated `chaosx.fallout` namespace and the reviewed event block range `670` through `676`. The human opening is `670`, hidden AI opening is `671`, visible result is `672`, hidden AI result is `673`, visible callback is `674`, hidden AI callback is `675`, and cleanup is `676`. The ordinary survivor history row is `9173`. The transaction key is `710067`, the route id is `7167`, and the reserved route upper bound is `7168`.

The chain remains dormant. The scheduler activation flags are not set, so no ordinary popup or hidden AI delivery is claimed from this source tranche. The static tranche audit is clear, but release-floor credit still waits on the shared scheduler and runtime presentation gates.

## Native target and admission proof

The source selector is `fallout_event_pilot_work_for_rations_harvest_state_is_current`. It requires the current Fallout state identity row, durable state resource row, current Supply Access row, a produced Air Winter food snapshot, adaptation and exposure values, a bounded disease value, surviving population, positive supply access, and control by the requesting country. It also requires a current transition generation, a Food Compact eligible owner, and the native state source kind. The selector refuses a missing target, a stale generation, owner or controller drift, a committed labor registry, or a missing Food resource rather than selecting a generic state.

The opening gate rehydrates the issued state from the ordinary dispatch envelope. It checks the typed state target, target existence, owner and controller identity, current-generation rows, event token, dispatch mode, first post-consequence-year window, and country eligibility. The producer and both opening lanes require at least one complete affordable branch. The hidden AI lane uses the same target gate and the same four branch costs as the visible lane.

Every resolved branch now writes `fallout_event_670_policy_memory_generation` and `fallout_event_670_policy_memory_owner` on the selected state. These durable values allow later Food Compact chains to prove that the branch flag belongs to the current Fallout generation and current owner after the Work for Rations transaction registry has been cleaned up.

## Branches and deterministic grading

The four authored branches are Universal Duty, Paid Labor, Refugee Work Program, and Mechanized Harvest. Universal Duty spends Food 3, Fuel 1, Scrap 1, and Recognition 1. Paid Labor spends Food 4, Fuel 1, and Command Power 4. Refugee Work Program spends Food 5, Shelter Capacity 3, Medicine 2, and Recognition 1. Mechanized Harvest spends Fuel 6, Scrap 2, Power 4, and Support Equipment 2.

The selected branch is paid exactly once after the opening receipt and target are reauthenticated. The result is scheduled for 35 days. The grade is deterministic and uses the frozen pretransition Food reserve, live Supply Access, pretransition Adaptation, pretransition Reclamation, inverse pretransition Exposure, and inverse Disease Pressure. The weighted components use the authored 30, 20, 15, 10, 15, and 10 weights with a 100-point divisor. Branch thresholds produce success, partial, or failure without randomness. Mechanized maintenance is only recorded when its frozen Adaptation is below the low-adaptation threshold. Every resolved Refugee result, including failure, records a durable owner-state host memory with the current controller, generation, and outcome.

The hidden AI lane scores every affordable branch from the frozen food, live supply, adaptation, exposure, disease, refugee pressure, and country power ledgers. Food Compact, continuity, refugee, technate, machine, and warlord government archetypes add authored weights, while low supply adds a shelter-pressure weight and surplus power favors mechanized harvest. Branch order is the deterministic tie break. It does not use a separate generic fallback. Result and callback events recheck the dispatch ticket, branch range, state owner, transition generation, frozen population, frozen supply, frozen disease, frozen exposure, frozen adaptation, and frozen reclamation before applying effects. A Refugee callback additionally requires the durable owner-state host memory.

## Result and callback effects

Result effects update the Food Compact ledger and branch memory, state Food and harvest reserve, Supply Access, Air Winter Exposure, Adaptation, Reclamation, Disease Pressure, labor, production, manpower, integration, maintenance, Recognition, Cohesion, and Stability. The four branches have distinct success and partial values. Failure reduces harvest, supply, labor, and production and raises exposure and disease. Failure population loss is sent through `apply_exact_state_civilian_population_loss` and the Deaths system with cause `fallout_aftermath` rather than being added directly to the state population outside the Deaths receipt.

The callback is scheduled for 270 days after the result. It evaluates current Food, supply, harvest reserve, disease ceiling, exposure, labor, production, and the same-generation state registry. Success, partial, and failure write branch-aware ledgers and Air Winter values. Callback failure records a bounded Deaths-system loss with the same Fallout cause and clears the state reservation only through authenticated cleanup. Refugee callback entry fails closed if the owner-state memory is missing or stale, while the result event itself does not require memory that is created by applying that result.

The cleanup effect is idempotent. It requires the issued cleanup ticket, current generation, current owner and controller, and committed labor registry. It clears the state and country flags, temporary variables, dispatch envelope, delayed receipt, cleanup tombstone, branch payment receipt, and target reservation. Durable branch, cause, and Refugee owner-state memories remain after cleanup. The opening cancellation path terminalizes a stale or missing opening receipt without touching a newly rebuilt generation. Generation-reset cancellation and automatic refunds remain outside this dormant tranche.

## Public history and presentation

The dedicated sprite is `GFX_report_event_fallout_work_for_rations`, registered in `interface/fallout_consolidated.gfx` and backed by `gfx/event_pictures/fallout/report_event_fallout_work_for_rations.dds`. The source and processed images, hashes, prompt, and handoff are under `docs/assets/670_work_for_rations/`. The visible opening, result, and callback use concrete Food Compact and Air Winter text. Hidden AI events have no player popup.

The authoritative workbook row is `Events!A258:M258` with identity `FALLOUT-670`. Its player-facing Details cell matches the current opening, branch, result, callback, and survivor-history wording. Evo I through Evo V, World-End Scenario columns, and internal mechanical columns are blank. The exported Events CSV was regenerated with SHA-256 `3ad6d6d633b738b51da1a0e987923d4c8666bc381de25d5b99d5db1ba52a81c4`.

Choice, result, callback, and failed-opening survivor memories write history id `9173` with event type `fallout_country_memory`. The shared Event Log name and detail routes, dedicated scripted detail resolver, and localisation payloads cover all four choices, three result outcomes per branch, three callback outcomes, and cancellation. No transition request, blackout, population sweep, or Air Cleanliness shutdown is registered as a normal event log entry or evolution by this chain.

## Static evidence and runtime boundary

Static source review and the tranche audit confirm separate Fallout ownership, dedicated ids, four branch costs, a native state selector, generation, owner, and controller authentication, first-year timing, all-branch affordability, hidden AI parity, delayed result and callback receipts, Air Winter and Deaths integration, dedicated art, localisation, Event Log survivor memory, and cleanup. No zombie id, file, asset, audio, sprite, or path is reused.

Static review does not prove Clausewitz event delivery, target persistence across 35 and 270 days, save recovery, multiplayer host authority, input blocking, Deaths readback, manpower readback, Event Log rendering, or scheduler cadence. Hearts of Iron IV was not launched for this task. The chain therefore remains dormant and outside the 660-block release floor until the shared scheduler, runtime delivery, and release receipt gates are proven.

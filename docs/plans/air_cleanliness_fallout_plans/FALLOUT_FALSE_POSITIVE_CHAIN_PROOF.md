# Fallout False Positive chain proof

## Scope

False Positive is the reviewed Quarantine archetype chain at candidate `691`, transaction `710070`, route `7172`, and survivor Event Log history `9176`. It occupies event blocks `chaosx.fallout.691` through `chaosx.fallout.697` in `events/fallout_world_end_events.txt` under the Fallout namespace. The chain is dormant and does not activate the Fallout scheduler.

## Admission and receipts

The candidate producer in `common/scripted_effects/fallout_consolidated_effects.txt` selects the lowest owned native state that passes `fallout_event_pilot_false_positive_state_is_current`. That gate requires current state identity, durable state resources, current Supply Access, a completed First Red Line memory, produced Air Winter Shelter Capacity, Adaptation, Reclamation, Exposure, Disease Pressure, phase, population, and a current Quarantine owner with public-health and grievance ledgers. Country admission also requires current Medicine, Cohesion, Recognition, campaign-day bounds, and one affordable branch.

The opening receipt freezes the target state, owner, controller, transition generation, Air Winter values, public health, grievance, reliability, compensation, inspection fatigue, appeal backlog, and cause memory. `fallout_event_691_opening_target_is_current`, `fallout_event_691_target_is_current`, `fallout_event_691_registry_is_current`, `fallout_event_691_delayed_result_can_enter`, `fallout_event_691_callback_can_enter`, and `fallout_event_691_cleanup_can_enter` recheck the relevant receipt before each lane. State reservations use `fallout_event_691_registry_reserved` and `fallout_event_691_registry_committed`.

## Branch and result contract

The four branches are Release and Compensate, Maintain the Cordon, Ward Tribunal, and Rotate Inspection Teams. Costs are branch-specific and checked in both candidate admission and visible options. Hidden AI calls the same affordability triggers and applies deterministic priority order. Result resolution is scheduled for fourteen days. The result grade combines frozen state Supply Access, Shelter Capacity, Adaptation, Disease Pressure, Exposure, country Medicine, Recognition, reliability, and inspection fatigue. Each branch has success, partial, and failure constants for Air Winter, Supply Access, country resources, Cohesion, public health, grievance, reliability, compensation, fatigue, backlog, and cause memory.

Failure requests bounded state population loss through `apply_exact_state_civilian_population_loss` with `chaos_meter_deaths_reason.fallout_aftermath` and damages one infrastructure level through the existing Deaths-backed failure helper. It does not delete a country, tag, state, division, or province.

## Callback and cleanup contract

The callback is scheduled for one hundred fifty days after result delivery. Callback grading uses public health, Cohesion, Recognition, reliability, compensation, cause memory, Supply Access, Reclamation, Disease Pressure, grievance, inspection fatigue, and appeal backlog. Success, partial, and failure apply separate Air Winter, Supply Access, resource, Cohesion, public-health, grievance, reliability, compensation, fatigue, and backlog deltas. Failure requests a smaller bounded Deaths loss. The callback writes stage-two memory before its cleanup ticket is prepared.

`fallout_event_691_cleanup` releases the issued callback or result cleanup receipt, retries the result cleanup when the callback cleanup arrives first, clears the state reservation, closes the state memory, and removes chain flags and generation-bound variables. The cleanup is idempotent because each receipt and flag is checked before it is changed.

## Event Log and presentation

History `9176` is survivor-country memory. The dedicated scripted localisation maps four choice payloads, twelve result payloads, three callback payloads, and cancellation to concrete regional and government-aware text. The chain does not register the Fallout consequence itself as an ordinary Event Log entry, evolution, or ordinary super-event.

The human opening, result, and callback use `GFX_report_event_fallout_false_positive`. The generated source, processed PNG, DDS, manifest, prompt, and handoff are under `docs/assets/691_false_positive/`. The final DDS is `210x176`, legacy one-level uncompressed BGRA, and the sprite is registered in `interface/fallout_consolidated.gfx`.

## Static proof and limits

The event ids are unique within the dedicated Fallout event file. The new scripted constants, triggers, effects, dynamic modifiers, localisation, candidate row, Event Log routing, and workbook row are intended to be loaded together. Hearts of Iron IV was not launched, so dispatch delivery, save recovery, host authority, runtime Event Log rendering, Deaths readback, and player-visible presentation remain user-owned validation surfaces. The scheduler remains dormant and the chain contributes zero release-floor credit until the wider release audit authorizes activation.

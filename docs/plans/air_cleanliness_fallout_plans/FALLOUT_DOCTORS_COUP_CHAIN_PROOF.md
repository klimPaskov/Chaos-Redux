# Fallout Doctor's Coup Chain Proof

## Scope

Doctor's Coup is a dormant Quarantine archetype chain that follows the completed Permit Market memory. It is Fallout-owned content and does not register the Fallout consequence as an ordinary event, evolution, super-event, event log entry, or scheduler activation.

The chain uses candidate `705`, transaction key `710072`, route `7176`, event blocks `chaosx.fallout.705` through `chaosx.fallout.711`, survivor Event Log history `9178`, and reserved route upper bound `7177`. Its event tokens, variables, flags, dynamic modifiers, localisation keys, and asset names are isolated from zombie content and from the earlier False Positive and Permit Market chains.

## Admission and target contract

The candidate producer writes the lowest eligible current-generation native state owned and controlled by a Quarantine country after the Permit Market state memory has closed. Admission requires a current state identity row, durable state resource row, current Supply Access, Shelter Capacity at least `18`, Supply Access at least `12`, Adaptation at least `10`, Disease Pressure from `10` through `81`, Exposure from `8` through `81`, surviving population, a nonzero Air Winter phase below its upper bound, current Quarantine government, public health at least `35`, grievance at least `1`, Medicine at least `8`, Cohesion at least `25`, Recognition at least `10`, campaign time from day `900` through day `5199`, and one complete affordable branch.

The candidate effect stores the state id, owner, controller, transition generation, target type, route, transaction key, human token, hidden-AI token, and crisis or medicine routing in the shared candidate arrays. Opening, delayed result, callback, and cleanup gates rehydrate that same state and owner receipt before any branch effect runs. A stale owner, controller, generation, reservation, or memory receipt fails closed rather than selecting a replacement state.

## Branches and costs

The human opening at `chaosx.fallout.705` exposes four authored choices. Accept Medical Rule costs `2` Food, `1` Medicine, and `3` Recognition. Build a Medical Coalition costs `3` Medicine, `2` Fuel, and `2` Recognition. Arrest the Medical Leadership costs `2` Food, `2` Scrap, and `3` Recognition. Call a Public Vote costs `2` Medicine, `1` Fuel, and `2` Power. The same affordability tests and priority table are used by the hidden-AI opening at `chaosx.fallout.706`, with deterministic tie order and no random fallback.

Every branch pays once after its ordinary receipt and committed branch are authenticated. A generation reset, stale target, invalid branch, or cancelled chain refunds exactly once through the chain-owned payment flag. Resource values are clamped through the existing Fallout survival resource helper after payment or refund.

## Delayed result and callback

The selected branch schedules one hidden or human result after exactly `30` days. Result grading combines state Supply Access, Shelter Capacity, Adaptation, Disease Pressure, Exposure, Medicine, Recognition, Medical Authority, and the Quarantine government bonus. The branch-specific success thresholds are `58` for Accept Medical Rule, `64` for Build a Medical Coalition, `56` for Arrest the Medical Leadership, and `60` for Call a Public Vote. The partial thresholds are `36`, `42`, `34`, and `38` respectively.

The result changes Air Winter Disease Pressure, Shelter Capacity, Exposure, Adaptation, Reclamation, Supply Access, Medicine, Cohesion, Recognition, public health, grievance, Medical Authority, Civil Legitimacy, Medical Fatigue, Coup Risk, cause memory, and the authored government-memory flags. Accept Medical Rule success establishes `fallout_government_archetype = technate` for the current transition generation. The other branches preserve civil control while recording coalition, arrest, or public-vote memory. Each branch also applies its dedicated dynamic modifier and can damage one target building on failure.

Result failure routes a bounded loss through the Deaths system at the authored `0.0008` rate when the target still has more than the minimum remaining population. The chain records the result outcome in survivor-country memory and appends a survivor Event Log payload with the selected branch and result grade. It never deletes the country or changes tags.

The callback is scheduled after exactly `240` days from the result receipt. Callback grading uses the stored result and current ledgers. It applies branch-independent settlement changes to disease, Shelter Capacity, Exposure, Adaptation, Reclamation, Supply Access, Medicine, Cohesion, Recognition, public health, grievance, Medical Authority, Civil Legitimacy, Medical Fatigue, and Coup Risk. The callback writes a success, partial, or failure payload to the same survivor Event Log history and applies the matching dynamic modifier. Callback failure routes a bounded Deaths loss at the authored `0.0004` rate and preserves the same minimum-population guard.

## Event Log, localisation, and asset wiring

History `9178` is routed through `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` to the dedicated Doctor's Coup detail localiser. Choice, result, callback, and cancellation payloads are defined in `common/scripted_localisation/fallout_world_end_doctors_coup_event_log_scripted_localisation.txt`, and all player-facing branch text is in `localisation/english/fallout_world_end_doctors_coup_l_english.yml` with a UTF-8 BOM.

The human opening, result, and callback use `GFX_report_event_fallout_doctors_coup`, registered in `interface/fallout_world_end.gfx`. The dedicated source, processed PNG, DDS, prompt, review note, and hashes are recorded in `docs/assets/705_doctors_coup/manifest.md`. The runtime DDS is `gfx/event_pictures/fallout/report_event_fallout_doctors_coup.dds` and is not shared with any other chain.

## Cleanup and dormancy

The hidden cleanup block at `chaosx.fallout.711` consumes only the authenticated Doctor's Coup delayed-cleanup receipt. It clears frozen state ledgers, branch and outcome variables, reservation flags, payment flags, result and callback tickets, temporary target context, generated modifiers, and the chain-owned memory markers exactly once. No shared Fallout consequence flag is created or cleared by this chain.

Both `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` remain unset. The chain therefore contributes zero release-floor blocks and cannot open a popup or hidden result during the current dormant tranche. Static source review did not include a Hearts of Iron IV runtime launch, so command issuance, save recovery, multiplayer ownership, delayed queue delivery, Event Log rendering, Deaths readback, and player-visible presentation remain unproven engine surfaces.

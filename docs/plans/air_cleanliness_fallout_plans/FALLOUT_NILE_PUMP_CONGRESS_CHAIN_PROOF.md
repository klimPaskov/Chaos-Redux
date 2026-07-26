# Fallout Nile Pump Congress chain proof

Status: dormant static implementation complete, runtime unobserved.

## Ownership and identifiers

The chain is owned by `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`. It uses candidate `579`, transaction key `710055`, scheduler route `7155`, Event Log history `9161`, and events `579` through `585`. It does not reuse Zombie Apocalypse identifiers, paths, sprites, audio, or assets.

## Candidate and target

`fallout_world_end_event_candidate_effects.txt` resets a country-owned candidate state id, scans current owned states, and keeps the lowest eligible native id. The state trigger requires the current generation, owner control, durable Fallout and Air Winter rows, rural category, positive population, food, supply, adaptation, reclamation, exposure and disease limits, and a non-damaged infrastructure level. The country gate requires sub-Saharan Africa, campaign day 730 through 5999, food, clean water, cohesion, recognition, and at least one complete branch cost.

## Branch and delayed-result proof

The opening offers four authored choices with distinct costs. The public pump board spends food, scrap, recognition, and clean water. The upstream command spends fuel, Power, and Command Power. River cooperatives spend medicine, food, recognition, and clean water. Emergency hold spends Power, medicine, and clean water. Payment happens once after current-country, current-target, candidate-target, and affordability revalidation, then refunds on scheduling failure.

The human opening is event `579`, the hidden AI opening is `580`, the result pair is `581` and `582`, the callback pair is `583` and `584`, and cleanup is `585`. Results resolve after 42 days and callbacks after 240 days. The result snapshots the registry before calculating a deterministic viability grade, then applies three outcome classes, country resources, Cohesion, Stability, War Support, state Supply Access, Air Winter reclamation, exposure, disease, infrastructure damage on failure, and bounded Deaths through `apply_exact_state_civilian_population_loss`. Branch-specific ledgers and a persistent water-memory flag distinguish river compact, contested compact, and basin war outcomes. The callback calculates once for a human delivery through `fallout_event_579_callback_outcome_locked`, while hidden AI calculates only when the lock is absent. Both paths include current target-state values in a temporary callback score before authenticated cleanup.

## Memory, AI, Event Log, and assets

The chain freezes owner, controller, generation, state survival values, country ledgers, and the target state. Hidden AI uses affordability, water pressure, government, winter exposure, and War Support to select from the same four branches, then fails closed if none remains affordable. Choice, result, callback, and cancellation payloads write through `record_events_log_system_history_entry` with history `9161`. Central Event Log name and detail routing plus dedicated scripted localisation are wired. If ownership or control changes, metadata-only delayed triggers revalidate the authenticated target and write an explicit `target_lost` cancellation before cleanup rather than silently applying state effects to a new owner. Opening cancellation uses a separate cancellation-history flag so a later retry can record its own choice. The report picture uses the dedicated sprite `GFX_report_event_fallout_nile_pump_congress`, the generated source and processed preview under `docs/assets/579_nile_pump_congress/`, and final DDS `gfx/event_pictures/fallout_world_end/report_event_fallout_nile_pump_congress.dds` at `210x176`.

## Validation boundary

Static checks found balanced braces in the new constants, triggers, and effects, unique event ids `579` through `585`, complete event localisation keys including the six applied dynamic modifiers, a UTF-8 BOM localisation file, and a valid `210x176` uncompressed BGRA DDS with exact file length and texture caps. The engine-native delayed queue, target delivery, Event Log rendering, Deaths readback, save recovery, multiplayer presentation, and AI frequency remain unobserved because HOI4 was not run.

The chain remains dormant because scheduler activation flags are unset. It contributes one reviewed ordinary candidate row and seven defined blocks, but it is not release-floor credit until the broader activation audit is approved.

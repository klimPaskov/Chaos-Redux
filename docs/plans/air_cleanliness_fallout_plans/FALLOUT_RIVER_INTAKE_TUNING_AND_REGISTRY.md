# Fallout River Intake at Dawn Tuning and Registry Contract

## Scope

This document records the dormant River Intake at Dawn survival pilot. It is a global-survival event family under `add_namespace = chaosx.fallout`. The pilot is not an activation approval and it is not included in the release-floor event-block count.

The opening uses one exact ordinary receipt from the Fallout dispatch substrate. The receipt target must be a state. The state must still belong to the receiving country, retain a current Fallout survival identity row, retain a durable resource row, expose an Air Winter water-security value, and carry the produced Air Winter snapshot source. The opening rejects a state that already has a committed intake registry flag.

## Registry contract

The opening copies the state target into a country and state registry. The country stores `fallout_event_107_intake_state_id`, `fallout_event_107_intake_registry_generation`, and `fallout_event_107_intake_registry_owner`. The state stores the generation and owner values and receives `fallout_event_107_intake_registry_committed`.

Every delayed result and cleanup trigger rechecks the generation, owner, state flag, state identity row, durable resource row, state owner, water-security variable, Air Winter snapshot generation, and produced source kind. Result and callback effects run only after their exact delayed receipt has been terminalized. A resolved result row remains callback-held until the callback cleanup receipt has removed its own row and prepared the exact result cleanup ticket. Final cleanup clears the registry after both rows are released, or after a callback scheduling failure. Durable state memories remain after cleanup so later chains can read the water history.

## Tuning tables

The contract is centralized in `common/script_constants/fallout_world_end_event_constants.txt`.

- Result delay is 2 days.
- Callback delay is 5 days.
- Ordinary modifiers last 90 days.
- Compact modifiers last 180 days.
- Epidemic modifiers last 120 days.
- The four branches are close the intake, ration filtered flow, seize upstream pumps, and accept foreign testing.
- Success thresholds use water 50, filters 40, medicine 40, recognition 35, and state water 45.
- Partial thresholds use water 28, filters 20, medicine 20, and state water 25.
- Failure mortality requests 0.004 of the current state population through `apply_exact_state_civilian_population_loss`, with the Fallout aftermath Deaths reason.
- Result and callback values change water, medicine, filters, fuel, recognition, stability, war support, army experience, and state water. The common orientation clamp runs after each result and callback.
- Supply-consumption modifiers follow engine semantics. Pump authority and a successful compact reduce consumption by 6 percent and 5 percent. An epidemic aftershock increases consumption by 10 percent.

The branch token upper bound is 5. The hidden AI result tokens use event IDs 1009 through 1012. The hidden AI callback uses event ID 1013. These IDs are above the existing ledger and do not collide with the NZL package or earlier dormant pilots.

## Branch effects

Closing the intake protects the settling tanks when the water reserve is healthy, while a failure contaminates the intake and records a state memory. Rationing spends filter and medicine stock to preserve measured distribution. Seizing upstream pumps improves the military water route while creating an upstream dispute memory. Foreign testing raises medicine and recognition when it works and applies a country testing modifier. The foreign branch is intentionally a pilot surface only. It does not yet select or validate a real bilateral partner target.

The callback resolves into a written water compact, an unequal-access memory, or an epidemic aftershock. A successful callback removes the temporary contamination modifier and records a durable state compact memory. Partial and failed callbacks retain the state dispute or epidemic memories. The separate river-raid continuation named by the event bible is not part of this pilot.

## Files and wiring

- `common/scripted_triggers/fallout_world_end_water_event_triggers.txt` owns target and registry authentication.
- `common/scripted_effects/fallout_world_end_water_event_effects.txt` owns scoring, result effects, Deaths calls, history payloads, callback scheduling, and cleanup.
- `common/dynamic_modifiers/fallout_world_end_water_security_dynamic_modifiers.txt` owns state and country consequence modifiers.
- `events/fallout_world_end_events.txt` owns human, hidden AI, delayed result, callback, and cleanup event blocks.
- `localisation/english/fallout_world_end_l_english.yml` owns concrete text for the four choices, three outcome bands, callback outcomes, modifiers, and event-log payloads.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt` maps history 9106 and its fifteen payloads.
- `FALLOUT_EVENT_ID_LEDGER.md` records IDs 107 through 113 and the hidden AI IDs 1009 through 1013.

The dedicated event image `GFX_report_event_fallout_river_intake_at_dawn` is reused from the already wired River Intake asset package. No zombie asset, file, path, audio, or sprite is used.

## Static proof completed

- Braces are balanced in all touched script and event files.
- The Fallout event namespace has no duplicate event IDs after moving the hidden AI pair to 1009 through 1013.
- The localisation file retains UTF-8 with BOM.
- All new event, modifier, history, payload, and scripted-localisation keys are present in the touched localisation surfaces.
- The water chain contains no scheduler activation flag, active scheduler flag, or caller.
- The water chain contains no zombie reference.
- Callback cleanup order is statically reconciled in `FALLOUT_CALLBACK_CLEANUP_ORDER_PROOF.md`.
- The foreign testing result remains visible in the pilot event surface, but the full bilateral registry remains pending and is therefore not counted as a completed diplomacy chain.

## Runtime proof still required

HOI4 was not launched by request. Static inspection cannot prove that the engine resolves a numeric state value in `var:` scope as a live state target at every delayed boundary. It also cannot prove delayed receipt retention across save and reload, multiplayer owner checks, event ordering, dynamic modifier placement, Deaths callback accounting, event-log rendering, or scheduler performance.

The event caller and exact Fallout-owned scheduler activation are still absent. Until those are reviewed and wired, this chain must remain dormant. A future activation review must also replace the foreign-testing pilot with a live bilateral partner registry or explicitly reject the branch as a country-only result.

## Release accounting

This pilot adds no release-floor blocks. It is a typed implementation tranche for the first global-survival chain. The release floor remains 660 manually reviewed event blocks. Expansion toward 910 remains gated on review depth, scheduler activation proof, and the unresolved engine-sensitive surfaces above.

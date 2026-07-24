# Fallout Market Under the Viaduct chain proof

## Static wiring

The chain is defined in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout` with ids `chaosx.fallout.380` through `.386`.
Its constants, triggers, effects, dynamic modifiers, scripted Event Log localisation, localisation, and GFX registration are dedicated to the Market Under the Viaduct.
The candidate registry adds candidate `380`, transaction `710028`, route `7128`, and a deterministic supply-node state selector.

## Native state and ledger proof

The state trigger requires current Air Winter snapshot provenance, a surviving population, exposure from `18` through `73`, a non-damaged supply node, railway or infrastructure support, and reclamation or supply instability.
The producer scores supply node, railway, infrastructure, and industrial capacity, with the lowest native state id as the exact tie-breaker.
The result and callback mutate food, scrap, medicine, price, merchant, ration, supply access, reclamation, exposure, and state memory. Failure routes through the shared Deaths contract and damages the supply node before fallback buildings.

## Asset proof

The dedicated source, processed preview, prompt, manifest, GFX handoff, and runtime DDS are under `docs/assets/air_cleanliness_fallout/fallout_market_under_viaduct/` and `gfx/event_pictures/fallout_world_end/report_event_fallout_market_under_viaduct.dds`.

## Inspector boundary

The bounded `hoi4.event_inspect` lint request for `chaosx.fallout.380` used helper expansion disabled, depth one, twenty nodes, and forty edges with refresh enabled.
It returned a tool-call timeout after 180 seconds while awaiting `hoi4.event_inspect`.
No files scanned, diagnostics, proposed files, changed files, artifacts, or validation result were returned.
This is an inspector transport boundary, not proof of native runtime validity or delayed delivery.

## Release count

This chain defines seven reviewed event blocks and contributes zero of the 660 release-floor blocks while the scheduler, authority, save-recovery, multiplayer, Event Log, and final audit gates remain closed.

# Fallout Old Weather Station chain proof

## Static wiring

The chain is defined in `events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout` with ids `chaosx.fallout.373` through `.379`.
Its constants, triggers, effects, dynamic modifiers, scripted Event Log localisation, localisation, and GFX registration are dedicated to the Old Weather Station.
The candidate registry adds candidate `373`, transaction `710027`, route `7127`, and a deterministic radar-station state selector.

## Native state and ledger proof

The state trigger requires current Air Winter snapshot provenance, a surviving population, exposure from `12` through `67`, a non-damaged radar station, and reclamation or supply instability.
The producer scores radar station, infrastructure, and industrial capacity, with the lowest native state id as the exact tie-breaker.
The result and callback mutate forecast, contact, intelligence, supply access, reclamation, exposure, and state memory. Failure routes through the shared Deaths contract and damages the radar station before fallback buildings.

## Asset proof

The dedicated source, processed preview, prompt, manifest, GFX handoff, and runtime DDS are under `docs/assets/air_cleanliness_fallout/fallout_old_weather_station/` and `gfx/event_pictures/fallout_world_end/report_event_fallout_old_weather_station.dds`.

## Inspector boundary

The bounded `hoi4.event_inspect` lint request for `chaosx.fallout.373` used helper expansion disabled, depth one, twenty nodes, and forty edges with refresh enabled.
It returned `status: error`, `code: EVENT_ISSUE_LIMIT`, and `count: 23137` against a fixed maximum of `20000`.
The returned result contained no scanned files, diagnostics, proposed files, changed files, or artifacts, with `validation.passed: false`.
This is an inspector result ceiling, not proof of native runtime validity or delayed delivery.

## Release count

This chain defines seven reviewed event blocks and contributes zero of the 660 release-floor blocks while the scheduler, authority, save-recovery, multiplayer, Event Log, and final audit gates remain closed.

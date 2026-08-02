# Fallout Black Start chain proof

## Static evidence

- Candidate row: `common/scripted_effects/fallout_consolidated_effects.txt`, candidate `310`.
- Trigger contract: `common/scripted_triggers/fallout_consolidated_triggers.txt`.
- Transaction effects: `common/scripted_effects/fallout_consolidated_effects.txt`.
- Event ids `310` through `316`: `events/fallout_world_end_events.txt`.
- Constants: `fallout_event_310_*` groups in `common/script_constants/fallout_consolidated_constants.txt`.
- Event Log id `9123`: shared effects and scripted localisation plus the dedicated fifteen-payload mapping.
- Report asset: source, processed preview, DDS, manifest, and GFX handoff under `docs/assets/air_cleanliness_fallout/fallout_black_start/`.

The touched script files have balanced braces, no unsupported `<=` or `>=`
operators, and no non-ASCII script tokens. Event ids `310` through `316` are
defined once. Localisation keys are BOM encoded and event, modifier, and Event
Log references resolve by static scan.

## Engine-sensitive evidence

The read-only call
`hoi4.event_inspect(mode=lint, selector=chaosx.fallout.310,
expandHelpers=false, maxDepth=1, maxNodes=20, maxEdges=40, refresh=true)`
returned `Transport closed`. No HOI4 runtime was launched, as authorized by
the task. Therefore the exact engine-side reachability of the delayed result,
host authority, save recovery, and multiplayer delivery is unproven.

## Release-floor disposition

Black Start is a dormant reviewed pilot and contributes zero countable blocks
to the 660-block release floor. It is suitable for deeper expansion only after
the engine-sensitive coordinator surfaces are proven or the blocker is
resolved.

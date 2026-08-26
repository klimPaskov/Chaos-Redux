# Disaster Wardens sound-design handoff

Status: source and derived audio evidence retained; the custom Disaster Wardens entity and custom action-state registrations were retired in favor of the vanilla infantry consumer. The selection cue is an active runtime candidate, while the remaining action cues are optional evidence pending parent review and do not establish an eight-unit audio completion receipt.

## Exact runtime identifiers

For each role `<role>` in the manifest:

- Source sound ID: `chaosx_disaster_wardens_<role>_sound`.
- Soundeffect wrapper ID: `chaosx_disaster_wardens_<role>_sfx`.
- Packaged file: `audio/derived/chaosx_disaster_wardens_<role>.wav`.
- Proposed runtime copy: `sound/012_africa/units/disaster_wardens/chaosx_disaster_wardens_<role>.wav`.

## Consumer map

| Role | Exact sound ID | Exact soundeffect ID | Action / phase |
|---|---|---|---|
| `select` | `chaosx_disaster_wardens_select_sound` | `chaosx_disaster_wardens_select_sfx` | `selection/acknowledgement`; one-shot |
| `idle` | `chaosx_disaster_wardens_idle_sound` | `chaosx_disaster_wardens_idle_sfx` | Optional retained cue; no custom entity-state consumer after vanilla infantry reuse |
| `move` | `chaosx_disaster_wardens_move_sound` | `chaosx_disaster_wardens_move_sfx` | Optional retained cue; vanilla infantry supplies the movement state |
| `rescue` | `chaosx_disaster_wardens_rescue_sound` | `chaosx_disaster_wardens_rescue_sfx` | Optional retained special-action cue; no custom entity-state consumer |
| `containment` | `chaosx_disaster_wardens_containment_sound` | `chaosx_disaster_wardens_containment_sfx` | Optional retained special-action cue; no custom entity-state consumer |
| `death` | `chaosx_disaster_wardens_death_sound` | `chaosx_disaster_wardens_death_sfx` | Optional retained cue; vanilla infantry supplies the death state |

The closest installed-vanilla model precedent inspected was `gfx/entities/units_infantry.asset`: its state event calls the animation-category soundeffect `infantry_move_animation`. The exact package IDs remain registered in `sound/012_africa_strange_forces_sound.asset`, but the retired custom entity no longer consumes the action roles. The selection role can play after successful formation creation, while vanilla infantry supplies movement, combat, and death states.

All six derived/runtime WAVs are PCM signed 16-bit, 44.1 kHz, mono. Do not loop the selection, optional action, or death cues. Runtime volume, distance, category, and instance limits require parent integration and live-consumer review.

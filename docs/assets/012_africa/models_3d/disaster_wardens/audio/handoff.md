# Disaster Wardens sound-design handoff

Status: source and derived audio package complete; parent runtime registration and consumer wiring complete.

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
| `idle` | `chaosx_disaster_wardens_idle_sound` | `chaosx_disaster_wardens_idle_sfx` | `chaosx_disaster_warden_idle`; frame 1 entry accent; 1–61 action |
| `move` | `chaosx_disaster_wardens_move_sound` | `chaosx_disaster_wardens_move_sfx` | `chaosx_disaster_warden_move`; frame 16; 1–31 loop |
| `rescue` | `chaosx_disaster_wardens_rescue_sound` | `chaosx_disaster_wardens_rescue_sfx` | `chaosx_disaster_warden_rescue`; frame 16; 1–31 action |
| `containment` | `chaosx_disaster_wardens_containment_sound` | `chaosx_disaster_wardens_containment_sfx` | `chaosx_disaster_warden_containment`; frame 24; 1–46 action |
| `death` | `chaosx_disaster_wardens_death_sound` | `chaosx_disaster_wardens_death_sfx` | `chaosx_disaster_warden_death`; frame 24; 1–46 action |

The closest installed-vanilla model precedent inspected was `gfx/entities/units_infantry.asset`: its state event calls the animation-category soundeffect `infantry_move_animation`. The exact package IDs are registered in `sound/012_africa_strange_forces_sound.asset`. Animation roles use entity-state events, the selection role plays after successful formation creation, and every wrapper has a runtime consumer.

Do not loop the selection, action, special-action, or death cues. Idle is an entry accent, not a continuous bed. Move is a repeatable one-shot aligned to the named frame in each 31-frame movement cycle. Runtime volume, distance, category, and instance limits require parent integration and live-consumer review.

# Stone Cohorts sound-design handoff

Status: source and derived audio package complete; parent runtime registration and consumer wiring complete.

## Exact runtime identifiers

For each role `<role>` in the manifest:

- Source sound ID: `chaosx_stone_cohorts_<role>_sound`.
- Soundeffect wrapper ID: `chaosx_stone_cohorts_<role>_sfx`.
- Packaged file: `audio/derived/chaosx_stone_cohorts_<role>.wav`.
- Proposed runtime copy: `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_<role>.wav`.

## Consumer map

| Role | Exact sound ID | Exact soundeffect ID | Action / phase |
|---|---|---|---|
| `select` | `chaosx_stone_cohorts_select_sound` | `chaosx_stone_cohorts_select_sfx` | `selection/acknowledgement`; one-shot |
| `idle` | `chaosx_stone_cohorts_idle_sound` | `chaosx_stone_cohorts_idle_sfx` | `chaosx_stone_idle`; frame 1 entry accent; 1–61 action |
| `move` | `chaosx_stone_cohorts_move_sound` | `chaosx_stone_cohorts_move_sfx` | `chaosx_stone_move`; frame 16; 1–31 loop |
| `attack` | `chaosx_stone_cohorts_attack_sound` | `chaosx_stone_cohorts_attack_sfx` | `chaosx_stone_attack`; frame 21; 1–41 action |
| `collapse_recovery` | `chaosx_stone_cohorts_collapse_recovery_sound` | `chaosx_stone_cohorts_collapse_recovery_sfx` | `chaosx_stone_collapse_recovery`; frame 16; 1–31 action |
| `death` | `chaosx_stone_cohorts_death_sound` | `chaosx_stone_cohorts_death_sfx` | `chaosx_stone_death`; frame 24; 1–46 action |

The closest installed-vanilla model precedent inspected was `gfx/entities/units_infantry.asset`: its state event calls the animation-category soundeffect `infantry_move_animation`. The exact package IDs are registered in `sound/012_africa_strange_forces_sound.asset`. Animation roles use entity-state events, the selection role plays after successful formation creation, and every wrapper has a runtime consumer.

Do not loop the selection, action, special-action, or death cues. Idle is an entry accent, not a continuous bed. Move is a repeatable one-shot aligned to the named frame in each 31-frame movement cycle. Runtime volume, distance, category, and instance limits require parent integration and live-consumer review.

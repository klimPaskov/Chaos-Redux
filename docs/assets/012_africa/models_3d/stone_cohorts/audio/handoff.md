# Stone Cohorts sound-design handoff

Status: source and runtime-format files revalidated; synchronization and exact selection binding blocked.

## Exact runtime identifiers

For each role `<role>` in the manifest:

- Source sound ID: `chaosx_stone_cohorts_<role>_sound`.
- Soundeffect wrapper ID: `chaosx_stone_cohorts_<role>_sfx`.
- Packaged file: `audio/derived/chaosx_stone_cohorts_<role>.wav`.
- Proposed runtime copy: `sound/012_africa/units/stone_cohorts/chaosx_stone_cohorts_<role>.wav`.

## Consumer map

| Role | Exact sound ID | Exact soundeffect ID | Action / phase |
|---|---|---|---|
| `select` | `chaosx_stone_cohorts_select_sound` | `chaosx_stone_cohorts_select_sfx` | one-shot; exact engine selection consumer blocked |
| `idle` | `chaosx_stone_cohorts_idle_sound` | `chaosx_stone_cohorts_idle_sfx` | resync after accepted `chaosx_stone_idle` provider action |
| `move` | `chaosx_stone_cohorts_move_sound` | `chaosx_stone_cohorts_move_sfx` | resync after accepted `chaosx_stone_move` provider action |
| `attack` | `chaosx_stone_cohorts_attack_sound` | `chaosx_stone_cohorts_attack_sfx` | resync to aim/contact/recoil/recovery phases of accepted provider action |
| `collapse_recovery` | `chaosx_stone_cohorts_collapse_recovery_sound` | `chaosx_stone_cohorts_collapse_recovery_sfx` | resync after distinct accepted provider action |
| `death` | `chaosx_stone_cohorts_death_sound` | `chaosx_stone_cohorts_death_sfx` | resync to impact/settling phases of accepted provider action |

The closest installed-vanilla model precedent remains `gfx/entities/units_infantry.asset`: its move-state event calls `infantry_move_animation`. The installed selection surface resolves the global `select_army` soundeffect in `sound/soundeffects.asset`; the inspected unit and entity definitions expose no per-subunit selection hook. The existing creation-time `scoped_sound_effect = "chaosx_stone_cohorts_select_sfx"` is therefore not the actual selection consumer. The mandatory custom selection role is blocked unless the parent proves a real per-unit selection binding surface; runtime definitions and live consumers remain parent-owned.

Do not loop the selection, action, special-action, or death cues. Idle remains an entry accent, not a continuous bed. Exact frames, volume, distance, category, instance limits, and selection routing require parent integration after the provider action package exists.

## Non-firing melee audit

`stone_cohorts` is `non_firing`. The polearm attack is melee. Required firing states, muzzle/discharge locators, muzzle particles, discharge lights, firearm sounds, and cartridge/beam effects are all zero. The attack and impact candidate is a sourced metal-contact cue only; it must synchronize to the accepted polearm-contact phase if a valid provider action is later produced.

# Event 014 Retired Animation Source Manifest

- Original package date: 2026-07-01
- Retirement reconciliation: 2026-07-13
- Package root: `docs/assets/014_cannibalism/animations_imagegen/`
- Status: **historical source/provenance package; not a live runtime-output owner**

This directory preserves six early imagegen animation experiments, their separate source frames, processed PNG frames, sheet PNGs, GIF previews, and contact sheets. The experiments were superseded before final Event 014 wiring. Their former DDS and sprite names are not registered, are not expected to exist under `gfx/interface/animated/014_cannibalism/`, and must not be treated as missing runtime files.

The live animation source of truth is:

- `docs/assets/014_cannibalism/gui_animation_portraits/manifest.md`
- `docs/assets/014_cannibalism/gui_animation_portraits/gfx_handoff.md`
- `interface/014_cannibalism.gfx`
- `interface/014_cannibalism_frontline_hunger.gui`
- `common/scripted_guis/014_cannibalism_scripted_gui.txt`

That accepted package owns fourteen live animations: the 12-frame ordinary Hannibal portrait, 16-frame Wendigo portrait, and twelve non-portrait GUI animations. Each has a live sheet DDS and static fallback DDS.

## Preserved historical experiments

| Historical slug | Preserved frames | Preserved evidence | Runtime disposition |
| --- | ---: | --- | --- |
| `cannibalism_frontline_hunger_seal` | 8 source + 8 processed | sheet PNG, GIF, contact sheet | Superseded; no live DDS or sprite. |
| `cannibalism_cult_pressure_warning` | 8 source + 8 processed | sheet PNG, GIF, contact sheet | Superseded; no live DDS or sprite. |
| `cannibalism_island_signal_card` | 8 source + 8 processed | sheet PNG, GIF, contact sheet | Superseded; no live DDS or sprite. |
| `cannibalism_hannibal_resonance_seal` | 8 source + 8 processed | sheet PNG, GIF, contact sheet | Superseded; no live DDS or sprite. |
| `cannibalism_council_portrait_overlay` | 8 source + 8 processed | sheet PNG, GIF, contact sheet | Superseded; no live DDS or sprite. |
| `cannibalism_world_end_progress_border` | 8 source + 8 processed | sheet PNG, GIF, contact sheet | Superseded; no live DDS or sprite. |

The still-protected archival file `gfx/leaders/014_cannibalism/hannibal.dds` was not touched by either the retired or accepted animation processing. Its expected SHA-256 remains `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88`.


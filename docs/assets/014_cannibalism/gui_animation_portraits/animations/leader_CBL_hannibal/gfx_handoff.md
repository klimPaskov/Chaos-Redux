# leader_CBL_hannibal GFX Handoff

## Existing registration verified

`interface/014_cannibalism.gfx` already contains the required live registrations, so no GFX edit is needed:

```txt
spriteType = { name = "GFX_portrait_CBL_hannibal" texturefile = "gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds" }
spriteType = { name = "GFX_cannibalism_revealed_portrait_static" texturefile = "gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds" }
frameAnimatedSpriteType = { name = "GFX_cannibalism_revealed_portrait_animated" texturefile = "gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds" noOfFrames = 12 animation_rate_fps = 6 looping = yes play_on_show = yes pause_on_loop = 0.0 }
```

## Final runtime files

- Static DDS: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds`, 156x210
- Sheet DDS: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`, 1872x210
- Frame count: 12 horizontal frames
- Static fallback: frame 000
- Character key: `CBL_hannibal`
- Character portrait field: `portraits = { civilian = { large = GFX_portrait_CBL_hannibal } }`
- GUI window: `cannibalism_revealed_command_window`
- GUI animated icon: `cannibalism_revealed_portrait_animated`
- GUI static icon: `cannibalism_revealed_portrait_static`

## Reveal and fallback behavior verified

- `common/scripted_guis/014_cannibalism_scripted_gui.txt` requires `cannibalism_reveal_complete` for `cannibalism_revealed_command_scripted_gui`.
- `common/scripted_effects/014_cannibalism_unification_effects.txt` sets `cannibalism_reveal_complete` before recruiting `CBL_hannibal`.
- When animations are enabled, the GUI shows the animated sprite. When `cannibalism_gui_animations_disabled` is set, it shows the static fallback.

## Local references used

- Offline wiki: `Graphical asset modding - Hearts of Iron 4 Wiki.md`, `frameAnimatedSpriteType`
- Offline wiki: `Interface modding - Hearts of Iron 4 Wiki.md`, `iconType`
- Offline wiki: `Scripted GUI modding - Hearts of Iron 4 Wiki.md`, window visibility and triggers
- Vanilla: `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, `interface/_leader_portraits.gfx`, `common/characters/ABK.txt`
- Official vanilla documentation: `documentation/effects_documentation.md`, `set_country_leader_portrait`, `set_leader_portrait`, and `set_portraits`

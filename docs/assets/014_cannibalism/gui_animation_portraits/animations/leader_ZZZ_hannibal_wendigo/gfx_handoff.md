# leader_ZZZ_hannibal_wendigo GFX Handoff

## Existing registration verified

`interface/014_cannibalism.gfx` already contains the required live registrations, so no GFX edit is needed:

```txt
spriteType = { name = "GFX_portrait_ZZZ_hannibal_wendigo" texturefile = "gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds" }
spriteType = { name = "GFX_cannibalism_wendigo_portrait_static" texturefile = "gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds" }
frameAnimatedSpriteType = { name = "GFX_cannibalism_wendigo_portrait_animated" texturefile = "gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds" noOfFrames = 16 animation_rate_fps = 6 looping = yes play_on_show = yes pause_on_loop = 0.0 }
```

## Final runtime files

- Static DDS: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds`, 156x210
- Sheet DDS: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds`, 2496x210
- Frame count: 16 horizontal frames
- Static fallback: frame 000
- Character key: `ZZZ_hannibal_wendigo`
- Character portrait field: `portraits = { civilian = { large = GFX_portrait_ZZZ_hannibal_wendigo } }`
- GUI window: `cannibalism_wendigo_command_window`
- GUI animated icon: `cannibalism_wendigo_portrait_animated`
- GUI static icon: `cannibalism_wendigo_portrait_static`

## Reveal and fallback behavior verified

- `common/scripted_guis/014_cannibalism_scripted_gui.txt` requires both `cannibalism_reveal_complete` and `cannibalism_wendigo_route_active` for `cannibalism_wendigo_command_scripted_gui`.
- The window also requires `is_cannibalism_wendigo_hannibal_country = yes`.
- When animations are enabled, the GUI shows the animated sprite. When `cannibalism_gui_animations_disabled` is set, it shows the static fallback.

## Local references used

- Offline wiki: `Graphical asset modding - Hearts of Iron 4 Wiki.md`, `frameAnimatedSpriteType`
- Offline wiki: `Interface modding - Hearts of Iron 4 Wiki.md`, `iconType`
- Offline wiki: `Scripted GUI modding - Hearts of Iron 4 Wiki.md`, window visibility and triggers
- Vanilla: `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, `interface/_leader_portraits.gfx`, `common/characters/ABK.txt`
- Official vanilla documentation: `documentation/effects_documentation.md`, `set_country_leader_portrait`, `set_leader_portrait`, and `set_portraits`

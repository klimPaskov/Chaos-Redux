# Alien infantry counter handoff

Status: `needs_user_review` and pending `chaosx_icon_artist` production.

The owning subunit is `alien_infantry`, its sprite token is `alien_infantry`, and its model consumer is `alien_infantry_entity`.

Required counter consumers are `GFX_unit_alien_infantry_icon_medium` using `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds` and `GFX_unit_alien_infantry_icon_medium_white` using `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds`.

The installed vanilla definitions are `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx:46` and `:199`. Their source DDS files are `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` and `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.

The large strip is 152x42 with two 76x42 frames. The map strip is 60x12 with two 30x12 frames. Both use real alpha, `noOfFrames = 2`, left-to-right normal/state frame order, dark borders, a pale selected/inverted state, compact military silhouette, and no opaque canvas. The large green family is anchored by RGB 73,106,73 and nearby shaded greens such as 74,107,74; the artist must sample the decoded reference rather than use an arbitrary green.

Matching skill-local families are `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/` and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/`, including their contact sheets and decoded `unit_infantry_icon.png` / `onmap_infantry.png` precedents.

The icon-artist package must return original ImageGen source PNGs with native transparency, prompts, processed two-frame alpha PNGs, final DDS strips, decoded round-trip evidence, native-size comparison/contact sheets, manifest entries, and `gfx_handoff.md`. The silhouette should combine an unmistakable large-eyed alien head with a simple laser-rifle bar while staying readable at 30x12. Reused vanilla art, renamed counters, primitive local drawing, arbitrary green, or an opaque background is forbidden.

Parent-owned `.gfx` registration and runtime validation remain pending. No counter output was created by the 3D worker.

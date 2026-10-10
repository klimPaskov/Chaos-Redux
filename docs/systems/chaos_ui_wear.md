# Chaos UI Wear

The vanilla interface cracks as global Chaos rises. Hairline fractures appear on the top bar, the left-hand country panels and the minimap frame at Chaos tier 1, spread with every tier, and turn purple once a world-end scenario has begun. The player can turn the effect off in Settings > Miscellaneous or in the All Settings window.

## How it works

1. `update_chaos_meter_tier` (`common/scripted_effects/chaos_meter_effects.txt`) owns the `chaos_tier` global flag, whose value is the Chaos tier from `chaos_meter_tier_id` (0 to 5). Its last step calls `update_chaos_ui_wear`.
2. `update_chaos_ui_wear` (`common/scripted_effects/chaos_ui_wear_effects.txt`) copies that tier into `global.chaos_ui_wear_frame`. Tier 0 leaves the frame at 0.
3. `chaos_ui_wear_visible` (`common/scripted_triggers/chaos_ui_wear_triggers.txt`) is true while the frame is above tier 0 and the `chaos_ui_wear_disabled` global flag is unset. Every overlay scripted GUI uses it as its `visible` trigger.
4. Each crack decal in `interface/chaos_ui_wear.gui` is a five-frame sheet; the scripted GUI `properties` block sets `frame = global.chaos_ui_wear_frame`, so frame N is the decal for tier N.
5. Every decal has a dark twin and a purple twin at the same position. The element triggers show the dark one while `world_end` is unset and the purple one once it is set, so the colour switch follows any of the world-end scenarios without hooks in their effects.
6. All decals are `iconType` elements with `alwaystransparent = yes`, inside containers without backgrounds, so they never take clicks or tooltips from the vanilla controls underneath.

The overlay GUIs have no `dirty` variable because the world-end colour is read live; each refresh is one flag check and one variable read per element, which costs nothing measurable. AI never evaluates them (`ai_enabled = { always = no }`).

## Surfaces

| Scripted GUI | Parent | Decals (position in the parent) |
| --- | --- | --- |
| `chaos_ui_wear_topbar_gui` | `parent_window_token = top_bar` | flag frame corner (`corner_tl`, 0,0, scale 0.6); lower lip of the resource and menu block (`strip_h`, 96,56); lower lip of the war-status block (`strip_short`, 780,16); top border of the date and speed widget (`strip_short`, UPPER_RIGHT -330,-14) |
| `chaos_ui_wear_minimap_gui` | `parent_window_name = mini_map_interface` | upper-left corner of the minimap frame (`corner_tl`, -6,-6, scale 0.7) |
| `chaos_ui_wear_<panel>_gui` | `politics_tab`, `decision_tab`, `production_tab`, `construction_tab`, `trade_tab`, `deployment_tab`, `logistics_tab` | header plate seam between the title and the close button (`strip_short`, width-184,26); right frame column (`strip_v`, width-34,60) |
| `chaos_ui_wear_research_gui` | `technology_tab` | right frame column only; the Research and Facilities tabs sit on the header seam |

Panel widths are 550 except Trade (689). Top-bar decals left of the date widget are anchored UPPER_LEFT and the date-widget decal UPPER_RIGHT, matching the vanilla `topbar.gui` anchors, so they stay on the same frame pieces at every resolution; UI scale scales them with the vanilla elements.

No decal is placed over text, values, portraits or list rows. The decals cover frame borders, the empty right span of panel header plates, the flag frame and the minimap picture edge.

## Engine limits and excluded surfaces

- Event and news windows: `EventWindow`, `EventWindow_news` and their variants have no scripted GUI token and are created as several simultaneous instances, so a `parent_window_name` attachment would bind to one instance at most. Overriding the vanilla `eventwindow.gui` would not solve the per-instance problem. They stay clean, which also keeps every event text fully readable.
- National focus tree and the full-screen technology tree: their whole surface is content, so there is no frame region where a crack would avoid focus or technology text.
- Diplomacy view: it has no header plate or frame column comparable to the other panels.
- The tier is read from `chaos_tier`; a world end that happens at Chaos tier 0 shows no cracks until Chaos reaches tier 1. World-end scenarios add Chaos, so this does not occur in normal play.

## Settings

- Settings > Miscellaneous: `chaos_ui_wear_checkbox` with label and description below Static Winter Map (`interface/chaosx.gui`, `common/scripted_guis/chaosx_scripted_gui_settings.txt`).
- All Settings window: `all_settings_chaos_ui_wear_checkbox` row below Static winter map (`interface/chaosx_all_settings.gui`, `common/scripted_guis/chaosx_scripted_gui_all_settings.txt`).
- Both call `toggle_chaos_ui_wear`. The checkbox sprite comes from `GetChaosUiWearCheckboxSprite` (`common/scripted_localisation/chaos_ui_wear_scripted_localisation.txt`) and is ticked while the cracks are enabled.
- `reset_miscellaneous_to_defaults` clears `chaos_ui_wear_disabled`, so a settings reset turns the cracks back on.
- Localisation: `localisation/english/chaos_ui_wear_l_english.yml` and `chaosx.all_settings.chaos_ui_wear` in `chaosx_all_settings_l_english.yml`.

## Assets

| Sprite (`interface/chaos_ui_wear.gfx`) | DDS (`gfx/interface/chaos_ui_wear/`) | Sheet | Frame |
| --- | --- | --- | --- |
| `GFX_chaos_ui_wear_corner_tl` / `_purple` | `chaos_ui_wear_corner_tl.dds` / `_purple.dds` | 640x128 | 128x128 |
| `GFX_chaos_ui_wear_strip_h` / `_purple` | `chaos_ui_wear_strip_h.dds` / `_purple.dds` | 2560x40 | 512x40 |
| `GFX_chaos_ui_wear_strip_v` / `_purple` | `chaos_ui_wear_strip_v.dds` / `_purple.dds` | 200x512 | 40x512 |
| `GFX_chaos_ui_wear_strip_short` / `_purple` | `chaos_ui_wear_strip_short.dds` / `_purple.dds` | 640x32 | 128x32 |

All sheets have `noOfFrames = 5` and are uncompressed BGRA DDS written with the event-assets converter's `write_bgra_dds`.

Sources (kept locally under the git-ignored `docs/assets/chaos_ui_wear/source/`): `crack_corner_source.png` (corner fracture network) and `crack_strip_source.png` (long fracture), both generated through the gptimage MCP with native alpha (about 96% fully transparent pixels). Processing: the source alpha is dilated so hairlines stay at least one pixel wide after downscaling, then redrawn as a near-black core (12,11,10) with a pale chipped edge (205,198,182) offset one pixel down-right so the crack reads on HOI4's dark metal. The strip is the source's central band; `strip_v` is that strip rotated; `strip_short` is a quarter-width segment from 55% along it. Tier frames reveal 34, 50, 66, 83 and 100% of the crack (radially from the corner, inward from both ends for strips) at 55, 66, 77, 88 and 96% opacity. Purple frames recolour the same pixels from (88,24,150) to (214,150,255) by luminance and add a 2.2px violet glow at 55%.

## Validation

- `hoi4.gui_render` of `chaos_ui_wear_topbar_window` at 1920x1080 and 2560x1440 (UI scale 1) with scenarios `wear_tier5_dark`, `wear_tier1_dark` and `wear_tier5_purple` (source revision `c4bbb87f…`): frames resolve from `global.chaos_ui_wear_frame`, the purple twins replace the dark ones only with `world_end`, the right-anchored date decal follows the screen edge, and no click regions are reported for the overlay.
- Tier 1, 3, 5 and purple composites of the decals over the MCP baseline renders of the vanilla `topbar` and `countrydecisionview` confirmed that no decal covers text or values.
- DDS round trip: every sheet decodes back to its processed PNG with zero pixel difference.
- `hoi4.gui_render` of `chaos_ui_wear_decisions_window` (purple tier 5) at 1920x1080 and 2560x1440 rendered without blockers; the only findings are the dark/purple twin overlaps, which the `world_end` triggers make mutually exclusive in game, and expected edge-anchored drift.
- Not checked: the minimap and the other left-panel attachments were reviewed from source geometry and the decision panel render, not rendered in their parents; the trade, construction and production header plates were not rendered. In-game confirmation belongs to the user.

## Future extensions

- A sixth frame with debris flakes for the final tier, or a slow frame-animated hairline spread when the tier rises.
- Anchor containers in overridden vanilla windows (wiki "anchor" pattern) for surfaces that need cracks under, rather than over, their own elements.
- Event-specific tints (green for plagues, ash grey for nuclear winter) through further twins driven by the same frame variable.

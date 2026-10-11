# Chaos UI Wear

The vanilla interface wears as global Chaos rises. Fine surface fractures and small chips along panel edges appear on the top bar, the left-hand country panels and the minimap frame from Chaos tier 1, spread with every tier (none at Calm World), and turn purple once a world-end scenario has begun. The player can turn the effect off in Settings > Miscellaneous or in the All Settings window.

## How it works

1. Wear starts at Chaos tier 1 (Gathering Storm) and grows with every tier through tier 5 (World Collapse). Calm World (tier 0, meter 0 to 199) shows nothing.
2. `update_chaos_meter_tier` (`common/scripted_effects/chaos_meter_effects.txt`) owns the `chaos_tier` global flag (value 0 to 5). It runs on every meter change, the Settings and debug tier controls and the load-time recalculation; the overlay needs no hook of its own.
3. Every decal exists once per tier and colour in `interface/chaos_ui_wear.gui` (`<decal>_t<N>` and `<decal>_t<N>_purple`). Each icon displays one fixed sheet frame (`frame = N`).
4. The scripted GUIs show exactly one of those icons per decal through element `_visible` triggers that call `chaos_ui_wear_dark_tier_N` or `chaos_ui_wear_purple_tier_N` (`common/scripted_triggers/chaos_ui_wear_triggers.txt`). Those read the live `chaos_tier`, `world_end` and `chaos_ui_wear_disabled` global flags, so the tier is never copied into a stored variable that could be stale, and nothing depends on a `properties` frame refresh. Purple replaces dark while `world_end` is set.
5. All decals are `iconType` elements with `alwaystransparent = yes`, inside containers without backgrounds, so they never take clicks or tooltips from the vanilla controls underneath.

Root cause of the earlier "no change with the tier" report: the visible frame came from `global.chaos_ui_wear_frame`, a copy of the tier written by a hook and read through a `properties` `frame` binding, and the hook compared the flag with `constant:` tokens inside `has_global_flag`. A stale or unset copy (a save loaded before the hook ran, or an unresolved comparison) left the GUI on its fallback frame whatever the tier. The variable, the hook and the `properties` bindings are removed.

The GUIs set no `dirty` variable, so they refresh every tick and the live flag reads take effect immediately; each refresh is a few flag lookups per element. AI never evaluates them (`ai_enabled = { always = no }`).

## Surfaces

| Scripted GUI | Parent | Decals (position in the parent) |
| --- | --- | --- |
| `chaos_ui_wear_topbar_gui` | `parent_window_token = top_bar` | flag frame corner (`corner_tl`, 0,0, scale 0.6); lower lip of the resource and menu block (`strip_h`, 96,40); lower lip of the war-status block (`strip_short`, 780,8); top border of the date and speed widget (`strip_short`, UPPER_RIGHT -330,4) |
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

Look: damage to the metal surface itself, following the bevels of the vanilla dark brushed-steel plates (reference crops under `docs/assets/chaos_ui_wear/ref/`, from `gfx/interface/topbar/background.dds` and `gfx/interface/minimap.dds`): hairline fractures with a near-black core and a faint pale edge, tiny chips at corners, low contrast, vanilla grey-black palette, fading out with distance from the corner. Purple twins (world end) recolour the same pixels.

| Sprite (`interface/chaos_ui_wear.gfx`) | DDS (`gfx/interface/chaos_ui_wear/`) | Sheet | Frame |
| --- | --- | --- | --- |
| `GFX_chaos_ui_wear_corner_tl` / `_purple` | `chaos_ui_wear_corner_tl.dds` / `_purple.dds` | 640x128 | 128x128 |
| `GFX_chaos_ui_wear_strip_h` / `_purple` | `chaos_ui_wear_strip_h.dds` / `_purple.dds` | 2560x40 | 512x40 |
| `GFX_chaos_ui_wear_strip_v` / `_purple` | `chaos_ui_wear_strip_v.dds` / `_purple.dds` | 200x512 | 40x512 |
| `GFX_chaos_ui_wear_strip_short` / `_purple` | `chaos_ui_wear_strip_short.dds` / `_purple.dds` | 640x32 | 128x32 |

Sheets have `noOfFrames = 5` (frame N = tier N) and are uncompressed BGRA DDS written with the event-assets converter's `write_bgra_dds`. Sources (git-ignored, `docs/assets/chaos_ui_wear/source/`): `v2_corner_source.png` and `v2_edge_source.png`, generated with the gptimage MCP with native alpha (about 97% zero-alpha pixels, verified). `docs/assets/chaos_ui_wear/process_v2.py` crops, downsamples with premultiplied alpha, darkens to the steel palette, fades the corner network radially, and reveals more fractures per tier (corner radially, strips by whole fracture clusters in a fixed order, cumulative) at 45 to 92% opacity. `docs/assets/chaos_ui_wear/gen_gui.py` regenerates the `.gui`, scripted GUI and trigger files.

## Validation

- `hoi4.gui_render` was attempted for the top bar window twice and both calls ended with `JOB_WORKER_EXIT` (worker stopped without an outcome), so no MCP render exists; the retry limit is spent. A source-geometry composite of the decals on the vanilla top bar texture for tiers 1 to 5 is kept at `docs/assets/chaos_ui_wear/check_topbar_tiers_1_5.png`; the top-bar decals were positioned (lip y=40, war block y=8, date y=4) so that every decal pixel of every frame lies on opaque plate pixels of the vanilla top bar texture (0 pixels outside, checked programmatically); calm shows no decal because tier 0 has no icon or trigger. The render tool also only accepts boolean scenario flags, so the valued `chaos_tier` flag cannot be set in a scenario.
- Decals contain only borders and empty plate by position; the other surfaces were reviewed from geometry only. In-game confirmation belongs to the user.

## Future extensions

- A sixth frame with debris flakes for the final tier, or a slow frame-animated hairline spread when the tier rises.
- Anchor containers in overridden vanilla windows (wiki "anchor" pattern) for surfaces that need cracks under, rather than over, their own elements.
- Event-specific tints (green for plagues, ash grey for nuclear winter) through further twins driven by the same frame variable.

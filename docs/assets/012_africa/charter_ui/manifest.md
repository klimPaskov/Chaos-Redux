# Event 012 Charter League UI asset manifest

Status: complete for the sixteen binary texture dependencies reserved by `interface/012_africa_charter.gfx`. Runtime wiring remains parent-owned. The package uses generated source art from the official built-in ImageGen workflow and deterministic crop, resize, chroma-key removal, sheet assembly, and DDS conversion only.

## Style and reference evidence

The canonical reference root was used at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference`. I inspected `icons/decision_categories/contact_sheet.png` and `icons/balance_of_power/contact_sheet.png` before production for the restrained brass, indigo, earth-red, and painted-metal language. These references are review material only and are not runtime inputs. No project-local visual-reference copy was used.

## Static runtime assets

All static files below have an ImageGen source under `source_png/`, an exact-size processed PNG under `processed_png/`, a decoded-DDS review PNG under `decoded_dds_png/`, and a final BGRA DDS under `gfx/interface/012_africa/`.

| Sprite name | Source | Processed size | Final DDS |
| --- | --- | ---: | --- |
| `GFX_012_africa_charter_window_background` | `source_png/charter_window_background_source.png` | 1000x680 | `gfx/interface/012_africa/charter_window_background.dds` |
| `GFX_012_africa_charter_header_plate` | `source_png/header_plate_source.png` | 976x84 | `gfx/interface/012_africa/charter_header_plate.dds` |
| `GFX_012_africa_member_card_frame` | `source_png/member_card_frame_source.png` | 300x546 | `gfx/interface/012_africa/member_card_frame.dds` |
| `GFX_012_africa_regional_card_frame` | `source_png/regional_card_frame_source.png` | 316x546 | `gfx/interface/012_africa/regional_card_frame.dds` |
| `GFX_012_africa_relationship_badges` | `source_png/relationship_badges_source.png` | 256x64 | `gfx/interface/012_africa/relationship_badges.dds` |
| `GFX_012_africa_primary_value_icons` | `source_png/primary_value_icons_source.png` | 128x36 | `gfx/interface/012_africa/primary_value_icons.dds` |
| `GFX_012_africa_secondary_value_icons` | `source_png/secondary_value_icons_source.png` | 128x36 | `gfx/interface/012_africa/secondary_value_icons.dds` |
| `GFX_012_africa_clause_tabs` | `source_png/clause_tabs_source.png` | 70x24 | `gfx/interface/012_africa/clause_tabs.dds` |
| `GFX_012_africa_regional_overlay_buttons` | `source_png/regional_overlay_buttons_source.png` | 92x28 | `gfx/interface/012_africa/regional_overlay_buttons.dds` |
| `GFX_012_africa_project_progress_frame` | `source_png/project_progress_frame_source.png` | 330x240 | `gfx/interface/012_africa/project_progress_frame.dds` |
| `GFX_012_africa_rival_bloc_panel` | `source_png/rival_bloc_panel_source.png` | 330x94 | `gfx/interface/012_africa/rival_bloc_panel.dds` |
| `GFX_012_africa_diaspora_summary_panel` | `source_png/diaspora_summary_panel_source.png` | 330x202 | `gfx/interface/012_africa/diaspora_summary_panel.dds` |

The canvas sizes are derived from the 1000x680 Charter window and the exact positions, button sizes, text extents, and column boundaries in `interface/012_africa_charter.gui`. Static panel textures are intentionally opaque painted surfaces. The relationship badge and value strips are atlas-like strips because their registered consumers use one texture surface.

## Animated runtime assets

| Animated sprite | Static fallback | Frames | Frame size | Sheet | Rate / loop |
| --- | --- | ---: | ---: | ---: | --- |
| `GFX_012_africa_charter_seal_activation_animated` | `GFX_012_africa_charter_seal_activation_static` | 8 | 64x64 | 512x64 | 8 fps, looping, play on show |
| `GFX_012_africa_charter_authority_ring_animated` | `GFX_012_africa_charter_authority_ring_static` | 10 | 64x64 | 640x64 | 6 fps, looping, play on show |

Seal frames are independently generated authored states from dim rest through stamped activation and return. Ring frames are independently generated authored states from a dim authority ring through a closed stamped ring and return. Chroma-key removal is used only to obtain alpha; the visual state changes are present in the generated frame sources. Each animation includes source frames, processed 64x64 frames, a horizontal sheet PNG, final sheet DDS, static fallback PNG and DDS, GIF preview, contact sheet, and frame metadata.

## Source and processing notes

- Source mode: `$imagegen` built-in mode for every static asset and every animation frame.
- Palette: restrained brass, charcoal-indigo, aged parchment, muted olive, and terracotta; no modern web-dashboard styling.
- Mechanical processing: deterministic crop/fit, exact-size resize, chroma-key removal for animation transparency, horizontal sheet assembly, GIF preview assembly, DDS conversion with `convert_to_dds.py`, and DDS header decode for review.
- No `.gfx`, `.gui`, gameplay, localisation, or spreadsheet files were edited by this asset package.

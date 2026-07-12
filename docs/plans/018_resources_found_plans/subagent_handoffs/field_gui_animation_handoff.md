# Event 018 selected-field GUI animation handoff

## Result

The selected-field GUI visual tranche is complete. It supplies all thirteen runtime textures already named by `interface/018_resources_found.gfx`, five real-frame animations with exact live counts and rates, five exact static fallbacks, Suspended and Closed static states, a 470 by 304 panel, 58 real state-art frames, five GIF previews, seven contact sheets, a precise manifest, and a full binary hash inventory.

No `.gfx`, `.gui`, scripted GUI, gameplay, localisation, focus, idea, decision, category, achievement, spreadsheet, or shared tooling file was edited.

## Canonical documentation

- Brief: `docs/assets/018_resources_found/animations/selected_field_ui/brief.md`
- Frame plan: `docs/assets/018_resources_found/animations/selected_field_ui/frame_plan.md`
- Exact generation prompts: `docs/assets/018_resources_found/animations/selected_field_ui/prompts.md`
- Manifest and provenance: `docs/assets/018_resources_found/animations/selected_field_ui/manifest.md`
- Full SHA-256 inventory: `docs/assets/018_resources_found/animations/selected_field_ui/hash_inventory.md`
- Validation record: `docs/assets/018_resources_found/animations/selected_field_ui/validation.md`

## Exact runtime files and live sprites

Target GFX: `interface/018_resources_found.gfx`.

| Runtime file | Dimensions | Live sprite | Frames | FPS | Static fallback | State role |
| --- | ---: | --- | ---: | ---: | --- | --- |
| `gfx/interface/018_resources_found/resource_field_panel.dds` | 470 by 304 | `GFX_018_resource_field_panel` | 1 | Not animated | Not applicable | Selected-field panel background |
| `gfx/interface/animated/018_resources_found/resource_field_seal_sheet.dds` | 1280 by 128 | `GFX_018_resource_field_seal_animated` | 10 | 8 | `gfx/interface/animated/018_resources_found/resource_field_seal_static.dds`, sprite `GFX_018_resource_field_seal` | Productive safe field |
| `gfx/interface/animated/018_resources_found/resource_field_unsafe_sheet.dds` | 1280 by 128 | `GFX_018_resource_field_unsafe_animated` | 10 | 8 | `gfx/interface/animated/018_resources_found/resource_field_unsafe_static.dds`, sprite `GFX_018_resource_field_unsafe` | Unsafe supports and corrosion, no creature |
| `gfx/interface/animated/018_resources_found/resource_field_disturbance_sheet.dds` | 1536 by 128 | `GFX_018_resource_field_disturbance_animated` | 12 | 9 | `gfx/interface/animated/018_resources_found/resource_field_disturbance_static.dds`, sprite `GFX_018_resource_field_disturbance` | Physical fractures, tools, dust, vibration |
| `gfx/interface/animated/018_resources_found/resource_field_breach_sheet.dds` | 1536 by 128 | `GFX_018_resource_field_breach_animated` | 12 | 10 | `gfx/interface/animated/018_resources_found/resource_field_breach_static.dds`, sprite `GFX_018_resource_field_breach` | Open shaft, pressure, rubble, moving silhouettes |
| `gfx/interface/animated/018_resources_found/resource_field_sealing_sheet.dds` | 1536 by 128 | `GFX_018_resource_field_sealing_animated` | 12 | 8 | `gfx/interface/animated/018_resources_found/resource_field_sealing_static.dds`, sprite `GFX_018_resource_field_sealing` | Concrete, supports, pumping, shutter, pinning cycle |
| `gfx/interface/018_resources_found/resource_field_suspended.dds` | 128 by 128 | `GFX_018_resource_field_suspended` | 1 | Not animated | Not applicable | Guarded idle machinery behind locked gate |
| `gfx/interface/018_resources_found/resource_field_closed.dds` | 128 by 128 | `GFX_018_resource_field_closed` | 1 | Not animated | Not applicable | Permanent steel-and-concrete seal with extraction symbols removed |

All five animated GFX definitions should retain `looping = yes`, `play_on_show = yes`, and `pause_on_loop = 0.0`. The live definitions already use those values and the exact frame counts and FPS above.

## Frame-source ownership and count

| Family | Generated source atlas | Individual source frames | Processed frames | Sheet PNG | Preview GIF | Contact sheet |
| --- | --- | ---: | ---: | --- | --- | --- |
| Seal | `source_frames/seal/resource_field_seal_source_atlas.png` | 10 | 10 | `sheets/resource_field_seal_sheet.png` | `previews/resource_field_seal_preview.gif` | `contact_sheets/resource_field_seal_contact_sheet.png` |
| Unsafe | `source_frames/unsafe/resource_field_unsafe_source_atlas.png` | 10 | 10 | `sheets/resource_field_unsafe_sheet.png` | `previews/resource_field_unsafe_preview.gif` | `contact_sheets/resource_field_unsafe_contact_sheet.png` |
| Disturbance | `source_frames/disturbance/resource_field_disturbance_source_atlas.png` | 12 | 12 | `sheets/resource_field_disturbance_sheet.png` | `previews/resource_field_disturbance_preview.gif` | `contact_sheets/resource_field_disturbance_contact_sheet.png` |
| Breach | `source_frames/breach/resource_field_breach_source_atlas.png` | 12 | 12 | `sheets/resource_field_breach_sheet.png` | `previews/resource_field_breach_preview.gif` | `contact_sheets/resource_field_breach_contact_sheet.png` |
| Sealing | `source_frames/sealing/resource_field_sealing_source_atlas.png` | 12 | 12 | `sheets/resource_field_sealing_sheet.png` | `previews/resource_field_sealing_preview.gif` | `contact_sheets/resource_field_sealing_contact_sheet.png` |

All paths in this table are relative to `docs/assets/018_resources_found/animations/selected_field_ui/`.

The 56 animated source frames are separately illustrated atlas cells, not script-made transformations. Suspended and Closed were generated separately and raise the real state-art count to 58. Mechanical processing only crops, removes chroma, isolates the intended medallion from a neighboring atlas sliver, aligns, rescales, sheets, previews, and converts existing art.

## Current GUI state mapping

The live `interface/018_resources_found.gui` places every active state image at child position x 290, y 4 in `resources_found_gui_selection` and the Closed image at the same position in `resources_found_gui_closed_selection`. Each content area is 438 by 180. The state art is 128 by 128 and therefore fits at x 290 through 417 and y 4 through 131. Both containers begin at global coordinates x 16, y 82, preserving the inspected medallion position at x 306, y 86.

The live `common/scripted_guis/018_resources_found_scripted_gui.txt` currently maps:

- Seal to safe, active, non-suspended, non-sealing, non-disturbance, non-breach fields.
- Unsafe to the same baseline state when workforce safety is below band 3.
- Disturbance to `resources_found_disturbance_revealed` before breach and full sealing.
- Breach to `resources_found_breach_revealed` before full sealing.
- Sealing to `resources_found_full_seal_active`.
- Suspended to `resources_found_field_suspended` before full sealing.
- Each animated state to its static fallback when `resources_found_animations_disabled` is set.

## Closed-state parent disposition

The dedicated historical-field surface now consumes `GFX_018_resource_field_closed`. Successful exact closure stores the removed six-resource ledger and a `resources_found_last_closed_field` pointer, removes the field from the active owner registry, and opens the history view. The field-management category accepts the same history trigger and remains reachable after the last active field closes. The History button toggles that view without ever assigning the sealed state to the gameplay selection. This preserves the exact-closure invariant while making the permanent closure identity visible.

## Visual inspection performed

- Inspected all 56 source frames and all 56 processed frames through the five family contact sheets.
- Inspected Panel, all five fallback frames, Suspended, and Closed through `selected_field_ui_runtime_contact_sheet.png`.
- Inspected all seven state images at the exact live panel coordinates through `selected_field_ui_live_position_contact_sheet.png`.
- Confirmed Seal contains only productive machinery and survey motion.
- Confirmed Unsafe contains redrawn damaged supports and corrosion without creatures.
- Confirmed Disturbance contains physical fracture, tool, rubble, lamp, and dust changes without magical glow.
- Confirmed Breach contains persistent open stone, pressure, rubble, and changing silhouettes.
- Confirmed Sealing contains a physical support, concrete, pump, drainage, shutter, and pinning sequence.
- Confirmed Suspended reads as guarded idle works and Closed removes extraction machinery and symbols.
- Confirmed the panel contains no baked text and preserves a quiet left content field, right medallion recess, and an uncluttered bottom strip; the live GUI fits five compact controls across that strip.

## Technical validation

- Animated source frames: 56 present, 56 unique hashes.
- Animated processed frames: 56 present, 56 unique hashes.
- Static real state frames: 2 present.
- Runtime DDS: 13 present.
- Sheet PNG and DDS dimensions match exact frame multiples.
- Every sheet section equals its processed frame.
- Every fallback equals processed frame 000.
- Transparent corners and zero visible chroma contamination confirmed.
- All DDS files use one-surface uncompressed 32-bit BGRA and decode pixel-identically to their processed PNGs.
- Largest runtime texture is 1536 by 128, well below the approximate 16 MB sprite-texture concern in the graphical asset reference.

## Changed paths

- Added the complete 145-file package under `docs/assets/018_resources_found/animations/selected_field_ui/`, consisting of six package Markdown files, five source atlases, 56 individual source frames, 56 processed frames, five sheet PNGs, five fallback PNGs, five GIFs, and seven contact sheets.
- Added three source PNGs under `docs/assets/018_resources_found/source_png/gui/`.
- Added three processed PNGs under `docs/assets/018_resources_found/processed_png/gui/`.
- Added three runtime DDS files under `gfx/interface/018_resources_found/`.
- Added ten runtime DDS files under `gfx/interface/animated/018_resources_found/`.
- Added this handoff file.

## Risks and remaining parent work

- The Closed identity has a live history-only consumer and is not an open mapping.
- Engine display at supported UI scales was waived by the user. Decoded DDS and exact-coordinate visual inspection found no asset-side layout or format issue.
- The consolidated Event 018 manifest and GFX handoff should reference this package rather than duplicate or rewrite its source/provenance data.

## Simplifications, omissions, and fallbacks

No simplification, omission, placeholder, fallback substitution, alternate filename, or transform-only animation was used. The five static assets are the required explicit fallbacks for players who disable animation. All requested visual states and runtime files are present.

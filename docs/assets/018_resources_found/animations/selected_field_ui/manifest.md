# Event 018 selected-field UI asset manifest

## Package identity

- Event: 018, Resources Found
- Tranche: selected resource-field scripted-GUI panel and state art
- Production date: 2026-07-11
- Source mode: generated fictional art through Codex's built-in image-generation workflow
- Image-generation fallback: none
- Status: source art, processing, runtime conversion, previews, contact sheets, validation, and handoff complete
- Parent-owned work not performed here: `.gfx`, `.gui`, scripted GUI, gameplay, localisation, consolidated Event 018 manifest, and live in-game wiring

This package contains one 470 by 304 panel, five real-frame animation families, five static fallbacks, and two additional static states. The five animation families contain 56 separately illustrated source frames. Suspended and Closed add two separately generated static state frames, giving 58 real state-art frames in total. The panel is additional UI background art.

## References inspected

- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/countryintelligenceagencyview.gfx`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/countryintelligenceagencyview.gui`
- `docs/assets/system_camp_repression_rework/processed/ui/GFX_repression_ledger_window_bg.png`
- `docs/assets/017_random_faction/source/random_faction_bloc_pressure_seal_source_atlas.png`
- `docs/assets/014_cannibalism/animations_imagegen/cannibalism_cult_pressure_warning/previews/cannibalism_cult_pressure_warning_contact.png`
- `docs/assets/014_cannibalism/animations_imagegen/cannibalism_island_signal_card/previews/cannibalism_island_signal_card_contact.png`

The asset skill's named idea, focus, decision, and UI reference folders were checked. Only the achievement overlay is present under the current skill asset folder, so the closest existing Chaos Redux GUI and animation packages above were used as visual references. No reference art was copied into the final assets.

## Prompt and provenance record

The exact prompts used for all eight image-generation calls are preserved verbatim in `docs/assets/018_resources_found/animations/selected_field_ui/prompts.md`, SHA-256 `18ebabe381058930d7a65498eb12510c95061dbec36104d68867190a3be348e6`.

| Master | Built-in generation artifact | Prompt section | Reference input role | Workspace source | Source dimensions | SHA-256 |
| --- | --- | --- | --- | --- | ---: | --- |
| Panel | `exec-8dea4f06-03a8-49de-8ef4-ca3606fa50ac.png` | Panel source | None, brand-new generation | `docs/assets/018_resources_found/source_png/gui/resource_field_panel_source.png` | 1560 by 1008 | `8e2257ed7dbfa8ab675cc782c023e91b591b687d7d40cf4dfcd50e866c66a0f9` |
| Safe seal atlas | `exec-723afa44-8199-4d48-bbae-10c2b05732cc.png` | Safe seal source atlas | None, brand-new generation | `docs/assets/018_resources_found/animations/selected_field_ui/source_frames/seal/resource_field_seal_source_atlas.png` | 1774 by 887 | `7acabbe8d90d8549509ef8eabfd5188bda1dd1c569d5a8bd66bd8be669e89f05` |
| Unsafe atlas | `exec-7806f673-9600-4c3a-bec1-940fc4d0fafd.png` | Unsafe source atlas | Seal atlas used only for style, camera, scale, and materials | `docs/assets/018_resources_found/animations/selected_field_ui/source_frames/unsafe/resource_field_unsafe_source_atlas.png` | 1774 by 887 | `7f440a0c221c8ec118d6b70519720254ac0890d27318fb456c6c05f3d9ef7f9e` |
| Disturbance atlas | `exec-ffe608c6-d90d-4015-9935-8da27bfd6b96.png` | Disturbance source atlas | Unsafe atlas used only for style, camera, scale, and materials | `docs/assets/018_resources_found/animations/selected_field_ui/source_frames/disturbance/resource_field_disturbance_source_atlas.png` | 1774 by 887 | `111f5a49f7385f8575721a62069f8cc8433f805434acb3faeaedf3d6d566012a` |
| Breach atlas | `exec-cdb648ab-5909-43a6-b9be-98cd4c3c841c.png` | Breach source atlas | Disturbance atlas used only for style, camera, scale, and materials | `docs/assets/018_resources_found/animations/selected_field_ui/source_frames/breach/resource_field_breach_source_atlas.png` | 1774 by 887 | `2a576283d13261025897d82db02ee144b1a31ca0a57761ae3748d96f345b4f22` |
| Sealing atlas | `exec-39322f0d-ea64-4fbd-98b4-d4e1372c2ef0.png` | Sealing source atlas | Seal atlas used only for style, camera, scale, and materials | `docs/assets/018_resources_found/animations/selected_field_ui/source_frames/sealing/resource_field_sealing_source_atlas.png` | 1774 by 887 | `aef53e0857955b7af26de4c1a205ff85d13d76dc07e1e190fc13ffd834ff3408` |
| Suspended | `exec-17bd4345-21c9-4724-af5e-109146523d34.png` | Suspended static source | Seal atlas used only for style, camera, scale, and materials | `docs/assets/018_resources_found/source_png/gui/resource_field_suspended_source.png` | 1254 by 1254 | `69e87ab5ecc13cede7438e2b8e9d700761cdde9635df58d3bf1b2a9cc16ac1f4` |
| Closed | `exec-c434cbe6-2921-4bec-bd67-884329ec8acf.png` | Closed static source | Suspended source used only for style, camera, scale, and materials | `docs/assets/018_resources_found/source_png/gui/resource_field_closed_source.png` | 1254 by 1254 | `34d02979877f7ab0f61b29ad5104689c93267357215f9a93daae2129db170c23` |

Every storyboard atlas was generated specifically as animation source art. Its cells were individually illustrated according to the frame plan, then preserved as individual source-frame PNGs in left-to-right, top-to-bottom order. The generated cells visibly redraw machinery, supports, fractures, tools, rubble, silhouettes, concrete, pumps, shutters, and other local scene content. No script created the animation's visual changes.

## Mechanical processing

- The original source atlases and static source PNGs are preserved unchanged.
- Atlas cells were cropped mechanically into the named source-frame PNGs.
- The canonical imagegen chroma helper at `C:/Users/klimp/.codex/skills/.system/imagegen/scripts/remove_chroma_key.py` removed the sampled border green with soft matte and despill.
- Stray neighboring-atlas slivers were removed by keeping the main medallion region while retaining dust, tools, rubble, hoses, and silhouettes within that region.
- Each family used one shared scale and a bottom-center anchor on a 128 by 128 transparent canvas.
- Frames were assembled left-to-right into exact one-row sheets.
- Static fallbacks are exact copies of approved frame 000 after processing.
- GIFs are review-only dark-background previews and are not game assets.
- DDS files were written through `.tools/convert_to_dds.py` as one-surface, uncompressed 32-bit BGRA textures with canonical channel masks.

The complete binary hash inventory, including every source frame and processed frame, is in `docs/assets/018_resources_found/animations/selected_field_ui/hash_inventory.md`.

## Animation assets

| State | Intended use | Source art | Processed frames | Frame size | Frames | FPS | Loop | Sheet PNG | Runtime sheet DDS | Static fallback PNG | Runtime fallback DDS | Sprites | Status |
| --- | --- | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- |
| Seal | Productive safe field and survey machinery motion, no horror | `source_frames/seal/resource_field_seal_000_source.png` through `_009_source.png` | `processed_frames/seal/resource_field_seal_000.png` through `_009.png` | 128 by 128 | 10 | 8 | Yes, play on show | `sheets/resource_field_seal_sheet.png` | `gfx/interface/animated/018_resources_found/resource_field_seal_sheet.dds` | `sheets/resource_field_seal_static.png` | `gfx/interface/animated/018_resources_found/resource_field_seal_static.dds` | `GFX_018_resource_field_seal`, `GFX_018_resource_field_seal_animated` | Complete |
| Unsafe | Damaged supports, corrosion, fastener failure, rubble, no creature | `source_frames/unsafe/resource_field_unsafe_000_source.png` through `_009_source.png` | `processed_frames/unsafe/resource_field_unsafe_000.png` through `_009.png` | 128 by 128 | 10 | 8 | Yes, play on show | `sheets/resource_field_unsafe_sheet.png` | `gfx/interface/animated/018_resources_found/resource_field_unsafe_sheet.dds` | `sheets/resource_field_unsafe_static.png` | `gfx/interface/animated/018_resources_found/resource_field_unsafe_static.dds` | `GFX_018_resource_field_unsafe`, `GFX_018_resource_field_unsafe_animated` | Complete |
| Disturbance | Physical fractures, displaced tools, dust, and vibration without magical glow | `source_frames/disturbance/resource_field_disturbance_000_source.png` through `_011_source.png` | `processed_frames/disturbance/resource_field_disturbance_000.png` through `_011.png` | 128 by 128 | 12 | 9 | Yes, play on show | `sheets/resource_field_disturbance_sheet.png` | `gfx/interface/animated/018_resources_found/resource_field_disturbance_sheet.dds` | `sheets/resource_field_disturbance_static.png` | `gfx/interface/animated/018_resources_found/resource_field_disturbance_static.dds` | `GFX_018_resource_field_disturbance`, `GFX_018_resource_field_disturbance_animated` | Complete |
| Breach | Open broken shaft, pressure dust, rubble, and moving heavy silhouettes | `source_frames/breach/resource_field_breach_000_source.png` through `_011_source.png` | `processed_frames/breach/resource_field_breach_000.png` through `_011.png` | 128 by 128 | 12 | 10 | Yes, play on show | `sheets/resource_field_breach_sheet.png` | `gfx/interface/animated/018_resources_found/resource_field_breach_sheet.dds` | `sheets/resource_field_breach_static.png` | `gfx/interface/animated/018_resources_found/resource_field_breach_static.dds` | `GFX_018_resource_field_breach`, `GFX_018_resource_field_breach_animated` | Complete |
| Sealing | Beam placement, concrete pumping, drainage, shutter closure, and pinning | `source_frames/sealing/resource_field_sealing_000_source.png` through `_011_source.png` | `processed_frames/sealing/resource_field_sealing_000.png` through `_011.png` | 128 by 128 | 12 | 8 | Yes, play on show | `sheets/resource_field_sealing_sheet.png` | `gfx/interface/animated/018_resources_found/resource_field_sealing_sheet.dds` | `sheets/resource_field_sealing_static.png` | `gfx/interface/animated/018_resources_found/resource_field_sealing_static.dds` | `GFX_018_resource_field_sealing`, `GFX_018_resource_field_sealing_animated` | Complete |

## Panel and static states

| Asset | Intended use | Source PNG | Processed PNG | Runtime DDS | Dimensions | Sprite | Status |
| --- | --- | --- | --- | --- | ---: | --- | --- |
| Resource-field panel | Compact selected-field background with left text field, right medallion recess, and bottom control strip | `docs/assets/018_resources_found/source_png/gui/resource_field_panel_source.png` | `docs/assets/018_resources_found/processed_png/gui/resource_field_panel.png` | `gfx/interface/018_resources_found/resource_field_panel.dds` | 470 by 304 | `GFX_018_resource_field_panel` | Complete |
| Suspended | Guarded locked works, tarped idle drum, disconnected belt, maintained supports | `docs/assets/018_resources_found/source_png/gui/resource_field_suspended_source.png` | `docs/assets/018_resources_found/processed_png/gui/resource_field_suspended.png` | `gfx/interface/018_resources_found/resource_field_suspended.dds` | 128 by 128 | `GFX_018_resource_field_suspended` | Complete |
| Closed | Permanent concrete-and-steel bulkhead with extraction machinery and symbols removed | `docs/assets/018_resources_found/source_png/gui/resource_field_closed_source.png` | `docs/assets/018_resources_found/processed_png/gui/resource_field_closed.png` | `gfx/interface/018_resources_found/resource_field_closed.dds` | 128 by 128 | `GFX_018_resource_field_closed` | Complete |

Processed PNG hashes:

| Path | SHA-256 |
| --- | --- |
| `docs/assets/018_resources_found/processed_png/gui/resource_field_panel.png` | `19a5015ab07f08c924b35274ecdc9dba60f0b0bd01e39e2af0cc020dde7b147c` |
| `docs/assets/018_resources_found/processed_png/gui/resource_field_suspended.png` | `e2ad4689b1eff815f964cd313f8b0609bb9f910afe5413c054cfdec3e5ffde66` |
| `docs/assets/018_resources_found/processed_png/gui/resource_field_closed.png` | `cf52528a5166d170a376dedac93b1f856eca037640f5ef86afadb0e8bbe9e580` |

## Runtime DDS inventory

| Runtime path | Dimensions | SHA-256 | Live sprite |
| --- | ---: | --- | --- |
| `gfx/interface/018_resources_found/resource_field_panel.dds` | 470 by 304 | `b42f24e708c569d771070f0304ee5ad700a9ef1e6facffb73f4031127ff922f8` | `GFX_018_resource_field_panel` |
| `gfx/interface/animated/018_resources_found/resource_field_seal_sheet.dds` | 1280 by 128 | `2ad8e47cae010e12812e223ffe8a68d057589e7679ce942c2eb53a00fbb90f21` | `GFX_018_resource_field_seal_animated` |
| `gfx/interface/animated/018_resources_found/resource_field_seal_static.dds` | 128 by 128 | `82148f4a5c2c9abc4882a80b206136e2b2ab0c45715d8d81ed9b1b889ed4f920` | `GFX_018_resource_field_seal` |
| `gfx/interface/animated/018_resources_found/resource_field_unsafe_sheet.dds` | 1280 by 128 | `7924fa12ea8a395051f49a56904e0e10707e6b374940e5560df779585a22b0f0` | `GFX_018_resource_field_unsafe_animated` |
| `gfx/interface/animated/018_resources_found/resource_field_unsafe_static.dds` | 128 by 128 | `f48cb3eb5c7c7eb8bf63b6369c2558c52640b7af94508d4f86700bc3d5bc9259` | `GFX_018_resource_field_unsafe` |
| `gfx/interface/animated/018_resources_found/resource_field_disturbance_sheet.dds` | 1536 by 128 | `9b30463b33af3a50254dd5f131ca8e96b69436ac57333ab297118bcbf3807289` | `GFX_018_resource_field_disturbance_animated` |
| `gfx/interface/animated/018_resources_found/resource_field_disturbance_static.dds` | 128 by 128 | `482565df2d9f9fe168e05e126323fdfe8b166609b719ee1a316fd179ab092e72` | `GFX_018_resource_field_disturbance` |
| `gfx/interface/animated/018_resources_found/resource_field_breach_sheet.dds` | 1536 by 128 | `c0819adbd057ad28e8c2d132a3cec461c294fc503b51ee30c7c122dd6e542a20` | `GFX_018_resource_field_breach_animated` |
| `gfx/interface/animated/018_resources_found/resource_field_breach_static.dds` | 128 by 128 | `25f093d0f455c0513fe0f75e64bf2fb3a5ee35fc89c065b91ab692ed38cc552b` | `GFX_018_resource_field_breach` |
| `gfx/interface/animated/018_resources_found/resource_field_sealing_sheet.dds` | 1536 by 128 | `91ddb6b01bf4ee50579920cef45e838d6a8c9dde15d0be774ba2e8b94857f289` | `GFX_018_resource_field_sealing_animated` |
| `gfx/interface/animated/018_resources_found/resource_field_sealing_static.dds` | 128 by 128 | `1884dd2ed437841a5fb0e46b3d99bf07fa06129090edeb57d8715a8919a0b7e9` | `GFX_018_resource_field_sealing` |
| `gfx/interface/018_resources_found/resource_field_suspended.dds` | 128 by 128 | `e38bac59b0bc7c30073d4f65f8a79563438e51797ec06bea98eee4f9a92f7db2` | `GFX_018_resource_field_suspended` |
| `gfx/interface/018_resources_found/resource_field_closed.dds` | 128 by 128 | `0c4ac109d47c9c8dfd245d4693a46eb34093691a8180397b04807fa61d1c0ead` | `GFX_018_resource_field_closed` |

## Review outputs

- Five GIF previews: `previews/resource_field_<state>_preview.gif`.
- Five source-and-processed frame contact sheets: `contact_sheets/resource_field_<state>_contact_sheet.png`.
- One compact runtime family review: `contact_sheets/selected_field_ui_runtime_contact_sheet.png`.
- One exact-position panel composite: `contact_sheets/selected_field_ui_live_position_contact_sheet.png`.

## Validation summary

- 56 source frames exist and have 56 unique SHA-256 hashes.
- 56 processed frames exist and have 56 unique SHA-256 hashes.
- All processed frames are 128 by 128 with transparent corners.
- No visible processed pixel matches the chroma-green contamination test.
- Every sheet section is pixel-identical to its corresponding processed frame.
- Every static fallback is pixel-identical to processed frame 000.
- Sheet sizes are exactly 1280 by 128 for the 10-frame families and 1536 by 128 for the 12-frame families.
- GIF frame counts are exactly 10, 10, 12, 12, and 12.
- All thirteen runtime DDS files use 32-bit BGRA masks `00FF0000`, `0000FF00`, `000000FF`, and `FF000000` with no mip chain.
- All thirteen runtime DDS files decode pixel-identically to their processed panel, sheet, fallback, suspended, or closed PNG sources.
- The exact live-position composite confirms a 128 by 128 state medallion fits the registered x 290, y 4 position inside each 438 by 180 active/history selection area; both retain the inspected global x 306, y 86 position.
- Every source and processed frame was inspected through the five contact sheets. The panel, suspended state, closed state, and all seven runtime family appearances were inspected through the two package contact sheets.

## Wiring note

The live GFX file registers all thirteen runtime paths and the correct frame counts and FPS. The live GUI and scripted GUI display and gate Panel, Seal, Unsafe, Disturbance, Breach, Sealing, Suspended, and the presentation-only Closed history state. `GFX_018_resource_field_closed` is consumed by `resources_found_gui_closed_selection` when `resources_found_last_closed_field` carries the exact-seal markers. The parent field-management category accepts the same history trigger, so the record remains reachable after the country's last active field closes. The active gameplay pointer remains separate, so showing this history never makes the sealed state selectable for projects or discovery.

## Simplifications, substitutions, and blockers

No visual simplification, placeholder, fallback substitution, transform-only animation, or alternate runtime filename was used. The five static files are the explicitly required animation fallbacks, not substitutions. There is no asset-production blocker, and the registered closed-state identity has the definitive lifecycle disposition documented above.

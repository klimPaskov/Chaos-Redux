# Event 018 focus icon handoff: Count Every Vein and Chamber Autonomy

Status: complete for the two requested static national-focus icons. No `docs/assets/018_resources_found/` or other event asset workspace was created. Temporary source and processing evidence was kept outside the repository under `%TEMP%\cr018_icons_work\` and the Codex generated-image directory.

## Runtime assets

| Focus | Final DDS | Sprite already registered by the parent | Target GFX |
| --- | --- | --- | --- |
| `DHO_count_every_vein` | `gfx/interface/goals/018_resources_found/goal_DHO_count_every_vein.dds` | `GFX_focus_DHO_count_every_vein` and `GFX_focus_DHO_count_every_vein_shine` | `interface/018_resources_found.gfx` |
| `DHO_chamber_autonomy` | `gfx/interface/goals/018_resources_found/goal_DHO_chamber_autonomy.dds` | `GFX_focus_DHO_chamber_autonomy` and `GFX_focus_DHO_chamber_autonomy_shine` | `interface/018_resources_found.gfx` |

Both textures are native `94x86` RGBA focus icons with transparent corners, matching the existing Event 018 focus surface. The converter output is one-level uncompressed BGRA DDS with a 128-byte legacy header, `DDS_PIXELFORMAT` flags `65`, 32-bit BGRA masks, `DDSCAPS_TEXTURE`, and exact file length `32464` bytes.

## Art and source evidence

Source mode: generated fictional symbolic art using the official built-in ImageGen workflow, followed by the approved chroma-key-to-alpha helper and deterministic native-size processing. The generated source masters were original per focus and were not copied, resized, recoloured, or relabelled from an existing icon.

Canonical reference contact sheet inspected before generation: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png`.

Installed vanilla focus DDS inspected before generation: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/goals/focus_AFG_helmand_river_authority.dds` (`100x88`, RGBA, transparent corners, thick dark outline and compact emblem footprint).

Existing Event 018 focus family inspected from `gfx/interface/goals/018_resources_found/*.dds`, including `goal_DHO_distributed_command.dds`, `goal_DHO_many_chambers.dds`, `goal_DHO_link_the_chambers.dds`, `goal_DHO_mineral_tithe.dds`, `goal_DHO_hoard_the_veins.dds`, and a native-size contact sheet assembled outside the repository. The family's charcoal basalt, restrained brass, amber mineral seams, heavy outline, and full-height 94x86 silhouette were used as style constraints while keeping both motifs new.

`Count Every Vein` uses a severe central carved basalt/brass accounting tablet with distinct counting bars over branching amber mineral veins, expressing strict capacity accounting.

`Chamber Autonomy` uses five visibly separate basalt chambers with independent brood sigils or amber cores and short connecting corridors, expressing distributed regional queues rather than one central hive.

## Processing and QA

The generated source masters were saved by ImageGen as `C:/Users/klimp/.codex/generated_images/019fe6eb-ae03-7312-aa28-2701b8603daa/exec-a4898c98-f1b0-427b-a6b4-fdbd37e2ec1a.png` and `C:/Users/klimp/.codex/generated_images/019fe6eb-ae03-7312-aa28-2701b8603daa/exec-02f2cf43-80c3-4324-b2ae-d268994e2985.png`. Temporary processed previews were `%TEMP%\cr018_icons_work\count_processed.png` and `%TEMP%\cr018_icons_work\autonomy_processed.png` at `94x86` RGBA. Chroma-key validation found no residual green pixels, all four corners are fully transparent, and both outputs retain partially transparent antialiased edges.

Round-trip DDS decoding with Pillow matched each processed PNG exactly at all `94x86` RGBA pixels. Final DDS alpha extrema are `(0,255)`, and decoded visible bounds are `(7,0,87,86)` for Count Every Vein and `(8,0,86,86)` for Chamber Autonomy.

Final SHA-256 hashes:

- `goal_DHO_count_every_vein.dds`: `E90D4810AA4C9E66FB8300CBF3CFE89F709ECD08E43B06F47778A6F5BFA311BE`
- `goal_DHO_chamber_autonomy.dds`: `801F908D519DECAFD6D3EAA67CB3B52B5FC037ACFE658416A6EBAF891DE344F1`

No fallback or simplification was used. No `.gfx`, gameplay, focus, localisation, GUI, spreadsheet, or unrelated asset files were edited by this handoff.

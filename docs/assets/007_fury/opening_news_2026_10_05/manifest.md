# Event 007 Fury Opening World News Image

Status: `complete`.

Asset type: Fictional alternate-history World News scene, not a character portrait.

Consumer: Event `chaosx.news.7008` uses sprite `GFX_news_event_fury_begins` from `interface/007_fury.gfx` and texture `gfx/event_pictures/007_fury/fury_begins.dds`.

Source mode and generation fit: Original scene generated with the official built-in ImageGen tool as fictional alternate-history documentary art. The 1930s railway-yard mobilisation shows arriving reservists, officers forming armed infantry columns, and a modest barracks before the first battle. It uses an unnamed setting without national markers or identifiable people. The full-canvas news consumer requires an opaque black-and-white image, so the generation used `transparent_background=false`; no background removal or sourced material was used.

Generation provenance: Native ImageGen output was returned at `C:\Users\klimp\.codex\generated_images\01a10d45-ab7a-7e20-a650-ad5eead446f3\exec-790a0ba2-5905-4181-b97c-42c19d6b2323.png` and retained unchanged as `source_png/fury_begins_source.png`. The saved generation prompt is [prompts/fury_begins_prompt.md](prompts/fury_begins_prompt.md).

Processing: The original PNG is 2020x778 RGB. The processed preview uses the central-band crop `(1, 0, 2020, 778)`, grayscale conversion, and Lanczos resize to 397x153. The processed PNG is mode `L` and fully opaque. The asset contains no generated lettering, labels, or overlay. See [contact_sheets/fury_begins_contact_sheet.png](contact_sheets/fury_begins_contact_sheet.png) for the source/processed comparison.

DDS conversion and QA: Converted from the processed preview with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. The final DDS is 397x153, one-level uncompressed 32-bit BGRA with the standard 128-byte header and texture caps. File length is 243092 bytes; alpha is 255 throughout. Pillow DDS decode matched the processed PNG pixel-for-pixel in grayscale (`roundtrip_luma_diff_extrema = (0, 0)`). Visual review at 397x153 confirmed readable central mobilisation, continuous full-frame coverage, and no combat aftermath, destruction, flags, readable text, or portrait framing.

Source SHA-256: `8CF6FDD930C0EF28694FC4F9F7D5407971FE7E6C021B6BCD5DF5A0594D3FAB39`.

Processed PNG SHA-256: `21F08A8249C7FC866FDF9AE537E7E9D0CEC97702FBF39E35EE7AC9D79DD286C1`.

Final DDS SHA-256: `082BC5C16229BC34821101D386953FB7973108A87FA5F0FE0D990ED05734873B`.

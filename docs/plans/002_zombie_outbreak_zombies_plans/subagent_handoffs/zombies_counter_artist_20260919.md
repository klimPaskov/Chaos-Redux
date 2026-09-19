# Zombie counter artist handoff — 2026-09-19

Status: `needs_user_review`.

Asset id: `chaosx.event002.zombies`.

Owner token: `002_zombie_outbreak`.

This handoff covers only the bespoke 2D large division counter and small land map counter for the ordinary Chaos Redux base zombie. It does not claim gameplay, entity, `.asset`, `.gfx`, or live-game completion.

## Selected deliverables

Large staged DDS: `docs/assets/002_zombie_outbreak/models_3d/zombies/counter/runtime_gfx/interface/counters/divisions_large/zombies_icon.dds`.

Small staged DDS: `docs/assets/002_zombie_outbreak/models_3d/zombies/counter/runtime_gfx/interface/counters/divisions_small/onmap_unit_zombies_icon.dds`.

Processed PNG previews:

- `docs/assets/002_zombie_outbreak/models_3d/zombies/counter/processed_png/zombies_icon.png` — RGBA 152x42, two adjacent 76x42 frames.
- `docs/assets/002_zombie_outbreak/models_3d/zombies/counter/processed_png/onmap_unit_zombies_icon.png` — RGBA 60x12, two adjacent 30x12 frames.

The final selected art is original ImageGen output processed into the exact inspected Vanilla canvas and frame geometry. Frame 0 is the normal state and frame 1 is the separate sparse alternate/template state.

## Exact runtime consumers and parent wiring

The parent supplied and owns these existing sprite tokens in `interface/chaosx_subuniticons.gfx`:

```text
GFX_unit_zombies_icon_medium -> gfx/interface/counters/divisions_large/zombies_icon.dds, noOfFrames = 2
GFX_unit_zombies_icon_medium_white -> gfx/interface/counters/divisions_small/onmap_unit_zombies_icon.dds, noOfFrames = 2
```

The parent must promote or copy the staged DDS files to those exact runtime paths and retain those exact sprite names. This worker did not edit `interface/chaosx_subuniticons.gfx`.

## Installed Vanilla inspection evidence

Installed definition inspected before generation:

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/subuniticons.gfx`.

Large precedent:

`GFX_unit_infantry_icon_medium` uses `gfx/interface/counters/divisions_large/unit_infantry_icon.dds` with `noOfFrames = 2`.

Small precedent:

`GFX_unit_infantry_icon_medium_white` uses `gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds` with `noOfFrames = 2`.

Installed large reference DDS:

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_large/unit_infantry_icon.dds`.

SHA-256: `b33a8e3b69cc789eb0e31ba99f4e5ba4e5b0a8b51ec1a7a7f709c3516f720c23`.

Bytes: `25664`.

Decoded dimensions: `152x42`.

Frame geometry: two adjacent `76x42` frames.

Pixel format: uncompressed 32-bit BGRA, DDS header size 124, pixel-format flags 65, fourCC 0, masks R `0x00ff0000`, G `0x0000ff00`, B `0x000000ff`, A `0xff000000`, texture caps `0x1000`.

Frame 0 alpha bbox: `(21,9,53,35)`.

Dominant sampled green: RGB `(73,106,73)`.

Sampled green range among opaque green-dominant pixels: R `7..212`, G `12..221`, B `7..212`.

Installed small reference DDS:

`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/counters/divisions_small/onmap_unit_infantry_icon.dds`.

SHA-256: `58ab78662c2a64a519b8d5d144582e7b2785915bd0a0a822696d87a9de6f766c`.

Bytes: `3008`.

Decoded dimensions: `60x12`.

Frame geometry: two adjacent `30x12` frames.

Pixel format: uncompressed 32-bit BGRA with the same strict legacy header layout.

The small installed family is neutral gray/white; no green-dominant pixels were found in the canonical small infantry frame.

Canonical review-only families inspected before generation:

- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/counters_large/contact_sheet.png`.
- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/units/land/map_counters/contact_sheet.png`.
- `.../units/land/counters_large/unit_infantry_icon.png`, 152x42, SHA-256 `caf241717af26ca1688742a86be1a8a89c5a9b8caba41410b4cf799827ad1972`.
- `.../units/land/map_counters/onmap_infantry.png`, 60x12, SHA-256 `5a6274e5847cbe9d030b547b9c2bb723215269b234bef227a43f273b22dc42b9`.

Copied review-only sheets and an installed-definition snippet are retained under `docs/assets/002_zombie_outbreak/models_3d/zombies/counter/reference_evidence/`.

## Source provenance and exact prompts

Official built-in ImageGen was used for all generated candidates. Every initial call requested a genuinely transparent background. Image 1 was the approved Blender render at `C:/Users/klimp/.codex/visualizations/2026/09/19/01a0ba60-d7e2-7190-a254-8e3fb7215eb9/model_inventory_renders/units__chaosx_zombies__chaosx_zombies_front.png`, SHA-256 `8d8c118d94f0e17935607c5e0bdfee852fa27037cef1050a6bf4f0de7b8fba80`, 720x720 RGBA. Image 2 was the approved model input at `docs/assets/002_zombie_outbreak/models_3d/zombies/refs/original/meshy_input.png`, SHA-256 `3f9e12f20c4d9e5533ccc3af7a59a8c994bc77c3c77801f9ba17743edf796f8b`, 1024x1536 RGB.

Exact prompts and full candidate lineage are retained in `docs/assets/002_zombie_outbreak/models_3d/zombies/counter/prompts/zombies_counter_prompts.md`.

Selected normal large source:

- Tool output: `C:/Users/klimp/.codex/generated_images/01a0ba8d-7a95-7e20-8ebc-82a331d3eec4/exec-cb6a553d-7e46-4bf7-ac6b-f8b1b9905b0f.png`.
- Retained source: `source_png/zombies_large_normal_source_v2.png`.
- SHA-256: `19c57e2b675c58ef389794f5304285594a17859b58e35a88c78c0fa06280849e`.
- Decoded source: 1688x932 RGBA, alpha 0..255, alpha bbox `(249,31,1383,904)`.
- Prompt emphasis: approved zombie identity, wide low crouched pose, both arms spread and bent upward, source aspect about 1.1–1.4, sampled Vanilla green anchor, native transparency, no text/weapons/background.

Selected alternate large source:

- Tool output: `C:/Users/klimp/.codex/generated_images/01a0ba8d-7a95-7e20-8ebc-82a331d3eec4/exec-0fefe4a4-b5a4-4fe4-b47a-1b695059473a.png`.
- Retained source: `source_png/zombies_large_alt_source_v2.png`.
- SHA-256: `06ca2fa0edbcbddbd339f49bdee838fca7fc7b3dea0f5eb6aa2d76ff15a409c0`.
- Decoded source: 1686x933 RGBA, alpha 0..255, alpha bbox `(457,120,1335,901)`.
- Prompt emphasis: separate sparse pale schematic state with broad silhouette planes, charcoal contour, no face/texture/gradient, transparent unused canvas, no detailed repaint.

Selected normal small source:

- Tool output: `C:/Users/klimp/.codex/generated_images/01a0ba8d-7a95-7e20-8ebc-82a331d3eec4/exec-accebe39-06d6-4ec0-8508-5ab6b10f8803.png`.
- Retained source: `source_png/zombies_small_normal_source_v2.png`.
- SHA-256: `9a7506c03e87d41031de67002d12e000603540e59fb8c9479ed2d76f98c81dbb`.
- Decoded source: 1983x793 RGBA, alpha 0..255, alpha bbox `(275,28,1566,771)`.
- Prompt emphasis: wide low map-counter pose with arms spread, pale gray/white family, 30x12 readability, native transparency, no green/opaque background.

Selected alternate small source:

- Tool output: `C:/Users/klimp/.codex/generated_images/01a0ba8d-7a95-7e20-8ebc-82a331d3eec4/exec-083ce042-d37b-4aa9-85bd-32a0fd8def0d.png`.
- Retained source: `source_png/zombies_small_alt_source_v2.png`.
- SHA-256: `b888f5da2cad4feddfe2ea3a7d5b4858bc8b11f0bbdcab0255e7bd0209e2c21c`.
- Decoded source: 1774x887 RGBA, alpha 0..255, alpha bbox `(259,166,1526,855)`.
- Prompt emphasis: very wide low schematic glyph, approximately 2:1 footprint, pale gray/white and charcoal only, sparse alternate state, native transparency.

Superseded and rejected candidates remain immutable for lineage:

- `source_png/zombies_large_normal_source_v1.png`, SHA-256 `6d622bc026771740cbc715cb8651de1bb4f95031d83316d381a6734fcfbdc381`; native alpha passed, but the high-confidence silhouette was too narrow for the large frame.
- `source_png/zombies_small_normal_source_v1.png`, SHA-256 `51601b7da2cbc5d35583d9b944d22300cad0a64c16ae7fb29a92ab1165ef46b0`; native alpha passed, but the crop was too vertical for the 30x12 map frame.
- `source_png/zombies_small_alt_source_v1.png`, SHA-256 `ba735aeccf3ed76eaced62f3bab96957a0c42f0fc858e856676a83e1e6577031`; native alpha passed, but the crop was too vertical for the 30x12 map frame.
- `source_png/zombies_large_alt_source_v1_rejected_detailed.png`, SHA-256 `84f0e3ade939f4b50a25339e56644fbb9be77971b2f01a343611e57616255e5e`; rejected because it was a detailed full-color repaint rather than a sparse alternate schematic.

## Processing and alpha evidence

The large normal source was cropped using an alpha threshold of 8 with 2 source pixels of padding, resized with Lanczos, centered in a 76x42 frame, and palette-matched to sampled green pixels from the canonical large infantry frame. Dark generated charcoal contours with maximum channel below 40 were retained. The alternate large source was independently cropped, resized with Lanczos, and centered without recoloring.

The two small sources were independently cropped, resized with Lanczos, centered in 30x12 frames, and luma-mapped to exact neutral grayscale values sampled from the canonical `onmap_infantry.png` family. No background removal fallback was used.

All final assets have alpha minimum 0 and maximum 255, transparent unused canvas, and no fake checkerboard or opaque matte. The processed and decoded DDS alpha bboxes are:

- Large strip `(19,4,127,37)`; frame 0 `(19,4,57,37)`; frame 1 `(25,6,51,36)`.
- Small strip `(6,0,56,12)`; frame 0 `(6,0,24,12)`; frame 1 `(3,0,26,12)`.

The final small opaque pixels are neutral grayscale after processing. The final large normal frame uses only sampled Vanilla green palette values for its generated interior, with the sampled anchor RGB `(73,106,73)` retained in the palette.

## Final hashes and strict DDS results

Large processed PNG: `processed_png/zombies_icon.png`, 152x42 RGBA, SHA-256 `89099b72c10b4f7e3424e2b6c5a0d0d816ad12b393ff27e7072a788529682114`.

Large final DDS: `runtime_gfx/interface/counters/divisions_large/zombies_icon.dds`, 25,664 bytes, 152x42, SHA-256 `30c89417d33cfbaa3262fe58814a300f4d3f704f99011779ab138cf3ada23046`, strict uncompressed BGRA header pass, alpha 0..255.

Small processed PNG: `processed_png/onmap_unit_zombies_icon.png`, 60x12 RGBA, SHA-256 `230b3df60079a45cd9e8ed4d5bbb0408f4fcd26e73dffd2635d2d354be848189`.

Small final DDS: `runtime_gfx/interface/counters/divisions_small/onmap_unit_zombies_icon.dds`, 3,008 bytes, 60x12, SHA-256 `280b37f245714c9eb76fbd66518c02fc4aafa017108db88897365dcadf39172e`, strict uncompressed BGRA header pass, alpha 0..255.

The DDS decoder round-trips are pixel-identical to the processed PNGs. Evidence is in `validation/dds_header_validation.json`, `validation/decoded_large_dds_roundtrip.png`, `validation/decoded_small_dds_roundtrip.png`, and `validation/file_hashes.json`.

## Visual QA and remaining parent work

Review contact sheet: `docs/assets/002_zombie_outbreak/models_3d/zombies/counter/contact_sheets/zombies_counter_qa.png`.

The sheet shows the canonical Vanilla review references, native-alpha sources, processed strips with frame labels, native-size enlarged views, smooth previews, and DDS round-trips.

Remaining parent work is to review the sheet, promote the staged DDS files to the exact `gfx/interface/counters/...` targets, verify the existing sprite tokens and consumer registration, and complete live-game validation.

No gameplay files, localisation, GUI, entities, sound definitions, events, focuses, decisions, country/history/AI, on_actions, spreadsheets, or parent `.gfx` files were edited by this worker.

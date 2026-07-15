# Event 006 live AFX/AGX portrait regeneration manifest

## Scope

This self-contained tranche replaces only the four generated AFX/AGX portrait
masters and their existing runtime derivatives:

- AFX Walloon Provisional Assembly;
- AFX Marcel Delcourt, reserve commander;
- AGX Friesland Coastal Council;
- AGX Sjoerd Hoekstra, coastal commander;
- the existing 50×67 army thumbnails for Delcourt and Hoekstra.

No gameplay, localisation, character, tag, specification, `.gfx`, `.gui`, flag,
advisor, or other-event file was edited. The runtime filenames and sprite names
remain unchanged.

## Source and style control

All four masters are original fictional artwork generated through four separate
calls to the official OpenAI Codex built-in `image_gen` tool. No source master
is shared, no face is reused, and no real or recognisable historical person is
depicted. Exact prompts and generation provenance are recorded in
`prompts.md` and `imagegen_provenance.json`.

Before generation and processing, the canonical vanilla leader references in
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`
and `contact_sheets/portraits_and_flags.png` were inspected. The source masters
were then finished with `.tools/process_hoi4_portrait.py` version 1.1 and
explicit full-canvas crops. The four per-asset comparison sheets show the
source crop, processed candidate, and two canonical vanilla references.

## Asset records

### AFX — Walloon Provisional Assembly

- Asset type: fictional collective country-leader portrait.
- Identity: exactly three tightly clustered delegates; one focal municipal
  magistrate with subordinate mineworker and steel engineer.
- Gender/name handling: institutional body; do not assign an individual gender
  flag, biography, or personal name pool.
- Source: `source_png/generated_nwe/institutional_portraits/portrait_AFX_walloon_provisional_assembly_source.png` (`1080×1456`).
- Explicit crop: `[0, 0, 1080, 1456]`.
- Processed PNG: `processed_png/generated_nwe/institutional_portraits/portrait_AFX_walloon_provisional_assembly.png` (`156×210`).
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_AFX_walloon_provisional_assembly.dds` (`156×210`).
- DDS decode: `dds_decoded_png/generated_nwe/institutional_portraits/portrait_AFX_walloon_provisional_assembly.png`.
- Sprite: `GFX_portrait_AFX_walloon_provisional_assembly` in `interface/006_independence_wave_region_01_portraits.gfx`.
- Comparison: `comparisons/portrait_AFX_walloon_provisional_assembly_source_final_canonical.png`.
- Status: complete and visually approved.

### AFX — Marcel Delcourt

- Asset type: fictional male-presenting commander and country-leader portrait.
- Identity: weathered Walloon industrial-valley reserve organiser; dark wavy
  hair greying at the temples, angular face, grey-green field coat, burgundy
  scarf; no regular-army celebrity styling.
- Source: `source_png/generated_nwe/command_portraits/portrait_AFX_walloon_reserve_commander_source.png` (`1081×1455`).
- Explicit large crop: `[0, 0, 1081, 1455]`.
- Processed PNG: `processed_png/generated_nwe/command_portraits/portrait_AFX_walloon_reserve_commander.png` (`156×210`).
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` (`156×210`).
- Army-thumbnail derivation: crop `[0, 0, 156, 209]` from the approved large
  processed portrait, then Lanczos resize to `50×67`.
- Army-thumbnail PNG/DDS: `processed_png/generated_nwe/command_portraits_small/portrait_AFX_walloon_reserve_commander_small.png`; `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander_small.dds`.
- Sprites: `GFX_portrait_AFX_walloon_reserve_commander` and `GFX_portrait_AFX_walloon_reserve_commander_small` in `interface/006_independence_wave_region_01_portraits.gfx`.
- Comparison: `comparisons/portrait_AFX_walloon_reserve_commander_source_final_canonical.png`; thumbnail review at `comparisons/portrait_AFX_walloon_reserve_commander_small_nearest_6x.png`.
- Thumbnail role: army portrait only; it is not an advisor or high-command
  dossier icon and has no advisor frame.
- Status: complete and visually approved at `156×210`, native `50×67`, and 6× nearest-neighbour review size.

### AGX — Friesland Coastal Council

- Asset type: fictional collective country-leader portrait.
- Identity: exactly three tightly clustered delegates; one focal female
  municipal water-board chair with subordinate harbor master and dike engineer.
- Gender/name handling: institutional body; do not assign an individual gender
  flag, biography, or personal name pool.
- Source: `source_png/generated_nwe/institutional_portraits/portrait_AGX_friesland_coastal_council_source.png` (`1080×1456`).
- Explicit crop: `[0, 0, 1080, 1456]`.
- Processed PNG: `processed_png/generated_nwe/institutional_portraits/portrait_AGX_friesland_coastal_council.png` (`156×210`).
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_council.dds` (`156×210`).
- DDS decode: `dds_decoded_png/generated_nwe/institutional_portraits/portrait_AGX_friesland_coastal_council.png`.
- Sprite: `GFX_portrait_AGX_friesland_coastal_council` in `interface/006_independence_wave_region_01_portraits.gfx`.
- Comparison: `comparisons/portrait_AGX_friesland_coastal_council_source_final_canonical.png`.
- Status: complete and visually approved.

### AGX — Sjoerd Hoekstra

- Asset type: fictional male-presenting commander and country-leader portrait.
- Identity: fair-haired Frisian dike-and-harbor constabulary officer; narrow
  face, blue-grey eyes, eyebrow scar, navy weather coat and knit sweater;
  deliberately distinct from Delcourt and all council delegates.
- Source: `source_png/generated_nwe/command_portraits/portrait_AGX_friesland_coastal_commander_source.png` (`1080×1456`).
- Explicit large crop: `[0, 0, 1080, 1456]`.
- Processed PNG: `processed_png/generated_nwe/command_portraits/portrait_AGX_friesland_coastal_commander.png` (`156×210`).
- Runtime DDS: `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander.dds` (`156×210`).
- Army-thumbnail derivation: crop `[0, 0, 156, 209]` from the approved large
  processed portrait, then Lanczos resize to `50×67`.
- Army-thumbnail PNG/DDS: `processed_png/generated_nwe/command_portraits_small/portrait_AGX_friesland_coastal_commander_small.png`; `gfx/leaders/006_independence_wave/portrait_AGX_friesland_coastal_commander_small.dds`.
- Sprites: `GFX_portrait_AGX_friesland_coastal_commander` and `GFX_portrait_AGX_friesland_coastal_commander_small` in `interface/006_independence_wave_region_01_portraits.gfx`.
- Comparison: `comparisons/portrait_AGX_friesland_coastal_commander_source_final_canonical.png`; thumbnail review at `comparisons/portrait_AGX_friesland_coastal_commander_small_nearest_6x.png`.
- Thumbnail role: army portrait only; it is not an advisor or high-command
  dossier icon and has no advisor frame.
- Status: complete and visually approved at `156×210`, native `50×67`, and 6× nearest-neighbour review size.

## DDS conversion and review

All six final DDS files were produced with the required
`.tools/convert_to_dds.py` command. In this environment the converter selected
its ffmpeg raw-BGRA path and wrote the same canonical legacy DDS header used by
its `write_bgra_dds` implementation. Every file is a one-level, uncompressed
32-bit BGRA texture with `DDSCAPS_TEXTURE`, no FourCC, correct channel masks,
and opaque alpha.

`validation.json` records every header field, exact file length, alpha range,
and raw-pixel SHA-256 comparison. Each DDS raw-pixel hash is identical to its
processed PNG raw-pixel hash. The contact sheet at
`contact_sheets/afx_agx_live_portraits_final_dds_contact_sheet.png` shows the
actual decoded runtime DDS files, including native and 6× views of both army
thumbnails.

## Wiring preservation

The existing six sprite definitions and character references were rechecked.
They still point to the same runtime filenames listed above. No `.gfx` or
character edit was necessary.

## Simplifications, omissions, and blockers

None. No fallback art, placeholder, reused face, photorealistic substitute,
advisor icon, new character, renamed sprite, or reduced asset was introduced.
There are no remaining blockers in this bounded portrait tranche.

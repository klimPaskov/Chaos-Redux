# Visual validation notes

Date: 2026-07-22

## Reference analysis

- Vanilla special-project picture placeholder: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/interface/special_project/PLACEHOLDER_UI/PLACEHOLDER_sp_project_picture.dds`.
  - Native canvas: `198x218`.
  - Legacy one-level uncompressed BGRA DDS, `32` bits per pixel, transparent outer corners, clipped paper-card treatment.
- Vanilla special-project project-icon references in `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/special_projects/` are `161x98`; they are a separate project-icon surface and were not used as reward-card source art.
- Existing Chaos Redux `gfx/interface/special_project/project_icons/sp_*_bomb.dds` assets are also `161x98` project icons and remain untouched.
- Existing `.gfx` organization inspected: `interface/special_projects/biowarfare.gfx` contains the Chaos Redux special-project sprite family. It was not edited in this package.
- Review aids: `contact_sheets/source_keyed_contact_sheet.png`, `contact_sheets/processed_checker_contact_sheet.png`, and `contact_sheets/final_dds_contact_sheet.png`.

## Source and processing review

- All eleven retained assets are independent built-in ImageGen outputs; no master image was resized, cropped, filtered, recolored, or relabeled to satisfy another id.
- Every source was generated as its own clipped vertical dossier card on a flat `#00ff00` key background and retained under `source_png/`.
- Each source was keyed with the official ImageGen chroma-removal helper, then cropped to its own alpha subject bounds, resized to an inner `194x214` footprint, and placed at `(2,2)` on an exact `198x218` transparent RGBA canvas.
- The final cards retain transparent outer corners, a slight dark card edge/shadow authored in the source art, and a readable central subject at runtime size.
- Three single-pixel alpha-1 chroma residues were removed from processed edge pixels before reconversion; no visible green key pixels remain.
- No final art contains generated text, labels, logos, watermark, pathogen depiction, culture imagery, biological procedure, gore, victim, dispersal instruction, or operational detail.

## DDS validation

`dds_validation.json` records the per-file checks. Every retained DDS passed:

- exact `198x218` dimensions;
- exact `172784` byte length (`128 + 198*218*4`);
- legacy DDS header with `DDS ` magic, `DDS_HEADER` size `124`, `DDS_PIXELFORMAT` size `32`, flags `65`, zero FourCC, 32-bit BGRA masks, and `DDSCAPS_TEXTURE`;
- alpha minimum `0` and maximum `255` with transparent corners;
- zero remaining chroma-key pixels;
- exact RGBA decode equality between the processed PNG and final DDS payload.

## Package status

All eleven requested icons are `complete` and ready for main-agent `.gfx` wiring. No gameplay, localisation, raid art, existing Chaos Redux icon, or `.gfx` file was edited by this package.

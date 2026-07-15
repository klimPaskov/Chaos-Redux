# Event 014 Wendigo Focus Icon Validation

## Coverage

- Focus IDs in `common/national_focus/014_cannibalism_focus.txt`: 28 unique Wendigo overlay focuses.
- Unique registered Wendigo texture paths in `interface/014_cannibalism.gfx`: 28.
- Accepted imagegen source PNGs: 28.
- Alpha-master PNGs: 28.
- Processed 94 by 86 PNGs: 28.
- Final 94 by 86 DDS files: 28.
- Missing, extra, or misnamed registered paths: none.

## DDS format and decoded-pixel check

Every final DDS has:

- `DDS ` magic and a 124-byte DDS header
- 94 by 86 dimensions
- 376-byte row pitch
- 32-bit RGB plus alpha pixel format
- red, green, blue, and alpha masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, and `0xFF000000`
- one uncompressed BGRA/B8G8R8A8-style image and a 32,464-byte total file size
- a decoded RGBA buffer that is pixel-identical to the matching processed PNG

## Transparency and chroma check

- All four corners of every alpha master are fully transparent.
- No visible alpha-master pixel retained the #ff00ff key or a magenta fringe under the residual-key test.
- Final transparent-pixel counts range from 1,882 to 3,040 pixels per 94 by 86 icon.
- Final partially transparent edge-pixel counts range from 1,304 to 2,356.
- Every icon contains both fully transparent unused canvas and fully opaque painted subject pixels.
- Checkerboard review confirms no opaque square background, fake transparency, white matte, or colored key fringe.

## Uniqueness

- 28 unique source SHA-256 hashes.
- 28 unique processed PNG SHA-256 hashes.
- 28 unique decoded-pixel SHA-256 hashes.
- 28 unique DDS SHA-256 hashes.
- 28 unique 256-bit perceptual difference hashes.
- Nearest-neighbor dHash Hamming distances range from 73 to 103 bits out of 256, so no two final icons are perceptual duplicates or light transform variants.

Full hashes and per-icon statistics are recorded in `../manifest.md` and `../validation/wendigo_focus_icons_validation.tsv`.

## Final-size visual review

The actual-size processed and decoded-DDS contact sheets were reviewed directly. All 28 silhouettes remain readable at 94 by 86. The set has distinct visual anchors for the merge trunk, winter warfare, Pack recruitment, cannibal inheritance, transformation countdown, and terminal hunt. Neutral-background luminance standard deviation ranges from 34.18 to 56.52, retaining useful value contrast at game size.

The accepted source, processed, and decoded-DDS contact sheets are:

- `../contact_sheets/wendigo_focus_source_contact_sheet.png`
- `../contact_sheets/wendigo_focus_final_contact_sheet.png`
- `../contact_sheets/wendigo_focus_dds_decoded_contact_sheet.png`

## Cultural and content review

The accepted set uses fictional military, industrial, winter, bone, chain, blood, road, rail, ledger, pack, and transformation-pylon imagery. It contains no antlers, deer skull focal emblems, dreamcatchers, totem poles, headdresses, medicine wheels, sacred objects, tribal runes, ceremonial regalia, or insignia borrowed from living Indigenous traditions. It contains no readable text, logo, real-world political insignia, identifiable real victim, stock icon, or reused art.

The first Warlord Captains generation was rejected because a cap badge could be read as historical military insignia. The accepted source is a separate corrected generation with plain improvised helmets.

## Scope boundary

This tranche changed only source/processed asset files, exact final DDS files, contact sheets, prompts, manifest, validation, and handoff documentation. It did not edit gameplay, localisation, GFX, GUI, audio, spreadsheet, catalog, or other event implementation files.

No fallback or simplification was used.

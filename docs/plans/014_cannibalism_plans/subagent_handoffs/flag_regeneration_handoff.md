# Event 014 Flag Regeneration Handoff

## Scope completed

Regenerated every live Event 014 Cannibalism flag as a distinct built-in-imagegen design and replaced its normal, medium, and small runtime TGA while preserving all existing filenames.

- Families: `CBA`, `CBB`, `CBC`, `CBD`, `CBE`, `CBF`, `CBG`, `CBH`, `CBL`, `CBL_CENTRAL_COMMAND`, `CBL_HOST_CONFEDERATION`, `CBL_RITUAL_STATE`, `ZZZ_CANNIBALISM_HANNIBAL`
- Variants per family: base, `_communism`, `_democratic`, `_fascism`, `_neutrality`
- Distinct generated designs: 65
- Runtime TGA outputs: 195
- Deliberately excluded and untouched: `ZZZ_weaponized_wendigo`

No gameplay, localisation, interface, spreadsheet, or source-specification files were edited.

## Files and artifacts

- Canonical package: `docs/assets/014_cannibalism/flags_refresh/`
  - `prompts/prompt_specs.json`
  - 65 exact per-design prompt files under `prompts/`
  - 65 retained imagegen masters under `source_png/`
  - 65 flattened 82x52 runtime masters under `processed_png/`
  - `contact_sheets/source_masters_contact_sheet.png`
  - `contact_sheets/final_runtime_flags_contact_sheet.png`
  - `contact_sheets/source_vs_final_contact_sheet.png`
  - `manifest.md`, with one complete provenance entry per design
  - `notes/process_flags.py`, the deterministic crop, flatten, export, sheet, and manifest builder
- Runtime replacements:
  - 65 normal TGAs under `gfx/flags/`
  - 65 medium TGAs under `gfx/flags/medium/`
  - 65 small TGAs under `gfx/flags/small/`

The manifest is the exact per-file inventory. Each entry records the Event 014 use, source mode `imagegen`, exact final prompt, source and processed paths, all three final TGA paths, dimensions, palette size, processed hash, and completion status.

## Processing decisions

- Each design came from its own imagegen call and source PNG; no ideology design is a filtered, flipped, or recolored derivative.
- Source masters remain unmodified for provenance.
- Runtime masters use a centered 82:52 crop and no-dither four-color flattening to remove source gradients, vignettes, and soft shadows while preserving generated geometry.
- Medium and small assets derive from the corresponding flattened normal master and are remapped to that same palette.
- `CBL_CENTRAL_COMMAND_communism` uses maximum-coverage palette selection because median-cut dropped its small emblem. Small disconnected red quantization islands were then removed.
- Comparable isolated gray quantization pixels were removed from `CBG_democratic` before rebuilding all three sizes and contact sheets.
- TGAs are written as uncompressed 32-bit BGRA with descriptor byte `8`; the top-origin bit is unset, so pixel data is bottom-origin.

## Validation evidence

- Inventory: 65 prompt files, 65 source PNGs, 65 processed PNGs, and 195 runtime TGAs.
- Dimensions: every processed/normal asset is 82x52, every medium asset is 41x26, and every small asset is 10x7.
- Palette: every processed and runtime asset has exactly four fully opaque flat colors, within the required two-to-four-color range.
- Distinctness: all 65 processed PNG hashes are unique and all 65 normal TGA hashes are unique.
- TGA inspection: all 195 headers are uncompressed true-color, 32-bit, with zero x/y origins and descriptor `8`; every alpha byte is 255.
- Origin proof: all 65 decoded normal TGAs match their processed PNG pixel-for-pixel when interpreted bottom-first.
- `file` inspection: all 195 report the expected RGBA dimensions and 8-bit alpha; zero outputs contain `- top`.
- Visual proof: source-only, final-runtime, and source-versus-final contact sheets show all 65 labeled normal designs. Labels are outside the artwork.
- `ZZZ_weaponized_wendigo` does not appear in the generated manifest or output list and was not modified.

## Simplifications, omissions, and blockers

None. All requested families, variants, sizes, source artifacts, prompts, provenance records, contact sheets, and runtime files are present. No fallback asset was used.

## Skills used

- `chaos-redux-event-assets`
- `imagegen`

No skill was created or updated. No commit was created; the parent agent retains final review and commit ownership.

# Event 014 Cannibalism Flag Asset Package Handoff

## Outcome

The frozen Event 014 flag ledger is fully implemented as an asset-only package.

- 13 families complete.
- 5 genuinely distinct image-generated compositions per family.
- 65 selected high-resolution source crops.
- 195 processed PNG previews.
- 195 live HOI4 TGA files.
- 65 standard files at 82x52.
- 65 medium files at 41x26.
- 65 small files at 10x7.
- 13 obsolete `CBL_LAST_TABLE` live remnants removed after the current 195-file set passed validation.
- Existing Wendigo base/neutrality flags preserved byte-for-byte.

No gameplay, localisation, `.gfx`, GUI, country, history, decision, focus, scripted effect, scripted trigger, on-action, or spreadsheet file was edited.

## Implemented identifiers

Each family has base, `_communism`, `_democratic`, `_fascism`, and `_neutrality` files at all three engine sizes:

- `CBA`
- `CBB`
- `CBC`
- `CBD`
- `CBE`
- `CBF`
- `CBG`
- `CBH`
- `CBL`
- `CBL_CENTRAL_COMMAND`
- `CBL_HOST_CONFEDERATION`
- `CBL_RITUAL_STATE`
- `ZZZ_CANNIBALISM_HANNIBAL`

The exact 65 composition rows and 195 live paths are in:

`docs/assets/014_cannibalism/flags_imagegen/asset_manifest.tsv`

## Files created or updated

### Asset package

- `docs/assets/014_cannibalism/flags_imagegen/manifest.md`
- `docs/assets/014_cannibalism/flags_imagegen/asset_manifest.tsv`
- `docs/assets/014_cannibalism/flags_imagegen/process_event014_flags.py`
- `docs/assets/014_cannibalism/flags_imagegen/prompts/imagegen_prompt_ledger.md`
- 13 files under `docs/assets/014_cannibalism/flags_imagegen/source_sheets/`
- 65 files under `docs/assets/014_cannibalism/flags_imagegen/source_crops/`
- 195 files under `docs/assets/014_cannibalism/flags_imagegen/processed_png/`
- 4 files under `docs/assets/014_cannibalism/flags_imagegen/contact_sheets/`
- `docs/assets/014_cannibalism/flags_imagegen/validation/tga_validation.tsv`
- `docs/assets/014_cannibalism/flags_imagegen/validation/rgba_uniqueness.tsv`
- `docs/assets/014_cannibalism/flags_imagegen/validation/processing_summary.json`
- `docs/assets/014_cannibalism/flags_imagegen/validation/sha256sums.tsv`
- `docs/assets/014_cannibalism/flags_imagegen/validation/validation_report.md`

### Live flags

- 65 current TGA files in `gfx/flags/`
- 65 current TGA files in `gfx/flags/medium/`
- 65 current TGA files in `gfx/flags/small/`

### Documentation index

- `docs/assets/014_cannibalism/manifest.md` now links the frozen flag package and names all three live flag folders.

### Handoff

- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_flag_asset_package_2026-07-12.md`

## Removed live files

The following obsolete pattern was removed only from the three live flag folders:

- `gfx/flags/CBL_LAST_TABLE{,_communism,_democratic,_fascism,_neutrality}.tga`
- `gfx/flags/medium/CBL_LAST_TABLE{,_communism,_democratic,_fascism,_neutrality}.tga`
- `gfx/flags/small/CBL_LAST_TABLE{,_communism,_democratic,_fascism,_neutrality}.tga`

Only 13 of the possible 15 paths existed at the cleanup gate: three standard files and all ten medium/small files. All 13 were removed. The final live scan found zero obsolete files. Historical source and processed documentation outside the live folders was preserved.

## Before and after

Before this package, CBA-CBH and the three current CBL cosmetic identities had no complete live five-variant/three-size coverage; CBL itself was incomplete across the three folders; the explicit public Hannibal cosmetic family did not exist; and 13 obsolete `CBL_LAST_TABLE` live files remained.

After this package, every frozen family has complete base plus ideology coverage at each engine size. The generated compositions differ in subject arrangement and command language, rather than color alone. The obsolete runtime identity is absent.

## Image generation and selection

All 13 selected source sheets were generated with the built-in `image_gen` tool. Each sheet contains five separately composed flag artworks and one blank review cell. The selected cells map in order to base, communism, democratic, fascism, and neutrality.

The first CBL generation was rejected because its route geometry could be read as a real national cross. It was not copied into the package. The retained CBL replacement uses asymmetric route networks, an empty table, no weapon, no map outline, and no national or sacred form.

The complete selected generation IDs, source-sheet hashes, shared restrictions, and family-specific prompt blocks are recorded in:

`docs/assets/014_cannibalism/flags_imagegen/prompts/imagegen_prompt_ledger.md`

## Content review

The selected sheets and TGA-decoded contact sheets were reviewed visually.

- No real people, recognizable people, or real victims appear.
- No readable text, labels, numbers, or generated slogans appear.
- No real political emblem, extremist insignia, national coat of arms, or recognizable national symbol appears.
- No Indigenous regalia, sacred motif, tribal symbol, antlered figure, headdress, mask, totem, feather, or rune appears.
- The Hannibal family uses only a frost-cracked animal jaw, frozen chain, ruined road, and dark-red ice.
- Each family has five different layouts and object relationships.

## Validation evidence

### Counts

- Expected current live TGAs: 195.
- Present current live TGAs: 195.
- Missing: 0.
- Standard: 65.
- Medium: 65.
- Small: 65.
- Source sheets: 13.
- Source crops: 65.
- Processed PNGs: 195.
- TGA-decoded contact sheets: 4.
- Manifest rows: 65.
- Hash inventory rows: 474.

### TGA contract

- 195/195 image type 2, uncompressed true-color.
- 195/195 32 bpp.
- 195/195 descriptor `0x08`.
- 195/195 bottom-left origin.
- 195/195 8-bit alpha declaration.
- 195/195 opaque alpha with minimum and maximum 255.
- 195/195 exact uncompressed file length.
- 195/195 decode to the exact RGBA pixels and orientation of their processed PNG.
- GNU `file`: 195 Targa rows, zero non-Targa rows, zero `- top` rows.

### Uniqueness

- Source crops: 65 assets, 65 unique orientation-normalized RGBA digests.
- Standard TGAs: 65 assets, 65 unique normalized RGBA digests.
- Medium TGAs: 65 assets, 65 unique normalized RGBA digests.
- Small TGAs: 65 assets, 65 unique normalized RGBA digests.
- Duplicate groups: 0.

### Protected Wendigo hashes

- Standard base and neutrality: `670BC991820B8ECC904000472E1324B47E087F6E920E1FA0FFD1B32286FAD41D`
- Medium base and neutrality: `8A89271075C90B4773BE973DB3B0BC233DE418B80B370EC7E58812F3DD179207`
- Small base and neutrality: `53EDCA39CCECE9812C1FAF1C60DC95236435DF8A38B28673B4B0ABC0BAAAF195`
- Before/after mismatch count: 0 of 6.

Full per-file evidence is under:

`docs/assets/014_cannibalism/flags_imagegen/validation/`

## Reference review

The required offline wiki core pages plus Country creation, Cosmetic tag modding, Localisation, and Interface modding were consulted. Relevant official vanilla cosmetic-tag effect/trigger documentation was read. Vanilla GER ideology variants and normal/medium/small TGA headers were inspected.

The event-assets skill's named `assets/flags` reference directory was absent in this checkout. The skill directs the closest existing Chaos Redux and vanilla flag precedents when a type-specific folder is absent, so the current Wendigo files and prior Event 014 generated sources were inspected instead. No alternate source mode or non-generated substitute was used.

## Safety and scope

The work is bounded to Event 014 flag binaries and their asset documentation. The processing helper does not edit gameplay or remove obsolete files. Obsolete live files were removed separately only after the 195 current files passed.

## Simplifications, omissions, and blockers

- Simplifications: none.
- Omissions: none.
- Fallbacks: none.
- Blockers: none.
- Meaningful validation skipped: none for the asset-only contract.
- Commit: intentionally not created, per parent scope.

## Parent follow-up

No asset production or runtime flag cleanup remains. The parent should review the scoped diff and include this package in the broader Event 014 completion assessment. Gameplay/localisation/GFX/country changes were explicitly outside this handoff and were not touched.

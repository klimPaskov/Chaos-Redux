# Event 014 Cannibalism Flag Validation Report

## Final counts

| Surface | Expected | Actual | Result |
|---|---:|---:|---|
| Family source sheets | 13 | 13 | PASS |
| Selected source crops | 65 | 65 | PASS |
| Processed 82x52 PNGs | 65 | 65 | PASS |
| Processed 41x26 PNGs | 65 | 65 | PASS |
| Processed 10x7 PNGs | 65 | 65 | PASS |
| Live standard TGAs | 65 | 65 | PASS |
| Live medium TGAs | 65 | 65 | PASS |
| Live small TGAs | 65 | 65 | PASS |
| Total live TGAs | 195 | 195 | PASS |
| TGA-decoded contact sheets | 4 | 4 | PASS |
| Machine manifest rows | 65 | 65 | PASS |
| Hash inventory rows | 474 | 474 | PASS |

## TGA format and orientation

Every live TGA passed independent header and file-length checks after the obsolete family was removed.

- Image type: 2, uncompressed true-color, on all 195 files.
- Pixel depth: 32 bpp on all 195 files.
- Descriptor: `0x08` on all 195 files.
- Origin: bottom-left on all 195 files; descriptor bit 5 is clear.
- Alpha declaration: 8 bits on all 195 files.
- Alpha content: minimum 255 and maximum 255 on all 195 files.
- File length: exactly 18-byte header plus width x height x 4 pixel bytes on all 195 files.
- Decoded equality: every TGA decodes to the exact orientation-normalized RGBA bytes of its corresponding processed PNG.
- GNU `file` check: 195 Targa rows, zero non-Targa rows, and zero rows containing `- top`.

Raw per-file results and normalized digests are in `tga_validation.tsv`.

## Uniqueness

Normalized RGBA uniqueness was checked after decoding each TGA into viewer orientation.

| Scope | Assets | Unique normalized RGBA digests | Duplicate groups | Result |
|---|---:|---:|---:|---|
| 82x52 TGAs | 65 | 65 | 0 | PASS |
| 41x26 TGAs | 65 | 65 | 0 | PASS |
| 10x7 TGAs | 65 | 65 | 0 | PASS |
| High-resolution source crops | 65 | 65 | 0 | PASS |

The machine-readable result is `rgba_uniqueness.tsv`.

## Visual review

The normal, medium, small, and combined three-size contact sheets are decoded from the live TGAs rather than copied from the processed PNGs. They were reviewed at original resolution.

- All 65 standard flags display upright.
- Every family has five visibly different object layouts, not palette swaps.
- Base, collective-command, civic-resistance, rigid-command, and warlord-neutrality compositions remain distinguishable through layout.
- Central silhouettes remain visible at 10x7, within the unavoidable pixel limit of the engine size.
- No selected sheet contains readable text, a recognizable person, a real victim, real political or extremist insignia, national coats of arms, borrowed Indigenous or sacred imagery, or a recognizable national symbol.
- The first CBL generation was rejected before processing because its base route layout could be read as a national cross. The selected replacement uses asymmetric route geometry and is the only CBL source sheet retained in the package.

## Protected Wendigo base flags

The six existing Wendigo base/neutrality files were hashed before generation and again after final cleanup. All six hashes were unchanged.

| Path pair | SHA256 | Result |
|---|---|---|
| `gfx/flags/ZZZ_weaponized_wendigo{,_neutrality}.tga` | `670BC991820B8ECC904000472E1324B47E087F6E920E1FA0FFD1B32286FAD41D` | PASS |
| `gfx/flags/medium/ZZZ_weaponized_wendigo{,_neutrality}.tga` | `8A89271075C90B4773BE973DB3B0BC233DE418B80B370EC7E58812F3DD179207` | PASS |
| `gfx/flags/small/ZZZ_weaponized_wendigo{,_neutrality}.tga` | `53EDCA39CCECE9812C1FAF1C60DC95236435DF8A38B28673B4B0ABC0BAAAF195` | PASS |

## Obsolete family cleanup

Thirteen live `CBL_LAST_TABLE` remnants existed at the validation gate: three standard, five medium, and five small. They were removed only after the 195 current files passed. A final scan of `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` found zero remaining `CBL_LAST_TABLE*.tga` files.

Historical source and processed documentation under `docs/assets/014_cannibalism/generated_art_sources/` and `generated_art_processed/` was not deleted because the frozen ledger requested removal of obsolete live files only.

## Hashes and evidence

- Exact source generation IDs, selected source-sheet hashes, and prompt blocks: `../prompts/imagegen_prompt_ledger.md`
- Every selected source sheet, crop, processed PNG, contact sheet, prompt record, manifest row set, and live TGA: `sha256sums.tsv`
- Every live TGA's decoded normalized RGBA digest: `tga_validation.tsv`
- Count summary: `processing_summary.json`

## References consulted

- Offline Paradox wiki core pages required by `AGENTS.md`.
- Offline Country creation, Cosmetic tag modding, Localisation, and Interface modding pages.
- Official vanilla `effects_documentation.md`, `triggers_documentation.md`, and `console_commands_documentation.md` cosmetic-tag entries.
- Vanilla GER ideology flag family and standard/medium/small TGA headers.
- Existing Chaos Redux Wendigo flags and prior Event 014 generated flag sources.

The skill's named `assets/flags` reference folder was not present in this checkout. The event-assets skill explicitly directs the closest existing Chaos Redux and vanilla flag precedents when a matching folder is absent, so no alternate source mode or non-generated substitution was used.

# Event 006 live historical flag comparison record

## Scope and acceptance rule

This record covers the four live Event 006 northern/western Europe country
flags: ACX Cornwall, AFX Wallonia, AGX Friesland, and AJX Saar. Acceptance
requires the cited historical design, correct geometry, palette, symbol count,
orientation, and historical function at all three HOI4 sizes. The visual audit
uses both contact sheets:

- `contact_sheets/006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png`
- `contact_sheets/006_nwe_generated_flags_contact_sheet.png`

The first sheet compares the cited design reference, unchanged official
ImageGen output, and deterministic flat master. The second renders the actual
bottom-origin runtime TGA ladder at enlarged nearest-neighbour scale.

## Design comparison

| Tag | Historical function | Geometry and colours | Symbols and orientation | Comparison result |
| --- | --- | --- | --- | --- |
| ACX | St Piran's Cross, the registered Cornish community flag; the Flag Institute gives a 3:5 registry proportion, while the HOI4 engine requires its fixed 82:52 ladder. | Solid black field with one centered white upright cross. Final exact palette is `#000000` and `#FFFFFF`. The design is fitted to the engine canvas without cropping or rotation. | One cross, upright, no charge, border, text, or reversal. | Matches. Palette normalization preserves the ImageGen cross geometry; one partially quantized horizontal edge scanline is promoted to the adjoining white field to remove raw edge noise. |
| AFX | Walloon coq hardi identity officially adopted in 1913; the modern rights-cleared flat vector is used as the distributable representation of that identity. | Solid yellow field with one centered red charge. Final exact palette is `#FFD100` and `#E4002B`. | Exactly one coq hardi, facing the historical direction, beak closed and dexter leg raised; no extra emblem. | Matches at normal and medium. The unavoidable ten-pixel silhouette reduction remains a direct resize, not a redesigned icon. |
| AGX | Provincial flag of Friesland/Fryslân, officially recognized by the province. | Seven diagonal bands, four blue and three white, with final exact palette `#244994`, `#FFFFFF`, and `#E72326`. Band direction is unchanged. | Exactly seven red pompeblêden in the documented arrangement; no hoist device or pan-Frisian substitute. | Matches at normal and medium. All seven charges remain distinguishable at medium; the ten-pixel output is an unedited direct reduction of normal. |
| AJX | Saar Territory flag used during the League of Nations administration, 1920–1935. | Three equal horizontal bands, blue over white over black. Final exact palette is `#00209F`, `#FFFFFF`, and `#000000`. | No emblem, text, vertical hoist, or reversed stripe order. | Matches at all sizes; stripe order, equal division, and orientation remain explicit. |

## ImageGen derivation and deterministic processing

Each tag was generated in a separate official ImageGen call from its cited flat
historical reference plus a canonical vanilla normal/medium/small flag ladder.
The exact prompts, inputs, raw output locations, repo copies, palettes, and
historical citations are recorded in
`prompts/006_nwe_generated_art.md`. Processing is limited to:

1. retain the untouched 1536×1024 ImageGen PNG;
2. nearest-palette conversion without dithering;
3. for ACX only, promote one almost-solid noisy cross-edge scanline using only
   the quantized ImageGen pixels;
4. resize the flat master to 82×52 with LANCZOS and re-quantize;
5. resize normal to 41×26 and 10×7 with LANCZOS and re-quantize;
6. write uncompressed 32-bit BGRA TGA with a bottom-left origin.

No source mask, vector trace, symbol replacement, reconstructed geometry, or
hand-authored small-size fallback is used.

## Runtime delivery and AEX retirement

The four runtime triplets live at `gfx/flags/`, `gfx/flags/medium/`, and
`gfx/flags/small/`. Matching review PNGs live under
`processed_png/generated_nwe/flags/`.

AEX is not a standalone Event 006 country. Its obsolete generated civic master,
processed flag previews, and runtime TGA triplet are deleted and explicitly
rejected by the builder. The Lion of Flanders source remains only as historical
overlay evidence for vanilla `BEL_flanders`; it is not an AEX flag input.

All cited sources, raw outputs, flat masters, processed ladders, decoded
runtime ladders, canonical vanilla references, and contact sheets are covered
by `generated_nwe_hashes.sha256`.

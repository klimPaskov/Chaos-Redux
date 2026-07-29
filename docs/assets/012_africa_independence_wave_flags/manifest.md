# Event 12 Africa Independence-Wave Flag Manifest

## Package scope

This package supplies the exact base-country flag ladders requested for the Event 12 Africa independence-wave dependency.

It contains seven normal, seven medium, and seven small runtime TGA files for `DOX`, `DSX`, `DUX`, `DYX`, `DZX`, `EMX`, and `EQX`.

No ideology variants are included because the dependency is limited to the exact base tag files.

The engine resolves these flags by filename, so no `.gfx` sprite registration is required.

## Historical-status boundary

`DOX` uses the approved public-domain Asante flag artwork as its source.

The other six flags are original, intentionally fictional 1936 revival designs.

They are not presented as historical empire flags or reconstructions.

The research trail in [notes/research_and_design_rationale.md](notes/research_and_design_rationale.md) records why tempting online “historic flag” candidates were rejected.

## Asset inventory

| Tag | In-game identity | Status | Source master | Runtime ladder |
|---|---|---|---|---|
| `DOX` | Asante | Public-domain published Asante flag design; palette-cleaned and resized | `source_png/DOX_flag_of_ashanti_1024.png` | `gfx/flags/DOX.tga`, `gfx/flags/medium/DOX.tga`, `gfx/flags/small/DOX.tga` |
| `DSX` | Oyo revival | Original fictional 1936 revival flag; Ìbọ̀/Solomon-knot and cavalry vocabulary | `source_png/DSX_oyo_revival_imagegen.png` | `gfx/flags/DSX.tga`, `gfx/flags/medium/DSX.tga`, `gfx/flags/small/DSX.tga` |
| `DUX` | Kanem-Bornu revival | Original fictional 1936 revival flag; Lake Chad crescent, Sahel court lances, and cavalry vocabulary | `source_png/DUX_kanem_bornu_revival_imagegen.png` | `gfx/flags/DUX.tga`, `gfx/flags/medium/DUX.tga`, `gfx/flags/small/DUX.tga` |
| `DYX` | Luba revival | Original fictional 1936 revival flag; lukasa memory-board, copper, and stool vocabulary | `source_png/DYX_luba_revival_imagegen.png` | `gfx/flags/DYX.tga`, `gfx/flags/medium/DYX.tga`, `gfx/flags/small/DYX.tga` |
| `DZX` | Lunda revival | Original fictional 1936 revival flag; lukano regalia, copper, and crossroads vocabulary | `source_png/DZX_lunda_revival_imagegen.png` | `gfx/flags/DZX.tga`, `gfx/flags/medium/DZX.tga`, `gfx/flags/small/DZX.tga` |
| `EMX` | Kilwa revival | Original fictional 1936 revival flag; coral-stone arch and dhow vocabulary | `source_png/EMX_kilwa_revival_imagegen.png` | `gfx/flags/EMX.tga`, `gfx/flags/medium/EMX.tga`, `gfx/flags/small/EMX.tga` |
| `EQX` | Zulu revival | Original fictional 1936 revival flag; Nguni shield, spears, and regalia vocabulary | `source_png/EQX_zulu_revival_imagegen.png` | `gfx/flags/EQX.tga`, `gfx/flags/medium/EQX.tga`, `gfx/flags/small/EQX.tga` |

## Source and licensing records

### DOX Asante

- Source page: [Wikimedia Commons — Flag of Ashanti](https://commons.wikimedia.org/wiki/File:Flag_of_Ashanti.svg)
- Supporting design discussion: [Flags of the World — Ashanti](https://www.fotw.info/flags/gh_asa.html)
- Source-file status: public domain
- Local source: `source_png/DOX_flag_of_ashanti_1024.png`
- Processing: the downloaded Commons raster was resized to a clean master and snapped to its yellow, green, black, and white source palette before the ladder was built.

### DSX through EQX

- Source-file status: original generated artwork created for Chaos Redux with the image-generation workflow.
- Historical status: fictional alternate-history designs, not asserted historical flags.
- Cultural references: listed in [notes/research_and_design_rationale.md](notes/research_and_design_rationale.md).
- Exact generation prompts: preserved in [prompts.md](prompts.md).
- Processing: the generated masters were resized and snapped to compact per-flag palettes to remove incidental generation gradients and preserve legibility at HOI4 flag sizes.

## Processed deliverables

Each source has a palette-cleaned `820x520` PNG master in `processed_png/`.

PNG review copies of the normal, medium, and small ladders are stored in `processed_png/normal/`, `processed_png/medium/`, and `processed_png/small/`.

The runtime files are uncompressed true-color 32-bit TGA files with opaque alpha and bottom-left origin:

- Normal: `82x52`
- Medium: `41x26`
- Small: `10x7`

The deterministic processor is [build_flags.py](build_flags.py).

## Validation evidence

- Visual ladder review: [contact_sheets/africa_revival_flag_ladders_contact_sheet.png](contact_sheets/africa_revival_flag_ladders_contact_sheet.png)
- Machine-readable TGA header, dimension, alpha, origin, byte-length, round-trip, and SHA-256 results: [notes/validation.json](notes/validation.json)
- Source, processed, contact-sheet, and runtime checksums: [notes/hashes.sha256](notes/hashes.sha256)
- Runtime wiring handoff: [gfx_handoff.md](gfx_handoff.md)

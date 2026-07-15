# Event 006 Mediterranean and Danube generated-flag manifest

## Scope and status

This bounded package delivers exactly three official-ImageGen-derived HOI4 flag
triplets:

| Tag | Package | Classification | Asset status |
|---|---|---|---|
| `ARX` | IW-018 Sardinia | explicitly fictional 1936 civic synthesis based on attested Four Moors motifs | `handed_off` |
| `ASX` | IW-019 Sicily | historically grounded reconstruction of the surviving 1848 S.015 constitutional-independence national colour | `needs_user_review` for route ownership before gameplay use |
| `ICX` | IW-021 Trieste | historically grounded 1918-1936 civic reconstruction | `handed_off` |
| `AXX` | IW-024 Banat | no asset produced | `blocked` because no attested 1918 Republic flag or approved fictional route design exists |

These statuses describe the asset handoff only. They do not make any country,
route, event, or Event 006 package content-ready.

## Runtime assets

HOI4 discovers flags by exact tag filename. No `.gfx` sprite registration is
needed.

| Tag | Normal | Medium | Small |
|---|---|---|---|
| `ARX` | `gfx/flags/ARX.tga` | `gfx/flags/medium/ARX.tga` | `gfx/flags/small/ARX.tga` |
| `ASX` | `gfx/flags/ASX.tga` | `gfx/flags/medium/ASX.tga` | `gfx/flags/small/ASX.tga` |
| `ICX` | `gfx/flags/ICX.tga` | `gfx/flags/medium/ICX.tga` | `gfx/flags/small/ICX.tga` |

The ladder dimensions are 82x52, 41x26, and 10x7. Every TGA is uncompressed
32-bit BGRA with eight-bit alpha and a bottom-left origin.

Only the unsuffixed triplets are supplied. No approved route-to-filename map
exists for `_communism`, `_democratic`, `_fascism`, `_neutrality`, or a
cosmetic tag, so no ideology or route variant was invented.

## Historical and generated source provenance

### ARX Sardinia

- **Artifact input:** `sardinia_gelre_armorial_folio_62r.png`, a KBR manuscript
  image digitized by Nitosane, CC BY-SA 4.0. Required attribution: *Page out of
  the Armorial Gelre, folio 62r; digital file by Nitosane from KBR; CC BY-SA
  4.0*. It supports the Four Moors motif but is not evidence of a 1936 state
  flag.
- **Geometry aid:** `sardinia_traditional_four_moors_reference.png` by
  Betelgeuse2003, CC0 1.0. It is a modern reconstruction and was used only to
  recognize the motif; its hoist-facing blindfolded treatment was rejected.
- **Generated source:** `source_png/ARX_sardinia_four_moors_imagegen_raw.png`.
- **Classification:** fictional alternate-history synthesis, not an attested
  sovereign flag. The retained field has one edge-reaching red St George
  cross, four black profile heads facing inward, forehead bands above visible
  eyes, and no Savoy, crown, dynastic, religious, or party overlay.

### ASX Sicily

- **Layout input:** `sicily_1848_national_flag_reference.svg`, attributed to
  Manny Mannheimer and later Wikimedia Commons contributors Havsjo and
  HapHaxion, CC BY-SA 4.0. Required attribution: *Flag of Sicilian Kingdom
  1848; Manny Mannheimer and subsequent Wikimedia Commons contributors; CC
  BY-SA 4.0*.
- The modern SVG is an auxiliary layout aid. Its flesh-and-gold, black-outlined
  emblem conflicts with the surviving S.015 object's all-gold embroidery
  description and was not copied.
- **Generated source:** `source_png/ASX_sicily_1848_s015_imagegen_raw.png`.
- **Normalized choices:** a 3:2 field; equal green, warm-ecru, and red vertical
  thirds; exactly one solid-gold Trinacria; one leg down and the other two
  directed upper-left and upper-right. Fringe, tassels, cravat, text, black
  outlines, and flesh colour are omitted.
- **Route lock:** this design belongs only to the constitutional-independence
  route represented by S.015. It is not evidence for a neutral baseline,
  Bourbon/TTS crown route, labor route, military route, fascist route, or
  client-state route.

### ICX Trieste

- **Layout input:** `trieste_free_territory_flag_reference.svg`, original
  uploader Kuemmjen, current version credited to Arlon Stok and Wikimedia
  Commons contributors, CC BY-SA 3.0 and GFDL 1.2+. Required attribution:
  *Free Territory Trieste Flag; Kuemmjen, Arlon Stok, and Wikimedia Commons
  contributors; CC BY-SA 3.0/GFDL*.
- The SVG is an auxiliary subject/layout aid because its file history disputes
  the historic versus modern silhouette. The research packet's Fabretto Plate
  45, figure 20 boundary controls the requested compact form.
- **Generated source selected:**
  `source_png/ICX_trieste_civic_imagegen_raw.png`.
- **Generated edits rejected:**
  `source_png/ICX_trieste_civic_imagegen_edit_rejected_small.png` and
  `source_png/ICX_trieste_civic_imagegen_edit_rejected_large.png`.
- **Normalized choices:** a 3:2 field, civic red `#D71920`, warm white/silver
  `#F8F6EF`, and one upright centered corsesca. The selected native ImageGen
  charge measures 67.3% of field height and 24.7% of field width. The licensed
  aid measures 59.9% by 23.8%; the height difference is disclosed rather than
  corrected with manual vector geometry. The first edit undershot to 46.9% by
  18.4%, and the second overshot to 74.7% by 28.3%, so both were rejected.
- **Form retained:** one long narrow top spear, exactly two symmetric
  upward-curving side blades, one compact joint, and one short lower shaft. No
  UN emblem, full arms, star, national tricolour, lettering, or border appears.

The upstream links, object dates, authority notes, and full licence decisions
are preserved in
`docs/assets/006_independence_wave/mediterranean_danube_flag_sources_2026_07_15/source_manifest.csv`.

## Deterministic processing

`build_flags.py` performs the complete retained-source-to-runtime build:

1. read each untouched 1536x1024 official ImageGen PNG;
2. map pixels without dithering to the declared fixed palette;
3. for ARX only, detect the ImageGen result's full-span red rows and columns,
   keep them as the cross, and remap off-cross red-tinted antialias speckle to
   the closest black or white source colour;
4. create 82x52 and 41x26 images with LANCZOS resampling followed by the same
   fixed-palette mapping;
5. create 10x7 images from source-master cell coverage so thin existing
   charges survive without drawing replacement geometry; and
6. write and reopen bottom-origin uncompressed 32-bit BGRA TGAs.

Declared palettes:

| Tag | Palette |
|---|---|
| `ARX` | warm white `#F7F5EC`, civic red `#C8102E`, near-black `#111111` |
| `ASX` | green `#009246`, warm ecru `#F5F1E6`, red `#CE2B37`, gold `#D8A328` |
| `ICX` | civic red `#D71920`, warm white/silver `#F8F6EF` |

The 10x7 coverage thresholds are black 8% then red 25% for ARX, gold 8% for
ASX, and white/silver 5% for ICX. These thresholds preserve charge pixels that
already exist in the selected ImageGen master; they do not trace a reference,
draw a new emblem, or substitute SVG geometry.

## Review artifacts and integrity

- `contact_sheets/006_mediterranean_danube_imagegen_raw_vs_flat_contact_sheet.png`
  compares the research aid, selected raw ImageGen output, and deterministic
  flat master.
- `contact_sheets/006_mediterranean_danube_final_tga_ladders_contact_sheet.png`
  reopens the actual runtime TGAs and shows all three sizes at enlarged nearest-
  neighbor scale.
- `notes/validation.json` records dimensions, palettes, alpha, TGA headers,
  origins, decode equality, and the tiny-size coverage rules.
- `hashes.sha256` records cited inputs, all generated source PNGs including the
  rejected Trieste edits, flat masters, processed PNGs, actual runtime TGAs,
  validation evidence, and contact sheets.
- `prompts/imagegen_prompts.md` records every exact prompt, ordered input list,
  original ImageGen output path, retained copy, selection, and rejection.

## Integration boundary, omissions, and blockers

No `.gfx`, `.gui`, country, history, event, decision, focus, idea, localisation,
state, or spreadsheet file is edited by this package. The main agent retains
route wiring, cosmetic-tag selection, country integration, documentation
alignment, review, and completion ownership.

- **ASX remains `needs_user_review`:** the art is handed off, but its S.015
  triplet must not become a neutral or universal Sicilian flag. The parent must
  either confirm that the ASX country identity exists only on the constitutional
  route or assign an approved cosmetic tag before gameplay wiring.
- **Banat AXX remains `blocked`:** no `AXX.tga`, processed PNG, generated source,
  prompt, ideology variant, or substitute design was created.
- **Ideology/cosmetic variants are intentionally omitted:** producing generic
  overlays or recolours would invent unsupported route ownership.
- **Trieste proportion is disclosed:** the selected ImageGen result is closest
  overall among the three official outputs but is taller than the auxiliary
  layout aid. No manual or SVG fallback was used.

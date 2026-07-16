# Event 006 northern and western Europe generated-flag manifest

## Authority and status

This is the current flag-only authority for the generated northern/western
Event 006 package. Its complete live scope is:

- ACX Cornwall;
- AFX Wallonia;
- AGX Friesland;
- AJX Saar.

The package owns four separately generated official-ImageGen flat masters,
their cited historical design inputs, canonical vanilla HOI4 presentation
ladders, deterministic processed PNGs, twelve runtime TGAs, two flag contact
sheets, prompts, comparison evidence, and a flag-only SHA-256 ledger. All
non-flag visual assets are outside this manifest and outside the build tool.

The historical function, geometry, palette, symbol count, and orientation audit
remains recorded in `006_nwe_historical_flag_comparison.md`.

## Runtime ownership and route boundary

Only unsuffixed baseline flags are authorized. No ideology or cosmetic route
owns an exact variant mapping, so this package does not create
`<TAG>_democratic.tga`, `<TAG>_communism.tga`, `<TAG>_fascism.tga`,
`<TAG>_neutrality.tga`, or cosmetic-tag variants.

| Tag | Historical design and function | Runtime triplet | Route boundary |
| --- | --- | --- | --- |
| ACX | St Piran's Cross: one white upright cross on black, the Cornish community flag | `gfx/flags/ACX.tga`, `gfx/flags/medium/ACX.tga`, `gfx/flags/small/ACX.tga` | unsuffixed ACX identity only |
| AFX | 1913 Walloon coq hardi: one red rooster on yellow | `gfx/flags/AFX.tga`, `gfx/flags/medium/AFX.tga`, `gfx/flags/small/AFX.tga` | unsuffixed AFX identity only |
| AGX | Friesland provincial flag: seven diagonal bands and seven red pompeblêden | `gfx/flags/AGX.tga`, `gfx/flags/medium/AGX.tga`, `gfx/flags/small/AGX.tga` | unsuffixed AGX Friesland identity; no pan-Frisian substitution |
| AJX | Saar Territory 1920–1935 blue-white-black horizontal tricolour | `gfx/flags/AJX.tga`, `gfx/flags/medium/AJX.tga`, `gfx/flags/small/AJX.tga` | unsuffixed AJX identity only |

HOI4 discovers these exact tag filenames automatically. No `spriteType` or
`.gfx` registration is required.

All twelve runtime TGAs are uncompressed 32-bit BGRA with eight-bit alpha and a
bottom-left origin. Their engine sizes are:

| Ladder level | Size | Runtime directory |
| --- | ---: | --- |
| normal | 82×52 | `gfx/flags/` |
| medium | 41×26 | `gfx/flags/medium/` |
| small | 10×7 | `gfx/flags/small/` |

## AEX no-standalone-flag boundary

AEX remains a vanilla `BEL_flanders` cosmetic overlay, not a standalone Event
006 country identity. There is no active AEX prompt, generated master,
processed preview, or runtime triplet in this package. The historical Lion of
Flanders source remains outside the generated flag tree as evidence for the
existing vanilla cosmetic overlay; it is not an AEX flag input.

The builder validates this boundary and fails if an `AEX*` source appears under
`source_png/generated_nwe/flags/` or if `AEX.png`/`AEX.tga` standalone outputs
appear in the package-owned processed or runtime ladder. It does not delete an
unexpected artifact; removal requires its own reviewed cleanup.

## Source and ImageGen provenance

Each live tag was produced in a separate official ImageGen call. Its cited
historical reference controls the design. Its canonical vanilla ladder controls
only flat presentation and small-size readability. Exact prompts, original
ImageGen output locations, repo copies, palettes, rights notes, and secondary
identity checks are preserved in `prompts/006_nwe_generated_art.md`.

| Tag | Cited design input | Rights/source record | Retained ImageGen raw and flat master | Canonical vanilla ladder | Exact palette |
| --- | --- | --- | --- | --- | --- |
| ACX | `source_png/country_symbols/acx_st_pirans_cross_source.png` | Wikimedia Commons, public domain; identity/proportion check from the Flag Institute UK Flag Registry | `source_png/generated_nwe/flags/ACX_st_pirans_cross_imagegen_raw.png`; `source_png/generated_nwe/flags/ACX_st_pirans_cross_imagegen_flat_master.png` | `arm.png` normal/medium/small | `#000000`, `#FFFFFF` |
| AFX | `source_png/country_symbols/afx_walloon_rooster_source.png` | Wikimedia Commons, CC0; historical identity check from the Wallonia Public Service | `source_png/generated_nwe/flags/AFX_walloon_coq_hardi_1913_imagegen_raw.png`; `source_png/generated_nwe/flags/AFX_walloon_coq_hardi_1913_imagegen_flat_master.png` | `isr.png` normal/medium/small | `#FFD100`, `#E4002B` |
| AGX | `source_png/country_symbols/agx_west_frisian_flag_source.png` | Wikimedia Commons, public domain; official design check from the Province of Fryslân | `source_png/generated_nwe/flags/AGX_friesland_provincial_imagegen_raw.png`; `source_png/generated_nwe/flags/AGX_friesland_provincial_imagegen_flat_master.png` | `ice.png` normal/medium/small | `#244994`, `#FFFFFF`, `#E72326` |
| AJX | `source_png/country_symbols/ajx_saar_territory_1920_1935_source.png` | Wikimedia Commons, public domain; institutional check from the Saarland State Chancellery | `source_png/generated_nwe/flags/AJX_saar_territory_1920_1935_imagegen_raw.png`; `source_png/generated_nwe/flags/AJX_saar_territory_1920_1935_imagegen_flat_master.png` | `arm.png` normal/medium/small | `#00209F`, `#FFFFFF`, `#000000` |

The canonical reference inputs live under
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/flags/` in
`normal/`, `medium/`, and `small/` subdirectories. The ARM ladder is shared by
ACX and AJX as a presentation reference, so its files appear once in the hash
ledger.

## Deterministic processing contract

`_tooling/build_nwe_generated_art.py` performs this exact flag-only sequence:

1. require the four retained raw inputs for ACX, AFX, AGX, and AJX and reject
   unrelated source files; retained flat masters may be rebuilt from the raws;
2. require every untouched ImageGen raw to be 1536×1024;
3. map raw pixels to the documented exact palette without dithering;
4. for ACX only, promote one almost-solid cross-edge scanline using only the
   quantized ImageGen pixels;
5. resize the flat master to 82×52 with LANCZOS and re-quantize;
6. resize normal to 41×26 and 10×7 with LANCZOS and re-quantize, without a
   bespoke small-size redesign;
7. write bottom-origin, uncompressed 32-bit BGRA TGA files;
8. decode every TGA and prove exact pixel and orientation equality with its
   processed PNG;
9. require the completed source tree to contain exactly the four raw/flat pairs;
10. rebuild both flag contact sheets;
11. hash only the explicit flag sources, cited inputs, canonical ladders,
    processed PNGs, runtime TGAs, and flag contact sheets.

It imports no reference mask, traces no vector, redraws no charge, replaces no
generated emblem, and scans no broad asset directory.

Run from the mod root with either equivalent invocation:

```powershell
python -B docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py
python -B docs/assets/006_independence_wave/_tooling/build_nwe_generated_art.py --scope flags
```

`--scope flags` is the only accepted scope value. Older mixed-surface scope
values are rejected by argument parsing.

## Processed layout and review evidence

Processed PNG ladders:

- `processed_png/generated_nwe/flags/normal/`;
- `processed_png/generated_nwe/flags/medium/`;
- `processed_png/generated_nwe/flags/small/`.

Review artifacts:

- `contact_sheets/006_nwe_generated_historical_flags_raw_vs_flat_contact_sheet.png`
  compares each cited design, retained official ImageGen raw, and deterministic
  flat master;
- `contact_sheets/006_nwe_generated_flags_contact_sheet.png` decodes and shows
  the actual runtime TGA triplets at all three engine sizes;
- `006_nwe_historical_flag_comparison.md` records the manual geometry, colour,
  symbol-count, orientation, and historical-function verdict for each tag.

## Hash ledger

`generated_nwe_hashes.sha256` is a flag-only ledger generated from an explicit
path allowlist. It covers:

- four retained ImageGen raw files and four flat masters;
- four cited historical design inputs;
- the three deduplicated canonical vanilla ladders used by the four tags;
- twelve processed PNGs;
- twelve runtime TGAs;
- two flag contact sheets.

It contains no rows from any non-flag source, processed, decoded, contact-sheet,
or runtime tree. Paths are repository-relative and use forward slashes.

## Integration and content boundary

This package does not edit `.gfx`, `.gui`, country, state, character, event,
decision, focus, idea, history, localisation, or spreadsheet files. The exact
engine lookup contract is maintained in
`northern_western_europe_generated_art_gfx_handoff.md`.

The four triplets resolve their flag-art requirement but do not prove country
content readiness. ACX remains blocked by its separate Cornwall geography and
state-ownership requirement. AEX remains outside standalone flag scope.

## Simplifications, omissions, and blockers

No flag was replaced by fallback art, a placeholder, a palette swap, a local
primitive reconstruction, or an unapproved route variant. Ideology and cosmetic
variants are intentionally absent because no accepted design assigns them exact
route mappings. No flag-only workflow blocker remains.

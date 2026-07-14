# Stage 6 Chemical Air Rack-Variant Validation

Validation date: 2026-07-14
Package: `stage_6_chemical_air_variants`
Scope: all 27 requested agents × physical rack variants.

## Inventory and provenance

- 27 source PNGs exist under `source_png/`.
- 27 final processed PNGs exist under `processed_png_64x64/`.
- 27 archive DDS files exist under `dds_archive/`.
- 27 byte-copied runtime DDS files exist under `gfx/interface/equipmentdesigner/planes/modules/stage_6_chemical_air_variants/`.
- 27 source SHA-256 values were checked and all 27 are unique; no source PNG is reused for another icon.
- The 12 authoritative chlorine, phosgene, mustard, and lewisite source/processed pairs were retained and only mechanically normalized into the separate 64×64 final-preview directory.
- The interrupted `chem_air_bomb_sarin_long_range` source and processed pair was inspected and retained. It met the physical-silhouette and transparency bar, so it was not regenerated.
- The other 14 missing icons were generated independently through the official imagegen workflow, each with a dedicated physical rack prompt. No palette swap, cross-type resize, collage, or reused still was used.

## PNG and alpha checks

All 27 files in `processed_png_64x64/` were checked individually:

- declared dimensions: `64×64` for every file;
- pixel format: RGBA;
- alpha minimum/maximum: `0..255` for every file;
- all four canvas corners are fully transparent;
- transparent unused canvas is real alpha, not a checkerboard or opaque matte;
- the final contact sheet was rendered over a checkerboard for visual review.

## DDS checks

All 27 archive DDS files and all 27 runtime copies were checked individually:

- file magic: `DDS `;
- legacy header size at byte 4: `124`;
- declared width/height: `64×64`;
- declared pitch: `256`;
- pixel format block at byte 76 has size `32`;
- pixel-format flags: `65` (`RGB | ALPHAPIXELS`);
- fourCC: `0`;
- bit count: `32`;
- channel masks: `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`;
- texture caps at byte 108: `0x1000` (`DDSCAPS_TEXTURE`);
- no mipmap data;
- exact file length: `16,512` bytes (`128 + 64 × 64 × 4`) for every file;
- actual DDS alpha-byte minimum/maximum: `0..255` for every file.

## Archive/runtime identity

Each runtime DDS was copied from its matching archive DDS after conversion. SHA-256 comparison passed for all 27 archive/runtime pairs; there are no mismatched runtime copies.

## Visual review and quality concerns

The Chaos Redux tech-icon references and the named vanilla aircraft-module references (`airplane_drop_tanks_icon`, `airplane_extra_fueltank_icon`, `airplane_large_bomb_bay_icon`, and `airplane_torpedo_icon`) were inspected before generation. The completed contact sheet confirms the three physical rack roles remain visually distinct at review scale: compact open/lightweight assemblies, elongated streamlined long-range pods, and integrated compact streamlined combinations.

No blocked icons or `needs_user_review` icons remain. One minor inherited variance is recorded: the retained sarin long-range icon includes a cyan release effect. It does not obscure the physical pod, does not introduce text or a matte, and was preserved because the parent explicitly required retaining a satisfactory interrupted source.

No `.gfx`, `.gui`, gameplay, localisation, or interface source file was edited by this package. The main agent still needs to copy the 27 definitions from `gfx_handoff.md` into `interface/chaosx_equipment.gfx`.

# Event 012 promoted Tier A visual package handoff — 2026-08-09

## Scope

Complete: six flat cosmetic flag ladders and six people-free 64x64 emblem/seal DDS assets for `AFRICA_PROMOTED_PAN`, `AFRICA_PROMOTED_GORILLA`, `AFRICA_PROMOTED_GREEN`, `AFRICA_PROMOTED_RIVERS`, `AFRICA_PROMOTED_STONEBORN`, and `AFRICA_PROMOTED_ANCIENT`. Parent integration registered the emblems and assigned each package emblem to its three idea-lifecycle stages.

## Runtime flags

Each tag has an opaque 32-bit bottom-left-origin TGA in all three engine roots:

```text
gfx/flags/AFRICA_PROMOTED_<NAME>.tga                 82x52, 17100 bytes
gfx/flags/medium/AFRICA_PROMOTED_<NAME>.tga         41x26, 4308 bytes
gfx/flags/small/AFRICA_PROMOTED_<NAME>.tga           10x7, 298 bytes
```

The six exact names are `PAN`, `GORILLA`, `GREEN`, `RIVERS`, `STONEBORN`, and `ANCIENT`. The final/evidence copies and SHA-256 hashes are in `docs/assets/012_africa_tiera_visual_packages/manifest.json`.

## Emblems and GFX wiring

Final DDS files are at `gfx/interface/012_africa/tier_a/emblems/AFRICA_PROMOTED_<NAME>_emblem.dds`, all 64x64, one-level uncompressed BGRA DDS with alpha. Stable sprite IDs registered in `interface/012_africa_tier_a_identity_icons.gfx` are:

```text
GFX_012_africa_promoted_pan_emblem
GFX_012_africa_promoted_gorilla_emblem
GFX_012_africa_promoted_green_emblem
GFX_012_africa_promoted_rivers_emblem
GFX_012_africa_promoted_stoneborn_emblem
GFX_012_africa_promoted_ancient_emblem
```

Each sprite points to the matching `gfx/interface/012_africa/tier_a/emblems/AFRICA_PROMOTED_<NAME>_emblem.dds`. Matching `GFX_idea_africa_promoted_<name>_emblem` aliases are live consumers for all three lifecycle ideas belonging to each package, replacing the former generic priority-member idea images.

## Evidence and provenance

- `docs/assets/012_africa_tiera_visual_packages/manifest.json` — six asset rows, source/final hashes, dimensions, source modes, visual-fit notes, and consumer audit.
- `docs/assets/012_africa_tiera_visual_packages/prompts_and_provenance.md` — retained-source uncertainty, normalized acceptance prompts, exact Ancient emblem ImageGen prompt, and processing convention.
- `docs/assets/012_africa_tiera_visual_packages/evidence/flags_contact_sheet.png` — each source master beside normal/medium/small exports.
- `docs/assets/012_africa_tiera_visual_packages/evidence/emblems_contact_sheet.png` — source, processed transparent PNG, and DDS decode round-trip for all six emblems.

The five existing generated masters were retained only after visual audit; the Ancient Hosts emblem was generated in this tranche using the official ImageGen skill. The package is complete and wired to runtime cosmetic identities and lifecycle ideas.

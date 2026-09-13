# Event 31 flat flag and category-picture asset handoff

Status: `needs_user_review`.

The generated non-portrait asset package is complete at the asset-production boundary. It contains `37` selected flat fictional flag designs with `111` final TGA variants and `3` generated fictional category pictures with final `114x101` legacy BGRA DDS files.

## Produced families

| Family | Count | Final runtime roots | Final format |
| --- | ---: | --- | --- |
| Ordinary and dormant-carrier pool | 24 designs / 72 variants | `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/` | uncompressed 24-bit TGA at `82x52`, `41x26`, `10x7` |
| Evolution-IV jihadist-route pool | 8 designs / 24 variants | same three standard flag roots | uncompressed 24-bit TGA at `82x52`, `41x26`, `10x7` |
| Merger/transnational-command pool | 4 designs / 12 variants | same three standard flag roots | uncompressed 24-bit TGA at `82x52`, `41x26`, `10x7` |
| False Revelation final | 1 design / 3 variants | same three standard flag roots | uncompressed 24-bit TGA at `82x52`, `41x26`, `10x7` |
| Category pictures | 3 | `gfx/interface/decisions/031_random_terror/` | opaque legacy BGRA DDS at `114x101` |

The authoritative ordinary count is `24`. The first eight provisional basenames are reserved for the eight dormant-carrier slots and the remaining sixteen are simultaneous ordinary actor alternates. This interpretation follows the Event 31 asset specification’s `24` ordinary base designs while covering the separately stated eight-carrier requirement.

## Runtime files and evidence

- Flat flags: `gfx/flags/event31_*.tga`, `gfx/flags/medium/event31_*.tga`, and `gfx/flags/small/event31_*.tga` for the exact selected basenames in [docs/assets/031_random_terror/flags/manifest.md](../../../assets/031_random_terror/flags/manifest.md).
- Category pictures: `gfx/interface/decisions/031_random_terror/random_terror_government_response_category.dds`, `random_terror_actor_command_category.dds`, and `random_terror_false_revelation_category.dds`.
- Source prompts and motif provenance: [docs/assets/031_random_terror/flags/prompts.md](../../../assets/031_random_terror/flags/prompts.md) and [docs/assets/031_random_terror/category-assets/prompts.md](../../../assets/031_random_terror/category-assets/prompts.md).
- Per-file source, processed, runtime, and checksum manifests: [flags/manifest.md](../../../assets/031_random_terror/flags/manifest.md) and [category-assets/manifest.md](../../../assets/031_random_terror/category-assets/manifest.md).
- Review sheets: [flags/contact_sheet.png](../../../assets/031_random_terror/flags/contact_sheet.png) and [category-assets/contact_sheet.png](../../../assets/031_random_terror/category-assets/contact_sheet.png).
- Machine-readable validation record: [flags/validation.json](../../../assets/031_random_terror/flags/validation.json).
- Human-readable validation record: [flags/validation.txt](../../../assets/031_random_terror/flags/validation.txt).
- Parent wiring guidance: [docs/assets/031_random_terror/gfx_handoff.md](../../../assets/031_random_terror/gfx_handoff.md).

## Generation and processing fit

Every selected flag source is a native ImageGen fictional master with a solid opaque background and no source-image dependency. Flags were resized into processed PNG previews and encoded as opaque uncompressed 24-bit TGA because the installed vanilla flag consumer uses TGA rather than DDS. The TGA headers use type `2`, 24-bit pixels, descriptor `0`, and bottom-left origin.

Every category source is a native ImageGen fictional period-documentary scene. The category masters were cover-cropped to the inspected live consumer canvas, processed as opaque warm monochrome PNGs, and converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`. The DDS outputs match the repository legacy BGRA masks and pass decoded round-trip comparison against their processed PNGs.

The designs are text-free, flat where flags require it, and avoid real extremist names, symbols, sacred calligraphy, deity depiction, stereotypes, modern props, watermarks, UI artifacts, graphic gore, and meme styling. Category scenes use period architecture, clothing, and equipment and keep any people incidental rather than treating the assets as portraits.

## Validation evidence

The final static asset validation passed `37` selected source masters, `111` processed/runtime TGA pairs, and `3` processed/runtime DDS pairs. It checked exact dimensions, TGA type/depth/origin/length, TGA decoded pixel equality, DDS header dimensions, pixel-format masks, caps, exact uncompressed length, opaque category alpha, and DDS decoded pixel equality.

## Parent follow-up and blockers

1. Audit the repository’s final dormant-carrier, country-tag, and cosmetic-tag identities and either keep or atomically rename the provisional flag basenames before wiring.
2. Register the three category sprite names from [gfx_handoff.md](../../../assets/031_random_terror/gfx_handoff.md) in the existing parent-owned `interface/chaosx_decision_category_pictures.gfx` registry and bind them to the category consumers.
3. Review both contact sheets and mark the assets approved or request targeted replacements.

The asset worker did not receive finalized tag/cosmetic IDs, so the flag basenames remain provisional. The existing category-picture registry was inspected and the exact target is recorded above, but it was not edited in this scope. No gameplay, localisation, GUI, GFX definitions, focus, decisions, missions, ideas, achievements, super-event scripts, spreadsheets, portraits, or 3D files were edited. No commit was made.

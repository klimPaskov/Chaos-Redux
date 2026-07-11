# Repression Ledger ImageGen Prompts

Date: 2026-07-11

These prompts produced the frozen visual sources consumed by `tools/build_ledger_ui_assets.py`. They contain no leader, flag, protected-class, or readable-text requirement.

## Archival ledger surface

Output: `source/ui_imagegen/repression_ledger_window_imagegen_source.png`

Reference: the earlier `900x560` placeholder background, used only to retain the functional aspect ratio and empty interaction surface.

```text
Transform this exact Repression Ledger UI background into a richly illustrated, historically grounded Hearts of Iron IV interface texture while preserving the 900x560 functional layout and every blank text/button zone. Dark 1930s-1940s government archive aesthetic: worn black-brown leather ledger cover, layered aged paper and carbon-copy forms, oxidized brass edge hardware, subtle red pencil annotations without readable letters, faint rail-map and filing-grid ghosts, stamped ink smudges, clipped dossier corners, restrained deep burgundy and desaturated olive accents. Orthographic flat game UI, crisp borders, high contrast around panels, richly textured but not cluttered. Preserve full bleed and exact proportions. No readable text, no numbers, no photographs, no people, no bodies, no flags, no insignia, no swastikas, no protected-class symbols, no modern objects.
```

## Dossier emblem atlas

Output: `source/ui_imagegen/repression_ledger_icon_atlas_imagegen_source.png`

```text
Create a clean 4-by-4 sprite atlas for a 1930s-1940s authoritarian government archive management interface in the visual language of Hearts of Iron IV. Exactly sixteen equal square cells on a perfectly flat pure black background, thin dark separators, one centered emblem per cell, no overlap and generous padding. Row 1: closed dossier ledger with brass clasp; stacked state files with map pin; barbed-wire perimeter around a small watchtower; national administrative seal with columns. Row 2: cracked evidence seal over a document; descending population record sheet; industrial labor cog and rail hammer; guarded gate with helmet silhouette. Row 3: freight rail line and supply crate; reform olive branch around an open file; tribunal scales over papers; retreat warning folder with a burning corner. Row 4: chemical hazard dossier with sealed ampoule symbol; biological quarantine dossier with microscope symbol; dismantlement tools over an empty filing cabinet; critical overextension warning with snapped rail and red wax seal. Richly illustrated period dossier emblems, engraved brass, worn paper, ink, wax, muted burgundy, olive, bone, charcoal, painterly but crisp at icon scale. No readable text, no letters, no numbers, no flags, no swastikas, no people or bodies, no protected-class symbols, no modern objects.
```

## Processing contract

- Preserve both frozen generated files unchanged.
- Derive the 24 accepted runtime sprites through `tools/build_ledger_ui_assets.py`.
- Keep sprite ids and dimensions from `manifest_ui.md` stable.
- Downscaled final icons must contain no readable generated marks.
- Convert processed PNGs through `.tools/convert_to_dds.py` with one mip and BGRA output.

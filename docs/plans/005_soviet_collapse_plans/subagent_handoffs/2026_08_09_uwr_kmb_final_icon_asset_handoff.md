# Event 005 UWR and KMB Final Icon Asset Handoff

## Scope

This handoff records the final visual package for the Unconventional Warfare Republic and Kuznetsk Mining Board follow-up country packages.

## Installed assets

- 30 final focus icons: 14 UWR and 16 KMB, installed under `gfx/interface/goals/005_soviet_collapse/`.
- 18 final decision icons: 7 UWR and 11 KMB, installed under `gfx/interface/decisions/005_soviet_collapse/`.
- 2 final identity-idea icons, installed under `gfx/interface/ideas/005_soviet_collapse/`.
- All 50 DDS files have distinct SHA-256 hashes.
- Focus icons are 100 by 88 pixels, decision icons are 33 by 32 pixels, and idea icons are 60 by 68 pixels.

## Wiring

- `interface/005_soviet_collapse_uwr_kmb_icons.gfx` registers the 30 focus sprites, their 30 shine sprites, and all 18 decision sprites.
- `interface/005_soviet_collapse.gfx` registers the two final identity-idea textures.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt` assigns the exact dedicated sprite to every UWR and KMB focus.
- `common/decisions/005_soviet_collapse_decisions.txt` assigns the exact dedicated sprite to every UWR and KMB decision.

## Review evidence

- `docs/assets/005_soviet_collapse/uwr_kmb_final_icons/manifest.json` records every installed file, preview, dimension, and SHA-256 hash.
- `docs/assets/005_soviet_collapse/uwr_kmb_final_icons/processed_png/` contains decoded previews for all 50 DDS files.
- `docs/assets/005_soviet_collapse/uwr_kmb_final_icons/contact_sheets/focus_contact_sheet.png` was visually reviewed for focus-level semantics, route-family consistency, legibility, and accidental duplication.
- `docs/assets/005_soviet_collapse/uwr_kmb_final_icons/contact_sheets/decision_contact_sheet.png` was visually reviewed for action semantics, silhouette separation, and small-size legibility.
- `docs/assets/005_soviet_collapse/uwr_kmb_final_icons/contact_sheets/idea_contact_sheet.png` was visually reviewed for country-identity distinction.

The UWR family uses a coherent dark laboratory, pathogen, containment, and release vocabulary. The KMB family uses a distinct coal-black and furnace-gold mining, extraction, treaty, convoy, and industrial vocabulary. The package contains no placeholders, borrowed temporary icons, or missing registrations.

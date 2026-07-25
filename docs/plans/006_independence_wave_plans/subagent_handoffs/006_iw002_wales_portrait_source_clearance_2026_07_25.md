# IW-002 Wales alternative portrait source-clearance handoff — 2026-07-25

## Result

Source-clearance is complete for two different, historically defensible Welsh male candidates with stronger facial geometry than the previously failed David Grenfell and George Cornwallis-West treatments:

| Role | Candidate | Source disposition | Why it is useful |
| --- | --- | --- | --- |
| Civic or national council | W. J. Gruffydd (1881–1954) | `needs_user_review` | 3,070×3,962 Cardiff University archive portrait; very clear round glasses, bald crown, brow, nose, mouth and shoulders; CC BY-SA 4.0. |
| Mountain or territorial commandant | Brigadier Lewis Pugh Evans VC (1881–1962) | `needs_user_review` | 605×800 Imperial War Museums HU 93411 portrait; clear eyes, ears, jaw, moustache, cap, tunic and period rank details; Commons PD-Old. |

Both candidates passed the subject-ownership scan with no meaningful owner in current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226`. No transfer guard is required for either candidate. Aneurin Bevan and William Ambrose Bebb were excluded because Kaiserreich actively owns them.

## Files created

- Asset package: `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/wales_two_role_clearance/`
- Unchanged masters: `source_masters/w_j_gruffydd_original.jpg`, `source_masters/lewis_pugh_evans_iwm_hu93411.jpg`.
- Lossless decoded masters: `source_master_png/w_j_gruffydd_civic_master.png`, `source_master_png/lewis_pugh_evans_commander_master.png`.
- Exact crops: `source_crops/w_j_gruffydd_civic_crop.png`, `source_crops/lewis_pugh_evans_commander_crop.png`.
- Crop equality proofs: the two sibling `.json` files; both report `decoded_pixels_equal: true` and matching master/output RGBA hashes.
- Source page snapshots: `source_page_snapshots/w_j_gruffydd_commons_api.json`, `source_page_snapshots/lewis_pugh_evans_commons_file_page.html`.
- Comparison sheet: `contact_sheets/wales_two_role_clearance_contact_sheet.png`.
- Package manifest and notes: `manifest.json`, `manifest.md`, `ownership_scan.md`, `research/source_clearance.md`, `gfx_handoff.md`.

## Hash and crop facts

- W. J. Gruffydd JPEG master SHA-256: `b484a6e364adb0b006a8d67a5cdb8d5bc5beaddfc1f8582d3073a2aa87bbb313`.
- W. J. Gruffydd exact crop rectangle: `(0,190)-(2874,3590)` in the `3070x3962` decoded master; crop SHA-256 `45a690657916cd18932dd1a525b8746f26f99a0a3f601fe2595027269081554b`.
- Lewis Pugh Evans JPEG master SHA-256: `fdfde87660f50eb9a2112186878fb8ee93b7c1f0e2cb9f533ca9b2c41c26012c`.
- Lewis Pugh Evans exact crop rectangle: `(60,20)-(580,730)` in the `605x800` decoded master; crop SHA-256 `7c12c4c993cba694c495267c1bd9bc285151fd9ce88c01c53d1b83d789d2ebb4`.

## Ownership evidence

`ownership_scan.md` records the roots, exact/variant search terms, no-match results and the existing WLS sprite consumers. Current runtime consumers remain untouched:

- `GFX_portrait_WLS_independence_wave_national_council` → `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds`.
- `GFX_portrait_WLS_independence_wave_mountain_commandant` → `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`.

## Parent-owned next step

This package is not runtime-ready. The parent must decide whether the 1946 W. J. Gruffydd civic source is acceptable for the 1936 setting and whether the circa-1918 Evans uniform should be aged for 1936. If accepted, use the exact crops as the sole identity inputs for source-locked identity-preserving ImageGen, perform independent likeness/style/provenance review, process to deterministic `156x210`, convert to DDS with the repository converter, and reconcile the current Saunders Lewis localisation before named wiring. Do not create advisor, dossier, `_small`, or fallback assets from these sources.

## Scope confirmation

No ImageGen, DDS conversion, runtime/GFX/localisation/gameplay edits, advisor or dossier assets, or unrelated repository changes were made by this handoff.


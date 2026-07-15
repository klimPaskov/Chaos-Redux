# Event 014 Portrait Refresh Validation

## Visual review

- The labelled CBA-CBD contact sheet was reviewed at final 156x210 scale: 28 distinct identities, readable faces and silhouettes, no prison, cell, bars, cage, restraints, detention corridor, or other confinement imagery.
- The enlarged `cba_cbd_baldness_audit_contact_sheet.png` was reviewed across all 28 source crops: every approved scalp is smooth and bald, with no visible hair, follicles, hair shadow, stubble, buzz cut, fringe, or sideburns. Nine first-set violations were rejected and replaced before final approval.
- `leader_CBA_warlord_south_america` visibly presses his tongue to the temple of a single weathered skull.
- The Hannibal source and processed contact sheets were reviewed frame by frame: the same scars, eye asymmetry, ear damage, coat, shoulder piece, map, shelves, palette, and camera remain coherent across the sequence.
- Hannibal frames `006`, `007`, and `008` show clear tongue-to-skull contact; `005` retains a visible pre-contact gap.
- The static fallback has no skull. The animation studio reads as a map-and-shelf command room, never as confinement.

## Package checks

- Warlord sources: 28 files and 28 unique SHA-256 hashes.
- Warlord processed PNGs: 28 files and 28 unique SHA-256 hashes, all 156x210.
- Hannibal frame sources: 12 files and 12 unique SHA-256 hashes.
- Hannibal processed frames: 12 files and 12 unique SHA-256 hashes, all 156x210.
- Static PNG: 156x210.
- Sheet PNG: 1872x210; every 156-pixel slice is pixel-identical to its corresponding processed frame.
- GIF: 12 frames with repeating `170, 170, 160` millisecond timing; total loop duration is exactly 2,000 milliseconds, averaging 6 fps.

## Live texture checks

- 28 warlord DDS files and the Hannibal static DDS report valid `DDS ` magic, 124-byte headers, 156x210 dimensions, 32-bit BGRA masks, and exact 131,168-byte file lengths.
- The Hannibal sheet DDS reports valid `DDS ` magic, a 124-byte header, 1872x210 dimensions, 32-bit BGRA masks, and the exact 1,572,608-byte file length.
- All 30 DDS pixel payloads are byte-for-byte identical BGRA encodings of their corresponding packaged PNG masters.
- Existing GFX wiring still declares 12 frames at 6 fps and points to the two replaced live files.
- `gfx/leaders/014_cannibalism/hannibal.dds` remains unchanged at SHA-256 `5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88`.

## Scope

The installed change set is limited to the 28 CBA-CBD warlord DDS files, the Hannibal static DDS, the Hannibal sheet DDS, and this self-contained source/processed/review/documentation package. No fallback, placeholder, or transform-only animation was used.

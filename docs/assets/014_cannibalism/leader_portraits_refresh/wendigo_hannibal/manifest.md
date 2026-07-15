# Event 014 Wendigo Hannibal portrait manifest

## Package

- Status: handed off.
- Subject class: fictional alternate-history transformed leader; no real-person or actor likeness.
- Static source: `source_png/leader_ZZZ_hannibal_wendigo_static_source.png`.
- Animation sources: `source_png/frames/leader_ZZZ_hannibal_wendigo_000_source.png` through `_015_source.png`.
- Static processed master: `processed_png/leader_ZZZ_hannibal_wendigo_static.png`.
- Processed frames: `processed_png/frames/leader_ZZZ_hannibal_wendigo_000.png` through `_015.png`.
- Horizontal processed sheet: `processed_png/leader_ZZZ_hannibal_wendigo_sheet.png`.
- Review GIF: `previews/leader_ZZZ_hannibal_wendigo_preview.gif`.
- Per-image processing metadata: `metadata/`.
- Per-image review sheets: `contact_sheets/reviews/`.
- Aggregate frame reviews: `contact_sheets/source_frames_contact_sheet.png` and `processed_frames_contact_sheet.png`.
- Live static DDS: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds`.
- Live animated DDS: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds`.
- Existing registration file: `interface/014_cannibalism.gfx`; no GFX edit was required.

## Source-generation record

Nineteen successful built-in image-generation calls produced the accepted package:

- one independent static master;
- one independent imagegen edit for each of frames 000-015;
- two additional generated frame-015 bridge candidates during loop audit, with only the final midpoint bridge retained.

Frame 000 was generated as an edit of the independent static master, so the static fallback and first animation frame are distinct source artworks. Frames 001-014 were generated as sequential edits with real anatomical, frost, breath, lighting, and expression changes. The retained frame 015 was generated from a temporary 50/50 registration guide derived from frames 014 and 000; imagegen redrew that guide into one coherent midpoint source. The temporary guide is not shipped, and the retained frame is not a blended, warped, translated, recoloured, or filtered final.

## Animation ledger

| Frame | Motion state | Source file | Processed file |
| --- | --- | --- | --- |
| 000 | Frontal rest | `leader_ZZZ_hannibal_wendigo_000_source.png` | `leader_ZZZ_hannibal_wendigo_000.png` |
| 001 | Turn begins | `leader_ZZZ_hannibal_wendigo_001_source.png` | `leader_ZZZ_hannibal_wendigo_001.png` |
| 002 | Deeper inhale | `leader_ZZZ_hannibal_wendigo_002_source.png` | `leader_ZZZ_hannibal_wendigo_002.png` |
| 003 | Turn-away crest | `leader_ZZZ_hannibal_wendigo_003_source.png` | `leader_ZZZ_hannibal_wendigo_003.png` |
| 004 | Return and unseal | `leader_ZZZ_hannibal_wendigo_004_source.png` | `leader_ZZZ_hannibal_wendigo_004.png` |
| 005 | Jaw 20 percent | `leader_ZZZ_hannibal_wendigo_005_source.png` | `leader_ZZZ_hannibal_wendigo_005.png` |
| 006 | Jaw 35 percent | `leader_ZZZ_hannibal_wendigo_006_source.png` | `leader_ZZZ_hannibal_wendigo_006.png` |
| 007 | Jaw 55 percent | `leader_ZZZ_hannibal_wendigo_007_source.png` | `leader_ZZZ_hannibal_wendigo_007.png` |
| 008 | Maximum gape | `leader_ZZZ_hannibal_wendigo_008_source.png` | `leader_ZZZ_hannibal_wendigo_008.png` |
| 009 | Maximum hold | `leader_ZZZ_hannibal_wendigo_009_source.png` | `leader_ZZZ_hannibal_wendigo_009.png` |
| 010 | Closing 70 percent | `leader_ZZZ_hannibal_wendigo_010_source.png` | `leader_ZZZ_hannibal_wendigo_010.png` |
| 011 | Closing 50 percent | `leader_ZZZ_hannibal_wendigo_011_source.png` | `leader_ZZZ_hannibal_wendigo_011.png` |
| 012 | Closing 30 percent | `leader_ZZZ_hannibal_wendigo_012_source.png` | `leader_ZZZ_hannibal_wendigo_012.png` |
| 013 | Nearly shut | `leader_ZZZ_hannibal_wendigo_013_source.png` | `leader_ZZZ_hannibal_wendigo_013.png` |
| 014 | Locked stare | `leader_ZZZ_hannibal_wendigo_014_source.png` | `leader_ZZZ_hannibal_wendigo_014.png` |
| 015 | Midpoint bridge | `leader_ZZZ_hannibal_wendigo_015_source.png` | `leader_ZZZ_hannibal_wendigo_015.png` |

## Visual and provenance review

- All 16 source frames and all 16 processed frames are cryptographically unique.
- Every frame is a real generated source-art state; the loop is not transform-only animation of one still.
- Subject, coat, collar, camera, crop, and open snowy backdrop remain coherent.
- The motion reads as inhale and turn, jaw unseal, nonhuman full gape, distinct peak hold, staged close, locked stare, and midpoint bridge.
- The creature is bald and antlerless. No prison, cell, bar, cage, restraint, actor likeness, sacred motif, cultural shorthand, text, or modern object appears.
- The frame sheet is 2496x210 in exact 000-015 order.
- In-game playback is exactly 6 fps through the existing sprite. The GIF review uses a 170/170/160 ms cadence, averaging 5.993 fps because GIF stores timing in 10 ms units.

## Preserved archival asset

`gfx/leaders/014_cannibalism/hannibal_wendigo.dds` was inspected and not modified. Its SHA-256 remained:

`26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717`

## Simplifications, omissions, and blockers

None. The independent static, 16 real source frames, 16 processed frames, exact sheet, review GIF, contact sheets, metadata, live DDS files, and existing sprite mappings are all present.

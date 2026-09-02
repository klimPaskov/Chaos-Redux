# Event 006 portrait archive runtime-size cleanup — 2026-09-03

## Status

Completed a bounded archive cleanup for the single Event 006 portrait evidence shelf. No gameplay, GFX, localisation, character, or runtime DDS file was changed.

## Archive contract

`docs/assets/portraits/006_independence_wave/` remains the only parent folder, with original source media flat at its root and the existing `processed/` child for crops, review images, provenance, and source metadata. No additional subfolder was created.

The archive contains no retained `156x210` image file after this cleanup. A recursive Pillow dimension check across the parent and `processed/` child returned zero files at `156x210`.

## Removed staged-size files

The following temporary source-review PNGs were removed from `processed/`:

- `portrait_CHU_independence_wave_bolgar_civic_presidium_source_1934_commons_156x210.png`
- `portrait_CHU_independence_wave_middle_volga_congress_source_1923_commons_156x210.png`

Their exact source originals and native-size crops remain preserved. The paired `.txt` contracts and crop JSON records now mark the runtime-sized output as reconstructed in memory and not retained under the consolidated archive policy; the temporary output hashes remain historical evidence only.

## Scope and limits

No source portrait was renamed, substituted, or promoted. The runtime portrait consumers remain governed by their existing provenance and package-admission gates. This cleanup does not clear the CHU identity, rights, or central-attestation blockers.

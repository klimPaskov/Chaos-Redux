# Event 014 CBE-CBH portrait validation

## 2026-07-16 reduction audit

- 19 attachment-listed CBE-CBH DDS files were removed from `gfx/leaders/014_cannibalism/`.
- 9 unique CBE-CBH DDS files remain live: CBE base/North America/South America, CBF base/Africa/Oceania, and CBH base/North America/South America.
- All 32 CBE-CBH sprite names remain registered; CBG aliases use the retained CBF base texture, and other retired regional aliases use the retained base texture for their slot.
- The checks below are the historical pre-reduction 28-portrait review record; the current live DDS inventory is the 9-file set above.

## Historical pre-reduction package checks

- Source masters: 28 present, 28 unique SHA-256 hashes.
- Accepted prompt records: 28 present; 25 first-call repaint masters plus independently regenerated replacements for glossy CBG default/Africa and the audit-duplicative first CBH Africa silhouette.
- Processing records and vanilla-reference review sheets: 28 of each present; every crop is in bounds and uses the exact 26:35 leader-portrait aspect ratio.
- Processed portraits: 28 present, 28 unique SHA-256 hashes, all 156x210.
- Historical live DDS files: 28 present before the reduction; 9 current live DDS files are documented in the reduction audit above.
- Source-to-processed-to-DDS filename coverage: complete for CBE, CBF, CBG, and CBH across Europe/default, Africa, Asia, Middle East, North America, South America, and Oceania.
- Historical DDS round-trip comparison: all 28 pre-reduction textures decoded pixel-identically to their processed PNG masters.
- DDS structure: `DDS ` magic, 124-byte legacy header, 32-bit uncompressed colour, opaque alpha, 131,168 bytes per 156x210 texture.
- Minimum 64-bit difference-hash separation among the final portraits: 13 bits. The closest pair, CBE Middle East and CBG North America, remains visibly and cryptographically distinct.

## Visual checks

The historical aggregate source-crop, final, and repaint-group contact sheets were reviewed at native portrait scale. All 28 pre-reduction portraits are bald, distinct, feral, tightly framed, and readable as classic HOI4 leader paintings. Each portrait retains its own macabre action after cropping, with distinct facial construction, clothing silhouette, pose, and atmosphere. Matte opaque oil/gouache handling, simplified facial planes, restrained period values, and quiet brushed backgrounds replace the previous photographic-modern treatment. No prison imagery, bars, restraints, actor likeness, antlers, sacred motif, copied portrait, modern equipment, or wide action scene appears.

## Registration checks

`interface/014_cannibalism.gfx` contains the complete expected 32 registrations at lines 199-230. Existing sprite names were preserved and the retired texture paths were replaced with the documented retained-texture aliases.

The independent read-only whole-set audit passed all 28 pre-reduction CBE-CBH portraits after the CBH Africa uniqueness correction. It reported no remaining style, period-fit, action-readability, prison-imagery, or silhouette-duplication findings and confirmed that the canonical `hannibal.dds` and `hannibal_wendigo.dds` remain byte-identical to `HEAD`.

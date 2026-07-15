# Event 014 CBE-CBH portrait validation

## Package checks

- Source masters: 28 present, 28 unique SHA-256 hashes.
- Accepted prompt records: 28 present; 27 first-attempt safe generations and one second-attempt safe generation for CBF Africa.
- Processing records and vanilla-reference review sheets: 28 of each present; every crop is in bounds and uses the exact 26:35 leader-portrait aspect ratio.
- Processed portraits: 28 present, 28 unique SHA-256 hashes, all 156x210.
- Live DDS files: 28 present, 28 unique SHA-256 hashes.
- Source-to-processed-to-DDS filename coverage: complete for CBE, CBF, CBG, and CBH across Europe/default, Africa, Asia, Middle East, North America, South America, and Oceania.
- DDS round-trip comparison: all 28 live textures decode pixel-identically to their processed PNG masters.
- DDS structure: `DDS ` magic, 124-byte legacy header, 32-bit uncompressed colour, opaque alpha, 131,168 bytes per 156x210 texture.
- Minimum 64-bit difference-hash separation among the final portraits: 13 bits. The closest pair, CBE Middle East and CBG North America, remains visibly and cryptographically distinct.

## Visual checks

The aggregate source-crop and final contact sheets were reviewed at native portrait scale. All 28 portraits are bald, distinct, feral, tightly framed, and readable as HOI4 leader busts. Each portrait retains its own visible macabre action or prop after cropping, with distinct facial construction, clothing silhouette, pose, lighting, and atmosphere. No prison imagery, bars, restraints, actor likeness, antlers, sacred motif, copied portrait, modern equipment, or wide action scene appears.

## Registration checks

`interface/014_cannibalism.gfx` contains the complete expected 32 registrations at lines 199-230. Existing filenames and sprite names were preserved; no GFX edit was necessary.

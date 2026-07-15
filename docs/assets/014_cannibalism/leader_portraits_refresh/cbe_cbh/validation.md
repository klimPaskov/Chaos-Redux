# Event 014 CBE-CBH portrait validation

## Package checks

- Source masters: 28 present, 28 unique SHA-256 hashes.
- Processed portraits: 28 present, 28 unique SHA-256 hashes, all 156x210.
- Live DDS files: 28 present, 28 unique SHA-256 hashes.
- Source-to-processed-to-DDS filename coverage: complete for CBE, CBF, CBG, and CBH across Europe/default, Africa, Asia, Middle East, North America, South America, and Oceania.
- DDS round-trip comparison: all 28 live textures decode pixel-identically to their processed PNG masters.
- DDS structure: `DDS ` magic, 124-byte legacy header, 32-bit uncompressed colour, opaque alpha, 131,168 bytes per 156x210 texture.
- Minimum 64-bit difference-hash separation among the final portraits: 10 bits; the closest pair is still visibly and cryptographically distinct.

## Visual checks

The aggregate final contact sheet was reviewed at native portrait scale. All 28 portraits are bald, distinct, feral, tightly framed, HOI4-readable leader busts. No prison imagery, bars, restraints, actor likeness, antlers, sacred motif, copied portrait, or wide action scene remains.

## Registration checks

`interface/014_cannibalism.gfx` contains the complete expected registrations at lines 185-216. Existing filenames and sprite names were preserved; no GFX edit was necessary.

# Technical validation

- Asset rows checked: **57** (focus 35, decisions 16, categories 2, ideas 4).
- Result: **PASS**.
- Processed PNGs: exact type target sizes, alpha range 0..255, transparent pixels RGB-zero.
- DDS: `DDS ` magic, 124-byte header, 32-bit BGRA flags/masks, 0x1000 texture caps, one-level length `128 + width*height*4`, alpha byte range 0..255.
- Package DDS and runtime DDS copies have matching SHA-256 hashes.

No technical failures recorded.

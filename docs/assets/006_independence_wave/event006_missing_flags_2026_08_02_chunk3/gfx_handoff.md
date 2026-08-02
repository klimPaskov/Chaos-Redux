# Event 006 flag GFX handoff, chunk 3

The runtime consumer is the normal HOI4 flag ladder, so no `.gfx` sprite declaration is required for these flags.

Use the tag stem as the filename and keep the three runtime sizes together:

- `gfx/flags/GMX.tga`, `gfx/flags/medium/GMX.tga`, `gfx/flags/small/GMX.tga`
- `gfx/flags/GTX.tga`, `gfx/flags/medium/GTX.tga`, `gfx/flags/small/GTX.tga`
- `gfx/flags/GYX.tga`, `gfx/flags/medium/GYX.tga`, `gfx/flags/small/GYX.tga`
- `gfx/flags/GZX.tga`, `gfx/flags/medium/GZX.tga`, `gfx/flags/small/GZX.tga`
- `gfx/flags/HAX.tga`, `gfx/flags/medium/HAX.tga`, `gfx/flags/small/HAX.tga`
- `gfx/flags/HCX.tga`, `gfx/flags/medium/HCX.tga`, `gfx/flags/small/HCX.tga`
- `gfx/flags/HDX.tga`, `gfx/flags/medium/HDX.tga`, `gfx/flags/small/HDX.tga`
- `gfx/flags/HEX.tga`, `gfx/flags/medium/HEX.tga`, `gfx/flags/small/HEX.tga`

The package copies are also kept in `final_tga/` for audit and reproducibility.

All TGAs are type 2, uncompressed, 32-bit BGRA, bottom-left origin, with no alpha transparency in the source artwork.

Parent-owned work remains limited to any `.gfx` edits, localisation, and gameplay wiring.

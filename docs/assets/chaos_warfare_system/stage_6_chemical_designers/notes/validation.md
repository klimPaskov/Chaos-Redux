# Validation record

Validated after DDS conversion and runtime copy.

| Asset | Source PNG | Processed PNG | Archive DDS | Runtime DDS |
| --- | --- | --- | --- | --- |
| `cbrn_chemical_munitions_combine` | 1254x1254 RGB, 2,338,023 bytes | 64x64 RGBA, 9,617 bytes, alpha 0..255 | 64x64, 16,512 bytes, alpha 0..255 | identical to archive, 16,512 bytes |
| `cbrn_aerosol_air_delivery_bureau` | 1254x1254 RGB, 1,809,512 bytes | 64x64 RGBA, 7,046 bytes, alpha 0..255 | 64x64, 16,512 bytes, alpha 0..255 | identical to archive, 16,512 bytes |

Both final DDS files have the complete legacy header contract:

- `DDS ` magic at byte 0 and `DDS_HEADER` size 124.
- Header flags 4111 (`CAPS | HEIGHT | WIDTH | PITCH | PIXELFORMAT`).
- Width 64, height 64, pitch 256, depth 0, mip-map count 0.
- `DDS_PIXELFORMAT` size 32, flags 65 (`RGB | ALPHAPIXELS`), fourCC 0, bit count 32.
- BGRA masks `0x00FF0000`, `0x0000FF00`, `0x000000FF`, `0xFF000000`.
- `DDSCAPS_TEXTURE` `0x00001000`, caps2 0.
- Exact file length `128 + 64*64*4 = 16,512` bytes.
- Alpha and payload scan found visible pixels, fully transparent pixels, and antialiased partial-alpha pixels in each icon.
- Opaque magenta residue scan found 0 pixels in both final DDS payloads.
- Archive/runtime SHA-256 identity: true for both assets.
- Final DDS hashes are unique: `504a34fbb2f5359deb4f066fb4b6b5ba640815290d4ea4b7bde36ab86dae4edf` and `9653875f1eef0ff6010c0ff078aa94e01afed7d01a1a518831f9886cb1db4732`.

Visual checks:

- Processed PNGs were viewed at exact 64x64.
- Runtime DDS files were decoded with FFmpeg and viewed at exact 64x64.
- Checkerboard review sheet: `../contact_sheets/stage_6_chemical_designers_checkerboard.png`.
- Parent integration reviewed the checkerboard contact sheet at original resolution and confirmed that the two silhouettes remain distinct and legible at runtime size.

No unresolved art, format, or sprite-registration blocker remains. Parent integration registers both exact names and paths in `interface/cbrn_designers.gfx`.

# Validation record: Stage 6 CBRN designer icons

Validated after imagegen source preservation, chroma-key removal, exact resize, DDS conversion, runtime copy, and contact-sheet review.

## Per-asset evidence

| Asset | Source | Processed PNG | PNG alpha: transparent / partial / opaque | Archive DDS | Runtime DDS | Opaque magenta |
| --- | --- | --- | --- | --- | --- | --- |
| `cbrn_protective_equipment_consortium` | 1254x1254 RGB, 2,167,593 bytes, SHA `a0d650603f08f5fec62563f6d8100e9fd4630560cab120c1f61e2758f6c0c81d` | 64x64 RGBA, 7,879 bytes, SHA `c3944e45fbadab5993b866d709a03907c28d62e97ee9fafcb7fffb03860b848c` | 1723 / 621 / 1752; alpha 0..255 | `48049c0a1c236f815748ab3c26c6b11e93f1aeace90d20213388fa5380f487a8` | byte-identical; same SHA | 0 |
| `cbrn_mobile_decontamination_works` | 1254x1254 RGB, 1,826,807 bytes, SHA `61f3c74481223419cce3378266b92e3bb60cb304c74a88019b117fc05614ea48` | 64x64 RGBA, 6,187 bytes, SHA `4c9db8901f6d114caa7487833eb5eb7b34ccac09a12ce3e5ca0a5a0dc261123f` | 2358 / 583 / 1155; alpha 0..255 | `8d1078531f28444f3b93c475db39144e5f68c266d7d346730459f56d9ed3ef39` | byte-identical; same SHA | 0 |
| `cbrn_biological_security_directorate` | 1254x1254 RGB, 1,822,781 bytes, SHA `5f63620156468a4605c97765a48db7d1c78a4066dee9aff52e2cd2413d850b58` | 64x64 RGBA, 5,650 bytes, SHA `20db6bda9681be7f78253a1dcb4b298d2263bf08c1244c1b2604c0bf470a375a` | 2232 / 638 / 1226; alpha 0..255 | `45b0e426148962508a3f598d7cbf9c984c679e9f3e3e79f0ae2ecacc5b8f1384` | byte-identical; same SHA | 0 |
| `cbrn_medical_countermeasure_directorate` | 1254x1254 RGB, 2,093,592 bytes, SHA `ca518366fe22600c46c7fad01d55849558a413b9d8cd2c4de0dbdc3ed010ed4d` | 64x64 RGBA, 8,238 bytes, SHA `063196ec3e071b5598b5649ac1d7a2fe583798b962b9380e91e7d77cda1824d3` | 1680 / 733 / 1683; alpha 0..255 | `3dde4dffe6b210a087b5c4f285da791597f41bf2659fd685439d939060f75da5` | byte-identical; same SHA | 0 |

## DDS header contract

All four archive and runtime DDS files were checked as legacy one-level uncompressed 32-bit BGRA/B8G8R8A8:

- `DDS ` magic at byte 0; header size 124.
- Header flags 4111; width 64; height 64; pitch 256; depth 0; mip-map count 0.
- Pixel-format size 32; flags 65; fourCC 0; bit count 32.
- Channel masks: `0x00FF0000 / 0x0000FF00 / 0x000000FF / 0xFF000000` for R/G/B/A.
- `DDSCAPS_TEXTURE` `0x00001000`; caps2 0; no mipmaps.
- Exact file length `128 + 64*64*4 = 16,512` bytes for every archive and runtime DDS.
- DDS payload alpha counts match the processed PNGs for all four assets: each has fully transparent, partially transparent, and opaque pixels.
- Pixelwise BGRA payload comparison against each processed RGBA PNG found 0 channel/alpha mismatches for all four assets.
- No opaque magenta residue was detected in any processed PNG or DDS payload.

## Visual and scope checks

- Contact sheet: `../contact_sheets/stage_6_cbrn_designers_checkerboard.png`; final PNGs are shown at 4x nearest-neighbor on a checkerboard.
- FFmpeg decoded all four runtime DDS files successfully after conversion.
- The four icons remain visually independent at review size: respirator/filter; truck/spray; sealed vial/containment; oxygen mask/medical kit.
- Biological-security art contains no zombie imagery and no explicit biohazard trefoil.
- No source, processed PNG, or DDS is a recolor, crop, resize, or cross-type derivative of the existing Stage 6 chemical designer compositions.
- No `.gfx`, gameplay, localisation, unrelated documentation, or existing asset package was edited.
- `.gfx` registration is a parent handoff only; proposed names and a ready-to-copy snippet are in `../gfx_handoff.md`.

Status: all four static icons are asset-complete and handed off; parent `.gfx`/gameplay wiring remains outside this bounded sidecar.

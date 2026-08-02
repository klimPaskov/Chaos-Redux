# Prempeh II historical DDS validation

**Validation date:** 2026-07-19
**PNG:** `processed_png/portrait_DOX_prempeh_ii_hoi4.png`
**DDS:** `gfx/leaders/006_independence_wave/portrait_DOX_prempeh_ii.dds`

- PNG dimensions: `156x210`
- DDS dimensions: `156x210`
- DDS pixel format: uncompressed BGRA with alpha, one mip level
- PNG SHA-256: `4f3ac8ecba82b41679a499bc56551440f5dad2772abaef8db0bd9570300f38a6`
- DDS SHA-256: `5fcab91f052810e66f3795734c55219488a592e513ab06f737dcbfb5cabbb26e`
- Decoded PNG RGBA SHA-256: `33f8cbc6a5bbf90ebd6f543d75fa9f5acab16646218d343c1e6cb3cba77455b6`
- Decoded DDS RGBA SHA-256: `33f8cbc6a5bbf90ebd6f543d75fa9f5acab16646218d343c1e6cb3cba77455b6`

The decoded pixel streams are exactly equal. This proves only the historical
PNG-to-DDS export. The separate visual review is withdrawn because the PNG was
produced through an ImageGen restyling of a real person; these hashes do not
grant current visual or package readiness.

## Retry-2 candidate (2026-08-02)

The retry-2 deterministic candidate is a 156x210 RGBA PNG with fully opaque
alpha and SHA-256
`E55BC4D3D79502E6AA5049CF554616C263FDAA00336433A4E1179119FEBDA833`.
It has not been converted to DDS. No runtime hash, decoded-stream equality, or
GFX promotion is claimed until the independent visual near-pass is accepted.

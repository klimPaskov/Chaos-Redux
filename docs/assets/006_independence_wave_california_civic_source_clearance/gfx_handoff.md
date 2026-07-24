# IW-184 California/HBX source-only GFX handoff

This handoff contains no runtime texture and does not authorize a `.gfx` edit. The source package stops at archival source clearance and exact crop evidence because the parent explicitly prohibited ImageGen, DDS conversion, runtime wiring, and gameplay changes in this tranche.

## Cleared source inputs

- Immutable source master: `docs/assets/006_independence_wave_california_civic_source_clearance/source_png/william_stephens_loc_master.jpg` (`743x1024`, SHA-256 `5ba60d2fd0fab9a0dcf6a47b08a89bed486e35e5c14fc200c7fc6204b8652b5d`).
- Exact head-and-shoulders crop: `docs/assets/006_independence_wave_california_civic_source_clearance/crops/william_stephens_head_shoulders.png` (`610x810`, SHA-256 `d87f5fe6773844b597a4a1175dd26a6016a5a9df87a6295ce074f92d33ea2085`).
- Crop equality evidence: `docs/assets/006_independence_wave_california_civic_source_clearance/crops/william_stephens_head_shoulders_crop.json` (`decoded_pixels_equal=true`, SHA-256 `4e7c4625a712eb55931902e004cfe316bedf0db96db437ad7c5da5c71c55f7b0`).

## Future runtime suggestion (not registered)

Subject token for parent review: `HBX_independence_wave_civic_convention_chair` with display identity William D. Stephens.

Suggested stable full portrait sprite name after independent full-pipeline approval: `GFX_portrait_HBX_william_d_stephens_civic_convention_chair`.

Suggested target family: the existing country-leader or named-officeholder portrait `.gfx` family that owns the HBX consumer. The eventual texture must be a deterministic `156x210` candidate produced after source-locked ImageGen and an independent likeness/style/provenance PASS; this package does not provide that DDS.

Final DDS path: `not produced by scope`.

Sprite definition snippet: intentionally omitted until the parent confirms the consuming character/leader family and completes the independent portrait audit. Do not point runtime at the source JPG or crop PNG.

## Source and licensing links

- [LOC object record](https://www.loc.gov/pictures/item/2014715011/)
- [LOC persistent handle](https://hdl.loc.gov/loc.pnp/ggbain.34859)
- [LOC direct large JPEG](https://cdn.loc.gov/service/pnp/ggbain/34800/34859v.jpg)
- [California State Library identity/role record](https://governors.library.ca.gov/24-Stephens.html)

# IW-177 Fiji source-only visual handoff

This handoff began as source research and now also contains one identity-preserving ImageGen repaint, deterministic 156x210 processing result, and a provisional runtime DDS/GFX consumer. The consumer is not runtime-admitted until the source-date, independent audit, and FORM-39 route gates pass.

## Recommended source master

`ratu_sir_lala_sukuna_source.jpg` is the recommended source master for a future source-locked FIJ leader or provisional-institution portrait.

- Identity: Ratu Sir Josefa Lalabalavu Vanayaliyali Sukuna (1888-1958).
- Source: National Archives of Fiji, Wikimedia Commons `File:Ratu Sir Lala Sukuna.jpg`.
- Source date: circa 1940s; this is later than the 1936 baseline and requires parent approval.
- Rights basis: Commons `PD-Fiji`; retain National Archives of Fiji credit.
- Master: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/ratu_sir_lala_sukuna_source.jpg` (2520x3128, SHA-256 `8cf20454f59f8644b3c34dd9ea40a7e98cdf5b56113cd8bb918f893fc6cff5e5`).
- Exact source crop: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/ratu_sir_lala_sukuna_crop.png` (300,250)-(2220,2550), with equality proof in `ratu_sir_lala_sukuna_crop.json`.

## Period-valid alternate

`vishnu_deo_fiji_source.jpg` is an alternate for an Indo-Fijian communal/labor/constitutional visual.

- Identity: Pt. Vishnu Deo (1900-1968).
- Source: *The Modern Review*, October 1929, anonymous; Wikimedia Commons `File:Vishnu Deo Fiji.jpg`.
- Rights basis: Commons `PD-India`.
- Master: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/vishnu_deo_fiji_source.jpg` (277x543, SHA-256 `680ae01b3e87937335321369c197a2d63f56b469608e700781639e2d0f1b8719`).
- Exact source crop: `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/vishnu_deo_fiji_crop.png` (25,35)-(252,330), with equality proof in `vishnu_deo_fiji_crop.json`.
- Caution: the halftone source is small and may not support a faithful full-size consumer; Deo's Council service resumed in 1937, so the 1936 role fit is communal rather than an in-office Council portrait.

## Review evidence

The side-by-side review sheet is `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/fiji_portrait_source_contact_sheet.png`. Its 156x210 thumbnails are deterministic review previews only and are not runtime textures.

The source manifest is `docs/assets/006_independence_wave/fiji_source_clearance_2026_07_27/source_manifest.json`.

## Evidence-only HOI4 repaint

The exact crop was repainted with the identity-preserving prompt in `prompts/ratu_sir_lala_sukuna_identity_preserve_imagegen.md`, then processed through the canonical leader pipeline. The raw repaint is `imagegen_results/ratu_sir_lala_sukuna_identity_preserve.png`; the normalized review candidate is `processed_png/ratu_sir_lala_sukuna_hoi4.png`; processor metadata and the side-by-side review sheet are under `metadata/` and `review_sheets/`. The output is a strong male HOI4-style candidate, but it remains evidence-only because the source is dated circa 1940s against the 1936-centered event and still needs an independent likeness/style/provenance audit. Do not convert it to DDS or wire it to `.gfx` until that gate is resolved.

## Sprite handoff

The following consumer is registered provisionally by the parent package tranche:

```text
sprite name: GFX_portrait_FIJ_independence_wave_founding_congress_chair
texture path: gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds
```

The provisional DDS is 156x210, 131168 bytes, and SHA-256 `31fea5eb5c7c4b6f34ec138ed6a3168a7c6c39755a992bd6abf0296c5838d2c6`. The main agent owns final admission after source/date approval, independent likeness/style/provenance audit, and the named FORM-39 FIJ/PNG/WPG route adapter. No advisor or small-portrait consumer exists.

## Clearance state

Overall state is `needs_user_review`. The Sukuna source is compelling but carries a circa-1940s date uncertainty against a 1936-centered event. The Deo source is period-valid but resolution-limited. If strict contemporaneous imagery is required, keep FIJ source clearance blocked rather than substituting an invented or wrong-era portrait.

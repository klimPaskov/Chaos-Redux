# Validation report — IW-043 / IW-058 static icons

Run: `python -B docs/assets/006_independence_wave/iw043_iw058_static_icons_2026_07_18/make_reviews.py`

Result: 27 DDS audits, 4 native contact sheets, and 4 enlarged contact sheets generated successfully.

## Format and dimensions

- Decision categories: 2 DDS, exact 52x40, transparent RGBA.
- Decisions: 16 DDS, exact 32x32, transparent RGBA.
- Ideas/national spirits: 6 DDS, exact 64x64, transparent RGBA.
- Assyria achievement: completed, grey, and not-eligible DDS, each exact 64x64 opaque RGBA. The existing Volga triplet was not overwritten.
- DDS header audit checks magic/header sizes, BGRA 32-bit masks, caps, byte length, exact dimensions, alpha range, and decoded RGBA pixel equality against the processed PNG. Full per-file results and hashes are in `dds_audit.json` and `build_rows.json`.

## Visual review

Every final icon was inspected at native size in:

- `review/native/decision_categories_native.png`
- `review/native/decisions_native.png`
- `review/native/ideas_native.png`
- `review/native/achievements_native.png`

The same 27 icons were inspected enlarged in:

- `review/enlarged/decision_categories_4x.png`
- `review/enlarged/decisions_5x.png`
- `review/enlarged/ideas_3x.png`
- `review/enlarged/achievements_4x.png`

Native review confirms that the categories are distinct and centered, all 16 decisions remain distinguishable at 32x32, all six spirit icons retain a single strong silhouette at 64x64, and the achievement triplet preserves the canonical frame/grey/red-X states.

Transparent families were reviewed over the checker-style contact-sheet background; unused pixels are fully transparent and there is no white halo, fake checkerboard, sticker border, or opaque square. Achievement variants intentionally use full opaque pixels.

## Scope audit

No fallback asset was used. No advisor/adviser, dossier-card, portrait, small/commander, military-high-command, theorist, or other character asset exists in this package or runtime install. No gameplay, localisation, `.gfx`, `.gui`, decision, idea, country, or achievement-definition file was edited by the asset producer.

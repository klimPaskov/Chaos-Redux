# Event 012 Africa achievement icon provenance

## Source evidence

The 44 source masters were present in the owned workspace before reconciliation as `source_png/<key>.png` files.

Every source is a 1254x1254 RGB PNG with a vivid green isolation background and a centered symbolic achievement composition.

The files contain no embedded author, prompt, generation timestamp, or license metadata that can establish an individual generation record.

The green isolation field and stylized symbolic treatment are consistent with generated icon-source production, but this package does not claim a specific generator call for any individual file.

Per-file source SHA-256 values are recorded in `validation/asset_validation.tsv` and `validation/hashes.sha256`.

## Reference review

The canonical achievement reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/achievements/contact_sheet.png` before individual reference review.

The reference sheet establishes the 64x64 footprint, compact central subject, transparent corners, and separate grey and not-eligible state convention.

The vanilla references were used for technical and stylistic review only.

No reference pixels were copied, traced, recoloured, or composited into the Event 012 source masters.

## Deterministic processing

The 24 pre-existing keyed intermediates were preserved byte-for-byte.

The 20 missing keyed intermediates were produced from their matching source masters with the installed ImageGen helper and the standard transparent workflow:

```text
remove_chroma_key.py --auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill
```

No visible artwork was generated or altered by this reconciliation.

All 44 keyed intermediates were resized from 1254x1254 to 64x64 with Pillow `Image.Resampling.LANCZOS` and saved as RGBA normal-state PNGs in `processed_png/`.

The processed previews retain real alpha and transparent corners.

Grey previews were derived from each normal-state preview with `ImageOps.grayscale` while preserving the original alpha channel.

Not-eligible previews were derived from each grey preview by alpha-compositing the canonical `icons/achievements/overlay.png` over the full 64x64 canvas.

No red tint, recolour, darkening filter, or generic fallback was used for the not-eligible state.

All 132 processed previews were converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 64 --height 64` into the root `gfx/achievements/` directory.

The processed output contains no visible near-green key pixels at alpha values of 16 or greater.

Six previews contain one alpha-1 pixel with exact green RGB values at an antialiased edge, which is visually transparent and is recorded in the validation ledger.

## Rights and review status

Because no per-source prompt or author record was supplied, source provenance is `needs_user_review` for final distribution approval.

No external photograph, historical portrait, flag, or third-party asset was introduced by this reconciliation.

The source package is symbolic icon art and does not assert a real historical person or institution.

Runtime DDS triplets are installed and validated against their matching processed PNGs.

The absence of per-source prompt metadata remains a provenance review item even though the technical asset package is complete.

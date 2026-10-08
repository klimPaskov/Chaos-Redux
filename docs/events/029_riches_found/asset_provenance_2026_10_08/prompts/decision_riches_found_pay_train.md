# pay_train compact decision-icon edit request

- Asset requirement: `decision_riches_found_pay_train`; registered alias `GFX_decision_riches_found_pay_train`.
- Source lineage: focused new v1 edit of the current baseline source master `docs/assets/029_riches_found/source_png/decision_riches_found_pay_train.png`, SHA-256 `ee7d9a01b74b1ec8aa243674404d2a9a9829b8760c63dd61025a1bd600df811a`.
- Historical prompt status: unavailable in the prior completion audit; this is a new focused repair prompt responding to the observed native 32×32 readability defect, not a reconstructed historical prompt.
- Retained source output path: `candidate/source_png_v1_compact_batch02_2026_10_07/decision_riches_found_pay_train.png`.
- Tool: built-in ImageGen.
- Exact arguments saved before call:
  - `prompt`: the full prompt below.
  - `transparent_background`: `true`.
  - `referenced_image_paths`: [`C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/assets/029_riches_found/source_png/decision_riches_found_pay_train.png`].
  - `num_last_images_to_include`: omitted.

## Exact prompt

```text
Use case: precise-object-edit
Asset type: Event 029 ordinary HOI4 decision icon; exact registered consumer GFX_decision_riches_found_pay_train; native consumer canvas 32x32.
Primary request: simplify the crowded escort scene into one secure payroll railcar: a compact, armored period rail wagon with one large central lock plate. The wagon is the only subject and signifies wages moving safely through the mine district. Remove guards, rifles, lanterns, mine tunnel, watchtower, smoke, extra cars and scattered track hardware.
Input images: Image 1 is the baseline source master docs/assets/029_riches_found/source_png/decision_riches_found_pay_train.png; preserve the pay-train identity, not its scene layout.
Scene/backdrop: genuinely transparent unused canvas.
Subject: one short armored railcar side silhouette with a single lock as the clear focal mark; only a small pair of wheels and a short rail hint if needed for recognition.
Style/medium: muted compact painterly HOI4 decision-icon art, aged iron and dark wood, dark outline, subtle shadow and clear value separation.
Composition/framing: square, centered, fully inset; bold wagon outline and lock remain readable after smooth reduction to 32x32.
Lighting/mood: soft neutral industrial light; no lantern glow.
Color palette: charcoal steel, worn walnut and muted brass; restrained, not orange.
Materials/textures: matte aged iron and wood; minimal rivets and no tiny decoration.
Text (verbatim): none.
Constraints: preserve secure wage shipment/pay-train meaning; genuine transparent background; no opaque square, frame, text, watermark or new asset family.
Avoid: guards, soldiers, rifles, money piles, coins, lanterns, smokestacks, mine entrance, multiple cars, large track scene, orange rim light, glow, border, background, extra props.
```


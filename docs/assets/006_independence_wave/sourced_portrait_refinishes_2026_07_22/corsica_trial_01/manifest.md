# IW-017 Corsica sourced portrait trial 01

Date: 2026-07-22

Status: `needs_independent_visual_audit`; no DDS or runtime overwrite is
authorized by this package.

Corsica is a grounded polity. Both candidates are identity-preserving ImageGen
edits of unchanged, attributed real male source portraits. ImageGen supplies
only the HOI4 painted finish; no fictional face or substitute identity is
allowed.

## Adolphe Landry — civic leader

- Stable character token: `COR_corsican_municipal_congress`; player-facing
  localisation already identifies Adolphe Landry.
- Stable sprite: `GFX_portrait_COR_independence_wave_adolphe_landry`.
- Authoritative runtime texture path:
  `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_adolphe_landry.dds`.
- Role: Corsican-born deputy, economist, former minister, and Ajaccio civic
  representative, alive and politically active in 1936.
- Unchanged source: `source_masters/COR_adolphe_landry.jpg`; `512x724` JPEG;
  SHA-256 `f1afc654cfeb655313cb943aaab54e438df8c483abe54a96dbf229ad6fa7c9a8`.
- Source authority: the Mediterranean source ledger records the 1917
  BnF/Gallica Agence Meurisse portrait and its French/US public-domain basis.
- Prompt: `prompts/COR_adolphe_landry_identity_preserve_trial_01.txt`.
- Style-only reference:
  `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/contact_sheet.png`.
- Raw ImageGen master: `raw_masters/COR_adolphe_landry_hoi4_trial_01.png`;
  `1081x1455` RGB; SHA-256
  `07e28ddd0a4fb0e0db40b87407322320fa15b95fa0576a29db16c9cba1a7ff99`.
- Native review PNG: `processed_png/COR_adolphe_landry.png`; `156x210` opaque
  RGBA; SHA-256
  `a542a1c6cecc1571501b8d08539be78530a59ba91a06e16d8a50f1c6d39d3505`.
- Processing: the raw master already matches the target aspect ratio within
  one output pixel, so the full `1081x1455` canvas was resized with Lanczos to
  `156x210`; no post-generation face edit, crop, or filter was applied.

## Jean Chiappe — security commander

- Stable character token: `COR_jean_chiappe`; player-facing localisation
  already identifies Jean Chiappe.
- Stable sprite: `GFX_portrait_COR_independence_wave_jean_chiappe`.
- Authoritative runtime texture path:
  `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_jean_chiappe.dds`.
- Role: Corsican-born prefect and security administrator, alive in 1936.
- Unchanged source: `source_masters/COR_jean_chiappe_gallica_f1_highres.jpg`;
  `1374x1054` JPEG; SHA-256
  `2dd15d292a7caa8081b099e7234b41960ede3f2e46318d9b7e752b4570b9d378`.
- Source authority: the Mediterranean source ledger records the 1927
  BnF/Gallica Agence Meurisse source and public-domain dedication.
- Supporting identity crop:
  `source_masters/COR_jean_chiappe_source_crop_preview.png`; `156x210` opaque
  source-derived preview; SHA-256
  `4c517f0e6f5a7db45f5f5ad6190dd5d95b5d86698c1ac6ff83d34bd03be04da2`.
  This deterministic crop is from the same unchanged source and supplies no
  generated detail.
- Prompt: `prompts/COR_jean_chiappe_identity_preserve_trial_01.txt`.
- Style-only reference:
  `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/contact_sheet.png`.
- Raw ImageGen master: `raw_masters/COR_jean_chiappe_hoi4_trial_01.png`;
  `1081x1455` RGB; SHA-256
  `703250cc5fff915991110aadf69549860a7f97ce3a1c220a185df7b4e4205614`.
- Native review PNG: `processed_png/COR_jean_chiappe.png`; `156x210` opaque
  RGBA; SHA-256
  `ef2a179bca8ad9148ff8d47f0c3b665bfbce40f98c4e2441833376be657fef45`.
- Processing: full `1081x1455` canvas resized with Lanczos to `156x210`; no
  post-generation face edit, crop, or filter was applied.

## Review boundary

The independent reviewer must compare every candidate against the unchanged
source at raw and `156x210` size. Exact same-person facial geometry, age,
expression, clothing, role, male-only source mode, head-and-shoulders framing,
and authentic restrained HOI4 painted finish must pass separately. Fail closed
on beautification, invented details, generic face drift, or role/costume drift.

`contact_sheets/source_result_style_comparison.png` records both source/result/
native/style comparisons; SHA-256
`a02b122b1bf2d07a89be49d5a434ffd6726e7b76f03d1db19505d65365508ef1`.

No advisor, dossier, `_small`, female, flag, focus, decision, or gameplay asset
is created here. DDS conversion and runtime wiring are deferred until an
independent audit passes the exact candidate hash.

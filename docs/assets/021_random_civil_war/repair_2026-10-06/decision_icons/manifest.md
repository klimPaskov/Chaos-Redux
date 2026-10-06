# Event 021 decision icon crop repair manifest

Status: implemented and accepted by parent review.
The parent enlarged both original subjects, reviewed light and dark composites, and corrected the relief subject's residual opacity by multiplying alpha by 1.3 with saturation at 255.
The source masters and first crop are retained unchanged.
The final relief preview is `processed_png/decisions/decision_021_relief_corridor_alpha_corrected.png`, with alpha mean 201.092, 28x27 visible bounds and transparent corners.
Its installed DDS SHA-256 is `12aa00530ad9baac214c8d69ef9eca30b0529488b7de7bc8a6ee8a6c722ba5e4`.
The final preview round trip is pixel-exact, with no chroma edge pixels and `ghosted: false`.
The parent correction is evidenced by `records/parent_alpha_conversion.json`, `records/parent_final_size.json` and `contact_sheets/parent_alpha_review.png`.
The original worker measurements below describe the first crop before that correction.

Both repairs reuse the existing native-alpha ImageGen source masters and their archived exact prompts. The 1254x1254 source PNGs remain unchanged. New evidence files include threshold-bounded source crops, 32x32 transparent PNG previews, staged and installed DDS files, exact decode previews, contact sheets, and process records.

Each source was cropped to its alpha>=8 bounding box, then resized proportionally with Pillow 11.1.0 RGBa premultiplied-alpha Lanczos and centered on a transparent 32x32 canvas with a 28-pixel maximum subject dimension. The crop removes diffuse alpha 1-7 pixels outside the subject. There was no background removal, redraw, recolour, opacity adjustment, new image generation, or GFX edit.

| Sprite | Archived source | New source crop | Processed PNG | Runtime DDS | Existing GFX line | Status |
|---|---|---|---|---|---|---|
| `GFX_decision_event021_relief_corridor` | `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/decision_021_open_relief_corridor_v01/source_png/decisions/decision_021_open_relief_corridor.png` | `source_png/decisions/decision_021_relief_corridor_source_crop_alpha8.png` | `processed_png/decisions/decision_021_relief_corridor.png` | `gfx/interface/decisions/021_random_civil_war/decision_021_relief_corridor.dds` | `interface/021_random_civil_war.gfx:37` | `needs_user_review` |
| `GFX_decision_event021_reconstruction` | `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/decision_021_reconstruct_administration_v01/source_png/decisions/decision_021_reconstruct_administration.png` | `source_png/decisions/decision_021_reconstruction_source_crop_alpha8.png` | `processed_png/decisions/decision_021_reconstruction.png` | `gfx/interface/decisions/021_random_civil_war/decision_021_reconstruction.dds` | `interface/021_random_civil_war.gfx:45` | `ready_for_parent_review` |

The archived source prompts remain at `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/decision_021_open_relief_corridor_v01/prompts/decision_021_open_relief_corridor_v01.md` and `docs/assets/021_random_civil_war/recovery_candidates_2026-09-25/icons/decision_021_reconstruct_administration_v01/prompts/decision_021_reconstruct_administration_v01.md`.

`records/process_record.json` contains source and crop hashes, crop coordinates, alpha bounds, before and after alpha means, and final PNG hashes. `records/dds_conversion.json` contains converter checks and candidate DDS hashes. `records/dds_roundtrip_record.json` contains DDS headers, decoded PNG hashes, exact pixel-equality results, and contact-sheet path. The two contact sheets are under `contact_sheets/`.

The relief icon's nonzero-subject mean alpha is 192.175, below the generic 200 diagnostic. The `.tools/gfx/gfx.py dds` report has no findings, all corners are transparent, and the icon was inspected at native size on light and dark backgrounds with intact edges. Its source alpha remains unchanged apart from resampling and the bounded source-space crop.

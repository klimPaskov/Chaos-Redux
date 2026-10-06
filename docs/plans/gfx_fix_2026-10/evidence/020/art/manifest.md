# Event 020 Black Plague Asset Manifest

This active asset workspace records six 020 Black Plague graphics findings; the machine-readable companion is `manifest.json`, and detailed frame lineage is in `candidate_lineage.json` with exact built-in ImageGen request arguments in `source/imagegen/generation_requests.md`.

All destination paths below retain their existing sprite identifiers and registration files; this producer changed runtime DDS files and package documentation only.

## `GFX_black_plague_crisis_seal_animated`

Status: `complete`.

The asset is a fictional symbolic crisis seal for `disease_containment_board_black_plague_crisis_seal_animated` under `disease_containment_board_window` in `interface/biowarfare_disease_containment.gui`, shown for the Severe or Collapsed Black Plague selection.

The static sprite is `GFX_black_plague_crisis_seal_static`, the animated sprite is `GFX_black_plague_crisis_seal_animated`, and the owning registration remains `interface/020_black_plague_rat_identity.gfx`.

The approved source mode is an existing 64×64 static seed plus seven separate built-in ImageGen native-transparent glint layers; each layer is composited over the unchanged seed, with frame 000 exactly equal to the seed.

Background mode is `native_transparent`; the 64×64 seed has real transparent unused pixels, and each generated glint layer has transparent unused canvas.

The prior full-seal generation candidate is preserved as `source/imagegen/crisis/rejected/frame_01_full_seal_drift_raw.png`; it changed seal identity and was rejected.

The inherited frame-001 glint-only test is preserved at `source/imagegen/crisis/frame_01_upper_left_glint_overlay_raw.png` and as a 64×64 composite under `source/imagegen/crisis/superseded/`; the parent requested a fresh authored source, so it is superseded and is not in the final sheet.

The source seed is `source/existing_png/crisis_static.png`; final generated source layers are `source/imagegen/crisis/frame_001_fresh_upper_left_glint_raw.png` and `frame_02_upper_left_glint_raw.png` through `frame_007_near_rest_glint_raw.png` as enumerated in `animations/crisis_seal/frame_plan.md`.

The exact frame-001 replacement prompt is `source/imagegen/requests/crisis_frame_001.json`; it was saved before generation, used the seed as the immutable identity anchor and the superseded layer as a style and placement reference, and produced the selected `crisis_f001_refresh` candidate.

The processed 64×64 frames are `animations/crisis_seal/processed_frames/frame_000.png` through `frame_007.png`; the master sheet is 512×64, runs at 6 fps, loops continuously, uses `play_on_show = yes`, and anchors at canvas centre.

The final files are `animations/crisis_seal/sheets/black_plague_crisis_seal_static.png`, `animations/crisis_seal/sheets/black_plague_crisis_seal_sheet.png`, `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_static.dds`, and `gfx/interface/animated/020_black_plague/crisis_seal/black_plague_crisis_seal_sheet.dds`.

The exact per-frame contact sheet is `animations/crisis_seal/crisis_seal_contact.png`, the review GIF is `animations/crisis_seal/previews/crisis_seal_preview.gif`, and the comparative 8-frame proof is `previews/020_animation_frame_proof.png`.

## `GFX_black_plague_rat_king_terminal_readiness_animated`

Status: `complete`.

The asset is a fictional symbolic readiness seal for `black_plague_rat_king_execute_terminal_takeover` in `common/decisions/020_black_plague_rat_decisions.txt`; an exact identifier and DDS-path search found no other runtime consumer.

The static sprite is `GFX_black_plague_rat_king_terminal_readiness_static`, the animated sprite is `GFX_black_plague_rat_king_terminal_readiness_animated`, and the owning registration remains `interface/020_black_plague_rat_identity.gfx`.

The approved source mode is an existing 64×64 static seed plus seven separate built-in ImageGen native-transparent glint layers; each layer is composited over the unchanged seed, with frame 000 exactly equal to the seed.

Background mode is `native_transparent`; the 64×64 seed has real transparent unused pixels, and each generated glint layer has transparent unused canvas.

The retained authored master remains 64×64 per frame with a 512×64 sheet, and the accepted runtime resize is 34×34 per frame with a 272×34 sheet because the sole decision-row consumer is 41 pixels wide.

The parent reviewed `animations/readiness_seal/decision_34x34_preview/readiness_decision_34x34_contact.png` and accepted the 34-pixel canvas correction on 2026-10-06; this acceptance basis covers the size adjustment and preserves all eight generated frame states.

The rejected circular-halo candidate is retained at `source/imagegen/readiness/rejected/frame_006_circular_halo_raw.png`; it failed the glint-only composition and was replaced with the accepted `frame_006_faint_glint_raw.png` layer.

The source seed is `source/existing_png/readiness_static.png`; generated source layers are enumerated in `animations/readiness_seal/frame_plan.md` and retained under `source/imagegen/readiness/`.

The runtime PNGs are `animations/readiness_seal/decision_34x34_preview/black_plague_rat_king_terminal_readiness_static_34x34_candidate.png` and `black_plague_rat_king_terminal_readiness_sheet_272x34_candidate.png`; frame 000 is pixel-identical to the corresponding resized static PNG.

The runtime DDS files are `gfx/interface/animated/020_black_plague/world_end_readiness_seal/black_plague_rat_king_terminal_readiness_static.dds` at 34×34 and `black_plague_rat_king_terminal_readiness_sheet.dds` at 272×34; the eight frames run at 6 fps, loop continuously, use `play_on_show = yes`, and anchor at canvas centre.

The retained 64×64 master sheet is `animations/readiness_seal/sheets/black_plague_rat_king_terminal_readiness_sheet_64x64_master.png`; the 8-frame 64px contact, 34px contact, and review GIF are `animations/readiness_seal/readiness_seal_contact.png`, `animations/readiness_seal/decision_34x34_preview/readiness_decision_34x34_contact.png`, and `animations/readiness_seal/previews/readiness_seal_preview.gif`.

## `GFX_black_plague_response_progress_fill`

Status: `needs_user_review` for the matching in-game comparison; PNG and DDS production is complete.

The existing 96×27 source is `source/existing_png/response_progress_fill.png`; its runtime destination is `gfx/interface/020_black_plague_response/response_progress_fill.dds`, registered as `GFX_black_plague_response_progress_fill` in `interface/020_black_plague_response.gfx`.

Background mode is `native_transparent`; the source artwork is a white rounded fill, and `processed/response_progress_fill_brass_candidate.png` maps its existing luminance into warm brass and parchment colours while preserving the 96×27 tile, alpha, edge bevel, and shading.

The source-versus-candidate preview is `previews/response_progress_fill_brass_candidate.png`, and the installed DDS is `gfx/interface/020_black_plague_response/response_progress_fill.dds`.

The consumer is the read-only 520×282 `black_plague_response_category_window`, which tiles five 96×27 bands into a 480×27 meter and exposes each band at 20-point thresholds.

The parent accepted the warm tint from the coherent 60 percent baseline and authorized installation; the GUI reviewer is comparing a matching 60 percent post-render against the scenario-matrix panel.
A valid 0 percent baseline full/crop exists, but no 0 percent post-render comparison is complete; 60 percent pre-change evidence is the scenario-matrix panel, and the 100 percent render and comparison remain unvalidated.

The canonical reference root has no progress-fill texture family; the corrected live-consumer baseline and the accepted parchment/brass treatment in the external fix plan supplied the style target.

## `GFX_decision_black_plague_clean_city_rats`

Status: `complete`.

The asset is a 33×32 decision icon for Black Plague’s clean-city-rats decision, registered as `GFX_decision_black_plague_clean_city_rats` in `interface/020_black_plague_response.gfx`.

The source is the existing PNG extraction `source/existing_png/decision_clean_city_rats.png`; background mode is `native_transparent`, and the processed PNG `processed/decision_clean_city_rats_alpha_fixed.png` rebuilds an opaque trap silhouette from the alpha mask and retains the existing RGB and soft exterior edge.

The final DDS is `gfx/interface/decisions/020_black_plague/decision_clean_city_rats.dds`; the before/after white-and-black comparison is in `previews/alpha_before_white_black.png` and `previews/alpha_after_white_black.png`.

## `GFX_goal_black_plague_rat_brood_signal`

Status: `complete`.

The asset is a 94×86 Black Plague progression badge registered as `GFX_goal_black_plague_rat_brood_signal` in `interface/020_black_plague_rat_identity.gfx`; its `_shine` alias uses the same texture.

The source is `source/existing_png/rat_brood_signal.png`; background mode is `native_transparent`, and the processed PNG `processed/rat_brood_signal_alpha_fixed.png` makes the enclosed emblem interior opaque, fills the signal-centre holes, and retains the original soft outer edge.

The final DDS is `gfx/interface/goals/020_black_plague/goal_black_plague_rat_brood_signal.dds`; the before/after white-and-black comparison is in `previews/alpha_before_white_black.png` and `previews/alpha_after_white_black.png`.

## `GFX_goal_black_plague_rat_king_the_royal_basin`

Status: `complete`.

The asset is a 94×86 Black Plague progression badge registered as `GFX_goal_black_plague_rat_king_the_royal_basin` in `interface/020_black_plague_rat_identity.gfx`; its `_shine` alias uses the same texture.

The source is `source/existing_png/rat_king_royal_basin.png`; background mode is `native_transparent`, and the processed PNG `processed/rat_king_royal_basin_alpha_fixed.png` rebuilds an opaque silhouette from the alpha mask and retains the original soft exterior edge.

The final DDS is `gfx/interface/goals/020_black_plague/goal_black_plague_rat_king_the_royal_basin.dds`; the before/after white-and-black comparison is in `previews/alpha_before_white_black.png` and `previews/alpha_after_white_black.png`.

## Shared processing and review

All new generated transparent layers from the resumed task explicitly requested native transparency, and the raw outputs retain alpha through sizing and composition.

The superseded crisis frame-001 carry-forward layer predates the resumed task; it retains genuine native alpha, but its original prompt record was unavailable and is not reconstructed.

The exact ImageGen requests for the resumed frames 002–007 were recovered from the active turn and saved after generation because the task resumed with existing candidates; the replacement frame-001 request was saved before its generation, and the superseded carry-forward and rejected full-seal prompts remain unavailable.

The six-asset package contact sheet is `contact_sheet.png`, the animation frame and sheet proof is `previews/020_animation_frame_proof.png`, and the source, processed, and decoded-DDS alpha comparison is `previews/020_alpha_contact_sheet.png`.

The three alpha repairs use the inherited source RGB and mechanical mask-derived alpha reconstruction; no subject or colour regeneration was used.

All final DDS files in this package were produced only with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and validated for the 128-byte BGRA header, native dimensions, exact data length, alpha range, and decoded-pixel equality with the approved PNG.

No `.gfx` or `.gui` file was edited; the parent owns final wiring review and the event owner retains any required GUI before/after evidence.

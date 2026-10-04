# Event 033 static veils and global weather visuals

Date: 2026-10-03.
Owner: chaosx_generated_event_art.
Disposition: produced and handed off; needs_user_review.
No Git commit was made.

## Scope and acceptance limits

The two static veil assets and the global weather animation family are the only art surfaces owned by this handoff.
The icon worker owns front, warning, and severe marker art and animation.
All requested source, processed PNG, canonical DDS, decoded round-trip, preview, manifest, lineage, and contact evidence exists.
Visual completion is not claimed because native ImageGen changed the static opacity and the inherited animation density differs from the current frame plan.
No generation, conversion, or file-delivery blocker remains.

The exact prior static alpha was not preserved across the native edits.
Warning mean alpha changed from 45.77567 to 85.14444, with mean absolute per-pixel alpha delta 39.445564.
Global mean alpha changed from 112.14439 to 133.17958, with mean absolute per-pixel alpha delta 21.970384.
Both selected candidates retain semitransparent weather, but these opacity differences require parent acceptance or further authorized repair.
The global v3 opacity revision worsened mean alpha to 141.223815 and was rejected; selected global v2 remains installed.

The recorded saturated-color check finds zero red/yellow pixels at alpha>=64 in both static finals.
Warning retains 717 red and 1694 yellow pixels with nonzero alpha, all at alpha<=3.
Global retains 74 red pixels at alpha<=1 and 202 yellow pixels at alpha<=3.
No visible colored fringe was found on the individually inspected dark/light composites.
Strict elimination of every nonzero-alpha color residue remains a parent review item.
The metric is HSV saturation>=0.75 and value>=0.65, red hue<20 or>345, yellow hue40..70 degrees, with the boundary defined within6 pixels of alpha0.
This defined metric is not claimed to be identical to the parent's earlier pixel classifier.

The supplied eight animation sources depict a nearly continuous cloud/rain curtain.
The current frame plan describes more separated cloud banks and broader sparse regions.
The provided real motion states were preserved and repaired, so density and full-panel map readability remain a parent review item.
No frame count, timing, canvas, path, or source-frame requirement was simplified.
No matte, chroma, background-removal fallback, primitive replacement, transform-created motion, or slideshow substitution was used.

## Canonical runtime outputs

| Asset | Final DDS | Sprite | Canvas | Bytes | RGBA round trip |
| --- | --- | --- | --- | --- | --- |
| Warning veil v6 | gfx/interface/033_acid_rain/gui/acid_rain_warning_veil.dds | GFX_acid_rain_warning_veil | 1672x941 | 6293536 | Exact, zero changed values |
| Global veil v2 | gfx/interface/033_acid_rain/gui/acid_rain_global_veil.dds | GFX_acid_rain_global_veil | 1672x941 | 6293536 | Exact, zero changed values |
| Global animation sheet v2 | gfx/interface/033_acid_rain/animation/acid_rain_global_sheet.dds | GFX_acid_rain_global_animated | 4480x300, eight560x300 frames | 5376128 | Exact for the whole sheet and every frame |
| Global fallback v2 | gfx/interface/033_acid_rain/animation/acid_rain_global_static.dds | GFX_acid_rain_global_static | 560x300, frame000 | 672128 | Exact, zero changed values |

All four DDS files use the repository-standard converter at .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py.
The final delivery audit verified 12 immutable input files, both updated main-manifest records, and all four canonical DDS hashes.
The audit record is docs/assets/033_acid_rain/icon_artist/animations/acid_rain_gui/global_repair_v2/evidence/final_delivery_validation_v2.json.
Its installed FFmpeg backend wrote canonical one-level uncompressed BGRA32.
The128-byte legacy header, pixel-format block at76, flags65, BGRA masks, texture caps0x1000, dimensions, byte length, alpha, and decoded pixels were checked.

DDS SHA-256 values:

- Warning:7466a97accc922a670c0c10e779144c782dbcd8ac8b4ff6e0992293805cf7a8e
- Global veil:d3ed0e0f2ff65822842b16861fd71137e4282e2f827bd7141f4fa6367ee4f9c4
- Global sheet:a5a206acff8c651de20dd8ddd8ddc981029f5384f228c4c431951c88aeb87281
- Global fallback:73cd09ebba69e53c2319c731b0c893e68dcbb9651a28307cf21a7e40e97fc970

## Static candidate lineage and files

Original master docs/assets/033_acid_rain/generated_event_art/source_png/acid_rain_warning_veil_source.png remains immutable at SHAe84b40c6798542b12b939850fb81190ae2529f0ba035b10f785562c2a8cee746.
Original master docs/assets/033_acid_rain/generated_event_art/source_png/acid_rain_global_veil_initial.png remains immutable at SHA4e547db1a015e56a4aae69fd5411bee3ab8c04f4d33c14cce8def5aa99d54238.
The original processed previews remain untouched.
The old rejected runtime DDS files are retained under generated_event_art/roundtrip/rejected_v1.
The superseded warning v5 runtime candidate is retained at generated_event_art/roundtrip/acid_rain_warning_veil_repair_v5_candidate.dds.

The warning branch is original master -> rejected focused edits v2/v3/v4; original normalized consumer preview -> v5 -> selected v6.
The global branch is original normalized consumer preview -> selected v2 -> rejected opacity revision v3.
The consumer-preview branch uses the original master lineage and preserves the exact1672x941 geometry authority.
Selected sources are genuine1672x941 native ImageGen outputs; the static processing performs no resize, repaint, alpha replacement, or opacity correction.
Selected source and processed pixels are identical before DDS conversion.

Selected warning source:docs/assets/033_acid_rain/generated_event_art/source_png/acid_rain_warning_veil_repair_v6_source.png.
Selected warning processed:docs/assets/033_acid_rain/generated_event_art/processed_png/acid_rain_warning_veil_repair_v6_processed.png.
Selected global source:docs/assets/033_acid_rain/generated_event_art/source_png/acid_rain_global_veil_repair_v2_source.png.
Selected global processed:docs/assets/033_acid_rain/generated_event_art/processed_png/acid_rain_global_veil_repair_v2_processed.png.

The exact submitted prompts, parent candidates, input roles, tool-reported paths, selected IDs, and rejection reasons are linked through docs/assets/033_acid_rain/generated_event_art/evidence/static_veil_candidate_lineage_2026_10_03.json.
Decoded dimensions, hashes, alpha, and corners for all11 candidates are in static_veil_candidate_inventory_v2.json.
The labeled alternatives contact sheet is static_veil_candidate_contact_2026_10_03.png.
Final alpha, prior-opacity comparisons, hashes, and exact round-trip results are in static_veil_repair_results_v2.json.
Each selected source, processed PNG, decoded DDS PNG, and contrasting-background edge view was inspected individually.

## Global animation lineage and evidence

The immutable inherited sources are docs/assets/033_acid_rain/icon_artist/animations/acid_rain_gui/source_frames/acid_rain_global_000_source.png through acid_rain_global_007_source.png.
Frame000 contained native alpha and artificial internal cutout defects.
Frames001-007 decoded with fully opaque alpha; checkerboard or black backing was therefore rejected.
Each source received its own focused native ImageGen edit.
Frame000 is the alpha/palette/anchor reference only for the other edits; each target's authored cloud folds, rain distribution, and runoff state remain distinct.

The complete versioned package is docs/assets/033_acid_rain/icon_artist/animations/acid_rain_gui/global_repair_v2/.
It includes source_frames/acid_rain_global_000_repair_v2_source.png through007, processed_frames/acid_rain_global_000.png through007, sheets/acid_rain_global_sheet.png, sheets/acid_rain_global_static.png, roundtrip PNGs, dark/light previews, per-frame edge views, contacts, prompts, and mechanical processing provenance.
generation_lineage.json links each native tool output and prompt.
animation_manifest.json records every original and selected source hash, canvas, alpha, processed frame, timing, runtime path, sprite, and review limit.

Normalization maps each full source canvas to560x300 with alpha-aware Lanczos and the upper-left origin0,0.
No independent tight crop, frame translation, rotation, per-frame scale animation, opacity animation, or local art change is performed.
The sheet contains exactly eight unique processed frames once, left-to-right000..007.
Frame000 is the static fallback.
All processed corners have alpha0, and each frame has native zero-alpha and partial-alpha pixels.
Each original and repaired source was reviewed individually at source resolution; every processed frame was inspected at560x300 and on both light and dark backgrounds.
The decoded sheet and fallback were inspected separately, and all eight decoded columns equal their processed PNGs.

Timing is4 FPS,250ms per frame,2000ms per loop, looping=yes, play_on_show=yes, pause_on_loop=0.0.
The two GIFs encode eight frames with250ms durations; they are review-only composites because GIF cannot preserve partial alpha.
previews/acid_rain_global_native_alpha_preview.png is an eight-frame APNG whose decoded RGBA equals every processed frame exactly.
The GIF frame contents were reviewed through the native-size frame and boundary evidence; timed live playback and in-game review are not claimed.

The007->000 mean absolute premultiplied RGBA delta is19.822554, smaller than every internal transition.
Internal transition deltas range20.101732..27.278057.
Boundary alpha>=64 mask IoU is0.958637, higher than every internal transition.
Alpha centroid ranges are14.18878 pixels horizontally and14.43064 vertically because the authored rain distribution changes; the registered full-canvas origin remains fixed.
Per-pair values are in animation_manifest.json, and evidence/acid_rain_global_loop_boundary.png shows007 beside000.
evidence/acid_rain_global_source_contact.png and acid_rain_global_processed_contact.png expose frame consistency and distinct states.

## Existing consumers and GFX handoff

The owning registry is interface/033_acid_rain.gfx.
The dedicated GUI is interface/033_acid_rain.gui, with a560x300 map panel at24,74.
Warning uses acid_rain_map_warning_veil at0,0 with scale0.335.
The1672x941 static canvas is the accepted consumer contract.
The active global child acid_rain_map_global_veil uses GFX_acid_rain_global_animated at0,0 and scale1.0.
The global frames are already560x300; do not apply0.335 to them.
GFX_acid_rain_global_veil and GFX_acid_rain_global_static are registered static assets; the active child currently uses the animated sprite.

Visibility comes from common/scripted_guis/033_acid_rain_scripted_guis.txt::acid_rain_decisions_scripted_gui.
Warning binds global.acid_rain_gui_warning_layer_active >0.
Global binds global.acid_rain_gui_global_layer_active >0.
The context is decision_category and the window is acid_rain_world_window.

Current inspected source hashes are GFX A24CBA2E9B7C4B567A96C0D1731AC97EE136E48CF41DB0F8E03FEF8BFF29B7F6, GUI77C002339D30C671F25EFCA40B28B1A22D0CB5658CA2BB7536384050C5271FDD, and scripted GUI0A784B5B04A39294A501FCD2D8CB2CA237CA85E8C0A8CAD967059B4846EE7D18.
These source inspections provide the registration/consumer crosswalk, not live-game evidence.
The parent retains GUI/MCP integration and final consumer review.
No GFX, GUI, localisation, gameplay, or other asset file was edited by this worker.

Existing registrations, reproduced as handoff data only:

```txt
spriteType = { name = "GFX_acid_rain_warning_veil" texturefile = "gfx/interface/033_acid_rain/gui/acid_rain_warning_veil.dds" noOfFrames = 1 }
spriteType = { name = "GFX_acid_rain_global_veil" texturefile = "gfx/interface/033_acid_rain/gui/acid_rain_global_veil.dds" noOfFrames = 1 }
frameAnimatedSpriteType = { name = "GFX_acid_rain_global_animated" texturefile = "gfx/interface/033_acid_rain/animation/acid_rain_global_sheet.dds" noOfFrames = 8 animation_rate_fps = 4 looping = yes play_on_show = yes pause_on_loop = 0.0 alwaystransparent = yes effectFile = "gfx/FX/buttonstate_blendframes.lua" }
spriteType = { name = "GFX_acid_rain_global_static" texturefile = "gfx/interface/033_acid_rain/animation/acid_rain_global_static.dds" }
```

## Concurrent work and manifest scope

Only the bounded mechanical processor recorded here was run.
The retained mechanical processor has four explicit DDS destinations: the two static veils and the global sheet/fallback.
No report file was moved or processed.
The read-only status snapshot observed five untracked event-scoped report DDS files and three legacy report/news deletions; the parent subsequently confirmed report alias/path repair commit174b1c7e7.
All five report paths were re-read after that repair and remain gfx/event_pictures/033_acid_rain/033_acid_rain_<name>.dds.

Only acid_rain_warning_veil and acid_rain_global_veil records were replaced in docs/assets/033_acid_rain/asset_manifest.json.
The exact bytes outside those objects are unchanged: SHAbada73cfda9605b071205240a8ec29ea922e74a2b3634f6b95a77fbaec09e176 before and after.
Manifest SHA before:111e8546e415fd5db80393dd20ab069872d22e6118c8fb02dad098f3419d24c4.
Manifest SHA after:dc6a3759d000bab18104ccfdabc62891bf1391e531be16dd664b93b672cf5fd0.
The proof is docs/assets/033_acid_rain/generated_event_art/evidence/manifest_veil_scope_proof_2026_10_03.json.
Both records and the global family manifest are marked needs_user_review.

Skills used:chaos-redux-event-assets, chaos-redux-frame-animation, and the official imagegen skill.
All native edits used the built-in image_gen path with transparent_background=true.
The exposed tool has no model selector, so no backend model is asserted.
The canonical gfx_references root was checked for a matching weather/map-veil family; no dedicated family was found and no unrelated reference family was substituted.

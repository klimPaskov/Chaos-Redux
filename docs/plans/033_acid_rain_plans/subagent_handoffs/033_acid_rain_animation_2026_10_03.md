# Event 033 small marker animation production handoff — 2026-10-03

Production is complete for the front, warning, and severe families and their static accessibility representatives.
All six runtime files are installed at the existing registered paths.
The assets are handed off for parent approval and final wiring; the orchestrator supplies GUI/live evidence.
This handoff does not claim full Event 033 integration completion.

## Authorized scope and deliverables

The latest user instruction limits this worker to three small marker families.
Owned documentation/evidence is under `docs/assets/033_acid_rain/icon_artist/animations/acid_rain_gui/front/`, `warning/`, and `severe/`.
The shared brief, shared frame plan, original source directory, rejected old package, and other workers' asset families receive no edits.
No GFX, GUI, localisation, gameplay, or spreadsheet file was edited, and no commit was made.

| Family | Exact sheet DDS under `gfx/interface/033_acid_rain/animation/` | Sheet size | Frames/rate | Static DDS |
| --- | --- | --- | --- | --- |
| Front | `acid_rain_front_sheet.dds` | 1024x128 | 8 at 6 FPS | `acid_rain_front_static.dds`, 128x128 |
| Warning | `acid_rain_warning_sheet.dds` | 768x128 | 6 at 5 FPS | `acid_rain_warning_static.dds`, 128x128 |
| Severe | `acid_rain_severe_sheet.dds` | 1024x128 | 8 at 6 FPS | `acid_rain_severe_static.dds`, 128x128 |

| Family | Exact animated sprite | Exact static sprite |
| --- | --- | --- |
| Front | `GFX_acid_rain_front_animated` | `GFX_acid_rain_front_static` |
| Warning | `GFX_acid_rain_warning_animated` | `GFX_acid_rain_warning_static` |
| Severe | `GFX_acid_rain_severe_animated` | `GFX_acid_rain_severe_static` |

Each horizontal strip contains only its listed authored frames, numbered from 000 and included once.
There are 22 processed frames in total; each is 128x128.
Each static representative is exact processed frame 000 from its own family.
The existing `looping = yes`, `play_on_show = yes`, `pause_on_loop = 0.0`, click-through behavior, and blend-frame effect are retained in the consumer.
The map/card review footprints use the current consumer's scale 0.375 and 0.3, approximately 48x48 and 38x38.

## Source production and repair evidence

All 22 owned September 4 originals were inspected individually and copied byte for byte into their family-owned `source_versions/original/` directories.
The originals in the preserved shared source directory were never overwritten, and their initial SHA-256 values were checked before and after processing.
No rejected old frame, matte-removal output, old sheet, old script, or old DDS supplies runtime content.

Front source frames 001 and 006 failed alpha validation: their entire 1254x1254 canvases were opaque and the unused canvas contained a painted checkerboard.
The authorized focused built-in ImageGen edits requested real transparency and preserved each frame's marker, cloud, precipitation state, full rim, lower bead, camera, palette, and framing.
Selected masters are `front/source_versions/native_alpha_edits/acid_rain_front_001_alpha_edit_v2.png` and `acid_rain_front_006_alpha_edit_v1.png`.
The sibling frame-001 v1 candidate is retained without promoting it.
Exact prompts, declared edit targets, output paths, selected-candidate hashes, alpha counts, and subject comparisons are in `front/source_versions/repair_records.json`.
The actual execution path is built-in `image_gen` with `transparent_background = true`; its schema exposes no model selector or reported backend model.
No local background extraction or matte fallback was used.

Warning and severe masters retained their native alpha and required no ImageGen repair.
Their separate source states provide actual cloud, corrosive precipitation, lightning, splash, and runoff changes.
There is no transform-only motion, recolor loop, glow pulse, fake primitive layer, or unrelated-scene slideshow.

## Processing and producer review

A shared premultiplied-alpha resize converts each full 1254x1254 master to 120x120, then places it at (4,4) in the exact 128x128 transparent runtime canvas.
The same scale, inset, origin, and (64,64) canvas anchor apply to all 22 frames.
There are no frame-dependent offsets, rotations, scaling, warps, filters, or opacity changes.
Native-size QA caught severe cloud tips approaching the boundary during the first downsample; the common inset preserves those complete edges and gives every final frame a zero-alpha border.

Every selected master and every final normalized frame was inspected individually.
Source/processed/enlarged/decoded contact sheets and configured-footprint boards provide retained visual evidence.
The rim/sign identity, material palette, complete silhouette, subject visibility, intentional internal gaps, and static readability passed producer review.
No final checkerboard, matte square, halo, colored spill, clipped silhouette, or unintended transparent hole was found.

Read-only landmark registration searches fixed rim/sign patches against frame 000 at integer offsets within two pixels.
Every frame's best offset is (0,0), without applying a registration transform.
The last-to-first transitions were reviewed visually and are not numerical outliers:

| Family | Last-to-first RGB mean absolute difference | Largest internal transition | Anchor result | Outer-edge alpha |
| --- | ---: | ---: | --- | --- |
| Front | 8.5792 | 13.6737 | (0,0) for all 8 frames | 0 for all frames |
| Warning | 8.7705 | 12.2911 | (0,0) for all 6 frames | 0 for all frames |
| Severe | 12.9658 | 20.4681 | (0,0) for all 8 frames | 0 for all frames |

These measurements support the reviewed continuity; they are not a substitute for the parent's engine presentation review.
The runtime loop durations are 8/6 seconds, 6/5 seconds, and 8/6 seconds.
The GIFs show the real frames on a review-only checkerboard and have 170/160 ms quantization for 6 FPS or 200 ms for 5 FPS.
Companion RGBA animated PNGs preserve all frame alpha, with 167/166 ms quantization for 6 FPS.
Decoded GIF frame count/timing and decoded APNG pixel equality were checked.

## DDS and coverage proof

The canonical `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` converted every sheet and static PNG.
The six final files are one-level legacy uncompressed BGRA32.
All six have a 128-byte header, DDSD flags 0x100F, a pixel-format block at byte 76 with size 32 and flags 65, the correct BGRA/alpha masks, and texture caps 0x1000.
Exact file lengths are 524416 bytes for each eight-frame sheet, 393344 bytes for the warning sheet, and 65664 bytes for each static.
Strict raw BGRA and independent Pillow decodes match the processed PNG pixels with zero RGBA and alpha mismatches.
The decoded sheets, statics, and 22 individual decoded frame slices are retained in each family's `qa/roundtrip/`.
Full hashes and converter commands are in the JSON manifests and QA metrics.

| Family | Manifest and coverage rows | QA evidence | Sprite handoff |
| --- | --- | --- | --- |
| Front | `front/manifest.md`; `front/animation_manifest.json` | `front/qa/metrics.json`; native/source/processed/DDS contacts; repair comparison | `front/gfx_handoff.md` |
| Warning | `warning/manifest.md`; `warning/animation_manifest.json` | `warning/qa/metrics.json`; native/source/processed/DDS contacts | `warning/gfx_handoff.md` |
| Severe | `severe/manifest.md`; `severe/animation_manifest.json` | `severe/qa/metrics.json`; native/source/processed/DDS contacts | `severe/gfx_handoff.md` |

Each family has original/master PNGs, processed per-frame PNGs, sheet/static PNGs, final sheet/static DDS, review GIF and alpha-preserving APNG, per-frame metadata/hashes, contact sheets, strict DDS roundtrips, a Markdown/JSON manifest, and a GFX handoff.
The retained mechanical processor is `front/qa/build_marker_package.py`, restricted to the three named families and their exact runtime paths.
It never creates the underlying artwork.
Reproduction uses `python -B <processor> --family front|warning|severe --record-producer-review` only after review of the same immutable masters.

## Exact consumer and canonical reference evidence

The canvas is taken from the existing preserved animation brief, not guessed from a reference icon.
The current registrations are `interface/033_acid_rain.gfx` lines 59-64; SHA-256 at handoff is `a24cba2e9b7c4b567a96c0d1731ac97ee136e48cf41db0f8e03fef8bff29b7f6`.
The current GUI consumer SHA-256 is `77c002339d30c671f25efca40b28b1a22d0cb5658ca2bb7536384050c5271fdd`; exact matched animated consumer lines are retained per family.
The static sprites are registered; the parent owns the motion-disabled/static selection binding and its final state coverage.

The one canonical shelf is `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/gfx_references`.
The relevant decision-category and idea contact sheets were inspected before `decision_category_generic_crisis.png` and `idea_generic_purge.png`.
The catalog identifies both as Vanilla HOI4 review material at lines 204 and 240; catalog SHA-256 is `5016985236132e8b0cd5c4392b7bde54de806f8ae960b0161a3a2e14d295aa29`.
No canonical reference art or visual-component layer is composited into the runtime markers.

The installed vanilla declaration is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/theatreselector.gfx` lines 171-183, `GFX_active_phase_anim`, with `gfx/interface/unitcontrol/active_phase_anim.dds`.
The vanilla source SHA-256 is `8207e84538725b05a4c0b438e06adedc2b585653a76f85c5df3e0cbfcf055367`.
The offline wiki rules read are Graphical asset modding lines 101-139 and Interface modding lines 178-195; their source revisions are in each JSON manifest.
The local installed-documentation search found no dedicated `frameAnimatedSpriteType`/FPS prose rule, so the exact installed declaration supplies the primary engine precedent.

The reference context/search/source-lookup routes were verified as exposed, but the combined read-only requests returned no result before cancellation after repeated waits.
Relevant local sections and source declarations were read directly and the route gap is retained.
No source-only result is described as live/in-engine GUI validation.

## Disposition, risks, and remaining ownership

Completed production: three animated markers and three static representatives.
Blocked production items: none.
Needs parent review: all six assets' art approval, final animated/static visibility coverage, and the orchestrator's GUI/live evidence.
The original exact September generation prompt gap is resolved for all 22 owned marker originals by the bounded session recovery below.
Original PNGs/hashes and authored frame states remain separate evidence, and every October repair prompt is retained exactly.
The GIF palette and timing limits affect only human previews; the runtime DDS retains full alpha and the registered FPS.
No animation simplification or unapproved fallback was used.

Skills used: `chaos-redux-event-assets`, `chaos-redux-frame-animation`, and the official `imagegen` skill.
No skill was created or modified.

## Bounded original-prompt recovery — 2026-10-03

All 22 exact submitted September 4 marker prompts were recovered from the original `chaosx_icon_artist` rollout, whose metadata names the agent “Focus Icons.”
The original session ID is `01a06dc0-ab15-7902-86b5-adbd0619ac52`; its parent thread ID is `01a04e71-3c1f-7003-b1bd-0110e2d26f21`.
The source record is `C:\Users\klimp\.codex\sessions\2026\09\04\rollout-2026-09-04T21-49-01-01a06dc0-ab15-7902-86b5-adbd0619ac52.jsonl`, metadata at line 1, SHA-256 `ce4950cc8285e0690fde529df77ecf884139b3c394fc9847ee990b3a799c9e4b`, 168897431 bytes.
The submitted wrapper requests call `tools.image_gen__imagegen`; exact prompt literals were copied verbatim or decoded from their static JSON-compatible JavaScript string literals, with no frame-plan reconstruction and no session code execution.

The bounded search checked the preserved repository prompt directory and PNG metadata, then searched only the September 4 Codex rollout directory for the exact owned original-source filenames.
The repository prompt directory is empty and all 22 owned PNGs have no embedded prompt metadata.
Two rollouts matched the filenames; the original icon-artist rollout contains the submitted requests and output/copy proof, while the other match is the Event UI worker.
The recovery stopped after resolving all 22 originals; neighboring dates and archived records were not scanned.

| Family | Actual submitted request lines | Actual returned output lines | Exact prompts recovered | Generated PNG/source byte-hash matches | Retained evidence |
| --- | --- | --- | ---: | ---: | --- |
| Front | 301–448 | 310–459 | 8/8 | 8/8 | `front/animation_manifest.json`, `original_prompt_recovery.frames` |
| Warning | 468–552 | 475–563 | 6/6 | 6/6 | `warning/animation_manifest.json`, `original_prompt_recovery.frames` |
| Severe | 572–700 | 579–707 | 8/8 | 8/8 | `severe/animation_manifest.json`, `original_prompt_recovery.frames` |

Each recovery entry retains the exact submitted prompt, request call ID/timestamp/line hash, actual referenced-image argument, actual transparent-background argument disposition, actual returned output hint/path and output-record citation, and the explicit exec/wait association when the request yielded.
The original source-copy mapping is the submitted copy operation at line 858; each owned mapping entry is retained verbatim.
All 22 returned PNG files still exist in `C:/Users/klimp/.codex/generated_images/01a06dc0-ab15-7902-86b5-adbd0619ac52/`, and their full SHA-256 values equal the corresponding preserved `source_frames/` originals.
This binds the archived requests and returned output IDs to the supplied original art without substituting a description or a source hash for the actual prompt.

The seed returned-output paths are:

| Family/frame | Actual ImageGen returned path | Request → output record |
| --- | --- | --- |
| Front 000 | `C:/Users/klimp/.codex/generated_images/01a06dc0-ab15-7902-86b5-adbd0619ac52/exec-ca33366e-f0f7-4933-a6e9-b1452673f2ad.png` | 301 → 310 |
| Warning 000 | `C:/Users/klimp/.codex/generated_images/01a06dc0-ab15-7902-86b5-adbd0619ac52/exec-fc195f37-d7e7-42b5-b1a0-8ac4d4bdb05d.png` | 468 → 475 |
| Severe 000 | `C:/Users/klimp/.codex/generated_images/01a06dc0-ab15-7902-86b5-adbd0619ac52/exec-c2c2ab46-b7ef-48b4-b236-b84a41b757bb.png` | 572 → 579 |

Full returned paths and exact prompt text for every non-seed frame are in the three owned JSON manifests.
The September request wrappers omitted the structured `transparent_background` argument in all 22 calls, while their literal prompt text requested real transparency.
The omission is retained as an observed fact, without claiming an unrecorded true argument, default, or backend model.
The source alpha outcomes and the two already documented October front repairs remain separate evidence.
Historical prompt wording such as “approved seed” is not treated as current parent approval.

The parent clarified that Part 10 count names are suggested, and the asset prompt permits front 8–12, warning 6–8, and severe 8.
The current 8/6/8 package conforms to those allowed ranges.
All parent frame/art approval and final integration statuses remain pending; this recovery performs no new generation or runtime asset change.
There are no unavailable exact original prompts remaining within the three owned marker families.

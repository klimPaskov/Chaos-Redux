# Holy Mandala Asset Manifest

Status: `implemented`; the parent approved all seven 218px sixteen-frame contacts on 2026-10-06, and all fourteen BGRA32 candidate DDS files were promoted to their exact runtime paths.

## Consumer and output contract

The consumer is `holy_realm_mandala_core`, selected through `GetHolyRealmMandalaSprite` and registered by `interface/003_holy_realm.gfx`. Target frame size is 420x420. Each animated sheet is 6720x420 with 16 left-to-right frames at 8 fps, looping over two seconds. Existing static and animated sprite names and paths remain unchanged. The static fallback is processed frame 000. Parent owns final GFX, GUI, and gameplay wiring.

Every finished frame must have native transparent unused canvas. All current baseline DDS files are fully opaque; the prior meditation static is RGB. No background-removal fallback is used for the newly generated art. Atlas v1 is preserved as a rejected framing attempt. Atlas v2 is an animation-source atlas with sixteen individually drawn smoke poses and real alpha; crop and visual QA are still required.

ImageGen route: built-in `image_gen__imagegen`, with referenced local art anchors. The tool exposes no model selector. No backend model name is claimed. The frame atlas is one state per generation call; no call combines multiple state assets.

## Reference evidence

Inspected the canonical `icons/decision_categories/contact_sheet.png` before `decision_category_generic.png`. Inspected `visual_components/CATALOG.md`, `national_spirit_backgrounds/contact_sheet.png`, and `decision_category_background_blue_roundel.png`. That component is 52x40 and does not fit the 420x420 standalone Mandala GUI emblem, so no background component layer is used. Existing Mandala assets are preserved separately as design cues and rejected baselines, never as final source frames.

The expected source archive `docs/assets/003_holy_realm_buddhahood/animations/` was absent. The only prior workflow record found is `docs/plans/003_holy_realm_plans/subagent_handoffs/2026-06-13_holy_mandala_state_animation_rebuild.md`, which identifies the prior motion as a glow pulse derived from one fixed image.

## Preserved previous runtime files

All files below are archived byte-for-byte in `previous_rejected_dds/`. SHA-256 digests refer to the archived copy. Dimensions and alpha were read by Pillow DDS decode; `opaque` means alpha extrema `(255, 255)`.

| Asset | Previous static DDS | Previous animated DDS |
| --- | --- | --- |
| dormant | `holy_realm_mandala_dormant.dds`, 420x420 RGBA, 176528 bytes, opaque, `B637D9C4730A072F1338F216C828688417F1997E5851072880763A4184382EB0` | `holy_realm_mandala_dormant_animated.dds`, 6720x420 RGBA, 1411328 bytes, opaque, `D19FED1D8B3128DBA6D3C08AA03FCE6D040A6F9FCF6ED98E166935E7F08B8A99` |
| teaching | `holy_realm_mandala_teaching.dds`, 420x420 RGBA, 176528 bytes, opaque, `EF7C6F90DC1658F6F865AFDAA8E93FAAA62F9F18E59C57ACFF2B06B257B78748` | `holy_realm_mandala_teaching_animated.dds`, 6720x420 RGBA, 1411328 bytes, opaque, `E5EEB514D2AB715A8DAF06AA643199AC27857470D9E2A168729FB8280F10F457` |
| meditation | `holy_realm_mandala_meditation.dds`, 420x420 RGB, 529328 bytes, opaque, `534856CA0DAB0052A11D8D70AD1AE337D8315E796328C1688E4696B1BC827786` | `holy_realm_mandala_meditation_animated.dds`, 6720x420 RGBA, 1411328 bytes, opaque, `67A0DC251BB5E95800D8945A6CD701E583B9E4E9CBD6B82612193D50E6E0DE4A` |
| awakened | `holy_realm_mandala_awakened.dds`, 420x420 RGBA, 176528 bytes, opaque, `CBDB13C7CB0705AF047C6214ED3354544418A25B02380DAD3E67ED4944A89732` | `holy_realm_mandala_awakened_animated.dds`, 6720x420 RGBA, 1411328 bytes, opaque, `341B584112747DF8DAA3BCD762C2699C3C7D9B116C71673B940456F92271128B` |
| wrathful | `holy_realm_mandala_wrathful.dds`, 420x420 RGBA, 176528 bytes, opaque, `A69C582E166654A392C966A4DF2E88169BF738D20DBB160F1A6C19463744277D` | `holy_realm_mandala_wrathful_animated.dds`, 6720x420 RGBA, 1411328 bytes, opaque, `35CC9DEF34986E6E0171001373CB68A059A03167A53E06E44EAA7EDF58089EFA` |
| final_silence | `holy_realm_mandala_final_silence.dds`, 420x420 RGBA, 176528 bytes, opaque, `25B37B4983A103A464532BE88A2DAEE68C5ABA03DDA65D9736ADA52999F2B01D` | `holy_realm_mandala_final_silence_animated.dds`, 6720x420 RGBA, 1411328 bytes, opaque, `D4D847D3E67A6D7D50CE94B8325B11E4415D66AFD83598AD3FAF0778B973434D` |
| empty | `holy_realm_mandala_empty.dds`, 420x420 RGBA, 176528 bytes, opaque, `5184ED824FA06167EB91A863492EBC49995FB147816CD1B5D08C922F81D09840` | `holy_realm_mandala_empty_animated.dds`, 6720x420 RGBA, 1411328 bytes, opaque, `6F0752DFA21885E815D547755635908D40521C572C103F928D09A7E7BB697025` |

## Generated candidate lineage

`source_atlases/dormant_atlas_v1_rejected_framing.png` is the initial ImageGen atlas. It is preserved as rejected because the medallions nearly touched cell boundaries. `prompts/dormant_atlas.txt` records its original prompt.

`source_atlases/dormant_atlas_v2_candidate.png` is the targeted ImageGen framing repair of v1. It is 1254x1254 RGBA with alpha extrema `(0, 255)` and SHA-256 `6F8B9AB2A37A5FE6D010E917FED81BF9FD5CC08216F0C8E365503474E94791D1`. `prompts/dormant_atlas_v1_framing_repair.txt` records the edit prompt. The provisional cell contact is `contact_sheets/dormant_v2_slices_check.png` with SHA-256 `B2A2EBED605B650BEE3293A45413D05EC7AF105CEAF9BF72CBFF72D8C5F0011A`.

## Current seven-state preview package

The selected source atlases are `dormant_atlas_v3_edge_repair.png`, `teaching_atlas_v2_framing_edge_repair.png`, `meditation_atlas_v2_framing_edge_repair.png`, `awakened_atlas_v2_framing_edge_repair.png`, `wrathful_atlas_v2_framing_edge_repair.png`, `final_silence_atlas_v2_framing_edge_repair.png`, and `empty_atlas_v2_framing_edge_repair.png` under `source_atlases/`. Each atlas is 1254x1254 RGBA and supplies 16 separately drawn states in reading order.

Each state has 16 raw source-cell crops, 16 processed 420x420 PNG frames, one 6720x420 sheet PNG, one static fallback PNG, one native preview GIF, one production-panel 218px preview GIF, and four contact sheets: native 420, 4x 1680-per-frame, 218px dark, and 218px light gray. `notes/frame_metadata.json` records exact crop rectangles, padding offsets, alpha bounds, per-frame hashes, sheet paths, distinct-pose counts, loop boundary deltas, and preview timing.

The initial ImageGen alpha was genuine but carried colored edge specks. Targeted ImageGen transparency-edge edits were attempted for the affected atlases and did not remove all spill. The verified local fallback therefore cleans each raw source cell with `rembg 2.0.61`, cached `isnet-general-use.onnx`, `alpha_matting=False`, and `post_process_mask=False`. The exact model path and SHA-256, actual 218px panel crop and sampled `#17202A` background, and frame lineage are recorded in `notes/frame_metadata.json` and `generation_provenance.md`. Preserved native source atlases and raw frame crops remain separate from cleaned processed frames.

All 14 DDS files were produced in `candidate_dds/` with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, using uncompressed BGRA / `B8G8R8A8_UNORM`. `notes/dds_roundtrip_report.json` records strict decode and exact pixel-roundtrip results for every static and animated DDS, four-channel masks, per-file hashes, and the package digest. After parent approval on 2026-10-06, each candidate was copied to its exact runtime path; `notes/runtime_promotion_report.json` confirms all runtime hashes match the pixel-exact candidates. The pre-repair DDS binaries remain preserved in `previous_rejected_dds/`.

The full parent review index is `preview_index.md`. `notes/runtime_promotion_report.json` records the accepted package hash and final runtime hash matches. The exact owned force-add file list is `notes/force_add_files.txt`. `gfx_handoff.md` and the plan-folder handoff identify the unchanged sprite names, current consumer and state selector, runtime paths, acceptance status, and exact owned file list. This worker changed only the fourteen authorized runtime DDS files; it did not edit `.gfx`, `.gui`, gameplay, localisation, or any unrelated runtime path.

The separate GUI worker reports its post-change MCP render timed out without artifacts; final matched GUI rendering remains a parent evidence gate. This asset package is complete, but no in-game completion claim is made.

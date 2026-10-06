# Holy Mandala ImageGen Provenance

Image generation used the built-in `image_gen__imagegen` tool. Its live schema had no model selector, so no backend model name is claimed. Every generation and edit call requested `transparent_background = true`. No paid alternate generator was used.

The attached local reference for each family is `source_references/previous_<state>_first_animated_frame.png`, a decoded first cell from the preserved old runtime sheet. It transfers only the general Mandala geometry, material, and state palette. Its opaque backdrop, haze, glow, and pixel artwork are excluded. The previous runtime DDS binaries and these reference decodes are preserved separately.

| State | First source-atlas prompt | First generated original | Framing/edge-edit prompt | Edited ImageGen output |
| --- | --- | --- | --- | --- |
| dormant | `prompts/dormant_source_atlas.txt` | `C:/Users/klimp/.codex/generated_images/01a10e13-df0c-74f1-8eab-0663ddd51cfd/exec-767b209a-750b-44f0-b436-777612200006.png` | `prompts/dormant_atlas_v1_framing_repair.txt`, then `prompts/dormant_edge_repair.txt` | `exec-d5ed2542-b205-4c74-9dac-8c8e1cdd0ce7.png`, then `exec-486e22c4-e6cc-47ce-b433-eb6afb89f8b8.png` in the same generated-images folder |
| teaching | `prompts/teaching_source_atlas.txt` | `exec-0ec888d3-0fe1-4562-9170-55eefb317152.png` in the generated-images folder | `prompts/teaching_framing_edge_repair.txt` | `exec-2443333c-e051-42d6-ac9a-1df25c57c1f5.png` in the generated-images folder |
| meditation | `prompts/meditation_source_atlas.txt` | `exec-d6f9a117-1022-47e5-9461-94d0ac69c81b.png` in the generated-images folder | `prompts/meditation_framing_edge_repair.txt` | `exec-b0f231f1-9acf-4ae5-b968-5f43f30cdc4c.png` in the generated-images folder |
| awakened | `prompts/awakened_source_atlas.txt` | `exec-08afa525-6960-4a2b-a7f8-b564276b710c.png` in the generated-images folder | `prompts/awakened_framing_edge_repair.txt` | `exec-e463769c-887f-458f-98e9-c71cd8c697d1.png` in the generated-images folder |
| wrathful | `prompts/wrathful_source_atlas.txt` | `exec-2c29ff45-3b2e-437b-a059-ee6d6987943e.png` in the generated-images folder | `prompts/wrathful_framing_edge_repair.txt` | `exec-222d9a51-04d7-47f1-8a26-3c14de4eed33.png` in the generated-images folder |
| final_silence | `prompts/final_silence_source_atlas.txt` | `exec-aebcdc25-a791-477f-84b3-4e0aed801153.png` in the generated-images folder | `prompts/final_silence_framing_edge_repair.txt` | `exec-88806cad-33ad-491d-9e0d-e629334f9cd1.png` in the generated-images folder |
| empty | `prompts/empty_source_atlas.txt` | `exec-1577e2fe-795d-45e1-bb9f-12d2a86b38b1.png` in the generated-images folder | `prompts/empty_framing_edge_repair.txt` | `exec-2b65e234-858e-4110-a011-4e564b6cdb2f.png` in the generated-images folder |

Dormant atlas v1 is separately retained as `source_atlases/dormant_atlas_v1_rejected_framing.png`; it was rejected because the complete Mandala nearly touched the atlas cell edges. The three dormant generations form a preserved candidate lineage rather than a replacement of the original source.

All seven ImageGen source atlases contain 16 individually drawn poses. Their source atlas pixels are preserved. The `source_frames/` files are exact crop cells. Uniform cell padding and 420x420 resizing normalize the atlas grid and consumer anchor only; no local translation, scaling, rotation, warping, blur, recoloring, or glow pulse creates the animation.

Initial native-alpha outputs and the first targeted ImageGen edge edits retained stray red, green, or yellow fringe pixels. The selected processed frames therefore use the verified local edge-removal fallback after the ImageGen edits. The installed tool is `rembg 2.0.61`; the cached model is `C:/Users/klimp/.u2net/isnet-general-use.onnx`, 178648008 bytes, SHA-256 `60920E99C45464F2BA57BEE2AD08C919A52BBF852739E96947FBB4358C0D964A`. Settings are `alpha_matting=False` and `post_process_mask=False`. One representative cell from every state was inspected after cleanup on the exact production dark panel and on light gray before processing the complete families.

The production-panel diagnostic uses the unscaled MCP crop `docs/plans/003_holy_realm_plans/subagent_handoffs/gui_release_20261005_evidence/gui_render_before_refuge_19360101_cropped.png`, 471x484 at UI scale 1.0. The empty icon rectangle was cleared to its measured surrounding color `#17202A` before compositing the candidate; the crop is not used as artwork or wired content.

Parent acceptance: on 2026-10-06 the parent reviewed all seven 218px sixteen-frame contact sheets, approved the stage identities, centered circles, readable cloth/smoke/petal/fire/ash poses, and clean dark/light alpha edges, and authorized promotion of all fourteen DDS files to the existing runtime paths.

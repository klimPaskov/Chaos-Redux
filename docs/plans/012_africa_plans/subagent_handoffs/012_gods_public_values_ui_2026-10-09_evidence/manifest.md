# Event 012 Gods of Africa public-value UI reference manifest

Disposition: `implemented` source with specific preview limitations recorded in the current implementation handoff. The parent viewed and accepted both integrated v4 native ImageGen references and sent `PROCEED` before engine implementation. The later participant crop acceptance is scoped to that exact48/38 image, not final overall/hover/multiscale completion.

These opaque PNGs are compositional references only. They are not runtime panels, sprites, backgrounds, or final asset art.

The exact source art preview supplied for integration is `docs/assets/012_africa/gods_public_values_ui/category_picture_native_preview.png`, 114x101 pixels, SHA-256 `00ba993dae9878710a18dd6442be4287511dbba19028c3ac683b9ce2579897b8`. It is a decoded preview of the existing category-picture DDS and guides the composition reference; runtime must use the registered sprite.

## Parent-accepted overall references

| Candidate | Path | Dimensions | SHA-256 | State | Prompt record | ImageGen source |
| --- | --- | --- | --- | --- | --- | --- |
| Participant overall normal | `docs/assets/012_africa/gods_public_values_ui/participant_with_picture_reference_v4.png` | 2163x727 | `eb72e986119f9160e8dbdd8725b7e75db1e99176dff52a3664e8bf507d141cd4` | `parent_accepted` | `reference_prompt_participant_with_picture_v4.md` | `C:\Users\klimp\.codex\generated_images\01a11ac5-6943-7a50-a08d-978b6a8f5558\exec-d6de2da9-0f03-44a6-a585-ba9c0ff1a9f5.png` |
| Host overall normal | `docs/assets/012_africa/gods_public_values_ui/host_with_picture_reference_v4.png` | 2172x724 | `687195983eda773ac89b45651a1ecda8cee4576a9fafd38ea456634979179535` | `parent_accepted` | `reference_prompt_host_with_picture_v4.md` | `C:\Users\klimp\.codex\generated_images\01a11ac5-6943-7a50-a08d-978b6a8f5558\exec-96ab0d3c-0101-4b6b-b0e1-60b1cb88ce32.png` |

## Parent-reviewed row-composition references

| Candidate | Path | Dimensions | SHA-256 | State | Role |
| --- | --- | --- | --- | --- | --- |
| Participant rows, neutral initial state | `docs/assets/012_africa/gods_public_values_ui/participant_reference_v3.png` | 2172x724 | `36668c42383adc177385d9541452c223a1f81be65403a566e4cb3788b41891ee` | `parent_accepted` | Row hierarchy, copy, bands, thresholds, and Steady trend; superseded only as the overall composition because it has no picture region. |
| Host row, neutral initial state | `docs/assets/012_africa/gods_public_values_ui/host_reference_v4.png` | 2172x724 | `da459f3afe86601ecf69d3dc4cbc5a84ec847b076b00ea6d9127bc170bac4543` | `parent_accepted` | Strength row hierarchy; its implementation-language lower-row copy is superseded by `The Gods can reach several states.` in the integrated host reference. |

## Alternate trend-state references

| Candidate | Path | Dimensions | SHA-256 | State | Prompt record | ImageGen source |
| --- | --- | --- | --- | --- | --- | --- |
| Participant with movement | `docs/assets/012_africa/gods_public_values_ui/participant_reference_v2.png` | 2172x724 | `545d15e4efa33cbf75939e3dbb64ac866827420f632a0ccea3f1622c9ca1fcda` | `supporting_study`, alternate to neutral initial state | `reference_prompt_participant_v2.md` | `C:\Users\klimp\.codex\generated_images\01a11ac5-6943-7a50-a08d-978b6a8f5558\exec-682706be-c5d0-4e12-abe8-dc158daf142c.png` |
| Host with movement | `docs/assets/012_africa/gods_public_values_ui/host_reference_v2.png` | 2172x724 | `61190b0ea8c7c43a1495f13ffa84c932462cdd5341316af43adebf7259b2b3dd` | `supporting_study`, alternate to neutral initial state | `reference_prompt_host_v2.md` | `C:\Users\klimp\.codex\generated_images\01a11ac5-6943-7a50-a08d-978b6a8f5558\exec-96a50aa6-14f1-4e56-b36f-96cb790f4ce9.png` |

## Rejected reference candidates

| Candidate | Path | SHA-256 | Disposition | Reason | Prompt record |
| --- | --- | --- | --- | --- | --- |
| Participant attempt 0 | `docs/assets/012_africa/gods_public_values_ui/participant_reference_attempt0.png` | `6363c33159dce5d30b6a107bd4c9ab8e56df416f1d4b2508f6265e84b8d5a775` | `rejected` | The first ImageGen output was not surfaced into the project at generation time. It was later recovered, reviewed, and rejected because it paired Strength 68 with Continental reach. The exact v1 prompt was saved after this first call and before a repeated v1 generation, so this candidate records a prompt-capture timing deviation. | `reference_prompt_participant_v1.md` |
| Participant v1 | `docs/assets/012_africa/gods_public_values_ui/participant_reference_v1.png` | `977fe96633c733b5eb5a8e04f36b3ed7a70b78d4d4acc1ca83d514d42d345aac` | `rejected` | The example paired Strength 68 with Continental reach and a Global threshold at 80. The accepted constants place 68 in Global reach, so the example was corrected. | `reference_prompt_participant_v1.md` |
| Host v1 | `docs/assets/012_africa/gods_public_values_ui/host_reference_v1.png` | `761ef81e73ef00b2eceec4d800122f06c13fbe8954231ecee416bfec762dc5f9` | `rejected` | It repeated the same invalid Strength band example. | `reference_prompt_host_v1.md` |
| Host v3 | `docs/assets/012_africa/gods_public_values_ui/host_reference_v3.png` | `7e3074c6a9e743e2bc76ea6c95905bb64d51fa1402a6fb535c8332d927d16ea7` | `rejected` | The second row repeated the Strength band already shown in the meter. The strip-only host v4 changed that copy, and the integrated host reference later replaced its implementation-language phrase with the accepted in-world reach line. | `reference_prompt_host_v3.md` |

## Superseded integrated composition candidates

| Candidate | Path | Dimensions | SHA-256 | Disposition | Reason |
| --- | --- | --- | --- | --- | --- |
| Participant with picture v1 | `docs/assets/012_africa/gods_public_values_ui/participant_with_picture_reference_v1.png` | 2172x724 | `1b40f67e365922166bebcd86de9c2ece7588afe9c1b8c17ca559754675174b67` | `superseded` | Correct art-left layout, but its painted fills were shorter than the requested 48% Strength and 38% Wrath. |
| Host with picture v1 | `docs/assets/012_africa/gods_public_values_ui/host_with_picture_reference_v1.png` | 2172x724 | `81a1791031b656e0ad1be57f6bb9cb338f73e5e1ac2957394aa56ed2e4284017` | `superseded` | Correct art-left layout and in-world reach copy, but its painted Strength fill was short of the requested 48%. |
| Participant with picture v3 | `docs/assets/012_africa/gods_public_values_ui/participant_with_picture_reference_v3.png` | 2164x727 | `7407f06929e92097d7a3e86414104c82df1db9badc063689ba190436dbb6ea93` | `superseded` | Constrained proportion prompt still produced visibly short fills; v4 corrects the relative lengths. |

## Source inputs and production route

The references used built-in native ImageGen with `transparent_background = false` because each image is an opaque composition study. The selected v4 participant and host prompts explicitly constrain the rail fills to 48% Strength and 38% Wrath; the visible fills are reference cues, while the native GUI must read the exact observer caches.

The built-in ImageGen tool did not expose a model, quality, size, or destination selector, so this manifest records only the actual built-in execution route and returned output paths.

The integrated participant v4 used the superseded participant composition, the exact 114x101 native DDS preview at `category_picture_native_preview.png`, the original picture source at `docs/assets/012_africa_gods_of_africa/source/decision_cat_picture_012_africa_gods.png`, and the existing processed Strength and Wrath icon PNGs. The integrated host v4 used the prior host composition, the same exact preview and source, and the existing Strength icon.

The host reference used the participant composition as a style and layout input and the existing Strength icon as its motif input.

Runtime icon registrations remain `GFX_012_africa_gods_strength` and `GFX_012_africa_gods_wrath` in `interface/012_africa.gfx`, with source DDS files under `gfx/interface/012_africa/gods_of_africa/`.

No new illustrated icon, background, animation, portrait, or 3D asset was produced. The implemented static meter requires `gods_public_values_meter_101.dds`,101 data-selected frames compiled from the exact selected vanilla subject-rail textures by `build_native_meter_frames.py`; it is not an animated asset or ImageGen runtime art.

The native 114x101 preview depicts the exact existing sprite registered as `GFX_decision_cat_picture_012_africa_gods` in `interface/012_africa_event_pictures.gfx:20`. ImageGen output is a composition study; implementation must place that existing sprite in the left region once and must not wire generated scene pixels as replacement art. The first native picture-only capture established the existing sprite inside the widget before both category `picture =` assignments were removed. The post-removal capture retained the same widget image; current source consumes the exact picture sprite once. Exact revisions and validation limits are in the implementation handoff.

The reference canvas scales from about 2172x724 to 502x167, matching the actual 502-unit decision-category slot. The host picture treatment is near the existing 114x101 size; the participant art region is modestly larger to accommodate the two meter rows while keeping the same compact hierarchy. The panel borders and metal texture are cues only. Runtime uses the ordinary category surface and verified native progress or frame-meter assets.

The original `view_image` DDS probe was unsupported and `texconv` was unavailable. Subsequent MCP images and Pillow decoding established the selected subject-rail pixels; the final static-frame asset reuses those source textures and its endpoints/sample frames were checked against them. That early route limitation is resolved for this selected asset; automatic native tooltip positioning and other bounded review limits remain in the handoff.

The parent reviewed `participant_with_picture_reference_v4.png` and `host_with_picture_reference_v4.png` and explicitly sent `PROCEED` before implementation. The strip-only references remain supporting row-layout studies. The parent subsequently reviewed and accepted only `mcp_frame_final_cropped.png`, SHA `5fb3ad49bacf7748c7a6011b06671f46f3fa9c773f488ddc78a4a277202ddbbf`, source revision `fadc0bc0e30e7867220daae540ecf9eda5f77a40f1fbc616d77ba5b1b75a0d6f`, for the participant502-width48/38 crop. Broader latest-source acceptance is not inferred.

## Current implementation evidence

See `docs/plans/012_africa_plans/subagent_handoffs/012_gods_public_values_ui_reference_2026-10-08.md` for the native mapping, exact source hashes, eight fixture identities, reviewed images, references, scope, and finite remaining check limitations.
`mcp_final_render_manifest.json` preserves the exact final render request/result and artifact URIs; `mcp_embedded_scenario_images.json` and `mcp_resolution_images.json` identify native PNGs extracted unchanged from returned matrix SVGs.
The accepted crop, full canvas, scenario/resolution matrices, underlying native PNGs, and detail crops remain in this directory.
The last capture precedes the inclusive next-tick correction; that source fix is verified in `threshold_review.json` and is not represented as recaptured.

The runtime meter DDS is `gfx/interface/012_africa/gods_public_values_meter_101.dds`, referenced by `interface/012_africa_gods_public_values.gfx`.
The identical workspace copy is retained as source evidence and is not a runtime dependency.
Frame1/49/39/81/86/101 represent0/48/38/80/85/100percent, using the parent-approved floor-plus-one caches and SOV-style `frame` properties.
Stored frames160x14 are scaled to181x15.8375 logical units, preserving layout at y44 and markers at y42.
The compiled asset is derived from installed Paradox subject-rail artwork; no third-party artwork/license was added, and existing picture/icon provenance remains unchanged.

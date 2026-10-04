# Event 023 Soviet nuclear bombs promoted decision-icon replacements

Production date: 2026-10-03.

Package status as of 2026-10-03: `fixed (parent DDS/native approved/runtime promoted)` for these six decision icons.
The parent accepted the selected sources and native DDS presentation and copied all six selected DDS files to the existing runtime destinations.
Actual live consumer validation and MCP category acceptance remain pending.
The 75-asset inventory count is unchanged, its full review remains incomplete, and this package does not establish Event 23 completion.

Acceptance basis: The parent explicitly authorized original image generation and replacement for these six decision icons because the old icon prompt set is absent from the checkout and history. The parent locked the six basenames, sprite names, runtime DDS paths, and exact 33x32 RGBA target. Prompts in this package are new lineage and do not claim to reconstruct old prompts.
The parent's explicit 2026-10-03 reconciliation instruction supplies the final selection, completed review, promotion facts, and six runtime hashes.
The parent opened all six initial source masters, storage v2, all six actual decoded DDS files, processed native and 4x previews, and storage neutral-composited native and 4x previews including a bilinear preview.
The parent accepted storage v2 low-alpha antialiasing after RGBA pixel proof and neutral previews.
The [dated documentation and promotion ledger](../../../plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_six_decision_icon_promotion_documentation_2026-10-03.md) preserves this acceptance basis, runtime hashes, archive checks, and validation limits.

## Consumer and reference evidence

The exact consumer is the existing Event 23 registration in interface/023_sov_nuclear_bombs.gfx. It defines the six sprites listed below and points them at gfx/interface/decisions/023_sov_nuclear_bombs/<basename>.dds. The parent retains runtime promotion and all GFX editing.

The canonical family inspected was .agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decisions/. Its contact_sheet.png was opened before the individual reference. The family has 15 references. The individual reference decision_generic_intelligence_operation.png is cataloged as Vanilla HOI4, 33x32, at CATALOG.md line 221, with SHA-256 f07c9c6d8d5c2f2b7d61c1fd45f92134cc1e0cdcbe324ecf75ed1dc3c1ab5c5.

The installed vanilla definition interface/decisions.gfx lines 1017-1020 maps GFX_decision_generic_intelligence_operation to gfx/interface/decisions/decision_generic_intelligence_operation.dds. The installed DDS is 33x32, a 4352-byte legacy BGRA32 one-level file, with alpha range 0-255 and SHA-256 651370037967bf198f8f4c33ab6d8ae3a3cd499cfed4d1d2483720cbc4027bab. Its decoded pixels exactly equal the canonical reference PNG.

The visual component catalog was inspected after the exact consumer and icon-reference family. Its decision-category background template does not apply to ordinary decision icons. No visual component layer was used. Canonical reference art was not attached to ImageGen and is not used in the final art.

## Current requirement-to-runtime crosswalk, 2026-10-03

| Requirement / decision-icon token | Exact existing sprite | Selected DDS in this package | Promoted runtime DDS path | Owning registry | Current status |
| --- | --- | --- | --- | --- | --- |
| sov_nuclear_decision_accounting | GFX_decision_sov_nuclear_decision_accounting | dds/sov_nuclear_decision_accounting.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_accounting.dds | interface/023_sov_nuclear_bombs.gfx | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_storage_hardening | GFX_decision_sov_nuclear_decision_storage_hardening | dds/sov_nuclear_decision_storage_hardening.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_storage_hardening.dds | interface/023_sov_nuclear_bombs.gfx | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_reactor_construction | GFX_decision_sov_nuclear_decision_reactor_construction | dds/sov_nuclear_decision_reactor_construction.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_reactor_construction.dds | interface/023_sov_nuclear_bombs.gfx | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_device_assembly | GFX_decision_sov_nuclear_decision_device_assembly | dds/sov_nuclear_decision_device_assembly.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_device_assembly.dds | interface/023_sov_nuclear_bombs.gfx | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_delivery_preparation | GFX_decision_sov_nuclear_decision_delivery_preparation | dds/sov_nuclear_decision_delivery_preparation.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_delivery_preparation.dds | interface/023_sov_nuclear_bombs.gfx | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_command_exercise | GFX_decision_sov_nuclear_decision_command_exercise | dds/sov_nuclear_decision_command_exercise.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_command_exercise.dds | interface/023_sov_nuclear_bombs.gfx | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |

## Generation and alpha handling

Each icon has its own ImageGen source PNG and exact prompt record under prompts/. The static source calls were separate built-in image_gen.imagegen calls with transparent_background=true and no image references. Storage hardening v2, v3, and v4 are separate native ImageGen edits of retained generated sources. Their exact target-image lineage is recorded in prompts/generation_trace.md.

The selected source PNGs are 1274x1234 or 1274x1235 for the five initial selections and 1273x1236 for storage v2, as recorded in the table below. It exposed no model, size, quality, or destination selector and returned no model identifier. The generated originals remain in the tool's default generated_images folder, and byte-identical source copies are retained here. No background-removal fallback was used.

The generated sources are RGBA with native transparent corners and alpha range 0-255. Processing used a deterministic content crop around source alpha greater than 8, expanded by 24 source pixels, then one uniform fit into a 29x28 box on an exact 33x32 transparent RGBA canvas. Resampling was Lanczos in premultiplied RGBA mode. No local painting, recoloring, matte, mask, or checkerboard was introduced into the art. The crop bounds below are left, top, right, bottom in source pixels.

| Asset stem | Selected source PNG | Source size | Source alpha bbox >0 | Visible bbox alpha >8 | Crop bounds | Uniform scale | Processed alpha bbox | Processed PNG SHA-256 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sov_nuclear_decision_accounting | source_png/sov_nuclear_decision_accounting.png | 1274x1235 | 0,9,1232,1235 | 85,51,1230,1184 | 61,27,1254,1208 | 0.02370872 | 2,2,30,30 | ce95d7f1f5302bde09404cfaf7a2364190e891b536a9885e57587e97d9c2948c |
| sov_nuclear_decision_storage_hardening | source_png/sov_nuclear_decision_storage_hardening_v2.png | 1273x1236 | 0,22,1064,1203 | 215,24,1061,1200 | 191,0,1085,1224 | 0.02287582 | 6,2,26,30 | d660b415a6bf45a036286fc763ea603285c510b03f8b04e00e29de2c6367719a |
| sov_nuclear_decision_reactor_construction | source_png/sov_nuclear_decision_reactor_construction.png | 1274x1234 | 82,55,1226,1234 | 84,62,1222,1142 | 60,38,1246,1166 | 0.02445194 | 2,2,31,30 | fe6b59e026dcbcc8f86507ab9153c5bf38cf1efb216245689d08f5f3c8cb7754 |
| sov_nuclear_decision_device_assembly | source_png/sov_nuclear_decision_device_assembly.png | 1274x1234 | 37,21,1208,1234 | 66,204,1199,1096 | 42,180,1223,1120 | 0.02455546 | 2,4,31,27 | ba866e3dd1eb8c6ad88b28abd043611a20401b9a4fffa969a267a1b3ce2030e5 |
| sov_nuclear_decision_delivery_preparation | source_png/sov_nuclear_decision_delivery_preparation.png | 1274x1235 | 0,52,1258,1193 | 10,354,1256,879 | 0,330,1274,903 | 0.02276295 | 2,9,31,22 | fcc50901addb49e848eaf36c0b2b60e0aae21e25f1d60ecae8cdc71a52a8213c |
| sov_nuclear_decision_command_exercise | source_png/sov_nuclear_decision_command_exercise.png | 1274x1234 | 0,49,1234,1234 | 57,201,1231,1080 | 33,177,1255,1104 | 0.02373159 | 2,5,31,27 | 10c5d81cccbfb3dd46e3c81aa8c4adfbf93aa854e247952416725b45a9eb8dbb |

Every processed PNG is exactly 33x32 RGBA, has alpha range 0-255, and has alpha zero at all four corners. Exact full-source and prompt lineage, including unselected storage edits, is in prompts/generation_trace.md.

## DDS conversion and round-trip proof

All six processed PNGs were converted with .agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py. Each candidate is a 4352-byte, 33x32, one-level legacy BGRA32 DDS with the expected BGRA masks, no mipmaps, alpha range 0-255, and zero alpha in the four canvas corners. Each DDS was strictly decoded and its RGBA pixels exactly matched its processed PNG.

| Asset stem | Candidate DDS | DDS SHA-256 | Round-trip pixel equality | Review status |
| --- | --- | --- | --- | --- |
| sov_nuclear_decision_accounting | dds/sov_nuclear_decision_accounting.dds | 0be0929d3377e6df511b0d454adf9e55697630defcd17dc725aa25c68e216fcb | exact | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_storage_hardening | dds/sov_nuclear_decision_storage_hardening.dds | a8d463b8534fbaed6a9299249a81bf035feb9eab95ccaafd8b29aef0299e55d1 | exact | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_reactor_construction | dds/sov_nuclear_decision_reactor_construction.dds | 0222ae3e4ff29767c3ef7b6cc4b87e1db1400d18b8ee98b7426e94d4c2ec691c | exact | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_device_assembly | dds/sov_nuclear_decision_device_assembly.dds | 52f5bdd904baf270b20b395701049b1c567d0d1cc5001ecfc106ac7bb0773495 | exact | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_delivery_preparation | dds/sov_nuclear_decision_delivery_preparation.dds | 1c276d5ba65392ee915fa650b453bf95a0b3ec22e6505877a31cf07e26ab137f | exact | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |
| sov_nuclear_decision_command_exercise | dds/sov_nuclear_decision_command_exercise.dds | d659b2d2fa09c74573223dde9d10a7c618509201633c9ead40f18c35989d3eb1 | exact | fixed (parent DDS/native approved/runtime promoted). Live consumer pending |

For every stem, the exact decoded RGBA PNG is review/<stem>_dds_roundtrip.png. Neutral-background, alpha-composited review images are review/<stem>_dds_neutral_1x.png, review/<stem>_dds_neutral_4x_nearest.png, and review/<stem>_dds_neutral_4x_smooth.png. These display composites are review-only. The retained round-trip PNG remains RGBA and is separate. The processed sources also have 1x and 4x review previews.

review/contact_sheet.png shows each source master, the 33x32 processed icon, the 33x32 DDS round trip, nearest-neighbour 4x, smooth 4x, source alpha bounds, crop bounds, scale, and review state. review/storage_hardening_edge_lineage_4x.png shows the RGBA-composited upper-edge crops of storage v1-v4 at 4x nearest-neighbour. The initial incorrectly sized edge-sheet attempt is retained as review/storage_hardening_edge_lineage_layout_failed_v1.png and is not the selected contact sheet.

## Storage-edge lineage and parent acceptance, 2026-10-03

The immutable v1 source has RGBA (255,0,0,1) at source pixel (320,24). The v2 ImageGen edit has (0,0,0,0) at that coordinate. The parent reports that the surrounding upper-edge pixels are mostly alpha 2-3. V2 is the selected source used for the current processed PNG and promoted DDS.
The parent accepted its remaining low-alpha upper-edge antialiasing after reviewing the retained RGBA source, decoded DDS, and neutral-background native and 4x previews including bilinear enlargement.
This is a bounded parent visual acceptance of v2 and does not assert that every retained source is defect-free.

Storage v3 and v4 are retained, unselected ImageGen edit outputs with exact prompts and hashes in prompts/generation_trace.md. Their full-resolution upper edges still show colored fringe and they were not used to build the current processed PNG or DDS. No further regeneration, local painting, recoloring, background removal, or silent alpha cleanup was applied.

## Visual findings and remaining consumer validation

Accounting reads as a closed blank leather ledger with one muted red seal cue at 33x32. Storage reads as a bolted closed depot door. V2 corrects the documented red alpha-1 sample, with remaining low-alpha upper-edge antialiasing accepted by the parent after RGBA and neutral-preview review. Reactor construction reads as a compact industrial vessel with pipework and a small construction cue, without glow or facility scenery. Device assembly reads as a heavy cylindrical casing on a cradle with one wrench cue. Delivery preparation reads as a period propeller bomber with one subordinate bomb cue. Its aircraft silhouette is horizontally elongated at the 33x32 target. Command exercise reads as a period field telephone with one key cue.

All six selected icons are `fixed (parent DDS/native approved/runtime promoted)` after parent review and promotion on 2026-10-03.
Live consumer validation remains pending and no current MCP category artifact is claimed.
The parent reported an absent namespace and current handshake gap in its own context.
In this curator session `mcp__hoi4_agent_tools__hoi4_decision_inspect` was exposed, but its read-only category inventory call timed out awaiting `tools/call` after 600 seconds and returned no artifact.
Tool exposure and a validation response do not establish service health, a standalone viewer, or current consumer acceptance.
The production worker did not edit runtime or GFX files, and the later runtime copies were performed by the parent.
This curator pass edits documentation only and does not repeat asset production or DDS visual validation.


## Promotion transaction and historical custody

The parent archived each pre-promotion runtime DDS under `runtime_before_promotion/<basename>.dds` before copying the six selected DDS files to runtime.
The parent reports that preflight matched every old runtime file to `../dds/gfx/interface/decisions/023_sov_nuclear_bombs/<basename>.dds` before overwrite.
The curator subsequently verified six candidate/runtime SHA-256 matches against the exact hashes above and six archive/legacy-mirror SHA-256 matches.
Those legacy mirrors, old `../source_png/decisions/<basename>_source.png` masters, and old `../processed_png/decisions/<basename>_33x32.png` previews remain retained historical archives and do not represent the six current source-to-runtime chains.
No files were deleted.
The existing `GFX_decision_sov_nuclear_decision_<stem>` registrations in `interface/023_sov_nuclear_bombs.gfx` remain unchanged and point only to runtime `gfx/` paths.

The [producer handoff](../../../plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_production_decision_icon_replacements_v1_2026-10-03.md) is preserved unchanged as candidate-stage evidence from worker `01a1019f-bdd2-7ac1-8d52-38edf0cd5c77`.
Its candidate-only and pending parent-edge-acceptance claims are `superseded` as current status by this dated promotion suffix and the [current reconciliation handoff](../../../plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_six_decision_icon_promotion_documentation_2026-10-03.md).
Its production and source-lineage evidence remains applicable.
Storage v1, v3, and v4 remain unselected historical branches with their exact prompts and hashes preserved.

The six initial prompt records are `prompts/sov_nuclear_decision_<stem>.md` for the six stems in the crosswalk.
Storage's selected edit prompt is `prompts/sov_nuclear_decision_storage_hardening_v2_edit.md`, and unselected edit prompts retain the v3 and v4 filenames.
[prompts/generation_trace.md](prompts/generation_trace.md) records exact call IDs, input roles, tool-returned paths, retained source paths, and source hashes.
The prompt records preserve the new period-object briefs and restrained palettes, while the processing table preserves exact bounds, scale, and alpha purpose.
The original `../prompts/icon_prompt_set.md` remains missing and unrecovered, and prompt-coverage repair for other legacy icons remains unresolved.

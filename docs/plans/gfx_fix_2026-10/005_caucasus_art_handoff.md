# Event 005 Caucasus Focus Art Handoff

Status: four original focus icons are generated, processed to 94x86, converted to DDS, and handed off for parent promotion.

The parent reviewed the native and enlarged review sheets and confirmed that all four subjects pass framing, readability, distinctness, and no-lettering review.

The production evidence and per-candidate lineage are in [new_art_manifest.json](../../assets/005_soviet_collapse/gfx_fix_caucasus/new_art_manifest.json), and the complete source, prompt, processed PNG, DDS, and review package remains under [gfx_fix_caucasus](../../assets/005_soviet_collapse/gfx_fix_caucasus/).

| Focus | Selected original subject | Existing sprite aliases | Staged DDS | Runtime DDS path |
| --- | --- | --- | --- | --- |
| `caucasus_soviet_collapse_mountain_artillery_schools` | Period mountain howitzer with spoked wheels, shells, and Caucasus ridges; matches the artillery equipment, army experience, and bunker rewards. | `GFX_focus_caucasus_soviet_collapse_mountain_artillery_schools`, `GFX_focus_caucasus_soviet_collapse_mountain_artillery_schools_shine` | [DDS](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_dds/focus_005_caucasus_soviet_collapse_mountain_artillery_schools.dds) | `gfx/interface/goals/005_soviet_collapse/focus_005_caucasus_soviet_collapse_mountain_artillery_schools.dds` |
| `caucasus_soviet_collapse_the_border_war_cabinet` | Three officers' caps, dispatch folders, and an unlabeled mountain route map under a brass desk lamp; reads as command and command-power support. | `GFX_focus_caucasus_soviet_collapse_the_border_war_cabinet`, `GFX_focus_caucasus_soviet_collapse_the_border_war_cabinet_shine` | [DDS](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_dds/focus_005_caucasus_soviet_collapse_the_border_war_cabinet.dds) | `gfx/interface/goals/005_soviet_collapse/focus_005_caucasus_soviet_collapse_the_border_war_cabinet.dds` |
| `caucasus_soviet_collapse_tbilisi_baku_yerevan_talks` | Three distinct city-seal vignettes around a blank treaty scroll and compact talks table; the scroll has no lettering or pseudo-writing. | `GFX_focus_caucasus_soviet_collapse_tbilisi_baku_yerevan_talks`, `GFX_focus_caucasus_soviet_collapse_tbilisi_baku_yerevan_talks_shine` | [DDS](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_dds/focus_005_caucasus_soviet_collapse_tbilisi_baku_yerevan_talks.dds) | `gfx/interface/goals/005_soviet_collapse/focus_005_caucasus_soviet_collapse_tbilisi_baku_yerevan_talks.dds` |
| `caucasus_soviet_collapse_the_compact_holds_the_ridge` | Stone ridge watchpost, winding defended road, and one joined three-ring compact seal; reads as enduring mountain security. | `GFX_focus_caucasus_soviet_collapse_the_compact_holds_the_ridge`, `GFX_focus_caucasus_soviet_collapse_the_compact_holds_the_ridge_shine` | [DDS](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_dds/focus_005_caucasus_soviet_collapse_the_compact_holds_the_ridge.dds) | `gfx/interface/goals/005_soviet_collapse/focus_005_caucasus_soviet_collapse_the_compact_holds_the_ridge.dds` |

The selected source PNGs are [mountain artillery](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_sources/mountain_artillery_schools_candidate02.png), [border cabinet](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_sources/the_border_war_cabinet_candidate01.png), [capital talks](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_sources/tbilisi_baku_yerevan_talks_candidate03.png), and [ridge compact](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_sources/the_compact_holds_the_ridge_candidate01.png).

The exact ImageGen prompts and focused-edit deltas are retained in `generated_prompts/`; every candidate is preserved as a separate immutable source in `generated_sources/` with the tool-reported output path, local SHA-256, dimensions, alpha bounds, input roles, review disposition, and prompt hash recorded in the manifest.

The [DDS round-trip contact sheet](../../assets/005_soviet_collapse/gfx_fix_caucasus/generated_reviews/native_dds_roundtrip_contact_sheet.png) shows each parent-baseline icon, the native-alpha ImageGen source preview, processed PNG, decoded DDS, dark and light background reviews, and smooth 3x baseline/output comparisons.

All selected source PNGs use native alpha with a 0-255 alpha range, and every staged 94x86 PNG and DDS has transparent unused canvas with no nonzero alpha at the final canvas edge.

For source cleanup, the processor used the alpha>=8 subject bounds plus a 16-pixel guard, enlarged the guard if necessary to preserve every outside-crop pixel above alpha 1, and applied uniform premultiplied-alpha Lanczos resizing into an 88x80 aperture before centering on a transparent 94x86 canvas.

That bounded transparent-canvas crop dropped no source pixel above alpha 1; the ridge candidate's 382 excluded alpha-1 edge specks are recorded in `generated_reviews/alpha_bounds_and_processing.json`, and no blanket erosion, background removal, opaque matte, anisotropic scaling, or visible-content crop was used.

The repository converter [convert_to_dds.py](../../../.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py) produced four legacy one-level BGRA DDS files, each 32,464 bytes with a 128-byte header, 94x86 dimensions, 32-bit BGRA masks, texture caps, and alpha range 0-255.

Each final DDS decoded to 94x86 and matched its processed PNG pixel-for-pixel; strict header, alpha, and round-trip evidence is in the manifest and alpha-processing report.

The canonical `icons/national_focus/contact_sheet.png` was inspected before individual canonical focus references, then the selected Vanilla references and the `visual_components` catalog and focus-piece/background contact sheets were inspected; only the two canonical Vanilla PNGs were ImageGen style inputs, and no component layer was used.

The existing sprite declarations remain in `interface/005_soviet_collapse_focus_icons.gfx`: mountain artillery at lines 2648-2649, talks at 2674-2675, border cabinet at 2680-2681, and ridge compact at 2684-2685.

All four current runtime DDS hashes still match the parent-provided pre-change `baseline.json`; the generated DDS files are staged only under `generated_dds/` for promotion to those exact paths.

The six parent-staged framing DDS repairs and their evidence files were left untouched; the parent can promote these four subject replacements with that reviewed framing tranche.

`hoi4_focus_inspect` returned the Caucasus tree with 40 focuses and no changed files, but its overall validation was false because the source inventory included an unrelated installed-game brace diagnostic at `game:common/national_focus/TSR_lingguang_incident_joint_branch.txt:469`.

The narrow `hoi4_focus_raster` request returned an empty result object without status or artifacts, so the parent-provided `caucasusBeforeRaster.json` remains the available before-raster evidence until the parent promotes these files and rerenders the tree.

The parent owns promotion and the post-change MCP comparison; the user owns live-game validation.

No gameplay, focus, localisation, GUI, `.gfx`, spreadsheet, or runtime DDS files were edited here, and no commit was created.

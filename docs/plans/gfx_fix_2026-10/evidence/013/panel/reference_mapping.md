# Event 013 damaged panel reference and native mapping

Acceptance basis: the parent task authorizes the accepted Event 013 GFX review row, based on the user's plan, which directs readable cracked glass over the main pane, a soot mark in one corner, a torn left paper edge, and unchanged layout grid. The parent reviewed candidate 04 at native 760x520 against the saved original and accepted its distinct light pane crack, localized damage, and preserved five-slot grid.

Baseline reference: docs/assets/gfx_fix_parent_2026-10/013_damaged_before.png, the decoded existing damaged-panel texture at 760x520.

Intended reference and selected candidate: source_png/013_damaged_candidate_04.png, retained at 1516x1038 with a 1.4605 aspect ratio, closely matching the 760x520 target's 1.4615 aspect ratio.

Native-size processed preview: processed_png/013_abnormal_disaster_panel_damaged_760x520.png.

| Reference region | Native GUI element and usable bounds | Content and interaction | Asset and state | Constraint or adaptation |
|---|---|---|---|---|
| Full panel canvas, 760x520 | The top-level window natural_disaster_abnormal_path_window is 1087x744; its background icon layers start at 0,0 and scale to 1.43. | Opaque decorative background only; text, cards, paths, markers, detail content, buttons, legend, and severity labels remain native HOI4 elements. | GFX_013_abnormal_disaster_panel_damaged, used by natural_disaster_gui_damaged_panel in the damaged record-result state. | Preserve canvas ratio and all compartment and grid positions; do not bake text, controls, values, or hit regions into the art. |
| Largest central pane, approximately source x154-538/y60-434 | The path canvas uses natural_disaster_gui_animated_layers and natural_disaster_gui_static_layers at x270-740/y102-442; marker controls occupy native slots over that canvas. | The crack is background decoration. Map paths, marker icons, labels, and click regions remain separate native controls. | Candidate 04 adds fine hairline cracks with one small impact point in the pane's upper-left area. | Keep the central usable area mostly clear; the crack is thin and does not replace or draw map information. |
| Extreme upper-right outer rim, approximately source x741-759/y0-44 | The header status ends at x926 in the 1087-wide window; the soot cue is at the far outer rim beyond that text region and outside the right detail pane. | Decorative background only; it creates no control or state. | Candidate 04 adds one small soot smudge in the damaged state only. | Keep the soot out of the vent, header text, right detail pane, and usable content. |
| Narrow outside-left trim beside the five cards, approximately source x10-28/y190-360 | The five card slots are separate native containers at x40-182 with their own labels and transparent button hitboxes. | The tear affects only the outer paper trim; card frames, labels, click regions, count, and spacing remain unchanged. | Candidate 04 has a short frayed edge on the left-side trim. | The torn texture stays outside the five functional card faces and does not alter their logical or painted bounds. |
| Other background zones | The right detail panel is at x798-1062/y94-613; the lower legend and severity areas are at y640-725. | All values, text, selection, timeline, progress, buttons, hover behavior, and costs remain native or parent-owned. | Unchanged normal panel is GFX_013_abnormal_disaster_panel; damaged state is selected when the result entry is greater than the normal result. | No layout, localization, gameplay, cost, AI, click-region, or shared-interface changes are authorized in this asset task. |

State mapping: natural_disaster_gui_normal_panel is visible when natural_disaster_gui_record_result_entries for the selected record equals constant:natural_disaster_gui_record_result.normal. natural_disaster_gui_damaged_panel is visible when that value is greater than normal. The selection is drawn by the event's record array; when the MCP route cannot resolve those arrays, the parent-authorized preview fixture may explicitly override the two visibility predicates for matched normal and damaged captures.

Resolution matrix: 1920x1080 at UI scale 1.0 and 1366x768 at UI scale 1.0, as supplied by the parent.

The panel uses an opaque background because its inspected consumer fills the complete window canvas. No transparency removal or fake-control workaround was used.

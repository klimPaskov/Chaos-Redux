# Compact selected-location card reference

Status: generated reference for a narrow presentation cleanup, not runtime art.

Acceptance basis: the user rejected the expensive fixed costs and debug-like presentation on 2026-09-05, within the already authorized repression GUI repair.
The parent reviewed this generated reference and accepted its compact identity header, grouped actions, consistent insets, and truthful status area as implementation choices within that scope.
The precise two-column arrangement and header treatment are parent-selected design choices, not details explicitly specified by the user.

Reference: [reference_compact.png](reference_compact.png), one full-window 960x600 PNG with the revised right card.

## Inputs and provenance

Current full-render source: `docs/plans/system_camp_repression_rework_plans/ui_polish_2026-09-05/after_308/repression_ledger_window-cropped.png`.

Current full-render dimensions: 992x632.

Current full-render SHA-256: `C2835C2264F2ABE50C71DA4E615FCB9DBD310E0C1E794251D974CC0D246BBA55`.

User-supplied card crop: `C:/Users/klimp/AppData/Local/Temp/codex-clipboard-918ff3eb-7026-44d4-b370-20cf98158057.png`.

User-supplied crop dimensions: 411x463.

User-supplied crop SHA-256: `E79BCDC17466FEF79A8F34510A3D58A390BB4B12EBBEC01219339997B165BC27`.

Generation method: official built-in ImageGen edit using the current full render as Image 1 edit target and the user-supplied crop as Image 2 supporting card reference.

ImageGen output before resampling: `C:/Users/klimp/.codex/generated_images/01a06e6d-a5d3-7a80-a12d-f53bea5b3ac9/exec-cca9abdd-e4bc-4a50-8f2c-f5eec790a611.png`.

ImageGen output dimensions: 1586x992.

ImageGen output SHA-256: `7D30CD43BB23CFDCCD6B6BE6325664EAFDE4F2C8B6F59EF2B0E738EEA0AEC89B`.

The ImageGen output was high-quality resampled to the requested 960x600 review canvas with System.Drawing using HighQualityBicubic interpolation.

Final file: `docs/plans/system_camp_repression_rework_plans/ui_polish_2026-09-05/reference_compact.png`.

Final dimensions: 960x600.

Final SHA-256: `340B36E015DE1BD57CA90285A28232E52757B6F6D7D14A8ED42E9E950B4451E6`.

## ImageGen prompt

```text
Use case: ui-mockup
Asset type: review-only reference image for a native Hearts of Iron IV inspired scripted GUI cleanup
Primary request: Edit Image 1 into one compact polished reference image for the existing 960x600 repression ledger window. Change only the right selected-location card, whose in-window footprint is approximately 396x460; keep the entire left navigation column, center operating-sites list, title bar, close X, and outer window visually unchanged. Use Image 2 as the close design reference for the card’s intended compact hierarchy.
Input images: Image 1 is the current full-window edit target. Image 2 is the user-supplied selected-location card crop and a supporting layout reference.
Scene/backdrop: opaque dark charcoal-black brushed metal panel with subtle fine grain, restrained beveled HOI4-style borders, no scene behind the window.
Subject: the existing selected-location card for Brandenburg detention.
Style/medium: polished in-game grand-strategy interface mockup, faithful to the supplied native panel and button textures, functional implementation feasible with ordinary HOI4 window, panel, text, button, and list controls.
Composition/framing: preserve the full 960x600 window and every control outside the right card. Inside the right card, remove the large empty gap below the header. Replace the generic header “SELECTED LOCATION” with a prominent “BRANDENBURG” title and concise “DETENTION” subtitle. Reserve a compact top status area under that subtitle for truthful selected-site status and civilian-losses labels using short descriptive text only, with no invented numerical balance. Arrange the six existing actions in a balanced 2-column by 3-row grid of equal-width groups with consistent insets and gutters. Each group contains a normal dark inset panel area, one real-looking native button, and its cost row or rows consistently below that button inside the same group. Cost text and tiny resource glyphs are preview guidance only; retain the source’s existing visible cost style or omit numbers where needed, but invent no new budget values.
Lighting/mood: subdued institutional, utilitarian, low glare.
Color palette: near-black charcoal, gunmetal, muted olive selection accents, warm off-white labels, restrained yellow cost numerals, tiny muted resource glyphs.
Text (verbatim): retain the six existing action names exactly: “Labor Works”, “Inspect”, “Dismantle”, “Destroy Records”, “Contaminated Order”, “Outbreak Order”. Use “BRANDENBURG” and “DETENTION” for the card header. Status labels may be concise generic text such as “SITE STATUS” and “CIVILIAN LOSSES” without invented figures.
Constraints: keep control identity, existing six actions, dark vanilla HOI4 texture and native-button style; keep all other UI unchanged; no new controls, no removed controls, no extra tabs, no portraits, no people, no scenes, no modern website UI, no animation, no effects, no decorative symbols, no invented numerical balance, no watermarks. The image is a design reference only, not runtime art.
```

## Native control map and usable insets

The exact owning source is `interface/camp_repression_ledger.gui`.

The parent window is `repression_ledger_window`, centered at `position = { x = -480 y = -300 }` with `size = { width = 960 height = 600 }`.

The in-scope card is the existing noninteractive `containerWindowType` `camp_ui_selected_location` at `position = { x = 530 y = 116 }` with `size = { width = 396 height = 460 }` and existing opaque `GFX_tiled_window_small` background.

Use a compact content inset of approximately 14–16 px from the card’s left and right edges and approximately 12–16 px from its top and bottom edges.

The header region uses the existing dynamic text owner `repression_ledger_selected_state_text` for the live selected-site identity and the existing `camp_ui_selected_status` text owner for concise live status copy; the generic `camp_ui_selected_heading` string should not remain as a standalone “SELECTED LOCATION” title in this selected-site state.

Reserve approximately the first 104–112 px inside the card for the Brandenburg title, Detention subtitle, a divider, and compact status/civilian-losses labels with live parent-owned values.

Reserve approximately the remaining 320–332 px for six noninteractive inset group backgrounds arranged in two equal columns and three equal rows.

Use approximately 8–10 px between columns and rows, with each group approximately 176–180 px wide and 96–100 px tall inside the card’s usable width.

Inside every group, center the existing `GFX_button_148x34` control horizontally near the top with approximately 10–14 px top inset, then place its existing cost text owner directly below within the same group with approximately 6–8 px vertical separation.

The six existing action mappings are:

| Group | Button ID | Existing cost text ID | Display label | Suggested native role |
| --- | --- | --- | --- | --- |
| row 1, column 1 | `camp_gui_start_labor_project` | `camp_ui_cost_start_labor_project` | Labor Works | interactive `buttonType` with live validation and cost text |
| row 1, column 2 | `camp_gui_inspect_selected_site` | `camp_ui_cost_inspect_selected_site` | Inspect | interactive `buttonType` with live validation and cost text |
| row 2, column 1 | `camp_gui_dismantle_selected_site` | `camp_ui_cost_dismantle_selected_site` | Dismantle | interactive `buttonType` with live validation and cost text |
| row 2, column 2 | `camp_gui_destroy_evidence` | `camp_ui_cost_destroy_evidence` | Destroy Records | interactive `buttonType` with live validation and cost text |
| row 3, column 1 | `camp_gui_chemical_method` | `camp_ui_cost_chemical_method` | Contaminated Order | interactive `buttonType` with live validation and cost text |
| row 3, column 2 | `camp_gui_biological_method` | `camp_ui_cost_biological_method` | Outbreak Order | interactive `buttonType` with live validation and cost text |

The visual inset group backgrounds are presentation containers only and must not add interaction, duplicate buttons, or invent a second action surface.

The existing `camp_gui_expand_selected_pool` alternate action remains parent-owned state logic and is outside this normal selected-site six-action reference state.

## Adaptation and review caveats

The generated image is a reference for the parent’s native HOI4 layout work and must not be wired as a texture, sprite, GFX entry, localisation asset, or gameplay dependency.

The card crop and generated image use existing visible yellow cost rows only as preview guidance; those numbers are not a balance decision or gameplay authority.

The status area intentionally uses short descriptive labels without invented numerical civilian-loss values; the parent must bind actual calculated values and appropriate localisation when implementing it.

ImageGen can introduce minor raster drift outside the requested card region, so the current full render and source GUI remain authoritative for all surrounding UI and exact control identity.

The parent owns native GUI edits, localisation alignment, dynamic cost and status wiring, MCP inspection/render evidence, and matched scenario comparison.
Live game validation belongs to the user.

No GUI, GFX, localisation, gameplay, DDS, or runtime files were edited for this reference.

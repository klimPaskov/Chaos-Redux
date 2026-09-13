# Repression ledger UI polish reference

Status: generated reference for narrow presentation cleanup, not runtime art.

The reference image is [reference.png](reference.png), an opaque 960x600 PNG for the existing repression ledger scripted GUI.

## Source and method

Source image: `docs/plans/system_camp_repression_rework_plans/ui_review_2026-09-05/sites_all_orders-repression_ledger_window-cropped.png`.

Source dimensions: 992x632.

Source SHA-256: `B8ECD34488DEB035C9058BF50CB58137BC939943A57FF8F18263FA9A02BD4D26`.

Source role: edit target and composition authority.

Generation method: official built-in ImageGen edit using the source screenshot as the sole referenced image and an opaque consumer background.

ImageGen output before resampling: `C:/Users/klimp/.codex/generated_images/01a06e6d-a5d3-7a80-a12d-f53bea5b3ac9/exec-c962d406-410f-41a6-8507-b46d3daac503.png`.

ImageGen output dimensions: 1586x992.

ImageGen output SHA-256: `F996AAE84327A50CE8498365E751F861FF035663857AA53BF16B29FB6D3D233C`.

The generated image was high-quality resampled to 960x600 with System.Drawing using HighQualityBicubic interpolation and retained as an opaque PNG.

Final file: `docs/plans/system_camp_repression_rework_plans/ui_polish_2026-09-05/reference.png`.

Final dimensions: 960x600.

Final SHA-256: `89F0317811E0DC3B670E7C48138E93FCDE1D6171F8D8E793BDFF699B993A4499`.

## Prompt

```text
Use case: ui-mockup
Asset type: review-only reference image for a Hearts of Iron IV inspired scripted GUI cleanup
Primary request: Perform a narrow presentation polish pass on Image 1, preserving its exact existing window composition and all controls. Create one opaque 960x600 reference image with the same dark installed HOI4 panel/button style. Improve only alignment, spacing, and readability: center the five left navigation labels within their buttons, balance panel gaps and insets, make the two right-side action columns equal width with consistent gutters, center every action label within its button, and keep each yellow cost line comfortably below its own button with clear vertical separation from the next action row.
Input images: Image 1 is the current repression ledger screenshot and is the edit target plus sole composition reference.
Scene/backdrop: dark charcoal-black brushed metal and subtle fine-grain HOI4 interface panel, restrained beveled steel borders, low contrast, no scene behind the window.
Subject: the existing repression and camps management window as a functional game UI.
Style/medium: polished in-game strategy interface mockup, faithful to the supplied screenshot, compact readable sans-serif and restrained small caps.
Composition/framing: preserve the existing centered 960x600 window proportion and all current regions: title bar with close X; left navigation column; middle operating-sites list; right selected-location panel with a two-column action grid.
Lighting/mood: subdued institutional, utilitarian, slightly ominous, even low-glare lighting.
Color palette: near-black charcoal, gunmetal, muted olive selection highlight, warm off-white labels, restrained yellow cost numerals, tiny muted resource glyphs.
Materials/textures: subtle metal grain and bevels only; no decorative ornament.
Text (verbatim): "REPRESSION AND CAMPS"; "Camp Administration • Active"; left labels "Situation", "Territories", "Sites", "Policy", "Accountability"; center heading "OPERATING SITES"; site rows "Brandenburg", "Niederbayern", "Upper Silesia", "Rhineland", "Saxony", "Westphalia"; center helper "Choose a site to inspect its status or issue an order."; right labels "SELECTED LOCATION", "BRANDENBURG", "DETENTION", "Review the orders below."; action labels "Labor Works", "Inspect", "Dismantle", "Destroy Records", "Contaminated Order", "Outbreak Order".
Constraints: preserve every current control, row, title, close X, selected Sites state, and dark panel hierarchy; no new controls, no removed controls, no concept redesign, no portraits, no people, no scenes, no maps, no flags, no symbols, no illustrations, no extra ornament, no watermarks, no modern UI conventions. This is a visual reference only, not final runtime art. Keep text concise and readable at the displayed scale.
```

## Adaptation caveats

This is a raster reference for the parent agent’s native GUI cleanup and must not be wired as a texture, sprite, GFX entry, localisation asset, or gameplay dependency.

The existing screenshot remains authoritative for control identity, state, and wording; the generated image is guidance for centered labels, balanced insets and gutters, equal action columns, and cost spacing.

ImageGen lettering is reference-grade and should be checked against existing localisation when the parent implements the native layout.

No GFX, GUI, localisation, gameplay, or runtime asset files were edited for this reference.

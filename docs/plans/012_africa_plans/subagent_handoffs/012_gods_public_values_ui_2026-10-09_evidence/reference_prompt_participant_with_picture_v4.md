# Integrated participant reference prompt v4

Execution record: generated to `C:\Users\klimp\.codex\generated_images\01a11ac5-6943-7a50-a08d-978b6a8f5558\exec-d6de2da9-0f03-44a6-a585-ba9c0ff1a9f5.png` and copied to `participant_with_picture_reference_v4.png` as the selected participant composition pending parent review.

Candidate: constrained meter-fill correction to the native ImageGen composition reference.

Use case: ui-mockup. This is a composition reference only, never runtime art.
Inputs: Image 1 is the compact participant composition; Image 2 is the exact 114x101 existing category-picture preview; Image 3 is its original art source; Images 4 and 5 are the existing Strength and Wrath icon references.
Edit only the two gold meter-fill endpoints and their threshold ticks. Preserve the complete layout, text, colors, rails, icons, picture treatment, and dark panel exactly as they appear in Image 1. Keep all picture art in its separate left region. The runtime uses the exact existing `GFX_decision_cat_picture_012_africa_gods` sprite.
For each rail, take the usable inner track as 100 equal units. The Strength fill must occupy exactly units 1–48 (48%) and its tick must sit at unit 60. The Wrath fill must occupy exactly units 1–38 (38%) and its tick must sit at unit 50. Both tracks have the same total length, and the Wrath fill is exactly 10 percentage points shorter. Extend the current fills to those endpoints; do not leave either at its present shorter length.
Keep all current text verbatim: Strength; 48 / 100; Continental reach; Steady; Next: Global reach at 60; Wrath; 38 / 100; Angered; Steady; Next: Hostile at 50. No other changes, added elements, or removed elements.

ImageGen request arguments:

- `transparent_background`: `false`
- `referenced_image_paths`: `participant_with_picture_reference_v3.png`; `category_picture_native_preview.png`; `docs/assets/012_africa_gods_of_africa/source/decision_cat_picture_012_africa_gods.png`; `docs/assets/012_africa_gods_icons/processed/strength.png`; `docs/assets/012_africa_gods_icons/processed/wrath.png`
- Model/quality/size/destination controls: not exposed by built-in ImageGen

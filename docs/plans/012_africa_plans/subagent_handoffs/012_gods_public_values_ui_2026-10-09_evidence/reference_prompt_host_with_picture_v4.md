# Integrated host reference prompt v4

Execution record: generated to `C:\Users\klimp\.codex\generated_images\01a11ac5-6943-7a50-a08d-978b6a8f5558\exec-96ab0d3c-0101-4b6b-b0e1-60b1cb88ce32.png` and copied to `host_with_picture_reference_v4.png` as the selected host composition pending parent review.

Candidate: constrained Strength-fill correction to the native ImageGen composition reference.

Use case: ui-mockup. This is a composition reference only, never runtime art.
Inputs: Image 1 is the compact host composition; Image 2 is the exact 114x101 existing category-picture preview; Image 3 is its original art source; Image 4 is the existing Strength icon reference.
Edit only the Strength gold meter-fill endpoint and its threshold tick. Preserve the complete layout, text, colors, rail, icon, picture treatment, and dark panel exactly as they appear in Image 1. Keep all picture art in its separate left region. The runtime uses the exact existing `GFX_decision_cat_picture_012_africa_gods` sprite.
Take the rail's usable inner track as 100 equal units. The Strength fill must occupy exactly units 1–48 (48%) and its next-threshold tick must sit at unit 60. Do not shorten the fill to make room for copy.
Keep all current text verbatim: Strength; 48 / 100; Continental reach; Steady; Next: Global reach at 60; Doctrine: Reciprocal Covenant; The Gods can reach several states. No other changes, added elements, or removed elements.

ImageGen request arguments:

- `transparent_background`: `false`
- `referenced_image_paths`: `host_with_picture_reference_v1.png`; `category_picture_native_preview.png`; `docs/assets/012_africa_gods_of_africa/source/decision_cat_picture_012_africa_gods.png`; `docs/assets/012_africa_gods_icons/processed/strength.png`
- Model/quality/size/destination controls: not exposed by built-in ImageGen

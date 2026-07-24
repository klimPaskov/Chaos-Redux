# Event 020 Black Plague decision icon prompts

The decision-icon family uses the official built-in image generator in generated mode. Each source was requested as a single centered, hand-painted Hearts of Iron IV-style object on a flat `#ff00ff` chroma-key background so the repository imagegen helper could produce real alpha. No generated text, watermark, frame, or extra object was requested.

## New source prompts

### `decision_quarantine_imagegen_source.png`

Single centered hand-painted HOI4-style icon of a heavy quarantine barricade gate with a small warning lantern and sealed medical seal, viewed straight-on. Warm desaturated brown, iron gray, and muted red palette; strong black outline, subtle painterly shading, compact silhouette, no text.

### `decision_cordon_imagegen_source.png`

Single centered hand-painted HOI4-style icon of two crossed wooden road barriers with a small military armband marker, clearly a cordon. Warm brown wood, iron gray, muted red accent, strong black outline, subtle painterly shading, compact silhouette, no text.

### `decision_treatment_reserves_imagegen_source.png`

Single centered hand-painted HOI4-style icon of a wooden medical supply crate with two glass ampoules and a folded bandage, representing treatment reserves. Muted tan wood, dark green glass, cream cloth, strong black outline, compact readable silhouette, no text.

### `decision_warren_purge_imagegen_source.png`

Single centered hand-painted HOI4-style icon of a shovel and burning torch thrust toward a dark rat burrow entrance, representing purge warrens. Brown iron tools, ember orange flame, charcoal earth, clear silhouette, thick black outline, subtle painterly shading, no gore, no text.

### `decision_countermeasure_program_imagegen_source.png`

Single centered hand-painted HOI4-style icon of a glass laboratory flask behind a sturdy medical shield, representing a countermeasure program. Muted teal glass, brass rim, deep blue-gray shield, tiny amber liquid, strong black outline, compact icon silhouette, no text.

### `decision_doctor_wu_protocol_imagegen_source.png`

Single centered hand-painted HOI4-style icon of a sealed physician's protocol folder with a stylized medical seal and small fountain pen, representing Doctor Wu protocol. Aged paper, dark leather, brass seal, muted red stamp shape without letters, thick black outline, simple readable silhouette, no text.

### `decision_doctor_wu_foreign_access_imagegen_source.png`

Single centered hand-painted HOI4-style icon of a medical passport and open gate with a small globe motif, representing foreign medical access. Aged blue-gray document, brass gate, muted green globe, bold black outline, compact silhouette, no readable text or flags.

## Preserved source concepts

The eight existing `*_imagegen_source.png` files for medical reserve, clean city rats, sealed food stores, sewer clearance, flea control, transport purge, demolition, and emergency hospital were preserved unchanged and processed through the same alpha and 33×32 normalization path. Their original generation prompts are not present in the current event workspace; the source PNGs remain the provenance evidence for this tranche.

## Shared generation constraints

The chroma-key field was required to be perfectly flat with no shadow, gradient, floor, texture, reflection, or lighting variation, and the subject was required not to use the key colour. The generated source was retained before local processing.

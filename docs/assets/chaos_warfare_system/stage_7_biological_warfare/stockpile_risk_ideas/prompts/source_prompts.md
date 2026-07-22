# Biological Stockpile Risk Icon Prompts and Source Notes

## Production scope

This package contains four independently generated idea / national-spirit icons and one independently generated decision icon for the accepted Stage 7 biological-warfare stockpile-risk and national-arsenal designation surfaces.

Source mode for every asset: built-in `$imagegen` generation, followed by the official chroma-key transparency workflow using `C:\Users\klimp\.codex\skills\.system\imagegen\scripts\remove_chroma_key.py`.

The generated source renders used a perfectly flat `#00ff00` background only as a removable key. The key was removed with a soft matte, despill, and edge contraction; each asset was then cropped from its own alpha bounds and fitted to its own target canvas. No source was derived from another icon type or from an existing Chaos Redux icon.

## Idea / national-spirit family

### Controlled

- Source output: `C:\Users\klimp\.codex\generated_images\019f79a1-5767-7381-8dde-21693b8ac29e\exec-e2706ff1-6cd2-4c88-a983-c3026fdc0b0e.png`
- Prompt: compact Hearts of Iron IV idea icon of a sealed reinforced biological stockpile storage cylinder behind an intact containment shield; calm orderly geometry, cool steel and muted brass, small green-blue status lamp, painterly aged industrial texture, strong dark edge definition, centered silhouette readable at 60x68.
- Required exclusions: text, letters, numbers, pathogen imagery, liquid, smoke, exposed contents, open container, gore, people, aircraft, map, opaque background, white rim, sticker border, fake checkerboard, and glow.

### Strained

- Source output: `C:\Users\klimp\.codex\generated_images\019f79a1-5767-7381-8dde-21693b8ac29e\exec-1dfe183c-706f-472f-b54d-cf9e7490470e.png`
- Prompt: compact Hearts of Iron IV idea icon of a crowded rack of sealed reinforced biological stockpile canisters; taut clamps and restraint bands, compressed spacing, one amber status lamp, visibly pressured but contained, painterly aged industrial texture, centered silhouette readable at 60x68.
- Required exclusions: text, letters, numbers, pathogen imagery, liquid, smoke, exposed contents, open container, gore, people, aircraft, map, opaque background, white rim, sticker border, fake checkerboard, and glow.

### Dangerous

- Source output: `C:\Users\klimp\.codex\generated_images\019f79a1-5767-7381-8dde-21693b8ac29e\exec-17bab778-4e0d-4095-95e5-ec5eaa25ee8c.png`
- Prompt: compact Hearts of Iron IV idea icon of a cracked outer containment housing around an intact inner sealed canister; clear structural fracture, diagonal emergency brace, yellow-orange warning lamp, layered silhouette showing the intact inner canister, painterly aged industrial texture, centered and readable at 60x68.
- Required exclusions: no leak, vapor, liquid, dust cloud, pathogen depiction, exposed contents, open container, text, letters, numbers, gore, people, aircraft, map, opaque background, white rim, sticker border, fake checkerboard, and glow.

### Critical

- Source output: `C:\Users\klimp\.codex\generated_images\019f79a1-5767-7381-8dde-21693b8ac29e\exec-990aefcc-5a99-4e63-bcd3-b7ee0189f9fe.png`
- Prompt: compact Hearts of Iron IV idea icon of a critically failing biological stockpile containment bay; warped blast door, failed restraint rack hanging askew, collapsed braces, angular emergency geometry, dark red warning lamps, closed opaque vessels only, painterly aged industrial texture, diagonally unstable silhouette readable at 60x68.
- Required exclusions: no exposed contents, pathogen imagery, liquid, smoke, dust cloud, fire, text, letters, numbers, gore, people, aircraft, map, opaque background, white rim, sticker border, fake checkerboard, diffuse glow, or watermark.

## Decision icon

### National biological arsenal designation and relocation

- Source output: `C:\Users\klimp\.codex\generated_images\019f79a1-5767-7381-8dde-21693b8ac29e\exec-b4710172-08d4-453b-a49b-68d0678edd72.png`
- Prompt: independently generated 32x32 Hearts of Iron IV decision icon of a sealed reinforced biological storage vault entrance with a locked canister rack and a precise map-pin / locator silhouette integrated in front; simplified high-contrast painterly steel and brass emblem, clear at 32x32.
- Required exclusions: no aircraft, map background, text, letters, numbers, pathogen imagery, liquid, smoke, exposed contents, open container, gore, people, opaque background, white rim, sticker border, fake checkerboard, diffuse glow, or tiny unreadable detail.

## Processing record

- Idea output canvas: `60x68` each, matching the inspected canonical idea reference canvas and the parent-provided requirement.
- Decision output canvas: `32x32`, independently composed for the decision surface.
- Alpha cleanup: remove chroma key with `--auto-key border --soft-matte --transparent-threshold 12 --opaque-threshold 220 --despill --edge-contract 2` for Controlled and `--edge-contract 1` for the other four source renders; final low-alpha green edge remnants were cleared during target-size alpha cleanup.
- Resampling: crop to the generated subject's alpha bounds, preserve aspect ratio, fit ideas within `56x64` on a transparent `60x68` canvas and decision art within `30x30` on a transparent `32x32` canvas.
- Visual review: `contact_sheets/bio_stockpile_risk_icons_contact_sheet.png` and each processed PNG were inspected over a checker background at exact target dimensions, enlarged with nearest-neighbour only for review.
- No source render, processed PNG, or DDS was copied, resized, recolored, or derived from an existing Chaos Redux icon or from another asset type.

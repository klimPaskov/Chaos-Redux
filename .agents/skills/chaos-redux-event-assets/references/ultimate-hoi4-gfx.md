# Curated Ultimate HOI4 GFX companion

Use this reference only when an accepted asset brief calls for a useful match in `assets/ultimate_hoi4_gfx/`. The local collection is a reviewed subset of [Globvs/Ultimate-HOI4-GFX](https://github.com/Globvs/Ultimate-HOI4-GFX), pinned to upstream tree commit `3626dc83c8573d6603fa497138090b04b64a15ba`. Read its `README.md` and `CATALOG.md` to identify the selected local file, original upstream path, hash, source credit, and approved use. Local files use Chaos Redux lowercase snake_case names and need not retain upstream filenames. Never assume a nearby upstream file was imported.

## Use boundary

- Inspect the exact installed vanilla or Chaos Redux consumer and the matching `assets/vanilla_reference/` entry first. Those determine canvas, alpha, frame/state behavior, presentation, and sprite wiring.
- Treat companion focus pieces and backgrounds chiefly as composition or style references. Create the subject as original ImageGen source art. Do not treat a focus piece as a finished icon or resize it into another icon family.
- Only a backdrop explicitly approved for persistent use in the companion catalog may be composited into a final, especially for decision-category icon backgrounds. Place original ImageGen subject art above it. Preserve the imported source layer separately, retain the original ImageGen source, and keep the processed preview and runtime DDS separate.
- Verify the composite at native size and against the exact consumer, including alpha, legibility, cropping, and state variants. Achievement template and state derivation rules remain governed by the asset skill; this companion does not replace those inputs.
- Portrait identity and source-mode gates remain in force. A companion image is never evidence of a grounded person's identity or a substitute for the user-supplied grounded styled final.

## Two selection examples

- Focus icon brief: inspect the matching vanilla focus sprites and `vanilla_reference/icons/national_focus/` first. Use `focus_pieces/focus_piece_ballot.png` and `focus_backgrounds/focus_background_plain.png` only to describe subject scale, shading, and composition in an ImageGen prompt. Keep both as references in the manifest; neither file becomes a layer in the final icon.
- Decision category icon brief: inspect the owning decision-category sprite and native decision-category references first. If its canvas and alpha treatment fit, use `national_spirit_backgrounds/decision_category_background_blue_roundel.png` as the credited backdrop layer under an original ImageGen subject. Retain the untouched backdrop, ImageGen source, composed PNG, and final DDS separately; record the catalog row and any crop or resize in the manifest.

## Attribution and manifest

The upstream `CREDITS` says contributors consented to free use, but the repository has no SPDX `LICENSE` file. Record that as the upstream statement, not as a formal license grant or an invented per-file author. Credit `Globvs/Ultimate-HOI4-GFX` and name an individual contributor only when the catalog or upstream evidence supports that attribution.

For any final that incorporates a catalog-approved backdrop, record in the output manifest: local layer path, original upstream path, pinned commit and source hash, supported credit, approved role, original ImageGen subject source and prompt, composite/output paths, and any crop, resize, recolour, or alpha processing. If the catalog does not establish a file's permitted persistent-backdrop role or traceable source, keep it as reference only and mark the proposed composite unresolved.

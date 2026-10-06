# `GFX_div_templ_47_small` biohazard emblem

Exact ImageGen request arguments:

- `prompt`: Generate one single, simple Hearts of Iron IV division-template emblem on a genuine transparent background. Use image 1 only to identify the symbol: a biohazard trefoil made from three rounded lobes around a small central ring. Make it a compact muted olive-green relief glyph with clean dark edge shading and bright restrained green highlights, in the same understated small-template-emblem rendering as image 2. The trefoil arms must be stout and distinct, with a bold approximately one-pixel stroke after smooth reduction to a 30x12 transparent canvas; center the glyph and let it occupy nearly the full 12-pixel canvas height. No badge, circle behind the symbol, text, letters, numbers, base, ground, shadow outside the emblem, checkerboard, panel, or background. Return one emblem only, not a sprite sheet or mockup.
- `transparent_background`: `true`
- `referenced_image_paths`: `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/source_runtime/custom_template_047_small.png` (symbol identity only); `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/references/vanilla_template_000_small.png` (style and restrained palette only)
- `num_last_images_to_include`: omitted

The source runtime DDS is preserved under `source_runtime/`. This candidate is a new native-alpha generation because the current 30x12 texture has only eight fully opaque pixels and reads faintly at native size. It is not yet selected for runtime promotion.

# Event 014 GUI and Non-Portrait Animation Handoff

Date: 2026-07-12

## Completed scope

- Finalized all 26 static GUI textures for the five Event 014 mechanic windows.
- Finalized all 12 non-portrait UI animation packages from 114 separate source frames.
- Wrote exact runtime PNG/DDS files to `gfx/interface/014_cannibalism/` and `gfx/interface/animated/014_cannibalism/`.
- Preserved every generated source, processed frame, static fallback, horizontal sheet, preview GIF, contact sheet, and hash inventory.
- Built two-layer OpenRaster masters for every static GUI asset. The text-safe layer reproduces the actual overlay rectangles from `interface/014_cannibalism_frontline_hunger.gui` and never enters runtime art.

## Runtime and format proof

- `docs/assets/014_cannibalism/gui_animation_portraits/validation/static_gui_inventory.tsv`
- `docs/assets/014_cannibalism/gui_animation_portraits/validation/nonportrait_animation_inventory.tsv`
- `docs/assets/014_cannibalism/gui_animation_portraits/validation/gfx_handoff_nonportrait.tsv`
- `docs/assets/014_cannibalism/gui_animation_portraits/validation/static_gui_text_safe_native_contact.png`

Every DDS has the exact registered dimensions, a 32-bit BGRA mask layout, one stored image level, and the expected raw payload size. Runtime copies are hash-identical to the documented package finals. Within each animation, source-frame hashes and processed-frame hashes are all distinct.

## Visual and secrecy review

- Early containment and network art contains no visible Hannibal Lecter face, personal title, unique revealed silhouette, or transformed-route symbol.
- Revealed-command art uses black, red, bone-white, damaged command material only after the reveal surface.
- Wendigo command art is fictional frozen body horror without antlers, runes, regalia, living-cultural motifs, or authenticity claims.
- The frame contacts show independently redrawn material changes rather than transform-only motion.

## Boundaries

The ordinary and Wendigo animated leader portraits remain owned by their dedicated portrait tranche. This handoff does not certify those two packages. The shared top-level GUI/portrait manifest and GFX handoff should be consolidated only after those portrait finals are present.

# Zol World-End Portrait Animation Brief

## Purpose

Rebuild the optional animated leader portrait package for Event 010 Death world-end use so it stays visually locked to the static fallback portrait. The animated sheet should preserve the same composition, silhouette, face veil, crown, costume, background, and overall values, with only a restrained eye-glow pulse across the loop.

## Visual Direction

- Fictional supernatural leader portrait, not a real person.
- Preserve Zol's HOI4 portrait readability: centered bust, hooded void face, white eyes, restrained painterly finish.
- Keep the portrait nearly identical to the static fallback in every frame.
- The only visible motion is a subtle eye-glow pulse.
- No mouth change, no head movement, no shroud drift, no crown growth, no aura expansion, no whole-portrait brightness pulse, and no facial drift.
- No gore, readable text, watermark, modern props, modern costume details, or copyrighted character likeness.
- Keep the result usable as a HOI4 portrait at `156x210`.

## Technical Targets

- Source frames: 8 individually edited PNGs derived from the approved static fallback portrait.
- Processed frames: `156x210` PNGs.
- Final frame sheet: `1248x210` DDS, 8 horizontal frames at 4 FPS.
- Static fallback: reuse `gfx/leaders/010_death/portrait_DTH_zol_world_end.dds` unchanged.
- Animated sprite: `GFX_portrait_DTH_zol_world_end_animated`.
- Static sprite: `GFX_portrait_DTH_zol_world_end`.

## Required Outputs

- Source frames: `docs/assets/010_death/source_png/portrait_DTH_zol_world_end_frame_XX_source.png`
- Processed frames: `docs/assets/010_death/processed_png/portrait_DTH_zol_world_end_frame_XX.png`
- Static processed PNG: `docs/assets/010_death/processed_png/portrait_DTH_zol_world_end.png`
- Sheet PNG: `docs/assets/010_death/animations/portrait_DTH_zol_world_end/sheets/portrait_DTH_zol_world_end_sheet.png`
- Preview GIF: `docs/assets/010_death/previews/portrait_DTH_zol_world_end_preview.gif`
- Contact sheet: `docs/assets/010_death/contact_sheets/portrait_DTH_zol_world_end_contact.png`
- Final DDS files: `gfx/leaders/010_death/portrait_DTH_zol_world_end.dds`, `gfx/leaders/010_death/portrait_DTH_zol_world_end_animated.dds`

## References

- Existing Death portrait reference: `docs/assets/010_death/processed_png/leader_zol.png`
- Static fallback base: `docs/assets/010_death/processed_png/portrait_DTH_zol_world_end.png`
- Existing DTH portrait sprite registration already preserved: `interface/chaosx_characters.gfx`

## Validation Targets

- Every processed frame stays `156x210`.
- Frame count stays `8`.
- Sheet size stays `1248x210`.
- Preview GIF loops with the same restrained eye pulse seen in the sheet.
- Identity drift check must show no meaningful change outside the eye area.
- Final motion must read as eyes-glow-only.

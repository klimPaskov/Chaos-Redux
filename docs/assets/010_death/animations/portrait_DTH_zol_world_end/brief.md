# Zol World-End Portrait Animation Brief

## Purpose

Create the optional animated leader portrait package for Event 010 Death world-end use. The static portrait fallback and the animated sheet both depict Zol as a final-stage nonhuman ruler of the black wasteland, using a real eight-frame generated key-state loop rather than a transform-only mockup.

## Visual Direction

- Fictional supernatural leader portrait, not a real person.
- Preserve Zol's HOI4 portrait readability: centered bust, hooded void face, white eyes, restrained painterly finish.
- World-end escalation should read through real frame-to-frame art changes: dead-spire crown growth, eclipse-halo rise and fall, ash drift, and shroud deformation.
- No gore, readable text, watermark, modern props, modern costume details, or copyrighted character likeness.
- Keep the result usable as a HOI4 portrait at `156x210`.

## Technical Targets

- Source frames: 8 individually generated PNGs.
- Processed frames: `156x210` PNGs.
- Final frame sheet: `1248x210` DDS, 8 horizontal frames at 4 FPS.
- Static fallback: `gfx/leaders/010_death/portrait_DTH_zol_world_end.dds`.
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
- Existing DTH portrait sprite registration: `interface/chaosx_characters.gfx`
- Existing animated portrait precedent: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/brief.md`

# Holy Realm Buddha Mandate Portrait Animation Brief

## Purpose

Create the animated leader portrait frame sheet for The Holy Realm after Buddhahood and the Buddha Mandate stage. The static country-leader portrait is generated from the same new portrait package, while the animated sprite provides the required frame-sheet asset package for event-log and UI presentation surfaces.

## Visual Direction

- Fictional sacred leader portrait, not a real historical religious figure.
- Use new Buddha Mandate portrait source art: frontal golden mask, jeweled crown, temple shadows, calm awakened expression.
- Animation reads as controlled awakening: very subtle halo breathing, crown jewel glints, eye-light changes, and gold aura variation across more frames.
- Do not rely on a simple vignette, transform, zoom, warp, or color-filter pulse from one still image.
- No readable text, letters, numbers, flags, maps, blood, gore, explosions, weapons, or modern UI.
- Keep the head centered and readable at `156x210`.

## Technical Targets

- Source frames: 16 generated PNGs split from a generated 4x4 animation source sheet.
- Processed frames: `156x210` PNGs.
- Final frame sheet: `2496x210` DDS, 16 horizontal frames.
- Static fallback: `gfx/leaders/THR/portrait_THR_buddha_mandate.dds`.
- Animated sprite: `GFX_portrait_THR_buddha_mandate_animated`.

## Required Outputs

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/processed_frames/`
- Sheet PNG: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/sheets/portrait_THR_buddha_mandate_sheet.png`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/previews/portrait_THR_buddha_mandate_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/portrait_THR_buddha_mandate/previews/portrait_THR_buddha_mandate_contact.png`
- Final DDS: `gfx/leaders/THR/portrait_THR_buddha_mandate_animated.dds`

## References

- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/documentation/effects_documentation.md`
- `interface/007_fury.gfx`
- `interface/007_fury_leader_overlay.gui`
- `docs/assets/003_holy_realm_buddhahood/leader_portrait_static_fallbacks/processed_png/portrait_THR_buddha_mandate.png`

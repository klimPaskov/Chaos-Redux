# Holy Mandala State Animation Rebuild Handoff

Date: `2026-06-13`

Scope: rebuild the Holy Mandala decision-category state animations with static-position artwork and visible 16-frame glow pulses.

## Result

Rebuilt all seven Holy Mandala state animations as 16-frame, 420x420 frame-sheet loops. Each state now uses a fixed generated Mandala base so the image does not translate between frames; the animation comes from a visible, smooth glow pulse derived from the generated artwork.

## Assets Rebuilt

- `GFX_holy_realm_mandala_dormant_animated`
- `GFX_holy_realm_mandala_teaching_animated`
- `GFX_holy_realm_mandala_awakened_animated`
- `GFX_holy_realm_mandala_wrathful_animated`
- `GFX_holy_realm_mandala_final_silence_animated`
- `GFX_holy_realm_mandala_empty_animated`
- `GFX_holy_realm_mandala_meditation_animated`

Each rebuilt package now has:

- `16` static-position source frames under `docs/assets/003_holy_realm_buddhahood/animations/<asset>/source_frames/`
- `16` static-position processed frames under `processed_frames/`
- a `6720x420` horizontal sheet PNG under `sheets/`
- a preview GIF and 4x4 contact sheet under `previews/`
- a refreshed `4x4` source grid under `notes/`
- a final `6720x420` DDS under `gfx/interface/decisions/holy_realm/mandala_states/`

## Wiring

- `interface/003_holy_realm.gfx` now declares `noOfFrames = 16` for every `GFX_holy_realm_mandala_*_animated` state sprite.
- `interface/chaosx_decisions.gui` now uses `GFX_holy_realm_mandala_dormant_animated` as the base `holy_realm_mandala_core` sprite before scripted localisation properties update it.
- `GetHolyRealmMandalaSprite` already returned animated state sprites, so no scripted localisation change was required.

## Validation

- Dimension audit confirmed all seven Mandala animated DDS sheets are `6720x420`.
- Frame audit confirmed all seven Mandala animation packages have `16` source frames and `16` processed frames.
- Mean-luminance audit confirms a visible pulse on all seven states.
- Contact-sheet review was performed on the full seven-state set after the static-position rebuild.
- Bright-pixel bounding changed only from the glow expanding and contracting; the underlying Mandala geometry is fixed per state.

## Remaining Risks

- The small decision-category row icon `GFX_decision_category_holy_mandala` is still a separate static `52x39` sprite. The requested animation problem was on the embedded Mandala state panel and state sheets, so that row icon was not converted into an animated sprite.

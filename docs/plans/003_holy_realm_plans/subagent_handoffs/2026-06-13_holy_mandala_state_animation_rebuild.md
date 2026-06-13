# Holy Mandala State Animation Rebuild Handoff

Date: `2026-06-13`

Scope: complete the parent-owned rebuild of the Holy Mandala decision-category state animations after the asset subagent was shut down while still partial.

## Result

Rebuilt the six non-meditation Holy Mandala state animations to match the newer meditation package standard: 16-frame, 420x420, subtle frame-sheet loops with generated painterly source art rather than simple line geometry, filter-only pulsing, or transform-only animation. The existing meditation animation remains 16 frames and is now part of a consistent seven-state Mandala set.

## Assets Rebuilt

- `GFX_holy_realm_mandala_dormant_animated`
- `GFX_holy_realm_mandala_teaching_animated`
- `GFX_holy_realm_mandala_awakened_animated`
- `GFX_holy_realm_mandala_wrathful_animated`
- `GFX_holy_realm_mandala_final_silence_animated`
- `GFX_holy_realm_mandala_empty_animated`

Each rebuilt package now has:

- `16` source frames under `docs/assets/003_holy_realm_buddhahood/animations/<asset>/source_frames/`
- `16` processed frames under `processed_frames/`
- a `6720x420` horizontal sheet PNG under `sheets/`
- a preview GIF and 4x4 contact sheet under `previews/`
- a copied generated `4x4` source grid under `notes/`
- a final `6720x420` DDS under `gfx/interface/decisions/holy_realm/mandala_states/`

## Wiring

- `interface/003_holy_realm.gfx` now declares `noOfFrames = 16` for every `GFX_holy_realm_mandala_*_animated` state sprite.
- `interface/chaosx_decisions.gui` now uses `GFX_holy_realm_mandala_dormant_animated` as the base `holy_realm_mandala_core` sprite before scripted localisation properties update it.
- `GetHolyRealmMandalaSprite` already returned animated state sprites, so no scripted localisation change was required.

## Validation

- Dimension audit confirmed all seven Mandala animated DDS sheets are `6720x420`.
- Frame audit confirmed all seven Mandala animation packages have `16` source frames and `16` processed frames.
- Contact-sheet review was performed for the regenerated teaching, dormant, and wrathful states; the old thin geometry/simple-shape teaching state has been replaced by carved painterly mandala art.

## Remaining Risks

- The small decision-category row icon `GFX_decision_category_holy_mandala` is still a separate static `52x39` sprite. The requested old animation problem was on the embedded Mandala state panel and state sheets, so that row icon was not converted into an animated sprite.

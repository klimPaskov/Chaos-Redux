# Holy Realm Dormant Mandala Animation Brief

## Purpose

Create the animated Holy Mandala state shown before The Holy Realm has unlocked Dharma teaching, Bodhi progress, Dhyana depth, Buddhahood, wrathful protection, or Final Silence states. The loop should read as sealed potential: present, watchful, and sacred, but not yet active.

## In-Game Wiring

- Static fallback sprite: `GFX_holy_realm_mandala_dormant`
- Animated sprite: `GFX_holy_realm_mandala_dormant_animated`
- Final DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_dormant_animated.dds`
- Sprite definition file: `interface/003_holy_realm.gfx`
- Runtime selection: `GetHolyRealmMandalaSprite` in `common/scripted_localisation/003_holy_realm_scripted_localisation.txt`
- GUI consumers: `interface/chaosx_decisions.gui` and `common/scripted_guis/chaosx_scripted_guis.txt`

## Technical Targets

- Frames: 8
- Frame size: 420x420
- Sheet size: 3360x420
- FPS: 8
- Looping: yes
- Play on show: yes
- Anchor: centered mandala, no crop shift

## Visual Direction

- Preserve the static fallback identity: centered teal-grey mandala, dark background, restrained star geometry.
- Keep the center dim and closed. No active golden lamp, no teaching rays, no awakened radiance, no red crisis tones.
- Use slow breath-like line brightening, faint frost-light around the outer ring, and a quiet locked-center pulse.
- Do not include literal text, letters, glyphs, readable mantras, or UI labels inside the image.
- Keep the image flat enough to function as a decision-category scripted GUI icon.

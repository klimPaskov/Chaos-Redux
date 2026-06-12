# Holy Realm Teaching Mandala Animation Brief

## Purpose

Create the animated Holy Mandala state shown while The Holy Realm is advancing through Dharma teaching, Bodhi progress, or early teaching mission successes. The animation should read as active instruction and compassionate transmission, not combat escalation or final-world silence.

## In-Game Wiring

- Static fallback sprite: `GFX_holy_realm_mandala_teaching`
- Animated sprite: `GFX_holy_realm_mandala_teaching_animated`
- Final DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_teaching_animated.dds`
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

- Preserve the static fallback identity: centered green-gold teaching mandala, circular geometry, calm dark background.
- Use saffron, green, teal, and warm gold highlights.
- Add a gentle teaching pulse: lamp-like center, outward Dharma rings, small compassion rays, and a quiet scripture glow.
- Do not include literal text, letters, glyphs, readable mantras, or UI labels inside the image.
- Keep the image flat enough to function as a decision-category scripted GUI icon.

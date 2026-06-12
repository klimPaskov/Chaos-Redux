# Holy Realm Wrathful Mandala Animation Brief

## Asset

- Asset name: `holy_realm_mandala_wrathful`
- Event id: `003`
- Event slug: `holy_realm_buddhahood`
- Asset type: animated scripted GUI state sprite
- Subject type: fictional, symbolic, supernatural UI state art
- In-game use: chaos-emergency Mandala state for Wrathful Protection, Sun and Moon crisis proof, or the awakened Touching Sun and Moon power.
- Gameplay surface: Holy Mandala decision-category scripted GUI, selected through `GetHolyRealmMandalaSprite`.
- Target frame size: `420x420`
- Frame count: `12`
- Horizontal sheet size: `5040x420`
- Static fallback sprite: `GFX_holy_realm_mandala_wrathful`
- Animated sprite: `GFX_holy_realm_mandala_wrathful_animated`
- Animation rate: `8` FPS
- Loop behavior: `looping = yes`
- Show behavior: `play_on_show = yes`, `pause_on_loop = 0.0`
- Anchor point: center
- Source mode: `$imagegen`, one generated source PNG per planned frame

## Paths

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/processed_frames/`
- Sheet PNG: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/sheets/holy_realm_mandala_wrathful_sheet.png`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/previews/holy_realm_mandala_wrathful_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/previews/holy_realm_mandala_wrathful_contact.png`
- Final DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_wrathful_animated.dds`
- Target `.gfx`: `interface/003_holy_realm.gfx`
- Target GUI files: `interface/chaosx_decisions.gui`, `common/scripted_guis/chaosx_scripted_guis.txt`

## References

- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/interface/theatreselector.gfx`
- `interface/007_fury.gfx`
- `interface/003_holy_realm.gfx`
- `.agents/skills/chaos-redux-event-assets/assets/decisions/`
- Static fallback: `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_wrathful.png`

## Visual Direction

The loop should read as a wrathful protective emergency state: the sacred wheel is still disciplined and centered, but the rings carry red-orange pressure, warning heat, and containment force. The motion is a controlled alarm rather than random fire.

Avoid readable text, letters, generated glyphs, UI labels, faces, deities, monsters, weapons, maps, flags, blood, gore, chaotic off-centre composition, extra symbols outside the Mandala, gold teaching light, meditation blue, or empty-seat silence. Keep the Mandala centered and recognizably related to the static wrathful fallback.

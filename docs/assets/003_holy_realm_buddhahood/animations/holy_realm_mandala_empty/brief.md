# Holy Realm Empty Seat Mandala Animation Brief

## Asset

- Asset name: `holy_realm_mandala_empty`
- Event id: `003`
- Event slug: `holy_realm_buddhahood`
- Asset type: animated scripted GUI state sprite
- Subject type: fictional, symbolic, supernatural UI state art
- In-game use: afterstate Mandala for non-terminal Final Silence completion and Empty Seat achievement readiness.
- Gameplay surface: Holy Mandala decision-category scripted GUI, selected through `GetHolyRealmMandalaSprite`.
- Target frame size: `420x420`
- Frame count: `8`
- Horizontal sheet size: `3360x420`
- Static fallback sprite: `GFX_holy_realm_mandala_empty`
- Animated sprite: `GFX_holy_realm_mandala_empty_animated`
- Animation rate: `8` FPS
- Loop behavior: `looping = yes`
- Show behavior: `play_on_show = yes`, `pause_on_loop = 0.0`
- Anchor point: center
- Source mode: `$imagegen`, one generated source PNG per planned frame

## Paths

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/processed_frames/`
- Sheet PNG: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/sheets/holy_realm_mandala_empty_sheet.png`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/previews/holy_realm_mandala_empty_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_empty/previews/holy_realm_mandala_empty_contact.png`
- Final DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_empty_animated.dds`
- Target `.gfx`: `interface/003_holy_realm.gfx`
- Target GUI files: `interface/chaosx_decisions.gui`, `common/scripted_guis/chaosx_scripted_guis.txt`

## References

- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/interface/theatreselector.gfx`
- `interface/007_fury.gfx`
- `interface/003_holy_realm.gfx`
- Static fallback: `docs/assets/003_holy_realm_buddhahood/mandala_static_fallbacks/processed_png/holy_realm_mandala_empty.png`

## Visual Direction

The loop should read as a quiet empty-seat afterimage, not an active teaching, meditation, wrathful, or Final Silence state. Keep the same centered Mandala identity as the static fallback: pale grey rings, dark ashen centre, faint star geometry, and subdued absence.

Avoid readable text, letters, generated glyphs, UI labels, extra symbols outside the mandala, gold teaching light, red crisis colour, green chroma edges, flames, faces, figures, weapons, maps, flags, or a second off-centre disc. The centre should feel vacant.

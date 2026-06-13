# Holy Realm Mandala Dormant Animation Brief

Asset name: `holy_realm_mandala_dormant`

In-game use: animated dormant-state mandala for the Holy Realm decision-category scripted GUI panel.

Gameplay surface:
- `interface/chaosx_decisions.gui`: `holy_realm_mandala_category_container` / `holy_realm_mandala_core`
- `common/scripted_guis/chaosx_scripted_guis.txt`: `holy_realm_mandala_category_scripted_gui`
- `common/scripted_localisation/003_holy_realm_scripted_localisation.txt`: `GetHolyRealmMandalaSprite`

Target:
- Frame size: `420x420`
- Frame count: `16`
- Sheet size: `6720x420`
- FPS: `8`
- Loop: `looping = yes`
- Play on show: `play_on_show = yes`
- Anchor: center

Sprite names:
- Static fallback sprite: `GFX_holy_realm_mandala_dormant`
- Animated sprite: `GFX_holy_realm_mandala_dormant_animated`

File targets:
- Static fallback DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_dormant.dds`
- Final animated sheet DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_dormant_animated.dds`
- Target `.gfx`: `interface/003_holy_realm.gfx`

Source mode:
- `$imagegen`, one generated 4x4 animation-source grid sliced into sixteen source-frame PNGs.
- Local processing only resizes, normalizes, sheets, previews, and converts frames.

Subject classification: symbolic and supernatural route-state UI art.

Reference inspected:
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/interface/menubar.gfx`
- `~/projects/Hearts of Iron IV/interface/theatreselector.gfx`
- `interface/003_holy_realm.gfx`
- `.agents/skills/chaos-redux-event-assets/assets/decisions/`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/`

Visual direction:
- Centered dormant mandala with teal-grey enamel, weathered stone-metal rims, restrained lotus filigree, and a dim sealed center.
- Subtle sealed-potential breath loop matching the newer meditation package cadence: light gathers, listens, and settles in many small steps instead of flashing.
- Calm sacred stillness, not teaching warmth, awakened radiance, wrathful alarm, terminal collapse, or afterimage vacancy.
- No text, faces, maps, modern UI, explosive effects, or generated symbols that read as letters.

Package paths:
- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/processed_frames/`
- Sheet PNG: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/sheets/holy_realm_mandala_dormant_sheet.png`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/previews/holy_realm_mandala_dormant_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_dormant/previews/holy_realm_mandala_dormant_contact.png`

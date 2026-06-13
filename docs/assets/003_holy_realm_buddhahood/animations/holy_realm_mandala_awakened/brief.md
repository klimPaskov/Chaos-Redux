# Holy Realm Mandala Awakened Animation Brief

Asset name: `holy_realm_mandala_awakened`

In-game use: animated awakened-state mandala for the Holy Realm decision-category scripted GUI panel.

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
- Static fallback sprite: `GFX_holy_realm_mandala_awakened`
- Animated sprite: `GFX_holy_realm_mandala_awakened_animated`

File targets:
- Static fallback DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_awakened.dds`
- Final animated sheet DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_awakened_animated.dds`
- Target `.gfx`: `interface/003_holy_realm.gfx`

Source mode:
- `$imagegen`, one generated 4x4 animation-source grid sliced into sixteen source-frame PNGs.
- Local processing only resizes, normalizes, sheets, previews, and converts frames.

Subject classification: symbolic and supernatural route-state UI art.

Reference inspected:
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/interface/core.gfx`
- `interface/007_fury.gfx`
- `interface/003_holy_realm.gfx`
- `.agents/skills/chaos-redux-event-assets/assets/decisions/`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/`

Visual direction:
- Centered awakened mandala with warm gold, pale ivory core, carved sacred wheel detail, and faint horizon texture beneath the lower ring.
- Subtle serene radiance matching the meditation package cadence: light rises, holds, and recedes across many small steps rather than flaring like a combat effect.
- Calm completion and numinous authority, not teaching activity, emergency alarm, terminal withdrawal, or afterimage vacancy.
- No text, faces, maps, modern UI, explosive effects, or generated symbols that read as letters.

Package paths:
- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/processed_frames/`
- Sheet PNG: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/sheets/holy_realm_mandala_awakened_sheet.png`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/previews/holy_realm_mandala_awakened_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_awakened/previews/holy_realm_mandala_awakened_contact.png`

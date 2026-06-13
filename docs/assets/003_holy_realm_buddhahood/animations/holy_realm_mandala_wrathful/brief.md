# Holy Realm Mandala Wrathful Animation Brief

Asset name: `holy_realm_mandala_wrathful`

In-game use: animated wrathful-state mandala for the Holy Realm decision-category scripted GUI panel.

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
- Static fallback sprite: `GFX_holy_realm_mandala_wrathful`
- Animated sprite: `GFX_holy_realm_mandala_wrathful_animated`

File targets:
- Static fallback DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_wrathful.dds`
- Final animated sheet DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_wrathful_animated.dds`
- Target `.gfx`: `interface/003_holy_realm.gfx`

Source mode:
- `$imagegen`, one generated 4x4 animation-source grid sliced into sixteen source-frame PNGs.
- Local processing only resizes, normalizes, sheets, previews, and converts frames.

Subject classification: symbolic and supernatural route-state UI art.

Reference inspected:
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`
- `~/projects/Hearts of Iron IV/interface/theatreselector.gfx`
- `interface/007_fury.gfx`
- `interface/003_holy_realm.gfx`
- `.agents/skills/chaos-redux-event-assets/assets/decisions/`
- `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/`

Visual direction:
- Centered wrathful mandala with disciplined red-orange, ember-gold, and contained pale warning light, built as a painted sacred wheel rather than thin linework.
- Subtle controlled alarm loop matching the meditation package cadence: containment pressure rises and falls smoothly across 16 steps without becoming chaotic fire.
- Protective emergency and sacred force, not serene awakening, terminal silence, or empty-seat absence.
- No text, faces, maps, modern UI, explosive effects outside the wheel, or generated symbols that read as letters.

Package paths:
- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/processed_frames/`
- Sheet PNG: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/sheets/holy_realm_mandala_wrathful_sheet.png`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/previews/holy_realm_mandala_wrathful_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_wrathful/previews/holy_realm_mandala_wrathful_contact.png`

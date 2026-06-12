# Holy Realm Mandala Meditation Animation Brief

Asset name: `holy_realm_mandala_meditation`

In-game use: animated central Holy Mandala state for active concentration sequence or any Dhyana progress before Buddhahood.

Gameplay surface:
- `interface/chaosx_decisions.gui`: `holy_realm_mandala_category_container` / `holy_realm_mandala_core`
- `common/scripted_guis/chaosx_scripted_guis.txt`: `holy_realm_mandala_category_scripted_gui`
- `common/scripted_localisation/003_holy_realm_scripted_localisation.txt`: `GetHolyRealmMandalaSprite`

Target:
- Frame size: `420x420`
- Frame count: `12`
- Sheet size: `5040x420`
- FPS: `8`
- Loop: `looping = yes`
- Play on show: `play_on_show = yes`
- Anchor: center

Sprite names:
- Static fallback sprite: `GFX_holy_realm_mandala_meditation`
- Animated sprite: `GFX_holy_realm_mandala_meditation_animated`

File targets:
- Static fallback DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_meditation.dds`
- Final animated sheet DDS: `gfx/interface/decisions/holy_realm/mandala_states/holy_realm_mandala_meditation_animated.dds`
- Target `.gfx`: `interface/003_holy_realm.gfx`

Source mode:
- `$imagegen`, one generated source PNG per planned frame.
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

Visual direction:
- Centered blue-violet sacred mandala wheel, matching the static fallback composition.
- Slow concentration-breath loop: inner orb brightens, settles, then returns.
- Calm luminous geometry, not a combat or world-end state.
- No text, faces, maps, modern UI, explosive effects, flames, gore, or generated symbols that read as letters.

Package paths:
- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/processed_frames/`
- Sheet PNG: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/sheets/holy_realm_mandala_meditation_sheet.png`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/previews/holy_realm_mandala_meditation_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_mandala_meditation/previews/holy_realm_mandala_meditation_contact.png`

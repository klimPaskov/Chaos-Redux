# Event 013 Natural Disasters Super-Events

Event 13 uses three non-terminal Evolution III super-events for the largest abnormal disaster families. They mark catastrophic escalation, not a world-end branch.

## Slots And Triggers

| Slot | Trigger helper | Family | Title | Once flag |
| --- | --- | --- | --- | --- |
| `67` | `natural_disasters_start_rupture_wave_chain_from_state` | Great rupture wave | `The Great Rupture` | `natural_disasters_super_event_great_rupture_seen` |
| `68` | `natural_disasters_start_massive_eruption_chain_from_state` | Massive eruption | `The Mountain Unsealed` | `natural_disasters_super_event_massive_eruption_seen` |
| `69` | `natural_disasters_start_meteor_cluster_chain_from_state` | Meteor cluster and skyfall | `Stones from Heaven` | `natural_disasters_super_event_skyfall_seen` |

The helper effects set `super_event_visible` with the matching slot value for `12` days and store `global.current_super_event_audio_id` through `constant:natural_disasters_super_event.*`. Each helper plays audio through the existing settings-aware `play_current_super_event_audio` path for non-AI countries.

## Text Sources

### The Great Rupture

- Localisation keys: `chaosx_super_event.67.t`, `.q`, `.a`, `.d`
- Quote: "Though the waters thereof roar and be troubled, though the mountains shake with the swelling thereof."
- Attribution: Psalm 46:3, King James Version.
- Verification URL: <https://www.biblegateway.com/passage/?search=Psalm+46%3A2-3&version=KJV>
- Copyright note: public domain translation.
- Remark: `The maps are obsolete.`

### The Mountain Unsealed

- Localisation keys: `chaosx_super_event.68.t`, `.q`, `.a`, `.d`
- Quote: "He looketh on the earth, and it trembleth: he toucheth the hills, and they smoke."
- Attribution: Psalm 104:32, King James Version.
- Verification URL: <https://www.biblegateway.com/passage/?search=Psalm+104%3A32&version=KJV>
- Copyright note: public domain translation.
- Remark: `The ash will choose the harvest.`

### Stones from Heaven

- Localisation keys: `chaosx_super_event.69.t`, `.q`, `.a`, `.d`
- Quote: "The meteors, midnight flambeaus of the sky, How after them they draw long trails of flame"
- Attribution: Lucretius, `On the Nature of Things`, Book II, William Ellery Leonard translation.
- Verification URL: <https://classics.mit.edu/Carus/nature_things.2.ii.html>
- Copyright note: public domain source text and public domain translation.
- Remark: `Keep clear of the windows.`

## Image Package

All images are generated period-documentary black-and-white radio art. The final size is `457x328`.

| Slot | Source PNG | Processed PNG | Final DDS | Sprite |
| --- | --- | --- | --- | --- |
| `67` | `docs/assets/013_natural_disasters/source_png/super_event_nd_great_rupture_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_great_rupture.png` | `gfx/super_events/super_event_nd_great_rupture.dds` | `GFX_super_event_nd_great_rupture` |
| `68` | `docs/assets/013_natural_disasters/source_png/super_event_nd_massive_eruption_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_massive_eruption.png` | `gfx/super_events/super_event_nd_massive_eruption.dds` | `GFX_super_event_nd_massive_eruption` |
| `69` | `docs/assets/013_natural_disasters/source_png/super_event_nd_skyfall_source.png` | `docs/assets/013_natural_disasters/processed_png/super_event_nd_skyfall.png` | `gfx/super_events/super_event_nd_skyfall.dds` | `GFX_super_event_nd_skyfall` |

The generated prompts are recorded in `docs/assets/013_natural_disasters/prompts/generated_event_art_prompts.md`.

## Audio Package

| Slot | Music file | Sound file | Source work | License |
| --- | --- | --- | --- | --- |
| `67` | `music/super_event_natural_disasters_great_rupture.ogg` | `sound/chaosx_super_event_natural_disasters_great_rupture.wav` | Beethoven, `Egmont Overture, Op. 84`, Czech National Symphony Orchestra via Musopen and Wikimedia Commons | CC0 recording, public domain composition |
| `68` | `music/super_event_natural_disasters_massive_eruption.ogg` | `sound/chaosx_super_event_natural_disasters_massive_eruption.wav` | Holst, `The Planets, Op. 32: V. Saturn, the Bringer of Old Age`, 1923 Holst-conducted recording via Wikimedia Commons | public domain recording, public domain composition |
| `69` | `music/super_event_natural_disasters_skyfall.ogg` | `sound/chaosx_super_event_natural_disasters_skyfall.wav` | Holst, `The Planets, Op. 32: VII. Neptune, the Mystic`, 1923 Holst-conducted recording via Wikimedia Commons | public domain recording, public domain composition |

Original source and processed research files are preserved under `docs/assets/013_natural_disasters/audio_research/`. The audio handoff is `docs/plans/013_natural_disasters_plans/subagent_handoffs/2026-06-29_event013_super_event_audio_handoff.md`.

## Wiring Checklist

- `interface/chaosx_super_events.gfx` defines the three `GFX_super_event_nd_*` sprites.
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt` resolves image, title, quote, remark, and description for values `67`, `68`, and `69`.
- `music/chaosx_super_event_music.asset` defines six settings-aware volume variants per slot.
- `sound/chaosx_sound.asset` defines matching sound-channel tracks and sound effects.
- `music/chaosx_super_event_music.txt` registers zero-chance music entries so the tracks do not enter normal random playback.
- `localisation/english/013_natural_disasters_l_english.yml` owns the visible super-event text.
- `localisation/english/chaosx_music_l_english.yml` owns the music-library names.

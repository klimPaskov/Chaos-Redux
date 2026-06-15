# Event 010 Death - Super-Event Prompt

## Required Super-Events

Event 010 needs five super-event roles. Only reveal, world-end, and world-consumed are mandatory for the first implementation; compact and defeat aftermath should be included if the corresponding mechanics are implemented in the same pass.

| Role | Title | Trigger |
| --- | --- | --- |
| Reveal | The Name On The Chart | first mainland/populous/major/player reveal |
| Compact | The Living Compact | first successful compact with sufficient members |
| World-end | No More Shores | Death world-end branch |
| Defeat aftermath | The Shore Returns Empty | Death defeated after public/severe crisis |
| World consumed | The Last Entry | all valid states consumed or controlled by Death |

## Text Package

Use public-domain or verified-source lines. Keep localisation concise.

### Reveal - The Name On The Chart

Quote:

> For death is come up into our windows...

Attribution: Jeremiah 9:21, King James Version. Source: https://biblehub.com/kjv/jeremiah/9-21.htm

Button:

> Watchman, what of the night?

Attribution: Isaiah 21:11, King James Version. Source: https://biblehub.com/kjv/isaiah/21-11.htm

Tone: governments finally agree that "Death" is not metaphor, enemy codename, or local rumor. It is the name already appearing on naval lists.

### Compact - The Living Compact

Quote direction:

- use a short public-domain line about common mortality, vigilance, or duty
- avoid triumphalism
- avoid invented quotes

Button direction:

- "Keep the lamps lit."
- "The living sign first."
- "Every shore, every name."

Tone: grim bureaucracy and survival, not heroic victory.

### World-End - No More Shores

Quote:

> there was silence in heaven...

Attribution: Revelation 8:1, King James Version. Source: https://biblehub.com/kjv/revelation/8-1.htm

Button:

> Darkness visible

Attribution: John Milton, `Paradise Lost`, Book I. Source: https://www.gutenberg.org/files/26/26-h/26-h.htm

Tone: terminal, sparse, quiet. Death is no longer a coastline crisis.

### Defeat Aftermath - The Shore Returns Empty

Quote:

> After great pain, a formal feeling comes -

Attribution: Emily Dickinson, "After great pain, a formal feeling comes - (372)". Source: https://www.poetryfoundation.org/poems/47651/after-great-pain-a-formal-feeling-comes-372

Button:

> The morning cometh, and also the night.

Attribution: Isaiah 21:12, King James Version. Source: https://biblehub.com/kjv/isaiah/21-12.htm

Tone: survival with scars. No restoration fantasy.

### World Consumed - The Last Entry

Quote direction:

- reuse Revelation-style silence if not used elsewhere, or choose a short public-domain line from Mary Shelley, Byron, or scripture after verification
- avoid plague-specific Poe/Red Death language unless deliberately chosen

Button direction:

- "The last entry is closed."
- "No clerk remains."
- "No more maps."

Tone: final and nearly silent.

## Wiring Requirements

Implementation must add or update:

- scripted GUI super-event visibility and image selectors
- scripted localisation image slot mappings
- `.gfx` sprite definitions
- localisation keys for titles, quotes, remarks/buttons, and descriptions
- audio package definitions after audio research
- docs/super-event source notes
- event-log/evolution entries that fire with each super-event

Reserve stable image slots after checking the current used slot list. Do not assume an unused number without inspecting `chaosx_scripted_localisation_super_events.txt`.

## Audio Requirements

Before implementation, spawn `chaosx_super_event_audio_researcher` for:

- reveal audio
- compact audio if super-event is implemented
- world-end audio
- defeat aftermath audio
- world-consumed audio

Audio must be public-domain, licensed, generated under allowed terms, or otherwise verified. Do not wire placeholder audio. If no suitable audio exists, report the blocker instead of substituting unrelated tracks.

## Image Requirements

Image direction:

- reveal: map office, empty harbor, black coastline on chart
- compact: officials around black shore maps, covered windows
- world-end: world coastline fading into black sea
- defeat: recovered shore, blank memorial boards
- world consumed: black ledger and extinguished lamp

No gore, no monster hordes, no readable generated text.

## Localisation Key Direction

Use stable keys such as:

- `super_event.010.death_reveal.t`
- `super_event.010.death_reveal.q`
- `super_event.010.death_reveal.a`
- `super_event.010.death_world_end.t`
- `super_event.010.death_world_end.q`
- `super_event.010.death_world_end.a`

Match existing Chaos Redux super-event localisation naming if implementation patterns require a different prefix.

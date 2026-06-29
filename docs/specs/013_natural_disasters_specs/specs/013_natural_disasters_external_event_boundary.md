# Event 013 Natural Disasters external event boundary

All labels in this file are working labels and are not final localisation.

## Non reuse contract

Event 13 owns all active natural disaster gameplay after this rework. Existing disaster adjacent events are catalogue entries that need their own future rework. Their current script, tuning, effects, variables, localisation structure, and helper logic must not be used as the implementation source for Event 13.

This rule exists because the old disaster adjacent events are not source quality. They are to be reworked, so copying their behaviour would turn Event 13 into a wrapper around shallow legacy logic.

The implementation agent must build Event 13 from the Event 13 spec pack, new or existing reusable Chaos Redux helpers, central script constants, and documented dynamic effects. It must not call, copy, adapt, or tune around old event code from Sandstorm, Meteor Shower, Heat Wave, Asteroid Incoming, Earth Earthquake, Massive Flood, BOOM, or any similar disaster placeholder unless the relevant source spec says that specific old event has already been fully reworked and approved as a reusable source.

## Catalogue boundary

| Existing catalogue entry | Current role after Event 13 rework | Event 13 ownership rule |
| --- | --- | --- |
| Event 51 Heat Wave | Separate future rework. Global heat event can remain a separate event identity. | Event 13 extreme heat and drought content must not copy Event 51 logic. Event 13 must guard against stacking with active Event 51 heat effects. |
| Event 99 Sandstorm | Placeholder or thin wrapper only. | Active sandstorm gameplay belongs to Event 13. Event 99 must not keep independent damage logic. |
| Event 28 Asteroid Incoming | Separate future rework built around a single predicted object. | Event 13 meteor shower and skyfall sequences must not copy Event 28. Meteor showers are multi impact abnormal disaster sequences, not the Asteroid Incoming prediction game. |
| Event 46 Unknown Placeholder | Inactive seismic placeholder. | Earthquake, great quake, aftershock, rupture wave, and delayed tsunami content belongs to Event 13. Event 46 remains unknown and inactive. |
| Event 43 Massive Flood | Separate future rework unless the user explicitly merges it later. | Event 13 floods use their own hydrology, warning, relief, and regional aftermath logic. Do not use Event 43 as source. |
| Event 47 BOOM | Separate future rework for mysterious explosion content. | Meteor airbursts and crater fields in Event 13 must stay natural disaster content and must not copy Event 47. |

If implementation finds a separate Meteor Shower event id that is not visible in the current spreadsheet excerpt, that event follows the same rule. It is not a logic source for Event 13. It can be left as a disabled placeholder or later reworked as a separate event, but Event 13 meteor shower mechanics must come from this spec.

## Placeholder and wrapper rules

A placeholder event may do only these things.

1. Show as inactive or unknown in the catalogue.
2. Explain in Event Details that active gameplay belongs elsewhere.
3. Call a narrow Event 13 manual family launch helper only if the user explicitly wants the old entry to act as a compatibility button.
4. Exit safely when Event 13 is disabled or terminal world state blocks ordinary events.

A placeholder event must not contain independent disaster effects, independent population loss, independent building damage, independent recovery decisions, independent evolutions, independent cluster members, or independent news spam.

## Non stacking rules

Event 13 must check active state modifiers and global event states before applying family effects.

- Heat: If Event 51 Heat Wave is active in a country or state, Event 13 extreme heat must not stack the same heat modifier. It may convert the selected incident into drought stress, wildfire ignition, water emergency, or heat aftermath if the final state effect remains unique.
- Sandstorm: Event 99 must not apply a parallel dust or visibility modifier. Event 13 owns sandstorm state modifiers.
- Seismic: Event 46 remains inactive. Event 13 owns all earthquake logic.
- Meteor: Event 28 can exist as a single object event, while Event 13 owns meteor shower, airburst field, and small crater chain logic.
- Flood: Event 43 can exist later as a separate global or coastal flood event, while Event 13 owns ordinary flood and regional flood season logic.

## Implementation source hierarchy

When implementing a disaster family, use this priority order.

1. Event 13 source specs in this package.
2. Chaos Redux reusable dynamic helpers that are already documented and safe.
3. New Event 13 scripted helpers and script constants created for this feature.
4. Vanilla HOI4 examples for syntax and structure only.
5. Future approved Event 13 addenda if they have been folded into this source spec.

Do not use old disaster event files as source logic. A grep hit from Event 51, Event 99, Event 28, Event 43, Event 46, or Event 47 is not a precedent. It is a migration warning.

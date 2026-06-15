# Event 010 Death - Research And Precedent Notes

## Tone Anchors

Use these as inspiration, not literal lore claims.

| Anchor | Use |
| --- | --- |
| Flannan Isles lighthouse disappearance | Early mood: delayed discovery, no bodies, no response, official uncertainty. |
| Phantom islands | Map and chart language: places that exist administratively before the world accepts the truth. |
| Danse macabre | Equality of death and world-end achievement language. |
| Lazaretto and quarantine islands | Ordinary-country containment mechanics: cordons, inspections, port closures, isolation stations. |
| Thanatos/Charon | Focus-name inspiration only; do not turn Death into a Greek myth country. |

Useful source links:

- National Records of Scotland, Flannan Isles disappearance: https://blog.nrscotland.gov.uk/2023/12/12/flannan-isles-lighthouse-keepers-the-disappearance/
- Britannica, Dance of Death: https://www.britannica.com/art/dance-of-death-art-motif
- Britannica, lazaretto: https://www.britannica.com/science/lazaretto
- National Park Service, quarantine islands: https://www.nps.gov/places/quarantine-islands.htm
- Britannica, Thanatos: https://www.britannica.com/topic/Thanatos-Greek-mythology
- Britannica, Charon: https://www.britannica.com/topic/Charon-Greek-mythology

## Quote Sources

Verified public-domain or public-domain-underlying quote candidates:

| Role | Source |
| --- | --- |
| Reveal quote | Jeremiah 9:21 KJV, https://biblehub.com/kjv/jeremiah/9-21.htm |
| Reveal button | Isaiah 21:11 KJV, https://biblehub.com/kjv/isaiah/21-11.htm |
| World-end quote | Revelation 8:1 KJV, https://biblehub.com/kjv/revelation/8-1.htm |
| World-end button | Milton, `Paradise Lost`, https://www.gutenberg.org/files/26/26-h/26-h.htm |
| Defeat quote | Emily Dickinson, "After great pain, a formal feeling comes -", https://www.poetryfoundation.org/poems/47651/after-great-pain-a-formal-feeling-comes-372 |
| Defeat button | Isaiah 21:12 KJV, https://biblehub.com/kjv/isaiah/21-12.htm |

Avoid Poe as the primary quote unless the event deliberately wants stronger pestilence/Red Death coloration.

## Local Chaos Redux Precedents

| System | Precedent |
| --- | --- |
| event-generated actor and world-end package | Event 007 Fury |
| consuming nonhuman actor and state decay | Event 002 Zombies |
| civilian death accounting and state destruction | zombie decay and Holy Realm final silence helpers |
| world-threat source aggregation | shared `world_threat_source_*` framework |
| super-event wiring | Fury and Holy Realm super-event helpers |
| anti-threat compact pattern | Anti-Zombie League |
| event details and evolutions | events log/evolutions system docs |
| custom achievements | custom achievements system docs |

## Vanilla Precedents

| Need | Vanilla precedent direction |
| --- | --- |
| state-targeted decisions | Italy state-targeted decisions and missions |
| dynamic country/release patterns | vanilla decisions using `create_dynamic_country`, though Death should prefer fixed tag |
| state transfer | event effects using `transfer_state` |
| unit template creation and spawning | vanilla Japan event unit spawning examples |
| focus tree loading | `load_focus_tree` documentation |
| state building damage/removal | `damage_building`, `remove_building`, `set_state_category` docs/examples |

## Design Risks

- State population deletion must feed the Chaos Meter death system; raw manpower changes are not enough.
- Full occupation defeat should be scripted, because "0% surrender" alone is too vague.
- Island eligibility must protect capitals and avoid invalid states.
- Death coring prevents resistance noise but needs cleanup and recovery rules.
- Coastal jumps must be bounded by cooldown, pressure, target validity, and clear failure behavior.
- World-end footholds must not choose invalid or impassable states.
- Super-event slots and audio must be reserved only after current slot/audio files are inspected.
- The Living Compact should not casually break existing factions unless that behavior is explicitly implemented and explained.
- No whole-world daily/weekly loops are allowed without explicit approval.

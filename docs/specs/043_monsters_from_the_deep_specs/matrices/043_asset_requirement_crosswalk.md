# Event 043 asset requirement-to-runtime crosswalk

## Rule

Every accepted asset row needs a live consumer. Extra art in a folder does not satisfy a missing consumer. One asset type cannot be resized to stand in for another.

| Asset family | Required count | Runtime consumer | Design direction | Source owner | Completion evidence |
| --- | ---: | --- | --- | --- | --- |
| Country flags | 16 full monster flag triplets | Every full monster tag | Flat fictional designs, unique at small size | Generated event art after cultural review | Tag audit, ImageGen source, three sizes, GFX or engine lookup proof |
| Terminal flags | 1 Cthulhu flag triplet | Cthulhu tag | Distinct union symbol, no commercial logo | Generated event art | Terminal tag proof and all three sizes |
| Remnant flags | 16 route-aware treatments or one approved system | Abyssal Remnants | Original identity remains readable with remnant state | Generated or retained under approved rule | Explicit authorization and runtime naming |
| Static leader portraits | 16 full monsters plus Cthulhu | Country leader consumer | 156x210 nonhuman composition | Portrait creator using native ImageGen | Source prompt, full-resolution review, DDS, wiring |
| Animated leader portraits | 16 full monsters plus Cthulhu | Country leader animation consumer | Real per-frame motion and static fallback | Portrait creator plus frame-animation skill | Source frames, sheet, DDS, FPS, fallback, consumer proof |
| Remnant leader portrait | Generic institutional or nonhuman remnant leader | Remnant tags | No fake restored apex | Portrait creator when authorised | Role and consumer proof |
| Monster category pictures | 16 | Monster Dominion category | Creature and regional setting, no fake controls | Generated event art | Consumer size inspection and GFX proof |
| Human response category picture | 1 | Defend the Littoral category | Period coastal defense and evacuation | Generated event art or sourced period material | Source mode and consumer proof |
| Country report images | 16 | Creature emergence and report events | Creature-specific documentary or mythic scene | Generated event art | Event-picture DDS and sprite proof |
| Opening super-event image | 1 | Event 043 opening | Multi-region global emergence without map collage | Generated event art | Super-event slot and sprite proof |
| Cthulhu super-event image | 1 | Terminal world end | Hierarchy of Cthulhu and surviving apexes | Generated event art | Terminal slot proof |
| Defeat super-event image | 1 | Eligible global aftermath | Ruined and repaired shores | Generated or sourced according to final brief | Aftermath trigger and sprite proof |
| Apex 3D models | 16 | Unique apex divisions | Creature-specific scale, anatomy, materials, rig, actions | Meshy 7 and Blender pipeline | Provider lineage, scale crosswalk, export, reimport, runtime entity |
| Support 3D models | 6 | Shared support families | Clearly smaller than apex and role-readable | Meshy 7 and Blender pipeline | Same full 3D evidence |
| Apex counters | 16 packages | Apex map counters | Bespoke vanilla-green silhouettes | Icon artist | Installed vanilla reference, palette sampling, DDS, consumer proof |
| Support counters | 6 packages | Support map counters | Bespoke family silhouettes | Icon artist | Installed vanilla reference, palette sampling, DDS, consumer proof |
| Apex sound packages | 16 | Selection, acknowledgement, idle, move, attack, impact, death | Unique sourced nonhuman sound identity | 3D model worker research, parent wiring | Source URL, license, checksums, action sync, sound definitions |
| Support sound packages | 6 | Same applicable roles | Family-specific sourced audio | 3D model worker research, parent wiring | Source URL, license, checksums, action sync |
| Anchor focus icons | At least 160 | Ten creature-specific anchors per full tree | Separate focus art designed for 94x86 | Icon artist | Source art, DDS, sprite, focus consumer |
| Shared focus icons | As required | Shared Hunger, Sea Bond, lair, pact, terminal nodes | Coordinated but not copied cross-type art | Icon artist | Manifest and consumer proof |
| Decision icons | At least 19 families | Monster and human decisions | Readable at final decision size | Icon artist | Separate source art, DDS, GFX, decision IDs |
| Mission icons | Mission family count | Human and monster missions | Mission-specific silhouettes | Icon artist | Separate mission source art and consumers |
| Achievement icon triplets | 10 | Event 043 achievements | Eligible, grey, and not-eligible states | Icon artist | Thirty final DDS files and achievement IDs |
| Pact emblem | 1 or route variants | Abyssal faction | Original abyssal identity | Generated art or icon artist by consumer | Faction consumer proof |
| Ocean Watch emblem | 1 | Postwar or response cooperation | Human coastal observation identity | Icon artist | Decision or faction-like consumer proof |

## Minimum count summary

| Family | Minimum final items |
| --- | ---: |
| Full-monster flag files | `48` |
| Cthulhu flag files | `3` |
| Full-monster static leader portraits | `16` |
| Full-monster animated portrait sheets | `16` |
| Cthulhu static and animated portrait set | `1` set |
| Creature category pictures | `16` |
| Human response category picture | `1` |
| Creature report images | `16` |
| Super-event images | `3` |
| Unique apex 3D packages | `16` |
| Shared support 3D packages | `6` |
| Unit counter packages | `22` |
| Unit sound packages | `22` |
| Creature-specific anchor focus icons | at least `160` |
| Achievement DDS files | `30` |

The count excludes shared secondary icons, route variants, static animation fallbacks, source frames, sheet PNGs, manifests, contact sheets, and audio wrappers.

## Animation evidence

An animated portrait set includes source frames, processed frames, horizontal sheet PNG, sheet DDS, static PNG, static DDS, preview GIF, contact sheet, frame metadata, GFX definition, and verified consumer.

A GIF alone does not count.

## Temporary workspace rule

All event-scoped working assets live under `docs/assets/043_monsters_from_the_deep/` while active. Durable evidence moves into permanent documentation before the workspace is deleted at true completion.

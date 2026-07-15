# Asset Inventory Matrix

This matrix is the current runtime summary. Filename-level provenance remains in `docs/assets/014_cannibalism/manifest.md` and its linked package manifests.

| Asset family | Final runtime count | Source and final form | Current evidence | Secrecy rule |
| --- | ---: | --- | --- | --- |
| Report and news pictures | 29 | Generated fictional period scenes. 210x176 report cards and 397x153 black-and-white news DDS | 22 report plus 7 news textures, all registered | Pre-reveal pictures contain no Hannibal identity |
| Action super-events | 4 | Generated 457x328 action scenes | Reveal, ordinary world end, global defeat, Wendigo world end | Each branch and aftermath gate is distinct |
| Regional warlord portraits | 56 | Independently image-generated fictional 156x210 HOI4-style DDS busts | Eight origin-agnostic slots across Europe, Asia, Africa, Middle East, North America, South America, and Oceania | No prison settings, Hannibal likeness, or living ceremonial dress |
| Ordinary revealed portrait | 1 canonical static plus 12-frame sheet | Supplied `hannibal.dds` directly registered as the static fallback, with canonical frame `000` plus 11 image-generated motion frames in a 1872x210 sheet | Static, sheet, source frames, GIF, contact sheet, manifest, 12 fps playback, and blend-frame handoff present | `cannibalism_reveal_complete` only |
| Wendigo revealed portrait | 1 canonical static plus 16-frame sheet | Supplied `hannibal_wendigo.dds` directly registered as the static fallback, with canonical frame `000` plus 15 image-generated motion frames in a 2496x210 sheet | Static, sheet, source frames, GIF, contact sheet, manifest, 12 fps playback, and blend-frame handoff present | Reveal plus merge gate |
| Event 014 flags | 195 TGA | 13 families, 5 compositions, 3 engine sizes | 65 independently image-generated layouts flattened to five opaque runtime colors | Unified and transformed identities are reveal-gated |
| Focus icons | 204 | Focus-specific 94x86 DDS | Exact 68 warlord, 108 unified, and 28 Wendigo icon set | Gated by tree and branch visibility |
| Idea and modifier icons | 62 | Purpose-built DDS, including eight new 68x68 idea icons | Every live Event 014 idea picture has an exact registered texture | Early icons remain spoiler-safe |
| Decision and category textures | 135 | Purpose-built 32x32 icons plus category panels | Includes 38 unified icons and the 21-icon closure package | Phase and public-stage gated |
| Closure package | 21 | 20 unique 32x32 icons and one 114x101 panel | 13 objective/action icons, 2 tracker textures, 4 hunt icons, Pack receipt icon, inherited-cell icon | Tracker pair is early-safe |
| Achievement icons | 18 triplets, 54 DDS | Separate complete, grey, and not-eligible variants | All root achievement paths exist | Late Career Profile entries remain statically hidden. Tracker stages disclosure |
| Scripted-GUI statics and animations | 48 animated runtime PNG/DDS files plus 26 static GUI pairs | 12 non-portrait frame packages and exact static surfaces | Source frames, sheets, fallbacks, GIFs, contacts, and manifests present | Early/network surfaces contain no revealed identity |
| Super-event audio | 4 OGG plus 4 WAV | Unique sourced recordings at 44.1 kHz | IDs 49, 50, 52, and 53 registered and documented | Audio metadata is not surfaced before the matching event |
| Bespoke unit counters and equipment art | 0 required | No custom subunit or equipment identifiers were added | Existing battalion and equipment surfaces are retained. This is a verified scope disposition, not a fallback | No additional reveal surface exists |

## GFX closure proof

A final filesystem scan covers exactly three Event 014 GFX files: the dedicated consolidated `interface/014_cannibalism.gfx` registry and the shared `interface/chaosx_pictures.gfx` and `interface/chaosx_super_events.gfx` registries.

- Texture references: 812
- Unique texture paths: 598
- Unique texture hashes: 598
- Missing runtime files: 0

The four super-event DDS files are action compositions. The two revealed leader sheets use the exact supplied portraits as frame `000` and separately image-generated action states for every later frame. Together with the twelve non-portrait packages, the current animation inventory is exactly 14 semantic packages and 142 real source plus 142 processed frames. No completion claim depends on transform-only motion, reused decision art, or a missing fallback.

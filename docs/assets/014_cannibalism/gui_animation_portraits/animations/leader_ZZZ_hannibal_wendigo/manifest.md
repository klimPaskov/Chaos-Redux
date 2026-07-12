# leader_ZZZ_hannibal_wendigo Animated Portrait Manifest

## Package result

- Event: 014 Cannibalism
- Asset: reveal-gated transformed Hannibal Lecter animated portrait
- Classification: original fictional male-presenting supernatural transformation of the ordinary Hannibal identity; no actor or real-person likeness
- Asset status: `complete` at the asset layer; the required sprite registrations already existed and were verified without editing GFX/GUI
- Source mode: sixteen separate built-in `$imagegen` full renders
- Final frame size: 156x210
- Frame count: 16
- Horizontal sheet size: 2496x210
- Runtime rate: 6 FPS
- Review GIF timing: 170 ms per frame, looped; review only
- Looping: yes
- Play on show: yes
- Anchor: bottom-center
- Static fallback: processed frame 000
- Character key: `ZZZ_hannibal_wendigo`
- Gender presentation: male
- Intended use: transformed ZZZ country-leader portrait and Wendigo command-window portrait
- Public identity boundary: the command window requires `cannibalism_reveal_complete` and `cannibalism_wendigo_route_active`

## Visual identity and action

The transformed portrait preserves the ordinary identity through its elongated bald skull, crooked nose, old scar line, torn ears, mismatched feverish eyes, and irregular teeth. It is otherwise dramatically inhuman: elongated kinked neck, unequal jaw hinges, one larger eye socket, blade-like high shoulder, collapsed low shoulder, long many-jointed claw, frost-split corpse-grey skin, ice plates, ruined frozen scavenged period clothing, dark-crimson icy staining, and frenzied asymmetric motion.

The loop is a distinct predatory action rather than the ordinary skull lick: crouch, split-eyed tracking, neck jerk, claw unfurl, jaw unhinge, diagonal spring, farthest reach, predatory snap, inhuman apex, ice-shedding recoil, reverse head whip, swallow spasm, shoulder collapse, jaw rethread, re-crouch, and near-start twitch.

No frame contains antlers, horns, deer traits, animal skull headdress, totem, runes, dreamcatcher, feathers, beadwork, tribal or Indigenous motif/regalia, sacred symbol, ritual circle, ceremonial garment, or cultural-authenticity claim. There is also no actor likeness or ancient-general/Carthaginian/Punic/elephant/classical framing.

## Paths and registered sprites

- Prompt record: `notes/source_prompts.md`
- Frame plan: `frame_plan.md`
- Source frames: `source_frames/leader_ZZZ_hannibal_wendigo_000_source.png` through `source_frames/leader_ZZZ_hannibal_wendigo_015_source.png`
- Processed frames: `processed_frames/leader_ZZZ_hannibal_wendigo_000.png` through `processed_frames/leader_ZZZ_hannibal_wendigo_015.png`
- Static PNG: `sheets/leader_ZZZ_hannibal_wendigo_static.png`
- Sheet PNG: `sheets/leader_ZZZ_hannibal_wendigo_sheet.png`
- Source contact sheet: `previews/leader_ZZZ_hannibal_wendigo_source_contact.png`
- Final-size contact sheet: `previews/leader_ZZZ_hannibal_wendigo_contact.png`
- Review GIF: `previews/leader_ZZZ_hannibal_wendigo_preview.gif`
- Runtime static DDS: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_static.dds`
- Runtime sheet DDS: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds`
- Character/static sprite: `GFX_portrait_ZZZ_hannibal_wendigo`
- GUI static sprite: `GFX_cannibalism_wendigo_portrait_static`
- GUI animated sprite: `GFX_cannibalism_wendigo_portrait_animated`
- Registered GFX file: `interface/014_cannibalism.gfx`
- Consuming GUI: `interface/014_cannibalism_frontline_hunger.gui`

## Frame source ledger

| Frame | Source mode | Source path | Frame-specific generated state |
| --- | --- | --- | --- |
| 000 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_000_source.png` | crooked inhuman predator crouch and static fallback |
| 001 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_001_source.png` | split-eyed tracking and independently flexed claw |
| 002 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_002_source.png` | reverse neck jerk, opening jaw, and shoulder drive |
| 003 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_003_source.png` | foreshortened claw unfurl toward viewer |
| 004 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_004_source.png` | unequal jaw unhinge and advancing claw |
| 005 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_005_source.png` | diagonal torso spring with tongue lash and ice shards |
| 006 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_006_source.png` | farthest frenzied reach and stretched neck |
| 007 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_007_source.png` | off-center predatory jaw snap and hooked recoil |
| 008 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_008_source.png` | maximum corkscrewed inhuman apex |
| 009 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_009_source.png` | ice-shedding diagonal recoil |
| 010 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_010_source.png` | reverse S-neck head whip and tongue lash |
| 011 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_011_source.png` | crooked swallow spasm and one-sided frost breath |
| 012 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_012_source.png` | shoulder collapse/swap and sternum-crawling claw |
| 013 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_013_source.png` | jaw rethreads into distorted feral grin |
| 014 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_014_source.png` | tense re-crouch with hovering claw |
| 015 | built-in imagegen full redraw | `source_frames/leader_ZZZ_hannibal_wendigo_015_source.png` | near-start twitch and smooth independent loop return |

## Processing

Processing was mechanical only: fixed center cover crop to 156x210, Lanczos resize, 1.04 contrast, 0.92 colour, 1.04 sharpness, static extraction from accepted frame 000, horizontal sheet assembly, contact-sheet assembly, GIF assembly, hashing, and conversion through `.tools/convert_to_dds.py`.

The DDS files are one-surface uncompressed 32-bit BGRA/B8G8R8A8-style files with one stored image and no generated mip chain. The runtime DDS pixels decode identically to the matching PNGs.

## Protected legacy assets

`gfx/leaders/014_cannibalism/hannibal.dds` and `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` were not modified. The registered live Wendigo paths are the `leader_ZZZ_hannibal_wendigo_*` files listed above.

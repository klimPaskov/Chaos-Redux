# leader_CBL_hannibal Animated Portrait Manifest

## Package result

- Event: 014 Cannibalism
- Asset: ordinary reveal-gated Hannibal Lecter animated portrait
- Classification: original fictional male-presenting human-origin leader; no actor or real-person likeness
- Asset status: `complete` at the asset layer; the required sprite registrations already existed and were verified without editing GFX/GUI
- Source mode: twelve separate built-in `$imagegen` full renders, plus one retained identity-only reference that is not a runtime frame
- Final frame size: 156x210
- Frame count: 12
- Horizontal sheet size: 1872x210
- Runtime rate: 6 FPS
- Review GIF timing: 170 ms per frame, looped; review only
- Looping: yes
- Play on show: yes
- Anchor: bottom-center
- Static fallback: processed frame 000
- Character key: `CBL_hannibal`
- Gender presentation: male
- Intended use: revealed CBL country-leader portrait and reveal command-window portrait
- Public identity boundary: Hannibal is not recruited or shown until `cannibalism_reveal_complete`

## Visual identity and action

The accepted portrait is gaunt, pallid, bald, long-faced, crooked, torn-eared, heavily scarred, bloodshot, irregular-toothed, severely dark-crimson stained, and visibly ecstatic and feral. The clothing is invented, symbol-free, scavenged 1936-1945 command clothing rather than a national uniform or tailored fashion coat.

The loop is a real action sequence: skull clutch, lift, tongue approach, first contact, upward drag, eye-socket sweep, crown apex, wet pull-away, second cheekbone lap, lowering, swallow, and near-start return. Jaw, tongue, fingers, eyes, skull angle, wet stains, shoulders, and cloth are newly rendered in every source frame.

Prohibited visual language was excluded: no actor likeness; no ancient-general, Carthaginian, Punic, elephant, classical, laurel, toga, or legionary framing; no antlers, horns, sacred motif, Indigenous motif, political symbol, insignia, text, or watermark.

## Paths and registered sprites

- Prompt record: `notes/source_prompts.md`
- Frame plan: `frame_plan.md`
- Source frames: `source_frames/leader_CBL_hannibal_000_source.png` through `source_frames/leader_CBL_hannibal_011_source.png`
- Processed frames: `processed_frames/leader_CBL_hannibal_000.png` through `processed_frames/leader_CBL_hannibal_011.png`
- Static PNG: `sheets/leader_CBL_hannibal_static.png`
- Sheet PNG: `sheets/leader_CBL_hannibal_sheet.png`
- Source contact sheet: `previews/leader_CBL_hannibal_source_contact.png`
- Final-size contact sheet: `previews/leader_CBL_hannibal_contact.png`
- Review GIF: `previews/leader_CBL_hannibal_preview.gif`
- Runtime static DDS: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds`
- Runtime sheet DDS: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`
- Character sprite: `GFX_portrait_CBL_hannibal`
- GUI static sprite: `GFX_cannibalism_revealed_portrait_static`
- GUI animated sprite: `GFX_cannibalism_revealed_portrait_animated`
- Registered GFX file: `interface/014_cannibalism.gfx`
- Consuming GUI: `interface/014_cannibalism_frontline_hunger.gui`

## Frame source ledger

| Frame | Source mode | Source path | Frame-specific generated state |
| --- | --- | --- | --- |
| 000 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_000_source.png` | feral skull clutch and static fallback |
| 001 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_001_source.png` | skull rises; wrists, fingers, jaw, eyes, and shoulders change |
| 002 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_002_source.png` | tongue extends toward stained temple without contact |
| 003 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_003_source.png` | first tongue contact on temple |
| 004 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_004_source.png` | upward tongue drag toward brow |
| 005 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_005_source.png` | eye-socket sweep with rotated skull and changed grip |
| 006 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_006_source.png` | crown-lick apex with maximum tongue extension and asymmetry |
| 007 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_007_source.png` | wet pull-away, redrawn recoil grip, and strand |
| 008 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_008_source.png` | second cheekbone lap with new jaw and shoulder angle |
| 009 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_009_source.png` | tongue retracts and skull rolls down |
| 010 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_010_source.png` | ecstatic swallow with lower skull position |
| 011 | built-in imagegen full redraw | `source_frames/leader_CBL_hannibal_011_source.png` | independently redrawn near-start clutch and loop return |

## Processing

Processing was mechanical only: fixed center cover crop to 156x210, Lanczos resize, 1.04 contrast, 0.92 colour, 1.04 sharpness, static extraction from accepted frame 000, horizontal sheet assembly, contact-sheet assembly, GIF assembly, hashing, and conversion through `.tools/convert_to_dds.py`.

The DDS files are one-surface uncompressed 32-bit BGRA/B8G8R8A8-style files with one stored image and no generated mip chain. The runtime DDS pixels decode identically to the matching PNGs.

## Protected legacy assets

`gfx/leaders/014_cannibalism/hannibal.dds` and `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` were not modified. The registered live CBL paths are the `leader_CBL_hannibal_*` files listed above.

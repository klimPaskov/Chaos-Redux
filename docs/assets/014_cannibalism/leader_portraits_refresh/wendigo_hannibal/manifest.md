# Event 014 Wendigo Hannibal portrait manifest

Status: canonical static portrait directly registered, genuine source-frame animation installed, and live GFX registration updated.

## Canonical portrait

- Required input: `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`.
- Live static fallback and character portrait: `gfx/leaders/014_cannibalism/hannibal_wendigo.dds` (the exact user-supplied canonical file).
- The canonical live file has SHA-256 `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717`.
- Decoded source for generation reference: `source_png/leader_ZZZ_hannibal_wendigo_static_source.png`.
- Decoded processed master: `processed_png/leader_ZZZ_hannibal_wendigo_static.png`, 156x210.
- Frame `000` is the exact decoded canonical portrait. It is not a generated substitute.

## Animation package

- Frames: 16 source states under `source_png/frames/`, ordered `000` through `015`.
- Frame provenance: canonical frame `000`, followed by 15 accepted image-generated motion frames.
- Generation record: 16 successful edit outputs for frames `001`-`015`; one earlier frame-`015` bridge was superseded by the accepted closer loop bridge.
- Processed frames: 16 files under `processed_png/frames/`, each 156x210.
- Horizontal sheet: `processed_png/leader_ZZZ_hannibal_wendigo_sheet.png`, 2496x210.
- Live sheet: `gfx/leaders/014_cannibalism/leader_ZZZ_hannibal_wendigo_sheet.dds`.
- Preview: `previews/leader_ZZZ_hannibal_wendigo_preview.gif`, 16 frames, 1,330 ms, approximately 12 fps.
- Review surfaces: source and processed contact sheets under `contact_sheets/`, plus individual review sheets under `contact_sheets/reviews/`.
- Playback smoothing: the live sprite uses the vanilla `gfx/FX/buttonstate_blendframes.lua` effect.

Every motion frame after `000` is a real image-generation output. No accepted frame was manufactured by translating, scaling, warping, recolouring, filtering, or interpolating one still.

## Frame ledger

| Frame | State |
| --- | --- |
| `000` | Exact supplied portrait; sealed jaw and fixed stare. |
| `001` | Red eyes ignite and the jaw seam separates. |
| `002` | Jaw opens and the tongue appears. |
| `003` | Tongue curls out of the widening maw. |
| `004` | Tongue reaches toward a bone-white skull fragment. |
| `005` | Tongue coils around the fragment. |
| `006` | Coiled fragment is drawn toward the teeth. |
| `007` | Jaw reaches its maximum nonhuman gape. |
| `008` | Teeth close around the fragment. |
| `009` | The fragment cracks inside the mouth. |
| `010` | First chewing state. |
| `011` | Second chewing state and tongue retraction. |
| `012` | Mouth narrows through the swallow. |
| `013` | Jaw rises toward recovery. |
| `014` | Nearly closed fixed stare. |
| `015` | Closed-mouth bridge near canonical rest. |

## Live bindings

- `GFX_portrait_ZZZ_hannibal_wendigo` and `GFX_cannibalism_wendigo_portrait_static` use the exact supplied static portrait file directly.
- `GFX_cannibalism_wendigo_portrait_animated` uses the 16-frame sheet at 12 fps.
- All bindings are in the consolidated `interface/014_cannibalism.gfx` file.

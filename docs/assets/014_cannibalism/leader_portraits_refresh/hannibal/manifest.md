# Event 014 Hannibal Lecter portrait manifest

Status: canonical static portrait directly registered, genuine source-frame animation installed, and live GFX registration updated.

## Canonical portrait

- Required input: `gfx/leaders/014_cannibalism/hannibal.dds`.
- Live static fallback and character portrait: `gfx/leaders/014_cannibalism/hannibal.dds` (the exact user-supplied canonical file).
- The canonical live file has SHA-256 `5c48c9a5b503c3185dcb38ee1aabc403d7668094079b78a20010323930d10b88`.
- Decoded source for generation reference: `source_png/leader_CBL_hannibal_static_source.png`.
- Decoded processed master: `sheets/leader_CBL_hannibal_static.png`, 156x210.
- Frame `000` is the exact decoded canonical portrait. It is not a generated substitute.

## Animation package

- Frames: 12 source states under `source_frames/`, ordered `000` through `011`.
- Frame provenance: canonical frame `000`, followed by 11 separately generated identity-preserving image edits.
- Processed frames: 12 files under `processed_frames/`, each 156x210.
- Horizontal sheet: `sheets/leader_CBL_hannibal_sheet.png`, 1872x210.
- Live sheet: `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`.
- Preview: `previews/leader_CBL_hannibal_preview.gif`, 12 frames, 1,000 ms, approximately 12 fps.
- Review surfaces: source and processed contact sheets under `previews/`, plus individual review sheets under `review_sheets/`.
- Playback smoothing: the live sprite uses the vanilla `gfx/FX/buttonstate_blendframes.lua` effect.

Every motion frame after `000` is a real image-generation output. No accepted frame was manufactured by translating, scaling, warping, recolouring, filtering, or interpolating one still.

## Frame ledger

| Frame | State |
| --- | --- |
| `000` | Exact supplied portrait; direct canonical stare. |
| `001` | Eyes lower as the fork begins entering frame. |
| `002` | Gloved hand raises the same fork and morsel to the chest. |
| `003` | Fork reaches the mouth; tongue tip appears. |
| `004` | Tongue extends toward the stained tines. |
| `005` | Tongue makes first contact with the fork. |
| `006` | Deliberate lick continues along the tines. |
| `007` | Teeth close on the morsel. |
| `008` | Fork withdraws as chewing begins. |
| `009` | Chewing continues under direct eye contact. |
| `010` | Fork lowers and the expression settles. |
| `011` | Utensil leaves frame and the portrait returns close to canonical rest. |

## Live bindings

- `GFX_portrait_CBL_hannibal` and `GFX_cannibalism_revealed_portrait_static` use the exact supplied static portrait file directly.
- `GFX_cannibalism_revealed_portrait_animated` uses the 12-frame sheet at 12 fps.
- All bindings are in the consolidated `interface/014_cannibalism.gfx` file.

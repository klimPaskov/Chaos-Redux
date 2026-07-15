# Event 014 Revealed Hannibal Portrait Manifest

Status: visually approved, assembled, and installed in the existing static and animated DDS paths.

## Identity masters

- Selected static source: `source_png/leader_CBL_hannibal_static_source.png`.
- Selected static processed PNG: `sheets/leader_CBL_hannibal_static.png`, 156x210.
- Rejected but retained review candidate: `source_png/rejected/leader_CBL_hannibal_static_rejected_composed.png`.
- Identity direction: bald fictional commander, cloudy misaligned eye, damaged ear, dense scar web, irregular teeth, feral grin, and a map-and-shelf command studio with no confinement imagery.

## Animation package

- 12 separately generated identity-preserving edit sources under `source_frames/`.
- 12 deterministic 156x210 processed frames under `processed_frames/`.
- Horizontal sheet: `sheets/leader_CBL_hannibal_sheet.png`, 1872x210.
- Review GIF: `previews/leader_CBL_hannibal_preview.gif`, 12 frames over exactly 2 seconds, averaging 6 fps.
- Source contact sheet: `previews/leader_CBL_hannibal_source_contact_sheet.png`.
- Processed contact sheet: `previews/leader_CBL_hannibal_processed_contact_sheet.png`.
- Per-frame processor metadata and comparison sheets: `metadata/` and `review_sheets/`.

The frames are real image-model edits derived from the selected static identity master. No frame is a transform-only, filter-only, recolour-only, or overlay-only derivative.

## Frame content

| Frame | State |
| --- | --- |
| `000` | Skull barely enters at the lower edge; direct stare. |
| `001` | Skull raised to lower chest. |
| `002` | Skull lifted and turned toward Hannibal. |
| `003` | Skull appraised beside the cheek. |
| `004` | Tongue begins extending toward the skull. |
| `005` | Tongue approaches with a visible gap. |
| `006` | First tongue-to-skull contact. |
| `007` | Peak deliberate lick. |
| `008` | Contact completes at the cheekbone. |
| `009` | Tongue retracts and eye contact returns. |
| `010` | Skull lowers; broad feral grin. |
| `011` | Skull returns to the lower edge for the loop. |

## Image-generation accounting

- Hannibal invocations: 15.
- Selected deliverables: one static identity master and 12 frame sources.
- Additional successful output retained for review history: one rejected composed static candidate.
- Failed/non-persisted Hannibal attempt: one first attempt at frame `005`, rejected by moderation before a successful safer retry.
- Combined CBA-CBD plus Hannibal package: 60 built-in image-generation invocations, 41 selected deliverables, 14 preserved rejected review sources, and five failed/non-persisted attempts.

## Live outputs

- `gfx/leaders/014_cannibalism/leader_CBL_hannibal_static.dds`, 156x210.
- `gfx/leaders/014_cannibalism/leader_CBL_hannibal_sheet.dds`, 1872x210, 12 horizontal frames.
- Existing `gfx/leaders/014_cannibalism/hannibal.dds` is a separate asset and was not changed.

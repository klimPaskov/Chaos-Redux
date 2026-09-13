# Event 023 device-disablement decision icon handoff

Status: production complete; parent `.gfx` wiring, path reconciliation, and live consumer review remain `needs_user_review`.

Asset: `sov_nuclear_decision_device_disablement`, a dedicated decision icon for `sov_nuclear_bombs_disable_devices` in Event 023 `sov_nuclear_bombs`.

The icon shows an inert olive nuclear-device module secured in a steel isolation cradle, with the front connector open and a red safety plug removed on a short disconnected cable. It is distinct from the existing authentication, dismantlement, device-assembly, hold/abort, depot-recall, and storage-hardening icons.

## Runtime handoff

| Item | Exact value |
| --- | --- |
| Decision id | `sov_nuclear_bombs_disable_devices` |
| Proposed sprite | `GFX_decision_sov_nuclear_decision_device_disablement` |
| Final DDS | `gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_device_disablement.dds` |
| Runtime dimensions | `33x32` |
| Source PNG | `docs/assets/023_sov_nuclear_bombs/source_png/decisions/sov_nuclear_decision_device_disablement_source.png` |
| Processed PNG | `docs/assets/023_sov_nuclear_bombs/processed_png/decisions/sov_nuclear_decision_device_disablement_33x32.png` |
| Decoded DDS review PNG | `docs/assets/023_sov_nuclear_bombs/notes/decoded_dds_icons/sov_nuclear_decision_device_disablement.png` |
| Contact sheet | `docs/assets/023_sov_nuclear_bombs/contact_sheets/decision_device_disablement_review.png` |
| Prompt | `docs/assets/023_sov_nuclear_bombs/prompts/sov_nuclear_decision_device_disablement.txt` |
| Suggested registry | `interface/023_sov_nuclear_bombs.gfx` |

Ready-to-copy parent-owned sprite definition:

```text
spriteType = { name = "GFX_decision_sov_nuclear_decision_device_disablement" texturefile = "gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_device_disablement.dds" }
```

The final path follows the explicit asset-worker assignment in the parent prompt. Existing Event 023 decision textures use the established repository precedent `gfx/interface/decisions/023_sov_nuclear_bombs/`; no duplicate DDS was created there. The parent must keep the requested final path or deliberately reconcile the path before wiring.

## Production and provenance

Source mode: official built-in ImageGen, fresh generated source with a genuinely transparent background requested in the initial call.

The selected native source is `1254x1254` RGBA with alpha range `0..255`, zero-alpha corners, visible bounds `(103, 21, 1192, 1228)`, and no source-canvas edge clipping.

Processing used the existing Event 023 contained Lanczos pipeline with a one-pixel inset to `33x32`, preserving alpha and clamping only sub-2 alpha fringe values as in the established package process.

No background-removal fallback, chroma key, matte repair, transform-only substitute, reused vanilla art, or cross-type resized icon was used.

Two earlier native ImageGen candidates were rejected before promotion because their source silhouettes approached or touched source-canvas edges; only the selected safe-margin source is retained at the assigned source path.

## Checksums and audit evidence

| File | SHA-256 |
| --- | --- |
| Source PNG | `60ce859233883123d598bec419703442749dbf7f47ca6f4477f124fe110cdeb5` |
| Processed PNG | `5d1da1eab1e1fce3fdadc7f08ca0994e6fa360e1cb4bee48c782e033db48bba3` |
| Final DDS | `f996088b851e527fa9bd3b1cc36aeaa9e910f3e909fa92303e9b0643b9a27ffe` |

Strict DDS audit: `DDS ` magic, header size `124`, `33x32` dimensions, pitch `132`, mip count `0`, 32-bit BGRA pixel format, flags `65`, fourCC `0`, masks `0x00ff0000/0x0000ff00/0x000000ff/0xff000000`, texture caps `0x1000`, exact length `4352` bytes, and alpha range `0..255`.

Pixel audit: decoded DDS pixels match the processed PNG byte-for-byte; decoded bounds are `(4, 5, 28, 25)`; all four decoded corners are alpha `0`.

Visual audit: the source PNG, processed PNG, decoded DDS PNG, and dedicated contact sheet were opened individually. The native-size preview remains legible as a compact isolated device with a visible open connector and red removed plug, without clipping, halo, matte, fake checkerboard, or unintended transparent holes.

Distinctness audit: the candidate is not an exact pixel duplicate of any inspected Event 023 neighbor. At `33x32`, alpha-mask IoU / checker-background RGB MAE were `authentication 0.412 / 36.7`, `dismantlement 0.421 / 32.1`, `device_assembly 0.403 / 31.6`, `hold_abort 0.405 / 30.4`, `depot_recall 0.438 / 26.2`, and `storage_hardening 0.409 / 28.8`.

Full per-file validation notes and the manifest row are in `docs/assets/023_sov_nuclear_bombs/notes/icon_validation.md` and `docs/assets/023_sov_nuclear_bombs/manifest.md`.

## Reference audit

The canonical decision family was inspected before generation at `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decisions/`, beginning with `contact_sheet.png`, then the individual canonical `decision_generic_disband_irregulars.png`, `decision_generic_intelligence_operation.png`, and `decision_border_war.png` references.

Existing Event 023 decision peers were inspected only as runtime-family neighbors for visual distinctness, not used as source art: `authentication`, `dismantlement`, `device_assembly`, `hold_abort`, `depot_recall`, and `storage_hardening`.

No `.gfx`, gameplay, localisation, GUI, portrait, flag, animation, report, news, or 3D files were edited.

User-live limitation: this worker did not wire or validate the in-game consumer. The parent must register the proposed sprite, ensure the final texture path matches the selected registry path, and perform live Event 023 decision-surface review.

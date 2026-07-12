# Event 018 selected-field UI validation record

## Count and identity checks

| Family | Planned source frames | Present source frames | Unique source hashes | Present processed frames | Unique processed hashes | Preview frames |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Seal | 10 | 10 | 10 | 10 | 10 | 10 |
| Unsafe | 10 | 10 | 10 | 10 | 10 | 10 |
| Disturbance | 12 | 12 | 12 | 12 | 12 | 12 |
| Breach | 12 | 12 | 12 | 12 | 12 | 12 |
| Sealing | 12 | 12 | 12 | 12 | 12 | 12 |
| Total animated | 56 | 56 | 56 | 56 | 56 | 56 |

Suspended and Closed are two additional separately generated state frames. Animated plus static state art therefore totals 58 real frames. The panel is additional background art.

## Animation-art inspection

- Seal redraws the bucket, drum, flywheel, drill, lamp, cart load, and sample tray across a productive cycle. No unsafe, magical, or creature element appears.
- Unsafe redraws corroded supports, cracked timber, failing clamps, loose fasteners, rubble, the jammed cart, and lamp movement. Damage persists and no creature appears.
- Disturbance redraws physical fractures, sheared strata, tools, pebbles, slabs, dust, and the swinging lamp. No magical glow or energy effect appears.
- Breach redraws the open shaft, bent gate, cable, dust pressure, falling stone, rubble profile, and moving silhouettes at changing depths.
- Sealing redraws the hoist beam, brackets, shutter, pump hose, concrete fill, drainage, pins, and next-work position through a real engineering cycle.
- The first and final source frames of every family approach the same operating state without duplicating a frame. Review contact sheets show the full transition order.
- No two source or processed frames share a SHA-256 hash. Consecutive processed frames change at least 38.48 percent of canvas pixels above the comparison threshold, consistent with redrawn local scene content rather than a filter-only pulse.

## Image and alpha checks

- Every processed frame is exactly 128 by 128.
- Every processed frame has alpha value 0 in all four corner pixels.
- The visible-pixel chroma contamination test found zero green-key pixels in every processed frame.
- Shared-scale normalization preserves one center and bottom anchor per family.
- The sheet section for every frame is pixel-identical to its processed PNG.
- Every static fallback is pixel-identical to processed frame 000.
- Suspended and Closed have transparent unused pixels and remain legible at 128 by 128.
- The panel is exactly 470 by 304 and has no baked text.

## Runtime checks

- Runtime textures present: 13 of 13.
- Seal and Unsafe sheet size: 1280 by 128.
- Disturbance, Breach, and Sealing sheet size: 1536 by 128.
- Panel size: 470 by 304.
- Static fallback, Suspended, and Closed sizes: 128 by 128.
- All DDS files use one-surface uncompressed 32-bit BGRA with masks `00FF0000`, `0000FF00`, `000000FF`, and `FF000000`.
- Every DDS decodes pixel-identically to its processed PNG source.
- GIF frame counts are exactly 10, 10, 12, 12, and 12. GIFs are review-only and are not referenced by GFX.

## Layout inspection

The exact-position composite places each 128 by 128 state image at global panel coordinates x 306, y 86. This corresponds to the live child position x 290, y 4 inside either 438 by 180 active/history selection container at global position x 16, y 82. All seven state images remain inside the content area and align with the panel's right-side medallion recess.

## Processing correction recorded

Initial alpha processing used the nominal `#00ff00` key. Visual contact-sheet inspection found that the generated green background was slightly darker than the nominal value and caused three families to normalize too small. The final pass samples the actual border green for each frame, removes detached neighboring-atlas slivers without changing the main scene art, and regenerates every processed frame, sheet, fallback, preview, contact sheet, and DDS. All hashes in the package inventory describe the corrected final pass.

## Remaining parent-owned wiring check

The Closed sprite is registered in `interface/018_resources_found.gfx` and consumed by the live `resources_found_gui_closed_selection` container. The parent decision category and scripted GUI expose it only through a verified exact-seal history pointer, including when no active field remains. That pointer is independent of the active selected-field registry, so the state remains permanently ineligible for projects and rediscovery.

# CHU federal-presidium durable source archive repair — 2026-08-03

## Scope

The current worktree audit found that `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_federal_presidium.png` had been reduced to a three-byte non-image artifact. This handoff repairs the archive only; it does not promote IW-043, change runtime DDS/GFX wiring, create advisor art, or use the obsolete pasted flag-log.

## Repair

- Preserved the documented archival source at `docs/assets/portraits/006_independence_wave/portrait_CHU_independence_wave_federal_presidium_source.jpg`.
- Recreated `portrait_CHU_independence_wave_federal_presidium.png` as a lossless original-size PNG copy of that source (`863x1272`, grayscale), without repainting, filtering, recolouring, resizing, or cropping.
- Removed the stale generated-prompt TXT beside this grounded source-placeholder archive row. Prompts remain reserved for generated or explicitly styled portraits.

The repaired PNG decodes successfully with Pillow and is retained as evidence only. The existing CHU package and its portrait/rights/role admission gates remain fail-closed.

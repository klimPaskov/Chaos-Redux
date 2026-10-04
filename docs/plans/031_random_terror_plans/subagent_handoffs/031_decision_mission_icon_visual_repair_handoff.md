# Event 31 decision and mission icon repair

## Disposition and scope

Disposition: implemented for the 40 decision and eight mission runtime icons.

The active user goal and attached visual-audit request authorize final art and visual repairs for every accepted Event 31 decision and mission row.

The icon worker produced 48 separate ImageGen source masters in `docs/assets/031_random_terror/icon_visual_repair_20260904/source_png/` before its handle became unavailable.

The parent completed processing and runtime installation from those source masters on 2026-09-05 and revalidated the current files on 2026-10-03.

## Runtime and consumer evidence

All 48 runtime files live under `gfx/interface/decisions/031_random_terror/` and retain their pre-registered filenames.

The final sprites are registered in `interface/031_random_terror.gfx` and consumed by the existing Event 31 decisions and missions.

The exact filename, sprite, SHA-256, dimensions, and consumer file for each repaired icon are recorded in the 40 Decision icon rows and eight Mission icon rows of `../031_random_terror_visual_asset_inventory.md`.

The mission aliases use `GFX_decision_mission_random_terror_*`.

Five actor icon filenames differ from their sprite suffixes, which remain stable:

| Runtime basename | Registered sprite |
| --- | --- |
| `decision_random_terror_actor_actor_merger` | `GFX_decision_random_terror_actor_absorb_actor` |
| `decision_random_terror_actor_coerced_extraction` | `GFX_decision_random_terror_actor_force_extraction` |
| `decision_random_terror_actor_foreign_fighters` | `GFX_decision_random_terror_actor_foreign_fighter_recruitment` |
| `decision_random_terror_actor_jihadist_international_membership` | `GFX_decision_random_terror_actor_jihadist_international` |
| `decision_random_terror_actor_leadership_contest` | `GFX_decision_random_terror_actor_network_contest` |

No category picture, focus icon, idea icon, portrait, achievement state, or unrelated icon was replaced by this repair.

## Processing and visual review

Each source was cropped to its visible alpha bounds, fitted within a 30x30 footprint on a transparent 32x32 canvas, and downsampled with Lanczos.

The processing used contrast 1.10, colour 0.92, a restrained unsharp mask, and a small dark alpha shadow to preserve silhouettes against variable backgrounds.

The canonical `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` converter produced the one-level legacy BGRA DDS outputs.

Every output was decoded and compared with the corresponding processed PNG.

The parent inspected the complete source sheet, the processed 32x32 family shown at 3x, and decoded-final evidence for subject separation, clipping, silhouette, crop, alpha, and legibility.

The repaired symbols replace the previously dense scene compositions that lost readability at 32x32.

## Transparency fallback

Forty-seven sources retained native ImageGen transparency.

`mission_random_terror_prevent_capital_seizure_source.png` was emitted as RGB with an unwanted pale backdrop.

The parent preserved that source and removed only pale, low-chroma pixels connected to the canvas edge using a deterministic flood mask.

The recorded mask criteria were minimum RGB channel 164 and maximum channel spread 34, followed by a 1.2-pixel alpha blur before final downsampling.

The repaired subject and exterior edges were visually reviewed in the processed sheet, and the final DDS is pixel-equal to the processed PNG.

This is a recorded background-removal fallback, not a native-alpha source.

The current asset skill's preferred edit-to-transparency recovery step was not retained in the earlier attempt history, so that procedural evidence remains open for final asset acceptance.

## Retained temporary evidence

- Prompt record: `docs/assets/031_random_terror/icon_visual_repair_20260904/prompts/031_decision_mission_icon_visual_repair_prompt_record.md`
- Original masters: `docs/assets/031_random_terror/icon_visual_repair_20260904/source_png/`
- Processed candidates: `docs/assets/031_random_terror/icon_visual_repair_20260904/processed_png/`
- DDS roundtrips: `docs/assets/031_random_terror/icon_visual_repair_20260904/roundtrip/`
- Source contact sheet: `contact_sheets/01_native_sources_48.png`
- Processed review: `contact_sheets/02_processed_native_48.png`
- Decoded-final review: `contact_sheets/03_decoded_dds_native_48.png`
- Source, processed, runtime, and roundtrip hashes: `validation.json` in that package

The temporary workspace remains because Event 31 has incomplete portrait consumers, open audits, and outstanding final acceptance evidence.

## Current validation

The 2026-10-03 recheck read all 48 current runtime files, decoded them, compared every RGBA pixel with the corresponding processed PNG, checked the retained runtime hash, and resolved the exact GFX sprite.

Result: 48 checked and zero dimension, pixel-equality, runtime-hash, or registration mismatches.

No in-game validation is claimed.

This handoff closes the interrupted processing and installation work but does not close the complete Event 31 visual acceptance audit.

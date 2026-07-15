# Event 014 Achievement Icon Manifest

Date: 2026-07-12

The current Event 014 campaign set has 18 purpose-built generated masters and 54 exact runtime states. The authoritative IDs are derived from `interface/014_cannibalism_achievements.gfx`; the processor refuses anything other than 18 complete registered triplets.

## Output contract

- Generated masters: `source_png/<achievement_id>_source.png`
- Chroma-cleaned masters: `alpha_png/<achievement_id>_alpha.png`
- Completed, true monochrome, and not-eligible PNGs: `processed_png/`
- Package DDS triplets: `dds/`
- Runtime DDS triplets: `gfx/achievements/`
- Exact size: 64x64
- DDS: uncompressed one-image-level 32-bit BGRA, fully opaque
- Completed treatment: generated subject over a dark achievement field with the package frame
- Grey treatment: true per-pixel monochrome derived only after the completed icon exists
- Not-eligible treatment: an exact copy of the 64x64 RGBA grey variant with `.agents/skills/chaos-redux-event-assets/assets/achievements/overlay.png` alpha-composited on top; no brightness adjustment, darkening, filtering, recolouring, or locally redrawn X

No completed icon reuses a focus, idea, decision, report, portrait, or earlier achievement composition. `014_cannibalism_stop_the_reveal` is explicitly face- and silhouette-free. The Wendigo terminal icon contains no antlers, horns, runes, regalia, feathers, sacred motif, or living-cultural claim.

## Proof

- 54-row path/hash/format/variant validation: `validation/achievement_icon_validation.tsv`
- Exact 18-row sprite handoff: `validation/achievement_gfx_handoff.tsv`
- Generated master review: `contact_sheets/achievement_source_contact_sheet.png`
- Completed/grey/not-eligible review: `contact_sheets/achievement_final_variants_contact_sheet.png`
- Runtime DDS decode review: `contact_sheets/achievement_dds_decoded_contact_sheet.png`
- Generation-output and source-hash ledger: `prompts/achievement_generation_ledger.md`
- Reproducible processor: `process_achievement_icons.py`

The processor refuses to run if the mandated overlay is missing, is not 64x64, or is not RGBA. It also verifies that every not-eligible PNG is byte-for-byte identical to the result of alpha-compositing that exact overlay over a copy of its grey variant before DDS conversion.

The former 13-ID package under `static_icons_imagegen/achievements/` is superseded and inactive. Its unrelated IDs are not registered by the current Event 014 achievement GFX file, and its overlapping `no_second_table` runtime triplet has been replaced by this package's newly generated master.

Runtime cleanup removed the twelve obsolete triplets on 2026-07-12. `gfx/achievements/` now contains exactly the 54 Event 014 textures registered by `interface/014_cannibalism_achievements.gfx`, with no unregistered historical Event 014 triplets.

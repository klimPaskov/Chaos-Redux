# Stage 4 HQ command visual inspection notes

## References inspected

- Stage 3 large-counter contact sheet: `../stage_3_regimental_support/contact_sheets/unit_large_contact_sheet_checker.png`.
- Stage 3 small-counter contact sheet: `../stage_3_regimental_support/contact_sheets/unit_small_contact_sheet_checker.png`.
- Stage 3 technology contact sheet: `../stage_3_regimental_support/contact_sheets/technology_contact_sheet_checker.png`.
- Stage 3 zoom references for large, small, and technology DDS framing, copied into `source_png/references/` for this package.
- Chaos Redux reference folders `.agents/skills/chaos-redux-event-assets/assets/focuses`, `ideas`, `decisions`, and `tech_icons/small` and `tech_icons/medium`.
- Existing Chaos Redux CBRN technology DDS examples, including `gfx/interface/technologies/cbrn_hazard_pioneer_formation.dds`, for the 64x64 alpha and header contract.
- Existing Chaos Redux ability registration pattern in `interface/chaosx_ability.gfx` for proposed ability sprite naming. No GFX file was edited.

## Style decisions

- Large counters use centered, equipment-forward WWII staff and field-service emblems with olive/khaki/steel/brass materials, dark outlines, and restrained toxic green accents.
- Small counters were independently generated as long horizontal bone-white silhouettes with charcoal/olive cuts, because the Stage 3 examples are materially different from the large-counter treatment at 30x12.
- Ability icons use a single compact subject or controlled equipment cluster with stronger silhouettes and less interior detail than the counters.
- The technology icon uses a command compass, sealed map folio, filter, hose, ampoule case, and radio as one integrated headquarters emblem. A blank green seal was used after rejecting a first generation with an unintended biohazard glyph.
- No baked text, modern hazmat suits, photographs, real company marks, swastikas, camp/genocide imagery, zombies, or biological-bomb imagery were used.

## Review and rejection record

- The initial Protective Logistics large frame contained unintended skull markings on supply crates. It was rejected and regenerated with blank equipment panels.
- The first Medical Countermeasure large frame contained a baked checkerboard-looking background rather than a clean chroma-key source. It was rejected and regenerated.
- The first Theater CBRN Headquarters technology generation contained an unnecessary biohazard glyph. It was rejected and regenerated with a blank wax seal.
- Final contact sheets were visually inspected over a checkerboard. All final subjects are centered, readable at their target scale, and surrounded by transparent unused pixels. The active and muted frames are visually distinct and their source/master compositions are separate.

## QA notes

- All six large DDS sheets are `152x42` with `2` horizontal `76x42` frames.
- All six small DDS sheets are `60x12` with `2` horizontal `30x12` frames.
- All seven ability DDS files are `34x33` and one-frame.
- The technology DDS is `64x64` and one-frame.
- Every processed PNG and DDS has transparent corner pixels; no fake checkerboard was retained in final art.
- DDS byte sizes match the uncompressed contract: `25664` large, `3008` small, `4616` ability, and `16512` technology.
- No animation timing or GIF preview is included because these are active/muted counter state sheets, not looping animated sprites. The frame count and left-to-right state order are documented in the manifest and GFX handoff.

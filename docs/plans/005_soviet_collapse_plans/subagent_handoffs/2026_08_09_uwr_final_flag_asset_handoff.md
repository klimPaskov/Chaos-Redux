# Event 005 UWR final flag asset handoff

Status: complete for the bounded asset-production task.

## Scope and source classification

This handoff covers the fictional `UWR` country flag family for Event 005, including the base flag and the `communism`, `democratic`, `fascism`, and `neutrality` variants at normal, medium, and small HOI4 sizes. UWR is the fictional Unconventional Warfare Republic, a high-chaos Soviet successor centered on the Tver pathogen directorate, laboratory security, and chemical/biological warfare command. The family uses generated fictional flat flag designs and does not depict a real person, historical flag, historical emblem, or documentary scene.

## Files changed

Runtime files replaced:

- `gfx/flags/UWR.tga`
- `gfx/flags/UWR_communism.tga`
- `gfx/flags/UWR_democratic.tga`
- `gfx/flags/UWR_fascism.tga`
- `gfx/flags/UWR_neutrality.tga`
- `gfx/flags/medium/UWR.tga`
- `gfx/flags/medium/UWR_communism.tga`
- `gfx/flags/medium/UWR_democratic.tga`
- `gfx/flags/medium/UWR_fascism.tga`
- `gfx/flags/medium/UWR_neutrality.tga`
- `gfx/flags/small/UWR.tga`
- `gfx/flags/small/UWR_communism.tga`
- `gfx/flags/small/UWR_democratic.tga`
- `gfx/flags/small/UWR_fascism.tga`
- `gfx/flags/small/UWR_neutrality.tga`

Evidence and handoff files:

- `docs/assets/005_soviet_collapse/uwr_final_flags/source_png/UWR_master.png`
- `docs/assets/005_soviet_collapse/uwr_final_flags/source_png/UWR_communism_master.png`
- `docs/assets/005_soviet_collapse/uwr_final_flags/source_png/UWR_democratic_master.png`
- `docs/assets/005_soviet_collapse/uwr_final_flags/source_png/UWR_fascism_master.png`
- `docs/assets/005_soviet_collapse/uwr_final_flags/source_png/UWR_neutrality_master.png`
- `docs/assets/005_soviet_collapse/uwr_final_flags/processed_png/`
- `docs/assets/005_soviet_collapse/uwr_final_flags/dds_preview/`
- `docs/assets/005_soviet_collapse/uwr_final_flags/contact_sheets/current_reference_flags.png`
- `docs/assets/005_soviet_collapse/uwr_final_flags/contact_sheets/final_flag_family_contact_sheet.png`
- `docs/assets/005_soviet_collapse/uwr_final_flags/prompts/uwr_flag_generation_prompts.md`
- `docs/assets/005_soviet_collapse/uwr_final_flags/manifest.md`
- `docs/assets/005_soviet_collapse/uwr_final_flags/gfx_handoff.md`

No `.gfx`, gameplay, event, localisation, GUI, country, idea, focus, decision, or non-UWR flag file was edited.

## Before and after

The prior `UWR` base, democratic, and neutrality ladders were byte-identical to `DSC` at corresponding sizes, and the prior ideology variants shared DSC-derived institutional imagery. The replacement is a new five-design family built from separate ImageGen source masters. The common identity is sealed containment hardware and a tri-lobed pathogen/leaf glyph, while the field and emblem construction differ by ideology for readability and route distinction.

## Runtime identifiers and parent wiring

HOI4 resolves these files by tag and ideology filename directly from `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. No `.gfx` sprite definition is needed, and no new sprite name should be invented. Use the filenames listed in `docs/assets/005_soviet_collapse/uwr_final_flags/gfx_handoff.md`.

## Validation evidence

- Every runtime TGA is 82x52, 41x26, or 10x7 as appropriate.
- Every runtime TGA is uncompressed truecolor image type 2, 32-bit, bottom-origin descriptor `0x00`, and exactly `18 + width * height * 4` bytes.
- Every runtime TGA has alpha min/max `255/255` and decodes pixel-identically to its processed PNG preview.
- Every processed preview was produced by mechanical resizing of a retained ImageGen master; no local emblem redraw, palette swap, copied DSC image, or fallback was used.
- Every DDS QA artifact was produced by `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` and passed the standard 32-bit BGRA header, dimension, exact length, mask, texture-cap, and alpha checks.
- Every final UWR TGA is non-identical to DSC and KMB at the corresponding size, with visual comparison retained in `contact_sheets/final_flag_family_contact_sheet.png` and `contact_sheets/current_reference_flags.png`.
- The final TGA SHA-256 values are recorded in `docs/assets/005_soviet_collapse/uwr_final_flags/manifest.md`.

## Skipped validation and remaining risk

The Unix `file` utility was unavailable in the Windows shell, so its textual Targa report was not run; direct binary-header validation and Pillow round-trip decoding verified the same image type, dimensions, bit depth, byte length, and bottom-origin invariant. Live in-game presentation and parent-side final diff review were not run by this asset worker because the asset boundary forbids launching HOI4 and the parent retains final runtime validation ownership.

## Follow-up for parent

Review the final contact sheet and preserve the exact UWR filenames when checking the Event 005 country package. No gameplay or `.gfx` wiring change is required for this asset handoff.

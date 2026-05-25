# Event 005 Generated Asset Sidecar Handoff

## Final Asset Paths

This handoff changes only flag image assets and asset documentation. No `.gfx` edits are needed for flags.

Final PRA flag outputs:

- `gfx/flags/PRA.tga`
- `gfx/flags/PRA_communism.tga`
- `gfx/flags/PRA_democratic.tga`
- `gfx/flags/PRA_fascism.tga`
- `gfx/flags/PRA_neutrality.tga`
- `gfx/flags/medium/PRA.tga`
- `gfx/flags/medium/PRA_communism.tga`
- `gfx/flags/medium/PRA_democratic.tga`
- `gfx/flags/medium/PRA_fascism.tga`
- `gfx/flags/medium/PRA_neutrality.tga`
- `gfx/flags/small/PRA.tga`
- `gfx/flags/small/PRA_communism.tga`
- `gfx/flags/small/PRA_democratic.tga`
- `gfx/flags/small/PRA_fascism.tga`
- `gfx/flags/small/PRA_neutrality.tga`

Final MFR ideology flag outputs:

- `gfx/flags/MFR_communism.tga`
- `gfx/flags/MFR_democratic.tga`
- `gfx/flags/MFR_fascism.tga`
- `gfx/flags/MFR_neutrality.tga`
- `gfx/flags/medium/MFR_communism.tga`
- `gfx/flags/medium/MFR_democratic.tga`
- `gfx/flags/medium/MFR_fascism.tga`
- `gfx/flags/medium/MFR_neutrality.tga`
- `gfx/flags/small/MFR_communism.tga`
- `gfx/flags/small/MFR_democratic.tga`
- `gfx/flags/small/MFR_fascism.tga`
- `gfx/flags/small/MFR_neutrality.tga`

Source-sidecar repair outputs:

- `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/UKR_BLACK_BANNER_communism_source.png`
- `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/UKR_BLACK_BANNER_democratic_source.png`
- `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/UKR_BLACK_BANNER_fascism_source.png`
- `docs/assets/005_soviet_union_collapse/source_png/generated_custom_ideology_flags/UKR_BLACK_BANNER_neutrality_source.png`

## Proposed Sprite Names

None. HOI4 country flags are resolved by filename convention, not `.gfx` sprite names.

## Suggested `.gfx` File

None. Do not edit `.gfx` for this flag handoff.

## Use Notes

- `PRA` now has a generated base plus four generated ideology variants with distinct railway-authority motifs.
- `MFR` keeps its existing no-suffix base flag; only ideology variants were polished.
- `UKR_BLACK_BANNER` active flags are unchanged. The four new source PNGs only repair source-sidecar coverage from the existing generated strip.
- Existing-country base flags remain untouched. This pass creates no default overrides for vanilla-supported country tags.
- Contact sheets are in `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/contact_sheets/`.
- TGA validation notes are in `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25/notes/`.

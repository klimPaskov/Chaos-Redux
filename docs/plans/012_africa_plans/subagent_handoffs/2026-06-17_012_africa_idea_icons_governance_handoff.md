# 2026-06-17 012 Africa Governance Idea Icons Handoff

## Scope completed

Completed the bounded governance idea-icon regeneration batch only.

Final DDS outputs:

- `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds`
- `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds`
- `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds`
- `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds`

Evidence package:

- `docs/assets/012_africa/icon_regen_ideas_batch_governance/source_png/`
- `docs/assets/012_africa/icon_regen_ideas_batch_governance/processed_png/`
- `docs/assets/012_africa/icon_regen_ideas_batch_governance/contact_sheets/`
- `docs/assets/012_africa/icon_regen_ideas_batch_governance/manifest.md`
- `docs/assets/012_africa/icon_regen_ideas_batch_governance/gfx_handoff.md`

## Visual result summary

- `idea_africa_paper_core_mandate`: torn parchment with wax seal, pencil, and stamped core motif
- `idea_africa_charter_league`: linked-ring charter seal with scroll and clasped-hands motif
- `idea_africa_authority_atlas`: folded map with compass and map pin
- `idea_africa_regional_authority`: three-node authority network around a small central seat glyph

All four were generated as separate idea-icon source art, not resized or adapted from focus/goal icons.

## Validation

- Each final DDS exists at the requested path and is exactly `64x64`.
- All four DDS files have alpha transparency with fully transparent corners at `(0,0)`, `(63,0)`, `(0,63)`, and `(63,63)`.
- Border validation found `0` non-transparent pixels on the outermost edge for all four outputs.
- Checker preview confirms transparent unused canvas with no opaque square background.
- Visual comparison sheet confirms the new idea icons are distinct from the nearby 012 Africa goal icons:
  - `authority_atlas` uses folded map plus compass instead of the open-book atlas goal icon.
  - `charter_league` uses a linked-ring seal composition instead of the bronze charter medallion / diplomacy crest goal icons.
  - `paper_core_mandate` and `regional_authority` no longer use the previous round bronze medallion style.
- Opaque near-white matte pixels at final size:
  - `idea_africa_paper_core_mandate.dds`: `3`
  - `idea_africa_charter_league.dds`: `0`
  - `idea_africa_authority_atlas.dds`: `4`
  - `idea_africa_regional_authority.dds`: `0`

The remaining near-white opaque pixels are isolated highlight specks inside the painted subjects, not a white square, matte, or halo.

## Files intentionally not edited

- No `.gfx` files
- No idea script files
- No localisation
- No goal icons
- No gameplay or UI scripts

## Process notes

- Source mode: `imagegen`
- Transparency workflow: chroma-key generation on flat green background, then local alpha extraction with `remove_chroma_key.py`
- DDS conversion: local conversion from the processed `64x64` PNG outputs

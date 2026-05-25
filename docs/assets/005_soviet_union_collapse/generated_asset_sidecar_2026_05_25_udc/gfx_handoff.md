# Event 005 UDC Generated Ideology Flag Handoff

This package provides review handoff assets only. It does not change active `gfx/flags` files because the active `UDC` flag family is already present and dirty in the worktree.

## Proposed Active Paths

If the parent accepts these generated variants, copy the TGA outputs to:

| Asset | Normal | Medium | Small |
| --- | --- | --- | --- |
| `UDC_communism` | `gfx/flags/UDC_communism.tga` | `gfx/flags/medium/UDC_communism.tga` | `gfx/flags/small/UDC_communism.tga` |
| `UDC_democratic` | `gfx/flags/UDC_democratic.tga` | `gfx/flags/medium/UDC_democratic.tga` | `gfx/flags/small/UDC_democratic.tga` |
| `UDC_fascism` | `gfx/flags/UDC_fascism.tga` | `gfx/flags/medium/UDC_fascism.tga` | `gfx/flags/small/UDC_fascism.tga` |
| `UDC_neutrality` | `gfx/flags/UDC_neutrality.tga` | `gfx/flags/medium/UDC_neutrality.tga` | `gfx/flags/small/UDC_neutrality.tga` |

## Review Files

- Source PNGs: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_udc/source_png/`
- Processed PNG previews: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_udc/processed_png/`
- Review TGA outputs: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_udc/tga/`
- Review DDS outputs: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_udc/dds/`
- Contact sheets: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_udc/contact_sheets/`
- Validation notes: `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_udc/notes/identify_outputs.txt`

## Sprite Names And `.gfx`

None. HOI4 country flags are resolved by filename convention. No `.gfx` edits are needed for these flags.

## Orientation And Uniqueness

The generated flags were checked in large, normal, and small contact sheets. They are upright, not mirrored, and maintain a readable orientation cue at 82x52 and 41x26. The 10x7 versions remain distinguishable by palette and broad emblem mass.

The four normal-size PNGs and four normal-size TGAs have distinct hashes. They are not recolors, flipped copies, or simple single-shape edits of one another.

## Parent Wiring Needed

- Do not replace `gfx/flags/UDC.tga`; no new base flag was created.
- If accepted, copy only the four ideology TGA families from this sidecar into the active `gfx/flags` folders.
- Keep `ALN`, `KHW`, and `KZR` blocked for source research or explicit fictional-generation approval.


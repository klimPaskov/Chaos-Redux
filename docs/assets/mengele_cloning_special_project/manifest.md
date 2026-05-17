# Mengele Cloning Special Project Asset Manifest

## Package

This package supports the `sp_mengele_cloning` biowarfare special project documented in `docs/systems/mengele_cloning_special_project.md`.

Source and processed PNG previews live under:

- `docs/assets/mengele_cloning_special_project/source_png/`
- `docs/assets/mengele_cloning_special_project/processed_png/`

## Final Assets

| Asset | Type | Final path | Sprite | Size |
| --- | --- | --- | --- | --- |
| Cloning | special project icon | `gfx/interface/special_project/project_icons/sp_mengele_cloning.dds` | `GFX_sp_mengele_cloning` | 161x98 |

## Wiring

- `interface/special_projects/biowarfare.gfx` registers `GFX_sp_mengele_cloning`.
- `common/special_projects/projects/mengele_cloning_projects.txt` uses the sprite as the project icon.
- `common/dynamic_modifiers/chaosx_dynamic_modifiers.txt` uses the same sprite for the facility manpower dynamic modifier.

## Source Notes

- Source mode: `image_gen`
- Source PNG: `docs/assets/mengele_cloning_special_project/source_png/sp_mengele_cloning_source.png`
- Processed PNG: `docs/assets/mengele_cloning_special_project/processed_png/sp_mengele_cloning.png`
- Final DDS format: uncompressed 32-bit ARGB8888 DDS

Generation prompt summary: HOI4-style special project icon showing a dark biomedical laboratory, a red-lit cloning cylinder with a metallic DNA helix, steel pipes, and military science mood with no text, real logos, flags, gore, or explicit violence.

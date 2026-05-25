# Event 005 UKR Black Banner Ideology Variant Handoff

This is a docs-only sidecar package. It does not wire or replace active flags.

## Final Sidecar Outputs

Normal `82x52`, medium `41x26`, and small `10x7` outputs are available under:

- `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_ukr_black_banner_ideology_variants/processed_png/`
- `docs/assets/005_soviet_union_collapse/generated_asset_sidecar_2026_05_25_ukr_black_banner_ideology_variants/tga/`

## Proposed Active Paths

Use these only if the parent explicitly approves replacing the current dirty active route ideology flags:

| Variant | Normal | Medium | Small |
| --- | --- | --- | --- |
| `communism` | `gfx/flags/UKR_BLACK_BANNER_communism.tga` | `gfx/flags/medium/UKR_BLACK_BANNER_communism.tga` | `gfx/flags/small/UKR_BLACK_BANNER_communism.tga` |
| `democratic` | `gfx/flags/UKR_BLACK_BANNER_democratic.tga` | `gfx/flags/medium/UKR_BLACK_BANNER_democratic.tga` | `gfx/flags/small/UKR_BLACK_BANNER_democratic.tga` |
| `fascism` | `gfx/flags/UKR_BLACK_BANNER_fascism.tga` | `gfx/flags/medium/UKR_BLACK_BANNER_fascism.tga` | `gfx/flags/small/UKR_BLACK_BANNER_fascism.tga` |
| `neutrality` | `gfx/flags/UKR_BLACK_BANNER_neutrality.tga` | `gfx/flags/medium/UKR_BLACK_BANNER_neutrality.tga` | `gfx/flags/small/UKR_BLACK_BANNER_neutrality.tga` |

## Sprite And `.gfx` Notes

HOI4 country and cosmetic flags do not need `.gfx` sprite entries. No `.gfx` edits are proposed.

## Use Notes

- `UKR_BLACK_BANNER` is a route/cosmetic flag target, not a vanilla `UKR` default flag override.
- The current active route flag files already exist and are dirty in the worktree. Do not copy these sidecar TGAs over active files without parent approval.
- No DDS files were produced because this is a flag package; the HOI4 flag workflow uses normal/medium/small TGA outputs.

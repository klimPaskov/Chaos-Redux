# IW-006 AFX sprite handoff

## Main-agent action

Retain and review the exact registrations in `interface/006_independence_wave_wallonia_frisia_assets.gfx`, then include them in final AFX admission validation. At asset-package close, that file already contained all nineteen required definitions (eight base focus sprites, eight `_shine` focus sprites, and three report sprites) with the runtime paths below. This asset pass did not edit the interface file.

No sprite name, texture path, size, or consumer is uncertain.

## Focus sprites

| Runtime DDS | Base sprite | Shine sprite | Focus consumer |
| --- | --- | --- | --- |
| `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_sambre_meuse_authority.dds` | `GFX_goal_independence_wave_afx_sambre_meuse_authority` | `GFX_goal_independence_wave_afx_sambre_meuse_authority_shine` | `independence_wave_afx_charter_sambre_meuse_authority_focus` |
| `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_mines_rails_furnaces.dds` | `GFX_goal_independence_wave_afx_mines_rails_furnaces` | `GFX_goal_independence_wave_afx_mines_rails_furnaces_shine` | `independence_wave_afx_bind_mines_rails_furnaces_focus` |
| `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_basin_government.dds` | `GFX_goal_independence_wave_afx_basin_government` | `GFX_goal_independence_wave_afx_basin_government_shine` | `independence_wave_afx_codify_basin_government_focus` |
| `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_industrial_reserve.dds` | `GFX_goal_independence_wave_afx_industrial_reserve` | `GFX_goal_independence_wave_afx_industrial_reserve_shine` | `independence_wave_afx_integrate_industrial_reserve_focus` |
| `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_industrial_succession.dds` | `GFX_goal_independence_wave_afx_industrial_succession` | `GFX_goal_independence_wave_afx_industrial_succession_shine` | `independence_wave_afx_settle_industrial_succession_focus` |
| `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_meuse_network_office.dds` | `GFX_goal_independence_wave_afx_meuse_network_office` | `GFX_goal_independence_wave_afx_meuse_network_office_shine` | `independence_wave_afx_open_meuse_network_office_focus` |
| `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_meuse_conference.dds` | `GFX_goal_independence_wave_afx_meuse_conference` | `GFX_goal_independence_wave_afx_meuse_conference_shine` | `independence_wave_afx_mandate_meuse_conference_focus` |
| `gfx/interface/goals/006_independence_wave/afx/goal_independence_wave_afx_low_countries_delegation.dds` | `GFX_goal_independence_wave_afx_low_countries_delegation` | `GFX_goal_independence_wave_afx_low_countries_delegation_shine` | `independence_wave_afx_prepare_low_countries_dossier_focus` |

The base definition form is:

```text
spriteType = { name = "GFX_<exact_stem>" texturefile = "gfx/interface/goals/006_independence_wave/afx/<exact_stem>.dds" }
```

The shine definition uses the same texture and the repository's established effect:

```text
spriteType = { name = "GFX_<exact_stem>_shine" texturefile = "gfx/interface/goals/006_independence_wave/afx/<exact_stem>.dds" effectFile = "gfx/FX/buttonstate.lua" }
```

## Report sprites

| Runtime DDS | Sprite | Event consumer |
| --- | --- | --- |
| `gfx/event_pictures/006_independence_wave/afx/report_event_006_afx_industrial_authority.dds` | `GFX_report_event_006_afx_industrial_authority` | `chaosx.nr6.18` |
| `gfx/event_pictures/006_independence_wave/afx/report_event_006_afx_basin_government.dds` | `GFX_report_event_006_afx_basin_government` | `chaosx.nr6.19` |
| `gfx/event_pictures/006_independence_wave/afx/report_event_006_afx_meuse_ambition.dds` | `GFX_report_event_006_afx_meuse_ambition` | `chaosx.nr6.20` |

The report definition form is:

```text
spriteType = { name = "GFX_<exact_stem>" texturefile = "gfx/event_pictures/006_independence_wave/afx/<exact_stem>.dds" }
```

## Validation handoff

- Machine report: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/validation/asset_validation.json`
- Full package/runtime hash inventory: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/validation/sha256_inventory.txt`
- Focus review: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/contact_sheets/focus_icons_contact_sheet.png`
- Report review: `docs/assets/006_independence_wave/afx_unique_assets_2026_07_16/contact_sheets/report_scenes_contact_sheet.png`

All eleven DDS files are exact decoded matches to their processed PNGs. Focus textures are `94x86` with transparent corners and shaped alpha silhouettes. Report textures are `210x176` with the canonical tilted-card alpha treatment. No localisation or interface edits are required from the asset producer; final registration and consumer admission remain the main agent's responsibility.

## Blockers

None.

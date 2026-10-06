# Shared ChaosX GFX cleanup handoff

The parent can retain the existing sprite registrations and install the approved DDS files at the paths already referenced in `interface/chaosx_gfx_cleanup.gfx`.

| Sprite | Existing texture path | Canvas | Use note |
|---|---|---:|---|
| `GFX_div_templ_47_small` | `gfx/interface/counters/division_templates_small/custom_template_047.dds` | 30x12 | Light-neutral biohazard trefoil; centered and full-height on transparency. |
| `GFX_div_templ_46_large` | `gfx/interface/counters/division_templates_large/custom_template_046.dds` | 76x42 | Brightened flask emblem; centered at 36px tall. |
| `GFX_div_templ_47_large` | `gfx/interface/counters/division_templates_large/custom_template_047.dds` | 76x42 | Brightened biohazard trefoil; centered at 36px tall. |

The exact vanilla sizing and style precedent is `GFX_div_templ_0_large` and `GFX_div_templ_0_small` in the installed game's `interface/subuniticons.gfx`. No new GFX definitions or runtime path changes are proposed.

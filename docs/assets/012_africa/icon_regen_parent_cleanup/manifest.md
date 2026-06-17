# Event 012 Africa Parent Icon Cleanup Manifest

Date: 2026-06-17

This parent pass repaired the remaining white-background issues found after the icon subagent batches landed. The final sprite names and DDS filenames stayed unchanged, so no `.gfx`, focus, idea, localisation, or script wiring changed.

## Cleaned Goal Icons

| Asset | Asset type | Source mode | Processed PNG | Final DDS | Sprite |
| --- | --- | --- | --- | --- | --- |
| Political Congress | focus/goal icon | `imagegen`, parent chroma-key cleanup | `docs/assets/012_africa/icon_regen_parent_cleanup/processed_png/goal_africa_political_congress.png` | `gfx/interface/goals/012_africa/goal_africa_political_congress.dds` | `GFX_goal_africa_political_congress` |
| High-Chaos Bestiary | focus/goal icon | subagent `imagegen`, parent white-matte cleanup | `docs/assets/012_africa/icon_regen_parent_cleanup/processed_png/goal_africa_high_chaos_bestiary.png` | `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds` | `GFX_goal_africa_high_chaos_bestiary` |
| Scramble for Africa | focus/goal icon | subagent `imagegen`, parent white-matte cleanup | `docs/assets/012_africa/icon_regen_parent_cleanup/processed_png/goal_africa_scramble_for_africa.png` | `gfx/interface/goals/012_africa/goal_africa_scramble_for_africa.dds` | `GFX_goal_africa_scramble_for_africa` |
| Sponsor Paths | focus/goal icon | subagent `imagegen`, parent white-matte cleanup | `docs/assets/012_africa/icon_regen_parent_cleanup/processed_png/goal_africa_sponsor_paths.png` | `gfx/interface/goals/012_africa/goal_africa_sponsor_paths.dds` | `GFX_goal_africa_sponsor_paths` |
| World Order Route | focus/goal icon | subagent `imagegen`, parent white-matte cleanup | `docs/assets/012_africa/icon_regen_parent_cleanup/processed_png/goal_africa_world_order_route.png` | `gfx/interface/goals/012_africa/goal_africa_world_order_route.dds` | `GFX_goal_africa_world_order_route` |

## Source and Review Files

- `docs/assets/012_africa/icon_regen_parent_cleanup/source_png/goal_africa_political_congress_parent_regen_source.png`
- `docs/assets/012_africa/icon_regen_parent_cleanup/contact_sheets/parent_goal_cleanup_checker.png`

## Validation

- All five repaired DDS files are `94x86`.
- All five repaired DDS files have transparent corners and no non-transparent outer-border pixels.
- Parent review removed the interior white backing from `goal_africa_high_chaos_bestiary`, `goal_africa_scramble_for_africa`, `goal_africa_sponsor_paths`, and `goal_africa_world_order_route`.
- `goal_africa_political_congress` was regenerated from a new congress-table source because the narrowed subagent source read as an ornate seal rather than a political congress.

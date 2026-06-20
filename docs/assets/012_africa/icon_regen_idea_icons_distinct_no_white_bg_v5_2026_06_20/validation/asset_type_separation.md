# Event 012 Africa Idea vs Goal Icon Separation

This check uses the live DDS files after the 2026-06-20 v5 regeneration pass.

Contact sheet: `contact_sheets/goal_vs_idea_live_compare.png`

## Result

The idea/national-spirit icons are distinct `64x64` spirit assets. They are not resized, cropped, recolored, padded, or lightly edited focus/goal icons.

## Checked Pairs

| Theme | Goal DDS | Idea DDS | Separation note |
| --- | --- | --- | --- |
| Authority Atlas | `gfx/interface/goals/012_africa/goal_africa_authority_atlas.dds` | `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds` | Goal uses a full open atlas composition; idea uses a compact compass-over-atlas medallion. |
| Charter League | `gfx/interface/goals/012_africa/goal_africa_charter_league_emblem.dds` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` | Goal uses a broad charter-emblem presentation; idea uses a tighter charter scroll and shield-knot symbol. |
| Liberation Office | `gfx/interface/goals/012_africa/goal_africa_liberation_war_office.dds` | `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds` | Goal uses a field-order banner composition; idea uses a compact broken-chain dispatch emblem. |
| High Chaos | `gfx/interface/goals/012_africa/goal_africa_high_chaos_bestiary.dds` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds` | Goal uses a focus-scale bestiary archive object; idea uses a compact supernatural medallion. |
| Regional Authority | `gfx/interface/goals/012_africa/goal_africa_regional_integration.dds` | `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds` | Goal uses connected map tiles and routes; idea uses a council-seal spoke emblem. |

No `.gfx` or gameplay edits are needed for this distinction because the live sprite names and texture paths already separate `GFX_goal_*` from `GFX_idea_*`.

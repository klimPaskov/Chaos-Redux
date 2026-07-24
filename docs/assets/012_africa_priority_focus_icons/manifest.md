# Event 012 Africa priority-member focus icon manifest

Status: complete for the eight requested static focus icons.

Asset type: national focus icon.

Source mode: `$imagegen` built-in generation on a flat `#00ff00` chroma-key background, followed by the official `remove_chroma_key.py` helper.

Canonical reference inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png` and its 16 native 100x88 reference PNGs.

Style target: HOI4 focus-tree emblem treatment with an aged painterly finish, strong dark silhouette, transparent unused canvas, no text, no white matte, no sticker rim, and no opaque square.

| Focus id | Sprite name | Source PNG | Processed evidence | Runtime DDS | Target | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `africa_priority_define_compact_country` | `GFX_goal_012_africa_priority_compact_country` | `source_png/goal_012_africa_priority_compact_country_source.png` | `processed_png/goal_012_africa_priority_compact_country.png` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_compact_country.dds` | 94x86 RGBA | complete |
| `africa_priority_ratify_political_settlement` | `GFX_goal_012_africa_priority_political_settlement` | `source_png/goal_012_africa_priority_political_settlement_source.png` | `processed_png/goal_012_africa_priority_political_settlement.png` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_political_settlement.dds` | 94x86 RGBA | complete |
| `africa_priority_build_distinct_institution` | `GFX_goal_012_africa_priority_distinct_institution` | `source_png/goal_012_africa_priority_distinct_institution_source.png` | `processed_png/goal_012_africa_priority_distinct_institution.png` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_distinct_institution.dds` | 94x86 RGBA | complete |
| `africa_priority_secure_economic_function` | `GFX_goal_012_africa_priority_economic_function` | `source_png/goal_012_africa_priority_economic_function_source.png` | `processed_png/goal_012_africa_priority_economic_function.png` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_economic_function.dds` | 94x86 RGBA | complete |
| `africa_priority_negotiate_league_role` | `GFX_goal_012_africa_priority_league_role` | `source_png/goal_012_africa_priority_league_role_source.png` | `processed_png/goal_012_africa_priority_league_role.png` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_league_role.dds` | 94x86 RGBA | complete |
| `africa_priority_resolve_overlap_question` | `GFX_goal_012_africa_priority_overlap_question` | `source_png/goal_012_africa_priority_overlap_question_source.png` | `processed_png/goal_012_africa_priority_overlap_question.png` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_overlap_question.dds` | 94x86 RGBA | complete |
| `africa_priority_field_national_force` | `GFX_goal_012_africa_priority_national_force` | `source_png/goal_012_africa_priority_national_force_source.png` | `processed_png/goal_012_africa_priority_national_force.png` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_national_force.dds` | 94x86 RGBA | complete |
| `africa_priority_write_post_settlement_programme` | `GFX_goal_012_africa_priority_post_settlement` | `source_png/goal_012_africa_priority_post_settlement_source.png` | `processed_png/goal_012_africa_priority_post_settlement.png` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_post_settlement.dds` | 94x86 RGBA | complete |

The raw alpha-removal evidence is retained beside each processed PNG as `processed_png/goal_012_africa_priority_*_alpha.png`.

The generation prompts and ImageGen output paths are recorded in `prompts/prompts.md`.

The review contact sheet is `contact_sheets/focus_icons_contact_sheet.png`.

Visual QA: all eight icons are individually generated, visually distinct, centered, readable at 94x86, and transparent at all four canvas corners in the review sheet.

DDS QA: every final file is a 32-bit uncompressed BGRA DDS with 94x86 dimensions, 128 + 94x86x4 byte length, BGRA masks, texture caps, alpha range 0-255, and transparent corners.

No blockers or approved fallbacks were used.

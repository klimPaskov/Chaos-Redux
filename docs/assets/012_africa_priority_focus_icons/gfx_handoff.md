# Event 012 Africa priority-member focus icon GFX handoff

The parent registration is already in `interface/012_africa_priority_member_assets.gfx`; no `.gfx` file was edited by this asset tranche.

Each base sprite and its registered `_shine` companion must keep the exact sprite name and texture path below.

| Sprite name | Texture path | Consumer focus id | Target |
| --- | --- | --- | --- |
| `GFX_goal_012_africa_priority_compact_country` and `GFX_goal_012_africa_priority_compact_country_shine` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_compact_country.dds` | `africa_priority_define_compact_country` | 94x86 |
| `GFX_goal_012_africa_priority_political_settlement` and `GFX_goal_012_africa_priority_political_settlement_shine` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_political_settlement.dds` | `africa_priority_ratify_political_settlement` | 94x86 |
| `GFX_goal_012_africa_priority_distinct_institution` and `GFX_goal_012_africa_priority_distinct_institution_shine` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_distinct_institution.dds` | `africa_priority_build_distinct_institution` | 94x86 |
| `GFX_goal_012_africa_priority_economic_function` and `GFX_goal_012_africa_priority_economic_function_shine` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_economic_function.dds` | `africa_priority_secure_economic_function` | 94x86 |
| `GFX_goal_012_africa_priority_league_role` and `GFX_goal_012_africa_priority_league_role_shine` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_league_role.dds` | `africa_priority_negotiate_league_role` | 94x86 |
| `GFX_goal_012_africa_priority_overlap_question` and `GFX_goal_012_africa_priority_overlap_question_shine` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_overlap_question.dds` | `africa_priority_resolve_overlap_question` | 94x86 |
| `GFX_goal_012_africa_priority_national_force` and `GFX_goal_012_africa_priority_national_force_shine` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_national_force.dds` | `africa_priority_field_national_force` | 94x86 |
| `GFX_goal_012_africa_priority_post_settlement` and `GFX_goal_012_africa_priority_post_settlement_shine` | `gfx/interface/goals/012_africa/priority_members/goal_012_africa_priority_post_settlement.dds` | `africa_priority_write_post_settlement_programme` | 94x86 |

The `_shine` sprites intentionally reuse their corresponding base DDS through the existing `gfx/FX/buttonstate.lua` registration.

Source and review evidence is retained in `docs/assets/012_africa_priority_focus_icons/manifest.md`, `prompts/prompts.md`, and `contact_sheets/focus_icons_contact_sheet.png`.

No runtime wiring changes are required from the asset worker.

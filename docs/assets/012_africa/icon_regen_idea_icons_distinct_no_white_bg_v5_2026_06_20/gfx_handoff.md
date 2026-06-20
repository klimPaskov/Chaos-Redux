# Event 012 Africa Idea Icon GFX Handoff

The live sprite definitions already exist in `interface/012_africa.gfx`, so no `.gfx` edit is required for this package. This pass replaced the DDS files at the existing texture paths.

| Sprite | Final DDS |
| --- | --- |
| `GFX_idea_africa_is_one` | `gfx/interface/ideas/012_africa/idea_africa_is_one.dds` |
| `GFX_idea_africa_paper_core_mandate` | `gfx/interface/ideas/012_africa/idea_africa_paper_core_mandate.dds` |
| `GFX_idea_africa_charter_league` | `gfx/interface/ideas/012_africa/idea_africa_charter_league.dds` |
| `GFX_idea_africa_authority_atlas` | `gfx/interface/ideas/012_africa/idea_africa_authority_atlas.dds` |
| `GFX_idea_africa_liberation_war_office` | `gfx/interface/ideas/012_africa/idea_africa_liberation_war_office.dds` |
| `GFX_idea_africa_high_chaos_bestiary` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_bestiary.dds` |
| `GFX_idea_africa_regional_authority` | `gfx/interface/ideas/012_africa/idea_africa_regional_authority.dds` |
| `GFX_idea_africa_high_chaos_actor` | `gfx/interface/ideas/012_africa/idea_africa_high_chaos_actor.dds` |
| `GFX_idea_africa_rsa_continental_emergency` | `gfx/interface/ideas/012_africa/idea_africa_rsa_continental_emergency.dds` |

Package copies are under `docs/assets/012_africa/icon_regen_idea_icons_distinct_no_white_bg_v5_2026_06_20/dds/`.

Validation:

- All live DDS files decode as `64x64` ARGB8888.
- All live DDS files have transparent corners.
- No live DDS has an opaque square background.
- No live DDS has near-white outer-edge pixels or bright near-white matte pixels adjacent to fully transparent pixels.

Contact sheets:

- `contact_sheets/idea_icons_checker_contact.png`
- `contact_sheets/idea_icons_dark_contact.png`
- `contact_sheets/live_dds_checker_contact.png`
- `contact_sheets/live_dds_dark_contact.png`
- `contact_sheets/goal_vs_idea_compare.png`

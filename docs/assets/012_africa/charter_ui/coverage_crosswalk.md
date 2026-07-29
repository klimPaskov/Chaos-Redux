# Event 012 Charter League UI coverage crosswalk

| Accepted requirement | Runtime consumer | Package evidence | Status |
| --- | --- | --- | --- |
| Charter window background | `GFX_012_africa_charter_window_background` | source, processed PNG, decoded DDS, final DDS | complete |
| Charter header plate | `GFX_012_africa_charter_header_plate` | source, processed PNG, decoded DDS, final DDS | complete |
| Member dossier frame | `GFX_012_africa_member_card_frame` | source, processed PNG, decoded DDS, final DDS | complete |
| Regional congress frame | `GFX_012_africa_regional_card_frame` | source, processed PNG, decoded DDS, final DDS | complete |
| Relationship badge strip | `GFX_012_africa_relationship_badges` | source, processed PNG, decoded DDS, final DDS | complete |
| Primary values strip | `GFX_012_africa_primary_value_icons` | source, processed PNG, decoded DDS, final DDS | complete |
| Secondary values strip | `GFX_012_africa_secondary_value_icons` | source, processed PNG, decoded DDS, final DDS | complete |
| Clause selector tabs | `GFX_012_africa_clause_tabs` | source, processed PNG, decoded DDS, final DDS | complete |
| Regional overlay buttons | `GFX_012_africa_regional_overlay_buttons` | source, processed PNG, decoded DDS, final DDS | complete |
| Project progress frame | `GFX_012_africa_project_progress_frame` | source, processed PNG, decoded DDS, final DDS | complete |
| Rival bloc panel | `GFX_012_africa_rival_bloc_panel` | source, processed PNG, decoded DDS, final DDS | complete |
| Diaspora summary panel | `GFX_012_africa_diaspora_summary_panel` | source, processed PNG, decoded DDS, final DDS | complete |
| Charter seal activation animation | `GFX_012_africa_charter_seal_activation_animated` plus static fallback | 8 sources, 8 processed frames, 512x64 sheet, GIF/contact review, DDS pair | complete |
| Charter authority ring animation | `GFX_012_africa_charter_authority_ring_animated` plus static fallback | 10 sources, 10 processed frames, 640x64 sheet, GIF/contact review, DDS pair | complete |

No accepted row points to `docs/assets/` at runtime. The parent implementation owns the reserved `.gfx` references and GUI state wiring.

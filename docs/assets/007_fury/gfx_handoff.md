# Event 007 Fury GFX Handoff

`interface/007_fury.gfx` registers the final Fury idea, decision, decision-category, and key focus branch sprites. The super-event sprites are registered in `interface/chaosx_super_events.gfx` so slots `59` and `60` use the final filenames.

Report, news, and super-event images should present Fury as a rogue-country rage outbreak. Avoid map rooms, command desks, ledgers, route strings, globes, and war-office planning imagery for future replacements.

UI icon sources, processed PNGs, and the contact sheet are recorded in `docs/assets/007_fury/ui_icons/manifest.md`.

The Fury country-leader flame overlay is registered in `interface/007_fury.gfx`:

- `GFX_fury_leader_flame_overlay_animated` -> `gfx/interface/leader_frames/fury/fury_leader_flame_overlay_sheet.dds`
- `GFX_fury_leader_flame_overlay_static` -> `gfx/interface/leader_frames/fury/fury_leader_flame_overlay_static.dds`

The scripted GUI container is in `interface/007_fury_leader_overlay.gui`, with visibility and parent-window binding in `common/scripted_guis/007_fury_scripted_guis.txt`. The diplomacy overlay uses `selected_country_context` and `parent_window_name = countrydiplomacyview`, so it appears only when the selected diplomacy country is a Fury actor. The overlay position uses the summed vanilla coordinates for `country_info` -> `diplomacy_tab_top` -> `leader_portrait`.

The final major-Fury super-event image is wired at `gfx/super_events/fury_becomes_a_state.dds`. Its generated source and processed PNG live under `docs/assets/007_fury/super_events/fury_becomes_a_state/`. Slot `59` already returns `GFX_super_event_fury_becomes_a_state`.

The final world-end super-event image is wired at `gfx/super_events/super_event_world_in_fury.dds`. Its generated source and processed PNG live under `docs/assets/007_fury/super_events/world_in_fury/`. Slot `60` already returns `GFX_super_event_world_in_fury`.

Achievement sprite aliases already exist in `interface/chaosx_achievements.gfx`. Final Fury-specific DDS triplets are in place:

- `gfx/achievements/achievement_fury_fuse_cut.dds`
- `gfx/achievements/achievement_fury_no_minor_major.dds`
- `gfx/achievements/achievement_fury_firebreak.dds`
- `gfx/achievements/achievement_fury_pact_breaker.dds`
- `gfx/achievements/achievement_fury_ten_fires.dds`
- `gfx/achievements/achievement_fury_last_neighbor.dds`
- `gfx/achievements/achievement_fury_world_without_fury.dds`
- `gfx/achievements/achievement_fury_rivals_burn.dds`
- `gfx/achievements/achievement_fury_major_without_faction.dds`
- `gfx/achievements/achievement_fury_no_cores.dds`

Each achievement has matching `_grey.dds` and `_not_eligible.dds` variants.

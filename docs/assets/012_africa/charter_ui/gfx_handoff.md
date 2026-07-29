# Event 012 Charter League UI gfx handoff

The parent implementation must keep the existing sprite IDs and copy no files into alternate folders. The ready-to-wire texture paths are:

```text
GFX_012_africa_charter_window_background       gfx/interface/012_africa/charter_window_background.dds       1000x680
GFX_012_africa_charter_header_plate            gfx/interface/012_africa/charter_header_plate.dds            976x84
GFX_012_africa_member_card_frame               gfx/interface/012_africa/member_card_frame.dds               300x546
GFX_012_africa_regional_card_frame             gfx/interface/012_africa/regional_card_frame.dds             316x546
GFX_012_africa_relationship_badges             gfx/interface/012_africa/relationship_badges.dds             256x64
GFX_012_africa_primary_value_icons             gfx/interface/012_africa/primary_value_icons.dds             128x36
GFX_012_africa_secondary_value_icons           gfx/interface/012_africa/secondary_value_icons.dds           128x36
GFX_012_africa_clause_tabs                     gfx/interface/012_africa/clause_tabs.dds                     70x24
GFX_012_africa_regional_overlay_buttons       gfx/interface/012_africa/regional_overlay_buttons.dds       92x28
GFX_012_africa_project_progress_frame         gfx/interface/012_africa/project_progress_frame.dds         330x240
GFX_012_africa_rival_bloc_panel                gfx/interface/012_africa/rival_bloc_panel.dds                330x94
GFX_012_africa_diaspora_summary_panel         gfx/interface/012_africa/diaspora_summary_panel.dds         330x202
GFX_012_africa_charter_seal_activation_static gfx/interface/012_africa/animations/charter_seal_activation_static.dds 64x64
GFX_012_africa_charter_seal_activation_animated gfx/interface/012_africa/animations/charter_seal_activation_sheet.dds 512x64, 8 frames, 8 fps, looping, play_on_show
GFX_012_africa_charter_authority_ring_static gfx/interface/012_africa/animations/charter_authority_ring_static.dds 64x64
GFX_012_africa_charter_authority_ring_animated gfx/interface/012_africa/animations/charter_authority_ring_sheet.dds 640x64, 10 frames, 6 fps, looping, play_on_show
```

The existing `interface/012_africa_charter.gfx` already contains the exact sprite registrations. Do not add a second registration or rename the IDs. The existing `interface/012_africa_charter.gui` places the ring at `{ x = 792 y = 12 }` and the seal at `{ x = 886 y = 12 }` in the 1000x680 window. Both animated sprites are decorative and have static fallbacks at the same origin. Their transparent corners must remain unobstructive.

## Handoff evidence

- Static source and processed PNGs: `source_png/` and `processed_png/`.
- Animation source and processed frames: `animations/<asset>/source_frames/` and `animations/<asset>/processed_frames/`.
- Sheet PNGs, GIF previews, and contact sheets: each animation's `sheets/` and `previews/`.
- DDS decode review: `decoded_dds_png/`.
- Manifest, coverage, provenance, and validation: sibling markdown files in this directory.

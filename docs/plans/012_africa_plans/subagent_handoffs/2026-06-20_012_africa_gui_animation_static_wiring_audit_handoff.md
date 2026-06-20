# Event 012 Africa GUI/Animation Static Wiring Audit

Date: 2026-06-20

Scope:

- `common/scripted_guis/012_africa_scripted_gui.txt`
- `interface/012_africa_scripted_gui.gui`
- `interface/012_africa.gfx`
- `gfx/interface/animated/012_africa/`
- `localisation/english/012_african_union_l_english.yml`

Findings:

- The Continental Congress decision-category panel is registered through `africa_continental_congress_category = { scripted_gui = africa_continental_congress_scripted_gui }`.
- The scripted GUI `window_name` matches `africa_continental_congress_container` in `interface/012_africa_scripted_gui.gui`.
- Six visual-strip elements are present: Charter banner static/animated, Authority Atlas seal static/animated, and Bestiary warning static/animated.
- All six visual-strip elements now have matching `_visible` triggers in `common/scripted_guis/012_africa_scripted_gui.txt`.
- The Charter banner static fallback previously lacked a visibility hook and would be visible before the Charter surface was active. The audit patched `africa_continental_congress_charter_banner_static_visible` to match the Charter banner animated gate.
- All six Africa visual-strip sprites resolve in `interface/012_africa.gfx`.
- All six final DDS assets exist and are alpha-capable:
  - `authority_atlas_seal_loop_fallback_128x128.dds` at 128x128
  - `authority_atlas_seal_loop_sheet.dds` at 512x128 for four 128x128 frames
  - `bestiary_warning_loop_fallback_96x96.dds` at 96x96
  - `bestiary_warning_loop_sheet.dds` at 384x96 for four 96x96 frames
  - `charter_league_banner_pulse_fallback_160x96.dds` at 160x96
  - `charter_league_banner_pulse_sheet.dds` at 640x96 for four 160x96 frames
- All 26 unique GUI text and tooltip localisation references in the panel resolve in `012_african_union_l_english.yml`.

Validation:

- Scripted GUI brace delta is zero after the patch.
- `git diff --check` passed for `common/scripted_guis/012_africa_scripted_gui.txt`.
- A local cross-reference check found no missing visual hooks or Africa sprite registrations.
- ImageMagick `identify` confirmed the expected DDS dimensions and sRGBA channels for all static fallback and frame-sheet textures.

Remaining risk:

- This is a static wiring audit only. It does not replace live in-game render proof for the Continental Congress panel, animated frame playback, z-order, or hover readability inside the actual HOI4 decision UI.

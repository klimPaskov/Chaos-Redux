# Event 012 Africa Focus Filter Validation

Validation date: 2026-06-21

Scope:

- `common/national_focus/012_africa_focus.txt`
- `interface/012_africa.gfx`
- `localisation/english/chaosx_gui_l_english.yml`
- `docs/assets/012_africa/focus_filter_icons/processed_png/`
- `gfx/interface/focusview/filter/012_africa/`

Checks run:

- `identify` confirmed each active processed PNG and live DDS is `27x27`.
- Alpha inspection confirmed all active processed PNG corner pixels are fully transparent.
- Matte inspection found zero opaque white pixels and zero opaque gray-background pixels in the checked background range for active processed PNGs.
- Filter reference scan found 12 active `FOCUS_FILTER_AFR_*` IDs in `common/national_focus/012_africa_focus.txt`.
- Each active filter has a matching `GFX_FOCUS_FILTER_*` sprite definition in `interface/012_africa.gfx`.
- Each active filter has a matching localisation key in `localisation/english/chaosx_gui_l_english.yml`.
- The current Event 012 tree no longer assigns `FOCUS_FILTER_AFR_CHARTER`, `FOCUS_FILTER_AFR_SCRAMBLE`, or `FOCUS_FILTER_AFR_BESTIARY`.

Notes:

- The icon subagent produced the binary and PNG files but did not return a final handoff before shutdown. The parent agent reviewed sizes, transparency, focus references, localisation, and sprite wiring directly.
- The old compatibility filters remain registered and present on disk so existing non-tree references do not lose their texture definitions.

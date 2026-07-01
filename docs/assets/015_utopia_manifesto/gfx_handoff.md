# Event 015 Utopian Manifesto GFX handoff

## Event pictures

- Final DDS path: `gfx/event_pictures/015_utopia_manifesto/report_event_utopia_manifesto_found.dds`
- Proposed sprite name: `GFX_report_event_utopia_manifesto_found`
- Suggested `.gfx` file: `interface/chaosx_pictures.gfx`
- Related use: Event 015 acceptance-side report image

- Final DDS path: `gfx/event_pictures/015_utopia_manifesto/news_event_utopia_boundary_crisis.dds`
- Proposed sprite name: `GFX_news_event_utopia_boundary_crisis`
- Suggested `.gfx` file: `interface/chaosx_pictures.gfx`
- Related use: Event 015 boundary-crisis news image

## Super-events

- Final DDS path: `gfx/super_events/015_utopia_manifesto/super_event_utopia_new_utopia.dds`
- Proposed sprite name: `GFX_super_event_utopia_new_utopia`
- Suggested `.gfx` file: `interface/chaosx_super_events.gfx`
- Related use: Event 015 New Utopia proclamation super-event

- Final DDS path: `gfx/super_events/015_utopia_manifesto/super_event_utopia_marked_bounds.dds`
- Proposed sprite name: `GFX_super_event_utopia_marked_bounds`
- Suggested `.gfx` file: `interface/chaosx_super_events.gfx`
- Related use: Event 015 Marked Bounds doctrine super-event

## Scripted GUI pack

- Final DDS path: `gfx/interface/utopia_manifesto/utopia_ledger_background_panel.dds`
- Proposed sprite name: `GFX_utopia_ledger_background_panel`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: base decorative background for the Utopian Ledger scripted GUI

- Final DDS path: `gfx/interface/utopia_manifesto/utopia_ledger_header_plate.dds`
- Proposed sprite name: `GFX_utopia_ledger_header_plate`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: static top plate for the Utopian Ledger scripted GUI

- Final DDS path: `gfx/interface/utopia_manifesto/utopia_ledger_warning_panel.dds`
- Proposed sprite name: `GFX_utopia_ledger_warning_panel`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: warning-state panel for Overreach or Marked Bounds copy blocks

- Final DDS path: `gfx/interface/utopia_manifesto/utopia_ledger_seal_sheet.dds`
- Runtime sprite name: `GFX_utopia_ledger_seal_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: animated Ledger seal in `interface/015_utopia_manifesto_ledger.gui`

- Final DDS path: `gfx/interface/utopia_manifesto/utopia_overreach_warning_sheet.dds`
- Runtime sprite name: `GFX_utopia_overreach_warning_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: animated warning icon visible under high Overreach, high Suspicion, Marked Bounds pressure, or Marked Bounds State identity

- Final DDS path: `gfx/interface/utopia_manifesto/utopia_storehouse_fill_sheet.dds`
- Runtime sprite name: `GFX_utopia_storehouse_fill_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: animated storehouse meter visible after store-network, local-storehouse, or Common Store State progress

- Final DDS path: `gfx/interface/utopia_manifesto/utopia_new_utopia_seal_sheet.dds`
- Runtime sprite name: `GFX_utopia_new_utopia_seal_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: animated late New Utopia identity seal visible in the Ledger header

- Final DDS path: `gfx/interface/utopia_manifesto/utopia_marked_bounds_seal_sheet.dds`
- Runtime sprite name: `GFX_utopia_marked_bounds_seal_animated`
- Runtime `.gfx` file: `interface/015_utopia_manifesto.gfx`
- Related use: animated late Marked Bounds State identity seal visible in the Ledger header

## Implementation notes

- Runtime registration now lives in `interface/015_utopia_manifesto.gfx`.
- The event pictures, super-event pictures, focus icons, decision icons, idea icons, achievement icons, static GUI art, and animated GUI sheets are all registered through that Event 015 sprite file.
- The Utopian Ledger GUI uses `interface/015_utopia_manifesto_ledger.gui` and `common/scripted_guis/015_utopia_manifesto_scripted_gui.txt`.
- The full `gfx/interface/utopia_manifesto/` runtime family was regenerated from imagegen source art on 2026-07-01. Static fallbacks exist beside every animated sheet, and live scripted GUI visibility triggers are wired for all five animated sprites.

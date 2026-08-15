# Event 011 Secret Alliance GUI Repair Handoff

## Scope and ownership

This repair is limited to the Event 011-owned `secret_alliance_counter_network_scripted_gui` and its `secret_alliance_counter_network_container` window. The shared Event Log, event-details framework, settings window, super-event framework, and unrelated decision interfaces were not changed.

## Implemented layout

The 720x360 background remains scaled to the 500x250 decision-category surface at `0.694444`. The title and selected lead are centered inside the upper painted strip. Evidence and Preparedness occupy separate centered rows inside the second strip: equal 192-pixel label regions at y55 and centered 80x8 bars at y70, with the full band names retained in hover tooltips. All Event 011 centered text boxes use vanilla's lowercase `maxwidth` field; the former `maxWidth` spelling left them visibly anchored to the left in-game.

The three 184x96 source card frames resolve to 128x67 at displayed x28, x185, and x342, y112. Their transparent click regions use the same displayed bounds, and each suspect label is centered in the parchment area to the right of its portrait slot.

The old scrollable objectives block was removed because it duplicated the decision and mission list and crossed the third card bay. The footer now contains one scripted-localisation status line, a compact Evolution III warning emblem, a centered War Pressure readout, and the Motion control on the painted button plate. The status line chooses hidden-state or recent-operation text in one element, eliminating the previous overlapping pair.

## Files changed

- `interface/011_secret_alliance.gui`
- `common/scripted_guis/011_secret_alliance_scripted_gui.txt`
- `common/scripted_localisation/011_secret_alliance_gui_scripted_localisation.txt`
- `localisation/english/011_secret_alliance_l_english.yml`
- `localisation/english/011_secret_alliance_gui_l_english.yml`
- `docs/events/011_secret_alliance/overview.md`

## MCP evidence

The final narrow inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c2437d78f48e7fc2bbe6972809c184deed3f12a8db201512d5b147971388940/5f88cad39a3a659983af09e9b60a25e6507fcc4730d063a1b6fcb85904c7aa67/gui-inspect.0a6c6b016bac09b0.json`. It resolved 27 elements for the Event 011 window.

The final render-matrix artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30573dc1712096fe97fc9b1a1785d9d0d40665786b3e9f13f293844e4d8dce17/24b8ca44a53fc635c0c741dc08de43287f647a6148add47b8738bbfe852413a5/secret_alliance_counter_network_container-full.svg`. It covers normal, hover, selected, locked, disabled, warning, active, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states at 1280x720, 1366x768, 1600x900, 1920x1080, and 2560x1440, plus 1920x1080 at UI scale 1.25.

The mandatory `hoi4.gui_rewrite` call was attempted against the exact Event 011 file and window after the layout was authored. It returned `REWRITE_STRUCTURE_LIMIT` and changed no files. The bounded source edits were therefore applied through the repository patch workflow, then re-inspected and re-rendered through the MCP.

## Limitations

The MCP render is explicitly labelled as an offline approximation. Its magenta rectangles are click-region overlays for the three transparent suspect selectors, not missing in-game panels. The MCP's repository-wide GUI graph still truncates unrelated diagnostics, so the global diagnostic count is not evidence against or for this isolated Event 011 layout. No live in-game consumer validation is claimed.

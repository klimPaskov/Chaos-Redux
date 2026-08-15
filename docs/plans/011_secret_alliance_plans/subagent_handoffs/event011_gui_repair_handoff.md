# Event 011 Secret Alliance GUI Repair Handoff

## Scope and ownership

This repair is limited to the Event 011-owned `secret_alliance_counter_network_scripted_gui` and its `secret_alliance_counter_network_container` window. The shared Event Log, event-details framework, settings window, super-event framework, and unrelated decision interfaces were not changed.

## Implemented layout

The 720x360 background remains scaled to the 500x250 decision-category surface at `0.694444`. The title and selected lead are centered inside the upper painted strip. Evidence and Preparedness are centered over two 178x17 meters inside the second strip, with the full band names retained in hover tooltips.

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

The final narrow inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4c8c863afbbd1f28bfc6be60c194e8debf7680ac5cfd207d17419208e5b3b5df/66bda108e7bf48a9bcb82605b71c68fc7701596267f62f2481806eff08dc061a/gui-inspect.0b6cec564cb5be80.json`. It resolved 27 elements for the Event 011 window.

The final render-matrix artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfc6626f94a2bca0fb0ef3b44a476fdaa5ff0e1043f2a8ea94c698af13e5a477/c42c5a8f40ead8f3ecc91792076575e8d224c35b20848db55b3c5d0488d33bcf/secret_alliance_counter_network_container-full.svg`. It covers normal, hover, selected, locked, disabled, warning, active, empty-list, full-list, minimum-value, maximum-value, long-text, and missing-localisation states at 1280x720, 1366x768, 1600x900, 1920x1080, and 2560x1440, plus 1920x1080 at UI scale 1.25.

The mandatory `hoi4.gui_rewrite` call was attempted against the exact Event 011 file and window after the layout was authored. It returned `REWRITE_STRUCTURE_LIMIT` and changed no files. The bounded source edits were therefore applied through the repository patch workflow, then re-inspected and re-rendered through the MCP.

## Limitations

The MCP render is explicitly labelled as an offline approximation. Its magenta rectangles are click-region overlays for the three transparent suspect selectors, not missing in-game panels. The MCP's repository-wide GUI graph still truncates unrelated diagnostics, so the global diagnostic count is not evidence against or for this isolated Event 011 layout. No live in-game consumer validation is claimed.

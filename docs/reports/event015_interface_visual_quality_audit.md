# Event 015 interface and focus-tree visual-quality audit

This audit covers only Event 015 surfaces: the Commonwealth Ledger, the Event 015 route-specific proclamation in the shared super-event shell, and the `utopia_manifesto_tree` focus tree.

## Ledger GUI

The HOI4 MCP inspected `utopia_manifesto_ledger_container` with the `ledger_default` scenario and rendered normal, hover, selected, long-text, and missing-localisation states at 1280x720, 1600x900, 1920x1080, and 1920x1080 at UI scale 1.25.

The ledger layout contains 71 modeled elements with no visible clipping, no text overflow, and no scene-level layout diagnostics in the decoded 1920x1080 layout artifact.

The four tabs and refresh control each have a complete 123x36 clickable region at x positions 31, 195, 359, 523, and 545 respectively, and the panel content remains inside its 652x222 content frame.

The callings scenario was rendered separately at 1920x1080 at UI scales 1 and 1.25 with normal, hover, selected, and long-text states; it retained the same complete click regions and had no visible clipping or text overflow.

The renderer reports 1875 global source-graph blockers and 335 global visible-overlap diagnostics for the ledger call, but those diagnostics are from unrelated shared GUIs and conditional offline fallbacks rather than Event 015 layout elements.

## Regional proclamation super-event

The HOI4 MCP inspected and rendered `chaosx_super_events` with the Event 015 proclamation scenario across 1280x720, 1600x900, 1920x1080, and 1920x1080 at UI scale 1.25, including normal, hover, selected, long-text, and missing-localisation states.

The decoded Event 015 shell layout contains eight modeled elements, a 899x592 shell at the 1920x1080 reference resolution, no visible clipping, no text overflow, and a full 352x48 close-button region at x 559.5 and y 766.5.

The offline scenario schema accepts the visibility flag only as a boolean, so it cannot select the numeric Event 015 route image ID used by `GetSuperEventImage`; the route-specific image IDs and DDS files were nevertheless verified directly in `015_utopia_manifesto_super_event.gfx` and the five Event 015 route files.

The MCP emitted one `GUI_TEXTURE_UNSUPPORTED` warning for the shared `super_event_option.dds` close-button texture because its RGB parser considers the data truncated; the file is an exact 352x48 uncompressed RGBA payload, so this is an offline-parser warning rather than a source asset defect.

The super-event call also reports global shared-GUI diagnostics, including 1875 source-graph blockers and six visible overlaps, with no Event 015-specific clipping or bounds failure.

## Focus tree

The `hoi4-focus-trees` skill was applied before editing and the HOI4 MCP inspected, rendered, and rasterized `common/national_focus/015_utopia_manifesto_focus_tree.txt` with tree ID `utopia_manifesto_tree`.

The tree has 124 focuses and 174 prerequisite connectors with bounds x=-3..54 and y=0..16, zero duplicate coordinates, and no same-row spacing violations.

The authored coordinate pass changes only x positions and keeps focus IDs, y lanes, prerequisites, exclusions, rewards, AI, icons, and localisation unchanged.

The final MCP pass reports 47 connector crossings, 20 through-node warnings, and 20 long connectors as non-blocking layout warnings caused by deliberate inter-route prerequisites and the final multi-route convergence proof.

The MCP validation reports 14 blocking diagnostics for the shared continuous-focus palette, specifically missing generic continuous-focus sprites, plus one related continuous-focus localisation warning; no Event 015-authored focus icon or Event 015 focus localisation is missing.

The final render and raster are 6574x1836 at review scale 1 and were generated successfully with source-linked SVG, HTML, JSON, PNG, and source-map artifacts.

## Scope disposition

No shared event-log window or unrelated GUI was changed.

No additional source patch is justified by the Event 015 GUI geometry evidence after the tab hit-box, clipping, text-density, and focus-coordinate corrections.

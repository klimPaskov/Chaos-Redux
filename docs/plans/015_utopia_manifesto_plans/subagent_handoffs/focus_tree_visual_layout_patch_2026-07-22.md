# Event 015 focus-tree visual layout patch - 2026-07-22

## Scope

This handoff supersedes the earlier read-only visual finding for the narrow coordinate pass.

It changes only authored `x` positions in `common/national_focus/015_utopia_manifesto_focus_tree.txt`.

Focus IDs, y lanes, prerequisites, mutual exclusions, icons, rewards, AI, and localisation are unchanged.

## Evidence and result

The earlier HOI4 MCP inspection/render reported 124 focuses, 174 prerequisite connectors, 54 crossings, 17 through-node intersections, and 21 long connectors.

The patch rebalances opening, support, foreign-commonwealth, Necessary Ground, crisis, and formation-lane endpoints while retaining the existing y lanes and route identities.

The post-patch local geometry check reports 124 focuses, 174 connectors, 48 strict segment crossings, zero connector-through-focus intersections, zero duplicate coordinates, and zero same-row spacing violations.

The final recovered HOI4 MCP reports 47 connector crossings, 20 through-node warnings, and 20 long connectors as non-blocking layout warnings for the authored inter-route convergence geometry, with no duplicate-coordinate or same-row-spacing violation.

## Validation and remaining risk

The source parser confirms every prerequisite parent remains above its child.

The final MCP focus render and raster artifacts completed successfully at review scale 1 with a 6574x1836 raster and source-linked HTML, SVG, JSON, PNG, and source-map outputs.

No gameplay behavior or focus visibility logic was changed.

The remaining 14 MCP blocking diagnostics belong to the shared continuous-focus palette's generic missing sprite references, plus one related continuous-focus localisation warning.

No Event 015-authored focus icon or localisation is missing.

## Changed file

- `common/national_focus/015_utopia_manifesto_focus_tree.txt`

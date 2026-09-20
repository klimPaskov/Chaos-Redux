# Focus and technology visual QA profile

This profile records a reproducible, read-only review of three national focus trees and three technology folders, with five user-supplied in-game images. It is a review recipe, not a visual-accuracy verdict or a passed scenario suite.

## Route preflight

Before calling any route, verify the version and health of the **connected** `hoi4-agent-tools` server, inspect its live tool schemas, and confirm that the intended client can call them. Tool names being exposed do not establish service health or standalone viewer availability. The connected global process was identified as 3.0.7 for the supplied comparison; builds under `C:/Users/klimp/Documents/Projects/hoi4-agent-tools-stage5` are separate local evidence and must not be described as the connected process. If a newer schema or route is unavailable, use only the confirmed installed read-only route and record the exact gap. Check standalone Technology Tree Viewer availability separately.

The current exposed focus routes are `hoi4.focus_inspect`, `hoi4.focus_render`, and `hoi4.focus_raster`. Use `hoi4.focus_inspect` with `mode = national`, `relativePath`, and `treeId`; use the same `relativePath` and `treeId` with `hoi4.focus_render` for structural HTML/SVG/JSON and `hoi4.focus_raster` for icon-decoded PNG. For comparison with these screenshots, pass `horizontalSpacing = 96` and `verticalSpacing = 130` to both render routes. There is no exposed `hoi4.focus_compare` route; compare saved artifacts and the screenshot manually, with the same source revision and viewport assumptions.

The current exposed technology routes are `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare`. Use `hoi4.tech_inspect` with `mode = folders` to discover the inventory, then `hoi4.tech_render` with `view = folder` and the exact `folderId` for each folder; retain its JSON, SVG, PNG, source revision, diagnostics, and unresolved geometry. Use `hoi4.tech_compare` with explicit `before` and `after` source graphs only when checking a source change. It compares technology graphs, not an MCP image with an in-game screenshot. Confirm the live schema before supplying any additional selector.

## Reference mapping and expected evidence

| Surface and source selector | In-game reference in `C:/Users/klimp/OneDrive/Pictures/Screenshots/` | Inventory to check | Placement evidence to check |
| --- | --- | --- | --- |
| `fury_focus_tree` in `common/national_focus/007_fury_focus_tree.txt` | `Screenshot 2026-09-20 171441.png` | 52 focuses | Source coordinates, branch order, prerequisites, connector crossings, icons, labels, and continuous-focus placement. |
| `THR_focus` in `common/national_focus/003_holy_realm.txt` | `Screenshot 2026-09-20 171505.png` | 111 focuses | The same checks across the full tree; compare its large canvas at matched zoom and scroll. |
| `utopia_manifesto_tree` in `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `Screenshot 2026-09-20 171353.png` | 124 focuses | The same checks across its wide branches and continuous-focus panel. |
| `infantry_folder` | `Screenshot 2026-09-20 172032.png` | 43 rendered nodes in the supplied comparison | 43 source pixel placements, branch paths, card skins, equipment names, folder art, years, and research-state markers. |
| `chemical_warfare_folder` | `Screenshot 2026-09-20 172056.png` | 40 rendered nodes in the supplied comparison | Check all 40 placements before comparing the visible section, including the separate `mobile_cbrn_hospitals` gridbox and connector routing. |
| `biowarfare_folder` | **No supplied in-game screenshot** | 12 nodes in the separate local source-build evidence | Check source placement and render coverage only; in-game visual agreement is unmeasured. |

Technology source checks include `common/technologies/chaosx_technologies.txt`, `common/technologies/cbrn_hq_technologies.txt`, `common/technologies/cbrn_regimental_support_technologies.txt`, `common/technology_tags/chaosx_tech_tags.txt`, and `interface/countrytechtreeview.gui`. The infantry folder also draws on vanilla technology definitions and interface assets.

The private local evidence is `C:/Users/klimp/Documents/Projects/hoi4-agent-tools-visual-qa-2026-09-20/comparison.md`; its render artifacts remain outside the mod. That comparison found the 3.0.7 focus renders useful for inventory and branch structure at 96 by 130 spacing, while their cards, connectors, frame, and viewport differ visibly from the game. Its infantry render resolved 43 source placements. Its connected 3.0.7 chemical render reported all 40 placements unresolved despite a `sourceAccurate = true` flag, so that flag cannot establish layout fidelity. The separate local source build resolved 40 of 40 chemical and 12 of 12 biological placements, but it is not evidence of connected-process capability or biological in-game agreement.

## Review conditions and limits

Record the game country, enabled DLC, research state, zoom, scroll offset, and screenshot viewport before making a precise image comparison. Those values were not supplied for these five screenshots. Compare complete source inventory and placement first; then align a matching visible viewport and inspect icon centers, card states, labels, folder backgrounds, paths, continuous-focus panel, and clipped or missing elements. Keep source geometry agreement separate from presentation agreement. Do not infer a numerical similarity result from the current references.

The parent owns renderer fixes and final source/MCP review; the user owns live-game validation. Any future focused scenario suite must identify the checked surface, source revision, reference image, viewport assumptions, inventory coverage, placement coverage, visual findings, and unresolved limitations before it can report a case result.

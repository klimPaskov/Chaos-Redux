# Focus and technology visual QA profile

This profile records a reproducible, read-only review of three national focus trees and three technology folders, with five in-game screenshots and two icon crops supplied by the user. It is a review recipe, not a visual-accuracy verdict or a passed scenario suite.

## Route preflight

Before calling any route, verify the version and health of the **connected** `hoi4-agent-tools` server, inspect its live tool schemas, and confirm that the intended client can call them. Tool names being exposed do not establish service health or standalone viewer availability. Use only confirmed installed read-only routes and record any missing capability. Check standalone Technology Tree Viewer availability separately.

Use `hoi4.focus_inspect` with `mode = national`, `relativePath`, and `treeId`; use the same `relativePath` and `treeId` with `hoi4.focus_render` for structural HTML/SVG/JSON and `hoi4.focus_raster` for icon-decoded PNG. For comparison with these screenshots, pass `horizontalSpacing = 96` and `verticalSpacing = 130` to both render routes. Compare saved artifacts and the screenshot at the same source revision and viewport assumptions; use a focus comparison route only when its live schema is available.

Use `hoi4.tech_inspect` with `mode = folders` to discover the inventory, then `hoi4.tech_render` with `view = folder` and the exact `folderId` for each folder; retain its JSON, SVG, PNG, source revision, diagnostics, and unresolved geometry. Use `hoi4.tech_compare` with explicit `before` and `after` source graphs when checking a source change. It compares technology graphs, so compare its image with an in-game screenshot separately. Confirm the live schema before supplying any additional selector.

When `hoi4.scenario_test` is confirmed in the connected server, run `visual_surfaces_suite.json` with `suitePath = docs/testing/hoi4_agent_tools_profiles/visual_surfaces_suite.json` and a bounded `maxCases`; resume with its returned continuation until all nine cases finish. The suite checks focus inventories and tree selection plus technology folder placement and node coverage. Use `hoi4.focus_raster` and the rendered image artifacts for the screenshot review, since the suite cannot assert pixel similarity or replace the visual comparison below.

## Reference mapping and expected evidence

| Surface and source selector | User-supplied in-game reference | Inventory to check | Placement evidence to check |
| --- | --- | --- | --- |
| `fury_focus_tree` in `common/national_focus/007_fury_focus_tree.txt` | `Screenshot 2026-09-20 171441.png` | 52 focuses | Source coordinates, branch order, prerequisites, connector crossings, icons, labels, and continuous-focus placement. |
| `THR_focus` in `common/national_focus/003_holy_realm.txt` | `Screenshot 2026-09-20 171505.png` | 111 focuses | The same checks across the full tree; compare its large canvas at matched zoom and scroll. |
| `utopia_manifesto_tree` in `common/national_focus/015_utopia_manifesto_focus_tree.txt` | `Screenshot 2026-09-20 171353.png` | 124 focuses | The same checks across its wide branches and continuous-focus panel. |
| `infantry_folder` | `Screenshot 2026-09-20 172032.png` | 43 nodes | 43 source pixel placements, branch paths, card skins, equipment names, folder art, years, and research-state markers. |
| `chemical_warfare_folder` | `Screenshot 2026-09-20 172056.png` and three-card crop `codex-clipboard-16def16d-125e-40d1-b162-ed8b13c9fbd9.png` | All placements; 40 in the screenshot's source revision and 22 in the sampled render revision | Check every placement before comparing the visible section, including the separate `mobile_cbrn_hospitals` gridbox when present, connector routing, and three large icon cards. |
| `biowarfare_folder` | Four-card in-game crop `codex-clipboard-8e95273d-af93-4de3-862d-3cc9f2dba61b.png`; no full-folder screenshot | 12 nodes | Check source placement and render coverage, then compare the four large icon cards at native size. Full-folder visual agreement is unmeasured. |

Technology source checks include `common/technologies/chaosx_technologies.txt`, `common/technologies/cbrn_hq_technologies.txt`, `common/technologies/cbrn_regimental_support_technologies.txt`, `common/technology_tags/chaosx_tech_tags.txt`, and `interface/countrytechtreeview.gui`. The infantry folder also draws on vanilla technology definitions and interface assets.

## Review conditions and limits

Record the game country, enabled DLC, research state, zoom, scroll offset, and screenshot viewport before making a precise image comparison. Those values were not supplied for these five screenshots. Compare complete source inventory and placement first; then align a matching visible viewport and inspect icon centers, design-team icons, card states, status corners, labels, folder backgrounds, paths, continuous-focus panel, and clipped or missing elements. A screenshot and render with different source revisions cannot support a pixel-similarity claim. Keep source geometry agreement separate from presentation agreement. Do not infer a numerical similarity result from the current references.

The parent owns renderer fixes and final source/MCP review; the user owns live-game validation. Any future focused scenario suite must identify the checked surface, source revision, reference image, viewport assumptions, inventory coverage, placement coverage, visual findings, and unresolved limitations before it can report a case result.

## Large technology icon crops

The user also supplied `codex-clipboard-16def16d-125e-40d1-b162-ed8b13c9fbd9.png` with three chemical warfare cards and `codex-clipboard-8e95273d-af93-4de3-862d-3cc9f2dba61b.png` with four biological warfare cards. Check that `hoi4.tech_render` resolves the source `GFX_*_medium` artwork and paints it at native size inside each 72-pixel technology item. Compare the 70 by 70 pixel card interiors without resizing or sharpening and retain their source revision and mapped positions.

The sampled source render matches the seven supplied card interiors at normalized grayscale template correlations from 0.998712 to 0.999589. The biological card centers follow 180-pixel horizontal spacing and the chemical cards follow 90-pixel horizontal and 200-pixel vertical spacing in the supplied crops and render. The chemical scan revision is `23d51c74e307541decace0b3c0bd85687bdfdb3d64eb5cb409d8e1df214ade71`; the biological scan revision is `89d8360406721e6d29505f6bb009144979026e42302b4ba57a585abb578c02c1`. These are icon-card measurements; they do not measure full-folder pixel accuracy. The chemical screenshot and sampled source render contain different source inventories, so their whole-image similarity is unresolved.

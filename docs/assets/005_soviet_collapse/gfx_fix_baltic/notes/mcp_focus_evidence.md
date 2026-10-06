# Baltic Focus MCP Evidence

## Read-only tree inspection

- Tool: `hoi4.focus_inspect`, mode `national`, tree id `soviet_collapse_baltic_focus_tree`, source `common/national_focus/005_soviet_collapse_republics.txt`.
- Result: `FOCUS_INSPECTED`, status `ok`, no blockers, 42 focus nodes, one tree, source path `mod:common/national_focus/005_soviet_collapse_republics.txt`.
- Source revision returned by the inspect result: `5e097fb6ceb61b1a56cb0a828aaff2c6c0a474a03778966faa01ce4f60aa7852`.
- The saved inspect artifact is `notes/mcp_focus_inspect.json`; its SHA-256 is `af5d7db249bb4e074ecc502752c3ba1400f8819323cd290f81895abf9aa60953`.
- Diagnostics: five `FOCUS_LAYOUT_LINEAR_DETOUR` warnings within the Baltic tree and one generic continuous-focus localisation reference warning for `continuous_restrict_freedom_desc`. No icon-path diagnostic or blocker was returned.

## Read-only tree raster

- Tool: `hoi4.focus_raster`, mode `national`, tree id `soviet_collapse_baltic_focus_tree`, source `common/national_focus/005_soviet_collapse_republics.txt`, review scale `1`, 16 affected focus ids highlighted.
- Result: `FOCUS_RASTERIZED`, status `ok`, validation passed, no blockers, output size `4176x1280`, layout hash `2191325cb68b49ee8ebeeb335bd8e95b89c29b7e63cafad6eed4a57f03ebf517`.
- Raster artifact SHA-256: `ae9f5e2a7957203fe516fbe1f55d6f175d8d8c73d9cd599584b03e173de69220`; the PNG is copied to `contact_sheets/mcp_baltic_focus_tree_before.png`.
- The tool also returned `MCP_RESPONSE_TRUNCATED` because its JSON exceeded the wire limit; the PNG and its manifest were present locally and copied intact. The manifest records source revision `4aae15f240daebf073a43c45c0dce1a4db87b1d15989b8e496c3275eddbf7dac`, inventory count `59`, and tool version `3.9.0`.

## Scope limit

The GFX registry and runtime DDS files were not changed, so this package has no post-integration tree raster. The parent later reported the reference-search transport had closed; no repeat or refresh call was made because the required inspect and raster evidence had already completed and the staged art was not wired.

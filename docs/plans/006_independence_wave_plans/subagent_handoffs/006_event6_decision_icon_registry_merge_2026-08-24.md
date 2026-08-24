# Event 006 decision-icon registry merge

Date: 2026-08-24.

## Disposition

The two small decision-icon GFX registries were merged into the existing Event 006 small-asset registry. This is a definition-only source-layout change. No sprite identifier, texture path, decision category, decision, package gate, or asset file changed.

## Moved sources

- `interface/006_independence_wave_iw043_iw058_decision_icons.gfx` — 18 sprite definitions for the IW-043 and IW-058 categories and decisions.
- `interface/006_independence_wave_iw093_iw098_decisions.gfx` — 16 sprite definitions for the IW-093 and IW-098 decisions.

All 34 definitions now live in `interface/006_independence_wave_small_assets.gfx` under source markers matching their former files. The two redundant source files were removed. The remaining larger package-owned portrait registries and the FORM-03, FORM-05, and Wallonia/Frisia GFX files remain separate so ownership-specific audits do not become one undifferentiated registry.

## Static preservation checks

- Source-to-target comparison: 18/18 IW-043/IW-058 definitions present; 16/16 IW-093/IW-098 definitions present.
- Duplicate sprite names: 0.
- Duplicate texture paths: 0.
- Missing referenced texture files: 0.
- Target registry total: 65 sprite definitions.

The change is outside gameplay, AI/probability, event IDs, decision categories, localisation, portraits, map, focus, and admission surfaces. No live game or MCP runtime claim is made by this handoff.

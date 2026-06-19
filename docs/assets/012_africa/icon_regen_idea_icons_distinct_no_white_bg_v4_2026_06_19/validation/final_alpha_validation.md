# Final Alpha Validation

Validated all 9 live DDS files in `gfx/interface/ideas/012_africa/`.

- Exact dimensions: every file is `64x64`.
- Transparent corners: all four corners are alpha `0` for every icon.
- Full opaque square check: no icon resolves to an opaque full-canvas square.
- White matte check: no near-white edge-matte pixels were detected adjacent to transparency.
- Asset-type separation: all 9 icons were independently generated and composed for the 64x64 idea or national-spirit surface. None are resized, cropped, recolored, or lightly edited focus or goal icons.

## Per-file Notes
- `idea_africa_authority_atlas.dds`: bbox `(7, 4, 56, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.
- `idea_africa_charter_league.dds`: bbox `(12, 4, 51, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.
- `idea_africa_high_chaos_actor.dds`: bbox `(15, 4, 48, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.
- `idea_africa_high_chaos_bestiary.dds`: bbox `(13, 4, 51, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.
- `idea_africa_is_one.dds`: bbox `(7, 4, 56, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.
- `idea_africa_liberation_war_office.dds`: bbox `(6, 4, 58, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.
- `idea_africa_paper_core_mandate.dds`: bbox `(16, 4, 47, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.
- `idea_africa_regional_authority.dds`: bbox `(5, 4, 59, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.
- `idea_africa_rsa_continental_emergency.dds`: bbox `(9, 4, 55, 60)`, corners `[0, 0, 0, 0]`, near-white edge pixels `0`, opaque-square `False`.

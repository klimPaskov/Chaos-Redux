# Portal raider counter repair

Status: both assigned rows are implemented and parent-approved for the focused v9 asset commit.

| Raw plan row | Disposition | Runtime asset and result |
|---|---|---|
| `GFX_unit_portal_raider_icon_medium_white` | implemented | `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds` now uses a full-opacity white raider bust and a filled vanilla on-map NATO plate with a black ring-and-bar portal glyph. |
| `GFX_group_portal_raider_icon` | implemented | `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds` now uses a flat sampled vanilla-green hooded bust with portal ring and a filled vanilla NATO plate with the same black line glyph. |

The selected bust and portal-ring source edits are native-alpha ImageGen outputs at `docs/assets/gfx_fix_2026-10/portal_raider_system/source_v2/portal_raider_bust.png` and `docs/assets/gfx_fix_2026-10/portal_raider_system/source_v2/portal_ring_glyph.png`. Their exact requests and pre-edit SHA-256 values are in `docs/assets/gfx_fix_2026-10/prompts/source_edit_requests_v2.json`. The bust source has zero boundary pixels at alpha thresholds 8–64; the ring source is fully inset with zero alpha boundary pixels at all recorded thresholds. The ring source uses a broad continuous black stroke and a clear transparent center.

Both DDS files were converted through the skill-local 2D converter with DirectXTex and decoded pixel-for-pixel against their processed PNGs. The large and on-map counter profiles report no findings across the v9 tranche. The reviewed native/enlarged source-to-PNG-to-DDS sheets are `docs/assets/gfx_fix_2026-10/contact_sheets/final_large_counters_source_png_dds_v9.png` and `docs/assets/gfx_fix_2026-10/contact_sheets/final_small_counters_source_png_dds_v9.png`; the post-promotion first-frame page is `docs/assets/gfx_fix_2026-10/contact_sheets/post_promotion_v9/portal_raider_system_final_v9_1.png`.

No `.gfx` file was changed by this asset handoff. Live in-game presentation remains user-owned validation.

# Alien infantry counter repair

Status: the two assigned severity-1 rows are implemented and parent-approved for the focused v9 asset commit.

| Raw plan row | Disposition | Runtime asset and result |
|---|---|---|
| `GFX_group_alien_infantry_icon` | implemented | `gfx/interface/counters/divisions_large/unit_alien_infantry_icon.dds` now has a transparent flat-green alien bust in frame 1; the accepted green alien head in frame 2 is preserved byte-for-byte from the v8 runtime snapshot. |
| `GFX_unit_alien_infantry_icon_medium_white` | implemented | `gfx/interface/counters/divisions_small/onmap_unit_alien_infantry_icon.dds` now has a solid light-grey alien bust in frame 1; frame 2 is preserved from the current accepted two-frame plate. |

The selected source is the fresh native-alpha edit at `docs/assets/gfx_fix_2026-10/alien_infantry_system/source_v2/alien_infantry.png`; its exact saved prompt and v1 input hash are in `docs/assets/gfx_fix_2026-10/prompts/source_edit_requests_v2.json`. The source alpha has zero boundary pixels at thresholds 8 through 64; isolated alpha-1 edge pixels remain visible only in the preserved source and are outside the processed mask threshold. The green body hue is sampled from installed vanilla counters.

Both final DDS files were converted through the skill-local 2D converter with DirectXTex and decoded pixel-for-pixel against their processed PNGs. The 11-item large and 13-item on-map counter profiles report no findings across the approved v9 tranche, including the alien entries. The reviewed native and enlarged comparison is `docs/assets/gfx_fix_2026-10/contact_sheets/final_large_counters_source_png_dds_v9.png`, `docs/assets/gfx_fix_2026-10/contact_sheets/final_small_counters_source_png_dds_v9.png`, and the narrow post-promotion page `docs/assets/gfx_fix_2026-10/contact_sheets/post_promotion_v9/alien_infantry_system_final_v9_1.png`.

Frame 2 is deliberately retained because the accepted plan says the alien-head NATO state is already correct. This package does not claim in-game presentation acceptance; live validation remains user-owned.

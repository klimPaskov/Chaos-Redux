# Riga Corridor Switchyards Icon Handoff

The national-focus icon for `baltic_soviet_collapse_riga_corridor_switchyards` is staged at the exact registered basename as a new painted Baltic railway emblem. It makes the rail junction, manual point lever, freight semaphore, and blank brass dispatch panel readable at focus-icon scale. The native-alpha source has no text or readable glyphs.

## Source and processing

- ImageGen source: `docs/assets/005_soviet_collapse/gfx_fix_baltic/riga_followup/source_png/riga_corridor_switchyards_source.png` (1312x1199, SHA-256 `2b2c74599f0f59427c0baea0fa40381e3881d78e7f7e81d57fa0439028fdf552`).
- Exact generation prompt: `docs/assets/005_soviet_collapse/gfx_fix_baltic/riga_followup/prompts/riga_corridor_switchyards.prompt.txt` (SHA-256 `a6b8078b98aba125ae456ebfa4f19af08bcda69b2c80950e60d189217e9332cb`). Native transparent background was requested in the initial ImageGen call. No background removal was used.
- Processed PNG: `docs/assets/005_soviet_collapse/gfx_fix_baltic/riga_followup/processed_png/riga_corridor_switchyards_94x86.png` (94x86 RGBA, SHA-256 `40d18ba60b746e15c4d1d426eefb865d42c1faeed42a8cdb7ccdd95850ec89eb`). The complete nonzero-alpha bounds were fit proportionally with premultiplied Lanczos into 88x80 and centered on the transparent canvas. Visible bounds at alpha >=16 are `[3, 3, 91, 82]`, yielding an 88x79 subject and margins 3/3/3/4 px.
- The `gfx.py alpha` audit reports alpha range 0-255, alpha mean above 200, and zero chroma-edge pixels. No defringe, opacity boost, or alpha erosion was needed. The painted green laurel and red-white semaphore are intentional subject colors.

## DDS and review

- Staged DDS: `docs/assets/005_soviet_collapse/gfx_fix_baltic/riga_followup/final_dds/focus_005_baltic_soviet_collapse_riga_corridor_switchyards.dds`. Intended runtime path: `gfx/interface/goals/005_soviet_collapse/focus_005_baltic_soviet_collapse_riga_corridor_switchyards.dds`. DDS SHA-256: `c4d12af9f1549244ec33d5aac2d43c9aa4a63c2a679a5860d2532cba2953575d`.
- Strict validation is recorded in `notes/dds_validation.json`: 94x86, exact 128-byte legacy BGRA header, 32-bit BGRA masks, no mipmaps, exact payload length, full alpha range, and decoded RGBA exactly equals the processed PNG.
- Full-resolution source on checker and dark: `contact_sheets/riga_source_full_resolution_alpha_review.jpg`.
- Native PNG-before-DDS and strict DDS round-trip on checker, dark, and light backgrounds: `contact_sheets/riga_native_png_vs_dds_checker_dark_light.png`.
- Original 64x60 focus subject versus the new 88x79 subject at the same 94x86 consumer size: `contact_sheets/riga_before64_after88_native_compare.png`. The 4x DDS checker detail is `contact_sheets/riga_dds_enlarged_checker_4x.png`. Index and visual dimensions are in `notes/final_reviews.json`.

## Parent installation and limits

The pre-promotion original DDS snapshot was read from `docs/assets/005_soviet_collapse/gfx_fix_baltic/source_dds/live/focus_005_baltic_soviet_collapse_riga_corridor_switchyards.dds` (SHA-256 `628becd6fef411a7dfc56524e258cd346af68fc5898e377f0061524d463322d3`); its visible bounds were `[16, 15, 80, 75]`, or 64x60. The parent installed the approved candidate at the runtime path at 2026-10-06 07:42:27. My later read-only runtime observation is recorded in `notes/runtime_source_reference.json` and matches the staged DDS hash; I made no runtime, `.gfx`, focus, localisation, or gameplay write. The parent's `notes/parent_installed.json` receipt remains untouched.

The parent reported that the MCP connection was closed. I did not retry or refresh it and have no post-install MCP raster evidence. Final focus-tree reporting and the one-asset commit remain parent-owned.

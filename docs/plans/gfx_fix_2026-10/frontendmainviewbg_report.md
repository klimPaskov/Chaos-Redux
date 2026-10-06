# Frontend background repair

Disposition: implemented asset repair; MCP GUI visual gate remains blocked.
Acceptance basis: the graphics-fix task requests the full-bleed 1920×1440 background.

The original `gfx/chaosx_main_menu.dds` was 1448×1086 with black bands above and below the painting.
Native ImageGen extended the violet sky and foreground reeds while retaining the central red-river scene, temples, hand and staff.
The replacement is full-bleed 1920×1440 DXT1/BC1, one mip level, at the same runtime filename.
`interface/frontendmainviewbg.gfx` retains the existing sprite and 1920×1440 size block.
The inspected vanilla precedent is `interface/frontendmainviewbg.gfx` and `interface/frontendmainview.gui`, `frontend_background`, with native `load_5.dds` framing.

## Production evidence

Native source: `docs/assets/gfx_fix_shared_ui/menu_source.png`.
Original native ImageGen basename: `exec-9456d73f-d4af-4e5d-861e-e29c59b86b7e.png` under `C:/Users/klimp/.codex/generated_images/01a10fb7-f6ce-7862-9e28-a192ae914d46/`.
The prompt requests removal of the black strips through natural sky and grass extension, preserving the central painting without zoom or crop, no text, border or logo.
Processed source: `docs/assets/gfx_fix_shared_ui/menu_processed.png`.
DDS round-trip: `docs/assets/gfx_fix_shared_ui/chaosx_main_menu_roundtrip.png`.
Old/new group sheets: `docs/assets/gfx_fix_shared_ui/old_frontendmainviewbg_1.jpg` and `contact_sheets/frontendmainviewbg_1.jpg`.
The decoded texture was reviewed for full-bleed framing and the absence of black rows; compression introduces expected pixel differences from the lossless PNG.
Runtime SHA-256: `9af6897cd1bcc6729bfba54a148c569316bb0d487c8f7b70898a0a749c1a2029`.

The task explicitly requests DXT1/DXT5, so this background uses the DirectXTex primary backend directly with `-f BC1_UNORM -m 1`, rather than the skill's standard uncompressed icon output.
The converter is the official [Microsoft DirectXTex May 2026 release](https://github.com/microsoft/DirectXTex/releases/tag/may2026), executable SHA-256 `DCFDEC10244E02CF5037FBA089C55FB7E1326B1C8181742D77D15FA5CB5EEF06`.

## MCP gap and live check

The narrow `hoi4.gui_inspect` request for `frontend_background`, scenario `shared_ui_before`, date `1936.1.1`, `closedFlags=true`, stalled without a returned result and was stopped before promotion.
The following render request in that sequential cell was never reached.
No successful production render, cropped artifact or GUI validation file is claimed.
Local source/texture review does not establish production GUI coverage.

Open the main menu at 1920×1080, UI scale 1, and 1440×1080.
The river painting must fill its background with sky above and reeds below, without black letterbox bands; verify the logo and menu controls remain readable over it.
No findings were omitted or artwork fallbacks substituted; the outstanding limitation is the MCP GUI artifact gate.

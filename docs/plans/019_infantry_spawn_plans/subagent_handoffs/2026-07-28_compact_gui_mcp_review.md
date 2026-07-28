# Event 019 compact Muster Board MCP review

## Scope

This handoff records the user-directed compact correction for the direct Event 019 Muster Board surfaces. The board is now a 960 by 640 movable window over the compact background in `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/`.

The correction removes visible information rather than adding another decorative layer. The Overview keeps only Muster Control and Army Congestion as direct counters, removes the visible debt and saturation cards, removes the two explanatory request-cost paragraphs, and uses short labels for the request and lot-order controls. The Lots, Private Commands, Anomalous Hosts, and Muster History surfaces use shorter headings, constrained text boxes, and compact action rows. Gameplay tooltips and scripted GUI effects remain attached to the existing controls, so the visual reduction does not remove the underlying orders or their decision-equivalent logic.

The presentation deliberately has no authored slots, wells, rails, ledger cards, decorative grids, or portrait panels. The command surface keeps the existing army-only scene. The anomalous emblem sprite registrations remain available for the shared motion toggle but are scaled to zero in this presentation, matching the user-directed no-slot treatment.

## Source and asset changes

- `interface/019_infantry_spawn_muster_board.gui` now owns the 960 by 640 geometry, compact panel bounds, shortened action rows, and reduced text areas.
- `localisation/english/019_infrantry_spawn_l_english.yml` carries the compact player-facing labels and summaries.
- `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds` is the promoted 960 by 640 static background. Its authored source, processing proof, and manifest are in `docs/assets/019_infantry_spawn/gui_background_compact_2026_07/`.
- `docs/events/019_infantry_spawn.md`, `docs/assets/019_infantry_spawn/gfx_handoff.md`, and `docs/assets/019_infantry_spawn/manifest.md` describe the compact runtime contract.

## MCP visual review

The direct surfaces were rendered through `hoi4.gui_render` using the local Event 019 fixture with the compact source and promoted DDS:

- Overview at 1920 by 1080: artifact `a00aa6228d527b7e66d253f6f5374d5543116b9a7c85adbbb5f9629af75a0290`.
- Formation Lots at 1920 by 1080: artifact `ef49bd3bc41fa4bb9a7e23110db1d3d989f5de60cb6e34db8f81dedece34282b`.
- Private Commands at 1920 by 1080: artifact `20d298c6582450992cdea7a461d5c7c3b027fa5c519157efcfb4351bf96cb690`.
- Anomalous Hosts at 1920 by 1080: artifact `d7b694ef312418eca37902c4cae615bc28dd77726826ea856384b7d79ab3f20c`.
- Muster History at 1920 by 1080: artifact `5d93fb314af15d7ded355e2f5bb81f7f3965373c5f3d6d19d3f1df1fd29acb0d`.
- Overview at 1280 by 720: artifact `65ed1a91e52aa211d0e16aa786e784fab61f5328825d2019ca986840b99694f4`.

The first overview render exposed a title/seal collision. Moving the title and subtitle to the shared 92-pixel inset removed that overlap before the final sweep. The compact render review shows the frame, header, tabs, text, buttons, army scene, and lower band staying within their bounds at both reviewed resolutions; no clipping or overlap was visible on the populated direct surfaces.

The MCP fixture reports `MCP_RESPONSE_TRUNCATED` because its complete SVG diagnostics exceed the tool wire budget. Its offline renderer also lacks several vanilla font and sprite aliases and does not populate dynamic list rows, so list-entry text and live-data density were not asserted by the fixture. Those are review-environment limitations, not runtime GUI fallbacks. The source retains the existing dynamic lists and interaction hitboxes.

## Remaining presentation notes

No gameplay fallback, fixed-tag fallback, new registry file, Event Log surface, or direct Event 019 mechanic was changed in this presentation pass. The older 1120 by 760 handoffs remain as superseded historical records and point to this compact correction.

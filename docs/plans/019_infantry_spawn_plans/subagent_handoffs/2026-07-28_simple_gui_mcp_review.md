# Event 019 simple Muster Board GUI review

> Superseded by the compact 960x640 correction in `event19_compact_background_handoff.md` and the parent review handoff `2026-07-28_compact_gui_mcp_review.md`. The 1120x760 dimensions and evidence below are historical only.

## Scope

This handoff records the parent-owned visual correction after the earlier rail-and-slot treatment was rejected.

The Event 019 Muster Board now uses one authored 1120x760 background with a restrained header band, one broad paper/map field, and one shallow lower action band.

No decorative slot wells, left-side rail cells, registry cards, painted list cards, or tactical grid layers are used.

The GUI owns the title, tabs, dynamic text, list rows, army scene, and functional click regions over that field.

## Source changes

- `interface/019_infantry_spawn_muster_board.gui` removes the shared overview ledger rail and its six marker/text layers, removes decorative container backgrounds, and reflows every direct surface around the broad field.
- Overview, lots, command, anomalous, and history surfaces share the same margins and button rhythm while retaining their existing scripted GUI element names and decision effects.
- The seal and critical-command animation/static nodes remain registered for the existing scripted GUI references and are transparent interaction-free art layers.
- The anomalous animation/static nodes remain registered but are scaled to zero so the empty anomalous surface does not paint a small emblem that reads as an unintended slot; the anomalous tab and content remain state-driven.
- `docs/events/019_infantry_spawn.md` and `docs/assets/019_infantry_spawn/gfx_handoff.md` now describe the simple field/header/action-band composition and explicitly exclude decorative wells and slot grids.
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/2026-07-28_muster_board_layout_refinement.md` is marked historical and points to this superseding correction.

## MCP review evidence

The linked Event 019 GUI was inspected with the HOI4 MCP fixture and rendered on all five direct surfaces: overview, lots, command, anomalous, and history.

The explicit normal-state sweep covered 1280x720, 1366x768, 1920x1080, and 2560x1440 at UI scale 1.25 for the largest resolution.

The earlier state sweep also rendered normal, hover, selected, warning, and long-text cases at 1920x1080.

The MCP checks did not report text overflow, invalid size, children outside clipped parents, click-bound mismatches, conflicting click regions, missing sprites or textures, missing localisation, invalid animation frame counts or sheet dimensions, invalid parent windows, z-order risks, scroll-row cutoff, resolution drift, tab-state conflicts, missing button effects or triggers, cost mismatches, or missing AI-equivalent paths.

The corrected 1280x720 overview and the 1920x1080 previews for all five surfaces were visually inspected after the background replacement.

The previews show the broad authored field, aligned tabs, deliberate button rhythm, and army-only command imagery without painted wells or unused slot geometry.

## Offline fixture limits

The offline MCP renderer does not provide the full vanilla font and sprite alias registry, so it reports fixture-only missing-font and `GFX_tiled_window_transparent` diagnostics that are not Event 019 source omissions.

It also classifies the existing scripted `player_context` as unknown and emits heuristic overlap, alignment, spacing, transparent-hitbox, dynamic-list clipping, and unsupported-render-field warnings.

The dynamic list rows are intentionally empty in the fixture because the fixture does not populate the live scripted list data; this is not a gameplay fallback.

After the animation/static nodes were restored, no Event 019-specific missing-element or missing-animation-reference errors remained.

Live HOI4 was not launched, in accordance with the repository instructions that live consumer validation belongs to the user.

## Handoff status

The visual correction is ready for source review and commit.

No unapproved gameplay fallback was introduced by this pass.

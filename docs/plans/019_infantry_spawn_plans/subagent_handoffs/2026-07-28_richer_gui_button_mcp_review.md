# Event 019 richer background and button-label MCP review

## Scope

This handoff records the follow-up correction after the compact board review. The direct Event 019 Muster Board remains a 960 by 640 window with the reduced information set, but button labels are now separate left-aligned `instantTextBoxType` overlays rather than centered `buttonText` values. Every functional button keeps its original click name, scripted GUI binding, and `pdx_tooltip`; each visible overlay repeats the same tooltip key and is `alwaystransparent` so the underlying hitbox receives the click.

The static background is promoted from `docs/assets/019_infantry_spawn/gui_background_richer_2026_07/`. It keeps the same stable sprite identifier and runtime path while adding a continuous charcoal/brass frame, subdued map-grid drafting marks, paper seams, restrained red/steel traces, and an understated central muster compass. It contains no words, people, portraits, controls, slots, wells, rails, cards, or decorative compartments.

## Source changes

- `interface/019_infantry_spawn_muster_board.gui` removes centered `buttonText` and `buttonFont` fields from all direct Event 019 buttons and adds 39 left-aligned label overlays with compact padding. Overlay coordinates account for the `scale` applied to dense lot, claimant, and anomalous rows, so the left inset remains visually consistent instead of drifting toward the center. Dense scaled captions use the existing `hoi_12mbs` font; larger tabs and overview/request controls retain `hoi_14mbs`. Dynamic lot, family, and history entries retain their existing left-aligned text and transparent selection hitboxes.
- `gfx/interface/019_infantry_spawn/infantry_spawn_muster_board_background.dds` now uses the richer 960 by 640 runtime DDS. SHA-256: `758a9ec88a7f329b9a3aaf7a6570135e1e15becb75ef1bfd8f1a8db8439aa849`.
- `docs/events/019_infantry_spawn.md`, `docs/assets/019_infantry_spawn/gfx_handoff.md`, and `docs/assets/019_infantry_spawn/manifest.md` now describe the richer composition.

## Tooltip audit

All 41 Event 019 `buttonType` elements retain a `pdx_tooltip` key. The 39 new visible label overlays also carry the same key. The localization file contains 54 Event 019 Muster Board tooltip keys, and nested requirement/cost references resolve within the current localization package. No button was left without a hover description.

The visible captions are intentionally short where a full sentence would crowd a compact plate (`Audit`, `Close`, `Cadres`, `Field`, and `Accept`); the associated hover text remains the full cost, requirement, and outcome description. The longer `Territorial`, `Standardize`, `Demobilize`, and `Cannibalize` captions use the smaller scaled-row font rather than wrapping or changing the underlying actions.

## MCP review

The final MCP review requested normal and hover states and returned `GUI_INSPECTED` plus `GUI_RENDERED` for the affected Formation Lots, Private Commands, and Anomalous Hosts surfaces at 1920 by 1080 after the scale-aware coordinate pass. The broader sweep covered Overview, Formation Lots, Private Commands, Anomalous Hosts, and Muster History at 1920 by 1080, plus Overview at 1280 by 720. It showed the labels inside their hitboxes with a stable left inset, no wrapping, clipping, overlap, or accidental cross-panel labels, and the richer background remaining visible around the deliberately sparse board.

The final source GUI hash was `674E7C556E0EEB773EEB5F812719F40292537D9DE1B1966561888A27BAA09979` before this handoff-only documentation update.

The fixture has known environment limits: absent vanilla font metrics are approximated, some vanilla sprite aliases are unavailable, and dynamic list rows require supplied list data. These limitations affect evidence fidelity only. They are not runtime fallbacks and do not change the functional hitboxes or tooltip bindings.

## Remaining notes

No gameplay mechanic, Event Log surface, country registry, fixed-tag fallback, claimant identity, or focus route was changed in this presentation correction. The previous compact-background package remains retained as superseded asset history, while the richer package is the active runtime source.

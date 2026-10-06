# Event 006 animation asset manifest

Generated: 2026-07-25.

Scope: ASSET-040 recognition seal, ASSET-041 dependency warning, ASSET-042 league charter activation, and ASSET-043 formable eligibility seal.

Resolved target: 64x64 per frame for the small status-panel sprites. Every family uses a centered anchor, transparent corners, 5 FPS metadata, 200 ms frame timing, looping review playback, and `play_on_show = yes` for the explicit animated-mode toggle. The state strips, animated sprites, static fallbacks, GUI entries, and scripted-GUI mode toggle are registered in the Event 006 runtime definitions; dynamic visibility and click-region behavior remain an engine-evidence gate.

All source frames were separately authored with built-in ImageGen on a flat chroma-key background. The installed chroma-key remover, alpha crop, 58px fit, center placement, sheet assembly, GIF encoding, and DDS conversion are mechanical processing only. No transform-only animation is presented as final art.

| Asset | Package path | Source states / frame count | Processed frames | Sheet PNG / DDS | Static PNG / DDS | Review |
| --- | --- | --- | --- | --- | --- | --- |
| ASSET-040 | `independence_wave_recognition_seal/` | `hidden, weak, rising, strong, entrenched` / 5 | `source_frames/*.png`, `processed_frames/*.png` | `sheets/independence_wave_recognition_seal_sheet.png`; `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_sheet.dds` | `independence_wave_recognition_seal_static.png`; `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_static.dds` | `previews/independence_wave_recognition_seal_preview.gif`, `previews/independence_wave_recognition_seal_contact.png` |
| ASSET-041 | `independence_wave_dependency_warning/` | `calm, watch, danger` / 3 | `source_frames/*.png`, `processed_frames/*.png` | `sheets/independence_wave_dependency_warning_sheet.png`; `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_sheet.dds` | `independence_wave_dependency_warning_static.png`; `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_static.dds` | `previews/independence_wave_dependency_warning_preview.gif`, `previews/independence_wave_dependency_warning_contact.png` |
| ASSET-042 | `independence_wave_league_charter_activation/` | `rest, drafting, vote, activated` / 4 | `source_frames/*.png`, `processed_frames/*.png` | `sheets/independence_wave_league_charter_activation_sheet.png`; `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_sheet.dds` | `independence_wave_league_charter_activation_static.png`; `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_static.dds` | `previews/independence_wave_league_charter_activation_preview.gif`, `previews/independence_wave_league_charter_activation_contact.png` |
| ASSET-043 | `independence_wave_formable_eligibility_seal/` | `hidden, discovered, eligible, proclaimed` / 4 | `source_frames/*.png`, `processed_frames/*.png` | `sheets/independence_wave_formable_eligibility_seal_sheet.png`; `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_sheet.dds` | `independence_wave_formable_eligibility_seal_static.png`; `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_static.dds` | `previews/independence_wave_formable_eligibility_seal_preview.gif`, `previews/independence_wave_formable_eligibility_seal_contact.png` |

Exact byte sizes and SHA-256 values for every source, processed frame, sheet, static fallback, DDS, GIF, and contact sheet are in `animation_build_report.json` (report SHA-256 `26d2079766e05ac95fa342c0edc6b190820bd9e48015d6319fc63064037203c4`).

Registered sprite names are `GFX_independence_wave_recognition_seal_states`, `_static`, and `_animated`; `GFX_independence_wave_dependency_warning_states`, `_static`, and `_animated`; `GFX_independence_wave_league_charter_activation_states`, `_static`, and `_animated`; and `GFX_independence_wave_formable_eligibility_seal_states`, `_static`, and `_animated`.

Status: complete asset packages and registered runtime consumers. The current GUI/MCP evidence resolves the sprites and both supported resolutions, but does not execute dynamic tab visibility or prove live blendframe playback; no live runtime claim is made. No advisor, dossier, leader, commander, or unrelated gameplay surface was changed by this asset package.

## Current status consumers (2026-10-06)

Disposition: the four former semantic animation loops above are superseded as animated runtime consumers.
Their state-strip textures remain the static, value-selected readouts.
The four `_animated` sprite aliases use the same state-neutral ornamental ring; the four `_animated_static` aliases use its first frame.
All four static status symbols remain visible while the decorative ring plays.

The current ring is `gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_sheet.dds`: eight separately authored native-alpha 64x64 frames, one 512x64 sheet, 5 FPS.
The static fallback is `gfx/interface/006_independence_wave/animations/independence_wave_ornamental_ring_static.dds`.
Its source frames, selected processing outputs, contact sheets, preview, prompts and provider results are in `docs/assets/006_independence_wave/takeover_20261006_icons/animations/independence_wave_ornamental_ring/`.
The current hashes and parent wiring are recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/graphics_icons_20261006.md`.

Recognition state zero uses the selected bronze-rim seal, while recognition states one through four retain their exact prior pixels.
Dependency, League and formable semantic state strips remain unchanged.
The old loop GIFs above are archived historical previews; they do not describe the current animation.
MCP GUI source and visual evidence is reported separately in the current GUI handoff; native animation playback remains a live consumer check.

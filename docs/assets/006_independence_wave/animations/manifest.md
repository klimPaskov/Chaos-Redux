# Event 006 animation asset manifest

Generated: 2026-07-25.

Scope: ASSET-040 recognition seal, ASSET-041 dependency warning, ASSET-042 league charter activation, and ASSET-043 formable eligibility seal.

Resolved target: 64x64 per frame for the planned small status-panel sprites. Every family uses a centered anchor, transparent corners, 5 FPS metadata, 200 ms frame timing, looping review playback, and `play_on_show = no` for parent-controlled state display.

All source frames were separately authored with built-in ImageGen on a flat chroma-key background. The installed chroma-key remover, alpha crop, 58px fit, center placement, sheet assembly, GIF encoding, and DDS conversion are mechanical processing only. No transform-only animation is presented as final art.

| Asset | Package path | Source states / frame count | Processed frames | Sheet PNG / DDS | Static PNG / DDS | Review |
| --- | --- | --- | --- | --- | --- | --- |
| ASSET-040 | `independence_wave_recognition_seal/` | `hidden, weak, rising, strong, entrenched` / 5 | `source_frames/*.png`, `processed_frames/*.png` | `sheets/independence_wave_recognition_seal_sheet.png`; `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_sheet.dds` | `independence_wave_recognition_seal_static.png`; `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_static.dds` | `previews/independence_wave_recognition_seal_preview.gif`, `previews/independence_wave_recognition_seal_contact.png` |
| ASSET-041 | `independence_wave_dependency_warning/` | `calm, watch, danger` / 3 | `source_frames/*.png`, `processed_frames/*.png` | `sheets/independence_wave_dependency_warning_sheet.png`; `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_sheet.dds` | `independence_wave_dependency_warning_static.png`; `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_static.dds` | `previews/independence_wave_dependency_warning_preview.gif`, `previews/independence_wave_dependency_warning_contact.png` |
| ASSET-042 | `independence_wave_league_charter_activation/` | `rest, drafting, vote, activated` / 4 | `source_frames/*.png`, `processed_frames/*.png` | `sheets/independence_wave_league_charter_activation_sheet.png`; `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_sheet.dds` | `independence_wave_league_charter_activation_static.png`; `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_static.dds` | `previews/independence_wave_league_charter_activation_preview.gif`, `previews/independence_wave_league_charter_activation_contact.png` |
| ASSET-043 | `independence_wave_formable_eligibility_seal/` | `hidden, discovered, eligible, proclaimed` / 4 | `source_frames/*.png`, `processed_frames/*.png` | `sheets/independence_wave_formable_eligibility_seal_sheet.png`; `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_sheet.dds` | `independence_wave_formable_eligibility_seal_static.png`; `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_static.dds` | `previews/independence_wave_formable_eligibility_seal_preview.gif`, `previews/independence_wave_formable_eligibility_seal_contact.png` |

Exact byte sizes and SHA-256 values for every source, processed frame, sheet, static fallback, DDS, GIF, and contact sheet are in `animation_build_report.json` (report SHA-256 `713001ad6d865f45ff949d6687aa4bf5e91e791f2492f00d3e4be5c911a1a52d`).

Proposed sprite names are `GFX_independence_wave_recognition_seal_static` and `_animated`, `GFX_independence_wave_dependency_warning_static` and `_animated`, `GFX_independence_wave_league_charter_activation_static` and `_animated`, and `GFX_independence_wave_formable_eligibility_seal_static` and `_animated`.

Status: complete asset packages; runtime `.gfx`, `.gui`, scripted-GUI predicates, state triggers, and gameplay references remain parent-owned. No advisor, dossier, leader, commander, localisation, gameplay, `.gfx`, or `.gui` files were edited by this tranche.

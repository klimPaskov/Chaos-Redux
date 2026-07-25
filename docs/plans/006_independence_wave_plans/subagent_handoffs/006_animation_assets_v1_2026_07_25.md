# Event 006 animation asset handoff v1

Date: 2026-07-25.

Scope: ASSET-040 recognition seal, ASSET-041 dependency warning, ASSET-042 league charter activation, and ASSET-043 formable eligibility seal only.

## Resolution

The registry's implementation-defined size is resolved as `64x64` pixels per frame for all four small scripted-GUI status-panel assets. The compact status-marker role and the accepted Event 6 small-icon scale support this choice. All four sequences use a centered anchor, transparent corners, 5 FPS metadata, 200 ms per frame, looping review playback, and `play_on_show = no` for parent-controlled state display.

## Delivered packages

| Asset | Package root | Source states / frame count | Sheet | Static fallback |
| --- | --- | --- | --- | --- |
| ASSET-040 recognition seal | `docs/assets/006_independence_wave/animations/independence_wave_recognition_seal/` | `hidden, weak, rising, strong, entrenched` / 5 | `320x64`, `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_sheet.dds` | `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_static.dds` |
| ASSET-041 dependency warning | `docs/assets/006_independence_wave/animations/independence_wave_dependency_warning/` | `calm, watch, danger` / 3 | `192x64`, `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_sheet.dds` | `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_static.dds` |
| ASSET-042 league charter activation | `docs/assets/006_independence_wave/animations/independence_wave_league_charter_activation/` | `rest, drafting, vote, activated` / 4 | `256x64`, `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_sheet.dds` | `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_static.dds` |
| ASSET-043 formable eligibility seal | `docs/assets/006_independence_wave/animations/independence_wave_formable_eligibility_seal/` | `hidden, discovered, eligible, proclaimed` / 4 | `256x64`, `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_sheet.dds` | `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_static.dds` |

Each package contains `source_frames/`, `processed_frames/`, `sheets/`, `previews/`, `notes/source_prompts.md`, `brief.md`, `frame_plan.md`, and the static PNG. Review outputs are `<slug>_preview.gif` and `<slug>_contact.png`. Package-level manifest and sprite notes are `docs/assets/006_independence_wave/animations/manifest.md` and `gfx_handoff.md`.

## Runtime sprite contract

Reserved sprite names are `GFX_independence_wave_recognition_seal_static` and `_animated`, `GFX_independence_wave_dependency_warning_static` and `_animated`, `GFX_independence_wave_league_charter_activation_static` and `_animated`, and `GFX_independence_wave_formable_eligibility_seal_static` and `_animated`.

The proposed `.gfx` snippet, state trigger contracts, and exact runtime texture paths are in `docs/assets/006_independence_wave/animations/gfx_handoff.md`. Parent implementation owns final `.gfx`, `.gui`, scripted-GUI context, visibility predicates, frame-state mapping, and static fallback visibility. No runtime wiring is claimed by this handoff.

## Authorship and motion compliance

Every source frame was independently authored with the built-in ImageGen tool on a flat `#00ff00` chroma-key background. The source prompts and state-specific visual changes are recorded per package in `notes/source_prompts.md` and `frame_plan.md`. Mechanical processing was limited to chroma-key removal, alpha crop, deterministic fit/center normalization, sheet assembly, GIF preview creation, and DDS conversion. The final motion is not a translated, scaled, rotated, recoloured, blurred, opacity-only, or filter-only derivative of one still image.

No advisor, dossier, leader, commander, gameplay, localisation, `.gfx`, or `.gui` files were edited. No runtime GUI consumer is asserted.

## Hashes

`docs/assets/006_independence_wave/animations/animation_build_report.json` is the complete SHA-256 and byte ledger for all source frames, processed frames, sheets, static PNGs, DDS files, GIFs, and contact sheets. Report SHA-256: `713001ad6d865f45ff949d6687aa4bf5e91e791f2492f00d3e4be5c911a1a52d`.

Runtime DDS hashes:

- recognition static `c1871b031ccb2c264c6508e6a02482231020ab81c63cabe4efaa2f0e794c41cc`; sheet `b6572f49f85660e64842a9a4b5cc56a16076a0c12c1d00a875ba8708603fe9fd`.
- dependency static `c52d3a2d17dbd594c9ceac36778cab4eb6dfe525efb26d424211282a53bcd1c4`; sheet `2ed53c2f6ae1a55ebd89f5ede4795885de1b16d5fdd51741d0936fe192162fe6`.
- league static `08f021545bae25aa875a557e54275058bacaf0156ee6617d297d3724643457af`; sheet `fe4d108d4a085f719eaacf57352bb3f85b69bba1fec88360c0c41ef28734858b`.
- formable static `de2f835fb3e60bd6fa906884af572f9a588fc614b1b409d91411c6867ebb6a8a`; sheet `db8ca4e24c7ce343a354b9a768dc5b2533666bf5779ddf4a9f5a9282b4f64271`.

## Validation evidence

- All 16 generated source PNGs exist and have been retained by state name.
- All processed frames are RGBA `64x64`; transparent corner pixels were checked after key removal.
- Sheet PNG dimensions are exactly `320x64`, `192x64`, `256x64`, and `256x64`, matching frame width multiplied by frame count.
- Runtime DDS files exist for all four static fallbacks and all four sheets; decoded dimensions match the expected `64x64` static and sheet sizes.
- Contact sheets show centered anchors and state-specific visual changes; GIF previews are review-only.
- No advisor or dossier assets were created.

## Parent follow-up

Parent should copy or verify the ready-to-copy `.gfx` entries in `animations/gfx_handoff.md`, attach each pair to the planned status panel, map the named gameplay/UI states to the ordered frame sequences, and decide whether `play_on_show` remains `no` after live GUI inspection. Those steps are intentionally outside this asset-only handoff.

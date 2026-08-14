# Event 006 animation asset audit: no safe asset-only gap

Date: 2026-08-15.

Scope: ASSET-040 recognition seal, ASSET-041 dependency warning, ASSET-042 league charter activation, and ASSET-043 formable eligibility seal only.

## Current source status

All four accepted animation rows are already complete as asset packages and no additional accepted asset or scripted-GUI change is safe to implement inside this asset-only scope.

| Requirement | Accepted states and order | Frame package | Runtime DDS | Proposed sprites | Package status |
| --- | --- | --- | --- | --- | --- |
| ASSET-040 recognition seal | `hidden`, `weak`, `rising`, `strong`, `entrenched` | `docs/assets/006_independence_wave/animations/independence_wave_recognition_seal/` | `gfx/interface/006_independence_wave/animations/independence_wave_recognition_seal_static.dds`; `independence_wave_recognition_seal_sheet.dds` | `GFX_independence_wave_recognition_seal_static`; `GFX_independence_wave_recognition_seal_animated` | complete |
| ASSET-041 dependency warning | `calm`, `watch`, `danger` | `docs/assets/006_independence_wave/animations/independence_wave_dependency_warning/` | `gfx/interface/006_independence_wave/animations/independence_wave_dependency_warning_static.dds`; `independence_wave_dependency_warning_sheet.dds` | `GFX_independence_wave_dependency_warning_static`; `GFX_independence_wave_dependency_warning_animated` | complete |
| ASSET-042 league charter activation | `rest`, `drafting`, `vote`, `activated` | `docs/assets/006_independence_wave/animations/independence_wave_league_charter_activation/` | `gfx/interface/006_independence_wave/animations/independence_wave_league_charter_activation_static.dds`; `independence_wave_league_charter_activation_sheet.dds` | `GFX_independence_wave_league_charter_activation_static`; `GFX_independence_wave_league_charter_activation_animated` | complete |
| ASSET-043 formable eligibility seal | `hidden`, `discovered`, `eligible`, `proclaimed` | `docs/assets/006_independence_wave/animations/independence_wave_formable_eligibility_seal/` | `gfx/interface/006_independence_wave/animations/independence_wave_formable_eligibility_seal_static.dds`; `independence_wave_formable_eligibility_seal_sheet.dds` | `GFX_independence_wave_formable_eligibility_seal_static`; `GFX_independence_wave_formable_eligibility_seal_animated` | complete |

Each package retains `brief.md`, `frame_plan.md`, independent ImageGen source frames, processed frames, a horizontal sheet PNG, static fallback PNG, GIF preview, contact sheet, and source notes.

## QA evidence

- The 16 source masters are independent built-in ImageGen outputs on a documented `#00ff00` chroma-key background, with no external source-rights issue.
- Source masters are `1254x1254` RGB PNGs, and every processed frame is `64x64` RGBA with transparent corner pixels and a stable centered anchor.
- Sheet dimensions are `320x64` for ASSET-040, `192x64` for ASSET-041, `256x64` for ASSET-042, and `256x64` for ASSET-043.
- Every sheet column is byte-equivalent to its corresponding processed frame, preserving left-to-right state order without script-created motion.
- Static fallbacks are `64x64` and exist beside all eight runtime sheet and static DDS files.
- All eight runtime DDS files pass the legacy one-level BGRA checks: 128-byte header, exact declared dimensions and byte length, 32-bit RGBA pixel format, BGRA masks, and `DDSCAPS_TEXTURE`.
- `animation_build_report.json` covers 56 files with zero missing files and zero size or SHA-256 mismatches.
- Contact sheets show distinct state-specific authored changes for all four families, and all GIF previews contain the expected number of distinct frames.
- The canonical decision-category contact sheet and individual Vanilla references were inspected from `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/decision_categories/`; the installed `frameAnimatedSpriteType` precedent was inspected in Vanilla `interface/alerts.gfx` and `interface/countryconstructionsview.gfx`, together with the offline graphical-asset, interface, and scripted-GUI wiki pages.

## Parent-owned wiring status

The existing parent-owned `interface/006_independence_wave.gfx` registers the four state strips, four animated siblings, and four static fallbacks against the exact runtime DDS paths.

The existing parent-owned `interface/006_independence_wave.gui` places all four static and animated consumers, and `common/scripted_guis/006_independence_wave_scripted_gui.txt` exposes the four animation visibility predicates and the semantic frame properties.

No `.gfx`, `.gui`, scripted-GUI, gameplay, localisation, portrait, flag, registry, or shared interface file was edited by this audit.

The persistent ledger semantic frame selection is parent-owned and remains the deterministic default; live playback, threshold-transition timing, return-to-current-state behavior, save/load persistence, click-region behavior, and focused runtime rendering remain parent-owned review gates.

The asset briefs and build report describe `5 FPS` (`200 ms` per runtime frame) with parent-controlled `play_on_show = no`, while the currently installed parent `.gfx` entries use `play_on_show = yes` for the explicit Animate toggle.

The GIF previews are review-only and currently encode `180 ms` frame delays; this does not affect the runtime DDS or the `.gfx` FPS metadata, but the preview cadence should be normalized if the parent requires exact review-timing parity.

## No-safe-gap conclusion

There is no concrete accepted asset or scripted-GUI gap that can be safely implemented by this subagent without changing parent-owned wiring or mechanic semantics.

Do not invent another animation family, alter the accepted state order, change the 64x64 frame contract, rewrite the parent `.gfx` or `.gui`, or modify gameplay predicates in this tranche.

ImageGen was used for the retained source frames; no external rights clearance is required for these generated assets.

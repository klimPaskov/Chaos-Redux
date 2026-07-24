# Event 006 Bavaria Friedrich Dollmann ImageGen safety blocker

## Verdict

Friedrich Dollmann has a rights-clear attributed archival male source master and an explicit head-and-shoulders crop, but the mandatory source-locked ImageGen stage cannot currently produce a candidate.

Both the initial identity-preserving HOI4 repaint request and a second prompt that explicitly removed every political emblem from the requested output were blocked by image safety before generation.

The archival crop itself contains source-visible prohibited insignia, so changing only the requested output could not make the input eligible.

No raw ImageGen result, processed 156×210 candidate, independent portrait audit, DDS, sprite wiring, gameplay portrait, advisor icon, dossier, or `_small` derivative was created.

## Evidence

- Source package: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/bavaria_dollmann_source_retry/`.
- Immutable source SHA-256: `15D387707C22E7B73B513961AAE7EB42F40E3E296FF4A68E8AAB6B5DA6E82E12`.
- Explicit crop rectangle: `(300, 120, 500, 450)`.
- Explicit crop SHA-256: `C19C7D634EE585CB32853ED1A0F28BC4D37724AEAC2F58FF2509E20DE6C9B071`.
- Closed trial package: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/bavaria_dollmann_trial_01/`.
- Initial prompt: `prompts/BAY_friedrich_dollmann_trial_01.md`.
- De-symbolized retry prompt: `prompts/BAY_friedrich_dollmann_trial_01_retry_02.md`.
- Stable proposed consumer: `BAY_independence_wave_mountain_commandant`.
- Proposed sprite: `GFX_portrait_BAY_independence_wave_mountain_commandant`.
- Proposed runtime texture: `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.

## Resolution

Do not mask, alter, evade, or bypass the image safety system and do not use the source photograph directly as a runtime portrait.

The Dollmann trial is closed as evidence-only.

IW-009 Bavaria remains outside compile-time content attestation until a different rights-clear archival male source without prohibited source-visible symbols completes the full mandatory chain and the package passes a fresh independent audit.

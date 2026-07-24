# Friedrich Dollmann source-locked commander portrait trial 01

Status: `blocked_imagegen_safety_no_runtime_asset`

## Immutable archival source

- Subject: Friedrich Karl Albert Dollmann (1882–1944), real male Bavarian-born army officer.
- Source package: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/bavaria_dollmann_source_retry/`.
- Source master: `source_masters/BAY_friedrich_dollmann_bundesarchiv_1940_original_533x800.jpg`.
- Source dimensions: `533×800`.
- Source SHA-256: `15D387707C22E7B73B513961AAE7EB42F40E3E296FF4A68E8AAB6B5DA6E82E12`.
- Archive accession: `Bundesarchiv, Bild 101I-052-1435-20`.
- Canonical source page: <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_101I-052-1435-20,_Oberrhein,_Befestigung_am_Isteiner_Klotz.jpg>
- Archived original: <https://upload.wikimedia.org/wikipedia/commons/archive/1/11/20220702180551%21Bundesarchiv_Bild_101I-052-1435-20%2C_Oberrhein%2C_Befestigung_am_Isteiner_Klotz.jpg>
- Date and photographer: `1940`; photographer unknown (`o.Ang.`).
- Rights: Creative Commons Attribution-ShareAlike 3.0 Germany.
- Required attribution: `Bundesarchiv, Bild 101I-052-1435-20 / CC-BY-SA 3.0`.

## Explicit head-and-shoulders crop

- Crop rectangle in source pixels, left/top/right/bottom: `(300, 120, 500, 450)`.
- Crop: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/bavaria_dollmann_source_retry/source_crops/BAY_friedrich_dollmann_head_shoulders_300_120_500_450.png`.
- Crop dimensions: `200×330`.
- Crop SHA-256: `C19C7D634EE585CB32853ED1A0F28BC4D37724AEAC2F58FF2509E20DE6C9B071`.
- The crop is source-pixel evidence only and is not a runtime portrait.

## Source-locked repaint

- Prompt: `prompts/BAY_friedrich_dollmann_trial_01.md`.
- Retry prompt after the first request was blocked by the image safety system: `prompts/BAY_friedrich_dollmann_trial_01_retry_02.md`.
- The retry kept the exact identity crop but required every political emblem to be removed and replaced by plain unmarked fabric or non-symbolic metal.
- ImageGen safety result: both the original request and the de-symbolized retry were blocked before generation because the identity input itself contains prohibited source-visible insignia.
- Safety boundary: do not mask, alter, evade, or bypass the image safety system. No generated output was returned or retained.
- Identity input: the exact crop above.
- Style-only references: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/ger_erwin_von_witzleben.png` and `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/ger_erich_von_manstein.png`.
- Raw ImageGen result: none.
- Deterministic `156×210` candidate: none.
- Independent provenance/likeness/style audit: not eligible because no candidate exists.
- DDS conversion and runtime wiring: forbidden. This trial is closed as a documented safety blocker.

## Consumer and role boundary

The only proposed Event 6 consumer would have been the existing stable `BAY_independence_wave_mountain_commandant` token through full-size civilian-large and army-large portrait slots.
Friedrich Dollmann is used as Bavaria's emergency passes-and-depots commandant; this is a territorial-command abstraction, not a claim of historical Gebirgstruppe service.
The source is a 1940 uniform portrait, so its date and source-visible insignia remain explicit provenance caveats rather than invented 1936 Bavarian route history.
No advisor, dossier, `_small`, operative, or unrelated consumer is authorized, and this blocked trial supplies no runtime asset.

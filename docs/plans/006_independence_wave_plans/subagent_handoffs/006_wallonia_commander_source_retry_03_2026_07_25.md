# Subagent handoff: Wallonia commander source retry 03

## Outcome

Selected a distinct grounded real-person candidate for IW-006: Belgian Lieutenant-General Louis Hubert baron Ruquoy (period source spelling Louis Rucquoy), born 3 November 1861 at Frasnes-lez-Buissenal in Hainaut and alive throughout 1936. He was Chief of the Belgian General Staff from 6 January 1917, commanded the 5th Army Division, and later commanded Belgian occupation forces in the Rhineland. He was pensioned in 1927, so the intended 1936 framing is a senior veteran or council commander rather than an active staff chief.

## Selected source and exact crop

- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_commander_retry_03/source_masters/ruquoy_rol_1923_group.jpg` - unchanged 8419 x 6051 Agence Rol/BnF Gallica group photograph dated 12 March 1923, SHA-256 `bf11028c9b7da593062f4eb8730417c760748d10a5c6de8493cbbb8bc667c7ac`.
- Archive: Bibliotheque nationale de France, Gallica item `btv1b531010537`; source URL and Commons page are recorded in `manifest.json` and `source_clearance.md`.
- Rights: public domain as marked by the Commons Gallica record (PD France, PD-1996, PD US expired). Attribution: `Agence Rol / Bibliotheque nationale de France, Gallica, item btv1b531010537.`
- The full caption identifies the center figure as general Rucquoy between general Henri Maglinse and Defence Minister Albert Devèze. The archive title/default caption foregrounds Maglinse; this caption-order uncertainty is explicitly recorded.
- `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_commander_retry_03/source_crops/ruquoy_rol_1923_head_shoulders.png` - exact 1750 x 1900 source crop, SHA-256 `4aaf3591d040a9e6423803715404030148a2fcb0cc38801118bce9c398b6ca6a`, rectangle `[3300,1000,5050,2900]`.
- `source_crops/ruquoy_rol_1923_head_shoulders.json` records Pillow 11.1.0 equality proof with `decoded_pixels_equal: true` and RGBA digest `ed034beac18575bf34e9d4f3801698846256e50caa89106e2f36eb17910be58d`.

## Corroborating sources

- `source_masters/ruquoy_lpdf_118_1917.jpg` and exact crop - period frontal portrait, CC BY-SA 3.0 Garitan scan, retained as secondary corroboration because of low-resolution halftone quality and unknown original photographer.
- `source_masters/ruquoy_miroir_215_1917.jpg` and exact crop - larger circa-1917 *Le Miroir* face and uniform view, retained as geometry corroboration only because the Commons page carries a disputed-copyright-information warning.
- `contact_sheets/ruquoy_commander_source_comparison.png` compares the BnF primary with both corroborating sources; `contact_sheets/ruquoy_rol_grid.png` records coordinate review of the selected source.

## Files owned and created

The package's `manifest.json`, `manifest.md`, `source_clearance.md`, `gfx_handoff.md`, `ownership_audit.md`, `source_hashes.sha256`, source masters, exact crops, research snapshots, contact sheets, and rejected/redundant evidence are all under the owned retry directory. No gameplay, GFX, character, localisation, ImageGen, or DDS file was changed.

## Ownership audit

Exact and variant forms (`Louis Hubert Ruquoy`, `Louis Rucquoy`, `Louis Ruquoy`, `Ruquoy`, `Rucquoy`) were searched in current Chaos Redux, vanilla HOI4, Kaiserreich `1521695605`, and references `2265420196` and `1458561226` across `common/characters`, `history/countries`, `gfx/leaders`, `interface`, and `localisation`. Result: NO_MATCH; no transfer guard is required.

## Gate state and risks

Status is `needs_user_review`. Source rights, attribution, Walloon birthplace, alive-in-1936 test, commander history, high-resolution face geometry, and exact crop pass source-clearance review. Independent likeness/style/provenance audit is pending. No ImageGen repaint, 156 x 210 candidate, DDS, `.gfx`, gameplay, localisation, or runtime wiring was created.

Risks: the selected image is a group photograph, and the identity of the center subject relies on the full caption order while the archive page title foregrounds Maglinse. This is recorded for independent review. Ruquoy was retired by 1936, so the parent should use a veteran/council framing rather than claim active 1936 General Staff service.

## Parent next action

If the candidate is accepted, the parent owns independent review, any source-locked identity-preserving ImageGen repaint, deterministic full `156 x 210` commander processing, DDS conversion, `.gfx` registration, character wiring, and final in-game validation. The source crop must not be wired directly as a runtime commander texture.

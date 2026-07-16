# Event 006 Mediterranean gameplay-assets handoff — 2026-07-16

## Outcome

The bounded COR/ARX/ASX gameplay-art package is complete and wired: eight independently composed focus icons with shine registrations, eight independently composed decision icons, exactly eight shared Mediterranean lifecycle ideas, and `GFX_report_event_006_mediterranean_island_incidents`.

The selected art uses official `$imagegen` sources, package-local deterministic processing, exact HOI4 canvases, transparent 32-bit DDS output, a dedicated regional `.gfx` file, prompt/provenance records, hashes, row-level coverage evidence, and compact target-size/decoded-DDS review sheets.

## Files changed

- Added `interface/006_independence_wave_mediterranean_assets.gfx` with 33 registrations:
  - eight focus base sprites
  - eight focus `_shine` sprites
  - eight decision sprites
  - eight idea sprites
  - one report-event sprite
- Added eight DDS files under `gfx/interface/goals/006_independence_wave/mediterranean/`.
- Added eight DDS files under `gfx/interface/decisions/006_independence_wave/mediterranean/`.
- Added eight DDS files under `gfx/interface/ideas/006_independence_wave/mediterranean/`.
- Added `gfx/event_pictures/006_independence_wave/mediterranean/report_event_006_mediterranean_island_incidents.dds`.
- Added the retained source, processed-preview, prompt, manifest, validation, crosswalk, contact-sheet, hash, and regeneration package under `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/`.
- Added this handoff.

No gameplay, localisation, portrait, flag, or spreadsheet file was edited by this subagent.

## Live consumer coverage

| Family | Accepted rows | Live consumer evidence |
|---|---:|---|
| Focus | 8 base + 8 shine | all eight exact tokens occur in `common/national_focus/006_independence_wave_focus.txt`; occurrence counts are 2, 1, 2, 2, 2, 3, 1, and 3 respectively |
| Decision | 8 | all eight exact tokens occur in `common/decisions/006_independence_wave_mediterranean_decisions.txt`; occurrence counts are 5, 3, 6, 2, 6, 3, 1, and 3 |
| Idea | 8 | all eight exact `picture` tokens occur in `common/ideas/006_independence_wave_mediterranean_ideas.txt`; occurrence counts are 3, 3, 3, 1, 2, 2, 3, and 2 |
| Report | 1 | the exact report sprite is consumed by all seven events in `events/006_independence_wave_mediterranean.txt` |

The exact requirement-to-source-to-runtime-to-consumer mapping is recorded in `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/notes/requirement_to_runtime_crosswalk.md`. The machine-readable occurrence and registration audit is in `notes/runtime_validation.json` beside it.

## Ownership boundary

The eighth shared package concept is the maritime-congress bridge pair:

- `GFX_goal_independence_wave_form05_maritime_congress`
- `GFX_decision_independence_wave_form05_maritime_congress`

These two assets are owned here because they are consumed by the COR, ARX, and ASX package routes. Dedicated FORM05 charter/delegation, shipping, defence, customs, capital, proclamation, post-formation lifecycle-idea, emblem/flag, and charter-congress report surfaces are outside this package and were neither generated nor registered here.

No advisor assets were created or referenced by the registration file.

## Asset-specific validation evidence

- Count audit: 8 focus, 8 decision, 8 idea, 1 report; 25 selected source PNGs, 25 processed PNGs, and 25 runtime DDS files.
- Canvas audit: focus 94×86, decision 32×32, idea 64×64, report 210×176.
- Transparency audit: every processed/runtime asset has alpha range 0–255 and four transparent canvas corners; visible chroma residue count is zero.
- DDS audit: every file has the full legacy 124-byte header, 32-bit BGRA masks, exact pitch and byte length, texture caps, and alpha. Decoding every DDS produced pixels exactly equal to its processed PNG.
- Distinctness audit: no byte-identical source or processed asset exists within any family. Focus, decision, and idea concepts use separate official generation outputs and target-specific visual grammar.
- Registration audit: each accepted base sprite, focus shine sprite, texture path, and consumer token exists exactly once where registration uniqueness is required.
- Visual audit: both producer and parent inspected the compact target-size sheet; the parent approved the focus/decision/idea families as distinct, legible, and coherent and the report as correctly readable at 210×176. The processed-PNG and decoded-DDS contact sheets have the same SHA-256 because conversion is pixel-exact.
- Corrective selection: the first maritime-congress focus candidate contained an unintended mainland map silhouette. A targeted official ImageGen edit replaced it with an unmarked blue conference table and three neutral delegation tokens. The rejected path, corrective prompt, reason, and selected source are recorded in the prompt ledger.

Primary review artifacts:

- `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/contact_sheets/006_mediterranean_gameplay_contact_sheet.png`
- `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/contact_sheets/006_mediterranean_dds_decode_contact_sheet.png`
- `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/notes/runtime_validation.json`
- `docs/assets/006_independence_wave/mediterranean_gameplay_assets_2026_07_16/hashes.sha256`

## Skills used

- `chaos-redux-event-assets` for family separation, canonical sizes, processing, manifest, contact sheets, DDS output, and handoff structure
- `chaos-redux-subagents` for bounded ownership and parent handoff requirements
- `imagegen` for all original source artwork and the corrective maritime-congress edit

No reusable skill change was needed; the existing asset workflow covered the package.

## Simplifications, omissions, and blockers

None. Every accepted row is generated, processed, converted, registered, consumed, documented, hashed, and reviewed. The explicit FORM05 boundary above is task ownership, not an omission from the accepted package. No remaining asset-wiring blocker is known.

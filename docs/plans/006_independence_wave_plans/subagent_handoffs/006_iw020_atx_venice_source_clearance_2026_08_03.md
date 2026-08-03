# IW-020 ATX Venice source-only visual handoff — 2026-08-03

## Outcome

The bounded source review found one attributable male, period-compatible Venetian civic candidate and two authentic Venetian maritime flag references. Giuseppe Volpi is retained as a `needs_user_review` source-only candidate for a Saint Mark civic or Venetian port-institution role. The flag evidence is historical object photography and design geometry only; it does not authorize a doge, admiral, unchanged 1659 standard, or automatic replacement of the existing ATX ImageGen flag.

## Candidate and role gate

Giuseppe Volpi (19 November 1877–16 November 1947) was born in Venice and served as First Procurator of Saint Mark from 1927 to 1947. He also chaired the Biennale di Venezia (1930–1943), founded SADE, promoted Porto Marghera, and remained a major Adriatic industrial and civic actor. The Italian-language biographical record identifies the First Procurator term and his Venice/Adriatic institutional work: https://it.wikipedia.org/wiki/Giuseppe_Volpi. The office itself is described as a senior Venetian civic magistracy responsible for Saint Mark's assets and public buildings, with its continuity confirmed by the 1931 Italian royal decree: https://en.wikipedia.org/wiki/Procurators_of_Saint_Mark.

The immutable identity source is the Library of Congress National Photo Company Collection glass negative “Giuseppe Volpi, head of Debt Com., 11/2/25” (2 November 1925), LOC item `2016841107`, control `npcc.14843`: https://www.loc.gov/pictures/item/2016841107/ and https://hdl.loc.gov/loc.pnp/npcc.14843. The LOC rights statement is “No known restrictions on publication.” Wikimedia Commons mirrors the high-resolution file as Public domain: https://commons.wikimedia.org/wiki/File:Giuseppe_Volpi,_head_of_Debt_Com.,_11-2-25_LCCN2016841107.jpg.

The source shows an adult male in a 1925 suit, tie, and top hat with clear facial geometry. The exact crop keeps the hat, eyes, nose, moustache, beard, jaw, collar, tie, and upper shoulders without retouching, repainting, recolouring, or style transfer. It remains a source placeholder candidate and is not an approved runtime portrait.

## Delivered source package

- `docs/assets/006_independence_wave/iw020_atx_venice_source_research_2026_08_03/manifest.md` records provenance, rights, role fit, uncertainty, and flag boundaries.
- `source_masters/giuseppe_volpi_debt_commission_1925_lccn2016841107_original.jpg` is the retained 5554x4432 original-format grayscale source.
- `source_crops/portrait_atx_giuseppe_volpi_head_shoulders.png` is the exact 2750x3700 Pillow crop from `(1385,400)-(4135,4100)`.
- `source_metadata/portrait_atx_giuseppe_volpi_head_shoulders.json` proves decoded-pixel equality and records the crop tool, master/output dimensions, and hashes.
- `processed_preview/portrait_atx_giuseppe_volpi_source_placeholder_156x210.png` is a deterministic 156x210 resize for visual review only.
- `references/venice_naval_standard_saint_barbara_1659_museo_correr.jpg` and `references/venice_naval_standard_doge_contarini_1659_museo_correr.jpg` are authentic Museo Correr 1659 textile references with the artwork marked `PD-old-100`; the photographs are by Didier Descouens under CC BY-SA 4.0.
- `review/iw020_atx_venice_source_contact_sheet.png` compares the source chain, museum references, and the existing ATX generated reconstruction.
- `source_hashes.sha256` records SHA-256 digests for every retained source and review artifact.

## Parent-owned decisions and next steps

- Keep Volpi at `needs_user_review` until the parent assigns a stable ATX civic character key and confirms the selected route can represent a fascist-era industrialist as a civic or port institution rather than as a restored doge or military commander.
- If accepted, the parent owns final character wiring, source-placeholder DDS conversion, `.gfx` registration, localisation, independent likeness/framing/provenance audit, and runtime validation. No runtime basename has been assigned here; use `portrait_atx_<character_key>` after the character key is fixed.
- If a styled HOI4 replacement is later requested, hand the unchanged crop to `chaosx_portrait_creator`; do not use ImageGen or ComfyUI during this source-only clearance.
- Treat the 1659 flag objects as geometry and provenance evidence for a historical Venetian red/gold maritime symbol family. The existing ATX flat red-field Lion reconstruction remains a separate generated package, and any final flag decision must state whether it is a civic heraldic reconstruction or an attested object rather than silently calling it a 1936 flag.

## Scope confirmation

No `.gfx`, event, focus, idea, decision, localisation, character, country, history, spreadsheet, advisor, commander-small, operative, or gameplay files were changed. No final DDS or runtime asset was created. No unrelated repository edits were reverted.

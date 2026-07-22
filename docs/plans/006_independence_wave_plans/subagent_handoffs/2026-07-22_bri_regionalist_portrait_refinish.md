# BRI regionalist portrait refinish handoff

Date: 2026-07-22  
Asset scope: Event 006 Brittany civic leader Régis de l'Estourbeillon only  
Producer: generated-event-art asset subagent  
Status: `needs_user_review`

## Files created (owned scope)

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_candidate_v1.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/processed_png/leader_bri_regionalist_regis_de_l_estourbeillon.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/contact_sheets/bri_regionalist_identity_review.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/prompt.md`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/gfx_handoff.md`

No existing files were modified. No gameplay, localisation, spreadsheet,
country, character, `.gfx`, runtime texture, or DDS file was edited.

## Source and identity contract

- Grounded identity: Régis de l'Estourbeillon, male Breton regionalist civic
  figure; source mode remains attributed John Wickens 1904 photograph.
- Source authority: the newly committed
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/bri_regionalist_retry/`
  package, primary source master SHA-256
  `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D`.
- ImageGen was used only as an edit/repaint of that exact sourced person. The
  face, moustache, gaze/expression, head angle, apparent age, hat, and visible
  period costume were held as invariants. Canonical leader references were used
  only for vanilla HOI4 finish, pale quiet backdrop, and framing.
- The 1898 Maurice Dulac illustration was not used. No generated identity,
  generic, female, advisor, operative, flag, `_small`, dossier, localisation,
  or gameplay asset was made.

## Selected output and hashes

- selected raw master: `leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png`, `1024x1536`, RGB, SHA-256 `CAE505FFA05FBEE59360FAB7993062078482F01142F83F061A73193EB7953FF7`
- retained candidate v1: `leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_candidate_v1.png`, `1080x1456`, RGB, SHA-256 `8BE51C6A25E14BB93CE1996483F0E76CAB76B708118723091C998B49E454418B`
- processed preview: `leader_bri_regionalist_regis_de_l_estourbeillon.png`, `156x210`, opaque RGB, SHA-256 `BDEDCCB06A25807C70A774871607AE72DA4F9A51B711E88E45F1E389A99500C8`
- selected crop: `(0,79,1024,1457)` from v2 master, then Lanczos resize to `156x210`
- review sheet: `bri_regionalist_identity_review.png`, includes source crop, both ImageGen candidates, processed output, and vanilla Stauning/Mannerheim style references

## Runtime handoff

Preserve the existing sprite
`GFX_portrait_BRI_independence_wave_civic_commission` in
`interface/006_independence_wave_brittany_portraits.gfx` and its deferred
texture path:

`gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds`

The parent owns the final identity review, repository-standard DDS conversion,
runtime placement, and any live validation. No duplicate sprite declaration is
needed.

## Validation and skipped work

- visually inspected the unchanged source and canonical
  `vanilla_reference/portraits/leaders/contact_sheet.png`
- visually inspected both ImageGen outputs, the selected 156x210 portrait, and
  the review contact sheet
- confirmed source and generated masters are RGB and processed output is exactly
  `156x210` opaque RGB
- retained exact source, generated, processed, and review-sheet hashes in the
  manifest
- DDS conversion intentionally skipped because the parent explicitly reserved
  DDS/runtime conversion for the parent agent
- `.gfx`, gameplay, localisation, and spreadsheet wiring intentionally skipped

## Remaining risk / fail-closed condition

ImageGen can alter fine facial details even when the macro likeness is held.
The selected output currently reads as the same photographed man and retains
the source-supported hat and costume, but the parent must reject it if a direct
comparison judges any material identity drift. If rejected, leave the BRI civic
portrait slot blocked and commission a new sourced treatment; do not substitute
the Dulac illustration or an invented/generic person.


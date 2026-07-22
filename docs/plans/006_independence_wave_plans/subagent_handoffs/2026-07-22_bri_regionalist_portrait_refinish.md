# BRI regionalist portrait refinish handoff

Date: 2026-07-22  
Asset scope: Event 006 Brittany civic leader Régis de l'Estourbeillon only  
Producer: generated-event-art asset subagent  
Status: `needs_user_review` (revision 3 current candidate)

## Files created (owned scope)

- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_candidate_v1.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_john_wickens_1904_source_master.jpg`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/source_png/leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master_v3.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/processed_png/leader_bri_regionalist_regis_de_l_estourbeillon.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/processed_png/leader_bri_regionalist_regis_de_l_estourbeillon_v3.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/contact_sheets/bri_regionalist_identity_review.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/contact_sheets/bri_regionalist_v3_comparison.png`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/manifest.md`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/prompt.md`
- `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/bri_regionalist/gfx_handoff.md`

Only the existing manifest, prompt, hash ledger, and handoff inside this owned
package were updated. No gameplay, localisation, spreadsheet, country,
character, `.gfx`, runtime texture, or DDS file was edited.

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
- Revision 3 used the unchanged source photograph as the identity-bearing input
  and skill-local male vanilla HOI4 leader portraits (`den_thorvald_stauning`,
  `ire_eamon_de_valera`, `afg_mohammed_zahir_shah`) as style-only inputs. It
  shifts the presentation to muted full color and restrained HOI4 paint rather
  than sepia/photographic treatment.

## Selected output and hashes

- selected raw master: `leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master.png`, `1024x1536`, RGB, SHA-256 `CAE505FFA05FBEE59360FAB7993062078482F01142F83F061A73193EB7953FF7`
- retained candidate v1: `leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_candidate_v1.png`, `1080x1456`, RGB, SHA-256 `8BE51C6A25E14BB93CE1996483F0E76CAB76B708118723091C998B49E454418B`
- processed preview: `leader_bri_regionalist_regis_de_l_estourbeillon.png`, `156x210`, opaque RGB, SHA-256 `BDEDCCB06A25807C70A774871607AE72DA4F9A51B711E88E45F1E389A99500C8`
- selected crop: `(0,79,1024,1457)` from v2 master, then Lanczos resize to `156x210`
- review sheet: `bri_regionalist_identity_review.png`, includes source crop, both ImageGen candidates, processed output, and vanilla Stauning/Mannerheim style references

## Revision 3 output and hashes

- unchanged source master: `leader_bri_regionalist_regis_de_l_estourbeillon_john_wickens_1904_source_master.jpg`, `1145x1707` RGB JPEG, SHA-256 `C310F1D916A578FD4E3C5B9ADAC4D4737DA6D841D02D5EA59F66C4589AE9230D`
- v3 raw master: `leader_bri_regionalist_regis_de_l_estourbeillon_imagegen_master_v3.png`, `1082x1454` RGB PNG, SHA-256 `660E954102CC6DF902792E84D0B0F97F178351476485A008362E64A1610E8120`
- v3 processed preview: `leader_bri_regionalist_regis_de_l_estourbeillon_v3.png`, `156x210` opaque RGB PNG, SHA-256 `5426E39BC1622E7ECD32A41CC0A1C05D6596446A40FA0B7BA2047EF350BBAE80`
- v3 crop: `(1,0,1081,1454)` from the raw master, then Lanczos resize to `156x210`
- v3 comparison: `bri_regionalist_v3_comparison.png` includes unchanged source crop, v2 processed, v3 processed/master, and three male vanilla leader references

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

- visually inspected the unchanged source, v2, v3, the skill-local male vanilla
  leader contact sheet, and the canonical leader family
- visually inspected the v3 ImageGen output, v3 156x210 portrait, and the v3
  source/v2/v3/reference comparison sheet
- confirmed source and generated masters are RGB and both processed outputs are
  exactly `156x210` opaque RGB
- retained exact source, v2, v3, processed, and comparison-sheet hashes in the
  manifest and `sha256sums.txt`
- DDS conversion intentionally skipped because the parent explicitly reserved
  DDS/runtime conversion for the parent agent
- `.gfx`, gameplay, localisation, and spreadsheet wiring intentionally skipped

## Remaining risk / fail-closed condition

ImageGen can alter fine facial details even when the macro likeness is held.
Revision 3 now reads as a muted full-color painted HOI4 portrait and retains
the source-supported hat, moustache, gaze, face, pose, and costume, but the
parent must reject it if a direct comparison judges any material identity drift
or invented visible detail. If rejected, leave the BRI civic portrait slot
blocked and commission a new sourced treatment; do not substitute the Dulac
illustration or an invented/generic person.
